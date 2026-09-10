#!/usr/bin/env python3
"""
Power BI source auditor.

Answers one question for a pile of inherited reports: which of these are
actually connected to something, and which are carrying frozen data that will
never refresh no matter how often you press the button?

It opens each .pbix, pulls out the Power Query M, splits it into queries, and
classifies every query by the function it uses to reach its data. Queries built
with "Enter Data" or a hardcoded table literal are flagged STATIC, which means
the numbers are a snapshot somebody pasted in on the day they built it.

Where a query is STATIC it also decodes the embedded payload, so you get the
row and column count and a sample of the frozen rows. That is usually enough to
work out roughly when the snapshot was taken.

Usage
-----
    python pbi_source_audit.py --input "ISP Velocity Changes.pbix"
    python pbi_source_audit.py --input ./reports --markdown audit.md
    python pbi_source_audit.py --input pasted_query.m

--input takes a .pbix file, a folder to scan for .pbix files, or a text file
containing M code copied out of the Power Query Advanced Editor. The last form
is the fallback for when you can see a report in the Service but cannot
download it.

Standard library only. Nothing to install. Read only, it never writes to the
report file.

SECURITY: file paths, hostnames, URLs and credentials in connection strings are
abbreviated by default so the output is safe to paste into a ticket or an email.
Pass --show-paths if you need the full values and the output is staying
internal.
"""

import argparse
import base64
import io
import json
import re
import sys
import zipfile
import zlib
from pathlib import Path

# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------
# kind is what determines the verdict:
#   static  - data is frozen inside the file. Refresh does nothing.
#   file    - reads a file. Refreshable, but only from wherever that file sits.
#   live    - a database or service connection.
#   web     - an http endpoint or feed.
#   derived - builds on other queries in the same file, no source of its own.

CONNECTORS = [
    # (kind, label, regex)
    ("static", "Enter Data (pasted snapshot)",
     re.compile(r"Table\.FromRows\s*\(\s*Json\.Document\s*\(\s*Binary\.Decompress")),
    ("static", "hardcoded table literal", re.compile(r"#table\s*\(")),

    ("file", "Excel workbook", re.compile(r"Excel\.Workbook\s*\(")),
    ("file", "CSV file", re.compile(r"Csv\.Document\s*\(")),
    ("file", "XML file", re.compile(r"Xml\.(?:Tables|Document)\s*\(")),
    ("file", "Access database", re.compile(r"Access\.Database\s*\(")),
    ("file", "folder of files", re.compile(r"Folder\.(?:Files|Contents)\s*\(")),
    ("file", "SharePoint", re.compile(r"SharePoint\.(?:Files|Contents|Tables)\s*\(")),

    ("live", "SQL Server", re.compile(r"Sql\.Databases?\s*\(")),
    ("live", "Oracle", re.compile(r"Oracle\.Database\s*\(")),
    ("live", "Databricks", re.compile(r"Databricks(?:MultiCloud)?\.\w+\s*\(")),
    ("live", "Snowflake", re.compile(r"Snowflake\.Databases\s*\(")),
    ("live", "PostgreSQL", re.compile(r"PostgreSQL\.Database\s*\(")),
    ("live", "MySQL", re.compile(r"MySQL\.Database\s*\(")),
    ("live", "Db2", re.compile(r"Db2\.Database\s*\(")),
    ("live", "Teradata", re.compile(r"Teradata\.Database\s*\(")),
    ("live", "Analysis Services", re.compile(r"AnalysisServices\.Databases?\s*\(")),
    ("live", "Azure storage", re.compile(r"AzureStorage\.\w+\s*\(")),
    ("live", "ODBC", re.compile(r"Odbc\.(?:DataSource|Query)\s*\(")),
    ("live", "OLE DB", re.compile(r"OleDb\.DataSource\s*\(")),
    ("live", "Salesforce", re.compile(r"Salesforce\.\w+\s*\(")),
    ("live", "Dataverse / CDS", re.compile(r"(?:CommonDataService|PowerPlatform)\.\w+\s*\(")),
    ("live", "Power BI dataflow", re.compile(r"PowerBI\.Dataflows\s*\(")),

    ("web", "OData feed", re.compile(r"OData\.Feed\s*\(")),
    ("web", "web request", re.compile(r"Web\.(?:Contents|Page|BrowserContents)\s*\(")),
]

# A query that only chains off other queries has no source of its own.
DERIVED_HINT = re.compile(r"=\s*(?:#\"[^\"]+\"|[A-Za-z_]\w*)\s*(?:,|\{|\[|\n)")

NATIVE_QUERY = re.compile(r"Value\.NativeQuery\s*\(")

# Any quoted path or URL, for reporting where a file source points.
PATH_LITERAL = re.compile(r"\"((?:[A-Za-z]:\\|\\\\|https?://)[^\"]{2,400})\"")

# Anything that looks like a credential sitting in the M. Never printed.
SECRET_HINT = re.compile(
    r"(?i)\b(?:password|pwd|secret|apikey|api_key|token|sas|accountkey)\s*=", )


def shorten(value, show_paths):
    """Abbreviate a path or URL so it can be pasted somewhere public."""
    if show_paths:
        return value
    if value.startswith(("http://", "https://")):
        rest = value.split("://", 1)[1]
        host = rest.split("/", 1)[0]
        tail = rest.rsplit("/", 1)[-1] if "/" in rest else ""
        host = host.split(".")[0][:3] + "..." + (host.rsplit(".", 1)[-1])
        return f"https://{host}/.../{tail}"
    if value.startswith("\\\\"):
        tail = value.rsplit("\\", 1)[-1]
        return f"\\\\<server>\\...\\{tail}"
    if re.match(r"^[A-Za-z]:\\", value):
        tail = value.rsplit("\\", 1)[-1]
        return f"{value[:3]}...\\{tail}"
    return value


# ---------------------------------------------------------------------------
# Enter Data payloads
# ---------------------------------------------------------------------------

B64_BLOB = re.compile(
    r"Binary\.FromText\s*\(\s*\"([A-Za-z0-9+/=\s]{16,})\"\s*,\s*BinaryEncoding\.Base64\s*\)")


def decode_enter_data(m_text):
    """Enter Data stores its rows as deflate compressed JSON in base64.

    Returns (rows, columns, sample) or None if it will not decode. A failure
    here is not important, the STATIC verdict already stands on the pattern
    match alone.
    """
    match = B64_BLOB.search(m_text)
    if not match:
        return None
    blob = re.sub(r"\s+", "", match.group(1))
    try:
        raw = base64.b64decode(blob)
    except Exception:
        return None

    payload = None
    for wbits in (-15, 15, 47):          # raw deflate, zlib, gzip
        try:
            payload = zlib.decompress(raw, wbits)
            break
        except Exception:
            continue
    if payload is None:
        return None

    try:
        data = json.loads(payload.decode("utf-8", errors="replace"))
    except Exception:
        return None

    if isinstance(data, dict):
        for value in data.values():
            if isinstance(value, list):
                data = value
                break
    if not isinstance(data, list):
        return None

    rows = len(data)
    cols = max((len(r) for r in data if isinstance(r, list)), default=0)
    return rows, cols, data[:3]


# ---------------------------------------------------------------------------
# Splitting Section1.m into queries
# ---------------------------------------------------------------------------

QUERY_START = re.compile(
    r"^[ \t]*(?:\[[^\]]*\][ \t]*)?shared[ \t]+(#\"(?:[^\"]|\"\")*\"|[A-Za-z_][\w.]*)[ \t]*=",
    re.MULTILINE)


def split_queries(m_text):
    """Return [(name, body), ...] for every `shared X = ...;` in a section.

    Naive on purpose. An M string literal containing a line that begins with
    `shared` would confuse it, which has not happened yet and would only ever
    split one query in two.
    """
    starts = list(QUERY_START.finditer(m_text))
    if not starts:
        return [("(whole file)", m_text)]

    queries = []
    for i, match in enumerate(starts):
        end = starts[i + 1].start() if i + 1 < len(starts) else len(m_text)
        name = match.group(1)
        if name.startswith('#"'):
            name = name[2:-1].replace('""', '"')
        queries.append((name, m_text[match.start():end]))
    return queries


def classify(name, body, show_paths):
    """Work out where one query gets its data."""
    hits = [(kind, label) for kind, label, rx in CONNECTORS if rx.search(body)]

    # A hardcoded literal alongside a real connector is usually a lookup table
    # bolted onto a live query, so it should not drag the whole query to static.
    if len(hits) > 1:
        real = [h for h in hits if h[1] != "hardcoded table literal"]
        if real:
            hits = real

    detail = {"name": name, "sources": hits, "paths": [], "notes": []}

    for path in PATH_LITERAL.findall(body):
        short = shorten(path, show_paths)
        if short not in detail["paths"]:
            detail["paths"].append(short)

    if NATIVE_QUERY.search(body):
        detail["notes"].append("uses Value.NativeQuery, so there is SQL to harvest")
    if SECRET_HINT.search(body):
        detail["notes"].append(
            "WARNING: something matching a password or key appears in the M. "
            "Do not share this file. Value not printed here")

    if any(k == "static" for k, _ in hits):
        detail["kind"] = "static"
        payload = decode_enter_data(body)
        if payload:
            rows, cols, sample = payload
            detail["frozen"] = {"rows": rows, "cols": cols, "sample": sample}
    elif any(k == "live" for k, _ in hits):
        detail["kind"] = "live"
    elif any(k == "web" for k, _ in hits):
        detail["kind"] = "web"
    elif any(k == "file" for k, _ in hits):
        detail["kind"] = "file"
    elif DERIVED_HINT.search(body):
        detail["kind"] = "derived"
    else:
        detail["kind"] = "unknown"

    return detail


# ---------------------------------------------------------------------------
# Reading the file
# ---------------------------------------------------------------------------

def mashup_to_m(raw):
    """DataMashup is a zip wrapped in a binary header. Seek to the signature."""
    sig = raw.find(b"PK\x03\x04")
    if sig < 0:
        return None
    try:
        with zipfile.ZipFile(io.BytesIO(raw[sig:])) as z:
            parts = [n for n in z.namelist() if n.lower().endswith(".m")]
            if not parts:
                return None
            return "\n".join(
                z.read(n).decode("utf-8", errors="replace") for n in parts)
    except Exception:
        return None


def read_pbix(path):
    """Return (m_text, connection_count, warnings)."""
    warnings = []
    try:
        with zipfile.ZipFile(path) as z:
            names = z.namelist()

            m_text = None
            if "DataMashup" in names:
                m_text = mashup_to_m(z.read("DataMashup"))
            if m_text is None:
                for name in names:
                    if name.endswith("DataMashup"):
                        m_text = mashup_to_m(z.read(name))
                        if m_text:
                            break

            connections = None
            if "Connections" in names:
                try:
                    conn = json.loads(
                        z.read("Connections").decode("utf-8-sig", errors="replace"))
                    connections = len(conn.get("Connections", []) or [])
                except Exception:
                    connections = None

            if m_text is None:
                if any("SemanticModel" in n or n.endswith(".tmdl") for n in names):
                    warnings.append(
                        "no DataMashup part. This looks like a live connection or a "
                        "thin report pointing at a published semantic model, so the "
                        "queries live in the model and not in this file")
                else:
                    warnings.append(
                        "no Power Query found. If the report is a live connection to "
                        "a semantic model or Analysis Services, audit the model instead")
    except zipfile.BadZipFile:
        return None, None, ["not a readable .pbix (a PBIX is a zip; this is not)"]

    return m_text, connections, warnings


def audit_source(path, show_paths):
    """Audit one .pbix or one file of raw M."""
    result = {"file": path.name, "queries": [], "warnings": [], "connections": None}

    if path.suffix.lower() == ".pbix":
        m_text, connections, warnings = read_pbix(path)
        result["connections"] = connections
        result["warnings"].extend(warnings)
    else:
        m_text = path.read_text(encoding="utf-8", errors="replace")

    if not m_text:
        return result

    for name, body in split_queries(m_text):
        result["queries"].append(classify(name, body, show_paths))
    return result


VERDICTS = {
    "static": "NO LIVE SOURCE. Every query holds a pasted snapshot",
    "file": "refreshable, but only from files on a drive or SharePoint",
    "live": "connected to a database or service",
    "web": "connected to a web endpoint",
    "mixed": "part connected, part pasted snapshot. The pasted part will never move",
    "empty": "nothing to classify",
}


def verdict_for(queries):
    kinds = {q["kind"] for q in queries if q["kind"] != "derived"}
    if not kinds:
        return "empty"
    real = kinds - {"unknown"}
    if not real:
        return "empty"
    if real == {"static"}:
        return "static"
    if "static" in real:
        return "mixed"
    for kind in ("live", "web", "file"):
        if kind in real:
            return kind
    return "empty"


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def render(results, show_paths):
    lines = []
    lines.append("# Power BI source audit")
    lines.append("")
    lines.append("| Report | Queries | Verdict |")
    lines.append("|---|---|---|")
    for r in results:
        v = verdict_for(r["queries"])
        lines.append(f"| {r['file']} | {len(r['queries'])} | {VERDICTS[v]} |")
    lines.append("")

    for r in results:
        lines.append("")
        lines.append("=" * 72)
        lines.append(f"REPORT: {r['file']}")
        lines.append("=" * 72)
        if r["connections"] is not None:
            lines.append(f"  declared connections: {r['connections']}")
        for warning in r["warnings"]:
            lines.append(f"  NOTE: {warning}")
        if not r["queries"]:
            lines.append("  no queries found")
            continue

        for q in r["queries"]:
            labels = ", ".join(label for _, label in q["sources"]) or "none identified"
            lines.append("")
            lines.append(f"  {q['name']}")
            lines.append(f"      kind    : {q['kind'].upper()}")
            lines.append(f"      via     : {labels}")
            for path in q["paths"]:
                lines.append(f"      path    : {path}")
            if "frozen" in q:
                f = q["frozen"]
                lines.append(
                    f"      frozen  : {f['rows']} rows x {f['cols']} columns "
                    f"pasted into the file")
                for row in f["sample"]:
                    text = json.dumps(row)[:160] if not show_paths else json.dumps(row)
                    lines.append(f"                {text}")
            for note in q["notes"]:
                lines.append(f"      note    : {note}")

    lines.append("")
    lines.append("-" * 72)
    lines.append("What to do with this")
    lines.append("-" * 72)
    lines.append(
        "STATIC means the report cannot be populated by fixing a gateway or a")
    lines.append(
        "credential. The data layer has to be built. Take the column names out of")
    lines.append(
        "the frozen sample above, find those fields in the source system, and")
    lines.append("rebuild the query against it.")
    lines.append("")
    lines.append(
        "FILE means it will refresh, but only for whoever can reach that path. If")
    lines.append(
        "the path is a personal drive, treat it as static until the file is moved")
    lines.append("somewhere governed.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True,
                    help=".pbix file, a folder of them, or a text file of M code")
    ap.add_argument("--markdown", help="also write the report to this file")
    ap.add_argument("--show-paths", action="store_true",
                    help="print full paths and URLs instead of abbreviating them")
    args = ap.parse_args()

    root = Path(args.input)
    if not root.exists():
        raise SystemExit(f"Not found: {root}")

    if root.is_dir():
        targets = sorted(root.rglob("*.pbix"))
        if not targets:
            raise SystemExit(f"No .pbix files under {root}")
    else:
        targets = [root]

    results = [audit_source(t, args.show_paths) for t in targets]
    report = render(results, args.show_paths)

    print(report)
    if args.markdown:
        Path(args.markdown).write_text(report + "\n", encoding="utf-8")
        print(f"\nwritten to {args.markdown}", file=sys.stderr)

    # Non zero exit when nothing in the set can refresh, so this can gate a check.
    return 1 if all(verdict_for(r["queries"]) in ("static", "empty")
                    for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
