# Lucas County, Ohio — Handoff Document
**RUN_ID:** `lucas_oh_2026_04_27`  
**PREFIX:** `LUC`  
**Last updated:** 2026-06-12 (Supplemental resolution — MRQs 168–172/175)
**Status:** PIPELINE COMPLETE — SUPPLEMENTAL RESOLUTION APPLIED 2026-06-12

This document is the durable record across context breaks. Update before every session end.

---

## Batch Resolution Summary — 2026-06-10
Source: Quality review 2026-06-08; see `lucas_oh_batch_resolution_2026_06_10.md` for full detail.

- **+3 site_networks inserted:** OH-LUC-SN-0001 Metroparks Toledo (23 members, Fulton;Lucas;Ottawa;Wood), OH-LUC-SN-0002 Sylvania AJRD (4 members, counties fixed "Lucas, Ohio"→"Lucas"), OH-LUC-SN-0003 Olander Park System (6 members, Lucas)
- **+1 MC trail_segment:** OH-MC-TS-0007 WCT North Fork (parent OH-MC-T-0221, Fulton;Henry;Lucas;Williams)
- **+11 supplemental sites:** S-0234–S-0244 (Keil Farm 165ac, Devilbliss BSA 153ac, Lucas Co Rec Center 108ac, International Park 77ac, Riverfront North 63ac, Rogers Park 41ac, Harroun Park 28ac, Jackman Park 12ac, Hawthorne Hills 10ac, Horseshoe Island 10ac, Imperial Woods 2ac) — all confirmed Lucas FIPS 095 via TIGER spatial audit; GPS from PAD-US 4.0
- **+48 trail_parents:** OH-LUC-T-0012 through T-0083 (48 of 51 unmapped trails); 4 trails MRQ'd
- **Howard Farms identity resolved:** PAD-US "Howard Farms Land Acquisition" (987ac, lat=41.6482, lon=-83.2659) = OH-MC-S-0021 Howard Marsh Metropark — same entity, different name. No insert needed.
- **6 Wood County false positives documented:** WPA 44, Cedar Creeks Preserve, Orleans/Rivercrest/Woodlands Parks, Buttonwood/Betty C. Black — all confirmed Wood County (FIPS 173); MRQ-flagged for future Wood County run
- **Final counts:** 236 LUC sites | 3 site_networks | 55 LUC trail_parents | 4 MC trail_segments

## Supplemental Resolution — 2026-06-12

### MRQs 168–172/175 Resolved
- ~~MRQ 168 T-0011 WCT Connector~~ → trail_parent inserted: OH-LUC-T-0011 → OH-LUC-S-0029 (Side Cut Metropark). Identity_notes confirmed "Park: Side Cut Metropark." ✓
- ~~MRQ 169 T-0078 Anthony Wayne Trail~~ → No natural area site parent. Urban greenway corridor (status=Undeveloped per GIS); no natural area boundary encompasses it. MRQ closed. ✓
- ~~MRQ 170 T-0080 Salamander Flats~~ → trail_parent inserted: OH-LUC-T-0080 → OH-LUC-S-0228 (Kitty Todd Nature Preserve). Confirmed via T7 handoff entity list. ✓
- ~~MRQ 171 T-0081 Sandhill Crane~~ → trail_parent inserted: OH-LUC-T-0081 → OH-LUC-S-0228 (Kitty Todd Nature Preserve). Confirmed via T7 handoff entity list. ✓
- ~~MRQ 172 Wood County false positives~~ → 5 of 6 already in Wood DB: Buttonwood=WOD-S-0022, Cedar Creeks=WOD-S-0024, Orleans=WOD-S-0053, Rivercrest=WOD-S-0056, Woodland Park=WOD-S-0058 (acres updated to 42). WPA 44 (64ac, Lake Twp) not in Wood DB → MRQ 193 created for Wood County T1 supplemental. ✓
- ~~MRQ 175 Grand Rapids Access (LUC-F-07)~~ → Entity was never inserted in Lucas DB (correctly excluded at batch resolution). Grand Rapids is a Wood County village; Grand Rapids Park = OH-WOD-S-0071. LUC-F-07 fully closed. ✓

### Remaining Open Items
- S-0234 Keil Farm: access status "Unknown" per PAD-US — verify before finalizing
- LUC-F-09 Lucas County Recreation Ramp: identity vs S-0190 unclear
- LUC-F-03/04/05: GNIS marsh features — verify managed status at next review
- MRQ 193: WPA 44 (64ac, Lake Twp, Wood County) — staged for Wood County T1 supplemental run

---

## Open Items (post-batch)

---

## Tiers Completed

| Tier | Source Type | Entities Found | Notes |
|------|-------------|----------------|-------|
| T1 | Federal / USFWS / NPS | 2 Sites, 1 Access Point | Cedar Point NWR (~2,500 ac, fishing/paddling access May-Aug); West Sister Island NWR (82 ac, Wilderness, CLOSED). NPS: 10 OH units, none in Lucas Co. NCNST does not route through Lucas Co. USACE: no flood-control project in Lucas Co. All null entity types documented with evidence. |
| T2 | State — ODNR Parks, DNAP, DOW; OHC; OTIC; §4.7 | 11 Sites, 8 Trails, 4 APs | Maumee Bay SP; Irwin Prairie SNP; Campbell SNP; Kitty Todd SNP (TNC-governed → T7, T2 record notes ODNR designation only); Mallard Club WA; Metzger Marsh WA; Meilke Road Savanna WA; Lanker WA (new, not in baseline); Magee Marsh WA (GIS_VERIFY_COUNTY; primary=Ottawa); Missionary Island WA; Van Tassel WA (GIS_VERIFY_COUNTY). Trails/APs at Maumee Bay SP, Irwin Prairie, Campbell SNP, Metzger Marsh, Magee Marsh. Trail Segments/Trail Networks/Site Networks: NULL. Fallen Timbers BMP → T3; Audubon Islands SNP → T3; Maumee River Water Trail → T3 per §4.6. Open flags: ODOT rest areas (JS-rendered), ODNR Scenic Rivers, Stranahan Arboretum (UT §4.7), ODNR Historic Places, ODNR New Deal Era Sites. |
| T3 | District — Metropolitan Park District of the Toledo Area (Metroparks Toledo) | 23 Sites, 69 Trails, 2 Trail Segments, 1 Site Network, 13 APs | All 23 park properties staged (incl. Fallen Timbers, Audubon Islands, Oak Openings Preserve — major not-in-baseline discovery). 69 trails from listing page (7 regional/greenway + 62 intra-park). Wabash Cannonball North Fork (46 mi) + South Fork (17 mi) as Trail Segments. Metroparks Toledo Site Network (all 23 members; system map + unified membership). 13 APs: kayak launches (Farnsworth concession, Glass City Marina, Glass City Kayak Cove, Middlegrounds, Wiregrass Lake accessible launch, Fort Miamis kayak access, Bend View Water Trail, Blue Creek quarry, Cannonball Prairie pond, Kimble's Landing), trailheads (Oak Openings Beach Ridge, Springbrook, Buttonbush). Trail Networks: NULL with evidence. Howard Marsh county_primary = Ottawa (GIS_VERIFY_COUNTY); Providence county_primary = Wood (GIS_VERIFY_COUNTY). Wabash Cannonball multi-county (Lucas/Fulton/Williams/Henry). Lucas SWCD §4.7 check still pending. IMP-080 PASS. |

---

## Tiers Remaining

| Tier | Source Type | Entry Points |
|------|-------------|--------------|
| ~~T1~~ | ~~Federal / Tribal / OSM~~ | COMPLETE 2026-04-27 |
| ~~T2~~ | ~~State agency~~ | COMPLETE 2026-04-27 |
| ~~T3~~ | ~~District agency~~ | COMPLETE 2026-04-27 |
| ~~T4~~ | ~~County~~ | COMPLETE 2026-04-28 |
| ~~T5~~ | ~~Township~~ | COMPLETE 2026-04-28 |
| ~~T6~~ | ~~Municipal~~ | COMPLETE 2026-04-28 — 172 entities: Toledo (122 Sites+Trails, §5.13 batched), Oregon (8), Maumee (17), Waterville (7), Berkey (1), Harbor View (1), Holland (3), Ottawa Hills (7), Whitehouse (3). Swanton village: NULL. Source: NW_Ohio_Parks_View + NW_Ohio_Trails_View ArcGIS GIS layer. IMP-015 map verification COMPLETE 2026-04-28. GPS: 172/172 records. |
| ~~T7~~ | ~~Land trust / conservancy~~ | COMPLETE 2026-04-28 — 7 entities: Kitty Todd Nature Preserve (TNC, 1,464 ac) + 3 Trails + 3 APs. ACRES=NULL (no Lucas Co); ONAPA=NULL (links to ODNR); LTA=NULL (website 404); LCWT=NULL (not found); Ottawa NWR=NULL (all units in Ottawa Co). Howard Farms Conservancy District = T3 retro (2 Ottawa Wildlife Refuge parcels, GIS_VERIFY_COUNTY flagged). Trail Segment/Network/Site Network: NULL with evidence. IMP-080 PASS. |
| ~~T8~~ | ~~Private / other~~ | COMPLETE 2026-04-29 — 5 entities: Camp Miakonda (BSA, 160 ac, LUC-F-14 RESOLVED) + Miakonda Historical Trail (~2 mi) + Camp Miakonda Orienteering Trail; Agnes Reynolds Jackson Arboretum (Old West End Assoc., 1.66 ac — GOVERNANCE_REVIEW flag); River Tract (Owens Corning, 19.76 ac, public fitness trail). Toledo Zoo: OUT_OF_SCOPE (LUC-F-15 RESOLVED). Hunting preserves/church camps: NULL. |

---

## Key Active Flags

| Flag ID | Entity / Topic | Issue | Resolution Path |
|---------|----------------|-------|-----------------|
| ~~LUC-F-01~~ | ~~Kitty Todd~~ | **RESOLVED 2026-04-27** — Kitty Todd SNP is TNC-owned/managed land with an ODNR Nature Preserve designation overlaid. One entity; governance = TNC (T7). T2 raw record staged (notes ODNR SNP designation only); primary entity will be staged at T7. No duplicate entity needed. | CLOSED |
| ~~LUC-F-02~~ | ~~Fallen Timbers~~ | **RESOLVED 2026-04-27** — OHC page confirms Fallen Timbers Battlefield Memorial Park is "managed locally by the Metropolitan Park District of the Toledo area." OHC-listed but Metroparks-governed → T3. Not staged at T2. Will stage at T3 discovery. | CLOSED — stage at T3 |
| ~~LUC-F-16~~ | ~~ODOT Rest Areas in Lucas County~~ | **RESOLVED 2026-04-29** — NULL. ODOT rest areas page loaded via browser (transportation.ohio.gov/traveling/rest-areas); embedded JSON extracted listing all 82 Ohio rest areas — 0 entries with "Lucas" county prefix. I-75 rest areas are in Auglaize/Hancock/Butler/Miami counties only; I-80/I-90 Turnpike service plazas managed by OTIC (already confirmed NULL at T2). No ODOT rest areas in Lucas County. | CLOSED |
| ~~LUC-F-17~~ | ~~ODNR Scenic Rivers — Maumee River~~ | **RESOLVED 2026-04-29** — NULL for Lucas County. ODNR scenic rivers list loaded via browser (dx-stg.ohio.gov); Maumee River IS designated (Scenic+Recreational, July 18, 1974) but segment ends at US Route 25 bridge near Perrysburg (Wood County). Lucas County reach of the Maumee River is NOT within the designated scenic river segment. No new entity for Lucas County. Maumee River Water Trail already staged T3. | CLOSED |
| ~~LUC-F-18~~ | ~~University of Toledo Stranahan Arboretum (§4.7)~~ | **RESOLVED 2026-04-28** — Stranahan Arboretum at 4131 Tantara Rd, status=Open, agencyname=University of Toledo, 46 ac per NW_Ohio_Parks_View GIS. Staged retroactively at T2. | CLOSED |
| ~~LUC-F-19~~ | ~~ODNR Historic Places / New Deal Era Sites~~ | **RESOLVED 2026-04-29** — NULL for Lucas County. ODNR Historic Places page returns 404; checked via web search and Toledo Blade article. 5 iconic Toledo New Deal (WPA) structures all at Toledo Zoo (out of scope). WPA/CCC structures at Metroparks Toledo (Side Cut, Johlin Cabin at Oak Openings) are features within already-staged T3 parks. Maumee Bay SP opened 1975 — modern park, no CCC/WPA structures. Wildlife Areas/SNPs have no historic visitor structures. No ODNR Historic Places entities for Lucas County. | CLOSED |
| LUC-F-03 | Cedar Point Marsh | Baseline entry typed as "Area type 'Swamp' in GNIS" — likely a GNIS named feature, not a managed site; may overlap with or be adjacent to Cedar Point NWR | Verify at T1 whether this is a managed entity or just a GNIS geographic name |
| LUC-F-04 | Mallard Club Marsh | Baseline entry typed as "Area type 'Swamp' in GNIS" — same pattern as Cedar Point Marsh; may overlap with Mallard Club Wildlife Area | Verify at T1 / T2 — if purely a GNIS feature with no managed access, exclude |
| LUC-F-05 | Douglas Marsh, Pintail Marsh, Searles Marsh, Willow Point Marsh, Metzger Marsh (GNIS), Metzger Marsh WA | Multiple marsh GNIS entries; Metzger Marsh Wildlife Area (558 ac, ODNR) is a confirmed managed site; others need status check | Verify each at T1 — distinguish GNIS geographic names from managed public-access sites |
| ~~LUC-F-06~~ | ~~Glass City Riverwalk~~ | **RESOLVED 2026-04-28** — NW_Ohio_Parks GIS shows 2 parcels (1030 Water St and 1456 Summit St) with status=Undeveloped; agencyname=Metroparks Toledo. Not yet open. Not staged. | CLOSED |
| LUC-F-07 | Grand Rapids Access | Baseline has no type or management; described as "northeast of Grand Rapids, OH along St Rt 65" — Grand Rapids is in Wood County, not Lucas | Verify county assignment; likely a cross-county or Wood County entity — may be WRONG_COUNTY |
| ~~LUC-F-08~~ | ~~Olander Park~~ | **RESOLVED 2026-04-28** — "Milton Olander Park" at 6930 Sylvania Ave, 57 ac; governed by Olander Park System (Special District). Retroactively staged at T3 along with 5 other Olander properties (Site Network + 5 Sites). | CLOSED |
| LUC-F-09 | Lucas County Recreation Ramp | No type, management, or address in baseline — name suggests a boat ramp / access point | Identify governing body at T4; likely a Lucas County Parks asset |
| ~~LUC-F-10~~ | ~~Civic Center Mall~~ | **RESOLVED 2026-04-28** — status=Open, agencyname=City of Toledo per NW_Ohio_Parks_View GIS. Staged at T6. | CLOSED |
| LUC-F-11 | FitPark Ride | Listed as Toledo Metroparks; unusual name — may be a branded trail/facility within another metropark rather than a standalone site | Confirm entity type at T3 |
| LUC-F-12 | Cannaley Treehouse Village | Listed as Toledo Metroparks with no location; unique amenity name — may be a feature/child site within a larger metropark (Wildwood Preserve?) | Confirm at T3; determine if standalone site or child/feature |
| LUC-F-13 | Secret Forest | Listed as Toledo Metroparks; minimal baseline data | Confirm at T3 — may be a named feature within a larger metropark |
| ~~LUC-F-14~~ | ~~Camp Miakonda~~ | **RESOLVED 2026-04-29** — Scout camp (Erie Shores Council BSA), 160 ac, 5600 W Sylvania Ave, Toledo. Reservation-based access; facilities available to non-Scout groups. 2 named trails staged (Miakonda Historical Trail ~2 mi; Camp Miakonda Orienteering Trail). T8. | CLOSED |
| ~~LUC-F-15~~ | ~~Toledo Zoo~~ | **RESOLVED 2026-04-29** — OUT_OF_SCOPE. Toledo Zoological Society (nonprofit, 51 ac); animal exhibit facility; Wild Toledo = outreach program; no public nature trails accessible independent of zoo admission. Not staged. | CLOSED |

---

## Entities Discovered

| # | Tier | Type | Name | Governance | Notes |
|---|------|------|------|------------|-------|
| 1 | T1 | Site | Cedar Point National Wildlife Refuge | USFWS | ~2,500 ac; off Yondota Rd / SR-2, 3 mi E of Oregon OH; fishing/paddling access May 1–Aug 31; established 1964 (former hunt club); administered by Ottawa NWR staff |
| 2 | T1 | Site | West Sister Island National Wildlife Refuge | USFWS | 82 ac; Lake Erie Western Basin, 9 mi from shore; CLOSED — Wilderness Area since 1975; largest wading bird nesting colony in US Great Lakes; administered by Ottawa NWR staff |
| 3 | T1 | Access Point | Cedar Point NWR Fishing and Paddling Access | USFWS | Yondota Rd off SR-2; parking, shore fishing, non-motorized craft launch; open May 1–Aug 31 daylight hours |
| 4 | T2 | Site | Maumee Bay State Park | ODNR Parks | 1,336 ac (source); Lucas Co; SR-2 E of Oregon; campground, lodge, golf, beach, trails, birding |
| 5 | T2 | Site | Irwin Prairie State Nature Preserve | ODNR DNAP | 207 ac (source; baseline=226.47 ac — acreage discrepancy flagged); Lucas Co; rare wet prairie / fen complex |
| 6 | T2 | Site | Campbell State Nature Preserve | ODNR DNAP | Lucas Co; name differs from baseline "Louis W. Campbell SNP" — same entity confirmed |
| 7 | T2 | Site | Kitty Todd State Nature Preserve | ODNR DNAP / TNC | ODNR SNP designation on TNC-owned/managed land; governance = TNC → T7 primary entity; T2 record notes ODNR designation only |
| 8 | T2 | Site | Mallard Club Wildlife Area | ODNR DOW | 402 ac; Lucas Co |
| 9 | T2 | Site | Metzger Marsh Wildlife Area | ODNR DOW / USFWS cooperative | 558 ac; Lucas Co; cooperative management with USFWS Cedar Point NWR |
| 10 | T2 | Site | Meilke Road Savanna Wildlife Area | ODNR DOW | Lucas Co; acreage unconfirmed |
| 11 | T2 | Site | Lanker Wildlife Area | ODNR DOW | 26 ac; Lucas Co; NOT in baseline — new discovery via mandatory §3.3 hunting maps check |
| 12 | T2 | Site | Magee Marsh Wildlife Area | ODNR DOW | 2,202 ac; Lucas + Ottawa cos; GIS_VERIFY_COUNTY; county_primary=Ottawa (near Port Clinton / Oak Harbor) |
| 13 | T2 | Site | Missionary Island Wildlife Area | ODNR DOW | 297 ac; Lucas + Wood cos; county_primary=Lucas (2 mi SW of Waterville) |
| 14 | T2 | Site | Van Tassel Wildlife Area | ODNR DOW | 88 ac; Wood + Lucas cos; GIS_VERIFY_COUNTY |
| 15 | T2 | Trail | Paved Bike Trail | ODNR Parks (Maumee Bay SP) | Maumee Bay SP; paved multi-use |
| 16 | T2 | Trail | Interpretive Boardwalk | ODNR Parks (Maumee Bay SP) | Maumee Bay SP; 2 mi, ADA accessible |
| 17 | T2 | Trail | Mouse Trail | ODNR Parks (Maumee Bay SP) | Maumee Bay SP; 2.5 mi |
| 18 | T2 | Trail | Multi-use Trail | ODNR Parks (Maumee Bay SP) | Maumee Bay SP |
| 19 | T2 | Trail | Storybook Trail | ODNR Parks (Maumee Bay SP) | Maumee Bay SP; 0.3 mi |
| 20 | T2 | Trail | Irwin Prairie Boardwalk | ODNR DNAP | Irwin Prairie SNP; 1.25 mi, ADA loop |
| 21 | T2 | Trail | Campbell SNP Trail System | ODNR DNAP | Campbell SNP; 2.3 mi total |
| 22 | T2 | Trail | Magee Marsh Boardwalk | ODNR DOW | Magee Marsh WA; accessible boardwalk |
| 23 | T2 | Access Point | Maumee Bay State Park Main Access and Marina | ODNR Parks | Maumee Bay SP; main vehicle entry, marina, parking |
| 24 | T2 | Access Point | Metzger Marsh Boat Ramp and Channel | ODNR DOW | Metzger Marsh WA; motorized boat access |
| 25 | T2 | Access Point | Metzger Marsh Fishing Pier | ODNR DOW | Metzger Marsh WA; accessible fishing pier |
| 26 | T2 | Access Point | Magee Marsh Turtle Creek Fishing Access | ODNR DOW | Magee Marsh WA; Turtle Creek channel access |
| 27–49 | T3 | Site (23) | Bend View, Blue Creek, Blue Creek Connector, Brookwood SUA, Cannaley Treehouse Village, Cannonball Prairie, Fallen Timbers & Fort Miamis, Farnsworth, Glass City, Howard Marsh (GIS_VERIFY_COUNTY/Ottawa), Indian Creek, Irwin Prairie, Middlegrounds, Oak Openings Preserve, Oak Openings Beach Ridge Area, Oak Openings Springbrook, Old Mill, Pearson, Providence (GIS_VERIFY_COUNTY/Wood), Secor, Side Cut, Swan Creek Preserve, Tarr, Toledo Botanical Garden, Westwinds, Wildwood Preserve, Wiregrass Lake | Metropolitan Park District of the Toledo Area | All Metroparks Toledo properties; several not in baseline (Oak Openings Preserve, Springbrook, Beach Ridge, Old Mill, Tarr, Brookwood) |
| 50–118 | T3 | Trail (69) | 7 regional/greenway (Towpath, Wabash Cannonball, WC Connector, University/Parks, Maumee River Water Trail, Oak Openings Corridor/Moseley, Swan Creek Connector) + 62 intra-park trails | Metropolitan Park District of the Toledo Area | Full data from listing page; regional trails from individual pages |
| 119–120 | T3 | Trail Segment (2) | Wabash Cannonball Trail — North Fork (46 mi, Maumee→Montpelier); Wabash Cannonball Trail — South Fork (17 mi, Maumee→Liberty Center) | Metropolitan Park District of the Toledo Area | Named forks with documented lengths; multi-county (Lucas/Fulton/Williams/Henry) |
| 121 | T3 | Site Network (1) | Metroparks Toledo | Metropolitan Park District of the Toledo Area | 23-park system; system-wide map + PDF brochure; "Become a Member" unified membership |
| 122–134 | T3 | Access Point (13) | Kimble's Landing (Providence); Farnsworth Kayak Concession; Glass City Marina; Glass City Kayak Cove; Middlegrounds Kayak Cove; Wiregrass Lake Accessible Kayak Launch; Fort Miamis Kayak Access (Corey St); Bend View Water Trail Access; Blue Creek Quarry Pond Kayak; Cannonball Prairie Pond Kayak; Oak Openings Beach Ridge Trailhead; Oak Openings Springbrook Trailhead; Oak Openings Buttonbush Trailhead | Metropolitan Park District of the Toledo Area | Mix of water launches, named trailheads, and water trail accesses |
| 135 | T4 | Site (1) | Cooley Canal Boat Ramps | Lucas County Recreation Dept | Jerusalem Township, Lake Erie; free public boat ramps; boats ≤24 ft / 14-ft beam; likely = baseline LUC-F-09 "Lucas County Recreation Ramp" |
| 136–140 | T3 (retro) | Site Network (1) + Sites (4) | Sylvania Area Joint Recreation District (Site Network); Burnham Park (3.2 ac); Centennial Quarry (spring-fed swim quarry); Pacesetter Park (138 ac, 1.5-mi walk path); Veterans Memorial Park (36 ac) | Sylvania Area Joint Recreation District | ORC 755.14 statutory joint rec district. Retroactively staged at T3 after discovery during T5 (Sylvania Township) investigation. Governance = 12-member SAJRD Board (City of Sylvania 4, Sylvania Twp 4, Sylvania Schools 4). |
| 141–143 | T5 | Sites (3) | Shoreland Park (Washington Twp; 5470 Patriot Dr, Toledo); Monclova Community Park (Monclova Twp; 4335 Albon Rd); Keener Park (Monclova Twp; 4620 Keener Rd) | Washington Township; Monclova Township | Shoreland Park: MINIMAL_DATA. Keener Park adjacent to Wabash Cannonball Rails-to-Trails (T3). Springfield Twp website inaccessible (UNVERIFIED). Adams/Watkins Twps confirmed defunct. |
| 144–265 | T6 | Sites (122) | Toledo municipal parks — Batch 1 (Asbury Park → Promenade Park, parks 1–97) + Batch 2 (Ravine Park I → Yondota Park, parks 98–122). Source: NW_Ohio_Parks_View GIS (agencyname=City of Toledo; status=Open). Includes Civic Center Mall (LUC-F-10 RESOLVED). | City of Toledo | §5.13 batching applied. Toledo Zoo (LUC-F-15) not in GIS; scope assessment deferred to T8. Anthony Wayne Trail and Chessie Circle Trail staged as T6 Trails (see #267–268). |
| 266–271 | T6 | Sites (6) | Clegg Park, Groff Park, Maumee Bay Estates Park, Orchards Park, Oxford Park, Pearce Park | City of Oregon | oregonohio.org + NW_Ohio_Parks_View GIS |
| 272–274 | T6 | Sites (3) | Harroun Park; park(s) in City of Sylvania (GIS-confirmed open; Olander properties excluded → T3) | City of Sylvania | Olander Park System confirmed T3 Special District (LUC-F-08 RESOLVED); Sylvania SAJRD parks = T3 |
| 275–288 | T6 | Sites (14) | Maumee parks including Fallen Timbers Park, Oakwood Park, River Road Park, etc. | City of Maumee | NW_Ohio_Parks_View GIS; agencyname=City of Maumee |
| 289–293 | T6 | Sites (5) | Waterville parks (GIS-confirmed) | City of Waterville | NW_Ohio_Parks_View GIS |
| 294 | T6 | Site (1) | Berkey Village Park | Village of Berkey | NW_Ohio_Parks_View GIS |
| 295 | T6 | Site (1) | Harbor View Park | Village of Harbor View | NW_Ohio_Parks_View GIS |
| 296–297 | T6 | Sites (2) | Holland parks | Village of Holland | NW_Ohio_Parks_View GIS |
| 298–303 | T6 | Sites (6) | Ottawa Hills parks | Village of Ottawa Hills | NW_Ohio_Parks_View GIS |
| 304–306 | T6 | Sites (3) | Whitehouse parks | Village of Whitehouse | NW_Ohio_Parks_View GIS |
| 307–308 | T6 | Trails (2) | Anthony Wayne Trail (Toledo); Chessie Circle Trail (Toledo) | City of Toledo | NW_Ohio_Trails_View GIS; staged as Trail entities |
| 309–316 | T6 | Trails (8) | Oregon, Maumee, Waterville, Ottawa Hills municipal trails | Various municipalities | NW_Ohio_Trails_View GIS |
| 317–322 | T6 | Access Points (6) | Municipal boat launches and trailheads (Toledo, Oregon, Maumee area) | Various municipalities | NW_Ohio_Parks_View GIS |
| 335–341 | T7 | Site (1) + Trails (3) + APs (3) | Kitty Todd Nature Preserve (TNC, 1,464 ac, 10420 Old State Line Rd, Holland OH); Oak Savanna and Cactus Loop Trail; Salamander Flats Wetland Trail (0.75 mi); Sandhill Crane Wetland Viewing Area (300 ft); Main Trailhead/Parking (10420 Old State Line Rd); Salamander Flats Trailhead; Sandhill Crane Trailhead | The Nature Conservancy | Partner: ODNR (SNP designation), Green Ribbon Initiative. GPS: main site from GIS centroid (41.6176, -83.8027); main trailhead from GIS small parcel (41.6288, -83.7963). Trail GPS pending acquisition pass. |
| 342–343 | T3 retro | Sites (2) | Ottawa Wildlife Refuge (2 parcels, ~1 ac each, citymuni=Curtice) | Howard Farms Conservancy District | ORC 6101 statutory drainage district (ownertype=Special District); GIS_VERIFY_COUNTY flagged — centroids show lon=-83.24 (Ottawa Co area, not expected ~-83.40 for Curtice Lucas Co); GPS nullified pending verification. |
| 344–348 | T8 | 3 Sites + 2 Trails | Camp Miakonda (BSA/Erie Shores Council, 160 ac, 5600 W Sylvania Ave, Toledo); Miakonda Historical Trail (~2 mi, reservation required); Camp Miakonda Orienteering Trail (compass course, ~1 hr); Agnes Reynolds Jackson Arboretum (Old West End Association, 1.66 ac, 2501 Robinwood Ave, Toledo — GOVERNANCE_REVIEW); River Tract (Owens Corning, 19.76 ac, Maumee River frontage, public fitness trail) | BSA/Erie Shores Council; Old West End Association; Owens Corning | LUC-F-14 RESOLVED (Camp Miakonda); LUC-F-15 RESOLVED (Toledo Zoo = OUT_OF_SCOPE). GPS from GIS centroids for Camp Miakonda, Agnes, River Tract. |
| 323–334 | T6 retro / T1 retro | Sites (12) | T1 retroactive: Grassy Island (USACE, 2 ac; Maumee River); T2 retroactive: Maumee State Forest (ODNR-Forest); T3 retroactive: Olander Park System Site Network + 5 Olander Sites (Milton Olander Park 57 ac, + 4 others at 6930 Sylvania Ave area); T5 retroactive: Jerusalem Township parks (GIS-confirmed; missed T5 web); Springfield Twp parks (GIS UNVERIFIED status confirmed) | USACE; ODNR-Forest; Olander Park System; Jerusalem/Springfield Townships | Retroactive corrections from NW_Ohio_Parks_View GIS cross-check. LUC-F-08 RESOLVED (Olander=T3 Special District). Stranahan Arboretum (UT, 46 ac, 4131 Tantara Rd) staged retroactively at T2 (LUC-F-18 RESOLVED). |

---

## Held Entities

| # | Name | Hold Reason | Resolution Path |
|---|------|-------------|-----------------|
| — | — | — | — |

---

## Unresolved Baseline Seeds

All 114 baseline seeds from Sheet1 are unconfirmed. Key seeds to watch during discovery:

**Federal (T1):** ✓ CONFIRMED
- ~~Cedar Point National Wildlife Refuge~~ — CONFIRMED T1 (USFWS, ~2,500 ac)
- ~~West Sister Island National Wildlife Refuge~~ — CONFIRMED T1 (USFWS, 82 ac, CLOSED/Wilderness)
- Cedar Point Marsh (GNIS — not a managed entity; verify at T1 OSM or note as geographic feature only — see LUC-F-03)

**State (T2):** ✓ CONFIRMED / REASSIGNED
- ~~Audubon Islands State Nature Preserve (170 ac)~~ — ODNR SNP designation; **governance = Toledo Metroparks → T3**
- ~~Irwin Prairie State Nature Preserve (226.47 ac)~~ — CONFIRMED T2 (acreage discrepancy: source says 207 ac vs baseline 226.47 ac — note for normalization)
- ~~Kitty Todd State Nature Preserve (615.77 ac)~~ — CONFIRMED T2 ODNR record; **primary governance = TNC → T7**
- ~~Louis W. Campbell State Nature Preserve (210.09 ac)~~ — CONFIRMED T2 as "Campbell State Nature Preserve" (name discrepancy minor)
- ~~Maumee Bay State Park (1,436 ac)~~ — CONFIRMED T2 (source says 1,336 ac; acreage note for normalization)
- ~~Mallard Club Wildlife Area (402 ac)~~ — CONFIRMED T2
- ~~Metzger Marsh Wildlife Area (558 ac)~~ — CONFIRMED T2
- ~~Meilke Road Savanna Wildlife Area~~ — CONFIRMED T2
- ~~Fallen Timbers Battlefield Memorial Park (Ohio History Connection)~~ — OHC-listed; **governance = Toledo Metroparks → T3**
- Lanker Wildlife Area — NEW (not in baseline); CONFIRMED T2 (26 ac)
- Magee Marsh Wildlife Area — NEW (not in baseline); CONFIRMED T2 (2,202 ac; GIS_VERIFY_COUNTY; primary=Ottawa)
- Missionary Island Wildlife Area — NEW (not in baseline); CONFIRMED T2 (297 ac; Lucas primary)
- Van Tassel Wildlife Area — NEW (not in baseline); CONFIRMED T2 (88 ac; GIS_VERIFY_COUNTY)

**District / Toledo Metroparks (T3):** ✓ ALL CONFIRMED 2026-04-27
- ~~Bend View Metropark~~ — CONFIRMED T3
- ~~Blue Creek Metropark (678 ac)~~ — CONFIRMED T3 (Blue Creek + Blue Creek Connector both staged)
- ~~Cannaley Treehouse Village~~ — CONFIRMED T3 as standalone site (Wildwood Preserve child; own page)
- ~~Cannonball Prairie Metropark (89 ac)~~ — CONFIRMED T3
- ~~Fallen Timbers Battlefield Metropark & Fort Miamis State Memorial (204 ac)~~ — CONFIRMED T3 (LUC-F-02 RESOLVED)
- ~~Farnsworth Metropark~~ — CONFIRMED T3
- ~~FitPark Ride~~ — NOT staged as Site; feature/facility under Features & Rentals; no standalone acreage or governance; treated as trail feature (LUC-F-11 RESOLVED — not a site entity)
- ~~Glass City Metropark (66 ac)~~ — CONFIRMED T3
- ~~Glass City Riverwalk~~ — LUC-F-06 still open (open status unclear from source)
- ~~Howard Marsh Metropark (995 ac)~~ — CONFIRMED T3 (GIS_VERIFY_COUNTY; likely Ottawa Co primary)
- ~~Manhattan Marsh Preserve Metropark (57 ac)~~ — CONFIRMED T3 (staged as "Indian Creek Metropark" — verify identity at normalization)
- ~~Middlegrounds Metropark (28 ac)~~ — CONFIRMED T3
- Oak Openings Preserve Metropark — CONFIRMED T3 (⚠️ NOT IN BASELINE — major new discovery)
- Oak Openings Beach Ridge Area — CONFIRMED T3 (⚠️ NOT IN BASELINE)
- Oak Openings Springbrook Metropark — CONFIRMED T3 (⚠️ NOT IN BASELINE — Springbrook sub-unit)
- ~~Pearson Metropark (627 ac)~~ — CONFIRMED T3
- ~~Providence Metropark~~ — CONFIRMED T3 (GIS_VERIFY_COUNTY; likely Wood Co primary)
- ~~Secor Metropark (837 ac)~~ — CONFIRMED T3
- ~~Secret Forest~~ — RESOLVED: children's discovery area at Toledo Botanical Garden; not staged as standalone site (LUC-F-13 RESOLVED)
- ~~Side Cut Metropark (323 ac)~~ — CONFIRMED T3
- ~~Swan Creek Preserve Metropark (451 ac)~~ — CONFIRMED T3
- ~~Toledo Botanical Garden (60 ac)~~ — CONFIRMED T3
- ~~Westwinds Metropark (174 ac)~~ — CONFIRMED T3
- ~~Wildwood Preserve Metropark (493 ac)~~ — CONFIRMED T3
- ~~Wiregrass Lake Metropark (51 ac)~~ — CONFIRMED T3
- Brookwood Special Use Area — STAGED T3 (⚠️ NOT IN BASELINE)
- Tarr Metropark — STAGED T3 (⚠️ NOT IN BASELINE)
- Old Mill Metropark — STAGED T3 (⚠️ NOT IN BASELINE)

**Land Trust / Conservancy (T7):**
- Kitty Todd Nature Preserve (TNC, 1,400 ac)

**Private (T8):**
- Camp Miakonda (BSA, Erie Shores Council)
- Toledo Zoo

**City of Toledo parks (T6 — large list; 70+ entries in baseline):**
Asbury Park, Ashley Park, Bandore Park, Bay View Park, Beatty Park, Bennett Park, Beth Raudabusch Park, Beverly Park, Bicentennial Park, Birmingham Park, Boeschenstein Park, Bronson/T J Overton Park, Burroughs Park, Casey Jones Park, Cass Ryan Eastgate Park, Children's Park, Chorus Lane, Chub DeWolfe, Civic Center Mall (verify), Clinton Park, Close Park, Clover Lane Park, Clover Ridge Park, Collins Park, Copland Park, Corbin Park, Cuba Saturn Park, Cullen Park, Czelusta Park, Dale Stone Park, Danny Thomas Park, Delaware Creek, Delaware Park, DeLucia Park, Detwiler Park (200+ ac), Drummond Woods Park, Edgar Holmes Park, Elmhurst Park, Feeback Park, Fort Meigs Sertoma Park, Prentice Park, Promenade Park, Ravine Park I, Ravine Park II, Reverend H. V. Savage Park, River Road Park, Robinson Park, Romanoff Park, Schneider Soccer Park, Scott Park, Sleepy Hollow Park, Smith Park, Sterling Park, Thyer Park, Toledo Spain Plaza, Toledo Zoo (scope TBD), Trilby Park, Union Memorial, Walbridge Park, Washington Village Park, Waterbury Wet Woods, Wayne Snow Park, Westwood Park, Willys Park, Wilson Park, Winterfield Park, Woodsdale Park, Yondota Park

**Other / unclear governance:**
- Grand Rapids Access (LUC-F-07 — likely WRONG_COUNTY)
- Olander Park (LUC-F-08 — governance TBD)
- Lucas County Recreation Ramp (LUC-F-09 — likely T4)

---

## Open Questions

1. ~~Does Kitty Todd exist as two distinct entities (TNC parcel + ODNR parcel) or is it one site with dual management? (LUC-F-01)~~ — **RESOLVED**: One entity, TNC-governed (T7). ODNR SNP designation noted in T2 record.
2. ~~Is the Fallen Timbers historic site split into two entities under separate governance (Ohio History Connection vs. Toledo Metroparks), or is it one entity? (LUC-F-02)~~ — **RESOLVED**: OHC-listed memorial park managed by Toledo Metroparks → single entity staged at T3. Baseline has two entries; will consolidate at normalization.
3. Is Grand Rapids Access actually in Lucas County, or is it in Wood County? (LUC-F-07)
4. What is the complete list of Lucas County townships? (Confirm with authoritative source at T5)
5. ~~What is the complete list of municipalities in Lucas County?~~ — **RESOLVED 2026-04-28**: 5 cities (Toledo, Oregon, Sylvania, Maumee, Waterville) + 6 villages (Berkey, Harbor View, Holland, Ottawa Hills, Swanton‡, Whitehouse). Richfield Center = CDP only. See T6 Pre-Discovery Checklist.
6. Is Cannaley Treehouse Village a standalone metropark or a feature within Wildwood Preserve Metropark?
7. ~~Does Civic Center Mall still exist as a public park? (LUC-F-10)~~ — **RESOLVED 2026-04-28**: Confirmed active Open site per GIS; staged T6.
8. ~~Is the Glass City Riverwalk open yet, or still "coming soon"? (LUC-F-06)~~ — **RESOLVED 2026-04-28**: GIS shows status=Undeveloped (2 parcels); not staged.
9. Does the Toledo Metroparks system include any properties in adjacent counties (e.g., Wood, Ottawa) that would require cross-county network handling?
10. What is the full scope of the Maumee River Water Trail within Lucas County, and which access points does it include?

---

## Next Steps

1. ~~**T4 — Lucas County Parks & Recreation**~~ — COMPLETE 2026-04-28.
2. ~~**T3 residuals — Lucas SWCD §4.7 check**~~ — COMPLETE 2026-04-28.
3. ~~**T5 — Townships**~~ — COMPLETE 2026-04-28. 3 Sites (Shoreland, Monclova Comm. Park, Keener). SAJRD +5 retroactive T3. Springfield Twp UNVERIFIED (redirect). Adams/Watkins DEFUNCT.
4. ~~**T6 — Municipal**~~ — COMPLETE 2026-04-28. 172 entities (Sites, Trails, APs) across Toledo (§5.13 batched), Oregon, Sylvania, Maumee, Waterville, Berkey, Harbor View, Holland, Ottawa Hills, Whitehouse. Swanton=NULL. Source: NW_Ohio_Parks_View + NW_Ohio_Trails_View GIS. IMP-015 map verification COMPLETE. GPS: 172/172 records from GIS centroids.
5. ~~**T6 IMP-015 map verification pass**~~ — COMPLETE 2026-04-28. GPS centroids from NW_Ohio_Parks_View REST API; Maps spot-checks confirmed for Toledo, Maumee, Waterville, Ottawa Hills.
6. ~~**T7 — Land Trust / Conservancy**~~ — COMPLETE 2026-04-28. TNC Kitty Todd (1,464 ac, 10420 Old State Line Rd) + 3 Trails + 3 APs. LCWT not found. Howard Farms retro T3 (GIS_VERIFY_COUNTY). LEC/ACRES/LTA all null. 343 total records.
7. ~~**T8 — Private**~~ — COMPLETE 2026-04-29. 5 entities staged (3 Sites + 2 Trails). Toledo Zoo OUT_OF_SCOPE. Hunting preserves NULL. Church camps NULL. 348 total records.
8. ~~**Open flags LUC-F-16, -17, -19**~~ — ALL RESOLVED 2026-04-29. LUC-F-16: No ODOT rest areas in Lucas County (NULL). LUC-F-17: Maumee River scenic designation ends at Perrysburg/Wood County (NULL for Lucas Co). LUC-F-19: No ODNR Historic Places in Lucas County (NULL). All T2 sources now fully cleared.
9. ~~**T1 residual — Overpass sweep**~~ — COMPLETE 2026-04-29. 9 Overpass entities returned; all already staged; NO NEW ENTITIES. T1 fully complete.
10. ~~**Springfield Township (T5) UNVERIFIED**~~ — RESOLVED 2026-04-29. Correct website: springfieldtownship.net/departments/parks/. 4 parks confirmed (Community Homecoming Park, Lincoln Green Park, Carmella Gardens Park, Bear Creek Park); all already staged retroactively at T5 via GIS (indices 152–157 include 2 additional GIS-only parks: Florian Park, Springfield Athletic Complex). 4 site records enriched with description_raw, features_raw, acres_raw from website. **DISCOVERY COMPLETE — 348 records; all tiers and flags resolved.**

---

## Pre-Discovery Checklist — Tier 3 (District — Toledo Metroparks) — COMPLETE 2026-04-27

**Enumeration source**: metroparkstoledo.com homepage `/explore-your-parks/` links (fetched 2026-04-27).

### Metroparks Toledo — Full Property List
- [x] Bend View Metropark — STAGED
- [x] Blue Creek Metropark — STAGED (+ Blue Creek Connector)
- [x] Brookwood Special Use Area — STAGED (⚠️ NOT IN BASELINE)
- [x] Cannaley Treehouse Village — STAGED (LUC-F-12 RESOLVED: standalone site)
- [x] Cannonball Prairie Metropark — STAGED
- [x] Fallen Timbers Battlefield & Fort Miamis Metropark — STAGED (LUC-F-02 RESOLVED)
- [x] Farnsworth Metropark — STAGED
- [x] Glass City Metropark — STAGED
- [ ] Glass City Riverwalk — LUC-F-06 OPEN (open status unconfirmed; not staged)
- [x] Howard Marsh Metropark — STAGED (GIS_VERIFY_COUNTY; Ottawa primary)
- [x] Indian Creek Metropark (= Manhattan Marsh Preserve Metropark?) — STAGED; verify identity at normalization
- [x] Irwin Prairie Metropark — STAGED (= T2 Irwin Prairie SNP child or co-managed; noted in record)
- [x] Middlegrounds Metropark — STAGED
- [x] Oak Openings Preserve Metropark — STAGED (⚠️ NOT IN BASELINE — major discovery)
- [x] Oak Openings Beach Ridge Area — STAGED (⚠️ NOT IN BASELINE)
- [x] Oak Openings Springbrook Metropark — STAGED (⚠️ NOT IN BASELINE)
- [x] Old Mill Metropark — STAGED (⚠️ NOT IN BASELINE)
- [x] Pearson Metropark — STAGED
- [x] Providence Metropark — STAGED (GIS_VERIFY_COUNTY; Wood primary)
- [x] Secor Metropark — STAGED
- [x] Side Cut Metropark — STAGED
- [x] Swan Creek Preserve Metropark — STAGED
- [x] Tarr Metropark — STAGED (⚠️ NOT IN BASELINE)
- [x] Toledo Botanical Garden — STAGED
- [x] Westwinds Metropark — STAGED
- [x] Wildwood Preserve Metropark — STAGED
- [x] Wiregrass Lake Metropark — STAGED
- [x] FitPark Ride — LUC-F-11 RESOLVED: facility/feature under Features & Rentals; not a site entity
- [x] Audubon Islands SNP — staged as "Audubon Islands Metropark" (governance = Metroparks Toledo; ODNR SNP designation noted)
- [x] Secret Forest — LUC-F-13 RESOLVED: children's discovery area at Toledo Botanical Garden; not standalone
- [x] The Ribbon at Glass City Metropark — treated as amenity/feature within Glass City; not staged as standalone site

### Maumee River Water Trail (§4.6)
- [x] Management entity: Metroparks Toledo primary + multi-agency; Water Trail entity staged as T3 Trail (Maumee River Water Trail); 8 APs staged at T3

### Trails
- [x] 69 trails staged (7 regional/greenway from individual pages; 62 intra-park from listing page)

### Trail Networks
- [x] NULL with evidence documented — no named multi-trail network identity found

### Trail Segments
- [x] Wabash Cannonball North Fork (46 mi) and South Fork (17 mi) staged

### Site Network
- [x] Metroparks Toledo site network staged (23 member parks; system map; unified membership)

### Access Points
- [x] 13 APs staged (kayak launches, water trail accesses, named trailheads)

### Open / Deferred
- [x] Lucas County SWCD check (§4.7) — COMPLETE 2026-04-28; NULL with evidence. Lucas SWCD (lucasswcd.org) is a technical-assistance-only organization; no land holdings with public access found. Null staged in tier_3_null_results.

---

## Pre-Discovery Checklist — Tier 5 (Townships — Lucas County) — COMPLETE 2026-04-28

**OTA Active Township Roster cross-reference complete (§3.1a). 11 active townships confirmed.**
**Defunct candidates confirmed: Adams Twp (fully annexed to Toledo), Watkins Twp (absent from OTA roster + Lucas Co official list — no active govt)**

| # | Township | 2020 Pop | Website (OTA) | Status |
|---|----------|----------|---------------|--------|
| 1 | Harding | 726 | sites.google.com/view/hardingtownshiplucascountyohio (hardintwp.net DNS dead) | NULL — rural admin, no parks |
| 2 | Jerusalem | 2,895 | twp.jerusalem.oh.us | NULL — rec = youth sports only; outdoor parks are T1/T2 |
| 3 | Monclova | 14,827 | monclovatwp.org | ✓ 2 Sites (Community Park, Keener Park) |
| 4 | Providence | 3,378 | providencetwp.org | NULL — refs T3 parks only |
| 5 | Richfield | 1,575 | richfieldtwp.com | NULL — no park content found |
| 6 | Spencer | 1,746 | spencertownship.org | NULL — only industrial park hit |
| 7 | Springfield | 26,957 | springfieldtownship.net | ✓ VERIFIED 2026-04-29 — 6 parks in GIS (retroactive T5 staging: indices 152–157); 4 confirmed and enriched from official website (Community Homecoming Park 40 ac; Lincoln Green Park 3 ac; Carmella Gardens Park ~3 ac; Bear Creek Park). Florian Park + Springfield Athletic Complex GIS-only (not on parks page). Walking trail at Lincoln Green = unnamed park feature (not staged as Trail entity). No new entities needed. |
| 8 | Swanton | 2,822 | swantontwp.org | NULL — refs Oak Openings Metropark (T3) only |
| 9 | Sylvania | 50,679 | sylvaniatownship.com | NULL (twp-owned); SAJRD parks → T3 retroactive |
| 10 | Washington | 3,055 | washington-twp.com | ✓ 1 Site (Shoreland Park; MINIMAL_DATA) |
| 11 | Waterville | 7,036 | watervilletownship.com | NULL — refs Metroparks/Water Trail (T3) only |
| — | Adams | — | NOT IN OTA ROSTER | DEFUNCT — fully annexed to City of Toledo |
| — | Watkins | — | NOT IN OTA ROSTER | DEFUNCT — absent from OTA + Lucas Co official list; no active govt |

---

## Pre-Discovery Checklist — Tier 4 (County — Lucas County) — COMPLETE 2026-04-28

**Enumeration sources fetched:** co.lucas.oh.us/454/Recreation (dept page) + co.lucas.oh.us/603/Parks-Recreation (visitor page)

### County Recreation Department Subpages
- [x] Cooley Canal Boat Ramps (/468) — STAGED as Site T4; Jerusalem Township, Lake Erie; free public ramps; boats ≤24 ft / 14-ft beam. Likely = baseline "Lucas County Recreation Ramp" (LUC-F-09 RESOLVED)
- [x] Wabash Cannonball Bike Trail (/457) — cross-tier reference only; T3 (Metroparks Toledo) is canonical manager; county page confirms trail details but county is NOT manager; no new T4 record
- [x] Rec Center Complex (/472) — 2901 Key St, Maumee OH 43537; indoor rec halls, handball courts, walking trail; urban recreation facility; outside natural areas scope; NOT staged
- [x] Lucas County Fair (/469) — fairgrounds; NOT a natural area; NOT staged

### County Visitors / Parks & Recreation Subpages
- [x] Metroparks (/3109) — county info page about T3 Metroparks Toledo; no new entity
- [x] Toledo Botanical Garden (/3110) — already staged T3
- [x] Irwin Prairie State Nature Preserve (/3111) — already staged T2
- [x] Schedel Arboretum and Gardens (/3112) — 19255 W Portage River South Rd, Elmore OH 43416; WRONG COUNTY (Ottawa County); private arboretum; NOT staged at T4; flag for T7/T8 in Ottawa County run
- [x] Camping and Marinas (/3113) — all listed entities are private and mostly outside Lucas County (Stony Ridge KOA = Wood Co; Anchor Point, Meinke marinas = Ottawa Co; Twin Acres = Lucas Co private); no county-managed entities

### NRHP Check (§3.3)
- [x] NRHP Lucas County listings checked (Wikipedia list, complete through 2026-04-24)
- [x] Interurban Bridge (NR# 72001036, Waterville) — within/adjacent to Metroparks area; T3 captured; no new county entity
- [x] Sumner Street Bridge (NR# 100010713, Toledo 2024) — City of Toledo; T6
- [x] No covered bridges in Lucas County
- [x] Fort Miamis Site — within T3 Fallen Timbers Metropark; no new entity
- [x] Maumee Sidecut — within T3 Side Cut Metropark; no new entity
- [x] NULL: no county-managed NRHP natural features not already captured at other tiers

### Trails / Trail Networks / Site Networks / Access Points
- [x] No county-managed trails found (Wabash Cannonball = T3 canonical)
- [x] No county parks district with own branding/board → §4.5 Site Network does not apply
- [x] No named individual ramps at Cooley Canal → no T4 APs staged; facility staged as Site

---

## Pre-Discovery Checklist — Tier 2 (State) — COMPLETE 2026-04-27

### ODNR Parks
- [x] Maumee Bay State Park — CONFIRMED; 5 trails, 1 AP staged

### ODNR Nature Preserves
- [x] Irwin Prairie State Nature Preserve — CONFIRMED; 1 trail staged; acreage discrepancy noted
- [x] Audubon Islands State Nature Preserve — governance = Toledo Metroparks → T3; NOT staged T2
- [x] Kitty Todd State Nature Preserve — LUC-F-01 RESOLVED; governance = TNC → T7; T2 record staged (ODNR designation only)
- [x] Louis W. Campbell State Nature Preserve — CONFIRMED as "Campbell SNP"; 1 trail system staged

### Ohio History Connection
- [x] Fallen Timbers Battlefield Memorial Park — LUC-F-02 RESOLVED; governance = Toledo Metroparks → T3; NOT staged T2

### ODNR Division of Wildlife
- [x] Mallard Club Wildlife Area — CONFIRMED
- [x] Metzger Marsh Wildlife Area — CONFIRMED; 2 APs staged; USFWS cooperative management noted
- [x] Meilke Road Savanna Wildlife Area — CONFIRMED
- [x] Hunting Area Maps JSON — mandatory §3.3 check COMPLETE; 4 new WAs discovered (Lanker, Magee Marsh, Missionary Island, Van Tassel)
- [x] Magee Marsh Boardwalk trail staged; 1 AP staged

### ODNR Water Trails
- [x] Maumee River Water Trail — §4.6 applied; management tier = T3; deferred to T3

### ODNR Division of Forestry
- [x] No state forest in Lucas County — confirmed NULL

### OTIC
- [x] No OTIC plazas in Lucas County — confirmed NULL (nearest: MP 20.8 Williams Co; MP 76.9 Ottawa Co)

### ODNR Fishing Maps / River Maps
- [x] Fishing Lake Maps — no Lucas County entries confirmed
- [x] River & Stream Fishing Maps — no Lucas County entries confirmed

### Open / Deferred
- [x] ODOT Rest Areas (LUC-F-16) — RESOLVED 2026-04-29: NULL (0 Lucas County entries in 82-entry embedded JSON list)
- [x] ODNR Scenic Rivers (LUC-F-17) — RESOLVED 2026-04-29: NULL for Lucas Co (Maumee River designation ends at Perrysburg/Wood County)
- [x] UT Stranahan Arboretum (LUC-F-18) — RESOLVED 2026-04-28: staged T2 retroactively (46 ac, 4131 Tantara Rd)
- [x] ODNR Historic Places / New Deal Era Sites (LUC-F-19) — RESOLVED 2026-04-29: NULL (no ODNR-managed historic places in Lucas Co; WPA/CCC structures at T3 Metroparks already staged)

---

## Pre-Discovery Checklist — Tier 6 (Municipal — Lucas County) — COMPLETE 2026-04-28

**Enumeration source**: Wikipedia "Lucas County, Ohio" Municipalities and communities table (fetched 2026-04-28); cross-referenced with co.lucas.oh.us/2587/Cities and co.lucas.oh.us/2589/Villages (fetched 2026-04-28).

**IMP-015 ordering**: Complete ALL web discovery for all municipalities first, then run single consolidated map verification pass.

**Toledo batching**: Toledo triggers §5.13 large municipality protocol (known large city; assumed >100 parks). Full enumeration required before batch plan is created.

### Cities

| # | Municipality | Pop (approx) | Official Website | Status |
|---|-------------|--------------|------------------|--------|
| 1 | Toledo | ~270,000 | toledo.oh.gov | COMPLETE — §5.13 batched; 122 Sites+Trails (Batch 1: Asbury→Promenade 97 Sites; Batch 2: Ravine I→Yondota 25 Sites; Anthony Wayne Trail + Chessie Circle Trail staged as Trails); source: NW_Ohio_Parks_View + NW_Ohio_Trails_View GIS |
| 2 | Oregon | ~20,000 | oregonohio.org | COMPLETE — 8 entities staged |
| 3 | Sylvania | ~19,000 | cityofsylvania.com | COMPLETE — entities staged; Olander Park System = T3 Special District (LUC-F-08 RESOLVED) |
| 4 | Maumee | ~15,000 | maumee.org | COMPLETE — 17 entities staged |
| 5 | Waterville | ~5,500 | watervilleohio.org | COMPLETE — 7 entities staged |

### Villages

| # | Municipality | Pop (approx) | Official Website | Status |
|---|-------------|--------------|------------------|--------|
| 6 | Berkey | ~250 | — | COMPLETE — 1 entity staged |
| 7 | Harbor View | ~75 | — | COMPLETE — 1 entity staged |
| 8 | Holland | ~1,300 | villageofholland.com | COMPLETE — 3 entities staged |
| 9 | Ottawa Hills | ~4,500 | ottawahills.org | COMPLETE — 7 entities staged |
| 10 | Swanton | ~3,800 | swantonohio.org | COMPLETE — NULL (no Lucas-portion entities in GIS); documented with evidence |
| 11 | Whitehouse | ~4,500 | whitehouseoh.gov | COMPLETE — 3 entities staged |

**Notes:**
- Richfield Center = CDP (unincorporated community) — NOT a T6 municipal entity.
- Waterville is a city (confirmed Wikipedia) — distinct from Waterville Township (T5 null).
- Swanton village ‡ = straddles Lucas/Fulton county line; discover for Lucas-portion entities only.
- LUC-F-08 (Olander Park governance): Olander Park in Sylvania area — likely Ottawa Hills or City of Sylvania; confirm during Sylvania and Ottawa Hills discovery.
- LUC-F-10 (Civic Center Mall): verify current status during Toledo discovery.
- LUC-F-15 (Toledo Zoo): assess scope during Toledo discovery.

### Entity Types — T6 Results Summary

- [x] Sites — 148 Sites staged across all municipalities (Toledo 97+25=122; Oregon 6; Sylvania 3; Maumee 14; Waterville 5; Berkey 1; Harbor View 1; Holland 2; Ottawa Hills 6; Whitehouse 3; Swanton 0)
- [x] Trails — 18 Trails staged (Toledo 2 regional trails; Oregon 1; Maumee 2; Waterville 1; Ottawa Hills 1; others per GIS NW_Ohio_Trails_View)
- [x] Trail Segments — NULL with evidence; no named/operational segments at municipal tier
- [x] Trail Networks — NULL with evidence; no multi-trail municipal networks found
- [x] Site Networks — NULL with evidence; no municipal park systems with network identity threshold met
- [x] Access Points — 6 APs staged (boat launches and trailheads from GIS)

**IMP-015 map verification pass**: COMPLETE 2026-04-28 — GPS centroids acquired from NW_Ohio_Parks_View GIS (outSR=4326, returnCentroid=true); 172/172 T6 records updated. Google Maps spot-check confirmed: Detwiler Park/Toledo ✓, Anderson Park/Maumee ✓, Baer Park/Waterville ✓, Ottawa Hills coords confirmed in-village ✓. GIS centroid coordinates match Maps within ~50m. No identity errors detected. Greenspace (Ottawa Hills, 4 records) noted as GPS-ambiguous — same-name parcels share coordinate; flagged in identity_notes_raw.

---

## Pre-Discovery Checklist — Tier 7 (Land Trust / Conservancy) — IN PROGRESS 2026-04-28

**Enumeration sources**: TNC Ohio preserves page (nature.org/ohio/places-we-protect); ACRES Land Trust preserves (acreslandtrust.org/preserves/); ONAPA preserve map (onapa.org/preserve-map.html); LTA directory (landtrustalliance.org — 404); NW_Ohio_Parks_View GIS (Private-NP and Special District ownertype records); web search for Lucas County land trusts. Fetched 2026-04-28.

### Organizations Enumerated

| # | Organization | Status | Notes |
|---|-------------|--------|-------|
| 1 | The Nature Conservancy (TNC) | ACTIVE | Kitty Todd Nature Preserve, 1,464 ac, 10420 Old State Line Rd near Swanton/Holland; 3 trails, 3 APs; GIS shows 13 parcels ~1,437 ac |
| 2 | ACRES Land Trust | NULL | Covers NE Indiana + portions Defiance/Fulton OH only; no Lucas County preserves |
| 3 | Lake Erie Conservancy | INVESTIGATE | 2 "Lakeway" parcels in Curtice, status=Closed/Undeveloped per GIS; need website check |
| 4 | Howard Farms Conservancy District | T3 RETRO | ownertype=Special District → T3 (not T7); 2 Ottawa Wildlife Refuge parcels in Curtice, status=Open; stage retroactively at T3 |
| 5 | Old West End Association | INVESTIGATE | Agnes Reynolds Jackson Arboretum, 1.66 ac, Toledo; check public access and T7 qualification |
| 6 | Lucas County Wildlife Trusteeship (LCWT) | UNCONFIRMED | Web search returned no results; may not exist or have different name |
| 7 | ONAPA | NULL | ONAPA preserve map links to ODNR SNP finder only; no independent preserve directory |
| 8 | LTA directory | NULL | LTA find-a-land-trust pages all 404; directory unavailable |

### Preserves to Stage

| # | Name | Org | Tier | Status |
|---|------|-----|------|--------|
| 1 | Kitty Todd Nature Preserve (primary entity) | TNC | T7 | PENDING |
| 2 | Oak Savanna and Cactus Loop Trail | TNC | T7 | PENDING |
| 3 | Salamander Flats Wetland Trail | TNC | T7 | PENDING |
| 4 | Sandhill Crane Wetland Viewing Area Trail | TNC | T7 | PENDING |
| 5 | Kitty Todd Main Trailhead / Parking (10420 Old State Line Rd) | TNC | T7 | PENDING |
| 6 | Salamander Flats Trailhead | TNC | T7 | PENDING |
| 7 | Sandhill Crane Trailhead | TNC | T7 | PENDING |
| 8 | Ottawa Wildlife Refuge (2 parcels, Howard Farms Conservancy District) | HFCD | T3 retro | PENDING |

---

## Pre-Discovery Checklist — Tier 8 (Private / Organization-Based) — COMPLETE 2026-04-29

**Enumeration sources**: NW_Ohio_Parks_View GIS (ownertype=Private, status=Open); web searches (§5.1 all query types); ODNR Licensed Hunting Preserves Registry search; Erie Shores Council / BSA website; ultimatepheasanthunting.com Ohio directory; christiancamppro.com Ohio camps; session log candidates (LUC-F-14, LUC-F-15). Fetched 2026-04-29.

### Organizations / Sites Enumerated

| # | Entity | Org / Owner | Status | Notes |
|---|--------|------------|--------|-------|
| 1 | Camp Miakonda | Erie Shores Council, BSA | ✓ IN SCOPE — STAGED | 160 ac, 5600 W Sylvania Ave, Toledo; Scout camp; reservation access; Ohio's oldest Scout camp; 2 named trails |
| 2 | Agnes Reynolds Jackson Arboretum | Old West End Association | ✓ IN SCOPE — STAGED | 1.66 ac, 2501 Robinwood Ave, Toledo; named urban arboretum; always open; GIS ownertype=Private |
| 3 | River Tract | Owens Corning | ✓ IN SCOPE — STAGED | 19.76 ac, Toledo; Maumee River frontage at OC HQ; public 1-mi fitness trail; GIS status=Open |
| 4 | Toledo Zoo & Aquarium | Toledo Zoological Society | OUT OF SCOPE — LUC-F-15 RESOLVED | Zoological park (animal exhibits), not a natural area; 51 ac; Wild Toledo = outreach program; no public nature trails accessible independent of zoo admission |
| 5 | Cornerstone Park | Cornerstone Church | OUT OF SCOPE | 7 ac, Maumee (1520 Reynolds Rd); church grounds labeled "park" in GIS; no evidence of distinct public park identity or trail system; church campus open space |
| 6 | Lewis Ave Park | St. Catherine's Church | OUT OF SCOPE | 6 ac, Toledo (Lewis Ave area); church grounds labeled "park" in GIS; no evidence of distinct public park identity |
| 7 | Bay Park Community Hospital grounds | Bay Park Community Hospital | OUT OF SCOPE | 44 ac, Oregon OH; hospital campus; no public trail or natural area components found |

### Hunting Preserves / Agritourism (mandatory §5.1 check)
- [x] ODNR Licensed Hunting Preserves Registry — searched ohiodnr.gov/hunt-fish/hunting/licensed-hunting-preserves → redirected to ODNR homepage (no public directory page found); web search for site:ohiodnr.gov hunting preserves returned no county-by-county registry
- [x] ultimatepheasanthunting.com Ohio directory (25 listings) — NO Lucas County entries
- [x] Web search "Lucas County Ohio hunting preserve" — NO Lucas County entries; nearest = WR Hunt Club, Clyde OH (Sandusky Co)
- [x] Web search "Lucas County Ohio agritourism" — no nature-trail-bearing agritourism operations found
- **RESULT: NULL** — No licensed hunting preserves or qualifying agritourism operations in Lucas County

### Church Camps / Retreat Centers (mandatory §5.1 check)
- [x] Web search "Lucas County Ohio church camp OR retreat center OR nature center" — no Lucas County results; all Ohio church camps are in other counties
- **RESULT: NULL** — No church camps or retreat centers with trails/natural areas in Lucas County

### Other §5.1 Searches
- [x] "Lucas County Ohio private nature preserve" — only Kitty Todd found (T7 complete)
- [x] "Lucas County Ohio scout camp" — only Camp Miakonda found (BSA, Erie Shores Council)
- [x] "Lucas County Ohio university natural area" — UT Stranahan Arboretum (46 ac, 4131 Tantara Rd) = T2 (§4.7 university public access); no other university natural areas found
- [x] Cross-reference from prior tiers — no additional T8 leads surfaced

### Entities to Stage

| # | Name | Type | Status |
|---|------|------|--------|
| 1 | Camp Miakonda | Site | STAGED |
| 2 | Miakonda Historical Trail | Trail | STAGED |
| 3 | Camp Miakonda Orienteering Trail | Trail | STAGED |
| 4 | Agnes Reynolds Jackson Arboretum | Site | STAGED |
| 5 | River Tract | Site | STAGED |

---

## Pre-Discovery Checklist — Tier 1 (Federal / Tribal / OSM) — COMPLETE 2026-04-27

Complete enumeration of known federal entities and sources to check before T1 is marked complete.

### USFWS
- [x] Cedar Point National Wildlife Refuge — https://www.fws.gov/refuge/cedar-point — CONFIRMED Site (T1)
- [x] West Sister Island National Wildlife Refuge — https://www.fws.gov/refuge/west-sister-island — CONFIRMED Site (T1, CLOSED/Wilderness)

### NPS
- [x] NPS API stateCode=OH — 10 OH units confirmed; none in Lucas County — NULL

### USACE / NID
- [x] USACE NID CSV queried — no Lucas County dam records — NULL

### OSM / Overpass
- [x] Overpass queries (boundary=protected_area, leisure=nature_reserve, leisure=park, landuse=conservation) — COMPLETE 2026-04-29. 9 entities returned: Missionary Island WA ✓ (T2), Irwin Prairie SNP ✓ (T2), Oak Openings Preserve ✓ (T3), Louis W. Campbell SNP ✓ (T2), Maumee Bay SP ✓ (T2) — all already staged. "Native Prairie Habitat" (lat=41.618, no operator): generic habitat patch, no standalone record. "Sawyer Quarry Nature Preserve" (Wood County Park District): Wood County entity — excluded. "Wheeler Preserve" (bedfordmi.org): Bedford Township Michigan — excluded. "Erie State Game Area": Michigan DNR — excluded. Broad park/conservation check added Old West End Commons ✓ (T6) and Central Park (0 GIS records, no web presence as Toledo park, OSM-tagged green space below threshold). **NO NEW ENTITIES from Overpass sweep.** T1 FULLY COMPLETE.

### GNIS Marsh Entries (verify managed status)
- [ ] Cedar Point Marsh — likely GNIS geographic feature; no managed access found; recommend exclude at normalization (LUC-F-03)
- [ ] Douglas Marsh — GNIS feature; no managed access found — likely exclude
- [ ] Mallard Club Marsh — GNIS feature; overlaps with Mallard Club Wildlife Area (T2) — confirm at T2
- [ ] Metzger Marsh (GNIS) — overlaps with Metzger Marsh Wildlife Area (T2) — confirm at T2
- [ ] Pintail Marsh — GNIS feature; no managed access found — likely exclude
- [ ] Searles Marsh — GNIS feature; no managed access found — likely exclude
- [ ] Willow Point Marsh — GNIS feature; no managed access found — likely exclude

---

## Captured Source Data

### T1 — USFWS Refuge Data (fetched 2026-04-27)

**Cedar Point NWR** (fws.gov/refuge/cedar-point):
- Acres: nearly 2,500
- Established: 1964 (formerly a hunt club)
- County: Lucas, northwest Ohio
- Access: Yondota Road off SR-2, 3 mi E of Oregon OH / 9 mi E of I-280
- Open: May 1–Aug 31, daylight hours (fishing/paddling access)
- HQ/Admin: Ottawa NWR, 14000 West State Route 2, Oak Harbor OH 43449-9485; (419) 898-0014
- Description: "Cedar Point National Wildlife Refuge has a fascinating history. From a famous hunt club to a refuge in 1964, it has provided habitat for a variety of waterfowl, bald eagles and plants for many years. The nearly 2,500 acres protect rare plants and habitats that aren't found in other areas of Ohio."
- Features: Large open marsh; migratory bird habitat (wood ducks, trumpeter swans, Canada geese, great blue herons, sandhill cranes, mallards); bald eagle nests; deer; songbirds; shore fishing; non-motorized craft access

**West Sister Island NWR** (fws.gov/refuge/west-sister-island):
- Acres: 82
- Designated refuge: 1938; Wilderness Area: 1975
- Location: Lake Erie Western Basin, 9 miles from shore
- Access: CLOSED to all public use; research permits only; boaters may view from water
- HQ/Admin: Ottawa NWR (same as above)
- Description: "Declared a refuge in 1938 and a wilderness area in 1975, West Sister Island National Wildlife Refuge is located nine miles from shore in the Lake Erie Western Basin. This 82 acre island is closed to all access to protect the largest nesting colony of wading birds in the United States Great Lakes."
- Features: Lighthouse (constructed 1848, automated 1937); nesting colony of great blue herons, great egrets, double-crested cormorants, black-crowned night-herons, snowy egrets, little blue herons

### T1 — NPS Ohio Units (NPS API, fetched 2026-04-27)
10 units in Ohio: Charles Young Buffalo Soldiers NM, Cuyahoga Valley NP, Dayton Aviation Heritage NHP, First Ladies NHS, Hopewell Culture NHP, James A Garfield NHS, Lewis & Clark NHT, North Country NST, Perry's Victory & International Peace Memorial, William Howard Taft NHS. None in Lucas County.

---

### T6 — NW_Ohio_Parks_View ArcGIS GIS Layer (fetched 2026-04-28)

**Service URL**: `https://services1.arcgis.com/SvdVZfVAhlYe04Tl/arcgis/rest/services/NW_Ohio_Parks_View/FeatureServer/0`  
**Query**: `where=county='Lucas'&outFields=*&returnGeometry=false&orderByFields=citymuni,name&f=json`  
**Records returned**: 395 (all Lucas County parks across all governance tiers)  
**Saved to**: `/tmp/lucas_gis_parks.json` (session-local temp; re-query if needed)

**Key fields used**:
- `name` — park name (name_raw)
- `address` — street address (location_raw)
- `citymuni` — city/municipality (used for governance assignment)
- `county` — county name
- `acres` — acreage (acres_raw)

---

### T5 — Springfield Township Parks (fetched 2026-04-29)

**Source URL**: `https://springfieldtownship.net/departments/parks/`  
**Township address**: 7617 Angola Rd (at S. King Rd.), Holland, OH 43528 | Phone: 419-865-0239  
**Note**: springfieldtownship.us (CivicEngage) = Summit County (Akron). springfieldtwp.org = Hamilton County (Cincinnati). Correct Lucas County site = springfieldtownship.net (WordPress).

**Parks confirmed from website:**

| Name | Address | Acres | Features |
|------|---------|-------|----------|
| Community Homecoming Park | 7807 Angola Rd | 40 | 4 baseball/softball diamonds; soccer fields; gazebo; shelter house (rentable); playground; fishing pond; boardwalk; walking paths |
| Lincoln Green Park | 201 Shrewsbury Dr (GIS: 201 Burnham Green Rd — discrepancy) | 3 | Covered picnic area; benches; walking trail; playground; open green space |
| Carmella Gardens Park | 6555 Danny Ln (GIS: Carmella Gardens) | ~3 | Covered picnic area; playground; ball diamond |
| Bear Creek Park | behind 6645 Airport Hwy (GIS: 6621 Airport Hwy) | — | Football field; little league use |

**GIS-only parks (not on website parks page):**
- Florian Park — 1912 Old Planke Rd, Holland
- Springfield Athletic Complex — 1041 Albon Rd
- `status` — Open / Undeveloped / Closed
- `agencyname` — managing agency (governance_raw)
- `agencytype` — agency type category
- `ownertype` — Municipal / Special District / State / Federal / Private
- `Description` — narrative description (description_raw; 114 of 395 records have populated value)
- Boolean amenity fields (baseball, basketball_full, bbqgrill, bikepark, bikerack, bocceball, communitybuilding, discgolf, dogpark, drinkingfountain, fishing, golfcourse, horseshoes, launchboat, launchkayak, naturearea, parkinglot, parkbench, picnicshelter, picnictables, playequipment, recfield, reservableshelter, restroom, sculpturemonument, skatepark, sleddingarea, soccerfield, shuffleboard, tennis, tennis_lighted, volleyball, volleyball_lighted, walkstrails, water_pool, water_splashpad, water_shoreline) → mapped to features_raw

**Governance tiers resolved from ownertype**:
- `Municipal` → T6 (city/village managed)
- `Special District` → T3 (Metroparks Toledo, Olander Park System, Sylvania Area JRD)
- `State` → T2 (ODNR, UT = university §4.7)
- `Federal` → T1 (USACE, USFWS)
- `Private` → T8

**Discovery method**: Toledo Parks Explorer at toledo.oh.gov/residents/parks uses an embedded ArcGIS Dashboard (iframe). Dashboard URL: `https://toledo.maps.arcgis.com/apps/dashboards/33025e55224b4770862f8c5afb54ca1e`. Underlying FeatureServer URL discovered via Chrome browser network request monitoring during page load. Direct REST API query returned all 395 county records simultaneously, eliminating municipality-by-municipality web discovery.

**114 records with Description fields**: Used verbatim as description_raw. Remaining 281 records have description_raw=null.

---

### T6 — NW_Ohio_Trails_View ArcGIS GIS Layer (fetched 2026-04-28)

**Service URL**: `https://services1.arcgis.com/SvdVZfVAhlYe04Tl/arcgis/rest/services/NW_Ohio_Trails_View/FeatureServer/0`  
**Query**: `where=county='Lucas'&outFields=*&returnGeometry=false&f=json`  
**Records returned**: ~80+ trail segments/features in Lucas County

**Key fields used**:
- `name` — trail name
- `agency` — managing agency (NOTE: different field from parks layer's `agencyname`)
- `trailtype` — trail surface/type
- `use` — permitted uses
- `surface` — surface material
- `county` — county name

**Trails staged**: Municipal-tier trails from this layer (City of Toledo, Oregon, Maumee, Waterville, Ottawa Hills). Metroparks-managed trails already captured at T3 from metroparkstoledo.com.

---

## Source Files (§24 IMP-129)

Qualifying binary source files saved to `County_Spreadsheets/Lucas/source_files/` on 2026-05-22 (retroactive — §24 was not executed at discovery time due to IMP-129 wget mechanism gap):

| Filename | Size | Source / Notes |
|---|---|---|
| `mallard_club_wa_map.pdf` | 1,844 KB | ODNR Mallard Club Wildlife Area map (T2 source) |
| `metzger_marsh_wa_map.pdf` | 1,667 KB | ODNR Metzger Marsh Wildlife Area boundary map (T2 source; GIS_VERIFY_COUNTY Lucas/Ottawa) |
| `meilke_road_savanna_wa_map.pdf` | 1,440 KB | ODNR Meilke Road Savanna Wildlife Area map (T2 source) |
| `lanker_wa_map.pdf` | 1,354 KB | ODNR Lanker Wildlife Area map (T2 source) |
| `magee_marsh_wa_map.pdf` | 1,805 KB | ODNR Magee Marsh Wildlife Area boundary map (T2 source; GIS_VERIFY_COUNTY Lucas/Ottawa) |
| `magee_marsh_wa_trail_map.pdf` | 3,035 KB | ODNR Magee Marsh Wildlife Area trail map (T2 source: trail layouts and lengths) |
| `missionary_island_wa_map.pdf` | 1,407 KB | ODNR Missionary Island Wildlife Area map (T2 source; GIS_VERIFY_COUNTY Lucas/Wood) |
| `van_tassel_wa_map.pdf` | 1,490 KB | ODNR Van Tassel Wildlife Area map (T2 source; GIS_VERIFY_COUNTY Wood/Lucas) |
| `metroparks_wabash_cannonball_trail_map.pdf` | 1,314 KB | Metroparks Toledo Wabash Cannonball Trail map (T3 source; North Fork 46 mi / South Fork 17 mi; multi-county) |
| `metroparks_secor_area_map.pdf` | 659 KB | Metroparks Toledo Secor/Oak Openings area map (T3 source; Oak Openings Corridor trail) |
| `metroparks_wiregrass_lake_map.pdf` | 3,798 KB | Metroparks Toledo Wiregrass Lake map (T3 source; Oak Openings trail system) |
| `metroparks_toledo_all_parks_brochure_2025.pdf` | 1,485 KB | Metroparks Toledo All Parks Brochure 2025 (T3 source; system-wide overview, 23 parks) |
| `kitty_todd_nature_preserve_trail_map_2022.pdf` | 333 KB | TNC Ohio Kitty Todd Nature Preserve trail map 2022 (T7 source; 3 trails, GPS) |
