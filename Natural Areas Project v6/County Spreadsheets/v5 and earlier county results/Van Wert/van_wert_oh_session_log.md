# Van Wert County, Ohio — Session Log
# Natural Areas Project v5.x | RUN_ID: van_wert_oh_2026_04_14 | PREFIX: VNW

---

## County Context

- **County seat**: Van Wert (city)
- **Cities**: Van Wert, Delphos (partial — mostly Allen County)
- **Villages**: Convoy, Elgin, Middle Point, Ohio City, Scott, Venedocia, Willshire, Wren
- **Townships (12)**: Harrison, Hoaglin, Jackson, Jennings, Liberty, Pleasant, Ridge, Tully, Union, Washington, Willshire, York
- **Adjacent counties**: Paulding (north), Putnam (northeast), Allen OH (east), Auglaize (southeast), Mercer (south), Allen IN / Adams IN (west)
- **Park district**: None
- **Known state presence**: ODNR Division of Wildlife (wildlife production areas)
- **Known conservancy presence**: Van Wert County Foundation (land acquisition), Black Swamp Conservancy (regional)

---

## Baseline Seeds (15 entries)

| Seed | Type | Notes | Status |
|------|------|-------|--------|
| Children's Garden and Butterfly House | Van Wert city park | Located within Smiley Park | Unconfirmed |
| Hiestand Woods | Van Wert city park | Purchased by Van Wert County Foundation | Unconfirmed |
| Ohio City Fireman's Park | Ohio City city park | — | Unconfirmed |
| Van Wert Convoy Edgewood Park | Van Wert city park | Unusual name — may be in Convoy? | Unconfirmed |
| Van Wert Fountain Park | Van Wert city park | Can be rented | Unconfirmed |
| Van Wert Franklin Park | Van Wert city park | Funded by Van Wert County Foundation | Unconfirmed |
| Van Wert Jubilee Park | Van Wert city park | — | Unconfirmed |
| Van Wert Memorial Park | Van Wert city park | Owned/cared for by American Legion Post 178 | Unconfirmed |
| Van Wert Reservoir 1 | Unknown | — | Unconfirmed |
| Van Wert Reservoir 2 | Unknown | — | Unconfirmed |
| Van Wert Reservoir Recreation Area | Van Wert city park | — | Unconfirmed |
| Van Wert Rotary Athletic Complex | Van Wert city park | — | Unconfirmed |
| Van Wert Smiley Park | Van Wert city park | Parent of Children's Garden | Unconfirmed |
| Van-Del Drive-In | Private park | 19986 Lincoln Highway, Middle Point OH 45863 | Unconfirmed |
| Whitey Case Wildlife Production Area | State Wildlife Production Area | 9 acres; ODNR Div. of Wildlife | Unconfirmed |

**Baseline notes**: Sparse — heavy concentration on Van Wert city parks. Missing expected ODNR state nature preserves, any county-level parks, township parks, and likely additional wildlife production areas. Van Wert County Foundation involvement in multiple parks warrants direct outreach/research.

---

## Discovery Progress

| Tier | Governance Level | Sites | Trails | Trail Segs | Trail Nets | Site Nets | APs | Status |
|------|-----------------|-------|--------|-----------|-----------|----------|-----|--------|
| 1 | Federal & Tribal | 0 | 0 | 0 | 0 | 0 | 0 | **NULL — Complete** |
| 2 | State | 3 | 1 | 0 | 0 | 0 | 0 | **Complete** |
| 3 | District | 1 | 0 | 0 | 0 | 0 | 0 | **Complete** |
| 4 | County | 0 | 0 | 0 | 0 | 0 | 0 | **NULL — Complete** |
| 5 | Township | 0 | 0 | 0 | 0 | 0 | 0 | **NULL — Complete** |
| 6 | Municipal | 11+2child | 1+Trail | 0 | 0 | 0 | 1 | **Complete — Delphos confirmed null (Allen County)** |
| 7 | Conservancy | 1 | 0 | 0 | 0 | 0 | 0 | **Complete** |
| 8 | Private | 1 | 0 | 0 | 0 | 0 | 0 | **Complete** |

---

## Session Notes

*(Tier-by-tier notes appended below as tiers are completed.)*

---

### DISCOVERY COMPLETE — 2026-04-15

**Total raw records**: 22 (YAML: 22 raw_record entries)
**Baseline seeds resolved**: 15/15
**New discoveries (not in baseline)**: 7 (Rotary Dog Park, Warrior Trail, Middle Point Ball Park, US 30 EB Rest Area, US 30 WB Rest Area, Whitey Case WPA via Tier 2, Children's Garden as child Site)
**Delphos parks**: 5 parks flagged (GPS_VERIFY_COUNTY) — not yet staged pending GIS verification

**Entity counts by tier**:
- T1: 0 (null)
- T2: 3 Sites (Whitey Case WPA, US 30 EB + WB Rest Areas)
- T3: 1 Site (Convoy Edgewood Park)
- T4: 0 (null)
- T5: 0 (null)
- T6: 14 entities (9 Sites + 2 child Sites + 1 Trail + 1 Access Point + 1 private Site)
- T7: 1 Site (Hiestand Woods)
- T8: 1 Site (Van-Del Drive-In, private)

**Status**: Ready for pipeline (pending 6 flags resolved; see handoff Next Steps).

---

### PRE-PIPELINE FLAG RESOLUTION — 2026-04-19

**Flags resolved this session**: 5 of 11

**1. Delphos GIS (GPS_VERIFY_COUNTY) — RESOLVED**
All 5 Delphos city parks are in Allen County (Marion Township). The Miami-Erie Canal (Canal Street) is the county boundary in Delphos. Stadium Park confirmed Allen County via ohiostadiums.com. visitvanwert.com lists no Delphos parks, consistent with no Van Wert County parks. Washington Township (Van Wert County) portion of Delphos is residential only. Open Question #3 closed. Delphos = Tier 6 null for Van Wert County.

**2. US 30 EB Storybook Trail (STORYBOOK_TRAIL_CONFIRM_NEEDED) — RESOLVED for EB**
Storybook trail confirmed at the US 30 Eastbound Convoy rest area via hometownstations.com governor's visit article (July 2025). Described as "an outdoor Storybook Trail in which small children can enjoy a walking path that includes stands with pages from a children's book, a project made possible in partnership with Dolly Parton's Imagination Library of Ohio." Trail record VNW-T2-004 created. WB facility (VNW-T2-003) likely also has a storybook trail per Wyandot County precedent but unconfirmed; flag retained on WB.

**3. Memorial Park (DETAILS_INCOMPLETE) — RESOLVED**
Features documented from vanwert.org/parks-department/memorial-park/: veteran monuments, parking lot, display of gardens, open grassy areas. Owned/cared for by American Legion Post #178. 611 W Main St.

**4. Fountain Park (DETAILS_INCOMPLETE) — RESOLVED**
Features documented from vanwert.org/parks-department/fountain-park/: gazebo with hanging flower baskets (Van Wert Evergreen Garden Club), Band Pavilion (Summer Music Series, Friday evenings June–August), concession stand, restrooms (open during scheduled activities), park benches. Downtown location at W Main & S Jefferson. Rentable.

**5. Van Wert Reservoir 2 GPS and acreage (GPS_VERIFY_NEEDED) — RESOLVED**
Acreage confirmed: 101 acres, 2.1 mi shoreline (ODNR lake map, surveyed 2014). GPS centroid: 40.8409°N, 84.5741°W (Ohio Hometown Locator / Ohio gazetteer).

**Partially resolved:**
- Reservoir 1: Acreage confirmed (61 acres, 1.2 mi shoreline, ODNR 2014). GPS centroid still pending.
- Van-Del Drive-In PRIVATE_VENUE_REVIEW: Removed (per IMP-073 logged 2026-04-15; drive-in theaters are in scope).

**Remaining flags (non-blocking)**: GPS_VERIFY_NEEDED (Whitey Case, Reservoir 1 GPS centroid), STORYBOOK_TRAIL_CONFIRM_NEEDED (WB rest area), LENGTH_VERIFY_NEEDED (storybook trail), DETAILS_INCOMPLETE (Ohio City Fireman's Park), FIELD_VERIFY_NEEDED (Hiestand Woods trails).

**New entity added**: VNW-T2-004 Convoy Rest Area Storybook Trail (Trail, Tier 2, ODOT, parent = VNW-T2-002)

**Total raw records**: 23

**Status**: All open questions resolved. Non-blocking flags remain. **READY FOR PIPELINE.**

---

### PIPELINE COMPLETE — 2026-04-19

**Script**: `van_wert_oh_pipeline.py`

**Stages executed**: Normalization → GPS Acquisition → TSV Output → Vocab Gate → Integrity Check → DB Upsert

**Results**:
- Stage 2 Normalization: 19 Sites, 3 Trails, 1 AP — all vocabulary checks PASSED
- Stage 3 GPS: 19/19 sites have GPS (14 HIGH/MED; 5 LOW fallback)
- Stage 4.5 Vocab Gate: PASSED — 0 violations
- Stage 5 Integrity: PASSED — 0 warnings
- Stage 6 DB: 19 Sites + 3 Trails + 1 AP committed to `natural_areas_v5.db`
- Run metadata: `van_wert_oh_2026_04_14` — input=23, normalized=23, held=0

**Entity IDs**: VNW-S-001 through VNW-S-019 (Sites); VNW-T-001 through VNW-T-003 (Trails); VNW-AP-001 (Access Point)

**Remaining non-blocking flags**: GPS_VERIFY_NEEDED (VNW-S-001 Whitey Case, VNW-S-008 Reservoir 1), STORYBOOK_TRAIL_CONFIRM_NEEDED (VNW-S-003 WB rest area), LENGTH_VERIFY_NEEDED (VNW-T-001 storybook trail), DETAILS_INCOMPLETE (VNW-S-016 Fireman's Park), FIELD_VERIFY_NEEDED (VNW-S-018 Hiestand Woods trail paths)

**Status**: **COUNTY COMPLETE.**

---

### Tier 1 — Federal & Tribal — NULL (2026-04-14)

**Result**: Null across all six entity types. No federal land ownership or management in Van Wert County.

**Sources checked**:
- NPS Find A Park — Van Wert County, OH → 0 results
- USFS national forest locator — no national forests in northwest Ohio
- USFWS NWR finder — no national wildlife refuges in Van Wert County
- USACE Ohio district project list — no USACE lakes, dams, or recreation areas in Van Wert County
- North Country Trail Association route — NCT goes through Fulton, Henry, Lucas, Williams; not Van Wert
- Buckeye Trail Association — Delphos section officially covers Auglaize, Allen, Putnam, Paulding; Van Wert not listed
- Ohio Admin Code 1501:31-15-04 — Whitey Case WPA is ODNR DOW = Tier 2 (State)
- ODNR State Nature Preserves guide PDF — zero preserves in Van Wert County

**Decisions / Flags**:
- Whitey Case Wildlife Production Area routed to Tier 2 (ODNR DOW)
- Buckeye Trail Delphos boundary flagged: Delphos straddles Van Wert/Allen line; BTA officially
  lists section under Allen/Auglaize/Putnam/Paulding only. No Van Wert-side BTA infrastructure found.
  Flag preserved for Tier 7 review if BTA has conservancy or easement presence on Van Wert side.
- Van Wert Reservoirs: city-owned water supply; ODNR manages fish stocking only; routed to Tier 6 (Municipal)

**Baseline seeds confirmed this tier**: 0

---

### Tier 7 — Conservancy — 1 Site (2026-04-15)

**Entities found**:
- T7-001: Hiestand Woods Park and Preserve (Van Wert County Foundation) — 78 acres, 1510 Hospital Dr, nature preserve paths (undocumented length/surface), ongoing modernization — baseline seed confirmed

**Other conservancy review**:
- WCOLC: serves Van Wert County but no confirmed holdings; flagged for monitoring
- BTA (Buckeye Trail): no Van Wert County presence confirmed; Delphos section = Allen/Auglaize/Putnam/Paulding only

**Tier 7 trail note**: Hiestand Woods has nature preserve paths but insufficient documentation (no name, length, surface) to create a Trail record. Flag for field verification. VWCF modernization plan includes boardwalk trail — stage trail record when construction data available.

**Baseline seeds confirmed this tier**: 1 (Hiestand Woods)

---

### Tier 8 — Private (2026-04-15)

**Entities found**:
- T8-001: Van-Del Drive-In (Middle Point, private entertainment venue) — staged for resolution review; PRIVATE_VENUE_REVIEW flag; likely excluded from NAP entity graph

**Baseline seeds confirmed this tier**: 1 (Van-Del Drive-In — baseline seed, staged for exclusion review)

---

### Tier 2 — State — 3 Sites, 0 other entities (2026-04-15)

**Entities found**:
- VNW-T2-001: Whitey Case Wildlife Production Area (ODNR DOW) — 9.29 acres, GPS ~40.80°N/84.79°W (approximate), baseline seed confirmed
- VNW-T2-002: Van Wert Rest Area — Eastbound (ODOT), US 30 MM 9, opened March 2025
- VNW-T2-003: Van Wert Rest Area — Westbound (ODOT), US 30 MM 9, opened March 2025

**Flags**:
- VNW-T2-001: GPS_VERIFY_NEEDED (toposports source; only 2 decimal places)
- VNW-T2-002 & 003: STORYBOOK_TRAIL_CONFIRM_NEEDED (at least one has storybook trail per governor's
  visit article; unknown which facility; trail records pending confirmation)

**Null agencies (Tier 2)**:
- ODNR Parks & Watercraft: null (no state parks)
- ODNR Forestry: null (no state forests)
- ODNR DNAP: null (no state nature preserves — confirmed prior session)
- ODNR Scenic Rivers: null (Auglaize not designated; Maumee not in county)
- Ohio History Connection: null ("Nothing Found" for Van Wert tag)
- ODOT bikeways/overlooks: null (rest areas staged)
- OTIC: null (US 30 ≠ Ohio Turnpike)
- Public universities: null

**Sources checked**:
- Ohio Admin Code 1501:31-15-04 — "Whitey case" confirmed for Van Wert County
- toposports.com hunting layer — Whitey Case: 9.29 acres, GPS ~40.80/84.79
- ohiorestareas.com — EB and WB MM 9 US 30 confirmed as Van Wert Rest Areas
- thevwindependent.com (3 articles) — construction, reopening, governor's ribbon cutting details
- trekohio.com/vanwert/ — full county parks inventory (no state lands listed beyond what staged)
- visitvanwert.com/outdoor-adventure/ — full county parks list with addresses
- ohiohistory.org/tag/van-wert/ — "Nothing Found"

**Baseline seeds confirmed this tier**: 1 (Whitey Case Wildlife Production Area)

---

### Tier 3 — District — 1 Site (2026-04-15)

**Entities found**:
- VNW-T3-001: Convoy Edgewood Park (Tully-Convoy Park District) — 643 N Main St, Convoy; 4 diamonds, 2 basketball courts, playground, community building, pavilion, scenic pond; baseline seed confirmed

**Open Question #1 RESOLVED**: Convoy Edgewood Park is managed by the **Tully-Convoy Park District** (statutory, PO Box 302 shared with park), not the Village of Convoy. Tier 3, not Tier 6.

**Null agencies**:
- Van Wert SWCD: null (conservation programs; no land holdings)
- Watershed/conservancy districts: null (none in Van Wert County)
- Metro parks: null (no metro parks system)
- Other park districts: null (only Tully-Convoy found in Ohio Auditor search)

**Trail note**: Warrior Trail in Ohio City (2.6 mi, rail-trail, asphalt/gravel) — managed by Village of Ohio City (Tier 6 Municipal). Wabash Cannonball Trail confirmed NOT in Van Wert County.

**Baseline seeds confirmed this tier**: 1 (Van Wert Convoy Edgewood Park = Tully-Convoy Park District Edgewood Park)

---

### Tier 6 — Municipal — 11+ Sites, 1 Trail, 1 Access Point (2026-04-15)

**City of Van Wert entities staged**:
- T6-001: Smiley Park (29.4 ac, 1451 Leeson Ave) — baseline confirmed
  - T6-001a: Children's Garden & Butterfly House (child Site) — baseline confirmed
- T6-002: Van Wert Reservoir Recreation Area (S Washington St) — baseline confirmed
  - T6-002a: Van Wert Reservoir 1 (child Site) — baseline confirmed
  - T6-002b: Van Wert Reservoir 2 (child Site, ~100 ac) — baseline confirmed
  - T6-002c: Van Wert Reservoir Health Trail (3.1 mi paved loop) — Trail
  - T6-002d: Reservoir Boat Launch — Access Point
- T6-003: Franklin Park (305 Frothingham St) — baseline confirmed
- T6-004: Jubilee Park (137 Gleason Ave) — baseline confirmed
- T6-005: Memorial Park (611 W Main St) — DETAILS_INCOMPLETE — baseline confirmed
- T6-006: Fountain Park (210 W Main St) — DETAILS_INCOMPLETE — baseline confirmed
- T6-007: Rotary Athletic Complex (9085 John Brown Rd) — baseline confirmed
- T6-008: Rotary Dog Park (1264 S Washington St) — NEW (not in baseline)

**Village of Ohio City entities staged**:
- T6-009: Fireman's Park (St Rt 118) — DETAILS_INCOMPLETE — baseline confirmed
- T6-010: Warrior Trail (2.6 mi rail-trail, Ohio City Greenway Project) — NEW (not in baseline)

**Village of Middle Point**:
- T6-011: Middle Point Ball Park (406 N Adams St) — NEW (not in baseline)

**Delphos — FLAGGED** (GPS_VERIFY_COUNTY): 5 parks (Stadium, Waterworks, Leisure, Garfield, Suever); county side unknown; GIS review needed. Open Question #3 still open.

**Private (staged as T8)**:
- T8-001: Van-Del Drive-In (Middle Point) — PRIVATE_VENUE_REVIEW — baseline confirmed

**Open Question #2 RESOLVED**: Reservoirs 1 & 2 are child Sites within the Reservoir Recreation Area.

**Baseline seeds confirmed this tier**: 11 of 15 total baseline seeds now confirmed (Whitey Case T2, Edgewood Park T3, and 9 city/village parks T6). Remaining unconfirmed: Van-Del Drive-In (staged T8, needs Resolution review).
