# Fulton County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_FUL_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PASS with minor items

---

## 1. Supplemental T5 — Springfield Township Park (1 new site, S-0038)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-FUL-S-0038 | Springfield Township Park | 12 | Springfield Twp | 41.506024, -84.412247 |

Confirmed Fulton County via centroid + township lookup (Springfield Township exists in Fulton County).

---

## 2. Trail Parents Added (2 entries)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-FUL-T-0016 Beach Ridge Singletrack Trail | OH-MC-S-0025 Oak Openings Beach Ridge Area | Trail runs through multi-county Oak Openings preserve complex |
| OH-FUL-T-0017 Chessie Circle Trail | OH-FUL-S-0002 Harrison Lake State Park | Trail within Harrison Lake SP |

---

## 3. AP-0001 Added to held_entities

**OH-FUL-AP-0001** (Wabash Cannonball Trail — CR 23 Trailhead) had null GPS in the DB and was not in held_entities. Added with `hold_reason = gps_missing`. Acquire coordinates from OSM, county GIS, or field verification at County Road 23 intersection.

---

## 4. Williams County Bbox Bleed (1 entity excluded)

West Unity Memorial Park (11ac, PAD-US) — township lookup: Brady Township = Williams County. West Unity, Ohio is in Williams County, not Fulton. Not a Fulton gap. MRQ-flagged for Williams County T6 supplemental discovery.

---

## 5. MRQ Entries (2 total)

1. `WILLIAMS-WEST-UNITY-MEM-PARK` — West Unity Memorial Park, stage for Williams County T6
2. `OH-FUL-S-0022` — Delta Park acreage discrepancy (DB=23ac vs alt source=37ac), verify against Fulton County parcel data

---

## 6. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites | 35 | 36 |
| Trails | 7 | 7 |
| Trail parents | 4 | 6 |
| Access Points | 1 | 1 (AP-0001 now in held_entities) |

---

## 7. Open Items

- OH-FUL-AP-0001: GPS acquisition needed; currently held (gps_missing)
- Delta Park (S-0022): acreage discrepancy 23 vs 37ac — verify
- West Unity Memorial Park: stage for Williams County T6 run
