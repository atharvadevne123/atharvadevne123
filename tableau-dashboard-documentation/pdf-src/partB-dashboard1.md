# PART B: HANDS-ON EVIDENCE BRIEF, DASHBOARD 1

Scoped to `Healthcare - Heart Failure` only. Structured for a hiring manager confirming hands-on experience.

**Evidence base.** The packaged workbook `Healthcare - Heart Failure.twb`, parsed from its XML, plus a short set of answers the author gave directly. The two are kept clearly apart throughout. Where neither supplies an answer, the entry reads **"Not recorded"** and the question appears in section 12.

**Confirmed by the author, not by the file:**

| Item | Answer |
|---|---|
| Author | Atharva Devne |
| Why it was built | **Self-directed, for the author's own skill development.** Not a course, not a client, not an employer. |
| Dataset origin | **Kaggle** |
| Dataset public? | **Yes.** This resolves the only disclosure concern the file raised, since the workbook embeds a full extract and publishes to Tableau Public. |

**Scope note.** This is an individual Tableau dashboard build over one local flat file. It is not pipeline, warehouse or platform work, and this brief does not pretend otherwise. Sections 2, 4, 6, 8 and 10 are therefore short, and the reasons are stated rather than padded.

---

## 1. PROJECT CONTEXT

| Item | Detail |
|---|---|
| Business problem | No stated problem. The workbook contains no description, annotation, caption or text object of any kind. What the build addresses, read from its structure: every one of the 14 charts encodes `Death Event` on Colour and 12 chart titles end in `- Survival Stats`, so it is a **survival profiling** view. For each recorded clinical or demographic attribute, show how the cohort splits between `Surivive` and `Death`. |
| Who requested it | **Nobody.** Self-directed. |
| What decisions it supports | No external decision. The purpose was the author's own skill development. What it mechanically enables a reader to ask is in Part A section 16. |
| My role | Sole author and sole builder. Every layer is one person's work: connection, extract, semantic layer, calculations, 19 worksheets, dashboard layout, filter scoping, action design, publication. |
| Who else was involved | Nobody. No collaborators, no reviewers. The workbook contains no second person: every data source is `inline='true'` (embedded, not published to a server) and every connection points at one local file on one machine. |
| Timeline | Not recorded. |
| Tool | Tableau Desktop, `source-build='2025.1.0 (20251.25.0313.2002)'`, `source-platform='mac'`, document format `version='18.1'`. |
| Current status | **Published to Tableau Public.** `repository-location` id `Healthcare-HeartFailure_17429983482570`, derived from `?rev=1.1`, current `revision='1.2'`, so at least two publish revisions. Whether it is live right now could not be checked: the network policy in the documenting environment denied `public.tableau.com`. |

---

## 2. SOURCE SYSTEM AND DATA INVENTORY

**There is no source system in the enterprise sense.** No database, no API, no SharePoint, no shared folder, no server. One local CSV on one Mac.

| Attribute | Value |
|---|---|
| System | Local file system |
| Connector | `textscan`, Tableau's delimited text file connector |
| File | `heart_failure_clinical_records_dataset.csv` |
| Path | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` |
| Named connection id | `textscan.0eo7kao1bn80dv0zsqdco0t9bxql` |
| Parsing configuration | `character-set='UTF-8'`, `separator=','`, `header='yes'`, `locale='en_US'` |
| Relation | `<relation name='heart_failure_clinical_records_dataset.csv' table='[heart_failure_clinical_records_dataset#csv]' type='table' />` |
| Schema | 13 columns, flat, no key declared |
| Provenance | **Kaggle, public dataset.** Confirmed by the author. |
| Owner | Publicly available, no internal owner |
| Access method | Direct file read, then full extract to Hyper |
| Legacy versus current | Not applicable, one file, no history, no second system |

### Exact schema, with ordinals and declared types

| Ordinal | Column | Declared type | Tableau `remote-type` |
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

Every metadata record carries `<contains-null>true</contains-null>` and the shared `object-id` `[heart_failure_clinical_records_dataset.csv_6F1533318D5F4C8AB71453465976CF29]`. The null flag is Tableau's default optimistic value on a scanned text file, **not** evidence that nulls exist.

**All 13 columns are consumed.** Nothing in this dataset was imported and then ignored.

---

## 3. SOURCE-TO-TARGET MAPPING

| Target field | Source field | Transformation rule | Notes |
|---|---|---|---|
| `Age` | `age` | Caption rename only. Type `real`, role measure. | Used as `AVG` on the KPI, `CNT` on the histogram, unaggregated on the scatter |
| `Death Event` | `DEATH_EVENT` | Caption rename; role measure → dimension `ordinal`; alias `0` → `Surivive`, `1` → `Death` | **The alias is literally `Surivive` in the file, a typo for "Survive", and it renders that way in every legend and label** |
| `Anaemia` | `anaemia` | Caption rename; role → dimension `ordinal`; alias `0` → `Negative`, `1` → `Positive` | |
| `Diabetes` | `diabetes` | Same pattern | |
| `High Blood Pressure` | `high_blood_pressure` | Same pattern | |
| `Sex` | `sex` | Caption rename; role → dimension `ordinal`; alias `0` → `Female`, `1` → `Male` | |
| `Smoking` | `smoking` | Caption rename; role → dimension `ordinal`; alias `0` → `" Non-Smoker"`, `1` → `Smoker` | **The `Non-Smoker` alias carries a leading space** |
| `Creatinine Phosphokinase` | `creatinine_phosphokinase` | Caption rename only | |
| `Ejection Fraction` | `ejection_fraction` | Caption rename only | |
| `Platelets` | `platelets` | Caption rename only | |
| `Serum Creatinine` | `serum_creatinine` | Caption rename only | |
| `Serum Sodium` | `serum_sodium` | Caption rename only | |
| `Time` | `time` | Caption rename only | Integer follow-up period, **not a date** |
| `Age (bin)` | `age` | `class='bin'`, `size='4.48'`, `peg='0'`, `decimals='0'` | |
| `Creatinine Phosphokinase (bin)` | `creatinine_phosphokinase` | `class='bin'`, `size='376'`, `peg='0'`, `decimals='2'` | |
| `Ejection Fraction (bin)` | `ejection_fraction` | `class='bin'`, `size='8.22'`, `peg='0'`, `decimals='0'` | |
| `Platelets (bin)` | `platelets` | `class='bin'`, `size='41767'`, `peg='0'`, `decimals='4'` | |
| `Serum Creatinine (bin)` | `serum_creatinine` | `class='bin'`, `size='0.772'`, `peg='0'`, `decimals='-1'` | |
| `Serum Sodium (bin)` | `serum_sodium` | `class='bin'`, `size='3.57'`, `peg='0'`, `decimals='0'` | |
| `Time (bin)` | `time` | `class='bin'`, `size='15.1'`, `peg='0'`, `decimals='1'` | |
| `Total Individuals` | none | `"Total Individuals"` | String literal, KPI caption |
| `Total Deaths` | none | `"Total Deaths"` | String literal, KPI caption |
| `Total Males` | none | `"Total Males"` | String literal, KPI caption |
| `Total Females` | none | `"Total Females"` | String literal, KPI caption |
| `Average Age` | none | `"Average Age"` | String literal, KPI caption |
| `0` | none | `0` | Dual-axis placeholder measure |

**Fields whose meaning differed between systems.** Not applicable. One system, so no cross-system semantic mismatch existed and none was resolved.

### Grain

| Object | Grain |
|---|---|
| Source | One row per patient. Inferred from the schema: no patient identifier, no repeated-measure column, no date, and every column is a single clinical attribute. |
| KPI sheets | Whole cohort, no dimensions |
| Donuts | One mark per `Death Event` x comorbidity combination |
| Histograms | One mark per bin x `Death Event` |
| `Sheet 6 (8)` scatter | One mark per distinct `age` x `time` combination |
| `Sheet 6 (9)` dot plot | **Record grain**, because `aggregation='false'` |

**Grain mismatches: none.** Every target aggregates upward from a single-grain source. No fan-out, no many-to-many, no double-counting risk, because there is no join anywhere.

---

## 4. DATA FLOW AND ARCHITECTURE

No orchestration tool, no staging layer, no warehouse, no lakehouse, no scheduler.

```
[1] Local CSV on a Mac                            TOOL: none, manual placement
    heart_failure_clinical_records_dataset.csv
        v
[2] Tableau Desktop 2025.1.0, macOS               TOOL: Tableau Desktop
    textscan connector: UTF-8, comma, header, en_US
        v
[3] Tableau Hyper extract                         TOOL: Tableau Desktop
    <extract enabled='true' count='-1' units='records'>
    materialised as Data/tableau-temp/#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper
        v
[4] Semantic layer, inside the workbook           TOOL: Tableau Desktop
    13 captions, 6 role conversions, 6 alias sets, 7 bins, 6 calculated fields
        v
[5] 19 worksheets
        v
[6] Dashboard "Dashboard 1", 1900 x 1050
        v
[7] Tableau Public
    Healthcare-HeartFailure_17429983482570, revision 1.2
```

| Stage | Where data lands |
|---|---|
| Source | Local file system |
| Staging | **None** |
| Warehouse / lakehouse | **None** |
| Curated files | The Hyper extract inside the packaged workbook. The only materialised intermediate. |
| Serving | Tableau Public |

**Inherited or previous architecture:** none. Nothing in the workbook records a predecessor, a migration or a rebuild.

**Flow in boxes and arrows:** local CSV → Tableau Desktop textscan connector → Hyper extract (all records, no filter) → semantic layer (captions, roles, aliases, bins) → 19 worksheets → 1 dashboard → Tableau Public. A side box, "filter scoping and one highlight action", feeds into the dashboard box. There are no other boxes: no SQL step, no Python step, no Power Query, no Alteryx, no Airflow, no dbt.

---

## 5. DATA CONSOLIDATION, CLEANING AND STANDARDISATION

**No consolidation occurred.** One table in, one table used.

### Every cleaning rule applied, all four

| # | Rule | Exact definition | Fields affected | Layer | Why there |
|---|---|---|---|---|---|
| 1 | Display renaming | `caption` attribute on `<column>` | All 13 source columns | Data source | Defined once, inherited by all 19 worksheets |
| 2 | Role reclassification | `role='dimension' type='ordinal'` | `DEATH_EVENT`, `anaemia`, `diabetes`, `high_blood_pressure`, `sex`, `smoking` | Data source | Tableau imports 0/1 integers as measures and defaults to `SUM`, which is meaningless for a flag. Dimensions can drive Colour, Label and Filter. |
| 3 | Code-to-label standardisation | `<aliases enabled='yes'>` with explicit key/value pairs | 6 fields, 12 aliases | Data source | Same reason: one definition, 19 inheritors |
| 4 | Binning | `<calculation class='bin' ... />` | 7 continuous measures | Data source | Required to draw a distribution of a continuous measure |

### Exact alias mappings

| Field | Key | Aliased value |
|---|---|---|
| `DEATH_EVENT` | `0` | `Surivive` |
| `DEATH_EVENT` | `1` | `Death` |
| `anaemia` | `0` / `1` | `Negative` / `Positive` |
| `diabetes` | `0` / `1` | `Negative` / `Positive` |
| `high_blood_pressure` | `0` / `1` | `Negative` / `Positive` |
| `sex` | `0` / `1` | `Female` / `Male` |
| `smoking` | `0` / `1` | `" Non-Smoker"` (leading space) / `Smoker` |

### Cleaning rules NOT applied

Stated so nothing is over-claimed.

| Rule category | Status |
|---|---|
| Null handling (`ISNULL`, `IFNULL`, `ZN`) | **Not present** |
| Duplicate detection or removal | **Not present** |
| Explicit type casting (`INT()`, `STR()`, `FLOAT()`, `DATE()`) | **Not present.** All types came from the CSV scan. |
| Date parsing, date parts, timezone handling | **Not present, and not possible.** The dataset has no date column. `time` is an integer follow-up period. |
| Text normalisation (`TRIM`, `UPPER`, `REPLACE`, `REGEXP`) | **Not present.** Note that the workbook's own `" Non-Smoker"` alias is itself untrimmed. |
| Outlier detection or capping | **Not present** |
| Country, currency or unit standardisation | **Not present.** No such field exists. |
| Domain classification logic | **Not present** |
| Referential validation | **Not present.** No joins to validate. |
| Data source filter | **Not present** |
| Extract filter | **Not present** |
| Tableau Prep flow | **Not present** in the archive |
| Groups, sets, hierarchies | **Not present** |

### Which layer performed each transformation, and why there

All of it was done inside Tableau Desktop. No SQL, no Python, no Prep flow is referenced anywhere. Whether anything was cleaned before Tableau is **not recorded**.

Within Tableau, a deliberate layering is visible:

| Layer | What sits there | Why |
|---|---|---|
| Data source scope | Captions, role conversions, aliases, bins | Defined once, inherited everywhere. Changing one alias updates 19 sheets. |
| Calculated field scope | 7 bins, 5 string literals, the `0` placeholder | Reusable across sheets |
| Worksheet scope | The three hard-coded KPI member filters | Local to one card, no reason to promote |
| Dashboard scope | Sex filter control, colour legend, highlight action | Interaction, not data |

---

## 6. DATA MODEL: SCHEMA AND TABLE DESIGN

**No dimensional model was designed.** This is the single most important scope boundary to understand about this artefact.

| Design element | Status |
|---|---|
| Fact tables | **None** |
| Dimension tables | **None** |
| Star or snowflake schema | **None** |
| Surrogate key strategy | **None.** No key column is declared or used. |
| Slowly changing dimensions | **None** |
| Date dimension | **None, and impossible.** No date column exists. |
| Relationships and filter directions | **None.** One table. |
| Historical migration or backfill | **None** |
| Cutover between systems | **Not applicable** |
| Cardinality and referential integrity settings | **Not applicable** |

### Design rules that WERE set, and the reason for each

Real, verifiable structural decisions, even though they are not dimensional modelling decisions.

| # | Rule | Evidence | Reason |
|---|---|---|---|
| 1 | Extract everything, filter nothing at extract time | `count='-1'`, no extract filter | Keeps the workbook self-contained and keeps all filtering interactive |
| 2 | Embed the data source rather than publish it | `inline='true'` | Self-contained portfolio artefact |
| 3 | Binary flags are dimensions, not measures | `role='dimension' type='ordinal'` on 6 fields | Prevents meaningless `SUM` on a flag; enables Colour, Label, Filter |
| 4 | Decode codes at the source, not in the view | `<aliases enabled='yes'>` at data source level | One definition, 19 inheritors |
| 5 | Scope a filter to a chosen subset of sheets | `filter-group='3'` on 14 of 19 sheets | Applies one control to the charts. Consequence: the 5 KPI cards are excluded. |
| 6 | One visual grammar, repeated | 5 structurally identical donuts, 7 structurally identical histograms | The reader learns the chart once and reads six more for free |
| 7 | Hide axes that carry no information | `major-show='false'`, blank axis titles on the donut sheets | The constant `0` axis exists only to enable the dual axis |

---

## 7. BUSINESS RULES, VALIDATION AND GOVERNANCE

### Business rules encoded

**None.** This workbook encodes no business rule at all. Its aliases are label mappings, not rules. There is no classification logic, no exclusion, no threshold, no derived category and no conditional expression anywhere in it. The only decision logic is the three hard-coded member filters on the KPI cards (`DEATH_EVENT = 1`, `sex = 1`, `sex = 0`), and those are filters, not rules.

### Validation checks

**None are present.** A complete absence, not an omission from this brief.

| Check type | Present? |
|---|---|
| Reconciliation to source | **No.** No reconciliation sheet, control total or comparison view. |
| Control totals | **No** |
| Cross-system checks | Not applicable, one system |
| Step-change or regression checks | **No** |
| Data-quality flags shown to users | **No.** No worksheet, annotation or field surfaces a quality indicator. |

Whether validation was performed outside Tableau is **not recorded**.

### Governance

| Item | Status |
|---|---|
| Metric definitions and data dictionary | **None.** No documentation field, description or dictionary. |
| Sign-off process and owners | **None.** Self-directed work, nothing to sign off. |
| Decision log | **None** |
| Open questions register | **None** |
| Documentation | **None** in the workbook |
| Version control | Tableau Public revision counters only: `revision='1.2'`, derived from `?rev=1.1`, so at least two publishes |

### Defects observable in the delivered artefact

Found by reading the XML, not reported by anyone. All six are **unfixed in the delivered file**.

| # | Defect | Evidence |
|---|---|---|
| 1 | The `DEATH_EVENT = 0` alias is spelled **`Surivive`**, a misspelling of "Survive", and it renders in every legend and label | `<alias key='0' value='Surivive' />` |
| 2 | The `smoking = 0` alias has a **leading space**: `" Non-Smoker"` | `<alias key='0' value=' Non-Smoker' />` |
| 3 | The Sex dashboard filter is scoped to `filter-group='3'`, covering 14 of 19 sheets and **excluding all five KPI cards**, so the headline numbers do not move when the filter is used | Filter group membership per worksheet |
| 4 | All 7 bin sizes are non-round values (`4.48`, `8.22`, `0.772`, `3.57`, `15.1`, `376`, `41767`), consistent with Tableau's suggested defaults rather than chosen widths | Bin `size` attributes |
| 5 | **No number formatting** is defined anywhere | No `number-format` attribute in the file |
| 6 | **No custom tooltip** on any of the 19 worksheets | No `<customized-tooltip>` element in the file |

A seventh point, not a defect but a design consequence worth being able to defend: `Total Individuals` uses `CNT([DEATH_EVENT])` rather than `COUNT(*)` or an explicit `Number of Records`. It counts non-null values, so it equals the cohort size only if `DEATH_EVENT` is never null.

---

## 8. REFRESH, OPERATIONS AND SECURITY

| Item | Status |
|---|---|
| Refresh frequency | **Not recorded.** No schedule, no incremental configuration, no refresh definition exists. |
| Full or incremental | **Full, by construction.** `count='-1' units='records'`, no incremental refresh key, no extract filter. An extract configured this way refreshes in full when refreshed at all. |
| Refresh trigger | The connection is to a local file, so a refresh requires that file to be present on that Mac and a manual refresh to be run. |
| How the source connects to Tableau | Direct local file read via the `textscan` connector, then extract. **No server, no gateway, no DSN, no connection string, no credentials, no DirectQuery equivalent.** The live-versus-extract choice is **extract**. |
| Connection parameters | Text parsing options only: `UTF-8`, `,`, header row, `en_US` |
| Credentials handling | `workgroup-auth-mode='as-is'`, the default for a file connection needing no authentication. No credential is stored, because none is needed. |
| Access control | Published to **Tableau Public**, which is public by default with no user-based access control. |
| Row-level security | **None.** No user filter, no `USERNAME()`, no `ISMEMBEROF()`, no user function appears anywhere. |
| Workspace administration | Not applicable. Tableau Public has no workspace model. |
| What data was allowed to leave the source | **No restriction, and none needed.** The workbook is packaged with a full data extract embedded, so publishing it publishes the underlying records, downloadable by any viewer. **The dataset is a public Kaggle dataset**, confirmed by the author, so there is no disclosure issue. Worth stating explicitly: embedding a full extract in a public workbook would be a real problem with any non-public source, and knowing that distinction is the point. |
| Monitoring, failure handling, notification | **None.** No alert, subscription or notification is configured. |

---

## 9. REQUIREMENTS TO KPIs AND DASHBOARD LOGIC

### How requirements were gathered

**No requirements were gathered.** Self-directed work with no stakeholder, no brief and no session. Nothing is recorded in the workbook either.

### KPI list

| KPI | Business definition | Decision it supports | Grain | Source fields | Calculation logic | Owner | Sign-off |
|---|---|---|---|---|---|---|---|
| `Total Individuals` | Count of patients in the cohort | Sets the base for reading every other figure | Whole cohort, unfiltered | `DEATH_EVENT` | `CNT([DEATH_EVENT])`, no filter | Author | None, self-directed |
| `Total Deaths` | Count of patients with the mortality flag set | Absolute mortality volume | Filtered to `DEATH_EVENT = 1` | `DEATH_EVENT` | `CNT([DEATH_EVENT])` with worksheet filter `member='1'` | Author | None |
| `Total Males` | Count of male patients | Cohort sex composition | Filtered to `sex = 1` | `sex` | `CNT([sex])` with worksheet filter `member='1'` | Author | None |
| `Total Females` | Count of female patients | Cohort sex composition | Filtered to `sex = 0` | `sex` | `CNT([sex])` with worksheet filter `member='0'` | Author | None |
| `Average Age` | Mean patient age | Frames the age distribution below it | Whole cohort, unfiltered | `age` | `AVG([age])` | Author | None |

**None of the five responds to the dashboard's Sex filter**, because the five KPI worksheets sit outside `filter-group='3'`.

**There is no rate KPI.** Mortality rate is never computed as a KPI, only counts and one mean.

### Measures written, actual code

No DAX and no SQL exists. The Tableau code, transcribed exactly:

```
// The five KPI caption fields
"Total Individuals"
"Total Deaths"
"Total Males"
"Total Females"
"Average Age"

// Dual-axis placeholder
0

// The seven bin definitions
class = bin, formula = [age],                      size = 4.48,  peg = 0, decimals = 0
class = bin, formula = [creatinine_phosphokinase], size = 376,   peg = 0, decimals = 2
class = bin, formula = [ejection_fraction],        size = 8.22,  peg = 0, decimals = 0
class = bin, formula = [platelets],                size = 41767, peg = 0, decimals = 4
class = bin, formula = [serum_creatinine],         size = 0.772, peg = 0, decimals = -1
class = bin, formula = [serum_sodium],             size = 3.57,  peg = 0, decimals = 0
class = bin, formula = [time],                     size = 15.1,  peg = 0, decimals = 1

// The one table calculation, applied on 5 sheets
<table-calc ordering-type='Rows' type='PctTotal' />
```

**There are no LOD expressions.** Verified by absence of `{` in every formula.

### Dashboard design

| Item | Value |
|---|---|
| Pages | 1 dashboard, no story, no navigation |
| What it shows | Top strip: 5 KPI cards. Second strip: 5 donuts, one per binary attribute, crossed with the survival outcome. Third and fourth strips: 7 biomarker histograms plus 2 scatter-style views. |
| Visuals used | Donut built as a dual-axis pie, stacked histogram, scatter, disaggregated dot plot with a per-cell average reference line, text cards |
| Filters shown to the user | 1 dropdown, `Sex`, applied to 14 of 19 sheets |
| Parameter controls | **None.** There are no parameters. |
| Drill paths | **None.** No hierarchy exists. |
| How assumptions and definitions are shown to the user | **They are not.** No text object, no annotation, no caption, no custom tooltip anywhere on this dashboard. |
| Canvas | 1900 x 1050, `sizing-mode='range'`, black, fully tiled with nested flow containers |

**Anything the business explicitly asked for in the presentation:** nothing. There was no business.

---

## 10. STAKEHOLDER COORDINATION

**Nothing to report, and that is accurate rather than a gap in the evidence.** The project was solo and self-directed. There were no stakeholders, no meetings, no working sessions, no agreements, no pushback and no disagreements to handle. The workbook contains no name, comment, review or approval artefact of any kind.

---

## 11. OUTCOMES AND STATUS

| Item | Status |
|---|---|
| What is live | Published to Tableau Public, workbook id `Healthcare-HeartFailure_17429983482570`, dashboard repository id `Dashboard1`. Published at least twice (revision advanced `1.1` → `1.2`). Whether currently live could not be checked, the documenting environment's network policy denied `public.tableau.com`. |
| Completeness | **Complete build.** All 19 worksheets in the workbook are placed on the dashboard. No orphaned, unfinished or staged worksheets. |
| What is validated | **Nothing.** No validation artefact exists. |
| What is signed off | Not applicable, self-directed. |
| What is still open | The 6 defects in section 7, all unfixed. The three most consequential: the `Surivive` misspelling, the KPI cards being outside the filter scope, and the absence of any custom tooltip across 19 worksheets. |

### Measurable results

**None can be claimed.** No view count, adoption figure, time saving, grade, feedback or business outcome exists. No data values were read either, because the `.hyper` extract is binary and no Hyper reader was available, so no mortality rate, distribution shape or correlation can be stated.

What can be counted, and only this:

| Metric | Value |
|---|---|
| Worksheets built | 19 |
| Worksheets placed on the dashboard | 19 of 19 |
| Calculated fields authored | 13 |
| Source columns consumed | 13 of 13 |
| Distinct chart forms | 5 |
| Dual-axis constructions | 5 |
| Table calculations | 1 type, on 5 sheets |
| Reference lines | 1 |
| Value aliases defined | 12, across 6 fields |
| Dashboard actions | 1 |
| Custom worksheet titles | 14 |
| Publish revisions | at least 2 |

### Lessons learned

Not recorded in the workbook. The defect list in section 7 is an external reading of the file, not a record of anything the author wrote down.

---

## 12. GAPS AND QUESTIONS

### Already answered

| Question | Answer |
|---|---|
| Was this for a course, a client, or self-directed? | **Self-directed, for your own development.** The `UIC/Business Data Visualization` folder is just where the file sat. |
| Where did the dataset come from? | **Kaggle.** |
| Is the dataset public, given the embedded extract? | **Yes, public. No disclosure issue.** |

### Still open

1. **Was the CSV cleaned before it reached Tableau?** If yes, with what tool and what exact rules?
2. **Does `DEATH_EVENT` contain any nulls?** `CNT([DEATH_EVENT])` is the cohort-size KPI and it counts non-nulls, so nulls would silently understate it.
3. **Why counts and no mortality rate?** Was a rate considered and rejected?
4. **Why were Tableau's suggested bin sizes accepted** (`4.48`, `8.22`, `0.772`, `3.57`, `15.1`)? Was a clinically meaningful width considered?
5. **Was excluding the KPI cards from the Sex filter deliberate**, so the cards act as a constant baseline, or an oversight?
6. **Why a highlight action rather than filter actions?** This is a genuinely good design question and a strong answer lands well.
7. **Why no custom tooltips across 19 worksheets?** Deliberate minimalism on a dark theme, or not reached?
8. **Did anyone review or use it**, and what did they say?
9. **The confirmed live Tableau Public URL.** The recoverable id is `Healthcare-HeartFailure_17429983482570`.
10. **Any view counts or feedback?**
11. **What changed between the two publish revisions?**
12. **One concrete insight you personally found** in this dataset while building. Not a figure the dashboard computes, but something you noticed. Interviewers ask "what did you find", and "the dashboard lets you find X" is a weaker answer than "I found X".
13. **Which of the 6 defects do you agree with**, and does any have an explanation this reading has missed?

---

## 13. SANITISED VERSION

The same brief with identifying details replaced. All technical detail, counts, rules and logic unchanged.

**1. Project context.** Self-directed work by a single author for their own skill development, not for a course, client or employer. No requester, no stakeholder, no collaborators. Subject matter inferable from structure: profiling patient survival in a cardiac care dataset, evidenced by 12 of 14 chart titles ending in a survival-statistics suffix and a mortality outcome field on the Colour shelf of every chart. The workbook contains no description, annotation, caption or text object. BI tool version 2025.1.0 on a workstation. Published to a public visualisation hosting platform, at least twice.

**2. Source system and data inventory.** No enterprise source system. One local delimited file on one workstation, read through the delimited text connector with `character-set='UTF-8'`, `separator=','`, `header='yes'`, `locale='en_US'`, one relation of `type='table'`, 13 columns, no key declared. Provenance: a public dataset from a public data-sharing platform. Schema: patient age (real), four binary comorbidity or lifestyle flags (integer), five continuous biomarker measurements (three real, two integer), a binary demographic flag (integer), an integer follow-up period, and a binary mortality outcome (integer). All 13 columns are consumed. Every metadata record carries the connector's default optimistic null flag, which is not evidence that nulls exist.

**3. Source-to-target mapping.** Thirteen source columns mapped as: caption rename on all 13; role conversion measure → dimension `ordinal` on six binary flags; value aliases decoding `0` and `1` into readable terms on those same six, including a misspelled survival label and an untrimmed leading space on one lifestyle label; seven bin fields with `peg='0'` and fixed sizes `4.48`, `376`, `8.22`, `41767`, `0.772`, `3.57`, `15.1` and `decimals` `0`, `2`, `0`, `4`, `-1`, `0`, `1`; five string-literal caption fields; and one constant `0` dual-axis placeholder. No cross-system semantic mismatch existed, because there is one system. Source grain is one row per patient; target grains range from whole-cohort to record grain on the one worksheet with aggregation switched off. No grain mismatches, because no join exists.

**4. Data flow.** Local delimited file → BI desktop tool, delimited text connector → columnar in-memory extract, all records, no filter → semantic layer (captions, roles, aliases, bins) → 19 worksheets → one dashboard → public hosting platform. No staging, no warehouse, no lakehouse, no scheduler, no SQL step, no scripting step, no ETL tool. No inherited architecture.

**5. Cleaning and standardisation.** No consolidation, one table. Four rules: display renaming on all 13 columns at data source scope; role reclassification on six binary integer columns because the tool imports them as measures and defaults to summing a flag; code-to-label standardisation via data source aliases, six fields and twelve pairs; and binning of seven continuous measures. Not applied: null handling, duplicate detection, explicit type casting, date parsing or timezone handling (impossible, no date column), text normalisation, outlier treatment, unit or code standardisation, referential validation, data source filter, extract filter, external preparation flow, groups, sets, hierarchies. All work was done inside the BI tool across four deliberate layers: data source scope for anything inherited everywhere, calculated field scope for reusable definitions, worksheet scope for view-local devices, dashboard scope for interaction.

**6. Data model.** No dimensional model. No fact or dimension tables, no surrogate keys, no slowly changing dimensions, no date dimension (impossible, no date column), no relationships, no migration, no cutover. Seven design rules were set and are listed with reasons: extract everything and filter nothing at extract time; embed rather than publish the data source; treat binary flags as dimensions; decode codes at the source; scope a filter to a chosen subset of sheets; repeat one visual grammar; hide axes that carry no information.

**7. Business rules, validation, governance.** No business rule is encoded at all; the aliases are label mappings, not rules. No validation checks of any kind: no reconciliation, control total, step-change check, regression check or data-quality flag. No data dictionary, sign-off, decision log or documentation. Version control limited to publish revision counters. Six defects are verifiable in the delivered file, all unfixed: a misspelled outcome label that renders in every legend; an untrimmed leading space in one lifestyle label; a dashboard filter scoped to a sheet group that excludes all five KPI cards; seven bin sizes matching the tool's suggested defaults rather than chosen widths; no number formatting anywhere; and no custom tooltip on any of the 19 worksheets.

**8. Refresh, operations, security.** Refresh frequency not recorded. Full by construction: all records, no incremental key, no extract filter. Direct local file read then extract, with no server, gateway, DSN, connection string, credentials or direct-query equivalent. Authentication mode is the default for a file connection needing none, so no credential is stored. Published to a public-by-default platform with no user-based access control and no row-level security; no user function appears anywhere. The workbook embeds a full extract, so publishing it publishes the records, but the dataset is public so there is no disclosure issue. No monitoring, failure handling or notification.

**9. Requirements to KPIs.** No requirements were gathered; the work was self-directed. Five KPIs: cohort size as a count of non-null outcome values with no filter; a death count as the same count filtered to the outcome member `1`; two demographic counts each filtered to one member of the demographic flag; and a mean age. None of the five responds to the dashboard filter. There is no rate KPI. No DAX and no SQL; the actual code is five string literals, one zero constant, seven bin definitions and one built-in percent-of-total table calculation, all transcribed unchanged in the full section 9. No level-of-detail expressions. Dashboard: one page, a KPI strip of five cards, a strip of five donuts crossing each binary attribute with the outcome, then seven biomarker histograms and two scatter-style views, on a 1900 x 1050 range-sized dark canvas, fully tiled with nested flow containers. One dropdown filter on 14 of 19 sheets, no parameter controls, no drill paths. Assumptions and definitions are not shown to the user at all.

**10. Stakeholder coordination.** None. Solo, self-directed work with no stakeholders, meetings, agreements or disagreements.

**11. Outcomes and status.** Published at least twice to a public hosting platform. Complete build: all 19 worksheets placed on the dashboard, none orphaned. Nothing validated, nothing signed off, six defects still open. No measurable results can be claimed and no data values were read. Countable facts: 19 worksheets, 13 calculated fields, 13 of 13 source columns consumed, 5 distinct chart forms, 5 dual-axis constructions, 1 table calculation type on 5 sheets, 1 reference line, 12 value aliases, 1 dashboard action, 14 custom titles, at least 2 publish revisions.

**12. Gaps and questions.** Three answered (self-directed, public data-sharing platform origin, dataset is public). Thirteen still open, listed in full in the unsanitised section 12, covering pre-tool cleaning, nulls in the outcome column, why counts and not a rate, why default bin widths, whether the KPI filter exclusion was deliberate, why a highlight action, why no tooltips, review and feedback, the confirmed live URL, view counts, what changed between revisions, one concrete personal finding, and which defects are agreed.

### Substitution list

| # | Original | Replaced with |
|---|---|---|
| 1 | `Tableau`, `Tableau Desktop`, `Tableau Public` | "BI desktop tool", "public visualisation hosting platform" |
| 2 | `Hyper`, `.hyper` | "columnar in-memory extract" |
| 3 | `textscan` connector | "delimited text connector" |
| 4 | `Atharva Devne` | "a single author" / "the author" |
| 5 | `atharvadevne` (account name in file paths) | omitted |
| 6 | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` | omitted |
| 7 | `UIC` | omitted |
| 8 | `Kaggle` | "a public data-sharing platform" |
| 9 | `Healthcare - Heart Failure.twb` | "the workbook" |
| 10 | `heart_failure_clinical_records_dataset.csv` | "one local delimited file" |
| 11 | `Healthcare-HeartFailure_17429983482570` | omitted |
| 12 | `public.tableau.com` | "the host" |
| 13 | `Dashboard 1`, `Dashboard1` | "the dashboard" |
| 14 | `anaemia`, `diabetes`, `high_blood_pressure` | "binary comorbidity flags" |
| 15 | `smoking` | "lifestyle flag" |
| 16 | `sex` | "binary demographic flag" |
| 17 | `DEATH_EVENT` | "mortality outcome" |
| 18 | `Surivive` / `Death` | "a misspelled survival label" |
| 19 | `" Non-Smoker"` | "an untrimmed leading space on one lifestyle label" |
| 20 | `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium` | "five continuous biomarker measurements" |
| 21 | `time` | "integer follow-up period" |
| 22 | `age` | "patient age" |
| 23 | Worksheet names (`Sheet 1`, `Sheet 6 (9)`, and so on) | described by chart type |
| 24 | Federated data source id `federated.15n4u4511e3xfk1749m9r1i714e1` | omitted |
| 25 | Internal calculation ids (`[Calculation_215609893383794688]` and so on) | replaced with the readable field name |
| 26 | Dashboard UUID `{14818E80-7948-4984-90AD-D1E566C79BE9}` | omitted |
| 27 | Extract filename `#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper` | omitted |
| 28 | `macOS` | "workstation" |

**Not substituted, deliberately:** all bin sizes, decimal settings, formulas, colour hex codes, canvas dimensions, zone counts, filter scopes, action counts, worksheet counts and column counts, because the instruction was to keep technical detail, counts, rules and logic unchanged.

**One item to check yourself:** the sanitised version still states that the subject is cardiac patient survival. If the subject matter itself is sensitive, replace it with something like "a clinical outcome dataset".
