# Distribution reporting rebuild

Working notes for rebuilding the inbound and outbound distribution reporting after
inheriting an unfinished Power BI project. Written for my own use and for walking the
manager through the plan.

Sanitised for a public repository: no connection strings, internal hostnames, catalog
names, colleague surnames or email addresses. Those stay in internal notes.

## Contents

| Document | Purpose |
|---|---|
| [`01-approach.md`](01-approach.md) | The plan to propose. Why the last attempt failed, the architecture recommendation, sequencing, and the sixty second version |
| [`02-inherited-sql-findings.md`](02-inherited-sql-findings.md) | Defect register for the inherited queries. Six critical, eight high, six medium |
| [`03-metric-definitions.md`](03-metric-definitions.md) | The definition sheet template and the eight ambiguities that must be resolved before building |
| [`04-context-and-landscape.md`](04-context-and-landscape.md) | Systems, terminology, who to ask by role, open decisions, and the adjacent pallet utilisation project |
| [`05-build-runbook.md`](05-build-runbook.md) | Step by step build instructions, Phase 0 through Phase 5, with what done looks like at each step |

## The short version

Three things went wrong last time, and none of them were Power BI problems.

1. Nobody wrote down what the numbers meant, so they could not be checked.
2. Everything was assembled by hand inside one report file, so when the analyst left,
   the knowledge left.
3. The numbers were never reconciled against anything the business already trusts
   before leadership saw them.

So the order is: **define, source, conform, model, visualise, reconcile, publish.**
The visuals are last and they are the fastest part.

Meanwhile the inherited queries contain real, findable bugs. Two examples:

- The inbound appointments query joins appointments to ASNs to purchase orders on
  vendor ID alone, which is not a key in any of them. That is a cartesian product, and
  it inflates inbound counts by orders of magnitude.
- The ISP receipts extract covers a window that runs past the WMS cutover, while the
  current-system query has no date filter at all. So ISP is very likely counted twice
  from go-live onward, which would show as a step change in the trend with no
  operational cause.

Leading with specific defects rather than generalities is the point. It shows the
problem is diagnosable, which is the case for rebuilding rather than patching.

## Two decisions needed from leadership

1. How far back the history has to go. Recommendation: two years for phase one,
   designed so earlier years can be appended later without a rebuild.
2. Whether the data lake team can host the combined data, instead of two systems being
   stitched together inside Power BI. Recommendation: yes, and the data lake owner has
   already suggested the same thing independently.
