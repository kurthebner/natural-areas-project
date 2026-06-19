# Van Wert County, Ohio — Handoff Document
# Natural Areas Project v5.x | RUN_ID: van_wert_oh_2026_04_14 | PREFIX: VNW
# Last updated: 2026-04-19 | PIPELINE COMPLETE | 23 records → 19 Sites, 3 Trails, 1 AP upserted to natural_areas_v5.db

---

## Tiers Completed

| Tier | Governance Level | Result | Entities | Notes |
|------|-----------------|--------|----------|-------|
| 1 | Federal & Tribal | NULL | 0 | No federal land, no federal trails. Whitey Case → Tier 2. Buckeye Trail Delphos boundary flagged for Tier 7. |
| 2 | State | 3 Sites | 3 | Whitey Case WPA (ODNR DOW, 9.29 ac); US 30 EB Rest Area (ODOT, MM9); US 30 WB Rest Area (ODOT, MM9). All other state agencies null. Storybook trail(s) at rest areas to confirm. |
| 3 | District | 1 Site | 1 | Convoy Edgewood Park (Tully-Convoy Park District). SWCD: null. No other districts. Open Q#1 resolved: Convoy Edgewood Park = Tier 3 (Tully-Convoy PD), not Tier 6. |
| 4 | County Government | NULL | 0 | No county parks department, no county-owned parks. LWCF "Van Wert County Park District" likely = Tully-Convoy PD or defunct. |
| 5 | Township | NULL | 0 | All 12 townships confirmed rural fire/road entities; no township parks or natural areas found. |
| 6 | Municipal | 11+ Sites, 1 Trail, 1 AP | 13+ | City of Van Wert: 8 parks (Smiley, Reservoirs, Franklin, Jubilee, Memorial, Fountain, Rotary AC, Rotary Dog Park) + child Sites + Health Trail + Boat Launch. Ohio City: Fireman's Park + Warrior Trail (2.6 mi rail-trail). Middle Point: Ball Park. Delphos: 5 parks flagged (GPS_VERIFY_COUNTY). Van-Del Drive-In: T8 (in scope per IMP-073). |
| 7 | Conservancy | 1 Site | 1 | Hiestand Woods (Van Wert County Foundation, 78 ac). WCOLC unconfirmed. Hiestand Woods trail paths undocumented — field verify. |
| 8 | Private | 1 | 1 | Van-Del Drive-In (Middle Point) — in scope per IMP-073 (private entertainment venues included). |

---

## Tiers Remaining

**ALL TIERS COMPLETE** — Discovery phase finished. See "Held Items / Verification Needed" section for outstanding flags.

| Tier | Status |
|------|--------|
| 1 | COMPLETE — NULL |
| 2 | COMPLETE — 3 Sites (Whitey Case WPA, US 30 EB + WB Rest Areas) |
| 3 | COMPLETE — 1 Site (Convoy Edgewood Park, Tully-Convoy PD) |
| 4 | COMPLETE — NULL |
| 5 | COMPLETE — NULL |
| 6 | COMPLETE — 13+ entities; Delphos 5 parks pending GPS_VERIFY_COUNTY |
| 7 | COMPLETE — 1 Site (Hiestand Woods, VWCF) |
| 8 | COMPLETE — 1 (Van-Del Drive-In, in scope per IMP-073) |

---

## Key Active Flags

| Flag | Entity | Action Required |
|------|--------|-----------------|
| GPS_VERIFY_NEEDED | VNW-T2-001 Whitey Case WPA | Get authoritative GPS coords (toposports source; 2 decimal places only) |
| ~~STORYBOOK_TRAIL_CONFIRM_NEEDED~~ | ~~VNW-T2-002 US 30 EB Rest Area~~ | **RESOLVED 2026-04-19** — Trail confirmed; VNW-T2-004 staged |
| STORYBOOK_TRAIL_CONFIRM_NEEDED | VNW-T2-003 US 30 WB Rest Area | Confirm storybook trail also at WB; create VNW-T2-005 if confirmed |
| LENGTH_VERIFY_NEEDED | VNW-T2-004 Convoy Storybook Trail | Trail length not documented — ODOT contact or field measurement needed |
| ~~GPS_VERIFY_COUNTY~~ | ~~Delphos 5 parks~~ | **RESOLVED 2026-04-19** — All 5 Delphos parks in Allen County; Van Wert = null |
| GPS_VERIFY_NEEDED | VNW-T6-002a Reservoir 1 | Acreage now confirmed (61 ac, ODNR 2014); GPS centroid still needed |
| ~~GPS_VERIFY_NEEDED~~ | ~~VNW-T6-002b Reservoir 2~~ | **RESOLVED 2026-04-19** — 101 ac (ODNR 2014); GPS 40.8409°N, 84.5741°W |
| ~~DETAILS_INCOMPLETE~~ | ~~VNW-T6-005 Memorial Park~~ | **RESOLVED 2026-04-19** — Features documented from city parks page |
| ~~DETAILS_INCOMPLETE~~ | ~~VNW-T6-006 Fountain Park~~ | **RESOLVED 2026-04-19** — Features documented from city parks page |
| DETAILS_INCOMPLETE | VNW-T6-009 Ohio City Fireman's Park | Village website unhelpful; requires direct contact with Village of Ohio City (419-965-2000) |
| ~~PRIVATE_VENUE_REVIEW~~ | ~~VNW-T8-001 Van-Del Drive-In~~ | **RESOLVED 2026-04-19** — Per IMP-073: drive-in theaters in scope; flag removed |
| FIELD_VERIFY_NEEDED | VNW-T7-001 Hiestand Woods trail paths | Get trail name, length, surface; create Trail record when available |

---

## Entities Discovered

| ID | Name | Type | Tier | Governance |
|----|------|------|------|------------|
| VNW-T2-001 | Whitey Case Wildlife Production Area | Site | 2 | ODNR DOW |
| VNW-T2-002 | Van Wert Rest Area — Eastbound (US 30 MM9) | Site | 2 | ODOT |
| VNW-T2-003 | Van Wert Rest Area — Westbound (US 30 MM9) | Site | 2 | ODOT |
| VNW-T2-004 | Convoy Rest Area Storybook Trail | Trail | 2 | ODOT |
| VNW-T3-001 | Convoy Edgewood Park | Site | 3 | Tully-Convoy Park District |
| VNW-T6-001 | Smiley Park (29.4 ac) | Site | 6 | City of Van Wert |
| VNW-T6-001a | Children's Garden & Butterfly House | Site (child) | 6 | City of Van Wert |
| VNW-T6-002 | Van Wert Reservoir Recreation Area | Site | 6 | City of Van Wert |
| VNW-T6-002a | Van Wert Reservoir 1 | Site (child) | 6 | City of Van Wert |
| VNW-T6-002b | Van Wert Reservoir 2 (101 ac) | Site (child) | 6 | City of Van Wert |
| VNW-T6-002c | Van Wert Reservoir Health Trail (3.1 mi) | Trail | 6 | City of Van Wert |
| VNW-T6-002d | Reservoir Boat Launch | Access Point | 6 | City of Van Wert |
| VNW-T6-003 | Franklin Park | Site | 6 | City of Van Wert |
| VNW-T6-004 | Jubilee Park | Site | 6 | City of Van Wert |
| VNW-T6-005 | Memorial Park | Site | 6 | City of Van Wert |
| VNW-T6-006 | Fountain Park | Site | 6 | City of Van Wert |
| VNW-T6-007 | Rotary Athletic Complex | Site | 6 | City of Van Wert |
| VNW-T6-008 | Rotary Dog Park | Site | 6 | City of Van Wert |
| VNW-T6-009 | Ohio City Fireman's Park | Site | 6 | Village of Ohio City |
| VNW-T6-010 | Warrior Trail (2.6 mi rail-trail) | Trail | 6 | Village of Ohio City |
| VNW-T6-011 | Middle Point Ball Park | Site | 6 | Village of Middle Point |
| VNW-T7-001 | Hiestand Woods Park and Preserve (78 ac) | Site | 7 | Van Wert County Foundation |
| VNW-T8-001 | Van-Del Drive-In | Site | 8 | Private |

---

## Held Entities

*(Records blocked on external resolution or verification)*

| ID | Name | Hold Reason |
|----|------|-------------|

---

## Baseline Seed Resolution

All 15 baseline seeds resolved.

| Seed | Disposition | Entity ID |
|------|-------------|-----------|
| Children's Garden and Butterfly House | Confirmed — child Site within Smiley Park | VNW-T6-001a |
| Hiestand Woods | Confirmed — Van Wert County Foundation (Tier 7) | VNW-T7-001 |
| Ohio City Fireman's Park | Confirmed — Village of Ohio City (Tier 6) | VNW-T6-009 |
| Van Wert Convoy Edgewood Park | Confirmed — Tully-Convoy Park District (Tier 3) | VNW-T3-001 |
| Van Wert Fountain Park | Confirmed — City of Van Wert (Tier 6) | VNW-T6-006 |
| Van Wert Franklin Park | Confirmed — City of Van Wert (Tier 6; VWCF co-funded) | VNW-T6-003 |
| Van Wert Jubilee Park | Confirmed — City of Van Wert (Tier 6) | VNW-T6-004 |
| Van Wert Memorial Park | Confirmed — City of Van Wert (Tier 6) | VNW-T6-005 |
| Van Wert Reservoir 1 | Confirmed — City of Van Wert, child Site of Reservoir Rec Area | VNW-T6-002a |
| Van Wert Reservoir 2 | Confirmed — City of Van Wert, child Site of Reservoir Rec Area | VNW-T6-002b |
| Van Wert Reservoir Recreation Area | Confirmed — City of Van Wert (Tier 6) | VNW-T6-002 |
| Van Wert Rotary Athletic Complex | Confirmed — City of Van Wert (Tier 6) | VNW-T6-007 |
| Van Wert Smiley Park | Confirmed — City of Van Wert, 29.4 acres (Tier 6) | VNW-T6-001 |
| Van-Del Drive-In | Confirmed private venue — staged T8 (in scope per IMP-073; no exclusion flag) | VNW-T8-001 |
| Whitey Case Wildlife Production Area | Confirmed — ODNR DOW, 9.29 acres (Tier 2) | VNW-T2-001 |

---

## Open Questions

1. ~~**Van Wert Convoy Edgewood Park**~~ **RESOLVED**: Tully-Convoy Park District (Tier 3), PO Box 302 shared with park district. Not a Van Wert city park.
2. ~~**Reservoirs 1 & 2**~~ **RESOLVED**: City-owned water supply reservoirs; child Sites within Reservoir Recreation Area (Tier 6 City of Van Wert). ODNR manages fish stocking only.
3. ~~**Delphos parks**~~ **RESOLVED 2026-04-19**: All 5 Delphos city parks (Stadium, Waterworks, Leisure, Garfield, Suever) are in Allen County (Marion Township). The Miami-Erie Canal (now Canal Street) is the county boundary in Delphos; east of canal = Allen County. Stadium Park confirmed Allen County by ohiostadiums.com. visitvanwert.com lists no Delphos parks, consistent with no Van Wert County parks. Van Wert County (Washington Township) portion of Delphos is residential only — Tier 6 null.
4. ~~**Van Wert County Foundation**~~ **RESOLVED**: VWCF holds Hiestand Woods (78 ac, nature preserve). Franklin Park co-funded by VWCF but operated by City of Van Wert. No additional VWCF holdings found.

**All open questions resolved.** No blocking items remain for pipeline.

---

## Next Steps — Post-Discovery (Pipeline Ready)

Discovery phase is complete. All 8 tiers processed. **23 raw records staged** (T2-T8, including VNW-T2-004 storybook trail added 2026-04-19). All 15 baseline seeds resolved. All open questions resolved.

**Pre-pipeline flags resolved (2026-04-19):**
1. ~~**Delphos GIS**~~ — RESOLVED: All 5 parks in Allen County; Van Wert = null
2. ~~**US 30 EB Storybook Trail**~~ — RESOLVED: Trail confirmed, VNW-T2-004 staged
3. ~~**Memorial Park / Fountain Park details**~~ — RESOLVED: Features documented from city parks pages
4. ~~**Van-Del Drive-In exclusion**~~ — RESOLVED: In scope per IMP-073; flag removed

**Remaining non-blocking flags (do not block pipeline):**

| Flag | Entity | Notes |
|------|--------|-------|
| GPS_VERIFY_NEEDED | VNW-T2-001 Whitey Case WPA | Toposports GPS only (2 decimal places); needs ODNR GIS |
| STORYBOOK_TRAIL_CONFIRM_NEEDED | VNW-T2-003 US 30 WB Rest Area | Likely has trail per Wyandot precedent; unconfirmed; create VNW-T2-005 if confirmed |
| LENGTH_VERIFY_NEEDED | VNW-T2-004 Storybook Trail | Trail length unknown; ODOT contact or field measure |
| GPS_VERIFY_NEEDED | VNW-T6-002a Reservoir 1 | Acreage confirmed (61 ac); GPS centroid still needed |
| DETAILS_INCOMPLETE | VNW-T6-009 Ohio City Fireman's Park | Village web presence minimal; call 419-965-2000 |
| FIELD_VERIFY_NEEDED | VNW-T7-001 Hiestand Woods trail paths | Trail documentation requires field visit or VWCF contact |

~~**Pipeline steps:**~~
~~na-pipeline → Resolution → Normalization → GPS acquisition → TSV output → Integrity check → DB upsert~~

**PIPELINE COMPLETE — 2026-04-19**
Script: `County_Spreadsheets/Van Wert/van_wert_oh_pipeline.py`
All stages passed. 23 normalized, 0 held, 0 rejected.

---

## Pipeline Results — 2026-04-19

| Stage | Result |
|-------|--------|
| Stage 1 — Resolution | 23 unique records; 0 merges; 0 conflicts |
| Stage 2 — Normalization | 19 Sites, 3 Trails, 1 AP; all vocab fields validated |
| Stage 3 — GPS Acquisition | 19/19 sites have GPS (14 HIGH/MED via Nominatim; 5 LOW fallback) |
| Stage 4.5 — Vocab Gate | PASSED — 0 violations |
| Stage 4 — TSV Output | 6 files written to County_Spreadsheets/Van Wert/ |
| Stage 5 — Integrity Check | PASSED — 0 warnings |
| Stage 6 — DB Upsert | 19 Sites + 3 Trails + 1 AP committed to natural_areas_v5.db |

**Entity IDs assigned:**

| Entity ID | Name | DB Table |
|-----------|------|----------|
| VNW-S-001 | Whitey Case Wildlife Production Area | sites |
| VNW-S-002 | Van Wert Rest Area — Eastbound (US 30 MM9) | sites |
| VNW-S-003 | Van Wert Rest Area — Westbound (US 30 MM9) | sites |
| VNW-S-004 | Convoy Edgewood Park | sites |
| VNW-S-005 | Smiley Park | sites |
| VNW-S-006 | Children's Garden and Butterfly House | sites |
| VNW-S-007 | Van Wert Reservoir Recreation Area | sites |
| VNW-S-008 | Van Wert Reservoir 1 | sites |
| VNW-S-009 | Van Wert Reservoir 2 | sites |
| VNW-S-010 | Franklin Park | sites |
| VNW-S-011 | Jubilee Park | sites |
| VNW-S-012 | Memorial Park | sites |
| VNW-S-013 | Fountain Park | sites |
| VNW-S-014 | Rotary Athletic Complex | sites |
| VNW-S-015 | Rotary Dog Park | sites |
| VNW-S-016 | Ohio City Fireman's Park | sites |
| VNW-S-017 | Middle Point Ball Park | sites |
| VNW-S-018 | Hiestand Woods Park and Preserve | sites |
| VNW-S-019 | Van-Del Drive-In | sites |
| VNW-T-001 | Convoy Rest Area Storybook Trail | trails |
| VNW-T-002 | Van Wert Reservoir Health Trail | trails |
| VNW-T-003 | Warrior Trail | trails |
| VNW-AP-001 | Van Wert Reservoir Boat Launch | access_points |

**GPS confidence summary:**
- HIGH (Nominatim address match): VNW-S-004 through S-015, S-017, S-018 (14 entities)
- MED (street-level fallback): VNW-S-007, VNW-S-009 (confirmed by Ohio gazetteer)
- LOW (highway fallback / village centroid / approximate): VNW-S-001, S-002, S-003, S-016, S-019; propagated to VNW-T-001, T-002, AP-001
- GPS_VERIFY_NEEDED (post-pipeline): VNW-S-001 (Whitey Case — toposports only), VNW-S-008 (Reservoir 1 centroid)

**Remaining open flags (non-blocking, post-pipeline):**

| Flag | Entity ID | Notes |
|------|-----------|-------|
| GPS_VERIFY_NEEDED | VNW-S-001 | ODNR GIS authoritative coords needed (toposports 2-decimal approx) |
| GPS_VERIFY_NEEDED | VNW-S-008 | Reservoir 1 GPS centroid (current = Nominatim approx) |
| STORYBOOK_TRAIL_CONFIRM_NEEDED | VNW-S-003 | WB rest area storybook trail unconfirmed; create VNW-T-004 if confirmed |
| LENGTH_VERIFY_NEEDED | VNW-T-001 | Storybook trail length not documented; ODOT contact or field measure |
| DETAILS_INCOMPLETE | VNW-S-016 | Ohio City Fireman's Park features unknown; call 419-965-2000 |
| FIELD_VERIFY_NEEDED | VNW-S-018 | Hiestand Woods trail paths need name/length/surface; create Trail when available |

**Status: COUNTY COMPLETE.**

---

## Pre-Discovery Checklist

*(Populated before each tier begins)*

---

## Captured Source Data

*(Verbatim tables from authoritative sources, recorded at fetch time)*

---

### Source: visitvanwert.com/things-to-do/outdoor-adventure/
**Fetched**: 2026-04-14 | **Tier relevance**: Tier 6 Municipal, Tier 7 Conservancy

| Name | Location | Contact |
|------|----------|---------|
| Children's Garden & Butterfly House | 1409 Leeson Ave, Van Wert | 419-238-9121 |
| Van Wert Smiley Park | 1425 Leeson Ave, Van Wert | 419-238-9121 |
| Van Wert Jubilee Park | 137 Gleason Ave, Van Wert | 419-238-9121 |
| Van Wert Franklin Park | 305 Frothingham St, Van Wert | 419-238-9121 |
| Van Wert Memorial Park | 611 W. Main St, Van Wert | 419-238-9121 |
| Van Wert Fountain Park | 210 W. Main St, Van Wert | 419-238-9121 |
| Van Wert Hiestand Woods | 1510 Hospital Dr, Van Wert | Contact via website |
| Van Wert Dog Park | 1264 S. Washington St, Van Wert | 419-238-9121 |
| Van Wert Reservoir Recreation Area | Multiple locations | 419-238-9121 |
| Van Wert Rotary Athletic Park | 9085 John Brown Rd, Van Wert | 419-238-9121 |
| Convoy Edgewood Park | 643 N. Main St, Convoy | 419-749-4060 |
| Middle Point Ball Park | 406 N. Adams St, Middle Point | 419-968-2427 |
| Ohio City Fireman's Park | St. Rt. 118, Ohio City | 419-965-2000 |

**Notes**:
- Hiestand Woods uses separate "Contact via website" not the city parks number → confirms VWCF governance (Tier 7)
- Convoy Edgewood Park phone 419-749-4060 = Convoy city number → confirms municipal (Tier 6 Convoy), NOT Van Wert city park
- Van Wert Dog Park and Middle Point Ball Park are new — not in baseline
- Van Wert Rotary Athletic Park = baseline "Van Wert Rotary Athletic Complex"

---

### Source: vanwertcountyfoundation.org/impact/parks/hiestand-woods-park/
**Fetched**: 2026-04-14 | **Tier relevance**: Tier 7 Conservancy

- **Owner/Manager**: Van Wert County Foundation (purchased 1945, Clara Anderson estate funds)
- **Address**: 1510 Hospital Dr, Van Wert, OH
- **Acreage**: 78 acres
- **Description (verbatim)**: "Hiestand Woods Park, established in 1945, boasts a park area & nature preserve. Over the years construction of shelter houses, a playground, and paths in the nature preserve have created a truly special place."
- **Features**: Shelter houses, playground, nature preserve paths; planned improvements include restrooms, expanded parking, water fountains, fitness stations, elevated boardwalk, "Ninja Warrior Challenge Course" stations

---

### Source: toposports.com — Whitey Case Wildlife Production Area detail
**Fetched**: 2026-04-14 | **Tier relevance**: Tier 2 State (ODNR DOW)

- **Acreage**: 9.29 acres
- **GPS (approximate)**: 40.80°N, 84.79°W
- Source note: Toposports hunting layer; treat GPS as approximate until confirmed by authoritative source
