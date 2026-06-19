# Hancock County, Ohio — Session Handoff
**RUN_ID:** `hancock_ohio_2026_05_12`  
**County:** Hancock County, Ohio  
**County seat:** Findlay  
**Prefix:** `HAN` | ID format: `OH-HAN-{TYPE}-{SEQ}` (four-digit zero-padded)  
**Last updated:** 2026-05-17 (LOCAL-007 cemetery supplemental upsert complete — 54 new cemetery sites added)
**Session status:** PIPELINE COMPLETE + LOCAL-007 RESOLVED. Run ID: `hancock_ohio_2026_05_12`. 236 sites total in DB (182 original pipeline + 10 golf course supplemental + 54 cemetery supplemental). 71 cemetery sites total (17 original + 54 LOCAL-007). Cemetery supplemental run_id: `hancock_ohio_LOCAL007_cem_suppl`. GPS: 49/54 new cemeteries resolved via Nominatim; 5 GPS-null (Frontiers Repose, High Bank, Indian Grove, Maple Lawn, Riley Creek). TSV regenerated: `hancock_ohio_2026_05_12_sites.tsv` now contains 166 Hancock County sites. One soft block: Portage Township Cemetery name (contact trustees at 9313 CR 203, Van Buren OH 45889 — does not block DB entry). Cross-county candidates flagged: HAN-S-098 (Bluffton Village Park), HAN-T-012 (Old Mill Stream Scenic Byway), HAN-T-023 (Bluffton Bicycle Pathway).

---

## County Context

**Major municipalities:**
- **Findlay** (city, county seat) — largest park system; managed by City of Findlay Parks & Recreation
- **Fostoria** (city) — straddles Hancock and Seneca counties; confirm park addresses before staging
- **Bluffton** (village/city) — straddles Hancock and Allen counties; confirm addresses
- **Arlington** (village)
- **Arcadia** (village)
- **Benton Ridge** (village)
- **McComb** (village)
- **Mount Blanchard** (village)
- **Van Buren** (village)
- **Vanlue** (village)

**Park district:** Hancock Park District — primary district-level land manager; website: https://www.hancockparks.com

**GIS note:** The regional `Parks_and_Open_Space_7241389496048841555.csv` covers a 15-county set (DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI). **Hancock County is NOT in this set.** Do not apply this CSV for Tier 4 or Tier 6 cross-checks.

**Known Multi-County Entities (DB check — IMP-104):** DB queried 2026-05-12. **None found.** No existing entities in the database have counties fields referencing Hancock County. This county is clean for all entity tables (sites, trails, trail_segments, trail_networks, site_networks, access_points, held_entities).

---

## Tiers Completed

| Tier | Result | Date | Notes |
|------|--------|------|-------|
| T1 — Federal & Tribal | 0 entities | 2026-05-12 | All 6 entity types null. Sources: NPS Ohio listing (10 units, none in Hancock), NHAs (Ohio & Erie Canalway and NAHA — neither in Hancock), NCT route (eastern Ohio only), USACE Ohio project list (38 projects, none in NW Ohio), USFWS (404 on find endpoint; NW Ohio confirmed as Ottawa NWR + Cedar Point NWR, both Ottawa County), USFS Wayne NF (SE Ohio only), BLM (SE Ohio only), DoD (none), Tribal (none). Evidence in staging file `tier_null_results` and `tier_1_entity_type_results`. |
| T2 — State (ODNR) | 47 records | 2026-05-13 | 15 Sites (Van Buren SP + Campground + 6 WAs + 7 WPAs), 3 Trails (Hiking/MTB/Bridle systems at VBSP), 19 Trail Segments (9 hiking loops + 2 MTB loops + 4 bridle loops + Purple + 3 connectors at VBSP), 10 Access Points (VBSP main entrance, Equestrian Day Use Area, Horseman's Camp, Paddling Access, + 6 WA parking areas). Trail Segment lengths/difficulties from official park map rev. 10/2025. All 6 entity types documented in staging file. IMP-080 verified. IMP-104 clean (no multi-county entities). Sources in `tier_2_entity_type_results` and `tier_null_results`. Maps in `source_files/`. |
| T3 — District (HPD) | 53 records | 2026-05-13 | 20 Sites (Oakwoods NP, Litzenberg, Riverbend RA, 5 CAs, Aeraland, Blanchard River NP, Blue Rock NP, Centennial, Eastpoint, Great Karg Well, River Landings, Waterfalls, Jackson/Liberty/Blanchard Landings, Riverbend CA stub), 9 Trails (Heritage Trail, BRWT, BRGT, Riverwalk, Highline, Upland, Ladybug Loop, Backwoods, Old Mill Stream Scenic Byway [IDENTITY_FLAG]), 16 Trail Segments (Heritage Trail segments 1–16), 0 Trail Networks (null — no system-level identity found), 0 Site Networks (null — conservation areas not meeting threshold), 8 Access Points (BRWT: Blanchard River NP/Jackson/Riverbend RA/Waterfalls/Great Karg/Liberty/Blanchard; BRGT: Eastpoint kayak launch). IMP-080 PASSED. IMP-104: Old Mill Stream Scenic Byway flagged CROSS_COUNTY_CANDIDATE (Hancock+Putnam). COUNTY_VERIFY flags on Aeraland (Fostoria), Blanchard River NP (Forest/Hardin). Sources in `tier_3_entity_type_results`. |
| T4 — County | 1 record | 2026-05-13 | 1 Site: Hancock County Infirmary Cemetery (IMP-099 county cemetery; GPS 41.0512, -83.6888 from GNIS #1730821; Liberty Township). All other entity types null. County government has no parks department, no facilities, no trails. NRHP §3.3: 14 listings, no bridges/natural features. Commissioners agenda: no land acquisitions. Tourism CVB: all parks HPD/city/village. Golf courses: null. Soldiers relief cemetery: not found. IMP-080 PASSED. IMP-104 clean (no multi-county entities). Sources in `tier_4_entity_type_results`. |
| T6 — Municipal | 56 records (web complete) | 2026-05-14 | All 10 municipalities complete. 45 Sites + 10 Trails + 1 Site Network. Findlay (25S+3T+1SN), Fostoria (10S+6T LOCAL-003), Arlington (2S), Arcadia (0 T6 — HPD), Benton Ridge (0 T6 — HPD), Bluffton (4S+1T LOCAL-005 CROSS_COUNTY_CANDIDATE), McComb (1S), Mt. Blanchard (2S), Van Buren (1S), Vanlue (0 T6 — HPD). T3 additions: Arcadia Lions CP, Benton Ridge CP+Trail, Vanlue CP, Island Park+AP, Cloe Greiner CP (all HPD, 7 records). T5 defect remediated: Van Buren Sportsplex (Allen Twp). IMP-099 ✓ all 10. IMP-104 ✓ (6 multi-county records flagged). IMP-080 ✓. 64 null result blocks. MAP VERIFICATION PASS (IMP-015/IMP-031) PARTIAL — 2026-05-15. GPS captured for all cross-county entities (Bluffton LOCAL-005, Fostoria LOCAL-004), COUNTY_VERIFY flags updated (Aeraland RA, Blanchard River NP), Arlington (2), new T6 entities from this session. 45 records have GPS. Remaining GPS-blank: Findlay (29 single-county — defer to GPS Acquisition Module), Fostoria walking trails (7, derive from parent sites), Lake LeComte (1, no Maps entity), Bluffton Pool/Cemetery/Pathway (3, no Maps entities), Hoadley Park (1, new park). LOCAL-004 (Fostoria) STILL OPEN — GIS parcel verification needed for city parks at lon=-83.424 to -83.437 (Seneca County risk); Veterans Memorial Res. (lon=-83.455) and Lamberjack (lon=-83.437) more likely Hancock. LOCAL-005 (Bluffton) STILL OPEN — GIS parcel verification needed for Village Park/Buckeye Park/Pool/Pathway. T6 COMPLETE for pipeline purposes; GPS Acquisition Module handles remaining coordinates. |
| T7 — Conservancy / Land Trust | 0 entities | 2026-05-15 | All 6 entity types null. Sources: BSC (16 owned preserves all non-Hancock; Blanchard River NP donated to HPD — already T3; `partner_agencies_raw` updated in T3 record); TNC Ohio (8 preserves, NE/Central/Southern Ohio only); WRLC (NE Ohio organization — Hancock County outside service area); ONAPA map (redirects to ODNR nature preserves finder — same null confirmed T2); Ducks Unlimited (no Hancock County public-access easements); ODNR VPP (no Hancock County results). IMP-029 Pre-Discovery Checklist written. IMP-080 PASSED. IMP-104 clean. 6 entity type result blocks staged in `tier_7_entity_type_results`. |
| T8 — Private / Organizational | 1 entity (Camp Berry) + 5 T6 misses | 2026-05-16 | T8: 1 Site — Camp Berry (BSA/Scouting America, 360 ac, Hancock County, group rental access). T6 misses found and staged: Findlay Reservoir #1 Fishing Area (186 ac, City of Findlay/ODNR cooperative), Findlay Reservoir #2 Fishing Area (645 ac, City of Findlay/ODNR cooperative), Findlay Reservoir Dike Trail (5.3 mi dike trail), McComb Reservoirs 1 & 2 (Site, 6+20 ac, Village of McComb/ODNR), McComb Reservoir Walk Trail (1 mi paved). ODNR hunting preserves: no public registry; no Hancock County preserves found. Private golf: Fostoria CC = Seneca County (out of scope); Findlay CC already T4 note. Church/family cemeteries: all accounted for T4/T5/T6. eBird hotspots: all previously staged or roadside-only. IMP-029 Pre-Discovery Checklist written. IMP-080 PASSED. IMP-104 clean (all 6 new records single-county). 6 entity type result blocks staged in `tier_8_entity_type_results`. |

---

## Tiers Remaining

**ALL TIERS COMPLETE. PIPELINE COMPLETE.**

| Stage | Status | Notes |
|-------|--------|-------|
| T1–T8 Discovery | ✅ COMPLETE | 185 records in YAML |
| Resolution + Normalization | ✅ COMPLETE 2026-05-16 | 182 entities normalized (3 Allen County records excluded) |
| GPS Acquisition | ✅ COMPLETE 2026-05-16 | 69/102 sites, 13/19 APs with GPS; 13 WAs unresolvable; ~20 small parks not in OSM |
| TSV Output | ✅ COMPLETE 2026-05-16 | 6 TSV files in County_Spreadsheets/Hancock/ |
| DB Upsert | ✅ COMPLETE 2026-05-16 | run_id=hancock_ohio_2026_05_12; 182 entities in natural_areas_v5.db |

---

## Key Active Flags

| Flag ID | Issue | Status |
|---------|-------|--------|
| LOCAL-001 | Tiffin River Wildlife Area likely multi-county | **RESOLVED 2026-05-13** — Listed under Fulton County in ODNR Hunting Area Maps, NOT Hancock. Baseline seed was misattributed. Not staged for Hancock. Flag for Fulton County run. |
| LOCAL-002 | Blanchard River Water Trail may extend outside Hancock | **RESOLVED 2026-05-13** — Trail is 37.6 mi, ODNR-designated, but managed by Hancock Park District (per hancockparks.com). Per §4.6, goes to Tier 3 (District), not Tier 2. Discovery deferred to T3. |
| LOCAL-003 | Old Mill Stream Scenic Byway — entity type eligibility unclear | Open — assess during Tier 2/T8 |
| LOCAL-004 | Fostoria parks cross Hancock/Seneca county line | **RESOLVED 2026-05-16** — Fostoria city website (fostoriaohio.gov/parks-and-rec) explicitly states county for every park: City Park and Gray Park = **Hancock County**; Foundation Park, Buckley St Courts, Harmon Park, Jackson Park = Seneca County; Portage Park = Wood County. All 16 staged Hancock T6 Fostoria records confirmed Hancock County: City Park (Hancock per city), Gray Park (Hancock per city), City Pool (adjacent to City Park, Hancock), Fountain Cemetery (Hancock per OHGenWeb Hancock County cemetery list + 702 Van Buren St location), Reservoirs 1–6 and 6 walking trails (all in western Hancock portion, lon=-83.43 to -83.46). Seneca/Wood County parks correctly NOT staged. LOCAL-004 closed. |
| LOCAL-005 | Bluffton parks cross Hancock/Allen county line | **RESOLVED 2026-05-16** — County determinations made for all 5 Bluffton records. **Hancock County** (keep): Village Park (lat=40.883, County Line Rd — Hancock CVB confirmation), Bluffton Bicycle Pathway (CROSS_COUNTY_CANDIDATE, county_primary=Hancock, counties_raw=[Hancock,Allen]). **Allen County** (county_primary corrected in YAML): Buckeye Park (lat=40.899 — ~1.1 mi north of County Line Rd, Allen County per GPS), Bluffton Community Swimming Pool (205 Snider Rd — confirmed Allen County via Wiserbase), Maple Grove Cemetery (Columbus Grove-Bluffton Rd — confirmed Allen County via hometownlocator, BillionGraves, Mapcarta: Richland Township Allen County). Three Allen County records remain in Hancock YAML with county_primary=Allen — pipeline will route them to Allen County processing. LOCAL-005 closed. |
| LOCAL-006 | 7 Copilot-flagged speculative entries need verification | Open — do not stage until confirmed |
| LOCAL-007 | **Cemetery supplemental pass — RESOLVED 2026-05-17.** OhioGenealogyExpress Hancock index (70 unique names) cross-referenced against 16 already-staged cemeteries → 54 unstaged identified. All 54 upserted via `hancock_ohio_LOCAL007_cem_suppl`. IDs HAN-S-113–HAN-S-166. Subtypes: Church×7, Family×3, Private×1, Public×43. GPS: 49/54 resolved via Nominatim (MED confidence, OSM polygon). GPS-null (5): Frontiers Repose, High Bank, Indian Grove, Maple Lawn, Riley Creek. TSV regenerated: 166 Hancock sites. Sources added to handoff Captured Source Data below. | **RESOLVED 2026-05-17** |

---

## Baseline Seed Summary

Baseline internalized from two sources:

**Sheet1 (~57 unique real entries):** Seed list covering Hancock Park District sites, Findlay city parks, ODNR wildlife areas (numbered 1–7), Van Buren State Park, Tiffin River Wildlife Area, Findlay Reservoirs 1 & 2, Lake LeComte, Leipsic Reservoir, McComb Reservoirs. Sparse — no trail segments, no trail access points, no URLs for many entries.

**"from Copilot" sheet (135 rows, richer):** Expands on Sheet1 with trails, trail segments, trail access points, village parks, township parks. Adds GPS coordinates for ~15 Hancock Park District sites. Notes several entries as "may be Copilot overzealousness" — these require authoritative confirmation before staging. Key additions: Blanchard River Greenway Trail (+ 5 named segments), Heritage Trail, Blanchard River Water Trail, Van Buren Bridle Trail, Van Buren Lake Trail, Riverwalk, McComb Reservoir Trail, Findlay Reservoir Trail. Also adds Fostoria parks (City Park, Gray Park, Lake Mosier Park, Meadowlark Park), Fostoria-area lakes (Lake LeComte/Leipsic Reservoir, Daugherty Reservoir, Mosier Lake), village parks (Arcadia, Mt. Blanchard, Van Buren), township parks (Jackson, Liberty).

**Baseline seeds are prompts for discovery, not import-ready records.** Every seed must be confirmed through authoritative tier sources before staging.

**Speculative Copilot entries (verify before staging — flagged "may be Copilot overzealousness"):**
1. CSX Rail Corridor (Abandoned Segment) — "Closed (potential)" — not open to public
2. DEA Floodplain Restoration Zone — "Planned" — not yet realized
3. Findlay Airport Buffer Zone — "Restricted (partial)" — informal use only
4. Fostoria Greenbelt Edge Parcel — no known manager; "Open (informal)"
5. Old Findlay Landfill Green Zone — no signage; "Open (informal)"
6. Van Buren Rail Spur Edge — no known public access; "Open (informal)"
7. Blanchard River Flood Mitigation Parcels — FEMA acquisition program, not formal park

**Internal sub-components (will resolve as child records or be excluded per entity type rules):**
Brugeman Lodge, Litzenberg Activity Barn, Fort Findlay Playground, Nature Play Area (Oakwoods), Oakwoods Discovery Center, Observation Tower (Oakwoods), Riverside Bandshell, Lakefront Activity Center, Riverside Park Waterfalls, Guthrie Field, Remington Field, Hancock Field, Koehler Field, Marathon Diamonds, Roethlisberger Field, Riverside Island Bridge.

**Cemeteries (in scope per IMP-099 — some staged, others pending LOCAL-007 supplemental pass):**
Of the 5 baseline cemetery seeds: Mount Blanchard Cemetery (staged HAN-S-031, Delaware Twp T5), Van Horn Cemetery (staged HAN-S-022, Amanda Twp T5). Knollcrest Cemetery, Maple Grove Cemetery, and St. Michael Cemetery not yet staged — candidates for LOCAL-007 supplemental pass. OhioGenealogyExpress lists 77 total Hancock cemeteries; ~60 are unstaged.

---

## Entities Discovered

| Tier | Sites | Trails | Trail Segments | Trail Networks | Site Networks | Access Points | Total |
|------|-------|--------|----------------|----------------|---------------|---------------|-------|
| T1 — Federal | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| T2 — State | 15 | 3 | 19 | 0 | 0 | 10 | **47** |
| T3 — District | 25 | 10 | 16 | 0 | 0 | 9 | **60** *(+7 HPD community parks/APs added during T6: Arcadia Lions CP, Benton Ridge CP, Benton Ridge Trail, Vanlue CP, Island Park, Island Park AP, Cloe Greiner CP)* |
| T4 — County | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| T5 — Township | 15 | 0 | 0 | 0 | 0 | 0 | **15** *(+1 Van Buren Sportsplex/Allen Twp — T5 defect remediated)* |
| T6 — Municipal | 48 | 12 | 0 | 0 | 1 | 0 | **61** *(+5 T6 misses found during T8: Findlay Reservoir #1 Fishing Area, Findlay Reservoir #2 Fishing Area, Findlay Reservoir Dike Trail, McComb Reservoirs 1 & 2, McComb Reservoir Walk Trail)* |
| T7 — Conservancy | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| T8 — Private | 1 | 0 | 0 | 0 | 0 | 0 | **1** *(Camp Berry — BSA/Scouting America)* |
| **Running total** | **105** | **25** | **35** | **0** | **1** | **19** | **185** |

**T2 Sites (15):** Van Buren State Park, Van Buren SP Campground, Hancock County WA 1/3/4/5/6/7 (6 sites), Wildlife Production Areas 9/25/32/41/43/45/46 (7 sites).

**T2 Trails (3):** Van Buren SP Hiking Trails, Van Buren SP Mountain Bike Trails, Van Buren SP Bridle Trails.

**T2 Trail Segments (19):** 9 hiking loops (Green/Blue/Orange/Haiku/Sensory/Purple/Pink/Red/White/Yellow + Campground Connector/Day Use Connector/Cable Line Road), 2 MTB loops (Green/Blue), 4 bridle loops (Red/Pink/White/Yellow). Note: shared-treadway loops have parallel records under each parent trail.

**T2 Access Points (10):** Van Buren SP Main Entrance/South Trailhead, Equestrian Day Use Area, Horseman's Camp, Paddling Access; WA 1/3/4/5/6/7 parking areas.

**T3 Sites (20):** Oakwoods NP, Litzenberg Memorial Woods, Riverbend RA, Bright CA, Lehman CA, Indian Green–Worden CA, Lawrence CA, Vogelsong CA, Aeraland RA (COUNTY_VERIFY), Blanchard River NP (COUNTY_VERIFY — may be Hardin County), Blue Rock NP, Centennial Park, Eastpoint Area, Great Karg Well Historical Site, River Landings, Waterfalls Area, Jackson Landing, Liberty Landing, Blanchard Landing, Riverbend CA (stub — needs map verify).

**T3 Trails (9):** Heritage Trail (20.22 mi), Blanchard River Water Trail (37.6 mi, CROSS_COUNTY_CANDIDATE pending Blanchard River NP county verify), Blanchard River Greenway Trail, Riverwalk, Highline Trail (Aeraland), Upland Trail (Aeraland), Ladybug Loop Trail (0.3 mi, Blue Rock), Backwoods Trail (bridle, Litzenberg), Old Mill Stream Scenic Byway (IDENTITY_FLAG: 52-mi driving byway; CROSS_COUNTY_CANDIDATE Hancock+Putnam).

**T3 Trail Segments (16):** Heritage Trail segments 1–16 (totaling 20.22 mi). Segments 3/4 and 11/12 show duplicate text on HPD source page — verify via brochure PDF.

**T3 Access Points (8):** Blanchard River NP launch (BRWT start, COUNTY_VERIFY), Jackson Landing, Riverbend RA (BRWT midpoint/camping), Waterfalls Area portage, Great Karg Well portage, Liberty Landing (9.3mi float start), Blanchard Landing (BRWT end), Eastpoint Area kayak launch (BRGT east terminus).

**T5 Sites (14):** Bechtel Cemetery (Allen Twp), Van Horn Cemetery (Amanda Twp), Enon Valley Cemetery (Biglick Twp), Baker-Hamlin Cemetery (Cass Twp), Mount Blanchard Cemetery (Delaware Twp), Bishop Cemetery (Eagle Twp) [CONFIRMED 2026-05-16 — Find a Grave ID 39916 + OHGenWeb], Houcktown Cemetery (Jackson Twp) [BEST_CANDIDATE 2026-05-16 — WorldCat OGS publication confirms Houcktown Cemetery in Jackson Twp; 4 other cemeteries exist in township; basic audit non-naming; trustees at 15524 SR 37, Arlington OH to confirm], Bright Cemetery (Marion Twp), Elm Grove Cemetery (Marion Twp), Hasson Joint Cemetery (Orange Twp — joint entity), McComb Union Cemetery (Pleasant Twp — joint w/ Village of McComb), Portage Township Cemetery (Portage Twp) [UNCONFIRMED_NAME — audit reviewed 2026-05-16: Note 1 confirms "cemetery maintenance"; finding 2020-002 confirms cemetery revenue fund (fully corrected); no cemetery named in audit; 3 OGS candidates: Pleasant Hill/Ten Mile-Bethel/Thomas; contact trustees at 9313 CR 203, Van Buren OH 45889], Cannonsburg Joint Cemetery (Union Twp — joint entity), Arcadia Cemetery (Washington Twp). NULL townships: Blanchard, Liberty, Madison, Van Buren.

---

## Held Entities

*None yet.*

---

## Unresolved Baseline Seeds

All 57 Sheet1 seeds and 135 Copilot seeds remain unconfirmed. Confirmation occurs during tier discovery.

---

## Open Questions

1. Does Tiffin River Wildlife Area span Hancock County only, or does it extend into Defiance and Paulding counties? If multi-county, it will be a cross-county entity requiring KNOWN_MC treatment in future runs.
2. Does the Blanchard River Water Trail (37.6 mi) stay within Hancock County, or does it cross into adjacent counties?
3. What is the correct scope and entity type for the Old Mill Stream Scenic Byway? Likely not a trail (vehicular byway) — possibly a Site Network or out of scope.
4. Which Fostoria parks fall within the Hancock County portion of the city vs. the Seneca County portion?
5. Which Bluffton parks (if any) fall within Hancock County vs. Allen County?
6. Are the Hancock County Wildlife Areas (1–7) discrete parcels with separate identities, or do some share a common administrative name? Verify via ODNR hunting maps.
7. Does Camp Berry (BSA) have public access components that qualify it as a project entity, or is it a private camp?
8. Is Lake LeComte the same feature as Leipsic Reservoir? Baseline has conflicting entries — Sheet1 lists both separately with the same acreage (194.5 and 322.5 ac), suggesting they may be distinct features.
9. Is Findlay Reservoir #2 the same as "Leipsic Reservoir" (322.5 ac per Sheet1), or is Lake LeComte/Leipsic a third, separate reservoir near Fostoria?
10. Do the Fostoria Reservoirs (#1–#5 implied by "Reservoir #5 = Lake LeComte") exist as discrete public-access entities?

---

## Session Startup Checklist

**Run these checks at the start of every session (new or resumed) before touching any data:**

1. **Chrome availability** — Call `mcp__Claude_in_Chrome__list_connected_browsers`. If a browser is returned, Chrome is available and should be used for all web fetching (Google Maps verification, official park pages, ODNR, etc.). If the call fails or returns empty, fall back to `mcp__workspace__web_fetch`. Do NOT use bash `curl`/`wget`/`python requests` to fetch URLs — those are blocked regardless of Chrome availability.
2. **Staging file key structure** — Confirm `hancock_ohio_raw_discovery.yaml` top-level keys are intact before any appends.
3. **Tier position** — Confirm the current tier in this handoff matches the canonical tier order in Discovery Orchestration Module §6.
4. **Re-read the sub-procedure** for the tier about to begin (IMP-075 — mandatory, no substitutions).

---

## Next Steps

**ALL DISCOVERY TIERS COMPLETE (T1–T8). 185 records in YAML. Pipeline prerequisites below.**

### Pre-Pipeline Prerequisites (resolve before na-pipeline run)

1. **LOCAL-004 — RESOLVED 2026-05-16** — All 16 Fostoria records confirmed Hancock County (see Key Active Flags). No pipeline blocking issue.
2. **LOCAL-005 — RESOLVED 2026-05-16** — Village Park confirmed Hancock; Bicycle Pathway flagged CROSS_COUNTY_CANDIDATE. Three records (Buckeye Park, Pool, Maple Grove Cemetery) corrected to county_primary=Allen in YAML — pipeline will route to Allen County. No pipeline blocking issue for Hancock run.
3. **COUNTY_VERIFY Blanchard River NP — RESOLVED 2026-05-16** — Confirmed Hancock County. BSC donated to Hancock County Park District; Visit Findlay (Hancock CVB) lists it; BirdingHotspots attributes to "Hancock, Ohio, US." Forest OH mailing address is a Hardin County village but parcel is in Hancock County near southern boundary. COUNTY_VERIFY flag removed from YAML.
4. **COUNTY_VERIFY Aeraland RA — RESOLVED 2026-05-16** — Confirmed Hancock County. GPS lon=-83.511 is ~5 miles west of the Hancock/Seneca boundary (lon≈-83.41–83.43 per Fostoria parks page). COUNTY_VERIFY flag removed from YAML.
5. **T5 UNCONFIRMED_NAME follow-ups** (2026-05-16 — partially resolved):
   - Eagle Township / Bishop Cemetery → **CONFIRMED** — Find a Grave ID 39916 + OHGenWeb both confirm "Bishop Cemetery in Eagle Township, Ohio." Eagle Twp 2024/2023 basic audit fetched — no fund names in basic audit format. Name confirmed from independent sources. ✅
   - Jackson Township / Houcktown Cemetery → **BEST_CANDIDATE** — WorldCat/UW-Madison OGS publication (OCLC 24620846) confirms Houcktown Cemetery in Jackson Township, Hancock County. Jackson Twp 2023/2022 basic audit fetched (15524 SR 37, Arlington OH — correct county confirmed); no cemetery fund named in basic audit. jacksontwp.net found to be Mahoning County (wrong county). UNCONFIRMED_NAME flag retained; to fully confirm, contact Jackson Township trustees at 15524 State Route 37, Arlington OH 45814.
   - Portage Township / UNCERTAIN → **STILL UNCONFIRMED** — Portage Township 2022/2021 regular audit fetched and reviewed. Note 1 explicitly states "cemetery maintenance" as a township service. Prior finding 2020-002 (fully corrected): "cemetery revenue posted to incorrect fund" — confirms a separate cemetery fund existed. No specific cemetery name in audit; fund schedules aggregate into Health disbursement category. Three OGS candidates remain: Pleasant Hill Cemetery (McComb), Ten Mile-Bethel Cemetery, Thomas Cemetery. portagetownship.net confirmed as wrong county (Ottawa County). Action: contact trustees at 9313 CR 203, Van Buren OH 45889 to confirm name.
6. **GPS Acquisition Module** — ~40 GPS-blank records remain: 29 Findlay single-county parks (defer to GPS Module), 7 Fostoria walking trails (derive from parent site coords), Lake LeComte (no Maps entity found), 3 Bluffton entities (Pool/Cemetery/Pathway — no Maps entity), Hoadley Park (Van Buren), Findlay Reservoir #2, Camp Berry, McComb Reservoir Walk Trail, Findlay Reservoir Dike Trail, Cloe Greiner CP (already has GPS from map verify), Bluffton Bicycle Pathway (endpoints noted in identity_notes_raw).
7. **Open Question Q9 resolution** — Copilot seed "Leipsic Reservoir (322.5 ac)" does NOT match Findlay Reservoir #2 (645 ac) or any staged entity. Leipsic is in Putnam County — likely out of scope for Hancock County run. Flag for Putnam County session.
8. **Jenera / Rawson / Mt. Cory** — unincorporated communities with HPD community parks. Confirm whether incorporated as villages requiring separate T6 entries. HPD community parks already staged at T3.
9. **Riverbend Conservation Area stub** (T3 record) — no page content found; stub record only. Confirm existence and location via Google Maps or HPD contact before normalization.

### Remaining Items (non-blocking)

1. **Portage Township Cemetery name** — soft block only; entity is in DB as-is. Contact trustees at 9313 CR 203, Van Buren OH 45889 to confirm canonical name.
2. **Cross-county candidates** — HAN-S-098 (Bluffton Village Park, Hancock+Allen), HAN-T-012 (Old Mill Stream Scenic Byway, Hancock+Putnam), HAN-T-023 (Bluffton Bicycle Pathway, Hancock+Allen). These are flagged in DB but require cross-county resolution when Allen and Putnam County runs are executed.
3. **Wildlife areas GPS** — HAN-S-003 through HAN-S-015 (13 entities) remain GPS-null. Nominatim cannot resolve numbered wildlife areas or rural WPA parcels. Acceptable as null; `notes` field documents unresolvability.
4. **Small parks GPS** — ~20 Findlay/village parks not in OSM remain GPS-null (Roethlisberger Field, Marathon Diamonds, Cube Ice Arena, Guthrie/Hancock/Koehler/Remington Fields, etc.). May resolve in a future GIS/address-lookup pass.
5. **Cemetery supplemental pass (LOCAL-007)** — ✅ **RESOLVED 2026-05-17.** 54 cemeteries upserted, IDs HAN-S-113–HAN-S-166. GPS-null 5 cemeteries remain (Frontiers Repose, High Bank, Indian Grove, Maple Lawn, Riley Creek) — can be resolved in a future GPS acquisition pass. Pleasant Hill Cemetery (HAN-S-154) is a candidate name for Portage Township Cemetery (HAN-S-048, UNCONFIRMED_NAME) — merge if confirmed.

**Golf course supplemental (IMP-105, 2026-05-16):** 10 courses added per new scope rule requiring all golf courses regardless of access. HAN-S-103–HAN-S-112: Shady Grove, Red Hawk Run, Hillcrest, Wayside, Shady Acres, Sycamore Springs, Lakeland, Loudon Meadows, Findlay Country Club (private/members-only), Oak Mallett (Closed 2014). Fostoria CC confirmed Seneca County — not staged. 3 courses with GPS (Shady Grove, Hillcrest, Findlay CC); HAN-S-110 (Loudon Meadows) GPS flagged GPS_REVIEW — Nominatim returned wrong coordinates; needs manual lookup. Total HAN sites: 112.

**Note for future counties:** T8 sub-procedure updated to v5.6 (IMP-105). Run the mandatory PGA.com course finder + county CVB golf page enumeration step at the start of every T8 before any direct searches.

**Wood County golf courses:** Not yet remediated. Needs supplemental upsert: Stone Ridge Golf Club (Bowling Green, public), Riverby Hills Golf Club (Bowling Green), Bowling Green Country Club (private), Forrest Creason Golf Course (Bowling Green, municipal — may be T6), Belmont Country Club (Perrysburg, private), Tanglewood Golf Club (Perrysburg), Crosswinds Golf Club (Perrysburg, public), plus others. Wood County T8 golf course pass is a pending task.

**Hancock County run is complete.**

---

## Pre-Discovery Checklist

### Tier 1 — Federal ✓ COMPLETE
*Completed 2026-05-12. Result: 0 entities — all 6 entity types null.*

- [x] **NPS** — nps.gov/state/oh full Ohio listing (10 units); none in Hancock County. NHAs checked: Ohio & Erie Canalway (NE/central Ohio) and NAHA (Dayton area); neither in Hancock County.
- [x] **USFWS** — fws.gov find endpoint returned 404 (URL changed); NW Ohio USFWS confirmed as Ottawa NWR and Cedar Point NWR (Ottawa County only); neither in Hancock County.
- [x] **USFS** — Wayne National Forest is SE Ohio only (cert error on direct URL; confirmed via geographic knowledge); no USFS land in Hancock County.
- [x] **BLM** — Minimal BLM holdings in Ohio; confined to SE Ohio adjacent to Wayne NF; none in Hancock County.
- [x] **Army Corps of Engineers** — corpslakes.erdc.dren.mil full Ohio project list (38 projects); all eastern/southern/central Ohio; none in NW Ohio; Blanchard River flood mitigation is local/FEMA, not USACE fee-title.
- [x] **DoD** — No DoD installations in Hancock County (geographic knowledge; confirmed).
- [x] **Tribal** — No federally recognized tribal trust lands or reservations in Hancock County (confirmed via BIA geographic knowledge).

### Tier 2 — State (ODNR) ✓ COMPLETE
*Completed 2026-05-13. Result: 47 records — 15 Sites, 3 Trails, 19 Trail Segments, 10 Access Points. IMP-080 verified. IMP-104 clean.*

- [x] **ODNR Division of Parks & Watercraft** — Van Buren State Park: Site + Campground (child Site) + 3 Trail records + 19 Trail Segments (loops from park map rev. 10/2025) + 4 Access Points (Main Entrance, Equestrian Day Use Area, Horseman's Camp, Paddling Access). Maps saved to source_files/. 2026-05-13.
- [x] **ODNR Division of Wildlife** — Hunting Area Maps: WAs 1,3,4,5,6,7 staged (6 Sites + 6 WA Parking Area Access Points). No WA 2. Tiffin River WA → Fulton County (LOCAL-001 resolved). Fishing Lake Maps: null. River/Stream Fishing Maps: null. GIS (ODNR_ODNR_Lands_External3): WPAs 9,25,32,41,43,45,46 staged as 7 additional Sites (GIS-sourced, minimal data; no public AP documentation). Maps saved to source_files/. 2026-05-13.
- [x] **ODNR Division of Natural Areas & Preserves (DNAP)** — NULL confirmed via ODNR GIS (cnty_fips='063', no PROP_TYPE=SNP). TrekOhio confirms no state nature preserves in Hancock County. 2026-05-13.
- [x] **ODNR Division of Forestry** — NULL confirmed via ODNR GIS (cnty_fips='063', no PROP_TYPE=SF). NW Ohio agricultural plain; no state forests expected or found. 2026-05-13.
- [x] **ODNR Scenic Rivers** — NULL confirmed. Blanchard River is NOT among Ohio's 17 designated scenic rivers. 2026-05-13.
- [x] **ODNR Water Trails** — Blanchard River Water Trail (37.6 mi, ODNR-designated). Per §4.6, managed by Hancock Park District → Tier 3 entity, not Tier 2. No T2 record created. LOCAL-002 resolved. Guide PDF saved to source_files/. 2026-05-13.
- [x] **ODNR Mineral Resources** — GIS query returned Van Buren SP + DOW HQ + 7 WPAs only. No mineral resource surface lands. NULL. 2026-05-13.
- [x] **Ohio History Connection (OHC)** — NULL confirmed. 110 OHC statewide sites extracted; zero Hancock County matches. 2026-05-13.
- [x] **ODOT Rest Areas** — I-75 NB (01-25) and SB (01-26) rest areas fetched. Both have only Vending, Family Restroom, Drinking Water — no outdoor recreation features (no dog trail, Storybook Trail, native plant area). NULL per §4.2. 2026-05-13.
- [x] **OTIC (Ohio Turnpike)** — SKIP. I-80/90 does not run through Hancock County. Per §4.5. 2026-05-13.
- [x] **Public Universities (§4.7)** — NULL. No public universities in Hancock County. 2026-05-13.
- [x] **Ohio State Parks Trails (Van Buren SP)** — 19 Trail Segment records staged: 9 hiking loops (incl. Purple Trail from park map; Sensory, Haiku, connectors, Cable Line Road), 2 MTB loops, 4 bridle loops. Lengths/difficulties from official park map rev. 10/2025 (supersede web page values). Shared-treadway loops given parallel records per §7.3. 2026-05-13.

### Tier 3 — District (Hancock Park District + SWCD) ✓ COMPLETE
*Completed 2026-05-13. 53 records. IMP-080 PASSED. IMP-104 checked.*

**Ohio Auditor Canvass Block — 2026-05-13**
```
Ohio Auditor pre-enumeration complete — 2026-05-13
  URL: https://ohioauditor.gov/auditsearch/search.aspx
  County filter: Hancock
  Entity types searched: Park/Recreation District, Conservancy District,
    Soil/Water Conservation District/Joint Board, Water/Sewer/Sanitary District
  Entities found: 4 distinct entities (2 active, 1 historical, 1 project)
  Entity names:
    1. Hancock Park District — Park/Recreation District — ACTIVE (most recent audit FY2023-2024)
    2. Hancock County/City of Findlay Joint Recreation District — Park/Recreation District — HISTORICAL (last audit FY2002; likely dissolved/merged)
    3. Hancock County Soil and Water Conservation District — SWCD — ACTIVE (most recent audit FY2023-2024)
    4. Blanchard River Enhancement Project — SWCD category — ACTIVE (most recent basic audit FY2023-2024; project/program entity)
  Web-dark (no §3.1 web presence found): none confirmed yet — check in §3.1 step
```

**T3 Entity Scope (from §3.0):**
- [x] **Hancock Park District** — 53 records staged. See below. 2026-05-13.
- [x] **Hancock County/City of Findlay Joint Recreation District** — last Auditor entry 2002; presumed dissolved/absorbed. No separate web presence found. NULL — documented in tier_null_results. 2026-05-13.
- [x] **Hancock County SWCD** — hancockswcd.com: drainage maintenance, H2Ohio water quality programs, technical assistance only. No public lands, parks, or natural areas. NULL per §4.7. Documented in tier_null_results. 2026-05-13.
- [x] **Blanchard River Enhancement Project** — SWCD-administered one-time river cleaning project (Nov 2013–Feb 2015, completed). Not a land-managing entity, no public access sites. NULL. Documented in tier_null_results. 2026-05-13.

**HPD PARKS — AUTHORITATIVE ENUMERATION (IMP-029/030)**
*Source: hancockparks.com homepage map — fetched 2026-05-13. This is the complete HPD property list.*

| # | Park Name | Address | City | Notes |
|---|-----------|---------|------|-------|
| 1 | Aeraland Recreation Area | 1141 Township Road 243 | Fostoria | Fostoria — verify Hancock vs. Seneca county |
| 2 | Blanchard Landing | State Route 235, south of U.S. Route 224 West | Findlay | Water Trail landing |
| 3 | Blanchard River Nature Preserve | 22006 C.R. 17 | Forest | Forest is Hardin County — verify county |
| 4 | Blue Rock Nature Preserve | Edgar Avenue and Bank Street | Findlay | |
| 5 | Bright Conservation Area | 10184 Township Road 244 | Findlay | |
| 6 | Centennial Park | Cross Avenue, East of Blanchard Street | Findlay | |
| 7 | Eastpoint Area | East Main Cross Street, at Bright Road Bridge | Findlay | |
| 8 | Great Karg Well Historical Site | Liberty and River Street | Findlay | Historical site |
| 9 | Indian Green-Worden Family Conservation Area | East of Litzenberg Memorial Woods (south unit) | Findlay | |
| 10 | Jackson Landing | 16894 Township Road 173 | Findlay | Water Trail landing |
| 11 | Lawrence Conservation Area | South of Township Road 236 | Findlay | |
| 12 | Lehman Conservation Area | 16428 Township Road 208 | Findlay | |
| 13 | Liberty Landing | Township Road 89, west of County Road 140 | Findlay | Water Trail landing |
| 14 | Litzenberg Memorial Woods | 6100 U.S. Route 224 West | Findlay | |
| 15 | Oakwoods Nature Preserve | 1400 Oakwoods Lane | Findlay | |
| 16 | River Landings | 700 Fox Street | Findlay | Multiple landings — multiple APs |
| 17 | Riverbend Conservation Area | North of Bright Conservation Area | Findlay | |
| 18 | Riverbend Recreation Area | 16618 Township Road 208 | Findlay | |
| 19 | Vogelsong Conservation Area | West of State Route 568 Bridge | Findlay | |
| 20 | Waterfalls Area | 231 McManness Avenue | Findlay | HPD-owned; distinct from Riverside Park Waterfront (now City of Findlay) |

**Note — Riverside Park Waterfront**: HPD cancelled management agreement with City of Findlay effective Jan 1, 2026. No longer HPD-managed → will be Tier 6 entity (City of Findlay) with history note.

**HPD Trails to discover separately (after sites):**
- [ ] Heritage Trail — hancockparks.com/heritage-trail-map/
- [ ] Blanchard River Water Trail (LOCAL-002) — 37.6 mi ODNR-designated, HPD-managed
- [ ] Any additional trails on TRAILS menu of HPD website

**Individual park page fetch status (IMP-029 tracker):** ✓ ALL FETCHED 2026-05-13
- [x] Aeraland Recreation Area — 1141 TR 243, Fostoria; 74.8ac; Highline Trail, Upland Trail; COUNTY_VERIFY
- [x] Blanchard Landing — SR 235 S of US 224 W; GPS 41.045656, -83.791766; BRWT end
- [x] Blanchard River Nature Preserve — 22006 CR 17, Forest; GPS 40.844073, -83.556628; COUNTY_VERIFY (may be Hardin County)
- [x] Blue Rock Nature Preserve — Edgar Ave & Bank St; 11.3ac; GPS 41.011445, -83.645621; Ladybug Loop 0.3mi
- [x] Bright Conservation Area — 10184 TR 244; 29.4ac; GPS 41.018562, -83.557619
- [x] Centennial Park — Cross Ave & E Blanchard St; 0.5ac; City of Findlay owned; no GPS extractable
- [x] Eastpoint Area — E Main Cross St at Bright Rd Bridge; 1ac; Hancock County owned; GPS 41.038104, -83.614161
- [x] Great Karg Well Historical Site — Liberty & River St; 0.5ac; City of Findlay owned; GPS 41.043476, -83.657299
- [x] Indian Green-Worden Family Conservation Area — E of Litzenberg (south unit); 27.3ac; GPS ~41.041514, -83.651634
- [x] Jackson Landing — 16894 TR 173; GPS 40.992294, -83.559324; BRWT access
- [x] Lawrence Conservation Area — S of TR 236; 16.1ac; GPS 41.035128, -83.593393; appointment-only access
- [x] Lehman Conservation Area — 16428 TR 208; 7.1ac; GPS 41.034096, -83.570045
- [x] Liberty Landing — TR 89 W of CR 140; GPS 41.056366, -83.696242; BRWT 9.3mi float start
- [x] Litzenberg Memorial Woods — 6100 US 224 W; 227.7ac; Backwoods Trail (bridle), Heritage Trail; no GPS from page
- [x] Oakwoods Nature Preserve — 1400 Oakwoods Lane; 227.5ac; GPS 41.022606, -83.686242
- [x] River Landings — 700 Fox St; 10ac; City of Findlay owned; GPS 41.054328, -83.664686; BRGT west terminus
- [x] Riverbend Conservation Area — no page content; STUB ("North of Bright CA") — needs map verify
- [x] Riverbend Recreation Area — 16618 TR 208; 129ac; GPS 41.032926, -83.564270; BRWT access/camping
- [x] Vogelsong Conservation Area — W of SR 568 Bridge; 23.6ac; GPS 41.037082, -83.610896
- [x] Waterfalls Area — 923 E Main Cross St; 0.5ac; City of Findlay owned; GPS 41.041598, -83.631622; BRWT portage

### Tier 4 — County ✓ COMPLETE
*Completed 2026-05-13. 1 record (Hancock County Infirmary Cemetery). IMP-080 PASSED. IMP-104 clean.*

- [x] **Hancock County website** — co.hancock.oh.us: no parks/recreation dept (9 departments: family/children, elections, health, job/family, law library, public defender, solid waste, veterans, guardianship). Facilities page: "No facilities found." 2026-05-13.
- [x] **Hancock County Engineer** — roads/bridges only; no trails, open space, or recreation. 2026-05-13.
- [x] **Hancock County Commissioners page** — administrative/governmental; no land acquisitions, park resolutions, or conservation partnerships. Sample agenda 5/12/2026 reviewed: lawn mowing contract (office properties), SRTS Phase II (school-focused pedestrian project, not county park trail), flood mitigation topics. 2026-05-13.
- [x] **County GIS (§3.2)** — Beacon auditor property search confirmed as available (beacon.schneidercorp.com/Application.aspx?AppID=1128). Full parcel layer review deferred to GPS acquisition pass. No county-owned parks parcels surfaced from web sources. 2026-05-13.
- [x] **NRHP §3.3** — 14 NRHP listings in Hancock County (Wikipedia/NPS). No covered bridges, no bridges, no natural features on public land. All listings are private residences, commercial buildings, courthouse, or downtown historic district. NULL. 2026-05-13.
- [x] **County Planning Documents §3.4** — Hancock Regional Planning Commission (hancockrpc.org): zoning/CDBG only, no open space or trail plans. hancockcountytrailplan.com: domain inactive. No qualifying planning documents found. 2026-05-13.
- [x] **County Tourism §3.6** — visitfindlay.com (Hancock County CVB): parks page lists 9 entries — all managed by HPD (T3), City of Findlay (T6), or villages (T6). No county-direct entities. 2026-05-13.
- [x] **County-hosted municipal/township pages §3.7** — not present on co.hancock.oh.us. NULL. 2026-05-13.
- [x] **Hancock County Fairgrounds (§4.9 assessment)** — 1017 E Sandusky St, Findlay; operated by Hancock County Agricultural Society (independent nonprofit, not county government). Seasonal event venue; not a parks/recreation entity. Out of scope. 2026-05-13.
- [x] **County cemeteries IMP-099** — Hancock County Infirmary Cemetery confirmed (GNIS #1730821; GPS 41.0512, -83.6888; Liberty Township, CR 140 at Westfield Dr). **Staged as T4 Site.** No soldiers relief cemetery found. 2026-05-13.
- [x] **County golf courses IMP-099** — No HPD-operated golf course. Findlay Country Club Golf Course (NRHP-listed) is private. NULL. 2026-05-13.
- [x] **HPD vs. county parks commission confirmation** — Hancock Park District is the sole park district for Hancock County (Ohio Auditor canvass, T3). County government has no separate parks commission. Confirmed. 2026-05-13.

### Tier 5 — Township
*Created 2026-05-12 (bootstrap). 17 townships from authoritative roster.*

| Township | Seat/Area | Check URL/Source |
|----------|-----------|-----------------|
| Allen | Van Buren | allentownship.com |
| Amanda | Mount Blanchard area | — |
| Biglick | Findlay area | — |
| Blanchard | Findlay area | — |
| Cass | Findlay area | — |
| Delaware | Mount Blanchard | delawaretownshiphancockcountyohio.wordpress.com |
| Eagle | Findlay area | — |
| Jackson | Arlington area | — (baseline has Jackson Township Park) |
| Liberty | Findlay area | — (baseline has Liberty Township Park) |
| Madison | Arlington area | — |
| Marion | Findlay area | — |
| Orange | Bluffton area | — |
| Pleasant | McComb area | — |
| Portage | Van Buren area | — |
| Union | Bluffton area | — |
| Van Buren | Jenera area | — |
| Washington | Arcadia area | — |

For each: search "[Township Name] Township Hancock County Ohio park" and check any township trustee website for recreational lands. Known baseline seeds: Jackson Township Park (County Road 139, near Arcadia), Liberty Township Park (County Road 140).

### Tier 6 — Municipal
*Created 2026-05-12 (bootstrap).*

**City of Findlay** (primary — largest park system):
- Source: https://www.findlayohio.gov (Parks & Recreation section)
- Known seeds (confirm each): Bernard Park, Blanchard Valley HS Miracle Park, Cooper Field, Donnell Park, Eagle Creek Park, Ede Park, Emory Adams Park, Firestine Park, Flag City Sports Complex, Glenwood Park, Guthrie Field (internal), Hancock Field (internal), Jefferson Park, Koehler Field, Marathon Diamonds (internal), Millstream Art Plaza, Rawson Park, Remington Field (internal), Riverside Park, Riverside Swimming Pool, Roethlisberger Field (internal), Swale Park, The Cube Ice Arena, West Park, Brucklacher Memorial Park, Civic Center Park, Civitan Park
- Also check: Blanchard River Greenway Trail (City of Findlay managed portions), Heritage Trail (joint City/HPD)
- Trails source: https://trailsandparksinhancock.org/trails/

**City of Fostoria** (note: straddles Hancock/Seneca — confirm addresses):
- Source: https://fostoriaohio.gov/parks-and-rec
- Known seeds: City Park (Fostoria), Gray Park, Lake Mosier Park (157.9 ac), Meadowlark Park

**Village of Arlington:**
- Search for any village park

**Village of Arcadia:**
- Known seed: Arcadia Village Park (West Fremont Street)

**Village of Benton Ridge:**
- Search for any village park

**Village of Bluffton** (straddles Hancock/Allen — confirm addresses):
- Search for any village/city parks in Hancock portion

**Village of McComb:**
- Known seeds: McComb Reservoirs 1 & 2 (possible park/recreation area)

**Village of Mount Blanchard:**
- Known seeds: Island Park, Mount Blanchard Community Park, Mount Blanchard Cemetery (out of scope?)

**Village of Van Buren:**
- Known seed: Van Buren Village Park (North Main Street)

**Village of Vanlue:**
- Search for any village park

### Tier 7 — Conservancy / Land Trust
*Completed 2026-05-15. Result: 0 entities — all 6 entity types null. IMP-080 PASSED. IMP-104 clean (no multi-county entities).*

**BSC Entity Enumeration (IMP-029 — Land We Own, fetched 2026-05-15):**

| # | Preserve Name | County Finding |
|---|---------------|----------------|
| 1 | Bell Woods Nature Preserve | Pemberville/Wood County |
| 2 | Buttonwood Island Nature Preserve | Grand Rapids/Wood County (adjacent to Howard Island) |
| 3 | Dr. Robert L. Nehls Memorial Nature Preserve | Catawba Island/Ottawa County |
| 4 | Forder Bridge River Access Site (Forrest Woods) | Maumee River Trail Access Site — not Hancock |
| 5 | Forrest Woods Nature Preserve | Maumee River area — not Hancock |
| 6 | Heron Crest Nature Preserve | Maumee River, NW Ohio — not Hancock |
| 7 | Howard Island Nature Preserve | Maumee River at Grand Rapids/Wood County |
| 8 | Little Auglaize Wildlife Reserve | **Paulding County** (explicitly stated) |
| 9 | Pat & Clint Mauk's Prairie | 4825 Sugar Ridge Road, Pemberville/Wood County |
| 10 | Quinstock Woods Preserve | Catawba Island Township/Ottawa County |
| 11 | Rotary Riverside Preserve | Maumee River, GPS [41.41,-84.03] → Putnam County |
| 12 | St. Joseph River Confluence Preserve | St. Joseph River → Allen/Defiance area |
| 13 | St. Joseph River Floodplain Preserve | St. Joseph River → Allen/Defiance area |
| 14 | Water's Edge Nature Preserve | Sandusky River → Sandusky/Seneca area |
| 15 | Webber Woods Preserve | Toledo/Point Place, Lucas County |
| 16 | Weisgerber-Pohlman Nature Preserve | Tiffin River → Fulton/Henry area |

**BSC Land We Protect (publicly accessible, fetched 2026-05-15):**
Blanchard River Nature Preserve — Hancock County; BSC purchased 2013 and donated fee-simple to Hancock Park District. **Already staged as T3 Site.** BSC has no current ownership/easement role. BSC noted in T3 record `partner_agencies_raw`. Not a T7 entity. All other "Land We Protect" properties: Ottawa/Lucas/Wood/Sandusky County areas, not Hancock.

- [x] **Black Swamp Conservancy** — All 16 owned preserves checked. 0 in Hancock County. Blanchard River NP donated to HPD (T3 entity). `partner_agencies_raw` updated in T3 record. **NULL.** 2026-05-15.
- [x] **The Nature Conservancy Ohio** — 8 named preserves (https://www.nature.org/en-us/about-us/where-we-work/united-states/ohio/places-we-protect/): NE Ohio (Great Egret Marsh/Ottawa, Kitty Todd/Lucas, Morgan Swamp/Ashtabula, Herrick Fen/Portage, Lucia Nash/Erie) and Central/Southern Ohio (Brown's Lake Bog/Wayne, Big Darby Headwaters/Logan, Edge of Appalachia/Adams). None in Hancock County. **NULL.** 2026-05-15.
- [x] **Western Reserve Land Conservancy** — NE Ohio organization (Moreland Hills/Cuyahoga HQ; wrlandconservancy.org). 29-county footprint explicitly described as "northern and eastern Ohio from Sandusky Bay to Pennsylvania border." Hancock County (NW Ohio) is outside service area. **NULL.** 2026-05-15.
- [x] **ONAPA preserve map** — https://www.onapa.org/preserve-map.html redirects to ODNR nature preserves finder (naturepreserves.ohiodnr.gov/findapreserve) — same database confirmed null in T2 (0 ODNR DNAP state nature preserves in Hancock County). No ONAPA member organizations specific to Hancock County. **NULL.** 2026-05-15.
- [x] **Ducks Unlimited** — Web search found no Hancock County DU conservation easements. DU easements are typically on private land with no public access → below T7 threshold. **NULL.** 2026-05-15.
- [x] **ODNR Voluntary Protection Program** — Web search returned no Hancock County results. Cross-reference to T2 ODNR DNAP check (0 state nature preserves in Hancock County). **NULL.** 2026-05-15.
- [x] **Cross-tier partnerships (§3.4)** — T3 cross-reference: BSC purchased and donated Blanchard River NP → addressed above. No other T1–T6 partnership mentions requiring T7 investigation. **COMPLETE.** 2026-05-15.

### Tier 8 — Private / Other
*IMP-029 Pre-Discovery Checklist written 2026-05-15. IMP-075 sub-procedure read (na_private_discovery_subproc_v5.5.md) before enumeration.*

**IMP-029 Pre-Discovery Checklist — T8 Candidate Enumeration (written 2026-05-15 before individual page fetches)**

| # | Candidate | Source of Lead | Governance Finding | Stage? |
|---|-----------|----------------|-------------------|--------|
| 1 | Camp Berry (BSA/Scouting America) | Baseline seed; blackswampbsa.org | Private nonprofit (BSA); 360 ac; 11716 CR 40, Findlay OH 45840; Eagle Creek; 4-ac lake; facility rentals available to out-of-council groups | **YES — T8 Site** |
| 2 | Findlay Reservoir #1 Fishing Area | Baseline seed; ODNR Find a Property; norrik.com; hiking-ohio.com | City of Findlay owns (municipal water supply, built 1950); ODNR DOW cooperative fishing management; ODNR NOT in ODNR GIS Hancock lands (T2 GIS query returned null for this parcel); → **T6 miss** (City of Findlay / Water Dept) | **YES — T6 miss** |
| 3 | Findlay Reservoir #2 Fishing Area | Baseline seed; norrik.com; hiking-ohio.com | City of Findlay (primary owner); built cooperatively by City + ODNR 1968; ODNR cooperative fishing management; ODNR GIS null → **T6 miss** | **YES — T6 miss** |
| 4 | Findlay Reservoir Dike Trail | hiking-ohio.com; norrik.com | Trail on earthen dikes surrounding Reservoirs #1 and #2; 5.3 mi outer perimeter; City of Findlay / ODNR same governance as reservoirs; → **T6 miss** | **YES — T6 miss Trail** |
| 5 | Lake LeComte / Leipsic Reservoir / Fostoria Reservoir #5 | Baseline seed; Q8/Q9 | Already staged as T6 Site under City of Fostoria (Lake LeComte, Reservoir 5 at CR 23); Q8/Q9 open questions about identity; identity_notes_raw has LOCAL-004 flag; **NO new staging needed — resolved at T6** | NO (staged at T6) |
| 6 | Lake Daugherty, Mosier, Mottram, Lamberjack, Veterans Memorial Res. | T6 Fostoria | Already staged at T6 (City of Fostoria Parks & Recreation) | NO (staged at T6) |
| 7 | McComb Reservoirs 1 & 2 | Baseline seed | YAML check: no McComb reservoir records beyond McComb Pool and McComb Union Cemetery. Copilot baseline seed "McComb Reservoir Trail" suggests small reservoirs near village. No authoritative source found during T8 search; no McComb water department page identified. **UNRESOLVED — document as open question** | PENDING |
| 8 | ODNR Licensed Hunting Preserves | T8 §5.1 mandatory check | ODNR Pub 5129: "list of all wild animal hunting preserves may be obtained from the Division of Wildlife by contacting any district office" — no public online registry. Web search: no hunting preserves found in Hancock County. District Two office (Findlay): 952 Lima Ave, Findlay 45840; (419) 424-5000. NULL. | NO (null documented) |
| 9 | Private golf courses — IMP-099 | T8 §5.1; T4 prior check | Findlay Country Club (1500 Country Club Dr, private, confirmed T4); Fostoria Country Club (747 Independence Ave — **Seneca County**, per Destination Seneca County listing; out of scope); no other private golf courses found in Hancock County | NO (T4 miss already noted; Fostoria CC out of scope) |
| 10 | Woodland Lakes Christian Camp | web search | Located at 3054 Lindale Mt. Holly Rd, Amelia OH 45102 — **Clermont County**, SW Ohio. Not Hancock County. | NO (wrong county) |
| 11 | Church/family cemeteries IMP-099 | T8 §5.1; Find A Grave cross-check | T4 staged Hancock County Infirmary Cemetery; T5 staged 15 township cemeteries; T6 staged Fountain Cemetery (Fostoria) and Maple Grove Cemetery (Bluffton); search confirms no additional unaccounted municipal/church cemeteries requiring T8 staging based on web sources. Find A Grave lists private/family cemeteries but these are typically closed-access sites below NAP entity threshold. NULL for T8 new staging. | NO (null) |
| 12 | eBird hotspot cross-check | T8 §5.1; birdinghotspots.org Hancock County Drive | Blue Rock NP (L3786601) — already T3. Findlay Water Pollution Control Center (L480077) — roadside waterfowl observation on public road; no park/preserve entity. Riverbend RA (T3), Litzenberg (T3), Van Buren SP (T2) all previously staged. No new eBird hotspot entities requiring staging. NULL. | NO (null) |
| 13 | Findlay High School Outdoor Learning Lab | baseline seed | School-site restricted access. Out of scope per T8 sub-procedure §4.1 (no public access). NULL. | NO (out of scope) |

**Governance verification complete: Camp Berry = T8; Findlay Reservoirs #1 and #2 + Dike Trail = T6 misses (City of Findlay); all other candidates null or previously staged.**

- [x] **BSA Camp Berry** — blackswampbsa.org/camping/camp-berry/63302 fetched 2026-05-15. 360 acres, Eagle Creek, 4-ac lake, Karl Edelbrock Nature Center, facility rentals available to in- and out-of-council groups. **Staged as T8 Site.** 2026-05-15.
- [x] **Findlay Reservoir #1** — ODNR Find a Property + hiking-ohio.com + norrik.com fetched 2026-05-15. 186 ac, built 1950, City of Findlay water supply, public fishing via ODNR cooperative, walking trail on dike, boat ramp (electric motors only). **T6 miss — staged at T6.** 2026-05-15.
- [x] **Findlay Reservoir #2** — Same source set. 645 ac, built 1968, City of Findlay water supply, ODNR cooperative, walking trail, 9.9HP max outboard, restrooms. **T6 miss — staged at T6.** 2026-05-15.
- [x] **Findlay Reservoir Dike Trail** — hiking-ohio.com + norrik.com. ~5.3 mi outer perimeter; individual reservoir dike mileages: R1 = 2.0 mi, R2 = 4.3 mi (shared dike = 1 mi). **T6 miss Trail — staged at T6.** 2026-05-15.
- [x] **ODNR Licensed Hunting Preserves** — ODNR Pub 5129 reviewed; no public registry; web search returned no Hancock County preserves; District Two at Findlay is contact for full list. **NULL — documented in T8 null results.** 2026-05-15.
- [x] **Private golf courses** — Findlay CC confirmed private T4 miss (already noted); Fostoria CC is Seneca County. **NULL for T8.** 2026-05-15.
- [x] **Church/family cemeteries IMP-099** — All accounted for at T4/T5/T6. No additional T8 cemetery entities. **NULL.** 2026-05-15.
- [x] **eBird hotspot cross-check** — 5 Hancock County hotspots checked; all previously staged (T2/T3) or roadside-only observation points without park entity. **NULL.** 2026-05-15.
- [x] **McComb Reservoirs 1 & 2** — Village of McComb website (villageofmccomb.com/parks-and-amenities) + ODNR fishing map PDF (dam.assets.ohio.gov/…/mccomb.pdf) fetched 2026-05-16. R1: 6 ac / 0.40 mi shoreline; R2: 20 ac / 0.70 mi shoreline; public fishing (electric motors; no ice fishing); boat ramp; restrooms; 1-mile paved walk/fitness trail. eBird hotspot L508567. **T6 miss — staged as McComb Reservoirs 1 & 2 (Site) + McComb Reservoir Walk Trail (Trail) at T6.** 2026-05-16.

---

## Captured Source Data

### Tier 2 — ODNR Parks & Watercraft: Van Buren State Park (2026-05-13)
Source: https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/van-buren-state-park

| Field | Value |
|-------|-------|
| Name | Van Buren State Park |
| Address | 12259 Township Road 218, Van Buren, OH 45889 |
| Phone | (419) 832-7662 |
| GPS | 41.13268422129203, -83.62390670323607 |
| Acreage | 296 acres |
| Manager | Jeremy Babcock |
| Division | ODNR Parks & Watercraft |
| Trails | Hiking (9 named loops, ~14.3 mi total); Mountain Bike (3 mi, 2 loops); Bridle (4 loops, 9 mi) |
| Camping | 61 sites, 50-amp elec/water, pets allowed |
| Other amenities | Dog park (fenced), 18-hole disc golf, archery range, 3 reservable shelterhouses, volleyball, horseshoe pits, playground, sledding |
| Active notice | Dam Notching/Water Level Lowering underway (Aug 2025) — Rocky Ford Creek Restoration; lake not navigable |
| Map download | Available at park page |

### Tier 2 — ODNR Wildlife: Hunting Area Maps — Hancock County entries (2026-05-13)
Source: https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/hunting-area-maps

| Name | County | Type | PDF URL |
|------|--------|------|---------|
| Hancock County 1 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock1.pdf |
| Hancock County 3 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock3.pdf |
| Hancock County 4 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock4.pdf |
| Hancock County 5 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock5.pdf |
| Hancock County 6 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock6.pdf |
| Hancock County 7 | Hancock | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock7.pdf |
| Tiffin River | **Fulton** | Wildlife Area | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/tiffin.pdf |

**Key findings:**
- No "Hancock County Wildlife Area 2" exists in ODNR database (sequence: 1, then 3-7)
- Tiffin River Wildlife Area is listed under **Fulton County**, NOT Hancock County — resolves LOCAL-001 (baseline seed was misattributed)
- No individual ODNR property pages exist for numbered county WAs (not in Find-a-Property system)

### Tier 2 — ODNR Wildlife: Fishing Lake Maps — Hancock County (2026-05-13)
Source: https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/fishing-lake-maps
**Result: NULL** — No Hancock County fishing lakes found in ODNR database.

### Tier 2 — ODNR Wildlife: River/Stream Fishing Maps — Hancock County (2026-05-13)
Source: https://ohiodnr.gov/discover-and-learn/safety-conservation/about-ODNR/wildlife/documents-publications/river-stream-fishing-maps
**Result: NULL** — No Hancock County or Blanchard River entries found.

### Tier 2 — ODNR GIS Lands Layer: Hancock County full inventory (2026-05-13)
Source: https://gis.ohiodnr.gov/arcgis/rest/services/OIT_Services/ODNR_ODNR_Lands_External3/MapServer/1/query?where=cnty_fips='063'
**9 features total:**

| Name | PROP_TYPE | Managing Agency |
|------|-----------|----------------|
| Van Buren State Park | PARK | null |
| District 2 - Findlay Headquarters | HQ | DOW |
| Wildlife Production Area 9 Wildlife Area | WA | DOW |
| Wildlife Production Area 25 Wildlife Area | WA | DOW |
| Wildlife Production Area 32 Wildlife Area | WA | DOW |
| Wildlife Production Area 41 Wildlife Area | WA | DOW |
| Wildlife Production Area 43 Wildlife Area | WA | DOW |
| Wildlife Production Area 45 Wildlife Area | WA | DOW |
| Wildlife Production Area 46 Wildlife Area | WA | DOW |

**Key findings:** No State Nature Preserves (SNP), no State Forests (SF), no mineral resource lands. DOW HQ is administrative — not staged. WPAs 9,25,32,41,43,45,46 staged as additional Tier 2 Sites (GIS-sourced, minimal data; distinct from numbered county WAs from Hunting Area Maps).

### Tier 2 — ODNR Blanchard River Water Trail (2026-05-13)
Source: https://ohiodnr.gov/discover-and-learn/land-water/rivers-streams-wetlands/ohio-water-trails; https://hancockparks.com/trails/blanchard-river-water-trail/
**Resolution (LOCAL-002):** Trail is ODNR-designated but managed by Hancock Park District per hancockparks.com. Per §4.6, Tier 3 entity. ODNR designation noted; no T2 record created.
Length: 37.6 mi | Access points: 11 | Counties: Hancock

### Tier 2 — IMP-110 Source Files Downloaded (2026-05-13)
Location: `County_Spreadsheets/Hancock/source_files/`

| Filename | Source URL | Entity |
|----------|-----------|--------|
| hancock_wa_1_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock1.pdf | Hancock County WA 1 |
| hancock_wa_3_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock3.pdf | Hancock County WA 3 |
| hancock_wa_4_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock4.pdf | Hancock County WA 4 |
| hancock_wa_5_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock5.pdf | Hancock County WA 5 |
| hancock_wa_6_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock6.pdf | Hancock County WA 6 |
| hancock_wa_7_boundary_map.pdf | https://ohiodnr.gov/static/documents/wildlife/wildlife-area-maps/Hancock7.pdf | Hancock County WA 7 |
| van_buren_sp_park_map.pdf | https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/parks/parkmaps/vanburenparkmap.pdf | Van Buren State Park |
| van_buren_sp_hunting_map.pdf | https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/parks/parkmaps/vanburenhuntingmap.pdf | Van Buren State Park |
| blanchard_river_water_trail_guide.pdf | https://dam.assets.ohio.gov/image/upload/odnr/watertrails/BlanchardRiverMapGuide.pdf | Blanchard River Water Trail (T3) |

---

### Tier 5 — Township ✓ COMPLETE
*Completed 2026-05-14. Result: 14 records — 14 Sites (township cemeteries per IMP-099), 0 all other entity types. Running total after T5: 115 records.*

**Township Roster (from `Townships_Officials2022-2023.xlsx`, County = Hancock — 17 townships):**

| Township | Cemetery Staged | Name | Notes |
|----------|----------------|------|-------|
| Allen | ✓ | Allen Township Cemetery | Confirmed: allentownship.com/cemetary/; Bechtel Cemetery (Find A Grave) |
| Amanda | ✓ | Amanda Township Cemetery | Confirmed: Ohio Auditor FY2023 audit fund "Cemetery Fund" |
| Blanchard | ✓ | Blanchard Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Cass | ✓ | Cass Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Eagle | ✓ | Bishop Cemetery *(UNCONFIRMED_NAME)* | Ohio Auditor audit pending verification; secondary source only |
| Fairfield | ✓ | Fairfield Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| German | ✓ | German Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Jackson | ✓ | Houcktown Cemetery *(UNCONFIRMED_NAME)* | jacksontwp.net/Cemetery.shtml pending; name from secondary source |
| Liberty | ✓ | Liberty Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Madison | ✓ | Madison Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Marion | ✓ | Bright Cemetery | Confirmed: mariontwphancock.com/cemetery/ (2 cemeteries) |
| Marion | ✓ | Elm Grove Cemetery | Confirmed: mariontwphancock.com/cemetery/ (2 cemeteries) |
| Orange | ✓ | Hasson Joint Cemetery | Confirmed: joint governance with T5; identity_notes_raw CROSS_COUNTY_CANDIDATE |
| Pleasant | ✓ | McComb Union Cemetery | Confirmed: joint w/ McComb village; staged T5 per IMP-099 |
| Portage | ✓ | UNCERTAIN — name TBD *(UNCONFIRMED_NAME)* | 3 candidates: Portage, Van Buren, Hammansburg cemeteries; audit pending |
| Richland | ✓ | Richland Township Cemetery | Confirmed: Ohio Auditor FY2023 audit |
| Union | ✓ | Cannonsburg Joint Cemetery | Confirmed: joint governance; staged T5 per IMP-099 |

**IMP-080 PASSED** — 14 T5 records physically verified in YAML on 2026-05-14. All 6 entity-type result blocks present in `tier_5_entity_type_results`.

**IMP-104 PASSED** — Orange Township / Hasson Joint Cemetery flagged `CROSS_COUNTY_CANDIDATE` in `identity_notes_raw` (Hancock + Wood counties). All other T5 entities are single-county.

**UNCONFIRMED_NAME follow-ups required:**
1. Eagle Township / Bishop Cemetery → fetch `Eagle_Township_24_23_Hancock_FINAL.pdf` from Ohio Auditor
2. Jackson Township / Houcktown Cemetery → fetch `jacksontwp.net/Cemetery.shtml` + `Jackson_Township_23_22_Hancock_FINAL.pdf`
3. Portage Township → fetch Portage Township audit or contact trustees: 9313 County Road 203, Van Buren OH 45889

---

### Tier 6 — Municipal 🔄 IN PROGRESS

**Pre-start checklist:**
- [x] Read `na_municipal_discovery_subproc.md` v5.12 (IMP-075 ✓)
- [x] Confirm YAML top-level keys intact (115 records, all keys verified ✓)
- [x] Note: Hancock County is NOT in the Parks_and_Open_Space CSV 15-county region — CSV cross-reference not required

**⚠️ T3 PARTIAL DEFECT DISCOVERED (during T6):**
HPD manages community parks in villages under cooperative agreements — these were missed during T3 discovery. HPD community parks program covers: Arcadia, Benton Ridge, Bluffton, Vanlue, Van Buren, McComb, Mt. Blanchard, **Jenera, Rawson, Mt. Cory** (last three NOT in T6 municipality list — potential missing municipalities). Governance = HPD → discovery_tier = 3.
- Arcadia Lions Community Park: staged at T3 (163 total records) ✓
- Remaining HPD community parks: staged at T3 as discovered during T6 review
- **Jenera, Rawson, Mt. Cory**: not in T6 municipality list — need verification if incorporated villages requiring T6 entries; add to post-T6 review
- Remediation reference: `na_district_discovery_subproc.md` §HPD community parks program

**Municipality list (10 total):**
- [✓] Findlay (city — 25 Sites, 3 Trails, 1 Site Network staged; IMP-080 ✓; null docs ✓; 29 records total; IMP-099 ✓)
- [✓] Fostoria (city — LOCAL-003; 10 Sites, 6 Trails staged; null docs ✓; IMP-099 ✓; IMP-104 ✓; 16 records; Seneca/Wood parks excluded; COUNTY_VERIFY noted on R1/R4/R6)
- [✓] Arlington (village — 2 Sites: Arlington Village Park + Arlington Swimming Pool; null docs ✓; IMP-099 ✓ cemetery=Clay Twp/T5, golf=null; IMP-104 ✓)
- [✓] Arcadia (village — park is HPD-managed; staged at T3; T6 entities = null; null docs ✓; IMP-099 ✓)
- [✓] Benton Ridge (village — park is HPD-managed; staged at T3 [Benton Ridge Community Park Site + Trail]; T6 entities = null; null docs ✓; IMP-099 ✓ cemetery=null, golf=null)
- [✓] Bluffton (village — LOCAL-005 straddles Hancock/Allen; 3 Sites (Buckeye Park, Village Park, Pool — all CROSS_COUNTY_CANDIDATE) + 1 Trail (Bluffton Bicycle Pathway — CROSS_COUNTY_CANDIDATE) + 1 Site (Maple Grove Cemetery IMP-099); null docs ✓; IMP-099 ✓ golf=null/private; IMP-104 ✓)
- [✓] McComb (village — Cloe Greiner Community Park=HPD/T3; McComb Pool=T6 Site/Village of McComb; joint cemetery=T5; null docs ✓; IMP-099 ✓ golf=null)
- [✓] Mount Blanchard (village — Island Park=HPD/T3; Hurricane Park=T6 Site; Mt. Blanchard Pool=T6 Site; Cemetery=Delaware Twp/T5; null docs ✓; IMP-099 ✓ golf=null)
- [✓] Van Buren (village — Hoadley Park=T6 Site; Sportsplex=Allen Twp/T5 DEFECT REMEDIATED; null docs ✓; IMP-099 ✓ cemetery=Allen Twp/T5, golf=null)
- [✓] Vanlue (village — park is HPD-managed; staged at T3 [Vanlue Community Park]; T6 entities = null; null docs ✓; IMP-099 ✓ cemetery=null, golf=null)

**T6 Web Discovery COMPLETE. Map verification pass (IMP-015/IMP-031) pending before tier sign-off.**

**T6 Governance Routing Summary (T3 additions discovered during T6):**
- HPD community parks staged at T3: Arcadia Lions Community Park, Benton Ridge Community Park (+ Trail), Vanlue Community Park, Island Park (Mt. Blanchard) + Access Point, Cloe Greiner Community Park (McComb)
- T5 defect remediated: Van Buren Sportsplex (Allen Township)
- Village-governed T6 entities: Hoadley Park (Van Buren), Hurricane Park (Mt. Blanchard), Mt. Blanchard Pool, McComb Pool, Buckeye Park (Bluffton), Bluffton Village Park, Bluffton Community Pool, Bluffton Bicycle Pathway, Maple Grove Cemetery (Bluffton)

---

### T6 Captured Source Data

#### Findlay — City Facility Directory (IMP-030)
Source: https://www.findlayohio.gov/community/facility-directory-list (pages 1–2, fetched this session)
Source: https://www.findlayohio.gov/government/city-departments/parks-and-recreation/city-parks (nav sidebar)

| # | Facility Name | Address | Category |
|---|--------------|---------|----------|
| 1 | All Star Playground | 3430 North Main St | Park / playground |
| 2 | Bernard Park | 1105 Bernard Ave | Park |
| 3 | Blanchard Valley Health System Miracle Park | 3430 North Main St | Park / accessible play |
| 4 | Cooper Field | 501 Broad Ave | Athletic field |
| 5 | Dorney Plaza | 318 Dorney Plaza | Civic plaza |
| 6 | Eagle Creek Park | 526 Hancock St | Park (CITY — distinct from HPD Eagle Creek Conservation Area at CR 236) |
| 7 | Ede Park | 175 Rutherford Ave | Park |
| 8 | Emory Adams Park | 1827 South Blanchard St | Park |
| 9 | Firestine Park (Firestine 9-Hole Disc Golf Park) | 900 Fifth St | Park / disc golf |
| 10 | Flag City Sports Complex | 3430 North Main St | Sports complex |
| 11 | Guthrie Field | 1827 South Blanchard St | Athletic field |
| 12 | Hancock Field | 1827 South Blanchard St | Athletic field |
| 13 | Koehler Field | 1000 South Blanchard St | Athletic field |
| 14 | Marathon Diamonds | 3430 North Main St | Athletic field |
| 15 | Millstream Art Plaza | 419 South Main St | Plaza / public art |
| 16 | Rawson Park | 720 River St | Park |
| 17 | Remington Field | 1827 South Blanchard St | Athletic field |
| 18 | Riverside Park | 231 McManness Ave | Park |
| 19 | Riverside Swimming Pool | 231 McManness Ave | Pool / recreation |
| 20 | Roethlisberger Field | 3430 North Main St | Athletic field |
| 21 | Swale Park | 500 North West St | Park |
| 22 | The Cube Ice Arena | 3430 North Main St | Indoor recreation |
| 23 | West Park | 1425 Byal Ave | Park |
| 24 | Centennial Park | Tarhe Trail area | Park (cross-tier: also in HPD/T3 list) |
| 25 | Great Karg Well Historical Site | TBD | Historic site (cross-tier: HPD/T3 list) |
| 26 | River Landings | Riverside Dr area | Park / river access (cross-tier: HPD/T3 list) |
| 27 | Waterfalls Area | TBD | Natural feature / park (cross-tier: HPD/T3 list) |
| 28 | Riverside Park Waterfront | 231 McManness Ave area | Park (HPD cancelled mgmt Jan 1 2026 → now City) |

**IMP-099 Cemetery:** Maple Grove Cemetery — 1120 West Main Cross St — managed by Public Works (not Parks & Rec) ✓
**IMP-099 Golf course:** CONFIRMED NULL — no city-owned traditional golf course in Findlay; Firestine disc golf already staged as Firestine Park ✓

**T3 cross-tier notes:**
- Centennial Park, Great Karg Well Historical Site, River Landings, Waterfalls Area: City of Findlay owned; previously listed in HPD inventory. Need T6 records with `identity_notes_raw: CROSS_TIER:T3`
- Riverside Park Waterfront: HPD cancelled management Jan 1, 2026 → City-managed. Needs T6 record.
- Eastpoint Area (T3): Listed as "Hancock County owned" — needs COUNTY_VERIFY (T4 found no county parks; parcel verification needed)

---

#### Fostoria — City Parks & Reservoir System (IMP-030)
Source: https://fostoriaohio.gov/parks-and-rec (fetched this session)
Source: https://fostoriaohio.gov/fountain-cemetery (fetched this session)
Source: https://www.destinationsenecacounty.org/place/fostoria-reservoirs/ (fetched this session)
Source: https://www.alltrails.com/trail/us/ohio/lake-mosier-reservoir-4 (GPS coordinates R4)

**LOCAL-003 rule applied: only Hancock County portion staged.**
Parks explicitly labeled Seneca County (Foundation Park, Buckley St Courts, Harmon Park, Jackson Park, Iron Triangle Rail Park) and Wood County (Portage Park) are EXCLUDED from Hancock County staging.

| # | Facility Name | Address / Location | County | Category |
|---|--------------|-------------------|--------|----------|
| 1 | City Park | Vine St between Elm & Fremont | **Hancock** | Park |
| 2 | Fostoria City Pool (Water Park) | 932 Vine St & Park Drive | **Hancock** | Pool |
| 3 | Gray Park | Vine St between Elm & Fremont (across from City Park) | **Hancock** | Park |
| 4 | Fountain Cemetery | 702 Van Buren Street | **Hancock** | Cemetery (IMP-099) |
| 5 | Lake Daugherty (Reservoir 1) | Near Vine St edge of town; Herbert Court parking | **Hancock** (birding hotspots) | Reservoir / Recreation |
| 6 | Lake Mottram (Reservoir 2) | Adjacent to City Park, Hancock County | **Hancock** | Reservoir / Recreation |
| 7 | Lake Lamberjack (Reservoir 3) | Adjacent to Lake Mottram | **Hancock** | Reservoir / Recreation |
| 8 | Lake Mosier (Reservoir 4) | Hancock CR 23 SW of Fostoria; GPS 41.14035, -83.43078 | **Hancock** | Reservoir / Recreation |
| 9 | Lake LeComte (Reservoir 5) | Hancock CR 23, 3 mi N of SR 224 | **Hancock** (confirmed) | Reservoir / Recreation |
| 10 | Veterans Memorial Reservoir (R6) | Hancock CR 23 area | **Hancock** (hiiker.app) | Reservoir / Recreation |
| — | Foundation Park | S Union St & Woodland Ave | Seneca | EXCLUDED |
| — | Buckley Street Courts | Buckley St & Eastern Ave | Seneca | EXCLUDED |
| — | Harmon Park | Wood & Fourth Streets | Seneca | EXCLUDED |
| — | Jackson Park | Jackson St W of Buckley | Seneca | EXCLUDED |
| — | Iron Triangle Rail Park | Columbus Ave & Poplar St | Seneca | EXCLUDED |
| — | Portage Park | Perrysburg Rd (SR 199) | Wood | EXCLUDED |

**Trail entities (one per Hancock County reservoir):**

| # | Trail Name | Length | Surface | At Reservoir |
|---|-----------|--------|---------|-------------|
| 1 | Lake Daugherty Walking Trail | 0.6 mi | Stone | R1 |
| 2 | Lake Mottram Walking Trail | 0.69 mi | Paved | R2 |
| 3 | Lake Lamberjack Walking Trail | 1.29 mi | Paved | R3 |
| 4 | Lake Mosier Walking Trail | 1.49 mi | Stone | R4 |
| 5 | Lake LeComte Walking Trail | 1.8 mi | Stone | R5 |
| 6 | Veterans Memorial Reservoir Walking Trail | 2.3 mi | Stone | R6 |

**IMP-099 Cemetery:** Fountain Cemetery — 702 Van Buren Street — managed by Cemetery & Parks Dept; 38+ acres; Hancock County confirmed ✓
**IMP-099 Golf course:** CONFIRMED NULL — Fostoria Golf Club and Loudon Meadows are privately operated; no city-owned golf course ✓
**Aeraland COUNTY_VERIFY:** Aeraland Recreation Area is HPD-managed (T3) — not a city of Fostoria entity; no T6 record needed ✓

---

### Tier 7 — Captured Source Data (IMP-030, 2026-05-15)

#### Black Swamp Conservancy — Land We Own (fetched 2026-05-15)
Source: https://blackswamp.org/properties/land-we-own/

| Preserve | Geographic Evidence | County | Hancock? |
|---------|---------------------|--------|----------|
| Bell Woods NP | "next to Conservancy HQ, 4825 Sugar Ridge Rd, Pemberville" | Wood | NO |
| Buttonwood Island NP | Adjacent to Howard Island, Grand Rapids area | Wood | NO |
| Dr. Robert L. Nehls Memorial NP | Linked from Quinstock page (Catawba Island) | Ottawa | NO |
| Forder Bridge River Access Site (Forrest Woods) | "Maumee River Trail Access Site" (listing note) | varies | NO |
| Forrest Woods NP | Maumee River corridor | varies | NO |
| Heron Crest NP | "1.2 miles of the Maumee River in northwest Ohio" | NW Ohio, not Hancock | NO |
| Howard Island NP | "Maumee River at Grand Rapids, Ohio" | Wood | NO |
| Little Auglaize Wildlife Reserve | "226-acre...in Paulding County" | Paulding | NO |
| Pat & Clint Mauk's Prairie | "next to Conservancy HQ at 4825 Sugar Ridge Rd, Pemberville" | Wood | NO |
| Quinstock Woods Preserve | "Located in Catawba Island Township" | Ottawa | NO |
| Rotary Riverside Preserve | "mile of the Maumee River"; GPS [41.41356537,-84.02944543] | Putnam | NO |
| St. Joseph River Confluence Preserve | St. Joseph River system | Allen/Defiance area | NO |
| St. Joseph River Floodplain Preserve | St. Joseph River system | Allen/Defiance area | NO |
| Water's Edge NP | "61 acres along the Sandusky River" | Sandusky/Seneca | NO |
| Webber Woods Preserve | "Toledo's Point Place neighborhood" | Lucas | NO |
| Weisgerber-Pohlman NP | "75-acre property along the Tiffin River" | Fulton/Henry area | NO |

#### Black Swamp Conservancy — Land We Protect (publicly accessible, fetched 2026-05-15)
Source: https://blackswamp.org/properties/land-we-protect/

| Property | Finding | Hancock? |
|---------|---------|----------|
| Blanchard River NP | Purchased by BSC 2013, donated to HPD — **already T3 entity** | YES (T3 only) |
| All others (17 entries) | Ottawa/Lucas/Wood/Sandusky/Geauga/Wayne counties | NO |

**Key finding:** BSC is solely a historical donor for Blanchard River NP; currently HPD-owned/managed. No active BSC ownership or easement in Hancock County.

#### The Nature Conservancy Ohio (fetched 2026-05-15)
Source: https://www.nature.org/en-us/about-us/where-we-work/united-states/ohio/places-we-protect/

8 named preserves; none in Hancock County:
- Northern Ohio: Great Egret Marsh (Ottawa Co.), Kitty Todd (Lucas Co.), Morgan Swamp (Ashtabula Co.), Herrick Fen (Portage Co.), Lucia S. Nash (Erie Co.)
- Central/Southern Ohio: Brown's Lake Bog (Wayne Co.), Big Darby Headwaters (Logan Co.), Edge of Appalachia (Adams Co.)

#### Western Reserve Land Conservancy (fetched 2026-05-15)
Source: https://wrlandconservancy.org/

Headquarters: 3850 Chagrin River Road, Moreland Hills, OH (Cuyahoga County). Mission: "northeast Ohio." 29-county footprint described as "northern and eastern Ohio from Sandusky Bay to Pennsylvania border." Hancock County (NW Ohio) is outside service area. No Hancock County projects found.

#### ONAPA Preserve Map (fetched 2026-05-15)
Source: https://www.onapa.org/preserve-map.html

Page redirects to ODNR nature preserves finder: http://naturepreserves.ohiodnr.gov/findapreserve — same database as T2 ODNR DNAP GIS query (confirmed 0 state nature preserves in Hancock County, FIPS 063).

#### Ducks Unlimited (web search, 2026-05-15)
No Hancock County conservation easements found. DU easements are generally private with no public access requirement — below T7 threshold even if they existed. Confirmed null.

#### ODNR Voluntary Protection Program (web search, 2026-05-15)
No Hancock County results. Cross-reference to T2 ODNR DNAP null (0 state nature preserves, Hancock County). Confirmed null.

---

### Tier 8 — Captured Source Data (IMP-030, 2026-05-16)

#### Camp Berry — Black Swamp Area Council BSA (fetched 2026-05-16)
Source: https://www.blackswampbsa.org/camping/camp-berry/63302

| Field | Value |
|-------|-------|
| Name | Camp Berry |
| Address | 11716 CR 40, Findlay, OH 45840 |
| Council | Black Swamp Area Council, Boy Scouts of America (Scouting America) |
| Acreage | 360 acres |
| Water feature | 4-acre lake; Eagle Creek runs through property |
| Nature center | Karl Edelbrock Nature Center (wildlife pond) |
| Established | 1928 (donated by R.J. Berry family) |
| Access type | In-council groups (reservation); out-of-council group rentals available |
| Council office | 2100 Broad Ave, Findlay, OH 45840 |
| Governance | Private nonprofit (BSA/Scouting America) — T8 |

**Key finding:** Facility rentals available to out-of-council groups (packs, troops, crews, crews) — qualifies as organized group access per T8 sub-procedure §5.1.

#### Findlay Reservoirs 1 & 2 — City of Findlay / ODNR Cooperative (fetched 2026-05-16)
Sources: https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/findlay-reservoir-1-fishing-area | https://hiking-ohio.com/findlay-waterworks-reservoirs-and-riverbend-activity-area/ | https://norrik.com/fishing-spots/ohio/findlay-reservoirs-1-and-2/

| Field | Reservoir #1 | Reservoir #2 |
|-------|-------------|-------------|
| Acres | 186 | 645 |
| Built | 1950 (City of Findlay) | 1968 (City of Findlay + ODNR co-built) |
| Dike shoreline | 2.0 miles | 4.3 miles |
| Depth range | 20–28 ft (avg 24) | 16–33 ft (avg 24) |
| Motors | Electric only | 9.9HP max outboard |
| Boat ramp | Primitive ramp + floating pier | Standard ramp + EZ Launch |
| Restrooms | Near boat ramp (Riverbend RA) | At boat ramp |
| Parking | Handicapped accessible | Standard |
| Dike trail | 2.0 mi segment | 4.3 mi segment |
| ODNR page | Findlay Reservoir #1 Fishing Area (Find a Property) | Listed on ODNR fishing maps PDF |
| Governance | City of Findlay — Water Department + ODNR DOW cooperative | City of Findlay — Water Department + ODNR DOW cooperative |
| GPS (approx) | 41.0447, -83.6476 (hiking-ohio.com) | Pending GPS Acquisition Module |

**Combined dike trail:** Shared dike = 1.0 mi; outer perimeter of combined reservoir system = 5.3 miles.

**Governance finding:** City of Findlay owns both reservoirs. ODNR GIS Hancock County query (T2, 2026-05-13) returned no ODNR-owned parcel matching these reservoirs → confirmed City of Findlay ownership. ODNR has cooperative fishing management only. Staged as **T6 miss** (City of Findlay / Water Department).

#### McComb Reservoirs 1 & 2 — Village of McComb / ODNR Cooperative (fetched 2026-05-16)
Sources: https://www.villageofmccomb.com/parks-and-amenities | https://dam.assets.ohio.gov/image/upload/ohiodnr.gov/documents/wildlife/maps/mccomb.pdf | https://birdinghotspots.org/hotspot/L508567

| Field | Reservoir 1 | Reservoir 2 |
|-------|-------------|-------------|
| Acres | 6 | 20 |
| Shoreline | 0.40 miles | 0.70 miles |
| ODNR survey | 2013 | 2013 |
| Fishing | Public (electric motors; no ice fishing) | Public (electric motors; no ice fishing) |
| Boat ramp | Yes (shared facility) | Yes |
| Restrooms | Yes | Yes |
| Parking | Yes | Yes |
| GPS (approx) | lat=41.1056, lon=-83.7806 (from ODNR PDF map graticule) | Same complex |
| eBird hotspot | L508567 — McComb Village Park and Reservoirs | L508567 |
| Walk trail | 1-mile paved walk/fitness trail around both reservoirs | — |
| Governance | Village of McComb + ODNR DOW cooperative | Village of McComb + ODNR DOW cooperative |

**Associated park complex amenities (Village of McComb park, T6):** Zero-entry swimming pool with splash pad + 2 water slides (= McComb Pool, already staged T6); 2 tennis courts; basketball court; 5 shelter houses (free). Adjacent to Cloe Greiner Community Park (HPD/T3).

**Governance finding:** Village of McComb owns. ODNR has cooperative fishing management only. Staged as **T6 miss** (Village of McComb).

#### ODNR Licensed Hunting Preserves — Hancock County (web search, 2026-05-16)
Source: ODNR Pub 5129 (Wild Animal Hunting Preserve Requirements); web search

No public online registry of licensed hunting preserves exists. Per ODNR Pub 5129: "A list of all wild animal hunting preserves may be obtained from the Division of Wildlife by contacting any district office." ODNR Wildlife District Two office covers Hancock County: 952 Lima Ave, Findlay OH 45840; (419) 424-5000. Web search returned no hunting preserves in Hancock County. **Result: NULL.**

#### Private Golf Courses — IMP-099 (web search, 2026-05-16)
- Findlay Country Club (1500 Country Club Dr, Findlay OH) — private, confirmed T4 pass (already noted in T4 checklist as golf null per county governance check; Findlay CC is privately operated). No staging needed.
- Fostoria Country Club (747 Independence Ave, Fostoria OH 44830) — confirmed **Seneca County** per Destination Seneca County listing and geographic position. Out of scope for Hancock County run.
- All other Hancock County golf courses identified (Sycamore Springs, Red Hawk Run, Shady Grove) are public/semi-private daily-fee courses — not private membership clubs requiring T8 staging.
**Result: NULL for T8.**

---

### LOCAL-007 — Cemetery Supplemental Pass Captured Source Data (IMP-030, 2026-05-17)

#### OhioGenealogyExpress — Hancock County Cemetery Index (fetched 2026-05-17)
Source: https://ohiogenealogyexpress.com/hancock/hancockco_cems.htm

**70 unique cemetery names** (77 listed entries, 2 exact duplicates: Enon Valley ×2, Hickory Grove ×2).

**Already staged (16 names → 17 DB entries):** Arcadia, Bechel (=Bechtel), Bishop, Brights (=Bright), Cannonsburg (=Cannonsburg Joint), Elm Grove, Enon Valley, Fountain, Hamlin (=Baker-Hamlin), Hancock County Infirmary, Hassan+Hasson (=Hasson Joint), Maple Grove (Allen County), McComb Union, Mount Blanchard, Van Horn.

**Unstaged and upserted LOCAL-007 (54 entries):**

| ID | Name | Subtype | GPS |
|----|------|---------|-----|
| HAN-S-113 | Bethel Cemetery | Church Cemetery | 41.162271, -83.708595 |
| HAN-S-114 | Saint Michael Cemetery | Church Cemetery | 41.043535, -83.663866 |
| HAN-S-115 | Saint Pauls Cemetery | Church Cemetery | 40.884329, -83.689918 |
| HAN-S-116 | Saint Wendelin Cemetery | Church Cemetery | 41.16128, -83.431501 |
| HAN-S-117 | Salem Cemetery | Church Cemetery | 40.958677, -83.575099 |
| HAN-S-118 | Trinity Cemetery | Church Cemetery | 40.885302, -83.718523 |
| HAN-S-119 | Zion Bloom Cemetery | Church Cemetery | 40.947285, -83.486928 |
| HAN-S-120 | Hedges Family Cemetery | Family Cemetery | 41.058386, -83.679933 |
| HAN-S-121 | Horn Family Cemetery | Family Cemetery | 41.080886, -83.842161 |
| HAN-S-122 | Wells Family Cemetery | Family Cemetery | 41.122554, -83.478538 |
| HAN-S-123 | Memory Gardens Cemetery | Private Cemetery | 41.099223, -83.530635 |
| HAN-S-124 | Adams Cemetery | Public Cemetery | 40.872849, -83.518237 |
| HAN-S-125 | Alspach Cemetery | Public Cemetery | 41.006953, -83.558318 |
| HAN-S-126 | Ark Cemetery | Public Cemetery | 41.15885, -83.507283 |
| HAN-S-127 | Arlington Cemetery | Public Cemetery | 40.900131, -83.661995 |
| HAN-S-128 | Aurand Cemetery | Public Cemetery | 41.029677, -83.714555 |
| HAN-S-129 | Benton Ridge Cemetery | Public Cemetery | 41.003533, -83.800251 |
| HAN-S-130 | Biglick Cemetery | Public Cemetery | 41.035323, -83.440557 |
| HAN-S-131 | Castor Cemetery | Public Cemetery | 40.89195, -83.604598 |
| HAN-S-132 | Clymer Cemetery | Public Cemetery | 40.950463, -83.873484 |
| HAN-S-133 | Davis Cemetery | Public Cemetery | 41.059731, -83.57318 |
| HAN-S-134 | Dukes Cemetery | Public Cemetery | 41.051191, -83.822776 |
| HAN-S-135 | Eagle Creek Cemetery | Public Cemetery | 40.835072, -83.704277 |
| HAN-S-136 | Earlywine Cemetery | Public Cemetery | 40.870083, -83.588318 |
| HAN-S-137 | Ellis Cemetery | Public Cemetery | 40.957756, -83.62578 |
| HAN-S-138 | Ewing Cemetery | Public Cemetery | 41.057416, -83.496332 |
| HAN-S-139 | Five Points Cemetery | Public Cemetery | 40.920079, -83.514053 |
| HAN-S-140 | Flick Cemetery | Public Cemetery | 40.988269, -83.787745 |
| HAN-S-141 | Frontiers Repose Cemetery | Public Cemetery | null |
| HAN-S-142 | Graham Cemetery | Public Cemetery | 41.040265, -83.446794 |
| HAN-S-143 | Hartman Cemetery | Public Cemetery | 40.968933, -83.708535 |
| HAN-S-144 | Hickory Grove Cemetery | Public Cemetery | 41.006953, -83.558318 |
| HAN-S-145 | High Bank Cemetery | Public Cemetery | null |
| HAN-S-146 | Indian Grove Cemetery | Public Cemetery | null |
| HAN-S-147 | Johnson Cemetery | Public Cemetery | 40.841052, -83.546136 |
| HAN-S-148 | Keller Cemetery | Public Cemetery | 40.928726, -83.72695 |
| HAN-S-149 | Knepper Cemetery | Public Cemetery | 41.003135, -83.778015 |
| HAN-S-150 | Krout Cemetery | Public Cemetery | 40.913756, -83.556137 |
| HAN-S-151 | Lee Cemetery | Public Cemetery | 40.949507, -83.513537 |
| HAN-S-152 | Line Cemetery | Public Cemetery | 40.941463, -83.670209 |
| HAN-S-153 | Maple Lawn Cemetery | Public Cemetery | null |
| HAN-S-154 | Pleasant Hill Cemetery | Public Cemetery | 41.12341, -83.702836 |
| HAN-S-155 | Powell Cemetery | Public Cemetery | 40.980385, -83.726901 |
| HAN-S-156 | Radar Cemetery | Public Cemetery | 41.131442, -83.649932 |
| HAN-S-157 | Riley Creek Cemetery | Public Cemetery | null |
| HAN-S-158 | Riverview Cemetery | Public Cemetery | 40.913647, -83.557145 |
| HAN-S-159 | Schellbas Cemetery | Public Cemetery | 40.877814, -83.804969 |
| HAN-S-160 | Schwartz Cemetery | Public Cemetery | 41.043962, -83.782044 |
| HAN-S-161 | Siddall Cemetery | Public Cemetery | 40.927887, -83.544373 |
| HAN-S-162 | Smith Cemetery | Public Cemetery | 40.943942, -83.818549 |
| HAN-S-163 | Thomas Cemetery | Public Cemetery | 41.148283, -83.755404 |
| HAN-S-164 | Thompson Cemetery | Public Cemetery | 40.862695, -83.850286 |
| HAN-S-165 | Union Cemetery | Public Cemetery | 41.075122, -83.453452 |
| HAN-S-166 | Williamstown Cemetery | Public Cemetery | 40.83579, -83.650889 |

**GPS method:** Nominatim/OSM, all MED confidence (landuse=cemetery polygon match). 5 GPS-null entries not found in OSM: Frontiers Repose, High Bank, Indian Grove, Maple Lawn, Riley Creek.

**Note:** Pleasant Hill Cemetery (HAN-S-154) is a candidate name for HAN-S-048 (Portage Township Cemetery, UNCONFIRMED_NAME). If contact with trustees (9313 CR 203, Van Buren OH 45889) confirms Pleasant Hill = Portage Township Cemetery, merge HAN-S-154 into HAN-S-048 and retire one record.
