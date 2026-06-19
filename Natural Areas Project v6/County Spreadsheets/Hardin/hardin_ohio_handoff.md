# Hardin OH — Handoff Document (v6)
**RUN_ID:** `hardin_ohio_2026_06_01`
**PREFIX:** `OH-HAR`
**County:** Hardin, Ohio
**Session date:** 2026-06-01
**Status:** COMPLETE — UPSERTED 2026-06-02 | PAD-US SPOT-CHECK COMPLETE 2026-06-12 | MRQ 198 created | IMP-026 GPS ACQUISITION COMPLETE 2026-06-12 (2 sites GPS-missing; see Open Items)

---

## Supplemental Resolution — 2026-06-12

### PAD-US Spot-Check

PAD-US 4.0 Ohio fee layer cross-checked against Hardin DB (118 Sites, 0 Trails).

**Confirmed matches:**

| PAD-US Unit_Nm | GIS_Acres | DB Match | Notes |
|----------------|-----------|----------|-------|
| Lawrence Woods Dedicated Nature Preserve | 1036 | S-0001 (1034.93ac) | ✓ confirmed; 24ac addition parcel also appears separately in PAD-US |
| Saulisberry Park | 169 | S-0030 (167.4ac) | ✓ confirmed |
| C.E. Wharton Memorial Park | 19 | S-0032 | ✓ confirmed |
| Gormley Park | 16 | S-0039 | ✓ confirmed |
| Dunkirk Park | 6 | S-0041 | ✓ confirmed |

**Residuals → MRQ 198:**

| PAD-US Unit_Nm | GIS_Acres | d_Own_Name | Assessment |
|----------------|-----------|------------|------------|
| McGuffey Wildlife Preserve | 73 | Regional Agency Land | **HIGH PRIORITY** — not in DB; distinct from S-0042 McGuffey Village Park; research via SWCD or ODNR |
| Alger Park | 7 | City Land | Not in DB; possible second park in Alger distinct from S-0044 Ray Brown Memorial Park |
| Hardin Park | 3 | City Land | Not in DB as standalone; token-match with Veterans Memorial Park is coincidental; T6 gap in Kenton or other municipality |

**False positives:** Harding Memorial Park / Harding Ellis Park / Harding Park ×2 (Marion County — President Harding references); Hardin County Fairgrounds (event venue, not NAP).

---

## GPS Acquisition Summary — 2026-06-12 (IMP-026)

GNIS GPS acquisition run for all 26 Hardin cemetery sites with missing GPS. Result: 0 of 26 found in GNIS 2021 Ohio archive — these are small private/family cemeteries not cataloged. All 26 tagged in DB notes: "GPS: GNIS 2021 Ohio archive exhausted."

Glendale Skate Park (OH-HAR-S-0139): GPS acquired — 40.651835, -83.616422 (348 N Glendale St, Kenton; source: ohiobiz.com).

**Remaining GPS-missing (manual acquisition required):**

| Site ID | Name | Location |
|---------|------|----------|
| OH-HAR-S-0041 | Dunkirk Community Park | Dunkirk, OH — village website 404; no GPS found |
| OH-HAR-S-0138 | Ball Park | Kenton, OH — City of Kenton P&R; address not found in available web sources |

---

## County Context

- **County seat:** Kenton
- **Major municipalities:** Kenton (city), Ada (village), Forest (village), Dunkirk (village), McGuffey (village), Mount Victory (village), Ridgeway (village), Alger (village)
- **15 townships (from OTA roster):** Blanchard, Buck, Cessna, Dudley, Goshen, Hale, Jackson, Liberty, Lynn, Marion, McDonald, Pleasant, Roundhead, Taylor Creek, Washington
- **Known park districts:** None identified at bootstrap
- **Known multi-county entities:** None (bootstrap DB query clean)

---

## Tiers Completed

| Tier | Status | Entities | Notes |
|------|--------|----------|-------|
| T1 Federal & Tribal | COMPLETE | 0 Sites, 0 Trailthings, 0 SNs, 0 APs | Full null — no federal/tribal land in Hardin County; VA NCA null; no NHA |
| T2 State | COMPLETE | 3 Sites, 1 Trailthing, 0 SNs, 3 APs | Lawrence Woods SNP; Lawrence Woods WA (CC/Wyandot); Andreoff WA (CC/Wyandot) |
| T3 District | COMPLETE | 3 Sites, 2 Trailthings, 0 SNs, 2 APs | Veterans Memorial Park (T3 district!); Boy Scout Lake (child); Silver Creek Center (SWCD T3) |
| T4 County | COMPLETE | 0 Sites, 0 Trailthings, 0 SNs, 0 APs | Null — no county parks dept; Veterans Park is T3; Zimmerman Kame private land; Saulisberry/France Lake → T6 |
| T5 Township | COMPLETE | 23 Sites, 0 Trailthings, 0 SNs, 0 APs | 22 township cemeteries (10 twps confirmed); 1 unconfirmed Roundhead park; no parks in any of 15 townships |
| T6 Municipal | COMPLETE | 15 Sites, 1 Trailthing, 1 SN, 3 APs | Kenton (7 parks + France Lake child); Ada WM Park + Railroad Park; Forest (Gormley + Ranger); Ray Brown MP (Alger, new 2026); +4 village parks; SN PROVISIONAL Kenton Parks Dept |
| T7 Conservancy & Land Trust | COMPLETE | 0 Sites, 0 Trailthings, 0 SNs, 0 APs | Full null — WCOLC (ag easements only); TNC/BSC/NCOLC not applicable; ONAPA = ODNR preserves (T2); SKT planned extension unconfirmed |
| T8 Private | COMPLETE | 67 Sites, 1 Trailthing, 0 SNs, 0 APs | Memorial Park Golf Club (18-hole); ONU Green Monster Trail; 5 church cems; 2 Indian burial grounds; 59 family/private cems |
| T0 Baseline | PENDING | | |

---

## Tiers Remaining

- **T1 Federal & Tribal:** USFS (Hardin not in Wayne NF range), NPS, USFWS, VA NCA (mandatory §3.7), tribal, NHA check
- **T2 State:** ODNR — Lawrence Woods SNP and Wildlife Area confirmed in baseline; ODOT rest stops; public universities (ONU in Ada is T2)
- **T3 District:** Ohio Auditor pre-enumeration mandatory first step
- **T4 County:** Hardin County Veterans Memorial Park Board; county engineer; county auditor
- **T5 Township:** 15 townships from OTA roster
- **T6 Municipal:** Kenton, Ada, Forest, Dunkirk, McGuffey, Mount Victory, Ridgeway, Alger, plus any other villages
- **T7 Conservancy & Land Trust:** Known org inventory check; OALC, TNC, etc.
- **T8 Private:** Golf courses (GNIS enumeration); cemeteries

---

## Key Active Flags

- **IMP-017 validation run** — First v6 county. Note any inconsistencies in existing v5 DB data encountered during cross-county checks.
- No MC entities referencing Hardin found at bootstrap.

---

## Known Multi-County Entities

Bootstrap DB query result (2026-06-01): **No existing MC entities found for Hardin County.**

| Entity ID | Name | Type | Counties | Status |
|-----------|------|------|----------|--------|
| — | — | — | — | — |

---

## Baseline Seeds (internalized — not yet confirmed)

| Baseline Entry | Type in Baseline | Expected Tier | Notes |
|----------------|-----------------|---------------|-------|
| Lawrence Woods State Nature Preserve | State Nature Preserve | T2 | High confidence |
| Lawrence Woods Wildlife Area | State Wildlife Area | T2 | High confidence |
| Lawrence Woods Prairie Restoration | Prairie Restoration | T2 | Likely child site of SNP |
| Lawrence Woods Buffer Parcel | Natural Area Buffer | T2 | Low confidence — informal |
| Hardin County Veterans Memorial Park | County Park | T4 | High confidence |
| Boy Scout Lake | Reservoir | T4 | Likely child of Veterans Park |
| Hardin County Veterans Memorial Park Trail | Trail (→ Trailthing) | T4 | High confidence |
| C.E. Wharton Memorial Park | Municipal Park | T6 | Kenton |
| Pioneer Park | Municipal Park | T6 | Kenton |
| Saulisberry Park | Municipal Park | T6 | Kenton |
| Gormley Park | Village Park | T6 | Forest |
| Ranger Sports Complex | Sports Complex | T6 | Forest — scope check needed |
| Ada Memorial Park | Village Park | T6 | Ada |
| Ada Railroad Park | Village Park | T6 | Ada |
| Ada Railroad Park Path | Trail Spur (→ Trailthing) | T6 | Short paved path |
| Ada Trail Spur (Unmarked) | Trail Spur (→ Trailthing) | T6 | Informal; low confidence |
| Ada Reservoir | Reservoir | T6 | Ada; scope TBD |
| Dunkirk Community Park | Village Park | T6 | Dunkirk |
| McGuffey Village Park | Village Park | T6 | McGuffey |
| Mount Victory Park | Village Park | T6 | Mount Victory |
| Simon Kenton Trail (Planned Extension) | Trail (→ Trailthing) | T7/T8 | Planned only; low confidence |
| Kenton Greenbelt Parcel | Urban Edge | T6? | Unknown ownership; low confidence |
| Pleasant Township Green Parcel | Township Park | T5 | Informal; low confidence |
| Blanchard River Corridor | Riparian Corridor | T2/T7 | ODNR/private; likely not catalogable |
| Hog Creek Corridor | Riparian Corridor | T2/T7 | ODNR/private; likely not catalogable |
| Scioto River Corridor | Riparian Corridor | T2/T7 | ODNR/private; likely not catalogable |
| Scioto Marsh entries (×7) | Historical/drainage | — | Largely private/agricultural; scope very low |
| AEP Transmission Corridor — Ada Segment | Utility Corridor | — | Private easement; out of scope |
| Kenton Water Treatment Plant Buffer | Wellfield Buffer | T6 | Restricted; likely out of scope |
| Hog Creek Marsh (historical) | Historical Wetland | — | GNIS reference only; not accessible |
| McGuffey Reservoir | Reservoir | T6? | Unknown ownership; low confidence |
| Ada Reservoir Woodlot Buffer | Riparian Buffer | T6? | Informal; low confidence |
| Veterans Park North Buffer | Trailside Buffer | T4 | Informal; low confidence |

Trail-type baseline entries seeded as **Trailthings**: Ada Railroad Park Path, Ada Trail Spur (Unmarked), Hardin County Veterans Memorial Park Trail, Simon Kenton Trail (Planned Extension).

---

## Entities Discovered

*(Running table — all raw records pending pipeline)*

| Tier | Entity ID | Name | Type | Notes |
|------|-----------|------|------|-------|
| T2 | OH-HAR-S-001 (provisional) | Lawrence Woods State Nature Preserve | Site | 1034.93 ac; DNAP; eBird L324903 |
| T2 | OH-HAR-S-002 (provisional) | Lawrence Woods Wildlife Area | Site | DOW; CROSS_COUNTY_CANDIDATE Hardin+Wyandot; acres TBD |
| T2 | OH-HAR-S-003 (provisional) | Andreoff Wildlife Area | Site | DOW; CROSS_COUNTY_CANDIDATE Hardin+Wyandot; ~861 ac total |
| T2 | OH-HAR-TT-001 (provisional) | Lawrence Woods Boardwalk | Trailthing — accessible boardwalk | 1.1 mi; parent: Lawrence Woods SNP |
| T2 | OH-HAR-AP-001 (provisional) | Lawrence Woods SNP Entrance | Access Point | 13278 CR 190 |
| T2 | OH-HAR-AP-002 (provisional) | Andreoff WA North Tract Access | Access Point | CR 205 & TR 50, south of Forest |
| T2 | OH-HAR-AP-003 (provisional) | Andreoff WA South Tract Access | Access Point | CR 190 west of OH-292, south of Kenton |
| T3 | OH-HAR-S-004 (provisional) | Hardin County Veterans Memorial Park | Site — district park | 26 ac; statutory park district under ORC |
| T3 | OH-HAR-S-005 (provisional) | Boy Scout Lake | Site — child | 4.1 ac; child of Veterans Park |
| T3 | OH-HAR-S-006 (provisional) | Silver Creek Center for Environmental Studies | Site | 25 ac; Hardin SWCD T3 per IMP-004 |
| T3 | OH-HAR-TT-002 (provisional) | Veterans Memorial Park Walking Path | Trailthing — paved walking path | Parent: Veterans Park |
| T3 | OH-HAR-TT-003 (provisional) | Silver Creek Paved Trail | Trailthing — paved handicap trail | Parent: Silver Creek Center |
| T3 | OH-HAR-AP-004 (provisional) | Veterans Memorial Park Main Entrance | Access Point | 15906 OH-309 |
| T3 | OH-HAR-AP-005 (provisional) | Silver Creek Center Entrance | Access Point | 12525 SR-67W |

---

## Held Entities

| Entity ID | Name | Hold Reason | Resolution Path |
|-----------|------|-------------|-----------------|
| OH-HAR-S-002 (provisional) | Lawrence Woods Wildlife Area | cross_county_held | Wyandot County pipeline run |
| OH-HAR-S-003 (provisional) | Andreoff Wildlife Area | cross_county_held | Wyandot County pipeline run |

---

## Unresolved Baseline Seeds

| Baseline ID | Name | Status | Notes |
|-------------|------|--------|-------|
| Pleasant Township Green Parcel | Pleasant Township Green Parcel | UNCONFIRMED_BASELINE_SEED | No authoritative source; township has no parks; likely informal open space |
| Ada Trail Spur (Unmarked) | Ada Trail Spur (Unmarked) | UNCONFIRMED_BASELINE_SEED | No formal designation found; may be same as Ada Railroad Park Path |
| Simon Kenton Trail (Planned Extension) | Simon Kenton Trail (Planned Extension) | UNCONFIRMED_BASELINE_SEED | Planned only — not yet constructed; trail currently ends in Logan County |
| Kenton Greenbelt Parcel | Kenton Greenbelt Parcel | UNCONFIRMED_BASELINE_SEED | Unknown ownership; likely informal/private open space |
| Ada Reservoir | Ada Reservoir | UNCONFIRMED_BASELINE_SEED | GPS matches Ada Memorial Park stocked pond; likely same entity; pending field verification |
| Ada Reservoir Woodlot Buffer | Ada Reservoir Woodlot Buffer | UNCONFIRMED_BASELINE_SEED | GPS matches Ada Memorial Park cluster; informal edge; does not meet cataloging threshold |
| Kenton Water Treatment Plant Buffer | Kenton Water Treatment Plant Buffer | UNCONFIRMED_BASELINE_SEED | Restricted buffer around municipal water infrastructure; access restricted |
| McGuffey Reservoir | McGuffey Reservoir | UNCONFIRMED_BASELINE_SEED | Unknown ownership; limited info; did not confirm as public recreation area during T4/T6 |

---

## Pre-Discovery Checklist

*(Populated before beginning each tier)*

**T1 COMPLETE — null result (2026-06-01)**

**Current tier: T2 State**

Sites to check (pre-discovery enumeration before individual fetches):
- [ ] Lawrence Woods State Nature Preserve — https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/lawrence-woods-state-nature-preserve
- [ ] Lawrence Woods Wildlife Area — https://ohiodnr.gov/discover-and-learn/land-water/wildlife-areas/lawrence-woods-wildlife-area
- [ ] Andreoff Wildlife Area (ODNR Division of Wildlife — surfaced in T1 search) — https://www.facebook.com/ohiodivisionofwildlife/posts/andreoff-wildlife-area-located-in-hardin-county (confirm URL via ODNR)
- [ ] ODOT rest stops in Hardin County — cross-reference ODOT rest stops baseline.xlsx
- [ ] Ohio Northern University (Ada) — public university; check land holdings per T2 §4.7
- [ ] ODNR SORP parcels in Hardin County — cross-reference SORP_Parcels_2023.csv
- [ ] OTIC water trails — check if Blanchard River or Scioto River has a designated water trail
- [ ] ODA / DEFA — check for any ODA-managed agricultural demonstration sites
- [ ] Ohio EPA — no DEFA/EPA managed natural areas expected but confirm null

---

## Captured Source Data

*(Verbatim tables from authoritative sources — fetched at time of discovery)*

---

## Open Questions

1. ONU (Ada) confirmed private — T8. ONU campus has Green Monster Trail staged at T8. ✓ Resolved.
2. Ranger Sports Complex (Forest) — staged as T6 Village of Forest. Village-managed per official website. ✓ Resolved.
3. Scioto Marsh baseline entries — all 7+ entries represent historical/drained wetland on private agricultural land with restricted access. None meet public managed natural area threshold. All to be marked unconfirmed baseline seeds or excluded at T0 baseline processing.
4. Saulisberry Park GPS — address is 13344 SR 67W but current acres sources vary (167 vs 200). Pipeline GPS Gate will acquire coordinates from authoritative source.

## Discovery Totals (IMP-080 verified 2026-06-01)

| Tier | Sites | Trailthings | SNs | APs | Notes |
|------|-------|-------------|-----|-----|-------|
| T1 | 0 | 0 | 0 | 0 | Full null |
| T2 | 3 | 1 | 0 | 3 | Lawrence Woods SNP + 2 cross-county WAs |
| T3 | 3 | 2 | 0 | 2 | Veterans Park district; Silver Creek SWCD |
| T4 | 0 | 0 | 0 | 0 | Full null |
| T5 | 23 | 0 | 0 | 0 | 22 township cemeteries + 1 unconfirmed |
| T6 | 15 | 1 | 1 | 3 | Kenton (7+), Ada, Forest, Dunkirk, McGuffey, Mt. Victory, Alger |
| T7 | 0 | 0 | 0 | 0 | Full null |
| T8 | 67 | 1 | 0 | 0 | Memorial Park Golf; ONU trail; 67 cemeteries |
| **Total** | **111** | **5** | **1** | **8** | **144 records on disk** |

## Pipeline Completion — Stage 8 Upserted 2026-06-02

**Run ID:** `hardin_ohio_2026_06_01`
**Committed to:** `natural_areas_v6.db`

| Stage | Result |
|-------|--------|
| Stage 7.5 Human Review | PASSED — 2026-06-02 |
| Stage 8 Upsert | COMPLETE — 2026-06-02 |

**Entities upserted:**
- Sites: 108
- Trailthings: 5
- Site Networks: 1
- Access Points: 6
- Held entities logged: 33

**Held entity breakdown:**
- `cross_county_held`: 2 (Lawrence Woods WA, Andreoff WA → pending Wyandot County run)
- `identity_uncertain`: 1
- `parent_held`: 2
- `unconfirmed_baseline_seed`: 28

**GPS resolution:**
- 52 cemetery GPS coordinates resolved via OSM/Nominatim/Google Maps/parcel viewer/human-assist
- 36 cemeteries confirmed permanently `gps_unresolvable` — GNIS investigation complete (2026-06-02):
  - GNIS DomesticNames (current) no longer distributes Cemetery feature class
  - GNIS 2021 archive (OH_Features_20210825.txt) has 46 Hardin County cemeteries — all 46 match records already resolved in the 52; none of our 36 remaining were ever in GNIS
  - OSM/Nominatim: 0 matches for all 36 (small rural family/private cemeteries with no digital footprint)
  - County Auditor parcel search: only 5 cemeteries as registered owners, none matching our 36
  - **Status: CLOSED — 36 cemeteries are permanently gps_unresolvable, no further sources to check**
- Westminster Salem Cemetery (40.6788, -83.9614) identified as new T8 discovery during GPS pass — not yet in dataset

**Stage 7.5 review changes applied:**
- Cemetery `designation` and redundant `description` fields cleaned (109 fields)
- AP `features` scoped to entry-point only (removed parent-site amenities)
- Boy Scout Lake `parent_site_id` = OH-HAR-S-004 set
- Lawrence Woods SNP `features` updated (Hiking Trail added)
- Memorial Park Golf Club `features` updated (Golf Course added)
- Alternate cemetery names confirmed: Speeler/Behler, Lee/Hepburn, Morrison/Pfeiffer, Wolf Creek spelling variant

**DB schema migrations applied (first v6 county run):**
- `site_networks`: added `coordination`, `url`, `urls` columns
- `access_points`: added `counties`, `description`, `location`, `urls` columns

**Open items for follow-up:**
- ~~GNIS GPS pass for 34 unresolved cemeteries~~ — **CLOSED 2026-06-02**: 36 cemeteries confirmed permanently gps_unresolvable; GNIS never had these records; all automated sources exhausted
- Westminster Salem Cemetery — **NOT a Hardin record**; GIS lookup confirms Auglaize Township = Allen County (Allen borders Hardin to the northwest); note for Allen County run
- IMP-017 validation run — first v6 county; check for v5 DB data inconsistencies
- Wyandot County pipeline run — resolves 2 cross-county held entities

---

## Batch Resolution Update — 2026-06-09

**Session:** Quality review continuation from 2026-06-08 handoff  
**Run ID:** `BATCH_HARDIN_2026-06-09`

### GPS Acquisitions Applied

| Site ID | Name | New GPS | Source |
|---------|------|---------|--------|
| OH-HAR-S-0004 | Hardin County Veterans Memorial Park | 40.641443, -83.575206 | GNIS (Veterans Memorial Park feature) |
| OH-HAR-S-0033 | Home Run Memorial Park | 40.621574, -83.597332 | Census geocoder — 13625 SR 292 |
| OH-HAR-S-0034 | Gene Autry Park | 40.650703, -83.610456 | Census geocoder — 309 N Market St |
| OH-HAR-S-0036 | Murray Park | 40.653715, -83.605418 | Census geocoder — 511 N Cherry St |
| OH-HAR-S-0038 | Ada Railroad Park | 40.770401, -83.822975 | Census geocoder — 112 E Central Ave |

### Acreage Fills Applied

| Site ID | Name | Acres | Source |
|---------|------|-------|--------|
| OH-HAR-S-0039 | Gormley Park | 16.0 | PAD-US 4.0 |
| OH-HAR-S-0041 | Dunkirk Community Park | 6.0 | PAD-US 4.0 |

### manual_review_queue Entries Added

- **34 cemetery GPS** (OH-HAR-S-0008, 0010, 0025, 0051–0056, 0065–0066, 0069, 0075–0081, 0083, 0086, 0090–0091, 0094–0095, 0097–0099, 0101–0102, 0105, 0107–0108, 0110–0111): GPS unresolvable via GNIS/OSM/Nominatim/Overpass — requires county auditor parcel or FindAGrave
- **9 non-cemetery GPS** (OH-HAR-S-0039, 0040, 0041, 0043, 0044, 0005, 0045, 0059, 0092): Not found in OSM/GNIS; village parks need municipal contact; Indian Burial Grounds need GIS/county consultation; S-0005 and S-0045 need precision improvement from imprecise centroid
- **Salem Cemetery S-0064** (GPS precision): current 40.744,-83.3993 is 3-decimal (~100m); requires parcel lookup for 6-decimal precision
- **S-0029 Roundhead Community Park**: identity unconfirmed; no PAD-US/GNIS entry near Village of Roundhead; requires field verification
- **S-0138 Ball Park** / **S-0139 Glendale Skate Park**: GPS needed; new T6 supplemental sites

### Unconfirmed Baseline Seeds Reviewed (IMP-080)

All 25 held entities (OH-HAR-S-0112 through S-0136) reviewed against v6 Site qualification criteria:

- **14 RECOMMEND DISQUALIFICATION**: S-0112 (AEP ROW), S-0113 (Ada Reservoir = park feature), S-0114 (Reservoir woodlot buffer), S-0115 (Ada Trail Spur → reclassify as TT), S-0118 (Hog Creek Marsh historical), S-0120 (Kenton Greenbelt informal), S-0121 (WTP buffer), S-0122 (Lawrence Woods buffer), S-0125 (Pleasant Twp green parcel), S-0126 (Scioto Marsh historical), S-0128–0130 (drainage canals/district/access), S-0136 (Veterans Park buffer). All added to manual_review_queue with disqualification recommendation.
- **10 PENDING RESEARCH**: S-0116 (Blanchard River Corridor), S-0117 (Hog Creek Corridor), S-0119 (Hog Creek Marsh Remnant), S-0123 (Lawrence Woods Prairie Restoration), S-0124 (McGuffey Reservoir), S-0127 (Scioto Marsh Complex), S-0131–0133 (Scioto Marsh edge/prairie/remnants), S-0134 (Scioto River Corridor). Added to manual_review_queue with specific research directions (PAD-US Easements, NWI GDB, ODNR Natural Heritage, OPA).
- **1 KEEP HELD**: S-0135 (Simon Kenton Trail Planned Extension) — awaiting PTOC/RTC Hardin County construction announcement.

### Supplemental Discovery — T6 Sites Added

| Site ID | Name | GPS | Notes |
|---------|------|-----|-------|
| OH-HAR-S-0137 | Ohio Northern University Campus | 40.765886, -83.823826 | T8 private; site_parent for TT-0005 |
| OH-HAR-S-0138 | Ball Park | NULL | GPS in manual_review_queue |
| OH-HAR-S-0139 | Glendale Skate Park | NULL | GPS in manual_review_queue |

**TT-0005 ONU Green Monster Trail** → `site_parent_id` set to OH-HAR-S-0137 ✓

### Supplemental Items — Confirmed Not Hardin County

- **WPA 32 (47ac) and WPA 43 (40ac)**: PAD-US GDB query of full Hardin County bbox → zero USFWS/WPA entries. These WPAs are not in Hardin County. Flag for adjacent county discovery.
- **Marion Tallgrass Trail (30ac, County Land)**: PAD-US centroid 40.601N,-83.303W; polygon extends -83.42 to -83.185W but township lookup at all sample points returns Marion County townships (Big Island, Montgomery). Catalog under Marion County T4 when processed.

### Open Items Remaining for Hardin

- **GPS needed (manual_review_queue)**: 34 cemeteries + 9 non-cemetery sites + Salem precision + S-0138/0139
- **Baseline seed decisions (manual_review_queue)**: 14 disqualification recommendations + 10 research items pending human action
- **IMP-026 remediation**: Hardin upsert script bypassed GPS gate (45 sites upserted with NULL GPS directly). Flag `upsert_hardin.py` for correction in next pipeline refactor.
- **Wyandot County run**: releases 2 cross-county held entities (Lawrence Woods WA, Andreoff WA)

---

---

## Baseline Seed Resolution Update — 2026-06-11

**Session:** Cross-county held entity resolution pass

### OH-HAR-S-0029 Roundhead Community Park — RESOLVED (prior work, recorded here)
Ghost held entity (only in held_entities, no sites record). INSERT performed:
- Name: Roundhead-McDonald Park (ALT NAME: "Roundhead Community Park" per IMP-029)
- GPS: 40.5615625, -83.8391875 (plus_code 86GRH566+J8)
- Location: 17763 OH-117, Roundhead, OH 43346
- Governance: Roundhead Township, Hardin County
- Features: Athletic Field; Ball Diamond
- Released from held_entities ✓

### ODNR Water Trails Research — Blanchard River

Fetched and analyzed BlanchardRiverMapGuide.pdf (Hancock Park District + ODNR, 3.75MB).

Key findings:
- The ODNR-designated Blanchard River Water Trail is 37.6 miles, entirely within Hancock County
- All 11 access points: 40.84°–41.06°N (Hancock County; Hardin County boundary is ~40.74°N)
- Trail start: Blanchard River Nature Preserve, 22006 CR 17, Forest, OH (40.84407, -83.55662)
- Managed cooperatively by Hancock Park District and ODNR
- PDF source confirms: "The Blanchard River begins in central Hardin County, flows north into eastern Hancock County" — river originates here but designated trail does not
- **No formal "Blanchard River Corridor" designation exists for Hardin County**

**Note for Hancock County run:** The Blanchard River Water Trail (37.6 mi) is a T3 Trailthing under Hancock Park District. 11 access points with published GPS. PDF at source_documents for cataloging.

### Unconfirmed Baseline Seeds Disqualified — 2026-06-11

| Site ID | Name | Disqualification Reason |
|---------|------|------------------------|
| OH-HAR-S-0116 | Blanchard River Corridor | ODNR Blanchard River Water Trail entirely in Hancock County. No formal corridor designation in Hardin County. Source: BlanchardRiverMapGuide.pdf. |
| OH-HAR-S-0123 | Lawrence Woods Prairie Restoration | Prairie restoration is management activity at Lawrence Woods SNP (OH-HAR-S-0001, already in DB), not a separate named/bounded entity. Source: naturepreserves.ohiodnr.gov. |
| OH-HAR-S-0124 | McGuffey Reservoir | Not in GNIS Hardin County reservoir features (3 features found, none matching). No ODNR, county parks, or recreation designation found. Likely private/utility. |
| OH-HAR-S-0134 | Scioto River Corridor | Not on ODNR water trails list. No formal corridor designation found in Hardin County. Source: ohiodnr.gov/ohio-water-trails. |

All 4 removed from held_entities. No sites records to remove (all were ghost held entities).

### OH-HAR-S-0135 Simon Kenton Trail (Planned Extension) — KEEP HELD

Proposed trail extension into Hardin County, not yet constructed. Trail currently ends in Logan/Champaign Counties. Monitor POTA/PTOC for construction status updates.

### Hardin Held Entity Count — Post 2026-06-11

| Entity ID | Name | Hold Reason | Resolution Path |
|-----------|------|-------------|-----------------|
| OH-HAR-S-0002 | Lawrence Woods Wildlife Area | cross_county_held | Wyandot County pipeline run |
| OH-HAR-S-0003 | Andreoff Wildlife Area | cross_county_held | Wyandot County pipeline run |
| OH-HAR-AP-0002 | Andreoff Wildlife Area North Tract Access | parent_held | Resolves when OH-HAR-S-0003 released |
| OH-HAR-AP-0003 | Andreoff Wildlife Area South Tract Access | parent_held | Resolves when OH-HAR-S-0003 released |
| OH-HAR-S-0135 | Simon Kenton Trail (Planned Extension) | unconfirmed_baseline_seed | Monitor for construction |

**Total Hardin held: 5** (down from 9 at start of session; 4 disqualified, 1 active ghost resolved)

---

*This handoff is a progress tracker only. For authoritative procedure detail, read the module files. When this handoff and a module conflict, the module wins.*
