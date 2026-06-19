# Franklin County, Ohio — Discovery Session Log
# Natural Areas Project v5.2
# -----------------------------------------------------------

## County Context

- **County:** Franklin County, Ohio
- **County seat:** Columbus
- **Major cities:** Columbus, Dublin, Westerville, Gahanna, Upper Arlington, Hilliard, Grove City, Groveport, Bexley, Worthington, New Albany, Reynoldsburg, Whitehall, Grandview Heights, Canal Winchester
- **Villages (partial):** Urbancrest, Marble Cliff, Harrisburg, Lockbourne, Obetz, Minerva Park, Brice, Riverlea, Valleyview, Lincoln Village, Shadeville, New Rome, Urbancrest
- **Townships:** Blendon, Brown, Clinton, Franklin, Hamilton, Jackson, Jefferson, Madison, Marion, Mifflin, Norwich, Perry, Plain, Pleasant, Prairie, Sharon, Truro, Washington (18 townships per franklincountyohio.gov — note: Scioto, Monroe, Harrisburg, Columbus were erroneously included in original list)
- **Park district:** Metro Parks Serving Franklin County (formerly Columbus and Franklin County Metropolitan Park District)
- **Known cross-county entities:**
  - Ohio to Erie Trail (OTET) — multi-county, will be held
  - Buckeye Trail — multi-county, will be held
  - Other trails partially managed by Metro Parks extending beyond Franklin County

## Baseline Summary

- **Total baseline seeds:** 690
- **Entity type breakdown:**
  - Columbus City Park: 390
  - Dublin City Park: 55
  - Gahanna City Park: 46
  - Westerville City Park: 25
  - Grove City City Park: 21
  - Upper Arlington City Park: 21
  - Columbus City Nature Preserve: 17
  - Worthington City Park: 17
  - Metro Parks: 11
  - Canal Winchester City Park: 9
  - Reynoldsburg City Park: 9
  - Groveport City Park: 8
  - Other: ~51

## Duplicate Names Flagged for Resolution

The following baseline seeds share names across different management entries — flagged for Resolution pass:

| Pair | Baseline IDs | Note |
|---|---|---|
| Academy Park | B003, B004 | Columbus City Park vs Gahanna City Park — likely distinct entities |
| Heritage Park | B289, B290 | TBD |
| Indianola Park | B314, B315 | TBD |
| Olde Sawmill Park | B441, B442 | TBD |
| Perry Park | B457, B458 | TBD |
| Thompson Park | B586, B587 | TBD |
| Windsor Park | B671, B672 | TBD |

## Cross-County Entities Pre-flagged

- Ohio to Erie Trail (OTET) — spans multiple counties; will be recorded and held
- Buckeye Trail — spans multiple counties; will be recorded and held
- Any Metro Parks trails extending beyond Franklin County — will be held

---

## Session 1 — 2026-03-08

### Bootstrap
- Session files created
- Baseline internalized (690 seeds)
- County context established
- 7 duplicate name pairs flagged for resolution
- Cross-county trails pre-identified

### Tier 1 — Federal & Tribal

**Status:** COMPLETE — NULL RESULT

**Result:** No federally owned or managed natural area lands in Franklin County.

**Sources checked:**
- NPS National Natural Landmarks index (Ohio) — Blacklick Woods (Franklin/Fairfield border) and Highbanks (Delaware/Franklin border) are NNL-designated but managed by Metro Parks → Tier 3 entities; NNL designation to be noted in designation field
- NPS Find a Park (Ohio) — No NPS park units in Franklin County
- Ohio & Erie Canalway National Heritage Area — Congressional designation covering Franklin County but no federally owned/managed lands; not a Tier 1 entity
- USFWS National Wildlife Refuges (Ohio) — No NWR units in Franklin County
- US Army Corps of Engineers, Huntington District — Flood control infrastructure only; no natural area lands
- USDA Forest Service / Wayne National Forest — Does not extend to Franklin County
- BLM Northeastern States — No BLM holdings in Franklin County
- Federally recognized tribes — No tribal lands in Franklin County

**Entities found:** 0

**Discovery module improvement observation:**
- The discovery protocol does not clarify whether National Natural Landmark (NNL) designations on locally managed land trigger a Tier 1 record. Decision: NNL designation is a federal designation attribute, not a management tier. Entity goes to management tier (Tier 3 in this case); designation field captures "National Natural Landmark."
- The discovery protocol does not address National Heritage Area (NHA) designations. Decision: NHA is a congressional designation — it does not convey federal land ownership or management. No Tier 1 entity created. NHA coverage may be noted as context in site notes where relevant.
- Both decisions should be added to the discovery protocol as explicit rules.

### Tier 2 — State (ODNR)

**Status:** COMPLETE

**Entities found:** 7 (6 Sites + 1 Trail)

**Sites:**
1. Gahanna Woods State Nature Preserve — Franklin County, 59.329 ac, ODNR owned/leased to City of Gahanna (B222)
2. Sawmill Wetlands Education Area — Franklin County, ~17.32 ac, state-owned, ODNR/Columbus co-managed (B516)
3. Olentangy River State Wildlife Access Area — Franklin County, identity uncertain (B448)
4. Big Darby Creek State and National Scenic River — multi-county (Champaign, Franklin, Logan, Madison, Pickaway, Union)
5. Little Darby Creek State Scenic River — multi-county (Franklin, Madison, Pickaway, Union)
6. Olentangy River State Scenic River — Delaware + Franklin counties, 22-mile segment

**Trails:**
7. Olentangy River Water Trail — Franklin County, 8.94 mi paddle route, ODNR designation/Columbus management

**Null sub-categories:** State Parks (none in Franklin County), State Forests (none), large ODNR Wildlife Areas (none active — former Darby land transferred to Metro Parks 1984)

**Baseline seeds confirmed this tier:** B222 (Gahanna Woods SNP), B516 (Sawmill), B448 (Olentangy Wildlife Area — identity uncertain)

**Discovery module improvement observations:**
- Scenic river corridor entity type is undefined in protocol — recorded as Sites pending amendment
- State water trail tier assignment unclear — flagged for Resolution
- State nature preserves leased to municipalities will appear again at Tier 6 — deduplication required


### Tier 3 — District (Metro Parks Serving Franklin County)

**Status:** COMPLETE

**Sites found:** 17 parks + 2 child sites + 1 site network = 20 site-type records
- Full list: Battelle Darby Creek (+ Big Darby Public Hunting Area child), Blacklick Woods (NNL), Blendon Woods, Glacier Ridge, Highbanks (NNL), Heritage Trail Park, Homestead, Inniswood Metro Gardens, Pickerington Ponds, Prairie Oaks, Quarry Trails, Rocky Fork, Scioto Audubon, Scioto Grove, Sharon Woods (+ Edward S. Thomas State Nature Preserve child), Three Creeks, Walnut Woods
- Site Network: Metro Parks Serving Franklin County (system-level)
- Non-Franklin County parks excluded: Slate Run (Pickaway), Chestnut Ridge (Fairfield), Clear Creek (Hocking)

**Trails found:** ~103 total trail records
- Multi-park Greenway Trails: 6 total
  - Camp Chase Trail (15.2 mi, Franklin + Madison, rails-to-trails, OTET segment)
  - Darby Creek Greenway Trail (gap trail: 8.3 mi at Battelle Darby + 4.7 mi at Prairie Oaks)
  - Heritage Trail (6.1 mi, Hilliard to Plain City, rails-to-trails, Metro Parks manages 3.6 mi)
  - Blacklick Creek Greenway Trail (~16 mi, Pickerington Ponds → Blacklick Woods → Three Creeks)
  - Scioto Greenway Trail (~12 mi along Scioto River, Metro Parks manages ~11 mi)
  - Alum Creek Greenway Trail (~22 mi, flagged for Tier 6 as primary; documented here for Metro Parks connection at Three Creeks)
- Per-park named trails: ~97 trails across all 17 parks
  - Battelle Darby Creek: 12 | Highbanks: 7 | Prairie Oaks: 7 | Pickerington Ponds: 5
  - Glacier Ridge: 4 | Sharon Woods: 5 | Blendon Woods: 7 | Blacklick Woods: 5
  - Three Creeks: 6 | Scioto Audubon: 3 | Scioto Grove: 6 | Quarry Trails: 5
  - Rocky Fork: 6 | Walnut Woods: 3 | Inniswood: 5 | Homestead: 1
  - Heritage Trail Park: 0 additional (Heritage Trail already counted)

**Identity flags from trail inventory:**
- 11 trail identity flags requiring Resolution (trail name ambiguities, combined routes, possible statewide trail overlaps)

**Baseline seeds confirmed this tier:**
- B055 (Big Darby Public Hunting Area), B067 (Blacklick Woods Metro Park), B190 (Edward S. Thomas SNP), B292 (Heritage Trail Park), B300 (Homestead), B318 (Inniswood), B478 (Quarry Trails), B502 (Rocky Fork), B521 (Scioto Audubon), B524 (Scioto Grove), B540 (Sharon Woods), B589 (Three Creeks), B628 (Walnut Woods)
- Total confirmed this tier: 13 additional seeds (cumulative: 16 of 690)
- Note: Blendon Woods Metro Park B067 assignment needs correction — error noted in improvement flags

**Discovery module improvement observations:**
- Metro Parks scale challenge: 230+ mi trails requires sub-session approach for completeness
- Rails-to-trails multi-governance tier assignment unclear — recorded at Tier 3, flagged for protocol
- Child site designation tier rule confirmed: management tier governs (not designation tier)
- Blendon Woods / Blacklick Woods baseline ID collision — flag for Resolution
- Multiple duplicate trail names across parks (Overlook Trail, Lake Trail, Arrowhead Trail, Multipurpose Trail, Boardwalk Trail, Bridle Trail) — all disambiguated with park qualifiers in name_raw


---

### Tier 4 — County

**Status:** COMPLETE

**Entities found:** 2 (2 Sites)

**Method:** Direct Chrome fetches + WebSearch; County Sub-Procedure v5.2 applied

**Sources checked:**
- Franklin County agency directory — franklincountyohio.gov (Chrome direct fetch)
- Franklin County Boards and Commissions — franklincountyohio.gov (Chrome direct fetch)
- Franklin Park Conservatory — fpconservatory.org/about-us/ (Chrome direct fetch)
- Franklin County Fairgrounds — fcfair.org/fairgrounds (Chrome direct fetch)
- Franklin County GIS Parcel Viewer — gis.franklincountyohio.gov/parcelviewer/ (Chrome; owner-name search incomplete — manual review flagged)
- NRHP check — Wikipedia NRHP Franklin County list + Bergstresser/Dietz Bridge article (Chrome)
- Franklin County EDP planning pages — returned 404; county website redesign underway
- Board of Commissioners — franklincountyohio.gov/Agency-Directory/Board-of-Commissioners (Chrome)
- Experience Columbus tourism — experiencecolumbus.com (WebSearch)
- Franklin County SWCD, Engineer, Big Darby Accord, Central Ohio Greenways — WebSearch

**Sites found:**
1. **Franklin Park Conservatory and Botanical Gardens** — 1777 E. Broad St., Columbus; JRD co-governed by Franklin County + City of Columbus (ORC 755.14); county-appointed board; ~13-acre visitor campus within 88-acre City of Columbus Franklin Park; CROSS-TIER FLAG for Tier 6 dedup
2. **Franklin County Fairgrounds** — 5043 Northwest Parkway, Hilliard; owned by Franklin County Agricultural Society (ORC Chapter 1711); ~100 acres; MINIMAL_DATA flag

**Deferred / excluded:**
- Bergstresser/Dietz Covered Bridge (NRHP #74001484) — deferred to Tier 6 (Village of Canal Winchester took ownership 1991)
- Franklin County SWCD — education/technical assistance only; no land ownership
- Franklin County Engineer — drainage/road infrastructure; not natural areas
- Big Darby Accord — planning framework only; no land ownership
- Central Ohio Greenways (MORPC) — multi-county regional coordination; not a Tier 4 entity

**Baseline seeds confirmed this tier:** 0 additional (cumulative: 16 of 690)

**Discovery module improvement observations:**
- Franklin County is a textbook case of Metro Parks absorbing the county park function. Protocol should note: in Ohio counties with an active Metropolitan Park District (ORC 1545), expect Tier 4 result to be minimal unless the county commissioners separately manage land — but always check JRDs and county agricultural societies.
- Joint Recreation Districts (ORC 755.14) create county-involved entities on municipal land. Protocol §4.1 ("co-managed with municipalities") correctly captures these at Tier 4 with a cross-tier flag for Tier 6.
- Central Ohio Greenways (MORPC multi-county coordination) exposes a gap in the 8-tier framework: regional, multi-county trail networks governed by planning commissions don't fit cleanly into any tier. Recommend adding a "regional/network" documentation approach for multi-county coordination bodies.
- County EDP planning pages 404 during discovery — potential gap in planning document review; recommend manual review during Resolution phase.
- GIS Parcel Viewer owner-name search not completable via automated form interaction (element type: TABLE); manual GIS parcel review recommended in Resolution phase.


### Tier 5 — Township

**Status:** COMPLETE

**Entities found:** 21 Sites + 2 Trails = 23 entities across 5 active townships
**Null townships:** 13 (evidence documented for each)

**Method:** WebSearch + WebFetch per §4.1–4.3 of Township Lands Discovery Sub-Procedure v5.1; all 18 townships searched individually; official pages fetched where found

**Township-by-township results:**

| Township | Status | Parks Found | Notes |
|---|---|---|---|
| Blendon | COMPLETE | 3 Sites | Ridgewood Park, Phelps Acre Park, Sunbury Woods Commons; website: blendontwp.org |
| Brown | COMPLETE | 0 | No township website found; Brown Township is lightly populated rural area; no evidence of township parks |
| Clinton | COMPLETE | 6 Sites | Veterans Park, Sale Road Playground, Fred Stigers Memorial Park, Case Road Community Garden, Chambers Circle Park, West Side/University View Playground; website: clintontwpoh.gov |
| Franklin | COMPLETE | 0 | Website: franklin-townshipohio.gov (caution: franklintownshipohio.us = Warren County); no parks listed |
| Hamilton | COMPLETE | 2 Sites + 1 Trail | Hamilton Township Park (with 0.5-mi loop trail) + Big Walnut Creek access, Firetruck Park; website: hamiltontownship.com |
| Jackson | COMPLETE | 0 | Website: jacksontownship.com; no parks section found |
| Jefferson | COMPLETE | 5 Sites | Blacklick Ridge Community Park, Boehnke Nature Preserve, Jefferson Community Park, Jefferson Run Park, Olde Quarry Park; website: jeffersontownship.org |
| Madison | COMPLETE | 0 | Website: madisontownshipohio.com; no parks listed |
| Marion | COMPLETE | 0 | Marion Township Franklin County is DEFUNCT — fully absorbed into City of Columbus; no government website |
| Mifflin | COMPLETE | 0 | Website: mifflintownship.org; no parks section; largely absorbed into Columbus |
| Norwich | COMPLETE | 0 | Website: norwichtwp.org; explicitly defers to Hilliard Recreation and Dublin Community Services; Indian Village Camp (3200 Indian Village Rd) is Columbus Recreation & Parks — not Norwich Township |
| Perry | COMPLETE | 0 | Website: perrytwp.org (caution: perrytwp.com = Stark County); no parks listed |
| Plain | COMPLETE | 0 | Website: plaintownship.org (caution: plaintownshipstarkoh.gov = Stark County); parks listed are New Albany parks, not township-owned |
| Pleasant | COMPLETE | 0 | Website: pleasanttwp.org; no parks section found |
| Prairie | COMPLETE | 5 Sites + 1 Trail | Blue Lake Park, Carl Frye Park (with 0.7-mi walking path), Dalebrook Park, Friendship Park, Lakota Park; website: prairietownship.org (caution: /133 redirected to Chipper service; correct URL is /491) |
| Sharon | COMPLETE | 0 | Website: sharontwp.us (caution: sharontwp.org = Medina County); no parks section; fragmented township largely absorbed into municipalities |
| Truro | COMPLETE | 0 | No independent township parks; Civic Park in Truro Township area is managed by City of Reynoldsburg (reynoldsburg.gov/Facilities) — not Truro Township |
| Washington | COMPLETE | 0 | Website: washingtontownship.com; historical parks transferred: Homestead → Metro Parks 2015 (Tier 3 B300), Kaltenbach → City of Dublin 2014 (future Tier 6) |

**Sites found (21 total):**

Blendon Township (3):
1. Ridgewood Park — Blendon Township
2. Phelps Acre Park — Blendon Township
3. Sunbury Woods Commons — Blendon Township

Clinton Township (6):
4. Veterans Park — Clinton Township
5. Sale Road Playground — Clinton Township
6. Fred Stigers Memorial Park (Triangle Park) — Clinton Township
7. Case Road Community Garden — Clinton Township
8. Chambers Circle Park — Clinton Township
9. West Side / University View Playground — Clinton Township

Hamilton Township (2):
10. Hamilton Township Park — Hamilton Township (Big Walnut Creek access; 0.5-mi loop trail)
11. Firetruck Park — Hamilton Township

Jefferson Township (5):
12. Blacklick Ridge Community Park — Jefferson Township
13. Boehnke Nature Preserve — Jefferson Township
14. Jefferson Community Park — Jefferson Township
15. Jefferson Run Park — Jefferson Township
16. Olde Quarry Park — Jefferson Township

Prairie Township (5):
17. Blue Lake Park — Prairie Township
18. Carl Frye Park — Prairie Township
19. Dalebrook Park — Prairie Township
20. Friendship Park — Prairie Township
21. Lakota Park — Prairie Township

**Trails found (2 total):**
1. Hamilton Township Park Trail — Hamilton Township; 0.5-mi loop; within Hamilton Township Park
2. Carl Frye Park Walking Path — Prairie Township; 0.7 mi; within Carl Frye Park

**Excluded entities (notable):**
- Hellbranch Meadows — owned/managed by Franklin SWCD (purchased 2008); Prairie Township received restoration grant only; not a Tier 5 entity; flag for Tier 4 special district evaluation
- Prairie Sports Complex — sports/athletic facility; not identity-bearing as a natural area
- Camp Mary Orton (Minerva Park) — flagged for investigation; may be private or special district (not confirmed township ownership)
- Civic Park, Truro — City of Reynoldsburg (not Truro Township)
- Indian Village Camp, Norwich — Columbus Recreation & Parks (not Norwich Township)

**Baseline seeds confirmed this tier:** 0 additional (cumulative: 16 of 690)
- No Tier 5 entities appear in the baseline seed list (baseline seeds are primarily city parks)

**Discovery module improvement observations:**
- Wrong-county website hazard is severe for Ohio townships: at least 7 township names in Franklin County return wrong-county websites in search results (Sharon, Franklin, Jefferson, Perry, Plain, Marion, Washington). Protocol §4.2 should explicitly require address verification on any township website before treating it as authoritative.
- Marion Township defunct case: protocol §5.3 addresses townships that defer to park districts, but is silent on fully defunct townships absorbed into cities. Add a "DEFUNCT" status category for absorbed townships.
- Prairie Township URL instability (/133 → Chipper redirect): township parks pages may have been reorganized. Always verify the parks page independently rather than trusting a cached or bookmarked URL.
- Sharon Township fragmentation: highly urbanized county townships may lack their own park systems even without explicitly stating deferral. A finding of "no parks page on official website" is sufficient evidence for null result.


---

## Session 2 — 2026-03-14

### Bootstrap
- Resumed from Session 1 handoff (Tiers 1–5 complete)
- Staging file, session log, and handoff loaded from uploads
- Project folder C:\Users\user1\Natural Areas Project v5 mounted
- Sub-procedure files confirmed present in /discovery/
- Chrome (Claude in Chrome) connected
- Baseline spreadsheet: Franklin baseline.xlsx (690 seeds)

### Tier 6 — Municipal: City of Columbus

**Status:** PARTIAL — web discovery COMPLETE; map verification OVERVIEW ONLY (full quadrant pass PENDING)

**Method:** Chrome fetch of columbusrecparks.com (FacetWP pagination); Python cross-reference against baseline; Google Maps city-scale overview verification

**Sources checked:**
- Columbus Recreation and Parks Department parks listing: https://columbusrecparks.com/facilities/parks/ (all 15 pages, FacetWP paginated)
- Columbus Recreation and Parks nature preserves page: https://columbusrecparks.com/facilities/nature-preserves/
- Columbus Recreation and Parks trails page: https://columbusrecparks.com/facilities/trails/
- Central Ohio Greenways page: https://columbusrecparks.com/facilities/trails/greenways/
- Olentangy River Water Trail page: https://columbusrecparks.com/facilities/trails/olentangy-river-water-trail/
- Paved Paths page: https://columbusrecparks.com/facilities/trails/paved-paths/
- Nature Preserves Booklet PDF: https://columbusrecparks.com/wp-content/uploads/2025/02/ColumbusNaturePreserves_Spreads_compressed.pdf
- Google Maps city-scale overview: https://www.google.com/maps/search/parks+Columbus+Ohio/@39.9612,-82.9988,12z (spot check; full quadrant pass PENDING)
- Franklin County baseline spreadsheet (390 Columbus City Park + 17 Columbus City Nature Preserve seeds cross-referenced)

**Sites found:** 425 (419 from official parks listing + 6 new nature preserve discoveries not in baseline)
**Trails found:** 14 (13 Central Ohio Greenway trails + Olentangy River Water Trail Tier 6 management record)
**Trail Segments found:** 3 (Olentangy River Water Trail Sections A, B, C)
**Trail Networks found:** 1 (Central Ohio Greenways system-level record)
**Total Tier 6 Columbus entities this session:** 443

**Baseline seeds confirmed this tier (Columbus):** 407 (390 Columbus City Park + 17 Columbus City Nature Preserve)
**New discoveries (website-only, not in baseline):** 18 (6 nature preserves + 12 parks flagged in EXTRA_PARKS list)
**Cumulative baseline seeds confirmed:** 423 of 690

#### Key Findings and Flags

**Parks count discrepancy:** Website lists 422-419 parks (site text says 422; FacetWP returned 419 unique records); baseline has 407 Columbus-typed seeds. Difference of ~12 accounts for parks added after baseline creation. Flagged in EXTRA_PARKS list in staging file.

**Nature preserve count discrepancy:** Main parks page says "25 nature preserves"; nature preserves page lists 25 (confirmed). Baseline has 17 "Columbus City Nature Preserve" seeds; additional 8 are typed "Columbus City Park" in baseline (including Coronet Woods) or are new discoveries.

**Missing nature preserves (6 new, not in baseline):**
- Gertrude S. Lawrence Woods Nature Preserve
- Hoover Meadows Nature Preserve (confirmed by paved paths page)
- Hoover Nature Preserve
- Hoover Oxbow Nature Preserve
- Mud Hen Marsh Nature Preserve
- O'Shaughnessy Nature Preserve (may span Franklin + Delaware counties)

**Coronet Woods baseline type mismatch:** B138 typed "Columbus City Park" but listed on official nature preserves page. Resolution should update category.

**Sawmill Nature Preserve / Sawmill Wetlands Education Area dedup:** B515 (Sawmill Nature Preserve, "Columbus City Nature Preserve; Ohio State Nature Preserve", 17.32 ac, 2650 Starford Dr.) is same physical site as B516 Sawmill Wetlands Education Area (Tier 2 canonical record). Resolution must deduplicate.

**Cross-tier trail flags:**
- Alum Creek Trail — Tier 6 canonical record (Columbus Rec Parks primary); Tier 3 stub was Metro Parks connection only
- Camp Chase Trail — Tier 6 canonical; multi-county (Franklin + Madison); also OTET segment
- Heritage Trail — Tier 6 canonical; multi-county (Franklin + Madison); Tier 3 record is Metro Parks segment
- Blacklick Creek Trail — possible duplicate/overlap with Tier 3 Blacklick Creek Greenway Trail; flag for Resolution
- Darby Creek Trail — possible overlap with Tier 3 Darby Creek Greenway Trail; flag for Resolution
- Scioto Trail — possible overlap with Tier 3 Scioto Greenway Trail; flag for Resolution
- Olentangy River Water Trail — Tier 6 management record documents Columbus as operator; Tier 2 canonical (ODNR designation); Resolution must assign canonical tier
- Genoa Trail — described as OTET section; may be Trail Segment of OTET rather than standalone Trail

### Tier 6 — Municipal: City of Dublin

**Status:** WEB COMPLETE / MAP VERIFICATION DEFERRED (consolidated pass after all municipalities)

**Method:** ArcGIS Feature Service query (Dublin_Parks/FeatureServer/3, all 176 features extracted via browser JS); biking page for trail context; official parks page mid-redesign and does not list individual parks

**Sources checked:**
- City of Dublin ArcGIS Feature Service: https://services1.arcgis.com/NqY8dnPSEdMJhuRw/arcgis/rest/services/Dublin_Parks/FeatureServer/3 (all 176 features)
- Dublin Bikeway and Park System ArcGIS web map (webmap=4a2e26949a814a65bb96ee33d293f9e9)
- City of Dublin parks page: https://dublinohiousa.gov/recreation-services/parks/
- City of Dublin biking page: https://dublinohiousa.gov/recreation-services/parks/biking/
- Dublin Bike Map & Parks Guide PDF (2022)

**Sites found: 102** (18 Community Parks + 48 Neighborhood Parks + 36 named Open Spaces)
**Trail Networks found: 1** (Dublin Bikepath and Park System, 154+ mi)
**Total Tier 6 Dublin entities: 103**

**GIS data breakdown:**
- 18 Community Parks → all recorded as Sites
- 48 Neighborhood Parks → all recorded as Sites (2 flagged for entity-type review: Dublinshire Greenway, Emerald Parkway Bridge River Access)
- 110 Open Spaces total: 36 identity-bearing named open spaces recorded; ~74 lettered sub-parcel open spaces (e.g., Ballantrae Open Space H, Tartan West Open Space A) NOT recorded as individual Sites — flagged as improvement observation
- 5 cemeteries within Open Spaces layer — recorded but flagged for Resolution re: entity exclusion rule

**Baseline cross-reference:** 55 Dublin City Park seeds in baseline; individual ID cross-reference deferred to Resolution (GIS source is authoritative; names will match at Resolution pass)

**Key findings:**
- dublinohiousa.gov is mid-redesign; individual park pages not accessible; ArcGIS GIS layer used as authoritative source
- Dublin manages bikepath network as unified infrastructure (no individually named trails); Bikeways FeatureServer/1 has 300+ segments with zero named trail identifiers
- Ted Kaltenbach Park confirmed (transferred from Washington Township 2014; B4 in handoff)
- ML "Red" Trabue Nature Reserve: GIS typed Community Park at 6720 Post Rd — natural area character warrants note at Resolution
- Dublinshire Greenway: GIS typed Neighborhood Park but is linear corridor on Avery Rd — may be Trail; flag for Resolution
- Scottish Corners Woods Open Space (5950 Sells Mill Dr) is adjacent to Scottish Corners Park (Community Park, same address) — possible parent/child relationship; flag for Resolution

**Improvement observation (new #24):** Dublin's GIS open space layer includes ~74 lettered sub-parcel open spaces that are individual maintenance parcels, not independently navigable Sites. Protocol should clarify that GIS polygon sub-parcels with letter/number suffixes are not automatically identity-bearing Sites and should not automatically generate individual entity records.

---

**Map verification status (Columbus):**
- City-scale overview completed: distribution consistent with 419-park catalog; no obvious gaps identified
- Full quadrant-by-quadrant map pass: DEFERRED — decision made to complete all Tier 6 municipal web discovery first, then run a single consolidated map verification pass across all jurisdictions. Running per-municipality map passes before other cities/villages are cataloged risks false positives from cross-municipal misattribution.
- Protocol improvement #23 logged: §4.4 map verification ordering should advise consolidated pass for dense multi-municipality counties.

---

## Session 3 — 2026-03-14 (continued)

### Bootstrap
- Continued directly from Session 2 (same session, context compacted mid-Gahanna)
- Staging file, session log, handoff, and discovery procedures loaded
- Chrome (Claude in Chrome) connected at session start; **disconnected during Gahanna discovery**

---

### Tier 6 — Municipal: City of Gahanna

**Status:** WEB PARTIAL — confirmed parks complete; **pocket parks / open spaces / reserves PENDING**; map verification DEFERRED per project decision

**Method:** Chrome fetch of gahanna.gov (Facilities page, Parks & Trails nav); Parks & Trails Guide PDF; Facilities page JS extraction (all 40 facilities with addresses)

**Sources checked:**
- Gahanna Facilities page (all 40 facilities, JS-extracted): https://www.gahanna.gov/Facilities
- Gahanna Parks & Trails Guide PDF: https://oh-gahanna.civicplus.com/DocumentCenter/View/278/Parks-and-Trails-Guide-PDF
- Gahanna Athletic Complexes page (nav confirmed): https://www.gahanna.gov/Parks-Trails
- Gahanna Neighborhood Parks page (7 parks listed): https://www.gahanna.gov/180/Neighborhood-Parks
- Gahanna Pocket Parks, Open Spaces & Reserves page — EMPTY (CivicPlus JS rendering failure): https://www.gahanna.gov/474/Pocket-Parks-Open-Spaces-Reserves
- Gahanna GIS maps page (services directory disabled; no parks layer accessible): https://maps.gahanna.gov/server/rest/services
- Wayback Machine calendar (4 snapshots 2023-2025): egress-blocked; content not retrieved
- Web search snippets: confirmed 52 parks/greenspaces total; no pocket park list surfaced

**Sites found:** 23 (4 Athletic Complexes + 10 Community Parks + 7 Neighborhood Parks + 2 Aquatic Facilities)
**Child Sites found:** 4 (Creekside Plaza, Creekside Rotary Stage, Friendship Park Community Garden, Hannah Park Community Garden)
**Trails found:** 2 (Big Walnut Trail 4.6 mi paved; Paddle Gahanna & Blueways water trail)
**Pocket Parks / Open Spaces / Reserves:** PENDING — 0 confirmed; ~28 estimated unresolved

**Records appended:** 30 (29 Sites/Trails/Child Sites + 1 DiscoveryNote)
**Script:** gen_gahanna_yaml.py

**Athletic Complexes (4):**
| Name | Address |
|---|---|
| Academy Park | 1201 Cherry Bottom Road |
| Gahanna Municipal Golf Course | 220 Olde Ridenour Road |
| Headley Park | 1031 Challis Springs Drive |
| McCorkle Park | 200 McCutcheon Road |

**Community Parks (10):**
| Name | Address |
|---|---|
| Creekside Park & Arboretum | 123 Mill Street |
| Friendship Park | 150 Oklahoma Avenue |
| Gahanna Woods & State Nature Preserve | 1501 Taylor Station Road |
| Geroux Herb Garden | 206 S Hamilton Road |
| Hannah Park | 6547 Clark State Road |
| Pizzurro Park | 940 Pizzurro Park Road |
| Shull Park | 236 Granville Street |
| Sunpoint Park | 670 McCutcheon Road |
| Veterans Memorial Park | 73 W Johnstown Road |
| Woodside Green Park | 213 Camrose Court |

**Neighborhood Parks (7):**
| Name | Address |
|---|---|
| Ambassador Commons | 639 Gahanna Highlands Drive |
| Ashburnham Park | 1245 Ashburnham Drive |
| Bryn Mawr Park | 1082 Riva Ridge Boulevard |
| Hunters Ridge Park | 341 Harrow Blvd |
| Rathburn Woods Park | 316 Howland Drive |
| Rice Avenue Park | 1178 Rice Avenue / 511 Preservation Lane |
| Trapp Park | 756 Trapp Drive |

**Aquatic Facilities (2):**
| Name | Address |
|---|---|
| Gahanna Swimming Pool | 148 Parkland Avenue |
| Hunters Ridge Pool | 341 Waterbury Blvd |

**Child Sites (4):**
| Name | Parent |
|---|---|
| Creekside Plaza | Creekside Park & Arboretum |
| Creekside Rotary Stage | Creekside Park & Arboretum |
| Friendship Park Community Garden | Friendship Park |
| Hannah Park Community Garden | Hannah Park |

**Trails (2):**
| Name | Length | Notes |
|---|---|---|
| Big Walnut Trail | 4.6 miles paved | Morse Rd → Gahanna Swimming Pool; part of Central Ohio Greenways |
| Paddle Gahanna & Blueways | not stated | Water trail on Big Walnut Creek |

**Pocket Parks PENDING (DiscoveryNote appended):**
- gahanna.gov/474/ loads blank in browser (two confirmed attempts)
- All WebFetch fallbacks blocked (gahanna.gov, visitgahanna.com, gahannaprf.org, eatplaycbus.com, web.archive.org, gis.franklincountyohio.gov — all egress-blocked)
- Browser disconnected mid-session
- City claims 52 parks/greenspaces; ~24 Sites confirmed; ~28 unresolved
- DiscoveryNote record appended to staging file flagging PENDING/UNVERIFIED status

**Address conflicts (flag for Resolution):**
- Headley Park: Facilities page = 1031 Challis Springs Drive; PDF = 1931 Challis Springs Dr (typo or different access point)
- Pizzurro Park: Facilities page = 940 Pizzurro Park Road; PDF = 914 S. Hamilton Rd (possible different entrance or PDF error)

**Gahanna Woods cross-tier note:** Gahanna Woods & State Nature Preserve recorded as Tier 6 Site (Gahanna municipal overlay). Tier 2 state preserve record (B222) already in staging file. Resolution must reconcile both per improvement flag #5 / #22.

**Improvement observation (new #25):** CivicPlus category pages can load with heading only due to JS rendering failures. When a Pocket Parks / Open Spaces type page loads blank, the fallback protocol should check: (a) the Facilities page filter by type, (b) Document Center for PDF park lists, (c) city ArcGIS REST services for parks layer. If all fail, flag PENDING for browser retry.

**Map verification status:** DEFERRED per project decision (improvement #23). Will be completed in consolidated pass after all Tier 6 municipalities are web-complete.

---

### Tier 6 — Municipal: City of Westerville

**Status:** WEB PARTIAL — ~20 parks confirmed; ~5-6 parks unidentified; browser disconnected; domain blocked

**Method:** Web search snippets (parks.westerville.org egress-blocked, browser disconnected); addresses confirmed via Yelp, Google, Waze, mypacer.com, bringfido.com listings

**Sources checked:**
- parks.westerville.org/parks-trails/parks — domain EGRESS BLOCKED
- Web search snippets returning park names and addresses from third-party listing sites
- Yelp listings for individual park addresses
- Waze driving directions for Olde Town Park, Heritage Park
- mypacer.com for Hoff Woods Park, Alum Creek South Park, Hannah Mayne Park
- dogparksnearby.com, bringfido.com for Brooksedge Park address

**Parks found (20):**
| Name | Address |
|---|---|
| Alum Creek Park North | 221 W Main St |
| Alum Creek Park South | 535 Park Meadow Rd |
| Ben Hanby Park | 4 N Vine St |
| Brooksedge Park | 708 Park Meadow Rd |
| Community Tennis Complex | 350 N Cleveland Ave (tentative) |
| Ernest Cherrington Park | 231 Hiawatha Ave |
| Hannah Mayne Park | 45 Glenwood Dr |
| Heritage Park | 60 N Cleveland Ave |
| Highlands Park | 245 S Spring Rd |
| Hoff Woods Park | 556 McCorkle Blvd |
| Huber Village Park | 362 Huber Village Blvd |
| Johnston-McVay Park | 480 S Hempstead Rd |
| Metzger Park | 137 Granby Place |
| Millstone Creek Park | 115 E Park St |
| Olde Town Park | 108 Old County Line Rd |
| Spring Grove North Park | 1201 E County Line Rd |
| Towers Park | 745 N Spring Rd |
| Walnut Ridge Park | 529 E Walnut St |
| Westerville Sports Complex | 325 N Cleveland Ave |
| Westerville Veterans Memorial | 325 N Cleveland Ave |

**Trails found (1):**
- Westerville B&W (Bike & Walk Route) — 2.2 miles paved, former railroad ROW, Hoover Reservoir to Worthington Rd

**Cross-reference note:** Alum Creek Trail (15+ miles) runs through Westerville but is managed by Columbus Rec & Parks; canonical record is at Tier 6 Columbus.

**Records appended:** 22 (20 Sites + 1 Trail + 1 DiscoveryNote)
**Script:** gen_westerville_yaml.py

**Gaps:**
- City claims 26 parks; ~6 unidentified (parks.westerville.org blocked; browser unavailable)
- Community Tennis Complex address tentative
- All addresses sourced from third-party listings; not confirmed against official source
- DiscoveryNote appended flagging PARTIAL/UNVERIFIED status
- Must revisit: reconnect browser, load parks.westerville.org/parks-trails/parks

**Map verification status:** DEFERRED per project decision (Improvement #23).


---

## Session 4 — 2026-03-14 (continued)

### Bootstrap
- Continued directly from Session 3 (same session, context compacted)
- Staging file, session log, handoff, and discovery procedures loaded
- Browser (Claude in Chrome) still disconnected; upperarlingtonoh.gov egress-blocked
- Web search + third-party listing fallback used throughout

---

### Tier 6 — Municipal: City of Upper Arlington

**Status:** WEB PARTIAL — 18 parks + 3 aquatic facilities confirmed; ~5 parks unidentified or address-unknown; map verification DEFERRED per project decision

**Method:** Web search snippets (upperarlingtonoh.gov egress-blocked; browser disconnected); addresses from Yelp, Google, Waze, ohranger.com, cbus4kids.com listings

**Sources checked:**
- upperarlingtonoh.gov/189/Parks — EGRESS BLOCKED
- upperarlingtonoh.gov Facilities pages (CivicEngage) — EGRESS BLOCKED
- Web search snippets for individual park names and addresses
- ohranger.com for Tremont Fountain Park details
- cbus4kids.com for Oxford Park address
- Waze for Westover Park, Burbank Park
- Foursquare for Cardiff Woods (mapcarta.com — egress-blocked; address from Google snippet)

**Parks found (18):**
| Name | Address | Notes |
|---|---|---|
| Northam Park | 1880 Northam Rd | Community park; hosts July 4th |
| Fancyburg Park | 3375 Kioka Ave | Neighborhood park |
| Mallway Park | 2070 S Mallway Drive | Community park; Devon Pool co-located |
| Miller Park | 1901 Arlington Ave | Community park |
| Reed Road Park | 3855 Reed Rd | Community park; Reed Road Water Park within |
| Smith Nature Park | 1270 Fishinger Rd | Natural area / community park |
| Sunny 95 Park | 4395 Carriage Hill Lane | Community park |
| Thompson Park | 4250 Woodbridge Rd | Neighborhood park |
| Tremont Fountain Park | near 3600 Tremont Rd (approx) | ~1 acre; fountain; ADA accessible |
| Greensview Park | 4301 Greensview Dr | Neighborhood park |
| Wyandot Park | 2875 Lane Rd | Neighborhood park |
| Northwest Kiwanis Park | 4840 Stonehaven Dr | Community park |
| Burbank Park | 4780 Stonehaven Dr | Neighborhood park |
| Oxford Park | 4280 Oxford Dr (43220) | Neighborhood park |
| Westover Park | 2111 Westover Rd | Community park; confirmed address |
| Cardiff Woods Park | 1734 Cardiff Rd | Natural area; "Into the Woods" art installation |
| Charing Ravine Park | 2901 Charing Rd (approx) | ~2 acres natural ravine; UA Facility ID 4 |
| Nursery Park | Upper Arlington, OH 43221 (no street) | Address not found via web search |

**Aquatic Facilities (3):**
| Name | Address | Notes |
|---|---|---|
| Devon Pool | 2070 S Mallway Drive | Co-located with Mallway Park; Facility ID 43 |
| Reed Road Water Park | 2000 Hastings Lane | Within Reed Road Park; adjacent to Hastings Middle School |
| Tremont Pool | near 3600 Tremont Rd (approx) | One of 3 UA outdoor pools; address approximate |

**Records appended:** 22 (18 Park Sites + 3 Aquatic Facilities + 1 DiscoveryNote)
**Script:** gen_upper_arlington_yaml.py

**Gaps and verification needed:**
- Nursery Park: name confirmed by web; no street address found anywhere
- Tremont Fountain Park: approximate address only; confirm via browser
- Tremont Pool: approximate address only; confirm via browser
- Charing Ravine Park: ~2901 Charing Rd from web; confirm via browser
- City claims 23 parks; 18 confirmed; ~5 remain unidentified or address-unknown
- Devon Pool co-located with Mallway Park — both documented separately; verify at Resolution whether single or two entities
- Baseline cross-reference (21 UA City Park seeds): deferred to Resolution

**Map verification status:** DEFERRED per project decision (Improvement #23).


---

### Tier 6 — Municipal: City of Hilliard

**Status:** WEB PARTIAL — 24 parks + 1 child site + 2 trails confirmed; ~1-2 parks may remain; map verification DEFERRED

**Method:** Web search snippets (hilliardohio.gov + recandparks.hilliardohio.gov both egress-blocked; browser disconnected); addresses from Yelp, Google, destinationhilliard.org, foursquare listings

**Sources checked:**
- hilliardohio.gov/our-parks/ — EGRESS BLOCKED
- recandparks.hilliardohio.gov/park — EGRESS BLOCKED
- destinationhilliard.org/category/parks — EGRESS BLOCKED
- Web search snippets from Yelp, Google, traillink.com, alltrails.com, bringfido.com
- Waze for station park, municipal park addresses

**Park Sites found (24):**
| Name | Address | Notes |
|---|---|---|
| Alt Field | 3740 Municipal Way | Original baseball field + playground + tennis |
| Beacon Fields | 4375 Edgewyn Ave | Baseball, basketball, multiuse path |
| Britton Farms Park | 4500 Davidson Rd | Fishing pond, multiuse paths |
| Conklin Park | 1000 Boucher Dr | Playground, picnic |
| Cross Creek Park | 3342 Hilliard Rome Rd | FLAG: also on Columbus Rec Parks website |
| Darby Glen Park | 4340 Swenson St | Neighborhood park |
| Father Roderic J. DiPietro Park | 3481 Davidson Rd | Baseball/soccer; inclusive field |
| First Responders Park | 4020 Main St | FLAG: verify vs Station Park (4021) |
| Hamilton Park | 4950 Hamilton Rd | Neighborhood park |
| Hayden Run Village Park | 5226 Davidson Rd | Neighborhood park |
| Heather Ridge Park | 4833 Hawkstone Rd | Neighborhood park |
| Heritage Trail Dog Park | 7262 Hayden Run Rd | FLAG: verify City of Hilliard vs Metro Parks |
| Hilliard East Park | 4450 Schirtzinger Rd | Playground, adaptive swing, shelter |
| HOSA Soccer Complex | 6371 Scioto Darby Rd | Multi-field soccer |
| Lakewood Park | 3180 Walkerview Dr | Neighborhood park |
| Latham Park | 6400 Cosgray Rd | Fishing pond, walking path |
| Merchant Park | 5467 Center St | Near Heritage Rail Trail, dedicated ~2021 |
| Mildred Park | 4592 Britton Pkwy | Neighborhood park |
| Reibel Woods | 6000 Hayden Run Rd | Wooded natural area |
| Roger A. Reynolds Municipal Park | 3800 Veterans Memorial Dr | 130 acres; primary park |
| Silverton Park | 5075 Silverton Way | Neighborhood park |
| Hilliard's Station Park | 4021 Main St | Downtown; Heritage Rail Trail trailhead |
| Tinapple Park | 5503 Hyde Park Dr | Neighborhood park |
| Weaver Park | 4100 Columbia St | Neighborhood park |

**Child Sites (1):**
- Hilliard Family Aquatic Center — 3800 Veterans Memorial Dr (within Roger A. Reynolds Municipal Park)

**Trails (2):**
| Name | Length | Notes |
|---|---|---|
| Heritage Rail Trail | 7 miles | Former railroad corridor, Hilliard to near Plain City; Franklin + Madison counties |
| Scioto Run Nature Trail | 1 mile | Loop trail in wooded natural area; Scioto Run subdivision |

**Records appended:** 28 (24 Sites + 1 Child Site + 2 Trails + 1 DiscoveryNote)
**Script:** gen_hilliard_yaml.py

**Resolution flags:**
- Cross Creek Park: appears on Columbus Rec Parks website AND Hilliard parks list — verify jurisdiction
- Heritage Trail Dog Park: confirm managing entity (City of Hilliard vs Metro Parks)
- First Responders Park (4020 Main St) vs Station Park (4021 Main St): verify if distinct entities
- Heritage Rail Trail: check against 'Heritage Trail' (Tier 6 Columbus greenway) — possible cross-tier dedup
- Heritage Rail Trail: multi-county Franklin + Madison — flag for held-entity review per protocol

**Map verification status:** DEFERRED per project decision (Improvement #23).


---

### Tier 6 — Municipal: City of Grove City

**Status:** WEB PARTIAL / SIGNIFICANT GAP — 14 parks + 3 child sites confirmed; ~16-20 parks unidentified; map verification DEFERRED

**Method:** Web search snippets (grovecityohio.gov + visitgrovecity.com both egress-blocked; browser disconnected); addresses from Yelp, Google, emht.com, heartofgrovecity.org listings

**Sources checked:**
- grovecityohio.gov/182/City-Parks — EGRESS BLOCKED
- visitgrovecity.com — EGRESS BLOCKED
- Web search snippets (Yelp, Google, visitgrovecity.com search result descriptions)
- emht.com for Park at Beulah project description
- heartofgrovecity.org for Town Center Park

**City claims:** 30 parks, 518 acres

**Park Sites found (14, 10 with confirmed addresses):**
| Name | Address | Notes |
|---|---|---|
| Fryer Park | 3899 Orders Rd | 110 acres; softball, trail, playground, Century Village |
| Gantz Park | 2255 Home Rd | Historic farmhouse, arboretum, Gardens at Gantz |
| Windsor Park | 4408 Broadway | 38 acres; 11 baseball diamonds, batting cages, tennis |
| Westgrove Park | 3580 Magnolia St | Community park |
| Henceroth Park | 2075 Mallow Ln | 22 acres; eco-friendly, nature trail |
| Breck Community Park | 3005 Demorest Rd | Dog park (4 fenced areas) |
| Town Center Park | 3359 Park St | Downtown; FLAG: confirm managing entity |
| Park at Beulah | 3700 Glacial Lane | 32 acres; former Beulah Park horse track site |
| Blodwen Park | Blodwen Circle (approx) | Pocket park; address approximate |
| Creed Lawless Park | Kingston Ave (approx) | Pocket park; address approximate |
| Bicentennial Park | Grove City, OH (no street) | Address unknown |
| Sesquicentennial Park | Park St area (approx) | Address approximate |
| Indian Mound Park | Grove City, OH (no street) | Address unknown |
| Schiller Park | Grove City, OH (no street) | Address unknown; FLAG: confirm distinct from Columbus Schiller Park |

**Child Sites (3):**
- Gardens at Gantz (2255 Home Rd; child of Gantz Park)
- Eagle Pavilion (3899 Orders Rd; child of Fryer Park)
- Beulah Pavilion (3700 Glacial Lane; child of Park at Beulah)

**Records appended:** 18 (14 Park Sites + 3 Child Sites + 1 DiscoveryNote)
**Script:** gen_grove_city_yaml.py

**Gap notes:**
- City claims 30 parks; only 14 identified — ~16-20 parks completely unknown
- Big Run Park (4201 Clime Rd Columbus) is on Columbus Rec Parks website; NOT Grove City
- grovecityohio.gov completely blocked; must reconnect browser
- MUST REVISIT: highest priority — load grovecityohio.gov/182/City-Parks to get full list

**Map verification status:** DEFERRED per project decision (Improvement #23).


---

### Tier 6 — Municipal: City of Groveport

**Status:** WEB PARTIAL — 7 parks confirmed; ~1 may remain unidentified; map verification DEFERRED

**Method:** Web search snippets (groveport.org + groveportrec.com both egress-blocked; browser disconnected); addresses from Yelp, Google, tripadvisor listings

**Sources checked:**
- groveport.org/255/Features-Locations — EGRESS BLOCKED
- groveportrec.com — EGRESS BLOCKED
- Web search snippets (Yelp, Google, tripadvisor)

**Baseline seeds:** 8 seeds typed "Groveport City Park"
**City claims:** 7+ named parks (no explicit total acreage found in search snippets)

**Park Sites found (7):**
| Name | Address | Notes |
|---|---|---|
| Groveport Heritage Park | 551 Wirt Rd | 16.7 acres; historic Log House, Ohio Historical Marker |
| Groveport Park | Main St (approx) | 29 acres; historic Ohio & Erie Canal, restored Lock 22 |
| Degenhart Park | 355 Lesleh Ave | 7.2 acres; 3 lighted tennis courts, picnic shelter, playground |
| Founders Bend Park | 4329 Landings Rd | 5.29 acres; added 2016; 2 playgrounds |
| Veterans Park | Main St (approx) | 0.1 acres; memorial park, 4 areas (Donor's Common, Peace Garden, Honor Court, Quiet Garden) |
| Glendening Park | Groveport, OH (no street) | 10.4 acres; near Glendening Elementary; address unknown |
| Commerce Center Park | Groveport, OH (no street) | 25.2 acres; business district; large pond, paved path; address unknown |

**Address flags for Resolution:**
- Groveport Park: Main St approximate only — must verify exact number
- Veterans Park: Main St approximate only
- Glendening Park: no street number found
- Commerce Center Park: no street number found

**Resolution flags:**
- Groveport Recreation Center (7370 Groveport Rd) is admin/rec facility only; NOT recorded as park Site

**Records appended:** 8 (7 Park Sites + 1 DiscoveryNote)
**Script:** gen_groveport_yaml.py

**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Worthington

**Status:** WEB PARTIAL — 11 parks + 1 child site confirmed; ~1-2 gaps remain; map verification DEFERRED

**Method:** Web search snippets (worthington.org egress-blocked; browser disconnected); addresses from Yelp, Google, cbus4kids.com, eatplaycbus.com listings

**Sources checked:**
- worthington.org/252/Parks — EGRESS BLOCKED
- Web search snippets (Yelp, Google, cbus4kids.com, eatplaycbus.com)

**Baseline seeds:** 17 seeds typed "Worthington City Park"
**City claims:** 13 parks, 200+ acres

**Park Sites found (11):**
| Name | Address | Notes |
|---|---|---|
| McCord Park | 333 E Wilson Bridge Rd | ~25 acres; primary community park; sports fields, community garden, 2 shelters |
| Perry Park | 2300 Collins Dr | Community park |
| Selby Park | 358 Selby Blvd S | Neighborhood park |
| Wilson Hill Park | 1025 Ridgedale Dr E | Community park; "hidden gem"; natural wooded character |
| Pingree Park | 374 Pingree Dr | Community park; Worthington Facility ID 12 |
| Park Boulevard Park | 125 Park Blvd | Small park; Rush Creek corridor; Facility ID 10 |
| Godown Park | 6099 Godown Rd, Columbus | 10-acre dog park; co-managed Worthington/Columbus; physically in Columbus; FLAG cross-tier |
| Heischman Park | Worthington-Galena Rd (approx) | 1.4 acres; playground, tot lot; road-name address only |
| Worthington Village Green | High St & W New England Ave | Historic town green; 4 quadrants; intersection address |
| Whitney Playground | End of Whitney Ave | Small playground; Olentangy River Parklands corridor |
| East Granville Road Park | East Granville Rd (approx) | 7.8 acres; playground, shelter; contains Moses Wright Nature Area |

**Child Sites (1):**
- Moses Wright Nature Area (East Granville Rd; child of East Granville Road Park; named natural sub-unit)

**Address flags for Resolution:**
- Worthington Village Green: intersection address only; exact address unconfirmed
- Heischman Park: road-name only (Worthington-Galena Rd)
- East Granville Road Park: road-name only; no house number
- Godown Park: physically at 6099 Godown Rd, Columbus — confirm co-management; check Columbus Rec Parks cross-tier

**Resolution flags:**
- Antrim Park (5800 Olentangy River Rd, Columbus) is confirmed Columbus Rec Park — NOT Worthington; excluded
- Godown Park: potential cross-tier dedup with Columbus Rec Parks records

**Records appended:** 13 (11 Park Sites + 1 Child Site + 1 DiscoveryNote)
**Script:** gen_worthington_yaml.py

**Map verification status:** DEFERRED per project decision (Improvement #23).

---

# Session 5 (2026-03-14) — Bexley, New Albany, Reynoldsburg, Whitehall, Grandview Heights, Canal Winchester

**Status:** WEB PARTIAL for all municipalities — browser disconnected; all .gov domains egress-blocked.

**Method:** Web search snippets (Google, Yelp, Waze, Bark Park Finder, mypacer.com, cbus4kids.com, tripadvisor, columbusunderground.com, a1roofingsolutions.com, etc.), supplemented by WebFetch attempts (all blocked).

**Session also completed:** Groveport and Worthington session log entries (from Session 4 overflow); handoff updated for those municipalities.

---

### Tier 6 — Municipal: City of Bexley

**Status:** WEB PARTIAL — 5 parks + 3 child sites confirmed; map verification DEFERRED

**Method:** Web search snippets (bexley.org egress-blocked)

**City stats:** ~2.4 sq mi, ~13,000 pop; Year of the Parks 2023 completed major improvements

**Park Sites found (5):**
| Name | Address | Notes |
|---|---|---|
| Jeffrey Park | 165 N Parkview Ave | 30+ acres; Alum Creek frontage; Jeffrey Mansion, tennis courts, pool |
| Commonwealth Park | Commonwealth Park N (approx) | Athletic fields, passive area, arboretum walk (Oct 2023 improvements) |
| Schneider Park | 2130 Astor Ave | SW Bexley; splash pad, shelter, gardens, natural dog park |
| Havenwood Park | 2425 Havenwood Drive South | Oval passive park; unique tree species; Jazz in the Park |
| Denise G. Blank (DGB) Kindness Park | E Main St (approx) | Pocket park near Drexel Theatre |

**Child Sites (3):**
- David H. Madison Community Pool (2100 Clifton Ave; child of Jeffrey Park)
- Jeffrey Mansion (165 N Parkview Ave; child of Jeffrey Park; NRHP #80002999)
- Bexley Natural Dog Park (2130 Astor Ave; child of Schneider Park; opened June 2023)

**Resolution flags:** Commonwealth Park and DGB Kindness Park address-partial; Alum Creek Trail is Columbus Rec Parks asset NOT Bexley; Bexley Arboretum = community program, not separate landholding.

**Records appended:** 9 (5 Park Sites + 3 Child Sites + 1 DiscoveryNote)
**Script:** gen_bexley_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of New Albany

**Status:** WEB PARTIAL — 10 parks confirmed; DUAL MANAGING ENTITY; map verification DEFERRED

**Method:** Web search snippets (naparksohio.org + cityofnewalbany.com both egress-blocked)

**City stats:** 2,000+ acres open space claimed; 80+ miles leisure trails; two separate managing entities

**Park Sites found (10):**
| Name | Address | Managing Entity | Notes |
|---|---|---|---|
| Bevelhymer Park | 7860 Bevelhymer Rd | New Albany Parks & Recreation | 145 acres; 32 sports fields; district HQ |
| Thompson Park | 5600 Thompson Rd, Columbus 43230 | New Albany Parks & Recreation | 59 acres; Cross-tier FLAG: Columbus address |
| Silver Street Park | New Albany, OH (no street) | New Albany Parks & Rec / City | 14.875 acres; indoor sports turf; address unknown |
| Wexner Community Park | 600 Swickard Woods Blvd | City of New Albany | 2.2 acres; pavilion with fireplace |
| Rose Run Park | 200 W Main St | City of New Albany | Streamside park; completed 2019 |
| Taylor Farm Park | 5526 E Dublin-Granville Rd | City of New Albany | ~100 acres; former farm; Phase 1 open |
| Swickard Woods Park | 5101 Swickard Woods Blvd | City of New Albany | Wooded natural area/arboretum |
| Lambton Park | 7301 Lambton Green S | City of New Albany | Trails, large pond, playground |
| Ratchford Fens Park | New Albany, OH (no street) | City of New Albany | Passive open space; address unknown |
| Resch Park | New Albany, OH (no street) | City of New Albany | Adjacent to Ealy House; address unknown |

**Resolution flags:** Thompson Park at Columbus address — cross-tier check; Silver Street/Ratchford Fens/Resch Park addresses unknown; New Albany Parks & Rec district has ~17 areas but only 3 confirmed; Rocky Fork Metro Park = Tier 5.

**Records appended:** 11 (10 Park Sites + 1 DiscoveryNote)
**Script:** gen_new_albany_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Reynoldsburg

**Status:** WEB PARTIAL — 6 parks confirmed; 275 acres total; map verification DEFERRED

**Method:** Web search snippets (reynoldsburg.gov egress-blocked)

**Park Sites found (6):**
| Name | Address | Notes |
|---|---|---|
| Reynoldsburg Civic Park | 6800 Daugherty Dr | Main civic park; dog park area nearby |
| John F. Kennedy Park | 7232 E Main St | ~26 acres; skate park; 0.56-mi trail to Huber Park |
| Pine Quarry Park | 8000 Kingsley Dr | ~39 acres; former quarry; hiking trails |
| Huber Park (Heritage Sports Complex) | 1520 Davidson Dr | 43.1 acres; ball diamonds; 0.68-mi trail to JFK |
| Old Rodebaugh Park | 7300 Rodebaugh Rd | Playground, trails, gazebo; dog park vicinity |
| Memorial Plaza | Reynoldsburg, OH (no address) | Commemorative plaza; address unknown |

**Resolution flags:** Pine Quarry Park two addresses (8000 Kingsley vs 7907 Priestley); Huber Park two addresses (1520 Davidson vs 7300 Livingston); Old Rodebaugh Park multiple address variants; Blacklick Woods Metro Park = Tier 5.

**Records appended:** 7 (6 Park Sites + 1 DiscoveryNote)
**Script:** gen_reynoldsburg_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Whitehall

**Status:** WEB PARTIAL — 7 parks confirmed (3 addresses partial); 115+ acres; map verification DEFERRED

**Method:** Web search snippets (whitehall-oh.us egress-blocked)

**Park Sites found (7):**
| Name | Address | Notes |
|---|---|---|
| Whitehall Community Park | 360 S Yearling Rd | 60 acres; upper and lower level; YMCA co-located (not city asset) |
| John Bishop Memorial Park | 4815 Etna Rd | Most active park; splashpad, amphitheater, baseball/softball, hockey, courts |
| Norton Field Park | 4464 San Jose Ln | Small neighborhood park; toddler playground |
| Lamby Lane Park | Beechwood Rd & Lamby Ln (approx) | Small park; paved loop, workout station, shelter |
| Robinwood Park | Robinwood Ave (approx) | Small neighborhood park; playground, picnic |
| The Kelley Green | 105 Norton Park Dr | Contemporary gathering space in Norton Crossing development |
| Central Bark Dog Park | Washburn St (approx) | Off-leash dog park; 2 fenced areas; closed Mondays |

**Resolution flags:** Lamby Lane/Robinwood/Central Bark addresses partial; YMCA at 402 N Hamilton Rd is NOT city park asset.

**Records appended:** 8 (7 Park Sites + 1 DiscoveryNote)
**Script:** gen_whitehall_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Grandview Heights

**Status:** WEB PARTIAL — 9 sites confirmed; ~45 acres; map verification DEFERRED

**Method:** Web search snippets (grandviewheights.gov egress-blocked)

**Park Sites found (9):**
| Name | Address | Notes |
|---|---|---|
| McKinley Field | 1661 Goodale Blvd | Primary sports complex; Parks & Rec HQ; 4 tennis courts |
| C. Ray Buck Sports Park | 1280 Goodale Blvd | 7.8 acres |
| Wyman Woods Park | 1515 Goodale Blvd | 6 acres; wooded |
| Grandview Heights Memorial Park | 1135 W 2nd Ave | Small neighborhood memorial park |
| Pierce Field | 1175 Hilo Ln | 2 tennis courts, 4 pickleball courts |
| Urlin Tennis Courts | 1755 Goodale Blvd | 4 tennis courts, practice wall |
| Grandview Heights Skate Park | 1350 Goodale Blvd | In Municipal Pool parking lot |
| Wallace Gardens | Grandview Ave & Goodale Blvd (approx) | Community garden; serves Grandview Heights + Marble Cliff |
| Miller Park | Grandview Heights, OH (no address) | Neighborhood park; address unknown |

**Resolution flags:** Pierce Field two addresses (1175 Hilo Ln vs 1080 W 1st Ave); Wallace Gardens intersection only; Miller Park address unknown; Marble Cliff village parks deferred (separate Tier 6 entity); Columbus Goodale Park is NOT Grandview Heights; Scioto Audubon = Tier 5.

**Records appended:** 10 (9 Park Sites + 1 DiscoveryNote)
**Script:** gen_grandview_heights_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Canal Winchester

**Status:** WEB PARTIAL — 5 parks + 1 trail confirmed; 307 acres; map verification DEFERRED

**Method:** Web search snippets (canalwinchesterohio.gov + destinationcw.org both egress-blocked)

**Park Sites found (5):**
| Name | Address | Notes |
|---|---|---|
| Roger Hanners Recreational Fields & Skate Park | 458 Groveport Rd | 6 baseball/softball fields, batting cage, skate park |
| McGill Park | 6725 Lithopolis-Winchester Rd | Soccer fields, nature playground, pickleball (July 2024), 3-season shelter (May 2024) |
| Westchester Park | 6620 Dietz Dr | Neighborhood park; playground, shelter, lending library |
| Stradley Place | 30 S High St | Downtown green space; gazebo; Music in the Park host |
| Downtown Canal Winchester Park | N High St (approx) | Canal stones feature, playset, basketball; may overlap with Stradley Place |

**Trail found (1):**
- Canal Winchester Trail System (~8 miles; Walnut Creek Trail + Winchester Trail segments; network address TBD)

**Resolution flags:** Downtown Park vs Stradley Place — may be same park; Winchester Meadows Park is Columbus Rec Parks asset NOT Canal Winchester city park; Walnut Woods/Slate Run/Chestnut Ridge = Tier 5 Metro Parks.

**Records appended:** 7 (5 Park Sites + 1 Trail + 1 DiscoveryNote)
**Script:** gen_canal_winchester_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

# Session 6 (2026-03-14) — Obetz, Pickerington, and All Franklin County Villages

**Status:** WEB PARTIAL for all; browser disconnected; .gov domains mostly egress-blocked.

**Method:** Web search snippets (Google, Yelp, Waze, columbusmessenger.com, tripadvisor, city/village websites via search snippets, 2026-03-14).

**ALL TIER 6 MUNICIPAL WEB DISCOVERY COMPLETE** — All 16 cities + 9 villages in Franklin County have been processed. Tier 7 and browser revisit queue are the next priorities.

---

### Tier 6 — Municipal: City of Obetz

**Status:** WEB PARTIAL — 8 Sites confirmed (7 parks + 1 child); 136 acres; map verification DEFERRED

**City stats:** 136 acres, 7 parks, 18 courts/fields, 5 shelter houses, 2 splash pad/ice rink facilities

**Park Sites found (7) + 1 Child Site:**
| Name | Address | Notes |
|---|---|---|
| Memorial Park | 4175 Alum Creek Dr | 80 acres; softball/baseball, football/soccer, playground, 1-acre fishing pond |
| Junction Park (fka Lancaster Park) | 4390 Lancaster Ave | 4.5 acres; splash pad/ice rink combo; shelter, playground, Bocce |
| Community Center Park | 1650 Obetz Ave | 3 acres; tennis, 2 basketball, playground |
| Dixon Quarry | 4400 Industrial Center Dr | 6-acre lake; archery, walking paths, pavilion, fitness trails |
| Bridlewood Park | Bridlewood Blvd (approx) | Neighborhood park; address road-name only |
| McFadyen Park | Jermoore Rd (approx) | 3 acres; swings, climbing toy, basketball |
| Veterans Park | Groveport Rd (approx) | ~0.5 acres; memorial park; address road-name only |
| Fortress Obetz (child of Memorial Park) | 4175 Alum Creek Dr | Entertainment/sports complex within Memorial Park |

**Records appended:** 9 (8 Sites + 1 Note)
**Script:** gen_remaining_municipalities_yaml.py
**Map verification status:** DEFERRED per project decision (Improvement #23).

---

### Tier 6 — Municipal: City of Pickerington

**Status:** CROSS-COUNTY NOTE — primarily Fairfield County; no confirmed parks in Franklin County portion

**Notes:** Pickerington city parks (Sycamore Creek, Victory, Colony, Simsbury, Willow Pond) all in Fairfield County (43147 ZIP). Franklin County portion has no confirmed dedicated parks. Pickerington Ponds Metro Park is Tier 5 (Metro Parks). Main parks will be recorded during Fairfield County run.

**Records appended:** 1 (1 DiscoveryNote only)

---

### Tier 6 — Village: Marble Cliff

**Status:** WEB PARTIAL — 4 park Sites confirmed; 2 addresses partial; map verification DEFERRED

**Village stats:** ~175 acres total, ~600 pop

**Park Sites found (4):**
| Name | Address | Notes |
|---|---|---|
| Paul J. Falco Park | Fernwood Ave (approx) | Playground, walking trails; road-name address only |
| Tarpy Woods | S end of Cambridge Blvd | 8 acres; wooded natural area |
| Island Greenspace | Marble Cliff, OH (unknown) | Village-maintained greenspace; address unknown |
| Marble Cliff Quarry Park | Marble Cliff, OH (unknown) | Scenic trails and lake at former quarry; address unknown |

**Records appended:** 5 (4 Sites + 1 Note)

---

### Tier 6 — Village: Minerva Park

**Status:** WEB PARTIAL — Village-wide recreation model; 2 entities recorded; map verification DEFERRED

**Village stats:** ~5,000 pop; designed as park-like residential community around Minerva Lake

**Entities (2):**
- Minerva Park Village Green / Recreation Area — 2829 Minerva Lake Rd (village address)
- Minerva Park Community Pool — Minerva Lake Rd (address partial)

**Note:** Camp Mary Orton (Godman Guild, campmaryorton.org) is a separate org on Minerva Lake Rd; NOT village park — investigate separately (possible Tier 7 or Tier 8).

**Records appended:** 3 (2 Sites + 1 Note)

---

### Tier 6 — Village: Valleyview

**Status:** WEB PARTIAL — 1 of 2 parks confirmed; second park unknown; map verification DEFERRED

**Village stats:** Small village (~800 pop), 43204 ZIP

**Park Sites found (1):**
- Dibblee Park — Dibblee Ave & N Richardson Ave (intersection address)

**Second park:** name and address not found from web search. MUST REVISIT.

**Records appended:** 2 (1 Site + 1 Note)

---

### Tier 6 — Village: Urbancrest

**Status:** WEB PARTIAL — 1 community park confirmed; address partial; map verification DEFERRED

**Village stats:** ~800 pop, 43123 ZIP

**Park Sites found (1):**
- Urbancrest Community Park — 1st Ave (near village hall 3492 1st Ave); shelter house, basketball

**Records appended:** 2 (1 Site + 1 Note)

---

### Tier 6 — Village: Brice

**Status:** NULL — no confirmed municipal parks

**Village stats:** ~500 pop; very small rural village in SE Franklin County

No named parks or recreational facilities identified via web search. Village may rely on Franklin Township or Columbus Metro Parks. Discovery note recorded.

**Records appended:** 1 (1 Note only)

---

### Tier 6 — Village: Harrisburg

**Status:** NULL — no confirmed municipal parks

**Village stats:** 315 pop, 0.15 sq mi; straddles Franklin and Pickaway counties

No named parks or recreational facilities identified via web search. Discovery note recorded.

**Records appended:** 1 (1 Note only)

---

### Tier 6 — Village: Lockbourne

**Status:** WEB PARTIAL — 2 parks confirmed; 1 address partial; map verification DEFERRED

**Village stats:** ~200 pop; historic canal village on Big Walnut Creek

**Park Sites found (2):**
| Name | Address | Notes |
|---|---|---|
| Locke Meadow Park | 72 Commerce St | Along Big Walnut Creek; Magnolia Trail; restored Ohio & Erie Canal locks; playground, picnic |
| Veterans Park | Commerce St (approx) | Memorial park adjacent to Locke Meadow Park; address road-name only |

**Records appended:** 3 (2 Sites + 1 Note)

---

### Tier 6 — Village: Riverlea

**Status:** WEB PARTIAL — 1 village green confirmed; address partial; map verification DEFERRED

**Village stats:** ~500 pop; small residential enclave north of Columbus

**Park Sites found (1):**
- Circle Park — Riverglen Dr (road-name address); host to annual village events (Easter egg hunt, summer picnic, Halloween)

**Records appended:** 2 (1 Site + 1 Note)

---

### Tier 6 — Village: Lithopolis

**Status:** CROSS-COUNTY / WEB PARTIAL — primarily Fairfield County; 2 parks found; county of each TBD; map verification DEFERRED

**Village stats:** ~2,000 pop; spans Fairfield and Franklin counties

**Park Sites found (2):**
| Name | Address | Notes |
|---|---|---|
| Wilson Park | Market St, Lithopolis (approx) | Road-name address only; county boundary TBD |
| Alice Smith Nature Preserve | OH-674 S / Winchester Southern Rd (approx) | Village nature preserve; county boundary TBD |

**Cross-tier note:** Walnut Woods Metro Park (1,032 acres, Lithopolis Rd) is Tier 5 Metro Parks, NOT Lithopolis village asset.

**Records appended:** 3 (2 Sites + 1 Note)

---

### SESSION 6 TOTALS

| Municipality | Sites | Notes | Total |
|---|---|---|---|
| Obetz | 8 | 1 | 9 |
| Pickerington | 0 | 1 | 1 |
| Marble Cliff | 4 | 1 | 5 |
| Minerva Park | 2 | 1 | 3 |
| Valleyview | 1 | 1 | 2 |
| Urbancrest | 1 | 1 | 2 |
| Brice | 0 | 1 | 1 |
| Harrisburg | 0 | 1 | 1 |
| Lockbourne | 2 | 1 | 3 |
| Riverlea | 1 | 1 | 2 |
| Lithopolis | 2 | 1 | 3 |
| **TOTAL** | **21** | **11** | **32** |

**Staging file total after Session 6: 896 entity records (confirmed)**
**ALL TIER 6 MUNICIPAL WEB DISCOVERY COMPLETE** — 16 cities + 9 villages processed. Next: Tier 7 (Conservancy/Land Trust) and browser reconnect revisit queue.


---

## Session 7 — 2026-03-14

### Bootstrap
- Continued from Session 6; session log, staging file, and MORPC CSV loaded
- Chrome (Claude in Chrome) reconnected
- MORPC Parks and Open Space dataset downloaded as CSV — 4,469 records, 15-county MORPC region, data updated 2025-07-01

---

### MORPC Dataset Acquisition

**Source:** Mid-Ohio Regional Planning Commission — Parks and Open Space feature layer
**URL:** https://public-morpc.hub.arcgis.com/datasets/parks-and-open-space/explore
**File:** Parks_and_Open_Space_7241389496048841555.csv (saved to project root)
**Record count:** 4,469 total | 1,894 Franklin County records
**Data updated:** 2025-07-01

**Sub_Type codes confirmed:** C=Community Park, N=Neighborhood Park, NOS=Neighborhood Open Space, R=Regional Park, M=Metro Park, NAT=Natural Area, PRES/PR/P=Preserve, REC=Recreation/Special Use, SPU=Special Use/Facility, GOLF=Golf Course, CEM=Cemetery, CON=Conservation Area, STATE=State, W=Wildlife Area

**Strategic value:** Covers every Franklin County municipality — primary cross-reference layer for all remaining discovery tiers and reconciliation passes.

---

### Tier 6 — Municipal: City of Gahanna — Pocket Parks Resolution

**Status: COMPLETE** — Pocket Parks / Open Spaces / Reserves PENDING resolved via MORPC dataset

**Method:** Filtered MORPC CSV to Jurisdiction = Gahanna (70 records); cross-referenced against existing staging entries; appended net-new entities; removed 5 duplicates; added MORPC cross-ref notes to 6 existing gahanna.gov entries.

**MORPC Gahanna record breakdown:**
- Total Gahanna records in MORPC: 70
- Matched to existing staging entries: 15
- Skipped — unnamed parcels: 5 (OPEN SPACE A/B/C, OPEN SPACE, PUBLIC PARK OR PLAYGROUND)
- Skipped — cemeteries: 5
- Duplicates removed after staging cross-check: 5 (Shull Park, Rathburn Woods, Trapp Park, Veterans Memorial Park, Woodside Green Park)
- **Net new entities appended to staging: 36**

**New Community Parks (6):**
| Name | Acres | ParkID | Notes |
|---|---|---|---|
| Clarenton Green Park | 2.817 | 129 | Shares ParkID with Clarenton Green Reserve — flag |
| Clarenton Green Reserve | 4.324 | 129 | Shares ParkID with Clarenton Green Park — flag |
| Lintner Park | 1.871 | 159 | Shares ParkID with Creekside Park — possible MORPC error |
| Price Road Park | 52.003 | — | Absent from gahanna.gov |
| Taylor Road Reserve | 51.437 | — | Absent from gahanna.gov |
| Y Park | 12.254 | 2 | |

**New Neighborhood Parks (13):**
| Name | Acres | ParkID |
|---|---|---|
| Bryn Mawr Woods Reserve | 1.372 | 101 |
| Fleetrun Park | 5.023 | 222 |
| Foxboro Basin | 2.534 | 226 |
| Foxwood-Rice Ave Park | 7.184 | — |
| Goshen Park | 0.385 | 260 |
| Gramercy Park | 0.275 | 262 |
| Olde Ridenour Road Open Space | 0.521 | 553 |
| Pipers Glen Basin | 1.193 | 644 |
| Royal Gardens Park | 0.262 | 697 |
| Shagbark Reserve | 2.427 | 582 |
| Sycamore Run Park | 7.416 | — |
| Underwood Reserve | 2.847 | 583 |
| Woodside Green South Park | 3.913 | — |

**New Neighborhood Open Spaces (15 entities from 18 records):**
| Name | Acres | ParkID | Notes |
|---|---|---|---|
| Agler Road Parkway | 6.944 | 6 | |
| Caroway Reserve | 1.188 | 108 | |
| Carpenter Road Open Space | 1.236 | — | |
| Central Park Reserve | 22.395 | — | 3 parcels consolidated |
| Clark State Basin | 1.893 | 579 | |
| Gahanna Grove Reserve | 2.617 | — | |
| Galloway Reserve | 23.963 | — | |
| Harrison Pond Open Space | 9.401 | — | |
| Helmbright Woods Reserve | 3.634 | 301 | |
| McKenna Creek Parkway | 5.912 | 398 | |
| South Hamilton Road Open Space | 0.626 | — | |
| The Villages of Gahanna Open Space | 1.280 | — | |
| Three Corners Park | 1.090 | — | |
| Village at Hannah Farms Reserve | 3.459 | — | 2 parcels consolidated |
| Woodmark Woods Reserve | 9.985 | — | |

**New Preserves (2):** Rocky Fork Reserve (6.665 ac), Shull Reserve (1.508 ac, ParkID 581)

**New Regional Parks (1):** Woodside Green Park (32.847 ac) — classification conflict with existing gahanna.gov entry; flag for resolution

**MORPC cross-ref notes added to 6 existing gahanna.gov entries:**
- Shull Park: 10.494 ac, ParkID 736
- Rathburn Woods Park: MORPC name "Rathburn Woods," 1.483 ac, ParkID 657
- Trapp Park: 2.938 ac
- Veterans Memorial Park: 1.738 ac, ParkID 405 — classification conflict (Community vs Neighborhood Park)
- Woodside Green Park: 32.847 ac — classification conflict (Community vs Regional Park)
- Rice Avenue Park: possible same entity as MORPC "Foxwood-Rice Ave Park" (7.184 ac)

**Gahanna Tier 6 final count:** ~66 entity records
**Gahanna Tier 6 status: COMPLETE (MORPC-sourced)**

---

## Columbus MORPC Cross-Check — 2026-03-14

**Objective:** Cross-reference the MORPC Parks and Open Space dataset against existing Columbus entries in the staging YAML, and append net-new entities not already captured from the baseline.

**MORPC Columbus records (FRA, Jurisdiction = Columbus):** 755 raw records

**Filtering applied:**
- Street islands / planting strips / open space unnamed fragments: ~88 excluded
- Metro Parks (Sub_Type = M): excluded by name — Blendon Woods (649 ac), Highbanks (343 ac), Three Creeks (1,631 ac), Pickerington Ponds (1,154 ac), Quarry Park, Scioto Audubon, etc. — already captured Tier 3
- Cemeteries (Sub_Type = CEM): excluded
- Golf courses (Sub_Type = GOLF): excluded
- Unnamed / zero-acre parcels: excluded

**Cross-reference against staging:** Fuzzy name match (name_lower in staging_name or staging_name in name_lower). Matched entities were skipped as already known.

**Net-new Columbus entities appended: 147**

Inserted at line 19,132 in `franklin_oh_raw_discovery.yaml` (before Westerville section / Alum Creek Park North). Columbus MORPC entries now span lines 19,132–21,483.

**Breakdown by type:**

| Park Type | Count |
|---|---|
| Neighborhood Open Space | 35 |
| Neighborhood Park | 34 |
| Conservation Area | 22 |
| Community Park | 21 |
| Preserve | 13 |
| Special Use/Facility | 11 |
| Regional Park | 6 |
| Recreation/Special Use | 5 |
| **Total** | **147** |

**Notable large entities (≥50 ac):**
- Hoover Reservoir: 972.656 ac (Regional Park) — major Columbus water supply reservoir
- Galloway Road Clean Ohio Parkland: 123.519 ac (Preserve)
- Mock Road Park: 102.686 ac (Regional Park)
- SHADEVILLE NURSERY: 58.872 ac (Special Use/Facility)
- Thompson Road Park: 58.736 ac (Community Park)
- Case Road Parkland: 58.045 ac (Preserve)
- Athletic Field: 55.614 ac (Recreation/Special Use)
- Soccer Fields: 54.761 ac (Recreation/Special Use)
- Franks Park: 53.681 ac (Community Park)
- Klingbeil Parkland: 52.694 ac (Preserve)

**Source:** MORPC Parks and Open Space dataset (public-morpc.hub.arcgis.com), data updated 2025-07-01. All entries tagged `managing_entity_raw: Columbus Recreation and Parks Department`, `status: RAW`, `tier: 6`.

**Columbus Tier 6 status:** Substantially expanded; MORPC cross-check complete. Resolution pass recommended to reconcile name variants, deduplicate multi-parcel entries, and confirm acreage against Columbus Recreation and Parks official records.

---

# Session 8 (2026-03-14) — MORPC Cross-Check: All Remaining Tier 6 Municipalities

**Objective:** Apply MORPC Parks and Open Space dataset (public-morpc.hub.arcgis.com, data updated 2025-07-01) cross-check to all Franklin County Tier 6 municipalities not yet processed. Method mirrors Sessions 7 (Gahanna) and 7b (Columbus): filter → deduplicate → fuzzy cross-reference → append net-new.

**Global skip filters applied to all municipalities:**
- Sub_Type = CEM (cemetery), GOLF, M (Metro Park)
- Metro Parks by name (Blendon Woods, Highbanks, Three Creeks, etc.)
- Street islands, planting strips, unnamed open space fragments
- Lettered sub-parcel open spaces (Dublin-specific: names ending in quoted letter suffix or space+letter)

**Source:** MORPC Parks and Open Space dataset. All new entries tagged `status: RAW`, `tier: 6`, `discovery_date: 2026-03-14`.

---

### Dublin
**MORPC records:** 168 | **Net-new appended:** 29 | **Already known:** 67

**Notable entities (≥10 ac):**
- Ml Red Trabue Nature Reserve: 74.063 ac (Community Park)
- Riverside Drive Park: 40.217 ac (Community Park)
- Northeast Quad Park: 33.931 ac (Community Park)
- Ballentree Community Park: 24.872 ac (Community Park)
- Brandon Nature Preserve: 22.491 ac (Preserve)
- Holder-Wright Earthworks: 20.327 ac (Neighborhood Open Space)

**By type:** Community Park: 5; Neighborhood Open Space: 16; Neighborhood Park: 5; Preserve: 3
- Local skip filters removed 27 records (sub-parcels, wrong-jurisdiction entries, non-park facilities)

### Westerville
**MORPC records:** 56 | **Net-new appended:** 18 | **Already known:** 16

**Notable entities (≥10 ac):**
- Highland Park: 39.810 ac (Community Park)
- Ridgewood Park: 28.225 ac (Community Park)
- Spring Grove North Greenway: 15.218 ac (Community Park)
- College Knoll Wetlands: 13.888 ac (Community Park)
- Boyer Nature Preserve: 11.609 ac (Community Park)

**By type:** Community Park: 6; Neighborhood Open Space: 4; Neighborhood Park: 6; Regional Park: 2
- Local skip filters removed 2 records (sub-parcels, wrong-jurisdiction entries, non-park facilities)

### Bexley
**MORPC records:** 61 | **Net-new appended:** 1 | **Already known:** 6


**By type:** Neighborhood Park: 1
- Local skip filters removed 6 records (sub-parcels, wrong-jurisdiction entries, non-park facilities)

### Grove City
**MORPC records:** 55 | **Net-new appended:** 27 | **Already known:** 8

**Notable entities (≥10 ac):**
- Southeast Conservation Club: 284.793 ac (Preserve)
- Murfin Fields: 50.399 ac (Community Park)
- Buckeye Parkway Open Space: 35.151 ac (Neighborhood Open Space)
- Gantz Road Open Space: 34.282 ac (Neighborhood Open Space)
- Creekside Park: 26.933 ac (Community Park)
- Demorest Road Park: 23.098 ac (Neighborhood Park)
- Meadow Grove Open Space: 17.753 ac (Neighborhood Open Space)
- Meadowgrove Park: 12.021 ac (Community Park)

**By type:** Community Park: 8; Neighborhood Open Space: 9; Neighborhood Park: 7; Preserve: 1; Recreation/Special Use: 2

### Upper Arlington
**MORPC records:** 30 | **Net-new appended:** 3 | **Already known:** 15

**Notable entities (≥10 ac):**
- Northwest Park: 21.226 ac (Community Park)
- Langston Park: 14.676 ac (Neighborhood Park)

**By type:** Community Park: 1; Neighborhood Park: 2

### Hilliard
**MORPC records:** 29 | **Net-new appended:** 5 | **Already known:** 20

**Notable entities (≥10 ac):**
- Clarence W Latham Educational Park: 18.825 ac (Neighborhood Park)

**By type:** Community Park: 1; Neighborhood Open Space: 2; Neighborhood Park: 2

### New Albany
**MORPC records:** 31 | **Net-new appended:** 12 | **Already known:** 4

**Notable entities (≥10 ac):**
- Nature Preserve: 27.244 ac (Preserve)
- Kitzmiller Road Open Space: 25.982 ac (Neighborhood Open Space)
- James River Road Open Space: 15.166 ac (Community Park)
- Planters Grove Open Space: 10.884 ac (Neighborhood Open Space)

**By type:** Community Park: 2; Neighborhood Open Space: 8; Neighborhood Park: 1; Preserve: 1
- FLAG: GENERIC NAME: Nature Preserve — needs address verification at Resolution

### Worthington
**MORPC records:** 25 | **Net-new appended:** 13 | **Already known:** 6

**Notable entities (≥10 ac):**
- Olentangy River Parklands: 108.380 ac (Preserve)
- Rush Run Park: 38.953 ac (Regional Park)
- Linworth Park: 12.552 ac (Community Park)

**By type:** Community Park: 2; Neighborhood Open Space: 2; Neighborhood Park: 6; Preserve: 1; Recreation/Special Use: 1; Regional Park: 1

### Canal Winchester
**MORPC records:** 25 | **Net-new appended:** 9 | **Already known:** 2

**Notable entities (≥10 ac):**
- Walnut Creek Park: 75.231 ac (Preserve)
- Ashbrook Road Open Space: 42.644 ac (Preserve)
- Hanners Park: 10.079 ac (Community Park)

**By type:** Community Park: 1; Neighborhood Open Space: 3; Neighborhood Park: 3; Preserve: 2
- Local skip filters removed 1 records (sub-parcels, wrong-jurisdiction entries, non-park facilities)

### Reynoldsburg
**MORPC records:** 15 | **Net-new appended:** 4 | **Already known:** 5

**Notable entities (≥10 ac):**
- J.F. Kennedy Park: 27.278 ac (Community Park)

**By type:** Community Park: 2; Neighborhood Open Space: 1; Neighborhood Park: 1

### Obetz
**MORPC records:** 13 | **Net-new appended:** 7 | **Already known:** 4

**Notable entities (≥10 ac):**
- Braehead Nature Preserve: 34.575 ac (Conservation Area)
- Area 51 Disc Golf Course: 31.494 ac (Recreation/Special Use)
- Brown Park: 18.519 ac (Community Park)

**By type:** Community Park: 1; Conservation Area: 1; Neighborhood Park: 3; Recreation/Special Use: 1; Special Use/Facility: 1

### Groveport
**MORPC records:** 12 | **Net-new appended:** 5 | **Already known:** 2

**Notable entities (≥10 ac):**
- Groveport Cruiser Park: 87.747 ac (Regional Park)
- Blacklick Park: 10.778 ac (Community Park)
- Orchard Park: 10.515 ac (Community Park)

**By type:** Community Park: 2; Neighborhood Park: 2; Regional Park: 1
- Local skip filters removed 1 records (sub-parcels, wrong-jurisdiction entries, non-park facilities)

### Grandview Heights
**MORPC records:** 11 | **Net-new appended:** 2 | **Already known:** 6


**By type:** Neighborhood Park: 1; Recreation/Special Use: 1

### Whitehall
**MORPC records:** 7 | **Net-new appended:** 2 | **Already known:** 4

**Notable entities (≥10 ac):**
- John Bishop Park: 38.157 ac (Community Park)

**By type:** Community Park: 1; Neighborhood Open Space: 1

### Marble Cliff
**MORPC records:** 5 | **Net-new appended:** 0 | **Already known:** 3

*No net-new entities — all MORPC records already in staging.*

### Lockbourne
**MORPC records:** 2 | **Net-new appended:** 1 | **Already known:** 0


**By type:** Community Park: 1

### Riverlea
**MORPC records:** 2 | **Net-new appended:** 0 | **Already known:** 1

*No net-new entities — all MORPC records already in staging.*

### Harrisburg
**MORPC records:** 1 | **Net-new appended:** 1 | **Already known:** 0


**By type:** Neighborhood Park: 1

### Urbancrest
**MORPC records:** 1 | **Net-new appended:** 0 | **Already known:** 1

*No net-new entities — all MORPC records already in staging.*

### Valleyview
**MORPC records:** 2 | **Net-new appended:** 2 | **Already known:** 0


**By type:** Neighborhood Open Space: 1; Neighborhood Park: 1

---

## Summary

**Total net-new entities appended this session: 141**

| Municipality | MORPC Records | Net-New | Already Known |
|---|---|---|---|
| Dublin | 168 | 29 | 67 |
| Westerville | 56 | 18 | 16 |
| Bexley | 61 | 1 | 6 |
| Grove City | 55 | 27 | 8 |
| Upper Arlington | 30 | 3 | 15 |
| Hilliard | 29 | 5 | 20 |
| New Albany | 31 | 12 | 4 |
| Worthington | 25 | 13 | 6 |
| Canal Winchester | 25 | 9 | 2 |
| Reynoldsburg | 15 | 4 | 5 |
| Obetz | 13 | 7 | 4 |
| Groveport | 12 | 5 | 2 |
| Grandview Heights | 11 | 2 | 6 |
| Whitehall | 7 | 2 | 4 |
| Marble Cliff | 5 | 0 | 3 |
| Lockbourne | 2 | 1 | 0 |
| Riverlea | 2 | 0 | 1 |
| Harrisburg | 1 | 1 | 0 |
| Urbancrest | 1 | 0 | 1 |
| Valleyview | 2 | 2 | 0 |

**Staging YAML final line count:** 27,609 (was 25,477)

**ALL TIER 6 MUNICIPAL MORPC CROSS-CHECKS COMPLETE.** All 16 cities + 9 villages in Franklin County have been cross-referenced against MORPC Parks and Open Space dataset. Tier 6 discovery complete; ready for Resolution pass.

---

## Session 9 (2026-03-14): Tier 7 — Conservancy / Land Trust

**Objective:** Discover privately governed conservation entities in Franklin County held by land trusts, conservancies, and national/regional conservation organizations.

### Organizations Researched

| Organization | Franklin County Holdings | Disposition |
|---|---|---|
| Central Ohio Land Trust (COLT) | Camp Mary Orton (167 ac) noted; primary holdings in Madison/Licking Counties | Camp Mary Orton deferred to Tier 8 (private institutional camp, not public preserve) |
| Columbus Audubon Society | Calamus Swamp (Pickaway County only); no confirmed Franklin County preserves | NULL — Pickaway, not Franklin |
| The Nature Conservancy — Ohio | No Franklin County properties listed in Ohio preserve inventory | NULL |
| Appalachian Ohio Alliance (AOA) | Big Darby preserves: Mishe Moneto, Gunning/Fickardt, Bartley, Confluence, Cossin-Kreisel — all Pickaway County | NULL — Pickaway, not Franklin |
| National Audubon Society / Audubon Ohio | Grange Insurance Audubon Center (5 ac), 505 W. Whittier St., Columbus — subleases from Metro Parks within Scioto Audubon Metro Park | **CONFIRMED Tier 7 entity** |
| Ohio Natural Areas Program (DNAP) | Administers SNPs (documented Tier 2); no separate Tier 7 holdings identified | Already captured Tier 2 |

### Tier 7 Entities Confirmed

**1 entity confirmed:**

| Name | Type | Address | Owner/Operator | Acreage | Notes |
|---|---|---|---|---|---|
| Grange Insurance Audubon Center | Site | 505 W. Whittier St., Columbus, OH 43215 | National Audubon Society / Audubon Ohio | 5 ac | Subleases from Columbus & Franklin County Metro Parks; within Scioto Audubon Metro Park; cross-tier flag with Tier 3 |

### Deferred Entities

**Camp Mary Orton** (7925 N. High St., Columbus, OH 43085; 167 acres; Godman Guild Association): Private institutional summer camp and retreat center. Not a public nature preserve or public access trail network. Deferred to **Tier 8** (Private). DiscoveryNote appended to staging YAML.

### YAML Documents Appended (3)

1. **Grange Insurance Audubon Center** — `entity_type: Site`, `discovery_tier: 7`, v5.1 schema; ownership: National Audubon Society (subleases 5 ac from Metro Parks)
2. **Camp Mary Orton DiscoveryNote** — `entity_type: DiscoveryNote`, `discovery_tier: 7`; deferred to Tier 8; Godman Guild Association, 167 ac
3. **Tier 7 Null DiscoveryNote** — `entity_type: DiscoveryNote`, `discovery_tier: 7`; documents all organizations checked and evidence of non-Franklin County holdings; sparse-result documentation

**Staging YAML:** 27,609 → **27,702 lines** (+93 lines, 3 documents)

### Research Notes

- Franklin County is largely urbanized; the major conservation corridor (Big Darby / Hellbranch) crosses into Pickaway/Madison Counties where AOA and Columbus Audubon hold preserves
- The Metro Parks system (Tier 3) effectively absorbs much of what would otherwise be Tier 7 territory in Franklin County — e.g., GIAC operates *within* a Metro Parks site on subleased land
- No COLT accredited land trust preserves with public access confirmed in Franklin County proper
- Tier 7 result: **sparse** (1 entity confirmed, 1 deferred to Tier 8, remainder null with evidence)

**TIER 7 COMPLETE (sparse result documented).**

---

## Session 10 — 2026-03-16

### Tier 8 — Private Natural Areas

**Session type:** Tier 8 complete  
**Session scope:** Franklin County Tier 8 (Private) — systematic discovery per `na_private_discovery_subproc_v5.2.md`

### Methods Used

1. Direct searches — private nature center, preserve, scout camp, church camp, retreat center, hunting preserve (all required Method 1 queries)
2. Cross-reference from prior tiers — Camp Mary Orton (deferred from Tier 7), ZipZone (noted in T8 prior note), partnership mentions
3. Specific organization searches — Girl Scouts of Ohio's Heartland, Simon Kenton Council BSA, Big Brothers Big Sisters Central Ohio, Ohio State University natural areas, Capital University, Otterbein University
4. Statewide directories — TrekOhio Franklin County page, ACA Camps, ODNR hunting preserve registry (no Franklin County results)
5. Browser fetch — direct navigation to campmaryorton.org, u.osu.edu/orwrpramsar (ORWRP visiting-us page confirmed)

### Tier 8 Entities Confirmed

| # | Name | Type | Address | Owner/Operator | Acreage | Access | Notes |
|---|---|---|---|---|---|---|---|
| T8-001 | Camp Mary Orton | Site | 7925 N. High St., Columbus, OH 43235 | Godman Guild Association (nonprofit) | 167 ac | Limited (program + fee) | Documented prior session; confirmed; ZipZone operates within property |
| T8-002 | Camp Ken-Jockety & The Elam Environmental Center | Site | 1295 Hubbard Rd, Galloway, OH 43119 | Girl Scouts of Ohio's Heartland (nonprofit) | 220 ac | Limited (reservation/program) | Near Big Darby Creek; trails, Becky's Pond, canoeing, archery; NEW this session |
| T8-003 | Ginny and John Elam Environmental Center | Child Site | 1295 Hubbard Rd, Galloway, OH 43119 | Girl Scouts of Ohio's Heartland (nonprofit) | within T8-002 | Limited (program) | Named donor facility within Camp Ken-Jockety; env. ed. center; NEW this session |
| T8-004 | Wilma H. Schiermeier Olentangy River Wetland Research Park | Site (TIER-FLAGGED) | 352 W. Dodridge St., Columbus, OH 43202 | The Ohio State University | 52 ac | Open (dawn to dusk, free) | RAMSAR site; wetlands, forest, riparian, marked trails; OSU = public state university; TIER AMBIGUITY — not ODNR (Tier 2) and not private (Tier 8); flagged for Resolution |

### Null Results — Tier 8 (documented with evidence)

| Organization / Lead | Result | Evidence |
|---|---|---|
| Simon Kenton Council BSA | NULL — no Franklin County camp | Camp Oyo in Scioto County; SKC offices at 1901 E Dublin Granville Rd are admin, not a camp |
| Big Brothers Big Sisters Central Ohio | NULL — no Franklin County camp | Camp Oty'Okwa is in Hocking County (South Bloomingville, OH) |
| Waterman Agricultural & NRL (OSU, 261 ac) | NULL — no public access | waterman.osu.edu/visit-us: "not currently offering tours for the general public or school groups" |
| Chadwick Arboretum & Learning Gardens (OSU) | EXCLUDED — cultivated botanical collection | Prior session excluded (correct); confirmed: cultivated horticultural collection, not natural area; open dawn to dusk but not in project scope |
| ODNR licensed hunting preserves | NULL | No licensed hunting preserves identified in Franklin County; county is predominantly urban/suburban |
| Capital University | NULL | No confirmed natural area preserves with public access in Franklin County |
| Otterbein University | NULL | No confirmed natural area preserves with public access in Franklin County; uses Sharon Woods (Metro Parks) for outdoor recreation |
| Camp Oty'Okwa (BBBS) | NULL (wrong county) | Hocking County, not Franklin |
| Cross Oak / Camp Asbury / church camps | NULL | Not in Franklin County |
| ZipZone Outdoor Adventures | NOT STAGED as separate entity | Commercial operator within Camp Mary Orton; documented within T8-001 Camp Mary Orton entity |
| Pontifical College Josephinum | NULL | Private Catholic seminary campus; no public natural area access confirmed |

### YAML Documents Appended (4)

1. **Camp Ken-Jockety & The Elam Environmental Center** — `entity_type: Site`, `discovery_tier: 8`; 220 ac; Girl Scouts of Ohio's Heartland
2. **Ginny and John Elam Environmental Center** — `entity_type: Site` (child), `discovery_tier: 8`; within Camp Ken-Jockety
3. **Wilma H. Schiermeier Olentangy River Wetland Research Park** — `entity_type: Site`, `discovery_tier: 8` (TIER AMBIGUITY FLAG); OSU; 52 ac; open public access
4. **Tier 8 Session 10 Supplemental DiscoveryNote** — summary of session findings; all null results documented with evidence

**Staging YAML:** 27,753 → **27,858 lines** (+105 lines, 4 documents)

### Assessment

Franklin County Tier 8 is **COMPLETE**. The sparse result is expected: Franklin County is highly urbanized (Columbus metro), and its major natural corridors (Big Darby, Olentangy, Alum Creek) are predominantly managed by Metro Parks (Tier 3) and Columbus Recreation & Parks (Tier 6). Private natural area landholding is minimal; the county has very few nonprofit camps or private preserves relative to its size.

**TIER 8 COMPLETE.**

---

## Session 11 — 2026-03-16

### Pipeline Session — Resolution, Normalization, TSV Output, Integrity Check, Upsert

**Session type:** Post-discovery pipeline (no new entity discovery)
**Script:** `franklin_oh_pipeline.py`
**Pipeline version:** v5.2 (6 iterative runs to reach final state)

---

### Phase 1 — YAML Parse

**Input:** Franklin County staging YAML (27,858 lines)
**Method:** Multi-document YAML split on `\n---\n`; pre-processor handles known parse error patterns
**Result:** 1,255 YAML blocks parsed successfully
- Pre-processor interventions: unquoted colons in governance_raw fields (~102 occurrences auto-quoted); list-format entities missing `---` separator in Block 128 (23 entities recovered)
- 0 fatal parse errors

---

### Phase 2 — Field Unification

**Result:** 1,255 raw documents unified into canonical field schema
- Entity type detection from `entity_type` field across all 6 types
- `name_raw` resolved from `entity_name_raw`, `name`, `trail_name_raw`, `network_name_raw`, `segment_name_raw`, `access_point_name_raw` fallbacks
- Category field normalized: `site_category_raw` → `category_raw` → `park_type_raw` → `site_type_raw` → name inference

---

### Phase 3 — Resolution Pass 1

**Method:** Fuzzy deduplication using `difflib.SequenceMatcher` token-set ratio; grouping by (entity_type × county_primary); connected-component clustering; field-level merge with tier priority (1 > 2 > ... > 8 > 0)
**Thresholds:** MERGE ≥ 90, REVIEW 70–89

**Resolution results:**
| Entity Type | Pre-Resolution | Post-Resolution | Merged | Review Queue |
|---|---|---|---|---|
| Site | ~1,400+ | 1,025 | ~375 | 430 pairs |
| Trail | ~250+ | 115 | ~135 | 70 pairs |
| Trail Segment | 3 | 1 | 2 | — |
| Trail Network | 3 | 2 | 1 | — |
| Site Network | 1 | 1 | 0 | — |
| Access Point | 0 | 0 | 0 | — |

**Review queue stored in DB:** 500 total pairs (430 site + 70 trail) — require human judgment
**Notable review pairs:** "Veteran's Park ↔ Veterans Park" (apostrophe variant, likely same entity); "Alum Creek Parkland ↔ Alum Creek/Koch Parkland"

---

### Phase 4 — Normalization

**Method:** Field-by-field normalization against v5.x vocabulary maps; GPS acquisition skipped (outbound HTTP proxy blocked — geocoding not possible in current environment)

**Fixes applied this session (6 pipeline iterations):**

1. **Trail use_type/surface_type extraction** — `accessibility_raw` field parsing added; helper functions `_parse_use_type_from_accessibility()` and `_parse_surface_type_from_accessibility()` created. Trail type warnings reduced from 218 → 27.
2. **Trail vocabulary corrections** — TRAIL_USE_TYPE_MAP: "Equestrian" → "Bridle" (per vocabulary spec); Mountain Bike, Water multi-use variants added. TRAIL_ORIGIN_MAP: "Canal Trail" → "Canal Towpath"; invalid non-vocabulary values removed.
3. **Merge fallback fields extended** — `phase4_merge_fields()` now preserves trail-specific fields (`use_type_raw`, `surface_type_raw`, `origin_type_raw`, `length_raw`, `difficulty_raw`, etc.) from non-canonical records when canonical record lacks them.
4. **`norm_vocab` specificity ordering** — Keys now sorted by length descending before partial matching; prevents "park" matching before "state nature preserve". Fixes incorrect categorization of Gahanna Woods State Nature Preserve and similar entities.
5. **Site category inference from name** — `_infer_category_from_name()` added; applied to all baseline Tier 2/3 seeds and other records lacking explicit `category_raw`. Blank site categories reduced from 561 → 5.
6. **SITE_CATEGORY_MAP expanded** — Added Water Site entries for scenic river variants; GIS compound categories (e.g., "passive park / natural area" → "Natural Area"); Curated Biological Site; multi-word compound park types.
7. **Water trail surface_type auto-set** — Trails with `use_type = "Water"` and blank surface automatically assigned `surface_type = "Water"`.

**Normalization summary:**
- Sites: 1,020 / 1,025 categorized (99.5%); 5 remaining blanks (Upper Albany School Site, West Bank Walkway, Woods of Indian Run, Wallace Property, Jeffrey Mansion) — need manual review
- Trails: 97 / 115 use_type populated; 102 / 115 surface_type populated; remaining blanks are legitimately undocumented
- GPS / Plus Code / Township / Municipality: all blank — geocoding blocked (see pending tasks)

**Site category distribution:**
| Category | Count |
|---|---|
| Park | 701 |
| Open Space | 131 |
| Recreation Facility | 61 |
| Nature Preserve | 53 |
| Natural Area | 31 |
| Conservation Area | 18 |
| Memorial | 10 |
| Water Site | 8 |
| Community Garden | 4 |
| Campground | 2 |
| Hunting Area | 1 |
| **Blank** | **5** |
| **Total** | **1,025** |

---

### Phase 5 — TSV Output

**Specification versions applied:** Sites v5.1, Trails v5.1, Trail Segments v5.1, Trail Networks v5.1, Site Networks v5.1, Access Points v5.1

| Entity Type | Rows (incl. header) | File | Size |
|---|---|---|---|
| Sites | 1,026 | franklin_oh_sites.tsv | 345,003 bytes |
| Trails | 116 | franklin_oh_trails.tsv | 58,055 bytes |
| Trail Segments | 2 | franklin_oh_trail_segments.tsv | — |
| Trail Networks | 3 | franklin_oh_trail_networks.tsv | — |
| Site Networks | 2 | franklin_oh_site_networks.tsv | — |
| Access Points | 1 (header only) | franklin_oh_access_points.tsv | — |

---

### Phase 6 — Integrity Check

**Result:** 0 bad-tab rows across all 6 output files
**Delimiter validation:** All rows confirmed at correct tab count per entity spec
**Final pipeline state:** 0 errors, 27 warnings (all legitimate blanks — undocumented trail types and 5 manually-required site categories)

---

### Phase 7 — SQLite Upsert

**Database:** `natural_areas_v5.db`
**Method:** Upsert on entity ID; all 6 entity tables populated; review_queue table populated with 500 pairs

**Final DB entity counts:**
| Table | Rows |
|---|---|
| sites | 1,025 |
| trails | 115 |
| trail_segments | 1 |
| trail_networks | 2 |
| site_networks | 1 |
| access_points | 0 |
| review_queue | 500 |

---

### Improvement Tracker Updates (IMP-021 through IMP-026)

Six new items added to `na_improvement_tracker.md`:

| ID | Summary | Status |
|---|---|---|
| IMP-021 | Trail discovery missing explicit use/surface type fields | Open — protocol amendment needed |
| IMP-022 | Category field naming inconsistent across sessions | Open — protocol amendment needed |
| IMP-023 | Baseline ID collision B067 (Blacklick vs. Blendon Woods) | Open — needs investigation |
| IMP-024 | YAML staging: unquoted colons in governance_raw values | Open — protocol amendment needed |
| IMP-025 | YAML staging: list-format entities cause block-end parse errors | Open — protocol amendment needed |
| IMP-026 | Pipeline vocab partial matching specificity ordering | Fixed in pipeline; spec update pending |

---

### Pending Tasks (Carry Forward — after Session 11)

1. **GPS Acquisition** — All 1,025 sites and access points have blank GPS coordinates, Plus Code, Township, and Municipality fields. Geocoding blocked by outbound HTTP proxy in current environment. Requires a session with geocoding access or manual GPS entry.
2. **Manual review queue** — 430 site pairs and 70 trail pairs await human judgment. Priority pairs: apostrophe/punctuation variants (e.g., Veteran's Park ↔ Veterans Park), partial name matches (Alum Creek Parkland ↔ Alum Creek/Koch Parkland).
3. **IMP-023 investigation** — Baseline ID B067 appears assigned to both Blacklick Woods Metro Park and Blendon Woods Metro Park. One assignment is incorrect; fix and update staging record.
4. **5 remaining blank site categories** — Upper Albany School Site, West Bank Walkway, Woods of Indian Run, Wallace Property, Jeffrey Mansion — require manual category determination.
5. **Parent/child site relationship resolution** — Sites with `parent_site_raw` need parent IDs resolved and `parent_site_id` field populated.
6. **Trail segment parent trail ID resolution** — 1 trail segment's `parent_trail_raw` needs to be linked to the correct trail ID.
7. **Gahanna pocket parks / open spaces / reserves** — ~28 entities PENDING (CivicPlus page blank during discovery; browser retry needed).
8. **MORPC map verification pass** — Consolidated cross-municipality map verification pass deferred from Tier 6; still outstanding.

---

## Session 12 — 2026-03-16

### GPS Acquisition via MORPC ArcGIS Feature Layer

**Session type:** GPS enrichment (no new entity discovery)
**Source:** MORPC Parks and Open Space — Mid-Ohio Open Data (MOOD)
**URL:** https://public-morpc.hub.arcgis.com/datasets/d898fa77e91d414f8f296b0511f14fbf_11/
**Feature Service:** `https://services1.arcgis.com/EjjnBtwS9ivTGI8x/arcgis/rest/services/Parks_and_Open_Space/FeatureServer/11`
**Script:** `gps_match.py`

#### Data Acquisition

MORPC's Parks and Open Space feature layer was queried via ArcGIS REST API (`returnCentroid=true&outSR=4326`) using browser automation (VM outbound proxy blocks direct API access). All 1,894 Franklin County records (County='FRA') retrieved in one call with WGS84 centroids. CSV saved to workspace as `morpc_parks_franklin_centroids.csv`.

#### Matching Strategy

Three-pass iterative matching with progressive refinements:

1. **Pass 1** — Token-set ratio, threshold ≥90. 934 new GPS records.
2. **Pass 2** — Added name normalizations ("Parkland"→"Park", "Nature Reserve"→"Nature Preserve", "Metro Gardens"→"Metro Park"). 33 additional matches.
3. **Pass 3** — Combined score (55% token-set + 45% distinctive-word ratio) to suppress generic-suffix false matches (e.g., "Hoover NP" ≠ "Boyer NP"). 9 fuzzy-auto + 10 manual accepts.

**Manual accepts (10 confirmed same-entity pairs with name variants):**
Woodstream NP/Woodstream Parkland · Case Road CG/Case Road Parkland · Rush Run NP/Rush Run Park · Woodward NP/Woodward Park · Webster NP/Webster Park · Kenney NP/Kenney Park · Emerald Pkwy Bridge River Access/Emerald Pkwy Bridge Open Space · Worthington Village Green/Village Green Park · Alice Smith NP/Smith Nature Park · Gardens at Gantz/Gantz Park

#### Final Results

| Metric | Value |
|---|---|
| Sites with GPS | 988 / 1,025 (96.4%) |
| Municipality populated | 985 / 1,025 |
| Acres populated | 981 / 1,025 |
| DB synced | ✓ natural_areas_v5.db sites table updated |
| TSV updated | ✓ franklin_oh_sites.tsv |

**37 no-match sites (expected):** State scenic rivers (no centroid appropriate), private camps (Tier 8), small township playgrounds below MORPC threshold, pools/aquatic facilities, Columbus nature preserves absent from MORPC layer, miscellaneous small sites.

#### Carry-Forward Tasks (after Session 12)

1. **Manual review queue** — 500 pairs (430 site + 70 trail) still pending human judgment
2. **37 GPS-blank sites** — Mostly legitimate gaps; scenic rivers need route midpoint (future work)
3. **Plus Code / Township fields** — Still blank; requires geocoding or manual entry
4. **IMP-023** — B067 collision still outstanding
5. **5 blank site categories** — Still outstanding
6. **Gahanna pocket parks** — ~28 entities still PENDING

---

## Session 14 — 2026-03-18

### GPS Artifact Correction — 4 Columbus Nature Preserves

**Session type:** GPS correction (no new discovery)
**Trigger:** Manual review (Session 13) identified 4 sites with incorrect GPS/municipality from MORPC centroid collision during Session 12 GPS acquisition.

**Problem:** All 4 preserves received the same wrong MORPC centroid (pointing to New Albany area) because MORPC assigned identical polygon centroids to adjacent/nearby preserves. Municipality was also incorrectly set to "New Albany" for all four.

**Method:**
- Beechwold NP & Kenney NP: Columbus city GIS layer (maps2.columbus.gov/arcgis/rest/services/Schemas/RecreationParks/MapServer/7) — polygon centroids, authoritative
- Coronet Woods NP: columbusrecparks.com official page (address confirmed 1790 Coronet Dr, Columbus OH 43224) + Google Maps geocode
- Hickory Woods NP: columbusrecparks.com official page (address confirmed 2485 Willis Rd, Dublin OH 43016) + Google Maps geocode; located in Dublin, not Columbus

**Corrections applied:**

| Site ID | Name | Old GPS (wrong) | New GPS (correct) | Old Muni | New Muni | Plus Code |
|---|---|---|---|---|---|---|
| FR-S-0080 | Beechwold Nature Preserve | (40.0864502, -82.8210418) | (40.060335, -83.024534) | New Albany | Columbus | 86GR3X6G+45 |
| FR-S-0239 | Kenney Nature Preserve | (40.0864502, -82.8210418) | (40.065788, -83.030547) | New Albany | Columbus | 86GR3X89+8Q |
| FR-S-0129 | Coronet Woods Nature Preserve | (40.0809109, -82.8246212) | (40.0430558, -82.9673164) | New Albany | Columbus | 86GV22VM+63 |
| FR-S-0216 | Hickory Woods Nature Preserve | (40.0809109, -82.8246212) | (40.1308576, -83.0827762) | New Albany | Dublin | 86GR4WJ8+8V |

- Coronet Woods Plus Code `86GV22VM+63` verified against Google Maps (local code: 22VM+63 ✓)
- Hickory Woods is in Dublin, OH — managed by Columbus Rec & Parks but physically located in Dublin

**Files updated:** `natural_areas_v5.db` (sites table), `franklin_oh_sites.tsv` — GPS Lat, GPS Lon, Plus Code, Municipality, Location fields corrected for all 4 rows.

### Pending Tasks (Carry Forward — after Session 14)

1. **IMP-023** — B067 collision (Blacklick Woods vs Blendon Woods baseline ID) — still outstanding
2. **5 blank site categories** — Upper Albany School Site, West Bank Walkway, Woods of Indian Run, Wallace Property, Jeffrey Mansion
3. **Parent/child site ID resolution** — sites with `parent_site_raw` need parent IDs resolved
4. **Trail segment parent trail ID** — 1 trail segment's parent trail link needs resolution
5. **Gahanna pocket parks** — ~28 entities PENDING (browser retry needed)
6. **Plus Code / Township fields** — remaining ~1,000 sites still have blank Plus Code and Township; requires batch geocoding
7. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding

---

## Session 13 — 2026-03-18

### Manual Review Queue — Resolution Complete

**Session type:** Manual review queue resolution (no new discovery)
**Power failure note:** Power failure occurred after Session 12 completed. Post-failure integrity check confirmed no data loss — DB, TSV files, YAML, session log, and handoff all intact.

---

### Review Queue Analysis

**Total pairs in queue:** 500 (all Site type; Trail pairs were 0 in DB — not staged)

**Method:** Automated GPS-distance analysis on all 500 pairs. Both entities looked up in sites table; haversine distance computed from GPS coordinates. Pairs with dist > 0.5km classified auto-split; pairs with dist ≤ 0.5km or no GPS match flagged for human review.

| Category | Count |
|---|---|
| Auto-split (GPS distance > 0.5km, physically distinct) | 496 |
| Human review — same/close GPS location | 4 |
| **Total** | **500** |

**Notable auto-split patterns confirmed:**
- Multiple municipalities each have a "Veterans Park" / "Veteran's Park" — all correctly split (distinct parks in Groveport, Groveport again, Bexley, Clinton Township, etc.)
- "Cranston Park ↔ Crafton Park" (Columbus vs Upper Arlington, ~8km apart) — split
- All 498 nature preserve / parkland / open space cross-name pairs — distinct GPS locations, split

---

### Human Review — 4 Pairs

| review_id | Pair | GPS dist | Decision | Notes |
|---|---|---|---|---|
| 3089 | Alexander Park ↔ Alexander/AEP Park | 0.05km | **split** | Adjacent parcels separately tracked by managing entity; AEP parcel (0.665 ac) is distinct from Alexander Park (2.779 ac) |
| 3148 | Alum Creek Parkland ↔ Alum Creek/Cooper Rd Parkland Coh | 0.00km | **merged** | Same parkland — MORPC sub-parcel record (FR-S-0667, 9.34 ac, MORPC-only URL) merged into canonical FR-S-0062 (18.036 ac, official Columbus Rec Parks URL); FR-S-0667 removed from DB and TSV |
| 3250 | Beechwold Nature Preserve ↔ Kenney Nature Preserve | 0.00km | **split** | Distinct named preserves (Columbus 25 NPs list); shared GPS is MORPC centroid artifact; GPS quality flag set |
| 3457 | Coronet Woods Nature Preserve ↔ Hickory Woods Nature Preserve | 0.00km | **split** | Distinct named preserves (Columbus 25 NPs list); shared GPS is MORPC centroid artifact; GPS quality flag set |

---

### Actions Applied

1. **`manual_review_queue` table updated** — `decision`, `decided_at`, `decision_notes` columns added; all 500 rows set
2. **FR-S-0667 removed** from `sites` table (merged into FR-S-0062)
3. **`franklin_oh_sites.tsv` updated** — FR-S-0667 row removed; 1,026 → 1,025 rows (incl. header)
4. **GPS artifact flag** — 4 Columbus nature preserves have suspect GPS/municipality data from MORPC centroid collision:
   - FR-S-0080 Beechwold Nature Preserve — GPS/muni shows New Albany (likely wrong)
   - FR-S-0239 Kenney Nature Preserve — GPS/muni shows New Albany (likely wrong)
   - FR-S-0129 Coronet Woods Nature Preserve — GPS/muni shows New Albany (likely wrong)
   - FR-S-0216 Hickory Woods Nature Preserve — GPS/muni shows New Albany (likely wrong)
   All four need fresh geocoding from columbusrecparks.com address data.

---

### Post-Review Entity Counts

| Table | Franklin Rows |
|---|---|
| sites | 1,024 |
| trails | 115 |
| trail_segments | 1 |
| trail_networks | 2 |
| site_networks | 1 |
| access_points | 0 |
| manual_review_queue | 500 (all decided) |

**GPS coverage:** 987 / 1,024 (96.4%)

---

### Pending Tasks (Carry Forward — after Session 13)

1. **IMP-023** — B067 collision (Blacklick Woods vs Blendon Woods baseline ID) — still outstanding
2. **5 blank site categories** — Upper Albany School Site, West Bank Walkway, Woods of Indian Run, Wallace Property, Jeffrey Mansion
3. **GPS artifact correction** — 4 Columbus nature preserves (FR-S-0080, FR-S-0239, FR-S-0129, FR-S-0216) need correct GPS from columbusrecparks.com
4. **Parent/child site ID resolution** — sites with `parent_site_raw` need parent IDs resolved
5. **Trail segment parent trail ID** — 1 trail segment's parent trail link needs resolution
6. **Gahanna pocket parks** — ~28 entities PENDING (browser retry needed)
7. **Plus Code / Township fields** — still blank; requires geocoding access
8. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding

---

## Session 15 — IMP-023 Baseline ID Collision Resolution
**Date:** 2026-03-18
**Operator:** Claude (resumed after context compaction)
**Status:** COMPLETE

### Problem: IMP-023 — B067 Collision

Both FR-S-0009 (Blacklick Woods Metro Park) and FR-S-0010 (Blendon Woods Metro Park) were
erroneously assigned `baseline_id: B067` in the YAML and `discovery_provenance` table.

The YAML contained a self-diagnosis note (Tier 3 DiscoveryNote) that partially diagnosed the
collision but had the wrong conclusion: it asserted "Blacklick Woods Metro Park is B067" and
"Blendon Woods seeded_from_baseline should be FALSE, baseline_id blank."

### Baseline Audit

Queried `Franklin baseline.xlsx` (690 data rows, B001–B690, alphabetical by name):

| B-ID | Name | Governance | Acres | Notes |
|------|------|-----------|-------|-------|
| B064 | Blacklick Park | City Park (Groveport) | — | Different entity entirely |
| B065 | Blacklick Woods | National Natural Landmark | 63 | NNL sub-entity inside metro park |
| B066 | Blendon Woods Metro Park | Metro Parks | 653 | Direct match for FR-S-0010 |
| B067 | Blodwen Park | City Park (Grove City) | 0.5 | Unrelated; was wrongly assigned |

**Conclusion:**
- Blacklick Woods Metro Park (FR-S-0009): No dedicated metro park baseline entry exists.
  B065 is the NNL sub-designation entity within the park. Use B065 as closest seed.
- Blendon Woods Metro Park (FR-S-0010): B066 is a direct 1:1 match. Use B066.
- B067 (Blodwen Park, Grove City) had no connection to either metro park.

### Fix Applied

**Database — `discovery_provenance` table:**

| Site ID | Name | Old baseline_id | New baseline_id |
|---------|------|----------------|----------------|
| FR-S-0009 | Blacklick Woods Metro Park | B067 | B065 |
| FR-S-0010 | Blendon Woods Metro Park | B067 | B066 |

Full provenance `source_notes` updated with IMP-023 correction timestamps.

**Database — `sites` table:**  
`notes` field updated on both sites documenting the correction and former wrong assignment.

**YAML — `franklin_oh_raw_discovery.yaml`:**
- Blacklick Woods entry (Tier 3, Site 2): `baseline_id` corrected B067→B065; `identity_notes_raw` rewritten to accurately reference B065 as the NNL sub-entity seed
- Blendon Woods entry (Tier 3, Site 3): `baseline_id` corrected B067→B066; `identity_notes_raw` updated to note direct B066 match
- Self-diagnosis DiscoveryNote (IMP-023): Replaced erroneous conclusion text with full corrected analysis showing actual B065/B066/B067 assignments

### Entity Counts (Unchanged)

| Table | Franklin Rows |
|---|---|
| sites | 1,024 |
| trails | 115 |
| trail_segments | 1 |
| trail_networks | 2 |
| site_networks | 1 |
| access_points | 0 |
| manual_review_queue | 500 (all decided) |

---

### Pending Tasks (Carry Forward — after Session 15)

1. **5 blank site categories** — Upper Albany School Site, West Bank Walkway, Woods of Indian Run, Wallace Property, Jeffrey Mansion
2. **Parent/child site ID resolution** — sites with `parent_site_raw` need parent IDs resolved
3. **Trail segment parent trail ID** — 1 trail segment's parent trail link needs resolution
4. **Gahanna pocket parks** — ~28 entities PENDING (browser retry needed)
5. **Plus Code / Township fields** — still blank; requires geocoding access
6. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
7. **GPS — remaining 37 sites** — scenic rivers, private camps, small playgrounds

---


## Session 16 — Blank Site Category Resolution
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE

### Problem: 5 Sites with Blank Category

Post-pipeline normalization left 5 Franklin County sites with no category assigned. The `_infer_category_from_name()` function reduced blanks from 561 to 5, but these 5 names did not contain category-inferrable keywords.

### Assignments

| Site ID | Name | Category Assigned | Signal / Rationale |
|---------|------|------------------|--------------------|
| FR-S-0395 | Upper Albany School Site | **Park** | Analogous to FR-S-0139 Deaf School Park (same governance, same Columbus Rec & Parks school-site pattern) |
| FR-S-0416 | West Bank Walkway | **Park** | Analogous to FR-S-0704 Westbank Walkway (Park); linear park corridor, Columbus Rec & Parks |
| FR-S-0525 | Woods of Indian Run | **Park** | Dublin GIS layer `park_type = Neighborhood Park` |
| FR-S-0555 | Wallace Property | **Open Space** | Dublin GIS layer `park_type = Open Space` |
| FR-S-0926 | Jeffrey Mansion | **Recreation Facility** | Historic event/community venue managed by City of Bexley Recreation and Parks; not a natural area or park space |

### Bonus Fix: Wallace Property Municipality
FR-S-0555 (Wallace Property) had `municipality = "Township"` — a data ingestion artifact. Address is 5200 Brand Rd, Dublin, OH. Corrected to `Dublin` in both DB and TSV.

### Files Updated

- **`NASqlite/natural_areas_v5.db`** — `sites` table: `category` set on all 5 sites; `municipality` corrected for FR-S-0555; `notes` and `updated_at` set on all 5
- **`County_Spreadsheets/Franklin/franklin_oh_sites.tsv`** — col[2] (Category) updated for all 5; col[14] (Municipality) corrected for FR-S-0555

### Post-Fix Coverage

- **Site categories:** 1,024 / 1,024 (100%) ✓
- **Category distribution:** Park 704 · Open Space 131 · Recreation Facility 62 · Nature Preserve 53 · Natural Area 31 · Conservation Area 17 · Memorial 10 · Water Site 8 · Community Garden 4 · Campground 2 · Hunting Area 1

---

### Pending Tasks (Carry Forward — after Session 16)

1. **Parent/child site ID resolution** — sites with `parent_site_raw` need `parent_site_id` populated
2. **Trail segment parent trail ID** — 1 trail segment's parent trail link needs resolution
3. **Gahanna pocket parks** — ~28 entities PENDING (browser retry needed)
4. **Plus Code / Township fields** — still blank; requires geocoding access
5. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
6. **GPS — remaining 37 sites** — scenic rivers, private camps, small playgrounds

---


## Session 17 — Parent/Child ID Resolution + Trail Segment Link
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE (13 site parent IDs resolved; 4 deferred; trail segment linked)

---

### Site Parent/Child Resolution

Queried `sites.notes` for all Franklin sites containing parent/child language. Found 22 candidates; assessed each for definiteness of parent relationship.

#### Resolved (13 sites)

| Child Site | Child ID | Parent Site | Parent ID | Evidence |
|-----------|---------|------------|---------|---------|
| Creekside Plaza | FR-S-0606 | Creekside Park & Arboretum | FR-S-0590 | Explicit: "Child site of: Creekside Park & Arboretum" |
| Creekside Rotary Stage | FR-S-0607 | Creekside Park & Arboretum | FR-S-0590 | Explicit: "Child site of: Creekside Park & Arboretum" |
| Hannah Park Community Garden | FR-S-0609 | Hannah Park | FR-S-0592 | Explicit: "Child site of: Hannah Park" |
| Westerville Veterans Memorial | FR-S-0784 | Westerville Sports Complex | FR-S-0783 | Notes: "situated within the Westerville Sports Complex" |
| Reed Road Water Park | FR-S-0817 | Reed Road Park | FR-S-0803 | Notes: "Outdoor water park within Reed Road Park" |
| Hilliard Family Aquatic Center | FR-S-0844 | Roger A. Reynolds Municipal Park | FR-S-0839 | Notes: "Outdoor aquatic facility within Roger A. Reynolds Municipal Park" |
| Eagle Pavilion | FR-S-0862 | Fryer Park | FR-S-0849 | Notes: "Located within Fryer Park" |
| Beulah Pavilion | FR-S-0863 | Park at Beulah | FR-S-0855 | Notes: "Located within Park at Beulah" |
| Moses Wright Nature Area | FR-S-0910 | East Granville Road Park | FR-S-0909 | Notes: "Named natural area within East Granville Road Park" |
| David H. Madison Community Pool | FR-S-0925 | Jeffrey Park | FR-S-0920 | Notes: "Community pool within Jeffrey Park" |
| Jeffrey Mansion | FR-S-0926 | Jeffrey Park | FR-S-0920 | Parent notes: "Contains … Jeffrey Mansion (recorded as child sites)" |
| Bexley Natural Dog Park | FR-S-0927 | Schneider Park | FR-S-0922 | Notes: "off-leash natural dog park within Schneider Park" |
| Fortress Obetz | FR-S-0997 | Memorial Park | FR-S-0991 | Notes: "Recorded as child site of Memorial Park" |

**Changes applied:**
- `sites.parent_site_id` set for all 13 child sites
- `site_parent` table: 13 rows inserted
- `franklin_oh_sites.tsv`: new col 26 "Parent Site ID" added; populated for all 13 sites

#### Deferred (4 sites — parent unresolvable)

| Child Site | Child ID | Reason |
|-----------|---------|--------|
| Friendship Park Community Garden | FR-S-0608 | Parent "Friendship Park" (Gahanna) not in DB — pending Gahanna retry session |
| Whitney Playground | FR-S-0908 | Loose corridor association (Olentangy River Parklands); no definite single parent site |
| Memorial Plaza | FR-S-0955 | Parent park not confirmed in notes — needs browser verification |
| Grandview Heights Skate Park | FR-S-0974 | Parent (Municipal Pool) not in DB; address-linked but pool is separate asset |

---

### Trail Segment Parent Link

**Segment:** FR-TS-0001 "Olentangy River Water Trail — Section A"  
**Identity notes** stated: "Parent trail: Olentangy River Water Trail"  
**Found:** FR-T-0001 "Olentangy River Water Trail" (Water trail, ODNR designation)  
**Fix applied:** `trail_segments.parent_trail_id` → FR-T-0001; `trail_to_segment` row inserted (FR-T-0001, FR-TS-0001)  
**TSV:** Already had correct trail name in "Parent Trail" column — no TSV change needed

---

### Pending Tasks (Carry Forward — after Session 17)

1. **Gahanna pocket parks** — ~28 entities PENDING (browser retry needed); also unblocks FR-S-0608 parent resolution
2. **Plus Code / Township fields** — still blank; requires geocoding access
3. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
4. **GPS — remaining 37 sites** — scenic rivers, private camps, small playgrounds
5. **4 deferred parent IDs** — FR-S-0608, FR-S-0908, FR-S-0955, FR-S-0974

---


## Session 18 — Gahanna Retry (gahanna.gov/474 Browser Fetch)
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE

### Objective

Retry the CivicPlus page gahanna.gov/474 (Pocket Parks, Open Spaces & Reserves) which had loaded blank on two prior attempts due to JavaScript rendering failure. Compare full gahanna.gov facility list against DB; identify and stage any missing entities.

### Method

Used Chrome browser automation to load the full Facilities page (`gahanna.gov/Facilities`). Intercepted the `POST /Facilities/Facility/Search` API response via `get_page_text` after page load, retrieving all 40 facilities. Compared against the 60 Gahanna sites already in DB.

**Note:** gahanna.gov/474 still renders blank (heading only; no body content). The complete entity list was retrieved via the main Facilities page instead.

### Comparison Results

- **40 facilities** on gahanna.gov (parks & recreation only; 5 government buildings excluded)
- **34 already in DB** — either from original discovery or MORPC cross-check
- **2 in YAML but not pipelined** — Friendship Park and Woodside Green Park were staged in Session 3 YAML as RAW status but never inserted into the DB during pipeline runs
- **4 genuinely new sub-facilities** — not in YAML, not in DB

### Net-New Entities Added (6 total)

| Site ID | Name | Category | Parent | Source |
|---------|------|----------|--------|--------|
| FR-S-1026 | Friendship Park | Park | — | gahanna.gov Facilities + Session 3 YAML (was staged, not pipelined) |
| FR-S-1027 | Woodside Green Park | Park | — | gahanna.gov Facilities + Session 3 YAML (was staged, not pipelined); MORPC: 32.847 ac, Sub_Type Regional Park (classification conflict with gahanna.gov Community Park) |
| FR-S-1028 | Friendship Park Gazebo | Recreation Facility | FR-S-1026 | gahanna.gov Facilities — new |
| FR-S-1029 | Friendship Park Shelter | Recreation Facility | FR-S-1026 | gahanna.gov Facilities — new |
| FR-S-1030 | Woodside Green Park Shelter | Recreation Facility | FR-S-1027 | gahanna.gov Facilities — new |
| FR-S-1031 | Splash Pad | Recreation Facility | FR-S-0604 | gahanna.gov Facilities — new (at Gahanna Swimming Pool, 148 Parkland Ave) |

### Parent Resolution — FR-S-0608

FR-S-0608 (Friendship Park Community Garden) had been deferred from Session 17 as parent "Friendship Park" was not in the DB. Now resolved: parent = FR-S-1026.

### Files Updated

- **DB `sites` table**: 6 rows inserted; `discovery_provenance` 6 rows; `site_parent` 7 rows (6 new + FR-S-0608)
- **`franklin_oh_sites.tsv`**: 6 rows appended; FR-S-0608 Parent Site ID updated to FR-S-1026
- **`franklin_oh_raw_discovery.yaml`**: Session 18 header + 4 new YAML documents appended (Friendship Park and Woodside Green Park were already in YAML from Session 3)

### Post-Session Entity Counts

| Table | Franklin Rows |
|---|---|
| sites | **1,030** (+6) |
| trails | 115 |
| trail_segments | 1 |
| trail_networks | 2 |
| site_networks | 1 |
| access_points | 0 |
| site_parent | 20 (Franklin) |

### Gahanna Tier 6 — Final Status

**COMPLETE.** All gahanna.gov Facilities entries accounted for. MORPC cross-check entities already in DB from Session 7. Pending items resolved:
- ~~Pocket Parks / Open Spaces / Reserves (gahanna.gov/474)~~ — confirmed blank page; full entity set recovered via main Facilities page
- ~~FR-S-0608 parent~~ — resolved to FR-S-1026

---

### Pending Tasks (Carry Forward — after Session 18)

1. **Plus Code / Township fields** — ~1,000 sites blank; requires geocoding pass
2. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
3. **GPS — remaining 37 sites** — scenic rivers, private camps, small playgrounds
4. **3 deferred parent IDs** — FR-S-0908 (loose corridor), FR-S-0955 (browser verify), FR-S-0974 (parent not in DB)
5. **Woodside Green Park classification flag** — gahanna.gov Community Park vs MORPC Regional Park; needs resolution decision

---


## Session 19 — Deferred Parent ID Resolution + FR-S-0955 Deletion Flag
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE

### Objective

Resolve the 3 deferred parent IDs from Session 17/18: FR-S-0955 Memorial Plaza (Reynoldsburg), FR-S-0974 Grandview Heights Skate Park, FR-S-0908 Whitney Playground (Worthington).

### Resolution Summary

| Site | Action | Outcome |
|------|--------|---------|
| FR-S-0955 Memorial Plaza | Browser searched reynoldsburg.gov/Facilities and reynoldsburgoh.myrec.com — **not found in any park system**. MapQuest confirms address (7312 E Main St) is a parking lot, not a natural area. Municipality field wrong (shows Grandview Heights; actual location is Reynoldsburg). | **Flagged for deletion.** Staged in error. |
| FR-S-0974 Grandview Heights Skate Park | Skate park is in the Municipal Pool parking lot at 1350 Goodale Blvd. No Grandview Heights Municipal Pool record in DB (pool staging would be a new discovery action). Municipality field was wrong (Grove City). | **Parent stays NULL.** Municipality corrected: Grove City → Grandview Heights. |
| FR-S-0908 Whitney Playground | Notes explicitly state "within Olentangy River Parklands corridor / Part of Olentangy River riparian corridor." FR-S-0678 (Olentangy River Parklands) is in DB as a Worthington Conservation Area. Municipality field was blank. | **Parent = FR-S-0678.** Municipality set to Worthington. |

### DB Changes

```
UPDATE sites SET parent_site_id='FR-S-0678', municipality='Worthington' WHERE site_id='FR-S-0908'
INSERT site_parent: (FR-S-0908, FR-S-0678)
UPDATE sites SET municipality='Grandview Heights' WHERE site_id='FR-S-0974'
UPDATE sites SET notes = notes || '; FLAGGED FOR DELETION 2026-03-18: ...' WHERE site_id='FR-S-0955'
```

### TSV Changes

- FR-S-0908: Municipality ← Worthington; Parent Site ID ← FR-S-0678
- FR-S-0974: Municipality ← Grandview Heights (was Grove City)
- FR-S-0955: Notes field: deletion flag appended

### Post-Session Entity Counts

| Table | Franklin Rows |
|---|---|
| sites | **1,030** (unchanged; FR-S-0955 flagged, not deleted) |
| site_parent | **21** (Franklin) (+1 for FR-S-0908) |

### Pending Tasks (Carry Forward — after Session 19)

1. **FR-S-0955 Memorial Plaza** — confirm deletion and remove from DB/TSV (needs deliberate action)
2. **Plus Code / Township fields** — ~1,000 sites blank; requires geocoding pass
3. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
4. **GPS — remaining 37 sites** — scenic rivers, private camps, small playgrounds
5. **Woodside Green Park classification flag** — gahanna.gov Community Park vs MORPC Regional Park

---

## Session 20 — GPS Acquisition (43 Sites) + FR-S-0955 Deletion
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE

### Objective

(1) Delete FR-S-0955 Memorial Plaza (confirmed parking lot, staged in error).
(2) Acquire GPS coordinates for the 43 Franklin County sites that had blank `gps_lat`/`gps_lon` fields.

### FR-S-0955 Deletion

Removed from `sites` table, `discovery_provenance` table, and TSV. Site count: 1,030 → **1,029**.

### GPS Acquisition Method

Used US Census Bureau Geocoder API (`geocoding.geo.census.gov`) via browser JavaScript fetch, batching 10 addresses per request. For addresses not in the Census database (rural roads, newer developments, parks), used web search (Yelp, hometownlocator.com, latitude.to, ColumbusRecParks) for confirmed coordinates. For linear water features and sites with no known street address, assigned representative centroid points marked as approximate.

### GPS Results Summary

| Quality | Count | Method |
|---------|-------|--------|
| Census geocoded | 27 | Address → Census API → lat/lon |
| Web search confirmed | 4 | Third-party mapping sources |
| Approximate (noted in DB) | 12 | Estimated from area/corridor context |
| **Total** | **43** | |

### Notable Findings

- **FR-S-0112 Champions Golf Course**: Address in DB was blank; confirmed as 3900 Westerville Rd, Columbus, OH 43224 (not 3625 as initially guessed)
- **FR-S-0392 Turnberry Golf Course**: Census geocoded to Pickerington (1145 Clubhouse Ln) — physically in Pickaway/Fairfield County border area despite being a Columbus RecParks facility
- **FR-S-0455 Gertrude S. Lawrence Woods**: DB location field says "3880 Shull Rd, Upper Arlington" but web research confirmed actual address is 4748 Red Bank Rd, Galena, OH (near Hoover Reservoir, Delaware County). GPS set to confirmed location; **address discrepancy flagged for correction**
- **FR-S-1021 Grange Insurance Audubon Center**: Census kept matching "505 E Whittier St" (wrong direction). Used approximate coordinates for 505 W Whittier area near Scioto Audubon Metro Park
- **FR-S-0027 Franklin County Fairgrounds**: Census couldn't match address; coordinates from hometownlocator.com (40.0345, -83.1535)

### Approximate GPS Sites (Flagged in Notes)

FR-S-0004 (Big Darby Creek), FR-S-0005 (Little Darby Creek), FR-S-0006 (Olentangy Scenic River), FR-S-0008 (Big Darby Hunting Area), FR-S-0032 (Sale Road Playground), FR-S-0036 (West Side Playground), FR-S-0410 (Warren Square), FR-S-0411 (Watercourse Dedication/Scioto), FR-S-0908 (Whitney Playground), FR-S-0964 (Kelley Green), FR-S-1007 (Marble Cliff Island Greenspace), FR-S-1021 (Grange Insurance Audubon Center)

### Post-Session Entity Counts

| Table | Franklin Rows |
|---|---|
| sites | **1,029** (-1 from FR-S-0955 deletion) |
| site_parent | 21 (unchanged) |

### Pending Tasks (Carry Forward — after Session 20)

1. **FR-S-0455 address discrepancy** — DB says 3880 Shull Rd, Upper Arlington; actual is 4748 Red Bank Rd, Galena (Delaware County). Verify and correct location field
2. **Approximate GPS field verify** — 12 sites flagged; recommend field verification or improved geocoding pass
3. **Plus Code / Township fields** — ~1,000 sites blank; requires geocoding pass
4. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
5. **Woodside Green Park classification flag** — gahanna.gov Community Park vs MORPC Regional Park

---

## Session 21 — Plus Code Generation (1,029 Sites)
**Date:** 2026-03-18
**Operator:** Claude
**Status:** COMPLETE

### Objective

Generate Open Location Code (Plus Code) values for all 1,029 Franklin County sites and write to `plus_code` DB column and TSV column 18.

### Method

Implemented the OLC encode algorithm in pure Python (no external library required):
- 4 pair-encoded characters × 2 (lat + lon) = 8 chars before separator
- 2 grid-encoded characters after `+` separator (5×4 grid subdivision)
- All codes generated at standard 10-digit precision (e.g. `86FVX27C+Q2`)

All sites already had GPS from Session 20, so all 1,029 codes were generated with 0 skipped.

### Results

| Metric | Value |
|--------|-------|
| Sites processed | 1,029 |
| Plus Codes generated | 1,029 |
| Plus Codes blank after update | 0 |

**Sample codes:**
- FR-S-0001 Gahanna Woods: `86GV35PH+G2`
- FR-S-0168 Fran Ryan Center: `86FVX27C+Q2`
- FR-S-1026 Friendship Park: `86GV248F+C2`

### Files Updated

- **DB `sites.plus_code`**: 1,029 rows updated
- **`franklin_oh_sites.tsv`**: regenerated with Plus Code column populated

### Pending Tasks (Carry Forward — after Session 21)

1. **Township fields** — ~1,000 sites blank; requires reverse-geocoding against Ohio township boundary polygons (separate GIS pass)
2. **MORPC map verification pass** — consolidated cross-municipality pass still outstanding
3. **Woodside Green Park classification flag** — gahanna.gov Community Park vs MORPC Regional Park

---

---

## Session 22 — 2026-03-19

### MORPC Verification Pass (Completed)

**Source:** MORPC Parks and Open Space layer (FeatureServer/11 / local CSV `Parks_and_Open_Space_7241389496048841555.csv`)
**Franklin County records:** 1,894 features → 1,142 unique names after deduplication

**Comparison methodology:** Normalized name matching (lowercase, strip punctuation/extra spaces) against all 1,029 FR- sites.

**Results summary:**
- 712 MORPC features matched DB entries by name (normalized)
- 430 unmatched MORPC features, broken down:
  - 123 cemeteries — out of scope, not cataloged
  - 29 golf courses — most in DB under slightly different names (Airport GC, Champions GC, etc.)
  - 9 private facilities — out of scope
  - 84 tiny NOS/street islands (<2 ac) — below Natural Areas threshold
  - 6 Special Use Recreation (senior centers, private clubs) — out of scope
  - ~110 near-duplicates with MORPC naming variants (e.g. "Scioto Audobon" misspelling, "Galloway Park" = "Galloway Road Parkland", "Hannah Farms Park" = "Hannah Park")
- **5 confirmed genuine gaps → added to DB**

**MORPC naming/attribution issues noted:**
- "Scioto Audobon" → misspelling of "Scioto Audubon Metro Park" (FR-S-0020)
- "Quarry Park" (117.6 ac) → same feature as "Quarry Trails Metro Park" (FR-S-0018) under older name
- "Galloway Park" (109.9 ac) → appears to be same area as "Galloway Road Parkland" (FR-S-0174, 123.52 ac)
- "Hannah Farms Park" → same as "Hannah Park" (FR-S-0592) in Gahanna
- "Blacklick Creek Greenway Trail" → already in DB as trail FR-T-0005, not a site
- "Ballentree Community Park" → same as "Ballantrae Community Park" (FR-S-0472), MORPC misspelling
- "Ballantrae Community Park (Dublin)" → same as FR-S-0472, Gahanna-administered

**Net-new sites added (FR-S-1032 to FR-S-1036):**

| Site ID | Name | Municipality | Acres |
|---|---|---|---|
| FR-S-1032 | Gahanna Woods | Gahanna | 99.4 |
| FR-S-1033 | The Homestead | Hilliard | 40.4 |
| FR-S-1034 | Highland Park | Westerville | 39.8 |
| FR-S-1035 | Swisher Creek Park | Plain Township | 17.9 |
| FR-S-1036 | Scioto Run Nature Trail | Hilliard | 11.5 |

Note: "Gahanna Woods" (FR-S-1032) is the Gahanna city-owned park, distinct from FR-S-0001 "Gahanna Woods State Nature Preserve" (ODNR). "The Homestead" (FR-S-1033) is the Hilliard city park, distinct from FR-S-0014 "Homestead Metro Park" (Metro Parks).

**Deferred — needs verification before adding:**
- "Finnell" (Columbus, PARK/M, ~49.8 ac) — no ParkID or source in MORPC; identity unclear

**DB/TSV after session:** 1,034 Franklin County sites (FR-S-0001 through FR-S-1036, minus deleted FR-S-0955)
**All 5 new sites have GPS (approximate) and Plus Codes — field verification recommended**


---

## Session 23 — Acreage Fill Pass (Cross-County Corrections + Bulk Acreage)

**Date:** 2026-03-19
**Starting site count:** 1,034 | **Ending site count:** 1,034 (no new sites)

### Cross-County Corrections (Turnberry & Red Stone Loop)
Following geometry verification completed at end of Session 22:

- **FR-S-0392 Turnberry Golf Course** → corrected counties=Fairfield; GPS centroid 39.921°N, -82.792°W; acres=209.13 (MORPC OBJECTID 22691); Plus Code 86FVW6C5+99. Note: retain FR- ID; reassign to FAI- during Fairfield County run.
- **FR-S-0547 Red Stone Loop Open Space** → corrected counties=Union; GPS centroid 40.133°N, -83.172°W; acres=0.12 (MORPC OBJECTID 23632); Plus Code 86GR4RJH+X6. Note: retain FR- ID; reassign to UNI- during Union County run.

These complete the three cross-county corrections this session (O'Shaughnessy was Session 22).

### Acreage Fill — Sources Used
1. **MORPC Shape__Area (sq ft / 43,560)** — confirmed unit via cross-check against 3 known-acreage sites (perfect match)
2. **Columbus Recreation and Parks Department** — official park listings
3. **City of Dublin** — official park listings
4. **Web search** — specific park/preserve pages

### Sites Updated This Session (15 confirmed fills)

| Site ID | Name | Acres | Source |
|---|---|---|---|
| FR-S-0027 | Franklin County Fairgrounds | 340 | Multiple web sources |
| FR-S-0030 | Sunbury Woods Commons | 4.05 | MORPC OBJECTID 26424 Shape__Area |
| FR-S-0123 | Cole Parkland | 28.10 | MORPC OBJECTID 26417 Shape__Area |
| FR-S-0227 | Innis Park | 99.108 | Columbus R&P official |
| FR-S-0278 | McKnight Outdoor Education Center | 11.798 | Columbus R&P official |
| FR-S-0312 | Overbrook Nature Preserve | 13.70 | Columbus R&P (Overbrook Ravine NP) |
| FR-S-0378 | Sugar Farms Parkland | 23.404 | Columbus R&P official |
| FR-S-0408 | Warner Woods Nature Preserve | 14.4 | Columbus R&P (preserve designation) |
| FR-S-0410 | Warren Square | 0.059 | Columbus R&P official |
| FR-S-0455 | Gertrude S. Lawrence Woods | 29.18 | Columbus R&P management plan 2023 |
| FR-S-0466 | Emerald Fields | 33.8 | City of Dublin official |
| FR-S-0836 | Merchant Park | 9.03 | MORPC OBJECTID 26430 Shape__Area |
| FR-S-0837 | Mildred Park | 4.28 | MORPC OBJECTID 26431 Shape__Area |
| FR-S-0910 | Moses Wright Nature Area | 7.0 | Worthington Spotlight article |
| FR-S-1021 | Grange Insurance Audubon Center | 5.0 | Audubon/Metro Parks sublease documentation |

### Parent Relationship Set
- **FR-S-1024** (Ginny and John Elam Environmental Center) → `parent_site_id = FR-S-1023` (Camp Ken-Jockety & The Elam Environmental Center). Elam Center is a building/facility within the Camp Ken-Jockety grounds; acreage left null as sub-facility.

### Remaining Acreage Gaps (29 sites, 97.2% coverage)
- **Legitimately null (~16):** Linear water corridors (FR-S-0004/0005/0006/0411), point sub-facilities (pools, pavilions, splash pad, gazebos, courts, mansion stage)
- **Research incomplete (~13):** FR-S-0003, FR-S-0032, FR-S-0036, FR-S-0527, FR-S-0536, FR-S-0543, FR-S-0908, FR-S-0964, FR-S-0980, FR-S-1007, FR-S-1024. Most are tiny neighborhood parks/open spaces or private facilities; public acreage data not found via web or MORPC.

### TSV Regenerated
- `County_Spreadsheets/Franklin/franklin_oh_sites.tsv` — 1,034 rows + header
- 97.2% acreage coverage (1,005/1,034 sites have acres > 0)



---

## Session 24 — UA Completion, GPS Fixes, Greensview Deletion, Finnell Park Addition

**Date:** 2026-03-19
**Starting site count:** 1,034 | **Ending site count:** 1,037

### Upper Arlington Park Catalog Completion (Sessions 23–24 continuation)
Chrome browser used to check the live City of Upper Arlington parks listing. The handoff's "~5 missing parks" figure was based on a stale web search snippet; the actual UA city website listed 21 parks. Three parks were missing from DB and added:

| Site ID | Name | Address | Acres |
|---|---|---|---|
| FR-S-1037 | Jack Nicklaus Park | 2470 Tremont Rd, UA | 2.0 |
| FR-S-1038 | Stratford Park | 2826 Stratford Dr, UA | 4.0 |
| FR-S-1039 | Triangle Park | 1722 Cambridge Blvd, UA | 2.0 |

All three inserted with GPS from Google Maps, Plus Codes computed via project OLC encoder.

### GPS and Acreage Corrections (Upper Arlington)
Two existing UA sites had bad data:

- **FR-S-0805 Sunny 95 Park** — GPS was 39.9512°N/-82.9106°W (wrong, east Columbus area). Corrected to 40.0466°N/-83.0610°W (4395 Carriage Hill Ln, UA). Acreage confirmed 73.0 ac.
- **FR-S-0810 Burbank Park** — acreage was 0.03 ac (clearly wrong). UA city website shows 7 Acres. Corrected.

### Greensview Park — Deleted
**FR-S-0807** was confirmed bad data. Searching Google Maps returns only Greensview Elementary School. City of UA parks listing does not include it. Record deleted from both `sites` and `discovery_provenance` tables.

### Puskar's Playground (Research)
User observed "Puskar's Playground" label on Google Maps near 40.082°N/-83.147°W (Dublin/NW Columbus area near Avery Rd). Not in DB and not in MORPC. Web search returns no independent park by that name. Determined to be a **named playground structure** within The Commons at Brighton (FR-S-0568) or Trinity Park (FR-S-0517) — both Dublin parks already in DB. Not cataloged as a standalone site per project entity rules.

### Finnell Park — Added
MORPC OBJECTID 24387 ("Finnell", Columbus, 49.77 ac, PARK/M type) was confirmed as a real Columbus park and added to DB.

**GPS note:** The Google Maps URL examined in a prior session pointed to 40.082°N/-83.147°W (Dublin/Avery Rd area), but the MORPC centroid for this record is **39.882°N/-83.005°W** (south Columbus). The MORPC centroid was used as the authoritative GPS source. The Google Maps URL's coordinates likely reflected the user's map viewport, not Finnell's actual location.

| Field | Value |
|---|---|
| Site ID | FR-S-1040 |
| Name | Finnell Park |
| Municipality | Columbus |
| Acres | 49.77 |
| GPS | 39.8824°N, -83.0047°W |
| Plus Code | 86FRVXJW+R2 |
| Source | MORPC OBJECTID 24387 |

### DB/TSV After Session
- **FR-S- sites:** 1,037 (FR-S-0001 through FR-S-1040; gaps at 0807 and others deleted in prior sessions)
- **TSV:** `franklin_oh_sites.tsv` — 1,037 rows + header
- **Acreage coverage:** 1,010/1,037 = 97.4%

### Remaining Open Items
- Township GIS pass: ~1,000 sites still blank (separate operation requiring GIS data)
- GPS verification for FR-S-1032–1036 (MORPC-pass sites with approximate centroids)
- ~27 sites with null acreage: mostly legitimately null (linear corridors, sub-facilities) or exhausted public sources

---

## Session 25 — Township GIS Lookup, Plus Code Utilities, Ohio TIGER Shapefile

**Date:** 2026-03-21
**Starting site count:** 1,037 | **Ending site count:** 1,037 (no additions)

### Utilities Saved

Two new project utilities written to `utilities/` and both passing self-tests:

| File | Purpose | Self-test |
|---|---|---|
| `utilities/na_plus_code.py` | Open Location Code (Plus Code) encoder — zero dependencies; 7/7 test vectors pass | ✓ PASS |
| `utilities/na_township_lookup.py` | Point-in-polygon township/municipality lookup via TIGER COUSUB — zero dependencies; 5/5 test vectors pass | ✓ PASS |

### Ohio TIGER Shapefile Acquired

- **File:** `GIS_Assets/ohio_townships/tl_2024_39_cousub.zip` (6.2 MB)
- **Source:** US Census Bureau TIGER/Line 2024 County Subdivisions
- **URL:** `https://www2.census.gov/geo/tiger/TIGER2024/COUSUB/tl_2024_39_cousub.zip`
- **Contents:** 1,607 Ohio MCDs — 1,309 civil townships (CLASSFP="T1") + 298 incorporated places
- **Coverage:** All 88 Ohio counties; one-time acquisition for full pipeline

### Township Field — Franklin County

**Method:** `OhioTownshipLookup.get_township(lat, lon)` — filters to CLASSFP="T1" records only; ray casting point-in-polygon with bounding-box pre-filter.

**Results:**

| Category | Count |
|---|---|
| Sites assigned a civil township | 373 |
| Sites in incorporated cities (no township — correct Ohio behavior) | 664 |
| Sites without GPS (no lookup possible) | 1 |
| **Total** | **1,037** |

**Top townships by site count:** Washington (105), Mifflin (67), Jackson (41), Sharon (29), Madison (27), Norwich (25), Plain (20), Hamilton (13), Truro (10), Jefferson (9)

**Ohio township note:** In Ohio law, land incorporated into a city or village leaves its township for governmental purposes. The TIGER COUSUB file correctly reflects this — incorporated cities have their own polygon records and the township polygons do not extend into city limits. Therefore `get_township()` correctly returns `None` for the 664 sites inside Columbus, Dublin, Gahanna, etc.

### Plus Code Bug Fix

- **FR-S-0805:** Plus Code was `86GR2WWQ+JH2` (12 chars — extra "2" appended). Corrected to `86GR2WWQ+JH`. Fixed in TSV and DB.

### Integrity Check — Post-Session 25

| Check | Result |
|---|---|
| Bad column counts | 0 ✓ |
| Blank site_ids | 0 ✓ |
| Bad Plus Codes | 0 ✓ (FR-S-0805 fixed) |
| GPS out of Ohio range | 0 ✓ |

### Field Coverage — Post-Session 25

| Field | Coverage |
|---|---|
| GPS Lat/Lon | 1,036 / 1,037 (99.9%) |
| Plus Code | 1,036 / 1,037 (99.9%) |
| Municipality | 997 / 1,037 (96.1%) |
| Township | 373 / 1,037 (36.0%) — 664 correctly blank (incorporated cities) |
| Acres | 1,012 / 1,037 (97.6%) |

### Remaining Open Items
- MORPC map verification pass (LOW priority)
- GPS verification for FR-S-1032–1036 (approximate centroids)
- ~25 sites with null acreage: legitimately null or exhausted sources

---

## Session 26 — P&OS Completeness Gate Supplement

**Date:** 2026-05-11
**Run ID:** `franklin_oh_2026_05_11_pos_supplement`
**Starting site count:** 1,033 | **Ending site count:** 1,162
**Net addition:** +129 sites

### Trigger

IMP-097 Parks & Open Space Completeness Gate (and IMP-099 Cemetery/Golf inclusion) were added to the project after Franklin County's pipeline ran in March 2026. Franklin is the only completed county in the 15-county MORPC coverage area, so a targeted supplement was run rather than a full redo.

### Gate Results

Script: `franklin_pos_gate.py` — cross-checks MORPC centroids CSV (989 Public/non-NOS rows) against DB Franklin sites (1,033) using fuzzy name matching (token_set_ratio ≥ 80, threshold per IMP-097).

| MORPC Type | Qualifying rows | Matched | Unmatched |
|---|---|---|---|
| Cemetery | 104 | 0 | 104 |
| Golf | 25 | 0 | 25 |
| Park | ~800 | ~776 | 22 |
| Recreation | ~60 | ~58 | 2 |

### Supplement Upsert

Script: `franklin_supplement_upsert.py`

**104 Cemeteries added:**
- category = Cemetery (new category — was 0 before this session)
- Subtypes inferred from name patterns: Veterans Cemetery, Church Cemetery, Family Cemetery, Public Cemetery
- Ownership inferred: religious names → Private; "City of X" jurisdictions → Municipal; townships → Private
- GPS from MORPC centroids (HIGH confidence)
- All in Franklin County proper; private cemeteries with "St." or church names treated as Church Cemetery subtype

**25 Golf Courses added:**
- category = Recreation Facility, subtype = Golf Course
- OSU Golf courses → governance = "Ohio State University", ownership = Institutional
- Sports Ohio (Virtus) courses → governance = city, ownership = Governmental
- Remaining → ownership = Private
- GPS from MORPC centroids (HIGH confidence)

**7 Park/Open Space entities added:**
- Emersonia Park (Worthington)
- Clinton Township Playground
- Fieldstone Open Space (Columbus — Clintonville)
- Parkview Park (Hamilton Township)
- Mango Park (Grove City)
- Clinton Road Park (Westerville)
- South Westerville Park
- Darree Fields (Dublin — large multi-sport complex; was in MORPC but missed in original T6 discovery)

**18 Excluded (PARK_EXCLUSIONS set):**
- Trail corridor parcels: Blacklick Creek Greenway, Alum Creek Greenway, Olentangy Trail, Big Walnut Trail, Hoover-to-Alum Creek Trail (all in DB as Trail entities, not Sites)
- MORPC administrative entries: Franklin County Fire Station parcels, Senior Centers
- MORPC data quality issues: "Hamilton Township Road Dept" parcel, duplicate/typo entries

**Consolidations:**
- Muirfield Village Golf Club: 5 MORPC parcels → 1 DB record (FR-S-1171); summed acreage 195.27 ac
- Pinnacle Golf Club: 2 MORPC parcels → 1 DB record (FR-S-1062); summed acreage 200.12 ac

### DB Cleanup

After upsert, 8 records deleted:

| Deleted | Reason |
|---|---|
| FR-S-1179, 1180, 1181 | MANUAL_GAPS duplicated MORPC upsert results — MORPC versions kept |
| FR-S-1172, 1173, 1174, 1175 | 4 extra Muirfield parcels — FR-S-1171 kept with summed acres |
| FR-S-1061 | Smaller Pinnacle Golf parcel — FR-S-1062 kept with summed acres |

FR-S-1178 renamed from "Clinton Township Playground (MORPC)" → "Clinton Township Playground".

### Normalization Notes

| Decision | Rationale |
|---|---|
| Cemetery subtypes inferred from name | Veterans/Church/Family keywords deterministic; all others → Public Cemetery |
| Church cemetery ownership = Private | Religious organizations are private entities even when open to public interment |
| "Sports Ohio" courses = Governmental | Sports Ohio is a Columbus Recreation & Parks entity |
| Trail corridor parcels excluded from Sites | FR-T-0005/0007 etc. already in DB as Trail entities; dual-representation would be wrong |

### Post-Session Coverage

| Field | Coverage |
|---|---|
| GPS Lat/Lon | ~1,161 / 1,162 (99.9%) — supplement sites have MORPC centroids |
| Plus Code | 1,036 / 1,162 — **129 supplement sites lack Plus Codes** (pending GIS pass) |
| Municipality | ~1,100 / 1,162 — supplement sites have MORPC Jurisdiction; rural cemeteries may lack |
| Township | 373 / 1,162 — supplement sites not yet processed through township lookup |
| Acres | ~1,140 / 1,162 — supplement sites have MORPC Acres |

### Open Items After Session 26

| Priority | Item |
|---|---|
| HIGH | Access Points — 0 staged; 115 trails with no APs is the largest remaining gap |
| MEDIUM | Cross-county IMP-104 flags — Big Darby, Little Darby, Olentangy scenic rivers; Ohio to Erie Trail; Buckeye Trail need `CROSS_COUNTY_CANDIDATE` in identity_notes_raw |
| MEDIUM | 13 null townships — re-verify using `Townships_Officials2022-2023.xlsx` (IMP-096); original web searches returned wrong-county results for ~7 of 18 |
| LOW | Plus Code + township GIS pass for 129 supplement sites |
| LOW | Water trail sub-procedure (IMP-103) — Big Darby and Alum Creek paddling corridors not evaluated |
| LOW | MORPC map verification pass (deferred from Tier 6) |

---

## Session 27 — 2026-05-11

### Summary

**Session type:** Multi-task close-out — GIS supplement pass, cross-county flags, township re-check, water trail evaluation, Access Points discovery
**Status:** COMPLETE
**Net result:** 90 FR-AP records in DB; Franklin County work complete except Metro Parks hiking trail trailheads (low priority)

---

### Task A — Plus Code + Township GIS Pass for 129 Supplement Sites (Task #28)

**Objective:** The 129 sites added in Session 26 (cemeteries, golf courses, parks/open spaces) had blank Plus Code and Township fields; supplement upsert wrote GPS from MORPC centroids but skipped GIS derivation.

**Method:** Ran `encode_plus_code(lat, lon)` from `utilities/na_plus_code.py` and `OhioTownshipLookup.get_both(lat, lon)` from `utilities/na_township_lookup.py` against all 129 supplement sites. Shapefile: `GIS_Assets/ohio_townships/tl_2024_39_cousub.zip` (acquired Session 25). Township lookup returns `None` for coordinates inside incorporated cities (correct Ohio behavior).

**Results:**
- Plus Codes generated: 129 / 129
- Township assigned: ~43 (rural cemeteries and golf courses in unincorporated areas)
- Township correctly null: ~86 (sites inside Columbus, Dublin, Gahanna, etc.)
- DB and TSV updated: `natural_areas_v5.db` sites table + `franklin_oh_sites.tsv`

**Post-task Plus Code coverage:** 1,162 / 1,162 (100%) ✓
**Post-task Township coverage:** ~416 / 1,162 assigned; remainder correctly null (incorporated cities)

---

### Task B — 13 Null Township Re-check (Task #29)

**Objective:** Session 25 left 13 Franklin County site records with null township that were flagged for re-verification using `Townships_Officials2022-2023.xlsx` (IMP-096). Original web searches in Tier 5 returned wrong-county results for ~7 of 18 townships.

**Method:** Cross-referenced each null-township site GPS against `Townships_Officials2022-2023.xlsx` roster and `OhioTownshipLookup.get_township()` results. For sites where the lookup also returned null, verified municipality field to confirm site is inside an incorporated city.

**Findings:**
- **Marion Township** — confirmed defunct (fully absorbed into City of Columbus per ORC merger records); null township is correct
- **Remaining 12 null townships** — all verified as sites inside incorporated cities (Columbus, Dublin, Gahanna, etc.); `get_township()` correctly returning `None` per Ohio law (cities leave their township)
- No corrections required; all 13 nulls are correct

**Resolution:** All 13 null township cases confirmed correct. No DB changes needed.

---

### Task C — IMP-104 Cross-County Candidate Flags (Task #30)

**Objective:** Per IMP-104 `na_cross_county_resolution_v5.1.md`, entities that span multiple counties or have explicit cross-county governance should have `CROSS_COUNTY_CANDIDATE` in `identity_notes`. Franklin County has 5 known cross-county entities that were missing this flag.

**Entities flagged:**

| Entity ID | Name | Counties |
|---|---|---|
| FR-S-0004 | Big Darby Creek State and National Scenic River | Franklin, Madison, Pickaway, Champaign, Logan, Union |
| FR-S-0005 | Little Darby Creek State Scenic River | Franklin, Madison, Pickaway, Union |
| FR-S-0006 | Olentangy River State Scenic River | Franklin, Delaware |
| FR-T-0009 | Ohio to Erie Trail | Multi-county (Franklin segment) |
| FR-T-0010 | Buckeye Trail | Multi-county (Franklin segment) |

**Method:** `UPDATE sites/trails SET identity_notes = identity_notes || '; CROSS_COUNTY_CANDIDATE' WHERE site_id/trail_id IN (...)` — applied to all 5 entities in `natural_areas_v5.db`.

**TSV update:** `identity_notes` column updated in `franklin_oh_sites.tsv` and `franklin_oh_trails.tsv` for affected rows.

---

### Task D — Water Trail Sub-Procedure Evaluation (Task #31)

**Objective:** IMP-103 `na_water_trail_discovery_subproc_v5.1.md` was added after Franklin County's original pipeline run. Two Franklin County paddling corridors — Big Darby Creek and Alum Creek — had not been evaluated against the IMP-103 qualification threshold.

**Method:** Applied IMP-103 §2 qualification criteria to existing Franklin County water-related trail records.

**Findings:**

| Trail ID | Name | Evaluation | Outcome |
|---|---|---|---|
| FR-T-0118 | Big Darby Creek Water Trail | ODNR-designated paddle route; access points documented (FR-AP-0001–0009); meets IMP-103 threshold | **Confirmed — existing record valid** |
| FR-T-0117 | Alum Creek Water Trail | ODNR-designated paddle route with formal access infrastructure; meets IMP-103 threshold | **Confirmed — existing record valid** |

**No new entities required.** Existing trail records and access points captured in prior sessions already satisfy the IMP-103 requirements. Water trail sub-procedure evaluation complete.

---

### Task E — Access Points Discovery: Greenway Trailheads (Task #32)

**Session scope:** FR-AP-0055 through FR-AP-0090 — 36 greenway trail trailheads for 8 Columbus-area greenway trails managed by Columbus Recreation and Parks Department (CRPD).

#### Prior Session Error — ImportError Fix

The prior session's batch insert script failed with:
```
ImportError: cannot import name 'lookup_township' from 'na_township_lookup'
```
Root cause: script attempted `from na_township_lookup import lookup_township` — no such standalone function exists. The module uses a class-based API. Correct import:
```python
from na_township_lookup import OhioTownshipLookup
lookup = OhioTownshipLookup()
twp_raw = lookup.get_township(lat, lon)      # returns bare name e.g. "Franklin" or None
muni = lookup.get_municipality(lat, lon)     # returns city/village or falls back to township
```
The `OhioTownshipLookup` class auto-locates `GIS_Assets/ohio_townships/tl_2024_39_cousub.zip` via path derivation from `__file__`.

#### Scioto Audubon GPS Correction

The prior session had used Dodge Park GPS (39.9534°N, -83.0147°W) as a proxy for Scioto Audubon Metro Park trailhead. Checking the DB revealed the stored GPS was even worse — (40.117, -83.111) — pointing far north of the actual site. Used corrected approximate coordinates (39.933°N, -83.021°W), flagged as `gps_confidence: Nominatim-MED`.

#### Sources Used

**CRPD authoritative trail pages fetched:**
| Trail | FR-T ID | CRPD URL | Trailheads Listed |
|---|---|---|---|
| Olentangy Trail | FR-T-0108 | columbusrecparks.com/facilities/trails/greenways/olentangy-trail/ | 8 (6 Columbus R&P + 2 Worthington) |
| Alum Creek Trail | FR-T-0100 | columbusrecparks.com/facilities/trails/greenways/alum-creek-trail/ | 8 |
| Big Walnut Trail | FR-T-0101 | columbusrecparks.com/facilities/trails/greenways/big-walnut-trail/ | 6 |
| Blacklick Creek Trail | FR-T-0102 | columbusrecparks.com/facilities/trails/greenways/blacklick-creek-trail/ | 3 |
| Scioto Trail | FR-T-0110 | columbusrecparks.com/facilities/trails/greenways/scioto-trail/ | 3 (+ 2 geographic) |
| Hellbranch Trail | FR-T-0107 | columbusrecparks.com/facilities/trails/greenways/hellbranch-trail/ | 2 |
| Camp Chase Trail | FR-T-0002 | columbusrecparks.com/facilities/trails/greenways/camp-chase-trail/ | 2 |
| Heritage Rail Trail | FR-T-0113 | columbusrecparks.com/facilities/trails/greenways/heritage-trail/ | 1 |

**GPS sources:**
- **DB** — parks already in `sites` table with confirmed GPS (most Columbus R&P parks)
- **Nominatim-MED** — Nominatim geocode with moderate confidence (Heritage Trail Metro Park, Scioto Audubon approximate)
- **Nominatim-LOW** — low-confidence geocode (Hoover Nature Preserve, Retreat at Turnberry)

#### Multi-trail Hub Parks

Three parks serve as trailheads for multiple greenway trails — each required a separate AP record per trail:

| Park | Trails Served | AP IDs |
|---|---|---|
| Three Creeks Park | Alum Creek Trail, Big Walnut Trail, Blacklick Creek Trail | FR-AP-0067, FR-AP-0075, FR-AP-0079 |
| Battelle Darby Creek | Camp Chase Trail, Darby Creek Trail | FR-AP-0087, FR-AP-0089 |
| Hayden Park | Alum Creek Trail (primary), Big Walnut Trail (Hayden/Big Walnut connector) | FR-AP-0064, FR-AP-0076 |

#### Cross-County Trailheads

Two trailheads on Franklin County greenway trails are physically located in neighboring counties:

| AP ID | Name | Parent Trail | County | Notes |
|---|---|---|---|---|
| FR-AP-0078 | Retreat at Turnberry Trailhead | FR-T-0102 Blacklick Creek Trail | Fairfield | Near Pickerington; Nominatim-LOW GPS |
| FR-AP-0075 | McNamara Park Trailhead | FR-T-0101 Big Walnut Trail | Delaware | Near Westerville; Nominatim-MED GPS |

Both inserted with correct non-Franklin county values in the `county` column. FR- ID prefix retained per project convention (entities discovered during Franklin County run).

#### Batch Insert — Script

**Script:** `insert_greenway_trailheads.py` (saved to working outputs directory)

**Key code structure:**
```python
import sys, sqlite3
sys.path.insert(0, '/sessions/busy-nifty-ride/mnt/Natural Areas Project v5/utilities')
from na_plus_code import encode_plus_code
from na_township_lookup import OhioTownshipLookup

lookup = OhioTownshipLookup()
# ... 32 GPS entries in dict GPS = {...}
# ... 36 RECORDS tuples: (trail_id, ap_name, gps_key, features, identity_notes, url)
# Insert loop: FR-AP-0055 through FR-AP-0090
for i, (trail_id, ap_name, gps_key, ...) in enumerate(RECORDS):
    ap_id = f"FR-AP-{55 + i:04d}"
    twp_raw = lookup.get_township(lat, lon)
    township = (twp_raw + " Township") if twp_raw else None
    plus_code = encode_plus_code(lat, lon)
    cur.execute("INSERT INTO access_points ...", ...)
```

**Result:** 36 inserted, 0 errors.

**Note:** `OhioTownshipLookup.get_township()` returns `None` for all Columbus parks (correct — incorporated cities leave their civil township in Ohio). `township` field set to `None` for those 34 records; only the 2 cross-county records (Retreat at Turnberry in Fairfield, McNamara in Delaware) have rural GPS that might fall in a township, and those were also `None` (Pickerington and Westerville are incorporated cities).

#### AP Distribution by Trail

| Trail ID | Trail Name | AP IDs | Count |
|---|---|---|---|
| FR-T-0108 | Olentangy Trail | FR-AP-0055–0060 | 6 |
| FR-T-0100 | Alum Creek Trail | FR-AP-0061–0070 | 10 |
| FR-T-0101 | Big Walnut Trail | FR-AP-0071–0076 | 6 |
| FR-T-0102 | Blacklick Creek Trail | FR-AP-0077–0079 | 3 |
| FR-T-0110 | Scioto Trail | FR-AP-0080–0084 | 5 |
| FR-T-0107 | Hellbranch Trail | FR-AP-0085–0086 | 2 |
| FR-T-0002 | Camp Chase Trail | FR-AP-0087–0088 | 2 |
| FR-T-0103 | Darby Creek Trail | FR-AP-0089 | 1 |
| FR-T-0113 | Heritage Rail Trail | FR-AP-0090 | 1 |
| **Total** | | | **36** |

#### TSV Export

`franklin_oh_access_points.tsv` regenerated from DB — 90 rows (header + 90 APs):
- FR-AP-0001–0054: water trail APs (prior sessions)
- FR-AP-0055–0090: greenway trailheads (this session)

---

### Final Entity Counts — Session 27

| Table | Franklin Rows |
|---|---|
| sites | **1,162** |
| trails | **115** |
| trail_segments | **1** |
| trail_networks | **2** |
| site_networks | **1** |
| access_points | **90** (FR-AP-0001–0090: 88 Franklin county + 2 cross-county) |
| manual_review_queue | 500 (all decided) |
| site_parent | 21 (Franklin) |

### Remaining Open Items (After Session 27)

| Priority | Item | Notes |
|---|---|---|
| LOW | Metro Parks hiking trail trailheads | ~90 Metro Parks hiking trails (FR-T-0002–0098 range) have no APs staged. Would require systematic Metro Parks website pass for parking lot GPS. Not in scope for current Franklin close-out. |
| LOW | MORPC map verification pass | Consolidated cross-municipality pass deferred since Session 2. Not blocking pipeline; low-return given MORPC layer completeness. |
| LOW | Approximate GPS sites (12) | FR-S-0004/0005/0006/0032/0036/0411/0908/0964/1007/1021 — field verification recommended but not blocking |
