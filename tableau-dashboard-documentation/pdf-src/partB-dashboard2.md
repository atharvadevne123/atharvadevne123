# PART B: HANDS-ON EVIDENCE BRIEF, DASHBOARD 2

Scoped to `HR Dashboard ` only. Structured for a hiring manager confirming hands-on experience.

**Evidence base.** The packaged workbook `HR Analytics Dashboard.twb`, parsed from its XML, plus a short set of answers the author gave directly. The two are kept clearly apart throughout. Where neither supplies an answer, the entry reads **"Not recorded"** and the question appears in section 12.

**Confirmed by the author, not by the file:**

| Item | Answer |
|---|---|
| Author | Atharva Devne |
| Why it was built | **Self-directed, for the author's own skill development.** Not a course, not a client, not an employer. |
| Dataset origin | **Kaggle** |
| Dataset public? | **Yes.** This resolves the only disclosure concern the file raised, since the workbook embeds full extracts and publishes to Tableau Public. |

**Scope note.** This is an individual Tableau dashboard build over one local flat file. It is not pipeline, warehouse or platform work, and this brief does not pretend otherwise. Sections 2, 4, 6, 8 and 10 are therefore short, and the reasons are stated rather than padded.

---

## 1. PROJECT CONTEXT

| Item | Detail |
|---|---|
| Business problem | No stated problem, but unlike Dashboard 1 this workbook does contain one piece of authored prose: a dashboard title text object reading **`HR ANALYTICS DASHBOARD`**. What the build addresses, read from its structure: `Attrition Count` is the measure behind 5 of the 7 worksheets and 4 of the 7 worksheet names contain "Attrition", so it is an **attrition concentration** view. Where do leavers cluster, by department, education field, gender and age band? |
| Who requested it | **Nobody.** Self-directed. |
| What decisions it supports | No external decision. The purpose was the author's own skill development. What it mechanically enables a reader to ask is in Part A section 16. |
| My role | Sole author and sole builder. Connection, extract, semantic layer, metric definition, parameter, 7 worksheets, dashboard layout, filter scoping, six actions, tooltip authoring, publication. |
| Who else was involved | Nobody. No collaborators, no reviewers. Every data source is `inline='true'` and every connection points at one local file on one machine. |
| Timeline | Not recorded. |
| Tool | Tableau Desktop, `source-build='2025.2.0 (20252.25.0514.2217)'`, `source-platform='mac'`, document format `version='18.1'`. |
| Current status | **Published to Tableau Public.** `repository-location` id `HRAnalyticsDashboard_17561606616710`, dashboard path `/workbooks/HRAnalyticsDashboard_17561606616710/HRDashboard`, derived from `?rev=1.0`, current `revision='1.1'`, so at least two publish revisions. Whether it is live right now could not be checked: the network policy in the documenting environment denied `public.tableau.com`. |

---

## 2. SOURCE SYSTEMS AND DATA INVENTORY

**There is no source system in the enterprise sense.** No database, no API, no SharePoint, no shared folder, no server. Local files on one Mac.

**Four data sources are declared. Only one is used.**

| # | Caption | Internal name | Connector | File | Status |
|---|---|---|---|---|---|
| 1 | `HR data (HR Data)` | `federated.0f0h03p1it3gvo176rhln1y1tx4v` | `textscan` (active), plus a declared but unbound `excel-direct` connection | `HR_data.csv` | **ACTIVE.** All 7 worksheets and the dashboard bind to it. |
| 2 | `HR Data.xlsx - HR data` | `federated.049m4yg1psanb61b4tu3001365fp` | `textscan` | `HR Data.xlsx - HR data.csv` | **UNUSED**, extract still present |
| 3 | `HR data` | `federated.1g91kqr1twrfkg14hluc71es07jw` | `textscan` | `HR data.csv` | **UNUSED**, extract still present |
| 4 | `HR data (2)` | `federated.1u260d51era62r18fltmd02kg202` | `textscan` | `HR data.xlsx` | **UNUSED**, extract still present |

Plus a fifth `<datasource>` named `Parameters` with `hasconnection='false'`, which is Tableau's container for the one parameter.

All four sit in `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` and **all four declare the identical 39-column schema**.

**Consequence for the packaged file:** all four have extracts enabled, which is why the archive carries **four** `.hyper` files of 196,608 bytes each, three of them dead weight.

**The unbound connection, transcribed exactly:** `class='excel-direct'`, `cleaning='no'`, `compat='no'`, `dataRefreshTime=''`, `filename='/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main/HR data.csv'`, `interpretationMode='0'`, `validate='no'`, `workgroup-auth-mode='as-is'`. That is the Excel connector pointed at a `.csv` path. It is declared but the `<relation>` binds to the `textscan` connection `textscan.0ry86yc0w1h17j1d0atub17ll83k` instead.

| Attribute | Value (active source) |
|---|---|
| Relation | `<relation name='HR_data.csv' table='[HR_data#csv]' type='table' />` |
| Schema | 39 columns, flat, no key declared |
| Columns consumed | **15 of 39** |
| Provenance | **Kaggle, public dataset.** Confirmed by the author. |
| Owner | Publicly available, no internal owner |
| Extract | `enabled='true'`, `count='-1'`, `units='records'`, with `<relation name='Extract' table='[Extract].[Extract]' type='table' />` under `<properties context='extract'>` |
| Data source filter | One, on `[Education]`, at `<shared-view>` scope |
| Legacy versus current | Not applicable. Four variants of one file, no history, no second system, no date column. |

### The 39 source columns

| # | Column | Type | | # | Column | Type |
|---|---|---|---|---|---|---|
| 0 | `Attrition` | string | | 20 | `Environment Satisfaction` | integer |
| 1 | `Business Travel` | string | | 21 | `Hourly Rate` | integer |
| 2 | `CF_age band` | string | | 22 | `Job Involvement` | integer |
| 3 | `CF_attrition label` | string | | 23 | `Job Level` | integer |
| 4 | `Department` | string | | 24 | `Job Satisfaction` | integer |
| 5 | `Education Field` | string | | 25 | `Monthly Income` | integer |
| 6 | `emp no` | string | | 26 | `Monthly Rate` | integer |
| 7 | `Employee Number` | integer | | 27 | `Num Companies Worked` | integer |
| 8 | `Gender` | string | | 28 | `Percent Salary Hike` | integer |
| 9 | `Job Role` | string | | 29 | `Performance Rating` | integer |
| 10 | `Marital Status` | string | | 30 | `Relationship Satisfaction` | integer |
| 11 | `Over Time` | string | | 31 | `Standard Hours` | integer |
| 12 | `Over18` | string | | 32 | `Stock Option Level` | integer |
| 13 | `Training Times Last Year` | integer | | 33 | `Total Working Years` | integer |
| 14 | `Age` | integer | | 34 | `Work Life Balance` | integer |
| 15 | `CF_current Employee` | integer | | 35 | `Years At Company` | integer |
| 16 | `Daily Rate` | integer | | 36 | `Years In Current Role` | integer |
| 17 | `Distance From Home` | integer | | 37 | `Years Since Last Promotion` | integer |
| 18 | `Education` | string | | 38 | `Years With Curr Manager` | integer |
| 19 | `Employee Count` | integer | | | | |

**Three columns arrive pre-derived.** `CF_age band`, `CF_attrition label` and `CF_current Employee` carry the `CF_` prefix Tableau uses when a calculated field is exported to a flat file. **They carry no calculation in this workbook**, so that derivation happened upstream. `CF_age band` is used directly on a shelf. How they were produced is **not recorded**.

**24 of the 39 columns are never used** on any shelf, filter or calculation: `Business Travel`, `Marital Status`, `Over Time`, `Over18`, `Training Times Last Year`, `Daily Rate`, `Distance From Home`, `Environment Satisfaction`, `Hourly Rate`, `Job Involvement`, `Job Level`, `Monthly Income`, `Monthly Rate`, `Num Companies Worked`, `Percent Salary Hike`, `Performance Rating`, `Relationship Satisfaction`, `Standard Hours`, `Stock Option Level`, `Total Working Years`, `Work Life Balance`, `Years At Company`, `Years In Current Role`, `Years Since Last Promotion`, `Years With Curr Manager`.

---

## 3. SOURCE-TO-TARGET MAPPING

| Target field | Source field | Transformation rule | Notes |
|---|---|---|---|
| `Attrition Count` | `Attrition` (string `Yes`/`No`) | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | **The only conditional logic in the workbook.** Converts text to a summable flag. |
| `Attrition Rate` | `Attrition Count`, `Employee Count` | `SUM([Calculation_231935388807032832])/SUM([Employee Count])` | Aggregate over aggregate, so it recomputes at the view's level of detail |
| `Active Employees` | `Employee Count`, `Attrition Count` | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` | **Spacing transcribed exactly as stored** |
| `Age (bin)` | `Age`, `[Age Parameter]` | `class='bin'`, `formula='[Age]'`, `peg='0'`, `decimals='0'`, `size-parameter='[Parameters].[Age Parameter]'` | **Bin width is parameter-driven, not fixed** |
| `Number of Records` | none | `1`, `user:auto-column='numrec'` | Auto-generated by Tableau, never used |
| `min(1)` | none | `min(1)`, ad hoc inside one worksheet | Dual-axis placeholder |
| `Department1` | `Department` | Caption only | Collision artefact, not a business rename |
| `Education1` | `Education` | Caption only | |
| `Education Field1` | `Education Field` | Caption only | |
| `Gender1` | `Gender` | Caption only | |
| `Job Role1` | `Job Role` | Caption only | |
| `Job Satisfaction1` | `Job Satisfaction` | Caption; role measure → dimension `ordinal`, `aggregation='Sum'` retained | |
| `Emp No` | `emp no` | Caption only | Declared, never used on a shelf |
| `Employee Number` | `Employee Number` | Role measure → dimension `ordinal` | Declared, never used on a shelf |
| `CF age band` | `CF_age band` | Caption only, underscore removed. **No derivation here.** | Used directly on Columns |
| `CF attrition label` | `CF_attrition label` | Caption only | Declared, never used |
| `CF current Employee` | `CF_current Employee` | Caption only | Declared, never used |
| `Employee Count` | `Employee Count` | **No override at all** | Used as `SUM([Employee Count])`, the denominator of the rate |

**Fields whose meaning differed between systems.** Not applicable, one system. The closest real analogue is **within** the workbook: `Department` carries a `Department1` caption and two auto action groups (`Action (Department)` and `Action (Department1)`) that both resolve to the same underlying `[Department]` level. That is a Tableau artefact of a data source replacement, not a cross-system semantic mismatch.

### Grain

| Object | Grain |
|---|---|
| Source | One row per employee. Inferred from the schema: two identifier columns plus an `Employee Count` column. |
| `KPI` | Whole filtered population |
| `Attrition by Gender` | One mark per gender |
| `Department wise Attrition` | One mark per department |
| `No. of Employee by Age Group` | One mark per age bin |
| `Job Satisfaction Rating` | One mark per job role x satisfaction score |
| `Education Field wise Attrition` | One mark per education field |
| `Attrition Rate by Gender for Different Age Group` | One mark per age band x gender |

**Grain mismatches: none.** Every target aggregates upward from a single-grain source. No join exists anywhere, so no fan-out and no double-counting risk.

---

## 4. DATA FLOW AND ARCHITECTURE

No orchestration tool, no staging layer, no warehouse, no lakehouse, no scheduler.

```
[0] UPSTREAM, OUTSIDE THIS WORKBOOK               TOOL: not recorded
    CF_age band, CF_attrition label, CF_current Employee already derived
        v
[1] Local files on a Mac                          TOOL: none, manual placement
    HR_data.csv (active)
    HR data.csv, HR data.xlsx, HR Data.xlsx - HR data.csv (imported, unused)
        v
[2] Tableau Desktop 2025.2.0, macOS               TOOL: Tableau Desktop
    textscan connector on HR_data.csv
    (an excel-direct connection is declared but not bound)
        v
[3] FOUR Tableau Hyper extracts, one per source   TOOL: Tableau Desktop
    all <extract enabled='true' count='-1' units='records'>
    3 of the 4 .hyper files are unreferenced
        v
[4] Semantic layer, inside the workbook           TOOL: Tableau Desktop
    10 captions, 2 role conversions, 1 parameter,
    1 parameter-driven bin, 5 calculated fields,
    1 data source scoped filter on [Education] via <shared-view>
        v
[5] 7 worksheets
        v
[6] Dashboard "HR Dashboard ", 1580 x 900 fixed,
    floating over Image/HR background.pptx.png    TOOL: the image, per its
                                                  filename, came from PowerPoint
        v
[7] Tableau Public
    HRAnalyticsDashboard_17561606616710 / HRDashboard, revision 1.1
```

| Stage | Where data lands |
|---|---|
| Source | Local file system |
| Staging | **None** |
| Warehouse / lakehouse | **None** |
| Curated files | Four Hyper extracts inside the packaged workbook, only one referenced |
| Serving | Tableau Public |

**Inherited or previous architecture:** not recorded. Two artefacts hint at prior work without evidencing an architecture: the three unused data sources, which show the same dataset imported more than once in different formats, and the three `CF_` columns, which show that some derivation happened before this workbook.

**Flow in boxes and arrows:** upstream derivation (unrecorded) → local delimited files → Tableau Desktop textscan connector → four Hyper extracts → semantic layer (captions, roles, parameter, parameter-driven bin, calculations, data source filter) → 7 worksheets → 1 dashboard over a background image → Tableau Public. Two side boxes feed the dashboard: "six filter actions" and "one parameter slider", and the parameter side box also feeds back into the semantic layer box, because it drives the bin definition.

---

## 5. DATA CONSOLIDATION, CLEANING AND STANDARDISATION

**No consolidation occurred.** Four data sources exist, which is the usual precondition for blending, but no worksheet references more than one. No join, no union, no blend, no linking field. The other three sources are simply inert.

### Every cleaning rule applied, all ten

| # | Rule | Exact definition | Fields affected | Layer | Why there |
|---|---|---|---|---|---|
| 1 | **Text flag to numeric indicator** | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | new `Attrition Count`, from `Attrition` | Calculated field | The source column is the string `Yes`/`No` and cannot be aggregated |
| 2 | Rate derivation | `SUM([Calculation_231935388807032832])/SUM([Employee Count])` | new `Attrition Rate` | Calculated field | Written as aggregate over aggregate so it recomputes at any level of detail |
| 3 | Complement derivation | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` | new `Active Employees` | Calculated field | |
| 4 | **Parameter-driven binning** | `class='bin'`, `formula='[Age]'`, `peg='0'`, `decimals='0'`, `size-parameter='[Parameters].[Age Parameter]'` | new `Age (bin)` | Calculated field bound to a parameter | Lets the viewer change granularity at view time rather than committing to one bucket width |
| 5 | Role reclassification | `role='dimension' type='ordinal'` | `Job Satisfaction`, `Employee Number` | Data source | A 1-to-4 satisfaction score is a category, not a quantity to sum |
| 6 | Display renaming | `caption` attribute | 10 fields | Data source | 6 of these are `Name1` collision artefacts rather than deliberate renames |
| 7 | **Global scope filtering** | `<shared-view>` filter on `[none:Education:nk]`, `function='level-members'`, `ui-enumeration='all'` | `Education` | Data source scope | Applies to every worksheet using the data source, including the KPI sheet |
| 8 | Presentation-layer label correction | Hand-typed labels inside `<customized-tooltip>` | `Department:`, `Gender:`, `Job Role:`, `Education Field:`, `Job Satisfaction:` | Worksheet | Corrects the `Name1` captions where the user actually sees them |
| 9 | **Explicit category ordering** | `<manual-sort column='[none:CF_age band:nk]' direction='ASC'>` with dictionary `"Under 25"`, `"25 - 34"`, `"35 - 44"`, `"45 - 54"`, `"Over 55"` | `CF_age band` | Worksheet | Alphabetical ordering would place `Over 55` in the middle |
| 10 | Explicit measure ordering | `<manual-sort column='[:Measure Names]' direction='ASC'>` with a 4-member dictionary | Measure Names on `KPI` | Worksheet | Pins KPI tile order |

### Cleaning rules NOT applied

| Rule category | Status |
|---|---|
| Null handling (`ISNULL`, `IFNULL`, `ZN`) | **Not present** |
| Duplicate detection or removal | **Not present** |
| Explicit type casting (`INT()`, `STR()`, `FLOAT()`, `DATE()`) | **Not present.** The `IF/THEN` changes the encoding but is not a cast function. |
| Date parsing, date parts, timezone handling | **Not present, and not possible.** No date column exists. `Years At Company`, `Years In Current Role`, `Years Since Last Promotion`, `Years With Curr Manager` and `Total Working Years` are integer tenure counts, not dates. |
| Text normalisation (`TRIM`, `UPPER`, `REPLACE`, `REGEXP`) | **Not present** |
| **Value aliases** | **Not present.** No `<aliases>` element anywhere. |
| Outlier detection or capping | **Not present** |
| Country, currency or unit standardisation | **Not present** |
| Domain classification logic | **Not present** in this workbook. It happened upstream in the `CF_` columns. |
| Referential validation | **Not present.** No joins to validate. |
| **Groups (user-created)** | **Not present.** The four `<group>` elements are auto-generated hidden action groups (`user:auto-column='sheet_link'`), not data groups. |
| Sets, hierarchies, drill paths | **Not present** |
| Extract filter | **Not present** |
| Tableau Prep flow | **Not present** in the archive |

### Which layer performed each transformation, and why there

All of it was done inside Tableau Desktop. No SQL, no Python, no Prep flow is referenced. The three `CF_` columns are the one piece of evidence that derivation happened before Tableau, but how is **not recorded**.

| Layer | What sits there | Why |
|---|---|---|
| Data source scope | Captions, role conversions, the `Education` shared-view filter | Inherited by every worksheet, including the KPI sheet |
| Calculated field scope | `Attrition Count`, `Attrition Rate`, `Active Employees`, `Age (bin)` | Reusable business metrics, and Tableau enforces the dependency chain |
| Worksheet scope | `min(1)` placeholder, two manual sorts, all tooltips and labels | Local to one view |
| Dashboard scope | Education dropdown, `Age Size` slider, six filter actions | Interaction, not data |

---

## 6. DATA MODEL: SCHEMA AND TABLE DESIGN

**No dimensional model was designed.** This is the single most important scope boundary to understand about this artefact.

| Design element | Status |
|---|---|
| Fact tables | **None** |
| Dimension tables | **None** |
| Star or snowflake schema | **None** |
| Surrogate key strategy | **None.** `Employee Number` and `emp no` exist as natural identifiers but are never used on any shelf, filter or calculation. |
| Slowly changing dimensions | **None** |
| Date dimension | **None, and impossible.** No date column exists. |
| Relationships and filter directions | **None.** Four single-table sources, never combined. |
| Historical migration or backfill | **None** |
| Cutover between systems | **Not applicable** |
| Cardinality and referential integrity settings | **Not applicable** |

### Design rules that WERE set, and the reason for each

| # | Rule | Evidence | Reason |
|---|---|---|---|
| 1 | Extract everything, filter nothing at extract time | `count='-1'` on all four sources, no extract filter | Keeps the workbook self-contained and keeps all filtering interactive |
| 2 | Embed the data source rather than publish it | `inline='true'` | Self-contained portfolio artefact |
| 3 | Ordinal scores are dimensions, not measures | `role='dimension' type='ordinal'` on `Job Satisfaction` and `Employee Number` | A 1-to-4 score is a category; an identifier should never be summed |
| 4 | **Define metrics as promoted calculated fields, not per-view expressions** | `Attrition Count`, `Attrition Rate`, `Active Employees` at data source level | One definition per business metric, reused across sheets |
| 5 | **Write ratios as aggregate over aggregate** | `SUM(...)/SUM(...)` | So the ratio recalculates correctly at any level of detail rather than averaging row-level ratios |
| 6 | **Make analytical granularity a user choice** | `size-parameter='[Parameters].[Age Parameter]'` | Avoids committing to one bucket width, and lets a viewer test whether a pattern survives re-bucketing |
| 7 | **Scope global filters at the data source** | `<shared-view>` filter on `[Education]` | Guarantees the KPI sheet responds, which a hand-picked per-sheet filter selection can miss |
| 8 | Bind dashboard titles to sheet names | `<Sheet Name>` token in 6 titles | Renaming a worksheet renames its dashboard title automatically |
| 9 | Sequential colour for quantities, categorical for categories | `blue_10_0` and `purple_10_0` interpolated ramps on `SUM(Employee Count)`; default categorical on `Gender` and `Department` | The encoding matches the data type |

---

## 7. BUSINESS RULES, VALIDATION AND GOVERNANCE

### Business rules encoded

Three, all real and all consequential.

| # | Rule | Exact definition | Consequence |
|---|---|---|---|
| 1 | **What counts as attrition** | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | Attrition is whatever the source column marks `Yes`. There is **no** voluntary versus involuntary split, **no** tenure qualification, **no** status exclusion and **no** date window. |
| 2 | **What counts as active** | `SUM([Employee Count])- SUM([Attrition Count])` | The population is a closed set: every employee is either active or a leaver. A snapshot, not a point-in-time headcount, because no hire or termination date exists. |
| 3 | **How attrition rate is defined** | `SUM([Attrition Count])/SUM([Employee Count])` | Leavers over total headcount in the current view scope. No annualisation, no average-headcount denominator. |

**Whether the source system's own definition of `Attrition = 'Yes'` includes involuntary exits: not recorded.**

### Validation checks

**None are present.** A complete absence, not an omission from this brief.

| Check type | Present? |
|---|---|
| Reconciliation to source | **No** |
| Row or control totals | **No** |
| Cross-system checks | Not applicable, one system |
| Step-change or regression checks | **No** |
| Data-quality flags shown to users | **No** |

Whether validation was performed outside Tableau is **not recorded**.

### Governance

| Item | Status |
|---|---|
| Metric definitions and data dictionary | **None** as a document. The calculated field names (`Attrition Count`, `Attrition Rate`, `Active Employees`) are self-describing, which is the closest thing present. |
| Sign-off process and owners | **None.** Self-directed work. |
| Decision log, open questions register, documentation | **None** |
| Version control | Tableau Public revision counters only: `revision='1.1'`, derived from `?rev=1.0`, so at least two publishes |
| Circumstantial repository marker | The source folder is named `HR-Analytics-Dashboard-Using-Tableau-main`. The `-main` suffix is what downloading a GitHub repository ZIP of a `main` branch produces, so a repository was involved somewhere in the project's history. Whose and for what: **not recorded**. |

### Defects observable in the delivered artefact

Found by reading the XML, not reported by anyone. All nine are **unfixed in the delivered file**.

| # | Defect | Evidence |
|---|---|---|
| 1 | Three of four data sources are unused but still carry extracts, adding three redundant `.hyper` files to the packaged archive | Archive listing plus worksheet dependencies |
| 2 | Six field captions are `Name1` collision artefacts (`Department1`, `Gender1`, `Job Role1`, `Education1`, `Education Field1`, `Job Satisfaction1`) | `caption` attributes. **Partly mitigated**: tooltips hand-type the clean labels, but legends still show the artefacts. |
| 3 | The worksheet titled `Attrition Rate by Gender for Different Age Group` **does not use the `Attrition Rate` field.** Its Angle shelf carries `SUM([Attrition Count])` and its labels carry a percent-of-total table calculation. | Shelf contents and tooltip text |
| 4 | **No number formatting** is defined, so `Attrition Rate` renders as a decimal rather than a percentage | No `number-format` attribute in the file |
| 5 | The workbook was saved with a `Department = "R&D"` mark selected, persisting an action filter into **6 of 7 worksheets** | `<groupfilter function='member' member='"R&amp;D"' user:ui-action-filter='[Action1]' />` |
| 6 | `Job Satisfaction Rating` has a continuous colour encoding but **no colour legend** on the dashboard | Dashboard zone list |
| 7 | `Education Field wise Attrition` has **no sort**, so bars appear in data source order rather than ranked | No `<sort>` or `<manual-sort>` on that sheet |
| 8 | The dashboard name carries a **trailing space**: `HR Dashboard ` | `<dashboard name='HR Dashboard '>` |
| 9 | The parameter has three different names in three places: internal `Age Parameter`, caption `Bin Size`, control title `Age Size` | Parameter definition and zone title |

**Defect 5 is the one to check before any demo.** The saved state carries a live R&D filter on six of seven views, so any number read off the dashboard in that state is an R&D number, not an organisation-wide number.

---

## 8. REFRESH, OPERATIONS AND SECURITY

| Item | Status |
|---|---|
| Refresh frequency | **Not recorded.** No schedule, no incremental configuration, no refresh definition exists. |
| Full or incremental | **Full, by construction.** All four extracts are `count='-1' units='records'` with no incremental refresh key and no extract filter. |
| Refresh trigger | Local file connections, so a refresh requires the file to be present on that Mac and a manual refresh to be run. `dataRefreshTime=''` on the one connection that declares the attribute. |
| How the source connects to Tableau | Direct local file read via the `textscan` connector, then extract. **No server, no gateway, no DSN, no connection string, no credentials, no DirectQuery equivalent.** The live-versus-extract choice is **extract**, on all four sources. |
| Credentials handling | `workgroup-auth-mode='as-is'` on every connection, the default for a file connection needing no authentication. No credential is stored. |
| Access control | Published to **Tableau Public**, public by default with no user-based access control. |
| Row-level security | **None.** No user filter, no `USERNAME()`, no `ISMEMBEROF()`, no user function appears anywhere. |
| Workspace administration | Not applicable. Tableau Public has no workspace model. |
| What data was allowed to leave the source | **No restriction, and none needed.** The workbook is packaged with full extracts embedded, so publishing it publishes the underlying records, downloadable by any viewer. **The dataset is a public Kaggle dataset**, confirmed by the author, so there is no disclosure issue. Worth stating explicitly: embedding a full extract in a public workbook would be a real problem with any non-public source, and knowing that distinction is the point. |
| Monitoring, failure handling, notification | **None.** No alert, subscription or notification is configured. |

---

## 9. REQUIREMENTS TO KPIs AND DASHBOARD LOGIC

### How requirements were gathered

**No requirements were gathered.** Self-directed work with no stakeholder, no brief and no session.

### KPI list

All five live in **one** worksheet, `KPI`, built with Measure Names and Measure Values.

| KPI | Business definition | Decision it supports | Grain | Source fields | Calculation logic | Owner | Sign-off |
|---|---|---|---|---|---|---|---|
| `Employee Count` | Headcount in the filtered population | Denominator context for everything else | Current filter scope | `Employee Count` | `SUM([Employee Count])` | Author | None, self-directed |
| `Attrition Count` | Number of leavers in the filtered population | Absolute attrition volume | Current filter scope | `Attrition` | `SUM(IF [Attrition] = 'Yes' THEN 1 ELSE 0 END)` | Author | None |
| `Attrition Rate` | Leavers divided by headcount | Whether attrition is high relative to population size, comparably across slices of different sizes | Current filter scope, recomputed at view level of detail | `Attrition`, `Employee Count` | `SUM([Attrition Count])/SUM([Employee Count])` | Author | None |
| `Active Employees` | Headcount remaining after attrition | Retained population | Current filter scope | `Employee Count`, `Attrition` | `SUM([Employee Count]) - SUM([Attrition Count])` | Author | None |
| `AVG(Age)` | Mean employee age | Flags whether a cross-filter has isolated an unusually young or old cohort | Current filter scope | `Age` | `AVG([Age])` | Author | None |

**All five respond** to the global Education filter and to all six cross-filter actions, because the filter is data source scoped.

The `KPI` sheet's Measure Names filter is a `function='union'` with `op='manual'` over five explicit members, in this stored order: `SUM(Employee Count)`, `SUM(Attrition Count)`, `Attrition Rate`, `Active Employees`, `AVG(Age)`. A separate manual-sort dictionary lists only the first four, so `AVG(Age)` sorts after them.

### Measures written, actual code

No DAX and no SQL exists. The Tableau code, transcribed exactly:

```
// Attrition Count
IF [Attrition] = 'Yes' THEN 1 ELSE 0 END

// Attrition Rate
SUM([Calculation_231935388807032832])/SUM([Employee Count])
// reads in the UI as:  SUM([Attrition Count])/SUM([Employee Count])

// Active Employees
SUM([Employee Count])- SUM([Calculation_231935388807032832])
// reads in the UI as:  SUM([Employee Count]) - SUM([Attrition Count])

// Number of Records  (auto-generated, unused)
1

// min(1)  (ad-hoc dual-axis placeholder)
min(1)

// Age (bin)  (a bin definition, not a formula)
class = bin, formula = [Age], peg = 0, decimals = 0,
size-parameter = [Parameters].[Age Parameter]

// Parameter
[Age Parameter], caption "Bin Size", real, param-domain-type = range,
value = 3.0, min = 2.0, max = 10.0, granularity = 1.0

// The one table calculation, applied on 2 sheets
<table-calc ordering-type='Rows' type='PctTotal' />
// surfaced in tooltips as: "% of Total Attrition Count along Table (Across)"
```

**There are no LOD expressions.** Verified by absence of `{` in every formula.

### Dependency chain

```
[Attrition]  (source column, string 'Yes'/'No')
      |
      v
Attrition Count  =  IF [Attrition] = 'Yes' THEN 1 ELSE 0 END
      |
      +----------------------------+
      v                            v
Attrition Rate                Active Employees
 = SUM([Attrition Count])      = SUM([Employee Count])
   / SUM([Employee Count])       - SUM([Attrition Count])
      |                            |
      v                            v
   KPI tile 3                   KPI tile 4

[Age] + [Age Parameter] "Bin Size" (2.0 to 10.0, step 1.0, current 3.0)
      |
      v
Age (bin)  -->  Columns shelf of "No. of Employee by Age Group"
```

### Dashboard design

| Item | Value |
|---|---|
| Pages | 1 dashboard, no story, no navigation |
| What it shows | Header with a title text object and the Education filter. KPI band with 5 tiles plus a gender lollipop. Middle band with a department pie, a parameterised age histogram and a job-role-by-satisfaction highlight table. Bottom band with an education field bar chart and a row of age band donuts split by gender. |
| Visuals used | Measure Names/Values KPI strip, lollipop (Bar + Circle dual axis), pie with percent of total, parameterised bar histogram with a sequential purple ramp, highlight table with Square marks and a sequential blue ramp, horizontal bar, donut small multiples with the band total printed in the hole |
| Filters shown to the user | 1 dropdown, `Education`, applied to all 7 sheets via data source scope |
| Parameter controls | 1 slider, `Age Size`, real, 2.0 to 10.0, step 1.0, default 3.0 |
| Drill paths | **None.** No hierarchy exists. Cross-filtering by clicking substitutes for drill-down. |
| How assumptions and definitions are shown to the user | **Partially.** Custom tooltips on all 7 sheets spell out field labels and name the table calculation explicitly as `% of Total Attrition Count along Table (Across)`. There is **no** definition of what `Attrition = 'Yes'` means and **no** assumptions panel. |
| Canvas | 1580 x 900, `sizing-mode='fixed'`, floating objects over `Image/HR background.pptx.png` |

### Interactivity

Six filter actions, one sourced from every worksheet except `KPI`, all `command='tsc:tsl-filter'`, all `on-select` with `auto-clear='true'`, all `special-fields='all'`, all targeting the whole dashboard. Every chart is a cross-filter surface and the KPI strip recomputes on every click.

**Anything the business explicitly asked for in the presentation:** nothing. There was no business.

---

## 10. STAKEHOLDER COORDINATION

**Nothing to report, and that is accurate rather than a gap in the evidence.** The project was solo and self-directed. There were no stakeholders, no meetings, no working sessions, no agreements, no pushback and no disagreements to handle. The workbook contains no name, comment, review or approval artefact of any kind.

---

## 11. OUTCOMES AND STATUS

| Item | Status |
|---|---|
| What is live | Published to Tableau Public, workbook id `HRAnalyticsDashboard_17561606616710`, dashboard repository id `HRDashboard`. Published at least twice (revision advanced `1.0` → `1.1`). Whether currently live could not be checked, the documenting environment's network policy denied `public.tableau.com`. |
| Completeness | **Complete build.** All 7 worksheets in the workbook are placed on the dashboard. No orphaned, unfinished or staged worksheets. |
| What is validated | **Nothing.** No validation artefact exists. |
| What is signed off | Not applicable, self-directed. |
| What is still open | The 9 defects in section 7, all unfixed. The three most consequential: the rate-versus-count title mismatch, the persisted `R&D` selection, and the absence of percentage formatting on the one rate KPI. |

### Measurable results

**None can be claimed.** No view count, adoption figure, time saving, grade, feedback or business outcome exists. No data values were read either, because the `.hyper` extracts are binary and no Hyper reader was available, so no headcount, attrition rate or departmental ranking can be stated.

What can be counted, and only this:

| Metric | Value |
|---|---|
| Worksheets built | 7 |
| Worksheets placed on the dashboard | 7 of 7 |
| Calculated fields authored | 6 |
| Parameters authored | 1 |
| Calculation dependency depth | 3 levels |
| Source columns consumed | 15 of 39 |
| Distinct chart forms | 7 |
| Dual-axis constructions | 2 |
| Table calculations | 1 type, on 2 sheets |
| Manual sort dictionaries | 2 |
| Dashboard actions | 6 |
| Custom tooltip definitions | 8, across 7 worksheets |
| Custom mark label definitions | 6 |
| Colour legends on the dashboard | 3 |
| Publish revisions | at least 2 |

### Lessons learned

Not recorded in the workbook. The defect list in section 7 is an external reading of the file.

---

## 12. GAPS AND QUESTIONS

### Already answered

| Question | Answer |
|---|---|
| Was this for a course, a client, or self-directed? | **Self-directed, for your own development.** |
| Where did the dataset come from? | **Kaggle.** |
| Is the dataset public, given the embedded extracts? | **Yes, public. No disclosure issue.** |

### Still open

1. **How were the `CF_age band`, `CF_attrition label` and `CF_current Employee` columns derived, and by whom?** Were they already in the file you downloaded, or did you create them in an earlier Tableau workbook and export?
2. **What does `Employee Count` actually contain?** If it is 1 on every row, confirm it, because it is the denominator of your only rate KPI.
3. **Was the CSV cleaned before it reached Tableau?** If yes, with what tool and what exact rules?
4. **Does the source define `Attrition = 'Yes'` to include involuntary exits?**
5. **Why does the workbook have four data sources?** What did you try first, and why did `HR_data.csv` win?
6. **Was the bottom chart originally intended to show `Attrition Rate`** and then changed to `Attrition Count`, or was the title always approximate?
7. **Were the `Department1`, `Gender1`, `Job Role1` captions intentional**, or collision artefacts from replacing a data source?
8. **Was the saved `R&D` selection deliberate?**
9. **Why six filter actions rather than a highlight action?** A strong answer on the difference lands well.
10. **Where did `HR background.pptx.png` come from?** The filename says PowerPoint. Did you design it?
11. **Did anyone review or use it**, and what did they say?
12. **The confirmed live Tableau Public URL.** The recoverable id is `HRAnalyticsDashboard_17561606616710`.
13. **Any view counts or feedback?**
14. **What changed between the two publish revisions?**
15. **One concrete insight you personally found** in this dataset while building. Not a figure the dashboard computes, but something you noticed.
16. **Which of the 9 defects do you agree with**, and does any have an explanation this reading has missed?

---

## 13. SANITISED VERSION

The same brief with identifying details replaced. All technical detail, counts, rules and logic unchanged.

**1. Project context.** Self-directed work by a single author for their own skill development, not for a course, client or employer. No requester, no stakeholder, no collaborators. Subject matter: workforce attrition analysis, evidenced by an attrition measure behind 5 of 7 worksheets and 4 of 7 worksheet names containing "Attrition". The workbook contains one piece of authored prose, a dashboard title text object. BI tool version 2025.2.0 on a workstation. Published to a public visualisation hosting platform, at least twice.

**2. Source systems and data inventory.** No enterprise source system. Four data sources declared, all pointing at the same folder on one workstation and all declaring the identical 39-column schema, plus a fifth parameter container with no connection. Only one is used; the other three are inert but still carry their own extracts, which is why the packaged archive holds four in-memory extract files of which three are dead weight. The active source declares two connections, a delimited text connection that the relation binds to and a spreadsheet connection that it does not, the latter with `cleaning='no'`, `compat='no'`, `interpretationMode='0'`, `validate='no'`. Provenance: a public dataset from a public data-sharing platform. Schema covers an attrition flag, headcount, organisational unit, education field and level, gender, job role, five satisfaction and involvement scores, seven compensation and rate columns, five tenure columns, employee identifiers and demographics. Three columns arrive pre-derived carrying the tool's exported-calculated-field prefix, with no calculation in this workbook, so that derivation happened upstream by means not recorded. 15 of 39 columns are consumed; the other 24 are named in full in the unsanitised section 2.

**3. Source-to-target mapping.** Nineteen target fields mapped, covering one conditional indicator, one aggregate ratio, one aggregate difference, one parameter-bound bin, one auto-generated constant, one dual-axis placeholder, six captioned dimensions (all six captions being collision artefacts), two role-converted identifiers and scores, three pre-derived columns consumed as-is, and one headcount column used with no override at all. No cross-system semantic mismatch existed; the closest analogue is an internal one where a single underlying field carries a duplicate caption and two auto action groups after a data source replacement. Source grain is one row per employee; target grains range from whole-population to one mark per age band and gender. No grain mismatches, because no join exists.

**4. Data flow.** Upstream derivation (unrecorded) → local delimited files → BI desktop tool, delimited text connector → four columnar in-memory extracts, all records, no filter → semantic layer (captions, roles, parameter, parameter-driven bin, calculations, data-source-scoped filter) → 7 worksheets → one dashboard over a background image → public hosting platform. No staging, no warehouse, no lakehouse, no scheduler, no SQL step, no scripting step, no ETL tool. Two side boxes feed the dashboard, six filter actions and one parameter slider, and the parameter also feeds back into the semantic layer because it drives the bin.

**5. Cleaning and standardisation.** No consolidation: four sources exist but no worksheet references more than one, so no join, union, blend or linking field. Ten rules, transcribed in full in the unsanitised section 5: text flag to numeric indicator; rate derivation as aggregate over aggregate; complement derivation; parameter-driven binning; role reclassification on two columns; display renaming on ten fields; global scope filtering via a shared-view filter; presentation-layer label correction inside every custom tooltip; explicit category ordering via a manual sort dictionary running from the youngest band to the oldest; and explicit measure ordering. Not applied: null handling, duplicate detection, explicit type casting, date parsing or timezone handling (impossible, no date column), text normalisation, value aliases, outlier treatment, unit or code standardisation, domain classification in this workbook, referential validation, user-created groups, sets, hierarchies, extract filter, external preparation flow. All work was done inside the BI tool across four deliberate layers.

**6. Data model.** No dimensional model. No fact or dimension tables, no surrogate keys (two natural identifiers exist but are never used), no slowly changing dimensions, no date dimension (impossible), no relationships, no migration, no cutover. Nine design rules were set and are listed with reasons, including defining metrics as promoted calculated fields, writing ratios as aggregate over aggregate, making analytical granularity a user choice, scoping global filters at the data source, binding dashboard titles to sheet names, and matching colour encoding to data type.

**7. Business rules, validation, governance.** Three business rules, all consequential: what counts as attrition (a single text-equality test, with no voluntary versus involuntary split, no tenure qualification, no status exclusion and no date window); what counts as active (headcount minus leavers, a snapshot rather than a point-in-time figure because no hire or termination date exists); and how the rate is defined (leavers over headcount in the current view scope, with no annualisation and no average-headcount denominator). No validation checks of any kind. No data dictionary, sign-off, decision log or documentation; version control limited to publish revision counters, with a folder-name suffix indicating a repository was involved somewhere. Nine defects are verifiable and unfixed: three unused data sources carrying extracts; six collision-artefact captions; a worksheet titled as a rate that plots a count; no number formatting, so the rate renders as a decimal; a persisted mark selection saved into six of seven worksheets; a continuous colour encoding with no legend exposed; an unsorted bar chart; a dashboard name with a trailing space; and a parameter carrying three different names in three places.

**8. Refresh, operations, security.** Refresh frequency not recorded. Full by construction on all four extracts. Direct local file read then extract, with no server, gateway, DSN, connection string, credentials or direct-query equivalent. Authentication mode is the default for a file connection needing none. Published to a public-by-default platform with no user-based access control and no row-level security; no user function appears anywhere. The workbook embeds full extracts, so publishing it publishes the records, but the dataset is public so there is no disclosure issue. No monitoring, failure handling or notification.

**9. Requirements to KPIs.** No requirements were gathered; the work was self-directed. Five KPIs in a single worksheet built with the tool's measure-name and measure-value constructs: headcount as a sum; leaver count as a sum of the conditional indicator; a rate as the aggregate ratio; active headcount as the aggregate difference; and a mean age. All five respond to the global filter and to all six cross-filter actions. No DAX and no SQL; the actual code is one conditional indicator, one aggregate ratio, one aggregate difference, one auto-generated constant, one dual-axis placeholder, one parameter-bound bin definition, one range parameter and one built-in percent-of-total table calculation, all transcribed unchanged in the full section 9. The dependency chain runs three levels deep from a source text column. No level-of-detail expressions. Dashboard: one page on a 1580 x 900 fixed canvas with floating objects over a background image, a header with a title object and the global filter, a KPI band of five tiles plus a gender lollipop, a middle band with an organisational-unit pie, a parameterised age histogram and a role-by-satisfaction highlight table, and a bottom band with an education field bar chart and a row of age band donuts. One dropdown on all seven sheets, one slider parameter ranging 2.0 to 10.0 by 1.0 defaulting to 3.0, no drill paths, and six on-select auto-clear filter actions passing all fields. Assumptions are partially shown: every worksheet carries a hand-written tooltip and the table calculation is named explicitly, but the attrition rule itself is never defined to the user.

**10. Stakeholder coordination.** None. Solo, self-directed work with no stakeholders, meetings, agreements or disagreements.

**11. Outcomes and status.** Published at least twice. Complete build: all 7 worksheets placed on the dashboard, none orphaned. Nothing validated, nothing signed off, nine defects still open. No measurable results can be claimed and no data values were read. Countable facts: 7 worksheets, 6 calculated fields, 1 parameter, a 3-level dependency chain, 15 of 39 source columns consumed, 7 distinct chart forms, 2 dual-axis constructions, 1 table calculation type on 2 sheets, 2 manual sort dictionaries, 6 dashboard actions, 8 custom tooltip definitions, 6 custom label definitions, 3 colour legends, at least 2 publish revisions.

**12. Gaps and questions.** Three answered (self-directed, public data-sharing platform origin, dataset is public). Sixteen still open, listed in full in the unsanitised section 12.

### Substitution list

| # | Original | Replaced with |
|---|---|---|
| 1 | `Tableau`, `Tableau Desktop`, `Tableau Public` | "BI desktop tool", "public visualisation hosting platform" |
| 2 | `Hyper`, `.hyper` | "columnar in-memory extract" |
| 3 | `textscan` connector | "delimited text connector" |
| 4 | `excel-direct` connector | "spreadsheet connector" |
| 5 | `Measure Names`, `Measure Values` | "the tool's measure-name and measure-value constructs" |
| 6 | `Atharva Devne` | "a single author" / "the author" |
| 7 | `atharvadevne` (account name in file paths) | omitted |
| 8 | `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` | "the same folder on one workstation"; the `-main` suffix described as "a folder-name suffix indicating a repository was involved" |
| 9 | `Kaggle` | "a public data-sharing platform" |
| 10 | `HR Analytics Dashboard.twb` | "the workbook" |
| 11 | `HR_data.csv`, `HR data.csv`, `HR data.xlsx`, `HR Data.xlsx - HR data.csv` | "four files of the same dataset in different formats and naming conventions" |
| 12 | `HRAnalyticsDashboard_17561606616710`, `HRDashboard` | omitted |
| 13 | `public.tableau.com` | "the host" |
| 14 | `HR Dashboard ` (dashboard name) | "the dashboard"; the trailing-space defect described without reproducing the name |
| 15 | `Image/HR background.pptx.png` | "a background image"; PowerPoint described as "a presentation tool" |
| 16 | `Department`, `Department1` | "organisational unit" |
| 17 | `Education`, `Education1` | "education level" |
| 18 | `Education Field`, `Education Field1` | "education field" |
| 19 | `Job Satisfaction`, `Job Satisfaction1` | "satisfaction score" |
| 20 | `Attrition` | "attrition flag" |
| 21 | `Employee Count` | "headcount column" |
| 22 | `Employee Number`, `emp no` | "employee identifiers" |
| 23 | `CF_age band`, `CF_attrition label`, `CF_current Employee` | "three pre-derived columns" |
| 24 | `R&D` (the persisted selection member) | "a persisted mark selection" |
| 25 | `"Under 25"` through `"Over 55"` (sort dictionary) | "running from the youngest band to the oldest" |
| 26 | Federated data source ids (`federated.0f0h03p1it3gvo176rhln1y1tx4v` and so on) | omitted |
| 27 | Internal calculation ids (`[Calculation_231935388807032832]` and so on) | replaced with the readable field name |
| 28 | Dashboard UUID `{30867C40-EA91-4DA5-AF47-E92ACECA09BD}` | omitted |
| 29 | Extract filenames (`#TableauTemp_0uykjkf...` and so on) | omitted |
| 30 | Worksheet names | described by chart type and content |
| 31 | Palette names `blue_10_0`, `purple_10_0` | "sequential ramps" |
| 32 | `macOS` | "workstation" |

**Not substituted, deliberately:** all formulas, the parameter range and granularity, canvas dimensions, zone counts, filter scopes, action counts, worksheet counts, column counts and dependency depth, because the instruction was to keep technical detail, counts, rules and logic unchanged.

**One item to check yourself:** the sanitised version still states the subject is workforce attrition. If the subject matter itself is sensitive, replace it with something like "a workforce dataset".
