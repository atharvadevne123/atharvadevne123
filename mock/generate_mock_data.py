#!/usr/bin/env python3
"""
Mock data generator for the distribution reporting rebuild.

Produces CSVs whose column lists match exactly what the rewritten source
queries return, so that when real access arrives you repoint Power Query at
Databricks and nothing downstream has to change.

Standard library only. No pip install required.

    python3 generate_mock_data.py --out ./data

Edge cases are deliberate, not accidental. See EDGE CASES below.
"""

import argparse
import csv
import datetime as dt
import os
import random

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SEED = 20260904                 # fixed so runs are reproducible

START_DATE = dt.date(2024, 1, 1)
END_DATE   = dt.date(2026, 9, 1)

# Cutover to the current WMS. DELIBERATELY DIFFERENT per product line, because
# in the real system they may well be, and the model has to cope with that.
CUTOVER = {
    "REAGENTS": dt.date(2025, 4, 14),
    "ISP":      dt.date(2025, 6, 23),
}

FACILITY_ID       = "LC01"
FACILITY_TIMEZONE = "America/Chicago"
ORG_ID            = "01"

# Average oLPNs shipped and receipts taken per working day
OUTBOUND_LPNS_PER_DAY = 120
INBOUND_RECEIPTS_PER_DAY = 40

# EDGE CASES, injected on purpose so the model is tested against them
P_UNCLASSIFIED   = 0.02    # product line cannot be derived
P_ORPHAN_ITEM    = 0.005   # item missing from the item master
P_NULL_BATCH     = 0.08    # no batch number on the line
P_MULTILINE      = 0.35    # oLPN carries more than one order line

STATUSES_SHIPPED     = ["SHIPPED", "CLOSED"]
STATUSES_NOT_SHIPPED = ["CANCELLED", "IN PROCESS", "PACKED"]
STATUSES_RECEIVED    = ["RECEIVED", "PUTAWAY COMPLETE"]

CARRIERS   = ["FEDEX", "UPS", "DHL", "WORLDCOURIER", "LTL01"]
SHIP_VIAS  = ["PRIORITY", "GROUND", "2DAY", "NEXTDAY"]
MODES      = ["PARCEL", "LTL", "AIR"]
ORDER_TYPES= ["CUSTOMER", "TRANSFER", "SAMPLE", "REPLACEMENT"]
CONTAINERS = ["BOX-S", "BOX-M", "BOX-L", "COOLER-M", "COOLER-L"]
CLIMATES   = ["AMBIENT", "REFRIGERATED", "FROZEN"]
DIST_GROUPS= ["DG-A", "DG-B", "DG-C", "DG-D"]

US_CITIES = [
    ("CHICAGO", "IL", "US"), ("DALLAS", "TX", "US"), ("NEWARK", "NJ", "US"),
    ("ATLANTA", "GA", "US"), ("PHOENIX", "AZ", "US"), ("BOSTON", "MA", "US"),
]
INTL_CITIES = [
    ("TORONTO", "ON", "CA"), ("SINGAPORE", "", "SG"), ("FRANKFURT", "HE", "DE"),
    ("DUBLIN", "D", "IE"), ("SAO PAULO", "SP", "BR"),
]

OUTBOUND_COLUMNS = [
    "OLPN_ID", "ORDER_LINE_ID", "ORDER_ID", "ORG_ID", "FACILITY_ID",
    "ITEM_ID", "BATCH_NUMBER",
    "SOURCE_SYSTEM",
    "PRODUCT_LINE", "PRODUCT_CLASS_RAW", "ITEM_ATTRIBUTE1_RAW",
    "QUANTITY",
    "SHIPPED_TS_LOCAL", "SHIP_DATE", "SHIPPED_TS_UTC", "FACILITY_TIME_ZONE",
    "OLPN_STATUS_DESCRIPTION", "ORDER_TYPE", "CARRIER_ID", "SHIP_VIA_ID",
    "MODE_ID", "CONTAINER_SIZE_ID", "CONTAINER_TYPE_ID",
    "EXT_ICE_QUANTITY", "EXT_OLPN_TEMPERATURE",
    "ESTIMATED_VOLUME", "ESTIMATED_WEIGHT",
    "CLIMATE_CONTROL_ID", "HAZARDOUS_MATERIAL",
    "ITEM_DESCRIPTION", "EXT_DISTRIBUTION_GROUP", "RFID",
    "CUSTOMER_ID", "DESTINATION_ADDRESS_FIRSTNAME",
    "DESTINATION_ADDRESS_CITY", "DESTINATION_ADDRESS_STATE",
    "DESTINATION_ADDRESS_COUNTRY",
    "CUSTOMER_AFFILIATE", "DOMESTIC_INTERNATIONAL",
]

INBOUND_COLUMNS = [
    "RECEIPT_ID", "ILPN_ID", "ASN_ID", "PURCHASE_ORDER_ID",
    "ORG_ID", "FACILITY_ID", "ITEM_ID", "BATCH_NUMBER",
    "SOURCE_SYSTEM",
    "PRODUCT_LINE", "PRODUCT_CLASS_RAW", "ITEM_ATTRIBUTE1_RAW",
    "QUANTITY",
    "RECEIPT_TS_LOCAL", "RECEIPT_DATE",
    "ILPN_STATUS_DESCRIPTION", "EXPIRY_DATE", "VENDOR_ID",
    "ITEM_DESCRIPTION", "EXT_DISTRIBUTION_GROUP",
]

ITEM_COLUMNS = [
    "ITEM_ID", "ITEM_DESCRIPTION", "PRODUCT_CLASS", "ITEM_ATTRIBUTE1",
    "PRODUCT_LINE", "EXT_DISTRIBUTION_GROUP", "CLIMATE_CONTROL_ID",
    "KITS_PER_BOX", "BOXES_PER_PALLET",
]

CUSTOMER_COLUMNS = [
    "CUSTOMER_ID", "CUSTOMER_NAME", "DESTINATION_ADDRESS_CITY",
    "DESTINATION_ADDRESS_STATE", "DESTINATION_ADDRESS_COUNTRY",
    "CUSTOMER_AFFILIATE", "DOMESTIC_INTERNATIONAL",
]


# ---------------------------------------------------------------------------
# Reference data
# ---------------------------------------------------------------------------

def build_items(rng, n_reagents=180, n_isp=120):
    """Item master. product_class / ITEM_ATTRIBUTE1 follow the inherited rule
    so the classification CASE can be exercised, including the cases where it
    fails and has to fall through to UNCLASSIFIED."""
    items = []
    for i in range(n_reagents):
        items.append({
            "ITEM_ID": f"R{100000 + i}",
            "ITEM_DESCRIPTION": f"REAGENT KIT {i:04d}",
            "PRODUCT_CLASS": "Z1" + rng.choice(["A", "B", "C"]),
            "ITEM_ATTRIBUTE1": rng.choice(["1021", "204"]),
            "PRODUCT_LINE": "REAGENTS",
            "EXT_DISTRIBUTION_GROUP": rng.choice(DIST_GROUPS),
            "CLIMATE_CONTROL_ID": rng.choice(["REFRIGERATED", "FROZEN", "AMBIENT"]),
            "KITS_PER_BOX": rng.choice([4, 6, 12, 20, 24]),
            "BOXES_PER_PALLET": rng.choice([12, 16, 18, 24, 30]),
        })
    for i in range(n_isp):
        items.append({
            "ITEM_ID": f"S{200000 + i}",
            "ITEM_DESCRIPTION": f"SPARE PART {i:04d}",
            "PRODUCT_CLASS": rng.choice(["P2", "P3", "M4"]),
            "ITEM_ATTRIBUTE1": "204",
            "PRODUCT_LINE": "ISP",
            "EXT_DISTRIBUTION_GROUP": rng.choice(DIST_GROUPS),
            "CLIMATE_CONTROL_ID": "AMBIENT",
            "KITS_PER_BOX": rng.choice([1, 2, 5, 10]),
            "BOXES_PER_PALLET": rng.choice([8, 10, 20, 40]),
        })
    # EDGE CASE: items the classification rule cannot resolve. These are what
    # should land in UNCLASSIFIED. If they do not, the CASE is wrong.
    for i in range(int(len(items) * P_UNCLASSIFIED) + 3):
        items.append({
            "ITEM_ID": f"X{300000 + i}",
            "ITEM_DESCRIPTION": f"UNMAPPED ITEM {i:04d}",
            "PRODUCT_CLASS": rng.choice(["", "Q9", "Z1"]),
            "ITEM_ATTRIBUTE1": rng.choice(["", "999", "1021"]),
            "PRODUCT_LINE": "UNCLASSIFIED",
            "EXT_DISTRIBUTION_GROUP": "",
            "CLIMATE_CONTROL_ID": "AMBIENT",
            "KITS_PER_BOX": 1,
            "BOXES_PER_PALLET": 20,
        })
    return items


def build_customers(rng, n=140):
    customers = []
    for i in range(n):
        affiliate = rng.random() < 0.30
        domestic = rng.random() < 0.72
        city, state, country = rng.choice(US_CITIES if domestic else INTL_CITIES)
        name = (f"ABBOTT {city} {i:03d}" if affiliate else f"CUSTOMER {i:03d} LABS")
        customers.append({
            "CUSTOMER_ID": f"C{50000 + i}",
            "CUSTOMER_NAME": name,
            "DESTINATION_ADDRESS_CITY": city,
            "DESTINATION_ADDRESS_STATE": state,
            "DESTINATION_ADDRESS_COUNTRY": country,
            "CUSTOMER_AFFILIATE": "Affiliate" if name.startswith("ABBOTT") else "Customer",
            "DOMESTIC_INTERNATIONAL": "Domestic" if country == "US" else "International",
        })
    return customers


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def classify(product_class, item_attribute1):
    """Mirrors the repaired CASE in the outbound query exactly. Kept in one
    place here for the same reason it lives in one place there."""
    if not product_class or not item_attribute1:
        return "UNCLASSIFIED"
    pc2 = product_class[:2]
    if pc2 == "Z1" and item_attribute1 in ("1021", "204"):
        return "REAGENTS"
    if pc2 != "Z1" and item_attribute1 == "204":
        return "ISP"
    return "UNCLASSIFIED"


def source_system(product_line, day):
    """Below the cutover, legacy. At or after it, the current WMS.
    Exactly one system owns any given row."""
    if product_line == "ISP":
        return "MAWM" if day >= CUTOVER["ISP"] else "ADMS"
    if product_line == "REAGENTS":
        return "MAWM" if day >= CUTOVER["REAGENTS"] else "DFCS"
    return "MAWM" if day >= CUTOVER["REAGENTS"] else "DFCS"


def day_volume_factor(rng, day):
    """Weekday pattern plus mild seasonality plus noise, so trends look real
    enough that a broken trend is visible by eye."""
    if day.weekday() == 6:
        return 0.0
    if day.weekday() == 5:
        base = 0.25
    else:
        base = 1.0
    seasonal = 1.0 + 0.18 * ((day.month - 6) / 6.0)
    growth = 1.0 + 0.10 * ((day - START_DATE).days / 365.0)
    return base * seasonal * growth * rng.uniform(0.82, 1.18)


def daterange(a, b):
    d = a
    while d <= b:
        yield d
        d += dt.timedelta(days=1)


# ---------------------------------------------------------------------------
# Fact generation
# ---------------------------------------------------------------------------

def generate_outbound(rng, items, customers):
    rows = []
    olpn_seq, order_seq = 0, 0

    for day in daterange(START_DATE, END_DATE):
        factor = day_volume_factor(rng, day)
        n_lpns = int(OUTBOUND_LPNS_PER_DAY * factor)
        for _ in range(n_lpns):
            olpn_seq += 1
            order_seq += 1
            olpn_id = f"OL{olpn_seq:09d}"
            order_id = f"OR{order_seq:09d}"
            cust = rng.choice(customers)

            # EDGE CASE: most oLPNs are one line, a large minority are not.
            # This is what makes COUNTROWS wrong and DISTINCTCOUNT right.
            n_lines = rng.choice([2, 3]) if rng.random() < P_MULTILINE else 1

            hour = rng.randint(6, 19)
            ts_local = dt.datetime(day.year, day.month, day.day,
                                   hour, rng.randint(0, 59), rng.randint(0, 59))
            ts_utc = ts_local + dt.timedelta(hours=5)

            status = rng.choice(STATUSES_SHIPPED)
            container = rng.choice(CONTAINERS)
            climate = rng.choice(CLIMATES)

            for line_no in range(1, n_lines + 1):
                item = rng.choice(items)
                product_line = classify(item["PRODUCT_CLASS"], item["ITEM_ATTRIBUTE1"])

                # EDGE CASE: item missing from the master. The LEFT JOIN keeps
                # the shipment; the attributes come through blank.
                orphan = rng.random() < P_ORPHAN_ITEM
                if orphan:
                    item_id = f"Z{999000 + rng.randint(0, 400)}"
                    item_desc, dist_group, pc_raw, attr_raw = "", "", "", ""
                    product_line = "UNCLASSIFIED"
                else:
                    item_id = item["ITEM_ID"]
                    item_desc = item["ITEM_DESCRIPTION"]
                    dist_group = item["EXT_DISTRIBUTION_GROUP"]
                    pc_raw = item["PRODUCT_CLASS"]
                    attr_raw = item["ITEM_ATTRIBUTE1"]

                batch = "" if rng.random() < P_NULL_BATCH else f"B{rng.randint(10000, 99999)}"

                rows.append({
                    "OLPN_ID": olpn_id,
                    "ORDER_LINE_ID": f"{order_id}-{line_no:03d}",
                    "ORDER_ID": order_id,
                    "ORG_ID": ORG_ID,
                    "FACILITY_ID": FACILITY_ID,
                    "ITEM_ID": item_id,
                    "BATCH_NUMBER": batch,
                    "SOURCE_SYSTEM": source_system(product_line, day),
                    "PRODUCT_LINE": product_line,
                    "PRODUCT_CLASS_RAW": pc_raw,
                    "ITEM_ATTRIBUTE1_RAW": attr_raw,
                    "QUANTITY": rng.randint(1, 60),
                    "SHIPPED_TS_LOCAL": ts_local.isoformat(sep=" "),
                    "SHIP_DATE": day.isoformat(),
                    "SHIPPED_TS_UTC": ts_utc.isoformat(sep=" "),
                    "FACILITY_TIME_ZONE": FACILITY_TIMEZONE,
                    "OLPN_STATUS_DESCRIPTION": status,
                    "ORDER_TYPE": rng.choices(ORDER_TYPES, weights=[80, 10, 6, 4])[0],
                    "CARRIER_ID": rng.choice(CARRIERS),
                    "SHIP_VIA_ID": rng.choice(SHIP_VIAS),
                    "MODE_ID": rng.choice(MODES),
                    "CONTAINER_SIZE_ID": container,
                    "CONTAINER_TYPE_ID": container.split("-")[0],
                    "EXT_ICE_QUANTITY": rng.choice([0, 0, 0, 2, 4, 6]),
                    "EXT_OLPN_TEMPERATURE": climate,
                    "ESTIMATED_VOLUME": round(rng.uniform(0.2, 3.5), 3),
                    "ESTIMATED_WEIGHT": round(rng.uniform(0.5, 28.0), 2),
                    "CLIMATE_CONTROL_ID": climate,
                    "HAZARDOUS_MATERIAL": rng.choices(["Y", "N"], weights=[7, 93])[0],
                    "ITEM_DESCRIPTION": item_desc,
                    "EXT_DISTRIBUTION_GROUP": dist_group,
                    "RFID": rng.choices(["Yes", "No", ""], weights=[25, 70, 5])[0],
                    "CUSTOMER_ID": cust["CUSTOMER_ID"],
                    "DESTINATION_ADDRESS_FIRSTNAME": cust["CUSTOMER_NAME"],
                    "DESTINATION_ADDRESS_CITY": cust["DESTINATION_ADDRESS_CITY"],
                    "DESTINATION_ADDRESS_STATE": cust["DESTINATION_ADDRESS_STATE"],
                    "DESTINATION_ADDRESS_COUNTRY": cust["DESTINATION_ADDRESS_COUNTRY"],
                    "CUSTOMER_AFFILIATE": cust["CUSTOMER_AFFILIATE"],
                    "DOMESTIC_INTERNATIONAL": cust["DOMESTIC_INTERNATIONAL"],
                })
    return rows


def generate_inbound(rng, items):
    rows = []
    receipt_seq, asn_seq, po_seq, ilpn_seq = 0, 0, 0, 0

    for day in daterange(START_DATE, END_DATE):
        factor = day_volume_factor(rng, day)
        n_receipts = int(INBOUND_RECEIPTS_PER_DAY * factor)
        for _ in range(n_receipts):
            receipt_seq += 1
            asn_seq += 1
            po_seq += 1
            asn_id = f"ASN{asn_seq:08d}"
            po_id = f"PO{po_seq:08d}"
            vendor = f"V{rng.randint(1000, 1080)}"

            n_lines = rng.choice([1, 1, 2, 3])
            hour = rng.randint(5, 16)
            ts_local = dt.datetime(day.year, day.month, day.day,
                                   hour, rng.randint(0, 59), rng.randint(0, 59))

            for _ in range(n_lines):
                ilpn_seq += 1
                item = rng.choice(items)
                product_line = classify(item["PRODUCT_CLASS"], item["ITEM_ATTRIBUTE1"])
                orphan = rng.random() < P_ORPHAN_ITEM
                if orphan:
                    item_id = f"Z{999000 + rng.randint(0, 400)}"
                    item_desc, dist_group, pc_raw, attr_raw = "", "", "", ""
                    product_line = "UNCLASSIFIED"
                else:
                    item_id = item["ITEM_ID"]
                    item_desc = item["ITEM_DESCRIPTION"]
                    dist_group = item["EXT_DISTRIBUTION_GROUP"]
                    pc_raw = item["PRODUCT_CLASS"]
                    attr_raw = item["ITEM_ATTRIBUTE1"]

                expiry = day + dt.timedelta(days=rng.randint(180, 900))
                rows.append({
                    "RECEIPT_ID": f"RC{receipt_seq:09d}",
                    "ILPN_ID": f"IL{ilpn_seq:09d}",
                    "ASN_ID": asn_id,
                    "PURCHASE_ORDER_ID": po_id,
                    "ORG_ID": ORG_ID,
                    "FACILITY_ID": FACILITY_ID,
                    "ITEM_ID": item_id,
                    "BATCH_NUMBER": "" if rng.random() < P_NULL_BATCH
                                    else f"B{rng.randint(10000, 99999)}",
                    "SOURCE_SYSTEM": source_system(product_line, day),
                    "PRODUCT_LINE": product_line,
                    "PRODUCT_CLASS_RAW": pc_raw,
                    "ITEM_ATTRIBUTE1_RAW": attr_raw,
                    "QUANTITY": rng.randint(5, 400),
                    "RECEIPT_TS_LOCAL": ts_local.isoformat(sep=" "),
                    "RECEIPT_DATE": day.isoformat(),
                    "ILPN_STATUS_DESCRIPTION": rng.choice(STATUSES_RECEIVED),
                    "EXPIRY_DATE": expiry.isoformat(),
                    "VENDOR_ID": vendor,
                    "ITEM_DESCRIPTION": item_desc,
                    "EXT_DISTRIBUTION_GROUP": dist_group,
                })
    return rows


# ---------------------------------------------------------------------------

def write_csv(path, columns, rows):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="./data", help="output directory")
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    rng = random.Random(args.seed)

    items = build_items(rng)
    customers = build_customers(rng)
    outbound = generate_outbound(rng, items, customers)
    inbound = generate_inbound(rng, items)

    n1 = write_csv(os.path.join(args.out, "fact_outbound.csv"), OUTBOUND_COLUMNS, outbound)
    n2 = write_csv(os.path.join(args.out, "fact_inbound.csv"), INBOUND_COLUMNS, inbound)
    n3 = write_csv(os.path.join(args.out, "dim_item.csv"), ITEM_COLUMNS, items)
    n4 = write_csv(os.path.join(args.out, "dim_customer.csv"), CUSTOMER_COLUMNS, customers)

    # ---- the same checks you will run against real data (Step 11) ----------
    key = lambda r: "|".join([r["OLPN_ID"], r["ORDER_LINE_ID"], r["ORDER_ID"],
                              r["ORG_ID"], r["FACILITY_ID"], r["ITEM_ID"],
                              r["BATCH_NUMBER"]])
    rows_ob, keys_ob = len(outbound), len({key(r) for r in outbound})
    distinct_olpn = len({r["OLPN_ID"] for r in outbound})
    unclassified = sum(1 for r in outbound if r["PRODUCT_LINE"] == "UNCLASSIFIED")

    print(f"fact_outbound.csv  {n1:>8,} rows")
    print(f"fact_inbound.csv   {n2:>8,} rows")
    print(f"dim_item.csv       {n3:>8,} rows")
    print(f"dim_customer.csv   {n4:>8,} rows")
    print()
    print("--- grain proof (Step 11) ---")
    print(f"  rows                {rows_ob:>8,}")
    print(f"  distinct grain keys {keys_ob:>8,}   {'PASS' if rows_ob == keys_ob else 'FAIL'}")
    print()
    print("--- the COUNTROWS trap ---")
    print(f"  COUNTROWS would report      {rows_ob:>8,} oLPNs")
    print(f"  DISTINCTCOUNT reports       {distinct_olpn:>8,} oLPNs")
    print(f"  inflation if you get it wrong  {rows_ob / distinct_olpn:>8.2f}x")
    print()
    print("--- data quality ---")
    print(f"  UNCLASSIFIED rows   {unclassified:>8,}  ({unclassified / rows_ob:.2%})")
    for pl in ("REAGENTS", "ISP", "UNCLASSIFIED"):
        srcs = sorted({r["SOURCE_SYSTEM"] for r in outbound if r["PRODUCT_LINE"] == pl})
        print(f"  {pl:<14} sources: {', '.join(srcs)}")


if __name__ == "__main__":
    main()
