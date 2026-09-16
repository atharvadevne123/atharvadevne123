# Tableau Dashboard Reverse-Engineering Documentation

Complete technical documentation of two Tableau workbooks, extracted directly from the workbook XML.

## How this document was produced

Both uploaded files carry a `.twb` extension, but both are actually ZIP archives, which means both are **packaged workbooks (`.twbx` content)** that were renamed or saved with a `.twb` extension. Each archive was unpacked and the inner `.twb` XML was parsed with `xml.etree.ElementTree`.

| Uploaded file | Actual container | Inner workbook XML | Other archive members |
|---|---|---|---|
| `26be98de-Healthcare_-_Heart_Failure.twb` | ZIP (packaged workbook) | `Healthcare - Heart Failure.twb` (186,093 bytes) | `Data/tableau-temp/#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper` (65,536 bytes) |
| `a952d992-HR_Analytics_Dashboard.twb` | ZIP (packaged workbook) | `HR Analytics Dashboard.twb` (360,533 bytes) | `Image/HR background.pptx.png` (410,683 bytes), 4 x `Data/tableau-temp/*.hyper` (196,608 bytes each) |

Every fact below is tagged:

- **✓ DIRECTLY VERIFIED** means the value is literally present in the workbook XML and is quoted or transcribed.
- **△ INFERRED** means it is a reasonable reading of the XML structure, not a stored value.
- **✗ NOT AVAILABLE** means the workbook does not contain it.

## A note on screenshots

Rendering a live screenshot of either dashboard requires a Tableau runtime or access to `public.tableau.com`. Neither is available in this environment: the outbound network policy returned `403 to CONNECT` for `public.tableau.com:443`, and no Tableau renderer is installed. **No real screenshots were captured.**

What was produced instead are two **coordinate-accurate layout wireframes**, generated directly from the `<zone>` x/y/w/h values in the XML. These are exact reconstructions of object geometry, not pictures of the rendered dashboards:

- `screenshots/dashboard1_heart_failure_layout.svg`
- `screenshots/dashboard2_hr_analytics_layout.svg`

Placeholder slots for your own screenshots and Tableau Public links are provided in `screenshots/README.md`.

## Files in this documentation set

| File | Contents |
|---|---|
| `00-overview-and-method.md` | This file |
| `01-dashboard1-heart-failure.md` | Dashboard 1, sections 1 to 19 |
| `02-dashboard2-hr-analytics.md` | Dashboard 2, sections 1 to 19 |
| `03-cross-dashboard-comparison.md` | Cross-dashboard comparison, final technical inventory, evidence and confidence |
| `04-hands-on-evidence-brief.md` | The structured hands-on brief for a hiring manager, sections 1 to 13 |
| `screenshots/` | Layout wireframes and placeholder slots |
