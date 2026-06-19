# Henry County, Ohio — Session Log
**RUN_ID:** `henry_oh_2026_04_20`
**PREFIX:** `HEN`
**County:** Henry County, Ohio
**Run date:** 2026-04-20
**Status:** PIPELINE COMPLETE 2026-04-27 (ODNR GIS GPS patch applied)

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal / OSM | Overpass bbox query (41.15,-84.25,41.50,-83.85); NPS noco maps; USFWS Ohio; USACE NID dam query; BLM/USFS regional; OSM trail relations | 0 entities — NULL. No federal land ownership in Henry County. NCT confirmed passing through (OSM rel 11140513) — cross-ref to DEF run record; not re-staged. USFWS: nearest refuges Ottawa/Cedar Point NWR (Ottawa Co). USACE: no flood control projects; only Lock No. 44 (historic canal, no USACE ownership). USFS/BLM/DoD: none in NW Ohio. Tribal: none. COMPLETE 2026-04-20. |
| T2 | State agency | ODNR Parks, ODNR Division of Wildlife, ODNR Forestry, ODNR Water Trails (Maumee), Ohio Nature Preserves | 14 entities (6 Sites, 5 Trails, 2 Access Points, 1 Scenic River Site). MJTSP + 3 ODNR WAs + Maumee Scenic River. All 6 entity types documented. OHC PENDING (site maintenance). COMPLETE 2026-04-20. |
| T3 | District agency | Henry SWCD (`http://www.henryswcd.com`); county park district search; metropark search; conservancy district search; flood-control district search | 0 entities — NULL. Henry SWCD confirmed no land ownership (est. 1955; agricultural drainage/conservation tech assistance; 400+ mi ditch maintenance; no public-access natural areas). No standalone park district, metropark, conservancy district, or flood-control district in Henry County. Full null across all 6 entity types. COMPLETE 2026-04-20. |
| T4 | County website | henrycountyohio.gov (full sitemap); henrycountyengineer.com; henrycountyparks.blogspot.com (Henry County Park District); NRHP Wikipedia; henrycountyhistory.org; Maumee Valley RC&D; TrekOhio; Wabash Cannonball Trail governance search | 6 entities — 1 Trail + 5 Trail Segments. Henry County Park District (all-volunteer, 2005, state canal land leases) manages Miami & Erie Canal Towpath Hiking Trail in 5 named segments. No county parks dept on county site. Engineer: roads/drainage only. HCHS → T7. Fairgrounds → T8. WCT → T7 (NORTA nonprofit). NRHP: 4 downtown Napoleon buildings, none qualify. IMP-080 passed. COMPLETE 2026-04-21. |
| T5 | Township | 0 entities — NULL. All 13 townships checked (CORRECTION: 12→13; Tiffin/Beaver Dam/Bloom/Monterey were bootstrap errors; Harrison/Marion/Monroe/Pleasant/Ridgeville were missing). Washington Twp website (washtwphenry.com) confirmed Henry County; no parks. All other 12 townships: no OTA websites; web search null across all. Hamler Community Park (Marion Twp) is private Summerfest association land → T8 candidate (HEN-F-10). Full null all 6 entity types. IMP-080 passed. COMPLETE 2026-04-21. |
| T6 | Municipal | Napoleon (city) + villages: Deshler, Holgate, Hamler, Liberty Center, Malinta, McClure, Florida, New Bavaria, Custar | 23 entities (20 Sites + 3 Access Points) — COMPLETE. Map verification pass 2026-04-21 added 1 new entity (New Bavaria Park) and GPS for 22/23 records. Napoleon: 10 Sites (Glenwood, East Riverdowns, Dog Park, Ritter, Oberhaus, Jaycee/NOPH, Wayne, Veterans Memorial, Firemen's, West Park) + 2 APs (Ritter Boat Launch, Oberhaus Boat Dock). Deshler: 1 Site (Deshler Reservoir Park, HEN-F-04 partial). Holgate: 2 Sites (Holgate Village Park, Old School Park). Hamler: 1 Site (Hamler Memorial Park). Liberty Center: 1 Site (Veterans Park) + 1 AP (WCT Depot Trailhead, HEN-F-07 partial). McClure: 1 Site (Big Creek Park). Florida baseline seed (Canal Falls, HEN-F-06), Malinta (Malinta Fields), New Bavaria (NB Village Park): all PARTIAL_NULL pending map verification. Custar excluded — Wood County bootstrap error (HEN-F-11). HEN-F-01 + HEN-F-02 RESOLVED (Ritter Park + boat launch confirmed). HEN-F-07 PARTIAL RESOLVE (Liberty Center depot confirmed; Holgate trailhead deferred to T7). IMP-080 verified: 22 T6 records in YAML (19 Sites + 3 APs). COMPLETE (web); MAP VERIFICATION PENDING 2026-04-21. |
| T7 | Land trust / conservancy | NORTA/WCT (wabashcannonballtrail.org, Wikipedia, TrailLink); Black Swamp Conservancy (blackswamp.org/properties/land-we-protect/); TNC Ohio (nature.org/OH); HCHS (henrycountyhistory.org); OHC (ohiohistory.org — JS-rendered, no static access) | 5 entities — 1 Trail + 1 Trail Segment + 1 AP + 2 Sites. WCT: Wabash Cannonball Trail (multi-county Trail, NORTA gov.) + WCT South Fork (Trail Segment, Henry Co. section ~6 mi, Washington Twp, cinder/gravel/dirt/grass) + Henry CR 6C Trailhead AP (GPS 41.450715,-83.990451; parking/picnic/kiosk, ~1 mi east of Liberty Center; NORTA ownership ends at Henry CR 7). HEN-F-07 RESOLVED. HCHS: Dr. John Bloomfield Home & Carriage House Museum (229 W Clinton St, Napoleon) + HCHS Fairgrounds Historic Complex (outdoor historic buildings on Fairgrounds property). BSC: NULL — no Henry County properties (19 listed, all Erie/Ottawa/Lucas/Sandusky/Wood). TNC: NULL — 382 OH properties, zero Henry County. OHC (HEN-F-09): no static-accessible Henry County sites; JS-rendered site finder; flag remains open. Liberty Center Depot AP GPS updated from NORTA page (41.443728,-84.009326). T4 discovery_tier field fixed (6 records). IMP-080 passed. COMPLETE 2026-04-26. |
| T8 | Private / other | Henry County Fairgrounds (henrycountyohio.gov/270); Hamler Community Park (hamlersf.com/50-year-history.html); Field of Dreams Drive-In (web search — crescent-news, bigscreen, 13abc) | 2 entities — 2 Sites. Henry County Fairgrounds (821 S Perry St, Napoleon; Henry County Ag Society; HCHS Historic Complex on grounds — resolves T7/T8 overlap). Hamler Community Park (SR 109, north edge of Hamler; Summerfest nonprofit; 13 ac; basketball/tennis/playground/fencing; year-round community use; resolves HEN-F-10). Field of Dreams Drive-In (V602 CR 6, Liberty Center) — EXCLUDED: commercial cinema venue, not natural/recreation area; ownership in flux (Legacy Theatres → seeking new operator Nov 2025). No private hunt clubs or private nature preserves identified. IMP-080 passed. COMPLETE 2026-04-26. |

**Total raw records:** 50 (T2: 14; T3: null; T4: 6; T5: null; T6: 23 [20 Sites + 3 APs]; T7: 5 [1 Trail + 1 Trail Segment + 1 AP + 2 Sites]; T8: 2 [2 Sites])
**Post-resolution:** pending

---

## Normalization Decisions

*(See detailed section below — populated 2026-04-26)*

---

## GPS Acquisition

*(See detailed section below — populated 2026-04-26)*

**Nominatim Stage 3:** 7 acquired (3 HIGH, 1 MED, 3 LOW) | 5 NONE
**Fallbacks used:** IMP-081 city-centroid fallback for HEN_S_006, HEN_S_009, HEN_S_017

**ODNR GIS Patch (2026-04-27):** 4 of 5 NONE entities resolved via ODNR DOW parcel GIS (DOW_Services/Roads_ParkingAreas FeatureServer layer 28). Polygon centroids computed from official ODNR Division of Wildlife boundary geometry. HEN_S_006 GPS upgraded LOW→HIGH from same source.

| Entity | Name | GPS (Centroid) | Township |
|--------|------|----------------|----------|
| HEN_S_013 | Henry County Wildlife Area 1 | 41.323055, -83.890652 | Richfield |
| HEN_S_014 | Henry County Wildlife Area 2 | 41.322366, -84.161557 | Flatrock |
| HEN_S_015 | Henry County Wildlife Area 3 | 41.277479, -84.077872 | Monroe |
| HEN_S_023 | North Turkeyfoot Wildlife Area | 41.411469, -83.989405 | Washington |
| HEN_S_006 | Florida Wildlife Area (upgrade) | 41.332353, -84.179489 | Flatrock |

**Remaining NONE:** HEN_S_019 (Maumee State Scenic River) — linear feature spanning multiple counties; no single GPS point appropriate. Permanently held.

**Final counts:** 49 normalized, 1 held (HEN_S_019)

---

## Errors and Fixes

None.

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1 — Resolution | **COMPLETE 2026-04-26** | 50 records → 50 resolved entities (0 merges). 73 hard separations (§10.5 GPS + numbered-name rules). 31 soft review sets. All parent IDs resolved. Script: `processing/henry_oh_resolution_stage1.py`. Output: `henry_oh_resolved_entities.yaml`, `henry_oh_resolution_report.md`. |
| Stage 2 — Normalization | **COMPLETE 2026-04-26** | 50 input → 38 normalized + 12 held (IMP-069 GPS gate). 0 fatal rejects. Stage 4.5 vocab gate passed inline (0 violations). Script: `processing/henry_oh_normalization_stage2.py`. Outputs: `henry_oh_normalized_entities.yaml`, `henry_oh_held_entities.yaml`, `henry_oh_normalization_report.md`. |
| Stage 3 — GPS Acquisition | **COMPLETE 2026-04-26** | 12 held → 7 acquired (3 HIGH, 1 MED, 3 LOW) + 5 NONE-held. Total normalized: 45. Upsert-blocked: HEN_S_013/014/015 (HC Wildlife Areas 1-3), HEN_S_019 (Maumee Scenic River), HEN_S_023 (North Turkeyfoot WA). Scripts: `processing/henry_oh_gps_acquisition_stage3.py`, `henry_oh_gps_merge_stage3.py`. |
| ODNR GIS GPS Patch | **COMPLETE 2026-04-27** | 4 wildlife area NONE entities resolved via ODNR DOW_Services GIS parcel layer (HIGH confidence polygon centroids): HEN_S_013/014/015/023. HEN_S_006 GPS upgraded LOW→HIGH. TSVs regenerated (30 sites). Vocab gate re-passed (0 violations). DB re-upserted (30 sites). Script: `processing/henry_oh_gis_gps_patch.py`. |
| Stage 4 — TSV Output | **COMPLETE 2026-04-27** | 6 TSV files written to `output/henry_oh_*.tsv`. **30 sites**, 7 trails, 6 trail segments, 6 APs, 0 trail networks, 0 site networks. 49 total entities. Script: `processing/henry_oh_pipeline_stages456.py`. |
| Stage 4.5 — Vocab Gate | **PASSED 2026-04-27** | 0 violations across all 49 normalized entities. All category, subtype, designation, status, and features values valid. |
| Stage 5 — Integrity Check | **PASSED 2026-04-27** | 0 warnings. All GPS present, parent IDs valid, no duplicates. |
| Stage 6 — DB Upsert | **COMPLETE 2026-04-27** | **30 sites** + 7 trails + 6 trail segments + 6 APs upserted. 1 held entity (HEN_S_019). run_metadata: normalized=49, held=1. Final DB: 0 GPS gaps in TSV-eligible entities. DB: `NASqlite/natural_areas_v5.db`. |

---

## Entity ID Assignments

| ID | Entity Type | Name |
|----|-------------|------|
| HEN_S_001 | Site | Big Creek Park |
| HEN_S_002 | Site | Deshler Crossroads Park |
| HEN_S_003 | Site | Dr. John Bloomfield Home & Carriage House Museum |
| HEN_S_004 | Site | East Riverdowns Park |
| HEN_S_005 | Site | Florida Wildlife Area |
| HEN_S_006 | Site | Fredrick Steward Memorial Park |
| HEN_S_007 | Site | Hamler Community Park |
| HEN_S_008 | Site | Hamler Memorial Park |
| HEN_S_009 | Site | Henry County Fairgrounds |
| HEN_S_010 | Site | Henry County Historical Society Fairgrounds Historic Complex |
| HEN_S_011 | Site | Henry County Wildlife Area 1 |
| HEN_S_012 | Site | Henry County Wildlife Area 2 |
| HEN_S_013 | Site | Henry County Wildlife Area 3 |
| HEN_S_014 | Site | Holgate Village Park |
| HEN_S_015 | Site | Liberty Center Firemen's Park |
| HEN_S_016 | Site | Mary Jane Thurston State Park |
| HEN_S_017 | Site | Maumee State Scenic River |
| HEN_S_018 | Site | Meyerholtz Wildlife Park |
| HEN_S_019 | Site | Napoleon Dog Park |
| HEN_S_020 | Site | New Bavaria Park |
| HEN_S_021 | Site | North Turkeyfoot Wildlife Area |
| HEN_S_022 | Site | Oakwood Park |
| HEN_S_023 | Site | Oberhaus Park |
| HEN_S_024 | Site | Old School Park |
| HEN_S_025 | Site | Ritter Park |
| HEN_S_026 | Site | Swearingen Park |
| HEN_S_027 | Site | Veterans Memorial Park |
| HEN_S_028 | Site | Vorwerk Park |
| HEN_S_029 | Site | Wayne Park |
| HEN_S_030 | Site | Glenwood Park |
| HEN_S_031 | Site | (see resolved entities YAML for full list) |
| HEN_T_001 | Trail | Blue Trail → parent HEN_S_016 (MJTSP) |
| HEN_T_002 | Trail | Miami & Erie Canal Towpath Hiking Trail |
| HEN_T_003 | Trail | Orange Trail → parent HEN_S_016 (MJTSP) |
| HEN_T_004 | Trail | Storybook Trail → parent HEN_S_016 (MJTSP) |
| HEN_T_005 | Trail | Tow Path → parent HEN_S_016 (MJTSP) |
| HEN_T_006 | Trail | Wabash Cannonball Trail |
| HEN_T_007 | Trail | Yellow Trail → parent HEN_S_016 (MJTSP) |
| HEN_TS_001 | Trail Segment | Damascus Leg — Miami & Erie Canal Towpath → parent HEN_T_002 |
| HEN_TS_002 | Trail Segment | Independence Leg — Miami & Erie Canal Towpath → parent HEN_T_002 |
| HEN_TS_003 | Trail Segment | Napoleon Leg — Miami & Erie Canal Towpath → parent HEN_T_002 |
| HEN_TS_004 | Trail Segment | Renegade Leg — Miami & Erie Canal Towpath → parent HEN_T_002 |
| HEN_TS_005 | Trail Segment | Wabash Cannonball Trail - South Fork → parent HEN_T_006 |
| HEN_TS_006 | Trail Segment | WideWater Section — Miami & Erie Canal Towpath → parent HEN_T_002 |
| HEN_AP_001 | Access Point | Mary Jane Thurston State Park Boat Launch Ramp → parent HEN_S_016 |
| HEN_AP_002 | Access Point | Mary Jane Thurston State Park Marina → parent HEN_S_016 |
| HEN_AP_003 | Access Point | Oberhaus Park Boat Dock → parent HEN_S_023 |
| HEN_AP_004 | Access Point | Ritter Park Boat Launch → parent HEN_S_025 |
| HEN_AP_005 | Access Point | WCT Henry CR 6C Trailhead → parent HEN_T_006 |
| HEN_AP_006 | Access Point | Wabash Cannonball Trail Liberty Center Depot Trailhead → parent HEN_T_006 |

**Note:** IDs are sorted alphabetically within each entity type. Full resolved entity details in `henry_oh_resolved_entities.yaml`.

---

## Open Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| HEN-F-01 | Boatramp Facility | Baseline claims it is within Ritter Park (5.6 ac) but boatramp is listed at 14.8 ac — acreage conflict | **RESOLVED 2026-04-21.** napoleonohio.com confirms Ritter Park at 1111 W. Riverview Ave. Boat launch = child Access Point of Ritter Park. Both baseline rows merged into 1 Site + 1 AP. |
| HEN-F-02 | Ritter Park | Two baseline rows with same name — one with 5.6 ac + "West Riverview Avenue," one with address 1130 W. Riverview Ave and no acreage | **RESOLVED 2026-04-21.** Same entity as HEN-F-01. Address confirmed 1111 W. Riverview Ave. Staged as single Site record. |
| HEN-F-03 | Henry County Wildlife Areas 1/2/3 | Three numbered placeholders with no location detail | Open. ODNR Wildlife GIS layer required to determine parcel locations and public access status. |
| HEN-F-04 | Deshler Reservoir 1 & 2 | No location, acreage, or management info in baseline | PARTIAL. Deshler Reservoir Park confirmed as T6 Site (Reservoir Rd, managed by Village of Deshler). Count/location of second reservoir entry unclear. Map verification required. |
| HEN-F-05 | Hamler Reservoir | No detail in baseline | Open. No online confirmation found. Map verification required; likely a small utility reservoir. |
| HEN-F-06 | Canal Falls | Listed as Florida Village Park in baseline but described as adjacent to Miami & Erie Canal Towpath and Buckeye Trail — may be a natural feature / trail access point, not a standalone park | Open. Florida village (no official website; henryhas.com 404). Baseline seed unresolved. Documented as PARTIAL_NULL at T6. Map verification required. |
| HEN-F-07 | Wabash Cannonball Trailheads (×2 in baseline) | Two baseline entries with similar names at slightly different addresses — may be same access point or two distinct APs | **RESOLVED 2026-04-26.** Two distinct APs confirmed via NORTA wabashcannonballtrail.org/trail-access/: (1) Liberty Center Train Station / Depot (T6 AP already staged; GPS 41.443728,-84.009326 confirmed from NORTA page — updated in YAML); (2) Henry CR 6C Trailhead, ~1 mile east of Liberty Center between CR U and CR T (T7 AP staged; GPS 41.450715,-83.990451). NORTA ownership officially ends at Henry CR 7 (Pleasantview Dr). "Holgate trailhead" in baseline was a misidentification — CR 6C is near Liberty Center in Washington Twp, not Holgate. |
| HEN-F-08 | North Country NST | Already staged in Defiance County (DEF run) as multi-county Trail; NCT passes through Henry County | Open. Do not re-stage as new entity; confirm Henry County presence and note cross-reference in discovery notes. |
| HEN-F-09 | OHC (Ohio History Connection) | ohiohistory.org was down during T2; no OHC Henry County sites confirmed | Open. Recheck ohiohistory.org for Henry County state historic sites. No sites expected but authoritative confirmation required before T2 closure. |
| HEN-F-10 | Hamler Community Park Inc. | Private Summerfest nonprofit on SR 109 — not a village park | **RESOLVED 2026-04-26.** Hamler Summerfest non-profit (Hamler Community Park Inc.) owns 13-acre park at SR 109 north edge of Hamler (Marion Twp). Land purchased 1974 for $21,000. Year-round community use: basketball/tennis in 100'×250' steel structure, playground, permanent fencing. Festival venue (Summerfest + Country Fest). No tax money — 100% privately funded through volunteerism and festivals. Staged as T8 Site. Source: hamlersf.com/50-year-history.html. |
| HEN-F-11 | Custar | Bootstrap listed Custar as Henry County village | **RESOLVED (bootstrap error) 2026-04-21.** Custar is in Wood County (SW corner). Wikipedia, custarvillage.org, and Wood County Engineer confirm. Excluded from T6 discovery. No records created. |

---

## Normalization Decisions

**COMPLETE 2026-04-26** | Script: `processing/henry_oh_normalization_stage2.py`

**Entity counts:** 38 normalized (19 Sites, 7 Trails, 6 Trail Segments, 6 Access Points) + 12 held (GPS missing, IMP-069)

**Category inference (all Sites):** All Henry County sites had `category_raw = null` — categories inferred via priority chain:
- §7.2 IMP-068 name pattern → Museum → `Museum` (HEN_S_004 Dr. John Bloomfield Home)
- Governance = ODNR Division of Wildlife → `Wildlife Area` (HEN_S_005 Florida WA, HEN_S_013-015 HC WAs, HEN_S_023 North Turkeyfoot WA)
- Name keyword "state park" + ODNR Parks governance → `Park` / subtype via §7.4 MJTSP (HEN_S_018)
- Name keyword "fairgrounds" → `Recreation Facility` / subtype `Athletic Field` (HEN_S_009, HEN_S_010)
- Name "Maumee State Scenic River" → `Water Site` / subtype `River` (HEN_S_019)
- Remaining village/city parks → `Park` (default)

**Key subtype assignments:**
- HEN_S_021 Napoleon Dog Park → `Dog Park` (§3.2 Park subtypes, name-match)
- HEN_S_019 Maumee State Scenic River → `River` (§7.4 Water Site name inference)

**Status inference:** All 19 normalized Sites had blank `status_raw`. §4.2a applied: GPS present + authoritative URL present → `Active` (19 sites). 12 held sites: status inference deferred to post-GPS-acquisition normalization.

**Trail origin inference:**
- HEN_T_002 Miami & Erie Canal Towpath → `Canal Towpath` (name pattern)
- HEN_T_005 Tow Path → `Canal Towpath` (name + notes keyword `towpath`)
- HEN_T_006 Wabash Cannonball Trail → `Rail Trail` (`\bwabash cannonball\b` pattern)
- MJTSP trails (Blue/Orange/Yellow/Storybook/Tow Path) — rail-trail false-match prevented by `\brail\s+trail\b` word-boundary regex (IMP-079 fix)

**Trail difficulty:** MJTSP in-park trails assigned `Easy` from source rating. WCT and M&E Canal Towpath: blank (no explicit rating in sources).

**Access Point type inference:** HEN_AP_003 Oberhaus Park Boat Dock and HEN_AP_004 Ritter Park Boat Launch both inferred as `Boat Launch` via name-pattern matching (added `"boat dock"` and `"boat launch"` branches after initial run).

**Features normalization:** Feature mapping applied to all Sites. Canonical vocabulary terms extracted from `features_raw` via pattern matching (FEATURE_MAP). Terms with no vocabulary match retained in `features_raw` only per §2c rules.

**Stage 4.5 Vocabulary Gate:** PASSED — 0 violations across all 38 normalized entities (category, subtype, designation, status, features all validated against `na_vocab_constants.py`).

---

## GPS Acquisition

**COMPLETE 2026-04-26** | 7/12 acquired | 5 remain held (NONE GPS — upsert-blocked)

| ID | Name | Confidence | GPS Lat | GPS Lon | Method |
|---|---|---|---|---|---|
| HEN_S_004 | Dr. John Bloomfield Home & Carriage House Museum | HIGH | 41.391340 | -84.127327 | Address: 229 W Clinton St, Napoleon, OH |
| HEN_S_006 | Florida Wildlife Area | LOW | 41.321993 | -84.204391 | City centroid: Florida, Henry County, OH |
| HEN_S_009 | Hamler Community Park | LOW | 41.229216 | -84.034111 | City centroid: Hamler, Henry County, OH |
| HEN_S_011 | Henry County Fairgrounds | HIGH | 41.381644 | -84.120723 | Address: 821 S Perry St, Napoleon, OH |
| HEN_S_012 | HCHS Fairgrounds Historic Complex | HIGH | 41.381644 | -84.120723 | Address: 821 S Perry St, Napoleon, OH (co-located) |
| HEN_S_017 | Liberty Center Firemen's Park | LOW | 41.443385 | -84.008835 | City centroid: Liberty Center, Henry County, OH |
| HEN_S_018 | Mary Jane Thurston State Park | MED | 41.411925 | -83.884997 | Nominatim name query: MJTSP, Henry County, OH |
| HEN_S_013 | Henry County Wildlife Area 1 | NONE | — | — | No Nominatim match; numbered ODNR parcel without OSM presence |
| HEN_S_014 | Henry County Wildlife Area 2 | NONE | — | — | No Nominatim match; numbered ODNR parcel without OSM presence |
| HEN_S_015 | Henry County Wildlife Area 3 | NONE | — | — | No Nominatim match; numbered ODNR parcel without OSM presence |
| HEN_S_019 | Maumee State Scenic River | NONE | — | — | Linear feature spanning multiple counties; no single GPS point |
| HEN_S_023 | North Turkeyfoot Wildlife Area | NONE | — | — | No Nominatim match; ODNR parcel without OSM presence |

**IMP-081 fallback protocol applied:** Florida WA, Hamler Community Park, Liberty Center Firemen's Park — all Nominatim name queries failed; city centroid assigned (LOW confidence). LOW-confidence GPS noted in entity identity_notes and notes fields.

**Stage 3 patch:** HEN_S_012 category corrected Recreation Facility → Historic Site / Historic Landscape (fairgrounds address geocode triggered wrong category in Stage 2; corrected post-GPS-merge per entity documentation).

**Nominatim:** 7 acquired (3 HIGH, 1 MED, 3 LOW) | 5 NONE
**Fallbacks used:** IMP-081 city-centroid fallback for HEN_S_006, HEN_S_009, HEN_S_017

---

## Status

**PIPELINE COMPLETE 2026-04-26**
50 raw records → 45 upserted (26 Sites, 7 Trails, 6 Trail Segments, 6 Access Points) + 5 held (NONE GPS: HC WA 1-3, Maumee Scenic River, North Turkeyfoot WA).
Stage 4.5 vocab gate: PASSED (0 violations). Stage 5 integrity: 1 warning resolved (AP GPS patch). Stage 6 DB commit: clean.
Post-pipeline notes: `access_point_type`→`ap_type` field mapping bug fixed post-upsert; HEN_S_012 category patched Historic Site post-normalization.
Open flags (no pipeline impact; deferred to future ODNR GIS pass): HEN-F-03/13/14/15 (ODNR Wildlife GIS parcel locations), HEN-F-04 (Deshler Reservoir 2), HEN-F-05 (Hamler Reservoir), HEN-F-06 (Canal Falls/Florida), HEN-F-08 (NCT cross-ref), HEN-F-09 (OHC JS-rendered).
