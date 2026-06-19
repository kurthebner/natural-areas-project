# Franklin County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_FRA_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PASS with supplemental work
**Script:** `outputs/batch_fra.py`

---

## 1. Site Network Membership Corrections (3 changes)

| Action | Site | SN | Reason |
|--------|------|----|--------|
| REMOVE | OH-FR-S-0825 Cross Creek Park | OH-FR-SN-0003 Columbus R&P | Site is Hilliard-governed; Columbus SN membership was systemic pipeline artifact |
| REMOVE | OH-FR-S-0797 First Responders Park | OH-FR-SN-0008 Hilliard R&P | Site is Westerville-governed; wrong network assignment |
| ADD | OH-FR-S-0797 First Responders Park | OH-FR-SN-0015 Westerville Parks & Rec | Correct network for Westerville-governed site |

Post-change counts:
- OH-FR-SN-0003 Columbus R&P: 548 → 547 members
- OH-FR-SN-0008 Hilliard R&P: 31 → 30 members
- OH-FR-SN-0015 Westerville Parks & Rec: 29 → 30 members

---

## 2. Supplemental Sites (7 new, S-1182–S-1188)

All confirmed Franklin County (FIPS 049) via TIGER/Line 2024 spatial audit. GPS from PAD-US 4.0 GDB centroids.

| Site ID | Name | Acres | Governance | GPS | MCD | GAP |
|---------|------|-------|------------|-----|-----|-----|
| OH-FR-S-1182 | River Bluffs | 45 | Columbus R&P | 40.1356, -83.0343 | Columbus | 4 |
| OH-FR-S-1183 | Darby Creek Conservation Area | 105 | Columbus R&P | 39.9526, -83.2379 | Prairie Twp | 2 |
| OH-FR-S-1184 | Glen Echo Ravine Restoration & Protection Area | 10 | Columbus R&P | 40.0194, -83.0004 | Columbus | 2 |
| OH-FR-S-1185 | Brandon Open Space | 15 | City of Dublin, Recreation Services Department | 40.1236, -83.1376 | Washington Twp | 2 |
| OH-FR-S-1186 | Hawks Nest Open Space | 15 | City of Dublin, Recreation Services Department | 40.1271, -83.1518 | Washington Twp | 2 |
| OH-FR-S-1187 | Riverside Woods Open Space | 21 | City of Dublin, Recreation Services Department | 40.1188, -83.1058 | Washington Twp | 2 |
| OH-FR-S-1188 | Woerner-Temple Open Space | 5 | City of Dublin, Recreation Services Department | 40.0853, -83.1513 | Washington Twp | 2 |

### PAD-US Consolidation Notes

**Dublin open spaces** — PAD-US stages each lettered parcel separately. Consolidated by named group:
- Brandon Open Space: A (6ac) + B (9ac) → 15ac; GPS = centroid of B (larger parcel)
- Hawks Nest Open Space: A (6ac) + D (2ac) + E (7ac) → 15ac; GPS = centroid of A
- Riverside Woods Open Space: A (2ac) + B (19ac) → 21ac; GPS = centroid of B
- Woerner-Temple Open Space: A (4ac) + B (0ac) + C (1ac) → 5ac; GPS = centroid of A

**Tartan West Open Space — NOT INSERTED:** All 17 PAD-US parcels (A–W, ~57ac combined, GAP2) confirmed as Union County (FIPS 159) via TIGER spatial audit. These are Dublin open spaces in Dublin's Union County portion. Bbox false positive. MRQ-flagged for Union County T6 discovery.

---

## 3. False Positive Resolved

**O'Shaughnessy Reservoir (1,279ac):** PAD-US record clips Franklin County bounding box but reservoir is Delaware County primary. Dam managed by City of Columbus Water. MRQ-flagged for Delaware County T2 discovery.

---

## 4. MRQ Entries (5 total)

| Record ID | Entity Type | Issue |
|-----------|-------------|-------|
| OH-FR-S-0047 | Site | Friendship Park possible duplicate vs OH-FR-S-1026 (Prairie Twp vs Gahanna, same 22.67ac, GPS 200m apart) |
| FRA-OSHAUGHNESSY-DEL | Site | O'Shaughnessy Reservoir — Delaware County primary; flag for Delaware T2 discovery |
| FRA-TARTANWEST-UNION | Site | Tartan West Open Space (17 parcels) — all Union County (FIPS 159); flag for Union County T6 discovery |
| OH-FR-S-1183 | Site | Darby Creek Conservation Area — governance verification needed (Columbus R&P vs TNC corridor vs other) |
| OH-FR-S-1184 | Site | Glen Echo Ravine — verify identity vs adjacent OH-FR-S-0180 Glen Echo Park (same lat, ~155m apart) |

---

## 5. Final Counts

| Entity Type | Before | After |
|-------------|--------|-------|
| Sites (FR) | 1,157 | 1,164 |
| Site Network memberships (SN-0003) | 548 | 547 |
| Site Network memberships (SN-0008) | 31 | 30 |
| Site Network memberships (SN-0015) | 29 | 30 |

---

## 6. Open Items Carried Forward

- Friendship Park duplicate resolution (S-0047 / S-1026): field verify or check Prairie Twp/Gahanna records
- Mifflin Township cemetery parcels (S-1077/1114/1115): co-named disambiguation via MORPC parcel data
- O'Shaughnessy Reservoir: stage for Delaware County T2 batch
- Tartan West Open Space: stage for Union County T6 batch
- Glen Echo Ravine (S-1184) identity vs S-0180: field verify adjacency
- Darby Creek Conservation Area (S-1183) governance: verify Columbus R&P vs TNC
- SN membership over-assignment (Columbus SN ~60 non-Columbus sites): systematic re-derivation deferred to next Franklin pipeline pass
