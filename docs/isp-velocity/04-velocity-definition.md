# What velocity means, and how to compare the two

Before the WMS designation can be compared against anything, both sides have to
be defined. The comparison is arithmetic. The definitions are the work.

---

## 1. The two reports are not measuring the same thing

The names on the list already say so.

**`ISP Velocity Changes`** implies transitions, items moving between velocity
classes over time. That is a maintenance report. It answers "what changed, and
should it have?".

**`ISP On Hand Velocity - Price`** implies value weighting against inventory on
hand. That answers "where is the money sitting, and how fast does it turn?".
Useful, and a finance question rather than a warehouse one.

Neither is a slotting velocity, which answers "how often do we walk to this
location?". Three different questions with one word covering all of them.

So the first thing to establish is which question is actually being asked.
Judging by where the conversation started, which was the designation on the
product master that drives slotting, the answer is the third one. Confirm it,
because building the wrong one of these three is an easy and expensive mistake.

---

## 2. Measure pick lines, not units and not value

Slotting cost is a function of how many times somebody has to travel to a
location. It is not a function of how many units come out when they get there,
and it is definitely not a function of what those units are worth.

- An item picked 400 times in a quarter, one unit each time, is a fast mover.
- An item picked twice in a quarter, 5,000 units each time, is a slow mover with
  large orders. Slotting it in the golden zone wastes the golden zone.
- An expensive item picked twice is a finance concern and a security concern,
  and it is still a slow mover.

So **pick lines is the primary measure**. Units, cases and value ride alongside
as secondary columns because they answer the other two questions, and because
somebody will ask for them.

`sql/velocity_observed.sql` implements this, with the assumed column names
listed in its header so they can be checked against the catalogue in five
minutes.

---

## 3. The direction trap

The WMS uses `L`, `M`, `H`. Classic ABC analysis uses `A`, `B`, `C`.

In ABC, **A is fast**. In the WMS letters, **H is fast**. So `A` maps to `H` and
`C` maps to `L`, and the two scales run in opposite directions alphabetically.

Somebody will get this backwards at least once, and the failure is silent
because the output still looks like a sensible distribution. The SQL classifies
straight into `H`, `M` and `L` and never produces an `A`, `B` or `C`, precisely
so there is nothing to translate.

---

## 4. Thresholds, and why the old ones matter

The default in `velocity_observed.sql` is cumulative share of pick lines:

- `H`: items making up the first 80% of pick lines
- `M`: the next 15%
- `L`: the last 5%

Those numbers are a convention, not a truth. Two things need to happen to them.

**Recover the original rule.** The values sitting in the WMS today were set by
some rule at some point, and comparing against them without knowing that rule
produces a variance number that means nothing. If the original was a fixed
threshold, say more than 50 picks a month is `H`, then a cumulative share rule
will disagree with it everywhere and none of that disagreement is a finding. The
Green Belt project storyboard is the most likely place to find it.

**Agree the new one with operations.** The right split depends on the size of the
fast pick face, which is a physical constraint. If the golden zone holds 300
locations then `H` needs to land near 300 items, and that is a decision for
whoever owns slotting, not a statistical default. Anchoring the threshold to the
physical constraint rather than to a round percentage is the difference between
a report that gets used and a report that gets admired.

---

## 5. Edge cases that will otherwise ruin the output

Each of these produces a confident, wrong recommendation if left alone. All are
flagged in `velocity_observed.sql`.

| Case | What goes wrong | Handling |
|---|---|---|
| New item | No history, so it classifies as slow and gets slotted in the back on the day it launches | Flag items first shipped inside the window and exclude from re-slot lists |
| Single order spike | One large order makes a dead part look fast | Flag items whose whole window is one or two active days |
| Discontinued item | Classifies as slow, correctly, but re-slotting it is wasted effort | Exclude on item status |
| Zero movement | Absent from a movement query entirely, so it silently disappears | Left join from the stocked item list, so it appears as a zero |
| Seasonal item | Fast in season, dead outside it, and the window decides which | Report both a rolling 90 day and a rolling 12 month class, and let the difference identify seasonality |
| Kits and components | Movement recorded against one level, velocity set at another | Establish which level the WMS picks at before trusting either |
| Facility scope | The same part with two designations at two sites | Always group by item and facility, never item alone |

The window length itself is a decision. Ninety days responds quickly and
overreacts to a quiet quarter. Twelve months is stable and slow to notice a
genuine change. Producing both, and treating the disagreement between them as
the signal, is more useful than picking one and defending it.

---

## 6. What the comparison should produce

Three outputs, in this order. `sql/velocity_variance.sql` produces all three.

**A confusion matrix.** WMS designation down the side, observed class across the
top. The diagonal is agreement. Everything off it is the conversation. This is
the one thing to put in front of leadership, because it fits on a slide and it
makes the size of the problem obvious without anybody reading a row.

Weight it by pick lines as well as by item count. Ten thousand slow items
disagreeing matters far less than forty fast ones, and an item count alone hides
that completely.

**A coverage report.** Items in the WMS extract with no movement data, items
moving with no WMS record, and items with velocity not set at all. This is
usually where the first real finding is. A large block of blanks means the field
was never populated for those parts, which is a different and simpler problem
than a field being wrong.

**A ranked re-slot candidate list.** Items the WMS calls slow that are actually
fast, ordered by pick lines descending, with the new item and single order spike
cases already excluded. Ordered that way, the top twenty rows are the entire
business case, because those are the items costing travel on every pick.

---

## 7. Reconcile before anybody sees it

Total pick lines for the window, per facility, checked against a number
operations already trusts. If the site tracks lines picked per day anywhere, on
a metric board, in a tier meeting pack, in an existing WMS report, that is the
check.

If it does not reconcile, the answer is not to explain the difference in a
footnote. The answer is to find out why before showing anybody the classification,
because every number downstream inherits the error.

This is the step that was skipped last time on the distribution reporting, and
the first person to check the numbers against reality was the distribution
manager, in a review, in front of the director. Not repeating that is worth the
extra day.
