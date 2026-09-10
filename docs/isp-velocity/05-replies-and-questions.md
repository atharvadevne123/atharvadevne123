# Drafts and the question list

Names are left as placeholders because this repository is public. Roles are used
where the person matters more than the name.

---

## Draft A. Reply to the WMS admin, copying my manager

Purpose: accept the ask, make the session productive rather than a demo, and get
one question answered in advance that changes the plan if the answer is yes.

> Subject: Item Facility velocity extract
>
> Hi \<WMS admin\>,
>
> Thanks, that Sku Velocity field on Item Facilities is exactly the one. Yes
> please, a report of the current value for all parts is what we are after.
>
> Could I get 30 minutes with you to walk through pulling it? I would like to
> learn the route rather than be sent the file, since we will want to repeat
> this.
>
> Two things that would help me prepare, if you know them off hand:
>
> 1. Is there a last modified date and user on the item facility record, and can
>    the extract carry it? That tells us whether these values have been
>    maintained since go live or whether they came across in the migration and
>    have not been touched.
> 2. Does anything write to this field through an interface from the ERP? It
>    matters for the mass update question, because if something upstream owns
>    the field then a bulk change in the WMS would get reverted on the next feed.
>
> On the mass update: before we look at how, it would be useful to know whether
> the system can recalculate velocity from its own movement history on a
> schedule. If it can, the better outcome is probably to configure that and use a
> one off correction to set the starting point, rather than maintaining the field
> by hand.
>
> I will bring a short list of columns we would like on the extract.
>
> Thanks,
> \<me\>

---

## Draft B. The answer to "what does it take to populate these reports"

For my manager to use, or to send on. It has to be honest about the finding
without sounding like an excuse for not producing a report.

> The short version is that these two reports are not waiting on a connection or
> a password. As far as I can tell they were never connected to anything.
>
> The inventory of the report lists its three tables as `Query1`, `Query2` and
> `Query3`, all with source type "Other" and no source location and no filename.
> Those are the default names Power Query assigns, and that combination is what
> you get when data has been pasted into the file rather than pulled from a
> system. The scan found no source because there is no source. If that is right,
> and I can confirm it in about an hour with the file open, then refreshing them
> will never do anything. The numbers in them are a snapshot from whenever they
> were built.
>
> I would suggest not repairing them. Since go live the WMS feeds the data lake
> every night, which means velocity can be calculated from actual outbound
> movement, for every item, on a schedule, without depending on anyone's desktop.
> That is a better answer than the reports were ever going to give, and it does
> not go stale the moment it is built.
>
> Three steps, and the first one has value on its own:
>
> 1. **This week.** Confirm the diagnosis, and pull the current velocity
>    designation for all parts out of the WMS. That alone answers "what does the
>    system think today", which nobody can currently answer for all parts at once.
> 2. **Two to three weeks.** Calculate observed velocity from outbound movement
>    in the lake and compare the two. The output is a short list of items the
>    system calls slow that are actually fast, ranked by how often they are
>    picked. That list is the business case.
> 3. **After that.** Correct the designations, and if the WMS can recalculate
>    velocity on a schedule, configure it so this does not need doing again.
>
> One thing worth flagging. Velocity drives slotting and pick paths, so this is
> not only a reporting exercise. Any correction needs operations to agree it and
> to have the capacity to move stock to match, otherwise the data ends up
> disagreeing with the building, which is worse than the current position.
>
> I would also like to run the same check across the rest of the reports on the
> list. It is a quick automated pass and it separates the ones that need a
> credential from the ones that need rebuilding, which are very different
> conversations.

---

## Draft C. Asking for the Green Belt material

Short, and worth sending early because it takes time to surface.

> Subject: Velocity Green Belt project material
>
> Hi \<name\>,
>
> I am looking at the ISP velocity reports and I understand they came out of a
> Green Belt project on ISP velocity a few years ago.
>
> Would you have, or know where to find, the project storyboard or the closing
> pack? I am specifically after how velocity was defined at the time: what was
> counted, over what period, and what the thresholds were between low, medium
> and high.
>
> The reason it matters is that we are about to compare the velocity values in
> the WMS against what the outbound data actually shows, and without knowing what
> rule set the original values, any difference we find is not interpretable.
>
> Thanks,
> \<me\>

---

## The question list

Grouped by who to ask. Ordered so the ones that change the plan come first.

### Changes the plan if the answer is yes

1. Is item facility already in the nightly feed to the lake? *(data lake owner)*
2. Can the WMS recalculate velocity from its own movement history on a schedule?
   *(WMS admin, implementation partner)*
3. Does an upstream interface own the Sku Velocity field? *(WMS admin)*
4. Does the Green Belt storyboard still exist? *(the manager, the operations
   manager who holds the history)*

### Definition

5. What rule set the current L, M and H values, and when?
6. What is the full value domain, and what does blank mean?
7. Which of the three questions is being asked: slotting velocity, velocity
   changes over time, or value weighted turns?
8. What is the size of the fast pick face? The threshold should be anchored to it.
9. Does the WMS pick at kit level or component level?

### Data

10. Is `outbound_lpn_detail` one row per pick or one row per item per LPN?
    *(WMS reporting contacts)*
11. Which line types are not customer demand: transfers, replenishment,
    adjustments, returns?
12. What number does the site already trust for lines picked per day, to
    reconcile against?
13. Is there a last modified date and user on item facility?

### Access and logistics

14. Can the two velocity PBIX files be downloaded, or can access to the workspace
    be granted?
15. Who created the original reports? Item details, workspace access list, or the
    tenant audit log.
16. Which extract routes exist for item facility, and what are their row limits?
17. What is the change control process for a bulk attribute change?

### Operations

18. What consumes velocity downstream: slotting, putaway, pick path, wave
    planning, replenishment?
19. If a re-slot list were produced, who owns acting on it and what capacity do
    they have?
20. Is there a seasonality in ISP demand that a 90 day window would misread?
