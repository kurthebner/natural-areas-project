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

**Map verification status:**
- City-scale overview completed: distribution consistent with 419-park catalog; no obvious gaps identified
- Full quadrant-by-quadrant map pass: PENDING — required before marking Columbus COMPLETE per Municipal Sub-Procedure v5.2 §4.4
- Recommend dedicated sub-session for Columbus map pass before pipeline handoff

