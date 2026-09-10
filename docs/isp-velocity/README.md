# ISP velocity reports

Working notes on the two ISP velocity reports in Power BI, the velocity
designation held against every part in the WMS, and what it would take to make
the two agree.

Sanitised for a public repository: no connection strings, internal hostnames,
catalog names, colleague surnames or email addresses. Those stay in internal
notes.

## Contents

| Document | Purpose |
|---|---|
| [`01-report-diagnosis.md`](01-report-diagnosis.md) | Why the reports are empty, how to confirm it in ten seconds per query, and how to check the whole report list at once |
| [`02-mawm-velocity-extract.md`](02-mawm-velocity-extract.md) | Pulling Sku Velocity for every part. Four routes, the columns to ask for, and the question that could remove the need entirely |
| [`03-mass-update.md`](03-mass-update.md) | Bulk changing velocity, the two questions to answer before asking how, and how to do it without causing an incident |
| [`04-velocity-definition.md`](04-velocity-definition.md) | What velocity should mean, the thresholds, the seven edge cases that produce confident wrong answers, and what the comparison should output |
| [`05-replies-and-questions.md`](05-replies-and-questions.md) | Draft replies and the full question list, grouped by who to ask |

| Code | Purpose |
|---|---|
| [`tools/pbi_source_audit.py`](../../tools/pbi_source_audit.py) | Reads a folder of PBIX files and reports which are connected to a source and which are carrying a pasted snapshot |
| [`sql/velocity_observed.sql`](../../sql/velocity_observed.sql) | Observed velocity per item and facility from outbound movement in the gold layer |
| [`sql/velocity_variance.sql`](../../sql/velocity_variance.sql) | System designation against observed, the confusion matrix, and the ranked re-slot candidates |

## The short version

**The reports are not broken. They were never connected.**

The report inventory lists their tables as `Query1`, `Query2` and `Query3`, all
with source type "Other" and no source location and no filename. Those are
Power Query's default names, and that combination is the signature of data
pasted into a file rather than pulled from a system. The scan found no source
because there is no source.

So the honest answer to "what does it take to populate these?" is that no amount
of credential, gateway or refresh schedule work will do anything. The data layer
has to be built. That takes an hour to confirm and it is worth confirming before
saying it out loud.

**There is a much better answer available than the one that was lost.** Since go
live the WMS has fed the lake nightly. Velocity can be calculated from actual
outbound movement, for every item, on a schedule. That is a stronger report than
the original ever was, and it does not depend on anybody's desktop.

**The interesting question is not the report anyway.** Every part carries a
velocity designation in the WMS that drives where it gets slotted and how it
gets picked. Nobody currently knows what rule set those values or when they were
last reviewed. Comparing them against actual movement produces a ranked list of
items the system calls slow that are in fact fast, and every one of those is
costing travel on every pick. That list is the deliverable. The dashboard is
just how it gets looked at.

## Sequencing

**Week one.** Confirm the diagnosis with the file open. Run the audit tool
across the whole report list, not just these two, so the ones needing a
credential are separated from the ones needing a rebuild. Pull the current
velocity designation for all parts from the WMS and stage it. That last item has
standalone value: nobody can currently answer "what does the system think" for
all parts at once.

**Weeks two and three.** Recover the original definition if it survives in the
Green Belt material. Agree the measure and the thresholds. Build observed
velocity in the lake, reconcile the totals against something operations already
trusts, then produce the comparison.

**After that.** Correct the designations through change control, smallest
meaningful scope first. If the WMS can recalculate velocity on a schedule,
configure it, because that is what stops this recurring.

## Four things to decide, and who decides them

1. **Which question is being asked.** Slotting velocity, velocity changes over
   time, or value weighted inventory turns? The two report names suggest two
   different answers and the original conversation suggests a third. Needs the
   requester.
2. **The thresholds.** They should be anchored to the size of the fast pick face,
   which is a physical constraint, rather than to a round percentage. Needs
   whoever owns slotting.
3. **Whether velocity is recalculated or maintained.** A mass update fixes today.
   A recalculation stops it going stale again. Needs the WMS admin to confirm the
   capability exists.
4. **Who acts on the output.** A re-slot list only has value if stock actually
   moves to match it. A velocity flag that disagrees with the building is worse
   than the current position. Needs operations to own it before anything is
   changed.

## Related

This is the second inherited Power BI artefact in the same building with the
same shape: data and business logic both living inside one desktop file, built by
someone who has since left, with no written definition of what the numbers meant.
The diagnosis and the fix are the same as in `docs/distribution-reporting`, which
is on its own branch and not yet merged, and the two pieces of work should be
argued as one.
