# Ottawa County Ohio — Session Log
**RUN_ID:** `ottawa_ohio_2026_05_17`  
**PREFIX:** `OTT`  
**County:** Ottawa County, Ohio  
**FIPS:** 39123  
**Run date:** 2026-05-17  
**Status:** IN PROGRESS — T1 ✅ T2 ✅ T3 ✅ T4 ✅; T5 (Township) next

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal | USFWS (fws.gov/refuge/ottawa), NPS (nps.gov/pevi), VA NCA (cem.va.gov) | **32 records** — Ottawa NWR (main + Navarre Marsh unit + West Harbor Landing), Perry's Victory, Confederate Stockade Cemetery; 17 trails; 1 site network (Ottawa NWR Complex); 2 APs; USFS/USACE/BLM/DoD/Tribal null |
| T2 | State agency | ODNR Parks (7 parks), ODNR Wildlife (9+ areas), ODNR DNAP (Lakeside Daisy SNP), Ohio National Guard (Camp Perry), OSU §4.7 (Stone Lab); ODNR coastal PDFs | **60 records** — 20 Sites, 24 Trails (11 East Harbor + 4 Middle Bass + 1 Marblehead + 1 Lakeside Daisy + 7 Magee Marsh WA), 2 APs; Sandusky River = out of scope; Crane Creek SP dissolution confirmed; Lake Erie Islands Water Trail deferred T3; 3 pending WAs (West Harbor, OC WA 1 & 2) |
| T3 | District agency | Ohio Auditor pre-enumeration (IMP-072): PIBTPD, Park District of Ottawa County, Ottawa County SWCD, Sand Beach CD; PIBTPD brochure (PDF); PDOC website; Ottawa County Park District confirmed ✅ | **19 records** — 7 Sites (PIBTPD: Ladd Carr Wildlife Woods, Dodge Woods Preserve, Massie Cliffside Preserve, Scheeff East Point Nature Preserve, Duff Homestead and Bayfront Preserve, Middle Bass Island Forested Wetlands Preserve, Middle Bass Island East Point Preserve); 8 Trails (6 PIBTPD + Lake Erie Islands Water Trail [CROSS_COUNTY_CANDIDATE] + North Coast Inland Trail [CROSS_COUNTY_CANDIDATE]); 4 tier_result nulls; KNOWN_MC confirmed: OH-MC-S-021 (Howard Marsh) ✅, OH-MC-TR-002 (Portage River Water Trail) ✅; IMP-104 PASS: OH-OTT-T-072 to -076; Bootstrap correction: Park District of Ottawa County confirmed to exist (Q1 resolved) |
| T4 | County | Ottawa County government website (co.ottawa.oh.us), Park District of Ottawa County (ottawacountyparksoh.org), NRHP Wikipedia list, Ohio PoorHouseStory (IMP-099 cemeteries), FWS Ottawa NWR visit-us page (T1-miss sweep) | **11 records** — 1 Site Network (Park District of Ottawa County), 1 Site (Ottawa County Home Cemetery — IMP-099), 1 Trail (Catawba Islander Trail — PLANNED), 1 Access Point (Ottawa County Fairgrounds PRWT Launch); 5 T1-miss Sites (Ottawa NWR units: Marinewood, Turkey Run, Turtle Creek Island, Upper Toussaint, Little Portage); 2 tier_result NULLs (NRHP bridge check, county golf course IMP-099); T7 deferred: Nehls Memorial Nature Preserve; IMP-080 PASS (122 total) |
| T5 | Township | 12 Ottawa County townships | pending |
| T6 | Municipal | Port Clinton, Oak Harbor, Elmore, Put-in-Bay, Marblehead, Lakeside-Marblehead; island municipalities handled separately | pending |
| T7 | Conservancy | TNC (Great Egret Marsh), Black Swamp Conservancy, local land trusts | pending |
| T8 | Private | African Safari Wildlife Park, Winous Point, Schedel Arboretum, other private | pending |

**Total raw records:** 122 (T1: 30 [25 original + 5 T1-miss discovered at T4], T2: 60, T3: 19, T4: 4 direct + 2 tier_result NULLs; plus 7 tier_result NULLs from T1–T3)  
**Post-resolution:** TBD

---

## Normalization Decisions

*To be populated during pipeline.*

**Pre-normalization flags:**
- Catawba Island SP: 10 ac actual (baseline error: 677 ac)
- South Bass Island SP: 33 ac actual (baseline error: 677 ac)
- Oak Point SP: 1.5 ac actual (baseline error: 677 ac)
- Marblehead Lighthouse SP: 13.5 ac actual (baseline error: 9 ac)
- Little Portage WA: 407 ac actual (baseline error: 357 ac)
- Fox's Marsh WA: 132 ac actual (baseline error: 133.49 ac)
- Crane Creek SP: dissolved — entity confirmed absent
- Green Island WA: No public access — normalization decision needed
- Gallagher Memorial Trail (Magee source) likely = T1 John Gallagher Trail — resolve at GPS acquisition
- Middle Bass Island East Point Preserve: 7.8 ac actual (handoff T3-deferred noted 11 ac — brochure authoritative)
- Petersen Woods (T2, 2 ac): same entity as PIBTPD brochure Petersen Woods (1.5 ac) + Lawrence Evans (0.75 ac); PIBTPD owner; ODNR co-manager — flag T2 record at normalization (T3-FLAG-6)
- Lake Erie Islands Water Trail: CROSS_COUNTY_CANDIDATE — manage via MC- pipeline; determine primary county
- North Coast Inland Trail: CROSS_COUNTY_CANDIDATE — in MULTI_COUNTY.xlsx; manage via MC- pipeline; determine primary county and Ottawa County segment length
- Little Portage Unit: possible T1 miss with updated public access (Eagle Scout kayak launch 2023) — re-evaluate T2-FLAG-4 (T3-FLAG-7)

---

## GPS Acquisition

**Nominatim:** TBD  
**Fallbacks used:** TBD

**GPS already captured (from authoritative sources):**
- Ottawa NWR: 41.6074975, -83.209608 (FWS)
- Perry's Victory: PO Box 549, Put-in-Bay (GPS TBD)
- Confederate Stockade Cemetery: 41.5007, -82.7300 (ODNR coastal PDF)
- East Harbor SP: 41.5452, -82.8176 (ODNR coastal PDF)
- South Bass Island SP: 41.6423, -82.8373 (ODNR coastal PDF)
- Oak Point SP: 41.6539, -82.8174 (ODNR coastal PDF)
- Middle Bass Island SP: 41.6761, -82.8110 (ODNR coastal PDF)
- North Bass Island SP (S): 41.7074, -82.8162 (ODNR coastal PDF)
- Marblehead Lighthouse SP: 41.5363, -82.7125 (ODNR coastal PDF)
- Catawba Island SP: 41.5745, -82.8570 (ODNR coastal PDF)
- Mazurik Access Area: 41.5411, -82.7636 (ODNR coastal PDF)
- Dempsey Fishing Access: 41.5077, -82.7608 (ODNR coastal PDF)
- Sandusky Bay Bridge Access N: 41.4842, -82.8293 (ODNR coastal PDF)
- Camp Perry: 41.5465, -83.0135 (ODNR coastal PDF)
- Little Portage WA: 41.4912, -83.0319 (approximate center)
- Fox's Marsh WA: 41.7120, -82.8311 (ODNR coastal PDF)
- Honey Point WA: 41.7074, -82.8083 (ODNR coastal PDF)
- Kuehnle WA: 41.6905, -82.8068 (ODNR coastal PDF)
- Johnson's Island Confederate Cemetery: 41.5007, -82.7300 (ODNR coastal PDF — updates T1 staged record)

**GPS needed:** Toussaint Creek WA, Lakeside Daisy SNP, Stone Lab Peach Point Campus, Green Island WA, Petersen Woods, Honey Point WA (acreage), all T2 trail GPS, Middle Bass SP trail lengths

**T3 GPS already captured (from authoritative sources):**
- (none — all T3 GPS deferred to GPS acquisition pass)

**T3 GPS needed:** All 7 PIBTPD Sites (island preserves; GPS acquisition via Nominatim/GIS); all 8 T3 Trail lengths where TBD (Burgundy Bay trail, Middle Bass East Point path, Lake Erie Islands Water Trail total, North Coast Inland Trail Ottawa County segment)

---

## Errors and Fixes

| Error | Fix |
|-------|-----|
| Baseline acreages for island parks heavily inflated (677 ac for Catawba IS SP, South Bass IS SP, Oak Point SP) | Corrected from ODNR coastal PDF: Catawba ~10 ac, South Bass 33 ac, Oak Point 1.5 ac. Baseline confusion between island/peninsula size and park size. |
| Baseline listed Marblehead Lighthouse SP as 9 ac | Corrected: 13.5 ac per ODNR coastal PDF. |
| Baseline listed Little Portage WA as 357 ac | Corrected: 407 ac per ODNR wildlife area map data. |
| Baseline listed Fox's Marsh WA as 133.49 ac | Corrected: 132 ac per ODNR coastal PDF. |

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 0 — Discovery | T1 ✅ T2 ✅ T3 ✅ T4 ✅; T5–T8 pending | 122 records staged; T5 (Township) next |
| Stage 1 — Resolution | pending | |
| Stage 2 — Normalization | pending | |
| Stage 3 — GPS Acquisition | pending | |
| Stage 4 — TSV Output | pending | |
| Stage 4.5 — Vocab Gate | pending | |
| Stage 5 — Integrity Check | pending | |
| Stage 6 — DB Upsert | pending | |

---

## Entity ID Assignments

*To be populated during pipeline. Prefix: OTT.*

*Discovery-stage counts (IDs assigned at pipeline):*
- T1 Sites: 5 → will consume OTT-S-001 through OTT-S-005
- T2 Sites: 20 → will consume OTT-S-006 through OTT-S-025
- **T3 Sites: 7 → will consume OTT-S-026 through OTT-S-032**
- T1 Trails: 17 → will consume OTT-T-077 through OTT-T-093
- T2 Trails: 24 → will consume OTT-T-094 through OTT-T-117
- **T3 Trails: 8 → will consume OTT-T-118 through OTT-T-125** *(Note: Lake Erie Islands Water Trail and North Coast Inland Trail are CROSS_COUNTY_CANDIDATE — may receive MC- prefix IDs instead of OTT- at pipeline)*
- T1 Site Networks: 1 → will consume OTT-SN-001
- T1 Access Points: 2 → will consume OTT-AP-001 through OTT-AP-002
- T2 Access Points: 2 → will consume OTT-AP-003 through OTT-AP-004
- **T4 Site Networks: 1 → will consume OTT-SN-002** (Park District of Ottawa County)
- **T4 Sites: 1 → will consume OTT-S-033** (Ottawa County Home Cemetery)
- **T1-miss Sites discovered at T4: 5 → will consume OTT-S-034 through OTT-S-038**
  - OTT-S-034: Ottawa NWR — Marinewood Unit
  - OTT-S-035: Ottawa NWR — Turkey Run Unit
  - OTT-S-036: Ottawa NWR — Turtle Creek Island Unit
  - OTT-S-037: Ottawa NWR — Upper Toussaint Unit
  - OTT-S-038: Ottawa NWR — Little Portage Unit
- **T4 Trails: 1 → will consume OTT-T-126** (Catawba Islander Trail)
- **T4 Access Points: 1 → will consume OTT-AP-005** (Ottawa County Fairgrounds PRWT Launch)

*Note: OH-OTT-T-072 through OH-OTT-T-076 (Howard Marsh trails) already in DB from Lucas County run. IMP-104 PASS confirmed at T3.*

---

## Open Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| IMP-104 | OH-OTT-T-072 to -076 | Howard Marsh trails in DB with Ottawa county; discovered during Lucas run | Confirm during T3 discovery (Toledo Metroparks); no new entity needed, confirm IDs and count match |
| T1-FLAG-1 | Ottawa NWR Wildlife Drive | Auto tour route staged as Trail (TRAIL_TYPE_REVIEW) | Verify Auto Tour is in use_type vocabulary at normalization |
| T1-FLAG-2 | Grimm Prairie / John Gallagher Trail / Gallagher Memorial Trail | Naming inconsistency: FWS page shows John Gallagher Trail (0.99 mi) and Grimm Prairie Trail (0.39 mi) as distinct; Magee Marsh source calls a trail "Gallagher Memorial Trail" (1.2 mi) and says it's "in Ottawa NWR"; may be 2 or 3 distinct trails | Verify against FWS map and field GPS at acquisition pass |
| T1-FLAG-3 | Metzger Marsh Trail | County uncertain (Ottawa or Lucas); staged with both | Verify county via GIS at normalization |
| T1-FLAG-4 | Ottawa NWR (main) | CROSS_COUNTY_CANDIDATE (Ottawa/Lucas) due to Metzger Marsh unit | Resolve at cross-county resolution; primary county is Ottawa |
| T2-FLAG-1 | Crane Creek Estuary Trail (Magee Marsh) | CROSS_SITE_FLAG: may overlap with T1 Estuary Trail (0.54 mi) at Ottawa NWR | Verify trail boundary via GPS acquisition; may be same trail described from both property sides |
| T2-FLAG-2 | Magee-Ottawa Partnership Trail — Magee Segment | CROSS_SITE_FLAG: 0.5 mi Magee segment may be part of T1 Partnership Trail (1.41 mi, Ottawa NWR side) | Verify whether to merge into one cross-property trail record or keep as two segment records |
| T2-FLAG-3 | Green Island Wildlife Area | NO PUBLIC ACCESS (state bird sanctuary; closed to public) | Normalization decision: does no-public-access preclude NAP entity? Compare to Navarre Marsh (T1, restricted/permit access) |
| T2-FLAG-4 | FWS Little Portage Unit | FWS page exists (fws.gov/refuge/ottawa/visit-us/locations/little-portage-unit); "view from roadside only" — potential T1 miss | Normalization review: does roadside-view-only unit meet public-access threshold? If yes, stage as T1 child of Ottawa NWR at normalization |
| T2-FLAG-5 | West Harbor WA / Ottawa County WA 1 & 2 | Not found in ODNR coastal PDF; likely ODNR hunting areas | Confirm via ODNR hunting area maps at normalization |
| T3-FLAG-1 | Lake Erie Islands Water Trail | CROSS_COUNTY_CANDIDATE staged at T3; management tier = PIBTPD; ODNR-designated water trail; island loops; GPS and total length TBD | GPS acquisition pass; confirm loop routes and total mileage; determine primary county for MC- ID |
| T3-FLAG-2 | North Coast Inland Trail | CROSS_COUNTY_CANDIDATE staged at T3; PDOC Ottawa County managing entity; 4-county trail (Erie;Huron;Sandusky;Ottawa); MULTI_COUNTY.xlsx listed (not yet in DB); also US Bike Route 30; Ottawa County segment length TBD | Pipeline: determine primary county and assign MC- ID; confirm total Ottawa County segment mileage via GIS |
| T3-FLAG-3 | Middle Bass Island East Point Preserve | Acreage correction: handoff T3-deferred list said 11 ac; brochure says 7.8 ac; use 7.8 ac (brochure authoritative) | Note at normalization; correct any downstream references |
| T3-FLAG-4 | Duff Homestead and Bayfront Preserve | Acquired 2023 (post-2021 PIBTPD brochure); visitor center opening summer 2024; no formal trail yet; GPS TBD | GPS acquisition pass; confirm visitor center/public access status; determine if trail entity needed |
| T3-FLAG-5 | Middle Bass Island Forested Wetlands Preserve — Hahn Property | Hahn Property (~8.3 ac, Middle Bass) listed "under contract" in 2021 brochure; may be acquired by 2023 | Check current PIBTPD website/2023 Annual Report; if acquired, note as additional acreage in notes (not staged separately — no public access per Q28-Q29) |
| T3-FLAG-6 | Petersen Woods overlap | T2-staged Petersen Woods (2 ac, ODNR Wildlife + PIBTPD) corresponds to PIBTPD brochure Petersen Woods (1.5 ac) + Lawrence Evans Property (0.75 ac) = 2.25 ac. Same physical entity; PIBTPD is owner, ODNR co-manages. | Normalization: flag as KNOWN_MC-like same-entity; update T2 Petersen Woods record to note PIBTPD ownership; do not create duplicate T3 record |
| T3-FLAG-7 | Little Portage Unit — public access update | T2-FLAG-4 staged as "roadside-view-only" FWS unit; PDOC PRWT page shows Eagle Scout Tyler Shadoan kayak launch at this site (2023). If launch is on FWS land, unit now has water-based public access. | Re-evaluate T2-FLAG-4 at normalization; may qualify as T1 FWS child entity of Ottawa NWR (Q24) |
| IMP-104-T3 | Howard Marsh trails OH-OTT-T-072 to -076 | Confirmed at T3 via Toledo Metroparks/Howard Marsh Metropark KNOWN_MC:OH-MC-S-021 | PASS — IDs confirmed, no new records |
| T4-FLAG-1 | Ottawa NWR — Turkey Run Unit (OTT-S-035) | COUNTY_UNCERTAIN — located ~16 mi SE of main refuge; may be Ottawa or Sandusky County | Verify county boundary via GIS at normalization (Q31) |
| T4-FLAG-2 | Ottawa NWR — Upper Toussaint Unit (OTT-S-037) | COUNTY_UNCERTAIN — Toussaint River area may straddle Ottawa/Sandusky county line | Verify county boundary via GIS at normalization (Q32) |
| T4-FLAG-3 | Catawba Islander Trail (OTT-T-126) | PLANNED — physical trail not yet built; Master Plan adopted July 2023; Phase 1 route mapped | Update flag when Phase 1 construction confirmed; remove PLANNED status (Q36) |
| T4-FLAG-4 | Ottawa County Fairgrounds PRWT Launch (OTT-AP-005) | ADDRESS_DISCREPANCY — PRWT source lists 7870 W SR 163, Oak Harbor; PDOC grant page lists 770 SE Catawba Rd, Port Clinton | Verify physical AP location vs. fairgrounds office address at GPS acquisition (Q37) |
| T4-FLAG-5 | Ottawa NWR — Marinewood Unit (OTT-S-034) | GPS/address TBD; PRWT launch address (4640 W Harbor Rd) may not reflect main unit entrance | Verify unit GPS and primary address at acquisition pass (Q30) |
| T4-RESOLVE | FWS Little Portage Unit (OTT-S-038) | RESOLVES T2-FLAG-4 and T3-FLAG-7 — Eagle Scout kayak launch (PRWT Mile 3.7, 2023) confirmed; unit now has water-based public access; staged as T1 child of Ottawa NWR | T2-FLAG-4 and T3-FLAG-7 closed at T4 staging |

---

## Status

**IN PROGRESS — T1 ✅ T2 ✅ T3 ✅ T4 ✅ — T5 (Township) next**

T1–T4 complete. 122 records in YAML. IMP-080 PASS (122 verified). IMP-104 PASS at all tiers.

**T4 key findings (2026-05-18):**
- Park District of Ottawa County confirmed as formal county parks district (est. 1992); staged as Site Network (OTT-SN-002); primarily a grants/planning body — directly manages trails (NCIT, PRWT, Catawba Islander) but does not own individual parks
- Ottawa County Home Cemetery (infirmary/poorhouse, Salem Township) staged per IMP-099 (OTT-S-033)
- Catawba Islander Trail staged as PLANNED (OTT-T-126); Master Plan adopted July 2023; ~5 mi, Catawba Island; Phase 1 route mapped but unbuilt (T4-FLAG-3 / Q36)
- Ottawa County Fairgrounds PRWT Launch staged as T4 AP (OTT-AP-005); PDOC grant; PRWT Mile 7.8; address discrepancy flagged (T4-FLAG-4 / Q37)
- 5 Ottawa NWR units missed at T1 now staged (OTT-S-034 through OTT-S-038): Marinewood, Turkey Run, Turtle Creek Island, Upper Toussaint, Little Portage; Turkey Run and Upper Toussaint have COUNTY_UNCERTAIN flags (T4-FLAG-1, T4-FLAG-2)
- T2-FLAG-4 and T3-FLAG-7 (Little Portage Unit public access) RESOLVED at T4 — Eagle Scout kayak launch (2023, PRWT Mile 3.7) confirmed; unit staged as T1 entity
- Nehls Memorial Nature Preserve (Black Swamp Conservancy-owned) confirmed T7, deferred
- NRHP bridge check: 31 Ottawa County listings reviewed; no county-managed bridge/structure entity; SR 51 bridge replaced 2020 (likely demolished)
- County golf course IMP-099: none found; former Marinewood Golf Course now NWR land

**T3 key findings (2026-05-17):**
- PIBTPD owns 7 publicly accessible natural area preserves (South Bass + Middle Bass islands)
- Duff Homestead and Bayfront Preserve (6.5 ac, 2023 acquisition) confirmed via PDOC grant page
- North Coast Inland Trail staged as CROSS_COUNTY_CANDIDATE (T3, PDOC, 4-county trail, not yet in DB)
- Lake Erie Islands Water Trail staged as CROSS_COUNTY_CANDIDATE (T3, PIBTPD managed per §4.6)
- Portage River Water Trail = KNOWN_MC:OH-MC-TR-002 confirmed via PDOC (Q12 resolved)
- Ottawa County Park District (Q1): bootstrap error corrected — Park District of Ottawa County CONFIRMED EXISTS (Ohio Auditor, est. 1992)
- Little Portage Unit public access: Eagle Scout kayak launch 2023 confirmed (resolved at T4)
