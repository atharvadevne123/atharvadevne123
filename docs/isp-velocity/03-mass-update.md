# Changing velocity in bulk

The second question asked was whether there is an option in the WMS to mass
update velocity for many items at once.

Short answer: almost certainly yes, by more than one route. The longer and more
useful answer is that the mass update is the least interesting part of the
problem, and doing it before answering two other questions would be a mistake.

---

## 1. Ask these two questions before asking how

**Does anything upstream own this field?**

If an interface from the ERP writes item facility attributes into the WMS, then
a mass update applied in the WMS gets quietly reverted the next time that
interface runs. The change appears to work, the report looks right for a day or
two, and then the values drift back with nobody watching. This is the single
most common way a bulk data correction fails, and it is invisible unless
somebody asks in advance.

If the ERP does own it, the update has to be made there, or the interface has to
be told to stop overwriting it. Either way that is a different piece of work
with different people in it.

**Can the WMS recalculate velocity itself?**

Many warehouse systems can re-class velocity from their own movement history on
a schedule, which is exactly the calculation this project is otherwise about to
build by hand. If that capability exists and is simply not switched on or not
configured, then the correct outcome of this work is not a mass update at all.
It is a configured recalculation running on a cadence, and a one off mass update
only to correct the starting position.

That distinction is worth being firm about. A mass update fixes the values
today. A recalculation stops them going stale again. The reason this report
exists at all is that nobody has been maintaining these values, and a mass
update does nothing about that.

---

## 2. The routes, once those are answered

To confirm against this configuration rather than assumed:

**Bulk edit on the list screen.** Select rows in an Item Facilities search and
apply an attribute change to the selection. Usually role gated, usually capped
at a modest number of rows. Fine for tens of items, not for thousands.

**Import or data loader.** Upload a file of item, facility and new value.
Normally the right route for a large correction, because the file is reviewable
before it is applied and it doubles as the record of what was changed.

**REST API.** Scripted updates, batched, with a log. The right route if this has
to be repeatable, and the natural pair to the API extract in
`02-mawm-velocity-extract.md`.

**The recalculation job**, if it exists. See above. This is the one to hope for.

---

## 3. How to do it without causing an incident

Velocity drives slotting, putaway and pick path. A mass change to it is not a
data change, it is an instruction to move physical stock. Treat it accordingly.

1. **Extract first, and keep it.** The before state is the only way back. Stage
   it with a timestamp, as in `02-mawm-velocity-extract.md`.
2. **Change control.** Whatever the site's process is, this goes through it. The
   audience for a velocity change is operations, not reporting.
3. **Scope it small first.** One product class, or one facility, or the top
   fifty items by pick lines. Enough to see the effect, small enough to reverse
   by hand.
4. **Agree what happens physically.** A re-class is only worth anything if stock
   actually moves to match it. Whoever owns slotting needs to know it is coming
   and needs the capacity to act on it. A velocity field that says `H` on an item
   sitting in a back aisle has made things worse, not better, because now the
   data disagrees with the building.
5. **Extract again and diff.** Prove the change landed, prove nothing else moved,
   and prove it is still there a week later. That last check is what catches an
   upstream interface quietly reverting the work.
6. **Then widen.**

---

## 4. What to recommend

Assuming the recalculation capability exists:

> Run the comparison, agree the thresholds with operations, apply a one off
> correction through the import route for the items where the gap is costing
> something, and then configure the recalculation so this never has to be done
> by hand again.

Assuming it does not:

> Same one off correction, plus a scheduled report that lists items whose
> observed velocity has diverged from their designation, reviewed on a cadence
> that operations owns. The report is the compensating control for the missing
> automation, and it should be small and actionable rather than a full listing.

Either way the deliverable is not a dashboard. It is correct velocity codes in
the WMS. Worth stating plainly when this is presented, because a report that
nobody actions is how the current situation came about.
