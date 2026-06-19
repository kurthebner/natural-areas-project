# Hardin County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 108 active | OH-HAR-S-0001–0111 (gaps at 0002, 0003, 0029 — all held) |
| Trailthings | 5 | OH-HAR-TT-0001 through 0005 |
| Site Networks | 1 | OH-HAR-SN-0001 City of Kenton Parks & Recreation |
| Access Points | 6 active | OH-HAR-AP-0001/0004/0005/0006/0007/0008 |
| Held Entities | 30 | 2 cross_county_held sites + 2 parent_held APs + 1 identity_uncertain + 24 unconfirmed_baseline_seeds + 1 cross_county_held AP-related |

**Run metadata:** `hardin_ohio_2026_06_01` — input=144, normalized=120, held=33

Notes: "108 Sites, 5 Trailthings, 1 Site Networks, 6 APs. 33 held entities. 52 cemetery GPS coordinates resolved via OSM/Nominatim/human-assist. 34 cemeteries gps_unresolvable pending GNIS acquisition."

Note: Held count in run_metadata is 33; current held_entities count is 30. Three entities resolved since run date.

---

## 2. FK Integrity — Fixes Applied This Session

All FK padding errors stem from the same v5 pipeline 3-digit non-padded ID format. Hardin is the first v6 county run in this review series, and it shares the bug — the upsert script used 3-digit IDs in all FK fields.

### Access Points (6 fixes)

| AP | Old | New |
|---|---|---|
| OH-HAR-AP-0001 (Lawrence Woods SNP Entrance) | OH-HAR-S-001 | OH-HAR-S-0001 |
| OH-HAR-AP-0004 (Veterans Memorial Park Entrance) | OH-HAR-S-004 | OH-HAR-S-0004 |
| OH-HAR-AP-0005 (Silver Creek Center Entrance) | OH-HAR-S-006 | OH-HAR-S-0006 |
| OH-HAR-AP-0006 (Saulisberry Park Entrance) | OH-HAR-S-030 | OH-HAR-S-0030 |
| OH-HAR-AP-0007 (Home Run Memorial Park Entrance) | OH-HAR-S-033 | OH-HAR-S-0033 |
| OH-HAR-AP-0008 (Ada War Memorial Park Entrance) | OH-HAR-S-037 | OH-HAR-S-0037 |

### Trailthings — site_parent_id (4 fixes)

| Trailthing | Old | New |
|---|---|---|
| OH-HAR-TT-0001 Lawrence Woods Boardwalk | OH-HAR-S-001 | OH-HAR-S-0001 |
| OH-HAR-TT-0002 Veterans Memorial Park Walking Path | OH-HAR-S-004 | OH-HAR-S-0004 |
| OH-HAR-TT-0003 Silver Creek Paved Trail | OH-HAR-S-006 | OH-HAR-S-0006 |
| OH-HAR-TT-0004 Ada Railroad Park Path | OH-HAR-S-038 | OH-HAR-S-0038 |

### Site Network — member_site_ids (1 fix)

OH-HAR-SN-0001 member_site_ids: all 6 member IDs were 3-digit non-padded.

Old: `OH-HAR-S-030;OH-HAR-S-032;OH-HAR-S-033;OH-HAR-S-034;OH-HAR-S-035;OH-HAR-S-036`
New: `OH-HAR-S-0030;OH-HAR-S-0032;OH-HAR-S-0033;OH-HAR-S-0034;OH-HAR-S-0035;OH-HAR-S-0036`

All 6 members verified against sites table: ✓

All fixes verified post-update.

---

## 3. Remaining FK Issue

**OH-HAR-TT-0005 "ONU Green Monster Trail" — NULL site_parent_id.**

The Green Monster Trail is on the Ohio Northern University campus in Ada, OH. No ONU campus site entity exists in the DB. The site_parent cannot be assigned until an ONU campus site is discovered and upserted.

Batch action: T6 supplemental discovery for Ohio Northern University campus as a site; then add site_parent_id on TT-0005.

---

## 4. GPS Status — GPS Gate Bypass (IMP-026)

**45 of 108 active sites have NULL GPS.** None are in held_entities with hold_reason=gps_missing. Per Stage 4c protocol, sites without GPS and without gps_unresolvable=true must route to held_entities. These 45 sites were upserted directly to the sites table, bypassing the GPS gate.

**Breakdown by category:**

| Category | Count | Sites |
|---|---|---|
| Cemetery | 34 | See §4a |
| Park | 4 | Gormley Park (S-0039), Dunkirk Community Park (S-0041), Mount Victory Village Park (S-0043), Murray Park (S-0036) |
| Recreation Facility | 2 | Home Run Memorial Park (S-0033), Ranger Sports Complex (S-0040) |
| Memorial | 2 | Gene Autry Park (S-0034), Ray Brown Memorial Park (S-0044) |
| Historic Site | 3 | Ada Railroad Park (S-0038), Indian Burial Grounds Buck Twp (S-0059), Indian Burial Grounds McDonald Twp (S-0092) |

### 4a — Cemetery GPS (34 sites)

Per run_metadata: "34 cemeteries gps_unresolvable pending GNIS acquisition." These were recorded as gps_unresolvable in the discovery YAML but the DB has no gps_unresolvable column — they were upserted with NULL GPS and no hold. The intended behavior was to flag them for GNIS-based GPS acquisition.

Batch action: run GNIS GPS acquisition (`utilities/na_gnis_query.py`) for the 34 cemetery IDs; populate gps_lat/gps_lon where found; sites that cannot be resolved via GNIS move to held_entities with hold_reason=gps_missing.

### 4b — Non-cemetery GPS-missing sites (11 sites)

These are parks, recreation facilities, memorials, and historic sites that should either have had GPS acquired during Stage 4b or been routed to held_entities. They are in the active sites table without GPS, which violates Stage 4c protocol.

Batch action: GPS acquisition for all 11 from web/GNIS sources; move to held_entities if not resolvable.

**Additional GPS concern — shared low-precision coordinates:**

Three sites share GPS 40.647, -83.6095 (Hardin County centroid approximation):
- OH-HAR-S-0004 Hardin County Veterans Memorial Park
- OH-HAR-S-0005 Boy Scout Lake
- OH-HAR-S-0045 Memorial Park Golf Club

These are in Kenton, OH. Precision GPS needed for all three.

---

## 5. Held Entities

### 5a — Cross-county held (Wyandot primary)

| Record ID | Name | Hold Reason |
|---|---|---|
| OH-HAR-S-0002 | Lawrence Woods Wildlife Area | cross_county_held (Wyandot primary) |
| OH-HAR-S-0003 | Andreoff Wildlife Area | cross_county_held (Wyandot primary) |
| OH-HAR-AP-0002 | Andreoff WA North Tract Access | parent_held (parent = S-0003) |
| OH-HAR-AP-0003 | Andreoff WA South Tract Access | parent_held (parent = S-0003) |

All four holds valid. Will resolve when Wyandot County pipeline runs.

### 5b — Identity uncertain

OH-HAR-S-0029 "Roundhead Community Park (name unconfirmed)" — held pending name and location confirmation. Village of Roundhead, Hardin County. Batch action: T6 supplemental research to confirm park name and GPS.

### 5c — 24 unconfirmed_baseline_seeds (S-0112 through S-0136)

A large block of speculative entities seeded during discovery — corridor features, marsh remnants, buffer parcels, and planned infrastructure. Examples: AEP Transmission Corridor, Ada Reservoir Woodlot Buffer, Blanchard River Corridor, Hog Creek Corridor, Scioto Marsh complex (8 entries), planned trail extensions.

Several of these (particularly the Scioto Marsh entries and river corridors) may not qualify as discrete sites under v6 entity rules — they may be habitat descriptions or GIS features rather than managed public access areas. Requires review against the site qualification criteria before any can be released.

Batch action: review each against v6 site qualification rules; release those confirmed as in-scope public sites with GPS; delete those that are habitat features or unconfirmed planning-stage entities.

---

## 6. PAD-US Spatial Audit

**Bbox:** Hardin County bounding box. 16 PAD-US fee records in bbox; 7 matched (≥80); 6 unmatched; 3 skipped.

### 6a. Skipped — note

"Lawrence Woods Dedicated Nature Preserve" (closed access) skipped — entity IS in DB as OH-HAR-S-0001. The closed-access PAD-US record refers to the restricted interior areas; the main preserve is open. Not a gap.

### 6b. Matched — acreage notes

| PAD-US Record | PAD-US Acres | DB Entity | Note |
|---|---|---|---|
| Saulisberry Park | 169 | OH-HAR-S-0030 | DB acres: NULL — populate |
| Lawrence Woods SNP | 24 | OH-HAR-S-0001 | PAD-US fee parcel only; full preserve likely larger |
| Gormley Park | 16 | OH-HAR-S-0039 | DB acres: NULL — populate |
| Dunkirk Park | 6 | OH-HAR-S-0041 | DB acres: NULL — populate |
| C.E. Wharton Memorial Park | 19 | OH-HAR-S-0032 | DB acres: NULL — populate |

### 6c. Genuine Hardin County gaps

**T2 — State / ODNR:**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Killdeer Plains Wildlife Area | 8,581 | 2 | **Bbox false positive — Wyandot County.** Centroid 40.709°N, -83.321°W; polygon southern edge at 40.690°N clips Hardin's bbox. Entity is in Wyandot County (Crane Township); flag for Wyandot County run. |
| Wildlife Production Area 32 | 47 | 2 | ODNR; not in DB; confirm county before cataloging |
| Wildlife Production Area 43 | 40 | 2 | ODNR; not in DB; confirm county before cataloging |

**T4 — County / Regional:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Marion Tallgrass Trail | 30 | County | Rail trail corridor connecting Kenton to Marion County; not in DB; likely Trailthing entity (rail trail) with associated corridor parcel as site |

**T6 — Municipal:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Ball Park | 6 | City | Small city ballfield; not in DB |
| Glendale Skate Park | 1 | City | Not in DB |

---

## 7. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | 6 AP FK padding errors | FIXED | Applied this session |
| 2 | 4 Trailthing site_parent_id padding errors | FIXED | Applied this session |
| 3 | SN-0001 member_site_ids padding errors (6 IDs) | FIXED | Applied this session |
| 4 | GPS gate bypass: 45 active sites with NULL GPS | HIGH | IMP-026; batch GNIS acquisition for cemeteries; GPS acquisition + possible held for 11 non-cemeteries |
| 5 | TT-0005 NULL site_parent (ONU campus not in DB) | MEDIUM | T6 supplemental: ONU campus site; then add TT-0005 parent |
| 6 | WPA 32 (47ac) and WPA 43 (40ac) not cataloged | MEDIUM | Supplemental T2 discovery; confirm Hardin County before cataloging |
| 7 | Marion Tallgrass Trail corridor (30ac) not cataloged | MEDIUM | Supplemental T4/Trailthing discovery |
| 8 | 3 sites sharing centroid GPS 40.647, -83.6095 | MEDIUM | Precision GPS acquisition |
| 9 | 24 unconfirmed_baseline_seed held entities (S-0112–0136) | MEDIUM | Review each against site qualification rules; release or delete |
| 10 | OH-HAR-S-0029 Roundhead Community Park: identity_uncertain | MEDIUM | T6 supplemental research; confirm name and GPS |
| 11 | Ball Park (6ac) and Glendale Skate Park (1ac) not cataloged | MEDIUM | Supplemental T6 discovery |
| 12 | Killdeer Plains WA (8,581ac) — bbox false positive, Wyandot County | NOTE | Flag for Wyandot County run; not a Hardin gap |
| 13 | Lawrence Woods WA and Andreoff WA held (Wyandot primary) | PENDING | Resolves at Wyandot County run |
| 14 | NULL acreage on multiple matched sites | LOW | Batch: populate from PAD-US values |

---

## 8. Batch Phase Actions

- [ ] GNIS GPS acquisition for 34 cemetery sites; populate gps_lat/gps_lon; move unresolvable to held_entities
- [ ] GPS acquisition for 11 non-cemetery GPS-missing sites; move unresolvable to held_entities
- [ ] Precision GPS for S-0004 (Veterans Memorial Park), S-0005 (Boy Scout Lake), S-0045 (Memorial Park Golf Club) — all share centroid coordinate
- [ ] Supplemental T2 discovery: WPA 32 (47ac), WPA 43 (40ac) — confirm Hardin County before cataloging
- [ ] Supplemental T4/TT discovery: Marion Tallgrass Trail (30ac rail trail corridor)
- [ ] T6 supplemental: ONU campus site (for TT-0005 parent); Ball Park; Glendale Skate Park; Roundhead Community Park (confirm S-0029 identity)
- [ ] Review 24 unconfirmed_baseline_seed held entities (S-0112–0136) against site qualification rules
- [ ] Populate NULL acreages from PAD-US: Saulisberry Park (169ac), Gormley Park (16ac), Dunkirk Community Park (6ac), C.E. Wharton Memorial Park (19ac)
- [ ] Flag Hardin upsert script for IMP-026 remediation: GPS gate must enforce held routing before upsert
- [ ] Note for Wyandot County run: Killdeer Plains Wildlife Area (8,581ac, GAP2) — confirmed bbox bleed; catalog as T2 ODNR entity in Wyandot run
