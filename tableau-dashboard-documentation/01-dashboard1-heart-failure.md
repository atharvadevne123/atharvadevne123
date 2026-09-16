# DASHBOARD 1: Healthcare - Heart Failure

> **Screenshot slot.** Paste your own dashboard screenshot here.
>
> `![Healthcare - Heart Failure dashboard](screenshots/dashboard1_screenshot.png)`
>
> **Tableau Public link slot:** `_______________________________________________`
>
> (The workbook XML contains the publish target `https://public.tableau.com/workbooks/Healthcare-HeartFailure_17429983482570`, revision 1.2. Verify the live viz URL yourself before using it.)
>
> Coordinate-accurate layout wireframe generated from the XML: `screenshots/dashboard1_heart_failure_layout.svg`

---

## 1. DASHBOARD OVERVIEW

| Item | Value | Evidence |
|---|---|---|
| Dashboard name | `Dashboard 1` | ✓ DIRECTLY VERIFIED (`<dashboard name='Dashboard 1'>`) |
| Workbook name | `Healthcare - Heart Failure.twb` (inside a packaged archive) | ✓ DIRECTLY VERIFIED (archive member name) |
| Tableau version | Document format `version='18.1'`, `original-version='18.1'`; `source-build='2025.1.0 (20251.25.0313.2002)'`; build comment `20243.25.0110.1701` | ✓ DIRECTLY VERIFIED |
| Source platform | `source-platform='mac'` | ✓ DIRECTLY VERIFIED |
| Publish target | `repository-location derived-from='https://public.tableau.com/workbooks/Healthcare-HeartFailure_17429983482570?rev=1.1'`, `id='Healthcare-HeartFailure_17429983482570'`, `revision='1.2'` | ✓ DIRECTLY VERIFIED |
| `xml:base` | `https://haproxy-traffic-splitter` | ✓ DIRECTLY VERIFIED |
| Author / owner field | No author, owner, or `<user>` element is stored anywhere in the workbook | ✗ NOT AVAILABLE |
| Author evidence (indirect) | The source file path is `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction`, so the macOS account was `atharvadevne` and the work sat in a folder named `UIC/Business Data Visualization` | △ INFERRED (path only, not an authorship field) |
| Dashboard dimensions | 1900 x 1050 px, `sizing-mode='range'` (min and max both 1900 x 1050) | ✓ DIRECTLY VERIFIED |
| Dashboard background | `#000000` (black) | ✓ DIRECTLY VERIFIED |
| Dashboard UUID | `{14818E80-7948-4984-90AD-D1E566C79BE9}` | ✓ DIRECTLY VERIFIED |

### Dashboards contained in the workbook

| # | Dashboard name | Analyzed here |
|---|---|---|
| 1 | `Dashboard 1` | Yes. It is the only dashboard in the workbook. |

**Stories:** none. There is no `<stories>` element. ✓ DIRECTLY VERIFIED

### Purpose, business problem, audience, story

These four items are **not stored as text anywhere in the workbook**. There is no dashboard description, no caption, no annotation, and no text object. ✗ NOT AVAILABLE as stated fact.

What can be read off the structure (△ INFERRED, from worksheet titles, encodings and filters):

- **Purpose (inferred).** Every single chart on the dashboard encodes `Death Event` on Color, and 12 of the 14 chart titles end with the literal words `- Survival Stats`. The dashboard is a *survival profiling* view: for each clinical attribute in the dataset, show how the population splits between `Surivive` and `Death`.
- **Business / clinical question (inferred).** "Among heart failure patients, how does each clinical and demographic attribute relate to mortality during the follow-up period?"
- **Intended audience (inferred).** The source folder is `UIC/Business Data Visualization`, so the immediate audience is academic. The content itself (clinical biomarkers, comorbidity flags, follow-up time) suits a clinical analytics or population health audience.
- **Overall story (inferred).** Top row states the cohort size and its composition. Middle rows split each binary comorbidity by outcome. Lower rows show the distribution of each continuous biomarker by outcome, ending with two scatter views that bring age, follow-up time and sex together.

---

## 2. DATA SOURCE INVENTORY

There is exactly **one** data source in this workbook.

| Data Source | Type | Connection | Tables/Files | Important Fields | Live/Extract | Notes |
|---|---|---|---|---|---|---|
| `heart_failure_clinical_records_dataset` (internal name `federated.15n4u4511e3xfk1749m9r1i714e1`) | Federated wrapper over a flat file | `class='textscan'`, `directory='/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction'`, `filename='heart_failure_clinical_records_dataset.csv'`, `server=''`, `workgroup-auth-mode='as-is'` | 1 table: `[heart_failure_clinical_records_dataset#csv]` | `age`, `DEATH_EVENT`, `ejection_fraction`, `serum_creatinine`, `serum_sodium`, `platelets`, `creatinine_phosphokinase`, `time`, `sex`, `smoking`, `diabetes`, `anaemia`, `high_blood_pressure` | **Extract**, `enabled='true'`, `count='-1'`, `units='records'` | `count='-1'` means all rows are extracted, no sampling. The extract is materialised in the packaged archive as `Data/tableau-temp/#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper` |

✓ DIRECTLY VERIFIED for all cells above.

### Detailed data source attributes

| Attribute | Value | Evidence |
|---|---|---|
| Data source caption | `heart_failure_clinical_records_dataset` | ✓ |
| Internal name | `federated.15n4u4511e3xfk1749m9r1i714e1` | ✓ |
| `inline` | `true` (embedded in the workbook, not a published data source) | ✓ |
| Named connection | `textscan.0eo7kao1bn80dv0zsqdco0t9bxql` | ✓ |
| Connection class | `textscan` (Tableau's delimited text file connector) | ✓ |
| File name | `heart_failure_clinical_records_dataset.csv` | ✓ |
| Directory | `/Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction` | ✓ |
| Database / schema | None. A flat CSV has no database or schema. | ✓ (absence) |
| Number of tables | 1 | ✓ |
| Text parsing options | `character-set='UTF-8'`, `header='yes'`, `locale='en_US'`, `separator=','` | ✓ |
| Extract name | Not stored as a friendly name. The physical file is `#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper` | ✓ |
| Extract row limit | `count='-1'`, `units='records'` (no limit) | ✓ |
| Extract is user-specific | `false` | ✓ |
| Data source filters | **None.** No `<filter>` exists at the `<datasource>` level. | ✓ (absence) |
| Extract filters | **None.** The `<extract>` element carries no filter child. | ✓ (absence) |
| Custom SQL | **None.** The relation `type='table'`, not `type='text'`. No SQL text anywhere. | ✓ (absence) |
| Aliases | **Yes**, `<aliases enabled='yes'>`. Six fields carry value aliases (see section 4). | ✓ |
| Renamed fields | **Yes**, 13 of 13 source columns carry a `caption` that differs from the raw column name. | ✓ |
| Hidden fields | **None.** No column carries `hidden='true'`. | ✓ (absence) |
| Geographic roles | **None.** No `semantic-role` or geographic role assignment exists. No map is used. | ✓ (absence) |
| Data source calculations | 13 calculated columns (7 bins, 5 string labels, 1 constant). See section 6. | ✓ |
| Row count of source data | The `.hyper` extract is binary and no Hyper API is available here, so the row count cannot be read. | ✗ NOT AVAILABLE |

---

## 3. DATA MODEL / RELATIONSHIPS / JOINS

**There is no data model to speak of. This is a single-table data source.** ✓ DIRECTLY VERIFIED

| Check | Result |
|---|---|
| Joins | None. Only one `<relation type='table'>` exists. |
| Relationships (noodles) | None. |
| Unions | None. |
| Blending | None. Only one data source exists, so blending is impossible. |
| Nested joins | None. |
| Cardinality settings | Not applicable, nothing to relate. |
| Referential integrity settings | Not applicable. |
| Custom SQL | None. |
| Join filters | None. |

### Plain English

The workbook reads one CSV file, `heart_failure_clinical_records_dataset.csv`, as a single flat table of 13 columns. Tableau wraps it in a `federated` connection (that is just Tableau's standard container since version 2020.2, it does not imply federation across systems here). The whole table is then materialised into a Hyper extract. Every worksheet and the dashboard all point at that one table. No second table is ever introduced, so there is nothing to join, relate, union or blend.

### Text representation

```
heart_failure_clinical_records_dataset.csv   (13 columns, 1 table)
        |
        |  full extract, count = -1 (all records), units = records
        v
#TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper
        |
        v
federated.15n4u4511e3xfk1749m9r1i714e1
   "heart_failure_clinical_records_dataset"
        |
        +--> 19 worksheets
        +--> Dashboard 1
```

---

## 4. DATA PREPARATION / CLEANING

Every transformation listed here is present in the workbook XML. Nothing is claimed that is not.

### 4.1 Field renaming (captions)

All 13 raw CSV columns were given display captions. The raw snake_case names are preserved as the field identity, the caption is what appears in the UI.

| Raw column (`name`) | Caption applied | Affected object |
|---|---|---|
| `age` | `Age` | measure |
| `anaemia` | `Anaemia` | dimension |
| `creatinine_phosphokinase` | `Creatinine Phosphokinase` | measure |
| `diabetes` | `Diabetes` | dimension |
| `DEATH_EVENT` | `Death Event` | dimension |
| `ejection_fraction` | `Ejection Fraction` | measure |
| `high_blood_pressure` | `High Blood Pressure` | dimension |
| `platelets` | `Platelets` | measure |
| `serum_creatinine` | `Serum Creatinine` | measure |
| `serum_sodium` | `Serum Sodium` | measure |
| `sex` | `Sex` | dimension |
| `smoking` | `Smoking` | dimension |
| `time` | `Time` | measure |

**What was done:** raw machine column names were replaced with human-readable labels.
**Why it was likely necessary (△ inferred):** the CSV uses lowercase snake_case and one all-caps name, which reads badly in axis titles, legends and tooltips.

### 4.2 Role conversion (measure to dimension)

Six integer columns were converted from Tableau's default `measure` role to `dimension`, with `type='ordinal'`.

| Field | New role | New type | Default aggregation retained |
|---|---|---|---|
| `[DEATH_EVENT]` | dimension | ordinal | `Sum` |
| `[anaemia]` | dimension | ordinal | `Sum` |
| `[diabetes]` | dimension | ordinal | `Sum` |
| `[high_blood_pressure]` | dimension | ordinal | `Sum` |
| `[sex]` | dimension | ordinal | `Sum` |
| `[smoking]` | dimension | ordinal | `Sum` |

**What was done:** the 0/1 flag columns were reclassified as categorical dimensions.
**Why it was likely necessary (△ inferred):** Tableau imports `0`/`1` integers as measures and would default to `SUM()`. Summing a flag is meaningless for these fields. Making them dimensions lets them drive Color, Label and Filter shelves.

The seven genuinely continuous columns were left as measures: `age`, `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium`, `time`.

### 4.3 Value aliasing (0/1 decoding)

`<aliases enabled='yes'>` at the data source level, with six aliased fields. This is the single most substantive cleaning step in the workbook.

| Field | Key `0` becomes | Key `1` becomes | Note |
|---|---|---|---|
| `[DEATH_EVENT]` | `Surivive` | `Death` | **The string is literally `Surivive` in the XML. It is a typo for "Survive" and it will render that way on the dashboard.** |
| `[anaemia]` | `Negative` | `Positive` | |
| `[diabetes]` | `Negative` | `Positive` | |
| `[high_blood_pressure]` | `Negative` | `Positive` | |
| `[sex]` | `Female` | `Male` | |
| `[smoking]` | ` Non-Smoker` | `Smoker` | **The value has a leading space: `" Non-Smoker"`.** |

**What was done:** raw binary codes were decoded to clinical language at the data source layer, so every worksheet inherits the decoding.
**Why it was likely necessary (△ inferred):** a legend reading "0 / 1" is unreadable; "Surivive / Death" and "Positive / Negative" are directly interpretable by a clinical reader.
**Two defects worth flagging:** the `Surivive` spelling and the leading space in `" Non-Smoker"`. Both are real values in the file and both are user-visible.

### 4.4 Binning

Seven bins were created, one for each continuous measure. All are `<calculation class='bin'>` with `peg='0'` (bins anchored at zero) and a fixed numeric `size`.

| Bin field | Source field | Bin size | `decimals` |
|---|---|---|---|
| `[Age (bin)]` | `[age]` | `4.48` | `0` |
| `[Creatinine Phosphokinase (bin)]` | `[creatinine_phosphokinase]` | `376` | `2` |
| `[Ejection Fraction (bin)]` | `[ejection_fraction]` | `8.22` | `0` |
| `[Platelets (bin)]` | `[platelets]` | `41767` | `4` |
| `[Serum Creatinine (bin)]` | `[serum_creatinine]` | `0.772` | `-1` |
| `[Serum Sodium (bin)]` | `[serum_sodium]` | `3.57` | `0` |
| `[Time (bin)]` | `[time]` | `15.1` | `1` |

**What was done:** each continuous biomarker was discretised into fixed-width buckets.
**Why it was likely necessary (△ inferred):** these bin sizes are not round numbers. `4.48`, `8.22`, `0.772`, `3.57`, `15.1` are the values Tableau proposes by default when you right-click a measure and choose Create > Bins, because Tableau suggests a size derived from the field's range and row count. **The sizes were accepted as offered rather than hand-set.** That is a defensible choice, but it is worth knowing if you are asked about it in an interview.

### 4.5 Transformations that are NOT present

Stated explicitly so nothing is over-claimed:

| Transformation | Present? |
|---|---|
| Null handling (`ISNULL`, `IFNULL`, `ZN`) | **No.** No such function appears in any formula. |
| Duplicate handling / dedup logic | **No.** |
| Data type conversions (`INT()`, `STR()`, `FLOAT()`, `DATE()`) | **No.** All types came from the CSV scan. |
| Date conversions or date parts | **No.** The dataset has no date field at all. `time` is an integer follow-up period, not a date. |
| String manipulation (`LEFT`, `SPLIT`, `TRIM`, `REPLACE`, `CONTAINS`) | **No.** |
| Split fields | **No.** |
| Pivot | **No.** |
| Union | **No.** |
| Groups | **No.** No `<group>` element exists. |
| Sets | **No.** |
| Hierarchies / drill paths | **No.** |
| Geographic role assignment | **No.** |
| Tableau Prep flow | **No.** Nothing in the archive references Prep. |
| Data source filter | **No.** |
| Extract filter | **No.** |

---

## 5. COMPLETE FIELD INVENTORY

### 5.1 Source fields (13, from the CSV)

| Field Name (caption) | Original Name | Data Type | Role | Aggregation | Table | Description / Usage |
|---|---|---|---|---|---|---|
| Age | `age` | real | Measure | Sum (default); used as `AVG` and `CNT` in views | `heart_failure_clinical_records_dataset.csv` | Drives the Age histogram, the Average Age KPI, the Age-Sex box scatter and the Age-Time scatter |
| Anaemia | `anaemia` | integer | Dimension (ordinal) | Sum | same | Color + Angle + Label on the Anaemia donut |
| Creatinine Phosphokinase | `creatinine_phosphokinase` | integer | Measure | Sum | same | Binned, drives the CPK histogram |
| Death Event | `DEATH_EVENT` | integer | Dimension (ordinal) | Sum | same | **The outcome variable.** On Color in every chart, and it is the field the highlight action brushes on |
| Diabetes | `diabetes` | integer | Dimension (ordinal) | Sum | same | Color + Angle + Label on the Diabetes donut |
| Ejection Fraction | `ejection_fraction` | integer | Measure | Sum | same | Binned, drives the Ejection Fraction histogram |
| High Blood Pressure | `high_blood_pressure` | integer | Dimension (ordinal) | Sum | same | Color + Angle + Label on the HBP donut |
| Platelets | `platelets` | real | Measure | Sum | same | Binned, drives the Platelets histogram |
| Serum Creatinine | `serum_creatinine` | real | Measure | Sum | same | Binned, drives the Serum Creatinine histogram |
| Serum Sodium | `serum_sodium` | integer | Measure | Sum | same | Binned, drives the Serum Sodium histogram |
| Sex | `sex` | integer | Dimension (ordinal) | Sum | same | Donut dimension, KPI filter for Total Males / Total Females, dashboard filter control, and column split on the Age-Sex scatter |
| Smoking | `smoking` | integer | Dimension (ordinal) | Sum | same | Color + Angle + Label on the Smoking donut |
| Time | `time` | integer | Measure | Sum | same | Binned for the Time histogram; used raw on the Age-Time scatter |

### 5.2 Calculated fields (13)

| Field Name | Class | Data Type | Role | Formula |
|---|---|---|---|---|
| `[Age (bin)]` | bin | integer | Dimension (quantitative) | `[age]`, size `4.48` |
| `[Creatinine Phosphokinase (bin)]` | bin | integer | Dimension (quantitative) | `[creatinine_phosphokinase]`, size `376` |
| `[Ejection Fraction (bin)]` | bin | integer | Dimension (quantitative) | `[ejection_fraction]`, size `8.22` |
| `[Platelets (bin)]` | bin | integer | Dimension (quantitative) | `[platelets]`, size `41767` |
| `[Serum Creatinine (bin)]` | bin | integer | Dimension (quantitative) | `[serum_creatinine]`, size `0.772` |
| `[Serum Sodium (bin)]` | bin | integer | Dimension (quantitative) | `[serum_sodium]`, size `3.57` |
| `[Time (bin)]` | bin | integer | Dimension (quantitative) | `[time]`, size `15.1` |
| `Total Individuals` (`[Calculation_215609893383794688]`) | tableau | string | Dimension (nominal) | `"Total Individuals"` |
| `Total Deaths` (`[Calculation_215609893384032257]`) | tableau | string | Dimension (nominal) | `"Total Deaths"` |
| `Total Males` (`[Calculation_215609893384187906]`) | tableau | string | Dimension (nominal) | `"Total Males"` |
| `Total Females` (`[Calculation_215609893384642563]`) | tableau | string | Dimension (nominal) | `"Total Females"` |
| `Average Age` (`[Calculation_215609893384794116]`) | tableau | string | Dimension (nominal) | `"Average Age"` |
| `0` (`[Calculation_144326355385667585]`) | tableau | integer | Measure | `0` |

### 5.3 Field categorisation

| Category | Members |
|---|---|
| **Dimensions (from source)** | `Anaemia`, `Death Event`, `Diabetes`, `High Blood Pressure`, `Sex`, `Smoking` |
| **Measures (from source)** | `Age`, `Creatinine Phosphokinase`, `Ejection Fraction`, `Platelets`, `Serum Creatinine`, `Serum Sodium`, `Time` |
| **Dates** | **None.** The dataset contains no date or datetime field. |
| **Geographic fields** | **None.** |
| **Calculated fields** | The 13 listed in 5.2 |
| **Parameters** | **None.** There is no `Parameters` data source and no `param-domain-type` column anywhere in this workbook. |
| **Sets** | **None.** |
| **Groups** | **None.** |
| **Bins** | 7 (listed in 5.2) |

### 5.4 Usage classification

| Classification | Fields |
|---|---|
| **Used on the dashboard** (every worksheet placed on Dashboard 1 uses them) | All 13 source fields, all 7 bins, all 5 label calcs, and the `0` calc |
| **Used only in worksheets, not surfaced as a control** | All except `Sex`, which additionally appears as a dashboard filter control, and `Death Event`, which additionally appears as a dashboard color legend |
| **Used inside other calculations** | `age`, `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium`, `time` (each is the input to its bin) |
| **Hidden** | None |
| **Unused** | None. Every declared field is referenced by at least one worksheet. |

---

## 6. CALCULATED FIELDS

### 6.1 The seven bin calculations

All seven follow the same pattern, so one worked example plus the table is enough.

**Calculated Field: `Age (bin)`**

- **Exact Tableau definition:** `<calculation class='bin' decimals='0' formula='[age]' peg='0' size='4.48' />`
- **Data type:** integer
- **Role / type:** dimension, quantitative, `aggregation='None'`
- **Referenced fields:** `[age]`
- **Used in worksheet(s):** `Sheet 6` (on the Columns shelf)
- **Used in KPI(s):** none
- **Purpose:** turn a continuous age measure into fixed-width buckets so a count can be drawn as a histogram.
- **Plain English:** every patient is placed into an age bucket 4.48 years wide, with the first bucket anchored at 0.
- **Business logic:** age is a risk factor, and a histogram of counts split by outcome shows where in the age range deaths concentrate.
- **Dependencies:** none. It depends only on a raw source column.

| Bin calculated field | `formula` | `size` | `peg` | `decimals` | Used in worksheet |
|---|---|---|---|---|---|
| `Age (bin)` | `[age]` | `4.48` | `0` | `0` | `Sheet 6` |
| `Creatinine Phosphokinase (bin)` | `[creatinine_phosphokinase]` | `376` | `0` | `2` | `Sheet 6 (2)` |
| `Ejection Fraction (bin)` | `[ejection_fraction]` | `8.22` | `0` | `0` | `Sheet 6 (3)` |
| `Platelets (bin)` | `[platelets]` | `41767` | `0` | `4` | `Sheet 6 (4)` |
| `Serum Creatinine (bin)` | `[serum_creatinine]` | `0.772` | `0` | `-1` | `Sheet 6 (5)` |
| `Serum Sodium (bin)` | `[serum_sodium]` | `3.57` | `0` | `0` | `Sheet 6 (6)` |
| `Time (bin)` | `[time]` | `15.1` | `0` | `1` | `Sheet 6 (7)` |

### 6.2 The five KPI label calculations

**Calculated Field: `Total Individuals`**

- **Exact Tableau formula:** `"Total Individuals"`
- **Internal name:** `[Calculation_215609893383794688]`
- **Data type:** string
- **Role / type:** dimension, nominal
- **Referenced fields:** none. It is a string literal.
- **Used in worksheet(s):** `Sheet 15`
- **Used in KPI(s):** the Total Individuals KPI card
- **Purpose:** supply the caption text that sits next to the number on the KPI card.
- **Plain English:** a constant text field that always returns the words "Total Individuals".
- **Business logic:** none, it is presentation only.
- **Dependencies:** none.

The same pattern for the other four:

| Calculated field | Internal name | Exact formula | Used in worksheet |
|---|---|---|---|
| `Total Individuals` | `[Calculation_215609893383794688]` | `"Total Individuals"` | `Sheet 15` |
| `Total Deaths` | `[Calculation_215609893384032257]` | `"Total Deaths"` | `Sheet 15 (2)` |
| `Total Males` | `[Calculation_215609893384187906]` | `"Total Males"` | `Sheet 15 (3)` |
| `Total Females` | `[Calculation_215609893384642563]` | `"Total Females"` | `Sheet 15 (4)` |
| `Average Age` | `[Calculation_215609893384794116]` | `"Average Age"` | `Sheet 15 (5)` |

**Technique note (△ inferred):** placing a constant string on the Text shelf next to a measure is a common way to build a KPI card without using a title or a text object, because the caption then inherits the worksheet's font formatting and moves with the mark.

### 6.3 The axis placeholder calculation

**Calculated Field: `0`**

- **Exact Tableau formula:** `0`
- **Internal name:** `[Calculation_144326355385667585]`
- **Data type:** integer
- **Role:** measure
- **Scope:** declared with `user:unnamed='Sheet 1'`, that is, it was created ad hoc inside `Sheet 1` and then promoted to the data source
- **Referenced fields:** none
- **Used in worksheet(s):** all five donut sheets: `Sheet 1`, `Sheet 1 (2)`, `Sheet 1 (3)`, `Sheet 1 (4)`, `Sheet 1 (5)`
- **Used in KPI(s):** none
- **Purpose:** give the pie chart a numeric axis so that a **dual axis** can be created, which is what turns a pie into a donut.
- **Exact shelf expression:** the Rows shelf of each donut sheet is literally
  `([federated.15n4u4511e3xfk1749m9r1i714e1].[sum:Calculation_144326355385667585:qk] + [federated.15n4u4511e3xfk1749m9r1i714e1].[sum:Calculation_144326355385667585:qk])`
  which is `SUM([0])` placed on Rows twice, the standard dual-axis construction.
- **Plain English:** a measure that is always zero. Two copies of it create two overlapping axes at the same position. The first axis carries the coloured pie, the second carries a smaller solid black pie that punches the hole.
- **Business logic:** none, it is a charting device.
- **Dependencies:** none.

### 6.4 Calculation type census for Dashboard 1

| Calculation type | Present? | Detail |
|---|---|---|
| **LOD expressions** (`FIXED`, `INCLUDE`, `EXCLUDE`) | **No.** No `{` appears in any formula. |
| **Table calculations** | **Yes, one type.** `<table-calc ordering-type='Rows' type='PctTotal' />` |
| **Window calculations** (`WINDOW_SUM`, `WINDOW_AVG`, etc.) | **No.** |
| **Running totals** | **No.** |
| **Percent-of-total** | **Yes.** `PctTotal` applied to `CNT(<dimension>)` on all five donut sheets: `[pcto:cnt:anaemia:qk]`, `[pcto:cnt:diabetes:qk]`, `[pcto:cnt:high_blood_pressure:qk]`, `[pcto:cnt:sex:qk]`, `[pcto:cnt:smoking:qk]` |
| **Rank calculations** | **No.** |
| **Date calculations** | **No.** There is no date field. |
| **Conditional calculations / IF-THEN-ELSE** | **No.** |
| **CASE statements** | **No.** |
| **Parameters used inside calculations** | **No.** There are no parameters in this workbook. |
| **Aggregations used on shelves** | `CNT` (count), `SUM`, `AVG`, and `None` (continuous dimension) |

**Important honesty note.** The calculation layer of this workbook is deliberately thin. The heavy lifting is done by aliasing, role conversion, binning and a built-in percent-of-total table calculation, not by written formulas. Do not describe this workbook as containing LODs or complex conditional logic, because it does not.

---

## 7. PARAMETERS

**There are no parameters in this workbook.** ✓ DIRECTLY VERIFIED by absence: there is no `Parameters` data source, no column carrying `param-domain-type`, and no `paramctrl` zone on the dashboard.

| Parameter | Data Type | Current Value | Allowed Values | Used By | Purpose |
|---|---|---|---|---|---|
| (none) | | | | | |

---

## 8. FILTERS

### 8.1 Filter inventory

| Filter | Field | Type | Values / Condition | Scope | Effect |
|---|---|---|---|---|---|
| Sex quick filter | `[sex]` as `[none:sex:ok]` | Categorical, `function='level-members'`, `ui-enumeration='all'` | All members selected (`Female`, `Male`) | `filter-group='3'` on **14 worksheets**, exposed on the dashboard as a **dropdown** control sourced from `Sheet 6 (9)` | Filters every donut, every histogram and both scatters simultaneously. Does **not** touch the five KPI cards. |
| Total Deaths KPI filter | `[DEATH_EVENT]` as `[none:DEATH_EVENT:ok]` | Categorical, `function='member'`, `member='1'`, `ui-enumeration='inclusive'` | Keeps only `Death Event = 1` (aliased `Death`) | Worksheet-only: `Sheet 15 (2)` | Reduces the card's count to deaths only |
| Total Males KPI filter | `[sex]` as `[none:sex:ok]` | Categorical, `function='member'`, `member='1'` | Keeps only `sex = 1` (aliased `Male`) | Worksheet-only: `Sheet 15 (3)` | Reduces the card's count to males only |
| Total Females KPI filter | `[sex]` as `[none:sex:ok]` | Categorical, `function='member'`, `member='0'` | Keeps only `sex = 0` (aliased `Female`) | Worksheet-only: `Sheet 15 (4)` | Reduces the card's count to females only |

### 8.2 Worksheets affected by the shared Sex filter (`filter-group='3'`)

`Sheet 1`, `Sheet 1 (2)`, `Sheet 1 (3)`, `Sheet 1 (4)`, `Sheet 1 (5)`, `Sheet 6`, `Sheet 6 (2)`, `Sheet 6 (3)`, `Sheet 6 (4)`, `Sheet 6 (5)`, `Sheet 6 (6)`, `Sheet 6 (7)`, `Sheet 6 (8)`, `Sheet 6 (9)`. That is 14 of the 19 worksheets.

**Not affected:** `Sheet 15`, `Sheet 15 (2)`, `Sheet 15 (3)`, `Sheet 15 (4)`, `Sheet 15 (5)`, the five KPI cards.

**Consequence worth knowing (△ inferred):** because the KPI cards sit outside `filter-group 3`, selecting `Male` in the Sex dropdown will re-filter all 14 charts but the `Total Individuals`, `Total Deaths`, `Total Males` and `Total Females` cards will not move. That is a real behaviour of the workbook as built, and a likely interview question.

### 8.3 Filter types NOT present

| Filter type | Present? |
|---|---|
| Data source level filter | No |
| Extract filter | No |
| Context filter | No. No filter carries a context flag. |
| Measure filter | No. Every filter is categorical on a dimension. |
| Relative date filter | No. There is no date field. |
| Range / quantitative filter | No |
| Top N filter | No |
| Parameter-based filter | No. There are no parameters. |
| Condition or formula filter | No |

---

## 9. KPI IDENTIFICATION

Five KPI cards are on the dashboard, each one its own worksheet, all sitting in the top strip at `y=762` (roughly the top 7 percent of the canvas).

### KPI 1: Total Individuals

| Attribute | Value |
|---|---|
| Exact displayed name | `Total Individuals` (the literal string from `[Calculation_215609893383794688]`) |
| Tableau field behind the number | `[cnt:DEATH_EVENT:qk]` |
| Exact expression | `CNT([DEATH_EVENT])` |
| Aggregation | `CNT` (count of non-null values) |
| Numerator | Count of rows where `DEATH_EVENT` is not null |
| Denominator | Not applicable |
| Filters affecting it | **None.** `Sheet 15` has no filter at all and is outside `filter-group 3`. |
| Parameters affecting it | None |
| Time period | Not applicable, the dataset has no dates |
| Unit | Count of patients |
| Worksheet | `Sheet 15` |
| Dashboard location | Zone id `17`, x=421 y=762 w=20892 h=6855 (leftmost KPI, top strip), `show-title='false'` |
| Business meaning | Cohort size |
| Why useful | Every percentage on the dashboard is only interpretable against the base population |
| What a user learns | How many heart failure patients the entire dashboard is describing |
| Dependency chain | `[Calculation_215609893383794688]` supplies the caption text; the number is a direct `CNT` of a source column. No calculated field feeds the number. |

**Technical note:** counting `DEATH_EVENT` rather than using `COUNT(*)` or a `Number of Records` field is a design choice. It counts non-null `DEATH_EVENT` values, which equals the row count only if `DEATH_EVENT` is never null. The metadata record for `DEATH_EVENT` says `<contains-null>true</contains-null>`, which is Tableau's default optimistic flag for a scanned CSV rather than a measured fact, so this cannot be resolved from the workbook alone. ✗ NOT AVAILABLE whether any nulls exist.

### KPI 2: Total Deaths

| Attribute | Value |
|---|---|
| Exact displayed name | `Total Deaths` |
| Field behind the number | `[cnt:DEATH_EVENT:qk]` |
| Exact expression | `CNT([DEATH_EVENT])` filtered to `DEATH_EVENT = 1` |
| Aggregation | `CNT` |
| Numerator | Rows where `Death Event = Death` |
| Denominator | Not applicable. **No rate is computed.** The dashboard shows the count, not the mortality rate. |
| Filters affecting it | Worksheet filter `[none:DEATH_EVENT:ok]`, `function='member'`, `member='1'` |
| Parameters affecting it | None |
| Unit | Count of patients |
| Worksheet | `Sheet 15 (2)` |
| Dashboard location | Zone id `18`, x=21313 y=762 w=19736 h=6855 |
| Business meaning | Absolute mortality in the cohort during follow-up |
| Why useful | The headline outcome count |
| What a user learns | How many patients in the cohort died |
| Dependency chain | Caption from `[Calculation_215609893384032257]`; number is `CNT` on a filtered source column |

### KPI 3: Total Males

| Attribute | Value |
|---|---|
| Exact displayed name | `Total Males` |
| Field behind the number | `[cnt:sex:qk]` |
| Exact expression | `CNT([sex])` filtered to `sex = 1` |
| Aggregation | `CNT` |
| Filters affecting it | Worksheet filter `[none:sex:ok]`, `function='member'`, `member='1'` |
| Unit | Count of patients |
| Worksheet | `Sheet 15 (3)` |
| Dashboard location | Zone id `19`, x=41049 y=762 w=18783 h=6855 |
| Business meaning | Male cohort size |
| What a user learns | The sex composition of the cohort, read together with KPI 4 |

### KPI 4: Total Females

| Attribute | Value |
|---|---|
| Exact displayed name | `Total Females` |
| Field behind the number | `[cnt:sex:qk]` |
| Exact expression | `CNT([sex])` filtered to `sex = 0` |
| Aggregation | `CNT` |
| Filters affecting it | Worksheet filter `[none:sex:ok]`, `function='member'`, `member='0'` |
| Unit | Count of patients |
| Worksheet | `Sheet 15 (4)` |
| Dashboard location | Zone id `20`, x=59832 y=762 w=20217 h=6855 |
| Business meaning | Female cohort size |
| What a user learns | Whether the cohort is sex-balanced, which conditions how the Sex donut should be read |

### KPI 5: Average Age

| Attribute | Value |
|---|---|
| Exact displayed name | `Average Age` |
| Field behind the number | `[avg:age:qk]` |
| Exact expression | `AVG([age])` |
| Aggregation | `AVG` |
| Filters affecting it | **None.** `Sheet 15 (5)` has no filter and is outside `filter-group 3`. |
| Unit | Years |
| Worksheet | `Sheet 15 (5)` |
| Dashboard location | Zone id `21`, x=80049 y=762 w=19530 h=6855 (rightmost KPI) |
| Business meaning | Central tendency of cohort age |
| What a user learns | Roughly how old this heart failure population is, which frames the Age histogram below it |

### KPIs that are NOT present

There is **no mortality rate**, **no survival rate**, **no percentage KPI**, and **no target or benchmark comparison** on this dashboard. The percent-of-total figures exist only inside the donut labels, not as KPI cards. ✓ VERIFIED by absence.

---

## 10. WORKSHEET / SHEET-BY-SHEET ANALYSIS

19 worksheets exist and **all 19 are placed on Dashboard 1**. None is orphaned.

Global formatting shared by the chart worksheets (`Sheet 1` family and `Sheet 6` family), read from each `<style>` block:

| Style element | Setting |
|---|---|
| `table` background-color | `#000000` |
| `worksheet` font | bold, `#ffffff`, size `8` |
| `zeroline` | `stroke-size 0`, `line-visibility off` |
| `table-div` (grid lines), cols scope | `stroke-size 0`, `line-visibility off` |
| `title` | 1px solid `#ffffff` border |
| `header` subtotal border | 1px solid `#ffffff` |
| `cell` size on donut sheets | width `290`, height `223` |

### 10.1 to 10.5: The five donut charts (`Sheet 1` family)

All five are structurally identical. Only the comorbidity dimension changes.

| Worksheet | Title (exact) | Dimension used | Angle field | Percent-of-total field |
|---|---|---|---|---|
| `Sheet 1` | `Anaemia-Survival Stats` | `[anaemia]` | `[cnt:anaemia:qk]` | `[pcto:cnt:anaemia:qk]` |
| `Sheet 1 (2)` | `Diabetes-Survival Stats` | `[diabetes]` | `[cnt:diabetes:qk]` | `[pcto:cnt:diabetes:qk]` |
| `Sheet 1 (3)` | `High Blood Pressure-Survival Stats` | `[high_blood_pressure]` | `[cnt:high_blood_pressure:qk]` | `[pcto:cnt:high_blood_pressure:qk]` |
| `Sheet 1 (4)` | `Sex-Survival Stats` | `[sex]` | `[cnt:sex:qk]` | `[pcto:cnt:sex:qk]` |
| `Sheet 1 (5)` | `Smoking-Survival Stats` | `[smoking]` | `[cnt:smoking:qk]` | `[pcto:cnt:smoking:qk]` |

**Worksheet: `Sheet 1` (representative of all five)**

| Property | Value |
|---|---|
| Purpose | Show how patients split across `Death Event` and `Anaemia` at the same time, with both a count and a share |
| Visualization type | **Donut chart**, built as a dual-axis pie |
| Data source | `heart_failure_clinical_records_dataset` |
| Rows shelf | `(SUM([0]) + SUM([0]))`, that is the `0` calc placed twice to create a dual axis |
| Columns shelf | empty |
| Marks type | `Pie` on all three panes |
| Marks > Color | Pane 1: `[none:DEATH_EVENT:ok]` **and** `[none:anaemia:ok]` (two fields on Color, producing a 4-way crossed palette). Pane 2: solid `#000000` via `mark-color` format, no field. |
| Marks > Size | Pane 1 `size = 0.69165748357772827`. Pane 2 `size = 0.42779004573822021`. `mark-sizing-setting='marks-scaling-off'` on both. **The smaller black pie on the second axis is what creates the donut hole.** |
| Marks > Angle (wedge-size) | `[cnt:anaemia:qk]`, that is `CNT([anaemia])` |
| Marks > Label (text) | Three fields: `[none:anaemia:ok]`, `[none:DEATH_EVENT:ok]`, `[pcto:cnt:anaemia:qk]`. Labels shown (`mark-labels-show = true`) and culled (`mark-labels-cull = true`) on pane 1; hidden on pane 2. |
| Marks > Detail | none beyond the above |
| Marks > Tooltip | **No custom tooltip.** Tableau default applies. |
| Filters | `[none:sex:ok]`, level-members, all, `filter-group='3'` |
| Pages | none |
| Parameters | none |
| Sets / Groups | none |
| Calculated fields used | `[Calculation_144326355385667585]` (the `0` axis placeholder) |
| Table calculations | `PctTotal`, `ordering-type='Rows'`, applied to `CNT([anaemia])` |
| Sorting | none defined |
| Reference lines / trend lines / forecasting | none |
| Analytics features | none |
| Axis configuration | Both row axes: `major-show='false'`, `major-spacing='2147483647'`, axis `title=''` (blank), axis `width=48`. Axes are effectively hidden. |
| Number formatting | **None specified.** No `number-format` attribute exists anywhere in this workbook, so defaults apply. |
| Date formatting | Not applicable |
| **Dual axis** | **Yes.** Two `SUM([0])` fields on Rows, panes with `y-index='1'` on the second. |
| **Synchronized axis** | Both axes are the same constant `SUM([0])` expression, so they coincide by construction. There is no separate `<synchronize>` flag in the XML. △ INFERRED |
| Measure Names / Measure Values | Not used |
| Color palette | `palette='summer_10_0'` with an explicit override map |

**Exact color map on the donut sheets (identical on all five):**

| `Death Event` bucket | Comorbidity bucket | Hex |
|---|---|---|
| `0` (`Surivive`) | `0` | `#8fb202` (olive green) |
| `0` (`Surivive`) | `1` | `#b9ca5d` (light green) |
| `1` (`Death`) | `0` | `#cf3e53` (deep red) |
| `1` (`Death`) | `1` | `#f1788d` (pink) |

**Plain English, how the donut works.** A constant measure of zero is placed on Rows twice, which gives Tableau two identical vertical axes to draw on. Both mark types are set to Pie. The first pie is sized `0.69` and is coloured by the crossed combination of outcome and comorbidity, so it has four wedges: survived without the condition, survived with it, died without it, died with it. Wedge angle is the count of patients in each combination, and each wedge is labelled with the comorbidity value, the outcome value and the wedge's percent of the total count computed across rows. The second pie is sized `0.43`, coloured solid black to match the dashboard background, and has its labels turned off. Overlaying the small black pie on the large coloured one punches a hole in the middle, which is how a donut is made in Tableau without a dedicated donut mark type.

### 10.6 to 10.12: The seven histograms (`Sheet 6` family, part 1)

All seven are structurally identical: a bin on Columns, a count on Rows, outcome on Color.

| Worksheet | Title (exact) | Columns shelf | Rows shelf |
|---|---|---|---|
| `Sheet 6` | `Age - Survival Stats` | `[none:Age (bin):qk]` | `[cnt:age:qk]` |
| `Sheet 6 (2)` | `Creatinine Phosphokinase - Survival Stats` | `[none:Creatinine Phosphokinase (bin):qk]` | `[cnt:creatinine_phosphokinase:qk]` |
| `Sheet 6 (3)` | `Ejection Fraction - Survival Stats` | `[none:Ejection Fraction (bin):qk]` | `[cnt:ejection_fraction:qk]` |
| `Sheet 6 (4)` | `Platelets - Survival Stats` | `[none:Platelets (bin):qk]` | `[cnt:platelets:qk]` |
| `Sheet 6 (5)` | `Serum Creatinine - Survival Stats` | `[none:Serum Creatinine (bin):qk]` | `[cnt:serum_creatinine:qk]` |
| `Sheet 6 (6)` | `Serum Sodium - Survival Stats` | `[none:Serum Sodium (bin):qk]` | `[cnt:serum_sodium:qk]` |
| `Sheet 6 (7)` | `Time - Survival Stats` | `[none:Time (bin):qk]` | `[cnt:time:qk]` |

**Worksheet: `Sheet 6` (representative of all seven)**

| Property | Value |
|---|---|
| Purpose | Show the distribution of age across the cohort, split by survival outcome |
| Visualization type | **Stacked histogram** (bar marks over a bin dimension) |
| Marks type | `Automatic`. With a continuous measure on Rows and a discrete bin on Columns, Tableau resolves Automatic to **Bar**. △ INFERRED from Tableau's mark resolution rules; the XML stores only `Automatic`. |
| Marks > Color | `[none:DEATH_EVENT:ok]` |
| Color map (all seven sheets) | `0` (`Surivive`) `#59a14f` (green), `1` (`Death`) `#e15759` (red). `type='palette'`, no named palette override. |
| Marks > Size / Label / Detail | none |
| Marks > Tooltip | No custom tooltip, Tableau default |
| Filters | `[none:sex:ok]`, level-members, all, `filter-group='3'` |
| Sorting | none |
| Reference lines | none |
| Analytics features | none |
| Dual axis | no |
| Measure Names / Values | not used |
| Aggregate Measures | `true` |
| Color legend | **Only `Sheet 6` exposes its color legend on the dashboard** (zone id `25`). The other six histograms reuse the same color scheme without their own legend. |

**Plain English.** Age is bucketed into 4.48-year bins on the horizontal axis. The bar height is the count of patients in that bin. Each bar is split into a green segment (survived) and a red segment (died), stacked. Reading left to right shows where in the age range the red proportion grows. The same construction is repeated for creatinine phosphokinase, ejection fraction, platelets, serum creatinine, serum sodium and follow-up time, which means seven biomarkers are profiled in exactly the same visual grammar.

### 10.13: `Sheet 6 (8)` Age vs Time scatter

| Property | Value |
|---|---|
| Title (exact) | `Age-Time - Survival Stats` |
| Purpose | Relate patient age to follow-up time, coloured by outcome |
| Visualization type | Scatter plot |
| Columns shelf | `[none:age:qk]`, that is `Age` used with **no aggregation** (continuous dimension) |
| Rows shelf | `[none:time:qk]`, that is `Time` used with **no aggregation** |
| Marks type | `Automatic` |
| Marks > Color | `[none:DEATH_EVENT:ok]`, green `#59a14f` / red `#e15759` |
| Marks > Size / Label / Detail | none |
| Tooltip | default |
| Filters | `[none:sex:ok]`, level-members, all, `filter-group='3'` |
| Aggregate Measures | `true` |
| Reference lines / trend lines / forecast | **none** |
| Dual axis | no |
| Dashboard zone | id `32`, x=41049 y=66285 w=39002 h=32953. **This is the widest chart zone on the dashboard**, twice the width of a normal tile. |

**Plain English.** Both `age` and `time` are placed on the shelves as continuous *dimensions* rather than aggregated measures, so each distinct age-and-follow-up-time combination draws its own mark instead of being rolled up. Colour shows whether that combination corresponds to survivors or deaths. The wide zone gives the horizontal age axis room to spread out.

### 10.14: `Sheet 6 (9)` Age by outcome and sex

| Property | Value |
|---|---|
| Title (exact) | `Age-Sex - Survival Stats` |
| Purpose | Compare the age distribution across the four outcome-by-sex cells |
| Visualization type | Disaggregated dot plot with an average reference line per cell |
| Columns shelf | `([none:DEATH_EVENT:ok] / [none:sex:ok])`, a nested discrete split: outcome first, then sex inside it, giving 4 cells |
| Rows shelf | `[avg:age:qk]`, that is `AVG([age])` |
| Marks type | **`Circle`** (explicitly set, not Automatic) |
| **Aggregate Measures** | **`false`**. This is the only worksheet in the workbook where Analysis > Aggregate Measures is switched off, so each underlying record is plotted as its own circle. |
| Marks > Color | none defined on this sheet |
| Marks > Size / Label / Detail | none |
| **Reference line** | **Yes.** `<reference-line axis-column='[avg:age:qk]' formula='average' value-column='[avg:age:qk]' scope='per-cell' label-type='automatic' id='refline0' z-order='1' probability='95' symmetric='false' boxplot-whisker-type='standard' boxplot-mark-exclusion='false' enable-instant-analytics='true' />` |
| Reference line meaning | An **average** line drawn **per cell**, so each of the four outcome-by-sex cells gets its own mean age line |
| Filters | `[none:sex:ok]`, level-members, all, `filter-group='3'`. **This worksheet is the source of the dashboard's Sex dropdown control.** |
| Field labels | `display-field-labels` set to `false` for cols scope, so the column header captions are suppressed |
| Dual axis | no |

**Plain English.** The horizontal axis is split into four groups: survived-female, survived-male, died-female, died-male (nesting outcome over sex). Because aggregation is turned off, every patient appears as an individual circle at their own age. On top of each group a horizontal line marks that group's average age. This is the one view in the dashboard that shows within-group spread rather than just counts, and it is also the view that hosts the global Sex filter control.

### 10.15 to 10.19: The five KPI worksheets (`Sheet 15` family)

| Worksheet | Text shelf field 1 (caption) | Text shelf field 2 (value) | Worksheet filter |
|---|---|---|---|
| `Sheet 15` | `[none:Calculation_215609893383794688:nk]` = `"Total Individuals"` | `[cnt:DEATH_EVENT:qk]` | none |
| `Sheet 15 (2)` | `[none:Calculation_215609893384032257:nk]` = `"Total Deaths"` | `[cnt:DEATH_EVENT:qk]` | `DEATH_EVENT` member `1` |
| `Sheet 15 (3)` | `[none:Calculation_215609893384187906:nk]` = `"Total Males"` | `[cnt:sex:qk]` | `sex` member `1` |
| `Sheet 15 (4)` | `[none:Calculation_215609893384642563:nk]` = `"Total Females"` | `[cnt:sex:qk]` | `sex` member `0` |
| `Sheet 15 (5)` | `[none:Calculation_215609893384794116:nk]` = `"Average Age"` | `[avg:age:qk]` | none |

Shared properties for all five:

| Property | Value |
|---|---|
| Visualization type | Text / BAN card (big aggregate number) |
| Marks type | `Automatic` (resolves to Text, since only Text encodings are present) |
| Rows shelf | empty |
| Columns shelf | empty |
| Marks > Text | two fields: the constant caption string, then the aggregate |
| Mark labels | `mark-labels-show = true`, `mark-labels-cull = true` |
| Marks > Color / Size / Detail | none |
| Tooltip | default |
| Title on dashboard | suppressed, all five zones carry `show-title='false'` |
| Aggregate Measures | `true` |
| Number formatting | none specified |

**Plain English.** Each card is an empty viz with two things on the Text shelf: a string constant that acts as the label and a single aggregate that acts as the number. Because rows and columns are empty, Tableau draws exactly one mark, which renders as a centred block of text. Titles are hidden on the dashboard so the constant string is the only caption visible.

---

## 11. VISUALIZATION-BY-VISUALIZATION BREAKDOWN

| # | Visual | What it shows | Fields driving it | Dimensions compared | Measure analysed | Aggregation | Filters affecting it | Calculations affecting it | Business question answered | Why appropriate |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KPI: Total Individuals | Cohort size | `DEATH_EVENT` | none | count of patients | `CNT` | none | none | How big is the population? | A single number is the right form for a scalar |
| 2 | KPI: Total Deaths | Deaths in cohort | `DEATH_EVENT` | none | count of patients | `CNT` | `DEATH_EVENT = 1` | none | How many died? | Same |
| 3 | KPI: Total Males | Male count | `sex` | none | count of patients | `CNT` | `sex = 1` | none | Sex composition | Same |
| 4 | KPI: Total Females | Female count | `sex` | none | count of patients | `CNT` | `sex = 0` | none | Sex composition | Same |
| 5 | KPI: Average Age | Mean age | `age` | none | age | `AVG` | none | none | How old is this population? | Same |
| 6 | Donut: Anaemia-Survival Stats | 4-way split of the cohort across outcome and anaemia status | `DEATH_EVENT`, `anaemia` | Outcome x Anaemia | count, plus share of total | `CNT` + `PctTotal` | Sex filter | `[0]` axis calc, `PctTotal` | Do anaemic patients die more often? | A donut with a crossed colour encoding shows composition and share in one mark; the hole leaves room for the dark theme |
| 7 | Donut: Diabetes-Survival Stats | Same for diabetes | `DEATH_EVENT`, `diabetes` | Outcome x Diabetes | count + share | `CNT` + `PctTotal` | Sex filter | same | Does diabetes associate with mortality? | Same |
| 8 | Donut: High Blood Pressure-Survival Stats | Same for hypertension | `DEATH_EVENT`, `high_blood_pressure` | Outcome x HBP | count + share | `CNT` + `PctTotal` | Sex filter | same | Does hypertension associate with mortality? | Same |
| 9 | Donut: Sex-Survival Stats | Same for sex | `DEATH_EVENT`, `sex` | Outcome x Sex | count + share | `CNT` + `PctTotal` | Sex filter | same | Does outcome differ by sex? | Same |
| 10 | Donut: Smoking-Survival Stats | Same for smoking | `DEATH_EVENT`, `smoking` | Outcome x Smoking | count + share | `CNT` + `PctTotal` | Sex filter | same | Does smoking associate with mortality? | Same |
| 11 | Histogram: Age - Survival Stats | Age distribution split by outcome | `Age (bin)`, `DEATH_EVENT` | Age buckets | count of patients | `CNT` | Sex filter | `Age (bin)` | Where in the age range do deaths cluster? | A stacked histogram is the standard form for a binned continuous variable split by a binary class |
| 12 | Histogram: Creatinine Phosphokinase | CPK distribution by outcome | `Creatinine Phosphokinase (bin)`, `DEATH_EVENT` | CPK buckets | count | `CNT` | Sex filter | bin | Is CPK elevated among those who died? | Same |
| 13 | Histogram: Ejection Fraction | EF distribution by outcome | `Ejection Fraction (bin)`, `DEATH_EVENT` | EF buckets | count | `CNT` | Sex filter | bin | Is low ejection fraction associated with death? | Same |
| 14 | Histogram: Platelets | Platelet distribution by outcome | `Platelets (bin)`, `DEATH_EVENT` | Platelet buckets | count | `CNT` | Sex filter | bin | Does platelet count separate the outcomes? | Same |
| 15 | Histogram: Serum Creatinine | Creatinine distribution by outcome | `Serum Creatinine (bin)`, `DEATH_EVENT` | Creatinine buckets | count | `CNT` | Sex filter | bin | Does renal function associate with mortality? | Same |
| 16 | Histogram: Serum Sodium | Sodium distribution by outcome | `Serum Sodium (bin)`, `DEATH_EVENT` | Sodium buckets | count | `CNT` | Sex filter | bin | Does hyponatraemia associate with mortality? | Same |
| 17 | Histogram: Time | Follow-up time distribution by outcome | `Time (bin)`, `DEATH_EVENT` | Time buckets | count | `CNT` | Sex filter | bin | How does follow-up duration relate to outcome? | Same |
| 18 | Scatter: Age-Time - Survival Stats | Age against follow-up time | `age`, `time`, `DEATH_EVENT` | none (two continuous axes) | age, time | none (unaggregated) | Sex filter | none | Do deaths cluster at particular age-and-follow-up combinations? | A scatter is the right form for two continuous variables with a categorical colour |
| 19 | Dot plot: Age-Sex - Survival Stats | Individual ages in four outcome-by-sex cells with per-cell mean lines | `age`, `DEATH_EVENT`, `sex` | Outcome nested over Sex | age | disaggregated, plus an `average` reference line | Sex filter | reference line `formula='average'`, `scope='per-cell'` | Does mean age differ across outcome and sex? | Showing individual points plus a mean line conveys both central tendency and spread, which a bar of averages would hide |

---

## 12. DASHBOARD LAYOUT

| Property | Value |
|---|---|
| Dashboard name | `Dashboard 1` |
| Size | 1900 x 1050 px, `sizing-mode='range'`, min and max both 1900 x 1050 |
| Background | `#000000` |
| Layout style | **Fully tiled.** There are no floating objects. The whole dashboard is built from nested flow containers. |
| Container structure | `layout-basic` (id 4) > `layout-flow param='horz'` (id 35) > `layout-flow param='vert'` (id 16) > `layout-flow param='horz'` (id 7) > `layout-basic` (id 5) which holds all 19 worksheet zones |
| Outer container padding | `margin='8'` |
| Worksheet zone padding | `margin='4'` on every worksheet zone |
| Borders | `border-style='none'`, `border-width='0'`, `border-color='#000000'` on every zone |
| Device layouts | One auto-generated **Phone** layout, `sizing-mode='vscroll'`, height 4450 px, `auto-generated='true'`. It re-stacks the same 21 objects into a single vertical flow container (id 41). No Tablet layout. |

### Object census

| Object type | Count | Detail |
|---|---|---|
| Worksheets | 19 | All 19 worksheets in the workbook |
| Color legend | 1 | Zone id `25`, `type-v2='color'`, `param='[none:DEATH_EVENT:ok]'`, sourced from `Sheet 6`, `show-title='false'`, at x=74105 y=36667 w=5474 h=3905 |
| Filter control | 1 | Zone id `36`, `type-v2='filter'`, `mode='dropdown'`, `param='[none:sex:ok]'`, sourced from `Sheet 6 (9)`, at x=34842 y=37143 w=5474 h=4762 |
| Text objects | **0** | There is no title text object and no annotation |
| Images | **0** | |
| Blank objects | **0** | |
| Navigation buttons | **0** | |
| Extension objects | **0** | |
| Web page objects | **0** | |
| Parameter controls | **0** | No parameters exist |

### Reconstructed hierarchy

```
Dashboard 1  (1900 x 1050, black, tiled)
└── layout-basic  [id 4, margin 8]
    └── layout-flow horz  [id 35]
        └── layout-flow vert  [id 16]
            └── layout-flow horz  [id 7]
                └── layout-basic  [id 5]
                    ├── ROW 1  y=762, h=6855   KPI STRIP (titles hidden)
                    │   ├── Sheet 15       Total Individuals    x=421    w=20892
                    │   ├── Sheet 15 (2)   Total Deaths         x=21313  w=19736
                    │   ├── Sheet 15 (3)   Total Males          x=41049  w=18783
                    │   ├── Sheet 15 (4)   Total Females        x=59832  w=20217
                    │   └── Sheet 15 (5)   Average Age          x=80049  w=19530
                    │
                    ├── ROW 2  y=7617, h=25240   DONUT STRIP (comorbidity vs outcome)
                    │   ├── Sheet 1        Anaemia              x=421    w=20892
                    │   ├── Sheet 1 (3)    High Blood Pressure  x=21313  w=19736
                    │   ├── Sheet 1 (5)    Smoking              x=41049  w=18792
                    │   ├── Sheet 1 (2)    Diabetes             x=59841  w=20208
                    │   └── Sheet 1 (4)    Sex                  x=80049  w=19530
                    │
                    ├── ROW 3  y=32857, h~33428   DISTRIBUTION STRIP A
                    │   ├── Sheet 6        Age histogram        x=421    w=20892
                    │   │    └── [floating-in-flow] color legend "Death Event"  x=74105 y=36667
                    │   ├── Sheet 6 (2)    CPK histogram        x=21313  w=19736
                    │   ├── Sheet 6 (9)    Age-Sex dot plot     x=41049  w=18792
                    │   │    └── [control] Sex filter dropdown  x=34842 y=37143
                    │   ├── Sheet 6 (3)    Ejection Fraction    x=59841  w=20210
                    │   └── Sheet 6 (4)    Platelets            x=80051  w=19528
                    │
                    └── ROW 4  y~66285, h~32953   DISTRIBUTION STRIP B
                        ├── Sheet 6 (6)    Serum Sodium         x=421    w=20892
                        ├── Sheet 6 (7)    Time histogram       x=21313  w=19736
                        ├── Sheet 6 (8)    Age-Time scatter     x=41049  w=39002   <-- double width
                        └── Sheet 6 (5)    Serum Creatinine     x=80051  w=19528
```

Note on reading the numbers: zone `x`, `y`, `w`, `h` are stored in hundred-thousandths of the dashboard dimension. Multiply by 1900/100000 for pixels horizontally and 1050/100000 vertically. For example `Sheet 15` at `x=421 w=20892` is roughly 8 px from the left and 397 px wide.

**Headers and footers:** there are none as distinct objects. The KPI strip functions as a header visually, but it is five worksheets, not a header object. ✓ VERIFIED.

---

## 13. DASHBOARD ACTIONS / INTERACTIVITY

There is exactly **one** action in the workbook.

| Attribute | Value |
|---|---|
| Caption | `Highlight 1 (generated)` |
| Internal name | `[Action1_F214FEC6D9404714A6A883192F2B2305]` |
| Action type | **Highlight** (`command='tsc:brush'`) |
| Trigger | `<activation type='on-select' auto-clear='true' />`, that is, select a mark, and deselecting clears it |
| Source | `<source dashboard='Dashboard 1' type='sheet' />`, so the source is the whole dashboard, every sheet on it |
| Target | `param name='target' value='Dashboard 1'`, the whole dashboard |
| Fields used | `param name='field-captions' value='Death Event'` |
| Result / effect | Selecting any mark highlights, across all 19 worksheets at once, every other mark that shares the same `Death Event` value. Selecting a red wedge on the Anaemia donut dims every non-`Death` mark on all the histograms, both scatters and the other four donuts. |
| Caption suffix `(generated)` | Indicates Tableau auto-named it when the user created a highlight action on a field. △ INFERRED |

### Interactivity types NOT present

| Interactivity | Present? |
|---|---|
| Filter actions | **No** |
| URL actions | **No** |
| Parameter actions | **No** (no parameters exist) |
| Set actions | **No** (no sets exist) |
| Navigation / Go to Sheet actions | **No** |
| Sheet swapping | **No** |
| Dashboard-to-dashboard navigation | **No** (there is only one dashboard) |
| Drill-down hierarchies | **No** (no hierarchies defined) |
| Viz-in-tooltip | **No** |
| Custom tooltip interactions | **No** |

**Interactive controls available to the end user:** the Sex dropdown filter (affecting 14 sheets), the Death Event highlight action (affecting all 19), and the Death Event color legend (which in Tableau also supports highlight-on-click).

---

## 14. TOOLTIPS

**No worksheet in this workbook has a customised tooltip.** There is not a single `<customized-tooltip>` element in the file. ✓ DIRECTLY VERIFIED by absence.

| Worksheet | Custom tooltip? | Calculated values in tooltip? | Custom descriptions? | Viz-in-tooltip? | Conditional behaviour? |
|---|---|---|---|---|---|
| All 19 worksheets | No | No | No | No | No |

**What users will actually see.** Tableau's default tooltip lists whatever is on the shelves for that mark. So for example:

- On a donut wedge: `Anaemia`, `Death Event`, `CNT(Anaemia)`, `% of Total CNT(Anaemia)`.
- On a histogram bar: `Age (bin)`, `Death Event`, `CNT(Age)`.
- On the Age-Sex dot plot: `Death Event`, `Sex`, `Age`.

These are △ INFERRED from the encodings, since the tooltip content itself is not stored when it is left at default.

**Worksheet titles that ARE customised** (these are stored, unlike tooltips). All use bold white 11pt text with `fontalignment='1'` (centred):

| Worksheet | Exact title text |
|---|---|
| `Sheet 1` | `Anaemia-Survival Stats` |
| `Sheet 1 (2)` | `Diabetes-Survival Stats` |
| `Sheet 1 (3)` | `High Blood Pressure-Survival Stats` |
| `Sheet 1 (4)` | `Sex-Survival Stats` |
| `Sheet 1 (5)` | `Smoking-Survival Stats` |
| `Sheet 6` | `Age - Survival Stats` |
| `Sheet 6 (2)` | `Creatinine Phosphokinase - Survival Stats` |
| `Sheet 6 (3)` | `Ejection Fraction - Survival Stats` |
| `Sheet 6 (4)` | `Platelets - Survival Stats` |
| `Sheet 6 (5)` | `Serum Creatinine - Survival Stats` |
| `Sheet 6 (6)` | `Serum Sodium - Survival Stats` |
| `Sheet 6 (7)` | `Time - Survival Stats` |
| `Sheet 6 (8)` | `Age-Time - Survival Stats` |
| `Sheet 6 (9)` | `Age-Sex - Survival Stats` |
| The five `Sheet 15` cards | No custom title; titles are hidden on the dashboard |

---

## 15. BUSINESS LOGIC

Stated carefully: the workbook records *what was built*, not *why*. Everything below is either the mechanical logic that is in the file (✓) or a reading of it (△).

**What business problem was identified (△ INFERRED).** Heart failure patients vary widely in outcome, and clinicians and analysts want to know which recorded attributes travel with mortality. The dashboard treats that as a profiling problem rather than a prediction problem: it does not model risk, it displays how the cohort splits on every available attribute.

**What data was needed (✓).** A single patient-level clinical record file with one row per patient, containing a binary mortality outcome (`DEATH_EVENT`), a follow-up period (`time`), four binary comorbidity or lifestyle flags (`anaemia`, `diabetes`, `high_blood_pressure`, `smoking`), a demographic flag (`sex`), and six continuous clinical measurements (`age`, `creatinine_phosphokinase`, `ejection_fraction`, `platelets`, `serum_creatinine`, `serum_sodium`).

**How the data was transformed (✓).**
1. The CSV was read with a `textscan` connection using UTF-8, comma separator, header row, `en_US` locale.
2. The whole table was extracted to Hyper with no row limit and no extract filter.
3. All 13 columns were given display captions.
4. Six binary integer columns were converted from measure to dimension with ordinal type.
5. Value aliases decoded `0`/`1` into clinical language on all six.
6. Seven bins were created on the continuous measures using Tableau's suggested bin sizes.
7. Five string-literal calculated fields were created to caption the KPI cards.
8. One constant `0` measure was created to enable dual-axis donuts.

**What KPIs were selected (✓).** Cohort size, death count, male count, female count, mean age. All are counts or a mean. No rates, no ratios, no targets.

**What dimensions were analysed (✓).** `Death Event` (the outcome, present on every chart), `Sex`, `Anaemia`, `Diabetes`, `High Blood Pressure`, `Smoking`, plus seven binned continuous dimensions.

**What comparisons were made (✓).**
- Outcome crossed with each binary attribute, as a 4-way donut with counts and percent of total (5 charts).
- Outcome across the distribution of each continuous biomarker, as a stacked histogram (7 charts).
- Outcome against two continuous variables at once, as a scatter (1 chart).
- Mean age compared across four outcome-by-sex cells with individual points visible (1 chart).

**What trends were intended to be identified (△ INFERRED).** The design points at three things: whether the red (`Death`) proportion is visually larger in the presence of each comorbidity; where along each biomarker's range the red mass concentrates; and whether outcome separation is different for men and women. Note that `time` is a follow-up duration, not a calendar date, so **this dashboard contains no time series and cannot show a trend over time.** That is a distinction worth stating plainly rather than glossing.

**What decisions a business user could make (△ INFERRED).** Identify which recorded attributes deserve a formal statistical test or a predictive model; decide which biomarker thresholds are worth investigating for a risk score; decide whether a sex-stratified analysis is warranted; and communicate cohort composition to a clinical stakeholder.

---

## 16. KEY INSIGHTS THE DASHBOARD IS DESIGNED TO ENABLE

No actual data values were read, so no findings are claimed.

### A. Insights explicitly encoded by the dashboard

These are things the dashboard computes and displays as a matter of construction:

1. The cohort size, death count, male count, female count and mean age are computed and displayed as five standing figures.
2. For each of anaemia, diabetes, high blood pressure, sex and smoking, the dashboard computes the count and the **percent of total** for each of the four combinations of that attribute with the survival outcome.
3. For each of age, creatinine phosphokinase, ejection fraction, platelets, serum creatinine, serum sodium and follow-up time, the dashboard computes the count of patients per fixed-width bin, stacked by outcome.
4. For the four outcome-by-sex cells, the dashboard computes and draws the **mean age per cell** as a reference line.
5. Selecting any mark propagates a highlight on `Death Event` across all 19 views at once.

### B. Questions the dashboard enables users to answer

- "How large is this heart failure cohort, and how is it split by sex?"
- "How many patients died during follow-up?"
- "What share of anaemic patients died, compared with the share of non-anaemic patients who died?" (and the same for diabetes, hypertension, smoking and sex)
- "Across the range of ejection fraction, where do deaths concentrate?" (and the same for the other six binned measures)
- "Is the age profile of patients who died different from those who survived, and does that differ by sex?"
- "If I restrict to men only, does every one of those patterns change?" (via the Sex dropdown, noting the KPI cards will not respond)
- "Which marks anywhere on the dashboard belong to the same outcome class as the one I just clicked?" (via the highlight action)

### C. Actual findings verifiable from the available data

**None can be stated.** The underlying values live only in the binary `.hyper` extract, and no Hyper reader is available in this environment. No row count, no mortality rate, no distribution shape and no correlation can be verified from the files supplied. ✗ NOT AVAILABLE.

---

## 17. TECHNICAL IMPLEMENTATION SUMMARY

```
DATA SOURCE
  heart_failure_clinical_records_dataset.csv
  13 columns, one row per patient
  /Users/atharvadevne/UIC/Business Data Visualization/Heart Fail Prediction
        |
        v
DATA CONNECTION
  Tableau textscan (flat file) connector
  UTF-8, comma-separated, header row, en_US locale
  wrapped in federated.15n4u4511e3xfk1749m9r1i714e1
  Extract enabled, count = -1 (all records), no extract filter
  Materialised to #TableauTemp_1yyvr7n0uz5nmh12wm62y1t1ntc5.hyper
        |
        v
DATA MODEL
  Single table. No joins, no relationships, no unions, no blends.
        |
        v
DATA CLEANING (all inside Tableau, no external prep)
  13 field captions applied
  6 integer flags converted measure -> dimension (ordinal)
  6 fields value-aliased: 0/1 -> Surivive/Death, Negative/Positive,
                          Female/Male, " Non-Smoker"/Smoker
  7 bins created on the continuous measures (Tableau-suggested sizes)
        |
        v
CALCULATED FIELDS  (13 total, no LODs, no IF/CASE)
  7 x bin calculations
  5 x string literal captions for KPI cards
  1 x constant 0 measure to enable dual-axis donuts
  + 1 built-in table calculation: Percent of Total (PctTotal, along Rows)
        |
        v
KPIs  (5)
  CNT(DEATH_EVENT)                       -> Total Individuals
  CNT(DEATH_EVENT) filtered DEATH_EVENT=1 -> Total Deaths
  CNT(sex) filtered sex=1                -> Total Males
  CNT(sex) filtered sex=0                -> Total Females
  AVG(age)                               -> Average Age
        |
        v
WORKSHEETS  (19)
  5  dual-axis donuts     (Pie + Pie, crossed colour, PctTotal labels)
  7  stacked histograms   (bin on Columns, CNT on Rows, outcome on Colour)
  1  scatter              (age vs time, unaggregated, outcome on Colour)
  1  disaggregated dot plot with per-cell average reference line
  5  text/BAN KPI cards
        |
        v
DASHBOARD  (1)
  "Dashboard 1", 1900 x 1050 range sizing, black background
  Fully tiled, nested horizontal/vertical flow containers
  19 worksheet zones + 1 color legend + 1 filter dropdown
  Auto-generated Phone layout (vscroll, 4450 px)
        |
        v
FILTERS / ACTIONS
  Sex dropdown -> filter-group 3 -> 14 worksheets (NOT the KPI cards)
  3 hard-coded worksheet filters on the Deaths/Males/Females cards
  1 highlight action on "Death Event", dashboard-wide, on-select, auto-clear
        |
        v
FINAL USER EXPERIENCE
  A single dark screen showing cohort headline numbers, five comorbidity
  donuts, seven biomarker histograms and two scatter-style views, all colour
  coded green for survival and red for death, with one dropdown to restrict
  by sex and click-to-highlight linking every view on the outcome field.
```

---

## 18. INTERVIEW EXPLANATION

Use this as a spoken narrative. Everything in it is supported by the workbook.

> "This one is a heart failure survival dashboard. The dataset is patient-level clinical records, 13 columns, one row per patient: a binary mortality flag, a follow-up period, four comorbidity flags for anaemia, diabetes, high blood pressure and smoking, plus sex, age and five clinical measurements like ejection fraction, serum creatinine and serum sodium.
>
> I built it because the raw file is basically unreadable as a table. It is all zeros and ones and unlabelled biomarker columns. The question I wanted the dashboard to answer was simple to state and hard to see in the data: for every attribute we record about a heart failure patient, how does the population split between survival and death?
>
> The data came in as a single CSV read through Tableau's flat file connector, comma-separated with a header row, and I extracted the whole thing to Hyper with no row limit so the workbook is self-contained and fast. There is only one table, so there is no join or relationship layer at all, and I would not pretend otherwise. That was a deliberate scope decision. The complexity in this project is not in the data model, it is in the preparation and the visual grammar.
>
> The preparation is where most of the real work sits. First I renamed all 13 columns to readable captions. Then, and this is the important one, Tableau imports those zero-one flag columns as measures, so it wants to sum them, which is meaningless. I converted six of them to ordinal dimensions so they could drive colour, labels and filters properly. Then I aliased every one of those binary values at the data source level, so zero and one became Survive and Death, Negative and Positive, Female and Male, Non-Smoker and Smoker. Because I did that at the source rather than in each sheet, all 19 worksheets inherit it and I only had to define it once. Finally I created seven bins on the continuous measures so I could draw distributions.
>
> For KPIs I picked cohort size, total deaths, male count, female count and average age. I built each one as its own worksheet with a string constant on the Text shelf for the caption and a single aggregate next to it, then hid the titles on the dashboard. Total Deaths, Total Males and Total Females each carry a hard worksheet filter on the member value, so the card is doing the filtering, not the sheet.
>
> The calculations are deliberately light. Seven bins, five string literals for the card captions, and one constant zero measure. That last one is a technique rather than a business calculation: I put the zero measure on Rows twice to create a dual axis, set both mark types to Pie, made the second pie smaller and solid black to match the background, and turned its labels off. That is how you build a donut in Tableau, since there is no donut mark type. For the wedge labels I used the built-in Percent of Total table calculation computed along Rows, so each wedge shows both its count and its share.
>
> For the distributions I used the same grammar seven times: the bin on Columns, a count on Rows, and the death event on Colour, green for survived and red for died. Repeating one visual form across seven biomarkers means a reader learns how to read the chart once and then reads six more for free.
>
> There are two views that break the pattern on purpose. One is a scatter of age against follow-up time, where I put both fields on the shelves as continuous dimensions rather than aggregated measures so every record draws its own mark. The other is a dot plot of age split by outcome and then by sex, where I switched off Aggregate Measures so you see the individual spread, and added an average reference line scoped per cell so each of the four groups gets its own mean line. That view shows distribution, not just counts.
>
> For the dashboard itself, 1900 by 1050, black background, fully tiled with nested flow containers rather than floating objects, so it reflows cleanly. Nineteen worksheets, one colour legend and one sex filter dropdown, and Tableau's auto-generated phone layout on top.
>
> For interactivity I went with one highlight action on Death Event, scoped to the whole dashboard, triggered on select with auto-clear. Click any mark anywhere and every other view dims everything that is not the same outcome class. Combined with the sex dropdown, which is applied to the 14 chart sheets, that gives you two ways to interrogate the same picture.
>
> If I were to extend it, the honest gaps are these: I would add a mortality rate KPI rather than only counts, I would put the sex filter on the KPI cards too so the whole dashboard moves together, I would set my own bin sizes instead of accepting Tableau's suggested widths, and I would fix two data quality issues I can see in my own aliases, a misspelling of Survive and a leading space on Non-Smoker.
>
> Skills-wise this shows data source level aliasing and role management, binning, dual-axis chart construction, table calculations, reference lines, disaggregated views, filter scoping across sheet groups, dashboard action design, container-based layout, and a consistent dark visual system across nineteen views."

---

## 19. RESUME-READY PROJECT DESCRIPTION

Only verified facts. No invented percentages, record counts or outcomes.

**Healthcare Analytics Dashboard, Heart Failure Survival Profiling (Tableau)**

- Built a 19-worksheet Tableau dashboard profiling heart failure patient survival across 13 clinical and demographic attributes, using a single-table CSV extracted to Hyper with no row limit, delivered as a fixed 1900x1050 dark-theme canvas and published to Tableau Public.

- Engineered the semantic layer entirely in Tableau: applied display captions to all 13 source fields, converted six binary integer flags from measures to ordinal dimensions, and defined data source level value aliases decoding 0/1 codes into clinical terms (Survive/Death, Positive/Negative, Male/Female, Smoker/Non-Smoker) so all 19 worksheets inherited the decoding from a single definition.

- Constructed five dual-axis donut charts from a constant-zero placeholder measure with a crossed two-field colour encoding and a Percent of Total table calculation computed along Rows, giving each comorbidity a simultaneous count and share view against the mortality outcome.

- Designed seven fixed-width binned histograms and two disaggregated views, including a dot plot with an `average` reference line scoped per cell, to expose distribution and spread of six clinical biomarkers and follow-up time by survival outcome.

- Implemented dashboard interactivity with a dashboard-scoped highlight action on the mortality outcome field and a Sex dropdown filter applied to a 14-worksheet filter group, built on a fully tiled nested-container layout with an auto-generated phone layout.
