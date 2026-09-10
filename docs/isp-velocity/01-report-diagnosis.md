# Why the velocity reports are empty

The question asked was "what does it take to get some of the reports on the list
populated with actual data?". This document answers it for the two ISP velocity
reports, and sets up a way to answer it for the whole list at once.

Sanitised for a public repository: no connection strings, internal hostnames,
catalog names, colleague surnames or email addresses.

---

## 1. What the artefacts already tell us

Two things were shared: screenshots of the workspace contents, and a row from a
report inventory spreadsheet.

**The workspace screenshots show four items, not four reports.** Each name
appears twice with a different icon. One icon is a report, the other is a
semantic model. So there are two reports, `ISP Velocity Changes` and
`ISP On Hand Velocity - Price`, each with its own model underneath it. That
matters because the data problem lives in the model, and anything done to the
report layer will change nothing.

**The inventory row is the real finding.** Against `ISP Velocity Changes` it
lists three tables:

| Table | Source Type | Source Location | Filename |
|---|---|---|---|
| `Query1-3e5a23fb-...` | Other | *(blank)* | *(blank)* |
| `Query2-08506136-...` | Other | *(blank)* | *(blank)* |
| `Query3` | Other | *(blank)* | *(blank)* |

Three things in that table are worth reading carefully.

**The names are still `Query1`, `Query2` and `Query3`.** Those are the default
names Power Query hands out. Nobody renamed them. That is what a fast, one off
build looks like, and it is not what a maintained data source looks like.

**The GUID suffixes mean the inventory was machine generated.** A person typing
a spreadsheet does not write `Query1-3e5a23fb-debe-4ceb-8db6-81755916db3b`. That
string is the model's internal table identifier, so this row was produced by a
scanner reading the model. Which means the blank Source Location is not somebody
failing to fill in a column. It is the scanner looking for a source and finding
nothing. The blank is evidence.

**Source Type "Other" is where Power BI puts anything it cannot name.** Custom
connectors, ODBC, blank queries and data typed straight into the file all land
in that bucket. Combined with a blank location and a blank filename, the reading
is that these tables carry data that was pasted into the file rather than
fetched from anywhere.

If that is right, then the answer to the original question is uncomfortable but
clean: **these reports cannot be populated by fixing a credential, a gateway or
a refresh schedule. There is nothing to refresh. The data layer has to be
built.**

---

## 2. Four possible sources, and how to tell them apart in ten seconds

The diagnosis above is a strong hypothesis, not a fact, and it is cheap to
settle. Open the file in Power BI Desktop, go to Transform Data, and look at the
first line of each query in the Advanced Editor. The first function call names
the source and there is no ambiguity in it.

| First function in the query | What it means | Can it be populated? |
|---|---|---|
| `Table.FromRows(Json.Document(Binary.Decompress(Binary.FromText(` | Enter Data. The rows are compressed inside the file | No. Rebuild required |
| `#table({...},{...})` | Hardcoded literal typed into the M | No. Rebuild required |
| `Excel.Workbook(File.Contents("C:\...` | A workbook on somebody's desktop | Only for that person, on that machine |
| `Excel.Workbook(File.Contents("\\server\...` | A workbook on a share | Yes, if the share still exists |
| `SharePoint.Files(` or `SharePoint.Contents(` | SharePoint | Yes, with credentials |
| `Sql.Database(` | SQL Server | Yes, with a gateway and credentials |
| `Oracle.Database(` | Oracle, so probably the ISP ERP | Yes, with a gateway and credentials |
| `Odbc.DataSource(` | ODBC, which also reports as "Other" | Yes, with a gateway and a DSN |
| `Databricks...` | The lake | Yes, and this is the target state |

The two rows in bold territory are the ones that change the plan. Everything
below `#table` is a plumbing job measured in hours. The top two are a build.

---

## 3. Doing this without opening each file by hand

`tools/pbi_source_audit.py` does exactly the check in the table above, in bulk.
Point it at a folder of `.pbix` files and it reads the Power Query out of each
one, splits it into queries, and classifies every query by the function it uses
to reach its data.

```
python tools/pbi_source_audit.py --input ./reports --markdown audit.md
```

Output is a verdict per report plus the detail behind it:

```
| Report                      | Queries | Verdict                                    |
|-----------------------------|---------|--------------------------------------------|
| ISP Velocity Changes.pbix   | 4       | NO LIVE SOURCE. Every query holds a ...    |
| Outbound Volume.pbix        | 1       | connected to a database or service         |
```

Two things it does that are worth knowing about.

**Where a query is static, it decodes the frozen payload.** Enter Data stores
its rows as deflate compressed JSON in base64, so the tool unpacks it and prints
the row count, the column count and the first few rows. Those column names are
the specification for the rebuild, because they are what the original author
decided the report needed. If there is a date column, the last value in it dates
the snapshot, which usually answers "how old is this?" on the spot.

**It abbreviates paths, hostnames and URLs by default**, so the output can go
straight into a ticket or an email. It also flags, without printing, anything in
the M that looks like a password or a key.

It runs on a `.pbix`, on a folder of them, or on M code copied out of the
Advanced Editor, which is the fallback for a report that can be seen in the
Service but not downloaded. Standard library only, read only, it never writes to
the report.

The reason to run it across the whole list rather than these two reports is that
the question was about the list. One run separates "needs a credential" from
"needs a rebuild" for everything on it, and those two piles want very different
conversations.

---

## 4. Getting hold of the files

In order of preference:

1. **Download from the Service.** Workspace, the report, File, Download this
   file. Blocked if the report was published through a deployment pipeline, if
   it uses a live connection, or if the setting is off at tenant level.
2. **Ask the workspace admin** for the source file or for temporary access.
3. **Open the semantic model in the Service** and look at the table list and the
   refresh history. This is enough to confirm the diagnosis without the file at
   all, and it is covered in the next section.

---

## 5. Three checks in the Service that confirm the diagnosis without the file

Any one of these on its own is suggestive. All three agreeing is conclusive.

**Refresh history.** Semantic model, Settings, Refresh history. A model with no
scheduled refresh and no successful manual refresh has never pulled data from
anywhere.

**Data source credentials.** Same settings page. A model with a live source
lists its sources here and asks for credentials. A model built entirely from
pasted data lists nothing, because there is nothing to authenticate to.

**Gateway.** Same page again. Nothing bound, on a model that would need one,
means it was never intended to refresh.

Together these also answer the question the requester is really asking, which is
whether the reports ever worked. A model that has never refreshed successfully
never worked. It showed the numbers that were pasted into it on the day it was
built, and it has shown the same numbers ever since.

---

## 6. Finding who built it

Worth doing, because the original author knows what the numbers were supposed to
mean, and that is harder to reconstruct than the data.

- **The item's details pane in the Service** carries a created by and a
  modified by.
- **The semantic model's contact list**, on the settings page.
- **The workspace access list**, which is a short list of candidates even when
  the author has left.
- **The tenant audit log**, if an admin will run it. It holds the original
  `CreateDataset` and `PublishReport` events with the user and the date. This
  works even when the author's account is gone.
- **The Green Belt project file.** The context already in hand is that this
  originated in a Green Belt project on ISP velocity, run by someone who has
  since left. Green Belt projects are documented by design and the project
  storyboard will hold the definitions, the data sources and the thresholds.
  That document is more valuable than the PBIX and it is worth asking for by
  name.

---

## 7. What each outcome means for the plan

**If the queries are Enter Data.** Do not repair the reports. Read the column
names out of the frozen payload, treat them as the requirements that were agreed
at the time, and rebuild the measure in the lake where it can refresh nightly.
The rebuilt version is then a thin report over a governed source, which is the
same architecture already proposed for the distribution reporting.

**If the queries point at a workbook on a personal drive.** Slightly better,
same conclusion. It will refresh for one person on one machine, which is not a
report, it is a habit. Move the source somewhere governed, then rebuild.

**If the queries point at a live source.** Good news, and unlikely given the
evidence. Fix the credentials, bind a gateway, set a refresh schedule, and check
the numbers against something operations already trusts before telling anybody
it works.

---

## 8. The uncomfortable pattern

This is the second inherited Power BI artefact in the same building with the
same shape: business logic and data both living inside a single desktop file,
built by someone who has since left, with no written definition of what the
numbers mean.

Worth saying out loud when the plan is presented, because it changes the ask
from "please let me fix this report" to "please let me stop this happening a
third time". The fix for both is the same and it is already written up in
`docs/distribution-reporting/01-approach.md`: put the conformed data in the lake,
keep the report thin, and write the definitions down first.
