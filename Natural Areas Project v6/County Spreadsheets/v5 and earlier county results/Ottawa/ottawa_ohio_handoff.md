# Ottawa County, Ohio — Discovery Handoff
**RUN_ID:** `ottawa_ohio_2026_05_18`
**PREFIX:** `OTT`
**Schema:** Discovery Output Specification v5.3
**Status:** ✅ PIPELINE COMPLETE — BATCH RESOLUTION APPLIED 2026-06-10
**Last updated:** 2026-06-10

## Batch Resolution Summary — 2026-06-10
- AP-0006 (West Harbor Boat Launch) parent → OH-OTT-S-0003
- 9 trail parents added: T-0072–T-0076 → MC-S-0021; T-0126→S-0012; T-0127→S-0042; T-0128→S-0046; T-0129→S-0079
- S-0016 Honey Point WA acres updated to 8.0
- +5 supplemental sites: S-0134 SW Lake Erie Marshes (153ac TNC), S-0135 WPA 65 (31ac ODNR),
  S-0136 Port Clinton Waterfront (15ac), S-0137 Portage River FA (10ac), S-0138 Genoa Rec Complex (39ac)
- 13 QR gaps confirmed as neighboring county entities (Erie, Sandusky, Lucas, Wood) — not Ottawa gaps
  including Resthaven WA 2216ac → Erie County (major find for Erie run)
- Final: 138 OTT sites | 56 trail_parents | 9/9 APs parented
### Open Items
- T-0072–T-0076: verify trail names vs Howard Marsh Metropark
- WPA 44 (64ac, Erie Twp, Ottawa): investigate for next Ottawa pass
- S-0134 SW Lake Erie Marshes: confirm governance (TNC vs other NGO)
- Resthaven WA / Willow Point WA / Bayview West Marsh → flag for Erie County T2 run

---

## County Context

- **County seat:** Port Clinton
- **Major municipalities:** Port Clinton (city), Oak Harbor (village), Genoa (village), Elmore (village), Marblehead (village), Put-in-Bay (village)
- **Islands:** South Bass Island (Put-in-Bay), Middle Bass Island, North Bass Island (Isle Saint George), Kelleys Island (Erie County — NOT Ottawa)
- **Park district affiliation:** None identified; county may operate directly
- **Known cross-county entities (DB):** None — DB is empty at run start
- **Note:** Ottawa County is a Lake Erie county with significant island geography; several ODNR properties are on Lake Erie islands

---

## Townships (12 — from Townships_Officials2022-2023.xlsx)

| Township | County | Website |
|----------|--------|---------|
| Allen | Ottawa | allentownship.us |
| Bay | Ottawa | baytownship.com |
| Benton | Ottawa | Bentontownship.org |
| Carroll | Ottawa | (none listed) |
| Catawba Island | Ottawa | catawbaislandtownship.com |
| Clay | Ottawa | ClayTownshipOhio.net |
| Danbury | Ottawa | www.danburytownship.com |
| Erie | Ottawa | (none listed) |
| Harris | Ottawa | www.harristownshipohio.com |
| Portage | Ottawa | portagetownship.net |
| Put-In-Bay | Ottawa | pibtownship.com |
| Salem | Ottawa | (none listed) |

---

## Baseline Seeds (46 entries — internalized, not imported as raw records)

These must be confirmed through authoritative tier discovery.

| Seed Name | Type (baseline) | Notes |
|-----------|-----------------|-------|
| African Safari Wildlife Park | Private park | T8 candidate |
| Catawba Island State Park | State Park | T2 |
| Continental Marsh | GNIS Swamp | Verify if managed |
| Coopers Woods | GNIS Woods | Verify if managed |
| Darby Marsh | GNIS Swamp | Verify if managed |
| East Harbor State Park | State Park + Public Hunting | T2 |
| Eisenhour Marsh | GNIS Swamp | Verify if managed |
| Fox's Marsh Wildlife Area | State Wildlife Area + Hunting | T2; North Bass Island |
| France Marsh | GNIS Swamp | Verify if managed |
| Great Egret Marsh Nature Preserve | Nature Conservancy preserve | T7 |
| Green Island Wildlife Area | State Wildlife Area | T2 |
| Honey Point Wildlife Area | State Wildlife Area + Hunting | T2; North Bass Island |
| Hotel Victory Site at South Bass Island | ODNR Historic Site | T2; child of South Bass Island SP |
| Hunter Marsh | GNIS Swamp | Verify if managed |
| Kuehnle Wildlife Area | State Wildlife Area + Hunting | T2; Middle Bass Island |
| Lakeside Daisy State Nature Preserve | State Nature Preserve | T2; acreage discrepancy noted |
| Little Portage Wildlife Area | State Wildlife Area + Hunting | T2 |
| Lockwood (Marshall) Cemetery | ODNR Historic Site | T2; child of East Harbor SP |
| Lonz Winery at Middle Bass Island | ODNR Historic Site | T2; child of Middle Bass Island SP |
| Magee Marsh | GNIS Swamp | Likely also state wildlife area — verify |
| Marblehead Lighthouse | ODNR Historic Site | T2; child of Marblehead Lighthouse SP |
| Marblehead Lighthouse State Park | State Park | T2 |
| Mazurik Lake Erie Access Wildlife Area | State Wildlife Area | T2; 8957 North Shore Blvd |
| Middle Bass Island State Park | State Park | T2 |
| Navarre Marsh | GNIS Swamp | Verify if managed |
| Navarre Marsh National Wildlife Refuge | National Wildlife Refuge | T1 — verify; may be Ottawa NWR unit |
| Needles Eye | GNIS Arch | Likely not a managed entity |
| North Bass Island | State Park + Public Hunting | T2; aka Isle Saint George |
| Oak Point State Park | State Park | T2; on South Bass Island |
| Ottawa County Wildlife Area 1 | Public Hunting Area | T2; 551 S Wonnell Rd, Port Clinton |
| Ottawa County Wildlife Area 2 | Public Hunting Area | T2 |
| Ottawa National Wildlife Refuge - West Harbor Landing | NWR unit | T1; 231 N Hickory Ridge Dr, Port Clinton |
| Port Clinton Pier | Unknown | Verify type and manager |
| Put-In-Bay City Park | Municipal park | T6 |
| Put-In-Bay Fish Hatchery | Unknown | Verify manager |
| Ritter Marsh | GNIS Swamp | Verify if managed |
| Sand Beach Marsh | GNIS Swamp | Verify if managed |
| Schedel Arboretum & Gardens | Unknown | In Elmore; verify ownership |
| South Bass Island State Park | State Park | T2 |
| Starve Island Deep | GNIS Prairie | Verify if managed |
| Toussaint Creek Wildlife Area | State Wildlife Area + Hunting | T2 |
| Toussaint Marsh | GNIS Swamp | Verify if managed |
| Turtle Creek Access | Unknown | Verify type and manager |
| Walter Ory Park | Municipal park | T6; Elmore |
| West Harbor Wildlife Area | State Wildlife Area | T2 |
| Winous Point Marsh | GNIS Swamp | Verify if managed; may be private |

---

## Tiers Completed

| Tier | Source | Entity Records | Total Records (incl. metadata) | Date |
|------|--------|---------------|-------------------------------|------|
| T1 | Federal (USFWS, NPS, USACE) | 30 | 32 | 2026-05-18 |
| T2 | State (ODNR Parks, Wildlife, DNAP) | 46 | 59 | 2026-05-18 |
| T3 | District (PIBTPD, PDOC, Toledo Metroparks) | 15 | 19 | 2026-05-18 |
| T4 | County (Ottawa County, PDOC direct) | 4* | 11 | 2026-05-18 |
| T5 | Township (all 12 Ottawa County townships) | 35+1‡ | 47 | 2026-05-18 |
| T6 | Municipal (8 municipalities) | 29 | 62 | 2026-05-18 |
| T7 | Land Trust / Conservancy (BSC, TNC, WRLC) | 12** | 17† | 2026-05-19 |
| T8 | Private (safari, golf, hunting, church/private cemeteries) | 27‡‡ | 33†† | 2026-05-19 |

*T4 entity count (4) excludes 5 T1-miss NWR units (discovery_tier=1) that were discovered during T4. Those 5 units are counted in T1 (bringing T1 sites to 10 total).
**T7 entity records (12): 6 T7-native (4 Sites, 1 Trail, 1 Access Point) + 6 cross-tier finds staged during T7 investigation (1 T6 miss: Port Clinton Lakefront Preserve; 5 T3 misses: West Harbor Preserve, Costello Tract, Schneider Tract, Lawrence Evans Property, Prokesh Property).
†T7 total records (17): 12 entity + 5 null/evidence blocks (Trail Segment, Trail Network, Site Network, LEIC [advisory-only], ONAPA [no nonprofit directory]).
‡‡T8 entity records (27): 20 T8-native Sites + 7 cross-tier finds (2 T2 misses: Lockwood Cemetery, Aquatic Visitors Center; 5 T5 misses: Old Elliston, Hartshorn, Jamison, Kelly, Rymers/Rice cemeteries).
††T8 total records (33): 27 entity + 5 entity-type null blocks (Trail, Trail Segment, Trail Network, Site Network, Access Point) + 1 tier-level null block. Grand total in YAML: 287. IMP-080 verified 2026-05-19.

**Cumulative totals:** 199 entity records · 287 total records

---

## Tiers Remaining

*(None — all stages complete. Ready for Stage 6 Database Upsert.)*

---

## Pipeline Status

| Stage | Name | Status | Output |
|-------|------|--------|--------|
| 1a | Resolution Engine Pass 1 | ✅ COMPLETE | `ottawa_ohio_resolved.json` (198 entities, 6 held) |
| 2 | GPS Acquisition | ✅ COMPLETE | All non-held entities have GPS or `gps_unresolvable` flag |
| 2b | GPS Fix (supplements) | ✅ COMPLETE | 51 trails flagged unresolvable; 7 sites + 4 APs manually preseeded |
| 2c | Category Patch | ✅ COMPLETE | All 134 sites assigned `category_raw` via name/governance inference |
| 3 | Normalization Engine | ✅ COMPLETE | `ottawa_ohio_normalized.json` — 192 normalized, 0 rejected, 0 errors |
| 4 | TSV Output | ✅ COMPLETE | 4 TSV files: 134 sites, 51 trails, 6 APs, 1 site network (192 rows) |
| 4.5 | TSV Integrity Check | ✅ PASS | 192/192 rows pass — 0 errors |
| 4.6 | Cross-County Pass | ✅ COMPLETE | 7 MC entities — 4 trails, 1 site network, 2 APs (see registry below) |
| 4.7 | Post-CC Integrity Check | ✅ PASS | 199/199 rows pass — 0 errors |
| 5 | Human Review Gate | ✅ **APPROVED** | All 5 review items confirmed by user |
| 6 | Database Upsert | ✅ COMPLETE | `natural_areas_v5.db` — run `ottawa_ohio_2026_05_18` — 199 entities, 0 held |

### Stage 5 Human Review — Decisions Recorded

1. **OH-OTT-AP-006 → Reclassified as Site**: West Harbor Boat Launch has no parent trail/site; reclassified as Water Site / Boat Launch Area. Confirmed by user.
2. **6 held entities → Cross-county pass executed** (Stage 4.6): All 7 entities resolved and added to TSVs. Confirmed by user.
3. **Vocabulary warnings (non-fatal)**: No action required. Confirmed by user.
4. **SN-002 network_type = "Park District"**: Accepted. Confirmed by user.
5. **DeRivera Park split governance**: Accepted as documented. Confirmed by user.

---

## Cross-County Registry (Stage 4.6 — 2026-05-20)

| Original ID | Final ID | Entity Name | Type | Counties | Resolution Rule | Notes |
|-------------|----------|-------------|------|----------|-----------------|-------|
| OH-OTT-T-084 | OH-MC-T-0109 | Metzger Marsh Trail | Trail | Lucas;Ottawa | Condition B (USFWS; no county anchor) | Co-managed with Ohio Division of Wildlife |
| OH-OTT-T-125 | OH-MC-T-0110 | North Coast Inland Trail | Trail | Erie;Huron;Ottawa;Sandusky | Condition B (multi-county rail trail) | PDOC manages Ottawa County segment; US Bike Route 30 |
| OH-OTT-T-124 | OH-OTT-T-124 | Lake Erie Islands Water Trail | Trail | Ottawa (provisional) | Scenario A (Ottawa-only counties_raw; Erie not yet run) | ID provisional; Erie County must add Erie when processed |
| (pre-existing) | OH-MC-TR-002 | Portage River Water Trail | Trail | Ottawa;Wood | Pre-existing MC ID; Ottawa first to pipeline | 36-mi state water trail designated 2022-07-19; TMACOG governance |
| OH-OTT-SN-001 | OH-MC-SN-0002 | Ottawa National Wildlife Refuge Complex | Site Network | Lucas;Ottawa | Condition B (USFWS; no county anchor) | Ohio members: Ottawa NWR, Cedar Point NWR, West Sister Island NWR |
| OH-OTT-AP-007 | OH-OTT-AP-007 | Oak Harbor Station Interurban Overlook and Hand Powered Boat Launch | Access Point | Ottawa | Unblocked — parent OH-MC-TR-002 confirmed | Parent trail: Portage River Water Trail |
| OH-OTT-AP-008 | OH-OTT-AP-008 | Lake Erie Islands Water Trail — Access Point 9 (Lucien M. Clemons Park) | Access Point | Ottawa | Unblocked — parent OH-OTT-T-124 confirmed | Parent trail: Lake Erie Islands Water Trail (LEIT) |

**MC ID Sequence Updates:**
- OH-MC-T-*: previous max 0108 → assigned 0109, 0110 → next available: 0111
- OH-MC-SN-*: previous max 0001 → assigned 0002 → next available: 0003
- OH-MC-TR-002: pre-existing; no sequence update required

**Final TSV counts after cross-county pass:**

| File | Rows |
|------|------|
| ottawa_sites.tsv | 134 |
| ottawa_trails.tsv | 55 (51 Ottawa + 4 MC) |
| ottawa_access_points.tsv | 8 (6 Ottawa + 2 unblocked) |
| ottawa_site_networks.tsv | 2 (1 Ottawa + 1 MC) |
| **TOTAL** | **199** |

---

## Key Active Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| T5-FLAG-1 | John Braun Park (2370 NE Catawba Rd) | ~~Not CIT-managed; governance unclear~~ **RESOLVED T6 pass: T8 private/independent Board of Directors. Not municipal.** | ✅ CLOSED |
| T5-FLAG-2 | Nehl's Memorial Nature Preserve (4400 E. Muggy Rd) | ✅ RESOLVED T7: BSC fee-simple 40 ac, purchased 2019. Staged as "Dr. Robert L. Nehls Memorial Nature Preserve" (T7 Site) + Nehls ADA Kayak Launch (T7 Access Point). | ✅ CLOSED |
| T5-FLAG-3 | Three PDOC parks on NW Catawba Rd (3648, 3655, 133 W Catawba) | Announced on CIT Additional Parks page but not yet open | T3 (PDOC) — stage when open |
| T5-FLAG-4 | Black Swamp Conservancy park, NW Catawba Rd | ✅ RESOLVED T7: West Harbor Preserve — BSC purchased via Clean Ohio Conservation Fund, donated to PDOC; PLANNED/not yet open. Staged as T3 Site (PDOC ownership, discovery_tier=3). | ✅ CLOSED |
| T5-FLAG-5 | Oak Harbor Union Cemetery (Salem Township) | ~~May be municipal (T6)~~ **RESOLVED T6 pass: confirmed Salem Township entity (11565 SR-105, west of Oak Harbor limits). Staged as T5.** | ✅ CLOSED |
| T5-FLAG-6 | Catawba Island Township cemeteries governance | K'burg Cemetery governance inferred from OHGenWeb only; township site did not list it | Confirm at normalization |
| T6-FLAG-1 | DeRivera Park (Put-in-Bay) | Split governance: 4/5 managed by DeRivera Park Trustees (private charitable trust), 1/5 by Village. Baseline seed 'Put-In-Bay City Park' resolved here. | Resolution pass — determine canonical tier (T6 village vs T8 trust) |

---

## Entities Discovered

**199 entity records staged across T1–T8 (IDs to be assigned at resolution pass)**

| Entity Type | T1 | T2 | T3† | T4 | T5+‡ | T6§ | T7 | T8 | Total |
|-------------|----|----|-----|----|------|-----|----|----|-------|
| Site | 10* | 22 | 12 | 1 | 38 | 27 | 4 | 20 | 134 |
| Trail | 17 | 24 | 8 | 1 | 2 | 1 | 1 | — | 54 |
| Trail Segment | — | — | — | — | — | — | — | — | 0 |
| Trail Network | — | — | — | — | — | — | — | — | 0 |
| Site Network | 1 | — | — | 1 | — | — | — | — | 2 |
| Access Point | 2 | 2 | — | 1 | 1 | 2 | 1 | — | 9 |
| **Total** | **30** | **48** | **20** | **4** | **41** | **30** | **6** | **20** | **199** |

*T1 site count (10) includes 5 T1-miss NWR units (Marinewood, Turkey Run, Turtle Creek Island, Upper Toussaint, Little Portage) discovered during T4 but assigned `discovery_tier: 1`.
†T3 count updated from 15 → 20: 5 T3-miss PiBTPD records discovered during T7 investigation (West Harbor Preserve [PDOC], Costello Tract, Schneider Tract, Lawrence Evans Property, Prokesh Property [all PiBTPD]).
‡T5+ = 35 original T5 records + 1 T5-deferred (Oak Harbor Union Cemetery, staged during T6 pass) + 5 T5-miss cemeteries discovered during T8 GNIS enumeration (Old Elliston, Hartshorn, Jamison, Kelly, Rymers/Rice) = 41 total.
§T6 count updated from 29 → 30: Port Clinton Lakefront Preserve (T6 miss) discovered during T7 investigation, staged with discovery_tier=6.
¶T2 count updated from 46 → 48: Lockwood (Marshall) Cemetery (within East Harbor SP, ODNR Historic Site #37) + Aquatic Visitors Center (former Put-In-Bay Fish Hatchery, ODNR Division of Wildlife) discovered during T8 investigation, staged with discovery_tier=2.
T8 count (20): African Safari Wildlife Park, John Braun Park, Schedel Arboretum & Gardens, The Islander GCC, Catawba Island Club, Oak Harbor Golf Club, Bay Point Golf Club, Saunders Golf Course, Oak Harbor Conservation Club, Dr. L.J. Darr Memorial Wetlands, Lake Erie Club, Toussaint Shooting Club, and 8 church/family/private cemeteries (St. Joseph's-Carroll, Russian Orthodox, St. Joseph's-Danbury, St. Mary's Byzantine, St. Paul's Lutheran, Tynan, War of 1812, Guss).

### Key T1 entities
Ottawa NWR (main complex + visitor complex + 7 NWR unit sites), 16 NWR trails, Ottawa NWR Complex (Site Network), Perry's Victory NM, Confederate Stockade Cemetery, 2 NWR access points.

### Key T2 entities
20 ODNR sites (9 state parks, 7 wildlife areas, 2 state nature preserves, 1 fishing access, 1 recreation area), 24 trails (11 East Harbor SP, 7 Magee Marsh, 4 Middle Bass SP, plus Marblehead ADA path, Lakeside Daisy, Stone Lab), 2 access points.

### Key T3 entities
7 PIBTPD preserves (South Bass + Middle Bass islands), 6 PIBTPD trails, Lake Erie Islands Water Trail (CROSS_COUNTY_CANDIDATE), North Coast Inland Trail (CROSS_COUNTY_CANDIDATE).

### Key T4 entities
Park District of Ottawa County (Site Network), Ottawa County Home Cemetery, Catawba Islander Trail (PLANNED), Ottawa County Fairgrounds PRWT Launch (Access Point).

---

## Held Entities

*(None yet)*

---

## Unresolved Baseline Seeds

Seeds resolved through T1–T4 discovery. Resolution pass will match staged records to baseline seeds and assign IDs. Key confirmations:

- **Ottawa NWR** → staged T1 (main complex + 5 NWR units + 5 T1-miss units)
- **East Harbor SP, South Bass Island SP, Middle Bass Island SP, Marblehead Lighthouse SP, Catawba Island SP, Oak Point SP, North Bass Island SP** → staged T2
- **Toussaint Creek WA, Little Portage WA, Fox's Marsh WA, Honey Point WA, Kuehnle WA, Green Island WA, West Harbor WA, Mazurik Access, Little Portage WA** → staged T2
- **Lakeside Daisy SNP** → staged T2
- **Perry's Victory NM** → staged T1
- **Magee Marsh** → KNOWN_MC:OH-MC-S-010 (confirmed T2)
- **Hotel Victory Site, Lonz Winery, Lockwood Cemetery, Marblehead Lighthouse** → staged T2 as child sites
- **Ottawa County Wildlife Area 1 & 2** → need confirmation at resolution/normalization (not yet found under PDOC; may be county/township)
- **Put-In-Bay City Park** → T6 (staged as DeRivera Park, split governance — see T6-FLAG-1) ✅
- **Walter Ory Park** → T6 (Village of Elmore-managed, staged T6) ✅
- **Schedel Arboretum** → ✅ staged T8 (Schedel Foundation 501c3, 17 ac, Harris Twp)
- **African Safari Wildlife Park** → ✅ staged T8 (private, 100+ ac, Port Clinton)
- **Put-In-Bay Fish Hatchery** (baseline seed) → ✅ resolved: ODNR Aquatic Visitors Center, 360 W Shore Blvd PIB; staged T2 miss (discovery_tier=2)
- **Great Egret Marsh NP** → ✅ staged T7 (TNC fee-simple, 150+ ac, Great Egret Marsh Preserve + 1.2-mi loop Trail)
- **GNIS swamp/marsh entries** (Continental, Coopers Woods, Darby, Eisenhour, France, Hunter, Navarre, Ritter, Sand Beach, Starve Island Deep, Toussaint, Winous Point) → need GIS/GNIS verification; most expected to be non-entity (unmanaged natural features)

---

## Open Questions

1. Is "Navarre Marsh National Wildlife Refuge" a standalone NWR or a unit of Ottawa NWR? Confirm at T1.
2. What is the Ottawa County park district structure, if any? Does the county operate a formal park district? Confirm at T4.
3. Magee Marsh — GNIS shows "Swamp" type, but Magee Marsh Wildlife Area is well-known ODNR property. Confirm at T2.
4. Turtle Creek Access — unknown manager and type. Verify at T2/T4.
5. Put-In-Bay Fish Hatchery — verify manager (ODNR? Federal? Other?).
6. Winous Point Marsh — verify if publicly managed or private hunting club.
7. Schedel Arboretum & Gardens — verify ownership and public access status.
8. Great Egret Marsh Nature Preserve — The Nature Conservancy; verify if publicly accessible.

---

## Next Steps

1. **Resolution pass** — assign OTT-S-xxx / OTT-T-xxx IDs to all 199 entity records; match to baseline seeds; resolve COUNTY_UNCERTAIN (Q31 Turkey Run, Q32 Upper Toussaint), DeRivera Park governance (T6-FLAG-1), ambiguous GNIS cemeteries (Oakland, Veterans Memorial, St. George, Middle Bass / La Fleur)
2. **Normalization pass** — populate entity JSON from staged raw records; validate required fields
3. **GPS acquisition pass** — coordinate acquisition for all records with blank gps_lat/gps_lon; priority: Q37 Ottawa County Fairgrounds PRWT Launch (address discrepancy), Toussaint Shooting Club (no address)
4. **Cross-county verification** — CROSS-1 (Lake Erie Islands Water Trail, CROSS_COUNTY_CANDIDATE) + CROSS-2 (North Coast Inland Trail, CROSS_COUNTY_CANDIDATE); coordinate with Erie/Huron/Sandusky county runs
5. **Open flags to resolve** — key: Q31/Q32 (COUNTY_UNCERTAIN NWR units via GIS), Q35/Q36/Q37, T6-FLAG-1 (DeRivera Park canonical tier)

---

## Pre-Discovery Checklist

### T1 — Federal ✅ COMPLETE
- [x] Ottawa National Wildlife Refuge (main complex + 7 satellite units + 5 T1-miss units)
- [x] Perry's Victory and International Peace Memorial (NPS)
- [x] Confederate Stockade Cemetery (historic site within Perry's Victory)
- [x] USACE — Lake Erie harbors/access (no USACE entities found in Ottawa County)
- [x] BLM — no presence in Ottawa County confirmed

### T2 — State ✅ COMPLETE
- [x] ODNR Parks & Watercraft — 9 state parks staged
- [x] ODNR Wildlife — 7 wildlife areas staged
- [x] ODNR DNAP — 2 state nature preserves staged
- [x] ODNR Forestry — no state forests in Ottawa County
- [x] ODNR Coastal — public access guide reviewed (PAG-LE-02)
- [x] Magee Marsh — confirmed KNOWN_MC:OH-MC-S-010; 7 Magee trails staged

### T3 — District ✅ COMPLETE
- [x] Put-in-Bay Township Park District — 7 sites, 6 trails staged
- [x] Park District of Ottawa County — Lake Erie Islands Water Trail, North Coast Inland Trail staged
- [x] Toledo Metroparks (Howard Marsh) — confirmed KNOWN_MC:OH-MC-S-021
- [x] Portage River Water Trail — confirmed KNOWN_MC:OH-MC-TR-002
- [x] Ottawa County SWCD — NULL (no land holdings)
- [x] Sand Beach Conservancy District — NULL (no recreational land)

### T4 — County ✅ COMPLETE
- [x] Park District of Ottawa County — staged as Site Network
- [x] Ottawa County Home Cemetery — staged (mandatory per IMP-099 §4.9)
- [x] Catawba Islander Trail — staged (PLANNED)
- [x] Ottawa County Fairgrounds PRWT Launch — staged as Access Point
- [x] 5 T1-miss NWR units — staged with discovery_tier=1
- [x] NRHP Ottawa County check — NULL
- [x] Golf course check — NULL

### T5 — Township ✅ COMPLETE
All 12 townships searched. Parks and §5.6 cemeteries staged.
- [x] Allen Township — allentownship.us — parks: null; cemeteries: 2
- [x] Bay Township — baytownship.com — parks: null; cemeteries: 2
- [x] Benton Township — Bentontownship.org — parks: 1 (Graytown Park); cemeteries: 2
- [x] Carroll Township — carrolltownship.net (returned empty) — parks: null; cemeteries: 2
- [x] Catawba Island Township — catawbaislandtownship.com — parks: 3 sites + 1 trail + 1 AP; cemeteries: 2
- [x] Clay Township — ClayTownshipOhio.net — parks: null; cemeteries: 1
- [x] Danbury Township — danburytownship.com — parks: 4 sites + 1 trail; cemeteries: 2
- [x] Erie Township — (no website) — parks: null; cemeteries: 1
- [x] Harris Township — harristownshipohio.com — parks: null; cemeteries: 2
- [x] Portage Township — portagetownship.net — parks: null; cemeteries: 3
- [x] Put-In-Bay Township — pibtownship.com — parks: null (PIBTPD at T3); cemeteries: 4
- [x] Salem Township — (no website) — parks: null; cemeteries: 1

### T8 — Private / Organization-Based ✅ COMPLETE (2026-05-19)
Source: na_private_discovery_subproc_v5.7.md

**IMP-111 GNIS Cemetery Baseline:** ohiogenealogyexpress.com/ottawa/ottawaoh_cems.htm + ottawa.ohgenweb.org/places/cemeteries.htm (both fetched 2026-05-19). Full list in Captured Source Data. Cross-reference table in T8 GNIS Cemetery Baseline section.

**IMP-029 Pre-Discovery Entity Checklist (complete enumeration before individual page fetches):**

T8-Native Sites:
1. African Safari Wildlife Park — 267 S. Lightner Rd, Port Clinton; 100+ ac; drive-through safari + walk-through; private
2. John Braun Park — 2280 NE Catawba Rd, Catawba Island Twp; 12 ac; independent Board of Directors (Resurrection Lutheran affiliation history); T5-FLAG-1 resolved
3. Schedel Arboretum & Gardens — 19255 W Portage River S Rd, Elmore; 17 ac; operated by Joseph J. & Marie P. Schedel Foundation (501c3); Harris Township

Golf Courses — IMP-110 (all in scope regardless of access):
4. The Islander Golf & Country Club — 2590 Sand Rd, Port Clinton; 18 holes; public; fmr Catawba Willow Golf & Country Club; built 1970
5. Catawba Island Club — 4235 E Beachclub Rd, Port Clinton; 9-hole private/members club; historic (dates to 1920s)
6. Oak Harbor Golf Club — Oak Harbor; 18 holes; public; fmr Portage Point Golf Club; built 1964
7. Bay Point Golf Club — 10948 E Bay Shore Rd, Marblehead; 9 holes; public
8. Saunders Golf Course — 1495 Catawba Ave, Put-In-Bay; 9 holes Par 3; public; built 1954

Hunting Preserves — OBS-030 (fee/public access):
9. Oak Harbor Conservation Club — 975 South Gordon Rd, Oak Harbor; 397 ac; pheasant/quail/chukar hunting
10. Lake Erie Club — 3225 Lake Shore Dr, Port Clinton; 125 ac; pheasant hunting

Church Cemeteries — IMP-099/IMP-111:
11. St. Joseph's (Toussaint) Catholic Cemetery — Carroll Twp.; Co. Rd. 24 at Twp. Rd. 62
12. Russian Orthodox Cemetery — Danbury Twp.; south of 1100 Blk. West Main, Marblehead
13. St. Joseph's Catholic Cemetery — Danbury Twp.; south of 1100 Blk. West Main, Marblehead (distinct from Carroll Twp. entry)
14. St. Mary's Byzantine Catholic Cemetery — Danbury Twp.; 500 Blk. East Main St., Marblehead
15. St. Paul's Lutheran Church Cemetery — Danbury Twp.; SR 163 approx. 7 mi E of Port Clinton, then 0.5 mi S on Church Rd.

Family/Private Cemeteries — IMP-099/IMP-111:
16. Tynan Cemetery — Portage Twp.
17. War of 1812 Cemetery — Danbury Twp.; adjacent to Wolcott House on Bayshore Rd; governance TBD
18. Guss Cemetery — Harris/Elmore area (GNIS OhioGenealogyExpress only; not in OHGenWeb); governance TBD

Cross-tier Finds (T5 misses discovered during T8 GNIS enumeration):
19. Old Elliston Cemetery — Benton Twp.; Section 29, south of Toussaint North Road
20. Hartshorn Cemetery — Danbury Twp.; exact location TBD
21. Jamison Cemetery — Danbury Twp.; exact location TBD
22. Kelly Cemetery — Danbury Twp.; exact location TBD
23. Rymers (Rice) Cemetery — Harris Twp.; Section 18, S. side of SR 105 just east of Elmore Village

Cross-tier Finds (T2 misses discovered during T8 cemetery enumeration):
24. Lockwood (Marshall) Cemetery — within East Harbor SP; ODNR Historic Site #37; child of East Harbor SP
25. Aquatic Visitors Center (former Put-in-Bay Fish Hatchery) — 360 West Shore Blvd, Put-in-Bay; ODNR-operated; est. 1907; converted to educational center 1992; $6.2M renovation

Documented Nulls — Not staged separately:
- Perry Monument Interments — within Perry's Victory NM rotunda (T1); not a separate entity
- Ottawa County Infirmary Cemetery — STAGED T4 as "Ottawa County Home Cemetery" ✓
- Isle of St. George Cemetery — STAGED T5 as "North Bass Cemetery" ✓
- Middle Bass Island Cemetery — STAGED T5 as "La Fleur Cemetery" ✓
- Old Elmore Cemetery — STAGED T5 as "Harrington Cemetery" ✓
- DeRivera Park Trust (4/5 governance) — flagged T6-FLAG-1; evaluate at resolution pass

### T7 — Land Trust / Conservancy ✅ COMPLETE (2026-05-19)

**Organizations enumerated and checked (IMP-029 pre-discovery list):**

| Organization | Website | Ottawa County Holdings | Notes |
|---|---|---|---|
| Black Swamp Conservancy | blackswamp.org | Dr. Robert L. Nehls Memorial NP (40ac, fee-simple); Quinstock Woods Preserve (19ac, fee-simple); West Harbor Preserve (12ac, donated to PDOC); conservation easement on Meadowbrook Marsh (T5, already staged) | BSC also facilitated OTT NWR Turkey Run Unit transfer (T1) and held Port Clinton Lakefront Preserve easement (T6 miss) |
| The Nature Conservancy (Ohio) | nature.org/ohio | Great Egret Marsh Preserve (150+ ac, fee-simple, Catawba Island) | Only open Ottawa County TNC preserve |
| Lake Erie Islands Conservancy | lakeerieislandsconservancy.org | Advisory/fundraising council for PiBTPD — NO fee-simple land or easements in LEIC's name | All LEIC-funded properties are PiBTPD-owned (T3) |
| Western Reserve Land Conservancy | wrlandconservancy.org | Bay Point Sandbar (68 ac, fee-simple, Marblehead Peninsula); conservation easement on Lucien M. Clemons Park (T6, already staged) | WRLC also facilitated acquisition of port Clinton Lakefront Preserve (T6 miss) |
| ONAPA | onapa.org | No Ottawa County preserves — ONAPA "preserve map" links to ODNR SNP finder only | ONAPA mandatory check complete |

**Pre-Discovery Entity Inventory (enumerated before individual page fetches):**
1. Dr. Robert L. Nehls Memorial Nature Preserve (BSC, fee-simple, 40 ac, Catawba Island Twp)
2. Quinstock Woods Preserve (BSC, fee-simple, 19 ac, Catawba Island Twp, closed)
3. West Harbor Preserve (donated by BSC to PDOC, 12 ac, Catawba Island Twp, PLANNED)
4. Great Egret Marsh Preserve (TNC, fee-simple, 150+ ac, Catawba Island area)
5. Bay Point Sandbar (WRLC, fee-simple, 68 ac, Marblehead Peninsula/Sandusky Bay)
6. Great Egret Marsh Preserve Loop Trail (TNC, 1.2 mi, public)
7. Nehls Memorial Preserve ADA Kayak Launch — Access Point (BSC)

**Cross-tier entities confirmed during T7:**
- Port Clinton Lakefront Preserve — T6 miss (14.7 ac, City of Port Clinton-owned, BSC easement)
- West Harbor Preserve — resolves T5-FLAG-4; PDOC-owned (donated by BSC); PLANNED
- PiBTPD Costello Tract (3.937 ac, Middle Bass Island) — T3 miss
- PiBTPD Schneider Tract (7.33 ac, Middle Bass Island) — T3 miss
- PiBTPD Lawrence Evans Property (0.75 ac, Middle Bass Island) — T3 miss
- PiBTPD Prokesh Property (1 ac, Middle Bass Island, Burgundy Bay) — T3 miss

### T6 — Municipal ✅ COMPLETE (2026-05-18)
**8 incorporated municipalities: 1 city, 7 villages** (IMP-029 pre-enumeration — 2026-05-18)
Sources: citydirectory.us/county-ottawa-ohio.html; Ohio 2020 Census; ocogs.org/towns-places/

Lakeside-Marblehead is a census-designated place (gated Chautauqua community), NOT an incorporated municipality — excluded from T6 scope.
Unincorporated communities (Elliston, Lacarne, Williston, Gypsum, Curtice, Danbury, etc.) are NOT incorporated municipalities — excluded from T6 scope.

**Baseline seeds resolved:**
- **Put-In-Bay City Park** → DeRivera Park (341 Bayview Ave, PIB; split governance 4/5 trust + 1/5 village) ✅
- **Walter Ory Park (Elmore)** → confirmed Village of Elmore-managed ✅
- **Oak Harbor Union Cemetery** (T5-FLAG-5) → confirmed Salem Township T5, not T6 municipal ✅ RESOLVED
- **Port Clinton Pier** → resolved as Waterworks Park public dock/fishing pier (park amenity, not standalone AP) ✅

**T5-FLAG-1 resolved:** John Braun Park (2370 NE Catawba Rd) is private/independent Board of Directors — T8, not T6.

| Municipality | Type | Pop. (2020) | Official URL | Entity Records | Status |
|---|---|---|---|---|---|
| Port Clinton | City | 5,994 | portclinton.com | 9 (7 parks + 2 cemeteries) | ✅ COMPLETE |
| Oak Harbor | Village | 2,809 | oakharbor.oh.us | 5 (3 parks + 1 trail + 1 AP) | ✅ COMPLETE |
| Genoa | Village | 2,218 | genoaohio.org | 2 (Veterans Memorial Park + Genoa Quarry child) | ✅ COMPLETE |
| Elmore | Village | 1,378 | villageofelmoreohio.com | 6 parks | ✅ COMPLETE |
| Marblehead | Village | 844 | marbleheadohio.org | 5 (3 parks + 1 cemetery + 1 AP) | ✅ COMPLETE |
| Rocky Ridge | Village | 312 | none found | 0 — null confirmed (map verified) | ✅ COMPLETE |
| Clay Center | Village | 258 | none | 1 park (~7 acres) | ✅ COMPLETE |
| Put-in-Bay | Village | 150 | villageofpib.com | 1 (DeRivera Park — split governance) | ✅ COMPLETE |
| Rocky Ridge | Village | 310 | (TBC) | ⬜ PENDING |
| Clay Center | Village | 258 | (TBC) | ⬜ PENDING |
| Put-in-Bay | Village | 150 | putinbayvillage.com (TBC) | ⬜ PENDING |

---

## Captured Source Data

*(Populated at fetch time — verbatim tables from authoritative sources)*

### T6 Port Clinton — City Parks
Source: https://www.portclinton.com/services__/parks.php (fetched 2026-05-18)
Source: individual park detail pages at https://www.portclinton.com/business_detail_T30_R22-28.php

| Park Name | Address | Notes |
|---|---|---|
| Waterworks Park | W. State Rte. 163, Port Clinton, OH 43452 | Lake Erie shoreline; Port Clinton Lighthouse (separate org); fishing pier; public dock; walking trails |
| Friendship Park | 113 E. Perry St., Port Clinton, OH 43452 | Public art/community gathering space |
| Lakeview Park | 1100 E. Perry St., Port Clinton, OH 43452 | Lake Erie shoreline; beach access; Flagship Collaborative Play Place |
| Mosie Nesbit Johnson Community Garden | 323 Beech St., Port Clinton, OH 43452 | Former First Baptist Church site; civil rights history; 25 raised beds |
| Portage Park | 1142 Taft St., Port Clinton, OH 43452 | Youth sports fields; sledding hill |
| Veterans Park | W. Second St., Port Clinton, OH 43452 | WWII memorial; M5 anti-tank gun; M-42 Duster tank; Eternal Flame |
| West End Community Park | 431 Portage Dr., Port Clinton, OH 43452 | Basketball; playground; picnic |

### T6 Port Clinton — Cemeteries (IMP-099)
Source: https://www.portclinton.com/services__/cemetery.php (fetched 2026-05-18)

| Cemetery Name | Notes |
|---|---|
| Lakeview Cemetery | City-managed; database at cemeteryregister.com/search.asp?id=OH_PORTCLINTONLV |
| Riverview Cemetery | City-managed; database at cemeteryregister.com/search.asp?id=OH_PORTCLINTONRV |

---

## Captured Source Data (continued)

### T6 Oak Harbor — Parks
Source: https://www.oakharbor.oh.us/departments/public_works/parks.php (fetched 2026-05-18)

| Park Name | Address | GPS Lat | GPS Lon |
|---|---|---|---|
| Veterans Memorial Park | 300 Finke Road, Oak Harbor OH 43449 | 41.5094073 | -83.1354067 |
| Adolphus Kraemer Park | 125 N. Church Street, Oak Harbor OH 43449 | — | — |
| Flat Iron Park | Water, Main & Toussaint Sts, Oak Harbor OH 43449 | — | — |
| Oak Harbor Station Interurban Overlook & Hand Powered Boat Launch | S. end of Church St, Portage River, Oak Harbor OH 43449 | — | — |

### T6 Genoa — Parks
Source: https://genoaohio.org/village-departments/veterans-park-quarry/ (fetched 2026-05-18)

| Park Name | Address | GPS Lat | GPS Lon |
|---|---|---|---|
| Veterans' Memorial Park | Washington Street (Unnamed Rd), Genoa OH 43430 | 41.518595 | -83.3549743 |
| Genoa Quarry | Within Veterans' Memorial Park, Genoa OH 43430 | — | — |

### T6 Elmore — Parks
Source: https://villageofelmoreohio.wordpress.com/tag/walter-ory-park/ (fetched 2026-05-18)
Note: village.elmore.oh.us domain returned errors; WordPress blog used as secondary authoritative source.

| Park Name | Address | Notes |
|---|---|---|
| Walter Ory Park | Rice & Ottawa St (358 Harris St), Elmore OH 43416 | NCIT access; baseline seed confirmed |
| Depot Park | Ottawa Street, Elmore OH 43416 | NCIT nearby; Historical Society barn |
| Riverbend Park | 751 E. Rice Street, Elmore OH 43416 | Portage River |
| Veterans Park | Elmore OH 43416 | Smallest park; memorial post, flags |
| Well Park | Behind Woodmore High School, Elmore OH 43416 | 3 baseball diamonds |
| Witty Park (Harry Witty Park) | Main entrance, Portage River, Elmore OH 43416 | Gazebo, picnic |

### T6 Marblehead — Parks & Cemetery
Source: https://www.marbleheadohio.org/parks (fetched 2026-05-18)

| Park/Site Name | Address | GPS Lat | GPS Lon | Notes |
|---|---|---|---|---|
| James Park | 717 Prairie Street, Marblehead OH 43440 | — | — | 7 acres |
| Radar Park | 1305 W Main St (SR 163), Marblehead OH 43440 | — | — | Former Nike radar site; NPS lease |
| Lucien M. Clemons Park | 101-105 Lifeboat Ln, Marblehead OH 43440 | 41.541762 | -82.7204804 | Conservation easements; LEIT AP9 |
| Clemons Cemetery | Marblehead OH 43440 | — | — | Village-managed per Maintenance Dept. |

### T6 Clay Center — Park
Source: https://ottawacountyparksoh.org/grants/clay-center-playground/ (fetched 2026-05-18)

| Park Name | Address | Acres | Notes |
|---|---|---|---|
| Clay Center Park | Susan Street, Clay Center OH 43408 | 7 | PDOC grant recipient; soccer, pavilion, trail |

### T6 Put-in-Bay — Park
Source: https://putinbayohio.com/pib-activities/derivera-park/ (fetched 2026-05-18)

| Park Name | Address | GPS Lat | GPS Lon | Notes |
|---|---|---|---|---|
| DeRivera Park | 341 Bayview Ave, Put-In-Bay OH 43456 | 41.6533078 | -82.8170852 | 5.4 acres; split governance 4/5 trust + 1/5 village |

### T6 Rocky Ridge — Null
Source: Google Maps search + Wikipedia — no parks found (map verified 2026-05-18)

### T7 — Black Swamp Conservancy — Land We Own (Ottawa County)
Source: https://blackswamp.org/properties/land-we-own/ (fetched 2026-05-18)
Source: https://blackswamp.org/property/dr-robert-l-nehls-memorial-nature-preserve/ (fetched 2026-05-18)
Source: https://blackswamp.org/property/quinstock-woods-preserve/ (fetched 2026-05-18)

| Property | Acres | Location | Access | Notes |
|---|---|---|---|---|
| Dr. Robert L. Nehls Memorial Nature Preserve | 40 | Lake Erie West Harbor, Catawba Island Township | Public, dawn to dusk | ADA kayak launch, pavilion, loop trail, pollinator meadow; co-managed with USFWS Ottawa NWR |
| Quinstock Woods Preserve | 19 | Catawba Island Township | Closed to public | Mature hardwood forest, migratory bird habitat |

### T7 — Black Swamp Conservancy — Land We Protect (Ottawa County)
Source: https://blackswamp.org/properties/land-we-protect/ (fetched 2026-05-18)
Source: https://blackswamp.org/property/west-harbor-preserve/ (fetched 2026-05-18)
Source: https://blackswamp.org/property/port-clinton-lakefront-preserve/ (fetched 2026-05-18)
Source: https://blackswamp.org/property/meadowbrook-marsh-preserve/ (fetched 2026-05-18)

| Property | Acres | Owner | BSC Role | Notes |
|---|---|---|---|---|
| West Harbor Preserve | 12 | PDOC (donated by BSC) | Formerly owned; now PDOC | Catawba Island Twp; not yet open; kayak launch + trails planned. Resolves T5-FLAG-4 |
| Port Clinton Lakefront Preserve | 14.7 | City of Port Clinton | Conservation easement | Bald eagle fishing area; T6 miss |
| Meadowbrook Marsh Preserve | 191 | Danbury Township | Conservation easement | Already staged at T5 with BSC noted |
| Ottawa NWR Turkey Run Unit | 266 | USFWS | Facilitated transfer | Already staged at T1 with Q31 flag |
| Middle Bass Island East Point Preserve | 7.8 | PiBTPD | Partnership | Already staged at T3; PiBTPD+LEIC+BSC tri-partnership |

### T7 — The Nature Conservancy Ohio (Ottawa County)
Source: https://www.nature.org/en-us/get-involved/how-to-help/places-we-protect/great-egret-marsh-preserve/ (fetched 2026-05-18)
Source: https://www.nature.org/en-us/about-us/where-we-work/united-states/ohio/places-we-protect/ (fetched 2026-05-18)

| Property | Acres | Location | Access | Notes |
|---|---|---|---|---|
| Great Egret Marsh Preserve | 150+ | Catawba Island, Ottawa County (across from East Harbor SP) | Public, dawn to dusk year-round | Coastal marsh + upland; 1.2-mi loop trail; kayaking, fishing, hiking, birding; created 2013, Clean Ohio grant |

### T7 — Western Reserve Land Conservancy (Ottawa County)
Source: https://wrlandconservancy.org/bay-point-sandbar-property-acquired-set-to-be-permanently-conserved/ (fetched 2026-05-18)

| Property | Acres | Location | Access | Notes |
|---|---|---|---|---|
| Bay Point Sandbar | 68 | Narrow peninsula S of Marblehead Peninsula into Sandusky Bay | Water access (anchoring); conservation restrictions in place | Acquired Dec 28 2017; 34-ac coastal wetland; ~2.5 mi Lake Erie shoreline; 80+ bird species; 7 species of concern |

### T5-FLAG-1 Resolution
Source: https://www.thebeacon.net/catawba-island-garden-club-john-braun-park-a-blossoming-partnership/ (fetched 2026-05-18)
John Braun Park (2370 NE Catawba Rd) — independent Board of Directors; not township, state, or federally funded. → T8 (private/nonprofit). NOT T6.

### T8 — Cemetery GNIS Baseline (IMP-111 / IMP-030)
Source: https://ohiogenealogyexpress.com/ottawa/ottawaoh_cems.htm (fetched 2026-05-19)

| Cemetery Name | Township | GNIS Status | Staged? | Notes |
|---|---|---|---|---|
| Near 1812 Battle Site Marker - Cemetery | Danbury Twp. | Active | NO | Historic; evaluate governance |
| Allen Cemetery | Allen Twp. | Active | YES (T5) | Matched to "Allen Township Cemetery" |
| Allen Twp. (Williston) Cemetery | Allen Twp. | Active | YES (T5) | Same as Allen Cemetery / Williston entry |
| Billman Road Cemetery | Allen Twp. | Active | YES (T5) | "Allen (Billman Road) Cemetery" |
| Catawba Island Cemetery | Catawba Twp. | Active | YES (T5) | |
| Christy Chapel Cemetery | Portage Twp. | Active | YES (T5) | |
| Clay Cemetery | Clay Twp. | Active | YES (T5) | Matched to "Clay Township Cemetery" |
| Clay Township (Clay-Genoa) Cemetery | Clay Twp. | Active | YES (T5) | Same as Clay Cemetery above |
| Clemons Cemetery | Danbury Twp. | Active | YES (T6) | Village of Marblehead-managed |
| Confederate Cemetery — Johnston's Island | (Erie County) | Active | YES (T1) | "Confederate Stockade Cemetery" staged T1 |
| County Home Cemetery | Salem Twp. | Active | YES (T4) | "Ottawa County Home Cemetery" |
| Crown Hill Cemetery | Put-in-Bay Twp. | Active | YES (T5) | |
| Dewelle Cemetery | Portage Twp. | Active | YES (T5) | "Dwelle Cemetery" |
| **East Harbor State Park Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T2 miss — within ODNR East Harbor SP** |
| Elliston Cemetery | Benton Twp. | Active | YES (T5) | |
| **Guss Cemetery** | **Harris/Elmore Twp.** | **Active** | **NO** | **T5 miss — evaluate governance** |
| **Hartshorn Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T5 miss — evaluate; note: "Harrington Cemetery" staged may be this** |
| Hineline Cemetery | Bay Twp. | Active | YES (T5) | |
| Isle of St. George | (section header) | — | — | Not a cemetery name; refers to North Bass Island |
| **Jamison Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T5 miss — evaluate governance** |
| Johnson's Island (Confederate) | (Erie County) | Active | YES (T1) | Same as Confederate Cemetery above |
| K'burg Cemetery | Catawba Island Twp. | Active | YES (T5) | |
| **Kelly Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T5 miss — evaluate governance** |
| Lecarpe Cemetery | Erie Twp. | Active | YES (T5) | "LaCarpe Cemetery" |
| Lakeview Cemetery | Port Clinton / Portage Twp. | Active | YES (T6) | City of Port Clinton |
| Limestone Cemetery | Benton Twp. | Active | YES (T5) | |
| Locust Point Cemetery | Carroll Twp. | Active | YES (T5) | |
| Maple Leaf Cemetery | Put-in-Bay Twp. | Active | YES (T5) | |
| **Middle Bass Cemetery** | **Put-in-Bay Twp.** | **Active** | **UNCERTAIN** | **May match "La Fleur Cemetery" staged T5 — verify** |
| Oakland Cemetery | Unknown | Partial | **NO** | **Evaluate governance and location** |
| Oak Harbor Cemetery | Salem Twp. | — | YES (T5) | Cross-ref to Union Cemetery (Oak Harbor) — covered |
| **Old Elliston Cemetery** | **Benton Twp.** | **Active** | **NO** | **T5 miss — distinct from Elliston Cemetery** |
| **Old Elmore Cemetery** | **Harris Twp.** | **Active** | **NO** | **T5 miss — evaluate governance** |
| **Put-in-Bay Monument Burials** | **Put-in-Bay Twp.** | **Active** | **UNCERTAIN** | **Likely Perry's Victory NPS burials — check T1 staging** |
| Rice Cemetery | Harris Twp. | — | — | Cross-ref to Rymers Cemetery |
| Riverview Cemetery | Port Clinton / Bay Twp. | Active | YES (T5 + T6) | Staged as both Bay Twp T5 and Port Clinton T6 — may need normalization review |
| Roose Cemetery | Salem Twp. | Active | YES (T5) | |
| Rusha Cemetery | Carroll Twp. | Active | YES (T5) | |
| **Russian Orthodox Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T8 church cemetery** |
| **Rymers (Rice) Cemetery** | **Harris Twp.** | **Active** | **NO** | **T5 miss — evaluate governance** |
| Sackett Cemetery | Danbury Twp. | Active | YES (T5) | |
| **St. George Cemetery** | **Put-in-Bay** | **Active** | **NO** | **Evaluate — church or township?** |
| **Saint Joseph Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T8 church cemetery** |
| **St. Joseph Cemetery** | **Carroll Twp.** | **Active** | **NO** | **T8 church cemetery** |
| **St. Mary's Byzantine Catholic Church Graveyard** | **Danbury Twp.** | **Active** | **NO** | **T8 church cemetery** |
| **St. Paul Lutheran Cemetery** | **Danbury Twp.** | **Active** | **NO** | **T8 church cemetery** |
| Shook Cemetery | Portage Twp. | Active | YES (T5) | |
| **Tynan Burial Plot** | **Portage Twp.** | **Active** | **NO** | **T8 family cemetery** |
| Union Cemetery (Oak Harbor) | Salem Twp. | Active | YES (T5) | "Oak Harbor Union Cemetery" |
| Union (Elmore) Cemetery | Harris Twp. | Active | YES (T5) | "Harris-Elmore Union Cemetery" |
| **Veterans Memorial Cemetery** | **Unknown** | **Active** | **NO** | **Evaluate location and governance** |
| Williston Cemetery | Allen Twp. | Active | YES (T5) | Cross-ref to Allen Twp. (Williston) Cemetery |
| Wolcott Cemetery | Danbury Twp. | Active | YES (T5) | |

**Staged not in GNIS list (need verification):**
- Harrington Cemetery (T5 staged) — may be "Hartshorn Cemetery" Danbury Twp. (name variant); or distinct unlisted cemetery
- La Fleur Cemetery (T5 staged, Put-in-Bay Twp.) — may match "Middle Bass Cemetery" in GNIS; verify
- North Bass Cemetery (T5 staged) — not in GNIS list; verify independently

**T8 cemetery candidates from GNIS cross-reference:**
- 5 Danbury Twp. church cemeteries: Russian Orthodox, Saint Joseph, St. Mary's Byzantine, St. Paul Lutheran (+ Near 1812 Battle Site, Hartshorn, Jamison, Kelly as potential T5 misses)
- 1 Carroll Twp. church cemetery: St. Joseph
- 1 Put-in-Bay church/private: St. George
- 1 Portage Twp. family cemetery: Tynan Burial Plot
- T5 misses requiring governance confirmation: Guss, Old Elliston, Old Elmore, Rymers
- Ambiguous: Oakland Cemetery, Veterans Memorial Cemetery, Put-in-Bay Monument Burials, East Harbor SP Cemetery (T2 miss)

---

## IMP-080 Record Count Verification

| Tier | Entity Records Added | Running Entity Total | Total Records (incl. metadata) | Result |
|------|---------------------|---------------------|-------------------------------|--------|
| T1 | 30 | 30 | 32 | PASS |
| T2 | 46 | 76 | 91 | PASS |
| T3 | 15 | 91 | 110 | PASS |
| T4 | 4* | 95 | 121 | PASS |
| T5 | 35† | 130 | 168 | PASS |
| T5-deferred | 1‡ | 131 | — | PASS (added at T6 verification) |
| T6 | 29§ | 160 | 237 | PASS |
| T7 | 12** | 172 | 254 | PASS |
| T8 | 27‡‡ | 199 | 287 | PASS |

*T4 adds 4 "true T4" entity records + 5 T1-miss NWR units (discovery_tier=1). The running total of 95 includes all staged entity records regardless of discovery_tier.

---

## Source Files (§24 IMP-129)

Qualifying binary source files saved to `County_Spreadsheets/Ottawa/source_files/` on 2026-05-22 (retroactive — §24 was not executed at discovery time due to IMP-129 wget mechanism gap):

| Filename | Size | Source / Notes |
|---|---|---|
| `odnr_coastal_access_ottawa_county.pdf` | 17,179 KB | ODNR Lake Erie Public Access Guide — Ottawa County. Source for 14 coastal sites (T2): OT1–OT14 GPS, acreages, governance. |
| `odnr_lake_erie_islands_chapter3.pdf` | 2,369 KB | ODNR Coastal Management Plan Ch. 3 — Lake Erie Islands. Source for island state park GPS and acreages (T2): South Bass, Middle Bass, North Bass parks. |
| `pibtpd_nature_preserves_brochure_2021.pdf` | 5,004 KB | PIBTPD Nature Preserves Brochure 2021. Source for 7 island preserves (T3): trail lengths, acreages, access rules. |
| `magee_marsh_wa_trail_map.pdf` | 3,035 KB | ODNR Magee Marsh Wildlife Area trail map. Source for 7 Magee Marsh trails (T2): lengths, loop configurations. Also referenced in Ottawa YAML and Lucas YAML. |
| `little_portage_wa_map.pdf` | 3,819 KB | ODNR Little Portage Wildlife Area map. Source for T2 Little Portage WA boundary and acreage data. |
†T5 adds 35 entity records: 8 park/preserve Sites, 24 cemetery Sites (§5.6 mandatory), 2 Trails, 1 Access Point. Plus 12 null/metadata blocks (3 entity-type nulls + 9 township park-null results).
‡Oak Harbor Union Cemetery staged as T5 (discovery_tier=5) but processed during T6 verification pass after T5-FLAG-5 was resolved.
§T6 adds 29 entity records: 26 Sites (parks + cemeteries), 1 Trail, 2 Access Points. Plus 33 null/metadata blocks. Grand total in YAML: 237 records.
**T7 adds 12 entity records: 6 T7-native (4 Sites, 1 Trail, 1 AP) + 6 cross-tier finds (1 T6-miss Port Clinton Lakefront Preserve; 5 T3-miss PiBTPD/PDOC parcels). Plus 5 null/evidence blocks. Grand total in YAML: 254 records. IMP-080 verified 2026-05-19.
‡‡T8 adds 27 entity records: 20 T8-native Sites + 2 T2-miss Sites (Lockwood Cemetery, Aquatic Visitors Center) + 5 T5-miss Sites (Old Elliston, Hartshorn, Jamison, Kelly, Rymers/Rice cemeteries). Plus 5 entity-type null blocks + 1 tier-level null block. Grand total in YAML: 287 records. IMP-080 verified 2026-05-19.
