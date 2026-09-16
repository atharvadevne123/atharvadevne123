#!/usr/bin/env python3
"""Build one self-contained PDF per dashboard from the markdown documentation.

Markdown -> HTML (python-markdown, tables + fenced code) -> PDF (headless Chromium).
"""
import html
import os
import re
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.dirname(HERE)
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4 landscape; margin: 13mm 12mm 15mm 12mm; }
* { box-sizing: border-box; }
body {
  font-family: "DejaVu Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 9.2pt; line-height: 1.5; color: #15171a; margin: 0;
  -webkit-print-color-adjust: exact; print-color-adjust: exact;
}
p, ul, ol, blockquote { max-width: 205mm; }
h1 {
  font-size: 19pt; line-height: 1.2; margin: 0 0 6pt; padding-bottom: 5pt;
  border-bottom: 2.5pt solid #1f4e79; color: #1f4e79;
  break-before: page; break-after: avoid;
}
h1:first-of-type { break-before: auto; }
h2 {
  font-size: 13.5pt; margin: 16pt 0 5pt; padding-bottom: 3pt;
  border-bottom: 0.8pt solid #b8c4d0; color: #1f4e79; break-after: avoid;
}
h3 { font-size: 11pt; margin: 12pt 0 4pt; color: #24445e; break-after: avoid; }
h4 { font-size: 9.8pt; margin: 9pt 0 3pt; color: #3a3f45; break-after: avoid; }
table {
  border-collapse: collapse; width: 100%; margin: 6pt 0 10pt;
  font-size: 7.4pt; line-height: 1.34; table-layout: auto;
}
th, td {
  border: 0.5pt solid #c3ccd6; padding: 2.6pt 3.6pt;
  text-align: left; vertical-align: top; word-break: normal; overflow-wrap: anywhere;
}
th { background: #eaeff4; font-weight: 700; color: #1f4e79; }
tr:nth-child(even) td { background: #f7f9fb; }
tr { break-inside: avoid; }
code {
  font-family: "DejaVu Sans Mono", "SF Mono", Menlo, Consolas, monospace;
  font-size: 0.87em; background: #eef1f4; padding: 0.5pt 2.5pt;
  border-radius: 2pt; color: #8a2846; overflow-wrap: anywhere;
}
th code, td code { font-size: 0.93em; padding: 0.3pt 1.6pt; }
pre {
  background: #f5f7f9; border: 0.5pt solid #ccd5de; border-left: 2.5pt solid #1f4e79;
  padding: 6pt 8pt; font-size: 7.3pt; line-height: 1.38; overflow-x: hidden;
  white-space: pre-wrap; break-inside: avoid; max-width: 100%;
}
pre code { background: none; padding: 0; color: #1c2126; font-size: 1em; }
blockquote {
  border-left: 2.5pt solid #d8a13a; background: #fdf8ec;
  margin: 8pt 0; padding: 6pt 10pt; break-inside: avoid;
}
blockquote p { margin: 3pt 0; }
hr { border: none; border-top: 0.5pt solid #ccd5de; margin: 12pt 0; }
strong { color: #0f1216; }
li { margin: 1.5pt 0; }
a { color: #1f4e79; text-decoration: none; }

/* ---- cover ---- */
.cover { break-after: page; padding-top: 6mm; }
.cover .eyebrow {
  font-size: 9pt; letter-spacing: 2.4pt; text-transform: uppercase;
  color: #6d7782; margin-bottom: 5pt;
}
.cover h1 {
  font-size: 31pt; border: none; margin: 0 0 4pt; padding: 0;
  break-before: auto; color: #14324d; line-height: 1.12;
}
.cover .sub { font-size: 13pt; color: #4a5560; margin: 0 0 14pt; max-width: none; }
.cover .rule { height: 3pt; background: #1f4e79; width: 74mm; margin-bottom: 14pt; }
.meta { width: 100%; font-size: 8.4pt; margin-bottom: 12pt; }
.meta td { border: none; padding: 2.4pt 10pt 2.4pt 0; background: none !important; }
.meta td:first-child {
  color: #6d7782; width: 46mm; font-weight: 700;
  text-transform: uppercase; letter-spacing: 0.5pt; font-size: 7.4pt;
}
.slot {
  border: 1pt dashed #9aa6b2; background: #f7f9fb; padding: 9pt 11pt;
  margin: 9pt 0; font-size: 8.4pt; break-inside: avoid;
}
.slot .lbl {
  font-weight: 700; color: #1f4e79; text-transform: uppercase;
  letter-spacing: 0.9pt; font-size: 7.4pt; display: block; margin-bottom: 4pt;
}
.slot .line {
  border-bottom: 0.7pt solid #56606b; height: 15pt; margin-top: 5pt; width: 150mm;
}
.wire { text-align: center; margin: 8pt 0 0; break-inside: avoid; }
.wire svg { max-width: 100%; height: auto; border: 0.5pt solid #ccd5de; }
.wire .cap { font-size: 7.6pt; color: #6d7782; margin-top: 4pt; font-style: italic; }
.note {
  background: #eef4f9; border-left: 2.5pt solid #1f4e79;
  padding: 7pt 10pt; margin: 9pt 0; font-size: 8.4pt; break-inside: avoid;
}
.parthead { break-before: page; padding-top: 30mm; text-align: center; }
.parthead .pn {
  font-size: 9pt; letter-spacing: 3pt; text-transform: uppercase; color: #6d7782;
}
.parthead .pt {
  font-size: 25pt; color: #14324d; font-weight: 700; margin-top: 6pt; line-height: 1.2;
}
.parthead .pd {
  font-size: 10pt; color: #4a5560; margin-top: 8pt;
  max-width: 170mm; margin-left: auto; margin-right: auto;
}
.toc { font-size: 9pt; }
.toc td { border: none; padding: 2pt 8pt 2pt 0; background: none !important; }
.toc td:first-child { width: 20mm; color: #6d7782; font-weight: 700; }
"""


def md_to_html(text: str) -> str:
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )


def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def inline_svg(path: str) -> str:
    svg = read(path)
    return svg[svg.index("<svg"):]


def strip_leading_h1(body_md: str) -> str:
    """Drop the source file's own H1 so the Part divider carries the title."""
    return re.sub(r"\A#\s.*?\n", "", body_md, count=1)


def strip_screenshot_blockquote(body_md: str) -> str:
    """Remove the inline screenshot slot; the cover carries a nicer one."""
    lines = body_md.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("> **Screenshot slot."):
            while i < len(lines) and (lines[i].startswith(">") or not lines[i].strip()):
                i += 1
            while out and not out[-1].strip():
                out.pop()
            if i < len(lines) and lines[i].strip() == "---":
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def cover(title, subtitle, meta_rows, wire_svg, wire_cap, pub_hint):
    rows = "\n".join(
        f"<tr><td>{html.escape(k)}</td><td>{v}</td></tr>" for k, v in meta_rows
    )
    return f"""
<section class="cover">
  <div class="eyebrow">Tableau Workbook Reverse-Engineering</div>
  <h1>{html.escape(title)}</h1>
  <p class="sub">{html.escape(subtitle)}</p>
  <div class="rule"></div>
  <table class="meta">{rows}</table>

  <div class="slot">
    <span class="lbl">Screenshot slot</span>
    Paste your own dashboard screenshot here. No real screenshot could be captured:
    no Tableau runtime was available and the network policy denied
    <code>public.tableau.com</code>.
  </div>

  <div class="slot">
    <span class="lbl">Tableau Public link</span>
    {pub_hint}
    <div class="line"></div>
  </div>

  <div class="wire">{wire_svg}<div class="cap">{html.escape(wire_cap)}</div></div>
</section>
"""


def parthead(pn, pt, pd):
    return (
        f'<section class="parthead"><div class="pn">{html.escape(pn)}</div>'
        f'<div class="pt">{html.escape(pt)}</div>'
        f'<div class="pd">{html.escape(pd)}</div></section>'
    )


def build(slug, title, subtitle, meta_rows, part_a_md, part_b_md,
          wire_path, wire_cap, pub_hint, toc_rows, out_pdf):
    body = [
        cover(title, subtitle, meta_rows, inline_svg(wire_path), wire_cap, pub_hint),
        '<section class="parthead"><div class="pn">Contents</div>'
        '<div class="pt">What is in this document</div></section>',
        "<table class='toc'>"
        + "".join(f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td></tr>"
                  for a, b in toc_rows)
        + "</table>",
        parthead(
            "Part A",
            "Full technical documentation",
            "Sections 1 to 19: overview, data sources, data model, preparation, field "
            "inventory, calculated fields, parameters, filters, KPIs, worksheet analysis, "
            "visualization breakdown, layout, actions, tooltips, business logic, enabled "
            "insights, technical summary, interview explanation and resume bullets.",
        ),
        md_to_html(strip_leading_h1(strip_screenshot_blockquote(read(part_a_md)))),
        parthead(
            "Part B",
            "Hands-on evidence brief",
            "Sections 1 to 13 for a hiring manager confirming hands-on experience: "
            "context, source inventory, source-to-target mapping, data flow, cleaning "
            "rules, data model, business rules and governance, operations and security, "
            "requirements to KPIs, stakeholder coordination, outcomes, open questions "
            "and a sanitised version with its substitution list.",
        ),
        md_to_html(strip_leading_h1(read(part_b_md))),
    ]

    doc = (
        "<!DOCTYPE html><html lang='en'><head><meta charset='utf-8'>"
        f"<title>{html.escape(title)}</title><style>{CSS}</style></head>"
        f"<body>{''.join(body)}</body></html>"
    )

    html_path = os.path.join(HERE, f"{slug}.html")
    with open(html_path, "w", encoding="utf-8") as fh:
        fh.write(doc)

    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
         "--virtual-time-budget=20000", "--no-pdf-header-footer",
         f"--print-to-pdf={out_pdf}", f"file://{html_path}"],
        check=True, capture_output=True,
    )
    return out_pdf


D1_META = [
    ("Dashboard", "<code>Dashboard 1</code>"),
    ("Workbook", "<code>Healthcare - Heart Failure.twb</code> (packaged workbook)"),
    ("Author", "Atharva Devne"),
    ("Project type", "<strong>Self-directed</strong>, for the author's own skill development"),
    ("Dataset", "<strong>Kaggle</strong>, public dataset. "
                "<code>heart_failure_clinical_records_dataset.csv</code>, 13 columns"),
    ("Tableau", "Desktop 2025.1.0 <code>(20251.25.0313.2002)</code>, macOS, doc format 18.1"),
    ("Canvas", "1900 x 1050 px, <code>sizing-mode='range'</code>, black, fully tiled"),
    ("Scale", "19 worksheets, 1 dashboard, 13 calculated fields, 1 action"),
    ("Status", "Published to Tableau Public, revision 1.2"),
]

D2_META = [
    ("Dashboard", "<code>HR Dashboard </code> (the name carries a trailing space)"),
    ("Workbook", "<code>HR Analytics Dashboard.twb</code> (packaged workbook)"),
    ("Author", "Atharva Devne"),
    ("Project type", "<strong>Self-directed</strong>, for the author's own skill development"),
    ("Dataset", "<strong>Kaggle</strong>, public dataset. "
                "<code>HR_data.csv</code>, 39 columns, 15 consumed"),
    ("Tableau", "Desktop 2025.2.0 <code>(20252.25.0514.2217)</code>, macOS, doc format 18.1"),
    ("Canvas", "1580 x 900 px, <code>sizing-mode='fixed'</code>, floating over a background image"),
    ("Scale", "7 worksheets, 1 dashboard, 6 calculated fields, 1 parameter, 6 actions"),
    ("Status", "Published to Tableau Public, revision 1.1"),
]

TOC_A = [
    ("Part A", "Full technical documentation, sections 1 to 19"),
    ("1", "Dashboard overview"),
    ("2", "Data source inventory"),
    ("3", "Data model, relationships, joins"),
    ("4", "Data preparation and cleaning"),
    ("5", "Complete field inventory"),
    ("6", "Calculated fields, with exact formulas"),
    ("7", "Parameters"),
    ("8", "Filters"),
    ("9", "KPI identification"),
    ("10", "Worksheet by worksheet analysis"),
    ("11", "Visualization by visualization breakdown"),
    ("12", "Dashboard layout"),
    ("13", "Dashboard actions and interactivity"),
    ("14", "Tooltips"),
    ("15", "Business logic"),
    ("16", "Key insights the dashboard enables"),
    ("17", "Technical implementation summary"),
    ("18", "Interview explanation"),
    ("19", "Resume-ready project description"),
    ("Part B", "Hands-on evidence brief, sections 1 to 13"),
    ("1", "Project context"),
    ("2", "Source systems and data inventory"),
    ("3", "Source-to-target mapping"),
    ("4", "Data flow and architecture"),
    ("5", "Consolidation, cleaning and standardisation"),
    ("6", "Data model: schema and table design"),
    ("7", "Business rules, validation and governance"),
    ("8", "Refresh, operations and security"),
    ("9", "Requirements to KPIs and dashboard logic"),
    ("10", "Stakeholder coordination"),
    ("11", "Outcomes and status"),
    ("12", "Gaps and questions"),
    ("13", "Sanitised version and substitution list"),
]

if __name__ == "__main__":
    out1 = build(
        slug="Dashboard1_Healthcare_Heart_Failure",
        title="Healthcare, Heart Failure",
        subtitle="Complete technical documentation of a 19-worksheet Tableau survival "
                 "profiling dashboard, extracted from the workbook XML",
        meta_rows=D1_META,
        part_a_md=os.path.join(DOCS, "01-dashboard1-heart-failure.md"),
        part_b_md=os.path.join(HERE, "partB-dashboard1.md"),
        wire_path=os.path.join(DOCS, "screenshots", "dashboard1_heart_failure_layout.svg"),
        wire_cap="Coordinate-accurate wireframe reconstructed from the <zones> geometry "
                 "in the .twb XML. Not a screenshot.",
        pub_hint="Recoverable from the XML, to be verified by you: workbook id "
                 "<code>Healthcare-HeartFailure_17429983482570</code>, dashboard "
                 "repository id <code>Dashboard1</code>, current revision 1.2.",
        toc_rows=TOC_A,
        out_pdf=os.path.join(DOCS, "Dashboard1_Healthcare_Heart_Failure.pdf"),
    )
    print("built", out1)

    out2 = build(
        slug="Dashboard2_HR_Analytics",
        title="HR Analytics Dashboard",
        subtitle="Complete technical documentation of a 7-worksheet Tableau attrition "
                 "dashboard, extracted from the workbook XML",
        meta_rows=D2_META,
        part_a_md=os.path.join(DOCS, "02-dashboard2-hr-analytics.md"),
        part_b_md=os.path.join(HERE, "partB-dashboard2.md"),
        wire_path=os.path.join(DOCS, "screenshots", "dashboard2_hr_analytics_layout.svg"),
        wire_cap="Coordinate-accurate wireframe reconstructed from the <zones> geometry "
                 "in the .twb XML. Not a screenshot.",
        pub_hint="Recoverable from the XML, to be verified by you: workbook id "
                 "<code>HRAnalyticsDashboard_17561606616710</code>, dashboard path "
                 "<code>/workbooks/HRAnalyticsDashboard_17561606616710/HRDashboard</code>, "
                 "current revision 1.1.",
        toc_rows=TOC_A,
        out_pdf=os.path.join(DOCS, "Dashboard2_HR_Analytics.pdf"),
    )
    print("built", out2)
