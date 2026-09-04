# How to approach the rebuild

The proposal to walk through with the manager. It answers one question: why will this
attempt succeed where the last one did not?

---

## 1. Diagnose the last attempt before proposing anything

Three things went wrong. None of them were Power BI problems.

**Nobody wrote down what the numbers mean.** There is a detailed build document, and it
is entirely click-by-click instructions: open this, load that, change this format.
There is not one sentence defining what a shipped kit is, which order statuses count,
or which date drives a metric. So when the distribution manager said the numbers were
wrong, there was nothing to check them against, and no way to tell a bug from a
misunderstanding.

**Everything lived inside one Power BI file.** Business rules were encoded as Power
Query steps and hand-renamed columns. History sat in Excel workbooks assembled by
hand. When the analyst left, all of it left with him. That is not a criticism of him,
it is a design that guarantees this outcome.

**The numbers were never reconciled before they were shown to leadership.** The first
person to check them against reality was the distribution manager, in a review, in
front of the director. That is the most expensive possible place to find out.

Say this plainly. It sets up everything that follows, and it makes clear the plan is
not "be more careful this time".

---

## 2. Definitions before data, data before visuals

The order matters and it is the whole proposal.

```
  Define  ->  Source  ->  Conform  ->  Model  ->  Visualise  ->  Reconcile  ->  Publish
```

The visual layer is the fastest part and it is last. Most of the calendar goes into
the first three steps. When the manager asks why the dashboard is not appearing in
week two, this diagram is the answer.

---

## 3. Build a data layer, not a report file

Recommended architecture:

| Layer | What it holds | Where it lives |
|---|---|---|
| Source | Manhattan gold tables, legacy Reagents extracts, ISP ERP data | as-is |
| Conform | one outbound fact, one inbound fact, declared grain, `Source_System` and `Product_Line` on every row | **Databricks views** |
| Model | star schema plus DAX measures defined once | Power BI semantic model |
| Report | thin, few pages, built for the site director | Power BI report |

**The recommendation is to put the conformed layer in Databricks, not in Power Query.**
The data lake contact already suggested this independently, which is worth mentioning,
because it means the proposal has technical backing from the team that owns the
platform.

Reasons to give:

- A rule gets fixed in one place instead of inside a desktop file.
- The logic is readable by the data lake team and reviewable by operations, so it can
  actually be validated instead of taken on trust.
- It survives the analyst leaving. That is not hypothetical here.
- Refresh gets fast, because the joins and filters run in the warehouse rather than
  pulling whole tables into Power BI.
- The legacy Excel history stops being a single point of failure sitting on somebody's
  drive.

The honest cost: it needs capacity from the data lake team, which needs the director
to sponsor it. That is a decision to ask for, not to assume.

**Fallback if that capacity is not available:** build the conformed layer as Power BI
**dataflows** in a shared workspace rather than inside the PBIX. Same principle, lower
ceiling. Either way, the first move is to get the legacy extracts off local drives and
into one governed location with a fixed path.

---

## 4. Recommendation on the two open decisions

**History depth.** Recommend two years for phase one, roughly 2024 forward, with the
model designed so more history can be appended later without a rebuild.

The case: capacity and labour planning runs on recent run rates and seasonality, and
two years still gives one full year over year comparison. The marginal cost of 2022
and 2023 is high and it is exactly where the last attempt stalled, because it means
hand-assembling legacy Excel and dealing with an ERP data format that predates the
upgrade. Frame it as a phase, not a refusal: "2024 forward by <date>, and we will
scope the earlier years once the model is stable." That is much easier for the
director to approve than a request to drop history.

**ISP data source.** Recommend cleaning the ISP data and landing it in the WMS data
lake alongside Manhattan, rather than merging two systems inside Power BI. Same
reasoning as the layer decision above. Combining two systems inside a report file is
where terminology mismatches turn into silently wrong numbers, and it is unreviewable
by anyone except whoever built it.

---

## 5. Sequencing

**Phase 0, weeks 1 to 2. Access and orientation. Runs in parallel with everything.**
- Chase access: WMS view, data lake, Power BI workspace, the SharePoint holding the
  old file and the legacy extracts.
- Walk the floor. See a kit, a box, a pallet, an outbound label, an inbound label,
  receiving, the pack stations, the coolers. Do this before writing any DAX. The
  manager has already said this matters and she is right.
- Attend the daily 10am tier 2 for two weeks. It is the cheapest way to learn who owns
  what and what people actually argue about.
- Open the old file read only and inventory it: queries, measures, sources. Two hours,
  not two days. The purpose is to harvest the SQL and check the one specific thing in
  the defect register (C5, whether outbound got appended into the inbound table), not
  to repair it.

**Phase 1, weeks 2 to 3. Requirements.**
- One workshop with the director (the consumer) and the distribution manager (the
  reality check). Anchor every metric to a decision: what will you do differently
  depending on what this number says? A metric that cannot answer that gets cut.
- Produce the metric definition sheet and get it initialled. This is the phase one
  deliverable. Not a dashboard.
- Produce the system and data flow map the manager has explicitly asked for. Which
  system feeds which lake, who owns each one, how access is requested. It costs a day
  and she can show it to the director immediately.

**Phase 2, weeks 3 to 5. Data layer.**
- Rewrite the Manhattan queries against the defect register.
- Land the legacy Reagents history in one governed location, with a per-month control
  sheet of row counts and total quantity.
- Resolve the ISP source with the ISP SQL contact and the manufacturing site's
  analytics team.
- Build the conformed outbound and inbound facts.

**Phase 3, weeks 5 to 7. Model and report.**
- Star schema, measures defined once, one page per question the site director actually
  asks, filters at the top, and an assumptions and known gaps page inside the report
  itself.

**Phase 4. Reconciliation and sign off.**
- Reconcile every metric, month by month, for at least six months, against something
  the business already trusts.
- **Show the distribution manager the reconciliation before showing the director the
  report.** This is the step that was skipped last time and it is the one that decides
  whether this succeeds.

---

## 6. Working practices to state up front

- Every business rule gets written down with a named owner. Where an assumption has to
  be made, it goes in the assumptions table visible inside the report, not in
  somebody's head.
- No business rule gets decided alone. The previous attempt failed partly because
  reasonable-looking decisions were made by someone without the operational context to
  make them.
- Status gets reported as decisions blocked, not tasks done. The manager said directly
  that she could not get a clear statement of what was blocking the last attempt, which
  meant she could not bring in help. So: "blocked on the product class rule, need 20
  minutes with the distribution manager" rather than "still working on the outbound
  query".
- The director wants simple and user friendly. Design from her questions inward, not
  from the data outward.

---

## 7. The sixty second version

If she asks in a hallway:

> Three things went wrong last time and I want to fix the causes rather than the
> symptoms. Nobody wrote down what the numbers meant, so they could not be checked.
> Everything was assembled by hand inside one Power BI file, so when the analyst left,
> the knowledge left. And the numbers were never reconciled against anything the
> business already trusts before leadership saw them.
>
> So: first two weeks I learn the floor and write a metric definition sheet that the
> distribution manager signs. Then I build the data layer in the lake rather than
> inside Power BI, so the logic is reviewable and it survives me. Then I reconcile
> month by month against numbers he already believes. The visuals come last and they
> are the fastest part.
>
> I have already found specific bugs in the inherited queries, including one join that
> multiplies the inbound counts and one that looks like it double counts ISP across
> go-live. I would rather show you those than talk in generalities.
>
> Two decisions I need from you and the director: how far back the history has to go,
> and whether we can get the data lake team to host the combined data instead of me
> stitching it together inside Power BI.

That last paragraph is the important one. It ends with a specific ask, which is what
turns a status update into a decision meeting.
