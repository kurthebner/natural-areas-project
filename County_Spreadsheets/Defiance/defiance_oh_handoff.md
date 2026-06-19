# Defiance County, Ohio — Handoff Document
**RUN_ID:** `defiance_oh_2026_04_19`
**PREFIX:** `DEF`
**Last updated:** 2026-04-20 (PIPELINE COMPLETE — 32 Sites, 7 Trails, 6 APs normalized and committed to DB; all TSVs written; vocab gate passed; session log updated)
**Status:** PIPELINE COMPLETE — 45 entities in natural_areas_v5.db; run_id defiance_oh_2026_04_19; open flags: VERIFY_GOVERNANCE (DEF-S-016), GOVERNANCE_UNCERTAIN (DEF-T-007), GPS_LOW (4 sites), DEF-F-06 (Oxbow WA parcel)

This document is the durable record across context breaks. Update before every session end.

---

## Tiers Completed

| Tier | Source Type | Entities Found | Notes |
|------|-------------|----------------|-------|
| T1 | Federal & Tribal | 1 Trail | North Country NST; all other entity types null with evidence |
| T2 | State agency (ODNR, Water Trails) | 2 Sites, 1 Child Site, 2 Trails, 3 Access Points | Independence Dam SP, Oxbow Lake WA, Winchester's Camp, Maumee River Water Trail, Canal Towpath Trail; ODNR Forestry + Nature Preserves = null |
| T3 | District (Defiance SWCD) | 1 Site, 1 Trail, 1 Access Point | Penney Nature Center (78 ac); Storybook Trail; no park district exists |
| T4 | County (DCHS / Auglaize Village) | 1 Site | Auglaize Village (120 ac, 12296 Krouse Rd); county-owned, DCHS-managed; DEF-F-05 governance noted |
| T5 | Township | NULL — 0 entities | All 12 townships searched individually per §4.1–§4.5 with §4.2a wrong-county verification. No township parks, trails, or access points in any township. 5 wrong-county websites discarded. TrekOhio confirms no township parks in county. COMPLETE 2026-04-20. |
| T6 | Municipal — City of Defiance + Villages | 17 Sites + 2 Trails + 2 APs (City of Defiance); 6 Sites (villages) = 27 total entities | COMPLETE 2026-04-20. City: 15 web-discovered + 2 map-verification finds (Buchman Park on the Glaize, Memory Park). Villages: Hicksville ×3, Sherwood ×2 (Little Reservation Station Park + Moats Park map find), Ney ×1. Map verification §4.4 complete for all 4 municipalities — GPS captured for all entities. Open pipeline items: Canal Park=Amphitheater on Maps; StoryWalk Trail has no standalone Maps entity; Reservoir Boat Ramp links to ohiodnr.gov (possible T2 overlap); Veterans Memorial at Latty's Grove has two co-located Maps entities; Sherwood Ball Park entity unstaged. |
| T7 | Conservancy & Land Trust | 1 Site (Thoreau Wildlife Reserve) + 1 Trail (Hicksville Nature Trail) = 2 entities | COMPLETE 2026-04-20. BSC: Weisgerber-Pohlmann = Williams Co (WRONG_COUNTY); Forder Bridge = Paulding Co (WRONG_COUNTY). TNC: no Defiance County holdings. Thoreau Wildlife Reserve confirmed (250 ac, Diehl Family Foundation, 4 unnamed trails). Hicksville Nature Trail confirmed (1.8 mi, Hicksville Trail Association, GOVERNANCE_UNCERTAIN). |
| T8 | Private & Organization-Based | 3 Sites (Camp Lakota, Bark & Run Dog Park, Shallow Creek Hunting Preserve) | COMPLETE 2026-04-20. Camp Lakota confirmed Defiance County (2180 Ginter Rd, 640 ac, BSA). Bark & Run Dog Park confirmed (501c3 nonprofit, 11795 Precision Way). Shallow Creek Hunting Preserve confirmed (7599 Stever Rd, ODNR-licensed pheasant hunting). GM lagoons + Hickory Lake + Kettenring Hills dams excluded (no public access). Auglaize Hydro = Williams County (excluded). |

---

## Tiers Remaining

| Tier | Source Type | Entry Points |
|------|-------------|--------------|
| T1 | Federal + OSM | Overpass API (boundary=protected_area, leisure=park, leisure=nature_reserve, etc. within Defiance County polygon); USFWS, NPS, BLM, USACE NID national datasets; check North Country NST routing |
| T2 | State agency | ODNR Parks (`ohiodnr.gov`); ODNR Division of Wildlife (Oxbow Lake WA); ODNR Division of Forestry; ODNR Water Trails (Auglaize, Maumee, Tiffin); ODOT; Ohio Historic Preservation Office; USACE NID (`nid.sec.usace.army.mil`) |
| T3 | District agency | Defiance Soil and Water Conservation District (`defiancecounty.com/swcd/`) — manages Penney Nature Center; no separate park district |
| T4 | County website | Defiance County official site (`defiancecounty.com`); Defiance County Historical Society (Auglaize Village); Defiance County Engineer (covered bridges, etc.) |
| T5 | Township | COMPLETE — see T5 checklist and YAML per-township records |
| T6 | Municipal — City + Villages | COMPLETE — web discovery + §4.4 map verification done for all 4 municipalities |
| ~~T7~~ | ~~Conservancy~~ | COMPLETE 2026-04-20 — see above |
| ~~T8~~ | ~~Private / other~~ | COMPLETE 2026-04-20 — see above |

---

## Key Active Flags

| Flag ID | Entity / Topic | Issue | Resolution Path |
|---------|----------------|-------|-----------------|
| DEF-F-01 | Kingsbury Park | Duplicate baseline rows (24 + 25 — same address) | RESOLVED — confirmed single entity "Kingsbury Riverfront Park, Pool, and Pickleball Facilities," 102 Auglaize St, 15.49 ac. |
| DEF-F-02 | Pontiac Metro Park | Name implies metropark but none exists in county; governance unknown | RESOLVED — 315 E River Rd; "Metro Park" is local name only (not metropark affiliation). NCT/BTA routes through park. Ownership unclear; VERIFY_GOVERNANCE retained (city manages but website says "not city-owned"). Staged at Tier 5. |
| DEF-F-03 | Power Dam vs. Auglaize Hydro | May be same physical dam | RESOLVED — Auglaize Hydro = Power Dam = same dam; Bryan Municipal Utilities (Williams County), 23 ft, 1913. Birding hotspot with public access. NOT city of Defiance asset. Defer to Tier 8. |
| DEF-F-04 | Fort Defiance Park vs. Fort Grounds | Possibly same entity (both reference historic fort) | RESOLVED — same entity at 320 Fort St. "Fort Grounds" is the city's official current name. NRHP-listed 1980. Staged at Tier 5. |
| DEF-F-05 | Auglaize Village | Defiance County-owned, Defiance County Historical Society-managed | Note governance during normalization |
| DEF-F-06 | Oxbow Lake WA "western agreement parcel" | Scope ambiguous | No evidence of western agreement parcel found in any authoritative source (stateparks.com, ODNR map PDF, search results). May be baseline error or informal reference to a management agreement. UNRESOLVED — check ODNR Wildlife GIS layer or contact area manager. |
| DEF-F-07 | Bronson Park / Splash Park | Same address; possibly one site | RESOLVED — Bronson Park (25 ac) is parent; Splash Park (opened July 4, 2018; $1.6M; ADA; free) is child at same address. Connected by multi-use path added 2021. Both staged at Tier 5. |
| DEF-F-08 | Reservoir Nature Trail | Trail inside Reservoir and Disc Golf site | RESOLVED — Reservoir Nature Trail staged as Trail child of "Reservoir and Disc Golf" Site; connects to Buckeye Trail via Canal Road. Parent link to be assigned in normalization. |
| DEF-F-09 | Winchester's Camp No. 3 | ODNR Historic Site #24 inside Independence Dam SP | RESOLVED — discovered as child Site of Independence Dam SP. Also known as "Fort Starvation" and "Old Kentucky Burial Grounds." Historical marker erected 2010 on US Rt. 424 within park. |
| DEF-F-10 | Sheet2 of baseline | Sheet2 has GPS/URLs not in Sheet1 — unclear provenance | Treat Sheet2 as unverified prompt; verify each via authoritative source during discovery |

---

## Entities Discovered

| # | Tier | Type | Name | Governance | Notes |
|---|------|------|------|------------|-------|
| 1 | T1 | Trail | North Country National Scenic Trail | NPS / NCTA | Passes through Defiance, Pontiac Park, Independence Dam SP; co-routed with Buckeye Trail in Ohio |
| 2 | T2 | Site | Independence Dam State Park | ODNR Parks | 591 ac, 27722 Co. Rd 424, Defiance OH; Maumee River; NCT/BTA route |
| 3 | T2 | Site | Oxbow Lake Wildlife Area | ODNR Division of Wildlife | 416 ac; Big Oxbow Lake (38 ac, 1953) + Little Oxbow Lake (4.5 ac); DEF-F-06 western parcel unresolved |
| 4 | T2 | Site (child) | Winchester's Camp No. 3 / Fort Starvation | ODNR / Historic Site #24 | Inside Independence Dam SP; War of 1812 burial ground; historical marker 2010 |
| 5 | T2 | Trail | Maumee River Water Trail | ODNR + Metroparks Toledo | 107 mi, 39 access pts, 5 counties incl. Defiance; Independence Dam SP is named access point |
| 6 | T2 | Trail | Miami and Erie Canal Towpath Trail | ODNR Parks | 3 mi within Independence Dam SP to Florida OH; NCT/BTA co-route |
| 7 | T2 | Access Point | Independence Dam SP Boat Launch | ODNR Parks | 4-lane ramp + hand launch; Maumee River |
| 8 | T2 | Access Point | Bend Road Bridge | ODNR | Maumee River near Sherwood; MINIMAL_DATA |
| 9 | T2 | Access Point | Five-Mile Creek Access Area | ODNR Wildlife | Auglaize River, OH-111 SW of Defiance; MINIMAL_DATA |
| 10 | T6 | Site | Fort Grounds | City of Defiance Parks & Rec | 320 Fort St; Fort Defiance 1794 site; NRHP-listed; confluence of Maumee/Auglaize; DEF-F-04 resolved |
| 11 | T6 | Site | Diehl Park | City of Defiance Parks & Rec | 909 Wemor Dr; 39.77 ac; 4 ball fields + Kids Creation Playground |
| 12 | T6 | Site | Kingsbury Riverfront Park, Pool, and Pickleball | City of Defiance Parks & Rec | 102 Auglaize St; 15.49 ac; DEF-F-01 resolved |
| 13 | T6 | Site | Bronson Park | City of Defiance Parks & Rec | 2104 Power Dam Rd; 25 ac; parent of Splash Park; StoryWalk Trail |
| 14 | T6 | Site (child) | Splash Park | City of Defiance Parks & Rec | 2104 Power Dam Rd; opened July 4, 2018; $1.6M; ADA; free; DEF-F-07 resolved |
| 15 | T6 | Site | Canal Park | City of Defiance Parks & Rec | 310 Clinton St; Miami & Erie Canal Lock No. 37 remains + amphitheater |
| 16 | T6 | Site | Eastside Park | City of Defiance Parks & Rec | 1185 Karnes Ave; formerly Compo Park; revitalized neighborhood park |
| 17 | T6 | Site | Riverside Park | City of Defiance Parks & Rec | 849 Riverside Ave; 30 ac; Maumee River; 4 soccer fields + ball field |
| 18 | T6 | Site | Reservoir and Disc Golf | City of Defiance Parks & Rec | 1261 Precision Way; 9-hole disc golf; reservoir walkway; connects to Buckeye Trail |
| 19 | T6 | Site | Palmer Park | City of Defiance Parks & Rec | 1755 Palmer Dr; 5 tennis courts + playground; near HS + YMCA |
| 20 | T6 | Site | Pontiac Metro Park | VERIFY_GOVERNANCE | 315 E River Rd; Maumee/Auglaize confluence; NCT routes through; Chief Pontiac birthplace marker; boat launch; VERIFY_GOVERNANCE |
| 21 | T6 | Site | William C. Holgate Park | City of Defiance Parks & Rec | 811 Holgate Ave; former Second Ward School site; Victorian gazebo; renovated 2019 |
| 22 | T6 | Site | Hometown Heroes Park | City of Defiance Parks & Rec | 648 Clinton St; est. September 2013; active duty memorial with AMVETS Post 1991 |
| 23 | T6 | Site | Triangle Park | City of Defiance Parks & Rec | 655 Clinton St; clock tower; 1860s school donation site |
| 24 | T6 | Site | Veteran's Memorial Park at Latty's Grove | City of Defiance Parks & Rec | 610 Williams St; est. 1937/1947; baseball, basketball, tennis, 2 shelter houses |
| 25 | T6 | Trail | StoryWalk Trail | City of Defiance / Defiance Public Library | Within Bronson Park; seasonal outdoor reading trail |
| 26 | T6 | Trail | Reservoir Nature Trail | City of Defiance Parks & Rec | 1261 Precision Way; ~0.57 mi boardwalk + asphalt; ADA; connects to Buckeye Trail via Canal Rd |
| 27 | T6 | Access Point | Pontiac Metro Park Boat Launch | VERIFY_GOVERNANCE | 315 E River Rd; Maumee River confluence; primary in-town river access |
| 28 | T6 | Access Point | Reservoir Boat Ramp and Dock | City of Defiance Parks & Rec | 1129 Precision Way; 10-space stone lot; ramp + dock; AUTHORITY_FLAG: Maps links to ohiodnr.gov |
| 29 | T6 | Site | Buchman Park on the Glaize | City of Defiance Parks & Rec | 314 Auglaize St; MAP_VERIFICATION_FIND — not in web discovery |
| 30 | T6 | Site | Memory Park | City of Defiance Parks & Rec | 5th St, Defiance; MAP_VERIFICATION_FIND — 1 Maps review; pocket park |
| 31 | T6 | Site | Moats Park | Village of Sherwood | 210 Cedar St, Sherwood; MAP_VERIFICATION_FIND — not in web discovery; 37 Maps reviews |
| 32 | T7 | Site | Thoreau Wildlife Reserve | Diehl Family Foundation | 10485 Haller Rd, Defiance OH 43512; 250 ac; 4 unnamed trails 2 mi; public dawn-dusk; Audubon Sanctuary partner |
| 33 | T7 | Trail | Hicksville Nature Trail | Hicksville Trail Association | 1.8 mi loop; 9425 Casebeer Miller Rd, Hicksville; GOVERNANCE_UNCERTAIN |
| 34 | T8 | Site | Camp Lakota / Camp Neil Armstrong | Black Swamp Area Council BSA | 2180 Ginter Rd, Defiance OH 43512; 640 ac; Lake Glengary 48 ac; Auglaize River; est. 1941; member/group access |
| 35 | T8 | Site | Bark & Run Dog Park | Defiance Bark'n Runners (501c3) | 11795 Precision Way, Defiance OH 43512; 2 ac (two 1-ac areas); membership required; not city-affiliated |
| 36 | T8 | Site | Shallow Creek Hunting Preserve | private | 7599 Stever Rd, Defiance OH 43512; 40 ac; ODNR-licensed pheasant hunting; fee-based |

---

## Captured Source Data — GPS (§4.4 Map Verification Pass, 2026-04-20)

| Entity | GPS Lat | GPS Lon | Maps Name | Address |
|--------|---------|---------|-----------|---------|
| Fort Grounds | 41.2874974 | -84.3572446 | Fort Grounds | 320 Fort St |
| Diehl Park | 41.2982509 | -84.3674670 | Diehl Park | 833 Lake St |
| Kingsbury Riverfront Park | 41.2859503 | -84.3559868 | Kingsbury Park | 102 Auglaize St |
| Bronson Park | 41.2579920 | -84.3906290 | Bronson Park | 2104 Power Dam Rd |
| Eastside Park | 41.2724894 | -84.3535072 | Eastside Park | — |
| Riverside Park | 41.2768669 | -84.3616889 | Riverside Park | — |
| Reservoir and Disc Golf | 41.2707967 | -84.3920288 | Defiance City Reservoir | 1107–1149 Precision Way |
| Palmer Park | 41.2657975 | -84.3605872 | Palmer Park | 1634 Palmer Dr |
| William C. Holgate Park | 41.2833452 | -84.3732499 | Holgate Park | 829 OH-424 |
| Pontiac Metro Park | 41.2892403 | -84.3574256 | Pontiac Park | 9 E River Dr |
| Triangle Park | 41.2822475 | -84.3650681 | Triangle Park | Arabella St |
| Veteran's Memorial Park at Latty's Grove | 41.2794674 | -84.3673302 | Latty Grove Park (primary) | 606 Williams St |
| Splash Park | 41.2583791 | -84.3901891 | Defiance Splash Pad | 2104 Power Dam Rd |
| Canal Park | 41.2864106 | -84.3630635 | Amphitheater | 310 Clinton St |
| StoryWalk Trail | — | — | No standalone Maps entity | (trail program, no GPS) |
| Reservoir Nature Trail | 41.2690967 | -84.3993561 | Defiance Reservoir Nature Trail | 1261 Precision Way |
| Pontiac Metro Park Boat Launch | 41.2893480 | -84.3552717 | Pontiac Park Boat Ramp | E River Dr |
| Reservoir Boat Ramp and Dock | 41.2687580 | -84.3979906 | Defiance Reservoir Boat Launch | 1129 Precision Way |
| Buchman Park on the Glaize | 41.2836971 | -84.3563774 | Buchman Park on the Glaize | 314 Auglaize St |
| Memory Park | 41.2830331 | -84.3616312 | Memory Park | 5th St |
| Hicksville Community Park | 41.2966175 | -84.7727043 | Hicksville Park Pavilion | 598 N Bryan St |
| Froggy Park | 41.2970155 | -84.7687773 | Froggy Park | 547 N Main St |
| Hicksville Veterans Memorial | 41.2943616 | -84.7682625 | Hicksville Veterans Memorial | 200–220 W Arthur St |
| Little Reservation Station Park | 41.2896819 | -84.5525676 | Little Reservation Station Park | 405 N Harrison St |
| Ney Park | 41.3811614 | -84.5250569 | Ney Splash Pad | 370 W Main St |
| Moats Park | 41.2827831 | -84.5528207 | Moats Park | 210 Cedar St, Sherwood |

---

## Held Entities

None yet.

---

## Baseline Seed Audit (COMPLETE 2026-04-20)

41 unique seeds (Sheet1 ×39 + Sheet2 ×2). All resolved.

| # | Seed | Status | Entity / Resolution |
|---|------|--------|---------------------|
| 1 | Auglaize Hydro (NID) | EXCLUDED | Bryan Municipal Utilities, Williams County — not a Defiance County entity; same physical dam as Power Dam |
| 2 | Auglaize River WWT Lagoon (NID) | EXCLUDED | Wastewater treatment lagoon; no public access; no recreation role |
| 3 | Auglaize Village | CONFIRMED | T4 Site — DEF entity |
| 4 | Bark and Run Dog Park | CONFIRMED | T8 Site — DEF entity |
| 5 | Bronson Park | CONFIRMED | T6 Site — DEF entity |
| 6 | Camp Lakota (BSA) | CONFIRMED | T8 Site — DEF entity (2180 Ginter Rd, Defiance OH 43512) |
| 7 | Camp Lakota Boy Scout Lake Dam (NID) | RESOLVED | Dam infrastructure for Camp Lakota; no independent public access; noted in Camp Lakota identity_notes_raw; no separate entity |
| 8 | Canal Park | CONFIRMED | T6 Site — DEF entity |
| 9 | Defiance Upground Reservoir (NID) | RESOLVED | Dam/reservoir infrastructure within Reservoir and Disc Golf site; folded into T6 Site record |
| 10 | Diehl Park | CONFIRMED | T6 Site — DEF entity |
| 11 | Eastside Park / Compo Park | CONFIRMED | T6 Site — DEF entity (single entity "Eastside Park") |
| 12 | Fort Defiance Park | CONFIRMED | T6 Site — DEF entity (same as Fort Grounds; DEF-F-04 resolved) |
| 13 | Fort Grounds / Old Fort Defiance Park | CONFIRMED | T6 Site — DEF entity |
| 14 | Froggy Park (Hicksville) | CONFIRMED | T6 Site — DEF entity |
| 15 | General Motors Primary Lagoon (NID) | EXCLUDED | GM wastewater lagoon; no public access; no recreation role |
| 16 | General Motors Secondary Lagoon (NID) | EXCLUDED | GM wastewater lagoon; no public access; no recreation role |
| 17 | Hickory Lake Dam (NID, private) | EXCLUDED | Private dam; no public access documented in any source |
| 18 | Hicksville Community Park and Pool | CONFIRMED | T6 Site — DEF entity (includes Rotary Pavilion area) |
| 19 | Hicksville Veterans Memorial | CONFIRMED | T6 Site — DEF entity |
| 20 | Holgate Park / Second Ward Park | CONFIRMED | T6 Site — DEF entity ("William C. Holgate Park") |
| 21 | Hometown Heroes Park | CONFIRMED | T6 Site — DEF entity |
| 22 | Independence Dam (NID, state) | RESOLVED | ODNR dam; folded into Independence Dam State Park T2 Site record |
| 23 | Independence Dam State Park | CONFIRMED | T2 Site — DEF entity |
| 24 | Kettenring Hills Lake Dam (NID, private) | EXCLUDED | Private dam; no public access documented |
| 25 | Kingsbury Park | CONFIRMED | T6 Site — DEF entity ("Kingsbury Riverfront Park, Pool, and Pickleball Facilities"; DEF-F-01 resolved) |
| 26 | Oxbow Lake Dam (NID, state) | RESOLVED | ODNR dam; folded into Oxbow Lake Wildlife Area T2 Site record |
| 27 | Oxbow Lake Wildlife Area + western parcel | CONFIRMED | T2 Site — DEF entity (western parcel DEF-F-06 still unresolved) |
| 28 | Palmer Park | CONFIRMED | T6 Site — DEF entity |
| 29 | Penney Nature Center | CONFIRMED | T3 Site — DEF entity |
| 30 | Pontiac Metro Park | CONFIRMED | T6 Site — DEF entity (VERIFY_GOVERNANCE flag) |
| 31 | Power Dam | RESOLVED | Same physical dam as Auglaize Hydro; Bryan Municipal Utilities, Williams County; excluded |
| 32 | Reservoir and Disc Golf | CONFIRMED | T6 Site — DEF entity |
| 33 | Reservoir Nature Trail | CONFIRMED | T6 Trail — DEF entity (child of Reservoir and Disc Golf) |
| 34 | Riverside Park | CONFIRMED | T6 Site — DEF entity |
| 35 | Rotary Park (Hicksville) | RESOLVED | Rotary Pavilion is a feature/area within Hicksville Community Park (111 S Main St); village website describes one combined park; disc golf course informally called "Rotary Park"; no separate entity warranted |
| 36 | Splash Park | CONFIRMED | T6 Site — DEF entity (child of Bronson Park; DEF-F-07 resolved) |
| 37 | Triangle Park | CONFIRMED | T6 Site — DEF entity |
| 38 | Veterans Memorial Park at Latty's Grove | CONFIRMED | T6 Site — DEF entity |
| 39 | Winchester's Camp No. 3 / Fort Starvation | CONFIRMED | T2 child Site — DEF entity (inside Independence Dam SP) |
| 40 | City Center Park (Sheet2) | UNVERIFIED | Not on official cityofdefiance.com parks page; Sheet2 only; no authoritative source found; flag for pipeline review |
| 41 | Weisgerber-Pohlmann Nature Preserve (Sheet2) | WRONG_COUNTY | Black Swamp Conservancy; confirmed Williams County (Tiffin River corridor); NOT Defiance County; exclude from Defiance run |

---

## Open Questions (for Pipeline / Resolution phase)

1. ~~Does Defiance County have any formal park district?~~ RESOLVED — No county park district exists.
2. ~~Is "Pontiac Metro Park" a real managed site?~~ RESOLVED — Real site at 315 E River Rd; VERIFY_GOVERNANCE flag retained (city manages but website says "not city-owned").
3. ~~Are "Power Dam" and "Auglaize Hydro" the same structure?~~ RESOLVED — Same dam; Bryan Municipal Utilities, Williams County.
4. ~~Are "Fort Defiance Park" and "Fort Grounds" the same entity?~~ RESOLVED — Same entity; DEF-F-04 resolved.
5. What is the scope of the Oxbow Lake WA "western agreement parcel"? (DEF-F-06 — still unresolved; check ODNR Wildlife GIS layer)
6. ~~Does NCT route through Defiance County?~~ RESOLVED — Yes; Defiance city + Pontiac Park + Independence Dam SP.
7. ~~Are the three rivers designated water trails?~~ RESOLVED — Maumee = ODNR Water Trail (T2); Auglaize and Tiffin = no state designation.
8. What is the exact governance and land ownership for Pontiac Metro Park? (VERIFY_GOVERNANCE flag)
9. Does the Hicksville Trail Association hold fee-simple title or a management agreement for the Hicksville Nature Trail parcel? (GOVERNANCE_UNCERTAIN — verify county auditor parcel 9425 Casebeer Miller Rd)
10. ~~Does BSC hold Defiance County properties besides Weisgerber-Pohlmann?~~ RESOLVED — No confirmed Defiance County BSC holdings found.
11. Does Camp Lakota have any public-access components (e.g., day-use trails open to non-scouts)? Access policy affects tier assignment under T8 §4.1.
12. Does City of Defiance own the land at 11795 Precision Way where Bark & Run Dog Park is located? (Appears on city Facilities page despite "not affiliated with city" claim — affects tier assignment)
13. What are the individual trail names at Thoreau Wildlife Reserve? (4 unnamed trails documented; PDF map referenced on website but not publicly accessible)
14. Is "City Center Park" (Sheet2) a real entity? (Not on official parks page; no authoritative source found)

---

## Next Steps

1. ~~Tier 1~~ COMPLETE
2. ~~Tier 2~~ COMPLETE
3. ~~Tier 3~~ COMPLETE
4. ~~Tier 4~~ COMPLETE
5. ~~Tier 5 — Township~~ COMPLETE 2026-04-20 — 0 entities; 12 townships searched; all null with evidence
6. ~~Tier 6 — Municipal~~ COMPLETE 2026-04-20 — web discovery + §4.4 map verification for all 4 municipalities; 23 city + 6 village entities; GPS captured for all
7. ~~Tier 7 — Conservancy/Land Trust~~ COMPLETE 2026-04-20 — Thoreau Wildlife Reserve (Site) + Hicksville Nature Trail (Trail) staged.
8. ~~Tier 8 — Private~~ COMPLETE 2026-04-20 — Camp Lakota + Bark & Run Dog Park + Shallow Creek Hunting Preserve staged.
9. ~~Baseline seed audit~~ COMPLETE 2026-04-20 — all 41 seeds resolved (27 confirmed, 9 excluded, 3 resolved-as-infrastructure, 1 WRONG_COUNTY, 1 UNVERIFIED).
10. **Pipeline pass** (NEXT): resolution → normalization → GPS acquisition (supplement remaining blanks) → TSV output → DB upsert.

---

## Pre-Discovery Checklist

### Tier 1 — Federal & Tribal (COMPLETE 2026-04-20)
- [x] NPS Ohio state listing — https://www.nps.gov/state/oh/list.htm — confirmed North Country NST listed; no NPS land units in Defiance County
- [x] NPS NOCO page — https://www.nps.gov/noco/index.htm — NCT: NPS-administered, NCTA partner, 4,800 mi, 8 states
- [x] USFS / Wayne National Forest — https://www.fs.usda.gov/r09/wayne — confirmed SE Ohio only (Athens/Hocking/Perry etc.); NOT in Defiance County
- [x] USFWS refuge search NW Ohio — confirmed NW Ohio refuges are Cedar Point, Ottawa, West Sister Island (all Lucas/Ottawa Co.); none in Defiance County
- [x] BLM Northeastern States — https://www.blm.gov/office/northeastern-states — minimal Ohio surface holdings; none in Defiance County found
- [x] USACE Great Lakes & Ohio River Division — https://www.lrd.usace.army.mil/ — no USACE flood-control reservoir in Defiance County; NID dams in baseline are local/state/private owned
- [x] DoD MilitaryONESOURCE Ohio — confirmed no active DoD installation in Defiance County; historic Fort Defiance (1794) is NRHP-listed, now city park (Tier 5)
- [x] Tribal lands — BIA/search confirmed no federally recognized tribe holds land in Ohio
- [x] North Country NST routing — Buckeye Trail Defiance Section (northcountrytrail.org, buckeyetrail.org) — confirmed NCT passes through Defiance, Pontiac Park, Independence Dam SP

### Tier 2 — State (COMPLETE 2026-04-20)
Sources to check:
- [x] ODNR Parks — Independence Dam State Park — stateparks.com + ODNR campground page + Wikipedia — 591 ac, 27722 Co. Rd 424
- [x] ODNR Division of Wildlife — Oxbow Lake Wildlife Area — stateparks.com + ODNR map PDF — 416 ac; western parcel unresolved
- [x] ODNR Division of Forestry — confirmed NO state forest in Defiance County (Maumee State Forest = Fulton/Henry/Lucas)
- [x] ODNR Nature Preserves — confirmed NONE in Defiance County (Wikipedia list)
- [x] ODNR Scenic Rivers — Maumee State Scenic River confirmed (43 mi scenic + 53 mi recreational through Defiance Co.)
- [x] ODNR Water Trails / Maumee River Water Trail — Metroparks Toledo + ODNR, 107 mi, 39 access pts, through Defiance Co.
- [x] Auglaize River — no ODNR-designated water trail found; public access points documented
- [x] Tiffin River — no ODNR-designated water trail found; 2 informal launch sites documented
- [x] NID dams (partial) — Auglaize Hydro: Bryan Municipal Utilities, 23 ft, 1913; Independence Dam: ODNR, 11.8 ft, 1924; Oxbow Lake Dam: ODNR, 1953; remaining dams (Defiance Upground Reservoir, GM Lagoons, Hickory Lake, Kettenring Hills, Camp Lakota) deferred to Tier 4/5/8
- [x] Ohio Historic Sites — Winchester's Camp No. 3 (ODNR #24) confirmed inside Independence Dam SP; historical marker HMDB #37924
- [x] SHPO / NRHP — Fort Defiance site NRHP-listed 1980; now a city park (Tier 5). No standalone NRHP sites on state land.

### Tier 3 — District (COMPLETE 2026-04-20)
- [x] Defiance Soil and Water Conservation District — defianceswcd.org — Penney Nature Center (78 ac, 08855 Ashpacher Rd); 5 trails (3.5 mi); Storybook Trail named; 1 access point
- [x] No countywide park district exists — confirmed

### Tier 4 — County (COMPLETE 2026-04-20)
- [x] Defiance County Historical Society — auglaizevillage.org — Auglaize Village (120 ac, 12296 Krouse Rd); living history village; county-owned / DCHS-managed

### Tier 5 — Township (COMPLETE 2026-04-20 — 0 entities)
- [x] Read OTA roster (Townships_Officials2022-2023.xlsx), filter to Defiance County — 12 active townships confirmed (IMP-029 step 1)
- [x] Write full township list to Pre-Discovery Checklist below (IMP-029 step 2) — done before individual searches began
- [x] Defunct-candidate check per §5.5 — all 12 present in OTA roster; no defunct candidates
- [x] Individual search + page fetch for each of the 12 townships per §4.1–§4.5
- [x] Per-township outcome records written to YAML T5 section — all 12 COMPLETE / 0 parks each
- [x] Entity-type null documentation written to YAML for all 6 entity types at T5

**OTA Roster — Defiance County Active Townships (IMP-029 Pre-Discovery List)**
Source: Townships_Officials2022-2023.xlsx, sheet "Final Township Officials", filtered County Name = "Defiance"
All 12 townships confirmed active (present in OTA roster = active government). No defunct candidates.
OTA roster lists NO websites for any Defiance County township.
2026 Defiance County Township Directory PDF (defiance-county.com) confirms — contact info only, no parks listed for any township.
TrekOhio Defiance County page explicitly confirms: no township-owned or township-managed parks in county.

**Wrong-county websites discarded per §4.2a:** adamstwp.org (Butler Co PA), adamstwpoh.com (Seneca Co OH), milfordtownshipohio.org (Butler Co OH), richlandtownship.com (Michigan), delawaretownshipohio.org (Delaware Co OH)

| # | Township | 2020 Pop | Source Used | Outcome |
|---|----------|----------|-------------|---------|
| 1 | Adams | 884 | §4.1 search; directory PDF; no website | COMPLETE — 0 parks |
| 2 | Defiance | 13,216 | County-hosted page (defiance.php) fetched | COMPLETE — 0 parks |
| 3 | Delaware | 2,030 | §4.1 search; no verified website (Delaware Co site discarded) | COMPLETE — 0 parks |
| 4 | Farmer | 892 | §4.1 search; directory PDF; no website | COMPLETE — 0 parks |
| 5 | Hicksville | 4,872 | §4.1 search; no website (Village results only — T6) | COMPLETE — 0 township parks |
| 6 | Highland | 2,284 | §4.1 search; directory PDF; no website found | COMPLETE — 0 parks |
| 7 | Mark | 902 | §4.1 search; directory PDF; no website | COMPLETE — 0 parks |
| 8 | Milford | 1,120 | §4.1 search; milfordtownshipohio.org (Butler Co OH discarded) | COMPLETE — 0 parks |
| 9 | Noble | 5,909 | County-hosted page (noble.php) fetched | COMPLETE — 0 parks |
| 10 | Richland | 3,063 | richlandtownship.info fetched (Defiance Co confirmed); richlandtownship.com (MI discarded) | COMPLETE — 0 parks |
| 11 | Tiffin | 1,586 | §4.1 search; directory PDF; no website | COMPLETE — 0 parks |
| 12 | Washington | 1,528 | §4.1 search; washtownship@smta.cc; Ney OH confirmed Defiance Co | COMPLETE — 0 parks |

### Tier 6 — Municipal (COMPLETE 2026-04-20)
- [x] City of Defiance — web discovery complete (cityofdefiance.com + facilities pages)
- [x] City of Defiance — map verification (§4.4) COMPLETE 2026-04-20 — GPS captured for all 17 entities
- [x] Village of Hicksville — web discovery complete (villageofhicksville.com + chamber site)
- [x] Village of Hicksville — map verification (§4.4) COMPLETE 2026-04-20 — GPS captured
- [x] Village of Sherwood — web discovery complete (sherwoodohio.gov)
- [x] Village of Sherwood — map verification (§4.4) COMPLETE 2026-04-20 — GPS captured; Moats Park MAP_VERIFICATION_FIND
- [x] Village of Ney — web discovery complete (villageofney.com)
- [ ] Village of Ney — map verification (§4.4) PENDING/UNVERIFIED
- NOTE: Per IMP-015 multi-municipality ordering rule, run consolidated map verification pass after all web discovery is confirmed complete for all municipalities (already satisfied). Map verification pass is the remaining step.

### Tier 6 — Municipal — City of Defiance (web discovery COMPLETE 2026-04-20 — relabeled from erroneous T5)
- [x] cityofdefiance.com/216/Parks-Recreation — full parks list retrieved (17 entries)
- [x] cityofdefiance.com/231/City-Parks — additional descriptions
- [x] City facilities pages (/Facilities/Facility/Details/...) — individual park pages fetched
- [x] Fort Grounds (320 Fort St) — staged; DEF-F-04 resolved
- [x] Diehl Park (909 Wemor Dr, 39.77 ac) — staged
- [x] Kingsbury Riverfront Park, Pool, and Pickleball (102 Auglaize St, 15.49 ac) — staged; DEF-F-01 resolved
- [x] Bronson Park (2104 Power Dam Rd, 25 ac) — staged; parent of Splash Park + StoryWalk Trail
- [x] Splash Park (2104 Power Dam Rd) — staged as child of Bronson Park; DEF-F-07 resolved
- [x] Canal Park (310 Clinton St) — staged; Miami & Erie Lock No. 37 + amphitheater
- [x] Eastside Park / Compo Park (1185 Karnes Ave) — staged; single entity
- [x] Riverside Park (849 Riverside Ave, 30 ac) — staged
- [x] Reservoir and Disc Golf (1261 Precision Way) — staged; DEF-F-08 resolved; Buckeye Trail connection noted
- [x] Reservoir Nature Trail (1261 Precision Way) — staged as Trail child of Reservoir and Disc Golf
- [x] Palmer Park (1755 Palmer Dr) — staged; MINIMAL_DATA
- [x] Pontiac Metro Park (315 E River Rd) — staged; VERIFY_GOVERNANCE; NCT routes through; DEF-F-02 resolved
- [x] William C. Holgate Park (811 Holgate Ave) — staged
- [x] Hometown Heroes Park (648 Clinton St) — staged; est. September 2013; AMVETS Post 1991
- [x] Triangle Park (655 Clinton St) — staged; clock tower; MINIMAL_DATA
- [x] Veteran's Memorial Park at Latty's Grove (610 Williams St) — staged; est. 1937/1947
- [x] StoryWalk Trail (Bronson Park) — staged as Trail; Defiance Public Library program
- [x] Pontiac Metro Park Boat Launch — staged as Access Point
- [x] Reservoir Boat Ramp and Dock — staged as Access Point
- [x] Bark and Run Dog Park (11795 Precision Way) — DEFERRED to Tier 8; nonprofit membership required ("Defiance Bark'n Runners"); 2 ac; not a city park
- [x] City Center Park (Sheet2 only) — NOT on official city parks page; deferred pending verification
- [x] Defiance Upground Reservoir (NID) — resolves to dam infrastructure within Reservoir and Disc Golf site; no separate entity
- [x] Auglaize Hydro / Power Dam — Bryan Municipal Utilities (Williams County); deferred to Tier 8

### Tier 7 — Conservancy & Land Trust (COMPLETE 2026-04-20)

**Organizations searched (IMP-029 entity list — written before individual page fetches):**
1. Black Swamp Conservancy (blackswamp.org) — Weisgerber-Pohlmann Nature Preserve + any other Defiance County holdings
2. Thoreau Wildlife Reserve (thoreauwildlifereserve.org) — Diehl Family Foundation
3. The Nature Conservancy — Ohio chapter
4. Hicksville Trail Association (Hicksville Nature Trail, 9425 Casebeer Miller Rd)
5. Forder Bridge River Access Site (Black Swamp Conservancy)
6. ONAPA preserve map — cross-check

**Discovery outcomes:**
- [x] Black Swamp Conservancy — `blackswamp.org/properties/land-we-own/` fetched — 16 properties listed; **Weisgerber-Pohlmann = Williams County** (WRONG_COUNTY, not Defiance); **Forder Bridge = Paulding County** (WRONG_COUNTY, not Defiance); no confirmed Defiance County BSC properties found
- [x] Thoreau Wildlife Reserve — `thoreauwildlifereserve.org` fetched — **CONFIRMED Defiance County** (10485 Haller Rd, 43512); 250 ac; Diehl Family Foundation; 4 unnamed nature trails, 2 mi; public access dawn-dusk; Audubon Sanctuary partner → **T7 Site entity staged**
- [x] Hicksville Trail Association — visitdefianceohio.com + Facebook search — Hicksville Nature Trail, 1.8 mi loop, 9425 Casebeer Miller Rd; governance uncertain (no confirmed nonprofit status, no land ownership confirmed) → **T7 Trail staged with GOVERNANCE_UNCERTAIN flag**
- [x] The Nature Conservancy Ohio — `nature.org/en-us/ohio/places-we-protect/` fetched — **no Defiance County preserves** (closest is Kitty Todd, Lucas Co.)
- [x] ONAPA preserve map — `onapa.org/preserve-map.html` fetched — page redirects to ODNR; no Defiance County preserves independently identified
- [x] BSC "land we protect" (easements) — searched; county list confirms Defiance in service area but no specific Defiance County easement sites found with public access
- [x] Weisgerber-Pohlmann confirmed WRONG_COUNTY (Williams County) — not staged as Defiance entity
- [x] Forder Bridge confirmed WRONG_COUNTY (Paulding County) — not staged as Defiance entity

### Tier 8 — Private (COMPLETE 2026-04-20)

**Private sites searched (IMP-029 entity list — written before individual page fetches):**
1. Camp Lakota / Camp Neil Armstrong (Black Swamp Area Council BSA) — 2180 Ginter Rd, Defiance OH
2. Bark & Run Dog Park (Defiance Bark'n Runners 501c3) — 11795 Precision Way
3. Shallow Creek Hunting Preserve — 7599 Stever Rd, Defiance OH
4. NID dams: GM Primary Lagoon, GM Secondary Lagoon, Hickory Lake Dam, Kettenring Hills Lake Dam, Camp Lakota Boy Scout Lake Dam
5. Auglaize Hydro / Power Dam (Bryan Municipal Utilities, Williams County)

**Discovery outcomes:**
- [x] Camp Lakota — `blackswampbsa.org/camping/camp-lakota/` fetched — **CONFIRMED Defiance County** (2180 Ginter Rd, 43512); 640 ac; Black Swamp Area Council BSA; Lake Glengary 48 ac; Auglaize River border; est. 1941 → **T8 Site entity staged**
- [x] Bark & Run Dog Park — `defiancebarkandrun.com` fetched — **CONFIRMED Defiance County** (11795 Precision Way, 43512); 501c3 Defiance Bark'n Runners; "not affiliated with city"; membership required; 2 one-acre fenced areas → **T8 Site entity staged**
- [x] Shallow Creek Hunting Preserve — search confirmed (7599 Stever Rd, Defiance OH); 40-ac grassland; pheasant hunting; ODNR licensed → **T8 Site entity staged**
- [x] GM Primary/Secondary Lagoons — wastewater treatment infrastructure; no public access; no recreation role → **EXCLUDED** (not identity-bearing recreation sites)
- [x] Hickory Lake Dam — NID dam, private; no public access documented in any source → **EXCLUDED** (private pond, no public access)
- [x] Kettenring Hills Lake Dam — NID dam, private; no public access documented → **EXCLUDED** (private pond, no public access)
- [x] Camp Lakota Boy Scout Lake Dam — NID dam; associated infrastructure of Camp Lakota; no separate identity → noted in Camp Lakota identity_notes_raw; no separate entity
- [x] Auglaize Hydro / Power Dam — Bryan Municipal Utilities, Williams County; NOT a Defiance County entity → **EXCLUDED from Defiance County run**

---

## Captured Source Data

### Tier 1 — NPS Ohio Units (fetched 2026-04-20)
Source: https://www.nps.gov/state/oh/list.htm

| NPS Unit | Type | Location | Notes |
|----------|------|----------|-------|
| Charles Young Buffalo Soldiers | National Monument | Xenia | Not in Defiance Co. |
| Cuyahoga Valley | National Park | Cleveland/Akron area | Not in Defiance Co. |
| Dayton Aviation Heritage | National Historical Park | Dayton | Not in Defiance Co. |
| First Ladies | National Historic Site | Canton | Not in Defiance Co. |
| Hopewell Culture | National Historical Park | Chillicothe | Not in Defiance Co. |
| James A Garfield | National Historic Site | Mentor | Not in Defiance Co. |
| Lewis & Clark | National Historic Trail | Multi-state | Not in Defiance Co. |
| **North Country** | **National Scenic Trail** | **Multi-state incl. Defiance Co.** | **→ Tier 1 Trail entity** |
| Perry's Victory & International Peace | Memorial | Put-in-Bay | Not in Defiance Co. |
| William Howard Taft | National Historic Site | Cincinnati | Not in Defiance Co. |

### Tier 1 — NCT Ohio Route Summary (fetched 2026-04-20)
Source: https://northcountrytrail.org/the-trail/ohio/, https://en.wikipedia.org/wiki/North_Country_Trail, https://buckeyetrail.org/sections/sections-map.php?section=defiance

- NCT total length: ~4,800 miles across 8 states (ND to VT)
- Ohio NCT: ~1,076 miles, ~90% shared with Buckeye Trail
- **Defiance County route**: enters Defiance city, follows sidewalk/streets, crosses Maumee River, east through Pontiac Park, on-road, through Independence Dam State Park (along Miami and Erie Canal towpath past Lock No. 13 ruins)
- "Defiance Section" (BTA designation): 55 miles across Paulding, Defiance, Henry, and Lucas Counties (Junction Pt. 1 to River Rd Pt. 20 where NCT goes north)
- NPS-administered; NCTA is managing partner; BTA co-routes in Ohio

---

## Cross-County Watch

| Entity | Other Counties | Status |
|--------|----------------|--------|
| Black Swamp Conservancy holdings | Multi-county (NW Ohio) | Discover Defiance holdings; flag any cross-county networks |
| Maumee River corridor | Henry (downstream), Paulding/Allen via Auglaize (upstream), Williams via Tiffin (upstream) | Watch for shared water trails / access points |
| Auglaize River corridor | Paulding, Putnam, Allen, Auglaize, Mercer | Same |
| Tiffin River corridor | Williams, Fulton | Same |
| North Country NST (if present) | Multi-state | Check route |
