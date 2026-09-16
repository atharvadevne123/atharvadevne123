# CROSS-DASHBOARD COMPARISON

No ranking is offered. These are documented differences only.

## 1. Data source comparison

| Aspect | Dashboard 1: Healthcare - Heart Failure | Dashboard 2: HR Analytics |
|---|---|---|
| Number of `<datasource>` elements | 1 | 5 (1 `Parameters` container + 4 real connections) |
| Data sources actually used | 1 of 1 | 1 of 4, plus the `Parameters` container |
| Source file | `heart_failure_clinical_records_dataset.csv` | `HR_data.csv` |
| Source directory | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` | `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` |
| Connection class | `textscan` | `textscan` (an `excel-direct` connection is also declared but not bound) |
| Text parsing options stored | Yes: UTF-8, `,`, header yes, `en_US` | Not stored on the active relation |
| Source columns | 13 | 39 |
| Columns actually used on shelves | 13 of 13 | 15 of 39 |
| Live or extract | Extract, `count='-1'` | Extract, `count='-1'`, on all four data sources |
| `.hyper` files in the archive | 1 | 4 (3 of them unused) |
| Data source filters | None | One, on `[Education]`, at `<shared-view>` scope |
| Custom SQL | None | None |
| Aliases | Yes, 6 fields | None |
| Upstream-derived columns | None | 3 (`CF_age band`, `CF_attrition label`, `CF_current Employee`) |

## 2. Data modelling comparison

| Aspect | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Tables | 1 | 1 (per data source) |
| Joins | None | None |
| Relationships | None | None |
| Unions | None | None |
| Blending | Not possible, one data source | Not used, despite four data sources being present |
| Nested joins | None | None |
| Model complexity | Flat single table | Flat single table |

**Neither workbook demonstrates data modelling.** Both are single flat tables. If a hiring manager asks either of these projects to evidence SQL or data modelling skill, the honest answer is that they do not. That capability needs to be evidenced elsewhere.

## 3. KPI comparison

| Aspect | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Number of KPIs | 5 | 5 |
| Construction | **Five separate worksheets**, each with a string literal caption plus one aggregate on Text | **One worksheet** using Measure Names on Columns and Measure Values on Text |
| KPI list | `Total Individuals`, `Total Deaths`, `Total Males`, `Total Females`, `Average Age` | `Employee Count`, `Attrition Count`, `Attrition Rate`, `Active Employees`, `AVG(Age)` |
| Aggregations used | `CNT` x4, `AVG` x1 | `SUM` x2, User-defined aggregate x2, `AVG` x1 |
| Any true ratio KPI | **No.** All are counts or a mean. | **Yes**, `Attrition Rate` = `SUM([Attrition Count])/SUM([Employee Count])` |
| KPI dependency depth | 0. Every number is a direct aggregate of a source column. | **2.** `[Attrition]` → `Attrition Count` → `Attrition Rate` and `Active Employees` |
| How the caption is produced | Five string-literal calculated fields | Measure Names |
| Responds to the dashboard filter | **No.** The KPI worksheets sit outside `filter-group 3`. | **Yes.** The Education filter is data source scoped, so the KPI sheet is in scope. |
| Number formatting | None specified | None specified |
| Targets or benchmarks | None | None |
| Maintenance cost | Five sheets to edit if the style changes | One sheet |

## 4. Calculation complexity comparison

| Aspect | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Total calculated fields | 13 | 6 |
| Bins | 7, all fixed size | 1, **parameter-driven** |
| String literal calcs | 5 | 0 |
| Constant axis placeholder | 1 (`0`) | 1 (`min(1)`) |
| Conditional logic (`IF/THEN/ELSE`) | **0** | **1** (`Attrition Count`) |
| `CASE` statements | 0 | 0 |
| Aggregate-over-aggregate calcs | 0 | **2** (`Attrition Rate`, `Active Employees`) |
| LOD expressions | 0 | 0 |
| Table calculations | 1 type, `PctTotal` along Rows, on 5 sheets | 1 type, `PctTotal` along Table (Across), on 2 sheets |
| Window / rank / running total | 0 | 0 |
| Date calculations | 0 (no date field exists) | 0 (no date field exists) |
| Parameters inside calculations | 0 | **1** (`[Age Parameter]` as a `size-parameter`) |
| Longest dependency chain | 1 level (bins reference a source column) | **3 levels** (`[Attrition]` → `Attrition Count` → `Attrition Rate`) |
| Reference lines | **1** (`average`, `scope='per-cell'`) | 0 |

**Summary.** Dashboard 1 has more calculated fields; Dashboard 2 has deeper ones. Dashboard 1's calculations are mostly presentational (captions, an axis placeholder, seven default bins). Dashboard 2's calculations carry business logic and chain together. Neither uses LODs.

## 5. Visualization comparison

| Chart type | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Donut (dual-axis pie) | 5 | 1 (as a row of small multiples) |
| Plain pie | 0 | 1 |
| Histogram / bar over a bin | 7 | 1 |
| Horizontal bar | 0 | 1 |
| Lollipop (Bar + Circle dual axis) | 0 | 1 |
| Highlight table (Square marks) | 0 | 1 |
| Scatter plot | 1 | 0 |
| Disaggregated dot plot with reference line | 1 | 0 |
| Text / BAN KPI cards | 5 | 1 sheet holding 5 tiles |
| **Total worksheets** | **19** | **7** |
| Distinct chart forms | 5 (donut, histogram, scatter, dot plot, text) | 7 (KPI strip, lollipop, pie, histogram, highlight table, bar, donut multiples) |
| Mark types explicitly set | `Pie`, `Circle` | `Pie`, `Bar`, `Circle`, `Square` |
| Colour strategy | **Categorical only.** Explicit hex maps: a 4-way crossed palette (`summer_10_0` overridden to `#8fb202`, `#b9ca5d`, `#cf3e53`, `#f1788d`) and a 2-way outcome palette (`#59a14f`, `#e15759`) | **Mixed.** Two continuous sequential ramps (`blue_10_0`, `purple_10_0`, both `type='interpolated'`) plus two default categorical encodings with no override |
| Colour legends on the dashboard | 1 | 3 |
| Two fields on one Colour shelf | **Yes**, on all 5 donuts | No |
| Sorting | **None anywhere** | 2 manual sorts with explicit dictionaries |
| Reference lines | 1 | 0 |
| Trend lines / forecasting / clustering | None | None |
| Maps | None | None |
| Theme | Black canvas, white bold 8pt text, gridlines and zero lines switched off | Dark background image, gold (`#f1ce63`) titles, dark blue (`#2f5597`) tooltip values |
| Repetition strategy | One visual grammar repeated many times (5 identical donuts, 7 identical histograms) | Seven distinct chart forms, little repetition |

## 6. Interactivity comparison

| Aspect | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Total actions | **1** | **6** |
| Action type | **Highlight** (`tsc:brush`) | **Filter** (`tsc:tsl-filter`) x6 |
| Highlight actions | 1 | 0 |
| Filter actions | 0 | 6 |
| Parameter actions | 0 | 0 |
| Set actions | 0 | 0 |
| Navigation actions | 0 | 0 |
| Trigger | `on-select`, `auto-clear='true'` | `on-select`, `auto-clear='true'` on all six |
| Fields passed | One named field, `Death Event` | `special-fields='all'` on all six |
| Source scope | Whole dashboard | One named source worksheet per action |
| Filter controls | 1 dropdown (`Sex`) | 1 dropdown (`Education`) |
| Filter control scope | `filter-group='3'`, 14 of 19 worksheets, **excluding the KPI cards** | Data source `<shared-view>`, **all 7 worksheets including the KPI sheet** |
| Parameter controls | **0** | **1** slider (`Age Size`, 2 to 10) |
| Auto-generated hidden action groups | 0 | 4 |
| Persisted selection state saved into the file | None | **Yes**, `Department = "R&D"` on 6 of 7 worksheets |
| Viz-in-tooltip | No | No |
| Net interaction model | Click to highlight one shared class across every view; one dropdown to restrict by sex | Click any chart to cross-filter everything else; one dropdown and one slider |

## 7. Tableau features used in each

| Feature | Dashboard 1 | Dashboard 2 |
|---|---|---|
| Flat file connection (`textscan`) | Yes | Yes |
| Extract (Hyper) | Yes | Yes (x4) |
| Field captions / renaming | Yes (13) | Yes (10) |
| Measure to dimension role conversion | Yes (6 fields) | Yes (2 fields) |
| **Value aliases** | **Yes (6 fields, 12 aliases)** | No |
| **Fixed-size bins** | **Yes (7)** | No |
| **Parameter-driven bin** | No | **Yes (1)** |
| **Parameters** | No | **Yes (1, range type)** |
| **IF/THEN/ELSE** | No | **Yes (1)** |
| **Aggregate calculations** | No | **Yes (2)** |
| String literal calculated fields | Yes (5) | No |
| Constant axis placeholder for dual axis | Yes (`0`) | Yes (`min(1)`) |
| **Dual axis** | **Yes (5 sheets)** | **Yes (2 sheets)** |
| Table calculation: Percent of Total | Yes (5 sheets, along Rows) | Yes (2 sheets, along Table Across) |
| **Measure Names / Measure Values** | No | **Yes** |
| **Manual sort with dictionary** | No | **Yes (2)** |
| **Reference line** | **Yes (`average`, per-cell)** | No |
| **Disaggregation (Aggregate Measures off)** | **Yes (1 sheet)** | No |
| **Two fields on one Colour shelf** | **Yes (5 sheets)** | No |
| **Continuous / sequential colour ramp** | No | **Yes (2 sheets)** |
| Explicit hex colour overrides | Yes | No (defaults used for categorical) |
| **Custom tooltips** | **No (zero)** | **Yes (all 7 worksheets)** |
| **Custom mark labels** | No | **Yes (6 label definitions)** |
| Custom worksheet titles | Yes (14 typed strings) | Yes (6, using the `<Sheet Name>` token) |
| **Text object on the dashboard** | No | **Yes (1)** |
| **Image object on the dashboard** | No | **Yes (1, PNG exported from PowerPoint)** |
| Colour legend on the dashboard | Yes (1) | Yes (3) |
| Filter control on the dashboard | Yes (1 dropdown) | Yes (1 dropdown) |
| **Parameter control on the dashboard** | No | **Yes (1 slider)** |
| Tiled container layout | **Yes, fully tiled with nested flow containers** | Partly. Only the background image is tiled; everything else floats. |
| **Floating layout** | No | **Yes** |
| **Data source scoped filter** | No | **Yes** |
| Filter group scoping across selected sheets | **Yes (`filter-group='3'`)** | No |
| **Highlight action** | **Yes (1)** | No |
| **Filter actions** | No | **Yes (6)** |
| Auto-generated phone layout | Yes (vscroll, 4450 px) | Yes (vscroll, 2400 px) |
| Sets, groups, hierarchies, maps, LODs, forecasting, clustering, trend lines | **None** | **None** |

## 8. Common techniques used in both

1. Single flat CSV read through the `textscan` connector.
2. Full extract to Hyper with `count='-1'` and no extract filter.
3. Field captions applied to rename source columns for display.
4. Measure to dimension role conversion on integer columns that should be categorical.
5. Binning of a continuous measure.
6. A constant measure placed twice on a shelf to create a **dual axis**, then two pie marks of different sizes to build a **donut**.
7. The built-in **Percent of Total** table calculation for wedge share.
8. Text/BAN style KPI presentation.
9. One quick filter exposed on the dashboard as a **dropdown**.
10. `on-select` actions with `auto-clear='true'`.
11. Custom worksheet titles with explicit font colour and size.
12. Auto-generated Phone device layout with `vscroll` sizing, and no Tablet layout.
13. **No** date field, therefore **no** time series in either.
14. **No** LODs, sets, hierarchies, maps, trend lines, forecasting or clustering in either.
15. **No** number formatting specified in either workbook.
16. Both published to Tableau Public from a Mac.

## 9. Unique techniques used in each

### Unique to Dashboard 1 (Heart Failure)

1. **Data source level value aliasing** on six fields, decoding 0/1 into clinical language once and inheriting it across 19 worksheets.
2. **Two dimensions on a single Colour shelf**, producing a crossed 4-way palette with explicit hex overrides.
3. **Seven parallel bins** giving a consistent distribution grammar across seven biomarkers.
4. **A reference line** with `formula='average'` and `scope='per-cell'`.
5. **Aggregate Measures switched off** on one worksheet to show individual records rather than aggregates.
6. **Continuous dimensions on both axes** of a scatter (`none:` derivation on two measures).
7. **Filter group scoping** (`filter-group='3'`) to apply one filter to a chosen subset of worksheets.
8. **A highlight action** scoped to the entire dashboard on a single named field.
9. **Fully tiled nested flow container** layout.
10. **String literal calculated fields** used as KPI captions.
11. A scale of repetition: 19 worksheets on one canvas.

### Unique to Dashboard 2 (HR Analytics)

1. **A parameter**, and a **parameter-driven bin size**, exposed as a dashboard slider.
2. **Conditional logic** (`IF/THEN/ELSE`) converting a text flag into a numeric indicator.
3. **Aggregate-over-aggregate calculations** producing a true rate and a derived headcount.
4. **A three-level calculation dependency chain.**
5. **Measure Names / Measure Values** to build five KPI tiles in one worksheet.
6. **Manual sort dictionaries** to force logical ordering of age bands and measure order.
7. **Continuous sequential colour ramps** (`blue_10_0`, `purple_10_0`, interpolated).
8. **Square marks** for a highlight table.
9. **A Bar plus Circle dual axis** to build a lollipop chart.
10. **A label placed on the secondary axis** to print a total inside a donut hole.
11. **Custom tooltips on every worksheet** with a consistent typographic system.
12. **Custom mark labels** combining a value and a percent in one string.
13. **Dynamic `<Sheet Name>` title tokens** instead of typed titles.
14. **Data source scoped filtering** via `<shared-view>`.
15. **Six filter actions** with `special-fields='all'`, making every chart a cross-filter.
16. **Floating layout over a background image** exported from PowerPoint.
17. **A text object** as a dashboard title.

## 10. Skills demonstrated by each dashboard

### Dashboard 1 demonstrates

- Semantic layer work: renaming, role management and value aliasing applied once at the data source so every view inherits it.
- Binning and distribution analysis across many variables with a repeated visual grammar.
- Dual-axis chart construction from first principles (donuts with no built-in mark type).
- Table calculations (percent of total).
- Analytics pane usage: a scoped average reference line.
- Aggregation control: knowing when to switch aggregation off to reveal spread.
- Filter scoping across a subset of worksheets.
- Highlight action design for linked reading across many views.
- Container-based dashboard layout that reflows.
- Discipline in applying one visual system across 19 views.

### Dashboard 2 demonstrates

- Metric definition: turning a raw text flag into a defined, documented business measure and building a rate and a derived headcount on top of it.
- Correct use of aggregate calculations so a ratio recomputes at any level of detail.
- Parameterisation: giving the end user control over analytical granularity, and understanding the downstream effect on an action filter.
- Efficient KPI construction with Measure Names and Measure Values.
- Sort control with explicit dictionaries.
- Colour theory in practice: sequential ramps for quantities, categorical for categories.
- A broader chart vocabulary, including lollipop and highlight table construction.
- Interaction design: six-way cross-filtering with correct filter scoping so the headline numbers move with the charts.
- Presentation design: background image, typographic system, custom tooltips on every view.
- Floating layout with precise object positioning.

---

# FINAL TECHNICAL INVENTORY

## Data

| Item | Dashboard 1 | Dashboard 2 | Combined |
|---|---|---|---|
| Data sources (`<datasource>` elements) | 1 | 5 | 6 |
| Real data connections | 1 | 4 | 5 |
| Data connections actually used | 1 | 1 | 2 |
| Tables | 1 | 4 (one per source) | 5 |
| Source files | `heart_failure_clinical_records_dataset.csv` | `HR_data.csv`, `HR data.csv`, `HR data.xlsx`, `HR Data.xlsx - HR data.csv` | 5 files |
| Connection classes | `textscan` | `textscan` x4, `excel-direct` x1 (declared, unbound) | 2 classes |
| Source columns | 13 | 39 per source | 52 distinct |
| Joins | 0 | 0 | **0** |
| Relationships | 0 | 0 | **0** |
| Unions | 0 | 0 | **0** |
| Blends | 0 | 0 | **0** |
| Custom SQL | 0 | 0 | **0** |
| Extracts | 1 | 4 | **5** |
| `.hyper` files shipped | 1 | 4 | 5 |
| Data source filters | 0 | 1 | 1 |
| Extract filters | 0 | 0 | 0 |

## Tableau

| Item | Dashboard 1 | Dashboard 2 | Combined |
|---|---|---|---|
| Worksheets | 19 | 7 | **26** |
| Worksheets placed on a dashboard | 19 | 7 | 26 |
| Orphaned worksheets | 0 | 0 | 0 |
| Dashboards | 1 | 1 | **2** |
| Stories | 0 | 0 | **0** |
| Calculated fields | 13 | 6 | **19** |
| of which bins | 7 | 1 | 8 |
| of which conditional | 0 | 1 | 1 |
| of which aggregate calcs | 0 | 2 | 2 |
| of which string literals | 5 | 0 | 5 |
| of which axis placeholders | 1 | 1 | 2 |
| of which auto-generated | 0 | 1 (`Number of Records`) | 1 |
| Parameters | 0 | 1 | **1** |
| Sets | 0 | 0 | **0** |
| Groups (user-created) | 0 | 0 | **0** |
| Groups (auto action groups, hidden) | 0 | 4 | 4 |
| Bins | 7 | 1 | **8** |
| Hierarchies / drill paths | 0 | 0 | **0** |
| Filters (distinct definitions) | 4 | 6 | **10** |
| Filter controls on dashboards | 1 | 1 | 2 |
| Parameter controls on dashboards | 0 | 1 | 1 |
| Colour legends on dashboards | 1 | 3 | 4 |
| Actions | 1 | 6 | **7** |
| of which highlight | 1 | 0 | 1 |
| of which filter | 0 | 6 | 6 |
| LOD expressions | 0 | 0 | **0** |
| Table calculations | `PctTotal` on 5 sheets | `PctTotal` on 2 sheets | 1 type, 7 sheets |
| Reference lines | 1 | 0 | 1 |
| Trend lines / forecasts / clusters / totals | 0 | 0 | **0** |
| Maps / geographic roles | 0 | 0 | **0** |
| Dual axis worksheets | 5 | 2 | 7 |
| Custom tooltips | 0 | 8 definitions across 7 sheets | 8 |
| Custom mark labels | 0 | 6 | 6 |
| Custom worksheet titles | 14 | 6 | 20 |
| Text objects | 0 | 1 | 1 |
| Image objects | 0 | 1 | 1 |
| Device layouts | 1 (Phone) | 1 (Phone) | 2 |
| Dashboard canvas size | 1900 x 1050, range | 1580 x 900, fixed | |
| Mark types used | Pie, Circle, Automatic | Pie, Bar, Circle, Square, Automatic | 5 distinct |
| Colour palettes named | `summer_10_0` | `blue_10_0`, `purple_10_0` | 3 |
| Explicit hex colour overrides | 6 mappings | 0 | 6 |
| Number format definitions | 0 | 0 | **0** |

## Business

| Item | Dashboard 1 | Dashboard 2 |
|---|---|---|
| **KPIs** | `Total Individuals`, `Total Deaths`, `Total Males`, `Total Females`, `Average Age` | `Employee Count`, `Attrition Count`, `Attrition Rate`, `Active Employees`, `AVG(Age)` |
| **Business questions addressed** (△ inferred from structure) | Which clinical and demographic attributes accompany mortality in a heart failure cohort? What is the cohort's size, sex balance and age profile? Where along each biomarker's range do deaths concentrate? | Where does attrition concentrate by department, education field, gender and age band? What is the attrition rate for any given slice? Which job roles cluster at low satisfaction? |
| **Dimensions analysed** | `Death Event`, `Sex`, `Anaemia`, `Diabetes`, `High Blood Pressure`, `Smoking`, plus 7 binned biomarkers | `Department`, `Education Field`, `Education`, `Gender`, `Job Role`, `Job Satisfaction`, `CF age band`, `Age (bin)` |
| **Measures analysed** | `Age`, `Creatinine Phosphokinase`, `Ejection Fraction`, `Platelets`, `Serum Creatinine`, `Serum Sodium`, `Time`, plus counts | `Employee Count`, `Attrition Count`, `Attrition Rate`, `Active Employees`, `Age` |
| **Intended users** (△ inferred) | Clinical analytics, population health, or an academic audience (the folder path is `UIC/Business Data Visualization`) | HR business partners, people analytics, HR leadership |
| **Business objectives** (△ inferred) | Descriptive profiling to identify which attributes merit formal statistical testing or predictive modelling | Descriptive and exploratory attrition analysis to target retention effort |
| **What neither dashboard does** | No prediction, no statistical testing, no significance measure, no trend over time, no target or benchmark, no forecast | Same |

---

# EVIDENCE & CONFIDENCE

## Section-by-section confidence

| Section | Dashboard 1 | Dashboard 2 |
|---|---|---|
| 1. Dashboard overview: names, versions, size, publish target | ✓ DIRECTLY VERIFIED | ✓ DIRECTLY VERIFIED |
| 1. Author / owner | ✗ NOT AVAILABLE (no author field). Only a macOS username in a file path, which is △ INFERRED evidence at best. | ✗ NOT AVAILABLE, same situation |
| 1. Purpose, business problem, audience, story | △ INFERRED from titles, encodings and filters. Nothing is stored. | △ INFERRED, except the title text `HR ANALYTICS DASHBOARD` which is ✓ VERIFIED |
| 2. Data source inventory | ✓ DIRECTLY VERIFIED | ✓ DIRECTLY VERIFIED. That three sources are unused is ✓ verified by absence from every worksheet. Why they exist is △ INFERRED. |
| 3. Data model | ✓ DIRECTLY VERIFIED (single table, nothing to model) | ✓ DIRECTLY VERIFIED |
| 4. Data preparation | ✓ DIRECTLY VERIFIED for every listed transformation. The reason for each is △ INFERRED. That the bin sizes are Tableau defaults is △ INFERRED from their non-round values. | ✓ DIRECTLY VERIFIED. That the `Name1` captions are collision artefacts is △ INFERRED from the naming pattern. That the `CF_` columns were derived upstream is △ INFERRED from the prefix convention. |
| 5. Field inventory | ✓ DIRECTLY VERIFIED including usage and non-usage | ✓ DIRECTLY VERIFIED including the 24 unused source columns |
| 6. Calculated fields, exact formulas | ✓ DIRECTLY VERIFIED, transcribed character for character | ✓ DIRECTLY VERIFIED, transcribed character for character including spacing |
| 7. Parameters | ✓ VERIFIED that there are none | ✓ DIRECTLY VERIFIED (type, range, granularity, default, binding, control mode) |
| 8. Filters | ✓ DIRECTLY VERIFIED including scope and member values | ✓ DIRECTLY VERIFIED including the persisted `R&D` state. The user-facing consequence of that state is △ INFERRED. |
| 9. KPIs | ✓ DIRECTLY VERIFIED for fields, expressions, filters and placement. Business meaning is △ INFERRED. | ✓ DIRECTLY VERIFIED. That `Employee Count` equals 1 per row is ✗ NOT VERIFIABLE from the workbook. |
| 10. Worksheet analysis | ✓ DIRECTLY VERIFIED for shelves, marks, encodings, filters, styles. Resolution of `mark class='Automatic'` to Bar is △ INFERRED. | Same |
| 11. Visualization breakdown | ✓ for fields, aggregations and filters. △ for "why this visualization was appropriate". | Same |
| 12. Dashboard layout | ✓ DIRECTLY VERIFIED, all coordinates transcribed from `<zone>` attributes | ✓ DIRECTLY VERIFIED. That the background PNG came from PowerPoint is △ INFERRED from the filename. |
| 13. Actions | ✓ DIRECTLY VERIFIED | ✓ DIRECTLY VERIFIED |
| 14. Tooltips | ✓ VERIFIED that there are none. Default tooltip content is △ INFERRED from the encodings. | ✓ DIRECTLY VERIFIED, full text transcribed |
| 15. Business logic | Mechanics ✓ VERIFIED. Problem framing, intent and decisions are △ INFERRED. | Same |
| 16. Insights, part A (encoded) | ✓ DIRECTLY VERIFIED | ✓ DIRECTLY VERIFIED |
| 16. Insights, part B (answerable questions) | △ INFERRED from what is encoded | △ INFERRED |
| 16. Insights, part C (actual findings) | ✗ NOT AVAILABLE. No data values were read. | ✗ NOT AVAILABLE |
| 17. Technical summary | ✓ DIRECTLY VERIFIED, assembled from verified parts | ✓ DIRECTLY VERIFIED |
| 18. Interview explanation | Built only from verified facts, with defects named | Same |
| 19. Resume bullets | Built only from verified facts. No metrics, counts or outcomes invented. | Same |

## Things that are NOT available from either workbook

| Item | Status |
|---|---|
| Row counts of either dataset | ✗ NOT AVAILABLE. Values are inside binary `.hyper` files and no Hyper reader is installed here. |
| Any actual data value, distribution, rate or correlation | ✗ NOT AVAILABLE |
| Author, owner, creator or last-modified-by | ✗ NOT AVAILABLE. No such field exists in either file. |
| Creation date, edit history, time spent | ✗ NOT AVAILABLE. Only archive member timestamps exist: Heart Failure `.twb` dated 26 March 2025, HR `.twb` dated 26 August 2025. Those are file system timestamps from the packaging, not authorship dates. |
| Written dashboard description, documentation or data dictionary | ✗ NOT AVAILABLE |
| Requirements, stakeholders, sign-off | ✗ NOT AVAILABLE |
| Whether the CSVs were cleaned before import | ✗ NOT AVAILABLE, except that the `CF_` columns in the HR file were clearly derived upstream |
| Live Tableau Public URLs and view counts | ✗ NOT AVAILABLE. `public.tableau.com` is blocked by this environment's network policy (`403 to CONNECT`). Only the workbook IDs are recoverable from the XML. |
| Rendered screenshots | ✗ NOT AVAILABLE. No Tableau runtime, no network access to the published views. |
| Data source ownership, refresh schedule, governance | ✗ NOT AVAILABLE. Both are static local files. |

---

# INFORMATION I SHOULD PROVIDE MANUALLY

These cannot be extracted from the workbooks but will materially strengthen how you explain the projects.

## About the data

1. **The origin of each dataset.** Where did `heart_failure_clinical_records_dataset.csv` and `HR_data.csv` come from? Public dataset, coursework supply, Kaggle, UCI, a company export? Name it, because a hiring manager will ask.
2. **The row count of each file.** This is the single most useful number missing from this documentation and you can read it in one line.
3. **Whether either CSV was cleaned outside Tableau**, and if so with what (Excel, Python, SQL) and what rules were applied.
4. **How the `CF_age band`, `CF_attrition label` and `CF_current Employee` columns in the HR file were derived**, and by whom. Were they already in the file you downloaded, or did you create them in an earlier Tableau workbook and export?
5. **What `Employee Count` actually contains.** If it is 1 for every row, say so, because it is the denominator of your only rate KPI.
6. **Whether `DEATH_EVENT` has any nulls**, since `CNT(DEATH_EVENT)` is your cohort-size KPI and it counts non-nulls.

## About the context

7. **Why you built each dashboard.** Coursework, a portfolio piece, a job application task, self-directed practice? The Heart Failure file sits in a `UIC/Business Data Visualization` folder, which suggests a course. Confirm it.
8. **Whether there was a brief, an assignment prompt or a stakeholder**, and what it asked for.
9. **Who, if anyone, reviewed or used either dashboard**, and what they said.
10. **Dates.** When did you start and finish each? The file timestamps are March 2025 and August 2025 but those are packaging dates, not work dates.
11. **How long each took**, roughly.

## About the decisions

12. **Why you chose these five KPIs in each dashboard**, and what you rejected. For the Heart Failure one in particular: why counts and not a mortality rate?
13. **Why you accepted Tableau's suggested bin sizes** in the Heart Failure workbook (4.48, 8.22, 0.772 and so on) instead of setting clinically meaningful ones.
14. **Why the Sex filter in the Heart Failure workbook excludes the KPI cards.** Deliberate, so the cards act as a constant baseline, or an oversight?
15. **Why the HR workbook has four data sources.** What did you try first, and why did you settle on `HR_data.csv`?
16. **Why the bottom HR chart is titled `Attrition Rate by Gender for Different Age Group`** when the measure on it is `Attrition Count` with a percent-of-total. Was the rate intended and then changed?
17. **Whether the `Department1`, `Gender1` and similar captions were intentional.** If they are collision artefacts, saying so yourself is far better than being asked.
18. **Whether the saved `R&D` selection in the HR workbook was deliberate.**
19. **Why you chose a highlight action in one dashboard and filter actions in the other.** This is a genuinely good design question and a strong answer will land well.
20. **Where the HR background image came from.** The filename says `HR background.pptx.png`, so did you design it in PowerPoint yourself?

## About the outcome

21. **The live Tableau Public URLs**, confirmed by you. The workbook IDs are `Healthcare-HeartFailure_17429983482570` and `HRAnalyticsDashboard_17561606616710`, but the live URLs need verifying.
22. **Any view counts, feedback, grades or reuse** either dashboard received.
23. **Screenshots of both dashboards as published**, since none could be captured here.
24. **Anything you changed after publishing**, and why.

## Interview-critical items

25. **One concrete insight you personally found** in each dataset while building. Not a number the dashboard computes, but something you noticed and acted on. Interviewers ask "what did you find?" and "the dashboard lets you find X" is a weaker answer than "I found X".
26. **What you would do differently now.** The defects listed in this documentation give you a ready-made honest answer; confirm which ones you agree with.
