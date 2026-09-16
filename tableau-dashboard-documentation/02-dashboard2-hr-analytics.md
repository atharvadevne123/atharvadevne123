# DASHBOARD 2: HR Analytics Dashboard

> **Screenshot slot.** Paste your own dashboard screenshot here.
>
> `![HR Analytics Dashboard](screenshots/dashboard2_screenshot.png)`
>
> **Tableau Public link slot:** `_______________________________________________`
>
> (The workbook XML contains the publish target `https://public.tableau.com/workbooks/HRAnalyticsDashboard_17561606616710`, dashboard path `/workbooks/HRAnalyticsDashboard_17561606616710/HRDashboard`, revision 1.1. Verify the live viz URL yourself before using it.)
>
> Coordinate-accurate layout wireframe generated from the XML: `screenshots/dashboard2_hr_analytics_layout.svg`

---

## 1. DASHBOARD OVERVIEW

| Item | Value | Evidence |
|---|---|---|
| Dashboard name | `HR Dashboard ` | ✓ DIRECTLY VERIFIED. **Note the trailing space.** The XML is `<dashboard name='HR Dashboard '>` and every action targets `value="HR Dashboard "` with that space. It is part of the actual object name. |
| Workbook name | `HR Analytics Dashboard.twb` (inside a packaged archive) | ✓ DIRECTLY VERIFIED |
| Tableau version | Document format `version='18.1'`, `original-version='18.1'`; `source-build='2025.2.0 (20252.25.0514.2217)'`; build comment `20252.25.0723.1135` | ✓ DIRECTLY VERIFIED |
| Source platform | `source-platform='mac'` | ✓ DIRECTLY VERIFIED |
| Publish target | `repository-location derived-from='https://public.tableau.com/workbooks/HRAnalyticsDashboard_17561606616710?rev=1.0'`, `id='HRAnalyticsDashboard_17561606616710'`, `revision='1.1'`. The dashboard itself: `id='HRDashboard'`, `path='/workbooks/HRAnalyticsDashboard_17561606616710'` | ✓ DIRECTLY VERIFIED |
| `xml:base` | `https://public.tableau.com` | ✓ DIRECTLY VERIFIED |
| Author / owner | Atharva Devne. **Confirmed by the author.** The workbook itself stores no author field. | ✓ CONFIRMED BY AUTHOR (not from the file) |
| Author evidence in the file | Source file paths are `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main`, so the macOS account was `atharvadevne`. The `-main` suffix is the naming convention produced by downloading a GitHub repository ZIP of a branch called `main`. | ✓ VERIFIED path; the `-main` reading is △ INFERRED |
| Dashboard dimensions | 1580 x 900 px, `sizing-mode='fixed'` | ✓ DIRECTLY VERIFIED |
| Dashboard UUID | `{30867C40-EA91-4DA5-AF47-E92ACECA09BD}` | ✓ DIRECTLY VERIFIED |
| Dashboard-level style | `parameter-ctrl` text `#ffffff`; `parameter-ctrl-title` text `#f1ce63` in `Tableau Semibold` | ✓ DIRECTLY VERIFIED |

### Dashboards contained in the workbook

| # | Dashboard name | Analyzed here |
|---|---|---|
| 1 | `HR Dashboard ` | Yes. It is the only dashboard in the workbook. |

**Stories:** none. ✓ DIRECTLY VERIFIED

### Purpose, business problem, audience, story

Unlike Dashboard 1, this workbook does contain one piece of authored text: the dashboard title text object reads **`HR ANALYTICS DASHBOARD`** (zone id 7). ✓ DIRECTLY VERIFIED. Beyond that there is no description, no annotation and no caption. ✗ NOT AVAILABLE as stated fact.

What can be read off the structure (△ INFERRED):

- **Purpose (inferred).** Attrition analysis. `Attrition Count` is the measure behind five of the seven worksheets, and four of the seven worksheet names contain the word "Attrition".
- **Business question (inferred).** "Who is leaving the organisation, from which departments, education fields, age bands and genders, and how does that sit against headcount and job satisfaction?"
- **Project type (confirmed by the author).** **Self-directed. Built for the author's own skill development**, not for a course, a client or an employer.
- **Dataset origin (confirmed by the author).** **Kaggle.** A public dataset.
- **Intended audience (inferred).** The design is framed for HR business partners, a people analytics function or HR leadership: the KPI strip leads with headcount and attrition, which is the standard opening for an HR leadership view. In practice the audience is anyone reviewing the author's portfolio.
- **Overall story (inferred).** A title bar with one global Education filter, then a five-tile KPI strip with a companion gender breakdown, then three mid-canvas views splitting attrition by department, headcount by age band and satisfaction by job role, then two lower views splitting attrition by education field and by gender within age band. Every chart is click-to-filter, so the dashboard functions as an exploratory cross-filtering surface rather than a fixed report.

---

## 2. DATA SOURCE INVENTORY

This workbook contains **five** `<datasource>` elements. One is the parameter container, four are real connections, and **only one of the four is actually used**. Each is documented separately below.

| Data Source | Type | Connection | Tables/Files | Important Fields | Live/Extract | Notes |
|---|---|---|---|---|---|---|
| `Parameters` | Parameter container (Tableau built-in, not a real connection) | `hasconnection='false'` | none | `[Age Parameter]` (caption `Bin Size`) | n/a | Holds the single parameter in the workbook |
| `HR data (HR Data)` (`federated.0f0h03p1it3gvo176rhln1y1tx4v`) | Federated over a flat file | **Two** named connections declared: (a) `excel-direct` named `HR Data` pointing at `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main/HR data.csv`; (b) `textscan` named `HR_data` pointing at directory `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main`, filename `HR_data.csv`. **The active relation uses the `textscan` connection.** | 1 table: `[HR_data#csv]` | `Attrition`, `Employee Count`, `Department`, `Education Field`, `Gender`, `Job Role`, `Job Satisfaction`, `Age`, `CF_age band` | **Extract**, `enabled='true'`, `count='-1'`, `units='records'` | **This is the only data source any worksheet uses.** All 7 worksheets and the dashboard bind to it. |
| `HR Data.xlsx - HR data` (`federated.049m4yg1psanb61b4tu3001365fp`) | Federated over a flat file | `textscan`, directory `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main`, filename `HR Data.xlsx - HR data.csv` | 1 table: `[HR Data.xlsx - HR data#csv]` | Same 39-column schema | **Extract**, `count='-1'` | **Unused.** No worksheet references it. |
| `HR data` (`federated.1g91kqr1twrfkg14hluc71es07jw`) | Federated over a flat file | `textscan`, same directory, filename `HR data.csv` | 1 table: `[HR data#csv]` | Same 39-column schema | **Extract**, `count='-1'` | **Unused.** |
| `HR data (2)` (`federated.1u260d51era62r18fltmd02kg202`) | Federated over a flat file | `textscan`, same directory, filename `HR data.xlsx` | 1 table: `[HR data.xlsx]` | Same 39-column schema | **Extract**, `count='-1'` | **Unused.** |

✓ DIRECTLY VERIFIED for every cell.

### 2.1 Notes on the four connections

**All four point at the same folder and the same 39-column schema.** The four filenames differ (`HR_data.csv`, `HR data.csv`, `HR data.xlsx`, `HR Data.xlsx - HR data.csv`), which is the signature of **repeated import attempts of the same dataset in different file formats and naming conventions** before settling on one. That is an observation, not a criticism. △ INFERRED from the naming pattern; the XML does not record intent.

**Why this matters for the packaged archive:** all four data sources have extracts enabled, which is exactly why this `.twbx` carries **four** `.hyper` files of 196,608 bytes each in `Data/tableau-temp/`, three of which are dead weight. ✓ VERIFIED (the archive listing).

**The `excel-direct` named connection is worth flagging.** The active data source declares a connection of `class='excel-direct'` whose `filename` is `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main/HR data.csv`, that is, the Excel connector pointed at a `.csv` path. Its attributes are `cleaning='no'`, `compat='no'`, `interpretationMode='0'`, `validate='no'`, `dataRefreshTime=''`. It is declared but the `<relation>` element binds to the **`textscan`** connection, not this one. ✓ VERIFIED.

### 2.2 Active data source, detailed attributes

| Attribute | Value |
|---|---|
| Caption | `HR data (HR Data)` |
| Internal name | `federated.0f0h03p1it3gvo176rhln1y1tx4v` |
| `inline` | `true` (embedded) |
| Active connection | `textscan.0ry86yc0w1h17j1d0atub17ll83k` |
| File | `HR_data.csv` |
| Directory | `/Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main` |
| Relation | `<relation name='HR_data.csv' table='[HR_data#csv]' type='table' />` |
| Number of tables | 1 |
| Source columns | 39 |
| Database / schema | None (flat file) |
| Extract | `enabled='true'`, `count='-1'`, `units='records'`, `user-specific='false'` |
| Extract relation | `<relation name='Extract' table='[Extract].[Extract]' type='table' />` under `<properties context='extract'>` |
| Data source filters | **One.** A `<shared-view>` filter on `[none:Education:nk]`, see section 8. |
| Extract filters | **None.** |
| Custom SQL | **None.** `type='table'`, no SQL text. |
| Aliases | **None.** No `<aliases>` element exists anywhere in this workbook. |
| Renamed fields | **Yes**, 10 fields carry captions, 6 of which are the `Name1` pattern. See section 4. |
| Hidden fields | **Yes**, 4 auto-generated hidden action groups. See section 5. |
| Geographic roles | **None.** No map is used. |

### 2.3 The 39 source columns (identical across all four data sources)

| # | Column | Datatype | | # | Column | Datatype |
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

**The three `CF_` columns matter.** `CF_age band`, `CF_attrition label` and `CF_current Employee` carry the `CF_` prefix that Tableau uses when a **calculated field is exported to a flat file**. They arrive as ordinary source columns here, which means **that derivation was done upstream, outside this workbook**, and this workbook consumes the result. `CF_age band` in particular is used directly on a shelf without any calculation in this workbook. △ INFERRED from the naming convention; ✓ VERIFIED that they are plain source columns here with no calculation attached.

---

## 3. DATA MODEL / RELATIONSHIPS / JOINS

**Each of the four real data sources is a single flat table. There is no data model.** ✓ DIRECTLY VERIFIED

| Check | Result |
|---|---|
| Joins | None. Each `<connection>` holds exactly one `<relation type='table'>`. |
| Relationships (noodles) | None. The `<object-graph>` contains a single object per data source. |
| Unions | None. |
| **Blending** | **None**, and this is worth stating precisely. Four data sources exist, which is the usual precondition for blending, but no worksheet references more than one of them. There is no `<datasource-dependencies>` in any worksheet pointing at two data sources, and no linking field is defined. The other three data sources are simply inert. |
| Nested joins | None. |
| Cardinality / referential integrity | Not applicable. |
| Custom SQL | None. |

### Plain English

The workbook reads one CSV, `HR_data.csv`, as a single flat table of 39 columns at one row per employee. Tableau wraps it in a federated container and extracts it whole to Hyper. Three other data sources point at variants of the same file and were left in the workbook without ever being used. Every worksheet and the dashboard bind to the single active source, plus the `Parameters` container for the one parameter. There is nothing to join, relate, union or blend.

### Text representation

```
HR_data.csv   (39 columns, one row per employee)
      |
      |  textscan connection, full extract (count = -1)
      v
federated.0f0h03p1it3gvo176rhln1y1tx4v   "HR data (HR Data)"   [ACTIVE]
      |
      +--> shared-view data source filter on [Education]
      +--> 7 worksheets
      +--> HR Dashboard

Parameters  (no connection)
      |
      +--> [Age Parameter] "Bin Size"
               |
               +--> size-parameter of [Age (bin)]
               +--> slider control on HR Dashboard

HR Data.xlsx - HR data.csv  --> federated.049m4yg1psanb61b4tu3001365fp   [UNUSED, extract present]
HR data.csv                 --> federated.1g91kqr1twrfkg14hluc71es07jw   [UNUSED, extract present]
HR data.xlsx                --> federated.1u260d51era62r18fltmd02kg202   [UNUSED, extract present]
```

---

## 4. DATA PREPARATION / CLEANING

### 4.1 Field renaming (captions)

Ten fields in the active data source carry captions. Six of them follow the `Name1` pattern.

| Raw column | Caption applied | Comment |
|---|---|---|
| `Department` | `Department1` | |
| `Education` | `Education1` | |
| `Education Field` | `Education Field1` | |
| `Gender` | `Gender1` | |
| `Job Role` | `Job Role1` | |
| `Job Satisfaction` | `Job Satisfaction1` | Also role-converted, see 4.2 |
| `emp no` | `Emp No` | Genuine readability rename |
| `CF_age band` | `CF age band` | Underscore removed |
| `CF_attrition label` | `CF attrition label` | Underscore removed |
| `CF_current Employee` | `CF current Employee` | Underscore removed |

**Honest reading of the `Name1` pattern (△ INFERRED).** A trailing `1` is what Tableau appends automatically when a field name would collide with an existing one, typically after replacing or re-adding a data source. These are almost certainly **not intentional business renames**. They are collision artefacts that were left in place. This is worth knowing because a hiring manager reading `Department1` in a legend will ask about it. Note that the **tooltips override the display**: the custom tooltips spell out `Department:`, `Gender:`, `Job Role:`, `Education Field:` and `Job Satisfaction:` as hand-typed labels, so the `1` does not leak into the tooltip text. ✓ VERIFIED from the tooltip XML.

### 4.2 Role conversion

| Field | Role | Type | Note |
|---|---|---|---|
| `[Job Satisfaction]` | dimension | ordinal | Converted from measure. `aggregation='Sum'` retained as the default. Used as a discrete column header on the highlight table. |
| `[Employee Number]` | dimension | ordinal | Converted from measure, so it is not summed. |
| `[Age]` | measure | quantitative | Left as a measure, used with `AVG` on the KPI strip and as the input to the bin |
| `[CF_current Employee]` | measure | quantitative | Left as a measure. Not used on any sheet. |

### 4.3 Parameterised binning

| Bin field | Source field | Bin size |
|---|---|---|
| `[Age (bin)]` | `[Age]` | **`size-parameter='[Parameters].[Age Parameter]'`** |

Exact definition: `<calculation class='bin' decimals='0' formula='[Age]' peg='0' size-parameter='[Parameters].[Age Parameter]' />`

**What was done:** `Age` was binned, but instead of a hard-coded width the bin size is bound to a parameter, so the end user can change the bin width at view time from a slider on the dashboard.
**Why it was likely necessary (△ inferred):** an age histogram reads very differently at 2-year buckets versus 10-year buckets. Letting the user choose avoids committing to one granularity.
**This is the single most advanced data-preparation technique in either workbook.** ✓ VERIFIED.

Contrast with Dashboard 1, where all seven bins are fixed-size.

### 4.4 Cleaning calculated fields

See section 6 for full detail. In summary:

| Calculated field | Formula | Cleaning function |
|---|---|---|
| `Attrition Count` | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END` | Converts a `Yes`/`No` **string** column into a numeric 0/1 flag so it can be aggregated. This is a genuine type-and-encoding transformation. |

### 4.5 Transformations that are NOT present

| Transformation | Present? |
|---|---|
| Null handling (`ISNULL`, `IFNULL`, `ZN`) | **No** |
| Duplicate handling | **No** |
| Explicit type casts (`INT()`, `STR()`, `FLOAT()`) | **No.** The `IF/THEN` in `Attrition Count` changes the encoding but is not a cast function. |
| Date conversions / date parts | **No.** The dataset has **no date field at all.** `Years At Company`, `Years In Current Role`, `Years Since Last Promotion`, `Years With Curr Manager` and `Total Working Years` are integer tenure counts, not dates. |
| String manipulation (`LEFT`, `SPLIT`, `TRIM`, `REPLACE`, `CONTAINS`) | **No** |
| Split fields | **No** |
| Pivot | **No** |
| Union | **No** |
| **Value aliases** | **No.** Unlike Dashboard 1, this workbook uses no aliasing at all. |
| **Groups (data groups)** | **No.** The four `<group>` elements present are auto-generated hidden action groups (`user:auto-column='sheet_link'`), not user-created groups. |
| Sets | **No** |
| Hierarchies / drill paths | **No** |
| Geographic roles | **No** |
| Tableau Prep flow | **No** |
| Extract filter | **No** |
| Upstream derivation | **Partly, but outside this workbook.** The `CF_age band`, `CF_attrition label` and `CF_current Employee` columns arrive already derived. |

---

## 5. COMPLETE FIELD INVENTORY

### 5.1 Fields declared in the active data source (18 `<column>` elements)

| Field Name | Original Name | Data Type | Role | Aggregation | Table | Description / Usage |
|---|---|---|---|---|---|---|
| `Age (bin)` | derived from `[Age]` | integer | Dimension (ordinal) | None | `HR_data.csv` | Columns shelf of `No. of Employee by Age Group`. Bin width driven by the `Bin Size` parameter. |
| `Age` | `Age` | integer | Measure | (default) | `HR_data.csv` | `AVG(Age)` on the KPI strip; input to `Age (bin)` |
| `CF age band` | `CF_age band` | string | Dimension (nominal) | None | `HR_data.csv` | Columns shelf of `Attrition Rate by Gender for Different Age Group`; manually sorted |
| `CF attrition label` | `CF_attrition label` | string | Dimension (nominal) | None | `HR_data.csv` | Declared but **not used on any worksheet** |
| `CF current Employee` | `CF_current Employee` | integer | Measure | None | `HR_data.csv` | Declared but **not used on any worksheet** |
| `Attrition Count` | `[Calculation_231935388807032832]` | integer | Measure | Sum in use | `HR_data.csv` | **The core measure.** Drives 5 of the 7 worksheets |
| `Attrition Rate` | `[Calculation_231935388807876609]` | real | Measure | User-defined aggregate | `HR_data.csv` | KPI strip only |
| `Active Employees` | `[Calculation_231935388808294402]` | integer | Measure | User-defined aggregate | `HR_data.csv` | KPI strip only |
| `Department1` | `Department` | string | Dimension (nominal) | None | `HR_data.csv` | Colour of `Department wise Attrition`; source field of filter Action1 |
| `Education Field1` | `Education Field` | string | Dimension (nominal) | None | `HR_data.csv` | Rows shelf of `Education Field wise Attrition`; source field of filter Action5 |
| `Education1` | `Education` | string | Dimension (nominal) | None | `HR_data.csv` | The one data source level filter, exposed as a dashboard dropdown |
| `Employee Number` | `Employee Number` | integer | Dimension (ordinal) | None | `HR_data.csv` | Declared, **not used on any worksheet** |
| `Gender1` | `Gender` | string | Dimension (nominal) | None | `HR_data.csv` | Rows/Colour on two worksheets |
| `Job Role1` | `Job Role` | string | Dimension (nominal) | None | `HR_data.csv` | Rows shelf of `Job Satisfaction Rating` |
| `Job Satisfaction1` | `Job Satisfaction` | integer | Dimension (ordinal) | Sum | `HR_data.csv` | Columns shelf of `Job Satisfaction Rating` |
| `Number of Records` | auto-generated | integer | Measure | Sum | `HR_data.csv` | Formula `1`. `user:auto-column='numrec'`. **Not used on any worksheet.** |
| `Emp No` | `emp no` | string | Dimension (nominal) | None | `HR_data.csv` | Declared, **not used on any worksheet** |
| `HR_data.csv` object id | internal | table | Measure | None | `HR_data.csv` | Tableau internal table object |

Plus `Employee Count` (source column 19), which is **not** given its own `<column>` override but is used heavily as `SUM([Employee Count])`.

### 5.2 Ad-hoc worksheet-level calculated field

| Field Name | Internal Name | Formula | Scope | Purpose |
|---|---|---|---|---|
| `min(1)` | `[Calculation_1302666200262176769]` | `min(1)` | `user:unnamed='Attrition Rate by Gender for Different Age Group'`, that is, created inside that worksheet and never promoted | Axis placeholder for the dual-axis donut construction |

### 5.3 Parameter

| Field Name | Caption | Data Type | Domain | Current Value | Range |
|---|---|---|---|---|---|
| `[Age Parameter]` | `Bin Size` | real | `param-domain-type='range'` | `3.0` | min `2.0`, max `10.0`, granularity `1.0` |

### 5.4 Hidden auto-generated action groups (4)

These are created automatically by Tableau when a dashboard filter action is defined. They are marked `hidden='true'` and `user:auto-column='sheet_link'`.

| Group name | Caption | Underlying level | Created by |
|---|---|---|---|
| `[Action (Age (bin))]` | `Action (Age (bin))` | `[Age (bin)]` | filter action `[Action2]` |
| `[Action (Department)]` | `Action (Department)` | `[Department]` | filter action `[Action1]` |
| `[Action (Department1)]` | `Action (Department1)` | `[Department]` | filter action `[Action1]` |
| `[Action (Education Field)]` | `Action (Education Field)` | `[Education Field]` | filter action `[Action5]` |

Each has the structure `<groupfilter function='crossjoin'><groupfilter function='level-members' level='[...]' /></groupfilter>`.

### 5.5 Field categorisation

| Category | Members |
|---|---|
| **Dimensions used on the dashboard** | `Department1`, `Education Field1`, `Education1`, `Gender1`, `Job Role1`, `Job Satisfaction1`, `CF age band`, `Age (bin)` |
| **Measures used on the dashboard** | `Employee Count` (SUM), `Attrition Count` (SUM), `Attrition Rate`, `Active Employees`, `Age` (AVG), `min(1)` |
| **Dates** | **None.** The dataset contains no date or datetime field. |
| **Geographic fields** | **None.** |
| **Calculated fields** | `Attrition Count`, `Attrition Rate`, `Active Employees`, `Number of Records`, `Age (bin)`, `min(1)` |
| **Parameters** | `[Age Parameter]` (`Bin Size`) |
| **Sets** | **None.** |
| **Groups** | 4 hidden auto action groups only. No user-created data groups. |
| **Bins** | 1 (`Age (bin)`, parameter-driven) |

### 5.6 Usage classification

| Classification | Fields |
|---|---|
| **Used on the dashboard** | `Attrition Count`, `Attrition Rate`, `Active Employees`, `Employee Count`, `Age`, `Age (bin)`, `CF age band`, `Department1`, `Education Field1`, `Education1`, `Gender1`, `Job Role1`, `Job Satisfaction1`, `min(1)`, `[Age Parameter]` |
| **Used inside other calculations** | `Attrition` (inside `Attrition Count`), `Attrition Count` (inside both `Attrition Rate` and `Active Employees`), `Employee Count` (inside both), `Age` (inside `Age (bin)`), `[Age Parameter]` (inside `Age (bin)`) |
| **Hidden** | The 4 auto action groups |
| **Declared but unused** | `CF attrition label`, `CF current Employee`, `Employee Number`, `Emp No`, `Number of Records` |
| **Source columns never surfaced** | 24 of the 39 source columns are never used on any shelf, filter or calculation: `Business Travel`, `Marital Status`, `Over Time`, `Over18`, `Training Times Last Year`, `Daily Rate`, `Distance From Home`, `Environment Satisfaction`, `Hourly Rate`, `Job Involvement`, `Job Level`, `Monthly Income`, `Monthly Rate`, `Num Companies Worked`, `Percent Salary Hike`, `Performance Rating`, `Relationship Satisfaction`, `Standard Hours`, `Stock Option Level`, `Total Working Years`, `Work Life Balance`, `Years At Company`, `Years In Current Role`, `Years Since Last Promotion`, `Years With Curr Manager`. ✓ VERIFIED by absence from every worksheet's `<datasource-dependencies>`. |

---

## 6. CALCULATED FIELDS

### Calculated Field: `Attrition Count`

- **Exact Tableau formula:** `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END`
- **Internal name:** `[Calculation_231935388807032832]`
- **Data type:** integer
- **Role / type:** measure, quantitative
- **Referenced fields:** `[Attrition]` (source column 0, string)
- **Used in worksheet(s):** `KPI`, `Attrition by Gender`, `Department wise Attrition`, `Education Field wise Attrition`, `Attrition Rate by Gender for Different Age Group` (5 of 7)
- **Used in KPI(s):** the `Attrition Count` KPI tile, and indirectly the `Attrition Rate` and `Active Employees` tiles
- **Purpose:** turn the textual `Yes`/`No` attrition flag into a numeric indicator so it can be summed.
- **Plain English explanation:** for every employee row, return 1 if that employee left, otherwise 0. Summing this field over any group therefore gives the number of leavers in that group.
- **Business logic:** attrition is defined strictly as `Attrition = 'Yes'`. There is no tenure qualification, no voluntary versus involuntary split, and no exclusion of any status. Whatever the source system meant by `Yes` is what this dashboard counts as attrition.
- **Dependencies on other calculated fields:** none. It is the **root** of the calculation chain.
- **Calculation type:** conditional, `IF/THEN/ELSE`. This is the only conditional logic in either workbook.

### Calculated Field: `Attrition Rate`

- **Exact Tableau formula:** `SUM([Calculation_231935388807032832])/SUM([Employee Count])`
  (written in the Tableau UI as `SUM([Attrition Count])/SUM([Employee Count])`)
- **Internal name:** `[Calculation_231935388807876609]`
- **Data type:** real
- **Role / type:** measure, quantitative
- **Referenced fields:** `[Attrition Count]` (calculated), `[Employee Count]` (source column 19)
- **Used in worksheet(s):** `KPI` only
- **Used in KPI(s):** the `Attrition Rate` tile
- **Purpose:** express attrition as a proportion of headcount rather than an absolute count.
- **Plain English explanation:** add up the leaver flags, add up the employee count, and divide. Because both halves are aggregates, the result is an **aggregate calculation**: it recomputes at whatever level of detail the view is at, rather than averaging row-level ratios. On the KPI tile the view has no dimensions, so it evaluates across the whole filtered population.
- **Business logic:** numerator is leavers, denominator is total employees. `Employee Count` is a source column that is 1 for every row (△ INFERRED, the standard IBM HR Analytics convention; the values themselves are inside the binary extract so this cannot be confirmed from the workbook. ✗ NOT VERIFIABLE here).
- **Dependencies on other calculated fields:** **depends on `Attrition Count`.**
- **Aggregation on the shelf:** `derivation='User'`, giving `[usr:Calculation_231935388807876609:qk]`, meaning Tableau treats the field's own aggregate definition as the aggregation rather than wrapping it.
- **Number formatting:** **none specified.** There is no `number-format` attribute anywhere in this workbook, so this ratio renders with Tableau's default number formatting rather than as a percentage. That is a real, verifiable gap.

### Calculated Field: `Active Employees`

- **Exact Tableau formula:** `SUM([Employee Count])- SUM([Calculation_231935388807032832])`
  (written in the Tableau UI as `SUM([Employee Count]) - SUM([Attrition Count])`)
  **Note the spacing exactly as stored: no space before the minus, one space after.**
- **Internal name:** `[Calculation_231935388808294402]`
- **Data type:** integer
- **Role / type:** measure, quantitative
- **Referenced fields:** `[Employee Count]`, `[Attrition Count]` (calculated)
- **Used in worksheet(s):** `KPI` only
- **Used in KPI(s):** the `Active Employees` tile
- **Purpose:** headcount remaining after attrition.
- **Plain English explanation:** total employees minus leavers.
- **Business logic:** treats the population as a closed set where every employee is either active or a leaver. There is no hire date or termination date in the dataset, so this is a snapshot figure, not a point-in-time headcount.
- **Dependencies on other calculated fields:** **depends on `Attrition Count`.**
- **Aggregation on the shelf:** `derivation='User'`, giving `[usr:Calculation_231935388808294402:qk]`.

### Calculated Field: `Age (bin)`

- **Exact Tableau definition:** `<calculation class='bin' decimals='0' formula='[Age]' peg='0' size-parameter='[Parameters].[Age Parameter]' />`
- **Data type:** integer
- **Role / type:** dimension, ordinal, `aggregation='None'`
- **Referenced fields:** `[Age]`, `[Parameters].[Age Parameter]`
- **Used in worksheet(s):** `No. of Employee by Age Group` (Columns shelf)
- **Purpose:** bucket employee age into user-controllable bands.
- **Plain English explanation:** put each employee into an age bucket whose width is whatever the `Bin Size` slider is currently set to, anchored at 0.
- **Business logic:** age band granularity is a user decision, not a fixed design decision.
- **Dependencies:** depends on the `[Age Parameter]` parameter.
- **This is a parameter-driven calculation**, the only one in either workbook.

### Calculated Field: `Number of Records`

- **Exact Tableau formula:** `1`
- **Data type:** integer, measure
- **Attribute:** `user:auto-column='numrec'`, that is, auto-generated by Tableau, not hand-created
- **Used in worksheet(s):** **none**
- **Purpose:** legacy Tableau auto-field. Present but unused.

### Calculated Field: `min(1)`

- **Exact Tableau formula:** `min(1)`
- **Internal name:** `[Calculation_1302666200262176769]`
- **Data type:** integer, measure
- **Scope:** ad-hoc inside `Attrition Rate by Gender for Different Age Group`
- **Used in worksheet(s):** that one worksheet
- **Purpose:** axis placeholder for the dual-axis donut.
- **Exact shelf expression:** the Rows shelf is literally
  `([federated.0f0h03p1it3gvo176rhln1y1tx4v].[usr:Calculation_1302666200262176769:qk] + [federated.0f0h03p1it3gvo176rhln1y1tx4v].[usr:Calculation_1302666200262176769:qk])`
- **Plain English:** a measure that always returns 1. Two copies on Rows create a dual axis so a second, smaller pie can be overlaid to form a donut hole.
- **Note on technique:** Dashboard 1 uses a constant `0` for the same job, Dashboard 2 uses `min(1)`. Both are standard variants of the same trick.

### 6.1 Dependency chain

```
[Attrition]  (source column, string 'Yes'/'No')
      |
      v
Attrition Count  =  IF [Attrition] = 'Yes' THEN 1 ELSE 0 END
      |
      +----------------------------+
      |                            |
      v                            v
Attrition Rate                Active Employees
 = SUM([Attrition Count])      = SUM([Employee Count])
   / SUM([Employee Count])       - SUM([Attrition Count])
      |                            |
      v                            v
   KPI tile 3                   KPI tile 4

[Age]  +  [Age Parameter] "Bin Size" (2.0 to 10.0, step 1.0, current 3.0)
      |
      v
Age (bin)   -->  Columns shelf of "No. of Employee by Age Group"
```

### 6.2 Calculation type census for Dashboard 2

| Calculation type | Present? | Detail |
|---|---|---|
| **LOD expressions** (`FIXED`, `INCLUDE`, `EXCLUDE`) | **No.** No `{` appears in any formula. |
| **Table calculations** | **Yes.** `PctTotal` on `SUM([Attrition Count])`, giving `[pcto:sum:Calculation_231935388807032832:qk]` |
| **Window calculations** | **No.** |
| **Running totals** | **No.** |
| **Percent-of-total** | **Yes**, on `Department wise Attrition` and `Attrition Rate by Gender for Different Age Group`. The tooltip labels it `% of Total Attrition Count along Table (Across)`. |
| **Rank calculations** | **No.** |
| **Date calculations** | **No.** There is no date field. |
| **Conditional calculations / IF-THEN-ELSE** | **Yes**, exactly one: `Attrition Count`. |
| **CASE statements** | **No.** |
| **Aggregate calculations** | **Yes**, two: `Attrition Rate` and `Active Employees`, both aggregate-over-aggregate. |
| **Parameters used inside calculations** | **Yes**, one: `[Age Parameter]` as the `size-parameter` of `[Age (bin)]`. |
| **Aggregations used on shelves** | `SUM`, `AVG`, `User` (the field's own aggregate definition), `None` (discrete dimension) |

---

## 7. PARAMETERS

| Parameter | Data Type | Current Value | Allowed Values | Used By | Purpose |
|---|---|---|---|---|---|
| `Bin Size` (internal name `[Age Parameter]`) | real (`float`) | `3.0` | `param-domain-type='range'`, `min='2.0'`, `max='10.0'`, `granularity='1.0'` (so effectively 2, 3, 4, 5, 6, 7, 8, 9, 10) | `[Age (bin)]` as its `size-parameter`; exposed on the dashboard as a **slider** control (zone id 13) titled `Age Size` | Let the viewer change the width of the age buckets at view time |

✓ DIRECTLY VERIFIED for every cell.

### How the parameter affects the dashboard

The parameter is bound to the `size-parameter` attribute of the `Age (bin)` calculation. It does **not** appear in any other formula, on any shelf, in any filter or in any action. Its effect is therefore surgical and single-target:

1. The user drags the `Age Size` slider on the dashboard between 2 and 10 in steps of 1.
2. Tableau recomputes `[Age (bin)]` with the new bin width.
3. The `No. of Employee by Age Group` worksheet redraws with wider or narrower bars. At `Bin Size = 2` the histogram is fine-grained; at `10` it collapses into a handful of decade-wide bands.
4. **Nothing else on the dashboard changes.** The KPI strip, the department pie, the job satisfaction table, the education field bars and the age band donuts are all unaffected, because none of them reference `[Age (bin)]`.

There is a second-order effect worth naming: because `No. of Employee by Age Group` is the source of filter action `[Action2]`, which passes `[Age (bin)]` to the rest of the dashboard, changing the bin size changes **what a click on that chart filters to**. A click at `Bin Size = 3` filters a 3-year band; the same click at `Bin Size = 10` filters a 10-year band. △ INFERRED from the action and bin definitions, which are both ✓ VERIFIED.

### Parameter control formatting

| Property | Value |
|---|---|
| Control zone | id `13`, `type-v2='paramctrl'`, `mode='slider'` |
| Position | x=55190 y=28000 w=9810 h=5444, that is, overlaid on the upper right of the `No. of Employee by Age Group` area |
| Displayed title | `Age Size` |
| Title colour | `#f1ce63` in `Tableau Semibold` (dashboard-level `parameter-ctrl-title` style rule) |
| Value text colour | `#ffffff` (dashboard-level `parameter-ctrl` style rule) |

**Naming inconsistency worth knowing:** the parameter's internal name is `Age Parameter`, its caption is `Bin Size`, and the control on the dashboard displays `Age Size`. Three different names for the same object. All three are ✓ VERIFIED in the XML.

---

## 8. FILTERS

### 8.1 Filter inventory

| Filter | Field | Type | Values / Condition | Scope | Effect |
|---|---|---|---|---|---|
| **Education (global)** | `[Education]` as `[none:Education:nk]` | Categorical, `function='level-members'`, `ui-enumeration='all'` | All members selected | **`<shared-view>` filter**, that is, "Apply to all worksheets using this data source". Exposed on the dashboard as a **dropdown** (zone id 29, sourced from `Department wise Attrition`) | Filters **all 7 worksheets** at once, including the KPI strip |
| Action filter: Department | `[Action (Department)]` | Categorical, `level-members`, all, `ui-action-filter='[Action1]'` | All | Auto-generated by `[Action1]` | Applied to `Attrition Rate by Gender for Different Age Group`, `Attrition by Gender`, `Education Field wise Attrition`, `Job Satisfaction Rating`, `KPI`, `No. of Employee by Age Group` |
| **Action filter: Department1 (with saved state)** | `[Action (Department1)]` | Categorical, **`function='member'`, `member='"R&D"'`**, `ui-enumeration='inclusive'`, `ui-action-filter='[Action1]'` | **Only `R&D`** | Applied to the same 6 worksheets | **See the important note below.** |
| Action filter: Age (bin) | `[Action (Age (bin))]` | Categorical, `level-members`, all, `ui-action-filter='[Action2]'` | All | Auto-generated by `[Action2]` | Applied to `Attrition Rate by Gender for Different Age Group`, `Attrition by Gender`, `Department wise Attrition`, `Education Field wise Attrition`, `Job Satisfaction Rating`, `KPI` |
| Action filter: Education Field | `[Action (Education Field)]` | Categorical, `level-members`, all, `ui-action-filter='[Action5]'` | All | Auto-generated by `[Action5]` | Applied to `Attrition Rate by Gender for Different Age Group`, `Attrition by Gender`, `Department wise Attrition`, `Job Satisfaction Rating`, `KPI`, `No. of Employee by Age Group` |
| Measure Names filter | `[:Measure Names]` | Categorical, `function='union'`, `op='manual'`, 5 explicit members | See 8.3 | Worksheet-only: `KPI` | Controls which 5 measures appear as KPI tiles and in what order |

### 8.2 The persisted `R&D` selection (important)

The workbook was saved while a mark representing `Department = "R&D"` was selected on the `Department wise Attrition` chart. Tableau persisted that selection as a member-level action filter:

```xml
<filter class='categorical' column='[federated.0f0h03p1it3gvo176rhln1y1tx4v].[Action (Department1)]'>
  <groupfilter function='member' level='[Department]' member='"R&amp;D"'
               user:ui-action-filter='[Action1]'
               user:ui-domain='database'
               user:ui-enumeration='inclusive'
               user:ui-marker='enumerate' />
</filter>
```

✓ DIRECTLY VERIFIED. It appears in six worksheets: `Attrition Rate by Gender for Different Age Group`, `Attrition by Gender`, `Education Field wise Attrition`, `Job Satisfaction Rating`, `KPI`, `No. of Employee by Age Group`. It does **not** appear in `Department wise Attrition`, which is the source of the action and so excludes itself.

**What this means in practice (△ INFERRED, but a direct consequence of the verified XML):** the dashboard as saved carries a live `R&D` filter state on six of its seven views. Depending on how it is opened and whether the action's `auto-clear` fires, a viewer may land on a dashboard that is already filtered to the R&D department rather than showing the full organisation. If you are demoing this, check the published view and be ready to explain it. If it does open filtered, the fix is to deselect the mark and re-save.

### 8.3 The `KPI` worksheet Measure Names filter

`<groupfilter function='union' user:op='manual'>` containing five explicit `member` entries, in this stored order:

| Order | Member | Rendered as |
|---|---|---|
| 1 | `[sum:Employee Count:qk]` | `SUM(Employee Count)` |
| 2 | `[sum:Calculation_231935388807032832:qk]` | `SUM(Attrition Count)` |
| 3 | `[usr:Calculation_231935388807876609:qk]` | `Attrition Rate` |
| 4 | `[usr:Calculation_231935388808294402:qk]` | `Active Employees` |
| 5 | `[avg:Age:qk]` | `AVG(Age)` |

A separate `<manual-sort column='[:Measure Names]' direction='ASC'>` carries a dictionary listing only the **first four** members. `[avg:Age:qk]` is not in the sort dictionary, which in Tableau means it sorts after the explicitly ordered members. ✓ VERIFIED.

### 8.4 Filter types NOT present

| Filter type | Present? |
|---|---|
| Extract filter | **No** |
| Context filter | **No** |
| Measure filter | **No.** Every filter is categorical on a dimension or on Measure Names. |
| Relative date filter | **No.** There is no date field. |
| Range / quantitative filter | **No** |
| Top N filter | **No** |
| Parameter-based filter | **No.** The parameter drives a bin size, not a filter. |
| Condition or formula filter | **No** |

### 8.5 Filter scope map

| Worksheet | Education (global) | Action(Department) | Action(Department1) = R&D | Action(Age (bin)) | Action(Education Field) | Measure Names |
|---|---|---|---|---|---|---|
| `KPI` | Yes | Yes | Yes | Yes | Yes | Yes |
| `Attrition by Gender` | Yes | Yes | Yes | Yes | Yes | no |
| `Department wise Attrition` | Yes | no (source of Action1) | no | Yes | Yes | no |
| `No. of Employee by Age Group` | Yes | Yes | Yes | no (source of Action2) | Yes | no |
| `Job Satisfaction Rating` | Yes | Yes | Yes | Yes | Yes | no |
| `Education Field wise Attrition` | Yes | Yes | Yes | Yes | no (source of Action5) | no |
| `Attrition Rate by Gender for Different Age Group` | Yes | Yes | Yes | Yes | Yes | no |

**Design observation (△ inferred):** the Education filter being scoped at the data source level rather than per-worksheet is the technically correct choice for a global control, and it is a meaningfully better pattern than Dashboard 1's filter group, which left the KPI cards out of scope. Here the KPI strip does respond to the global filter.

---

## 9. KPI IDENTIFICATION

All five KPIs live in **one** worksheet, `KPI`, built with Measure Names and Measure Values rather than as five separate worksheets. That is the structural difference from Dashboard 1.

Shared context for all five:

| Attribute | Value |
|---|---|
| Worksheet | `KPI` |
| Columns shelf | `[:Measure Names]` |
| Rows shelf | empty |
| Marks type | `Automatic` (text) |
| Marks > Text | `[Multiple Values]`, that is, Measure Values |
| Custom label | `<[Multiple Values]>` |
| Custom tooltip | `<[:Measure Names]>:  <[Multiple Values]>` in bold, measure name in black, value in `#2f5597` at 14pt |
| Dashboard zone | id `5`, x=1139 y=10667 w=83924 h=15111, `show-title='false'`. Spans roughly 84 percent of the canvas width in the upper strip. |
| Filters affecting all five | Education global filter, plus the four action filters including the persisted `R&D` state |
| Parameters affecting them | **None.** `Bin Size` does not touch the KPI strip. |
| Time period | Not applicable, no date field |
| Number formatting | **None specified.** Defaults apply. |

### KPI 1: Employee Count

| Attribute | Value |
|---|---|
| Exact displayed name | `Employee Count` (the Measure Names label for `[sum:Employee Count:qk]`) |
| Field behind it | `[Employee Count]`, source column 19 |
| Exact expression | `SUM([Employee Count])` |
| Aggregation | `SUM` |
| Numerator / Denominator | Not a ratio |
| Unit | Count of employees |
| Business meaning | Total headcount in the filtered population |
| Why useful | The denominator context for every other figure on the dashboard |
| What a user learns | The size of the population currently in scope after the Education filter and any cross-filter clicks |
| Dependency chain | Direct source column, no calculated field involved |

### KPI 2: Attrition Count

| Attribute | Value |
|---|---|
| Exact displayed name | `Attrition Count` |
| Field behind it | `[Calculation_231935388807032832]` |
| Exact formula | `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END`, aggregated as `SUM` |
| Aggregation | `SUM` |
| Numerator | Employees where `Attrition = 'Yes'` |
| Denominator | Not applicable |
| Unit | Count of employees |
| Business meaning | Number of leavers in the filtered population |
| Why useful | The headline attrition figure in absolute terms |
| Dependency chain | `[Attrition]` (source string) → `Attrition Count` |

### KPI 3: Attrition Rate

| Attribute | Value |
|---|---|
| Exact displayed name | `Attrition Rate` |
| Field behind it | `[Calculation_231935388807876609]` |
| Exact formula | `SUM([Calculation_231935388807032832])/SUM([Employee Count])` |
| Aggregation | `derivation='User'`, the field's own aggregate definition |
| **Numerator** | `SUM([Attrition Count])` |
| **Denominator** | `SUM([Employee Count])` |
| Unit | A proportion. **Not formatted as a percentage**, because no `number-format` is set anywhere in the workbook, so it will render as a decimal unless Tableau's default inference formats it otherwise. ✓ VERIFIED that no format is stored. |
| Business meaning | Share of the workforce that left |
| Why useful | Counts are not comparable across departments of different sizes. A rate is. |
| What a user learns | Whether attrition is high relative to headcount, and how that changes as they cross-filter by department, age band or education field |
| **Dependency chain** | `[Attrition]` → `Attrition Count` → `Attrition Rate`. This is the only two-level calculation dependency in either workbook. |

### KPI 4: Active Employees

| Attribute | Value |
|---|---|
| Exact displayed name | `Active Employees` |
| Field behind it | `[Calculation_231935388808294402]` |
| Exact formula | `SUM([Employee Count])- SUM([Calculation_231935388807032832])` |
| Aggregation | `derivation='User'` |
| Numerator / Denominator | Not a ratio, it is a difference |
| Unit | Count of employees |
| Business meaning | Headcount remaining after attrition |
| Why useful | Gives the retained population directly rather than making the reader subtract |
| **Dependency chain** | `[Attrition]` → `Attrition Count` → `Active Employees` |
| Note | `Employee Count` and `Active Employees` are shown side by side, so the pair implicitly communicates the attrition gap |

### KPI 5: Average Age

| Attribute | Value |
|---|---|
| Exact displayed name | the Measure Names label for `[avg:Age:qk]`, that is `AVG(Age)` |
| Field behind it | `[Age]`, source column 14 |
| Exact expression | `AVG([Age])` |
| Aggregation | `AVG` |
| Unit | Years |
| Business meaning | Mean age of the filtered population |
| Why useful | Frames the age band views below and flags whether a cross-filter has selected an unusually young or old subgroup |
| Dependency chain | Direct source column |
| Sort note | This is the one measure **not** listed in the `Measure Names` manual-sort dictionary, so it sorts after the other four |

### KPIs that are NOT present

There is **no target**, **no benchmark**, **no prior-period comparison**, **no variance** and **no trend indicator**. There is also no retention rate (the complement of attrition rate). ✓ VERIFIED by absence.

---

## 10. WORKSHEET / SHEET-BY-SHEET ANALYSIS

Seven worksheets exist and **all seven are placed on the dashboard**. None is orphaned.

Shared formatting:

| Property | Value |
|---|---|
| Worksheet title | Six of the seven use the dynamic token `<Sheet Name>` in `#f1ce63` (gold) `Tableau Semibold`, size 12 (size 11 and `fontalignment='1'` for `Attrition by Gender`). The `KPI` sheet has no title, and its dashboard zone sets `show-title='false'`. |
| Tooltip | All seven have a `<customized-tooltip>`. The house style is a bold black label, then the value in bold `#2f5597` (dark blue) at 14pt. |
| Number format | **None specified anywhere.** |

### 10.1 `KPI`

| Property | Value |
|---|---|
| Purpose | Present five headline HR figures in one strip |
| Visualization type | Text / BAN row driven by Measure Names and Measure Values |
| Data source | `HR data (HR Data)` |
| Columns shelf | `[:Measure Names]` |
| Rows shelf | empty |
| Marks type | `Automatic` (renders as Text) |
| Marks > Text | `[Multiple Values]` (Measure Values) |
| Marks > Color / Size / Detail | none |
| Custom label | `<[Multiple Values]>` |
| Custom tooltip | `<[:Measure Names]>:` then `<[Multiple Values]>` |
| Filters | Measure Names union of 5 members; Education global; 4 action filters including the `R&D` state |
| Pages | none |
| Parameters | none |
| Sets / Groups | the 4 hidden action groups |
| Calculated fields used | `Attrition Count`, `Attrition Rate`, `Active Employees` |
| Table calculations | none on this sheet |
| **Sorting** | `<manual-sort column='[:Measure Names]' direction='ASC'>` with an explicit dictionary of 4 members |
| Reference lines / trend lines / forecasting / analytics | none |
| Dual axis | no |
| **Measure Names / Measure Values** | **Yes, this worksheet is built on them.** |

**Plain English.** Measure Names is placed on Columns, which creates one column per selected measure, and Measure Values goes on Text, which prints the corresponding number in each column. A filter on Measure Names restricts the set to exactly five, and a manual sort pins their left-to-right order. The result is a single worksheet that behaves like five KPI tiles. This is a more economical construction than Dashboard 1's approach of building five separate worksheets, and it means all five tiles share one set of filters automatically.

### 10.2 `Attrition by Gender`

| Property | Value |
|---|---|
| Purpose | Compare absolute attrition between genders |
| Visualization type | **Lollipop chart**, built as a dual axis of Bar plus Circle |
| Rows shelf | `[none:Gender:nk]` (discrete) |
| Columns shelf | `([sum:Calculation_231935388807032832:qk] + [sum:Calculation_231935388807032832:qk])`, that is `SUM([Attrition Count])` placed twice |
| Marks type | Pane 0 `Automatic`, **Pane 1 `Bar`**, **Pane 2 `Circle`** (`x-index='1'` on pane 2) |
| Marks > Color | `[none:Gender:nk]` on all panes. No palette override is stored, so Tableau's default categorical palette applies. |
| Marks > Label | `SUM([Attrition Count])` in **bold white** (`fontcolor='#ffffff'`) on all three panes |
| Marks > Size / Detail | none |
| Custom tooltip | `Gender:` then `<Gender>`, `Attrition Count:` then `<SUM(Attrition Count)>` |
| Filters | Education global; Action(Department), Action(Department1)=R&D, Action(Age (bin)), Action(Education Field) |
| Sorting | none |
| Reference lines / analytics | none |
| **Dual axis** | **Yes.** Two identical `SUM([Attrition Count])` on Columns, second pane carries `x-index='1'` |
| **Synchronized axis** | Both axes carry the identical expression so they coincide. No separate synchronize flag is stored. △ INFERRED |
| Measure Names / Values | not used |
| Dashboard zone | id `6`, x=85127 y=10333 w=13671 h=15444, sitting to the right of the KPI strip |

**Plain English.** Gender goes on Rows, so there is one row per gender. Attrition Count goes on Columns twice, creating two overlapping horizontal axes. The first draws a bar from zero out to the value, the second draws a circle at the value. Overlaying them gives the lollipop form: a thin stem with a dot at the end. Both are coloured by gender and labelled in white bold with the count.

### 10.3 `Department wise Attrition`

| Property | Value |
|---|---|
| Purpose | Show how attrition is distributed across departments |
| Visualization type | **Pie chart** (single pane, so a pie rather than a donut) |
| Rows shelf | empty |
| Columns shelf | empty |
| Marks type | **`Pie`** |
| Marks > Color | `[none:Department:nk]`. No palette override stored, so Tableau's default categorical palette applies. |
| Marks > Angle (wedge-size) | `[sum:Calculation_231935388807032832:qk]`, that is `SUM([Attrition Count])` |
| Marks > Label | Two fields: `[pcto:sum:Calculation_231935388807032832:qk]` and `[sum:Calculation_231935388807032832:qk]` |
| Custom label | `<SUM(Attrition Count)>` then `(<% of Total Attrition Count>)`, both bold white in `Tableau Medium` |
| Custom tooltip | `Department:`, `% of Total Attrition Count along Table (Across):`, `Attrition Count:` |
| **Table calculation** | `PctTotal`, that is Percent of Total. The tooltip confirms the direction as `along Table (Across)`. |
| Filters | Education global; Action(Age (bin)); Action(Education Field). **Not** filtered by its own Department actions. |
| Sorting | none |
| Reference lines / analytics | none |
| Dual axis | no |
| **Role in interactivity** | Source worksheet of filter action `[Action1]`, which filters the rest of the dashboard on Department |
| Dashboard zone | id `10`, x=1266 y=27111 w=28544 h=40556. Its Department colour legend is a separate zone (id `11`) at x=1456 y=57556. |

**Plain English.** An empty viz with Department on Colour and Attrition Count on Angle. Each department becomes a wedge whose size is its share of total leavers, labelled with both the raw count and the percentage. Clicking a wedge fires `Action1` and filters the other six views to that department.

### 10.4 `No. of Employee by Age Group`

| Property | Value |
|---|---|
| Purpose | Show the age distribution of headcount, with user-controllable granularity |
| Visualization type | **Bar chart / histogram** |
| Columns shelf | `[none:Age (bin):ok]`, the parameter-driven bin, used as a discrete ordinal dimension |
| Rows shelf | `[sum:Employee Count:qk]`, that is `SUM([Employee Count])` |
| Marks type | `Automatic`. With a continuous measure on Rows and a discrete bin on Columns this resolves to Bar. △ INFERRED from Tableau's mark rules; the XML stores `Automatic`. |
| Marks > Color | `[sum:Employee Count:qk]` with `palette='purple_10_0'`, `type='interpolated'`, that is a **continuous purple sequential gradient** |
| Marks > Label | `[sum:Employee Count:qk]` at `fontsize='8'` |
| Marks > Size / Detail | none |
| Custom tooltip | `Age (bin):` then `<Age (bin)>`, `Employee Count:` then `<SUM(Employee Count)>` |
| Filters | Education global; Action(Department); Action(Department1)=R&D; Action(Education Field). **Not** filtered by its own Age (bin) action. |
| **Parameters** | **`[Age Parameter]`** via the bin. The slider control sits over this chart. |
| Row banding | `band-color='#00000000'` (fully transparent), `band-size='1'`, so banding is effectively switched off |
| Sorting | none |
| Reference lines / analytics | none |
| Dual axis | no |
| **Role in interactivity** | Source worksheet of filter action `[Action2]`, which filters on `Age (bin)` |
| Dashboard zone | id `12`, x=30633 y=27000 w=34367 h=40556, with its colour legend (id `14`) and the `Age Size` slider (id `13`) overlaid |

**Plain English.** Each bar is an age bucket, its height is the headcount in that bucket, and its fill is a purple shade that also encodes headcount, so taller bars are darker. The bucket width is not fixed: it is whatever the `Age Size` slider says, so the same chart can be read at 2-year or 10-year granularity. Clicking a bar filters the rest of the dashboard to that age band.

### 10.5 `Job Satisfaction Rating`

| Property | Value |
|---|---|
| Purpose | Cross-tabulate job role against satisfaction score |
| Visualization type | **Highlight table** (heatmap of squares with numbers) |
| Rows shelf | `[none:Job Role:nk]` |
| Columns shelf | `[none:Job Satisfaction:ok]` (the ordinal, role-converted field) |
| Marks type | **`Square`** |
| Marks > Color | `[sum:Employee Count:qk]` with `palette='blue_10_0'`, `type='interpolated'`, that is a **continuous blue sequential gradient** |
| Marks > Label | `[sum:Employee Count:qk]` |
| Marks > Size / Detail | none |
| Custom tooltip | `Job Role:`, `Job Satisfaction:`, `Employee Count:` |
| Filters | Education global; Action(Department); Action(Department1)=R&D; Action(Age (bin)); Action(Education Field) |
| Row banding | `band-color='#00000000'` on two rules, `band-size='1'`, so banding is off |
| Sorting | none |
| Reference lines / analytics | none |
| Dual axis | no |
| **Role in interactivity** | Source worksheet of filter action `[Action3]` |
| Dashboard zone | id `23`, x=65759 y=27222 w=33228 h=40444. **No colour legend is exposed for this chart on the dashboard.** |

**Plain English.** Job roles run down the rows and the satisfaction rating runs across the columns. Each cell is a square whose blue intensity and printed number both show how many employees are in that role-and-rating combination. Reading a row tells you how satisfaction is distributed within a role; reading a column tells you which roles cluster at a given rating.

**Observation (△ inferred):** the chart is titled `Job Satisfaction Rating` and is measured in `Employee Count`, not in `Attrition Count`. It is a headcount distribution view, not an attrition view, which makes it the one chart on the dashboard that answers a different question from the rest.

### 10.6 `Education Field wise Attrition`

| Property | Value |
|---|---|
| Purpose | Rank education fields by attrition volume |
| Visualization type | **Horizontal bar chart** |
| Rows shelf | `[none:Education Field:nk]` |
| Columns shelf | `[sum:Calculation_231935388807032832:qk]`, that is `SUM([Attrition Count])` |
| Marks type | `Automatic`, resolving to Bar. △ INFERRED |
| Marks > Color / Size / Label / Detail | **none.** This is the plainest chart on the dashboard. |
| Custom tooltip | `Education Field:` then `<Education Field>`, `Attrition Count:` then `<SUM(Attrition Count)>` |
| Filters | Education global; Action(Department); Action(Department1)=R&D; Action(Age (bin)). **Not** filtered by its own Education Field action. |
| Sorting | **none defined.** Bars will appear in the data source's default order, not sorted by value. ✓ VERIFIED by absence of any `<sort>` or `<manual-sort>` on this sheet. |
| Reference lines / analytics | none |
| Dual axis | no |
| **Role in interactivity** | Source worksheet of filter action `[Action5]` |
| Dashboard zone | id `24`, x=1139 y=68778 w=27278 h=29111 |

**Plain English.** One horizontal bar per education field, length equal to the number of leavers from that field. No colour, no label, tooltip only. Clicking a bar filters the dashboard to that education field.

### 10.7 `Attrition Rate by Gender for Different Age Group`

| Property | Value |
|---|---|
| Purpose | Break attrition down by gender within each age band |
| Visualization type | **A row of donut charts**, one per age band, built as a dual-axis pie |
| Columns shelf | `[none:CF_age band:nk]` |
| Rows shelf | `([usr:Calculation_1302666200262176769:qk] + [usr:Calculation_1302666200262176769:qk])`, that is `min(1)` placed twice |
| Marks type | `Pie` on all three panes, pane 2 carries `y-index='1'` |
| Marks > Color | Pane 1: `[none:Gender:nk]`. Pane 2: no colour field. |
| Marks > Angle (wedge-size) | Pane 1: `[sum:Calculation_231935388807032832:qk]`, that is `SUM([Attrition Count])` |
| Marks > Label | Pane 1: `[pcto:sum:...]` and `[sum:...]`. Pane 2: `[sum:...]` at `fontsize='15'`. |
| Custom label (pane 1) | `<SUM(Attrition Count)> (<% of Total Attrition Count>)` |
| Custom label (pane 2) | `<SUM(Attrition Count)>` at 15pt, that is the **total count printed in the centre of the donut hole** |
| Custom tooltip (pane 1) | `CF_age band:`, `Gender:`, `% of Total Attrition Count along Table (Across):`, `Attrition Count:` |
| Custom tooltip (pane 2) | `CF_age band:`, `Attrition Count:` |
| **Table calculation** | `PctTotal`, direction `along Table (Across)` per the tooltip |
| Filters | Education global; all four action filters including `R&D` |
| **Sorting** | `<manual-sort column='[none:CF_age band:nk]' direction='ASC'>` with an explicit dictionary: `"Under 25"`, `"25 - 34"`, `"35 - 44"`, `"45 - 54"`, `"Over 55"`. This forces logical age order instead of alphabetical. |
| Column header formatting | `CF_age band` header text `#ffffff` in `Tableau Semibold`; row axes hidden (`display` set to `false` for both classes) |
| Reference lines / analytics | none |
| **Dual axis** | **Yes**, via two `min(1)` on Rows |
| **Role in interactivity** | Source worksheet of filter action `[Action4]` |
| Dashboard zone | id `25`, x=29177 y=68889 w=69494 h=28333, the widest chart on the dashboard. Its Gender legend is zone `26`. |

**Plain English.** Age band goes on Columns, so there is one cell per band, ordered Under 25 through Over 55 by an explicit manual sort. In each cell, `min(1)` on Rows twice gives a dual axis. The first pie is coloured by gender with wedge angle equal to that gender's leaver count, labelled with count and percent of total across the row. The second pie is drawn on the secondary axis carrying only a large 15pt label, which places the age band's total attrition count in the middle of the donut. The row axes are hidden so only the donuts and the age band headers show.

**A precise and important naming note.** The worksheet is called `Attrition Rate by Gender for Different Age Group`, but the measure actually on the Angle shelf is `SUM([Attrition Count])`, **not** `Attrition Rate`. The `Attrition Rate` calculated field appears **only** on the `KPI` worksheet. The percentages shown in the labels are `% of Total Attrition Count` computed by a table calculation, which is a share of leavers across the row, not an attrition rate against headcount. ✓ DIRECTLY VERIFIED from the shelves and the tooltip text. This is a genuine discrepancy between the chart title and the chart content, and it is exactly the kind of thing a sharp interviewer will probe. It is better to name it yourself than to be caught by it.

---

## 11. VISUALIZATION-BY-VISUALIZATION BREAKDOWN

| # | Visual | What it shows | Fields driving it | Dimensions compared | Measure analysed | Aggregation | Filters affecting it | Calculations affecting it | Business question answered | Why appropriate |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KPI strip (5 tiles in one sheet) | Headcount, leavers, attrition rate, active headcount, mean age | `Employee Count`, `Attrition Count`, `Attrition Rate`, `Active Employees`, `Age`, Measure Names/Values | none | five measures | `SUM`, `SUM`, User, User, `AVG` | Education global + 4 action filters | `Attrition Count` → `Attrition Rate` and `Active Employees` | "What is the current state of the workforce and its attrition?" | Measure Names/Values gives five synchronised figures in one sheet with one filter scope |
| 2 | Attrition by Gender (lollipop) | Leaver counts for each gender | `Gender`, `Attrition Count` | Gender | attrition count | `SUM` | Education global + 4 action filters | `Attrition Count` | "Do men and women leave at different volumes?" | A lollipop reads cleanly with only two categories in a narrow zone, and carries less ink than a full bar |
| 3 | Department wise Attrition (pie) | Share of total leavers by department | `Department`, `Attrition Count` | Department | attrition count and share | `SUM` + `PctTotal` | Education global, Action(Age (bin)), Action(Education Field) | `Attrition Count`, percent of total | "Which departments account for most of our attrition?" | A pie is defensible here because the question is explicitly about share of a whole, and the labels carry the raw counts too |
| 4 | No. of Employee by Age Group (bar) | Headcount by age bucket at user-chosen granularity | `Age (bin)`, `Employee Count`, `[Age Parameter]` | Age buckets | headcount | `SUM` | Education global, Action(Department), Action(Department1)=R&D, Action(Education Field) | `Age (bin)` driven by `Bin Size` | "What is our age profile, and does it change shape at a different band width?" | A histogram is the standard form; making the bin width a parameter lets the viewer test whether a pattern is real or an artefact of bucketing |
| 5 | Job Satisfaction Rating (highlight table) | Headcount for every job role and satisfaction score combination | `Job Role`, `Job Satisfaction`, `Employee Count` | Job Role x Job Satisfaction | headcount | `SUM` | Education global + 4 action filters | none | "Which roles cluster at low satisfaction?" | A highlight table handles a two-dimensional categorical cross-tab better than any chart, and printing the value keeps it readable as a table |
| 6 | Education Field wise Attrition (bar) | Leaver counts by education field | `Education Field`, `Attrition Count` | Education Field | attrition count | `SUM` | Education global, Action(Department), Action(Department1)=R&D, Action(Age (bin)) | `Attrition Count` | "Do leavers come disproportionately from particular academic backgrounds?" | Horizontal bars handle long category labels well |
| 7 | Attrition Rate by Gender for Different Age Group (donut row) | Gender split of leavers within each age band, plus the band total | `CF age band`, `Gender`, `Attrition Count` | Age band x Gender | attrition count and share | `SUM` + `PctTotal` | Education global + 4 action filters | `Attrition Count`, percent of total, `min(1)` axis | "Within each age band, is attrition concentrated in one gender?" | Small multiples of donuts let you compare the same two-part split across five bands side by side; the hole carries the band total so the reader gets absolute and relative at once |

---

## 12. DASHBOARD LAYOUT

| Property | Value |
|---|---|
| Dashboard name | `HR Dashboard ` (trailing space) |
| Size | 1580 x 900 px, `sizing-mode='fixed'` |
| Layout style | **Floating over a full-canvas background image.** Only two objects sit inside the tiled container; the other twelve are floating siblings positioned absolutely. |
| Background | A PNG image object fills the canvas: `Image/HR background.pptx.png`, 410,683 bytes, zone id `3`, `type-v2='bitmap'`, at x=506 y=889 w=98988 h=98222. **The filename `HR background.pptx.png` indicates it was exported from a PowerPoint file.** △ INFERRED from the filename; ✓ VERIFIED that the file and reference exist. |
| Container structure | `layout-basic` (id 4, `margin='8'`) containing only the bitmap zone (id 3, `margin='4'`). All remaining zones are siblings at the top `<zones>` level, that is, floating. |
| Device layouts | One auto-generated **Phone** layout, `sizing-mode='vscroll'`, height 2400 px, `auto-generated='true'`. No Tablet layout. |

### Object census

| Object type | Count | Zone ids |
|---|---|---|
| Worksheets | 7 | 5 (`KPI`), 6 (`Attrition by Gender`), 10 (`Department wise Attrition`), 12 (`No. of Employee by Age Group`), 23 (`Job Satisfaction Rating`), 24 (`Education Field wise Attrition`), 25 (`Attrition Rate by Gender...`) |
| **Image object** | **1** | 3, `Image/HR background.pptx.png` |
| **Text object** | **1** | 7, containing the text `HR ANALYTICS DASHBOARD` |
| Colour legends | 3 | 11 (`Department`, from `Department wise Attrition`), 14 (`SUM(Employee Count)`, from `No. of Employee by Age Group`), 26 (`Gender`, from `Attrition Rate by Gender...`) |
| Filter control | 1 | 29, `mode='dropdown'`, `param='[none:Education:nk]'`, sourced from `Department wise Attrition` |
| **Parameter control** | **1** | 13, `mode='slider'`, `param='[Parameters].[Age Parameter]'`, titled `Age Size` |
| Blank objects | 0 | |
| Navigation buttons | 0 | |
| Extension / web page objects | 0 | |

**Note:** no colour legend is exposed for `Job Satisfaction Rating`, even though it has a continuous blue colour encoding. ✓ VERIFIED by absence.

### Reconstructed hierarchy

```
HR Dashboard    (1580 x 900, FIXED sizing)
│
├── layout-basic  [id 4, margin 8]
│   └── Image object  [id 3]  "Image/HR background.pptx.png"
│          full canvas: x=506 y=889 w=98988 h=98222
│
├── HEADER BAND  (y ~ 2000 to 9500)
│   ├── Text object  [id 7]   "HR ANALYTICS DASHBOARD"
│   │        x=1203  y=2111   w=65063  h=7222
│   └── Filter: Education (dropdown)  [id 29]
│            x=61709 y=2333   w=14620  h=6889
│
├── KPI BAND  (y ~ 10300 to 25800)
│   ├── KPI worksheet  [id 5]  show-title=false
│   │        x=1139  y=10667  w=83924  h=15111
│   └── Attrition by Gender  [id 6]
│            x=85127 y=10333  w=13671  h=15444
│
├── MIDDLE BAND  (y ~ 27000 to 67700)
│   ├── Department wise Attrition  [id 10]
│   │        x=1266  y=27111  w=28544  h=40556
│   │   └── Legend: Department  [id 11]   x=1456  y=57556
│   ├── No. of Employee by Age Group  [id 12]
│   │        x=30633 y=27000  w=34367  h=40556
│   │   ├── Legend: SUM(Employee Count)  [id 14]  x=30886 y=31000
│   │   └── Parameter slider "Age Size"  [id 13]  x=55190 y=28000
│   └── Job Satisfaction Rating  [id 23]
│            x=65759 y=27222  w=33228  h=40444
│            (no legend exposed)
│
└── BOTTOM BAND  (y ~ 68800 to 97900)
    ├── Education Field wise Attrition  [id 24]
    │        x=1139  y=68778  w=27278  h=29111
    └── Attrition Rate by Gender for Different Age Group  [id 25]
             x=29177 y=68889  w=69494  h=28333
        └── Legend: Gender  [id 26]   x=70316 y=69889  w=24114 h=3444
```

Zone `x`, `y`, `w`, `h` are in hundred-thousandths of the dashboard dimension. Multiply by 1580/100000 horizontally and 900/100000 vertically for pixels. For example the KPI zone at `x=1139 w=83924` is about 18 px from the left and about 1326 px wide.

**Headers and footers:** the header band is a genuine text object plus a filter control, unlike Dashboard 1 where the header was implied by worksheet placement. There is no footer object. ✓ VERIFIED.

---

## 13. DASHBOARD ACTIONS / INTERACTIVITY

**Six filter actions.** Every worksheet except `KPI` is the source of exactly one.

| Action | Caption | Type | Source worksheet | Target | Trigger | Fields |
|---|---|---|---|---|---|---|
| `[Action1]` | `Filter 1 (generated)` | **Filter** (`command='tsc:tsl-filter'`) | `Department wise Attrition` | `HR Dashboard ` (whole dashboard) | `on-select`, `auto-clear='true'` | `special-fields='all'` |
| `[Action2]` | `Filter 2 (generated)` | Filter | `No. of Employee by Age Group` | `HR Dashboard ` | `on-select`, `auto-clear='true'` | `special-fields='all'` |
| `[Action3]` | `Filter 3 (generated)` | Filter | `Job Satisfaction Rating` | `HR Dashboard ` | `on-select`, `auto-clear='true'` | `special-fields='all'` |
| `[Action4]` | `Filter 4 (generated)` | Filter | `Attrition Rate by Gender for Different Age Group` | `HR Dashboard ` | `on-select`, `auto-clear='true'` | `special-fields='all'` |
| `[Action5]` | `Filter 5 (generated)` | Filter | `Education Field wise Attrition` | `HR Dashboard ` | `on-select`, `auto-clear='true'` | `special-fields='all'` |
| `[Action6]` | `Filter 6 (generated)` | Filter | `Attrition by Gender` | `HR Dashboard ` | `on-select`, `auto-clear='true'` | `special-fields='all'` |

✓ DIRECTLY VERIFIED for every cell.

### What `special-fields='all'` means

The actions pass **all fields** in the source view rather than a named subset. So clicking a wedge on `Department wise Attrition` passes `Department` to every target view; clicking a square on `Job Satisfaction Rating` passes both `Job Role` and `Job Satisfaction`. This is the "Use all fields" option in the Tableau action dialog, and it is why the auto-generated hidden groups (`Action (Department)`, `Action (Age (bin))`, `Action (Education Field)`) exist.

### Result and effect

Every chart is a cross-filter surface. Selecting a mark anywhere filters the other six views, including the KPI strip, and deselecting restores the full view because `auto-clear='true'`. Combined with the global Education dropdown, a user can compose a query like "R&D department, science education field, 35 to 44 age band" purely by clicking, and the KPI strip recomputes headcount, leaver count, attrition rate, active headcount and mean age for that slice.

### Interactivity types NOT present

| Interactivity | Present? |
|---|---|
| **Highlight actions** | **No.** Contrast with Dashboard 1, which has exactly one highlight action and no filter actions. |
| URL actions | **No** |
| **Parameter actions** | **No.** The parameter is driven by its slider only, not by clicking a mark. |
| Set actions | **No** (no sets exist) |
| Navigation / Go to Sheet actions | **No** |
| Sheet swapping | **No** |
| Dashboard-to-dashboard navigation | **No** (only one dashboard) |
| Drill-down hierarchies | **No** (no hierarchies defined) |
| Viz-in-tooltip | **No** |

### Interactive controls available to the end user

1. Education dropdown filter, scoped to all seven worksheets.
2. `Age Size` parameter slider (2 to 10, step 1), affecting `No. of Employee by Age Group` and, indirectly, what `[Action2]` filters to.
3. Six click-to-filter actions, one from every chart.
4. Three colour legends, which in Tableau also support highlight-on-click.

---

## 14. TOOLTIPS

**Every one of the seven worksheets has a custom tooltip.** That is the sharpest contrast with Dashboard 1, which has none. ✓ DIRECTLY VERIFIED.

House style, consistent across all of them: the field label in **bold `#000000`**, then the value in **bold `#2f5597`** (dark blue) at **14pt**, with `Æ` separators (which is how a line break renders in the raw XML text runs).

| Worksheet | Fields in the tooltip | Calculated values? | Custom descriptions? | Viz-in-tooltip? | Conditional? |
|---|---|---|---|---|---|
| `KPI` | `<Measure Names>:` then `<Multiple Values>` | Yes, `Attrition Rate` and `Active Employees` flow through Measure Values | Yes, the label is hand-typed | No | No |
| `Attrition by Gender` | `Gender:` `<Gender>`; `Attrition Count:` `<SUM(Attrition Count)>` | Yes, `Attrition Count` | Yes | No | No |
| `Department wise Attrition` | `Department:` `<Department>`; `% of Total Attrition Count along Table (Across):` `<pcto SUM(Attrition Count)>`; `Attrition Count:` `<SUM(Attrition Count)>` | Yes, plus a table calculation | Yes | No | No |
| `No. of Employee by Age Group` | `Age (bin):` `<Age (bin)>`; `Employee Count:` `<SUM(Employee Count)>` | Yes, the parameter-driven bin | Yes | No | No |
| `Job Satisfaction Rating` | `Job Role:` `<Job Role>`; `Job Satisfaction:` `<Job Satisfaction>`; `Employee Count:` `<SUM(Employee Count)>` | No | Yes | No | No |
| `Education Field wise Attrition` | `Education Field:` `<Education Field>`; `Attrition Count:` `<SUM(Attrition Count)>` | Yes, `Attrition Count` | Yes | No | No |
| `Attrition Rate by Gender for Different Age Group` (pane 1) | `CF_age band:` `<CF_age band>`; `Gender:` `<Gender>`; `% of Total Attrition Count along Table (Across):` `<pcto>`; `Attrition Count:` `<SUM(Attrition Count)>` | Yes, plus a table calculation | Yes | No | No |
| `Attrition Rate by Gender for Different Age Group` (pane 2, the donut hole) | `CF_age band:` `<CF_age band>`; `Attrition Count:` `<SUM(Attrition Count)>` | Yes | Yes | No | No |

**Why this matters (△ inferred).** The tooltips are where the `Name1` caption artefacts get corrected. The field is captioned `Department1` in the data pane, but the tooltip reads `Department:`. The same holds for `Gender`, `Job Role`, `Education Field` and `Job Satisfaction`. Someone hand-wrote clean labels into every tooltip.

### Custom mark labels

| Worksheet | Custom label content |
|---|---|
| `Attrition by Gender` | `<SUM(Attrition Count)>` in bold `#ffffff`, on all three panes |
| `Department wise Attrition` | `<SUM(Attrition Count)>` then `(<% of Total Attrition Count>)`, bold `#ffffff` in `Tableau Medium` |
| `No. of Employee by Age Group` | `<SUM(Employee Count)>` at `fontsize='8'` |
| `KPI` | `<Multiple Values>` |
| `Attrition Rate by Gender...` pane 1 | `<SUM(Attrition Count)> (<% of Total Attrition Count>)` |
| `Attrition Rate by Gender...` pane 2 | `<SUM(Attrition Count)>` at `fontsize='15'`, the number placed in the donut hole |
| `Job Satisfaction Rating` | none (the default label from the Text shelf) |
| `Education Field wise Attrition` | none |

### Worksheet titles

Six worksheets use the dynamic `<Sheet Name>` token so the title always matches the worksheet name:

| Worksheet | Title definition | Font |
|---|---|---|
| `Attrition Rate by Gender for Different Age Group` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 12 |
| `Attrition by Gender` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 11, centred |
| `Department wise Attrition` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 12 |
| `Education Field wise Attrition` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 12 |
| `Job Satisfaction Rating` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 12 |
| `No. of Employee by Age Group` | `<Sheet Name>` | `#f1ce63`, `Tableau Semibold`, 12 |
| `KPI` | no custom title; hidden on the dashboard | n/a |

Using `<Sheet Name>` rather than typed text means renaming a worksheet automatically renames its dashboard title. That is a small but real maintainability choice. △ INFERRED as intent; ✓ VERIFIED as fact.

---

## 15. BUSINESS LOGIC

**What business problem was identified (△ INFERRED).** Attrition is expensive and uneven, and an HR team needs to know where it concentrates before it can act. The dashboard is built to answer "where", not "why" or "who next": it is a descriptive, cross-filterable profile, not a predictive model and not a driver analysis.

**What data was needed (✓).** One employee-level file at one row per employee, 39 columns, containing an attrition flag, headcount, department, education field, education level, gender, job role, job satisfaction score, age, and a pre-computed age band. Twenty-four of the thirty-nine available columns were not used.

**How the data was transformed (✓).**
1. `HR_data.csv` was read with a `textscan` connection and extracted whole to Hyper.
2. `Job Satisfaction` and `Employee Number` were converted from measures to ordinal dimensions.
3. `Attrition Count` was calculated as `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END`, converting a string flag into a summable indicator.
4. `Attrition Rate` was calculated as `SUM([Attrition Count])/SUM([Employee Count])`.
5. `Active Employees` was calculated as `SUM([Employee Count])- SUM([Attrition Count])`.
6. A `Bin Size` parameter (real, 2.0 to 10.0, step 1.0, default 3.0) was created and bound to an `Age (bin)` binning calculation as its `size-parameter`.
7. A global Education filter was set at data source scope via a `<shared-view>`.
8. `CF_age band`, `CF_attrition label` and `CF_current Employee` arrived already derived from upstream and were consumed as-is.

**What KPIs were selected (✓).** `Employee Count`, `Attrition Count`, `Attrition Rate`, `Active Employees`, `AVG(Age)`. Four counts or differences and one true ratio.

**What dimensions were analysed (✓).** `Department`, `Education Field`, `Education`, `Gender`, `Job Role`, `Job Satisfaction`, `CF age band`, and `Age (bin)`.

**What comparisons were made (✓).**
- Attrition volume between genders (lollipop).
- Attrition share across departments (pie with percent of total).
- Headcount across age buckets at user-chosen granularity (parameterised histogram).
- Headcount across the job role by satisfaction matrix (highlight table).
- Attrition volume across education fields (bar).
- Gender split of attrition within each of five age bands, with the band total in the hole (donut small multiples with percent of total and a manual age-band sort).

**What trends were intended to be identified (△ INFERRED).** The design points at concentration rather than trend. **There is no time series and there cannot be one, because the dataset has no date field.** The tenure columns (`Years At Company`, `Years Since Last Promotion`, and so on) could have supported a tenure-based view but are not used. Be precise about this in an interview: this dashboard shows *where* attrition sits, not *how it is moving*.

**What decisions a business user could make (△ INFERRED).** Target retention effort at the department, age band, education field or job role with the worst concentration; decide whether a gender-specific retention issue exists in a particular age band; identify job roles whose satisfaction distribution skews low and pair that with their attrition contribution; and scope a deeper analysis by using the cross-filters to isolate a cohort before requesting record-level data.

---

## 16. KEY INSIGHTS THE DASHBOARD IS DESIGNED TO ENABLE

No actual data values were read, so no findings are claimed.

### A. Insights explicitly encoded by the dashboard

1. Headcount, leaver count, attrition rate, active headcount and mean age are computed for whatever slice is currently filtered, and recompute on every cross-filter click.
2. Attrition is decomposed by department as a share of total leavers, with both the count and the percent of total on the label.
3. Attrition is decomposed by education field as an absolute count.
4. Attrition is decomposed by gender as an absolute count.
5. Attrition is decomposed by gender **within** each of five age bands, with both the count, the percent of total across the band row, and the band total in the donut hole.
6. Headcount is decomposed by age bucket at a granularity the user chooses between 2 and 10 years.
7. Headcount is cross-tabulated across job role and job satisfaction score, encoded by both colour intensity and printed value.
8. Selecting any mark on any chart re-filters the entire dashboard including the KPI strip.

### B. Questions the dashboard enables users to answer

- "What is our attrition rate, and how many people does that represent?"
- "Which department contributes the largest share of our leavers?"
- "Within the 25 to 34 age band, is attrition skewed towards one gender?"
- "If I restrict to a single education level, does the department picture change?"
- "Which job roles have the largest concentration of employees at the lowest satisfaction rating?"
- "Is our age distribution bimodal, or does that disappear when I widen the bins from 3 years to 8?"
- "For the R&D department specifically, what are the headcount, leaver count and attrition rate?" (by clicking the R&D wedge)
- "Does the age profile of the population change when I filter to a particular education field?"

### C. Actual findings verifiable from the available data

**None can be stated.** All values live in the binary `.hyper` extracts and no Hyper reader is available here. No headcount, no attrition rate, no departmental ranking and no satisfaction distribution can be verified from the files supplied. ✗ NOT AVAILABLE.

One thing that **is** verifiable and worth noting as a caveat rather than a finding: the saved workbook state carries a `Department = "R&D"` action filter on six of the seven worksheets (section 8.2). Any number read off the dashboard in that state is an R&D number, not an organisation-wide number.

---

## 17. TECHNICAL IMPLEMENTATION SUMMARY

```
DATA SOURCE
  HR_data.csv, 39 columns, one row per employee
  /Users/atharvadevne/Desktop/HR-Analytics-Dashboard-Using-Tableau-main
  (3 further data sources point at variants of the same file and are UNUSED)
  3 columns arrive pre-derived from upstream: CF_age band,
  CF_attrition label, CF_current Employee
        |
        v
DATA CONNECTION
  Tableau textscan (flat file) connector
  (an excel-direct connection is also declared but not bound to the relation)
  wrapped in federated.0f0h03p1it3gvo176rhln1y1tx4v
  Extract enabled, count = -1 (all records), no extract filter
  4 .hyper files ship in the archive, 3 of them dead weight
        |
        v
DATA MODEL
  Single table. No joins, no relationships, no unions, no blends.
        |
        v
DATA CLEANING (all inside Tableau except the CF_ columns)
  10 field captions (6 are Name1 collision artefacts, not deliberate renames)
  Job Satisfaction and Employee Number converted measure -> ordinal dimension
  Attrition Count converts a 'Yes'/'No' string into a summable 0/1 flag
  Age binned with a PARAMETER-DRIVEN bin width
  No aliases, no groups, no sets, no hierarchies
        |
        v
CALCULATED FIELDS  (6 total, no LODs)
  Attrition Count    = IF [Attrition] = 'Yes' THEN 1 ELSE 0 END
  Attrition Rate     = SUM([Attrition Count]) / SUM([Employee Count])
  Active Employees   = SUM([Employee Count]) - SUM([Attrition Count])
  Age (bin)          = bin of [Age], size-parameter = [Age Parameter]
  Number of Records  = 1   (auto-generated, unused)
  min(1)             = axis placeholder for the dual-axis donut
  + built-in table calculation: Percent of Total, along Table (Across)
        |
        v
PARAMETER  (1)
  [Age Parameter] "Bin Size", real, range 2.0 to 10.0, step 1.0, current 3.0
  Surfaced as a slider titled "Age Size"
        |
        v
KPIs  (5, all in ONE worksheet via Measure Names / Measure Values)
  SUM(Employee Count)      -> Employee Count
  SUM(Attrition Count)     -> Attrition Count
  Attrition Rate           -> Attrition Rate
  Active Employees         -> Active Employees
  AVG(Age)                 -> Average Age
        |
        v
WORKSHEETS  (7)
  1  Measure Names/Values KPI strip (manual-sorted)
  1  dual-axis lollipop            (Bar + Circle)
  1  pie with percent of total
  1  parameterised bar histogram   (purple sequential colour)
  1  highlight table               (Square marks, blue sequential colour)
  1  horizontal bar
  1  dual-axis donut small multiples (manual-sorted age bands,
                                      total printed in the hole)
        |
        v
DASHBOARD  (1)
  "HR Dashboard " (trailing space), 1580 x 900 FIXED
  Floating layout over a full-canvas PNG exported from PowerPoint
  7 worksheets + 1 text title + 3 colour legends
  + 1 filter dropdown + 1 parameter slider
  Gold (#f1ce63) title system, dark-blue (#2f5597) tooltip values
  Auto-generated Phone layout (vscroll, 2400 px)
        |
        v
FILTERS / ACTIONS
  Education filter at DATA SOURCE scope (shared-view) -> all 7 worksheets
  6 filter actions, one from every chart, on-select, auto-clear,
    special-fields = all, targeting the whole dashboard
  4 auto-generated hidden action groups
  A persisted Department = "R&D" selection saved into 6 worksheets
        |
        v
FINAL USER EXPERIENCE
  A single fixed-size branded screen. Pick an education level from the
  dropdown, drag the age bin slider to change histogram granularity, then
  click any wedge, bar, square or donut segment to re-filter the whole
  dashboard including the five KPI figures. Every mark carries a hand-written
  tooltip. Deselecting restores the full view.
```

---

## 18. INTERVIEW EXPLANATION

Use this as a spoken narrative. Everything in it is supported by the workbook.

> "This is an HR attrition dashboard I built for myself, to practise metric design and interaction design rather than just chart building. The dataset is a public employee-level set from Kaggle, 39 columns, one row per employee, with an attrition flag, department, education field and level, gender, job role, a job satisfaction score, age and a pre-computed age band.
>
> The problem I set out to solve was that HR teams usually know their overall attrition number and almost nothing about where it concentrates. So I built the dashboard as a cross-filtering surface rather than a static report. Every chart on it is clickable, and clicking anything re-filters everything else including the headline numbers.
>
> The data came in as a single CSV read through Tableau's flat file connector and extracted whole to Hyper. One table, no joins. I will be straight about something visible in the file: there are four data sources in that workbook pointing at variants of the same file, and only one is actually wired up. That is leftover from trying different import formats early on, and if I were tidying it I would delete the three dead ones, because each one carries its own extract and bloats the packaged file.
>
> The calculation layer is where the real design decisions are. The attrition column arrives as the text Yes or No, which you cannot aggregate, so the first thing I built was Attrition Count: IF Attrition equals Yes THEN 1 ELSE 0 END. Everything else on the dashboard hangs off that. Attrition Rate is SUM of Attrition Count divided by SUM of Employee Count. I wrote it as an aggregate over an aggregate on purpose, because that way it recalculates correctly at whatever level of detail the view happens to be at. Put it on a KPI tile with no dimensions and it is the organisation-wide rate; click into a department and the same field gives you that department's rate without me having to write a second calculation. Active Employees is SUM of Employee Count minus SUM of Attrition Count, so the strip shows total, leavers, rate and remaining side by side.
>
> The piece I am most pleased with is the parameterised bin. Instead of hard-coding an age bucket width, I created a Bin Size parameter, a float between 2 and 10 stepping by 1, defaulting to 3, and bound it to the bin's size-parameter property. Then I put it on the dashboard as a slider. That means the viewer can decide whether they want a fine-grained age profile or decade bands, and they can check whether a pattern they think they see survives a change of bucketing. It also has a second effect I had to think through: that histogram is a filter source, so changing the bin width changes the width of the band a click filters to.
>
> For the KPI strip I did not build five separate worksheets. I used Measure Names on Columns and Measure Values on Text in a single sheet, filtered Measure Names down to the five I wanted, and pinned their order with a manual sort. One sheet, five tiles, one filter scope, much less to maintain.
>
> The global Education filter is set at data source scope using apply-to-all-worksheets-using-this-data-source, rather than picking sheets by hand. That guarantees the KPI strip responds to it, which matters, because a filter that moves the charts but not the headline numbers is worse than no filter at all.
>
> Chart choices: a lollipop for gender attrition, which is a dual axis of a bar and a circle on the same measure, because with two categories in a narrow panel it reads cleaner than a full bar. A pie for department share, which I would normally avoid, but the question there is genuinely about share of a whole and I put the raw counts on the labels too. A highlight table of job role against satisfaction score with Square marks, because a two-way categorical cross-tab is what a highlight table is for. A parameterised histogram for age. Plain horizontal bars for education field. And the bottom chart is a row of donuts, one per age band, gender-split, with the band's total attrition count printed in the middle of each hole using the second axis of the dual-axis pie. I forced the age bands into logical order with a manual sort dictionary, Under 25 through Over 55, because alphabetical order would have put Over 55 in the middle.
>
> Every worksheet has a hand-written tooltip in a consistent style, bold black label and dark blue value. The worksheet titles use the Sheet Name token rather than typed text, so renaming a sheet renames its dashboard title automatically.
>
> Layout is 1580 by 900 fixed, floating objects over a full-canvas background image I exported from PowerPoint, with a gold title system.
>
> If I am being properly honest about what I would fix, there are four things I can see in my own file. First, the bottom chart is titled Attrition Rate by Gender for Different Age Group, but the measure on it is actually Attrition Count with a percent-of-total table calculation, not the Attrition Rate field. I would either rename the sheet or swap in the rate. Second, I set no number formatting anywhere, so Attrition Rate renders as a decimal rather than a percentage. Third, six of my field captions ended up as Department1, Gender1 and so on, which are Tableau collision artefacts from replacing a data source, not deliberate names. My tooltips paper over that but the legends do not. Fourth, I saved the workbook with an R&D mark still selected, so the saved state carries a department filter on six of seven sheets.
>
> Skills-wise this demonstrates parameter-driven calculations, aggregate calculations and a real dependency chain, Measure Names and Measure Values KPI construction, dual-axis chart building for both lollipops and donuts, table calculations, data source scoped filtering, six-way action-based cross-filtering, manual sort dictionaries, sequential colour encoding, custom tooltip authoring and floating dashboard layout over a designed background."

---

## 19. RESUME-READY PROJECT DESCRIPTION

Only verified facts. No invented percentages, record counts or outcomes.

**HR Analytics Attrition Dashboard (Tableau)**

- Built a 7-worksheet Tableau attrition dashboard over a 39-column employee-level dataset, published to Tableau Public on a fixed 1580x900 canvas with a floating layout over a custom-designed background.

- Authored the metric layer as a three-level calculation chain: converted a `Yes`/`No` text attrition flag into a summable indicator with `IF [Attrition] = 'Yes' THEN 1 ELSE 0 END`, then derived `Attrition Rate` as `SUM([Attrition Count])/SUM([Employee Count])` and `Active Employees` as `SUM([Employee Count]) - SUM([Attrition Count])` as aggregate calculations so both recompute correctly at any level of detail.

- Implemented a parameter-driven age histogram by binding a `Bin Size` range parameter (2 to 10, step 1) to the `size-parameter` of an `Age (bin)` calculation and exposing it as a dashboard slider, letting users change bucket granularity at view time.

- Condensed five KPIs into a single worksheet using Measure Names and Measure Values with a manual-sort dictionary, and scoped the Education filter at data source level so the KPI strip and all six charts respond to one control.

- Delivered full cross-filtering with six `on-select` filter actions (one per chart, passing all fields, auto-clear) alongside dual-axis chart construction for a Bar-plus-Circle lollipop and a row of donut small multiples, Percent of Total table calculations, sequential colour encodings, and hand-authored tooltips on all seven worksheets.
