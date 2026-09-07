# Build runbook

Step by step, in order. Each step has a **Do**, a **Done when**, and a **Blocked by**
where one applies.

Do not skip ahead to Phase 3. Every previous attempt at this failed in Phases 1 and 2,
and the symptoms only became visible in Phase 5.

---

# Phase 0. Before Power BI opens

Most of this can start now, in parallel, while access is pending.

### Step 1. Request every access on day one

They have different lead times and some are sequential, so submit them all now.

| Access | Note |
|---|---|
| WMS view access | Requires training completion first, so start the training immediately |
| WMS data lake (Databricks) | The main one. Chase it |
| Power BI licence and a workspace | Needed to even open the inherited file |
| SharePoint holding the old file and legacy extracts | Ask the owner directly |
| Oracle / TOAD for the legacy systems | May become unnecessary if the lake route works, but request it anyway |

**Done when:** you can log into each one yourself, not when someone says it is approved.

### Step 2. Walk the floor before writing anything

Ask for a guided walk and see these specific things:

- An outbound label being applied to a package. That is an oLPN.
- An inbound label on a box at receiving. That is an iLPN.
- A kit. Hold one. Note that sizes vary a lot.
- A box, and how many kits go in it.
- A pallet in a pallet location, and how many boxes are on it.
- The pack stations, and the coolers and freezer.
- Receiving, from truck arrival to putaway.

At each one ask: **"what do you call this, and where does it show up in the system?"**
Write the answer down verbatim. This is how the vocabulary gap gets closed.

**Done when:** you can point at a row in a table and say what physical object it is.

### Step 3. Attend the daily tier 2 for two weeks

Sit at the 10am. Do not present anything. Write down every metric anyone mentions, who
mentioned it, and what they did about it.

**Done when:** you have a list of the numbers the business actually uses today. That
list is your reconciliation target in Phase 5, and it tells you which of the requested
metrics are real versus nice to have.

### Step 4. Inventory the inherited file. Two hours, not two days

Open it read only. Produce a plain list of:

- every query, its source, and its row count
- every measure and its definition
- every hardcoded value

Then check the one specific thing: open the applied steps of the inbound append and
read which queries feed it. The handover document says the outbound query was appended
into the inbound table. Confirm or rule it out.

**Done when:** you have the list and the answer to that one question. Then close it and
do not open it again. You are not repairing it.

---

# Phase 1. Definitions. No Power BI at all

Roughly two weeks. The deliverable is a signed document, not a dashboard. Expect to
have to defend that.

### Step 5. Interview the director. What decisions does this drive?

The one question, asked repeatedly: **"when this number moves, what do you do
differently?"**

Get five to eight concrete questions the report must answer, for example "do I need
overtime next week", "am I running out of cooler space", "is inbound volume growing
faster than we can receive it".

Any requested metric that cannot be tied to a decision gets cut. Say so at the time.

**Done when:** you have the list of questions written in her words.

### Step 6. Interview the distribution manager. Ground truth

He is the person who rejected the last version, so he is the person who has to sign off
this one. Work through the eight ambiguities in `03-metric-definitions.md`:

1. What is a kit? One SKU unit, or an assembly?
2. Is a box the same thing as an oLPN?
3. Which date puts a shipment in a month?
4. Are transfers, returns, samples and cancellations in or out?
5. Can Reagents and ISP quantities be added together at all?
6. What is the exact cutover timestamp per product line?
7. What changed in the ISP ERP upgrade?
8. Which statuses mean it physically happened?

**Done when:** every one has an answer attributed to a name. Where he does not know,
that becomes an action on someone else, not an assumption you make.

### Step 7. Fill in and sign the metric definition sheet

One row per metric, all nine fields from the template. A blank field is a blocker.

**Done when:** the distribution manager has initialled it. Physically or over email,
but explicitly.

### Step 8. Draw the data flow map

One page. Which system feeds which lake, who owns each, how access is requested, where
the cutover sits. The manager has asked for this directly and it costs a day.

**Done when:** she can hand it to the director without you in the room.

---

# Phase 2. Data layer

### Step 9. Profile every source before modelling it

This is the step that gets skipped and it is the cheapest bug detection available. For
each source table:

```sql
-- row count, and the real date range
SELECT COUNT(*), MIN(<date_col>), MAX(<date_col>) FROM <table>;

-- rows per month, to spot missing or duplicated periods
SELECT DATE_TRUNC('month', <date_col>) AS m, COUNT(*)
FROM <table> GROUP BY 1 ORDER BY 1;

-- null rate on every column you intend to use
SELECT COUNT(*) AS total,
       SUM(CASE WHEN <col> IS NULL THEN 1 ELSE 0 END) AS nulls
FROM <table>;

-- distinct values on anything you will filter or classify by
SELECT <col>, COUNT(*) FROM <table> GROUP BY 1 ORDER BY 2 DESC;
```

Run the monthly count on every source. A month with a suspiciously round number, a zero,
or double its neighbours is a data problem you want to find now.

**Done when:** you have a profile sheet per source and can explain any gap in it.

### Step 10. Rewrite the current WMS queries, one at a time, in Databricks

Not in Power BI. Power BI is the last place to debug SQL.

Work through the defect register. For each query:

- Put the declared grain in a header comment. One row equals what, exactly.
- Add the facility predicate. Parameterise it, do not hardcode it.
- Add the date bounds. Parameterise them.
- Add the status filter from Step 6.
- Replace the concatenated join key with the real column tuple:
  ```sql
  ON  a.ORDER_LINE_ID = b.ORDER_LINE_ID
  AND a.ORDER_ID      = b.ORDER_ID
  AND a.ORG_ID        = b.ORG_ID
  AND a.FACILITY_ID   = b.FACILITY_ID
  ```
- Change master data joins from `INNER` to `LEFT`.
- Make the product line rule emit `'UNCLASSIFIED'` for anything unmapped, never a raw
  code, and keep the raw inputs as columns so the bucket can be audited.
- Add `SOURCE_SYSTEM` and `PRODUCT_LINE` as literal columns.

Build the appointment, ASN and PO extracts as **three separate queries**, not one. They
are three different grains and joining them into one flat table is what produced the
cartesian product in the inherited version. Relate them in the model instead.

**Done when:** each query runs standalone and returns a sane row count.

### Step 11. Prove the grain before going further

For every fact query, run:

```sql
SELECT COUNT(*) AS rows,
       COUNT(DISTINCT <the declared key columns concatenated with a separator>) AS keys
FROM (<your query>);
```

**These two numbers must be equal.** If they are not, the grain is not what you think
it is and every quantity downstream is inflated. Stop and fix it before continuing.
This single check would have caught three of the six critical defects in the inherited
version.

### Step 12. Land the legacy history in one governed place

Not a local drive. SharePoint or the lake, with a fixed path that will not move.

Build a control sheet alongside it: rows and total quantity per month, per source.
Check it against the source system once. That sheet is how you will later prove no
month is missing or duplicated.

**Done when:** the extracts are re-findable by someone who is not you, and the control
totals match.

### Step 13. Resolve the ISP source

Two conversations:

- The ISP SQL contact: the lot control filter question, and what the upgrade changed.
- The manufacturing site analytics team: what their lake already holds, and whether the
  cleaned ISP data can be landed alongside the WMS data rather than merged in Power BI.

Do not request another ad hoc extract until you can specify exactly what you want. Every
previous extract came back as "that is not what that means."

### Step 14. Build the two conformed views

One outbound fact, one inbound fact. Each with:

- one declared grain
- a fixed column list
- `SOURCE_SYSTEM` and `PRODUCT_LINE` on every row
- one date column with one declared meaning

Every source maps into that shape. Build them as views in the lake if you have the
capacity for it, as dataflows if not. Not inside the report file either way.

### Step 15. Run the cutover check before building any chart

```sql
SELECT <date>, SOURCE_SYSTEM, COUNT(*), SUM(QUANTITY)
FROM <fact>
WHERE <date> BETWEEN <cutover - 14 days> AND <cutover + 14 days>
GROUP BY 1, 2 ORDER BY 1, 2;
```

Look at the daily combined total across the boundary. **It should be continuous.** A
step up means double counting. A step down or a gap means a filter is wrong or an era is
missing. Also confirm no date has rows from both systems for the same product line.

**Done when:** the line is flat across the cutover and no overlap exists.

---

# Phase 3. The model

### Step 16. Star schema, not a flat table

```
                 Dim_Date
                     |
Dim_Item  ---  Fact_Outbound  ---  Dim_Customer
                     |
              Dim_Facility        Dim_Source_System
                     |
               Fact_Inbound
```

- Import mode. Set incremental refresh on the fact tables once it is stable.
- Build a proper date table and mark it as the date table. Do not rely on auto date
  hierarchies, and turn them off in options.
- Single direction relationships, one to many from dimension to fact. Do not turn on
  bidirectional filtering to make something work. If you need it, the model is wrong.
- Both facts join to the same `Dim_Date` and the same `Dim_Item`. That is what lets
  inbound and outbound sit on one page.

### Step 17. Write measures once, in DAX, on the model

Never aggregate in a visual. Every number on the report comes from a named measure.

Watch the grain when writing them:

```
Shipped Kits    = SUM( Fact_Outbound[QUANTITY] )
oLPNs Shipped   = DISTINCTCOUNT( Fact_Outbound[OLPN_ID] )   -- not COUNTROWS
```

`COUNTROWS` on the outbound fact gives LPN lines, not LPNs, because the grain is one row
per LPN per order line. This is defect H6 and it is easy to reintroduce.

### Step 18. Hide everything that is not for the user

Hide every raw column, every key, and every helper table. If a field is not meant to be
dragged onto a canvas, it should not be visible in the field list. This is most of what
"simple and user friendly" actually means in practice.

---

# Phase 4. The report

### Step 19. Wireframe on paper first and show it to the director

Before building anything. One sketch per question from Step 5. Ask "is this what you
meant" while changes are still free.

**Done when:** she has seen a sketch and corrected it at least once.

### Step 20. Build the pages

- One page per question. Resist putting everything on one canvas.
- Filters at the top, in a consistent position on every page.
- The headline number in the top left is the one people will quote, so it had better be
  the one that matters. If Reagents and ISP cannot be summed, do not put a combined
  total there.
- Consistent colour meaning across pages. One colour is one product line, everywhere.

### Step 21. Put an assumptions and known gaps page in the report

Inside the report, not in a separate document nobody opens. List:

- every assumption still unconfirmed, with its owner
- the known missing periods
- the size of the `UNCLASSIFIED` bucket
- what the date column means
- last refresh time

A report that states its own limits gets trusted. One that hides them gets rejected the
first time somebody spots one.

---

# Phase 5. Validate, then publish

### Step 22. Reconcile month by month against something already trusted

At least six months. Compare your numbers against the tier board numbers from Step 3,
or an existing report, or a direct query the business already believes.

Build it as a table: month, your number, their number, variance, explanation. Every
variance needs an explanation. "Close enough" is not one.

### Step 23. Show the distribution manager the reconciliation before the director sees the report

This is the single most important step in the whole runbook. It is the one that was
skipped last time.

Walk him through the variance table. Let him find the problems in a working session
rather than in a review in front of leadership. Fix what he finds and go back again.

**Done when:** he agrees the numbers are right. Then and only then, book the director.

### Step 24. Publish properly

- Publish to a shared workspace, not My Workspace.
- Set up a gateway or a service principal for the connection. Personal credentials
  cannot drive an unattended refresh, and this takes lead time, so start it earlier than
  you think.
- Schedule the refresh and set failure notifications to go to more than one person.
- Set row level security if any of this is restricted.

### Step 25. Write the handover while it is fresh

The thing that made this job hard was that the last person's knowledge left with him.
Do not repeat it. Keep the metric definition sheet, the data flow map, the query files
and the reconciliation table current and in a shared location.

Not click by click instructions. Definitions, decisions, and who signed off on them.

---

## What to do first, in order, on Monday

1. Chase the access requests and start the training that gates them.
2. Book the floor walk.
3. Book 45 minutes with the distribution manager, with the eight questions.
4. Start attending the 10am.
5. Two hours in the inherited file, then close it.

None of that needs Power BI, and all of it is on the critical path.
