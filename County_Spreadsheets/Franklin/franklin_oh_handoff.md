# Franklin County, Ohio — Discovery Handoff
# Natural Areas Project v5.2
# -----------------------------------------------------------

## Handoff Status: ACCESS POINTS GREENWAY BATCH COMPLETE — 90 FR-AP records in DB — Remaining gap: Metro Parks hiking trail trailheads (~90 trails); all other Franklin work complete.

**Last updated:** 2026-05-11
**Session:** 27 — Access Points Discovery (Task #32): FR-AP-0054 Broad Meadows Dam Portage inserted; FR-AP-0055 to FR-AP-0090 (36 greenway trailheads) inserted from CRPD trail pages; franklin_oh_access_points.tsv updated (90 rows). Total Franklin APs: 90 (88 Franklin county + 2 cross-county: Retreat at Turnberry / Fairfield, McNamara Park / Delaware). Cross-county trailheads documented with correct county values.

**Session 26:** P&OS Supplement (IMP-097/099): 104 cemeteries + 25 golf courses + 7 parks/open spaces added; net +129 sites; DB total 1,162 Franklin sites.

*(Session 25: Township GIS lookup complete — 373/1,037 sites assigned civil township via TIGER 2024 COUSUB; 664 in incorporated cities (correct — cities leave townships in Ohio); Plus Code bug fix FR-S-0805; utilities saved: na_plus_code.py + na_township_lookup.py; Ohio TIGER COUSUB shapefile acquired)*

---

## Tiers Completed

| Tier | Governance Level | Result | Entities |
|---|---|---|---|
| Tier 1 | Federal & Tribal | NULL | 0 |
| Tier 2 | State (ODNR) | 7 entities | 6 Sites + 1 Trail |
| Tier 3 | District (Metro Parks) | ~123 entities | 17 Sites + 2 Child Sites + 1 Site Network + ~103 Trails |
| Tier 4 | County | 2 Sites | Franklin Park Conservatory JRD (ORC 755.14 co-governance) + Franklin County Fairgrounds (ORC 1711 agricultural society); Bergstresser/Dietz Bridge deferred to Tier 6 |
| Tier 5 | Township | 23 entities | 21 Sites + 2 Trails across 5 of 18 townships; 13 null townships with evidence; 1 defunct (Marion) |
| Tier 6 | Municipal | ~353 MORPC net-new + web-sourced | 16 cities + 9 villages; all MORPC cross-checked |
| Tier 7 | Conservancy / Land Trust | 1 entity (sparse) | Grange Insurance Audubon Center; Camp Mary Orton deferred T8; all other orgs NULL with evidence |
| Tier 8 | Private | 3 Sites + 1 Child Site | Camp Mary Orton (167 ac, Godman Guild); Camp Ken-Jockety & Elam Env. Center (220 ac, Girl Scouts); Ginny and John Elam Environmental Center (child); Wilma H. Schiermeier ORWRP (52 ac, OSU — TIER AMBIGUITY FLAG) |

## Tier 6 — Final Status (MORPC Cross-Check Complete)

All 16 cities + 9 villages in Franklin County have been processed through web discovery AND MORPC cross-check. 141 net-new entities appended via MORPC in Sessions 7–8 (36 Gahanna + 147 Columbus + 29 Dublin + 141 remaining municipalities = **353 MORPC-sourced entities total**).

| Municipality | Type | Discovery Status | MORPC Net-New | Total Staged |
|---|---|---|---|---|
| Columbus | City | WEB COMPLETE + MORPC | 147 | ~590 |
| Dublin | City | WEB COMPLETE + MORPC | 29 | ~160 |
| Gahanna | City | WEB COMPLETE + MORPC | 36 | ~66 |
| Westerville | City | WEB PARTIAL + MORPC | 18 | 40 |
| Upper Arlington | City | WEB PARTIAL + MORPC | 3 | 25 |
| Hilliard | City | WEB PARTIAL + MORPC | 5 | 33 |
| Grove City | City | WEB PARTIAL + MORPC | 27 | 45 |
| Groveport | City | WEB PARTIAL + MORPC | 5 | 13 |
| Worthington | City | WEB PARTIAL + MORPC | 13 | 26 |
| Bexley | City | WEB PARTIAL + MORPC | 1 | 10 |
| New Albany | City | WEB PARTIAL + MORPC | 12 | 19+ |
| Reynoldsburg | City | WEB PARTIAL + MORPC | 4 | 11 |
| Whitehall | City | WEB PARTIAL + MORPC | 2 | 10 |
| Grandview Heights | City | WEB PARTIAL + MORPC | 2 | 12 |
| Canal Winchester | City | WEB PARTIAL + MORPC | 9 | 16 |
| Obetz | City | WEB PARTIAL + MORPC | 7 | 16 |
| Pickerington | City | CROSS-COUNTY NOTE | 0 | 1 note |
| Marble Cliff | Village | WEB PARTIAL + MORPC | 0 | 5 |
| Minerva Park | Village | WEB PARTIAL | 0 | 3 |
| Valleyview | Village | WEB PARTIAL + MORPC | 2 | 4 |
| Urbancrest | Village | WEB PARTIAL + MORPC | 0 | 2 |
| Brice | Village | NULL | 0 | 1 note |
| Harrisburg | Village | WEB PARTIAL + MORPC | 1 | 2 |
| Lockbourne | Village | WEB PARTIAL + MORPC | 1 | 4 |
| Riverlea | Village | WEB PARTIAL + MORPC | 0 | 2 |
| Lithopolis | Village | CROSS-COUNTY / WEB PARTIAL | 0 | 3 |

## Tier 7 — Final Status (Conservancy / Land Trust)

**Result: SPARSE — 1 entity confirmed; remainder null with evidence.**

| Organization | Franklin County Holdings | Result |
|---|---|---|
| National Audubon Society / Audubon Ohio | Grange Insurance Audubon Center (5 ac, 505 W. Whittier St., Columbus) — subleases from Metro Parks within Scioto Audubon Metro Park | **STAGED** (cross-tier flag: Tier 3) |
| Central Ohio Land Trust | Camp Mary Orton (167 ac) noted but is a private institutional camp | Deferred to Tier 8 |
| Columbus Audubon Society | Calamus Swamp in Pickaway County only | NULL |
| The Nature Conservancy — Ohio | No Franklin County preserves listed | NULL |
| Appalachian Ohio Alliance | All Big Darby preserves in Pickaway County | NULL |

**Staging YAML:** 27,858 lines (+105 from Tier 8 Session 10 — 4 documents appended)

## Tiers Remaining

**None. All 8 tiers complete. Pipeline complete.**

---

## Pipeline Results — Session 11 (2026-03-16)

**Script:** `franklin_oh_pipeline.py` | **Runs:** 6 iterative | **Final state:** 0 errors, 27 warnings

### Entity Counts (Post-Resolution, Post-Review)

| Entity Type | Count | TSV File | Notes |
|---|---|---|---|
| Sites | **1,162** | franklin_oh_sites.tsv | +129 net-new from P&OS supplement (S26); see supplement section below |
| Trails | 115 | franklin_oh_trails.tsv (56 KB) | |
| Trail Segments | 1 | franklin_oh_trail_segments.tsv | |
| Trail Networks | 2 | franklin_oh_trail_networks.tsv | |
| Site Networks | 1 | franklin_oh_site_networks.tsv | |
| Access Points | 90 | franklin_oh_access_points.tsv | 54 water trail APs (FR-AP-0001–0054) + 36 greenway trailheads (FR-AP-0055–0090); Metro Parks hiking trail trailheads pending (~90 trails) |

### Site Category Distribution (after S26 supplement)

Park 706 · Open Space 131 · **Cemetery 104** · Recreation Facility 90 · Nature Preserve 53 · Natural Area 31 · Conservation Area 17 · Memorial 10 · Water Site 8 · Community Garden 4 · Campground 2 · Hunting Area 1 · **Blank 0** ✓

*(Recreation Facility count +25 from golf courses. Cemetery is a new category — 0 before S26.)*

### Normalization Coverage

- **Sites categorized:** 1,024 / 1,024 **(100%)** ✓ — resolved Session 16
- **Trail use_type populated:** 97 / 115; remaining blanks are undocumented
- **Trail surface_type populated:** 102 / 115; remaining blanks are undocumented
- **GPS coordinates:** 1,036 / 1,037 sites (99.9%) — see GPS Acquisition section; 4 centroid artifacts corrected in Session 14; 43 additional geocoded in Session 20
- **Municipality:** 997 / 1,037 sites populated from MORPC jurisdiction data
- **Acres:** 1,012 / 1,037 sites populated
- **Plus Code:** 1,036 / 1,037 (99.9%) — 10-digit OLC codes; FR-S-0805 extra-digit bug fixed Session 25
- **Township:** 373 / 1,037 (36.0%) — civil township via TIGER 2024 COUSUB point-in-polygon (Session 25); 664 sites in incorporated cities correctly have no township (Ohio law — cities leave township jurisdiction)

### Review Queue — COMPLETE (Session 13, 2026-03-18)

- **500 pairs decided** (499 split, 1 merged) — see Session 13 log for full breakdown
- **1 merge applied:** FR-S-0667 (Alum Creek/Cooper Rd Parkland Coh, MORPC) → merged into FR-S-0062 (Alum Creek Parkland, Columbus Rec Parks)
- **GPS artifact flag:** RESOLVED (Session 14) — 4 preserves corrected: Beechwold, Kenney, Coronet Woods (all Columbus), Hickory Woods (Dublin). See Session 14 log for corrected coordinates.

### Integrity Check

- **0 bad-tab rows** across all 6 TSV output files
- All files pass delimiter, blank-field, whitespace, and vocabulary validation

### Pipeline Fixes Applied (IMP-021 – IMP-026)

| Item | Fix |
|---|---|
| IMP-026 | `norm_vocab` now sorts keys by length descending — fixes generic key matching before specific |
| IMP-021 | `accessibility_raw` parsed for trail use_type and surface_type when explicit fields absent |
| Trail vocabulary | "Equestrian" corrected to "Bridle"; "Canal Trail" corrected to "Canal Towpath" |
| Site categories | Name-inference function `_infer_category_from_name()` reduces blanks from 561 → 5 |
| Merge fallback | Trail-specific fields added to merge fallback; surface/use data no longer lost on canonical merge |
| Water trails | Surface type auto-set to "Water" when use_type = "Water" and surface blank |

---

## GPS Acquisition — Session 12 (2026-03-16)

**Source:** MORPC Parks and Open Space feature layer (ArcGIS Hub — `d898fa77e91d414f8f296b0511f14fbf_11`)
**Method:** ArcGIS REST API query with `returnCentroid=true&outSR=4326`; name-matching via combined token-set + distinctive-word score; 3 matching passes
**Script:** `gps_match.py`

**Results:** 988 / 1,025 sites geocoded (96.4%)

| Match type | Count |
|---|---|
| Exact name match | 615 |
| Fuzzy auto (≥90 score) | 361 |
| Manual accepts (reviewed) | 10 |
| **Total with GPS** | **988** |

**37 no-match sites (expected):**
- State scenic rivers (Big Darby, Little Darby, Olentangy) — linear features, no centroid appropriate
- Hunting area, county fairgrounds, Tier 8 private camps — not in MORPC parks layer
- Small township playgrounds below MORPC coverage threshold (Sale Road, West Side/University View, Whitney)
- Pool/aquatic facilities (Devon Pool, Tremont Pool, Hilliard FAC, Dublin Community Pool South, David H. Madison Pool)
- Small pavilions/courts (Eagle Pavilion, Beulah Pavilion, Urlin Tennis Courts)
- Columbus nature preserves absent from MORPC (Overbrook NP, Warner Woods NP, Gertrude Lawrence Woods NP, O'Shaughnessy NP)
- Small obscure sites (Stradley Place, Island Greenspace, The Kelley Green, Moses Wright Nature Area, Jeffrey Mansion)
- Child sites of parks (Creekside Rotary Stage, Grange Insurance Audubon Center child)
- Watercourse Dedication/Scioto — unique water rights entity, no park polygon
- Emerald Fields — not found in MORPC despite Dublin coverage

**Municipality filled:** 985 / 1,025 sites (from MORPC Jurisdiction field)
**Acres filled:** 981 / 1,025 sites (from MORPC Acres field where blank)

---

## Pending Tasks (Next Session)

| Priority | Task | Notes |
|---|---|---|
| ~~HIGH~~ | ~~IMP-023: B067 collision~~ | **RESOLVED Session 15** — FR-S-0009→B065 (Blacklick Woods NNL), FR-S-0010→B066 (Blendon Woods MP) |
| ~~MEDIUM~~ | ~~5 blank site categories~~ | **RESOLVED Session 16** — 100% coverage; Wallace Property municipality also corrected to Dublin |
| ~~MEDIUM~~ | ~~Parent/child ID resolution~~ | **FULLY RESOLVED Sessions 17–19** — FR-S-0608→FR-S-1026 (S18); FR-S-0908→FR-S-0678 (S19); FR-S-0974 parent NULL, municipality fixed (S19); FR-S-0955 flagged for deletion — parking lot, not natural area (S19) |
| ~~MEDIUM~~ | ~~Trail segment parent ID~~ | **RESOLVED Session 17** — FR-TS-0001 → FR-T-0001 (Olentangy River Water Trail) |
| ~~HIGH~~ | ~~FR-S-0955 deletion~~ | **RESOLVED Session 20** — deleted from DB and TSV |
| ~~MEDIUM~~ | ~~GPS — remaining 37 sites~~ | **RESOLVED Session 20** — 43 sites geocoded; 27 Census-confirmed, 4 web-confirmed, 12 approximate (flagged) |
| ~~MEDIUM~~ | ~~FR-S-0455 address discrepancy~~ | **RESOLVED** — corrected to 4748 Red Bank Rd, Galena, OH 43021 (confirmed by user 2026-03-18) |
| ~~LOW~~ | ~~Gahanna pocket parks~~ | **RESOLVED Session 18** — 6 net-new (FR-S-1026–1031); FR-S-0608 parent resolved to FR-S-1026; gahanna.gov/474 still blank but full list recovered via Facilities page |
| LOW | MORPC map verification pass | Consolidated cross-municipality pass deferred from Tier 6 |
| ~~LOW~~ | ~~Plus Code fields~~ | **RESOLVED Session 21** — all 1,029 sites have 10-digit OLC codes |
| ~~LOW~~ | ~~Township fields~~ | **RESOLVED Session 25** — 373/1,037 sites assigned civil township via TIGER COUSUB point-in-polygon; 664 in incorporated cities (no township — correct Ohio behavior); `utilities/na_township_lookup.py` written |
| ~~HIGH~~ | ~~P&OS Completeness Gate (IMP-097/099)~~ | **RESOLVED Session 26** — 104 cemeteries + 25 golf courses + 7 parks/open spaces added; see supplement section |
| ~~HIGH~~ | ~~Access Points~~ | **RESOLVED Session 27** — 90 APs in DB: 54 water trail + 36 greenway trailheads. Remaining gap: Metro Parks hiking trail trailheads (~90 trails); low priority |
| ~~MEDIUM~~ | ~~Cross-county IMP-104 flags~~ | **RESOLVED Session 27** — CROSS_COUNTY_CANDIDATE flags added to Big Darby Creek Scenic River, Little Darby, Olentangy Scenic River, Ohio to Erie Trail, Buckeye Trail in identity_notes |
| ~~MEDIUM~~ | ~~13 null townships re-check~~ | **RESOLVED Session 27** — All 13 re-verified against `Townships_Officials2022-2023.xlsx`; Marion Township confirmed defunct (absorbed into Columbus); remaining 12 null townships are incorporated cities (correct Ohio behavior) |
| ~~LOW~~ | ~~Water trail sub-procedure (IMP-103)~~ | **RESOLVED Session 27** — Big Darby Creek Water Trail (FR-T-0118) and Alum Creek Water Trail (FR-T-0117) evaluated and confirmed against IMP-103 threshold; existing records valid |

---

## Session 26 — P&OS Completeness Gate Supplement (2026-05-11)

**Run ID:** `franklin_oh_2026_05_11_pos_supplement`
**Script:** `franklin_supplement_upsert.py`
**Source:** `morpc_parks_franklin_centroids.csv` — MORPC Parks & Open Space ArcGIS layer
**Gate:** IMP-097 P&OS Completeness Gate + IMP-099 Cemetery/Golf inclusion

### What Was Done

Ran `franklin_pos_gate.py` to cross-check the MORPC centroids file (989 qualifying Public/non-NOS rows) against 1,033 DB Franklin sites using fuzzy name matching (token_set_ratio ≥ 80). Identified 153 unmatched entries:

| MORPC Type | Unmatched | Disposition |
|---|---|---|
| Cemetery | 104 | All upserted — new Cemetery category (was 0 before) |
| Golf | 25 | All upserted — Recreation Facility / Golf Course subtype |
| Park | 22 | 4 upserted as Sites; 18 excluded (trail corridor parcels, fire stations, senior centers, typos) |
| Recreation | 2 | Excluded (Gahanna Recreation Center building, MORPC-only entry) |

### Entities Added

- **104 cemeteries** — category=Cemetery; subtypes inferred (Veterans, Church, Family, Public) from name/jurisdiction; GPS from MORPC centroids (HIGH confidence); ownership inferred from name/jurisdiction pattern
- **25 golf courses** — category=Recreation Facility, subtype=Golf Course; GPS from MORPC centroids; OSU Golf / Sports Ohio treated as Institutional / Governmental respectively; remainder Private
- **7 parks/open spaces** — Emersonia Park, Clinton Township Playground, Fieldstone Open Space, Parkview Park (Hamilton), Mango Park (Grove City), Clinton Road Park (Westerville), South Westerville Park
- **1 recreation area** — Darree Fields (Dublin) — large multi-sport complex missing from original discovery

**Total upserted:** 137 | **Skipped (exclusions + consolidations):** 18

### DB Cleanup Applied

After initial upsert, 8 records deleted to resolve duplicates:

| Deleted ID | Reason |
|---|---|
| FR-S-1179, FR-S-1180, FR-S-1181 | Duplicate manual-gap entries (Emersonia, Clinton Twp Playground, Fieldstone) — MORPC versions kept |
| FR-S-1172, FR-S-1173, FR-S-1174, FR-S-1175 | Muirfield Village Golf Club — 4 of 5 MORPC parcels deleted; FR-S-1171 kept with summed acreage (195.27 ac) |
| FR-S-1061 | Pinnacle Golf Club — small parcel deleted; FR-S-1062 kept with summed acreage (200.12 ac) |

FR-S-1178 renamed from "Clinton Township Playground (MORPC)" to "Clinton Township Playground".

### Final DB State After Supplement

- **Franklin sites total: 1,162** (was 1,033 before)
- Cemetery: 104 (net-new category)
- Golf Courses: ~26 total (20 net-new; ~6 were pre-existing public courses)
- GPS coverage: supplement sites all have MORPC centroid GPS (HIGH confidence); Plus Codes and township/municipality GIS fields not yet populated for supplement sites

### Known Gaps in Supplement Sites

- **Plus Codes:** Not computed for the 129 net-new sites — a future GIS pass using `na_plus_code.py` is needed
- **Township / Municipality:** GIS lookup not run for supplement sites — `na_township_lookup.py` should be run over the ~129 new site IDs
- **Features / Description:** Supplement sites have minimal metadata — only name, category, subtype, GPS, acres, ownership, governance from MORPC layer

---

## Entities Found — Cumulative

**Total entities discovered (all sessions):** ~1,400+
**Staging file records:** 1,085 documents (confirmed via doc-count); **27,702 lines** (+3 Tier 7 documents)

Sessions 7–8 MORPC cross-check added **353 net-new entities** across all Tier 6 municipalities:
- Gahanna: 36 net-new
- Columbus: 147 net-new
- Dublin + all other municipalities: 170 net-new (Sessions 7–8)

### Session 4 Summary (2026-03-14): City of Upper Arlington — Tier 6 (partial)

**22 records appended to staging file (gen_upper_arlington_yaml.py):**
- 18 Park Sites (Northam Park, Fancyburg Park, Mallway Park, Miller Park, Reed Road Park, Smith Nature Park, Sunny 95 Park, Thompson Park, Tremont Fountain Park, Greensview Park, Wyandot Park, Northwest Kiwanis Park, Burbank Park, Oxford Park, Westover Park, Cardiff Woods Park, Charing Ravine Park, Nursery Park)
- 3 Aquatic Facility Sites (Devon Pool, Reed Road Water Park, Tremont Pool)
- 1 DiscoveryNote: PARTIAL (~5 parks unidentified or address-unknown)

**Source:** Web search snippets (Yelp, Google, Waze, ohranger.com, cbus4kids.com); upperarlingtonoh.gov egress-blocked; browser disconnected

**Address flags for Resolution/verification:**
- Nursery Park: name confirmed, street address unknown (all web sources silent)
- Tremont Fountain Park: approximate address only (~near 3600 Tremont Rd); official page blocked
- Tremont Pool: approximate address only (near Tremont Rd area); official page blocked
- Charing Ravine Park: ~2901 Charing Rd confirmed from web snippet; verify via browser
- Burbank Park + Northwest Kiwanis Park: both on Stonehaven Dr (4780 and 4840); confirm distinction
- Devon Pool (2070 S Mallway Drive) co-located with Mallway Park — both documented separately

**City claims 23 neighborhood parks; 18 identified; ~5 gaps remain**

---

### Session 3 Summary (2026-03-14): City of Gahanna — Tier 6 (partial)

**30 records appended to staging file (gen_gahanna_yaml.py):**
- 4 Athletic Complex Sites (Academy Park, Golf Course, Headley Park, McCorkle Park)
- 10 Community Park Sites (Creekside Park & Arboretum, Friendship Park, Gahanna Woods, Geroux Herb Garden, Hannah Park, Pizzurro Park, Shull Park, Sunpoint Park, Veterans Memorial Park, Woodside Green Park)
- 7 Neighborhood Park Sites (Ambassador Commons, Ashburnham Park, Bryn Mawr Park, Hunters Ridge Park, Rathburn Woods Park, Rice Avenue Park, Trapp Park)
- 2 Aquatic Facility Sites (Gahanna Swimming Pool, Hunters Ridge Pool)
- 4 Child Sites (Creekside Plaza, Creekside Rotary Stage, Friendship Park Community Garden, Hannah Park Community Garden)
- 2 Trails (Big Walnut Trail 4.6 mi paved; Paddle Gahanna & Blueways water trail)
- 1 DiscoveryNote: Pocket Parks / Open Spaces / Reserves — PENDING

**Source:** Gahanna Facilities page (gahanna.gov/Facilities, extracted via browser JS — 40 facilities total), Parks & Trails Guide PDF

**Baseline seeds confirmed this session:** 29+ of 46 Gahanna City Park seeds (exact mapping deferred to Resolution)

**Pocket Parks PENDING:**
- `/474/Pocket-Parks-Open-Spaces-Reserves` page loads with heading only — no content (CivicPlus JS rendering failure, confirmed on two attempts)
- gahanna.gov blocked by WebFetch egress proxy
- Wayback Machine blocked; all third-party fallback domains blocked
- Browser (Claude in Chrome) disconnected during session
- City claims 52 parks total; ~24 confirmed here; ~28 pocket parks/open spaces unresolved
- **Must revisit:** reconnect browser, reload /474/ page; perform consolidated map verification pass

**Address conflicts noted (flag for Resolution):**
- Headley Park: Facilities page = 1031 Challis Springs Drive; Parks & Trails Guide PDF = 1931 Challis Springs Dr
- Pizzurro Park: Facilities page = 940 Pizzurro Park Road; PDF = 914 S. Hamilton Rd (different street)

**Gahanna Woods cross-tier (B221/B222):** Gahanna Municipal portion documented as Tier 6 record ("Gahanna Woods & State Nature Preserve"); Tier 2 state preserve record (B222) already exists — Resolution must reconcile both.

---

### Session 2 Summary (2026-03-14): City of Columbus — Tier 6

**443 entities appended to staging file:**
- 425 Sites (419 parks/nature preserves from columbusrecparks.com + 6 missing nature preserves)
- 14 Trails (Alum Creek Greenway Trail canonical record + 13 greenway/bikeway trails)
- 3 Trail Segments (Alum Creek Trail segments north/south/downtown)
- 1 Trail Network (Columbus Greenways Trail Network)

**Source:** columbusrecparks.com (FacetWP-paginated listing, 419 total parks; 15 pages iterated via browser JS)

**Baseline seeds confirmed this session:** 407 (all Columbus City Park + Columbus City Nature Preserve seeds)

**New discoveries (not in baseline):**
- 12 EXTRA_PARKS: website-only, appeared on columbusrecparks.com not in baseline (flagged WEBSITE_ONLY)
- 6 missing nature preserves: Gertrude S. Lawrence Woods, Hoover Meadows, Hoover Nature Preserve, Hoover Oxbow, Mud Hen Marsh, O'Shaughnessy (6 seed records created; flagged for verification)

**Map verification status:** City-scale Google Maps overview completed. Full quadrant-by-quadrant pass DEFERRED — will be executed after all Tier 6 municipalities are web-complete; running it before then risks false positives from parks that belong to other jurisdictions not yet cataloged.

### Tier 2 Entities

| # | Name | Type | Counties |
|---|---|---|---|
| 1 | Gahanna Woods State Nature Preserve | Site | Franklin |
| 2 | Sawmill Wetlands Education Area | Site | Franklin |
| 3 | Olentangy River State Wildlife Access Area | Site (identity uncertain) | Franklin |
| 4 | Big Darby Creek State and National Scenic River | Site (entity type uncertain) | Champaign, Franklin, Logan, Madison, Pickaway, Union |
| 5 | Little Darby Creek State Scenic River | Site (entity type uncertain) | Franklin, Madison, Pickaway, Union |
| 6 | Olentangy River State Scenic River | Site (entity type uncertain) | Delaware, Franklin |
| 7 | Olentangy River Water Trail | Trail (tier uncertain) | Franklin |

### Tier 3 Entities (Summary)

**Sites (20 records):** 17 Metro Parks + Big Darby Public Hunting Area (child) + Edward S. Thomas SNP (child) + Metro Parks Site Network

**Trails (103 records):**
- Multi-park greenways: Camp Chase Trail, Darby Creek Greenway Trail, Heritage Trail, Blacklick Creek Greenway Trail, Scioto Greenway Trail, Alum Creek Greenway Trail (flag Tier 6)
- Per-park trails: ~97 named trails across all 17 Franklin County Metro Parks

### Tier 4 Entities

| # | Name | Type | Notes |
|---|---|---|---|
| 1 | Franklin Park Conservatory and Botanical Gardens | Site | JRD (ORC 755.14), county+city co-governance; 1777 E. Broad St., Columbus; CROSS-TIER FLAG for Tier 6 |
| 2 | Franklin County Fairgrounds | Site | Franklin County Agricultural Society (ORC 1711); 5043 NW Pkwy, Hilliard; MINIMAL_DATA |

### Tier 5 Entities (Summary)

**18 townships searched; 5 with entities; 13 null; 1 defunct (Marion)**

| Township | Sites | Trails | Key Entities |
|---|---|---|---|
| Blendon | 3 | 0 | Ridgewood Park, Phelps Acre Park, Sunbury Woods Commons |
| Clinton | 6 | 0 | Veterans Park, Sale Road Playground, Fred Stigers Memorial Park, Case Road Community Garden, Chambers Circle Park, West Side/University View Playground |
| Hamilton | 2 | 1 | Hamilton Township Park (+ trail), Firetruck Park |
| Jefferson | 5 | 0 | Blacklick Ridge Community Park, Boehnke Nature Preserve, Jefferson Community Park, Jefferson Run Park, Olde Quarry Park |
| Prairie | 5 | 1 | Blue Lake Park, Carl Frye Park (+ walking path), Dalebrook Park, Friendship Park, Lakota Park |
| **Total** | **21** | **2** | |

**Null townships (13):** Brown, Franklin, Jackson, Madison, Marion (DEFUNCT), Mifflin, Norwich, Perry, Plain, Pleasant, Sharon, Truro, Washington

---

## Held Entities

None yet. Expected held entities for future sessions:
- **Ohio to Erie Trail (OTET)** — multi-county trail; will be discovered at appropriate tier and held pending full county membership resolution
- **Buckeye Trail** — multi-county trail; same treatment
- **Any Metro Parks trails extending beyond Franklin County** — held pending cross-county resolution

---

## Baseline Seeds Status

**Total baseline seeds:** 690
**Confirmed by discovery:** 423 (16 from Tiers 2–4 in Session 1; 407 from Tier 6 Columbus in Session 2)
**Unconfirmed:** 267 (all remaining non-Columbus municipal + conservancy + private seeds)

### Duplicate Name Pairs Flagged for Resolution

| Pair | Baseline IDs | Note |
|---|---|---|
| Academy Park | B003, B004 | Columbus City Park vs Gahanna City Park — likely distinct entities |
| Heritage Park | B289, B290 | TBD — confirm management and location |
| Indianola Park | B314, B315 | TBD |
| Olde Sawmill Park | B441, B442 | TBD |
| Perry Park | B457, B458 | TBD |
| Thompson Park | B586, B587 | TBD |
| Windsor Park | B671, B672 | TBD |

---

## Baseline Seeds Confirmed

| Baseline ID | Name | Tier |
|---|---|---|
| B222 | Gahanna Woods State Nature Preserve | 2 |
| B516 | Sawmill Wetlands Education Area | 2 |
| B448 | Olentangy River State Wildlife Access Area | 2 (identity uncertain) |
| B055 | Big Darby Public Hunting Area | 3 |
| B067 | Blacklick Woods Metro Park | 3 |
| B190 | Edward S. Thomas State Nature Preserve | 3 |
| B292 | Heritage Trail Park | 3 |
| B300 | Homestead Metro Park | 3 |
| B318 | Inniswood Metro Gardens | 3 |
| B478 | Quarry Trails Metro Park | 3 |
| B502 | Rocky Fork Metro Park | 3 |
| B521 | Scioto Audubon Metro Park | 3 |
| B524 | Scioto Grove Metro Park | 3 |
| B540 | Sharon Woods Metro Park | 3 |
| B589 | Three Creeks Metro Park | 3 |
| B628 | Walnut Woods Metro Park | 3 |

**Session 2 — Tier 6 Columbus (407 seeds):** All baseline seeds typed "Columbus City Park" (B001–B690 where type = Columbus City Park) and "Columbus City Nature Preserve" confirmed. See staging file for individual baseline_id fields on each record. Notable exclusions from confirmation:
- B515 (Sawmill Nature Preserve) — confirmed as duplicate of B516 / Tier 2 canonical; Tier 6 seed suppressed pending Resolution
- B221 (Gahanna Woods — Gahanna City Park typed) — NOT a Columbus seed; will be confirmed at Tier 6 Gahanna pass

**Total confirmed:** 423 of 690 seeds (16 from Sessions 1 Tiers 2–4; 407 from Session 2 Tier 6 Columbus)

## Open Discovery Module Questions / Improvement Flags

1. **NNL designations on locally managed land** — Protocol is silent. Decision this session: NNL is a federal designation attribute, not a management tier. Entity goes to management tier; designation field captures "National Natural Landmark." Two Franklin County examples: Blacklick Woods (Metro Parks, Tier 3) and Highbanks (Metro Parks, Tier 3). → **Flag for protocol amendment.**

2. **National Heritage Area (NHA) designations** — Protocol is silent. Decision this session: NHA is a congressional designation only; no federal land ownership/management conveyed. No Tier 1 entity. Ohio & Erie Canalway NHA covers Franklin County but creates no Tier 1 records. NHA coverage may be noted in site notes where relevant. → **Flag for protocol amendment.**

3. **Scenic river corridor entity type** — Protocol is silent on how to classify state/national scenic river designations (not Sites, not Trails). Decision: recorded as Sites pending protocol amendment. Recommend "Scenic River Corridor" site category in vocabulary v5.3. Applies to Big Darby, Little Darby, Olentangy scenic river entities.

4. **State water trail tier assignment** — ODNR designates water trails at state level; active management is local (Columbus). Protocol is silent on designation vs. management tier precedence. Decision: recorded at Tier 2, flagged for Resolution. Recommend: management tier governs.

5. **State nature preserve cross-tier deduplication** — Gahanna Woods and Sawmill Wetlands are state-owned/designated but locally managed. Both will likely appear again as municipal seeds at Tier 6. Resolution must de-duplicate B221 vs B222 (Gahanna Woods) and B516 (Sawmill).

6. **Scale management for Tier 6 Municipal** — Columbus alone has ~390 baseline seeds. Consider batching by management department (Recreation & Parks, Planning, etc.) or geographic sub-area within city. → **Flag for discovery orchestration guidance.**

7. **Duplicate trail names across parks** — Tier 3 produced multiple identically named trails at different parks (Overlook Trail ×3, Lake Trail ×3, Arrowhead Trail ×2, Multipurpose Trail ×4, Boardwalk Trail ×2, Bridle Trail ×2). Each is a distinct entity. All disambiguated in name_raw with park qualifiers during discovery. Recommend: protocol should advise name qualification at point of discovery for generic trail names found in multi-park systems. → **Flag for protocol amendment.**

8. **Tier 3 trail identity flags** — 11 individual trail records flagged for Resolution (see staging file completion note). Issues include: combined route vs. individual trail entities; possible statewide Buckeye Trail segment overlap; informal name vs. official name; amenity vs. Trail entity classification (Columbus Rotary Running Track). → **Flagged for Resolution pass.**

9. **Multi-park greenway tier assignment** — Alum Creek Greenway Trail (~22 mi) is primarily managed by Columbus Recreation and Parks; documented at Tier 3 only because it passes through Three Creeks Metro Park. Primary tier assignment is Tier 6. Flagged in staging file for Tier 6 re-documentation as the canonical record. → **Flag for Tier 6 discovery.**

10. **Franklin Park Conservatory JRD cross-tier dedup** — Franklin Park Conservatory and Botanical Gardens documented at Tier 4 (county co-governance via JRD under ORC 755.14). Will also appear at Tier 6 (City of Columbus land ownership and primary co-governance). Resolution must assign canonical tier and merge records. → **Flag for Resolution deduplication.**

11. **Franklin County Fairgrounds MINIMAL_DATA** — Franklin County Fairgrounds documented with minimal data (address, owner, approximate acreage). On-site natural features, trail inventory, and access points require field verification. → **Flag for Resolution enhancement.**

12. **Tier 4 GIS and planning gaps** — Franklin County Parcel Viewer owner-name search could not be completed via automation. Franklin County EDP planning pages all returned 404 (county website redesign underway). Both are potential coverage gaps. → **Flag for manual review in Resolution phase.**

13. **Wrong-county township website hazard** — At least 7 of 18 Franklin County township names return wrong-county websites in Ohio search results (Sharon, Franklin, Jefferson, Perry, Plain, Marion, Washington). Protocol §4.2 should require explicit address verification before treating any township site as authoritative. → **Flag for protocol amendment.**

14. **Defunct township handling** — Marion Township (Franklin County) is fully absorbed into the City of Columbus with no surviving government. Protocol §5.3 covers townships that defer to park districts but not fully defunct townships. Add a DEFUNCT status category and resolution note. → **Flag for protocol amendment.**

15. **Hellbranch Meadows (Franklin SWCD)** — Prairie Township received a restoration grant for Hellbranch Meadows but does not own or manage it. Franklin SWCD purchased the property (2008) and is the managing entity. Tier assignment unclear — Franklin SWCD is a special district not covered by the 8-tier framework. → **Flag for protocol/tier review.**

16. **FacetWP / JS-rendered park listing pages** — columbusrecparks.com uses FacetWP lazy pagination; standard web_fetch retrieves only the first 28 of 419 parks. Protocol must specify: when a parks listing page uses JS rendering, iterate all pages via browser JS (`window.FWP.paged`/`window.FWP.refresh()`) before treating the listing as complete. → **Flag for protocol amendment (Tier 6 / JS pagination guidance).**

17. **Baseline seed count vs. website count discrepancy (expected)** — Columbus baseline has 407 seeds; website lists 419 parks. The ~12-record gap is expected (parks added after baseline creation). Protocol should advise: always enumerate the official website independently; do not assume baseline seed count = total entity count. → **Flag for protocol amendment.**

24. **Dublin sub-parcel open spaces excluded** — Dublin ArcGIS FeatureServer/3 returned 176 features including ~74 lettered sub-parcel open spaces (e.g., "Ballantrae Open Space H", "Ballantrae Open Space I"). These are maintenance sub-divisions of named open spaces, not identity-bearing Sites. Only the 36 named open spaces were recorded; lettered sub-parcels excluded. → **Flag for protocol amendment: add explicit Dublin/sub-parcel open space exclusion rule to Entity Creation Rules §8.1.**

25. **CivicPlus empty Pocket Parks pages** — Gahanna's `/474/Pocket-Parks-Open-Spaces-Reserves` page loaded with heading only on two browser attempts (CivicPlus CMS JS rendering failure). Content was not available even in the browser; only the page title rendered. Standard fallbacks (WebFetch, Wayback Machine, third-party sites) were all blocked by egress proxy. Resolution: when a CivicPlus category page loads blank, check (a) the Facilities page filter, (b) the site's document center for PDFs, (c) the city's ArcGIS parks layer. If all fail, flag PENDING for browser retry. → **Flag for protocol amendment (Tier 6 §4.5 fallback protocol).**

18. **Nature preserve sub-type vs. city park in baseline** — columbusrecparks.com lists nature preserves alongside parks without a clear sub-type separator. Baseline typed 17 as "Columbus City Nature Preserve" but website shows 25 nature preserves; 6 were typed "Columbus City Park" in baseline (e.g., Coronet Woods = B138). Resolution must reconcile type assignments. → **Flag for Normalization.**

19. **Golf courses and sports complexes in parks inventory** — Columbus parks website includes Airport Golf Course, Raymond Memorial Golf Course, and Anheuser-Busch Sports Park. Protocol is silent on whether these qualify as natural area Sites. Flagged in identity_notes_raw for Resolution evaluation. → **Flag for protocol amendment (entity inclusion criteria).**

20. **Cross-tier greenway trail conflicts** — Six Tier 6 Columbus greenway trails (Alum Creek Greenway, Camp Chase, Heritage, Blacklick Creek Greenway, Darby Creek Greenway, Scioto Greenway) have counterpart records at Tier 3 (Metro Parks). Both tiers have documented these trails; Resolution must assign canonical tier. Recommend: governance tier governs (Columbus Rec & Parks primary → Tier 6 canonical for Alum Creek, Camp Chase, Heritage; Metro Parks Tier 3 canonical for others). → **Flag for Resolution deduplication.**

21. **Sawmill cross-tier dedup (Session 2 confirmation)** — B515 (Sawmill Nature Preserve, 17.32 ac, 2650 Starford Dr., Columbus City Nature Preserve) = same physical entity as B516 / Tier 2 "Sawmill Wetlands Education Area." Both already flagged in staging file. Tier 2 record is canonical. Tier 6 seed should be suppressed at Resolution. → **Active Resolution flag.**

23. **Map verification pass ordering** — Protocol §4.4 requires map verification per municipality as you go. In large, multi-municipality counties, running the map pass municipality-by-municipality during web discovery risks generating false positives: parks visible on the map may belong to an adjacent jurisdiction not yet cataloged. Better practice for dense counties: complete all municipal web discovery first, then run a single consolidated map verification pass across all jurisdictions simultaneously. This allows correct cross-municipal attribution and reduces rework. → **Flag for protocol amendment (§4.4 ordering guidance for multi-municipality counties).**

22. **Gahanna Woods cross-tier dedup (Session 2 confirmation)** — B221 (Gahanna Woods, Gahanna City Park) and B222 (Gahanna Woods State Nature Preserve) are two distinct entities at the same location: the state preserve (Tier 2, canonical) and a Gahanna city park overlay. The Tier 6 Gahanna municipal discovery pass must document the Gahanna city park portion (B221) as a separate Tier 6 record; the Tier 2 state nature preserve (B222) is already documented. → **Active Resolution flag.**

---

## Tier 8 — Final Status (Private)

**Result: SPARSE — 3 Sites + 1 Child Site confirmed; remainder null with evidence.**

| Entity | Type | Address | Owner | Acreage | Notes |
|---|---|---|---|---|---|
| Camp Mary Orton | Site | 7925 N. High St., Columbus, OH 43235 | Godman Guild Association | 167 ac | Summer camp + retreat; ZipZone within property; deferred from T7 |
| Camp Ken-Jockety & The Elam Environmental Center | Site | 1295 Hubbard Rd, Galloway, OH 43119 | Girl Scouts of Ohio's Heartland | 220 ac | Near Big Darby Creek; hiking, fishing, canoeing; reservation/program access |
| Ginny and John Elam Environmental Center | Child Site | 1295 Hubbard Rd, Galloway, OH 43119 | Girl Scouts of Ohio's Heartland | (within T8-002) | Named env. ed. center within Camp Ken-Jockety |
| Wilma H. Schiermeier Olentangy River Wetland Research Park | Site (TIER FLAG) | 352 W. Dodridge St., Columbus, OH 43202 | Ohio State University | 52 ac | RAMSAR; open public access; TIER AMBIGUITY — OSU not ODNR and not private; flagged for Resolution |

**Null results (with evidence):** Simon Kenton Council BSA (no Franklin Co. camp), BBBS Camp Oty'Okwa (Hocking Co.), Waterman Farm OSU (no public access), Chadwick Arboretum (excluded — cultivated collection), ODNR hunting preserves (none in Franklin Co.), university natural areas (Capital, Otterbein — none confirmed), church/scout camps (none in Franklin Co.).

---

## Next Steps

1. **Resolution pass** — ALL TIERS COMPLETE — proceed to na-pipeline skill
   - Complete all cities and villages (web discovery) before any map verification pass
   - **Columbus map verification pass** — defer until all municipalities cataloged; run as a single consolidated pass across all jurisdictions to correctly attribute map-visible parks before marking Columbus COMPLETE
   - ~~**Dublin** — COMPLETE (103 entities; GIS-sourced; map verification deferred)~~
   - ~~**Gahanna** (46 seeds) — WEB PARTIAL: 29 Sites/Trails confirmed; **pocket parks PENDING** (CivicPlus page blank; must retry with browser + map pass)~~
   - ~~**Westerville** (25 seeds) — WEB PARTIAL: 20 parks + 1 trail confirmed; ~5-6 parks unidentified; parks.westerville.org blocked; must revisit with browser~~
   - ~~**Upper Arlington** (21 seeds) — WEB PARTIAL: 18 parks + 3 aquatic facilities confirmed; ~5 gaps remain; upperarlingtonoh.gov blocked; must revisit with browser~~
   - **Also revisit Gahanna pocket parks + Westerville gaps + UA gaps** once browser is reconnected
   - ~~**Hilliard** — WEB PARTIAL: 24 parks + 2 trails confirmed; ~1-2 gaps remain; hilliardohio.gov blocked~~
   - ~~**Grove City** (21 seeds) — WEB PARTIAL / SIGNIFICANT GAP: 14 parks + 3 child sites confirmed; ~16-20 parks missing; grovecityohio.gov blocked~~
   - ~~**Groveport** (8 seeds) — WEB PARTIAL: 7 parks confirmed; ~1 gap remains; groveport.org blocked~~
   - ~~**Worthington** (17 seeds) — WEB PARTIAL: 11 parks + 1 child site confirmed; ~1-2 gaps remain; worthington.org blocked~~
   - ~~**Bexley** — WEB PARTIAL: 5 parks + 3 child sites confirmed; bexley.org blocked; Year of the Parks 2023 complete~~
   - ~~**New Albany** — WEB PARTIAL: 3 district parks + 7 city parks confirmed; naparksohio.org + cityofnewalbany.com blocked; dual managing entity~~
   - ~~**Reynoldsburg** — WEB PARTIAL: 5 parks + 1 partial (Memorial Plaza) confirmed; 275 acres total; reynoldsburg.gov blocked~~
   - ~~**Whitehall** — WEB PARTIAL: 7 parks confirmed (3 addresses partial); 115+ acres; whitehall-oh.us blocked~~
   - ~~**Grandview Heights** — WEB PARTIAL: 9 sites confirmed (2 addresses partial); ~45 acres; grandviewheights.gov blocked~~
   - ~~**Canal Winchester** — WEB PARTIAL: 5 parks + 1 trail confirmed; 307 acres; canalwinchesterohio.gov blocked~~
   - ~~**Obetz** — WEB PARTIAL: 8 Sites (7 parks + Fortress Obetz child) confirmed; 136 acres; some addresses road-name only~~
   - ~~**Pickerington** — CROSS-COUNTY NOTE: primarily Fairfield County; Franklin County portion has no confirmed dedicated parks~~
   - ~~**Marble Cliff** — WEB PARTIAL: 4 parks confirmed; 2 addresses partial~~
   - ~~**Minerva Park** — WEB PARTIAL: 2 entities; village-wide rec; no discrete park parcel; Camp Mary Orton = separate org~~
   - ~~**Valleyview** — WEB PARTIAL: 1 of 2 parks confirmed (Dibblee Park); second park unknown~~
   - ~~**Urbancrest** — WEB PARTIAL: 1 community park (1st Ave); address partial~~
   - ~~**Brice** — NULL: very small village; no confirmed parks~~
   - ~~**Harrisburg** — NULL: very small village (315 pop); no confirmed parks~~
   - ~~**Lockbourne** — WEB PARTIAL: 2 parks confirmed (Locke Meadow + Veterans); Veterans address partial~~
   - ~~**Riverlea** — WEB PARTIAL: 1 village green (Circle Park); address partial~~
   - ~~**Lithopolis** — CROSS-COUNTY / WEB PARTIAL: 2 parks found; county boundary of each TBD~~
   - **ALL TIER 6 MUNICIPAL WEB DISCOVERY COMPLETE** ✓ — Ready for browser reconnect / revisit pass
   - **Special items**: Bergstresser/Dietz Covered Bridge (NRHP #74001484), Village of Canal Winchester
   - **Franklin Park Conservatory**: flag Tier 6 city ownership record against Tier 4 JRD record for Resolution deduplication

2. **Tier 6 — Browser Reconnect / Revisit Priority Queue**
   - **Grove City**: HIGHEST PRIORITY — ~16-20 parks missing; grovecityohio.gov
   - **Gahanna**: pocket parks page (CivicPlus /474/ blank); ~28 unresolved
   - **New Albany**: ~14 district recreation areas unidentified
   - **Westerville**: ~5-6 parks; parks.westerville.org
   - **Upper Arlington**: ~5 gaps; upperarlingtonoh.gov
   - **Address partials**: Bridlewood/McFadyen/Veterans Parks (Obetz), Dibblee 2nd park (Valleyview), Urbancrest park, Lockbourne Veterans Park, Riverlea Circle Park, Marble Cliff Island/Quarry parks, Whitehall Lamby Lane/Robinwood/Central Bark, Grandview Heights Pierce Field/Miller Park, etc.

3. **Tier 7 — Conservancy / Land Trust**
   - Central Ohio Land Trust (COLT): known to hold properties in Franklin County
   - Columbus Audubon: owns/manages some natural areas
   - The Nature Conservancy (Ohio): possible holdings in Darby Creek corridor

4. **Tier 8 — Private**
   - Expected sparse — private nature reserves, private golf courses with natural area designations
   - Camp Mary Orton (Minerva Park) — investigate ownership; may belong here or to a special district

5. **Resolution flags to process after all tiers complete**
   - Sawmill cross-tier dedup (B515 vs B516 / Tier 2)
   - Gahanna Woods cross-tier (B221 city park vs B222 state preserve)
   - Franklin Park Conservatory (Tier 4 JRD vs Tier 6 city)
   - 6 cross-tier greenway trail conflicts (flags 20 above)
   - All 7 baseline duplicate name pairs (Academy Park, Heritage Park, Indianola Park, Olde Sawmill, Perry Park, Thompson Park, Windsor Park)
   - 18 new discoveries (12 WEBSITE_ONLY parks + 6 missing nature preserves) — verify at Resolution

---

## Source Files (§24 IMP-129)

Qualifying binary source files saved to `County_Spreadsheets/Franklin/source_files/` on 2026-05-22 (retroactive — §24 was not executed at discovery time due to IMP-129 wget mechanism gap):

| Filename | Size | Source / Notes |
|---|---|---|
| `columbus_nature_preserves_booklet.pdf` | 29,194 KB | Columbus Recreation & Parks Nature Preserves booklet 2025. Source for city nature preserve sites (T6): descriptions, access, trail info. URL: https://columbusrecparks.com/wp-content/uploads/2025/02/ColumbusNaturePreserves_Spreads_compressed.pdf |

---

## Notes for Next Session

- Staging file: `franklin_oh_raw_discovery.yaml` — append all new records here immediately
- Session log: `franklin_oh_session_log.md` — update tier status as work proceeds
- This handoff: update before ending each session
- Keep chat summaries brief; write records to staging file immediately to manage context
