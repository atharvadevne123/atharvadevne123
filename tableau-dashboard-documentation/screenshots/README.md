# Screenshots and Tableau Public links

## What is in here, and what is not

**No real screenshots were captured.** Rendering a Tableau dashboard needs either a Tableau runtime or access to the published view. Neither was available:

- No Tableau renderer is installed in this environment.
- The outbound network policy returned `403 to CONNECT` for `public.tableau.com:443`, so the published views and their thumbnails could not be fetched.

What is here instead are two **coordinate-accurate layout wireframes**, generated directly from the `<zone>` `x`, `y`, `w`, `h` values in each workbook's XML. Every rectangle sits exactly where the real object sits. They are correct about **geometry, object type and object name**. They say nothing about the rendered charts themselves.

| File | What it shows |
|---|---|
| `dashboard1_heart_failure_layout.svg` | `Dashboard 1`, 1900 x 1050, all 19 worksheet zones plus the colour legend and the Sex filter dropdown |
| `dashboard2_hr_analytics_layout.svg` | `HR Dashboard `, 1580 x 900, all 7 worksheet zones plus the background image, title text object, 3 colour legends, Education filter and `Age Size` parameter slider |

Legend used in both wireframes:

| Colour | Object type |
|---|---|
| White outline | Worksheet |
| Blue | Colour legend |
| Amber | Filter control |
| Purple | Parameter control |
| Green | Text object |
| Dashed grey | Image object |

---

## Slots for your own screenshots

Drop your files in this folder using these exact names and the links in the documentation will resolve.

### Dashboard 1: Healthcare - Heart Failure

**Screenshot file to add:** `dashboard1_screenshot.png`

```markdown
![Healthcare - Heart Failure dashboard](screenshots/dashboard1_screenshot.png)
```

**Tableau Public link:**

```
_________________________________________________________________
```

Recoverable from the workbook XML, to be verified by you:
- Workbook id: `Healthcare-HeartFailure_17429983482570`
- `repository-location derived-from`: `https://public.tableau.com/workbooks/Healthcare-HeartFailure_17429983482570?rev=1.1`
- Dashboard repository id: `Dashboard1`, path `/workbooks/Healthcare-HeartFailure_17429983482570`
- Current revision: `1.2`

**Suggested extra captures:**

| File name | What to capture |
|---|---|
| `dashboard1_kpi_strip.png` | The five KPI cards across the top |
| `dashboard1_donut_detail.png` | One donut close up, showing the four-way colour split and the percent labels |
| `dashboard1_highlight_action.png` | The dashboard after clicking a `Death` mark, so the highlight action is visible across all views |
| `dashboard1_datasource_pane.png` | The data pane showing the aliases and the seven bins |

### Dashboard 2: HR Analytics

**Screenshot file to add:** `dashboard2_screenshot.png`

```markdown
![HR Analytics Dashboard](screenshots/dashboard2_screenshot.png)
```

**Tableau Public link:**

```
_________________________________________________________________
```

Recoverable from the workbook XML, to be verified by you:
- Workbook id: `HRAnalyticsDashboard_17561606616710`
- `repository-location derived-from`: `https://public.tableau.com/workbooks/HRAnalyticsDashboard_17561606616710?rev=1.0`
- Dashboard repository id: `HRDashboard`, path `/workbooks/HRAnalyticsDashboard_17561606616710/HRDashboard`
- Current revision: `1.1`

**Suggested extra captures:**

| File name | What to capture |
|---|---|
| `dashboard2_kpi_strip.png` | The five KPI tiles, ideally showing how `Attrition Rate` currently renders |
| `dashboard2_parameter_2.png` | The age histogram with `Age Size` set to 2 |
| `dashboard2_parameter_10.png` | The same histogram with `Age Size` set to 10, to evidence the parameter working |
| `dashboard2_crossfilter.png` | The dashboard after clicking one department wedge, so the cross-filter effect on the KPI strip is visible |
| `dashboard2_tooltip.png` | One custom tooltip open, showing the hand-authored labels |
| `dashboard2_calcs.png` | The calculated field editor showing `Attrition Rate` |

---

## Two things worth checking when you take these

1. **Dashboard 2 may open pre-filtered.** The workbook was saved with a `Department = "R&D"` mark selected, and that selection is persisted as an action filter into 6 of the 7 worksheets. Check whether the published view opens filtered to R&D. If it does, deselect and re-publish before screenshotting, or the numbers in your screenshot will be R&D numbers.

2. **Dashboard 1's Sex filter does not move the KPI cards.** If you are capturing a before-and-after of the filter, expect the five KPI cards to stay unchanged. That is the workbook's actual behaviour, documented in `01-dashboard1-heart-failure.md` section 8.2, not a rendering problem.
