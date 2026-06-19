# Sandusky County, Ohio — Handoff Document
**RUN_ID:** `sandusky_ohio_2026_05_21`
**PREFIX:** `SAN`
**County seat:** Fremont
**Session started:** 2026-05-20
**Last updated:** 2026-06-10 — BATCH RESOLUTION COMPLETE
**Pipeline status:** COMPLETE — all stages committed to DB

---

## Tiers Completed

| Tier | Status | Entities | Notes |
|------|--------|----------|-------|
| T1 — Federal & Tribal | COMPLETE — NULL | 0 | All 7 federal agencies + tribal checked; USACE has flood control infrastructure at Fremont (non-recreational, not a site); VA "Sandusky" addresses are in Erie/Ottawa counties |
| T2 — State | COMPLETE | 11 records: 8 Sites + 3 APs | Spiegel Grove, Pickerel Creek WA, Resthaven WA (Erie/SAN), Willow Point WA (Erie/SAN), Sandusky Scenic River (WYA/SEN/SAN), Ron Abraham Forest (OSU), Aldrich Pond WA, SAN WA 1-7 (placeholder); 8 null blocks |
| T3 — District | COMPLETE | 26 records: 20 Sites + 3 Trails + 3 APs | SCPD: 16 park sites + 4 White Star child sites; NCIT (KNOWN_MC:OH-MC-T-0110); White Star Quarry Loop Trail; Waggoner's Run MTB Trail (T3 miss caught at T4); 3 APs; SWCD null; 7 null blocks |
| T4 — County | COMPLETE — NULL | 0 direct entities; 2 cross-tier misses caught (Waggoner's Run → T3; Darr-Root AP → T2) | No county parks dept; SCPD handles parks (T3); county fairgrounds = private agri society; all golf private; NRHP null (Mull at T3); 8 null blocks |
| T5 — Township | COMPLETE | 34 records: 4 Parks + 30 Cemeteries | 12 townships confirmed active (OTA); Ballville (3 parks, 1 cem); Sandusky Twp (1 park, 3 cems); cemeteries across all townships; Green Creek cem unconfirmed → NEEDS_VERIFICATION; 6 null blocks |
| T6 — Municipal | COMPLETE | 39 records: 36 Sites + 2 APs + 1 Trail | Fremont (9 parks + 2 APs); Clyde (5 parks + reservoir + cemetery); Gibsonburg (4 parks + 1 trail); Woodville village (4 parks + cemetery); Bellevue (7 parks, GIS_VERIFY_COUNTY); Elmore (3 parks, GIS_VERIFY_COUNTY); Lindsey (1 park); Burgoon/Helena nulls; Green Springs null pending human contact; 7 null blocks |
| T7 — Conservancy & Land Trust | COMPLETE — NULL | 0 new entities | BSC properties (Redhorse Bend, Christy Farm, Decoy Marsh) already at T3/SCPD; agricultural easements excluded §4.2; Western Wildlife Corridor = Cincinnati-area org, not Sandusky County; ONAPA: 0 state preserves in county; 7 null blocks |
| T8 — Private | COMPLETE | 44 records: 44 Sites | 7 golf courses (Sycamore Hills 27-hole, Fremont CC members-only, Green Hills Clyde, Hidden Hills Woodville, River Cliff uncertain governance, Sugar Creek Elmore GIS_VERIFY, Sleepy Hollow CLOSED); WR Hunt Club (hunting preserve); Schedel Arboretum (GIS_VERIFY Ottawa/Sandusky); GNIS cemeteries: 10 church + 1 commercial + 21 family + 3 governance-uncertain; 6 null blocks |

---

## Tiers Remaining

| Tier | Governance | Sub-procedure | Status |
|------|-----------|---------------|--------|
| T1 | Federal & Tribal | na_fed_tribal_discovery_subproc_v5.3.md | COMPLETE — NULL |
| T2 | State | na_state_discovery_subproc_v5.5.md | COMPLETE |
| T3 | District (Metroparks, conservancy) | na_district_discovery_subproc_v5.7.md | COMPLETE |
| T4 | County | na_county_discovery_subproc_v5.3.md | COMPLETE — NULL |
| T5 | Township | na_township_discovery_subproc_v5.4.md | COMPLETE |
| T6 | Municipal | na_municipal_discovery_subproc_v5.9.md | COMPLETE |
| T7 | Conservancy & Land Trust | na_conservancy_discovery_subproc_v5.3.md | COMPLETE — NULL |
| T8 | Private | na_private_discovery_subproc_v5.3.md | COMPLETE |

---

## Key Active Flags

- **GIS_VERIFY_COUNTY — Bellevue (7 parks)**: Bellevue straddles Erie, Huron, Sandusky, and Seneca counties. All 7 staged parks require GIS parcel lookup to confirm which county each falls in.
- **GIS_VERIFY_COUNTY — Elmore (3 parks)**: Elmore straddles Ottawa and Sandusky counties. All 3 parks need GIS verification; county_primary set to Ottawa pending verification.
- **Green Springs village parks — human contact required**: Village parks page (gsohio.org) returned HTTP 403. Whirlpool Park closed/contaminated. At least one shelter/park implied by reservation page. Call Fiscal Officer 419-639-2123 to confirm park inventory before finalizing null.
- **Helena village park — human contact required**: Village has a Park & Recreation page (villageofhelena.org/park-recreation/) but no park names or features listed. Call Village of Helena at 567-482-1545 to confirm whether a park facility exists.
- **Woodville Cemetery governance (village)**: Staged on Cemetery Drive as Village of Woodville-managed (NEEDS_VERIFICATION). Distinct from Woodville Township Cemetery (CR 30). Confirm ownership with village office: 419-849-2731.
- ~~Muddy Creek Preserve (Western Wildlife Corridor) vs. Muddy Creek Reserve (SCPD)~~ — RESOLVED at T7: Western Wildlife Corridor Inc. is a Cincinnati-area organization with no Sandusky County presence. Muddy Creek Reserve (SCPD, Rice Township) is the only entity. No T7 record warranted.
- Ringneck Ridge (SCPD) and Ringneck Ridge Wildlife Area (ODNR) baseline entries — verify whether these are the same physical area under dual management or two distinct entities.
- Sandusky County Wildlife Areas 1–7: verify current ODNR inventory; confirm whether these numbered areas still exist under these names.
- Green Creek Township cemetery: name and location unconfirmed; contact Green Creek Township at 3106 Limerick Rd, Clyde OH (T5 open flag).
- Jackson Township / Smith Cemetery: no street address found; requires field verification (T5 open flag).

---

## Batch Resolution Update — 2026-06-10

See `sandusky_oh_batch_resolution_2026_06_10.md` for full log.

**DB changes applied:**
- Trail parents: T-0004 → S-0093 (Silver Rock Park); T-0110 → S-0021 (Tea Kaufman Homestead)
- Acreage: S-0002 = 3,148ac; S-0009 = 158ac; S-0029 = 18ac (all PAD-US)
- S-0105 Sugar Creek GC released from held; confirmed Harris Twp, Sandusky County; inserted as active
- 11 T2 supplemental sites inserted (S-0143–S-0153): Knobbys Prairie WA, Green Springs SF, Abbotts Bridge SR, WPAs 50/14/59/62/47/30/63/31
- 9 T6 supplemental sites inserted (S-0154–S-0162): Fremont/Clyde/Ballville parks
- Total SAN sites: 155 (was 134 active + 7 held → now 155 active + 6 held)

**Open items remaining:**
- Spiegel Grove SP acreage — MRQ
- White Star Park acreage discrepancy (797 vs 666ac) — MRQ
- Mosser Park site not in DB (AP-0005 NCIT access has no site parent)
- WPA catch-all S-0008 — deprecated in practice; formal deletion deferred
- S-0079/0080/0081, S-0107 sequence gaps — document in session log; likely Bellevue reclassification
- Portage Trail Park (S-0159) NCIT trail_parent — needs route map verification
- Veteran's Memorial Park (S-0160) — verify distinct from S-0096 Veterans Park (Clyde)
- 6 entities remain in held_entities (all valid cross-county holds):
  - S-0003/0004 Resthaven WA, Willow Point WA → Erie County primary
  - S-0005 Sandusky State Scenic River → Wyandot County primary
  - AP-0002/0003 Resthaven APs → Erie County primary
  - AP-0007 Darr-Root Fishing Access → parent_held (S-0005)

---

## Known Multi-County Entities (from DB bootstrap)

| Entity ID | Name | Counties |
|-----------|------|---------|
| OH-MC-T-0110 | North Coast Inland Trail | Erie;Huron;Ottawa;Sandusky |

When this entity is encountered during discovery, use `KNOWN_MC:OH-MC-T-0110` in `identity_notes_raw`.

---

## County Context

- **County seat:** Fremont (also major city)
- **Major municipalities:** Fremont (city), Clyde (city), Bellevue (partially — straddles Huron/Sandusky counties), Gibsonburg (village), Lindsey (village), Vickery (village), Green Springs (village), Woodville (village)
- **12 townships (from authoritative roster):** Ballville, Green Creek, Jackson, Madison, Rice, Riley, Sandusky, Scott, Townsend, Washington, Woodville, York
- **Key district:** Sandusky County Park District (SCPD)
- **State agencies with presence:** ODNR Division of Wildlife (multiple wildlife areas), ODNR Division of Parks (Spiegel Grove State Park)
- **MORPC coverage:** Sandusky County is NOT in the 15-county MORPC CSV — do not cross-reference.
- **OSU presence:** Ron Abraham Forest (~130 acres) — baseline seed for T2 (public university = Tier 2)

---

## Baseline Seeds (from Sandusky.xlsx — verify through tier discovery)

| Name | Baseline Type | Notes |
|------|--------------|-------|
| Aldrich Pond Wildlife Area | State Wildlife Area; Public Hunting Area | 39.93 ac; no ODNR web info yet |
| Biggs-Kettner Park | Fremont Park | 601 St. Joseph St, Fremont |
| Blue Heron Reserve | SCPD | 160 ac; 2134 CR 260, Vickery |
| Christy Farm Nature Preserve | SCPD | 151 ac; 2020 Old Oak Harbor Rd, Fremont |
| Creek Bend Farm | SCPD | 310 ac; nature center; 720 S Main St, Lindsey |
| Decoy Marsh | SCPD | 67 ac; previously private hunting club; 2700 CR 259, Fremont |
| Don W. Miller Memorial Park | SCPD | 80 ac; formerly River Cliff Park; 1329 Tiffin St, Fremont |
| Franklin & Phillip Rose Wildlife Preserve | SCPD | programming use only; 3861 CR 184, Fremont |
| Fremont Boat Ramp | — | provides access to Upper Sandusky Reservoir #1? |
| Green Creek Township Property | SCPD | 90 ac; off CR 195 south of Clyde |
| Millers Spring | GNIS Spring | |
| Mosser Park | Fremont Park | 1630 Walter Ave, Fremont |
| Mud Creek Prairie | GNIS Prairie | |
| Muddy Creek Preserve | Western Wildlife Corridor | 80 ac — verify vs. Muddy Creek Reserve |
| Muddy Creek Reserve | SCPD | 80 ac; Rice Township, off CR 157 |
| Mull Covered Bridge | SCPD | pedestrian use; 1515 CR 9, Fremont |
| North Coast Inland Trail segment | SCPD segment | 28-mile multi-use; Elmore–Bellevue; part of Buckeye Trail → KNOWN_MC:OH-MC-T-0110 |
| Ottawa Prairie | GNIS Prairie | |
| Pickerel Creek Wildlife Area | State Wildlife Area; Hunting | 3200 ac |
| Raccoon Creek Reservoir | — | 36-acre reservoir |
| Redhorse Bend | SCPD | 78 ac; 1616 N River Rd, Fremont |
| Ringneck Ridge | SCPD | 360 ac; archery range; 1818 CR 74, Gibsonburg |
| Ringneck Ridge Wildlife Area | State Wildlife Area | no ODNR web info yet |
| Rodger Young Park | Fremont Park | |
| Ron Abraham Forest | OSU property | 130.8 ac — T2 candidate |
| Saint Francis Springs | GNIS Spring | |
| Sandusky County Wildlife Areas 1–7 | Public Hunting Area (ODNR) | verify current inventory |
| Shelley Wetland | SCPD | 17 ac; usually closed; CR 292 & TR 177, Bellevue |
| Spiegel Grove State Park | State Park | 25 ac |
| Tea Kaufman Homestead | SCPD | 14 ac; near NCIT; 2091 CR 292, Bellevue |
| The Woods at the Luscombe Farm | SCPD | 55 ac; 2341 CR 213, Clyde |
| Walsh Park | Fremont Park | |
| Wendelle Miller Park | Lindsey Park | |
| White Star Park | SCPD | 797 ac; campground, wetlands, log cabins, quarry swim; 925 S Main St, Gibsonburg |
| Wolf Creek Park | SCPD; State Scenic River | canoe/kayak launch; ODNR-owned, SCPD-managed |

---

## Entities Discovered

*(none yet — to be populated as discovery proceeds)*

---

## Pipeline Results (2026-05-22)

| Entity | Active → DB | Held → held_entities |
|---|---|---|
| Sites | 94 | 48 (8 cross_county_held, 40 gps_missing) |
| Trails | 2 | 2 (gps_missing) |
| Access Points | 4 | 5 (2 cross_county_held, 2 gps_missing, 1 parent_held) |
| **Total** | **100** | **55** |

**DB note:** NCIT upserted as OH-MC-T-0110 (SAN-T-001 provisional ID retired).
**SAN-S-001 designation fix:** Multi-value `NRHP;State Memorial;State Park` → `National Historic Landmark` (NHL 1964, confirmed from identity_notes_raw).

---

## Held Entities Summary

- **Cross-county held (10):** SAN-S-003, SAN-S-004 (Erie primary); SAN-S-005, SAN-AP-007 (Wyandot primary); SAN-AP-002, SAN-AP-003 (Erie primary); + others
- **GPS missing — sites (40):** Primarily rural SCPD conservation/program-only sites, village parks where Nominatim returned null after 3 passes, and small rural cemeteries
- **GPS missing — trails (2):** SAN-T-003 (Waggoner's Run MTB Trail), SAN-T-004 (Silver Rock Trail)
- **GPS missing — APs (2):** SAN-AP-001, SAN-AP-005
- **Parent held — APs (1):** SAN-AP-007 (Darr-Root Fishing Access; parent SAN-S-005 is cross_county_held/Wyandot)

---

## Open Questions

1. Is Muddy Creek Preserve (Western Wildlife Corridor) the same parcel as Muddy Creek Reserve (SCPD), or two distinct 80-acre parcels with similar names?
2. Are Ringneck Ridge (SCPD) and Ringneck Ridge Wildlife Area (ODNR) the same physical area under dual management, or two distinct entities?
3. What are the current ODNR names/status for Sandusky County Wildlife Areas 1–7?
4. Does Bellevue's portion in Sandusky County contain any distinct municipal parks separate from Huron County parks?
5. Is Fremont Boat Ramp the same as or associated with a reservoir/wildlife area access point?

---

## Next Steps

**Discovery and pipeline are complete.** Remaining work is post-pipeline follow-up:

1. **GIS_VERIFY_COUNTY — Bellevue (7 parks):** Run GPS coordinates through GIS parcel lookup to confirm Sandusky County vs. Erie/Huron/Seneca. Update county_primary; may require reclassification of held sites.
2. **GIS_VERIFY_COUNTY — Elmore (3 parks):** Confirm Ottawa vs. Sandusky county boundary. Currently staged with county_primary=Ottawa.
3. **GIS_VERIFY_COUNTY — Schedel Arboretum:** Ottawa vs. Sandusky county determination needed.
4. **Human contact — Green Springs village:** Call Fiscal Officer 419-639-2123 to confirm park inventory.
5. **Human contact — Helena village:** Call 567-482-1545 to confirm whether a park facility exists.
6. **Woodville Cemetery governance:** Confirm Village of Woodville ownership (call 419-849-2731).
7. **GPS re-run (future):** 40 sites + 2 trails + 2 APs held for gps_missing. Re-attempt when improved address data is available or via field GPS acquisition.
8. **Cross-county partner runs:** When Erie and Wyandot counties are processed, cross_county_held entities will be released.

---

## Pre-Discovery Checklist

### Tier 3 — District (working 2026-05-21)

**Ohio Auditor Pre-Enumeration — 2026-05-21**
URL: https://www.auditor.state.oh.us/AuditSearch/Entities
County filter: Sandusky
Entity types searched: Park Districts, Joint Recreation Districts, Conservancy Districts, Watershed Districts, SWCDs, Special Districts
Entities found: 2
Entity names: Sandusky County Park District; Sandusky County Soil & Water Conservation District
Web-dark: None — both have web presence
Null results: Joint Recreation Districts, Conservancy Districts, Watershed Districts, Special Districts — none found

**SCPD Properties (all confirmed from lovemyparks.com — complete inventory):**
- [ ] Blue Heron Reserve — 160 ac, 2134 CR 260, Vickery
- [ ] Christy Farm Nature Preserve — 151 ac, 2020 Old Oak Harbor Rd, Fremont
- [ ] Creek Bend Farm — 310 ac, 720 S Main St, Lindsey (Wilson Nature Center)
- [ ] Decoy Marsh — 67 ac, 2700 CR 259, Fremont (program use only)
- [ ] Don W. Miller Memorial Park — 80 ac, 1329 Tiffin St, Fremont (SCPD HQ)
- [ ] Franklin & Phillip Rosa Wildlife Preserve — addr: 3861 CR 184, Fremont (program use only)
- [ ] Green Creek Township & Reserve — 90 ac, off CR 195 south of Clyde (closed to public)
- [ ] Muddy Creek Reserve — 80 ac, Rice Twp, off CR 157 (program use only)
- [ ] Mull Covered Bridge — 1515 CR 9, Fremont (NRHP; co-managed with county)
- [ ] Redhorse Bend — 78 ac, 1616 N River Rd, Fremont (program use only)
- [ ] Ringneck Ridge — 1818 and 2026 TR 74, Gibsonburg (public hunting/archery)
- [ ] Shelley Wetland — 17 ac, CR 292 & TR 177, Bellevue (program use only)
- [ ] Tea Kaufman Homestead — 14 ac, 2091 CR 292, Bellevue (NCIT access point)
- [ ] The Woods at the Luscombe Farm — 55 ac, 2341 CR 213, Clyde (1-mi loop trail)
- [ ] White Star Park — 797 ac, 925 S Main St, Gibsonburg (4 sub-areas)
- [ ] Wolf Creek Park — 2409 & 2701 SR 53, Fremont (canoe launch, trails)
- [ ] North Coast Inland Trail — 28 mi Sandusky County segment (KNOWN_MC:OH-MC-T-0110)

**Sandusky County SWCD:**
- [ ] sanduskycoswcd.org — check for any land holdings/restoration sites

### Tier 2 — State (working 2026-05-20)
Enumerated from baseline and known state sources before individual fetches begin:

**ODNR Division of Parks & Watercraft:**
- [ ] Spiegel Grove State Park (Fremont) — 25 ac baseline seed

**ODNR Division of Forestry:**
- [ ] Any state forest units in Sandusky County — verify

**ODNR Division of Wildlife:**
- [ ] Pickerel Creek Wildlife Area — 3,200 ac baseline
- [ ] Aldrich Pond Wildlife Area — 39.93 ac baseline; no ODNR web info yet
- [ ] Ringneck Ridge Wildlife Area — baseline; no ODNR web info yet
- [ ] Sandusky County Wildlife Areas 1–7 — ODNR managed; verify current names/status
- [ ] ODNR Hunting Area Maps — search Sandusky County entries
- [ ] ODNR Fishing Lake Maps — search Sandusky County entries
- [ ] ODNR River & Stream Fishing Maps — search Sandusky County entries

**ODNR Division of Natural Areas & Preserves (DNAP):**
- [ ] Any State Nature Preserves in Sandusky County — verify

**ODNR Scenic Rivers:**
- [ ] Sandusky River — baseline note "State Scenic River" on Wolf Creek Park entry; verify designation
- [ ] Any other scenic river designations in Sandusky County

**Ohio History Connection (OHC):**
- [ ] Spiegel Grove / Rutherford B. Hayes Presidential Center — state memorial in Fremont

**ODOT:**
- [ ] Rest areas — verify if I-80/90 (Ohio Turnpike) passes through Sandusky County
- [ ] Any scenic overlooks or bikeway corridors

**OTIC (Ohio Turnpike):**
- [ ] Check if Turnpike crosses Sandusky County — if yes, check service plazas

**Public Universities (§4.7):**
- [ ] Ron Abraham Forest — OSU property, 130.8 ac; Tier 2 candidate

---

### Tier 5 — Township (working 2026-05-21)

**OTA Active Township Roster — 2026-05-21 — 12 townships confirmed, 0 defunct**

| Township | Pop 2020 | OTA Website | Status |
|----------|----------|------------|--------|
| Ballville | 6,042 | https://www.ballville.org/ | COMPLETE — 3 parks + Oakwood Cem |
| Green Creek | 3,389 | http://www.greencreek.org | COMPLETE — no parks; 1 cem NEEDS_VERIFICATION |
| Jackson | 1,610 | http://www.jackson-sandusky.com | COMPLETE — Smith Cemetery (township-managed) |
| Madison | 3,587 | (none in OTA) | COMPLETE — West Union Cemetery (NEEDS_VERIFICATION) |
| Rice | 1,143 | http://www.ricetownship.com | COMPLETE — 5 cemeteries (Faith Lutheran NEEDS_VERIFICATION) |
| Riley | 1,214 | https://www.rileytownship.org/ | COMPLETE — 4 cemeteries |
| Sandusky | 3,551 | http://www.sanduskytownship.com | COMPLETE — 1 park (early dev) + 3 cemeteries |
| Scott | 1,333 | (none in OTA) | COMPLETE — Chestnut Grove Cemetery (NEEDS_VERIFICATION ownership) |
| Townsend | 1,523 | (none in OTA) | COMPLETE — 2 cemeteries |
| Washington | 2,315 | (none in OTA) | COMPLETE — 3 cemeteries |
| Woodville | 3,303 | http://woodvilletownship.org | COMPLETE — 3 cemeteries |
| York | 2,479 | http://www.yorktwp.com | COMPLETE — 5 cemeteries (2 inactive) |

*Note: Jackson, Madison, Washington, Riley — common names requiring §4.2a wrong-county verification*

### Tier 6 — Municipal (working 2026-05-21)

**Municipality List — 10 incorporated municipalities (3 cities, 7 villages)**

| Municipality | Type | Cross-County? | Website | Status |
|-------------|------|--------------|---------|--------|
| Fremont | City (county seat) | No | fremontohio.org | PENDING |
| Clyde | City | No | clydeohio.org | PENDING |
| Bellevue | City | Yes (Huron/Sandusky) | cityofbellevue.net | PENDING |
| Woodville | Village | No | woodvilleohio.com? | PENDING |
| Gibsonburg | Village | No | gibsonburg.com? | PENDING |
| Green Springs | Village | Yes (Sandusky/Seneca) | ? | PENDING |
| Elmore | Village | Yes (Ottawa/Sandusky) | ? | PENDING |
| Lindsey | Village | No | ? | PENDING |
| Burgoon | Village | No | ? | PENDING |
| Helena | Village | No | ? | PENDING |

*Known leads from earlier tiers: Fremont (Biggs-Kettner Park, Walsh Park, Rodger Young Park, Sand Docks, Darr-Root already staged); Clyde (Raccoon Creek Reservoir, clydeohio.org/165/Parks); Lindsey (Wendelle Miller Park baseline seed)*

### Tier 7 — Conservancy & Land Trust (working 2026-05-21)

**Organizations enumerated from LTA, BSC, NCOLC, WRLC, ONAPA listing pages:**

| Organization | Website | Sandusky County Holdings | Status |
|---|---|---|---|
| Black Swamp Conservancy (BSC) | blackswamp.org | Redhorse Bend (78 ac, transferred to SCPD); Christy Farm NP (147 ac, transferred to SCPD); Decoy Marsh (67 ac, SCPD); Washusky Farms easement (604 ac, private); Frankart Farm easement (510 ac, cross-county, private) | COMPLETE — all public holdings already at T3; private easements excluded §4.2 |
| North Central Ohio Land Conservancy (NCOLC) | ncolc.org | Blue Heron Reserve easement (160 ac) — SCPD owns/manages | COMPLETE — T3 already staged; NCOLC as easement holder noted |
| Western Reserve Land Conservancy (WRLC) | wrlandconservancy.org | Edwards Farm easement (656 ac, private, near Clyde, 2018) | COMPLETE — agricultural easement, no public access, excluded §4.2 |
| Western Wildlife Corridor, Inc. | westernwildlifecorridor.org | NOT ACTIVE in Sandusky County — operates in Hamilton County / Ohio River Valley area | COMPLETE — null; resolves open flag |
| ONAPA | onapa.org | No ODNR state nature preserves in Sandusky County confirmed | COMPLETE — null |
| The Nature Conservancy (TNC) | nature.org/ohio | No confirmed land holdings in Sandusky County | COMPLETE — null |
| Trust for Public Land (TPL) | tpl.org/ohio | Properties are in Erie County, not Sandusky County | COMPLETE — null |
| Coalition of Ohio Land Trusts | ohiolandtrusts.org | No Sandusky County member trusts identified | COMPLETE — null |

---

## Captured Source Data

### T8 — Sandusky County Cemetery Enumeration (IMP-030 — fetched 2026-05-21)
**Source:** OhioGenealogyExpress — https://ohiogenealogyexpress.com/sandusky/sanduskyco_cems.htm (60 entries)
**PeopleLegacy:** HTTP 403 — fallback to USGS GNIS file recommended for cross-check.

| # | Cemetery Name | T2–T7 Already Staged? | T8 Disposition |
|---|---|---|---|
| 1 | Bakertown Cemetery | No | T8 Family Cemetery |
| 2 | Beeler Cemetery | Yes — Riley Twp (T5) | skip |
| 3 | Binkley Cemetery | Yes — Sandusky Twp (T5) | skip |
| 4 | Bowlus Cemetery (x2) | No | T8 Family Cemetery |
| 5 | Brier Hill Cemetery | Yes — Rice Twp (T5) | skip |
| 6 | Collins Cemetery | No | T8 Family Cemetery |
| 7 | Colwell Cemetery | No | T8 Family Cemetery |
| 8 | County Home Cemetery | No | T4 miss — county government burial ground |
| 9 | Dana Cemetery | No | T8 Family Cemetery |
| 10 | Decker Cemetery | No | T8 Family Cemetery |
| 11 | Ellsworth Cemetery | Yes — York Twp (T5) | skip |
| 12 | Fourmile House Cemetery | Yes — Sandusky Twp (T5) | skip |
| 13 | Foust Cemetery | Yes — Faust/Riley Twp (T5 spelling variant) | skip |
| 14 | Fuller Cemetery | No | T8 Family Cemetery |
| 15 | Gibbs Cemetery | Yes — Green Creek Burial Ground/Riley Twp (T5) | skip |
| 16 | Gilbert Cemetery | Yes — York Twp (T5) | skip |
| 17 | Green Springs Cemetery | No | Possible T6 miss — Village of Green Springs |
| 18 | Greenlawn Memory Gardens | No | T8 Private Cemetery (commercial) |
| 19 | Greenwood Cemetery | Yes — Rice Twp (T5) | skip |
| 20 | Halters Cemetery | No | T8 Family Cemetery |
| 21 | Hayes Cemetery | No | T8 Family Cemetery |
| 22 | Hessville Cemetery | Yes — Washington Twp (T5) | skip |
| 23 | Hill Cemetery | No | T8 Family Cemetery |
| 24 | Hineline Cemetery | Yes — Rice Twp (T5) | skip |
| 25 | Hite Cemetery (x2) | No | T8 Family Cemetery (may be 2 distinct sites) |
| 26 | Lathrop Cemetery | No | T8 Family Cemetery |
| 27 | Lindsey Cemetery | Yes — Washington Twp (T5) | skip |
| 28 | Ludwig Cemetery | No | T8 Family Cemetery |
| 29 | McCreary Farm Cemetery | No | T8 Family Cemetery |
| 30 | McGormley Cemetery | No | T8 Family Cemetery |
| 31 | McPherson Cemetery | Yes — City of Clyde (T6) | skip |
| 32 | Metzgar Cemetery | No | T8 Family Cemetery |
| 33 | Mount Lebanon Cemetery | No | T8 Church Cemetery |
| 34 | North Union Cemetery | No | T8 Church or Community Cemetery |
| 35 | Oakwood Cemetery | Yes — Ballville Twp (T5) | skip |
| 36 | Old Fremont Cemetery | No | T8 — governance unknown; GNIS-only |
| 37 | Overmyer Cemetery | No | T8 Family Cemetery |
| 38 | Pember Farm Cemetery | No | T8 Family Cemetery |
| 39 | Quinshan Cemetery | No | T8 Family Cemetery |
| 40 | Reformed Church Cemetery | No | T8 Church Cemetery (Bellevue area — GIS_VERIFY_COUNTY) |
| 41 | Saint Anns Cemetery | No | T8 Church Cemetery |
| 42 | Saint Josephs Cemetery | No | T8 Church Cemetery |
| 43 | Saint Lawrence Cemetery | No | T8 Church Cemetery |
| 44 | Saint Marys Cemetery (x3) | No | T8 Church Cemetery (multiple parishes) |
| 45 | Saint Pauls Cemetery | No | T8 Church Cemetery |
| 46 | Saint Philomena Cemetery | No | T8 Church Cemetery |
| 47 | Schoch Cemetery | Yes — Riley Twp (T5) | skip |
| 48 | Shawl Cemetery | No | T8 Family Cemetery |
| 49 | Smith Cemetery | Yes — Jackson Twp (T5) | skip |
| 50 | Tew Cemetery | Yes — Townsend Twp (T5) | skip |
| 51 | Trinity Cemetery (x2) | No | T8 Church Cemetery |
| 52 | Wales Corner Cemetery | Yes — York Twp (T5) spelling variant | skip |
| 53 | Washington Chapel Cemetery | Yes — Washington Twp (T5) | skip |
| 54 | West Union Cemetery | Yes — Madison Twp (T5) | skip |
| 55 | Westwood Cemetery | Yes — Woodville Twp (T5) | skip |
| 56 | Whittlesey Cemetery | No | T8 Family Cemetery |
| 57 | Wickwire Cemetery | Yes — Wickwyre/York Twp (T5) spelling variant | skip |
| 58 | Woodville Cemetery | Yes — CR30/Woodville Twp (T5) | skip |
| 59 | York Free Chapel | No | Likely same as York Chapel Cemetery (T5) — evaluate |
| 60 | York Free Chapel Cemetery | Yes — York Chapel/York Twp (T5) | skip |

**Not on OhioGenealogyExpress (staged at T5, cross-check USGS GNIS):** Slates Cemetery, Parkhurst Cemetery, Sugar Creek Cemetery, LaPrairie Cemetery, Faith Lutheran Cemetery, Green Creek Township Cemetery (unconfirmed)

### T8 — Golf Course Enumeration (IMP-030 — fetched 2026-05-21)
**Sources:** PGA.com course finder; Sandusky County EDC; direct searches

| Course | Address | Holes | Access | Notes |
|---|---|---|---|---|
| Sycamore Hills Golf Club | 3728 W Hayes Ave, Fremont OH 43420 | 27 (3x9) | Public | Opened 1964/1967/1995; 5 lakes |
| Fremont Country Club | 2340 E State St, Fremont OH 43420 | 18 | Private/Members-only | Founded 1921; 6,650 yds, par 71 |
| River Cliff Golf Course | 1313 Tiffin St, Fremont OH 43420 | 9 | Public? | Adjacent to SCPD Don W. Miller Park — verify T3 vs T8 governance |
| Green Hills Golf Course | 1959 S Main St, Clyde OH 43410 | 18 + 9 executive | Public | Founded 1958 |
| Hidden Hills Golf Club | 4900 County Road 16, Woodville OH 43469 | 18 | Public | |
| Sugar Creek Golf & Driving Range | 950 W Elmore Eastern Rd, Elmore OH 43416 | 18 | Public | GIS_VERIFY_COUNTY — Elmore straddles Ottawa/Sandusky |
| Sleepy Hollow Golf Course | 6029 SR 101 E, Clyde OH 43410 | 18 | CLOSED 2019 | Converted to RV park; stage status: Closed |

### Fremont Parks — Source: fremontohio.org/departments/parks/ (fetched 2026-05-21)
| Park Name | Address | Notes |
|-----------|---------|-------|
| Anderson Fields | 1313 Oak Harbor Rd | 3 LL baseball, basketball, playground, restrooms; replaced historic Anderson Field 1996 |
| Biggs-Kettner Memorial East Side Park | 601 St. Joseph St | Basketball, playground, skate park, restrooms, soccer, tennis, 6 shelter houses, NCIT access; rec complex w/indoor courts, seasonal ice rink, heated pool |
| Birchard Park | 1400 Birchard Ave | Basketball, tennis, shelters, shuffleboard, walking path, bandstand; est. 1871, land donated by Sardis Birchard |
| Richard D. Maier Park | 1019 Birchard Ave | Trees, gazebo, benches; small; renamed 1986 for former mayor |
| Swartzlander-Rotary Park | 329 Avis St | Small downtown park |
| Tschumy Corner | Corner of State and Front Sts | Decorative plaza; dedicated 2001 |
| Robert L. Walsh Park | 610 Morrison St | Walking trails, playground, large shelter, restrooms, fountain, memorial garden; "largest city park"; dedicated 1996 |
| Rodger W. Young Park | 1111 Tiffin St | 6 ball/softball fields, 8 tennis, 2 basketball, playground, 2 shelters, 4 multi-purpose fields; dedicated 1943 to WWII hero |
| Ozzie Rauch Park | 344 2nd St | Half-court basketball, picnic, play area; revamped 2021 |
| Sand Docks | End of North St / Sand Rd | City of Fremont boat ramp, river bank access; fishing access |
| Miles Newton Bridge | Downtown / between State St and Miles Newton Bridges | City of Fremont fishing access area on Sandusky River |
