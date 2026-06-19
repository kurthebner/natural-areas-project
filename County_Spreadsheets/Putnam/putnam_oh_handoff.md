# Putnam County OH — Discovery Handoff
**RUN_ID:** `putnam_oh_2026_05_09`
**PREFIX:** `PUT`
**County:** Putnam, Ohio
**County Seat:** Ottawa
**Last updated:** 2026-05-09 — **PIPELINE COMPLETE.** 29 Sites + 3 APs upserted to natural_areas_v5.db. PUT-F-01 RESOLVED (DEF-T-001.counties updated). All flags closed. No open issues.

---

## Known Multi-County Entities (Bootstrap DB Check — IMP-104 §5)

Pre-discovery DB check run per `processing/na_cross_county_resolution_v5.1.md` §5.

| DB ID | Name | Type | Counties | Scenario | Action at Discovery |
|-------|------|------|----------|----------|---------------------|
| PAU-TR-001 | Miami and Erie Canal Towpath | Trail | Hamilton; Butler; Warren; Montgomery; Miami; Shelby; Auglaize; Allen; **Putnam**; Paulding | A (Paulding-anchored, Putnam presence documented) | At Tier 2: note KNOWN_MC, record PUT supplemental access points if found |
| PAU-TR-003 | Buckeye Trail — Delphos Section | Trail | Paulding; **Putnam**; Allen; Auglaize | A (Paulding-anchored) | At Tier 7: note KNOWN_MC:PAU-TR-003, document Putnam-specific presence |
| DEF-T-001 | North Country National Scenic Trail | Trail | Defiance; Henry; Lucas; Paulding | A (Defiance-anchored; Putnam missing from counties — flag PUT-F-01) | At Tier 1: MC_SUPPLEMENTAL:DEF-T-001; flag counties update needed |
| PAU-TN-001 | North Country National Scenic Trail (network) | Trail Network | Multi-state | A (known network) | At Tier 1: note KNOWN_MC:PAU-TN-001 |

**Held entities from other counties referencing Putnam:** None found in held_entities table.

---

## Tiers Completed

| Tier | Name | Status | Entity Count |
|------|------|--------|-------------|
| T1 | Federal & Tribal | COMPLETE | 1 Trail (NCT — MC_SUPPLEMENTAL:DEF-T-001); all other types null or known_existing |
| T2 | State | COMPLETE (remediated 2026-05-08) | 5 Sites: Cascade Wayside WA (36 ac ODNR / 62.78 ac SORP25); WPA 1 (69.14 ac); WPA 2 (71.26 ac); WPA 3 (71.49 ac); Ottoville Quarry WA (12.75 ac). Trail known_existing (PAU-TR-001). All 4 missed Sites added via SORP25 cross-check. |
| T3 | District | COMPLETE (null) | 0 entities — No park district or conservancy district in Putnam County. SWCD confirmed (no land). BRVT entirely Hancock County — CROSS_COUNTY_CANDIDATE flag corrected. Ottawa municipal launch sites flagged for T6. IMP-080 verified. |
| T4 | County | COMPLETE (null) | 0 entities — No county parks dept. No county-managed parks/trails. NRHP: 10 listings, no eligible natural sites or bridges. GIS: no parks layers. Ottawa Reservoir + Diversion Channel = T6. Baseline PUT-F-02 (Ottawa River Greenway) unresolved — not found as Ohio entity. IMP-080 verified. |
| T5 | Township | COMPLETE (null standard entities; §5.6 POTENTIAL) | 0 standard entities — all 15 townships searched; none have parks, trails, or recreational natural areas. §5.6: Union Township Cemetery / Old Union Township Cemetery near Kalida flagged for pipeline verification. IMP-080 verified. |
| T6 | Municipal | COMPLETE (2026-05-09) | 10 Sites + 3 Access Points (13 total). PUT-F-09 RESOLVED (Ottawa Reservoir ≠ Ottawa Waterworks Park). PUT-F-10 RESOLVED (Glandorf Bicentennial Park = Glandorf Community Park at 203 N Main St). 2 T6 defects corrected via map verification (Ottoville Community Park, Glandorf Community Park). GPS captured for 8 of 10 Sites + all 3 APs; Diversion Channel + Continental Pond GPS pending pipeline acquisition pass. |
| T7 | Conservancy & Land Trust | COMPLETE (null) | 0 entities — No nonprofit-owned or public-access conservancy land in Putnam County. BSC: no Putnam County holdings. WCOLC: agricultural easements only, no public access. BRWP: advocacy only. PUT-F-02 baseline seed unresolvable. IMP-080 verified. |
| T8 | Private | COMPLETE | 14 Sites (church cemeteries, IMP-099); Trail/Trail Segment/Trail Network/Site Network/Access Point null; no hunting preserves, no private nature preserves, no camps. IMP-080 PASS. |

---

## Tiers Remaining

- **T1 (Federal & Tribal)** — COMPLETE (2026-05-07). 1 Trail record (NCT); all other entity types null or known_existing. IMP-080 verified.
- **T2 (State)** — COMPLETE (remediated 2026-05-08). Original T2 pass (2026-05-07) staged Cascade Wayside WA only — DEFECTIVE (SORP not checked). Session 3 SORP25 cross-check added 4 missed ODNR Sites: WPA 1, WPA 2, WPA 3, Ottoville Quarry WA. All 4 baseline seeds (Wildlife Area 1/2/3 + Ottoville Quarry) now CONFIRMED. Acreage discrepancy on Cascade WA flagged (ODNR site: 36 ac; SORP25: 62.78 ac). Higher Education parcel (591060500000, 58.21 ac) unidentified — not an ODNR entity, not a T2 Site; open flag for follow-up. IMP-080 re-verified after remediation.
- **T3 (District)** — COMPLETE (null all types, 2026-05-08). Ohio Auditor pre-enumeration: 0 park/recreation districts, 0 conservancy districts in Putnam County. Putnam County SWCD verified (no land ownership). **Blanchard River Water Trail correction**: BRVT is entirely within Hancock County per City of Ottawa (ottawaohio.us) — "not a designated water trail beyond the last Findlay drop-in point." Prior CROSS_COUNTY_CANDIDATE flag in this handoff was incorrect. Ottawa, OH has 2 informal municipal launch sites (Reservoir Landing, Arrowhead Landing — added 2023) → flagged for T6 (City of Ottawa). HPD website corrected: `hancockparks.com` (not `hpd.org`). IMP-080 verified.
- **T4 (County)** — COMPLETE (null all types, 2026-05-08). No county parks department. No county-managed parks, trails, or natural areas. NRHP 10 listings — none eligible. GIS hub — no parks layers. "Putnam Parks & Pathways" confirmed as Indiana organization (putnamparks.org), not Ohio — baseline PUT-F-02 (Ottawa River Greenway) remains unresolved. Ottawa Reservoir (1972 S Agner St; natural trails, wetlands, canoe access, fishing) and Diversion Channel (protected wetland, nature trail, OG Road) are City of Ottawa entities → T6 (PUT-F-07). IMP-080 verified.
- **T5 (Township)** — COMPLETE (null all 6 standard types, 2026-05-08). All 15 active townships searched. No parks, trails, recreational sites, or access points found at any township. §4.2a wrong-county verification confirmed for 7 common-name townships: Liberty (Butler Co), Monroe (Pickaway/Licking area), Perry (Stark Co — perrytwp.com confirmed Massillon), Pleasant (Marion Co), Sugar Creek (Greene Co), Union (Clermont Co), Jackson (no Putnam-specific site). Notable false positives investigated and rejected: Putnam International Trailway (private dirt racing track, Riley Twp), Old Putnam Rail Trail (Putnam County NY, not Ohio). §5.6 cemetery: "Union Township Cemetery" and "Old Union Township Cemetery" near Kalida documented as POTENTIAL township-managed cemeteries; confirmation from authoritative source not obtained; flagged for pipeline verification. IMP-080 verified.
- **T6 (Municipal)** — COMPLETE (2026-05-09). Map verification pass (§4.4 / IMP-031 / OBS-018) complete. GPS captured for Arrowhead Park, Ottawa Reservoir, Hall Ave Park, Four Seasons Park (Kalida), Pandora Park, Fort Jennings Park, Ottoville Community Park, Glandorf Community Park, and all 3 APs. Diversion Channel + Continental Pond not found in Google Maps — GPS gaps noted; pipeline GPS acquisition pass will resolve. PUT-F-09 RESOLVED: "The Ottawa Reservoir" (1972 S Agner St) is distinct from "Ottawa Waterworks Park" (1035 E 3rd St); confirmed by go-ottawa.com fetch. PUT-F-10 RESOLVED: Glandorf Bicentennial Park (Dragon Towers + walking path) = Glandorf Community Park at 203 N Main St (PUT-S-015); glandorfpark.org confirms. 500 Rohe Rd address was incorrect. Deters Park (glandorfpark.org) confirmed as future/planned development — not a NAP entity.
- **T7 (Conservancy & Land Trust)** — COMPLETE (null all types, 2026-05-08). BSC/WCOLC/BRWP/BTA/ONAPA all checked. PUT-F-02 CLOSED.
- **T8 (Private)** — COMPLETE (2026-05-08). 14 church cemetery Sites staged. No hunting preserves, camps, or private nature preserves found.

---

## Key Active Flags

| Flag | Description | Resolution Path |
|------|-------------|-----------------|
| PUT-F-01 | DEF-T-001.counties missing Putnam — NCT confirmed through Putnam via BT Delphos Section route | Update DEF-T-001 during pipeline |
| ~~PUT-F-02~~ | ~~Ottawa River Greenway~~ | **CLOSED T7 (2026-05-08)**: No authoritative source for a formal "Ottawa River Greenway" entity in Putnam County OH. All T7 orgs checked (BSC, WCOLC, BRWP, BTA) — none hold an Ottawa River Greenway in Putnam County. Baseline seed NOT CONFIRMED. |
| PUT-F-03 | ~~Cascade State WA vs. Cascade Wayside WA — two baseline names for likely one ODNR entity~~ | **RESOLVED T2**: Official ODNR name = "Cascade Wayside Wildlife Area" (36 ac); "Cascade State WA" baseline seed is a misnaming |
| PUT-F-04 | Cascade WA acreage discrepancy: ODNR website = 36 ac; SORP 2023 CSV = ~37.38 ac (3 parcels); SORP25 REST = 62.78 ac (same 3 parcel IDs). Likely reflects ODNR land acquisition 2023–2025. | GPS acquisition pass + ODNR acreage verification at pipeline stage |
| PUT-F-05 | Higher Education state parcel (LocalParcelID 591060500000, ~58.21 ac per SORP25) in Putnam County — no Name, COMMON_NAME, or MANAGING_AGENCY in SORP25. Not an ODNR property. Likely OSU agricultural research station. Not a T2 Site unless public recreational access confirmed. | Research OSU AgResearch stations in Putnam County; check if public access exists |
| ~~PUT-F-06~~ | ~~Ottawa informal Blanchard River launch sites~~ | **RESOLVED T6 (2026-05-08)**: Staged as Access Points — Arrowhead Landing (parent: Arrowhead Park) and Reservoir Landing (parent: The Ottawa Reservoir). Both City of Ottawa. |
| ~~PUT-F-07~~ | ~~Ottawa Reservoir + Diversion Channel~~ | **RESOLVED T6 (2026-05-08)**: Both staged as T6 Sites — The Ottawa Reservoir (NAMING_CONFLICT: also called "Waterworks Park" per Putnam County Library; see PUT-F-09) and The Diversion Channel. Both City of Ottawa. |
| ~~PUT-F-09~~ | ~~Ottawa Reservoir naming conflict~~ | **RESOLVED (map verification 2026-05-08)**: Google Maps has both "Water Works Park" (address entity, water utility) and "Ottawa reservoir walking path" (Hiking area, 4.0★, Opens 7 AM Sat) at 1972 S Agner St. Library name "Waterworks Park" confirmed. Primary name in staging: "The Ottawa Reservoir" (per go-ottawa.com authoritative municipal source); Google Maps names documented in identity_notes_raw. GPS: 41.0115931, -84.0226281. |
| ~~PUT-F-10~~ | ~~Glandorf Bicentennial Park — 14.5 ac, 500 Rohe Rd, Glandorf, OH~~ | **RESOLVED (2026-05-09)**: glandorfpark.org confirms "Dragon Towers, swings, jeep, walking path" at 203 N Main St = Glandorf Community Park (PUT-S-015). The 500 Rohe Rd address was incorrect. No separate park exists at 500 Rohe Rd. Deters Park (also on glandorfpark.org) is a future/planned development — not a NAP entity. PENDING/UNVERIFIED record removed from Entities Discovered table. |
| PUT-F-08 | Union Township Cemetery and Old Union Township Cemetery near Kalida — appear in genealogy databases (Find a Grave, Billion Graves) as township-named cemeteries. Possibly township-managed (§5.6 / IMP-099) but governance confirmation not obtained from authoritative source. | Pipeline verification: check Putnam County Auditor parcel layer for parcels coded as cemetery owned by Union Township trustees. If confirmed township-managed and publicly accessible, create NAP records with category: Cemetery. |

---

## County Context

**State:** Ohio
**County Seat:** Ottawa
**Major waterways:** Blanchard River (major), Ottawa River (tributary of Auglaize), Portage River headwaters, Miami and Erie Canal corridor (historic)
**Known park districts:** None (no dedicated Putnam County Park District confirmed; "Putnam Parks & Pathways" may be a trails advocacy group rather than a formal park district — verify at Tier 4)
**Metropark affiliations:** None

### Active Townships (15) — from Townships_Officials2022-2023.xlsx

| Township | Notes |
|----------|-------|
| Blanchard | No website URL in roster |
| Greensburg | No website URL in roster |
| Jackson | No website URL in roster |
| Jennings | No website URL in roster |
| Liberty | No website URL in roster |
| Monroe | No website URL in roster |
| Monterey | No website URL in roster |
| Ottawa | No website URL in roster |
| Palmer | No website URL in roster |
| Perry | No website URL in roster |
| Pleasant | No website URL in roster |
| Riley | No website URL in roster |
| Sugar Creek | No website URL in roster |
| Union | No website URL in roster |
| Van Buren | No website URL in roster |

**Note:** No township in Putnam County has a website listed in the 2022-2023 roster. All 15 are confirmed active townships (present in roster = not defunct). At Tier 5, begin with general web searches for each township trustee office before ODNR/county fallback.

### Municipalities (to confirm at Tier 6)

Ottawa (city), Columbus Grove (village), Continental (village), Dupont (village), Gilboa (village), Kalida (village), Leipsic (village), Miller City (village), Ottoville (village), Pandora (village), Belmore (village), Vaughnsville (village), Glandorf (village), McComb (village — may straddle Hancock/Putnam line), Mount Blanchard (village — Hancock?), Blanchard (unincorporated?). Exact list to be confirmed against Ohio Secretary of State or county auditor at Tier 6.

---

## Baseline Seeds

| Seed Name | Type (baseline) | Confirmed | Tier | Notes |
|-----------|----------------|-----------|------|-------|
| Cascade State Wildlife Area | Wildlife Area (~35 ac) | **RESOLVED** | T2 | PUT-F-03 RESOLVED: misnaming of Cascade Wayside Wildlife Area; not a separate entity |
| Cascade Wayside Wildlife Area | State Wildlife Area / Public Hunting (36 ac) | **YES** | T2 | Confirmed — official ODNR name; 36 ac; Division of Wildlife; Cloverdale OH |
| Ottoville Quarry Wildlife Area | State Wildlife Area | **CONFIRMED** | T2 | SORP25 confirmed: CODED_NAME OttvllQryWA, DIV_CODE 740, 12.75 ac (SORP25) / 7.73 ac (SORP2023), RD 25-P. OwnerAll: STATE OF OHIO | FISH HATCHERY. Staged as PUT-S-004. NOT a Village of Ottoville entity. |
| Putnam County Wildlife Area 1 | Public Hunting Area (ODW) | **CONFIRMED** | T2 | SORP25: "Putnam County Wildlife Production Area 1", CODED WldlfPA51WA, 69.14 ac (SORP25) / 40.57 ac (SORP2023), SR 694. Staged as PUT-S-002. ODNR property finder did not return this property. |
| Putnam County Wildlife Area 2 | Public Hunting Area (ODW) | **CONFIRMED** | T2 | SORP25: "Putnam County Wildlife Production Area 2", CODED WldlfPA52WA, 71.26 ac (SORP25), RD 19-K. Staged as PUT-S-003. |
| Putnam County Wildlife Area 3 | Public Hunting Area (ODW) | **CONFIRMED** | T2 | SORP25: "Putnam County Wildlife Production Area 3", CODED WldlfPA54WA, 71.49 ac (SORP25), RD K-22. Staged as PUT-S-005. |
| Ottoville Quarry Wilderness Area | Local Natural Area / Former Quarry (133+ bird spp) | **NOT T6 entity** | T6 | Village of Ottoville website does not reference any quarry natural area. ODNR "Ottoville Quarry Wildlife Area" already staged as T2 Site (PUT-S-004). Baseline seed unconfirmed as separate village entity. |
| Ottawa River Greenway | Natural Corridor / Riparian (Putnam P&P) | **NOT CONFIRMED** | T7 | T7 CLOSED: No formal entity found in Putnam County OH. BSC/WCOLC/BRWP/BTA all checked. PUT-F-02 CLOSED. |
| Local Nature Preserve (Unnamed) | Local Preserve (Putnam P&P) | No | T4 | Not formally designated; may not qualify as NAP entity |
| Memorial Park (Ottawa) | Municipal Park | **NOT NAP** | T6 | T6 confirmed: Memorial Park Ottawa is a traditional municipal park (ball fields, gazebo, no natural character). NOT a NAP entity. |
| Waterworks Park (Ottawa) | Municipal Park | **NAMING_CONFLICT** | T6 | T6: "Waterworks Park" (Putnam County Library) = "The Ottawa Reservoir" (go-ottawa.com) at 1972 S Agner St, Ottawa OH. Staged as PUT-S-007 "The Ottawa Reservoir." See PUT-F-09. |
| Hall Avenue Park (Columbus Grove) | Municipal Park | **YES** | T6 | Confirmed: Hall Ave, Columbus Grove. Staged as PUT-S-009. |
| Ottawa River (Putnam Co. segment) | Stream / Natural Corridor | No | — | GNIS feature entry; likely not a NAP entity (not managed trail or park) |
| Beaver Swamp (historical) | GNIS Swamp type | No | — | Historical/GNIS feature; likely not a NAP entity unless managed preserve found |
| Ottawa Reservoir | Reservoir | **YES (T6)** | T6 | Confirmed as City of Ottawa managed site with natural trails + wetlands. Staged as PUT-S-007 "The Ottawa Reservoir." NAMING_CONFLICT: see PUT-F-09. |
| Sugarcamp 7 Blanchard Habitat Project | Conservation Area (Private, 9 ac) | No | T8 | Private, not publicly accessible |

---

## Entities Discovered

*(Running table — appended as tiers complete)*

| Entity ID | Name | Type | Tier | Status |
|-----------|------|------|------|--------|
| (pending PUT-T-001) | North Country National Scenic Trail | Trail | T1 | Staged — MC_SUPPLEMENTAL:DEF-T-001; PUT-F-01 counties update required |
| (pending PUT-S-001) | Cascade Wayside Wildlife Area | Site | T2 | Staged — 36 ac per ODNR / 62.78 ac per SORP25 (PUT-F-04 acreage discrepancy flagged); ODNR Division of Wildlife, Cloverdale OH; PUT-F-03 resolved |
| (pending PUT-S-002) | Putnam County Wildlife Production Area 1 | Site | T2 | Staged — 69.14 ac (SORP25); SR 694; ODNR DOW; baseline seed confirmed; no ODNR web page |
| (pending PUT-S-003) | Putnam County Wildlife Production Area 2 | Site | T2 | Staged — 71.26 ac (SORP25); RD 19-K; ODNR DOW; baseline seed confirmed; no ODNR web page |
| (pending PUT-S-004) | Ottoville Quarry Wildlife Area | Site | T2 | Staged — 12.75 ac (SORP25); RD 25-P; ODNR DOW; baseline seed confirmed; NOT a village entity |
| (pending PUT-S-005) | Putnam County Wildlife Production Area 3 | Site | T2 | Staged — 71.49 ac (SORP25); RD K-22; ODNR DOW; baseline seed confirmed; no ODNR web page |
| (pending PUT-S-006) | Arrowhead Park | Site | T6 | Staged — City of Ottawa; 615 W Main St / 901 N Locust St; Blanchard River adjacent; GPS: 41.0182257, -84.0553962 |
| (pending PUT-S-007) | The Ottawa Reservoir | Site | T6 | Staged — City of Ottawa; 1972 S Agner St; PUT-F-09 RESOLVED; Google Maps = Water Works Park + Ottawa reservoir walking path (Hiking area); GPS: 41.0115931, -84.0226281 |
| (pending PUT-S-008) | The Diversion Channel | Site | T6 | Staged — City of Ottawa; OG Road; protected wetland + nature trail; PUT-F-07 resolved |
| (pending PUT-S-009) | Hall Avenue Park | Site | T6 | Staged — Village of Columbus Grove; 208 Hall Ave; GPS: 40.9153979, -84.0547706 |
| (pending PUT-S-010) | Continental Pond | Site | T6 | Staged — Village of Continental; South Main St; pond, fishing pier, walking path, natural area |
| (pending PUT-S-011) | Four Seasons Park | Site | T6 | Staged — Village of Kalida; north side of Kalida btw SR-115 and SR-114 (kalidaparks.com); walking paths, fishing pond, restrooms. GPS: 40.9911318, -84.207144 |
| (pending PUT-S-012) | Pandora Park | Site | T6 | Staged — Village of Pandora; 303 W Washington St (villageofpandora.com); Blanchard River adjacent; GPS: 40.9493331, -83.9644403 |
| (pending PUT-S-013) | Fort Jennings Park | Site | T6 | Staged — Village of Fort Jennings; 22922 OH-189; Auglaize River adjacent (fjfortfest.com); GPS: 40.9023506, -84.2947787 |
| (pending PUT-A-001) | Arrowhead Landing | Access Point | T6 | Staged — City of Ottawa; Arrowhead Park; Blanchard River; GPS: 41.0182257, -84.0553962 |
| (pending PUT-A-002) | Reservoir Landing | Access Point | T6 | Staged — City of Ottawa; Ottawa Reservoir site; Blanchard River; GPS: 41.0115931, -84.0226281 |
| (pending PUT-A-003) | Fort Jennings Park River Access | Access Point | T6 | Staged — Village of Fort Jennings; Auglaize River; GPS: 40.9023506, -84.2947787 |
| ~~[REMOVED]~~ | ~~Glandorf Bicentennial Park~~ | ~~Site~~ | ~~T6~~ | PUT-F-10 RESOLVED — Glandorf Bicentennial Park = Glandorf Community Park (PUT-S-015) at 203 N Main St. No separate park at 500 Rohe Rd exists. PENDING record removed. |
| (pending PUT-S-014) | Ottoville Community Park | Site | T6 | T6 DEFECT — staged during map verification pass (IMP-031). 287 Church St, Ottoville OH 45876; GPS: 40.9343759, -84.3418784. Google Maps 4.8★ (19 reviews). |
| (pending PUT-S-015) | Glandorf Community Park | Site | T6 | T6 DEFECT — staged during map verification pass (IMP-031). 203 N Main St, Glandorf OH 45848; glandorfpark.org; Blanchard River adjacent; GPS: 41.0328993, -84.0792131. Google Maps 4.7★ (122 reviews). |

---

## Held Entities

*(None at bootstrap)*

---

## Unresolved Baseline Seeds

T1+T2 resolved: 6 confirmed (NCT/trail via multi-county DB; Cascade Wayside WA; WPA 1; WPA 2; WPA 3; Ottoville Quarry WA), 1 resolved-as-duplicate (Cascade State WA = Cascade Wayside WA). Remaining 9 seeds unresolved — see Baseline Seeds table.

---

## Open Questions

1. ~~Does Putnam County have a formal park district?~~ — RESOLVED T4: No park district. "Putnam Parks & Pathways" = Indiana org (putnamparks.org). PUT-F-02 CLOSED.
2. ~~Are "Cascade State WA" and "Cascade Wayside WA" the same entity?~~ — RESOLVED T2: Same entity. PUT-S-001.
3. ~~Is "Ottoville Quarry Wilderness Area" separate from "Ottoville Quarry Wildlife Area"?~~ — RESOLVED T6: No separate village entity found. Ottoville Community Park (PUT-S-014) staged at Ottoville; the ODNR property (PUT-S-005) is on RD 25-P, not Church St. Likely same entity with informal naming variation.
4. ~~Does the NCT physically enter Putnam County?~~ — RESOLVED T1: Yes, via BT Delphos Section. MC_SUPPLEMENTAL note on DEF-T-001. PUT-F-01 resolved post-pipeline.
5. ~~Municipality list for Putnam County~~ — RESOLVED T6: Ottawa, Columbus Grove, Continental, Kalida, Pandora, Fort Jennings, Ottoville, Glandorf, Cloverdale, Leipsic, Miller City, New Cleveland + small villages (Belmore, Vaughnsville, Dupont, Gilboa, West Leipsic).
6. ~~Does Ottawa Reservoir have public access?~~ — RESOLVED T6: Yes. City of Ottawa manages it as public open space (wetlands, nature trail, canoe access). PUT-S-007.

---

## Next Steps

~~1. Complete Tier 1 discovery~~ — DONE
~~2. Hand Tier 2 to Copilot / complete Tier 2~~ — DONE
~~3. Begin Tier 3 (District)~~ — COMPLETE (null).
~~4. Begin Tier 4 (County)~~ — COMPLETE (null).
~~5. Begin Tier 5 (Township)~~ — COMPLETE (null all standard entity types).
~~6. Begin Tier 6 (Municipal)~~ — COMPLETE.
~~7. Begin Tier 7 (Conservancy & Land Trust)~~ — COMPLETE (null).
~~8. Begin Tier 8 (Private)~~ — COMPLETE (14 church cemetery Sites).
~~9. Begin pipeline~~ — **COMPLETE (2026-05-09).** 29 Sites + 3 APs upserted. PUT-F-01 resolved. Run ID: putnam_oh_2026_05_09.

**Optional follow-ups (non-blocking):**
- **PUT-F-05**: Identify Higher Education parcel 591060500000 (~58 ac, Putnam County) — likely OSU AgResearch. Determine if public recreational access exists.
- **Codify SORP as mandatory T2 supplemental source**: SORP25 REST API should be queried at T2 for every Ohio county to catch ODNR Wildlife Production Areas the property finder website misses.
- **Cemetery GPS refinement**: 14 T8 cemetery GPS values are LOW confidence (town-center approximations). Could be improved by individual geocoding or field verification in a future pass.
- **Diversion Channel / Continental Pond GPS**: Both have LOW-confidence fallback GPS. Future GPS acquisition via county GIS or satellite imagery cross-reference would upgrade confidence.

**PUTNAM COUNTY COMPLETE.**

---

### Tier 6 — Municipal (PENDING/UNVERIFIED 2026-05-08)

| Source | URL | Content | Entities Found |
|--------|-----|---------|----------------|
| go-ottawa.com — Outdoor Recreation | https://www.go-ottawa.com/explore-ottawa/project-six-sz8wl-dy87p | Ottawa Reservoir (natural trails, wetlands, canoe, fishing); Diversion Channel (protected wetland, nature trail); Arrowhead Park (fishing pond, shelter, Blanchard River); Reservoir Landing launch (2023); Arrowhead Landing launch (2023) | PUT-S-006, PUT-S-007, PUT-S-008, PUT-A-001, PUT-A-002 |
| ottawaohio.us — Recreation on the Blanchard | https://ottawaohio.us/2217/Recreation-On-The-Blanchard | Confirms Arrowhead Landing + Reservoir Landing added 2023; BRVT entirely Hancock County | PUT-A-001, PUT-A-002 |
| Columbus Grove village website | https://www.columbusgroveohio.com | Hall Avenue Park confirmed (shelter, restrooms, walking path, pond) | PUT-S-009 |
| Continental village / area sources | search + maps | Continental Pond (South Main St; fishing pier, walking path, natural area) | PUT-S-010 |
| Village of Ottoville | search + maps | Four Seasons Park (308 North St; walking trail, wooded area) | PUT-S-011 |
| Village of Pandora | search + maps | Pandora Park (East Putnam St; fishing pond, nature walk) | PUT-S-012 |
| Village of Fort Jennings | search + maps | Fort Jennings Park (19+ ac; borders Auglaize River; river access, walking trails) | PUT-S-013, PUT-A-003 |
| Village of Glandorf | search + maps | Glandorf Bicentennial Park (500 Rohe Rd; 14.5 ac; walking path, playground — borderline) | PENDING PUT-F-10 |
| Putnam County Library — mypcdl.org | https://www.mypcdl.org/parks | Lists Ottawa "Waterworks Park" at 1972 S Agner St = same as Ottawa Reservoir (PUT-F-09 naming conflict) | PUT-F-09 |
| Villages confirmed null (no NAP entities) | Dupont, Gilboa, Kalida, Leipsic, Miller City, Belmore, Vaughnsville, Cloverdale OH, West Leipsic | All searched; no parks/trails meeting NAP qualifications found | null |

### Tier 5 — Township (COMPLETE 2026-05-08, null)

| Source | URL / Contact | Content | Notes |
|--------|---------------|---------|-------|
| All 15 township web searches | General web search per township | No Putnam-specific township websites found for any of the 15 townships. None have dedicated parks or recreation pages. | All 15 confirmed active (present in OTA roster = not defunct) |
| §4.2a wrong-county sites confirmed and excluded | liberty-township.com (Butler Co); monroetownshipohio.com (Licking/Pickaway area); perrytwp.com (Stark Co — Massillon); pleasanttwpmarion.org (Marion Co); sugarcreektownship.com (Greene Co); utclermont.gov (Clermont Co) | All confirmed as other-county; not Putnam County | Common Ohio township names requiring §4.2a verification |
| Putnam International Trailway | putnamtrailway.com | Private 1/8-mile oval dirt racing track in Riley Township near Pandora; "world's fastest 1/8th dirt track"; private membership club sitting among cornfields and Cranberry Run | NOT a NAP entity |
| bikeitorhikeit.org "Old Putnam Rail Trail" | bikeitorhikeit.org/north_county_trailway.htm | Page covers North County Trailway, South County Trailway, Old Putnam Rail Trail — all in Putnam County, NEW YORK (Westchester/Bronx). NOT Ohio. | Wrong-state §4.2a |
| Putnam County OH Cemetery Records | ldsgenealogy.com/OH/Putnam-County-Cemetery-Records.htm | Comprehensive list of 149 Putnam County OH cemetery resources organized by community. Predominately Catholic church cemeteries (heavily German-Catholic NW Ohio). Township-named: "Union Township Cemetery" (Fort Jennings area, Billion Graves) and "Old Union Township Cemetery" + "Union Township Cemetery" (Kalida area, Find a Grave/Billion Graves). No soldiers' relief or veterans township cemeteries found. | §5.6 cemetery — Union Township cemeteries flagged PUT-F-08 |

---

## Pre-Discovery Checklist — Tier 1 (Federal & Tribal) — COMPLETE

- [x] NPS — North Country National Scenic Trail (NOCO): https://www.nps.gov/noco/index.htm — loaded; maps page confirmed; NCT multi-state trail
- [x] NPS — Putnam County site search — no NPS-managed sites in county
- [x] USFWS — Refuge finder, Putnam County OH — 404 on county query; no NWR found
- [x] Army Corps of Engineers — no USACE impoundments in Putnam County
- [x] BLM — confirmed no Ohio BLM surface land (Wayne NF only, SE Ohio)
- [x] BTA — Delphos Section (buckeyetrail.org/sections/delphos.php) — page too large; Putnam confirmed via PAU-TR-003 DB record
- [x] Tribal — confirmed no tribal trust lands in Putnam County (Ottawa Tribe ancestral only)

---

## Pre-Discovery Checklist — Tier 2 (State) — FOR COPILOT

*Copilot handles web research; returns flat table. Claude writes YAML and verifies vocabulary.*

**Primary ODNR sources to fetch:**

- [ ] ODNR Wildlife Areas — Putnam County filter: https://ohiodnr.gov/discover-and-learn/safety-conservation/wildlife-management/wildlife-areas
- [ ] ODNR Public Hunting Areas — Putnam County: search "Putnam" on https://ohiodnr.gov/discover-and-learn/safety-conservation/wildlife-management/public-hunting-areas
- [ ] ODNR Nature Preserves — Putnam County: https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/nature-preserves
- [ ] Ohio Canal Lands — Miami and Erie Canal, Putnam County segment: https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/real-estate/ohio-canal-maps/miami-erie-canal-maps
- [ ] ODNR State Forests — Putnam County (confirm none): https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/state-forests
- [ ] ODNR State Parks — Putnam County (confirm none): https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/state-parks

**For each entity found, Copilot should capture:**

| Field | Notes |
|-------|-------|
| Name (exact from ODNR page) | |
| Entity type (Wildlife Area / Nature Preserve / State Forest / etc.) | |
| Acres | |
| Address or location description | |
| County (confirm Putnam) | |
| Managing division (Division of Wildlife / Division of Natural Areas & Preserves / etc.) | |
| URL of source page | |
| Any GPS coordinates listed | |
| Any trails mentioned | |
| Any access points / boat ramps / parking areas mentioned | |

**Specific seeds to investigate:**
- "Cascade State Wildlife Area" / "Cascade Wayside Wildlife Area" — are these the same entity? What is the official ODNR name?
- "Putnam County Wildlife Area 1/2/3" — enumerate all ODW public hunting areas in Putnam County with official names
- "Ottoville Quarry Wildlife Area" — confirm presence on ODNR list; get official name and acreage
- Miami and Erie Canal corridor in Putnam County — confirm ODNR management, any formally managed segments, any named access sites

**Copilot output format requested:** Flat table with one row per entity, columns as listed above. No YAML — Claude handles YAML.

---

## Captured Source Data

*(Populated at fetch time as sources are visited. GPS left blank at discovery; filled during map verification or GPS acquisition.)*

### Tier 4 — County (COMPLETE 2026-05-08, null)

| Source | URL | Content | Notes |
|--------|-----|---------|-------|
| Putnam County Ohio — County Agencies | https://putnamcountyohio.gov/county-agencies/ | Agencies: Airport, BDD, Elections, CSEA, Crime Victims, Dog Warden, ESC, Fairgrounds, GIS, Health Dept, Homecare Hospice, JFS, Library, OSU Extension, Planning Commission, Recycling, Red Cross, Soil Water, Veterans, WIC. **No parks or recreation department.** | No parks agency |
| Putnam County Commissioners | https://putnamcountyohio.gov/commissioners/ | Biographical content only; no parks resolutions or natural area mentions | No relevant content |
| TrekOhio — Putnam County | https://trekohio.com/putnam/ | Lists only 1 entity for Putnam County: Cascade Wildlife Area (state, 35 ac) — already staged as T2 | State entity only |
| NRHP — Putnam County Ohio | https://nationalregisterofhistoricplaces.com/oh/putnam/state.html | 10 NRHP listings: Bridenbaugh Schoolhouse (private museum), Columbus Grove Municipal Pool (T6 municipal), Edwards House (private/vacant), Gilboa Main Street HD (commercial), Huber Block (private), Leipsic City Hall (local govt), Ottawa Waterworks Building (vacant local), Putnam County Courthouse (govt), Round Barn (private), St. John the Baptist Church (private). No bridges, no publicly accessible natural sites. | No T4 NAP entities |
| Putnam County GIS Hub | https://new-pcohio.hub.arcgis.com/pages/downloads | Data layers: Aerials, Boundaries, Hydro, Land Features, Parcel Data, Transportation. Applications: Real Estate, Health Providers, Election Results, Flood Data. **No parks or recreation layers.** | No parks layers |
| Putnam County CIC | https://putnamcountyohio.com/projects/ | Economic development projects (manufacturing, housing) only | No natural areas |
| Go Ottawa — Outdoor Recreation | https://www.go-ottawa.com/explore-ottawa/project-six-sz8wl-dy87p | City of Ottawa parks/recreation: Ali's Dog Park, Arrowhead Park (nature trails, canoe, fishing), YMCA track, Ottawa Memorial Park, **Ottawa Reservoir** (1972 S Agner St — natural trails, wetlands, canoe, fishing), Ottawa Waterworks Park, Putnam Paddle Co. (private), **Diversion Channel** (protected wetland + nature trail, OG Road). All are City of Ottawa municipal entities. | T6 entities identified |
| Putnam County Fairgrounds | https://www.putnamcountyfair.com/ | 1490 E 2nd St, Ottawa; annual county fair venue; no natural area or trail access | Not a NAP entity |

---

### Tier 3 — District (COMPLETE 2026-05-08, null)

| Source | URL | Content | Notes |
|--------|-----|---------|-------|
| Ohio Auditor — Putnam County entity search | https://ohioauditor.gov/auditsearch/search.aspx | Park/Recreation District: 0 results. Conservancy District: 0 results. SWCD: 1 — Putnam County Soil and Water Conservation District. Other (metro parks, etc.): 0 results. | Pre-enumeration per IMP-075 §3.0 |
| Putnam County SWCD | https://putnamswcd.org | District operational; no land ownership found; services = technical assistance and education only | SWCD confirmed — no land |
| Hancock Park District — BRVT page | https://hancockparks.com/trails/blanchard-river-water-trail/ | HPD primary BRVT manager; 37.6 mi; page JS-rendered (no body text extracted) | HPD is at hancockparks.com, not hpd.org |
| Visit Findlay — BRVT page | https://visitfindlay.com/places/blanchard-river-water-trail/ | 37.6-mile ODNR State Water Trail; 11 access points all in Hancock County: Blanchard River Nature Preserve, Island Park, Jackson Landing, Riverbend Recreation Area, Eastpoint Area, Zonta Landing, Waterfalls Area, Riverside Landing, Great Karg Well Historical Site, Liberty Landing, Blanchard Landing | All 11 APs in Hancock County |
| Ottawa OH — Recreation on the Blanchard | https://ottawaohio.us/2217/Recreation-On-The-Blanchard | **Key finding**: "Although not a designated water trail beyond the last Findlay drop-in point, paddlers can continue west for approximately 17 miles on the Blanchard River and find multiple drop-in points along the way at Gilboa and Ottawa." Ottawa added 2 informal launch sites in 2023: Reservoir Landing (Water Treatment Plant) and Arrowhead Landing (Arrowhead Park). | Confirms BRVT is Hancock County only; Ottawa sites are undesignated municipal APs → T6 |

---

### Tier 2 — State (COMPLETE 2026-05-07)

| Source | URL | Content | GPS Captured |
|--------|-----|---------|-------------|
| ODNR Property Finder — Putnam County filter | https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property?county=Putnam | **1 destination found**: Cascade Wayside Wildlife Area — "This 36-acre wildlife area is located in Putnam County." Division of Wildlife badge. | No |
| SORP_Parcels_2023.csv (full statewide download) | https://experience.arcgis.com/experience/802e2079e2e4448e819cee71e4fefe92/ | Putnam County: 193 rows total. NATURAL RESOURCES: 13 parcels, 178.40 ac. HIGHER EDUCATION: 1 parcel (591060500000), 32.99 ac, no name. TBD: 24 parcels including Miami Erie Canal lands (6 parcels, ~43.65 ac). TRANSPORTATION: 154 parcels. CSV Name/Owner fields blank for all NR parcels — names only obtainable via REST API or map click. | No |
| SORP25 REST API — Putnam County NATURAL RESOURCES query | https://services2.arcgis.com/MlJ0G8iWUyC7jAmu/arcgis/rest/services/SORP25_gdb/FeatureServer/0 | 7 NR features returned. Properties: (1) Cascade Wayside WA — 3 parcels (CscdWysdWA, DIV_CODE 740): 370601200000 (33.62 ac, SR 114), 370601300000 (22.44 ac, END SR 694@SR 114), 370601400000 (6.72 ac, RD 22-K). (2) WPA1: 090370100000, 69.14 ac, SR 694, WldlfPA51WA. (3) WPA2: 370602100000, 71.26 ac, RD 19-K, WldlfPA52WA. (4) WPA3: 400600100000, 71.49 ac, RD K-22, WldlfPA54WA. (5) Ottoville Quarry WA: 250600900000, 12.75 ac, RD 25-P, OttvllQryWA, OwnerAll: STATE OF OHIO | FISH HATCHERY. Higher Ed parcel 591060500000: 58.21 ac, no Name/COMMON_NAME. | No |
| ODNR Cascade Wayside WA page | https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/cascade-wayside-wildlife-area | Name: CASCADE WAYSIDE WILDLIFE AREA. Description: "This 36-acre wildlife area is located in Putnam County. It is comprised of mostly woodlands along the Auglaize River." Natural Features: River, Woods. Activities: Hunting, Birding, Fishing. Address: Cloverdale, OH 45827. Phone: (419) 424-5000. Emergency: #ODNR / 911. Map PDF: "Cascade Wildlife Area Map [pdf]" available on page. | No |
| ODNR Property Finder — nature preserves | https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/nature-preserves | No Putnam County nature preserves found | No |
| ODNR State Parks | (knowledge-confirmed) | No state parks in Putnam County | No |
| ODNR State Forests | (knowledge-confirmed) | No state forests in Putnam County | No |

---

## Pre-Discovery Checklist — Tier 8 (Private)

**Enumerated 2026-05-08 before fetching individual pages (IMP-029).**

| Entity | Location | Type | Status | Notes |
|--------|----------|------|--------|-------|
| Moose Landing Country Club | 17374 SR 694, Ottawa | Golf Course | [x] NOT T8 | PUBLIC golf course (explicitly stated); tee times available; not private/member-only |
| Pike Run Golf Club | 10807 County Rd H, Ottawa | Golf Course | [x] NOT T8 | PUBLIC tee times available; not private/member-only |
| ODNR licensed hunting preserves | Putnam County | Hunting Preserve | [x] COMPLETE | No Putnam County hunting preserves found. Thorn Bottom = Paulding County. Rural flat agricultural county — no hunting preserve terrain. |
| [STAGED] Saint Barbara's Catholic Church Cemetery | Cloverdale | Church Cemetery | [ ] PENDING | IMP-099 |
| [STAGED] Saint Anthony Cemetery | Columbus Grove | Church Cemetery | [ ] PENDING | St. Anthony Parish; IMP-099 |
| [STAGED] Saint John the Baptist Catholic Church Cemetery | Glandorf | Church Cemetery | [ ] PENDING | IMP-099; also Saint John's Pioneer Cemetery (possibly separate historical section) |
| [STAGED] Saint Michael Cemetery | Kalida | Church Cemetery | [ ] PENDING | St. Michael Parish; IMP-099 |
| [STAGED] Saint Mary's Catholic Cemetery | Leipsic | Church Cemetery | [ ] PENDING | St. Mary Parish; IMP-099 |
| [STAGED] Saint Nicholas Cemetery | Miller City | Church Cemetery | [ ] PENDING | St. Nicholas Parish; IMP-099 |
| [STAGED] Holy Family Church Cemetery | New Cleveland | Church Cemetery | [ ] PENDING | Holy Family Parish; IMP-099 |
| [STAGED] Methodist Episcopal Church Cemetery | North Creek | Church Cemetery | [ ] PENDING | IMP-099 |
| [STAGED] Saint Joseph Catholic Cemetery | North Creek | Church Cemetery | [ ] PENDING | IMP-099 |
| [STAGED] Saints Peter and Paul Cemetery | Ottawa | Church Cemetery | [ ] PENDING | St. Peter & Paul Parish; IMP-099 |
| [STAGED] Saint Mary's Catholic Cemetery / Immaculate Conception | Ottoville | Church Cemetery | [ ] PENDING | IMP-099 |
| [STAGED] Saint Joseph Cemetery | Fort Jennings | Church Cemetery | [ ] PENDING | St. Joseph Parish; IMP-099 |
| [STAGED] Mount Calvary Cemetery | Fort Jennings | Church Cemetery | [ ] PENDING | Likely Catholic; IMP-099 |
| Scout camp / church camp / retreat center | Putnam County | Camp | [x] SEARCH DONE | No results for Putnam County; null |
| Private nature preserve / university natural area | Putnam County | Preserve | [x] SEARCH DONE | No results; null |
| Agritourism / farm trails | Putnam County | Private recreation | [x] COMPLETE | Haunted cornfield (Ottawa) = entertainment, not NAP. Lincoln Ridge Farms = Van Wert County (§4.2a). Null. |

---

## Pre-Discovery Checklist — Tier 7 (Conservancy & Land Trust)

**Enumerated from initial searches. Write to handoff before fetching individual pages (IMP-029).**

| Organization | URL | Status | Notes |
|-------------|-----|--------|-------|
| Black Swamp Conservancy | https://blackswamp.org/properties/land-we-own/ + /land-we-protect/ | [x] COMPLETE | No Putnam County holdings. Blanchard River NP donated to Hancock Park District 2013. Sugarcamp 7 (Putnam Co.) = private land, ODNR H2Ohio, no public access. |
| West Central Ohio Land Conservancy | https://www.wcolc.org/land-protection | [x] COMPLETE | Agricultural easements only; no public-access preserves in Putnam County. Excluded per §4.2. |
| ONAPA preserve map | https://www.onapa.org/preserve-map.html | [x] COMPLETE | Redirects to ODNR DNAP finder — already checked T2. No dedicated state nature preserves in Putnam County. |
| Land Trust Alliance directory | https://landtrustalliance.org/land-trusts/explore/west-central-ohio-land-conservancy-oh | [x] COMPLETE | WCOLC confirmed only relevant LTA member in area; page returned empty. |
| Buckeye Trail Association (BTA) | https://buckeyetrail.org | [x] COMPLETE | §4.7 confirmed: advocacy/maintenance only, not a landowner. |
| Ottawa River Greenway | (none found) | [x] COMPLETE | No authoritative source found. PUT-F-02 CLOSED as baseline seed NOT CONFIRMED. |
| Blanchard River Watershed Partnership | https://www.blanchardriver.org/ | [x] COMPLETE | §4.7: watershed education/advocacy org; not a landowner. Sugarcamp 7 = private land, no public access. |

---

## Pre-Discovery Checklist — Tier 6 (Municipal) — COMPLETE 2026-05-08

**All municipalities searched. Map verification pass still required (OBS-018).**

| Municipality | Type | Status | Result |
|-------------|------|--------|--------|
| Ottawa | City | [x] COMPLETE | PUT-S-006 Arrowhead Park; PUT-S-007 Ottawa Reservoir; PUT-S-008 Diversion Channel; PUT-A-001 Arrowhead Landing; PUT-A-002 Reservoir Landing |
| Columbus Grove | Village | [x] COMPLETE | PUT-S-009 Hall Avenue Park |
| Continental | Village | [x] COMPLETE | PUT-S-010 Continental Pond |
| Ottoville | Village | [x] COMPLETE | PUT-S-011 Four Seasons Park |
| Glandorf | Village | [x] COMPLETE | BORDERLINE — Glandorf Bicentennial Park (14.5 ac) PENDING map verification (PUT-F-10) |
| Fort Jennings | Village | [x] COMPLETE | PUT-S-013 Fort Jennings Park; PUT-A-003 Fort Jennings Park River Access |
| Dupont | Village | [x] COMPLETE | null — no parks |
| Gilboa | Village | [x] COMPLETE | null — no parks |
| Kalida | Village | [x] COMPLETE | null — no parks |
| Leipsic | Village | [x] COMPLETE | null — no parks |
| Miller City | Village | [x] COMPLETE | null — no parks |
| Pandora | Village | [x] COMPLETE | PUT-S-012 Pandora Park |
| Belmore | Village | [x] COMPLETE | null — no parks |
| Vaughnsville | Village | [x] COMPLETE | null — no parks |
| Cloverdale | Village | [x] COMPLETE | null — putnamparks.org = Indiana (§4.2a); no Ohio Cloverdale village park found |
| West Leipsic | Village | [x] COMPLETE | null — no parks |

---

## Pre-Discovery Checklist — Tier 5 (Township)

**Protocol**: Search each township in order. For each: (1) find trustee website; (2) verify wrong-county before treating as authoritative (§4.2a — mandatory for common names: Jackson, Liberty, Monroe, Perry, Pleasant, Union); (3) check for parks, trails, open space, cemeteries (§5.6 mandatory cemetery search for every township).

| Township | OTA Website | Searched | Trustee URL Found | Parks/Trails Result | Cemetery Result |
|----------|-------------|----------|-------------------|---------------------|-----------------|
| Blanchard | None in roster | [x] | None found | None | Church/private cemeteries only |
| Greensburg | None in roster | [x] | None found | None | St. John Baptist Catholic Church Cemetery (Glandorf) — church managed |
| Jackson | None in roster | [x] | ⚠️ §4.2a — no Putnam-specific site found | None | None identified |
| Jennings | None in roster | [x] | None found | None | None identified |
| Liberty | None in roster | [x] | ⚠️ §4.2a — liberty-township.com = Butler County | None | Monroe Cemetery (Continental area) |
| Monroe | None in roster | [x] | ⚠️ §4.2a — monroetownshipohio.com = Licking/Pickaway area | None | Monroe Cemetery (Continental/Monroe Twp area) |
| Monterey | None in roster | [x] | None found | None | Cemetery records (FamilySearch) — no township-managed confirmed |
| Ottawa | None in roster | [x] | ottawatwp@yahoo.com / 419-523-6214 | None | Pioneer Cem, Riley Creek Cem, Sts. Peter & Paul — church managed |
| Palmer | None in roster | [x] | None found | None | Wing Cemetery — private family cemetery |
| Perry | None in roster | [x] | ⚠️ §4.2a — perrytwp.com = Stark Co (Massillon confirmed) | None | Cascade Cemetery, St. Barbara's Catholic — church managed |
| Pleasant | None in roster | [x] | ⚠️ §4.2a — pleasanttwpmarion.org = Marion County; trustees at Columbus Grove | None | Osborne Cem, Campbell Family Cem — private/church |
| Riley | None in roster | [x] | rileytownship.org — §4.2a pending; trustees: 102 Monroe St, Pandora | None (Putnam Intl Trailway = private racing) | Pleasant Ridge Cem, Pandora Cem — community managed |
| Sugar Creek | None in roster | [x] | ⚠️ §4.2a — sugarcreektownship.com = Greene County | None | Sugar Ridge Cemetery, Blanchard Cemetery |
| Union | None in roster | [x] | ⚠️ §4.2a — utclermont.gov = Clermont County; trustees: Hermiller, D. Niese, R. Niese | None | **Union Twp Cem + Old Union Twp Cem near Kalida — PUT-F-08** |
| Van Buren | None in roster | [x] | None found | None | None identified |

---

### Tier 1 — Federal & Tribal (COMPLETE 2026-05-07)

| Source | URL | Content | GPS Captured |
|--------|-----|---------|-------------|
| NPS NOCO Maps | https://www.nps.gov/noco/planyourvisit/maps.htm | Maps page — confirms NCT as multi-state trail across 8 states including Ohio; no Putnam-specific data | No |
| NCTA Ohio | https://northcountrytrail.org/the-trail/ohio/ | Ohio state page — response too large for text extraction; NCT confirmed in Ohio via DB PAU-TR-003 cross-reference | No |
| BTA Delphos Section | https://buckeyetrail.org/sections/delphos.php | **Confirmed via Chrome** — Counties: Auglaize, Allen, Putnam, Paulding. Miles: 46.5 total / 22.7 off-road. Chapter: Miami and Erie Canal Chapter. Trail towns: Spencerville, Kossuth, Fort Jennings, Delphos, Ottoville. Putnam County towns: **Fort Jennings, Ottoville**. Northern terminus at Junction (Paulding County). Abutting sections: St. Marys (south), Defiance (north). Emergency services table explicitly lists Putnam County (sheriff 419.523.3208). No federal trailheads documented for Putnam County portion. Page last updated Mar 14, 2026. | No |
| USFWS fws.gov | https://www.fws.gov/ | Refuge finder — county-specific query returned 404; no NWR in Putnam County | No |
| USACE | (knowledge-based) | No USACE impoundments in Putnam County confirmed | No |
| BLM | (knowledge-based) | No Ohio BLM surface land; Wayne NF in SE Ohio only | No |
| NPS NHA list | (knowledge-based) | No NHA designation covers Putnam County | No |
| Tribal/BIA | (knowledge-based) | No tribal trust land in Putnam County; Ottawa Tribe ancestral connection only | No |

