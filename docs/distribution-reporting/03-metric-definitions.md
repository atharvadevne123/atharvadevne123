# Metric definition sheet

The phase one deliverable. One row per metric, filled in with the business, initialled
by the distribution manager before any of it is built.

The point is not documentation for its own sake. It is that a number nobody has
defined cannot be checked, so it can only be accepted or rejected on gut feel. That is
what happened last time.

---

## The template

Every metric gets all nine fields. A blank field is a blocker, not a detail.

| Field | Why it matters |
|---|---|
| Business name | What operations calls it, not what the column is called |
| Definition | One sentence, plain English, no table names |
| Grain | What exactly one row represents |
| Filters | Statuses, order types, facility, org. Explicit inclusions and exclusions |
| Driving date | Which date puts the row in a month. Ship date, create date, receipt date |
| Source, legacy era | System and query, with the date range it covers |
| Source, current era | System and query, with the date range it covers |
| Known gaps | Missing periods, excluded categories, known undercounts |
| Owner | The named person who signs off that this is correct |

---

## Metrics in scope for phase one

From the previous analyst's documentation, the requested set was:

**Outbound**
- Quantity of kits shipped
- Count of oLPNs
- Count of boxes

**Inbound**
- Quantity of kits received
- Count of iLPNs
- Count of ASNs
- Count of POs

Capacity (pallet positions used against available) and labour management are separate
later phases. They depend on the pallet dimension data, which is a known gap in its own
right, and on a labour system owned outside the site. Do not let them into phase one.

---

## The ambiguities that have to be resolved first

These are the questions where a wrong assumption silently produces a plausible but
incorrect number. Each one needs an answer from a named person, not a best guess.

### 1. What is a kit?

Is one kit one unit of a SKU, or is a kit an assembly of several SKUs shipped together?

This decides whether quantity is a straight sum of line quantity or something else
entirely. The intern handover describes kits varying substantially in physical size and
several kits fitting in a box, which suggests a kit is a discrete sellable unit. But if
a kit is an assembly, then summing line quantity across component SKUs counts
components, not kits, and the headline number is meaningless.

**Ask: distribution manager.** This is the single most important definition in the
report and everything else depends on it.

### 2. Is a box the same thing as an oLPN?

Post go-live, an oLPN is the label on every outgoing package, so oLPN count and box
count may be the same metric under two names. Pre go-live, the legacy system derives a
three character box *type* code, which is not a count at all.

If they are the same thing, say so and ship one metric. If they are not, the difference
needs defining, and the legacy era needs a real source, because it currently does not
have one.

**Ask: distribution manager.**

### 3. Which date puts a shipment in a month?

Ship date, order date, or requested delivery date? For capacity and labour planning the
answer is almost certainly the date the work physically happened, which is ship date
outbound and receipt date inbound. Confirm it rather than assume it, and confirm it
matches whatever the tier boards already use, otherwise the report will disagree with
the numbers people see every morning.

**Ask: distribution manager, and check against the tier 2 boards.**

### 4. What is in and what is out?

- Inter-facility transfers, in or out of "shipped volume"?
- Returns and RTVs, do they count as inbound, as negative outbound, or not at all?
- Samples, no-charge and replacement orders?
- Cancelled and short shipped lines?

Each of these is a defensible yes or no. What is not defensible is different answers in
different visuals in the same report.

**Ask: distribution manager.**

### 5. Can Reagents and ISP quantities be added together?

If a Reagents kit and an ISP spare part are different physical units, then a combined
"total kits" number is meaningless and should not exist. The safe default is to show
them side by side and never sum them, with the combined view only for LPN and box
counts, which are genuinely comparable because they count packages rather than
contents.

**Ask: distribution manager and the ISP operations manager.** Worth raising explicitly,
because a single big total number is exactly what a dashboard tends to put in the top
left corner, and it may be the one number that should not be there.

### 6. What is the exact cutover date per product line?

Reagents and ISP may not have moved to the new WMS on the same date. Every fact row
needs to belong to exactly one system, so this needs to be a timestamp, not a month.

**Ask: the WMS implementation team.**

### 7. What changed in the ISP ERP upgrade?

The manager has flagged that an upgrade, possibly in 2024, changed the shape of the
data, so extracts before and after are not comparable. Needed: the date, which tables
and columns changed, and whether pre-upgrade data needs a different mapping.

**Ask: the ISP SQL contact, and the manufacturing site analytics team who own that
lake.** Document it as a versioned mapping, because it will come up again.

### 8. Which statuses mean "it actually happened"?

Needed as an explicit list for outbound LPNs and for receipts. Anything not on the list
is excluded, and the list goes in the definition sheet so the exclusion is visible.

**Ask: distribution manager.**

---

## Known gaps to carry into the report

Recorded now so they appear on the assumptions page rather than being discovered by a
reader.

- ISP shipping data missing January to August 2022, and November to December 2023.
- ISP receiving data missing the same periods.
- Pallet dimension data is incomplete. Roughly 500 items measured, box-per-pallet
  counts only filled where an item was found stored on a pallet, and the WMS holds only
  one box configuration per item where some items ship in two.
- The legacy Reagents history exists only as manually assembled extracts.
- If the lot control filter in the ISP receipts query is confirmed as a defect, all
  previously published ISP inbound figures were understated.

A report that states its own gaps gets trusted. One that hides them gets rejected the
first time somebody notices.
