# Defect register: inherited queries and pipeline

Findings from reviewing the previous analyst's captured SQL and build documentation.
Nothing here has been run against live data yet. Each item lists the effect on the
number so it can be confirmed or dismissed quickly once access is granted.

Connection identifiers (workspace host, SQL warehouse ID, catalog name) and the
contact list are deliberately not reproduced in this repository. They live in the
internal notes.

Legend for **Effect**: OVERCOUNT, UNDERCOUNT, WRONG SPLIT, or UNKNOWN.

---

## Critical

### C1. Appointments / ASNs / POs are joined on vendor only

```sql
FROM   appointment ap
LEFT JOIN asn            ON ap.VENDOR_ID = asn.VENDOR_ID
LEFT JOIN purchase_order po  ON ap.VENDOR_ID = po.VENDOR_ID
```

`VENDOR_ID` is not a key in any of the three tables. One vendor has many
appointments, many ASNs and many POs. The result is every appointment crossed with
every ASN crossed with every PO for that vendor.

**Effect: OVERCOUNT, severe.** A vendor with 50 appointments, 200 ASNs and 300 POs
produces 3,000,000 rows where roughly 550 are wanted. Any count of ASNs or POs, and
any quantity summed through this table, is inflated by orders of magnitude. If the
inbound page of the report used this, that alone explains "the data is way off".

**Fix.** Join on the real relationships. Appointment relates to ASN or shipment via
its own reference column, and ASN relates to PO through the ASN detail lines
(the PO reference sits on the line, not the header). Confirm the actual foreign keys
in the gold schema before writing it. Then verify: the row count of the result must
equal the row count of the driving table when the joins are genuinely many-to-one.

**Confirm with:** WMS data lake owner.

---

### C2. ADMS receipts fan out across lots, then the transaction quantity is summed

```sql
select distinct rlt.lot_num, msib.segment1 part_num, rsh.receipt_num,
       rt.transaction_date receipt_date, rt.quantity, rt.source_document_code
from apps.rcv_transactions rt, apps.rcv_lot_transactions rlt, ...
```

`rcv_transactions` is one row per receiving transaction. `rcv_lot_transactions` is
one row per lot within that transaction. Joining them multiplies each transaction by
its lot count, and `rt.quantity` is the whole transaction quantity, repeated on every
lot row. `SELECT DISTINCT` does not collapse them, because `lot_num` differs on each.

**Effect: OVERCOUNT.** A receipt of 100 units split across 4 lots reports 400.
ISP inbound quantity is inflated by the average number of lots per receipt.

**Fix.** Either drop the lot join when the metric is receipt quantity, or take the
lot level quantity from `rcv_lot_transactions` instead of `rt.quantity`. Decide which
grain the metric needs first, then pick the quantity column that matches it.

**Confirm with:** ISP SQL / TOAD contact.

---

### C3. The ADMS extract window crosses go-live, so ISP is counted twice

The ADMS receipts query filters `transaction_date between '26-FEB-2024' and
'26-FEB-2026'`. Manhattan go-live was during 2025 and the Manhattan Receipts query
covers Reagents *and* ISP with no date filter at all. Every ISP receipt between
go-live and the end of the ADMS window therefore appears in both sources, and both
are appended into the same fact table.

Supporting evidence from the file naming in the build document: the inbound side is
labelled "ADMS ISP Receipts Data 2025 Pre-Go Live", but the outbound side is labelled
"ADMS ISP Shipping Data 2025" with no Pre-Go Live qualifier. That strongly suggests
the outbound ISP 2025 extract was never trimmed at the cutover.

**Effect: OVERCOUNT.** ISP volume roughly doubles from go-live onward. On a trend
chart this shows as a step change with no operational cause, which is exactly the
symptom described.

**Fix.** Adopt a single cutover rule, below. Then re-pull both sides bounded by it.

**Confirm with:** the WMS implementation team for the exact cutover timestamp
per product line. Reagents and ISP may not have cut over on the same date.

---

### C4. The Manhattan oLPN join key is a concatenation with no delimiter

```sql
concat(olpn_det.ORDER_LINE_ID, olpn_det.ORDER_ID, olpn.ORG_ID, olpn.FACILITY_ID)
```
joined to
```sql
concat(order_line.ORDER_LINE_ID, orders.ORDER_ID, orders.ORG_ID, orders.FACILITY_ID)
```

Without a separator, `('1','23',...)` and `('12','3',...)` both produce the string
`123`. Across millions of order lines, collisions are certain, and each collision
joins unrelated order lines to each other.

**Effect: OVERCOUNT, unpredictable.** Duplicated oLPN rows and inflated quantity, in
a pattern that will not reproduce consistently, which makes it very hard to debug
later.

**Fix.** Join on the four columns directly:
```sql
ON  olpn_info.ORDER_LINE_ID = order_info.ORDER_LINE_ID
AND olpn_info.ORDER_ID      = order_info.ORDER_ID
AND olpn_info.ORG_ID        = order_info.ORG_ID
AND olpn_info.FACILITY_ID   = order_info.FACILITY_ID
```
If a concatenated key is genuinely needed, separate the parts with a character that
cannot appear in the values, for example `concat_ws('|', ...)`.

---

### C5. Outbound data may have been appended into the inbound table

The build document, inbound section, says:

> Append queries 'Reagents Inbound 2022-2025', '2023 to 2025 ISP Receiving Data'
> and **'oLPN Details'** to create 'Reagents & ISP Receipts 2022-YTD'

`oLPN Details` is the outbound query. The inbound equivalent is `Receipts`. This is
either a copy and paste error in the document, or it is what was actually built.

**Effect if real: WRONG, completely.** Post go-live inbound volume would be showing
outbound shipments.

**Fix.** This is the first thing to check when the old PBIX opens. Look at the applied
steps of `Reagents & ISP Receipts 2022-YTD` and read which queries feed the append.
Two minutes of work, and it either explains a large part of the rejection or rules
itself out.

---

### C6. The ADMS receipts query only returns lot controlled items

```sql
and msib.lot_control_code = 2
```

In Oracle EBS, `lot_control_code = 2` means the item is under lot control. Code 1
means no lot control. Spare parts are frequently not lot controlled.

**Effect: UNDERCOUNT.** Every non-lot-controlled ISP part is missing from inbound
entirely. Given ISP stands for Instruments and Spare Parts, this could be a large
share of the line.

**Fix.** Almost certainly remove the filter, and use an outer join to the lot table so
that non-lot items survive. Do not do this silently: it will change published ISP
inbound numbers, so it needs to be raised as a correction.

**Confirm with:** ISP SQL / TOAD contact, and the ISP operations manager.

---

## High

### H1. No status filter on outbound LPNs

`OLPN_STATUS_DESCRIPTION` is selected but never used as a predicate. Cancelled,
voided, short shipped and still-in-process LPNs are all counted as shipped volume.

**Effect: OVERCOUNT.** Also note `SHIPPED_DATE_TIME` will be null for anything not
actually shipped, so those rows land with a null ship date and either vanish from a
date-filtered visual or pile up in a blank bucket.

**Fix.** Get the list of statuses that mean "physically left the building" and filter
to them. Put the list in the metric definition sheet.

**Confirm with:** Distribution manager.

---

### H2. No facility or organisation filter in any Manhattan query

The catalog is shared. The oLPN query joins `facility` only to read `TIME_ZONE`, and
never filters on it. The Receipts query has no filter at all.

**Effect: UNKNOWN, potentially OVERCOUNT.** If any other site posts into the same
catalog, their volume is in the site director's report. Even if it is single-site
today, the absence of the predicate is a landmine.

**Fix.** Add an explicit facility predicate to every fact query, driven by a Power
Query parameter so it is visible and changeable in one place.

---

### H3. Inner joins to master data silently drop transactions

The oLPN query inner joins `item` and `facility`. The DFCS outbound query inner joins
`sku`, `mbo` and `mba`. Any transaction whose master record is missing, retired or in
a different org disappears without trace.

**Effect: UNDERCOUNT, silent.** This is the failure mode nobody notices, because a
row that is not there cannot look wrong.

**Fix.** Use left joins, and add a reconciliation query that counts rows where the
master record did not match. If that count is not zero, it goes on the known gaps
page of the report.

---

### H4. The Reagents / ISP split rule is self-contradictory and null unsafe

```sql
Case When product_class  = 'Z1' and ITEM_ATTRIBUTE1 in ('1021','204') Then 'REAGENTS'
     When product_class != 'Z1' and ITEM_ATTRIBUTE1  = '204'          Then 'ISP'
     Else product_class
End as OLPN_Prodcut_Class
```

Four problems.

1. `ITEM_ATTRIBUTE1 = '204'` appears on both branches, so the entire split rests on
   `product_class = 'Z1'`. The attribute contributes nothing except to exclude items.
2. `!=` is null unsafe. Any row with a null `product_class` matches neither branch and
   falls through.
3. The `Else` branch emits raw class codes, so the product line slicer silently gains
   a third, fourth and fifth bucket of unlabelled codes rather than being a clean
   two-way split.
4. `product_class` is itself `left(item.product_class, 2)`, a truncation that can
   merge two genuinely different classes into one.

**Effect: WRONG SPLIT.** Volume lands under the wrong product line, or under no
product line, and the two headline totals the site director cares about are both off.

**Fix.** Do not guess this one. Get the actual rule from the business, write it down,
and make the `Else` branch emit `'UNCLASSIFIED'` rather than a raw code, so anything
unmapped is visible instead of hiding. Also fix the `Prodcut` typo before it
propagates into DAX measure names.

**Confirm with:** Distribution manager and the ISP operations manager.

---

### H5. There is no iLPN query

The captured "iLPN Details" query and the "Receipt Details" query are byte for byte
identical: both select from `receipt` left joined to `inbound_lpn`. The iLPN copy is
also truncated, missing its `ON` clause.

**Effect: metric has no source.** Counting distinct `LPN_ID` off `receipt` counts only
iLPNs that produced a receipt line. An iLPN created but not yet receipted, or closed
without a receipt, is invisible.

**Fix.** Decide what "iLPNs received" means as a business event, then query
`inbound_lpn` directly against the date field that represents that event.

---

### H6. Counting rows will not give a count of oLPNs

The oLPN result grain is one row per oLPN per order line per item, because of the
`GROUP BY`. `QUANTITY` is already summed to that grain.

**Effect: OVERCOUNT of LPNs, and double counting risk on quantity.** A `COUNTROWS`
gives the number of LPN-lines, not LPNs.

**Fix.** In DAX, `DISTINCTCOUNT(olpn_id)` for the LPN count. For quantity, sum once at
this grain and never re-aggregate a pre-aggregated column. Note also that the build
document references an "oLPN Details Box Count Query" that was never captured, so the
box metric currently has no documented source at all.

---

### H7. DFCS shipped quantity is inferred, not measured

```sql
(obdoqt - obdbko) AS "Qty"    -- ordered minus backordered
```

This is a derivation of what was probably shipped, not a shipped quantity field. It
will not reflect cancellations or short picks that were recorded some other way.

**Effect: UNKNOWN.** Needs validation against a month the business already trusts.

**Confirm with:** Reagents TOAD contact.

---

### H8. Three different grains are appended into one flat table

`Reagents Outbound 2022-2025` (DFCS, order line grain), `2023 to 2025 ISP Shipping
Data` (ADMS, grain unknown) and `oLPN Details` (Manhattan, LPN-line grain) are
appended into one table, with columns renamed to match by hand.

Each has a different meaning of "Qty" and a different date semantic. `Ship Date` in
DFCS is a date. `Facility Shipped Date Time` in Manhattan is a UTC timestamp
converted to facility local time. The ADMS column was renamed from `Date-a` with no
recorded definition.

**Effect: the total is not any real quantity.** It is a sum of three different units.

**Fix.** Conform deliberately rather than by column renaming. Every row carries a
`Source_System` column and a `Product_Line` column, every source is mapped into one
declared grain, and the model can then always answer "where did this number come
from". Without a source column, reconciliation is impossible.

---

## Medium

### M1. No date bounds on the Manhattan queries
Both pull the entire table on every refresh. This is the likely cause of the slow
refresh the previous analyst reported. Bound them by date, keep the predicate foldable
so it executes in the warehouse, and use incremental refresh partitions once the model
is stable.

### M2. Oracle date literals compared as strings
`between '26-FEB-2024' and '26-FEB-2026'` relies on the session `NLS_DATE_FORMAT`. It
will error or silently mis-parse under a different session setting. Use
`TO_DATE('26-FEB-2024', 'DD-MON-YYYY')` with an explicit `NLS_DATE_LANGUAGE`.

### M3. The DFCS extracts were assembled by hand
The captured DFCS queries have hardcoded single month windows. The build document
mentions doing "each half" of a year separately, which points at the Excel row limit.
So the entire pre-go-live Reagents history is a stack of manually pasted extracts with
no lineage and no way to re-run. A single missing or duplicated month would be
invisible. Whatever is kept, it needs a control sheet: rows and total quantity per
month, checked against the source.

### M4. Timezone treatment differs across eras
Manhattan converts UTC to facility local. DFCS and ADMS dates are presumably already
local. Left alone this produces a small discontinuity at the cutover and disagreement
with operations at month end boundaries. Declare one rule and apply it to all eras.

### M5. "Box" does not mean the same thing on both sides of go-live
DFCS derives box as `SUBSTR(obopdc, 1, 3)`, which is a box *type* code, not a count.
In Manhattan the natural analogue is the oLPN itself or `CONTAINER_TYPE_ID`. If box
and oLPN turn out to be the same physical thing post go-live, they should be one
metric with one name, not two.

### M6. The connection uses personal credentials
The build steps say to click "Edit Permissions" and authenticate. That works on the
desktop but cannot drive an unattended scheduled refresh in the service. A gateway or
a service principal is needed before this report can refresh on its own, and that is
a request that takes lead time. Raise it early.

---

## The cutover rule to adopt

Stated once, applied everywhere:

> Every fact row belongs to exactly one source system, decided by one cutover
> timestamp per product line. Strictly before the cutover, the legacy source.
> At or after the cutover, Manhattan. No overlap and no gap.

Then build the check that proves it: for the two weeks either side of each cutover,
chart daily volume from both sources. If the combined line steps up or down, the rule
is wrong or a filter is missing. Do this before showing anyone a trend chart.
