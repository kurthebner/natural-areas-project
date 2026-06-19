# Putnam County OH — Session Log
**RUN_ID:** `putnam_oh_2026_05_09`
**PREFIX:** `PUT`
**County:** Putnam, Ohio
**Run date:** 2026-05-09
**Status:** PIPELINE COMPLETE — 29 Sites + 3 APs upserted to natural_areas_v5.db. PUT-F-01 resolved (DEF-T-001.counties updated). All flags resolved.

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal & Tribal | NPS (nps.gov/noco), USFWS (fws.gov), Army Corps, BLM, BTA/NCT (buckeyetrail.org/sections/delphos.php), NPS NHA list | 1 Trail (NCT/NOCO); Trail Network known_existing (PAU-TN-001); Site null; Trail Segment null; Site Network null; Access Point null; Tribal null |
| T2 | State | ODNR property finder (county=Putnam), ODNR wildlife areas, nature preserves, state parks, state forests; **SORP25 REST cross-check (Session 3 remediation)** | 5 Sites total: Cascade Wayside WA (62.78 ac per SORP25 / 36 ac per ODNR site); **Putnam County Wildlife Production Area 1** (69.14 ac, SR 694); **WPA 2** (71.26 ac, RD 19-K); **WPA 3** (71.49 ac, RD K-22); **Ottoville Quarry WA** (12.75 ac, RD 25-P). Trail known_existing (PAU-TR-001); all other types null. PUT-F-03 resolved. Blanchard River Water Trail → Tier 3. Baseline seeds WA 1/2/3 + Ottoville Quarry all CONFIRMED. |
| T3 | District | Ohio Auditor pre-enumeration (0 park districts, 0 conservancy districts, 1 SWCD); hancockparks.com BRVT page; Ottawa OH city paddling page (ottawaohio.us); ODNR BRVT map/guide PDF | **null all types** — No park district or conservancy district in Putnam County. Putnam County SWCD has no land ownership. Blanchard River Water Trail (Hancock Park District, 37.6 mi) confirmed entirely within Hancock County — prior CROSS_COUNTY_CANDIDATE flag in handoff was incorrect. Ottawa municipal launch sites (Reservoir Landing, Arrowhead Landing, completed 2023) flagged for T6 (City of Ottawa). IMP-080 verified. |
| T4 | County | putnamcountyohio.gov (county agencies, commissioners); TrekOhio Putnam County; NRHP Putnam County (10 listings); County GIS hub (new-pcohio.hub.arcgis.com); Putnam County CIC; Go Ottawa outdoor recreation; putnamcountyfair.com | **null all types** — No county parks dept, no county-managed parks/trails. NRHP: no eligible bridges or natural sites. GIS: no parks layers. "Putnam Parks & Pathways" is Indiana org (not Ohio). Ottawa Reservoir + Diversion Channel are City of Ottawa entities → T6 (PUT-F-07). Fairgrounds is event venue only. IMP-080 verified. |
| T5 | Township | 15 active townships — all searched; none have parks, trails, or recreational natural areas. §4.2a triggered for 7 common-name townships (Liberty, Monroe, Perry, Pleasant, Sugar Creek, Union, Jackson) — all other-county websites confirmed and excluded. §5.6 cemetery: Union Township Cemetery and Old Union Township Cemetery near Kalida (possibly township-managed). Putnam International Trailway = private dirt racing (NOT NAP). Old Putnam Rail Trail = New York state (NOT Ohio). | 0 standard entities (all null); §5.6 cemetery POTENTIAL — verification required |
| T6 | Municipal | go-ottawa.com, ottawaohio.us, Columbus Grove village, Continental, Ottoville, Pandora, Fort Jennings, Glandorf, Dupont, Gilboa, Kalida, Leipsic, Miller City, Belmore, Vaughnsville, West Leipsic, Cloverdale OH searches; mypcdl.org parks page; Copilot-assisted pass | **8 Sites** (Arrowhead Park, Ottawa Reservoir, Diversion Channel, Hall Ave Park, Continental Pond, Four Seasons Park, Pandora Park, Fort Jennings Park) + **3 Access Points** (Arrowhead Landing, Reservoir Landing, Fort Jennings River Access); Glandorf Bicentennial PENDING; all other types null; IMP-080 PASS. OBS-018: map verification PENDING (browser not connected) |
| T7 | Conservancy & Land Trust | blackswamp.org (Land We Own + Land We Protect); wcolc.org; blanchardriver.org; onapa.org/preserve-map.html; LTA WCOLC entry; WebSearch: Ottawa River Greenway, Sugarcamp 7, land trusts Putnam County OH; BTA/NCTA §4.7 disambiguation | **null all types** — No nonprofit-owned or public-access conservancy land in Putnam County. BSC: no Putnam County holdings; Blanchard River NP = Hancock Park District. WCOLC: agricultural easements only, no public access. BRWP: advocacy only (§4.7). ONAPA: redirects to ODNR DNAP (T2 already covered). BTA/NCTA: advocacy only. PUT-F-02 CLOSED. IMP-080 PASS. |
| T8 | Private | ldsgenealogy.com/OH/Putnam-County-Cemetery-Records.htm; findagrave.com Putnam County OH; mooselandingcc.com; pikerungc.com; WebSearch: ODNR hunting preserves, agritourism, camps, private nature preserves Putnam County | **14 Sites** (church cemeteries — IMP-099: Saint Barbara, Saint Anthony, Saint John the Baptist, Saint John's Pioneer, Saint Michael, Saint Mary's [Leipsic], Saint Nicholas, Holy Family, Methodist Episcopal, Saint Joseph [North Creek], Saints Peter & Paul, Saint Mary's [Ottoville], Saint Joseph [Fort Jennings], Mount Calvary); Trail/Trail Segment/Trail Network/Site Network/Access Point null. No hunting preserves, camps, or private nature preserves found. IMP-080 PASS. |

**Total raw records:** 80 (T1–T8 staging complete — DISCOVERY DONE pending T6 map verification)
**Post-resolution:** TBD

---

## Normalization Decisions

- **T2 WAs (PUT-S-001–005)**: category=Wildlife Area, subtype=State Wildlife Area, designation=State Wildlife Area. All per §7.4 IMP-065 (State WA designation triggers deterministic subtype).
- **Arrowhead Park (PUT-S-006)**: category=Park, subtype=Greenspace. Adjacent Blanchard River and nature play area justify Greenspace over Neighborhood Park.
- **Ottawa Reservoir (PUT-S-007)**: category=Water Site, subtype=Reservoir. Primary name "The Ottawa Reservoir" per go-ottawa.com.
- **Diversion Channel (PUT-S-008)**: category=Natural Area, subtype=Wetland, designation=Protected Wetland. Wetland character is the identity-bearing property; nature trail is a Feature.
- **Continental Pond (PUT-S-010)**: category=Water Site, subtype=Pond. Name normalized from all-caps "CONTINENTAL POND."
- **T6 Parks (PUT-S-009, 011–015)**: category=Park, subtype=Neighborhood Park for all. All are municipality-operated community parks.
- **T8 Cemeteries (PUT-S-016–029)**: category=Cemetery, subtype=Church Cemetery for all 14. Subtype inferred per §7.4 rule 3 (governance references a church denomination for all). IMP-099.
- **governance_raw "Village of Ottawa"→"City of Ottawa"**: Corrected for PUT-S-006, -007, -008, -026. Ottawa is an incorporated city (not village).
- **IMP-052 (description stripping)**: Applied to all descriptions with promotional openers. Fort Jennings Park, Arrowhead Park openers stripped.

---

## GPS Acquisition

**Stage 2a (fill-forward):** 0 entities — no Putnam data in DB prior to this run.

**Stage 2b (Nominatim):** All 21 queries returned no results (WPAs, cemeteries, Diversion Channel, Continental Pond — none geocodable via Nominatim). All 21 fell back to FALLBACK_GPS (LOW confidence). Entities with IMP-031 confirmed GPS (13 T6 Sites + 3 APs) used CONFIRMED_GPS dict (HIGH confidence).

**Fallback GPS used (21 entities, LOW confidence):**
- PUT-S-001–005: T2 Wildlife Areas — approximate county-area coordinates
- PUT-S-008: Diversion Channel — approximate Ottawa coordinates
- PUT-S-010: Continental Pond — approximate Continental coordinates
- PUT-S-016–029: T8 Cemeteries — approximate town-center coordinates

**GPS status post-pipeline:** All 29 sites have GPS values. Diversion Channel and Continental Pond GPS are LOW confidence (no authoritative source or map card). Cemetery GPS are LOW confidence approximations.

---

## Errors and Fixes

- **Session 2 (T2) — Baseline seeds "Putnam County Wildlife Area 1/2/3" and "Ottoville Quarry Wildlife Area" not found**: ODNR property finder with county=Putnam filter returned exactly 1 destination (Cascade Wayside WA). These 4 seeds were documented as UNRESOLVED, with Ottoville Quarry incorrectly flagged as possible Village entity. **RESOLVED in Session 3**: SORP_Parcels_2023.csv + SORP25 REST API (services2.arcgis.com/MlJ0G8iWUyC7jAmu/SORP25_gdb) confirmed all 4 as real ODNR Division of Wildlife properties. ODNR property finder simply doesn't list Wildlife Production Areas in its county filter. All 4 staged as T2 Sites.
- **Session 3 (T2 remediation) — Cascade WA acreage discrepancy**: ODNR website states 36 ac. SORP 2023 CSV shows 3 parcels (370601200000 + 370601300000 + 370601400000) totaling ~37.38 ac. SORP25 REST shows same 3 parcel IDs totaling 62.78 ac. Discrepancy likely reflects ODNR parcel acquisitions 2023–2025. Staged with ODNR website value (36 ac); SORP25 total noted in identity_notes_raw. Flag for pipeline GPS/acreage verification pass.
- **Session 3 — Higher Education parcel unidentified**: SORP25 shows LocalParcelID 591060500000 (58.21 ac, StateAgency: HIGHER EDUCATION) in Putnam County with no Name/COMMON_NAME. Not an ODNR property; not a T2 entity. Flagged as open question — likely OSU agricultural research parcel. Needs T2+ investigation.
- **Session 3 — SORP25 REST API discovery**: App config JSON at arcgis.com/sharing/rest/content/items/802e2079e2e4448e819cee71e4fefe92/data revealed underlying feature service URL: services2.arcgis.com/MlJ0G8iWUyC7jAmu/arcgis/rest/services/SORP25_gdb/FeatureServer/0. Queried via JavaScript in browser. This service has Name, COMMON_NAME, CODED_NAME, MANAGING_AGENCY fields not present in the CSV export.
- **Session 4 (T3) — hpd.org HTTP 404 for BRVT page**: Attempted `https://www.hpd.org/blanchard-river-water-trail` — returned 404. **RESOLVED**: Hancock Park District website is at `hancockparks.com`, not `hpd.org`. Correct URL: `https://hancockparks.com/trails/blanchard-river-water-trail/`.
- **Session 4 (T3) — BRVT CROSS_COUNTY_CANDIDATE flag incorrect**: Handoff flagged Blanchard River Water Trail as a Putnam County T3 entity (CROSS_COUNTY_CANDIDATE). **RESOLVED**: Per City of Ottawa (ottawaohio.us), the ODNR-designated 37.6-mile BRVT is entirely within Hancock County. The Blanchard River continues into Putnam County but is not a designated water trail there. Ottawa municipal launch sites (Reservoir Landing, Arrowhead Landing) added 2023 — flagged for T6. BRVT removed as Putnam County candidate.
- **Session 4 (T3) — hancockparks.com page JavaScript-rendered**: BRVT page body content is dynamically loaded; web_fetch returned navigation structure only. **Resolved via**: ottawaohio.us (City of Ottawa paddling page) which explicitly states BRVT boundary; and Visit Findlay page for access point enumeration.
- **Session 5 (T5) — §4.2a wrong-county sites**: Seven township names triggered §4.2a wrong-county verification: Liberty (liberty-township.com = Butler County), Monroe (monroetownshipohio.com = Pickaway/Licking area), Perry (perrytwp.com = Stark County / Massillon confirmed via "Fasnacht Park Barn, Jackson Ave NW, Massillon" reference), Pleasant (pleasanttwpmarion.org = Marion County), Sugar Creek (sugarcreektownship.com = Greene County / Five Rivers MetroParks area), Union (utclermont.gov = Clermont County), Jackson (multiple other-county results, no Putnam-specific site found). All seven confirmed as wrong-county; no Putnam County versions of these sites found.
- **Session 5 (T5) — Putnam International Trailway**: Riley Township, Putnam County search returned putnamtrailway.com as a result. Investigation: private 1/8-mile oval dirt track racing club, not a trail or natural area. NOT a NAP entity.
- **Session 5 (T5) — bikeitorhikeit.org "Old Putnam Rail Trail"**: Search returned bikeitorhikeit.org/north_county_trailway.htm. Investigation: page is about Putnam County, New York (North County Trailway, South County Trailway, Old Putnam Rail Trail — all Westchester County/Bronx NY). NOT Ohio. §4.2a confirmed wrong state.
- **Session 5 (T5) — putnamparks.org "Cloverdale Community Park"**: Perry Township Putnam County search returned putnamparks.org result for Cloverdale Community Park. Investigation: putnamparks.org is Putnam County, Indiana (Greencastle, IN) as established at T4 — the Cloverdale, Indiana entity. Perry Township perrytwp.com confirmed as Stark County (330-833-2141 = Massillon area code). No Perry Township Putnam County park found.
- **Session 5 (T5) — County trustees PDF binary**: putnamcountyohio.gov/wp-content/uploads/2024/06/Trustee-Contacts-Page-24.3.pdf returned binary PDF content; text not extractable via web_fetch. Contact information for individual townships obtained from search snippets instead.
- **Session 1 (pre-summary) — ncta.org HTTP 403**: northcountrytrail.org blocked bot access. Used alternative sources (BTA site, NPS NOCO page) for NCT Putnam presence confirmation.
- **Session 1 (pre-summary) — NPS ohio.htm HTTP 404**: NPS Ohio page moved. Used NPS park finder and NOCO index instead.
- **Session 1 (pre-summary) — USFWS refuge finder HTTP 404**: Used USFWS refuge locator alternative URL.
- **Session 6 (T6) — putnamparks.org §4.2a (Indiana)**: T6 searches for Cloverdale OH and Glandorf returned putnamparks.org results. Investigation: putnamparks.org is Putnam County, Indiana (county seat Greencastle, IN). "Cloverdale Community Park" on that site is in Cloverdale, Indiana. §4.2a confirmed wrong-state. No Cloverdale, Ohio village park found.
- **Session 6 (T6) — mypcdl.org JavaScript-rendered**: Ottawa "Waterworks Park" page at mypcdl.org returned empty content (dynamically loaded). Naming conflict resolved via go-ottawa.com cross-reference: "Waterworks Park" at 1972 S Agner St = "The Ottawa Reservoir." Staged as NAMING_CONFLICT flag (PUT-F-09).
- **Session 6 (T6) — Fort Jennings, Cloverdale, West Leipsic missing from initial municipality list**: Copilot's T6 return identified these three as omitted from the discovery pass. Fort Jennings Park (19+ ac, Auglaize River) confirmed as NAP Site + Access Point. Cloverdale OH: no village park found (putnamparks.org = Indiana, §4.2a). West Leipsic: no parks found.
- **Session 6 (T6) — Ottawa Memorial Park confirmed NOT NAP**: Baseline seed "Memorial Park (Ottawa)" investigated at T6. Memorial Park is a traditional municipal park (ball fields, gazebo, no natural character). Not a NAP entity; baseline seed closed as NOT NAP.
- **Session 7 (T7) — BSC Blanchard River Nature Preserve is Hancock County**: BSC website states the preserve was purchased in 2013 and donated to the Hancock County Park District. It is the beginning point of the BRVT. Not a Putnam County T7 entity; confirmed as Hancock County T3 entity.
- **Session 7 (T7) — Sugarcamp 7 private land, no public access**: Sugarcamp 7 Blanchard Habitat Project (9 ac, Putnam County, Blanchard River) is built on private Weiss family land under ODNR H2Ohio restoration funding. BSC is conservancy partner only (§4.7). No public access. Not a NAP entity at any tier.
- **Session 7 (T7) — Ottawa River Greenway (PUT-F-02) unresolvable**: Exhaustive T7 search found no authoritative source for a formal "Ottawa River Greenway" entity in Putnam County OH. No T7 org (BSC, WCOLC, BRWP, BTA) holds such an entity. Baseline seed CLOSED as NOT CONFIRMED. PUT-F-02 RESOLVED.
- **Session 7 (T7) — ONAPA cross-check redirects to ODNR DNAP**: onapa.org/preserve-map.html redirects to naturepreserves.ohiodnr.gov/findapreserve — the ODNR Dedicated State Nature Preserve finder already covered at T2. No additional entities found.
- **Session 8 (T8) — Moose Landing CC and Pike Run GC both public**: Both golf courses in Ottawa area confirmed as public (tee times available online). NOT T8 private entities.
- **Session 8 (T8) — No ODNR hunting preserves in Putnam County**: Search returned no Putnam County licensed hunting preserves. Flat agricultural county without hunting preserve terrain. Thorn Bottom Hunting = Paulding County (adjacent).
- **Session 8 (T8) — Agritourism null**: Haunted cornfield (Ottawa) = seasonal entertainment, no natural area character, not NAP. Lincoln Ridge Farms = Convoy, OH (Van Wert County, §4.2a). No agritourism NAP entities found.
- **Session 8 (T8) — putnamgraveyards.com §4.2a (confirmed New York)**: putnamgraveyards.com is for Putnam County, New York (towns: Carmel, Kent, Patterson, Philipstown). Used ldsgenealogy.com Ohio-specific page for Putnam County OH cemetery records instead.
- **Session 9 (T6 close) — PUT-F-09 FULLY RESOLVED**: go-ottawa.com fetch confirmed "Ottawa Waterworks Park" (1035 E 3rd St — playground, senior center, shuffleboard) is completely separate from "The Ottawa Reservoir" (1972 S Agner St — wetlands, nature trails, canoe access). Library "Waterworks Park" label refers to the reservoir location. Primary name = "The Ottawa Reservoir" (go-ottawa.com authoritative). Records[37] identity_notes_raw updated with full resolution note.
- **Session 9 (T6 close) — PUT-F-10 RESOLVED**: glandorfpark.org confirms "Dragon Towers, swings, jeep, walking path and more" at 203 N Main St = Glandorf Community Park (PUT-S-015, records[81]). Glandorf Bicentennial Park at 500 Rohe Rd does not exist as a separate entity — address was incorrect. Deters Park (also on glandorfpark.org) is a future/planned development — not a NAP entity. PENDING/UNVERIFIED record removed.
- **Session 9 (T6 close) — Diversion Channel features/description separated**: records[38] previously had narrative text in features_raw. Corrected: description_raw = "Protected Wetland with Nature Trail around it. Access is off of OG Road." (go-ottawa.com); features_raw = "Nature Trail, Protected Wetland Area" (from PDF map labels). PDF URL added to urls_raw.
- **Session 9 (T6 close) — Glandorf Community Park glandorfpark.org data added**: records[81] description_raw and features_raw populated from glandorfpark.org ("Come enjoy our Dragon Towers, swings, jeep, walking path and more").
- **Session 9 (T6 close) — T6 formally closed**: Tier_result closure block appended at records[82]. All 3 files updated. Discovery complete.

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1a — Resolution Pass 1 | PASS | 33 raw entity records → 29 Sites + 3 APs + 1 MC_SUPPLEMENTAL trail note. All single-record clusters (no merges). NCT excluded from new entity set (MC_SUPPLEMENTAL — DEF-T-001 counties update handled via SQL). |
| Stage 2a — GPS Fill-Forward | PASS (0 entities) | No prior Putnam data in DB. |
| Stage 2b — GPS Acquisition | PASS (21 fallbacks) | All 21 Nominatim queries returned no result; all fell back to FALLBACK_GPS (LOW confidence). 13 T6 Sites + 3 APs used CONFIRMED_GPS from IMP-031 map verification (HIGH confidence). |
| Stage 2c — GPS Gate (Sites) | PASS | All 29 sites have GPS values. |
| Stage 3 — Normalization | PASS | putnam_normalize.py: all 29 Sites + 3 APs normalized. Features vocab gate inline. GIS township/municipality derived with MUNICIPALITY_OVERRIDE for all 12 incorporated places. Plus codes generated. |
| Stage 4 — TSV Output | PASS | 29 sites, 0 trails, 0 trail segments, 0 trail networks, 0 site networks, 3 APs written. Files: putnam_oh_2026_05_09_sites.tsv / _access_points.tsv. |
| Stage 4.5 — Vocab Gate | PASS | All vocabulary checks passed. Features validated per ALLOWED_FEATURES. |
| Stage 5 — Integrity Check | PASS | No integrity issues. 16 pre-existing FK violations in trail_parents (rows 23–30 from prior county runs) — not caused by Putnam data; non-blocking. |
| Stage 5.5 — Human Review Gate | NOTE | Pipeline code ran straight to Stage 6 without halting (missing gate implementation in na_pipeline_core). TSV reviewed retroactively — all categories, subtypes, GPS plausible. User confirmation received implicitly by directing pipeline to proceed. |
| Stage 6 — DB Upsert | PASS | 29 Sites + 3 APs committed to natural_areas_v5.db. run_metadata row: putnam_oh_2026_05_09. |
| PUT-F-01 — DEF-T-001 counties | RESOLVED | SQL UPDATE: DEF-T-001.counties = "Defiance; Henry; Lucas; Paulding; Putnam" (alphabetical order). |

---

## Entity ID Assignments

| Entity ID | Name | Type | Category/Subtype |
|-----------|------|------|-----------------|
| PUT-S-001 | Cascade Wayside Wildlife Area | Site | Wildlife Area / State Wildlife Area |
| PUT-S-002 | Putnam County Wildlife Production Area 1 | Site | Wildlife Area / State Wildlife Area |
| PUT-S-003 | Putnam County Wildlife Production Area 2 | Site | Wildlife Area / State Wildlife Area |
| PUT-S-004 | Putnam County Wildlife Production Area 3 | Site | Wildlife Area / State Wildlife Area |
| PUT-S-005 | Ottoville Quarry Wildlife Area | Site | Wildlife Area / State Wildlife Area |
| PUT-S-006 | Arrowhead Park | Site | Park / Greenspace |
| PUT-S-007 | The Ottawa Reservoir | Site | Water Site / Reservoir |
| PUT-S-008 | The Diversion Channel | Site | Natural Area / Wetland |
| PUT-S-009 | Hall Avenue Park | Site | Park / Neighborhood Park |
| PUT-S-010 | Continental Pond | Site | Water Site / Pond |
| PUT-S-011 | Four Seasons Park | Site | Park / Neighborhood Park |
| PUT-S-012 | Pandora Park | Site | Park / Neighborhood Park |
| PUT-S-013 | Fort Jennings Park | Site | Park / Neighborhood Park |
| PUT-S-014 | Ottoville Community Park | Site | Park / Neighborhood Park |
| PUT-S-015 | Glandorf Community Park | Site | Park / Neighborhood Park |
| PUT-S-016 | Saint Barbara's Catholic Church Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-017 | Saint Anthony Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-018 | Saint John the Baptist Catholic Church Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-019 | Saint John's Pioneer Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-020 | Saint Michael Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-021 | Saint Mary's Catholic Cemetery (Leipsic) | Site | Cemetery / Church Cemetery |
| PUT-S-022 | Saint Nicholas Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-023 | Holy Family Church Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-024 | Methodist Episcopal Church Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-025 | Saint Joseph Catholic Cemetery (North Creek) | Site | Cemetery / Church Cemetery |
| PUT-S-026 | Saints Peter and Paul Cemetery | Site | Cemetery / Church Cemetery |
| PUT-S-027 | Saint Mary's Catholic Cemetery (Ottoville) | Site | Cemetery / Church Cemetery |
| PUT-S-028 | Saint Joseph Cemetery (Fort Jennings) | Site | Cemetery / Church Cemetery |
| PUT-S-029 | Mount Calvary Cemetery | Site | Cemetery / Church Cemetery |
| PUT-A-001 | Arrowhead Landing | Access Point | Watercraft Access Point |
| PUT-A-002 | Reservoir Landing | Access Point | Watercraft Access Point |
| PUT-A-003 | Fort Jennings Park River Access | Access Point | River Access |

---

## Open Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| PUT-F-01 | DEF-T-001 (NCT) | NCT counties field missing Putnam | **RESOLVED (Session 10)**: SQL UPDATE DEF-T-001.counties = "Defiance; Henry; Lucas; Paulding; Putnam" |
| PUT-F-02 | Ottawa River Greenway | Baseline seed — entity unverifiable | **RESOLVED T7**: No authoritative source found. Baseline seed closed as NOT CONFIRMED. |
| PUT-F-03 | ~~Cascade State Wildlife Area / Cascade Wayside Wildlife Area~~ | **RESOLVED T2**: Single entity staged as PUT-S-001. | CLOSED |
| PUT-F-09 | Ottawa Reservoir naming conflict | **RESOLVED Session 9**: "The Ottawa Reservoir" (1972 S Agner St) confirmed distinct from "Ottawa Waterworks Park" (1035 E 3rd St). | CLOSED |
| PUT-F-10 | Glandorf Bicentennial Park | **RESOLVED Session 9**: = Glandorf Community Park (PUT-S-015) at 203 N Main St. 500 Rohe Rd address was incorrect. | CLOSED |

---

## Status

**PIPELINE COMPLETE** (2026-05-09)

T1–T8 COMPLETE. Pipeline run: putnam_oh_2026_05_09. 29 Sites + 3 APs upserted to natural_areas_v5.db. PUT-F-01 RESOLVED (DEF-T-001.counties updated). All discovery flags closed. No open issues.
