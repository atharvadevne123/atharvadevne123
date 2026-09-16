# HANDS-ON EVIDENCE BRIEF

**Purpose:** a structured, verifiable account of what was actually built, for a hiring manager confirming hands-on experience.

**Evidence base:** this conversation contains exactly two artefacts, the packaged Tableau workbooks `Healthcare - Heart Failure.twb` and `HR Analytics Dashboard.twb`, plus a short set of answers the author gave directly. Everything below is drawn from the workbook XML or from those stated answers, and the two are kept clearly apart. **Nothing is inferred from typical practice.** Where the evidence does not exist, the entry reads **"Not in chats"** and the corresponding question appears in section 12.

**Confirmed by the author, not by the files:**

| Item | Answer |
|---|---|
| Why both projects were built | **Self-directed. For the author's own skill development.** Not a course, not a client, not an employer. |
| Where both datasets came from | **Kaggle.** |
| Whether the heart failure dataset is public | **Yes, it is public.** This resolves the only disclosure concern the files raised, since both workbooks embed full extracts and publish to Tableau Public. |

**Important framing note.** This template is designed for a multi-system data engineering engagement with stakeholders, source systems, warehouses and refresh schedules. The artefacts supplied are two self-contained single-file Tableau workbooks. Large parts of sections 1, 2, 4, 7, 8, 10 and 11 therefore have no evidence, and saying so is more useful than filling them in. A hiring manager reading this should understand the scope accurately: these are **individual Tableau dashboard builds over local flat files**, not pipeline or platform work.

---

## 1. PROJECT CONTEXT

### Business problem

| Item | Evidence |
|---|---|
| Stated business problem | **Not in chats.** Neither workbook contains a description, annotation, caption or documentation field. |
| Only authored text in either workbook | One dashboard text object reading `HR ANALYTICS DASHBOARD`. That is the entirety of the authored prose across both files. |
| Inferable subject matter, Workbook 1 | Heart failure patient survival profiling. 12 of 14 chart titles end in `- Survival Stats`, and `Death Event` is on the Colour shelf of every chart. |
| Inferable subject matter, Workbook 2 | Employee attrition analysis. `Attrition Count` is the measure behind 5 of 7 worksheets, and 4 of 7 worksheet names contain "Attrition". |

### Who requested the work

**Nobody. Both projects were self-directed**, confirmed by the author. There was no requester, sponsor, client or stakeholder, and none is named anywhere in either file.

Note on a misleading path: Workbook 1's source file lives at `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction`. That folder name looks like coursework, but the author has confirmed it is not. The file simply sat there.

### What decisions the outputs support

**No external decision.** Both were built for the author's own skill development, so the "decision supported" is the author's own learning rather than a business decision. What the dashboards mechanically enable a reader to ask is documented in `01-dashboard1-heart-failure.md` section 16 and `02-dashboard2-hr-analytics.md` section 16.

### My role and responsibilities

| Item | Evidence |
|---|---|
| Role title | Sole author and sole builder, self-directed. Confirmed by the author. No author field exists in either workbook. |
| Only identity marker | The macOS account name `atharvadevne` appears in file paths in both workbooks: `/Users/atharvadevne/UIC/...` and `/Users/atharvadevne/Desktop/...`. This is a path string, not an authorship field. |
| Scope of work evidenced | Both workbooks are **single-author artefacts with no shared or published data source, no server connection and no collaboration markers**. Every data source is `inline='true'`, meaning embedded in the workbook rather than published to a server. Every connection points at a local file on one machine. |
| Responsibilities that can be evidenced from the files | Data connection, extract configuration, semantic layer definition (captions, roles, aliases), calculated field authoring, parameter creation, worksheet construction, chart formatting, dashboard layout, filter scoping, action configuration, tooltip authoring, publication to Tableau Public. |

### Who else was involved

**Nobody.** Both projects were solo and self-directed. No collaborators, no reviewers, and nothing in either workbook identifies a second person.

### Timeline

| Item | Evidence |
|---|---|
| Start and completion dates | **Not recorded here.** |
| Tableau build used, Workbook 1 | `source-build='2025.1.0 (20251.25.0313.2002)'`, build comment `20243.25.0110.1701`. The `20251.25.0313` component dates that build to 13 March 2025. |
| Tableau build used, Workbook 2 | `source-build='2025.2.0 (20252.25.0514.2217)'`, build comment `20252.25.0723.1135`. The `20252.25.0514` component dates that build to 14 May 2025 and the comment build to 23 July 2025. |
| Revision numbers | Workbook 1: `repository-location revision='1.2'`, derived from `?rev=1.1`, so **at least two publish revisions**. Workbook 2: `revision='1.1'`, derived from `?rev=1.0`, so **at least two publish revisions**. |
| Milestones | **Not in chats.** No milestone, phase or version history beyond the revision counters. |
| Current status | **Both are published.** Each workbook carries a `repository-location` pointing at `public.tableau.com`, which Tableau writes on publish. Workbook 1 to `Healthcare-HeartFailure_17429983482570`, Workbook 2 to `HRAnalyticsDashboard_17561606616710` with dashboard path `HRDashboard`. Whether the published views are currently live could not be checked, because this environment's network policy returned `403 to CONNECT` for `public.tableau.com:443`. |

---

## 2. SOURCE SYSTEMS AND DATA INVENTORY

**There are no source systems in the enterprise sense.** No database, no API, no SharePoint site, no shared folder, no server. Every connection in both workbooks is to a **local file on one Mac**. This is stated plainly rather than dressed up.

### Workbook 1: Healthcare - Heart Failure

| Attribute | Value |
|---|---|
| System | Local file system |
| Connector class | `textscan` (Tableau's delimited text file connector) |
| File | `heart_failure_clinical_records_dataset.csv` |
| Path | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` |
| Named connection id | `textscan.0eo7kao1bn80dv0zsqdco0t9bxql` |
| Parsing configuration | `character-set='UTF-8'`, `separator=','`, `header='yes'`, `locale='en_US'` |
| Relation | `<relation name='heart_failure_clinical_records_dataset.csv' table='[heart_failure_clinical_records_dataset#csv]' type='table' />` |
| Schema | 13 columns, flat, no key declared |
| Provenance | **Kaggle, public dataset.** Confirmed by the author. |
| Access method | Direct file read, then full extract |
| Owner | Publicly available dataset, no internal owner. |
| Legacy versus current | Not applicable, one file |

**Schema, exact column names, types and ordinals:**

| Ordinal | Column | Declared datatype | Tableau `remote-type` |
|---|---|---|---|
| 0 | `age` | real | 5 |
| 1 | `anaemia` | integer | 20 |
| 2 | `creatinine_phosphokinase` | integer | 20 |
| 3 | `diabetes` | integer | 20 |
| 4 | `ejection_fraction` | integer | 20 |
| 5 | `high_blood_pressure` | integer | 20 |
| 6 | `platelets` | real | 5 |
| 7 | `serum_creatinine` | real | 5 |
| 8 | `serum_sodium` | integer | 20 |
| 9 | `sex` | integer | 20 |
| 10 | `smoking` | integer | 20 |
| 11 | `time` | integer | 20 |
| 12 | `DEATH_EVENT` | integer | 20 |

Every column's metadata record carries `<contains-null>true</contains-null>` and a shared `object-id` of `[heart_failure_clinical_records_dataset.csv_6F1533318D5F4C8AB71453465976CF29]`. Note that `contains-null='true'` is Tableau's default optimistic flag on a scanned text file and is **not** evidence that nulls exist.

### Workbook 2: HR Analytics, four connections

| # | Data source caption | Connector | File | Status |
|---|---|---|---|---|
| 1 | `HR data (HR Data)` (`federated.0f0h03p1it3gvo176rhln1y1tx4v`) | `textscan` (active), plus a declared but unbound `excel-direct` connection | `HR_data.csv` | **ACTIVE.** All 7 worksheets and the dashboard bind to it. |
| 2 | `HR Data.xlsx - HR data` (`federated.049m4yg1psanb61b4tu3001365fp`) | `textscan` | `HR Data.xlsx - HR data.csv` | **UNUSED**, extract still present |
| 3 | `HR data` (`federated.1g91kqr1twrfkg14hluc71es07jw`) | `textscan` | `HR data.csv` | **UNUSED**, extract still present |
| 4 | `HR data (2)` (`federated.1u260d51era62r18fltmd02kg202`) | `textscan` | `HR data.xlsx` | **UNUSED**, extract still present |

All four sit in `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` and **all four declare the identical 39-column schema**.

The unbound connection on the active source, transcribed exactly:
`class='excel-direct'`, `cleaning='no'`, `compat='no'`, `dataRefreshTime=''`, `filename='/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main/HR data.csv'`, `interpretationMode='0'`, `validate='no'`, `workgroup-auth-mode='as-is'`. It is declared but the `<relation>` binds to the `textscan` connection `textscan.0ry86yc0w1h17j1d0atub17ll83k` on `HR_data.csv`.

**Why four data sources exist: Not in chats.** The four differing filenames and formats for one dataset are consistent with repeated import attempts, but the workbook does not record intent.

**Full 39-column schema** is transcribed in `02-dashboard2-hr-analytics.md` section 2.3.

**Three columns arrive pre-derived:** `CF_age band` (string), `CF_attrition label` (string), `CF_current Employee` (integer). The `CF_` prefix is the convention Tableau uses when a calculated field is exported to a flat file. **They carry no calculation in this workbook**, so whatever derived them happened upstream. The upstream step itself is **Not in chats**.

**Provenance: Kaggle, public dataset**, confirmed by the author. No internal owner for any of the four.

**Legacy versus current systems, and how history is split: Not applicable.** There is no history, no cutover and no second system. Neither dataset contains a date field of any kind, so no temporal split exists to describe.

---

## 3. SOURCE-TO-TARGET MAPPING

### Workbook 1 mapping

| Target field (as used in a view) | Source system | Source field | Transformation rule | Notes |
|---|---|---|---|---|
| `Age` | `heart_failure_clinical_records_dataset.csv` | `age` | Caption rename only. Type `real`, role measure. | Used as `AVG` on the KPI, `CNT` on the histogram, unaggregated on the scatter |
| `Death Event` | same | `DEATH_EVENT` | Caption rename; role changed measure → dimension, type `ordinal`; value alias `0` → `Surivive`, `1` → `Death` | **The alias string is literally `Surivive`, a typo for "Survive", and it renders that way** |
| `Anaemia` | same | `anaemia` | Caption rename; role → dimension ordinal; alias `0` → `Negative`, `1` → `Positive` | |
| `Diabetes` | same | `diabetes` | Caption rename; role → dimension ordinal; alias `0` → `Negative`, `1` → `Positive` | |
| `High Blood Pressure` | same | `high_blood_pressure` | Caption rename; role → dimension ordinal; alias `0` → `Negative`, `1` → `Positive` | |
| `Sex` | same | `sex` | Caption rename; role → dimension ordinal; alias `0` → `Female`, `1` → `Male` | |
| `Smoking` | same | `smoking` | Caption rename; role → dimension ordinal; alias `0` → `` ` Non-Smoker` ``, `1` → `Smoker` | **The `Non-Smoker` alias has a leading space** |
| `Creatinine Phosphokinase` | same | `creatinine_phosphokinase` | Caption rename only | |
| `Ejection Fraction` | same | `ejection_fraction` | Caption rename only | |
| `Platelets` | same | `platelets` | Caption rename only | |
| `Serum Creatinine` | same | `serum_creatinine` | Caption rename only | |
| `Serum Sodium` | same | `serum_sodium` | Caption rename only | |
| `Time` | same | `time` | Caption rename only | Integer follow-up period, **not a date** |
| `Age (bin)` | derived | `age` | `<calculation class='bin' formula='[age]' size='4.48' peg='0' decimals='0' />` | |
| `Creatinine Phosphokinase (bin)` | derived | `creatinine_phosphokinase` | bin, `size='376'`, `peg='0'`, `decimals='2'` | |
| `Ejection Fraction (bin)` | derived | `ejection_fraction` | bin, `size='8.22'`, `peg='0'`, `decimals='0'` | |
| `Platelets (bin)` | derived | `platelets` | bin, `size='41767'`, `peg='0'`, `decimals='4'` | |
| `Serum Creatinine (bin)` | derived | `serum_creatinine` | bin, `size='0.772'`, `peg='0'`, `decimals='-1'` | |
| `Serum Sodium (bin)` | derived | `serum_sodium` | bin, `size='3.57'`, `peg='0'`, `decimals='0'` | |
| `Time (bin)` | derived | `time` | bin, `size='15.1'`, `peg='0'`, `decimals='1'` | |
| `Total Individuals` (caption) | derived | none | `"Total Individuals"` | String literal |
| `Total Deaths` (caption) | derived | none | `"Total Deaths"` | String literal |
| `Total Males` (caption) | derived | none | `"Total Males"` | String literal |
| `Total Females` (caption) | derived | none | `"Total Females"` | String literal |
| `Average Age` (caption) | derived | none | `"Average Age"` | String literal |
| `0` | derived | none | `0` | Dual-axis placeholder |

### Workbook 2 mapping

| Target field | Source system | Source field | Transformation rule | Notes |
|---|---|---|---|---|
| `Attrition Count` | `HR_data.csv` | `Attrition` (string) | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | **The only conditional logic across both workbooks.** Converts text to a summable flag. |
| `Attrition Rate` | derived | `Attrition Count`, `Employee Count` | `SUM([Calculation_231935388807032832])/SUM([Employee Count])` | Aggregate over aggregate, so it recomputes at the view's level of detail |
| `Active Employees` | derived | `Employee Count`, `Attrition Count` | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` | Spacing transcribed exactly as stored |
| `Age (bin)` | derived | `Age`, `[Age Parameter]` | `<calculation class='bin' formula='[Age]' peg='0' decimals='0' size-parameter='[Parameters].[Age Parameter]' />` | **Bin width is parameter-driven, not fixed** |
| `Number of Records` | auto | none | `1`, `user:auto-column='numrec'` | Auto-generated by Tableau, never used |
| `min(1)` | derived | none | `min(1)`, ad hoc in `Attrition Rate by Gender for Different Age Group` | Dual-axis placeholder |
| `Department1` | `HR_data.csv` | `Department` | Caption only | Caption is a collision artefact, not a business rename |
| `Education1` | same | `Education` | Caption only | |
| `Education Field1` | same | `Education Field` | Caption only | |
| `Gender1` | same | `Gender` | Caption only | |
| `Job Role1` | same | `Job Role` | Caption only | |
| `Job Satisfaction1` | same | `Job Satisfaction` | Caption; role changed measure → dimension, type `ordinal`, `aggregation='Sum'` retained | |
| `Emp No` | same | `emp no` | Caption only | Declared, never used on a shelf |
| `Employee Number` | same | `Employee Number` | Role changed measure → dimension `ordinal` | Declared, never used on a shelf |
| `CF age band` | same | `CF_age band` | Caption only, underscore removed. **No derivation in this workbook.** | Used directly on Columns |
| `CF attrition label` | same | `CF_attrition label` | Caption only | Declared, never used |
| `CF current Employee` | same | `CF_current Employee` | Caption only | Declared, never used |
| `Employee Count` | same | `Employee Count` | **No override at all.** Used as `SUM([Employee Count])`. | Denominator of `Attrition Rate` |

### Fields whose meaning differed between systems

**Not applicable.** There is only one system in each project, so no cross-system semantic mismatch exists and none was resolved. Saying otherwise would be an invention.

The closest real analogue is **within** Workbook 2: `Department` carries two captions (`Department1`) and two auto action groups (`Action (Department)` and `Action (Department1)`) which both resolve to the same underlying `[Department]` level. That is a Tableau artefact of a data source replacement, not a semantic mismatch between systems.

### Grain

| Object | Grain |
|---|---|
| Workbook 1 source | One row per patient. Evidenced by the column set: there is no patient identifier, no repeated-measure column and no date, and every column is a single clinical attribute. △ INFERRED from the schema; the file itself was not read. |
| Workbook 1 targets | KPI sheets: whole cohort, no dimensions. Donuts: one mark per `Death Event` x comorbidity combination. Histograms: one mark per bin x `Death Event`. `Sheet 6 (8)`: one mark per distinct `age` x `time` combination. `Sheet 6 (9)`: **record grain**, because `aggregation='false'`. |
| Workbook 2 source | One row per employee. Evidenced by `Employee Number` and `emp no` identifier columns plus an `Employee Count` column. △ INFERRED from the schema. |
| Workbook 2 targets | `KPI`: whole filtered population. `Attrition by Gender`: one mark per gender. `Department wise Attrition`: one mark per department. `No. of Employee by Age Group`: one mark per age bin. `Job Satisfaction Rating`: one mark per job role x satisfaction score. `Education Field wise Attrition`: one mark per education field. `Attrition Rate by Gender...`: one mark per age band x gender. |
| Grain mismatches | **None.** Every target aggregates upward from a single-grain source. There is no fan-out, no many-to-many and no double-counting risk, because there is no join anywhere. |

---

## 4. DATA FLOW AND ARCHITECTURE

### End-to-end flow

Both projects share the same minimal shape. There is **no orchestration tool, no staging layer, no warehouse, no lakehouse and no scheduler** anywhere in either file.

**Workbook 1:**

```
[1] Local CSV on a Mac
    heart_failure_clinical_records_dataset.csv
    /Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction
        |  TOOL: none. Manual file placement.
        v
[2] Tableau Desktop 2025.1.0, macOS
    textscan connector: UTF-8, comma, header row, en_US
        |  TOOL: Tableau Desktop
        v
[3] Tableau Hyper extract
    <extract enabled='true' count='-1' units='records'>
    materialised as Data/tableau-temp/#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper
        |  TOOL: Tableau Desktop
        v
[4] Semantic layer, inside the workbook
    13 captions, 6 role conversions, 6 alias sets, 7 bins, 6 calculated fields
        |  TOOL: Tableau Desktop
        v
[5] 19 worksheets
        |
        v
[6] Dashboard "Dashboard 1", 1900 x 1050
        |
        v
[7] Tableau Public
    Healthcare-HeartFailure_17429983482570, revision 1.2
```

**Workbook 2:**

```
[0] UPSTREAM, OUTSIDE THIS WORKBOOK
    CF_age band, CF_attrition label, CF_current Employee already derived
    TOOL: Not in chats
        |
        v
[1] Local files on a Mac
    HR_data.csv  (active)
    HR data.csv, HR data.xlsx, HR Data.xlsx - HR data.csv  (imported, unused)
    /Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main
        |  TOOL: none. Manual file placement.
        v
[2] Tableau Desktop 2025.2.0, macOS
    textscan connector on HR_data.csv
    (an excel-direct connection is declared but not bound)
        |  TOOL: Tableau Desktop
        v
[3] FOUR Tableau Hyper extracts, one per data source
    all <extract enabled='true' count='-1' units='records'>
    4 x .hyper in Data/tableau-temp/, three of them unreferenced
        |  TOOL: Tableau Desktop
        v
[4] Semantic layer, inside the workbook
    10 captions, 2 role conversions, 1 parameter,
    1 parameter-driven bin, 5 calculated fields
    + 1 data source scoped filter on [Education] via <shared-view>
        |  TOOL: Tableau Desktop
        v
[5] 7 worksheets
        |
        v
[6] Dashboard "HR Dashboard ", 1580 x 900 fixed,
    floating over Image/HR background.pptx.png
        |  TOOL: Tableau Desktop. The image itself: PowerPoint, per its filename.
        v
[7] Tableau Public
    HRAnalyticsDashboard_17561606616710 / HRDashboard, revision 1.1
```

### Where data lands at each stage

| Stage | Landing |
|---|---|
| Source | Local file system on one Mac |
| Staging | **None.** No staging layer exists. |
| Warehouse / lakehouse | **None.** |
| Curated files | The Hyper extracts embedded in the packaged workbook. That is the only materialised intermediate in either project. |
| Serving | Tableau Public |

### Inherited or previous architecture

**Not in chats.** Neither workbook records a predecessor, a migration or a rebuild.

Two artefacts hint at prior work but do not evidence an inherited architecture:
1. Workbook 2's three unused data sources, which show the same dataset being imported more than once in different formats.
2. Workbook 2's `CF_` columns, which show that some derivation happened before this workbook.

**What was wrong with it and what I changed: Not in chats.**

### Flow diagram in words, boxes and arrows

```
BOX A  "Local CSV file"        --arrow-->  BOX B  "Tableau Desktop, textscan connector"
BOX B  "Tableau Desktop"       --arrow-->  BOX C  "Hyper extract, all records, no filter"
BOX C  "Hyper extract"         --arrow-->  BOX D  "Semantic layer: captions, roles,
                                                   aliases or calcs, bins, parameter"
BOX D  "Semantic layer"        --arrow-->  BOX E  "Worksheets, 19 or 7"
BOX E  "Worksheets"            --arrow-->  BOX F  "Dashboard, 1 per workbook"
BOX F  "Dashboard"             --arrow-->  BOX G  "Tableau Public"

SIDE BOX  "Filters and actions"  --arrow into--> BOX F
SIDE BOX  "Parameter (Workbook 2 only)" --arrow into--> BOX D and BOX F
```

There are no other boxes. No SQL step, no Python step, no Power Query, no Alteryx, no Databricks, no Airflow, no dbt, no scheduler. **Not in chats** whether any such tool was used outside the workbook.

---

## 5. DATA CONSOLIDATION, CLEANING AND STANDARDISATION

### How data from multiple sources was consolidated

**It was not.** There is no consolidation in either project. Each workbook reads one table. Workbook 2 holds four data sources but never combines them: no worksheet references more than one, no join, no union, no blend and no linking field exists.

### Every cleaning rule actually applied

#### Workbook 1

| # | Rule | Exact definition | Fields affected | Tool | Why there |
|---|---|---|---|---|---|
| 1 | Display renaming | `caption` attribute on the `<column>` element | All 13 source columns | Tableau data source layer | Applied at source scope so all 19 worksheets inherit one definition |
| 2 | Role reclassification | `role='dimension' type='ordinal'` | `DEATH_EVENT`, `anaemia`, `diabetes`, `high_blood_pressure`, `sex`, `smoking` | Tableau data source layer | Tableau imports 0/1 integers as measures and defaults to `SUM`, which is meaningless for a flag. Dimensions can drive Colour, Label and Filter. |
| 3 | Code-to-label standardisation | `<aliases enabled='yes'>` with explicit key/value pairs | 6 fields, 12 aliases | Tableau data source layer | Same reason as rule 1: define once, inherit everywhere |
| 4 | Binning | `<calculation class='bin' ... />` | 7 continuous measures | Tableau data source layer | Required to draw a histogram of a continuous measure |

**Exact alias mappings, transcribed:**

| Field | Key | Aliased value |
|---|---|---|
| `DEATH_EVENT` | `0` | `Surivive` |
| `DEATH_EVENT` | `1` | `Death` |
| `anaemia` | `0` | `Negative` |
| `anaemia` | `1` | `Positive` |
| `diabetes` | `0` | `Negative` |
| `diabetes` | `1` | `Positive` |
| `high_blood_pressure` | `0` | `Negative` |
| `high_blood_pressure` | `1` | `Positive` |
| `sex` | `0` | `Female` |
| `sex` | `1` | `Male` |
| `smoking` | `0` | `` ` Non-Smoker` `` (leading space) |
| `smoking` | `1` | `Smoker` |

**Exact bin definitions, transcribed:**

| Bin | Formula | Size | Peg | Decimals |
|---|---|---|---|---|
| `Age (bin)` | `[age]` | `4.48` | `0` | `0` |
| `Creatinine Phosphokinase (bin)` | `[creatinine_phosphokinase]` | `376` | `0` | `2` |
| `Ejection Fraction (bin)` | `[ejection_fraction]` | `8.22` | `0` | `0` |
| `Platelets (bin)` | `[platelets]` | `41767` | `0` | `4` |
| `Serum Creatinine (bin)` | `[serum_creatinine]` | `0.772` | `0` | `-1` |
| `Serum Sodium (bin)` | `[serum_sodium]` | `3.57` | `0` | `0` |
| `Time (bin)` | `[time]` | `15.1` | `0` | `1` |

#### Workbook 2

| # | Rule | Exact definition | Fields affected | Tool | Why there |
|---|---|---|---|---|---|
| 1 | **Text flag to numeric indicator** | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | new field `Attrition Count`, from `Attrition` | Tableau calculated field | The source column is the string `Yes`/`No` and cannot be aggregated |
| 2 | Rate derivation | `SUM([Calculation_231935388807032832])/SUM([Employee Count])` | new field `Attrition Rate` | Tableau calculated field | Written as aggregate over aggregate so it recomputes at any level of detail |
| 3 | Complement derivation | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` | new field `Active Employees` | Tableau calculated field | |
| 4 | Parameter-driven binning | `<calculation class='bin' formula='[Age]' peg='0' decimals='0' size-parameter='[Parameters].[Age Parameter]' />` | new field `Age (bin)` | Tableau calculated field bound to a parameter | Lets the viewer change granularity at view time |
| 5 | Role reclassification | `role='dimension' type='ordinal'` | `Job Satisfaction`, `Employee Number` | Tableau data source layer | A 1-to-4 satisfaction score is a category, not a quantity to sum |
| 6 | Display renaming | `caption` attribute | 10 fields | Tableau data source layer | 6 of these are `Name1` collision artefacts rather than deliberate renames |
| 7 | Global scope filtering | `<shared-view>` filter on `[none:Education:nk]`, `function='level-members'`, `ui-enumeration='all'` | `Education` | Tableau data source scope | Applies to every worksheet using the data source, including the KPI sheet |
| 8 | Presentation-layer label correction | Hand-typed labels inside `<customized-tooltip>` | `Department:`, `Gender:`, `Job Role:`, `Education Field:`, `Job Satisfaction:` | Tableau worksheet layer | Corrects the `Name1` captions where the user sees them |
| 9 | Explicit category ordering | `<manual-sort column='[none:CF_age band:nk]' direction='ASC'>` with dictionary `"Under 25"`, `"25 - 34"`, `"35 - 44"`, `"45 - 54"`, `"Over 55"` | `CF_age band` | Tableau worksheet layer | Alphabetical ordering would place `Over 55` in the middle |
| 10 | Explicit measure ordering | `<manual-sort column='[:Measure Names]' direction='ASC'>` with a 4-member dictionary | Measure Names on the `KPI` sheet | Tableau worksheet layer | Pins KPI tile order |

### Cleaning rules NOT applied, in either workbook

Stated explicitly so nothing is over-claimed:

| Rule category | Status |
|---|---|
| Null handling (`ISNULL`, `IFNULL`, `ZN`, null replacement) | **Not present in either workbook.** |
| Duplicate detection or removal | **Not present.** |
| Explicit type casting (`INT()`, `STR()`, `FLOAT()`, `DATE()`, `DATETIME()`) | **Not present.** |
| Date parsing, date parts, timezone handling | **Not present, and not possible.** Neither dataset contains a date or datetime column. |
| Text normalisation (`TRIM`, `UPPER`, `LOWER`, `REPLACE`, `REGEXP`) | **Not present.** Note that Workbook 1's own alias `` ` Non-Smoker` `` carries an untrimmed leading space. |
| Outlier detection or capping | **Not present.** |
| Country codes, currency codes, unit standardisation | **Not present.** No such field exists in either dataset. |
| Product or domain classification logic | **Not present.** |
| Referential validation | **Not present.** No joins exist to validate. |
| Tableau Prep flow | **Not present** in either archive. |

### Which tool performed each transformation, and why there

**Every transformation in both workbooks was performed inside Tableau Desktop.** No SQL, no Python, no Power Query, no Alteryx, no Prep flow is referenced anywhere in either file.

Within Tableau, a deliberate layering is visible and worth naming because it is a real design decision:

| Layer | What sits there | Why that layer |
|---|---|---|
| **Data source scope** | Captions, role conversions, aliases (Workbook 1), bins, the `Education` shared-view filter (Workbook 2) | Defined once, inherited by every worksheet. Changing an alias updates 19 sheets at once. |
| **Calculated field scope** | `Attrition Count`, `Attrition Rate`, `Active Employees`, `Age (bin)` (Workbook 2); the 7 bins and 5 string literals (Workbook 1) | Reusable across sheets, and the dependency chain is enforced by Tableau |
| **Worksheet scope** | The `0` and `min(1)` axis placeholders, manual sorts, the three hard-coded KPI filters in Workbook 1, tooltips and labels in Workbook 2 | Local to one view, so no reason to promote them |
| **Dashboard scope** | Filter controls, parameter control, actions | Interaction, not data |

**Whether any cleaning happened before Tableau: Not in chats**, except that Workbook 2's three `CF_` columns are evidence that some derivation did happen upstream.

---

## 6. DATA MODEL: SCHEMA AND TABLE DESIGN

**No dimensional model was designed.** There are no fact tables, no dimension tables, no surrogate keys, no slowly changing dimensions and no date dimension in either project. Both are single flat tables consumed directly.

This is stated plainly because it is the single most important scope boundary for a hiring manager to understand about these two artefacts.

| Design element | Workbook 1 | Workbook 2 |
|---|---|---|
| Fact tables designed | **None** | **None** |
| Dimension tables designed | **None** | **None** |
| Star or snowflake schema | **None** | **None** |
| Surrogate key strategy | **None.** No key column is declared or used. | **None.** `Employee Number` and `emp no` exist as natural identifiers but are never used on any shelf, filter or calculation. |
| Slowly changing dimensions | **None** | **None** |
| Date dimension | **None, and impossible.** No date column exists in either dataset. | **None, and impossible.** |
| Relationships and filter directions | **None.** One table, nothing to relate. | **None.** Four single-table sources, never combined. |
| Historical migration or backfill | **None** | **None** |
| Cutover between systems | **Not applicable.** No second system. | **Not applicable.** |
| Cardinality settings | **Not applicable** | **Not applicable** |
| Referential integrity settings | **Not applicable** | **Not applicable** |

### Design rules that WERE set, and the reason for each

These are real, verifiable structural decisions, even though they are not dimensional modelling decisions.

| # | Rule | Where it applies | Evidence | Reason (△ inferred unless noted) |
|---|---|---|---|---|
| 1 | Extract everything, filter nothing at extract time | Both workbooks, all 5 extracts | `count='-1'`, no extract filter | Keeps the workbook self-contained and keeps all filtering interactive |
| 2 | Embed the data source, do not publish it | Both workbooks | `inline='true'` on every data source | Consistent with a portfolio or coursework artefact intended to be self-contained |
| 3 | Binary flags are dimensions, not measures | Workbook 1, 6 fields; Workbook 2, 2 fields | `role='dimension' type='ordinal'` | Prevents meaningless `SUM` on a flag and enables Colour, Label and Filter |
| 4 | Decode codes at the source, not in the view | Workbook 1 | `<aliases enabled='yes'>` at data source level | One definition, 19 inheritors |
| 5 | Define metrics as calculated fields, not per-view expressions | Workbook 2 | `Attrition Count`, `Attrition Rate`, `Active Employees` promoted to the data source | One definition for a business metric, reused across sheets |
| 6 | Write ratios as aggregate over aggregate | Workbook 2 | `SUM(...)/SUM(...)` | So the ratio recalculates correctly at any level of detail rather than averaging row-level ratios |
| 7 | Make analytical granularity a user choice | Workbook 2 | `size-parameter='[Parameters].[Age Parameter]'` | Avoids committing to one bucket width |
| 8 | Scope global filters at the data source | Workbook 2 | `<shared-view>` filter on `[Education]` | Guarantees the KPI sheet responds, which a per-sheet filter selection can miss |
| 9 | Scope a filter to a chosen subset of sheets | Workbook 1 | `filter-group='3'` on 14 of 19 sheets | Applies one control to the charts. Note the consequence: the 5 KPI cards are excluded. |
| 10 | One visual grammar, repeated | Workbook 1 | 5 structurally identical donuts, 7 structurally identical histograms | The reader learns the chart once |
| 11 | Titles bound to sheet names | Workbook 2 | `<Sheet Name>` token in 6 titles | Renaming a sheet renames its dashboard title automatically |

---

## 7. BUSINESS RULES, VALIDATION AND GOVERNANCE

### Business rules actually encoded

Only two business rules exist in either workbook, and both are in Workbook 2.

| # | Rule | Exact definition | Consequence |
|---|---|---|---|
| 1 | **What counts as attrition** | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | Attrition is whatever the source column marks `Yes`. There is **no** voluntary versus involuntary split, **no** tenure qualification, **no** status exclusion and **no** date window. |
| 2 | **What counts as active** | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` | The population is treated as a closed set: every employee is either active or a leaver. This is a snapshot, not a point-in-time headcount, because no hire or termination date exists. |
| 3 | **How attrition rate is defined** | `SUM([Attrition Count])/SUM([Employee Count])` | Leavers over total headcount in the current view scope. No annualisation, no average-headcount denominator. |

**Workbook 1 encodes no business rule at all.** Its aliases are label mappings, not rules. There is no classification logic, no exclusion, no threshold and no derived category anywhere in it.

**Product classifications, status values excluded, domain coding logic: Not in chats.** None exists in either workbook.

### Validation checks

**None are present in either workbook.** This is a complete absence, not an omission from this brief.

| Check type | Present? |
|---|---|
| Reconciliation to source | **Not in chats.** No reconciliation sheet, no control total, no comparison view exists. |
| Row count checks | **Not in chats.** |
| Control totals | **Not in chats.** |
| Cross-system checks | Not applicable, one system. |
| Step-change checks | **Not in chats.** |
| Regression checks | **Not in chats.** |
| Data-quality flags shown to users | **None.** No worksheet, annotation or field surfaces a quality indicator. |

**Whether validation was performed outside Tableau: Not in chats.**

### Governance

| Item | Evidence |
|---|---|
| Metric definitions and data dictionary | **Not in chats.** No documentation field, no description, no dictionary. The calculated field names in Workbook 2 (`Attrition Count`, `Attrition Rate`, `Active Employees`) are self-describing, which is the closest thing to a definition present. |
| Sign-off process and owners | **Not in chats.** |
| Decision log | **Not in chats.** |
| Open questions register | **Not in chats.** |
| Documentation | **Not in chats.** Neither workbook contains any. |
| Version control | **Not in chats** for a repository. What does exist: Tableau Public revision counters, `revision='1.2'` on Workbook 1 and `revision='1.1'` on Workbook 2, indicating at least two publishes each. |
| Circumstantial repository marker | Workbook 2's source folder is named `HR-Analytics-Dashboard-Using-Tableau-main`. The `-main` suffix is the naming produced by downloading a GitHub repository ZIP of a `main` branch. This suggests a repository was involved somewhere in the project's history, but the workbook does not say whose or for what. △ INFERRED. |
| What is and is not stored in a repository | **Not in chats.** |

### Defects found in the inherited work, and what each fix was

**Not in chats.** No inherited work is identified.

### Defects observable in the delivered artefacts

To be useful rather than flattering, here are the defects that **are** verifiable in the two workbooks. These were found by reading the XML, not reported by anyone.

| # | Workbook | Defect | Evidence | Status |
|---|---|---|---|---|
| 1 | 1 | The `DEATH_EVENT = 0` alias is spelled **`Surivive`**, a misspelling of "Survive", and it renders in every legend and label | `<alias key='0' value='Surivive' />` | **Not fixed** in the delivered file |
| 2 | 1 | The `smoking = 0` alias has a **leading space**: `" Non-Smoker"` | `<alias key='0' value=' Non-Smoker' />` | **Not fixed** |
| 3 | 1 | The Sex dashboard filter is scoped to `filter-group='3'`, which covers 14 of 19 sheets and **excludes all five KPI cards**, so the headline numbers do not move when the filter is used | Filter group membership per worksheet | **Not fixed.** Whether deliberate is Not in chats. |
| 4 | 1 | All 7 bin sizes are non-round values (`4.48`, `8.22`, `0.772`, `3.57`, `15.1`, `376`, `41767`), consistent with Tableau's suggested defaults rather than chosen widths | Bin `size` attributes | **Not fixed.** Whether deliberate is Not in chats. |
| 5 | 1 | No number formatting is defined anywhere | No `number-format` attribute in the file | **Not fixed** |
| 6 | 1 | No custom tooltip on any of the 19 worksheets | No `<customized-tooltip>` element in the file | **Not fixed** |
| 7 | 2 | Three of four data sources are unused but still carry extracts, adding three redundant `.hyper` files to the packaged archive | Archive listing plus worksheet dependencies | **Not fixed** |
| 8 | 2 | Six field captions are `Name1` collision artefacts (`Department1`, `Gender1`, `Job Role1`, `Education1`, `Education Field1`, `Job Satisfaction1`) | `caption` attributes | **Partly mitigated.** Tooltips hand-type the clean labels; legends still show the artefacts. |
| 9 | 2 | The worksheet titled `Attrition Rate by Gender for Different Age Group` does **not** use the `Attrition Rate` field. Its Angle shelf carries `SUM([Attrition Count])` and its labels carry a percent-of-total table calculation. | Shelf contents and tooltip text | **Not fixed** |
| 10 | 2 | No number formatting is defined, so `Attrition Rate` renders as a decimal rather than a percentage | No `number-format` attribute in the file | **Not fixed** |
| 11 | 2 | The workbook was saved with a `Department = "R&D"` mark selected, persisting an action filter into 6 of 7 worksheets | `<groupfilter function='member' member='"R&amp;D"' user:ui-action-filter='[Action1]' />` | **Not fixed.** Whether deliberate is Not in chats. |
| 12 | 2 | `Job Satisfaction Rating` has a continuous colour encoding but **no colour legend** on the dashboard | Dashboard zone list | **Not fixed** |
| 13 | 2 | `Education Field wise Attrition` has **no sort**, so bars appear in data source order rather than ranked | No `<sort>` or `<manual-sort>` on that sheet | **Not fixed** |
| 14 | 2 | The dashboard name carries a **trailing space**: `HR Dashboard ` | `<dashboard name='HR Dashboard '>` | **Not fixed** |
| 15 | 2 | The parameter has three different names in three places: internal `Age Parameter`, caption `Bin Size`, control title `Age Size` | Parameter definition and zone title | **Not fixed** |

---

## 8. REFRESH, OPERATIONS AND SECURITY

Almost nothing in this section exists, and that is the accurate answer.

| Item | Evidence |
|---|---|
| **Refresh frequency of each stage** | **Not in chats.** No schedule, no incremental configuration, no refresh definition exists in either workbook. |
| **Full or incremental** | **Full, by construction.** Every extract is `count='-1' units='records'` with no incremental refresh key and no extract filter. An extract configured this way refreshes in full when refreshed at all. ✓ Verified. |
| Refresh trigger | **Not in chats.** Both connect to local files, so a refresh requires the file to be present on that Mac and a manual or scheduled refresh to be run. There is no `dataRefreshTime` value set (`dataRefreshTime=''` on the one connection that declares the attribute). |
| **How the source connects to Tableau** | Direct local file read via the `textscan` connector, then extracted. There is **no** server, **no** gateway, **no** DSN, **no** connection string, **no** credentials and **no** DirectQuery equivalent. Tableau's live-versus-extract choice here is **extract**, in both workbooks, on all five data sources. ✓ Verified. |
| Gateway | **None.** Not applicable to a local file. |
| Connection parameters | **None** beyond the text parsing options (`UTF-8`, `,`, header, `en_US`) on Workbook 1. |
| **Access control** | **Not in chats.** Both workbooks publish to **Tableau Public**, which is a public-by-default platform with no row-level security and no user-based access control. That is a property of the platform, verifiable from the `repository-location` pointing at `public.tableau.com`. ✓ Verified that they publish there. |
| Credentials handling | `workgroup-auth-mode='as-is'` on every connection, which is the default for a file connection requiring no authentication. No credential is stored, because none is needed. ✓ Verified. |
| **Row-level security** | **None.** No user filter, no `USERNAME()`, no `ISMEMBEROF()`, no user function appears in either workbook. ✓ Verified by absence. |
| Workspace administration | **Not applicable.** Tableau Public has no workspace model. |
| **What data was allowed to leave the source systems** | **No restriction, and none needed.** Both workbooks are packaged with full data extracts embedded, so publishing either one to Tableau Public publishes the underlying records with it, downloadable by any viewer. **Both datasets are public Kaggle datasets**, confirmed by the author, so there is no disclosure issue. Worth stating explicitly because embedding a full extract in a public workbook would be a real problem with any non-public source, and knowing that distinction is the point. |
| Monitoring | **Not in chats.** None exists. |
| Failure handling | **Not in chats.** None exists. |
| Who is notified | **Not in chats.** No alert, subscription or notification is configured. |

---

## 9. REQUIREMENTS TO KPIs, MEASURES AND DASHBOARD LOGIC

### How requirements were gathered

**Not in chats.** No requirement, session, question list or stakeholder input is recorded in either workbook. Nothing is known about what anyone asked for or what they used instead.

### KPI list

#### Workbook 1

| KPI | Business definition | Decision it supports | Grain | Source fields | Calculation logic | Owner | Sign-off |
|---|---|---|---|---|---|---|---|
| `Total Individuals` | Count of patients in the cohort | Sets the base for reading every other figure | Whole cohort, unfiltered | `DEATH_EVENT` | `CNT([DEATH_EVENT])`, no filter | Not in chats | Not in chats |
| `Total Deaths` | Count of patients with the mortality flag set | Absolute mortality volume | Whole cohort, filtered to `DEATH_EVENT = 1` | `DEATH_EVENT` | `CNT([DEATH_EVENT])` with worksheet filter `member='1'` | Not in chats | Not in chats |
| `Total Males` | Count of male patients | Cohort sex composition | Filtered to `sex = 1` | `sex` | `CNT([sex])` with worksheet filter `member='1'` | Not in chats | Not in chats |
| `Total Females` | Count of female patients | Cohort sex composition | Filtered to `sex = 0` | `sex` | `CNT([sex])` with worksheet filter `member='0'` | Not in chats | Not in chats |
| `Average Age` | Mean patient age | Frames the age distribution below it | Whole cohort, unfiltered | `age` | `AVG([age])` | Not in chats | Not in chats |

**Note:** none of these five responds to the dashboard's Sex filter, because the five KPI worksheets sit outside `filter-group='3'`. ✓ Verified.

**There is no rate KPI in Workbook 1.** Mortality rate is never computed as a KPI.

#### Workbook 2

| KPI | Business definition | Decision it supports | Grain | Source fields | Calculation logic | Owner | Sign-off |
|---|---|---|---|---|---|---|---|
| `Employee Count` | Headcount in the filtered population | Denominator context for everything else | Current filter scope | `Employee Count` | `SUM([Employee Count])` | Not in chats | Not in chats |
| `Attrition Count` | Number of leavers in the filtered population | Absolute attrition volume | Current filter scope | `Attrition` | `SUM(IF [Attrition] = 'Yes' THEN 1 ELSE 0 END)` | Not in chats | Not in chats |
| `Attrition Rate` | Leavers divided by headcount | Whether attrition is high relative to population size, comparably across slices of different sizes | Current filter scope, recomputed at view level of detail | `Attrition`, `Employee Count` | `SUM([Attrition Count])/SUM([Employee Count])` | Not in chats | Not in chats |
| `Active Employees` | Headcount remaining after attrition | Retained population | Current filter scope | `Employee Count`, `Attrition` | `SUM([Employee Count]) - SUM([Attrition Count])` | Not in chats | Not in chats |
| `AVG(Age)` | Mean employee age | Flags whether a cross-filter has isolated an unusually young or old cohort | Current filter scope | `Age` | `AVG([Age])` | Not in chats | Not in chats |

All five respond to the global Education filter and to all six cross-filter actions. ✓ Verified.

### Measures written, with the actual code

No DAX and no SQL exists in either project. The actual Tableau calculation code, transcribed exactly:

```
// Workbook 2, Attrition Count
IF [Attrition] = 'Yes' THEN 1 ELSE 0 END

// Workbook 2, Attrition Rate
SUM([Calculation_231935388807032832])/SUM([Employee Count])
// which reads in the UI as:  SUM([Attrition Count])/SUM([Employee Count])

// Workbook 2, Active Employees
SUM([Employee Count])- SUM([Calculation_231935388807032832])
// which reads in the UI as:  SUM([Employee Count]) - SUM([Attrition Count])

// Workbook 2, Number of Records  (auto-generated, unused)
1

// Workbook 2, min(1)  (ad-hoc dual-axis placeholder)
min(1)

// Workbook 2, Age (bin)  (not a formula, a bin definition)
class = bin, formula = [Age], peg = 0, decimals = 0,
size-parameter = [Parameters].[Age Parameter]

// Workbook 1, the five KPI caption fields
"Total Individuals"
"Total Deaths"
"Total Males"
"Total Females"
"Average Age"

// Workbook 1, dual-axis placeholder
0

// Workbook 1, the seven bin definitions
class = bin, formula = [age],                      size = 4.48,  peg = 0, decimals = 0
class = bin, formula = [creatinine_phosphokinase], size = 376,   peg = 0, decimals = 2
class = bin, formula = [ejection_fraction],        size = 8.22,  peg = 0, decimals = 0
class = bin, formula = [platelets],                size = 41767, peg = 0, decimals = 4
class = bin, formula = [serum_creatinine],         size = 0.772, peg = 0, decimals = -1
class = bin, formula = [serum_sodium],             size = 3.57,  peg = 0, decimals = 0
class = bin, formula = [time],                     size = 15.1,  peg = 0, decimals = 1
```

**There are no LOD expressions in either workbook.** ✓ Verified by absence of `{` in every formula.

### Dashboard design

#### Workbook 1, `Dashboard 1`

| Item | Value |
|---|---|
| Pages | 1 dashboard, no story, no navigation |
| What it shows | Top strip: 5 KPI cards. Second strip: 5 donuts, one per binary attribute, crossed with the survival outcome. Third and fourth strips: 7 biomarker histograms plus 2 scatter-style views. |
| Visuals used | Donut (dual-axis pie), stacked histogram, scatter, disaggregated dot plot with an average reference line, text cards |
| Filters shown to the user | 1 dropdown, `Sex`, applied to 14 of 19 sheets |
| Drill paths | **None.** No hierarchy exists. |
| How assumptions and definitions are shown to the user | **They are not.** There is no text object, no annotation, no caption, no legend explanation and no custom tooltip anywhere on this dashboard. |
| Canvas | 1900 x 1050, `sizing-mode='range'`, black, fully tiled with nested flow containers |

#### Workbook 2, `HR Dashboard `

| Item | Value |
|---|---|
| Pages | 1 dashboard, no story, no navigation |
| What it shows | Header with a title text object and the Education filter. KPI band with 5 tiles plus a gender lollipop. Middle band with a department pie, a parameterised age histogram and a job-role-by-satisfaction highlight table. Bottom band with an education field bar chart and a row of age band donuts split by gender. |
| Visuals used | Measure Names/Values KPI strip, lollipop (Bar + Circle dual axis), pie with percent of total, parameterised bar histogram with a sequential purple ramp, highlight table with Square marks and a sequential blue ramp, horizontal bar, donut small multiples with the band total in the hole |
| Filters shown to the user | 1 dropdown, `Education`, applied to all 7 sheets via data source scope |
| Parameter controls shown to the user | 1 slider, `Age Size`, real, 2.0 to 10.0, step 1.0, default 3.0 |
| Drill paths | **None.** No hierarchy exists. Cross-filtering by clicking substitutes for drill-down. |
| How assumptions and definitions are shown to the user | Partially. Custom tooltips on all 7 sheets spell out field labels and name the table calculation explicitly as `% of Total Attrition Count along Table (Across)`. There is **no** definition of what `Attrition = 'Yes'` means, and **no** stated assumptions panel. |
| Canvas | 1580 x 900, `sizing-mode='fixed'`, floating objects over `Image/HR background.pptx.png` |

### Anything the business explicitly asked for in the presentation

**Not in chats.** No requirement of any kind is recorded.

---

## 10. STAKEHOLDER COORDINATION

**Nothing in this section is available.** Neither workbook contains a single name, role, comment, review, approval or coordination artefact.

| Item | Evidence |
|---|---|
| Each stakeholder: name, role, contribution, decision | **Not in chats.** |
| Meetings and working sessions | **Not in chats.** |
| What was agreed | **Not in chats.** |
| What was pushed back on | **Not in chats.** |
| How disagreement was handled | **Not in chats.** |
| A rejected earlier report | **Not in chats.** |
| A dispute about a number | **Not in chats.** |
| How the work was framed to the business | **Not in chats.** |

The only human trace in either file is the macOS account name `atharvadevne` inside file paths. There is no second person anywhere in the evidence.

---

## 11. OUTCOMES AND STATUS

### What is live

| Item | Evidence | Confidence |
|---|---|---|
| Workbook 1 was published to Tableau Public | `repository-location derived-from='https://public.tableau.com/workbooks/Healthcare-HeartFailure_17429983482570?rev=1.1'`, `revision='1.2'` | ✓ Verified that it was published. Whether it is **currently** live could not be checked; `public.tableau.com` returned `403 to CONNECT` under this environment's network policy. |
| Workbook 2 was published to Tableau Public | `repository-location derived-from='https://public.tableau.com/workbooks/HRAnalyticsDashboard_17561606616710?rev=1.0'`, `revision='1.1'`, dashboard `id='HRDashboard'` | Same |
| Both were published at least twice | Revision counters advanced from `1.1` to `1.2` and from `1.0` to `1.1` | ✓ Verified |
| Both dashboards are complete builds | Every worksheet in each workbook is placed on its dashboard. There are **no orphaned, unfinished or staged worksheets** in either file. 19 of 19 and 7 of 7. | ✓ Verified |

### What is validated

**Nothing.** No validation artefact exists in either workbook. See section 7.

### What is signed off

**Not in chats.**

### What is still open

Not open work items in a project sense, but the 15 verifiable defects listed in section 7 are all **unfixed in the delivered files**. The most consequential three:

1. Workbook 2's bottom chart is titled `Attrition Rate ...` but plots `Attrition Count`.
2. Workbook 2 was saved with a `Department = "R&D"` selection persisted into 6 of 7 worksheets.
3. Workbook 1's Sex filter does not reach the 5 KPI cards.

### Measurable results

**Not in chats.** No view count, no adoption figure, no time saving, no grade, no feedback and no business outcome is recorded in either file. Nothing can be claimed.

What can be counted, and only this:

| Metric | Value | Evidence |
|---|---|---|
| Dashboards delivered | 2 | ✓ |
| Worksheets built | 26 (19 + 7) | ✓ |
| Calculated fields authored | 19 | ✓ |
| Parameters authored | 1 | ✓ |
| Distinct chart forms built | 9 across both | ✓ |
| Dashboard actions configured | 7 (1 highlight, 6 filter) | ✓ |
| Custom tooltips authored | 8 definitions across 7 worksheets | ✓ |
| Source columns consumed | 13 of 13, and 15 of 39 | ✓ |
| Tableau versions used | 2025.1.0 and 2025.2.0, both macOS | ✓ |
| Publish revisions | at least 2 per workbook | ✓ |

### Lessons learned

**Not in chats.** No retrospective, note or comment exists. The defect list in section 7 is an external reading of the files, not a record of anything learned.

---

## 12. GAPS AND QUESTIONS FOR ME

Every question below corresponds to a "Not in chats" entry above. They are ordered by how much they would strengthen the brief.

### Already answered by the author

These three are closed and are folded into the document above. They are listed so the trail is visible.

### Still open

1. ~~Was either project done for anyone?~~ **ANSWERED: both self-directed, for your own development. Not coursework.**
2. ~~Where did each dataset come from?~~ **ANSWERED: both from Kaggle.**
3. ~~Is the heart failure dataset public?~~ **ANSWERED: yes, public. No disclosure issue.**

### Data and logic questions

6. **Section 2, 5:** How were the `CF_age band`, `CF_attrition label` and `CF_current Employee` columns in the HR file derived, and by whom? Were they already in the file you obtained, or did you create them in an earlier Tableau workbook and export them?
7. **Section 3, 9:** What does `Employee Count` actually contain? If it is 1 on every row, please confirm, because it is the denominator of your only rate KPI.
8. **Section 5:** Does `DEATH_EVENT` contain any nulls? `CNT([DEATH_EVENT])` is your cohort-size KPI and it counts non-nulls, so nulls would silently understate it.
9. **Section 5:** Was either CSV cleaned before it reached Tableau? If yes, with what tool and what exact rules?
10. **Section 7:** Is there a definition anywhere of what `Attrition = 'Yes'` means in the source, for example whether it includes involuntary exits?

### Decision and design questions

11. **Section 6, 9:** Why counts and no mortality rate in the Heart Failure dashboard? Was a rate considered and rejected?
12. **Section 5:** Why were Tableau's suggested bin sizes accepted in Workbook 1 (`4.48`, `8.22`, `0.772`, `3.57`, `15.1`)? Was a clinically meaningful width considered?
13. **Section 7, defect 3:** Was excluding the KPI cards from the Sex filter deliberate, so the cards act as a constant baseline, or an oversight?
14. **Section 2:** Why does Workbook 2 have four data sources? What was tried first, and why did `HR_data.csv` win?
15. **Section 7, defect 9:** Was the bottom HR chart originally intended to show `Attrition Rate` and then changed to `Attrition Count`, or was the title always approximate?
16. **Section 7, defect 8:** Were the `Department1`, `Gender1`, `Job Role1` captions intentional, or collision artefacts from replacing a data source?
17. **Section 7, defect 11:** Was the saved `R&D` selection deliberate?
18. **Why a highlight action in one dashboard and six filter actions in the other?** This is a genuinely good design question and a strong answer lands well in an interview.
19. **Section 4:** Where did `HR background.pptx.png` come from? The filename says PowerPoint. Did you design it?

### Outcome questions

20. **Section 11:** The live Tableau Public URLs, confirmed by you. The recoverable IDs are `Healthcare-HeartFailure_17429983482570` and `HRAnalyticsDashboard_17561606616710`.
21. **Section 11:** Any view counts, feedback, grade or reuse for either dashboard?
22. **Section 11:** Screenshots of both as published, since none could be captured here.
23. **Section 11:** Anything changed after publishing, and why? Both show at least two publish revisions.
24. **Section 11:** One concrete insight you personally found in each dataset while building. Not a figure the dashboard computes, but something you noticed. Interviewers ask "what did you find", and "the dashboard lets you find X" is a weaker answer than "I found X".
25. **Section 7:** Which of the 15 listed defects do you agree with, and which have an explanation I have missed?

### Questions that clarify scope honestly

26. **Sections 4, 6, 8:** Have you done pipeline, warehouse, SQL or dimensional modelling work elsewhere? Neither of these workbooks evidences it, and if a hiring manager is assessing that capability it needs a different artefact. If these two are the whole portfolio, it is better to position them accurately as dashboard design and Tableau semantic layer work.

---

## 13. SANITISED VERSION

The same document with identifying details replaced. All technical detail, counts, rules and logic are unchanged.

---

### 1. PROJECT CONTEXT (sanitised)

**Business problem.** Not in chats. Neither workbook contains a description, annotation, caption or documentation field. The only authored prose across both files is a single dashboard title text object reading `HR ANALYTICS DASHBOARD`.

Subject matter inferable from structure: Workbook 1 profiles patient survival in a cardiac care dataset, evidenced by 12 of 14 chart titles ending in `- Survival Stats` and a mortality outcome field on the Colour shelf of every chart. Workbook 2 analyses workforce attrition, evidenced by an attrition measure behind 5 of 7 worksheets.

**Who requested the work.** Nobody. Both projects were self-directed, built by the author for their own skill development, confirmed by the author. Workbook 1's source file sits in a folder path containing a university name and a data visualisation course name, which looks like coursework but is not.

**My role.** Not in chats as a title. Both workbooks are single-author artefacts: every data source is embedded (`inline='true'`) rather than published to a server, every connection points at a local file on one workstation, and no collaboration marker exists. Responsibilities evidenced by the files: data connection, extract configuration, semantic layer definition, calculated field authoring, parameter creation, worksheet construction, formatting, dashboard layout, filter scoping, action configuration, tooltip authoring and publication to a public visualisation hosting platform.

**Who else was involved.** Not in chats. No second person appears anywhere in the evidence.

**Timeline.** Start and end dates: not recorded here. BI tool builds used: version 2025.1.0 (build component dating to 13 March 2025) and version 2025.2.0 (build components dating to 14 May 2025 and 23 July 2025), both on macOS. Both workbooks show at least two publish revisions. Current status: both published to a public visualisation hosting platform; whether currently live could not be checked because the environment's network policy blocked the host.

### 2. SOURCE SYSTEMS AND DATA INVENTORY (sanitised)

There are no source systems in the enterprise sense. No database, no API, no document management site, no shared folder, no server. Every connection is to a local file on one workstation.

**Workbook 1:** local file system, delimited text file connector, one CSV of clinical records, parsing configuration `character-set='UTF-8'`, `separator=','`, `header='yes'`, `locale='en_US'`, one relation of `type='table'`, 13 columns, no key declared. Provenance: a public dataset obtained from a public data-sharing platform, confirmed by the author.

Schema, 13 columns with ordinals and types: patient age (real), four binary comorbidity or lifestyle flags (integer), five continuous clinical biomarker measurements (three real, two integer), a binary demographic flag (integer), an integer follow-up period, and a binary mortality outcome (integer). Every metadata record carries `contains-null='true'`, which is the connector's default optimistic flag on a scanned text file rather than evidence that nulls exist.

**Workbook 2:** four data sources, all pointing at the same folder on the same workstation and all declaring the identical 39-column schema.

| # | Connector | File format | Status |
|---|---|---|---|
| 1 | delimited text (active), plus a declared but unbound spreadsheet connector | CSV | **ACTIVE**, all 7 worksheets bind to it |
| 2 | delimited text | CSV | UNUSED, extract still present |
| 3 | delimited text | CSV | UNUSED, extract still present |
| 4 | delimited text | spreadsheet | UNUSED, extract still present |

The unbound connection is declared with `cleaning='no'`, `compat='no'`, `dataRefreshTime=''`, `interpretationMode='0'`, `validate='no'`, `workgroup-auth-mode='as-is'`, but the relation binds to the delimited-text connection instead. Why four data sources exist: Not in chats.

39-column schema covering an attrition flag, headcount, organisational unit, education field and level, gender, job role, five satisfaction and involvement scores, seven compensation and rate columns, five tenure columns, employee identifiers and demographic columns.

Three columns arrive pre-derived, carrying the BI tool's exported-calculated-field prefix: an age band, an attrition label and a current-employee flag. They carry no calculation in this workbook, so the derivation happened upstream. The upstream step itself: Not in chats.

Provenance for all four sources: a public dataset obtained from a public data-sharing platform, confirmed by the author. Legacy versus current systems: not applicable, there is no second system, no history and no date field in either dataset.

### 3. SOURCE-TO-TARGET MAPPING (sanitised)

**Workbook 1**, 13 source columns to targets:

| Target | Source field | Transformation rule |
|---|---|---|
| Patient age | age column | caption rename only, type real, role measure |
| Mortality outcome | outcome flag column | caption rename; role measure → dimension `ordinal`; alias `0` → `Surivive` **(misspelled in the file, renders that way)**, `1` → `Death` |
| Comorbidity flag A | flag column | caption rename; role → dimension `ordinal`; alias `0` → `Negative`, `1` → `Positive` |
| Comorbidity flag B | flag column | same pattern |
| Comorbidity flag C | flag column | same pattern |
| Demographic flag | flag column | caption rename; role → dimension `ordinal`; alias `0` → `Female`, `1` → `Male` |
| Lifestyle flag | flag column | caption rename; role → dimension `ordinal`; alias `0` → `` ` Non-Smoker` `` **(leading space in the file)**, `1` → `Smoker` |
| Five biomarker measures | five measurement columns | caption rename only |
| Follow-up period | period column | caption rename only; integer period, **not a date** |
| 7 bin fields | the 7 continuous measures | `class='bin'`, `peg='0'`, fixed sizes `4.48`, `376`, `8.22`, `41767`, `0.772`, `3.57`, `15.1` with `decimals` `0`, `2`, `0`, `4`, `-1`, `0`, `1` |
| 5 KPI caption fields | none | string literals: `"Total Individuals"`, `"Total Deaths"`, `"Total Males"`, `"Total Females"`, `"Average Age"` |
| Axis placeholder | none | `0` |

**Workbook 2**, mapping:

| Target | Source field | Transformation rule |
|---|---|---|
| Attrition Count | attrition flag (string `Yes`/`No`) | `IF [attrition flag] = 'Yes' THEN 1 ELSE 0 END` |
| Attrition Rate | Attrition Count, headcount column | `SUM([Attrition Count])/SUM([headcount column])` |
| Active Employees | headcount column, Attrition Count | `SUM([headcount column])- SUM([Attrition Count])` |
| Age (bin) | age column, bin size parameter | `class='bin'`, `peg='0'`, `decimals='0'`, `size-parameter` bound to the parameter |
| Number of Records | none | `1`, auto-generated by the BI tool, unused |
| Dual-axis placeholder | none | `min(1)`, ad hoc within one worksheet |
| 6 captioned dimensions | organisational unit, education level, education field, gender, job role, satisfaction score | caption only; all six captions are `Name1` collision artefacts. The satisfaction score is additionally role-converted measure → dimension `ordinal`. |
| Employee identifier | identifier column | role converted measure → dimension `ordinal`; never used on a shelf |
| 3 pre-derived columns | upstream-derived columns | caption only, underscore removed; **no derivation in this workbook** |
| Headcount | headcount column | no override at all; used as `SUM(...)` |

**Fields whose meaning differed between systems.** Not applicable. One system per project, so no cross-system semantic mismatch existed and none was resolved.

**Grain.** Workbook 1 source: one row per patient, inferred from the schema. Workbook 2 source: one row per employee, inferred from the presence of two identifier columns and a headcount column. Target grains range from whole-population (KPI sheets) to record grain (one worksheet with aggregation switched off). **No grain mismatches**, because no join exists anywhere in either project.

### 4. DATA FLOW AND ARCHITECTURE (sanitised)

No orchestration tool, no staging layer, no warehouse, no lakehouse and no scheduler exists in either project.

```
[1] Local delimited file on a workstation
        |  TOOL: none, manual file placement
        v
[2] BI desktop tool, delimited text connector
        |  TOOL: BI desktop tool
        v
[3] Columnar in-memory extract, all records, no filter
        |  TOOL: BI desktop tool
        v
[4] Semantic layer inside the workbook
    captions, role conversions, aliases or calculations, bins, parameter
        |  TOOL: BI desktop tool
        v
[5] Worksheets  (19 in Workbook 1, 7 in Workbook 2)
        |
        v
[6] Dashboard, one per workbook
        |
        v
[7] Public visualisation hosting platform
```

Workbook 2 adds a stage zero: three columns arrive already derived from an upstream step that is **Not in chats**, and three additional unused data sources each carry their own extract into the packaged archive.

**Where data lands:** source is the local file system; staging, warehouse and lakehouse are all **none**; the only materialised intermediate is the in-memory extract embedded in the packaged workbook; serving is the public hosting platform.

**Inherited or previous architecture:** Not in chats. Two artefacts hint at prior work without evidencing an architecture: Workbook 2's three unused data sources and its three pre-derived columns.

### 5. DATA CONSOLIDATION, CLEANING AND STANDARDISATION (sanitised)

**No consolidation occurred.** Each workbook reads one table. Workbook 2 holds four data sources but never combines them: no join, no union, no blend, no linking field.

**Workbook 1 cleaning rules, all four of them:**

1. Display renaming via the `caption` attribute, applied to all 13 source columns at data source scope so all 19 worksheets inherit one definition.
2. Role reclassification to `role='dimension' type='ordinal'` on 6 binary integer columns, because the tool imports 0/1 integers as measures and defaults to `SUM`, which is meaningless for a flag.
3. Code-to-label standardisation via `<aliases enabled='yes'>` at data source scope, 6 fields and 12 alias pairs, with exact mappings: outcome `0` → `Surivive` and `1` → `Death`; three comorbidity flags `0` → `Negative` and `1` → `Positive`; demographic `0` → `Female` and `1` → `Male`; lifestyle `0` → `` ` Non-Smoker` `` and `1` → `Smoker`.
4. Binning of 7 continuous measures with the fixed sizes listed in section 3.

**Workbook 2 cleaning rules, all ten of them:**

1. Text flag to numeric indicator: `IF [attrition flag] = 'Yes' THEN 1 ELSE 0 END`.
2. Rate derivation as aggregate over aggregate: `SUM([Attrition Count])/SUM([headcount])`.
3. Complement derivation: `SUM([headcount])- SUM([Attrition Count])`.
4. Parameter-driven binning, `size-parameter` bound to a range parameter.
5. Role reclassification on 2 columns to `dimension ordinal`.
6. Display renaming on 10 fields, 6 of which are collision artefacts.
7. Global scope filtering via a shared-view filter on the education level field, applying to every worksheet using the data source.
8. Presentation-layer label correction: hand-typed clean labels inside every custom tooltip, correcting the collision-artefact captions where the user sees them.
9. Explicit category ordering via a manual sort dictionary: `"Under 25"`, `"25 - 34"`, `"35 - 44"`, `"45 - 54"`, `"Over 55"`, because alphabetical order would place the oldest band in the middle.
10. Explicit measure ordering via a manual sort dictionary on the measure-names field.

**Cleaning rules NOT applied in either workbook:** null handling, duplicate detection, explicit type casting, date parsing or timezone handling (impossible, neither dataset has a date column), text normalisation (note that one alias itself carries an untrimmed leading space), outlier treatment, country or currency or unit standardisation, domain classification logic, referential validation, and any external data preparation flow.

**Which tool performed each transformation.** All of it was done inside the BI desktop tool. No SQL, no Python, no query editor, no ETL tool and no data preparation flow is referenced anywhere. Within the tool, a deliberate four-layer placement is visible: data source scope for anything that should be inherited everywhere, calculated field scope for reusable metrics, worksheet scope for view-local devices, and dashboard scope for interaction.

### 6. DATA MODEL: SCHEMA AND TABLE DESIGN (sanitised)

**No dimensional model was designed.** No fact tables, no dimension tables, no surrogate keys, no slowly changing dimensions, no date dimension, no relationships and no filter directions in either project. Both are single flat tables consumed directly. Historical migration, backfill and cutover: not applicable, there is no history and no second system.

**Design rules that were set**, with the reason for each: extract everything and filter nothing at extract time; embed the data source rather than publish it; treat binary flags as dimensions rather than measures; decode codes at the source rather than in the view; define business metrics as promoted calculated fields rather than per-view expressions; write ratios as aggregate over aggregate so they recompute at the view's level of detail; make analytical granularity a user choice via a parameter; scope global filters at the data source so headline figures respond; scope a secondary filter to a chosen subset of sheets via a filter group; repeat one visual grammar across many views; bind dashboard titles to sheet names so renaming propagates.

### 7. BUSINESS RULES, VALIDATION AND GOVERNANCE (sanitised)

**Business rules encoded, all three, all in Workbook 2:**

1. **What counts as attrition:** `IF [attrition flag] = 'Yes' THEN 1 ELSE 0 END`. No voluntary versus involuntary split, no tenure qualification, no status exclusion, no date window.
2. **What counts as active:** `SUM([headcount])- SUM([Attrition Count])`. The population is a closed set; this is a snapshot, not a point-in-time headcount, because no hire or termination date exists.
3. **How attrition rate is defined:** leavers over total headcount within the current view scope. No annualisation, no average-headcount denominator.

**Workbook 1 encodes no business rule at all.** Its aliases are label mappings, not rules.

**Validation checks: none are present in either workbook.** No reconciliation, no row count check, no control total, no step-change check, no regression check and no data-quality flag surfaced to users. Whether validation happened outside the tool: Not in chats.

**Governance:** metric definitions and data dictionary, Not in chats. Sign-off process and owners, Not in chats. Decision log, Not in chats. Open questions register, Not in chats. Documentation, Not in chats. Version control, Not in chats for a repository, though publish revision counters show at least two publishes per workbook, and Workbook 2's source folder name carries the suffix that a downloaded repository archive of a default branch produces.

**Defects found in inherited work:** Not in chats, no inherited work is identified.

**Defects verifiable in the delivered artefacts, all 15, all unfixed:** a misspelled outcome alias that renders in every legend; an untrimmed leading space in a lifestyle alias; a dashboard filter scoped to a sheet group that excludes all five KPI cards; seven bin sizes that match the tool's suggested defaults rather than chosen widths; no number formatting anywhere in Workbook 1; no custom tooltip on any of Workbook 1's 19 worksheets; three unused data sources in Workbook 2 still carrying extracts; six collision-artefact field captions; a worksheet titled as a rate that plots a count; no number formatting in Workbook 2, so the rate renders as a decimal; a persisted mark selection saved into 6 of 7 worksheets; a continuous colour encoding with no legend exposed; an unsorted bar chart; a dashboard name with a trailing space; and a parameter carrying three different names in three places.

### 8. REFRESH, OPERATIONS AND SECURITY (sanitised)

Refresh frequency: Not in chats, no schedule exists. Full or incremental: **full by construction**, every extract is configured for all records with no incremental key and no extract filter. Refresh trigger: Not in chats; both connect to local files, so a refresh requires the file to be present on that workstation.

How the source connects to the BI tool: direct local file read via the delimited text connector, then extracted. No server, no gateway, no DSN, no connection string, no credentials and no direct-query equivalent. The live-versus-extract choice is **extract**, in both workbooks, on all five data sources.

Access control: Not in chats. Both publish to a **public-by-default** hosting platform with no row-level security and no user-based access control. Credentials: `workgroup-auth-mode='as-is'` on every connection, the default for a file connection needing no authentication, so no credential is stored. Row-level security: **none**, no user filter or user function appears anywhere.

What data was allowed to leave the source systems: **no restriction, and none needed.** Both workbooks are packaged with full data extracts embedded, so publishing either one publishes the underlying records with it, downloadable by any viewer. **Both datasets are public**, confirmed by the author, so there is no disclosure issue.

Monitoring, failure handling and notification: Not in chats. None exists.

### 9. REQUIREMENTS TO KPIs, MEASURES AND DASHBOARD LOGIC (sanitised)

**How requirements were gathered:** Not in chats. No requirement, session, question list or stakeholder input is recorded.

**Workbook 1 KPIs, five:** cohort size as a count of non-null outcome values with no filter; leaver-equivalent death count as the same count filtered to the outcome member `1`; two demographic counts each filtered to one member of the demographic flag; and mean age. Owners and sign-off: Not in chats for all five. **None of the five responds to the dashboard filter**, because the five KPI worksheets sit outside the filter group. **There is no rate KPI in Workbook 1.**

**Workbook 2 KPIs, five:** headcount as a sum; attrition count as a sum of the conditional indicator; attrition rate as the aggregate ratio; active employees as the aggregate difference; and mean age. Owners and sign-off: Not in chats for all five. All five respond to the global filter and to all six cross-filter actions.

**Measures written.** No DAX and no SQL exists in either project. The actual calculation code is transcribed in the unsanitised section 9 and is unchanged here: one conditional indicator, one aggregate ratio, one aggregate difference, one auto-generated constant, one dual-axis placeholder, one parameter-bound bin definition, five string literals, one zero constant, and seven fixed bin definitions. **There are no level-of-detail expressions in either workbook.**

**Dashboard design, Workbook 1:** one dashboard, no story, no navigation. A KPI strip of 5 cards, a strip of 5 donuts crossing each binary attribute with the outcome, then 7 biomarker histograms plus 2 scatter-style views. Visuals: donut built as a dual-axis pie, stacked histogram, scatter, disaggregated dot plot with an average reference line scoped per cell, and text cards. One dropdown filter applied to 14 of 19 sheets. No drill paths. **Assumptions and definitions are not shown to the user at all**: no text object, no annotation, no caption and no custom tooltip. Canvas 1900 x 1050, range sizing, black, fully tiled with nested flow containers.

**Dashboard design, Workbook 2:** one dashboard, no story, no navigation. A header with a title text object and the global filter, a KPI band of 5 tiles plus a gender lollipop, a middle band with an organisational-unit pie, a parameterised age histogram and a role-by-satisfaction highlight table, and a bottom band with an education field bar chart and a row of age band donuts split by gender. One dropdown applied to all 7 sheets via data source scope, and one slider parameter control ranging 2.0 to 10.0 by 1.0 with a default of 3.0. No drill paths; cross-filtering by clicking substitutes for drill-down. Assumptions are partially shown: custom tooltips on all 7 sheets spell out field labels and name the table calculation explicitly, but there is no definition of the attrition rule and no assumptions panel. Canvas 1580 x 900, fixed sizing, floating objects over a background image.

**Anything the business explicitly asked for in the presentation:** Not in chats.

### 10. STAKEHOLDER COORDINATION (sanitised)

**Nothing in this section is available.** No name, role, comment, review, approval or coordination artefact exists in either workbook. Stakeholders, meetings, agreements, pushback, disagreement handling and framing to the business are all Not in chats. The only human trace in either file is a workstation account name inside file paths.

### 11. OUTCOMES AND STATUS (sanitised)

**What is live:** both workbooks were published to a public visualisation hosting platform, each at least twice, evidenced by advancing revision counters. Whether either is currently live could not be checked because the environment's network policy blocked the host.

**Both dashboards are complete builds:** every worksheet in each workbook is placed on its dashboard, 19 of 19 and 7 of 7, with no orphaned or unfinished worksheets.

**What is validated:** nothing. **What is signed off:** Not in chats. **What is still open:** the 15 verifiable defects listed in section 7, all unfixed in the delivered files.

**Measurable results:** Not in chats. No view count, adoption figure, time saving, grade, feedback or business outcome is recorded. Nothing can be claimed.

What can be counted: 2 dashboards, 26 worksheets, 19 calculated fields, 1 parameter, 9 distinct chart forms, 7 dashboard actions, 8 custom tooltip definitions, 13 of 13 and 15 of 39 source columns consumed, two BI tool versions across two operating system releases of the same platform, and at least two publish revisions per workbook.

**Lessons learned:** Not in chats. No retrospective, note or comment exists.

### 12. GAPS AND QUESTIONS (sanitised)

Unchanged from the unsanitised section 12, except that questions referencing a named institution, folder path or account name are rephrased generically. The 26 questions cover: who the work was for, dataset provenance, whether the clinical dataset is public given that full extracts are embedded and published, row counts, real dates and durations, how the pre-derived columns were produced, what the headcount column contains, whether the outcome column has nulls, whether any pre-Tableau cleaning happened, the source definition of the attrition flag, why counts and not a rate in Workbook 1, why the tool's suggested bin sizes were accepted, whether the KPI filter exclusion was deliberate, why four data sources exist, whether the rate-versus-count title mismatch was intentional, whether the collision-artefact captions were intentional, whether the persisted selection was deliberate, why different action types in each dashboard, where the background image came from, confirmed live URLs, any view counts or feedback, screenshots, post-publish changes, one concrete personal finding per dataset, which defects are agreed, and whether pipeline or modelling work exists elsewhere in the portfolio.

---

### Substitution list

Check this list to confirm nothing identifying remains.

| # | Original in the unsanitised document | Replaced with |
|---|---|---|
| 1 | `Tableau`, `Tableau Desktop`, `Tableau Public` | "BI desktop tool", "public visualisation hosting platform" |
| 2 | `Hyper`, `.hyper` | "columnar in-memory extract" |
| 3 | `textscan` connector | "delimited text connector" |
| 4 | `excel-direct` connector | "spreadsheet connector" |
| 5 | `atharvadevne` (macOS account name in file paths) | "workstation account name" |
| 6 | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` | "a folder path containing a university name and a data visualisation course name" |
| 7 | `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` | "the same folder on the same workstation"; the `-main` suffix described as "the suffix that a downloaded repository archive of a default branch produces" |
| 8 | `UIC` | "a university" |
| 8a | `Kaggle` | "a public data-sharing platform" |
| 8b | `Atharva Devne` | "the author" |
| 9 | `Healthcare - Heart Failure.twb` | "Workbook 1" |
| 10 | `HR Analytics Dashboard.twb` | "Workbook 2" |
| 11 | `heart_failure_clinical_records_dataset.csv` | "one CSV of clinical records" |
| 12 | `HR_data.csv`, `HR data.csv`, `HR data.xlsx`, `HR Data.xlsx - HR data.csv` | "four files of the same dataset in different formats and naming conventions" |
| 13 | `Healthcare-HeartFailure_17429983482570`, `HRAnalyticsDashboard_17561606616710` | omitted entirely from the sanitised version |
| 14 | `public.tableau.com` | "the host" |
| 15 | `Image/HR background.pptx.png` | "a background image" |
| 16 | `anaemia`, `diabetes`, `high_blood_pressure` | "comorbidity flag A / B / C" |
| 17 | `smoking` | "lifestyle flag" |
| 18 | `sex` | "demographic flag" |
| 19 | `DEATH_EVENT` | "mortality outcome" / "outcome flag column" |
| 20 | `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium` | "five biomarker measures" |
| 21 | `time` | "follow-up period" |
| 22 | `Department`, `Department1` | "organisational unit" |
| 23 | `Education`, `Education1` | "education level" |
| 24 | `Education Field`, `Education Field1` | "education field" |
| 25 | `Gender`, `Gender1` | "gender" (retained, it is a generic attribute name) |
| 26 | `Job Role`, `Job Role1` | "job role" (retained, generic) |
| 27 | `Job Satisfaction`, `Job Satisfaction1` | "satisfaction score" |
| 28 | `Attrition` | "attrition flag" |
| 29 | `Employee Count` | "headcount column" |
| 30 | `Employee Number`, `emp no` | "identifier column" |
| 31 | `CF_age band`, `CF_attrition label`, `CF_current Employee` | "three pre-derived columns: an age band, an attrition label and a current-employee flag" |
| 32 | `R&D` (the persisted selection member) | "a persisted mark selection" |
| 33 | Federated data source ids such as `federated.0f0h03p1it3gvo176rhln1y1tx4v` | omitted entirely |
| 34 | Internal calculation ids such as `[Calculation_231935388807032832]` | replaced with the readable field name |
| 35 | Dashboard names `Dashboard 1` and `HR Dashboard ` | "the dashboard", with the trailing-space defect described but not reproduced with its name |
| 36 | Worksheet names such as `Sheet 6 (9)`, `Attrition Rate by Gender for Different Age Group` | described by chart type and content |
| 37 | Dashboard UUIDs | omitted entirely |
| 38 | `macOS` | "workstation" or "operating system" |
| 39 | `2025.1.0`, `2025.2.0` and their build strings | "version 2025.1.0" and "version 2025.2.0" retained as tool versions, build strings retained as dates only |

**Items deliberately NOT substituted, and why:** all formulas, bin sizes, decimal settings, alias values, colour hex codes, canvas dimensions, zone counts, filter scopes, action counts, worksheet counts, column counts, parameter ranges and sort dictionaries are unchanged, because the instruction was to keep all technical detail, counts, rules and logic intact. The alias values `Surivive` and `` ` Non-Smoker` `` are retained verbatim because they are the defect itself. The age band dictionary is retained verbatim because it is the sort rule. Generic role and attribute words such as gender, job role, age and headcount are retained because they are not identifying.

**One item to check yourself:** the sanitised version still states that Workbook 1 concerns cardiac patient survival and Workbook 2 concerns workforce attrition. If the subject matter itself is sensitive, those need replacing too, with something like "a clinical outcome dataset" and "a workforce dataset".
