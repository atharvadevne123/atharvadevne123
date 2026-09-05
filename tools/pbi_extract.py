#!/usr/bin/env python3
"""
Power BI report extractor.

Dumps everything about a Power BI report into plain text you can copy and
paste: pages, every visual, every field and measure each visual uses, the
full DAX, the Power Query M, relationships and data sources.

Works on either:
  * a .pbix file            (pages, visuals, fields, M queries)
  * a .pbip project folder  (all of the above PLUS full DAX measure code)

.pbip is much better because the DAX comes through. See --help output.

Standard library only. Nothing to install.

    python pbi_extract.py --input "Report Dashboard.pbix"
    python pbi_extract.py --input "C:\\work\\Report Dashboard.pbip" --mode full

Output goes to digest_01.txt, digest_02.txt ... sized to paste into chat.

SECURITY: hostnames, URLs, GUIDs, emails and warehouse paths are replaced
with stable placeholders (HOST_1, GUID_1 ...) by default. A summary of what
was replaced is printed at the end. Read the output before you share it.
Use --no-redact only if you are certain the output stays internal.
"""

import argparse
import io
import json
import os
import re
import zipfile
from pathlib import Path

# ---------------------------------------------------------------------------
# Redaction
# ---------------------------------------------------------------------------

class Redactor:
    PATTERNS = [
        ("URL",  re.compile(r"https?://[^\s\"'<>,;)\]]+")),
        ("HOST", re.compile(r"\b(?:[a-zA-Z0-9][a-zA-Z0-9\-]*\.)+(?:azuredatabricks\.net|"
                            r"database\.windows\.net|dfs\.core\.windows\.net|"
                            r"blob\.core\.windows\.net|sharepoint\.com|"
                            r"onmicrosoft\.com|databricks\.com)\b")),
        ("GUID", re.compile(r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}"
                            r"-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b")),
        ("EMAIL", re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")),
        ("WHPATH", re.compile(r"/sql/\d+\.\d+/(?:warehouses|endpoints)/[0-9a-fA-F]+")),
        ("UNCPATH", re.compile(r"\\\\[A-Za-z0-9._\-]+\\[^\s\"'<>,;)\]]+")),
        ("DSN", re.compile(r"(?i)(?:Data Source|Server|Initial Catalog|Catalog)\s*=\s*[^;\"']+")),
    ]

    def __init__(self, enabled=True):
        self.enabled = enabled
        self.map = {}
        self.counters = {}

    def _token(self, kind, value):
        if value in self.map:
            return self.map[value]
        self.counters[kind] = self.counters.get(kind, 0) + 1
        token = f"<{kind}_{self.counters[kind]}>"
        self.map[value] = token
        return token

    def scrub(self, text):
        if not self.enabled or not text:
            return text
        for kind, pattern in self.PATTERNS:
            text = pattern.sub(lambda m: self._token(kind, m.group(0)), text)
        return text

    def report(self):
        if not self.map:
            return "Nothing matched the redaction patterns."
        lines = [f"{len(self.map)} distinct values were replaced:"]
        for value, token in sorted(self.map.items(), key=lambda kv: kv[1]):
            lines.append(f"  {token:<14} was a {token[1:].split('_')[0].lower()} "
                         f"of length {len(value)}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def maybe_json(value):
    """Power BI nests JSON inside JSON strings, several levels deep.
    Parse it whenever it looks parseable."""
    if isinstance(value, str):
        s = value.strip()
        if s.startswith(("{", "[")):
            try:
                return json.loads(s)
            except Exception:
                return value
    return value


def deep_unwrap(node, depth=0):
    if depth > 12:
        return node
    node = maybe_json(node)
    if isinstance(node, dict):
        return {k: deep_unwrap(v, depth + 1) for k, v in node.items()}
    if isinstance(node, list):
        return [deep_unwrap(v, depth + 1) for v in node]
    return node


def find_field_refs(node, found=None):
    """Pull every table.column and table.measure reference out of a visual
    config, wherever it is buried."""
    if found is None:
        found = set()
    if isinstance(node, dict):
        for key in ("queryRef", "Property", "displayName"):
            v = node.get(key)
            if isinstance(v, str) and v and len(v) < 200:
                found.add(v)
        ent = node.get("Entity")
        prop = node.get("Property")
        if isinstance(ent, str) and isinstance(prop, str):
            found.add(f"{ent}.{prop}")
        for v in node.values():
            find_field_refs(v, found)
    elif isinstance(node, list):
        for v in node:
            find_field_refs(v, found)
    return found


def decode_bytes(raw):
    for enc in ("utf-16-le", "utf-8-sig", "utf-8", "latin-1"):
        try:
            text = raw.decode(enc)
            if text and text.lstrip().startswith(("{", "[")):
                return text
        except Exception:
            continue
    return raw.decode("utf-8", errors="replace")


# ---------------------------------------------------------------------------
# PBIX
# ---------------------------------------------------------------------------

def extract_layout(layout, out, red):
    sections = layout.get("sections", []) or []
    out.append(f"PAGE COUNT: {len(sections)}")
    out.append("")

    for idx, section in enumerate(sections, 1):
        name = section.get("displayName") or section.get("name") or f"Page {idx}"
        out.append("=" * 70)
        out.append(f"PAGE {idx}: {red.scrub(str(name))}")
        out.append("=" * 70)
        out.append(f"  internal name : {red.scrub(str(section.get('name','')))}")
        out.append(f"  size          : {section.get('width')} x {section.get('height')}")

        containers = section.get("visualContainers", []) or []
        out.append(f"  visuals       : {len(containers)}")
        out.append("")

        for vnum, container in enumerate(containers, 1):
            config = deep_unwrap(container.get("config", "{}"))
            single = {}
            if isinstance(config, dict):
                single = config.get("singleVisual", {}) or {}

            vtype = single.get("visualType", "unknown")
            title = ""
            vc = single.get("vcObjects", {}) or {}
            try:
                title = vc["title"][0]["properties"]["text"]["expr"]["Literal"]["Value"]
                title = title.strip("'")
            except Exception:
                pass

            out.append(f"  --- Visual {vnum}: {vtype} ---")
            if title:
                out.append(f"      title: {red.scrub(title)}")
            out.append(f"      position: x={container.get('x')} y={container.get('y')} "
                       f"w={container.get('width')} h={container.get('height')}")

            projections = single.get("projections", {}) or {}
            if projections:
                for role, items in projections.items():
                    refs = [i.get("queryRef", "") for i in items if isinstance(i, dict)]
                    refs = [r for r in refs if r]
                    if refs:
                        out.append(f"      {role}: {', '.join(red.scrub(r) for r in refs)}")
            else:
                refs = sorted(r for r in find_field_refs(single) if "." in r)
                if refs:
                    out.append(f"      fields: {', '.join(red.scrub(r) for r in refs[:25])}")

            filters = deep_unwrap(container.get("filters", "[]"))
            if isinstance(filters, list) and filters:
                fr = sorted(r for r in find_field_refs(filters) if "." in r)
                if fr:
                    out.append(f"      visual filters: {', '.join(red.scrub(r) for r in fr[:15])}")
            out.append("")

        pf = deep_unwrap(section.get("filters", "[]"))
        if isinstance(pf, list) and pf:
            fr = sorted(r for r in find_field_refs(pf) if "." in r)
            if fr:
                out.append(f"  PAGE FILTERS: {', '.join(red.scrub(r) for r in fr)}")
                out.append("")

    rf = deep_unwrap(layout.get("filters", "[]"))
    if isinstance(rf, list) and rf:
        fr = sorted(r for r in find_field_refs(rf) if "." in r)
        if fr:
            out.append("=" * 70)
            out.append("REPORT LEVEL FILTERS")
            out.append("=" * 70)
            out.append(", ".join(red.scrub(r) for r in fr))
            out.append("")


def extract_mashup(raw, out, red):
    """DataMashup holds the Power Query M. It is a zip embedded in a binary
    header, so seek to the first zip signature and read from there."""
    sig = raw.find(b"PK\x03\x04")
    if sig < 0:
        out.append("  (no embedded package found)")
        return
    try:
        with zipfile.ZipFile(io.BytesIO(raw[sig:])) as z:
            for name in z.namelist():
                if name.lower().endswith(".m") or "section" in name.lower():
                    text = z.read(name).decode("utf-8", errors="replace")
                    out.append(f"  --- {name} ---")
                    out.append(red.scrub(text))
                    out.append("")
    except Exception as exc:
        out.append(f"  (could not read embedded package: {exc})")


def read_pbix(path, out, red, mode):
    out.append("#" * 70)
    out.append("# SOURCE: .pbix")
    out.append("#" * 70)
    out.append("")
    out.append("NOTE: a .pbix cannot give up its DAX measure definitions. You will")
    out.append("get pages, visuals, fields and the Power Query M. To also capture")
    out.append("the DAX, open the file in Power BI Desktop and re-save it as .pbip,")
    out.append("then run this script against the .pbip folder instead.")
    out.append("")

    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        out.append("PARTS IN FILE: " + ", ".join(names))
        out.append("")

        for part in names:
            if part.endswith("Layout") or part.endswith("Report/Layout"):
                out.append("#" * 70)
                out.append("# REPORT LAYOUT: pages and visuals")
                out.append("#" * 70)
                out.append("")
                try:
                    layout = json.loads(decode_bytes(z.read(part)))
                    extract_layout(layout, out, red)
                except Exception as exc:
                    out.append(f"(failed to parse layout: {exc})")

        if "DataMashup" in names:
            out.append("#" * 70)
            out.append("# POWER QUERY (M)")
            out.append("#" * 70)
            out.append("")
            extract_mashup(z.read("DataMashup"), out, red)

        for part in ("Connections", "Metadata", "Settings", "Version"):
            if part in names and mode == "full":
                out.append("#" * 70)
                out.append(f"# {part.upper()}")
                out.append("#" * 70)
                try:
                    out.append(red.scrub(decode_bytes(z.read(part))))
                except Exception as exc:
                    out.append(f"(unreadable: {exc})")
                out.append("")


# ---------------------------------------------------------------------------
# PBIP
# ---------------------------------------------------------------------------

def read_pbip(root, out, red, mode):
    root = Path(root)
    if root.is_file():
        root = root.parent

    out.append("#" * 70)
    out.append("# SOURCE: .pbip project")
    out.append("#" * 70)
    out.append("")

    tmdl = sorted(root.rglob("*.tmdl"))
    if tmdl:
        out.append("#" * 70)
        out.append("# SEMANTIC MODEL (TMDL): tables, columns, measures with DAX,")
        out.append("# relationships, and the M partition queries")
        out.append("#" * 70)
        out.append("")
        for f in tmdl:
            out.append("=" * 70)
            out.append(f"FILE: {f.relative_to(root).as_posix()}")
            out.append("=" * 70)
            out.append(red.scrub(f.read_text(encoding="utf-8", errors="replace")))
            out.append("")

    model_json = sorted(root.rglob("model.bim")) + sorted(root.rglob("*.Dataset/model.bim"))
    for f in model_json:
        out.append("=" * 70)
        out.append(f"FILE: {f.relative_to(root).as_posix()}")
        out.append("=" * 70)
        out.append(red.scrub(f.read_text(encoding="utf-8", errors="replace")))
        out.append("")

    # Report definition. Newer PBIP splits pages into folders; older uses report.json.
    report_json = sorted(root.rglob("report.json"))
    for f in report_json:
        out.append("#" * 70)
        out.append("# REPORT DEFINITION (report.json)")
        out.append("#" * 70)
        try:
            layout = json.loads(f.read_text(encoding="utf-8", errors="replace"))
            extract_layout(layout, out, red)
        except Exception as exc:
            out.append(f"(failed to parse: {exc})")
        out.append("")

    pages = sorted(root.rglob("pages/**/page.json"))
    if pages:
        out.append("#" * 70)
        out.append("# REPORT PAGES")
        out.append("#" * 70)
        out.append("")
        for pfile in pages:
            try:
                page = json.loads(pfile.read_text(encoding="utf-8", errors="replace"))
            except Exception:
                continue
            out.append("=" * 70)
            out.append(f"PAGE: {red.scrub(str(page.get('displayName', pfile.parent.name)))}")
            out.append("=" * 70)
            vfiles = sorted(pfile.parent.rglob("visual.json"))
            out.append(f"  visuals: {len(vfiles)}")
            out.append("")
            for vfile in vfiles:
                try:
                    v = json.loads(vfile.read_text(encoding="utf-8", errors="replace"))
                except Exception:
                    continue
                vis = v.get("visual", {}) or {}
                out.append(f"  --- Visual: {vis.get('visualType','unknown')} ---")
                pos = v.get("position", {}) or {}
                if pos:
                    out.append(f"      position: x={pos.get('x')} y={pos.get('y')} "
                               f"w={pos.get('width')} h={pos.get('height')}")
                refs = sorted(r for r in find_field_refs(vis) if "." in r)
                if refs:
                    out.append(f"      fields: {', '.join(red.scrub(r) for r in refs[:30])}")
                if mode == "full":
                    out.append(red.scrub(json.dumps(v, indent=2))[:4000])
                out.append("")

    if not tmdl and not pages and not report_json and not model_json:
        out.append("Nothing recognisable found. Check that you pointed --input at the")
        out.append("folder containing the .pbip file, or at the .pbip file itself.")


# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help=".pbix file, .pbip file, or project folder")
    ap.add_argument("--out", default="digest", help="output file prefix (default: digest)")
    ap.add_argument("--mode", choices=["summary", "full"], default="summary",
                    help="full also dumps raw JSON blobs. Much longer.")
    ap.add_argument("--chunk-chars", type=int, default=40000,
                    help="characters per output file (default 40000)")
    ap.add_argument("--no-redact", action="store_true",
                    help="do NOT replace hostnames, GUIDs, emails and URLs")
    args = ap.parse_args()

    src = Path(args.input)
    if not src.exists():
        raise SystemExit(f"Not found: {src}")

    red = Redactor(enabled=not args.no_redact)
    out = []

    out.append("POWER BI REPORT DIGEST")
    out.append(f"source name : {src.name}")
    out.append(f"mode        : {args.mode}")
    out.append(f"redaction   : {'OFF' if args.no_redact else 'ON'}")
    out.append("")

    if src.is_file() and src.suffix.lower() == ".pbix":
        read_pbix(src, out, red, args.mode)
    else:
        read_pbip(src, out, red, args.mode)

    out.append("")
    out.append("#" * 70)
    out.append("# REDACTION SUMMARY")
    out.append("#" * 70)
    out.append(red.report())

    text = "\n".join(out)

    # chunk on line boundaries so nothing is cut mid line
    chunks, buf, size = [], [], 0
    for line in text.split("\n"):
        if size + len(line) + 1 > args.chunk_chars and buf:
            chunks.append("\n".join(buf))
            buf, size = [], 0
        buf.append(line)
        size += len(line) + 1
    if buf:
        chunks.append("\n".join(buf))

    for i, chunk in enumerate(chunks, 1):
        fname = f"{args.out}_{i:02d}.txt"
        header = f"===== PART {i} OF {len(chunks)} =====\n\n"
        Path(fname).write_text(header + chunk, encoding="utf-8")
        print(f"wrote {fname}  ({len(chunk):,} chars)")

    print()
    print(f"Total {len(text):,} characters across {len(chunks)} file(s).")
    print()
    print(red.report())
    print()
    print("Open each file, READ IT, then paste the contents into the chat in order.")


if __name__ == "__main__":
    main()
