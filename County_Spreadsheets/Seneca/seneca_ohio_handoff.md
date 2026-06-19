# Seneca County, Ohio — Handoff Document
**RUN_ID:** `seneca_oh_2026_05_25`
**PREFIX:** `SEN`
**County seat:** Tiffin
**Last updated:** 2026-05-26
**Status:** DISCOVERY COMPLETE — all 8 tiers finished; ready for pipeline

---

## County Context

- **County seat:** Tiffin
- **Major cities:** Tiffin (county seat), Fostoria (shared with Hancock/Wood counties)
- **Villages:** Attica, Bloomville, Bettsville, Flat Rock, Green Springs (shared with Sandusky County), New Riegel, Republic, Sycamore, Brokensword
- **15 townships** (from Townships_Officials2022-2023.xlsx — authoritative):
  Adams, Big Spring, Bloom, Clinton, Eden, Hopewell, Jackson, Liberty, Loudon, Pleasant, Reed, Scipio, Seneca, Thompson, Venice
- **Known park district:** Seneca County Park District — **confirmed Tier 3** (Park/Recreation District under OAC, audited as Park/Recreation District entity)
- **MORPC coverage:** No (Seneca County is not in the 15-county MORPC GIS layer)

---

## Known Multi-County Entities — Pre-Discovery DB Check (IMP-104)

Query run 2026-05-25 against natural_areas_v5.db. The following existing DB entities reference Seneca County:

### Sites (from Sandusky County run — City of Bellevue and Green Springs)
These entities were discovered during the Sandusky County run and assigned provisional OH-SAN-S-* IDs.
- **Bellevue (OH-SAN-S-072–078)**: City of Bellevue parks spanning Erie;Huron;Sandusky;Seneca. Bellevue is
  the only Ohio municipality in 4 counties. When encountered during T6 (Bellevue), use `KNOWN_MC:{id}`.
- **Green Springs (OH-SAN-S-110)**: Green Springs Cemetery spanning Sandusky;Seneca. When encountered
  during T6 (Green Springs), use `KNOWN_MC:{id}`.

| DB ID | Name | Counties | Municipality |
|-------|------|----------|--------------|
| OH-SAN-S-072 | Magdalyn Aigler Recreation Complex | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-073 | Amsden Park | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-074 | Buckingham Park | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-075 | Ellis Park | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-076 | Kern Street Park | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-077 | Ridge Park | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-078 | Robert Peters Athletic Field | Erie;Huron;Sandusky;Seneca | Bellevue |
| OH-SAN-S-110 | Green Springs Cemetery | Sandusky;Seneca | Green Springs |

**Handoff correction (2026-05-26)**: OH-SAN-S-072–078 are Bellevue city parks (not Green Springs).
City of Bellevue spans Erie, Huron, Sandusky, and Seneca counties (unique in Ohio). Also note:
OH-SAN-S-021 (Tea Kaufman Homestead) is solely in Sandusky County. OH-SAN-S-111 (Reformed Church Cemetery)
is Huron;Sandusky only, not Seneca.

No MC trails, trail networks, or site networks reference Seneca County.
No held_entities records are cross_county_held pending Seneca County.

---

## Baseline Seeds (from Seneca.xlsx — prompts, not imports)

Use these to recognize/confirm entities during tier discovery. Do NOT output as raw records.
Flag any seed never confirmed by an authoritative source as `unconfirmed_baseline_seed`.

| Name | Type (raw) | Acres | Notes |
|------|-----------|-------|-------|
| Attica Upground Reservoir | — | — | 2 entries; Ohio EPA water supply reservoirs — likely non-qualifying infrastructure; unresolved |
| Attica Upground Reservoir #2 | — | — | |
| Bowen Nature Preserve | Seneca County Parks | 66 | 11891 East CR 24, Republic, OH |
| Clary Boulee McDonald Preserve | Seneca County Parks | — | |
| Clinton Nature Preserve | Seneca County Parks | 33 | 400 East TR 132, Tiffin, OH — ODNR-owned, managed by SCPD → Tier 3 |
| Collier Scenic River Area (Sandusky River) | — | — | RESOLVED: Distinct from Howard Collier SNP; likely refers to river access near preserve |
| Forrest Nature Preserve | Seneca County Parks | 47 | |
| Fostoria Iron Triangle Rail Park | Fostoria City Park? | — | 499 S Poplar St, Fostoria, OH — Tier 6 (Fostoria municipal) |
| Fruth Wetland Nature Preserve | Seneca County Parks | 20 | |
| Garlo Heritage Nature Preserve | Seneca County Parks | 292 | |
| Hayes Presidential Library & Museums | Ohio History Connection | — | RESOLVED: Baseline error — Hayes Library is in Fremont (Sandusky County); no Seneca County presence |
| Howard Collier State Nature Preserve | State Nature Preserve | 114.86 | CONFIRMED T2 — staged |
| Knobbys Prairie Wildlife Area | State Wildlife Area / Public Hunting | 47 | CR 15 & TR 148; ODNR DOW — CONFIRMED T2 — staged |
| Lake Lepomis Wildlife Area | State Wildlife Area | — | UNRESOLVED — not found in OAC or any ODNR source |
| Mercy Community Nature Preserve | Seneca County Parks | 22 | |
| Mohawk Lake Dam | privately owned park | — | Tier 8 |
| Opportunity Park | Seneca County Parks | — | |
| Schekelhoff Nature Preserve | Tiffin Parks and Recreation | — | Tier 6 (Tiffin municipal) |
| Seneca Caverns | privately owned | — | 15248 E. Township Road 178, Bellevue, OH — Tier 8 |
| Seneca County Park District Conservation Area | Public Hunting / ODNR DOW | — | To be resolved at Tier 3 (SCPD discovery) |
| Seneca County Wildlife Area 1 | Public Hunting / ODNR DOW | — | CONFIRMED T2 — staged (OAC 1501:31-15-04) |
| Seneca County Wildlife Area 2 | Public Hunting / ODNR DOW | — | CONFIRMED T2 — staged |
| Seneca County Wildlife Area 3 | Public Hunting / ODNR DOW | — | CONFIRMED T2 — staged |
| Seneca County Wildlife Area 4 | Public Hunting / ODNR DOW | — | CONFIRMED T2 — staged |
| Silver Creek Wildlife Area | State Wildlife Area / Public Hunting | 42 | ODNR DOW — CONFIRMED T2 — staged |
| Springville Marsh State Nature Preserve | State Nature Preserve | 201.37 | CONFIRMED T2 — staged |
| St. John's Mill River Access | Seneca County Parks | — | Tier 3 (SCPD) |
| Steyer Nature Preserve | Seneca County Parks | 141 | Tier 3 (SCPD) |
| Sugar Creek Wildlife Area | State Wildlife Area / Public Hunting | 125 | ODNR DOW — CONFIRMED T2 — staged |
| Tiffin Drive-In Theater | privately owned | — | 4101 OH-53, Tiffin, OH — Tier 8 |
| Tiffin University Nature Preserve | Seneca County Parks | — | Managed by SCPD — Tier 3 |
| Wildlife Production Area 64 Wildlife Area | State Wildlife Area | 88.31 | UNRESOLVED — not found in OAC or any ODNR source |
| Zimmerman Nature Preserve | Seneca County Parks | 5.5 | 680 East SR 18, Tiffin, OH — Tier 3 (SCPD) |

---

## Tiers Completed

### Tier 8 — Private (COMPLETE — 78 entities; 11 null blocks)

**Golf courses (IMP-110 two-step enumeration complete):**
- Clinton Heights Golf Course (2760 E TR 122, Tiffin; public; 18-hole par 70; Active since 1957)
- Lakeland Golf Course (3770 CR 23, Fostoria; public; 18-hole par 70; Active; confirmed Seneca Co. via DSC)
- Loudon Meadows Golf Club (11072 W SR 18, Fostoria; private/members; 18-hole par 71; Active 1962)
- Mohawk Golf & Country Club (4399 S SR 231, Tiffin; private/country club; 18-hole Donald Ross; Active)
- Seneca Hills Golf Course (4044 W TR 98, Tiffin; Status: **Closed** per Golf Digest; conflicting info from GolfNow)

**Private nature / education / camp sites:**
- Seneca Caverns (15248 E TR 178, Bellevue OH; private show cave; ODNR Registered Natural Landmark; seasonal)
- Camp Pittenger / NWOCYC (8877 S TR 131, McCutchenville; private Christian youth camp; NRHP-listed)
- Franciscan Earth Literacy Center (194 St. Francis Ave., Tiffin; Sisters of St. Francis; env. education w/ trails)
- Camp Glen (6580 S TR 131, Tiffin; Camp Fire Sandusky County; Sandusky River; hiking; ACA-accredited; 1959)

**Private cemeteries (IMP-111 GNIS enumeration complete):**
- Greenlawn Cemetery (914 E CR 36, Tiffin; Greenlawn Cemetery Association 501c13; est. 1874)
- Fairmont Cemetery (1855 W TR 132, Tiffin; Fairmont Cemetery Association)
- Seneca Memory Gardens (4565 US 224, Tiffin; private partnership; est. 1970)
- 66 additional cemeteries from OGE GNIS enumeration (church, family, community — see YAML T8 records)
  - Deduplication flags: Attica Cemetery (may = T5 Attica-Venice Jt.), Zion Lutheran (may = T5 Zion Cem),
    Pleasant Ridge/Union/View (T5 relation uncertain), County Home Cem (possible T4), Bloomville Cem (possible T6)

**T8 null blocks (11):** Tiffin Drive-In (non-qualifying), Ag Society Fairgrounds (non-qualifying),
Mohawk Lake Dam (no confirmed managed park), Heidelberg University (private campus, no public natural area),
Seneca Hills Bible Camp (Pennsylvania — not Ohio), Cross Oak Camp (Auglaize Co.),
Fostoria CC (Hancock Co.), Hunting Preserves (none found), Agritourism (none qualifying),
Scout Camps (Camp Glen staged; Camp Pleasant Valley closed ~2011), Private Nature Centers (FELC + Camp Glen staged)

---

### Tier 7 — Conservancy / Land Trust (COMPLETE — 0 entities; 11 null blocks)

No T7 entities for Seneca County. Clary-Boulee McDonald Preserve was the only conservancy-managed property in the county; ownership confirmed transferred from Black Swamp Conservancy to SCPD → re-tiered to T3.

**§4 Known Organizations checked:**
- BSC (§4.2): land-we-own (16 props, none Seneca), land-we-protect (Clary-Boulee → SCPD → T3) → null
- TNC Ohio (§4.1): no Seneca County preserves → null
- NORTA/Wabash Cannonball (§4.4): Fulton/Henry/Lucas/Williams only, not Seneca → null
- ACRES (§4.3): Indiana border counties only, not applicable

**Additional organizations checked:**
- WCOLC: does not serve Seneca → null
- WRLC: operates in Seneca (24 counties) but conservation easements only; no publicly accessible preserves in Seneca → null
- Cardinal LC: southwest Ohio → null
- NCOLC: Richland County focus → null

**ONAPA check:** Springville Marsh = T2 (already staged). No new T7 entities.

**Land Trust Alliance / COLT:** No additional Seneca-specific land trusts found.

**T8 candidate flagged:** Franciscan Earth Literacy Center (FELC) — Sisters of St. Francis, 194 St. Francis Ave., Tiffin. Private religious nonprofit, not a land trust. Environmental education center with trails; to be staged at T8.

### Tier 6 — Municipal (COMPLETE — 27 entities)

**Tiffin (City of Tiffin Parks and Recreation Department)** — 17 Sites + 1 Trail:
- Sites: Hedges-Boyer Park (78 ac), Schekelhoff Park (37 ac, nature preserve), Highland Park (18 ac), Kernan Park (14 ac), Nature Trails Park (11 ac), Oakley Park (6 ac), Riverview Park (3.5 ac), Louisa K. Fast Park (3.25 ac, formerly Apple-Jack), Josiah Hedges Park (3 ac), Tiffin East Park (2.3 ac), Rotary Club of Tiffin Centennial Park (1.2 ac), Stalter Park (1 ac), Beechwood Park (1 ac), Junior Home Park, Lions Club Park (0.03 ac), Clouse-Kirian Leadership Park (0.1 ac), East Green
- Trail: Rock Creek Trail (2 miles paved, Hedges-Boyer to Josiah Hedges Park via Heidelberg University)

**Fostoria (City of Fostoria, Seneca County only)** — 6 Sites:
Foundation Park (50 ac), Iron Triangle Rail Park (5 ac), Jackson Park (8 ac), Harmon Park (0.5 ac), Buckley Street Courts, Veterans Memorial Reservoir (300 land ac)
Note: City Park, Gray Park (Hancock Co.) and Portage Park (Wood Co.) excluded. Reservoirs 1–5 (Daughtery, Mottram, Lamberjack, Mosier, LeComte) = Hancock Co., excluded.

**Attica** — 1 Site: Myers Park (14999 E. County Rd 56)
**Bloomville** — 1 Site: Beeghly Park (address TBD — GPS acquisition required)
**New Riegel** — 1 Site: New Riegel Park (13 Near West St.)
**Bellevue** — null (all 7 parks confirmed KNOWN_MC: OH-SAN-S-072–078 = exact match)
**Bettsville** — null (H.P. Eells Park handled at T3 with governance flag)
**Green Springs** — null (Whirlpool Park CLOSED Dec 2025; Beaver Creek Reservoir = Sandusky Co./City of Clyde)
**Republic** — null (no village-owned parks found)
**Tiffin cemeteries/golf** — null (Greenlawn = private 501(c)(13); no city cemetery; golf courses private T8)
**Fostoria cemeteries/golf** — null (no city cemetery; Fostoria CC + Loudon Meadows = private T8)

Apple-Jack Park renamed Louisa K. Fast Park by City Council in 2025 (name change confirmed from city website).

### Tier 5 — Township (COMPLETE — 12 entities)
- **Hopewell Township**: Meadowbrook Park (160 acres, 5430 W. Tiffin St., Bascom, OH 44809; wolf creek; confirmed township-owned since 1976)
- **Jackson Township**: Zion Cemetery (Active, CR 592) + Disinger Cemetery (Non-active, CR 25) — confirmed trustee-managed
- **Eden Township**: Rock Run Cemetery (S Township Rd 17 × US 224) — confirmed transferred to township trustees
- **Venice Township**: Attica Venice Township Joint Cemetery (ODRE registered CGR.0000981776, Attica)
- **Bloom Township**: Bloom Township Cemetery (E Township Rd 58 × S County Rd 43) — named cemetery, ownership presumed
- **Loudon Township**: Loudon Township Cemetery (SR 18 E, Fostoria; GPS 41.13533, -83.38742) — named cemetery, ownership presumed
- **Pleasant Township**: 5 cemeteries maintained by township (Chenoweth/Gay Rd., Gundy/Norton Rd., Ebenezer M.E./Johnson Rd., Little Pennsylvania/SR 665, Oak Grove/Alkire Rd.) — township maintains; ownership not fully confirmed
- 10 townships with no parks found; §4.2a: thompsonohio.org discarded (Geauga County); 9 townships with unconfirmed cemetery ownership

### Tier 4 — County (COMPLETE — null)
No county commissioner-managed parks, trails, or natural areas found. County departments page lists no parks department. All parks/preserves are under SCPD (Tier 3) or municipal governance. NRHP: 45 properties, none are natural areas or covered bridges. Seneca County Fairgrounds = Agricultural Society (T8). Camp Pittenger = NWOCYC (T8). Seneca County Museum = historic house, no natural area.

### Tier 3 — District (COMPLETE — 15 entities; 3 added as late-T3 during T7 review)
- **Seneca County Park District (Tier 3)**: 11 Sites — Bowen (64 ac), Clinton (33 ac, ODNR-leased), Forrest (47 ac), Fruth Wetland (20 ac), Garlo Heritage (292 ac), Mercy Community (22 ac), Opportunity Park, Steyer (141 ac), Tiffin University NP, Zimmerman (5.5 ac), St. John's Mill River Access
- **H.P. Eells Park** (Bettsville): 1 Site — governance uncertain; Bettsville Recreation Board possibly dissolved 2009; may re-tier to T6 (Village of Bettsville)
- **Clary Boulee McDonald Preserve** (SCPD): 1 Site + 2 Trails — LATE T3 DISCOVERY confirmed during T7 review. BSC website confirms "Now owned and managed by the Seneca County Park District." 160 ac, Kansas OH, two loop trails (1.0 mi + 0.4 mi H2Ohio). Staged via _stage_t3_late_clary_boulee.py.
- SWCD: no public natural areas → null
- Regional Planning Commission: no trail/land management → null
- Conservancy Districts: 0 → null | Water/Sewer Districts: 0 → null

### Tier 1 — Federal & Tribal (COMPLETE — all null)
All 8 federal/tribal governance categories checked and confirmed null for Seneca County.
Sources: USFS (WNF not in Seneca), NPS (no units), USFWS (no refuges), USACE (no projects),
BLM (no surface lands), DoD (no installations), VA NCA (no national cemeteries or soldiers lots),
Tribal (no federally recognized tribes with trust lands in Ohio).

### Tier 2 — State (COMPLETE — 10 entities)
- 2 State Nature Preserves (ODNR DNAP): Howard Collier SNP (114.86 ac), Springville Marsh SNP (201.37 ac)
- 3 Named Wildlife Areas (ODNR DOW): Sugar Creek WA (125 ac), Knobbys Prairie WA (47 ac), Silver Creek WA (42 ac)
- 4 Numbered Wildlife Areas (ODNR DOW, OAC confirmed): Seneca County WA 1, 2, 3, 4 (no GPS/acreage in web sources)
- 1 Scenic River (ODNR Scenic Rivers Program, CROSS_COUNTY_CANDIDATE): Sandusky State Scenic River (65 mi, Sandusky/Seneca/Wyandot)

Unresolved T2 baseline seeds: Lake Lepomis WA, Wildlife Production Area 64 (not in OAC or any ODNR web source)
Attica Upground Reservoirs: Village water supply infrastructure — no managed recreation confirmed; flagged for human review
Clinton Nature Preserve: ODNR-owned land, managed by SCPD → deferred to Tier 3

---

## Tiers Remaining

| Tier | Status | Notes |
|------|--------|-------|
| T1 — Federal & Tribal | COMPLETE (null) | All sources confirmed null — see staging YAML tier_nulls |
| T2 — State | COMPLETE | 10 entities staged; 2 unresolved seeds; 1 cross-county candidate |
| T3 — District | COMPLETE | 12 entities (11 SCPD Sites + 1 H.P. Eells Park w/ governance flag); 6 null blocks |
| T4 — County | COMPLETE (null) | No county commissioner-managed parks; SCPD is T3; 5 null blocks staged |
| T5 — Township | COMPLETE | 12 entities (1 park + 11 cemeteries); 24 null blocks; §4.2a: thompsonohio.org discarded (Geauga Co.) |
| T6 — Municipal | COMPLETE | 27 entities: 17 Tiffin sites + Rock Creek Trail + 6 Fostoria (Seneca Co.) + Myers Park (Attica) + Beeghly Park (Bloomville) + New Riegel Park; 10 null blocks |
| T7 — Conservancy | COMPLETE (null — 0 new T7 entities) | BSC/TNC/NORTA/WRLC/NCOLC all checked; Clary-Boulee re-tiered T3 (SCPD confirmed); 11 null blocks |
| T8 — Private | **COMPLETE** | 78 entities: 5 golf courses, Seneca Caverns, Camp Pittenger, FELC, Camp Glen, 3 named cemeteries, 66 OGE GNIS cemeteries; 11 null blocks |

---

## Key Active Flags

- **⚠️ TIER CORRECTION: Seneca County Park District is Tier 3 (not Tier 4)** — Ohio Auditor confirms SCPD as a Park/Recreation District entity (audited 2024). All SCPD baseline seeds (Bowen, Clary-Boulee, Clinton, Forrest, Fruth, Garlo, Mercy, Opportunity, St. John's Mill, Steyer, Tiffin University NP, Zimmerman) are Tier 3 entities. Tier 4 (County) will focus on county commissioner-managed properties only.
- **Bettsville Recreation Board** — Park/Recreation District per Ohio Auditor; last audit covers period ending 04/30/2009, released 2010. No audits since. Possibly dissolved. Investigate during Tier 3.
- **Collier/Howard SNP identity RESOLVED** — Howard Collier SNP confirmed as a terrestrial preserve (ODNR DNAP). "Collier Scenic River Area" in baseline is a distinct designation (river access near SNP) or a secondary name for the Sandusky State Scenic River access. Baseline seed marked resolved.
- **Hayes Library baseline error CONFIRMED** — Rutherford B. Hayes Library is in Fremont (Sandusky County). No Seneca County OHC presence found. Baseline entry is an error.
- **NCIT does not extend into Seneca County (Q4 RESOLVED)** — North Coast Inland Trail documented only in Erie/Huron/Ottawa/Sandusky counties; no Seneca County segment found.
- **Green Springs cross-county entities (OH-SAN-S-072–078, OH-SAN-S-110)** — 8 sites from Sandusky run. These will be encountered during Tier 6 (Green Springs municipal). Use KNOWN_MC notation.
- **Fostoria** — city straddles Seneca/Hancock/Wood county lines; entities will need multi-county handling.
- **Sandusky State Scenic River** — staged as CROSS_COUNTY_CANDIDATE (T2, Sandusky/Seneca/Wyandot); not currently in DB.

---

## Entities Discovered

### Tier 8 — Private (78 entities)

| # | Name | Type | Governance | Notes |
|---|------|------|-----------|-------|
| 62 | Clinton Heights Golf Course | Site | Private/public golf | 2760 E TR 122, Tiffin; public; 18-hole par 70; Active since 1957 |
| 63 | Lakeland Golf Course | Site | Private/public golf | 3770 CR 23, Fostoria; public; 18-hole; Active; confirmed Seneca Co. |
| 64 | Loudon Meadows Golf Club | Site | Private golf club | 11072 W SR 18, Fostoria; members-only; 18-hole par 71; Active 1962 |
| 65 | Mohawk Golf & Country Club | Site | Private country club | 4399 S SR 231, Tiffin; private; Donald Ross design; Active |
| 66 | Seneca Hills Golf Course | Site | Private golf | 4044 W TR 98, Tiffin; **Status: CLOSED** per Golf Digest; conflicting GolfNow |
| 67 | Seneca Caverns | Site | Private (Seneca Caverns LLC) | 15248 E TR 178, Bellevue OH; show cave; ODNR Reg. Natural Landmark |
| 68 | Camp Pittenger (NWOCYC) | Site | Private (NWOCYC / Christian camp) | 8877 S TR 131, McCutchenville; NRHP-listed; youth camp |
| 69 | Franciscan Earth Literacy Center | Site | Private (Sisters of St. Francis) | 194 St. Francis Ave., Tiffin; env. education; trails |
| 70 | Greenlawn Cemetery | Site | Private (501c13 association) | 914 E CR 36, Tiffin; est. 1874 |
| 71 | Fairmont Cemetery | Site | Private (cemetery association) | 1855 W TR 132, Tiffin |
| 72 | Seneca Memory Gardens | Site | Private (partnership) | 4565 US 224, Tiffin; est. 1970 |
| 73 | Camp Glen | Site | Camp Fire Sandusky County | 6580 S TR 131, Tiffin; Sandusky River; ACA-accredited; 1959 |
| 74–139 | OGE GNIS Cemeteries (66) | Site | Various private | Adams Lutheran, Armstrong, Assumption, Attica†, Bare, Baugher, Bethel, Block, Bloomville†, Brundedge, Bunker Hill, Caroline Lutheran, Clay, Coffman, County Home†, Crissa, Dunkard, Dysinger, East Baseline Baptist, Egbert, Farewell Retreat, Feaselburg, Fireside, Flat Rock, Fravel, French Town, Hopewell, Jerusalem, Kagy, Lay, Lowell, McMeen, Mennonite, Methodist, Null, Omar, Payne, Pleasant Ridge, Pleasant Union, Pleasant View, Randall, Raymond, Reformed, Reformed [2], Reisz, Rock Creek, Rock Creek [2], St Andrews, St Boniface, St Jacobs, St Josephs, St Marys, St Michaels, St Patricks, St Peters, St Stephens, Sts Peter and Paul, Sand Ridge, Sheller, Shiloh, Shock, Swamp, Underhill, Union, Woodlawn, Zion Lutheran† |

*† = deduplication flag; see identity_notes_raw in YAML*

### Tier 6 — Municipal (27 entities)

| # | Name | Type | Governance | Acres | Notes |
|---|------|------|-----------|-------|-------|
| 35 | Hedges-Boyer Park | Site | City of Tiffin | 78 | Coe St × Summit St; Rock Creek Trail trailhead; swimming pool |
| 36 | Schekelhoff Park | Site | City of Tiffin | 37 | Sandusky River; nature preserve; Storybook Trail; connects to SCPD Clinton NP |
| 37 | Highland Park | Site | City of Tiffin | 18 | 8th Ave × N. Washington; baseball, skate park, dog park |
| 38 | Kernan Park | Site | City of Tiffin | 14 | Ohio Ave × Riverside Dr; 2 youth softball fields |
| 39 | Nature Trails Park | Site | City of Tiffin | 11 | E. Davis St; Sandusky River; paved 0.25-mi trail |
| 40 | Oakley Park | Site | City of Tiffin | 6 | Park Ave × Grand Ave × 6th Ave; 0.7-mi lighted trail |
| 41 | Riverview Park | Site | City of Tiffin | 3.5 | Longfellow Dr area; 0.25-mi paved trail |
| 42 | Louisa K. Fast Park | Site | City of Tiffin | 3.25 | 432 Jackson St (Apple × Jackson); formerly Apple-Jack Park (renamed 2025) |
| 43 | Josiah Hedges Park | Site | City of Tiffin | 3 | Schonhardt × Park Place; Rock Creek Trail trailhead (east) |
| 44 | Tiffin East Park | Site | City of Tiffin | 2.3 | SR 101 E of city limits; Federal Lands to Parks; pending federal auction |
| 45 | Rotary Club of Tiffin Centennial Park | Site | City of Tiffin | 1.2 | Frost Parkway; Sandusky River views; Camp Ball marker |
| 46 | Stalter Park | Site | City of Tiffin | 1 | Ohio Ave × Clinton Ave; Camp Noble marker |
| 47 | Beechwood Park | Site | City of Tiffin | 1 | Ashwood Dr × Beechwood Dr |
| 48 | Junior Home Park | Site | City of Tiffin | — | Sandusky River north side; fishing/kayaking |
| 49 | Lions Club Park | Site | City of Tiffin | 0.03 | Downtown, adj. City Annex |
| 50 | Clouse-Kirian Leadership Park | Site | City of Tiffin | 0.1 | 22 S. Washington St; Sandusky River overlook; gazebo |
| 51 | East Green | Site | City of Tiffin | — | Downtown; splash pad + Frost-Kalnow Amphitheater |
| 52 | Rock Creek Trail | Trail | City of Tiffin | — | 2 mi paved; Hedges-Boyer to Josiah Hedges via Heidelberg University |
| 53 | Foundation Park | Site | City of Fostoria | 50 | 1225 S. Union St; Seneca Co.; 13 ball fields; dog park; formerly Meadowlark Park |
| 54 | Iron Triangle Rail Park | Site | City of Fostoria | 5 | 499 S. Poplar St; Seneca Co.; railroad viewing pavilion |
| 55 | Jackson Park | Site | City of Fostoria | 8 | Jackson St W of Buckley; Seneca Co. |
| 56 | Harmon Park | Site | City of Fostoria | 0.5 | Wood × Fourth Sts; Seneca Co. |
| 57 | Buckley Street Courts | Site | City of Fostoria | — | Buckley × Eastern Ave; Seneca Co.; 3 tennis, 1 basketball |
| 58 | Veterans Memorial Reservoir | Site | City of Fostoria | 300 | SR 12 area, Seneca Co.; 180 water ac; 2.3-mi stone trail; fishing/boating/hunting |
| 59 | Myers Park | Site | Village of Attica | — | 14999 E. County Rd 56, Attica |
| 60 | Beeghly Park | Site | Village of Bloomville | — | Bloomville; address TBD; GPS acquisition required |
| 61 | New Riegel Park | Site | Village of New Riegel | — | 13 Near West St.; 3 ball fields, basketball, playground |

### Tier 3 — District (12 entities)

| # | Name | Entity Type | Governance | Acres | Notes |
|---|------|-------------|-----------|-------|-------|
| 11 | Bowen Nature Preserve | Site | SCPD | 64 | 11891 East CR 24, Republic |
| 12 | Clinton Nature Preserve | Site | SCPD (ODNR-leased) | 33 | 400 E TR 132, Tiffin; co-op w/ Clinton Twp |
| 13 | Forrest Nature Preserve | Site | SCPD | 47 | 701 E CR 6, Tiffin; 2 parking lots |
| 14 | Fruth Wetland Nature Preserve | Site | SCPD | 20 | 10130 W SR 18, Fostoria (park office) |
| 15 | Garlo Heritage Nature Preserve | Site | SCPD | 292 | 6777 S SR 19, Bloomville; 7.4 mi trails |
| 16 | Mercy Community Nature Preserve | Site | SCPD | 22 | 45 St. Lawrence Dr, Tiffin; co-op w/ Mercy Hospital |
| 17 | Opportunity Park | Site | SCPD (co-op) | unknown | 780 E CR 20, Tiffin; accessible; co-op w/ County Comm./Opp. Center |
| 18 | Steyer Nature Preserve | Site | SCPD | 141 | 5901 N CR 33, Tiffin; 4.17 mi trails; Sandusky River frontage |
| 19 | Tiffin University Nature Preserve | Site | SCPD (TU land) | unknown | 2471 W CR 26, Tiffin; 1.23 mi trail; co-op w/ TU |
| 20 | Zimmerman Nature Preserve | Site | SCPD | 5.5 | 680 E SR 18, Tiffin |
| 21 | St. John's Mill River Access | Site | SCPD | unknown | 2320 W CR 6, Tiffin; Sandusky River; AP candidate |
| 22 | H.P. Eells Park | Site | BRC or Village of Bettsville? | unknown | 7461 N TR 70; GOVERNANCE FLAG |
| 23 | Clary Boulee McDonald Preserve | Site | SCPD | 160 | 4747 W. SR 12 / 5090 W. TR 36, Kansas OH; LATE T3 — confirmed SCPD during T7 |
| 24 | Clary Boulee McDonald Preserve — Wetland Loop Trail | Trail | SCPD | — | ~1.0 mi; north entrance; LATE T3 |
| 25 | Clary Boulee McDonald Preserve — H2Ohio Loop Trail | Trail | SCPD | — | ~0.4 mi; north entrance; LATE T3 |

### Tier 2 — State (10 entities)

| # | Name | Entity Type | Governance | Counties | Acres | Notes |
|---|------|-------------|-----------|---------|-------|-------|
| 1 | Howard Collier State Nature Preserve | Site | ODNR DNAP | Seneca | 114.86 | 1655 W TR 38, Tiffin |
| 2 | Springville Marsh State Nature Preserve | Site | ODNR DNAP | Seneca | 201.37 | 12250 TR 24, Carey |
| 3 | Sugar Creek Wildlife Area | Site | ODNR DOW | Seneca | 125 | TR 157 / TR 148 |
| 4 | Knobbys Prairie Wildlife Area | Site | ODNR DOW | Seneca | 47 | CR 15 / TR 148 |
| 5 | Silver Creek Wildlife Area | Site | ODNR DOW | Seneca | 42 | TR 58 at TR 181/CR 6, near Bloomville |
| 6 | Seneca County Wildlife Area 1 | Site | ODNR DOW | Seneca | unknown | Confirmed OAC 1501:31-15-04; no GPS |
| 7 | Seneca County Wildlife Area 2 | Site | ODNR DOW | Seneca | unknown | Confirmed OAC 1501:31-15-04; no GPS |
| 8 | Seneca County Wildlife Area 3 | Site | ODNR DOW | Seneca | unknown | Confirmed OAC 1501:31-15-04; no GPS |
| 9 | Seneca County Wildlife Area 4 | Site | ODNR DOW | Seneca | unknown | Confirmed OAC 1501:31-15-04; no GPS |
| 10 | Sandusky State Scenic River | Trail (water) | ODNR Scenic Rivers | Sandusky;Seneca;Wyandot | — | CROSS_COUNTY_CANDIDATE; 65 mi; designated 1970 |

---

## Held Entities

*(none yet — GPS-missing entities will be held at Stage 2c)*

---

## Unresolved Baseline Seeds

| Name | Reason |
|------|--------|
| Lake Lepomis Wildlife Area | Not found in OAC 1501:31-15-04, ODNR web, or any authoritative source |
| Wildlife Production Area 64 | Not found in OAC 1501:31-15-04, ODNR web, or any authoritative source |
| Attica Upground Reservoir | Village water supply infrastructure; no managed recreation confirmed; needs human verification |
| Attica Upground Reservoir #2 | Same as above |
| Hayes Presidential Library & Museums | Confirmed baseline error — facility is in Fremont (Sandusky County); no Seneca entity |

---

## Open Questions

1. ~~Does Hayes Presidential Library & Museums have any Seneca County presence, or is this a baseline error?~~ **RESOLVED: Baseline error. Hayes Library is in Fremont/Sandusky County.**
2. ~~Is "Collier Scenic River Area" the same entity as "Howard Collier State Nature Preserve," or are these distinct?~~ **RESOLVED: Distinct entities. Howard Collier SNP is a terrestrial ODNR preserve; Collier Scenic River Area appears to be a colloquial reference to river access near the preserve or part of the Sandusky Scenic River designation.**
3. What are the specific parcel locations/names for "Seneca County Wildlife Areas 1–4" and "Seneca County Park District Conservation Area"? No GPS or address found from web sources.
4. ~~Does the North Coast Inland Trail extend into Seneca County?~~ **RESOLVED: No — NCIT does not extend into Seneca County. Trail terminates in Sandusky/Erie/Ottawa/Huron/Lorain counties.**
5. Is Bettsville Recreation Board still active, or dissolved after 2009? H.P. Eells Park staged as T3 with governance flag. If dissolved → H.P. Eells re-tiers to T6 (Village of Bettsville).
6. ~~Does the Seneca County SWCD own any publicly accessible natural areas?~~ **RESOLVED: No — SWCD confirmed null.**
7. ~~Does the Seneca County Regional Planning Commission manage any trails or greenways?~~ **RESOLVED: No — RPC confirmed null; website redirects to County Auditor.**
8. ~~What is the timeline for Clary Boulee McDonald Preserve transfer from Black Swamp Conservancy to SCPD?~~ **RESOLVED (2026-05-26, T7 review):** BSC website confirms transfer complete — "Now owned and managed by the Seneca County Park District." Staged as 3 T3 entities (1 Site + 2 Trails).

---

## Next Steps (ordered)

**Discovery is COMPLETE. All 8 tiers finished (IMP-080 verified 2026-05-26).**
**Total: 146 raw records | 83 tier_nulls | 1 cross-county candidate (Sandusky State Scenic River)**

1. **Pre-pipeline open question resolution** (before Stage 1a):
   - Q5: H.P. Eells Park governance — is Bettsville Recreation Board still active or dissolved? If dissolved → re-tier to T6 (Village of Bettsville). Address: 7461 N TR 70, Bettsville.
   - Attica Upground Reservoirs — confirm public recreation access (or stage as unconfirmed_baseline_seed)
   - Deduplication: Attica Cemetery vs T5 Attica-Venice Joint Cemetery; Zion Lutheran vs T5 Zion Cemetery (Jackson Twp)
2. **Run Stage 1a — Resolution Engine Pass 1** → `na_resolution_engine_v5.5.md`
   - Read `processing/na_processing_orchestration_v5.5.md` first
   - Create `seneca_config.json` from `utilities/na_pipeline_config_template.json`
   - Entity IDs assigned: `OH-SEN-{TYPE}-{SEQ}`
3. **Stage 1b** — Resolution Engine Pass 2 (APs)
4. **Stage 2a** — GPS Fill-Forward (IMP-031)
5. **Stage 2b** — GPS Acquisition → `na_gps_acquisition_v5.3.md`
6. **Stage 2c/2d** — GPS Gate (Sites then APs) → hold GPS-missing entities
7. **Stage 3** — Normalization Engine → `na_normalization_engine_v5.8.md` (MANDATORY BLOCKING GATE)
8. **Stage 4** — TSV Output (read output spec per entity type)
9. **Stage 4.5** — Vocabulary Validation Gate (halts on violation)
10. **Stage 5** — TSV Integrity Check (non-halting; surface vocabulary expansion candidates)
11. **Stage 5.5** — HUMAN REVIEW GATE (pipeline halts; explicit human confirmation required)
12. **Stage 6** — DB Upsert → `ON CONFLICT DO UPDATE`; DDL for all 3 table groups (IMP-087)

**Known pipeline considerations:**
- Sandusky State Scenic River (T2, CROSS_COUNTY_CANDIDATE): hold as cross_county_held pending Wyandot/Sandusky runs
- Green Springs parks (KNOWN_MC: OH-SAN-S-072–078, OH-SAN-S-110): do NOT re-stage; reference existing DB IDs
- Seneca Memory Gardens, Greenlawn, Fairmont: private cemetery associations → normalize ownership carefully
- ~78 T8 cemeteries with no GPS: all will hit GPS Gate; most will be held unless gps_unresolvable=true
- County Home Cemetery: flag for T4 governance verification before normalization
- Bloomville Cemetery: flag for T6 governance verification before normalization

---

## Pre-Discovery Checklist — Tier 8

*Built 2026-05-26 before any T8 searches begin. (IMP-029)*
*Sub-procedure: na_private_discovery_subproc_v5.7.md (on disk as v5.3)*

### Known targets from prior tiers (§3.4 Cross-Reference triggers)

| Target | Source Tier | Address | Notes |
|--------|------------|---------|-------|
| Seneca Caverns | T4 baseline | 15248 E. Township Rd 178, Bellevue OH 44811 | Private tourist attraction; show cavern |
| Tiffin Drive-In Theater | T6 baseline | 4101 OH-53, Tiffin OH 44883 | Check qualifying criteria |
| Seneca County Ag Society / Fairgrounds | T4 null block | 100 Hopewell Ave, Tiffin OH 44883 | Agricultural Society (nonprofit); T8 candidate |
| Camp Pittenger / NWOCYC | T4 null block | 8877 S Township Rd 131, McCutchenville OH 44844 | NHRP-listed; private Christian youth camp |
| Greenlawn Cemetery | T6 null block | 895 E County Rd 36, Tiffin OH 44883 | Private 501(c)(13) cemetery |
| Franciscan Earth Literacy Center (FELC) | T7 null block | 194 St. Francis Ave., Tiffin OH 44883 | Sisters of St. Francis; env. education w/ trails |
| Heidelberg University natural areas | T2 null block | 310 E Market St, Tiffin OH 44883 | Private university; check accessible natural areas |
| Mohawk Lake Dam park | baseline | unknown location | Baseline seed "privately owned park" — needs web search |

### Golf course enumeration (IMP-110 — mandatory two-step)
- [x] Step 1a: PGA.com course finder (state → Seneca County filter)
- [x] Step 1b: Destination Seneca County golf page
- [x] Step 2: Direct search for any courses not in directories
- [x] Known from prior tiers: Clinton Heights GC, Seneca Hills GC, Fostoria Country Club, Loudon Meadows Golf Club
  Result: 5 courses staged (Clinton Heights, Lakeland, Loudon Meadows, Mohawk G&CC, Seneca Hills-Closed); Fostoria CC = Hancock Co. (null)

### Cemetery GNIS enumeration (IMP-111 — mandatory before search queries)
- [x] Step 1: OhioGenealogyExpress.com — 73 entries total
- [x] Step 2: PeopleLegacy cross-referenced (OGE treated as primary)
- [x] Step 3: Cross-referenced against T2–T7 staged records; 9 already staged, 3 in T8 main, 66 in T8 cemeteries
- [x] Complete cemetery list written to Captured Source Data (IMP-030) ✅

### Direct search methods (§5.1)
- [x] Private nature centers, preserves, nonprofits → FELC (staged), Camp Pittenger (staged), no others
- [x] Scout camps / church camps / retreat centers → Camp Glen (Camp Fire, staged); Seneca Hills = PA; Camp Pleasant Valley = closed ~2011
- [x] ODNR Licensed Hunting Preserves Registry → null (no licensed preserves found)
- [x] Agritourism / farm trails → null (no qualifying entities)
- [x] Heidelberg University natural areas → null (private campus; Rock Creek Trail = T6 city-managed)

### Entity fetches (§6.1 — fetch after Pre-Discovery Checklist is written)
- [x] Seneca Caverns website → staged T8
- [x] Camp Pittenger / NWOCYC website → staged T8
- [x] FELC (felctiffin.org) → staged T8
- [x] Heidelberg University arboretum/woodland → null block staged
- [x] Mohawk Lake Dam → null block staged (no confirmed managed park)
- [x] Ag Society Fairgrounds → null block staged (non-qualifying)
- [x] Golf courses (individual pages after enumeration) → all 5 staged
- [x] Cemeteries (individual pages after GNIS enumeration) → 66 OGE cemeteries staged

---

## Pre-Discovery Checklist — Tier 6

*Built 2026-05-26 from OTA roster, county baseline, Green Springs DB lookup, and T3-T5 cross-references.*
*MORPC CSV: Seneca County NOT in 15-county MORPC GIS layer.*
*Green Springs: KNOWN_MC entities from Sandusky run — use KNOWN_MC:{id} notation.*

*CONFIRMED INCORPORATED MUNICIPALITIES (from Wikipedia Seneca County article + DB verification):*
*CDPs (Bascom, Flat Rock, Fort Seneca, Kansas, McCutchenville, Melmore, Old Fort) = unincorporated → no T6 entity.*

### Cities (3)
- [x] **Tiffin** — 17 Sites + Rock Creek Trail staged; Schekelhoff Park confirmed (baseline "Schekelhoff Nature Preserve"); no city cemetery/golf
- [x] **Fostoria** — 6 Seneca Co. Sites staged; Hancock/Wood Co. parks excluded; Reservoirs 1–5 = Hancock Co.
- [x] **Bellevue** — KNOWN_MC: OH-SAN-S-072–078 confirmed = all 7 current parks; null for new T6 entities

### Villages (6)
- [x] **Attica** — Myers Park staged; Attica Upground Reservoir = deferred (no confirmed public recreation access); Attica Venice Joint Cemetery = T5 (already staged)
- [x] **Bettsville** — null (H.P. Eells at T3 w/ governance flag; no additional village parks found)
- [x] **Bloomville** — Beeghly Park staged; Garlo Heritage NP = T3 (SCPD, already staged)
- [x] **Green Springs** — null (Whirlpool Park CLOSED; Beaver Creek Reservoir = Sandusky Co./City of Clyde; OH-SAN-S-110 KNOWN_MC = cemetery only)
- [x] **New Riegel** — New Riegel Park staged (13 Near West St.)
- [x] **Republic** — null (no village-owned parks; Bowen NP = T3 SCPD already staged)

---

## Pre-Discovery Checklist — Tier 1 (COMPLETE)

✅ USFS — Wayne National Forest: Seneca County not in WNF territory — null
✅ NPS — NPS unit finder: no NPS units in Seneca County — null
✅ USFWS — refuge locator: no refuges in Seneca County — null
✅ USACE — USACE project locator: no USACE projects in Seneca County — null
✅ BLM — BLM parcel data: no BLM surface lands in Seneca County — null
✅ DoD — installation finder: no DoD installations in Seneca County — null
✅ VA NCA — national cemeteries directory: no VA national cemeteries in Seneca County — null
✅ VA NCA — Soldiers' Lots directory: no Soldiers' Lots in Seneca County — null
✅ Tribal — BIA tribal land registry: no federally recognized tribes with trust lands in Ohio — null

---

## Pre-Discovery Checklist — Tier 2 (COMPLETE)

✅ ODNR DNAP — State Nature Preserves: 2 found (Howard Collier, Springville Marsh)
✅ ODNR DOW — Wildlife Areas: 7 found (Sugar Creek, Knobbys Prairie, Silver Creek, WA 1–4)
✅ ODNR Scenic Rivers — Sandusky State Scenic River (CROSS_COUNTY_CANDIDATE)
✅ ODNR Division of Parks — no state parks in Seneca County — null
✅ ODNR Division of Forestry — no state forests in Seneca County — null
✅ Ohio History Connection — no OHC sites in Seneca County — null
✅ ODOT — no scenic byways or rest areas with recreation in Seneca County — null
✅ Public Universities — Heidelberg and Tiffin University both private; no public university natural areas — null
✅ SORP cross-check — 42 ODNR parcels / 1,065.6 acres; unresolved gap ~350 ac (Lake Lepomis, WPA 64 unconfirmed)

---

## Pre-Discovery Checklist — Tier 4

*Created 2026-05-26 before beginning T4 entity fetches.*

Sources to check:
- [ ] Seneca County government website — parks, recreation, facilities, open space pages
- [ ] Seneca County Commissioners website — land acquisitions, park resolutions
- [ ] Seneca County GIS / Auditor parcel data — county-owned open space parcels
- [ ] NRHP search for Seneca County Ohio — bridges, historic structures, natural features
- [ ] Destination Seneca County (tourism) — county-level facilities
- [ ] Seneca County Fairgrounds — county-owned agricultural/fair land
- [ ] Seneca County Engineer — any county-managed bikeway or trail corridor

---

## Pre-Discovery Checklist — Tier 5

*Built 2026-05-26 from OTA Active Township Roster (Townships_Officials2022-2023.xlsx).*
*All 15 townships confirmed active (all present in OTA roster — no defunct candidates).*
*Per §5.6 (IMP-099): cemetery search mandatory for every township regardless of parks.*
*High-risk common names (§4.2a): Clinton, Jackson, Liberty, Pleasant.*

| Township | Pop (2020) | Website (OTA) | Parks/Rec | Cemeteries | Status |
|----------|-----------|---------------|-----------|------------|--------|
| Adams | 1,247 | adamstwpoh.com ✅ | null | unconfirmed | COMPLETE |
| Big Spring | 1,683 | none | null | unconfirmed | COMPLETE |
| Bloom | 1,624 | none | null | Bloom Twp Cem ✅ | COMPLETE |
| Clinton | 4,105 | clintontwpsenecacounty.com ✅ | null | unconfirmed | COMPLETE |
| Eden | 2,042 | none | null | Rock Run Cem ✅ | COMPLETE |
| Hopewell | 2,672 | hopewell-township.com ✅ | Meadowbrook Park ✅ | unconfirmed | COMPLETE |
| Jackson | 1,401 | jacksontwpseneca.org ✅ | null | Zion+Disinger ✅ | COMPLETE |
| Liberty | 2,029 | none (§4.2a: others discarded) | null | Liberty Cem? uncertain | COMPLETE |
| Loudon | 2,246 | loudontownship.com ✅ | null | Loudon Twp Cem ✅ | COMPLETE |
| Pleasant | 1,477 | pleasanttownshipsenecacounty.com ✅ | null | 5 cems (maintains) ✅ | COMPLETE |
| Reed | 738 | none | null | unconfirmed | COMPLETE |
| Scipio | 1,674 | none | null | unconfirmed | COMPLETE |
| Seneca | 1,444 | none | null | unconfirmed | COMPLETE |
| Thompson | 1,370 | none (§4.2a: .org=Geauga Co.) | null | unconfirmed | COMPLETE |
| Venice | 1,683 | none | null | Attica-Venice Joint ✅ | COMPLETE |

---

## Pre-Discovery Checklist — Tier 3

*Ohio Auditor pre-enumeration complete — 2026-05-26*
*URL: https://ohioauditor.gov/AuditSearch/Search.aspx*
*County filter: Seneca*
*Entity types searched: Park/Recreation District, Conservancy District, Soil/Water Conservation District/Joint Board, Water/Sewer/Sanitary District, Regional Planning Commission / Organization*

### Entities to Investigate:

- [ ] **Seneca County Park District** — Park/Recreation District; active (last audit 2024, FY 2022–2023)
  - Website: https://www.senecacountyparks.com/
  - Primary source for many baseline seeds (Bowen, Clary-Boulee, Clinton, Forrest, Fruth, Garlo, Mercy, Opportunity, St. John's Mill, Steyer, Tiffin University NP, Zimmerman)
  - Clinton NP: ODNR-owned land managed by SCPD → governs at Tier 3

- [ ] **Bettsville Recreation Board** — Park/Recreation District; last audit covers 01/01/2008–04/30/2009 (released 2010). No audits since. Possibly dissolved. No web presence found.
  - Investigate: is this board still active? Does it own or manage any natural areas or parks in Bettsville?

- [ ] **Seneca County Soil and Water Conservation District** — SWCD; active (last audit 2024, FY 2022–2023)
  - Website: search for senecaswcd.org or similar
  - Check: does SCSWCD own demonstration areas, forest preserves, or nature education sites?

- [ ] **Seneca County Regional Planning Commission** — Regional Planning; active (last audit 2024, FY 2022–2023)
  - Check: does SCRPC manage any trails, greenways, or transportation corridors with recreation?

### Confirmed Nulls (Auditor pre-enumeration):
- Conservancy Districts: 0 records
- Water/Sewer/Sanitary Districts: 0 records

---

## Captured Source Data

### Ohio Auditor — Park/Recreation Districts, Seneca County (searched 2026-05-26)
```
Entity Name                   | County | Entity Type           | Last Period         | Released
Seneca County Park District   | Seneca | Park/Recreation Dist. | 01/01/2022–12/31/23 | 12/12/2024
Bettsville Recreation Board   | Seneca | Park/Recreation Dist. | 01/01/2008–04/30/09 | 04/08/2010
```

### Ohio Auditor — SWCD, Seneca County (searched 2026-05-26)
```
Entity Name                                      | County | Entity Type | Last Period         | Released
Seneca County Soil and Water Conservation Dist.  | Seneca | SWCD        | 01/01/2022–12/31/23 | 08/20/2024
```

### Ohio Auditor — Regional Planning, Seneca County (searched 2026-05-26)
```
Entity Name                              | County | Entity Type          | Last Period         | Released
Seneca County Regional Planning Comm.   | Seneca | Regional Planning    | 01/01/2022–12/31/23 | 07/23/2024
```

### OhioGenealogyExpress — Seneca County Cemetery List (fetched 2026-05-26)
Source: https://ohiogenealogyexpress.com/seneca/cemeteries.html
Total: 73 entries (2 duplicates noted: Reformed Cemetery × 2, Rock Creek Cemetery × 2)
```
1.  Adams Lutheran Cemetery
2.  Armstrong Cemetery
3.  Assumption Cemetery
4.  Attica Cemetery
5.  Bare Cemetery
6.  Baugher Cemetery
7.  Bethel Cemetery
8.  Big Spring Cemetery
9.  Block Cemetery
10. Bloom Township Cemetery          ← T5 staged (Bloom Township trustees)
11. Bloomville Cemetery
12. Brundedge Cemetery
13. Bunker Hill Cemetery
14. Caroline Lutheran Cemetery
15. Clay Cemetery
16. Coffman Cemetery
17. County Home Cemetery
18. Crissa Cemetery
19. Dunkard Cemetery
20. Dysinger Cemetery
21. East Baseline Baptist Cemetery
22. Egbert Cemetery
23. Fairmont Cemetery
24. Farewell Retreat Cemetery
25. Feaselburg Cemetery
26. Fireside Cemetery
27. Flat Rock Cemetery
28. Fravel Cemetery
29. French Town Cemetery
30. Greenlawn Cemetery              ← Private 501(c)(13); T8 staged
31. Hopewell Cemetery
32. Jerusalem Cemetery
33. Kagy Cemetery
34. Lay Cemetery
35. Liberty Cemetery
36. Loudon Township Cemetery        ← T5 staged (Loudon Township trustees)
37. Lowell Cemetery
38. McMeen Cemetery
39. Mennonite Cemetery
40. Methodist Cemetery
41. Null Cemetery
42. Omar Cemetery
43. Payne Cemetery
44. Pleasant Ridge Cemetery
45. Pleasant Union Cemetery
46. Pleasant View Cemetery
47. Randall Cemetery
48. Raymond Cemetery
49. Reformed Cemetery (×2)
50. Reisz Cemetery
51. Rock Creek Cemetery (×2)
52. Saint Andrews Cemetery
53. Saint Boniface Cemetery
54. Saint Jacobs Cemetery
55. Saint Josephs Cemetery
56. Saint Marys Cemetery
57. Saint Michaels Cemetery
58. Saint Patricks Cemetery
59. Saint Peters Cemetery
60. Saint Stephens Cemetery
61. Saints Peter and Paul Cemetery
62. Sand Ridge Cemetery
63. Scipio Township Cemetery
64. Seneca Memory Gardens
65. Sheller Cemetery
66. Shiloh Cemetery
67. Shock Cemetery
68. Swamp Cemetery
69. Thompson Center Cemetery
70. Underhill Cemetery
71. Union Cemetery
72. Woodlawn Cemetery
73. Zion Lutheran Cemetery
```
Cross-reference notes:
- T5 already staged: Bloom Township Cem, Loudon Township Cem, Zion Cem (Jackson Twp)*, Disinger Cem (Jackson Twp)*, Rock Run Cem (Eden Twp)*, Attica Venice Jt. Cem*, 5 Pleasant Twp cems*
  * Need to verify exact name match with OGE list entries
- Not in OGE list: Disinger Cemetery, Rock Run Cemetery — may be too small/private
- "Attica Cemetery" may = Attica-Venice Township Joint Cemetery (T5 staged)
- Known T8 private: Greenlawn Cemetery (private 501(c)(13))
- Known T8 private: Seneca Memory Gardens (private memorial park)
- Church cemeteries (T8): Adams Lutheran, Assumption, Bethel, Big Spring*, Bunker Hill*, Caroline Lutheran, Dunkard, East Baseline Baptist, Jerusalem, Mennonite, Methodist, Reformed, Saint Andrews, Saint Boniface, Saint Jacobs, Saint Josephs, Saint Marys, Saint Michaels, Saint Patricks, Saint Peters, Saint Stephens, Saints Peter Paul, Shiloh, Zion Lutheran
- Township-associated: Bloom Twp, Loudon Twp, Scipio Twp, Thompson Center, Liberty (T5?)
- Municipal-associated: Bloomville, Attica, Fairmont (Tiffin?), Woodlawn (Tiffin?)
- Family/private: Armstrong, Bare, Baugher, Block, Brundedge, Clay, Coffman, County Home, Crissa, Dysinger, Egbert, Farewell Retreat, Feaselburg, Fireside, Flat Rock, Fravel, French Town, Hopewell, Kagy, Lay, Lowell, McMeen, Null, Omar, Payne, Pleasant Ridge/Union/View (Pleasant Twp?), Randall, Raymond, Reisz, Rock Creek, Sand Ridge, Sheller, Shock, Swamp, Underhill, Union

### ODNR Nature Preserves Guide — Seneca County entries
```
Name                              | Address                              | Trails | Habitats
Howard Collier State NP           | 1655 W Township Rd 38, Tiffin 44883  | 1.2 mi | Woods, Wetlands, Spring Wildflowers
Springville Marsh State NP        | 12250 Township Rd 24, Carey 43316    | 0.8 mi | Wetlands, Bird Watching
```

### ODNR Wildlife Area PDFs — Seneca County
```
Name                         | Acres | Location                         | Habitat
Sugar Creek Wildlife Area    | 125   | TR 157 and TR 148                | Grassland, Brushland
Knobbys Prairie Wildlife Area| 47    | CR 15 at TR 148                  | (adjacent to Sugar Creek WA)
Silver Creek Wildlife Area   | 42    | TR 58 at TR 181/CR 6, Bloomville | Marshland, Grassland, Brushland
```

### Ohio Administrative Code 1501:31-15-04 — Seneca County hunting areas
```
Seneca county wildlife area 1
Seneca county wildlife area 2
Seneca county wildlife area 3
Seneca county wildlife area 4
(Sugar Creek, Knobbys Prairie, Silver Creek also listed separately by name)
```
