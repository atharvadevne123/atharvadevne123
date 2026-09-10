# Pulling Sku Velocity for every item

The ask: learn how to pull a report from the WMS containing the velocity
designation for all parts, so it can be compared against the velocity report in
Power BI.

Sanitised for a public repository. Screen and field names below are the ones
visible in the WMS user interface, which are product standard rather than
internal.

---

## 1. What the field actually is

The screenshot shows the **Item Facilities** screen, and on it a field named
**Sku Velocity** holding the value `L`. Alongside it on the same screen sit
`Plant Code`, `Platform`, `Putaway Type`, `Bulk Break Point` and `Full Case`.

Four things follow from where that field lives, and all four shape the extract.

**It is an item and facility attribute, not an item attribute.** The screen is
Item *Facilities*, plural. The same part can carry a different velocity at a
different site, which is correct behaviour, because a part that flies at one
site may sit still at another. So the extract must be keyed on item **and**
facility, and any comparison must join on both. Joining on item alone will
either duplicate rows or silently pick one facility's value, and both failures
look like data quality problems rather than join problems.

**Its neighbours are all slotting attributes.** Putaway Type, Bulk Break Point,
Full Case and velocity are the inputs to where stock gets put and how it gets
picked. That confirms what the field is for: it drives physical placement. It is
not a reporting label and changing it has consequences on the floor.

**`L` is one of a small set.** Almost certainly `L`, `M` and `H`. Confirm the
full domain rather than assuming it, because a fourth value, or blanks, will
turn up in the extract and it is better to know in advance what they mean.

**Nothing on that screen says when it was last set, or by what rule.** That is
the gap that matters most, and it is question one in the list at the end.

---

## 2. Check this before doing anything else

**Does Item Facility already land in the lake nightly?**

The WMS already feeds the gold layer every night. If item facility is part of
that feed, or can be added to it, then there is no extract to pull, no file to
pass around, and the comparison becomes a query that runs on a schedule instead
of a task somebody has to remember to repeat.

That is one message to the data lake owner and it could remove every option
below. Ask it first.

If the answer is no, ask the follow up: what would it take to add it? An item
facility table is small, slow changing and useful to more than this piece of
work, so it is an easy thing to justify.

---

## 3. Options if it is not in the lake, best last

**Option A. Export from the Item Facilities list screen.**

Search Item Facilities filtered by facility, export the result grid. This is the
option to learn first, because it is what was asked for, it needs no access
requests, and it produces an answer the same day.

Watch for three things:

- *Row caps.* Grid exports are usually capped. If the export comes back at a
  suspiciously round number, that is the cap and not the item count. Check the
  total on screen against the rows in the file, every time.
- *Visible columns only.* Exports typically carry the columns currently
  displayed. Add the columns needed to the grid layout before exporting.
- *Chunking.* If capped, split by a stable attribute, plant code or an item
  prefix, and stitch. Record which filter produced which file, or reconciling
  the total becomes guesswork.

**Option B. A scheduled extract from the reporting or integration layer.**

If the WMS has a standard extract or reporting module that can write item
facility to a share or SFTP on a schedule, that is the right answer for anything
recurring. Ask what already exists before asking for something new to be built.

**Option C. The REST API, scripted with pagination.**

Right answer if the comparison has to run repeatedly and there is no extract
module. Needs an integration or service account and the appropriate role, which
is an access request with a lead time, so start it early even if Option A is
covering the immediate need.

**Option D. Ask the implementation partner consultants.**

They are on site, in the same office, and they know which of A, B and C actually
exists in this configuration. This is the cheapest question in the document and
it is the most under used resource on the site.

---

## 4. The columns to ask for

Not just the velocity value. The extract is worth more if it carries enough
context to segment the results without going back for a second pull.

| Column | Why |
|---|---|
| Item ID | Join key |
| Facility ID | Join key. Non negotiable, see section 1 |
| Sku Velocity | The value being compared |
| Description | So the output is readable by people who do not know part numbers |
| Product class or equivalent | To filter ISP from the rest |
| Plant Code | Visible on the screen, useful for segmenting |
| Platform | Same |
| Putaway Type | The other half of the slotting picture |
| Full Case, Bulk Break Point | Context for why an item is slotted where it is |
| Item status, active flag | So discontinued parts can be excluded |
| Created and last modified date and user | **The most valuable columns in the list** |

That last row deserves its own sentence. If the extract can carry a last
modified date on the item facility record, it answers the question nobody can
answer right now: when was velocity last touched, and by whom? If most records
were last modified at go live and never since, the values are a migration
artefact rather than a maintained attribute, and that single fact reframes the
whole exercise.

---

## 5. Where the extract should land

Not a desktop. Not an email attachment. Not a personal drive.

Stage it as a table in the lake, `staging.mawm_item_facility_velocity`, with an
`extracted_at` column, which is what `sql/velocity_variance.sql` expects. Even a
manual CSV upload into a staging table is worth doing, because it makes the
comparison repeatable, it keeps a history of what velocity looked like at each
pull, and it means the next person does not have to find the file.

Keeping the history matters more than it sounds. Once there are two extracts a
few weeks apart, the question "is anybody maintaining this field?" gets answered
by a query rather than an opinion.

---

## 6. Questions for the WMS admin

Ordered so the first three can be asked in a five minute conversation.

1. What is the full set of values for Sku Velocity, and does blank mean
   anything different from `L`?
2. What rule set these values, and when? Was it a migration default at go live,
   a manual judgement, or a calculation?
3. Is there a last modified date and user on the item facility record, and can
   the extract carry it?
4. Does anything recalculate velocity automatically, on any schedule?
5. Does any upstream system write to this field through an interface? If the
   ERP owns it, a manual change here gets reverted on the next feed and that
   changes the whole approach. See `03-mass-update.md`.
6. What consumes velocity downstream: slotting, putaway, pick path, wave
   planning, replenishment? Knowing what breaks tells us how carefully to move.
7. Which export or extract routes exist for item facility, and what are their
   row limits?
8. Is item facility in the nightly feed to the lake, and if not, what would it
   take?
