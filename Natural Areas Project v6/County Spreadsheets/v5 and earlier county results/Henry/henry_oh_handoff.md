# Henry County, Ohio — Handoff Document
**RUN_ID:** `henry_oh_2026_04_20`
**PREFIX:** `HEN`
**Last updated:** 2026-06-10 — BATCH RESOLUTION COMPLETE
**Status:** ALL TIERS CLOSED. Batch resolution applied 2026-06-10. See `henry_oh_batch_resolution_2026_06_10.md`.

## Batch Resolution Summary — 2026-06-10
- S-0018 (MJTP Henry-only duplicate) → status=Retired
- AP-0001, AP-0002 reparented from S-0018 → OH-MC-S-0030
- Trail parents added: T-0001/T-0003/T-0004/T-0007 → OH-MC-S-0030 (4 entries)
- +3 supplemental sites: S-0032 Napoleon VMP (1ac), S-0033 Cherry Street Park (11ac), S-0034 Dry Creek WA (2ac)
- Camp Libbey 321ac: confirmed Defiance County, not Henry — flagged for Defiance T7 run
- Final: 33 HEN sites (active) | 4 trail_parents

## Supplemental Resolution — 2026-06-12
- MRQ 160 (Camp Libbey): RESOLVED — inserted as OH-DEF-S-0041 (Defiance T7). GPS 41.282768,-84.278949 (28325 State Route 281, Defiance OH). Girl Scouts of Western Ohio, 321ac, PAD-US GAP4.
- MRQ 161 (Napoleon T6 parks): RESOLVED — FALSE POSITIVE for Henry. All PAD-US park name matches (Diehl, Riverside, Woodland, VFW 3360, Second Ward) confirmed as City of Defiance parks, not Napoleon/Henry entities. Napoleon city parks website confirms only Oakwood, Glenwood, Ritter, Oberhaus, Swearingen, East Riverdowns — all already in Henry DB. Diehl Park → OH-DEF-S-0007; Riverside Park → OH-DEF-S-0013 (already in Defiance DB). 3 missing Defiance parks (Woodland 43ac, VFW 3360 24ac, Second Ward 1ac) staged as MRQ 191 for Defiance verification.
- GNIS spot-check: 1 Henry County Park feature (North Turkeyfoot State Park = OH-HEN-S-0023 under Wildlife Area name). No gaps.
- Henry County supplemental complete. 34 active sites in DB.

### Open Items (post-supplemental)
- ~~Camp Libbey: stage for Defiance County T7 batch~~ RESOLVED 2026-06-12: OH-DEF-S-0041
- ~~Napoleon T6 parks per QR: check City of Napoleon website~~ RESOLVED 2026-06-12: FALSE POSITIVE
- Cherry Street Park (S-0033): municipality confirm — Liberty Center or unincorporated
- S-0013 HEN-WA-1 acres blank — fill from ODNR
- S-0011 Henry County Fairgrounds: scope review

This document is the durable record across context breaks. Update before every session end.

---

## County Context

- **County:** Henry County, Ohio
- **County seat:** Napoleon
- **Major municipalities:**
  - City: Napoleon
  - Villages: Deshler, Holgate, Hamler, Liberty Center, Malinta, McClure, Florida, New Bavaria, Custar
- **Townships (13):** Washington, Napoleon, Flatrock, Richfield, Damascus, Harrison, Liberty, Marion, Monroe, Bartlow, Pleasant, Ridgeville, Freedom — **CORRECTION 2026-04-21**: Handoff originally listed 12 townships (Washington, Napoleon, Flatrock, Richfield, Damascus, Tiffin, Beaver Dam, Bartlow, Bloom, Liberty, Monterey, Freedom). OTA 2022-2023 Roster + Henry County Engineer confirm 13 active townships. Tiffin, Beaver Dam, Bloom, Monterey are NOT Henry County townships — bootstrap errors. Harrison, Marion, Monroe, Pleasant, Ridgeville were missing from original bootstrap.
- **Park districts:** No standalone park district identified. Napoleon operates its own city parks system. No metropark affiliation confirmed.
- **Known trail corridors:**
  - Wabash Cannonball Trail (rail-trail; multi-county; runs east–west through Liberty Center)
  - Buckeye Trail / Miami & Erie Canal Towpath (along CR 424 / Maumee River corridor through Florida and McClure to Mary Jane Thurston SP)
  - North Country NST (co-routes with Buckeye Trail in Ohio; passes through Henry County — already staged in Defiance run as multi-county entity)
  - Maumee River Water Trail (staged in Defiance run; passes through Henry County — confirm Henry presence)
- **Known cross-county entities:**
  - North Country NST (staged at T1 in Defiance run — do not re-stage; note Henry County presence)
  - Maumee River Water Trail (staged at T2 in Defiance run — do not re-stage; confirm Henry County access points)
  - Wabash Cannonball Trail (multi-county; Henry County is a primary host county — discover here as governing county)

---

## Tiers Completed

| Tier | Source Type | Entities Found | Notes |
|------|-------------|----------------|-------|
| T1 | Federal / OSM / Tribal | 0 — NULL | No federal land ownership in Henry County. NCT confirmed passing through (OSM rel 11140513, co-routes with BT along Miami & Erie Canal Towpath through MJTSP near McClure) — cross-ref to DEF run, not re-staged. USFWS: no refuges. USACE: no flood control projects. USFS/BLM/DoD: none. Tribal: none. All null result blocks written to staging YAML. COMPLETE 2026-04-20. |
| T2 | State agency | 14 entities | 6 Sites: MJTSP (105 ac ODNR / 591 ac baseline — conflict flagged), North Turkeyfoot WA (458 ac), Florida WA (3 ac), Henry County WA 1/2/3 (locations pending PDF), Maumee State Scenic River (multi-county). 5 Trails at MJTSP: Storybook, Blue, Orange, Tow Path, Yellow. 2 APs: MJTSP Marina + Boat Launch Ramp. No state forests, no SNPs, OHC site down (PENDING — HEN-F-09), no ODOT/OTIC. All 6 entity types covered. IMP-080 passed. COMPLETE 2026-04-20. |
| T3 | District agency | 0 — NULL | Henry SWCD confirmed no land ownership; no standalone park district; no metropark; no conservancy district; no flood-control district in Henry County. Full null across all 6 entity types. IMP-080 passed. COMPLETE 2026-04-20. |
| T4 | County website | 6 entities | 1 Trail + 5 Trail Segments: Miami & Erie Canal Towpath Hiking Trail (Henry County Park District, organized 2005, all-volunteer, state canal land leases) with 5 named segments: Independence Leg, Renegade Leg, Napoleon Leg, Damascus Leg, WideWater Section. No county parks dept on county site. Engineer: roads/drainage only. HCHS → T7. Fairgrounds → T8. WCT → T7 (NORTA). NRHP: 4 downtown Napoleon buildings, none qualify. IMP-080 passed. COMPLETE 2026-04-21. |
| T5 | Township | 0 — NULL | All 13 townships checked. Washington Twp (only OTA-listed website): confirmed Henry County; menu = Cemetery/Maintenance/Zoning/Employment only; no parks. Remaining 12 townships: no OTA websites; web search confirmed no township-managed parks, trails, or APs. Hamler Community Park (13 ac, Marion Twp): owned by Hamler Summerfest community association ("no tax money"), not township → T8 candidate. Damascus Twp Maumee River camping: informal private use, not township infrastructure. Full null across all 6 entity types, all 13 townships. IMP-080 passed. COMPLETE 2026-04-21. |
| T6 | Municipal | 23 entities (20 Sites + 3 Access Points) — CLOSED | Napoleon: 10 Sites (Oakwood, Glenwood, Ritter, Oberhaus, Swearingen, East Riverdowns, Dog Park, Wayne, Vorwerk, Meyerholtz) + 2 APs (Ritter Boat Launch, Oberhaus Boat Dock). Deshler: 2 Sites (Crossroads Park, Reservoir Park). Holgate: 2 Sites (Old School Park, Village Park). Liberty Center: 3 Sites (Firemen's Park, Steward Park, Veterans Memorial Park) + 1 AP (WCT Depot Trailhead). Hamler: 1 Site (Memorial Park). McClure: 1 Site (Big Creek Park). New Bavaria: 1 Site (New Bavaria Park — confirmed Google Maps, Thomas St, GPS 41.203170,-84.168809). Florida: no village park confirmed (HEN-F-06 — "Canal Falls River Access" is not a Florida village entity). Malinta: no park confirmed (no Maps listing). Custar: Wood County bootstrap error (excluded). GPS captured for 22 of 23 entities (Firemen's Park only exception — no address confirmed). IMP-080 passed. Map verification COMPLETE 2026-04-21. TIER CLOSED. |
| T7 | Conservancy / Land Trust | 5 entities — CLOSED 2026-04-26 | NORTA/WCT: Wabash Cannonball Trail (Trail, multi-county Fulton/Henry/Lucas/Williams, NORTA gov.) + WCT South Fork (Trail Segment, ~6 mi Henry Co. section, Washington Twp, cinder/gravel/dirt/grass, western terminus GPS 41.451114,-83.989429) + Henry CR 6C Trailhead (AP, GPS 41.450715,-83.990451, parking/picnic/kiosk, ~1 mi east of Liberty Center; NORTA ownership ends at Henry CR 7/Pleasantview Dr). HEN-F-07 RESOLVED — second baseline WCT entry confirmed as CR 6C trailhead; "Holgate" baseline label was misidentification. Liberty Center Depot AP GPS updated to 41.443728,-84.009326 from NORTA trail-access page. HCHS: Dr. John Bloomfield Home & Carriage House Museum (229 W Clinton St, Napoleon; T7 Site) + HCHS Fairgrounds Historic Complex (outdoor historic buildings on Fairgrounds property; T7 Site; pipeline to assess overlap with T8 Fairgrounds entity). BSC: NULL — 19 protected lands listed, all in Erie/Ottawa/Lucas/Sandusky/Wood counties; "Henry-Wood Sportsman Alliance" is partner org name, not Henry County location. TNC OH: NULL — 382 properties, zero in Henry County. OHC (HEN-F-09): no static-accessible Henry County sites; site finder is JS-rendered; search returns unrelated documents; flag remains open. T4 discovery_tier field corrected for 6 records (were None, now 4). IMP-080 passed. COMPLETE 2026-04-26. TIER CLOSED. |
| T8 | Private / Other | 2 entities — CLOSED 2026-04-26 | Henry County Fairgrounds (821 S Perry St, Napoleon; Henry County Agricultural Society; home of Henry County Fair; new 43,750 sf events center under construction at north end; HCHS Historic Complex on grounds — pipeline to resolve T7/T8 overlap). Hamler Community Park (SR 109, north edge of Hamler, Marion Twp; Hamler Summerfest non-profit, Hamler Community Park Inc.; 13 ac purchased 1974; 100'×250' steel structure with basketball/tennis courts; playground; year-round community use; Summerfest + Country Fest venue; no tax money; resolves HEN-F-10). Field of Dreams Drive-In (V602 CR 6, near Liberty Center) — EXCLUDED: commercial cinema, primary use not recreational/natural. No private hunt clubs or private nature preserves identified. IMP-080 passed. COMPLETE 2026-04-26. TIER CLOSED. |

---

## Tiers Remaining

| Tier | Source Type | Entry Points |
|------|-------------|--------------|
| ~~T1~~ | ~~Federal / OSM~~ | COMPLETE 2026-04-20 — null; see Tiers Completed |
| ~~T2~~ | ~~State agency~~ | COMPLETE 2026-04-20 — 14 entities; see Tiers Completed. OHC PENDING (site maintenance — HEN-F-09) |
| ~~T3~~ | ~~District agency~~ | COMPLETE 2026-04-20 — null; see Tiers Completed |
| ~~T4~~ | ~~County website~~ | COMPLETE 2026-04-21 — 6 entities; see Tiers Completed |
| ~~T5~~ | ~~Township~~ | COMPLETE 2026-04-21 — null; see Tiers Completed. Hamler Community Park (Marion Twp) → T8 candidate (private assoc). |
| ~~T6~~ | ~~Municipal~~ | COMPLETE 2026-04-21 — 23 entities (20 Sites + 3 APs). GPS captured for 22/23. New Bavaria Park confirmed during map verification. Florida/Malinta unresolved (no village parks confirmed). |
| ~~T7~~ | ~~Conservancy / Land Trust~~ | COMPLETE 2026-04-26 — 5 entities (1 Trail + 1 Trail Segment + 1 AP + 2 Sites). WCT (NORTA) + HCHS sites. BSC/TNC/OHC null. See Tiers Completed. |
| ~~T8~~ | ~~Private / other~~ | COMPLETE 2026-04-26 — 2 entities (2 Sites). See Tiers Completed. |

---

## Key Active Flags

| Flag ID | Entity / Topic | Issue | Resolution Path |
|---------|----------------|-------|-----------------|
| ~~HEN-F-01~~ | ~~Boatramp Facility~~ | RESOLVED 2026-04-21: Boat launch confirmed as part of Ritter Park per napoleonohio.com official parks page. Staged as Access Point "Ritter Park Boat Launch" (child of Ritter Park). Acreage discrepancy (5.6 ac vs 14.8 ac) likely reflects different parcel counts; address confirmed 1111 W. Riverview Ave. |
| ~~HEN-F-02~~ | ~~Ritter Park~~ | RESOLVED 2026-04-21: Both baseline rows are the same park. Official address = 1111 W. Riverview Ave (baseline said 1130 — minor discrepancy). Single Site record staged as Ritter Park. |
| HEN-F-03 | Henry County Wildlife Areas 1/2/3 | Three numbered placeholders; no specific location or parcel detail | Resolve via ODNR Wildlife GIS layer or ODNR public lands viewer during T2 |
| HEN-F-04 | Deshler Reservoir 1 & 2 | No location, acreage, or management detail | Confirm public access and governance during T6 Deshler discovery |
| HEN-F-05 | Hamler Reservoir | No detail in baseline | Confirm public access and governance during T6 Hamler discovery |
| HEN-F-06 | Canal Falls | Typed as Florida Village Park in baseline but described as a natural feature along the canal towpath / Buckeye Trail | Determine whether this is a natural feature, a named trail access point, or a sub-feature of Florida Village Park; resolve during T2 and T6 |
| ~~HEN-F-07~~ | ~~Wabash Cannonball Trailheads (×2)~~ | **RESOLVED 2026-04-26.** Two distinct APs confirmed via NORTA wabashcannonballtrail.org/trail-access/: (1) Liberty Center Train Station/Depot (T6 AP, staged; GPS 41.443728,-84.009326 updated from NORTA page); (2) Henry CR 6C Trailhead — ~1 mile east of Liberty Center between CR U and CR T; small park with parking, picnic table, info kiosk; GPS 41.450715,-83.990451; NORTA ownership ends at Henry CR 7 (Pleasantview Dr). "Holgate" label in baseline was misidentification — CR 6C is in Washington Twp near Liberty Center, not near Holgate village. |
| HEN-F-11 | Custar, OH | BOOTSTRAP ERROR 2026-04-21: Custar is in Wood County, not Henry County (SW corner of Wood County per custarvillage.org + Wood County Engineer). Baseline included Custar in error. Excluded from T6 discovery. No Henry County records created for Custar. |
| HEN-F-08 | North Country NST | Already staged in Defiance run as multi-county Trail | Do not re-stage; note Henry County presence during T1; cross-reference DEF run |
| HEN-F-09 | OHC Henry County sites | Ohio History Connection website returned HTTP 503 (scheduled maintenance) during T2 — unable to confirm presence or absence of OHC-managed state memorials or archaeological preserves | Recheck ohiohistory.org in a future session; no OHC sites expected in Henry County but authoritative confirmation required |
| ~~HEN-F-10~~ | ~~Hamler Community Park~~ | **RESOLVED 2026-04-26.** Hamler Summerfest non-profit (Hamler Community Park Inc.) owns 13-acre park at SR 109, north edge of Hamler (Marion Twp). Land purchased 1974 for $21,000. Year-round community use: basketball/tennis in 100'×250' steel structure, playground, ADA concrete, permanent fencing. Festival venue (Summerfest + Country Fest). No tax money. Staged as T8 Site (entity #50). Source: hamlersf.com/50-year-history.html. |

---

## Entities Discovered

| # | Tier | Type | Name | Governance | Notes |
|---|------|------|------|------------|-------|
| 1 | T2 | Site | Mary Jane Thurston State Park | ODNR Parks & Watercraft | 105 ac (ODNR) / 591 ac (baseline) — acreage conflict flagged. 1466 SR 65, McClure. Resolves baseline seed. |
| 2 | T2 | Site | North Turkeyfoot Wildlife Area | ODNR Division of Wildlife | 458 ac, 2 mi SE of Liberty Center. Buckeye Trail passes through. |
| 3 | T2 | Site | Florida Wildlife Area | ODNR Division of Wildlife | 3 ac, 1 mi NE of Florida. Buckeye Trail passes through. |
| 4 | T2 | Site | Henry County Wildlife Area 1 | ODNR Division of Wildlife | Location unknown — PDF map fetch failed. Resolves HEN-F-03. |
| 5 | T2 | Site | Henry County Wildlife Area 2 | ODNR Division of Wildlife | Location unknown — PDF map fetch failed. Resolves HEN-F-03. |
| 6 | T2 | Site | Henry County Wildlife Area 3 | ODNR Division of Wildlife | Location unknown — PDF map fetch failed. Resolves HEN-F-03. |
| 7 | T2 | Site | Maumee State Scenic River | ODNR Scenic Rivers Program | Multi-county (Defiance, Henry, Wood, Lucas). Category=Water Site, designation=State Scenic River. |
| 8 | T2 | Trail | Storybook Trail | ODNR Parks & Watercraft | 0.45 mi, Easy. Within MJTSP. |
| 9 | T2 | Trail | Blue Trail | ODNR Parks & Watercraft | 1.2 mi, Easy. Within MJTSP. |
| 10 | T2 | Trail | Orange Trail | ODNR Parks & Watercraft | 0.5 mi, Easy. Within MJTSP. |
| 11 | T2 | Trail | Tow Path | ODNR Parks & Watercraft | 0.3 mi within MJTSP, Easy; continues into Wood County. Multi-county flag. |
| 12 | T2 | Trail | Yellow Trail | ODNR Parks & Watercraft | 0.5 mi, Easy. Within MJTSP. |
| 13 | T2 | Access Point | Mary Jane Thurston SP Marina | ODNR Parks & Watercraft | Within MJTSP. Resolution engine to evaluate child Site vs. AP. |
| 14 | T2 | Access Point | Mary Jane Thurston SP Boat Launch Ramp | ODNR Parks & Watercraft | Within MJTSP. Co-located with marina. |
| 15 | T4 | Trail | Miami & Erie Canal Towpath Hiking Trail | Henry County Park District | All-volunteer, organized 2005, leases state canal lands from Ohio. Adjacent to Maumee River across Henry County. Co-routes with Buckeye Trail and North Country Trail (both already staged in DEF run). Multi-county (Defiance/Henry/Wood). 5 named segments. Source: henrycountyparks.blogspot.com. |
| 16 | T4 | Trail Segment | Independence Leg — Miami & Erie Canal Towpath | Henry County Park District | Independence Dam SP → Village of Florida. Western Henry County / Defiance county line. Multi-county (Defiance/Henry). |
| 17 | T4 | Trail Segment | Renegade Leg — Miami & Erie Canal Towpath | Henry County Park District | Village of Florida → Napoleon. Named for Renegade Simon Girty. Henry County only. |
| 18 | T4 | Trail Segment | Napoleon Leg — Miami & Erie Canal Towpath | Henry County Park District | Meyerholtz Park → Henry County Hospital. Runs through Napoleon. |
| 19 | T4 | Trail Segment | Damascus Leg — Miami & Erie Canal Towpath | Henry County Park District | Henry County Hospital → State Route 109. Named for Damascus Township. |
| 20 | T4 | Trail Segment | WideWater Section — Miami & Erie Canal Towpath | Henry County Park District | SR 109 → Providence Dam Metropark (Wood County). Multi-county (Henry/Wood). WideWater = historic canal engineering term. |
| 21 | T6 | Site | Oakwood Park | City of Napoleon | 1400 Oakwood Ave; 52 ac; fishing lake, hiking trails, ball diamonds, batting cages, basketball, football, volleyball, 2 shelters, restrooms. |
| 22 | T6 | Site | Glenwood Park | City of Napoleon | 521 Glenwood Ave; 50+ ac; golf, pool, youth baseball, Kidz Kingdom, 4th of July site. Veterans Field (pony league) is internal field — not a standalone entity. |
| 23 | T6 | Site | Ritter Park | City of Napoleon | 1111 W. Riverview Ave; passive Maumee River park; 1930s stone shelter, walking path, boat launch. Resolves HEN-F-01 + HEN-F-02. |
| 24 | T6 | Access Point | Ritter Park Boat Launch | City of Napoleon | Child AP of Ritter Park. ODNR Watercraft grant-funded. Resolves HEN-F-01. |
| 25 | T6 | Site | Oberhaus Park | City of Napoleon | 750 W. Maumee St; 15 ac; Maumee River frontage, 250-ft boat dock, walking path, Lions/Rotary building. |
| 26 | T6 | Access Point | Oberhaus Park Boat Dock | City of Napoleon | Child AP of Oberhaus Park. 250-ft public dock on Maumee River. |
| 27 | T6 | Site | Swearingen Park | City of Napoleon | S. Perry & E. Barnes Ave; skateboard park, basketball, playground, picnic tables. |
| 28 | T6 | Site | East Riverdowns Park | City of Napoleon | E. Front & Jefferson St; arboretum, tree nursery, 2 softball fields, horseshoes, playground, shelter, volleyball. |
| 29 | T6 | Site | Napoleon Dog Park | City of Napoleon | Child site of East Riverdowns Park. Off-leash, membership required. Girl Scout project. |
| 30 | T6 | Site | Wayne Park | City of Napoleon | 13 ac; rustic shelter (~25 people, rental), volleyball, picnic areas. Address not published — MINIMAL_DATA. |
| 31 | T6 | Site | Vorwerk Park | City of Napoleon | E. Riverview Ave; 24.5 ac; picnic, grills, restrooms, fishing, hiking trails, drinking fountains, parking. GPS: 41.410147, -84.090012. |
| 32 | T6 | Site | Meyerholtz Wildlife Park | City of Napoleon | 1781-1799 W. Riverview Ave; 21.5 ac; wildlife park, birding hotspot (eBird L3683369). |
| 33 | T6 | Site | Deshler Crossroads Park | Village of Deshler | At CSX rail diamond crossing. Railfan park; covered shelter, picnic, scanner speaker, 120VAC plugs, primitive camping. |
| 34 | T6 | Site | Deshler Reservoir Park | Village of Deshler | Fishing, picnic. Partially resolves HEN-F-04 (Deshler Reservoir 1&2). Address pending map verification. |
| 35 | T6 | Site | Old School Park | Village of Holgate | S. Wilhelm / Frazier St; walking trail, playground (CDBG-funded upgrade). |
| 36 | T6 | Site | Holgate Village Park | Village of Holgate | Basketball court, asphalt. Baseline name confirmed. Address pending map verification. |
| 37 | T6 | Site | Liberty Center Firemen's Park | Village of Liberty Center | Confirmed existence (Facebook page); address and amenities pending map verification. MINIMAL_DATA. |
| 38 | T6 | Site | Fredrick Steward Memorial Park | Village of Liberty Center | Tennis courts, Arbor Day trees. Baseline named "Steward Park." Address pending map verification. |
| 39 | T6 | Site | Veterans Memorial Park | Village of Liberty Center | Veteran banners planned (Hist. Society); restroom grant. Address pending map verification. |
| 40 | T6 | Access Point | WCT Liberty Center Depot Trailhead | Village of Liberty Center / NORTA | Wabash St at restored railroad depot. SW terminus WCT South Fork. Fix-it station, kiosk, Ohio hist. marker, parking. Partially resolves HEN-F-07. |
| 41 | T6 | Site | Hamler Memorial Park | Village of Hamler | Main village park. Also listed as "Hamler City Park" birding hotspot (eBird L3680027). Address pending map verification. MINIMAL_DATA. |
| 42 | T6 | Site | Big Creek Park | Village of McClure | 435 S Haley St; GPS 41.3682146,-83.9399398 (Maps: "Big Creek Park and Ball Fields"). Pickleball court (new fence 2024), playground (planned), ball fields. |
| 43 | T6 | Site | New Bavaria Park | Village of New Bavaria | Thomas St, New Bavaria, OH 43548; GPS 41.2031701,-84.1688089. Confirmed Google Maps during map verification pass. Baseline seed: "New Bavaria Village Park." |
| 44 | T7 | Trail | Wabash Cannonball Trail | Northwest Ohio Rails-to-Trails Association (NORTA) | Multi-county: Fulton, Henry, Lucas, Williams. ~64-66 mi total. NORTA owns Henry/Fulton/Williams portions (~32 mi); Metroparks Toledo owns Lucas section. Former Wabash Railroad corridor; South Fork 1855, North Fork ~1900. NCNST certified portions. End points: Montpelier; Maumee and Liberty Center. Resolves HEN-F-07. |
| 45 | T7 | Trail Segment | Wabash Cannonball Trail - South Fork | Northwest Ohio Rails-to-Trails Association (NORTA) | Named fork: Maumee (Lucas Co.) → Liberty Center (Henry Co.); ~18 mi per NORTA. Henry County section ~6 mi in Washington Township; cinder/gravel/dirt/grass. Western terminus GPS 41.451114,-83.989429. |
| 46 | T7 | Access Point | WCT Henry CR 6C Trailhead | Northwest Ohio Rails-to-Trails Association (NORTA) | GPS 41.450715,-83.990451. ~1 mile east of Liberty Center between CR U and CR T; parking, picnic table, info kiosk. NORTA ownership ends at Henry CR 7 (Pleasantview Dr). Resolves HEN-F-07 (second entry). Source: wabashcannonballtrail.org/trail-access/. |
| 47 | T7 | Site | Dr. John Bloomfield Home & Carriage House Museum | Henry County Historical Society (HCHS) | 229 W Clinton St, Napoleon, OH. Victorian Queen Anne house c. 1894, fully restored. Main HCHS museum. Period collections 1800s–1930s. Gray-area NAP entity — pipeline review. |
| 48 | T7 | Site | Henry County Historical Society Fairgrounds Historic Complex | Henry County Historical Society (HCHS) | Henry County Fairgrounds, Napoleon, OH. Outdoor historic buildings: Hartman Log Home c. 1860-1866, 1897 Schoolhouse, Ag Building, Smokehouse, c. 1910 Gazebo. Physically on Fairgrounds property (T8). Pipeline to resolve overlap. |
| 49 | T8 | Site | Henry County Fairgrounds | Henry County Agricultural Society | 821 S Perry Street, Napoleon, OH 43545. Governing body for Henry County Fair. New 43,750 sf events center under construction at north end. HCHS Historic Complex also on grounds. |
| 50 | T8 | Site | Hamler Community Park | Hamler Summerfest / Hamler Community Park Inc. | SR 109, north edge of Hamler (Marion Twp). 13 ac purchased 1974. 100'×250' steel structure: basketball/tennis courts. Playground, ADA concrete, permanent fencing. Year-round community use + Summerfest/Country Fest venue. No tax money. Resolves HEN-F-10. Source: hamlersf.com. |
| 44 | T7 | Trail | Wabash Cannonball Trail | Northwest Ohio Rails-to-Trails Association (NORTA) | Multi-county: Fulton, Henry, Lucas, Williams. ~64-66 mi total (two forks). NORTA owns Henry/Fulton/Williams sections (~32 mi); Metroparks Toledo owns Lucas section. Former Wabash Railroad corridor; South Fork built 1855; North Fork ~1900. North Country NST certified portions. End points: Montpelier; Maumee and Liberty Center. Resolves HEN-F-07 (baseline WCT). |
| 45 | T7 | Trail Segment | Wabash Cannonball Trail - South Fork | Northwest Ohio Rails-to-Trails Association (NORTA) | Named fork of WCT. Maumee (Lucas Co.) → Liberty Center (Henry Co.); ~18 mi per NORTA. Henry County section ~6 mi in Washington Township. Surface: cinder, gravel, dirt, grass. Western terminus GPS 41.451114,-83.989429. |
| 46 | T7 | Access Point | WCT Henry CR 6C Trailhead | Northwest Ohio Rails-to-Trails Association (NORTA) | GPS 41.450715,-83.990451. ~1 mile east of Liberty Center between CR U and CR T. Small park: parking, picnic table, information kiosk. NORTA ownership ends at Henry CR 7 (Pleasantview Dr). Resolves HEN-F-07 second entry. Source: wabashcannonballtrail.org/trail-access/. |
| 47 | T7 | Site | Dr. John Bloomfield Home & Carriage House Museum | Henry County Historical Society (HCHS) | 229 W Clinton St, Napoleon, OH (across from Napoleon Public Library). Victorian Queen Anne house c. 1894, fully restored. Main HCHS museum. Collections: period furnishings, textiles, china, silver (1800s–1930s). Publicly accessible historic site. Gray-area for NAP — pipeline review. |
| 48 | T7 | Site | Henry County Historical Society Fairgrounds Historic Complex | Henry County Historical Society (HCHS) | Henry County Fairgrounds, Napoleon, OH. Outdoor historic buildings: Nathaniel Hartman Log Home c. 1860-1866, 1897 Emmanuel Lutheran One Room Schoolhouse & Museum, Ag Building, Smokehouse, c. 1910 Historic Gazebo. Managed by HCHS; physically on Fairgrounds property (T8/Ag Society land). Pipeline to resolve overlap with T8 Fairgrounds entity. |

---

## Held Entities

*(None yet)*

---

## Unresolved Baseline Seeds

All 40 baseline seeds from Sheet1 remain unconfirmed by an authoritative source. Key seeds to watch:

| Seed Name | Baseline Type | Notes |
|-----------|---------------|-------|
| Mary Jane Thurston State Park | State Park | Expect T2 confirmation; 591 ac; 1466 SR 65, McClure |
| North Turkeyfoot Wildlife Area | State Wildlife Area | Expect T2; 458 ac; CR 424, Liberty Center |
| Florida Wildlife Area | State Wildlife Area | Expect T2; 3 ac |
| Henry County Wildlife Area 1/2/3 | Public Hunting Area | HEN-F-03 — no detail; ODNR GIS needed |
| Glenwood Park | Napoleon City Park | 71.9 ac; has pool + 9-hole golf |
| East Riverdowns Park | Napoleon City Park | 28.9 ac; arboretum + tree nursery |
| Oakwood Park | Napoleon City Park | 52 ac |
| Vorwerk Park | Napoleon City Park | 24.5 ac |
| Meyerholtz Wildlife Park | Napoleon City Park | 21.5 ac |
| Wayne Park | Napoleon City Park | 13 ac |
| Oberhaus Park | Napoleon City Park | 15 ac |
| Ritter Park | Napoleon City Park | 5.6 ac; see HEN-F-02 |
| Boatramp Facility | Napoleon City Park | 14.8 ac; see HEN-F-01 |
| Swearingen Park | Napoleon City Park | 1 ac |
| Veterans Park | Napoleon City Park | 0.5 ac |
| Canal Falls / Florida Village Park | Village / Natural Feature | See HEN-F-06 |
| Crossroads Park | Deshler Village Park | Rail enthusiast viewpoint |
| Reservoir Park | Deshler Village Park | |
| Swimming Pool Park | Deshler Village Park | |
| Veteran's Park (Deshler) | Deshler Village Park | |
| Village Park (Deshler) | Deshler Village Park | |
| Deshler Reservoir 1 & 2 | Reservoir | HEN-F-04 |
| Hamler Community Park | Hamler Village Park | |
| Hamler Reservoir | Reservoir | HEN-F-05 |
| Holgate Village Park | Holgate Village Park | |
| Old School Park | Holgate Village Park | |
| Liberty Center Firemen's Park | Liberty Center Village Park | |
| Liberty Center Veterans Memorial Park | Liberty Center Village Park | |
| Steward Park | Liberty Center Village Park | |
| Wabash Cannonball Trailhead (CR 6C) | Liberty Center / Trailhead | See HEN-F-07 |
| Wabash Cannonball Trailhead (Train Station) | Liberty Center / Trailhead | See HEN-F-07 |
| Malinta Fields | Malinta Village Park | |
| Big Creek Park & Ball Fields | McClure Village Park | |
| New Bavaria Village Park | New Bavaria Village Park | |
| Field of Dreams Drive-In | Private | T8 candidate |

---

## Open Questions

1. Does Henry County have a park district or conservation district with land management authority, or are parks entirely municipal/state?
2. What is the exact governance of the Wabash Cannonball Trail in Henry County — the Wabash Cannonball Trail organization, a county entity, or individual municipalities?
3. Are the Henry County Wildlife Areas 1/2/3 distinct parcels or segments of one named wildlife area? ODNR GIS layer will resolve.
4. Is the Boatramp Facility a sub-feature (child site or access point) of Ritter Park, or a separate park with independent parcel?
5. Is Canal Falls a natural feature, a named trail access point on the Buckeye Trail, or simply the local name for the Florida Village Park area?
6. Does the Maumee River Water Trail (staged in Defiance run) have formal named access points within Henry County that should be staged as Access Point entities here?
7. Is the Henry County Outdoor Education Center (from Copilot sheet) a public-access entity or school/program use only?
8. Is the Henry County Historical Society Complex a public-access site qualifying for the project?

---

## Next Steps

1. Begin Tier 1 — Federal & OSM discovery
   - Run Overpass query for Henry County polygon
   - Check NPS, USFWS, BLM, USACE for Henry County holdings
   - Confirm North Country NST presence (already staged in DEF run — note here, do not re-stage)
   - Confirm Maumee River Water Trail presence and identify any Henry County–specific access points
2. Proceed to Tier 2 — ODNR Parks, Wildlife, Forestry, Water Trails
   - Priority: Mary Jane Thurston SP, North Turkeyfoot WA, Florida WA, Henry County WAs 1–3
3. Continue tier-by-tier through T8 per protocol

---

## Pre-Discovery Checklist — Tier 1 (Federal / OSM) — COMPLETE 2026-04-20

### Federal Datasets
- [x] Overpass API — Henry County bbox query (boundary=protected_area, leisure=nature_reserve, landuse=military) — null
- [x] NPS — no NPS land in Henry County
- [x] USFWS — no refuges; nearest are Ottawa NWR + Cedar Point NWR (Ottawa Co, Lake Erie)
- [x] BLM — no BLM surface holdings in NW Ohio
- [x] USACE NID — dam query: only Lock No. 44 (historic canal lock, no USACE ownership); no flood control projects
- [x] North Country NST — confirmed passing through Henry County (OSM rel 11140513); cross-ref DEF run; not re-staged
- [x] Maumee River Water Trail — T2 ODNR entity; Henry County APs will be documented at T2
- [x] USFS — Wayne NF is SE Ohio; null for Henry County
- [x] DoD — no military installations in Henry County
- [x] Tribal — no federally recognized tribes with land in Henry County

---

## Pre-Discovery Checklist — Tier 2 (State — ODNR)

Complete before running any Tier 2 searches. Check off as visited.

### ODNR Parks & Watercraft
- [x] Mary Jane Thurston State Park — 1466 SR 65, McClure OH 43534; 105 ac (ODNR) / 591 ac (baseline) — acreage conflict; staged T2. Phone: (419) 832-7662. Manager: Jeremy Babcock.
- [x] ODNR State Parks listing for NW Ohio — no other state parks in Henry County confirmed

### ODNR Division of Wildlife
- [x] North Turkeyfoot Wildlife Area — 458 ac, 2 mi SE of Liberty Center; staged T2
- [x] Florida Wildlife Area — 3 ac, 1 mi NE of Florida; staged T2
- [x] Henry County Wildlife Area 1, 2, 3 — confirmed 3 distinct units from Hunting Area Maps; PDF locations unavailable (redirect failed); staged T2 with location TBD
- [x] ODNR Hunting Area Maps — Henry County 1, 2, 3 confirmed; PDF URLs documented in records
- [x] ODNR Fishing Lake Maps — NW Ohio list extracted; no Henry County fishing lakes
- [x] ODNR River/Stream Fishing Maps — Maumee River confirmed as NW Ohio entry; AP discovery deferred

### ODNR Water Trails
- [x] Maumee River Water Trail — ODNR page JS-rendered; cross-referenced to DEF run (staged there); Henry County APs deferred
- [x] ODNR water trail map PDF — not fetchable (JS-rendered page)

### ODNR Forestry
- [x] ODNR Division of Forestry — null confirmed; no state forests in NW Ohio

### Ohio Nature Preserves
- [x] ODNR Division of Natural Areas & Preserves — DNAP pages fully JS-rendered; no Henry County SNPs identified in any source; null documented

### H2Ohio / Wetland Restoration
- [x] H2Ohio program — JS-rendered (650K chars, no Henry County data); null documented

### ODNR Scenic Rivers
- [x] Maumee State Scenic River — staged as T2 Site; ODNR Scenic Rivers pages JS-rendered; confirmed via MJTSP page reference

### OHC
- [ ] Ohio History Connection — HTTP 503 site maintenance; PENDING (HEN-F-09)

### ODOT / OTIC
- [x] ODOT rest areas — null (no limited-access highways in Henry County; JS-rendered page)
- [x] OTIC — not applicable (no Ohio Turnpike in Henry County)

### Cardinal Collection / New Deal Sites
- [x] Cardinal Collection (hub.catalogit.app) — no MJTSP folder found; no child Sites identified from this source

---

## Pre-Discovery Checklist — Tier 3 (District) — COMPLETE 2026-04-20

### District Candidates Checked
- [x] Henry Soil & Water Conservation District — `http://www.henryswcd.com` (HTTP only; HTTPS SSL cipher mismatch). Home, About, H2Ohio pages fully fetched. Est. 1955. Mission: agricultural drainage and conservation tech assistance; 400+ mile ditch maintenance program. No land ownership, no public-access natural areas. Null confirmed.
- [x] County park district — None identified. Henry County has no standalone park district under ORC Chapter 1545.
- [x] Metropark affiliation — None. Lucas County Metro Parks (LCMP) does not extend into Henry County. No other metropark system present.
- [x] Conservancy district — None. MWCD is eastern Ohio; Miami Conservancy District is SW Ohio. No analogous district in NW Ohio.
- [x] Flood-control / watershed district — None. County drainage managed by SWCD and Henry County Engineer (T4 scope).
- [x] All 6 entity types (Site, Trail, Trail Segment, Trail Network, Site Network, Access Point) — null at T3.

---

## Pre-Discovery Checklist — Tier 4 (County) — COMPLETE 2026-04-21

### T4 Entities Enumerated (IMP-029 — before individual fetches)
- Miami & Erie Canal Towpath Hiking Trail (Henry County Park District)
- Independence Leg — MW&E Canal Towpath (Independence Dam SP → Village of Florida)
- Renegade Leg — MW&E Canal Towpath (Village of Florida → Napoleon)
- Napoleon Leg — MW&E Canal Towpath (Meyerholtz Park → Henry County Hospital)
- Damascus Leg — MW&E Canal Towpath (Henry County Hospital → SR 109)
- WideWater Section — MW&E Canal Towpath (SR 109 → Providence Dam Metropark, Wood County)

### Sources Checked
- [x] `henrycountyohio.gov` — county official website; CivicPlus CMS. Full sitemap enumerated. No parks or recreation department. No parks/trails pages. Government, Services, Business navigation only. No T4 natural areas entities from county main site.
- [x] `henrycountyohio.gov/362/Henry-County-Comprehensive-Plan` — Comprehensive Plan page; chapter list fetched. Natural Resources chapter PDF is binary (not text-extractable via fetch). Plan documents noted but not readable. No specific county-managed parks/trails identified from index.
- [x] `henrycountyengineer.com` — Henry County Engineer website; GIS data download page checked. No parks or trails layer. GIS layers: Parcels, Land Use, Streams, Maumee River ROW, Street Center Lines, FEMA Flood Data, Soils. No T4 natural areas entities.
- [x] `henrycountyohio.gov/178/Maumee-Valley-Resource-Conservation-Deve` — Maumee Valley RC&D; regional 10-county nonprofit headquartered in Defiance. No land ownership, no public-access natural areas. Not an entity.
- [x] `henrycountyohio.gov/174/Fair-Ag-Society` — Henry County Fair/Ag Society; 821 S Perry Street, Napoleon OH 43545. Henry County Agricultural Society governs the fair. T8 candidate (semi-public agricultural society per ORC Chapter 1711). Not T4.
- [x] `henrycountyhistory.org` — Henry County Historical Society; two sites: Bloomfield Home (229 W Clinton, Napoleon) and Historic Complex at Fairgrounds. HCHS is a private nonprofit. → T7 scope, not T4.
- [x] NRHP — 4 listed properties in Henry County: First Presbyterian Church (1990), Henry County Courthouse (1973), Henry County Sheriff's Residence and Jail (1981), St. Augustine's Catholic Church (1982). All are downtown Napoleon institutional buildings. None are outdoor natural areas or access points. Zero T4 records from NRHP.
- [x] `henrycountyparks.blogspot.com` / `henrycountyparks.org` — Henry County Park District (organized 2005, all-volunteer, county commissioner office address). Manages Miami & Erie Canal Towpath Hiking Trail on state-leased canal lands adjacent to Maumee River. 5 named segments mapped. Co-routes with Buckeye Trail (already staged DEF run) and North Country Trail (already staged DEF run). **KEY DISCOVERY — 6 T4 entities staged.**
- [x] Wabash Cannonball Trail — NORTA (Northwestern Ohio Rails-to-Trails Association, Inc., 501(c)3 nonprofit) governs Henry County section. → T7 scope via NORTA. Not T4.
- [x] TrekOhio `trekohio.com/henry/` — Lists only MJTSP and Independence Dam SP (both T2 state entities). No additional county-managed entities identified.
- [x] NRHP — no covered bridges, no public outdoor structures in Henry County.
- [x] ArcGIS / Henry County GIS Map gallery — JS-rendered; no downloadable parks/trails layer available.
- [x] `explorehenrycounty.com` — this is Henry County, Illinois tourism bureau (wrong state). No Henry County Ohio tourism bureau found.

### Governance Note
The Henry County Park District is **all-volunteer** and operates out of the Henry County Office Complex (1853 Oakwood Ave, Napoleon) — the county commissioner address. It does not appear to be a formal ORC Chapter 1545 park district with independent taxing authority. The T3 null result (no ORC 1545 park district) stands. The Park District is captured here at T4 as a county-affiliated volunteer organization operating under county government auspices.

---

## Pre-Discovery Checklist — Tier 5 (Township) — COMPLETE 2026-04-21

### OTA Active Township Roster — Henry County (from Townships_Officials2022-2023.xlsx)

| # | Township | 2020 Census Pop. | OTA Website Listed |
|---|----------|-------------------|--------------------|
| 1 | Washington | 2,619 | washtwphenry.com |
| 2 | Napoleon | 3,206 | — |
| 3 | Flatrock | 1,183 | — |
| 4 | Richfield | 983 | — |
| 5 | Damascus | 3,128 | — |
| 6 | Harrison | 1,038 | — |
| 7 | Liberty | 2,074 | — |
| 8 | Marion | 1,057 | — |
| 9 | Monroe | 1,381 | — |
| 10 | Bartlow | 1,042 | — |
| 11 | Pleasant | 1,097 | — |
| 12 | Ridgeville | 1,023 | — |
| 13 | Freedom | 1,209 | — |

**Source:** `Townships_Officials2022-2023.xlsx` (OTA 2022-2023 Roster), filtered for County Name = "Henry"; confirmed against Henry County Engineer township list at `henrycountyengineer.com/townships-municipalities/`.

### Bootstrap Error Documentation (§5.5 — Defunct/Non-Existent Township Check)

The following 4 names appeared in the original bootstrap township list but are **not** Henry County, Ohio townships per OTA roster or Henry County Engineer confirmation:

| Name | Status | Evidence |
|------|--------|----------|
| Tiffin | Bootstrap error | Not in OTA Henry County roster; Tiffin Township is in Seneca County, Ohio |
| Beaver Dam | Bootstrap error | Not in OTA Henry County roster; Beaver Dam is an unincorporated community in Hancock County, Ohio |
| Bloom | Bootstrap error | Not in OTA Henry County roster; Bloom Township is in Seneca County, Ohio |
| Monterey | Bootstrap error | Not in OTA Henry County roster; no Henry County municipality or township by this name |

These names were likely generated by confusing adjacent counties or Ohio-wide township name lists. None will be searched at T5. No §5.5 defunct investigation required — these are not defunct Henry County townships; they were never Henry County townships.

### T5 Entity Enumeration (IMP-029 — pre-search)

Per sub-procedure, individual township searches have not yet been run. No entities enumerated yet. This section will be populated as searches complete.

- Washington Township: NULL — website confirmed Henry County; no parks/trails (Cemetery, Maintenance, Zoning, Employment only)
- Napoleon Township: NULL — no township website; city of Napoleon parks are T6 scope
- Flatrock Township: NULL — no website; no parks (Girty's Island was defunct private 1900s recreation area)
- Richfield Township: NULL — no website; no parks
- Damascus Township: NULL — no website; Maumee River camping is informal private use, not township infrastructure
- Harrison Township: NULL — no website found (search dominated by wrong Harrison Township in Montgomery County)
- Liberty Township: NULL — no website; Liberty Center village parks are T6 scope
- Marion Township: NULL — no website; Hamler Community Park (13 ac, Ohio 109) owned by Hamler Summerfest association ("no tax money") → T8 candidate, not T5
- Monroe Township: NULL — no website (search dominated by wrong Monroe Townships in Clermont/Warren Counties)
- Bartlow Township: NULL — no website; Deshler village parks are T6 scope
- Pleasant Township: NULL — no website found
- Ridgeville Township: NULL — no website (North Ridgeville in search results is Lorain County — wrong)
- Freedom Township: NULL — no website (Freedom Twp Portage/Wood County results — wrong; Henry County has no official site)

### §4.2a Wrong-County Website Verification — High-Risk Townships

The following township names are common across Ohio and require §4.2a verification before treating any discovered website as Henry County authoritative:

- Washington (very common name)
- Liberty (common name)
- Monroe (common name)
- Harrison (common name)
- Marion (common name)
- Pleasant (common name)
- Freedom (common name)

Washington Township is the only OTA-listed website (`washtwphenry.com`) — must verify this is Henry County before treating as authoritative.

---

## Pre-Discovery Checklist — Tier 6 (Municipal) — IN PROGRESS

### Municipality List (IMP-029 — written before individual searches begin)

| # | Name | Type | Approx. Pop. (2020) | Official Website | Status |
|---|------|------|---------------------|-----------------|--------|
| 1 | Napoleon | City | ~8,749 | napoleonohio.com | PENDING |
| 2 | Deshler | Village | ~1,528 | TBD | PENDING |
| 3 | Holgate | Village | ~1,172 | TBD | PENDING |
| 4 | Liberty Center | Village | ~1,104 | lcvillage.com (per search result) | PENDING |
| 5 | Hamler | Village | ~619 | TBD | PENDING |
| 6 | McClure | Village | ~747 | TBD | PENDING |
| 7 | Florida | Village | ~267 | TBD | PENDING |
| 8 | Malinta | Village | ~257 | TBD | PENDING |
| 9 | New Bavaria | Village | ~67 | TBD | PENDING |
| 10 | Custar | Village | ~181 | TBD | PENDING |

**Note**: Map verification (IMP-015) runs as a SINGLE CONSOLIDATED PASS after all 10 municipalities' web discovery is complete.

### Baseline Seeds by Municipality (pre-known entities to verify)

**Napoleon (city):** Glenwood Park (71.9 ac, pool + golf), East Riverdowns Park (28.9 ac, arboretum + nursery), Oakwood Park (52 ac), Vorwerk Park (24.5 ac), Meyerholtz Wildlife Park (21.5 ac), Wayne Park (13 ac), Oberhaus Park (15 ac), Ritter Park (5.6 ac — HEN-F-02), Boatramp Facility (14.8 ac — HEN-F-01), Swearingen Park (1 ac), Veterans Park (0.5 ac)

**Deshler:** Crossroads Park, Reservoir Park, Swimming Pool Park, Veteran's Park, Village Park, Deshler Reservoir 1 & 2 (HEN-F-04)

**Holgate:** Holgate Village Park, Old School Park

**Liberty Center:** Liberty Center Firemen's Park, Liberty Center Veterans Memorial Park, Steward Park, Wabash Cannonball Trailhead at CR 6C (HEN-F-07), Wabash Cannonball Trailhead at Train Station (HEN-F-07)

**Hamler:** Hamler Community Park (T8 candidate — Summerfest association), Hamler Reservoir (HEN-F-05)

**McClure:** Big Creek Park & Ball Fields

**Florida:** Canal Falls / Florida Village Park (HEN-F-06)

**Malinta:** Malinta Fields

**New Bavaria:** New Bavaria Village Park

**Custar:** No baseline seeds

### Captured Source Data — T6 (IMP-030, populated at fetch time)

*(To be populated as municipality pages are fetched)*

---

## Captured Source Data

*(Populated at fetch time during discovery — verbatim tables from authoritative sources)*

*(None yet)*
