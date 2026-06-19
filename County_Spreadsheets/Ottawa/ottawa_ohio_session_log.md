# Ottawa Ohio — Session Log
**RUN_ID:** `ottawa_ohio_2026_05_18`
**PREFIX:** `OTT`
**County:** Ottawa, Ohio
**Run date:** 2026-05-18
**Status:** DISCOVERY COMPLETE — T1–T8 done; pipeline pending

---

## Discovery — Tier Yield

| Tier | Source Type | Key Sources | Entity Records | Total Records |
|------|-------------|-------------|---------------|---------------|
| T1 | Federal | USFWS Ottawa NWR (fws.gov), NPS Perry's Victory | 30 | 32 |
| T2 | State agency | ODNR Parks, ODNR Wildlife, ODNR DNAP, ODNR Coastal PDF | 46 | 59 |
| T3 | District agency | PIBTPD (putinbayparks.com), PDOC (ottawacountyparksoh.org), Toledo Metroparks | 15 | 19 |
| T4 | County | Ottawa County (PDOC grants, county records, FWS visit-us) | 4* | 11 |
| T5 | Township | 12 Ottawa County townships (bentontownship.org, catawbaislandtownship.com, danburytownship.com, others) | 35 | 47 |
| T6 | Municipal | portclinton.com, oakharbor.oh.us, genoaohio.org, villageofelmoreohio.wordpress.com, marbleheadohio.org, ottawacountyparksoh.org (Clay Center), villageofpib.com | 29 | 62 |
| T7 | Land trust / conservancy | Black Swamp Conservancy, The Nature Conservancy, Western Reserve Land Conservancy | 6* | 17** |
| T8 | Private / other | African Safari Wildlife Park, Schedel Arboretum, Oak Harbor Conservation Club, Catawba Island Club, golf courses (×4), hunting clubs (×3), church/private cemeteries (×8) | 20* | 26** |

*T4 entity count (4) excludes 5 T1-miss NWR units staged with discovery_tier=1.

**Total raw records (T1–T4):** 121 (95 entity + 26 metadata)
**Total raw records (T1–T5):** 168 (130 entity + 38 metadata)
**Total raw records (T1–T6):** 237 (160 entity + 77 metadata/null blocks)
**Total raw records (T1–T7):** 254 (17 new records: 6 T7-native entity + 6 cross-tier finds staged [1 T6 miss, 5 T3 misses] + 5 T7 null/evidence blocks)
**Total raw records (T1–T8):** 287 (33 new records: 20 T8-native entity + 7 cross-tier finds staged [2 T2 misses, 5 T5 misses] + 6 T8 null/evidence blocks)

*T7 entity count (6): 4 Sites (Nehls Memorial NP, Quinstock Woods, Great Egret Marsh, Bay Point Sandbar), 1 Trail (Great Egret Marsh Preserve Trail), 1 Access Point (Nehls ADA Kayak Launch). Excludes 6 cross-tier entities staged during T7 investigation (credited to their source tiers).
**T7 total records (17): 6 T7-native entity + 6 cross-tier finds (1 T6 miss: Port Clinton Lakefront Preserve; 5 T3 misses: West Harbor Preserve, Costello Tract, Schneider Tract, Lawrence Evans Property, Prokesh Property) + 5 null/evidence blocks (Trail Segment, Trail Network, Site Network, LEIC [advisory-only], ONAPA [no nonprofit directory]).

*T8 entity count (20): 12 Sites — recreation/wildlife (African Safari Wildlife Park, John Braun Park, Schedel Arboretum, Oak Harbor Conservation Club, Dr. L.J. Darr Memorial Wetlands, Lake Erie Club, Toussaint Shooting Club) + 4 golf courses (The Islander GCC, Catawba Island Club, Oak Harbor Golf Club, Bay Point Golf Club, Saunders Golf Course [5, counting Saunders]) + 8 church/private cemeteries (St. Joseph's-Toussaint, Russian Orthodox, St. Joseph's-Danbury, St. Mary's Byzantine, St. Paul's Lutheran, Tynan, War of 1812, Guss). Excludes 7 cross-tier finds staged during T8 investigation (5 T5-miss cemeteries + 2 T2 misses credited to source tiers).
**T8 total records (26): 20 T8-native entity + 5 entity-type null blocks (Trail, Trail Segment, Trail Network, Site Network, Access Point) + 1 tier-level null block (no additional private entities found beyond specifically researched candidates).

**Post-resolution:** TBD

---

## Normalization Decisions

*(To be populated post-discovery)*

---

## GPS Acquisition

*(To be populated post-discovery)*

---

## Errors and Fixes

- **Run v1 archived (2026-05-18):** Prior T1–T4 run used incorrect schema fields (county_raw instead of counties_raw: [], notes_raw instead of identity_notes_raw, address_raw instead of location_raw, source_url instead of urls_raw). Root cause: IMP-112 not yet implemented; broad Glob patterns surfaced deprecated v4 files instead of authoritative /discovery/ and /schemas/ modules. Fix: IMP-112 added to na-discovery skill; all session files archived to archive_v1/; fresh run started with correct v5.3 schema.

---

## Pipeline Stage Log

*(To be populated post-discovery)*

---

## Entity ID Assignments

| Entity ID | Name | Type |
|-----------|------|------|
| *(none yet — discovery in progress)* | | |

---

## Open Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| T1-FLAG-2 | John Gallagher Trail / Gallagher Memorial Trail | Name/length collision between T1-staged trail (0.99 mi, FWS) and Magee Marsh source (1.2 mi, "Gallagher Memorial Trail"). May be same trail. | GPS acquisition pass — measure and compare |
| T5-FLAG-1 | John Braun Park (2370 NE Catawba Rd, Catawba Island Twp) | ✅ RESOLVED T6: T8 private/nonprofit (independent Board of Directors) | CLOSED |
| T5-FLAG-2 | Nehl's Memorial Nature Preserve (4400 E. Muggy Rd) | ✅ RESOLVED T7: Black Swamp Conservancy fee-simple, 40 ac, purchased 2019. Staged as T7 Site "Dr. Robert L. Nehls Memorial Nature Preserve." ADA kayak launch also staged (T7 Access Point). | CLOSED |
| T5-FLAG-3 | Three PDOC parks on NW Catawba Rd (3648, 3655, 133 W Catawba) | Announced on CIT Additional Parks page; not yet open | T3 (PDOC) — stage when open |
| T5-FLAG-4 | Black Swamp Conservancy park, NW Catawba Rd | ✅ RESOLVED T7: West Harbor Preserve — BSC purchased via Clean Ohio Conservation Fund, donated to PDOC; PLANNED/not yet open. Staged as T3 Site (PDOC ownership). | CLOSED |
| T5-FLAG-5 | Oak Harbor Union Cemetery (Salem Township area) | ✅ RESOLVED T6: confirmed Salem Township entity (11565 SR-105 west of Oak Harbor city limits). Staged T5. | CLOSED |
| T2-FLAG-4 | Ottawa NWR Little Portage Unit | Deferred at T1 as roadside-view-only; resolved at T4 — Eagle Scout kayak launch confirmed 2023 (PRWT Mile 3.7). Now staged as T1 entity. | RESOLVED — see identity_notes_raw |
| T3-FLAG-7 | Ottawa NWR Little Portage Unit | Flagged T3 after launch confirmed; resolved at T4. | RESOLVED |
| Q31 | Ottawa NWR Turkey Run Unit | COUNTY_UNCERTAIN — may be Ottawa or Sandusky County | GIS verification at normalization |
| Q32 | Ottawa NWR Upper Toussaint Unit | COUNTY_UNCERTAIN — Toussaint River straddles Ottawa/Sandusky | GIS verification at normalization |
| Q35 | Ottawa County Home Cemetery | Confirm county vs. Salem Township management | Normalization pass |
| Q36 | Catawba Islander Trail | PLANNED flag — confirm when Phase 1 construction begins | Monitor; update flag when confirmed |
| Q37 | Ottawa County Fairgrounds PRWT Launch | Address discrepancy: 7870 W SR 163 (PRWT source) vs 770 SE Catawba Rd (PDOC grant page) | GPS acquisition pass |
| CROSS-1 | Lake Erie Islands Water Trail | CROSS_COUNTY_CANDIDATE — island loops in Ottawa; Kelleys Island in Erie County | Coordinate with Erie County run |
| CROSS-2 | North Coast Inland Trail | CROSS_COUNTY_CANDIDATE — Erie, Huron, Ottawa, Sandusky counties; extends into Genoa Veterans Memorial Park (2020) and passes through Elmore (Depot Park, Walter Ory Park) | Coordinate with multi-county run |
| T6-FLAG-1 | DeRivera Park (Put-in-Bay) | Split governance: 4/5 DeRivera Park Trustees (private charitable trust), 1/5 Village of Put-in-Bay. Baseline seed 'Put-In-Bay City Park' resolved here. | Resolution pass — determine canonical tier |

---

## Status

**DISCOVERY COMPLETE T1–T8.** 287 records staged in ottawa_ohio_raw_discovery.yaml (225 entity + 62 null/evidence blocks). Ready for Resolution → Normalization → GPS Acquisition → TSV Output pipeline.
