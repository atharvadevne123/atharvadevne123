# Context and system landscape

Reference notes assembled from the handover material. Kept deliberately free of
connection strings, internal hostnames, catalog names, colleague surnames and email
addresses, because this repository is public. Those live in internal notes only.

---

## The assignment

Rebuild the distribution reporting for the site. Inbound and outbound volume across two
product lines, Reagents and ISP (Instruments and Spare Parts). The audience is the site
director, and the report drives capacity and labour planning rather than being a
volume readout. The original target date was April and it has slipped. The previous
analyst has left. The distribution manager reviewed the previous version and rejected
it as not matching reality.

The manager's decision: document requirements from scratch, then rebuild.

---

## Systems

**Current WMS (Manhattan Active WM).** Live for both product lines since the 2025
go-live. Replaced the WMS role of both legacy systems. Its UI retains roughly 90 days;
data is fed nightly into a Databricks lakehouse where the `gold` layer holds the
reporting tables (`outbound_lpn`, `outbound_lpn_detail`, `order`, `order_line`, `item`,
`facility`, `receipt`, `inbound_lpn`, `asn`, `purchase_order`, `appointment`). This is
the source for everything post go-live, for both product lines.

**Legacy Reagents WMS (DFCS).** Retired as a WMS at go-live. Oracle backed, queried
through TOAD. There is no data lake for it. Pre go-live Reagents history exists only as
Excel extracts pulled month by month by ad hoc query. Its schema is terse four to six
character column names (`obo` order header, `obd` order detail, `sku` item master,
`mbo` and `mba` customer master, `ibo` inbound).

**Legacy ISP system (ADMS).** Oracle E-Business Suite. Was both WMS and ERP for ISP.
The WMS role moved to Manhattan; it remains live as the ISP ERP. Instances exist at
this site, at the Dallas manufacturing site, and in Singapore. The Dallas analytics
team owns an ADMS data lake. An upgrade around 2024 changed data formats, so
pre-upgrade and post-upgrade extracts are not directly comparable. Standard EBS
receiving tables apply (`rcv_transactions`, `rcv_lot_transactions`,
`rcv_shipment_lines`, `rcv_shipment_headers`, `mtl_system_items_b`).

**SAP.** ERP for Reagents. Transactions flow between the ISP ERP, SAP and the WMS.

**Important:** there is no single central lake. Each system has its own. When people at
the site say "the data lake" they mean the WMS one, because it is the only one they
deal with.

---

## Terminology

| Term | Meaning |
|---|---|
| Kit | The product unit. Kits go in boxes, boxes go on pallets. Exact definition still to be confirmed |
| oLPN | Outbound License Plate Number. The label on every outgoing package |
| iLPN | Inbound License Plate Number. The label on incoming boxes |
| ASN | Advance Shipping Notice. Supplier's notice of an incoming shipment |
| PO | Purchase Order |
| Appointment | Booked dock slot for an inbound delivery |
| Product class | Item attribute used to split Reagents from ISP. Current rule is unreliable |
| Distribution group | Item grouping carried through from the legacy Reagents system |
| CX1 to CX4, CX7, CX8 | WMS location codes meaning pallet storage |
| CX5, CX11, CX12 | WMS location codes that are not pallet storage |
| Tier 1 / 2 / 3 | Daily operational meetings. Tier 2 is 10am, area representatives. Tier 3 is senior leadership |
| MI boards | Physical metric boards in each area. Currently not maintained |

Pre go-live the legacy systems used order and sub-order terminology rather than LPNs,
so legacy reports and current reports do not share vocabulary. Mapping that is part of
the job.

---

## Who to ask, by role

Real names and contact details stay in internal notes. Kept here as roles so the
dependency map is usable.

| Role | Ask them about |
|---|---|
| Director | What decisions the report supports. Final consumer. Prefers simple and user friendly |
| Manager | Priorities, access, introductions, escalation |
| Distribution manager | Ground truth. Rejected the previous version. The person who must sign off definitions and reconciliation |
| Warehouse supervisor | Previously built reporting for his area, knows the ISP data and SQL. Now in an operational role, so his time is limited |
| WMS data lake owner | Databricks access, gold schema, the proposal to land ISP data alongside Manhattan |
| WMS reporting contacts (x2) | Existing reports, what already exists before rebuilding it |
| ISP SQL / TOAD contact | ISP ERP tables, the lot control question, the upgrade change |
| Reagents TOAD contact | Legacy Reagents extracts and their column semantics |
| ISP operations manager | ISP inbound, outbound, capacity and labour. Was previously the ISP manager, so holds the history. Currently unavailable |
| Power BI contact | Workspace, licensing, tenant conventions |
| Implementation partner consultants (on site, same office) | How the current WMS actually works. Nearest and most under-used resource |
| Manufacturing site analytics team | They own the ISP ERP lake and already have mature metrics |
| Labour management vendor contact | Labour event tables, later phase |
| Capacity contacts (site, and offsite / yard / trailer) | Pallet positions and storage capacity, later phase |

---

## Open decisions blocking the build

1. **History depth.** Two years, or back to 2022? Recommendation and reasoning in
   `01-approach.md`. Needs the director.
2. **Where the conformed layer lives.** In the WMS data lake, or stitched together
   inside Power BI? Recommendation is the lake. Needs the director to sponsor data lake
   team capacity.
3. **Exact cutover timestamp per product line.** Needed before any combined trend line
   can be trusted.
4. **The Reagents versus ISP classification rule.** The inherited rule is
   self-contradictory. Needs the business.

---

## Things worth knowing about how this site works

- It is a busy, multi-request environment. Requests arrive from several directions and
  more than one person may be working the same thing. Confirming who owns a request is
  part of the work.
- The metric boards and the tier meeting data were previously kept in a spreadsheet and
  the link to the reporting was never established. Rebuilding that process is queued
  behind the main reports.
- There is a backlog of previously built Power BI content of unknown value. Some may be
  useful, some abandoned. Auditing it is a later task, but check before building
  anything that might already exist.
- There is a divisional digital initiative with several workstreams including business
  intelligence, worth joining for context and for the governance material.
- Onboarding for this role did not previously exist. Documenting it as it goes is an
  explicit expectation.

---

## Adjacent project: pallet and warehouse utilisation

Handed over separately by a departing intern. Feeds the capacity metric later.

Goal: how much storage space exists versus how much is used, which needs to know how
much space each product takes.

Current state: roughly 500 items measured by hand. A spreadsheet holds quantity per
box and box dimensions. Boxes per pallet is filled in only where an item was found
physically stored on a pallet. Dimensions were clustered into standard box sizes, so
one confirmed count can populate every item sharing that size. Duplicate measurements
exist and are flagged.

Method for the gaps: take the item's dimensions, find another item with the same
dimensions, check its WMS location, and if the location is a pallet code (CX1 to CX4,
CX7, CX8) read the boxes per pallet from there. Where nothing is found on a pallet,
estimate from dimensions against standard pallet size and record it as an assumption.

Two known problems:
- The same product can ship in two different box sizes with two different quantities,
  but the WMS holds only one configuration per item. So reading quantity from one box
  and dimensions from the other gives a wrong estimate.
- The WMS has a native utilisation report using cubing, but it returns poor results
  because the dimension data it needs is not populated.

The real fix is to load the dimension data back into the WMS so the native report works
and the manual spreadsheet stops being needed. Worth proposing rather than rebuilding
the calculation in Power BI, but it is a phase two conversation.
