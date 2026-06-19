# Ottawa County, Ohio — Discovery Handoff
**RUN_ID:** `ottawa_ohio_2026_05_17`  
**PREFIX:** `OTT`  
**FIPS:** 39123  
**County seat:** Port Clinton  
**Bootstrap date:** 2026-05-17  
**Status:** TIER 1 IN PROGRESS

---

## County Context

- **State:** Ohio
- **County seat:** Port Clinton
- **Bounding box:** lat 41.37–41.77, lon -83.42 to -82.72
- **Adjacent counties:** Erie (E), Sandusky (S), Wood (SW), Lucas (W); Lake Erie forms the northern border
- **Special complexity:** Lake Erie island county — South Bass Island (Put-in-Bay), Middle Bass Island, North Bass Island, Catawba Island, and several smaller islands. Island municipalities require separate treatment at Tier 6.
- **Water content:** Ottawa National Wildlife Refuge, Magee Marsh, Navarre Marsh, multiple ODNR Wildlife Areas along the lakeshore and on islands. Significant water site and water trail content expected. Read `discovery/na_water_trail_discovery_subproc_v5.1.md` before Tier 2.

**Major municipalities:**
- Port Clinton (county seat) — city
- Oak Harbor — village
- Elmore — village
- Genoa — village (partially in Ottawa, partially in Lucas)
- Marblehead — unincorporated community / census-designated place (in Danbury Township)
- Lakeside-Marblehead — village
- Put-in-Bay — village (South Bass Island)
- Middle Bass Island — island community
- North Bass Island — island community
- Catawba Island — unincorporated peninsula community

**Townships (12 — from Townships_Officials2022-2023.xlsx, Ottawa County):**
1. Allen Township (Williston)
2. Bay Township (Port Clinton)
3. Benton Township (Graytown)
4. Carroll Township (Oak Harbor)
5. Catawba Island Township (Port Clinton)
6. Clay Township (Genoa)
7. Danbury Township (Marblehead)
8. Erie Township (Port Clinton)
9. Harris Township (Elmore)
10. Portage Township (Port Clinton)
11. Put-In-Bay Township (Put In Bay)
12. Salem Township (Oak Harbor)

**Park district affiliation:**
- No Ottawa County Park District confirmed during bootstrap. Ottawa County is not known to have a standalone county park district. Verify at Tier 4.
- Toledo Metroparks operates Howard Marsh Metropark which straddles Lucas/Ottawa county line.

---

## Known Multi-County Entities (IMP-104)

Entities already in DB with Ottawa County in their counties field. Use `KNOWN_MC:{id}` in identity_notes_raw when encountered during discovery — do not create new records.

| DB ID | Name | Entity Type | Counties | Notes |
|-------|------|-------------|----------|-------|
| OH-MC-S-010 | Magee Marsh Wildlife Area | Site | Lucas;Ottawa | State Wildlife Area, 2202 ac |
| OH-MC-S-021 | Howard Marsh Metropark | Site | Lucas;Ottawa | Toledo Metroparks |
| OH-MC-TR-002 | Portage River Water Trail | Trail | Ottawa;Wood | Water trail |
| OH-MC-T-008 | Magee Marsh Boardwalk | Trail | Lucas;Ottawa | Trail within Magee Marsh WA |
| OH-OTT-T-072 | Howard Marsh Sandpiper Trail | Trail | Ottawa | Pre-assigned from Lucas run |
| OH-OTT-T-073 | Howard Marsh Mallard Trail | Trail | Ottawa | Pre-assigned from Lucas run |
| OH-OTT-T-074 | Howard Marsh Madewell Trail | Trail | Ottawa | Pre-assigned from Lucas run |
| OH-OTT-T-075 | Howard Marsh Egret Trail | Trail | Ottawa | Pre-assigned from Lucas run |
| OH-OTT-T-076 | Howard Marsh Sora Trail | Trail | Ottawa | Pre-assigned from Lucas run |

**Multi-county candidates from MULTI_COUNTY.xlsx — not yet in DB:**

| Name | Counties | Type | Notes |
|------|----------|------|-------|
| Ottawa National Wildlife Refuge | Lucas;Ottawa | Site | Has nature center; Tier 1 discovery |
| North Coast Inland Trail | Erie;Huron;Ottawa;Sandusky | Trail | ~100-mi paved rail trail; multi-county |
| Sandusky River | Crawford;Erie;Huron;Ottawa;Richland;Sandusky | Site | State Scenic River designation |
| Crane Creek State Park | Lucas;Ottawa | — | **No longer a site (dissolved)**; do not create entity; confirm during discovery |

**No held entities from prior runs reference Ottawa County.**

---

## Baseline Seeds (46 rows — Ottawa.xlsx)

Internalized as discovery prompts. Do NOT import directly — confirm through authoritative sources during tier discovery.

| Seed Name | Noted Type | Key Notes |
|-----------|-----------|-----------|
| African Safari Wildlife Park | Privately owned park | Drive-through safari |
| Catawba Island State Park | State Park | 677 ac |
| Continental Marsh | GNIS swamp | — |
| Coopers Woods | GNIS woods | — |
| Darby Marsh | GNIS swamp | — |
| East Harbor State Park | State Park / Hunting Area | 1831 ac; ODNR Parks |
| Eisenhour Marsh | GNIS swamp | — |
| Fox's Marsh Wildlife Area | State Wildlife Area | 133.49 ac; Ile Saint George (North Bass Island); 41.7117°N -82.8274°W |
| France Marsh | GNIS swamp | — |
| Great Egret Marsh Nature Preserve | TNC Nature Preserve | 150 ac; across from East Harbor SP |
| Green Island Wildlife Area | State Wildlife Area | 16 ac; all of Green Island in Lake Erie |
| Honey Point Wildlife Area | State Wildlife Area | 7.87 ac; Isle Saint George (North Bass) |
| Hotel Victory Site at South Bass Island | ODNR Historic Site | Ohio Historic Site #11; within South Bass Island SP |
| Hunter Marsh | GNIS swamp | — |
| Kuehnle Wildlife Area | State Wildlife Area | 19 ac; Middle Bass Island |
| Lakeside Daisy State Nature Preserve | State Nature Preserve | 19.09 ac (or 117 ac); permit required |
| Little Portage Wildlife Area | State Wildlife Area | 357 ac |
| Lockwood (Marshall) Cemetery | ODNR Historic Site | Ohio Historic Site #37; within East Harbor SP |
| Lonz Winery at Middle Bass Island | State Historic Winery / ODNR Historic Site | Ohio Historic Site #12; 124 ac; part of Middle Bass Island SP |
| Magee Marsh | GNIS swamp | Likely part of OH-MC-S-010 |
| Marblehead Lighthouse | ODNR Historic Site | Ohio Historic Site #3; within Marblehead Lighthouse SP |
| Marblehead Lighthouse State Park | State Park | 9 ac |
| Mazurik Lake Erie Access Wildlife Area | State Wildlife Area | 15.9 ac; 8957 North Shore Blvd, Lakeside-Marblehead, OH 43440 |
| Middle Bass Island State Park | State Park | 124 ac |
| Navarre Marsh | GNIS swamp | — |
| Navarre Marsh National Wildlife Refuge | National Wildlife Refuge | Separate from Ottawa NWR; confirm at T1 |
| Needles Eye | GNIS arch | — |
| North Bass Island | State Park / Hunting Area | ODNR Parks |
| Oak Point State Park | State Park | 677 ac; South Bass Island |
| Ottawa County Wildlife Area 1 | Public Hunting Area | 551 S Wonnell Rd, Port Clinton, OH 43452 |
| Ottawa County Wildlife Area 2 | Public Hunting Area | — |
| Ottawa National Wildlife Refuge - West Harbor Landing | NWR unit | 231 N Hickory Ridge Dr, Port Clinton, OH 43452; east of main refuge on Catawba Island |
| Port Clinton Pier | — | Verify type/management |
| Put-In-Bay City Park | — | Municipal park; Tier 6 |
| Put-In-Bay Fish Hatchery | — | Verify type/management |
| Ritter Marsh | GNIS swamp | — |
| Sand Beach Marsh | GNIS swamp | — |
| Schedel Arboretum & Gardens | — | In Elmore |
| South Bass Island State Park | State Park | 677 ac; fossilized glacial grooves |
| Starve Island Deep | GNIS prairie | — |
| Toussaint Creek Wildlife Area | State Wildlife Area | 225 ac |
| Toussaint Marsh | GNIS swamp | — |
| Turtle Creek Access | — | Verify type/management |
| Walter Ory Park | Elmore park | Tier 6 |
| West Harbor Wildlife Area | State Wildlife Area | — |
| Winous Point Marsh | GNIS swamp | — |

**GNIS marsh/swamp entries** (Continental, Coopers Woods, Darby, Eisenhour, France, Hunter, Magee, Navarre, Ritter, Sand Beach, Toussaint, Winous Point, Starve Island Deep, Needles Eye): These are GNIS geographic features. Each must be assessed individually for whether they produce a Site entity. Most are named natural features; several overlap with ODNR-managed units already in the list. Assess during appropriate tier — do not auto-create from GNIS name alone.

---

## Tiers Completed

### Tier 2 — State ✅ COMPLETE (2026-05-17)
- **Sites:** 20 (East Harbor SP; South Bass Island SP; Oak Point SP; Middle Bass Island SP; North Bass Island SP; Marblehead Lighthouse SP; Catawba Island SP; Toussaint Creek WA; Little Portage WA; Fox's Marsh WA; Honey Point WA; Kuehnle WA; Petersen Woods; Green Island WA; Mazurik Access Area; Dempsey Fishing Access; Sandusky Bay Bridge Access–North; Camp Perry Recreation Area; Lakeside Daisy SNP; Stone Lab Peach Point Campus)
- **Trails:** 24 (East Harbor SP: 11 trails; Middle Bass Island SP: 4 trails; Marblehead Lighthouse SP: 1; Lakeside Daisy SNP: 1; Magee Marsh WA: 7)
- **Trail Segments:** NULL — documented
- **Trail Networks:** NULL — documented (Lake Erie Islands Water Trail = T3 per §4.6)
- **Site Networks:** NULL — documented
- **Access Points:** 2 (Turtle Creek Access within OH-MC-S-010; East Harbor SP Marina)
- **KNOWN_MC confirmations:** OH-MC-S-010 (Magee Marsh WA) ✅; OH-MC-T-008 (Magee Marsh Boardwalk) ✅
- **Pending (flagged):** West Harbor WA, Ottawa County WA 1 & 2 (not found in coastal PDF; check ODNR hunting maps at normalization); Great Egret Marsh (defer T7 TNC); FWS Little Portage Unit (potential T1 miss)
- **IMP-080 physical file check:** PASS (60 T2 records verified in YAML; 92 total)
- **IMP-104 cross-county check:** PASS (8 Magee Marsh trails + Turtle Creek AP all flagged Ottawa;Lucas, inherit KNOWN_MC:OH-MC-S-010)
- **Key corrections from baseline:**
  - Catawba Island SP: ~10 ac (NOT 677 ac — baseline confusion with peninsula size)
  - South Bass Island SP: 33 ac (NOT 677 ac)
  - Oak Point SP: 1.5 ac (NOT 677 ac)
  - Marblehead Lighthouse SP: 13.5 ac (NOT 9 ac)
  - Little Portage WA: 407 ac (NOT 357 ac)
  - Fox's Marsh WA: 132 ac (NOT 133.49 ac)
  - Crane Creek SP dissolution CONFIRMED — absorbed into Magee Marsh WA (OH-MC-S-010)
  - Sandusky River scenic reach: does NOT extend into Ottawa County (Q6 resolved)
  - Lake Erie Islands Water Trail: T3 entity (managed by Put-in-Bay Township PD, per §4.6)
  - Green Island WA: NO PUBLIC ACCESS (bird sanctuary; flag for normalization)

### Tier 4 — County ✅ COMPLETE (2026-05-18)
- **Site Networks:** 1 (Park District of Ottawa County)
- **Sites:** 1 (Ottawa County Home Cemetery — county infirmary cemetery, IMP-099)
- **Trails:** 1 (Catawba Islander Trail — PLANNED, ~5 mi, PDOC project)
- **Trail Segments:** NULL — documented
- **Trail Networks:** NULL — documented
- **Access Points:** 1 (Ottawa County Fairgrounds PRWT Launch — AP on KNOWN_MC:OH-MC-TR-002)
- **T1 misses discovered at T4:** 5 FWS Ottawa NWR units (Marinewood, Turkey Run, Turtle Creek Island, Upper Toussaint, Little Portage Unit) — staged as T1 records
- **T7 deferred:** Nehls Memorial Nature Preserve (Black Swamp Conservancy-owned, FWS-partnered access — confirmed T7, deferred)
- **NRHP check (§3.3):** 31 Ottawa County NRHP listings reviewed; no county-owned bridge/structure NAP entity found. SR 51 bridge over Portage River (NRHP #94000239) noted as replaced 2020 (likely demolished); not an active visitor entity.
- **County cemeteries (IMP-099):** Ottawa County Home Cemetery confirmed — SR 163, Salem Township; county infirmary/poorhouse cemetery — staged
- **County golf courses (IMP-099):** None found. Former Marinewood Golf Course acquired by FWS 2014 (now NWR Marinewood Unit); no active county-operated golf course
- **County GIS (§3.2):** Ottawa County GIS is a survey/plat data map; no parks or open space layer found; no new entities
- **Visitors Bureau (§3.6):** Search rate-limited; primary parks and trails coverage confirmed complete via PDOC and county government website
- **Key findings:**
  - PDOC is primarily a grants/planning body — does not directly own parks/sites; directly manages trails (NCIT, PRWT, Catawba Islander)
  - Ottawa County Fairgrounds (operated by Ottawa County Agricultural Society) has PRWT kayak/canoe launch at SR 163 (Mile 7.8) — staged as AP
  - 5 Ottawa NWR units missed at T1: Marinewood, Turkey Run, Turtle Creek Island, Upper Toussaint, Little Portage Unit — all now staged
  - Nehls Memorial Nature Preserve (21 ac + 18 ac submerged, East Muggy Rd, Catawba Island Twp) — Black Swamp Conservancy-owned; FWS co-manages public access — confirmed T7, deferred
- **IMP-080 physical file check:** PASS — 122 records verified in YAML (111 pre-T4 + 11 staged: 4 T4 direct + 5 T1-miss + 2 tier_result NULLs)
- **IMP-104 cross-county check:** PASS — no new cross-county candidates at T4; Ottawa NWR T1-miss units all Ottawa County only (Turkey Run and Upper Toussaint to verify at normalization)

### Tier 3 — District ✅ COMPLETE (2026-05-17)
- **Sites:** 7 (PIBTPD: Ladd Carr Wildlife Woods; Dodge Woods Preserve; Massie Cliffside Preserve; Scheeff East Point Nature Preserve; Duff Homestead and Bayfront Preserve; Middle Bass Island Forested Wetlands Preserve; Middle Bass Island East Point Preserve)
- **Trails:** 8 (PIBTPD: Jane Coates Wildflower Trail; Dodge Woods Nature Trail; Massie Cliffside Preserve Trail; Scheeff East Point Nature Preserve Trail; Burgundy Bay Walking Trail; Middle Bass Island East Point Preserve Walking Path; Lake Erie Islands Water Trail [CROSS_COUNTY_CANDIDATE]; PDOC: North Coast Inland Trail [CROSS_COUNTY_CANDIDATE])
- **Trail Segments:** NULL — documented
- **Trail Networks:** NULL — documented
- **Site Networks:** NULL — documented
- **Access Points:** NULL — documented (PRWT launch sites are municipal/county APs; deferred to T6)
- **KNOWN_MC confirmations:** OH-MC-S-021 (Howard Marsh Metropark, Toledo Metroparks) ✅; OH-MC-TR-002 (Portage River Water Trail, PDOC) ✅
- **IMP-104 cross-county check:** PASS — OH-OTT-T-072 to -076 (Howard Marsh trails) confirmed as Ottawa County entities from Lucas County run; no new records created
- **T3 NULL entities:** Ottawa County SWCD (no land holdings per §4.7); Sand Beach Conservancy District (flood control entity, no natural areas)
- **Bootstrap correction:** Park District of Ottawa County confirmed to exist (Q1 resolved). Bootstrap error in handoff line 47 corrected.
- **Key findings:**
  - PIBTPD owns 7 publicly accessible natural area preserves on South Bass and Middle Bass islands
  - Duff Homestead and Bayfront Preserve (6.5 ac) acquired 2023 — post-2021 brochure, confirmed via PDOC grant page
  - Middle Bass Island Forested Wetlands Preserve = 3 tracts (Burgundy Bay 8 ac + Schneider 7.3 ac + Dieperink 7.6 ac = 22.9 ac); Hahn Property (~8.3 ac, status TBD)
  - Middle Bass Island East Point Preserve = 7.8 ac (NOT 11 ac — T3 handoff line 545 correction; brochure is authoritative)
  - North Coast Inland Trail staged as CROSS_COUNTY_CANDIDATE (T3, PDOC; 4-county trail not yet in DB)
  - Lake Erie Islands Water Trail staged as CROSS_COUNTY_CANDIDATE (T3, PIBTPD-managed per §4.6)
  - Portage River Water Trail = KNOWN_MC:OH-MC-TR-002 confirmed at T3; no new record
  - Little Portage Unit public access updated: Eagle Scout kayak launch 2023 — T2-FLAG-4 may resolve at normalization (Q24)
- **IMP-080 physical file check:** PASS (19 T3 records verified in YAML; 111 total)
- **IMP-104 cross-county check:** PASS (North Coast Inland Trail and Lake Erie Islands Water Trail both flagged CROSS_COUNTY_CANDIDATE; Howard Marsh confirmed)

### Tier 1 — Federal & Tribal ✅ COMPLETE (2026-05-17)
- **Sites:** 5 (Ottawa NWR main, Navarre Marsh unit, West Harbor Landing unit, Perry's Victory, Confederate Stockade Cemetery)
- **Trails:** 17 (16 named hiking trails + Wildlife Drive auto tour at Ottawa NWR; TRAIL_TYPE_REVIEW on Wildlife Drive)
- **Trail Segments:** NULL — documented
- **Trail Networks:** NULL — documented
- **Site Networks:** 1 (Ottawa NWR Complex, cross-county Ottawa/Lucas)
- **Access Points:** 2 (Ottawa NWR visitor center entrance, trailhead parking)
- **USFS / USACE / BLM / DoD / Tribal:** all NULL — documented
- **IMP-080 physical file check:** PASS (32 records verified in YAML)
- **IMP-104 cross-county check:** PASS (Ottawa NWR, Metzger Marsh Trail, Ottawa NWR Complex all flagged CROSS_COUNTY_CANDIDATE)

---

## Tiers Remaining

| Tier | Scope | Entry Points |
|------|-------|-------------|
| ~~T1~~ | ~~Federal~~ | ~~COMPLETE~~ |
| ~~T2~~ | ~~State~~ | ~~COMPLETE~~ |
| ~~T3~~ | ~~District~~ | ~~COMPLETE~~ |
| ~~T4~~ | ~~County~~ | ~~COMPLETE~~ |
| T5 | Township | 12 townships — use Website column from Townships_Officials2022-2023.xlsx |
| T6 | Municipal | Port Clinton, Oak Harbor, Elmore, Genoa, Lakeside-Marblehead, Put-in-Bay; island municipalities (Put-in-Bay, Middle Bass, North Bass) require separate treatment |
| T7 | Conservancy | The Nature Conservancy (Great Egret Marsh Nature Preserve), Black Swamp Conservancy, other land trusts |
| T8 | Private | African Safari Wildlife Park, Winous Point (private hunting club/marsh), Schedel Arboretum, other private |

---

## Pre-Discovery Checklist — Tier 1 (Federal) ✅ COMPLETE

**U.S. Fish & Wildlife Service:**
- [x] Ottawa National Wildlife Refuge — https://www.fws.gov/refuge/ottawa — CONFIRMED; 8,000+ ac; 17 trails staged; child sites: Navarre Marsh, West Harbor Landing
- [x] Navarre Marsh NWR — CONFIRMED as unit of Ottawa NWR (not separate refuge); restricted access; near Davis-Besse Nuclear Power Station; staged
- [x] West Harbor Landing — CONFIRMED as Ottawa NWR child unit on Catawba Island; 231 N Hickory Ridge Dr; staged
- [x] Cedar Point National Wildlife Refuge — CONFIRMED in **Lucas County** (not Ottawa); ~2,500 ac; managed from Ottawa NWR complex; OUT OF SCOPE for Ottawa County discovery
- [x] West Sister Island NWR — CONFIRMED in **Lucas County** (Birding Hotspots: Lucas, OH); 80 ac; OUT OF SCOPE for Ottawa County
- [x] Green Island Wildlife Area — baseline lists as State Wildlife Area; confirmed no federal designation; will confirm at T2 ODNR

**National Park Service:**
- [x] Perry's Victory and International Peace Memorial — CONFIRMED; 25 ac; South Bass Island (Put-in-Bay); staged
- [x] No other NPS units in Ottawa County identified

**U.S. Army Corps of Engineers:**
- [x] USACE — NULL; no project sites or recreation areas in Ottawa County; Lake Erie navigation is USACE but produces no Site entities

**VA National Cemetery Administration (IMP-111):**
- [x] Confederate Stockade Cemetery — CONFIRMED in Ottawa County (Danbury Township, Johnson's Island); staged
- [x] Ohio Soldiers' Lots list reviewed — no additional VA Soldiers' Lots in Ottawa County
- [x] Ohio Veterans Home Cemetery (Sandusky) — Erie County, not Ottawa; out of scope

**BLM / DoD / Tribal:**
- [x] BLM — NULL; no surface holdings in Ottawa County
- [x] DoD — NULL; no public-access military lands in Ottawa County
- [x] Tribal — NULL; no tribal trust lands or fee-simple holdings in Ohio/Ottawa County

---

## Entities Discovered

### Tier 3 — District (2026-05-17) — 19 records staged

**Sites (7 — all PIBTPD):**
| Raw Name | Governance | Key Notes |
|----------|-----------|-----------|
| Ladd Carr Wildlife Woods | PIBTPD | 9.1 ac; South Bass Island; Put-in-Bay Rd; alt name: Jane Coates Wildflower Trail and Ladd Carr Wildlife Woods |
| Dodge Woods Preserve | PIBTPD | 3.6 ac; South Bass Island; Thompson/Langram Roads; StoryWalk® |
| Massie Cliffside Preserve | PIBTPD | 11 ac; South Bass Island; SR 357 East Point; dolomite cliffs; dock |
| Scheeff East Point Nature Preserve | PIBTPD | 9.1 ac; South Bass Island; SR 357 East Terminus; 1700 ft shoreline |
| Duff Homestead and Bayfront Preserve | PIBTPD | 6.5 ac; South Bass Island; acquired 2023; 150 ft lakefront; visitor center |
| Middle Bass Island Forested Wetlands Preserve | PIBTPD | 22.9 ac (Burgundy Bay 8 + Schneider 7.3 + Dieperink 7.6); Middle Bass Island; Fox Rd |
| Middle Bass Island East Point Preserve | PIBTPD | 7.8 ac (NOT 11 ac); Middle Bass Island; North Shore Rd; kayak/canoe only access |

**Trails (8):**
| Raw Name | Parent / Managing Entity | Length (mi) |
|----------|--------------------------|-------------|
| Jane Coates Wildflower Trail | Ladd Carr Wildlife Woods (PIBTPD) | 0.48 (2,550 ft), looped |
| Dodge Woods Nature Trail | Dodge Woods Preserve (PIBTPD) | 0.16 (852 ft), looped; mulched; StoryWalk® |
| Massie Cliffside Preserve Trail | Massie Cliffside Preserve (PIBTPD) | 0.33 (1,750 ft); rugged/hazardous |
| Scheeff East Point Nature Preserve Trail | Scheeff East Point Nature Preserve (PIBTPD) | 0.42 (2,205 ft), looped |
| Burgundy Bay Walking Trail | Middle Bass Island Forested Wetlands Preserve (PIBTPD) | TBD; natural surface |
| Middle Bass Island East Point Preserve Walking Path | Middle Bass Island East Point Preserve (PIBTPD) | TBD; kayak/canoe access to site |
| Lake Erie Islands Water Trail | PIBTPD (managed) | TBD; CROSS_COUNTY_CANDIDATE; water trail; island loops |
| North Coast Inland Trail | Park District of Ottawa County (Ottawa County segment) | TBD (Ottawa segment); CROSS_COUNTY_CANDIDATE; paved multi-use rail trail; 4 counties |

**KNOWN_MC Confirmations (no new records):**
- OH-MC-S-021 (Howard Marsh Metropark, Toledo Metroparks) — confirmed
- OH-MC-TR-002 (Portage River Water Trail, PDOC) — confirmed; 8 Ottawa County launches documented
- OH-OTT-T-072 to -076 (Howard Marsh 5 trails) — IMP-104 PASS

**T3 NULL Results (4 tier_result records staged):**
- Ottawa County SWCD — no land holdings
- Sand Beach Conservancy District — flood control entity, no natural areas

---

### Tier 1 — Federal (2026-05-17) — 32 records staged

**Sites (5):**
| Raw Name | Governance | Key Notes |
|----------|-----------|-----------|
| Ottawa National Wildlife Refuge | USFWS | 8,000+ ac; 14000 W SR-2, Oak Harbor; GPS 41.6075, -83.2096; CROSS_COUNTY_CANDIDATE (Ottawa/Lucas) |
| Ottawa NWR — Navarre Marsh Unit | USFWS | Restricted/permit only; near Davis-Besse; ~820 ac; child of Ottawa NWR |
| Ottawa NWR — West Harbor Landing | USFWS | 231 N Hickory Ridge Dr, Port Clinton; Catawba Island; child of Ottawa NWR |
| Perry's Victory and International Peace Memorial | NPS | 25 ac; South Bass Island; PO Box 549, Put-in-Bay OH 43456; phone 419-285-2184 |
| Confederate Stockade Cemetery | VA / NCA | Johnson's Island, Danbury Twp, Ottawa Co; ~1 ac; 206 graves; mailing: Sandusky OH 44870 |

**Trails (17):**
| Raw Name | Length (mi) | Difficulty | Season |
|----------|------------|-----------|--------|
| VC Boardwalk Trail | 0.36 | Easy, ADA | Year round |
| Estuary Trail | 0.54 | Moderate | Seasonal (Dec–Oct daily; Oct–Nov Sat PM/Sun) |
| Grimm Prairie Trail | 0.39 | Easy | Year round |
| John Gallagher Trail | 0.99 | — | — |
| Krause Road Trail | 0.27 | — | — |
| Lakeshore Preserve Trail | 1.30 | — | — |
| Marinewood Trail | 2.46 | — | — |
| Metzger Marsh Trail | 0.44 | — | — (may be Lucas Co; CROSS_COUNTY_CANDIDATE) |
| Middle Toussaint Trail | 8.06 | — | — |
| Ottawa Wildlife Interpretive Trail | 1.22 | Easy | Year round |
| Partnership Trail | 1.41 | Easy | Year round |
| Pool 1 West Trail | 0.22 | — | — |
| VC Fishing Pond Trail | 0.06 | — | — |
| West Harbor Landing Trail | 1.61 | Easy | Seasonal (Apr 1–Sep 15) |
| Woodies Roost Trail | 0.40 | Easy | Seasonal (Apr 1–Sep 15) |
| York Tract Trail | — | — | — (length not on page) |
| Ottawa NWR Wildlife Drive | 7.0 | — | Auto tour route; TRAIL_TYPE_REVIEW |

**Trail Segments:** NULL (documented — no segment triggers at any T1 entity)
**Trail Networks:** NULL (documented — no formal named network identity at T1)

---

### Tier 2 — State (2026-05-17) — 60 records staged

**Sites (20):**
| Raw Name | Governance | Key Notes |
|----------|-----------|-----------|
| East Harbor State Park | ODNR Parks | 1831 ac; Danbury Twp; 11 trails + multiuse; glacial grooves; Lockwood Cemetery (Historic #37) |
| South Bass Island State Park | ODNR Parks | 33 ac (NOT 677); South Bass Island; Hotel Victory ruins (Historic #11) |
| Oak Point State Park | ODNR Parks | 1.5 ac (NOT 677); smallest state park in Ohio; South Bass Island |
| Middle Bass Island State Park | ODNR Parks | 124 ac; Middle Bass Island; Lonz Winery (Historic #12); ADA Lonz Trail; 184-slip marina |
| North Bass Island State Park | ODNR Parks | 593 ac; North Bass Island (Isle St. George); primitive camping; remote |
| Marblehead Lighthouse State Park | ODNR Parks | 13.5 ac (NOT 9); Marblehead; oldest Great Lakes lighthouse (1821; Historic #3) |
| Catawba Island State Park | ODNR Parks | ~10 ac (NOT 677); Catawba Island Twp; day-use boat ramp only; island parks HQ |
| Toussaint Creek Wildlife Area | ODNR Wildlife | 225 ac; 5 mi north Oak Harbor; managed wetlands; GPS TBD |
| Little Portage Wildlife Area | ODNR Wildlife | 407 ac (NOT 357); SE of Oak Harbor; 2024 H2Ohio restoration; FWS LP Unit flag |
| Fox's Marsh Wildlife Area | ODNR Wildlife | 132 ac (NOT 133.49); North Bass Island; boat/paddle access only |
| Honey Point Wildlife Area | ODNR Wildlife | acreage TBD; North Bass Island; no road access |
| Kuehnle Wildlife Area | ODNR Wildlife + Put-in-Bay Twp PD | 20 ac; Middle Bass Island; Hauncks Pond; isthmus location |
| Petersen Woods | ODNR Wildlife + Put-in-Bay Twp PD | 2 ac; Middle Bass Island; adjacent Kuehnle |
| Green Island Wildlife Area | ODNR Wildlife | 16 ac est; Lake Erie island; NO PUBLIC ACCESS (bird sanctuary) |
| Mazurik Lake Erie Access Wildlife Area | ODNR | 15.9 ac; 8957 North Shore Rd, Marblehead; 4-lane boat ramp |
| Dempsey Fishing Access | ODNR | 66.8 ac; Bay Shore Rd south of Hartshorn, Danbury Twp; Sandusky Bay |
| Sandusky Bay Bridge Access — North | State | ~1-mi causeway; Danbury Twp; former bridge approach; ADA fishing deck |
| Camp Perry Recreation Area | Ohio National Guard | 640 ac; Erie Twp; beach/pier publicly accessible; world's largest outdoor rifle range |
| Lakeside Daisy State Nature Preserve | ODNR DNAP | 137 ac total (19 orig + 118 expansion); 309 Alexander Pike, Marblehead; federally threatened Lakeside Daisy; alvar; glacial grooves |
| Stone Laboratory Peach Point Campus | OSU / ODNR Wildlife | South Bass Island; T2 per §4.7; public fishing dock; Aquatic Visitor Center (2024); oldest freshwater field station in US |

**Trails (24):**
| Raw Name | Parent Site | Length (mi) |
|----------|------------|------------|
| Middle Harbor Trail | East Harbor SP | 0.75 |
| Middle Harbor Extension | East Harbor SP | 0.5 |
| Meadow Trail | East Harbor SP | 0.75 |
| Blackberry Trail | East Harbor SP | 0.25 |
| Red Bird Trail | East Harbor SP | 0.25 |
| Rock Garden Loop | East Harbor SP | 0.3 |
| Wetlands Trail | East Harbor SP | 2.0 |
| South Beach Trail | East Harbor SP | 2.5 |
| Water's Edge Trail | East Harbor SP | 1.0 |
| Channel Dunes Loop | East Harbor SP | 0.5 |
| West Harbor Trail | East Harbor SP | 0.75 |
| ADA Lonz Trail | Middle Bass Island SP | 1.3 (paved, ADA) |
| Campground Loop Trail | Middle Bass Island SP | TBD |
| Old Campground Trail | Middle Bass Island SP | TBD |
| Rocky Shore Trail | Middle Bass Island SP | TBD |
| Marblehead Lighthouse ADA Path | Marblehead Lighthouse SP | TBD |
| Lakeside Daisy Trail | Lakeside Daisy SNP | TBD |
| Magee Marsh Walking Trail — West Loop | Magee Marsh WA (OH-MC-S-010) | 0.5 |
| Magee Marsh Walking Trail — Bear Pond Loop | Magee Marsh WA (OH-MC-S-010) | 0.7 |
| Wildlife Beach Trail | Magee Marsh WA (OH-MC-S-010) | 0.7 |
| Crane Creek Estuary Trail | Magee Marsh WA (OH-MC-S-010) | 0.6 (CROSS_SITE_FLAG) |
| Magee-Ottawa Partnership Trail — Magee Segment | Magee Marsh WA (OH-MC-S-010) | 0.5 (CROSS_SITE_FLAG) |
| Goose Haven Trail | Magee Marsh WA (OH-MC-S-010) | 0.7 (seasonal Apr 15–Aug 31) |
| Lakefront Levee Trail | Magee Marsh WA (OH-MC-S-010) | 0.3 (seasonal Apr 15–May 31) |

**Trail Segments:** NULL (documented)
**Trail Networks:** NULL (documented — Lake Erie Islands Water Trail deferred to T3)
**Site Networks:** NULL (documented)

**Access Points (2):**
| Raw Name | AP Type | Parent |
|----------|---------|--------|
| Magee Marsh WA — Turtle Creek Access | Boat Launch / Fishing | OH-MC-S-010 |
| East Harbor State Park Marina | Marina / Boat Launch | East Harbor State Park |

**Site Networks (1):**
| Raw Name | Counties | Notes |
|----------|---------|-------|
| Ottawa National Wildlife Refuge Complex | Ottawa; Lucas | USFWS complex identity; members: Ottawa NWR, Cedar Point NWR, West Sister Island NWR; CROSS_COUNTY_CANDIDATE |

**Access Points (2):**
| Raw Name | AP Type | Address |
|----------|---------|---------|
| Ottawa NWR — Visitor Center Entrance | Trailhead / Refuge Entrance | 14000 W SR-2, Oak Harbor OH 43449; GPS 41.6075, -83.2096 |
| Ottawa NWR — Trailhead Parking Lot | Trailhead | Ottawa NWR, Oak Harbor OH (separate from VC; GPS needed) |

---

## Held Entities

*(none)*

---

## Unresolved Baseline Seeds

*(all 46 seeds unresolved — pending tier-by-tier confirmation)*

---

## Open Questions

1. ~~Does Ottawa County have an independent county park district?~~ **RESOLVED T3:** **Park District of Ottawa County** (also "Ottawa County Parks District") confirmed via Ohio Auditor (Park/Recreation District, audit history 2022–2023). Website: ottawacountyparksoh.org. Bootstrap error — initial seed said "not confirmed." CORRECTED. **Note: baseline handoff line 47 ("No Ottawa County Park District confirmed") is incorrect and should be disregarded.**
2. ~~Is Navarre Marsh NWR a standalone NWR or a unit of Ottawa NWR?~~ **RESOLVED T1:** Navarre Marsh is a managed unit of Ottawa NWR, restricted access. Not a standalone refuge.
3. Green Island Wildlife Area — baseline says State Wildlife Area; USFWS search returned no federal unit; **confirm at T2 ODNR.**
4. West Harbor Wildlife Area — baseline lists as State Wildlife Area; **confirm at T2 ODNR.** No federal unit found at T1.
5. ~~North Coast Inland Trail — multi-county rail trail; managing entity TBD.~~ **RESOLVED T3:** Confirmed T3 entity. Managing entity = **Park District of Ottawa County (PDOC)** for Ottawa County segment. Trail extends ~100 mi Lorain to Genoa through Erie;Huron;Sandusky;Ottawa counties. Ottawa segment: Sandusky County line NW through Elmore to Genoa (Veterans Park terminus). Staged as CROSS_COUNTY_CANDIDATE at T3. Also US Bike Route 30. MULTI_COUNTY.xlsx listed (not yet in DB as of bootstrap).
6. ~~Sandusky River State Scenic River designation.~~ **RESOLVED T2:** Designated reach is Upper Sandusky to Fremont (65 mi), entirely within Crawford/Wyandot/Sandusky counties. River mouth is in Sandusky County. Ottawa County has NO designated reach. MULTI_COUNTY.xlsx Ottawa County entry is an error. No Site entity for Ottawa County.
7. ~~Ottawa NWR West Harbor Landing — is this an Access Point or a separate Site?~~ **RESOLVED T1:** Staged as a child Site of Ottawa NWR (distinct location unit with its own trail).
8. ~~Crane Creek State Park dissolution.~~ **RESOLVED T2:** Confirmed dissolved. ODNR coastal PDF: "The wildlife area [Magee Marsh] includes the former Crane Creek State Park." Absorbed into OH-MC-S-010. No entity created.
9. GNIS marsh/swamp entries — 12+ marsh names in baseline. Each needs independent assessment for Site entity eligibility. Many overlap with ODNR units. **Assess as encountered at T2.**
10. Island townships (Put-In-Bay Township) — Tier 6 island treatment applies; enumerate island municipalities before T6.
11. Howard Marsh trails (OH-OTT-T-072 to -076) — in DB from Lucas run. **Confirm at T3 (Toledo Metroparks)** that IDs and trail count are correct.
12. ~~Portage River Water Trail (OH-MC-TR-002) — confirm at T3/T4.~~ **RESOLVED T3:** **KNOWN_MC:OH-MC-TR-002 confirmed**. PDOC (Park District of Ottawa County) manages Ottawa County segment. 36-mi paddle trail, officially state-designated 2022-07-19. Ottawa County launch sites (Mile 0–23): Lake Erie Beach Access (Port Clinton, Mile 0), Portage River SWA (Mile 2, walking trail also), Marinewood Unit FWS (Mile 4.8), Little Portage Unit (Mile 3.7, Eagle Scout kayak launch 2023), Ottawa County Fairgrounds (Mile 7.8), Oak Harbor Interurban Overlook (Mile 12.7, ADA), Elmore-Riverbend Park (Mile 22), Harry Witty Memorial Park (Mile 23). No new T3 record created (KNOWN_MC). AP entities for individual launches deferred to T6/municipal tier.
13. Ottawa NWR Wildlife Drive — 7-mile auto tour route staged as Trail (use_type: Auto Tour) with TRAIL_TYPE_REVIEW flag. Verify whether auto tour routes qualify as Trail entities under NAP vocabulary at normalization.
14. Grimm Prairie Trail vs. John Gallagher Trail — FWS page narrative references "Gallagher Memorial Trail" at 0.3 mi (BSBO offices) and the structured listing shows both "Grimm Prairie Trail" (0.39 mi) and "John Gallagher Trail" (0.99 mi) as distinct entries. May be three trails total, or two with a naming inconsistency. **Verify against FWS map at GPS acquisition pass.**
15. Metzger Marsh Trail — staged with counties Ottawa;Lucas pending GIS confirmation of physical location. If purely Lucas County, remove from Ottawa records. **Verify county during normalization.**
16. Johnson's Island access — Confederate Stockade Cemetery is on Johnson's Island (Ottawa County). The island is privately owned; access is via a causeway from Danbury Township. **Note at T6: check whether Johnson's Island has any township/municipal public parks or open spaces.**
17. West Harbor Wildlife Area — not found at T2 in ODNR coastal PDF. May be a small ODNR hunting area. **Confirm via ODNR hunting area maps at normalization. Do NOT confuse with USFWS West Harbor Landing (T1).**
18. Ottawa County Wildlife Area 1 (551 S Wonnell Rd, Port Clinton) and Wildlife Area 2 — not found at T2. **Confirm via ODNR hunting area maps at normalization.**
19. Green Island Wildlife Area — confirmed NO PUBLIC ACCESS per ODNR (bird sanctuary, closed). **Flag for normalization: does no-public-access preclude NAP entity? Compare to Navarre Marsh (T1, staged with restricted access).**
20. FWS Little Portage Unit — FWS page exists at fws.gov/refuge/ottawa/visit-us/locations/little-portage-unit. Birding Hotspots: "view from roadside only." **Potential T1 miss. Check if FWS land parcel meets public-access threshold for NAP entity. Flag for normalization review.**
21. Crane Creek Estuary Trail at Magee Marsh WA — CROSS_SITE_FLAG with T1 "Estuary Trail" (0.54 mi) at Ottawa NWR. May be same physical trail described from both property pages. **Verify at GPS acquisition pass.**
22. Magee-Ottawa Partnership Trail — Magee Segment (0.5 mi) may be same physical trail as T1 "Partnership Trail" (1.41 mi from Ottawa NWR side). These are two measurements of the same trail from different agency sources OR two segments of a cross-property trail. **Verify at GPS acquisition pass whether to merge or keep as two segment records.**
23. Great Egret Marsh Nature Preserve (150 ac, Danbury Twp) — baseline says TNC; not found in ODNR DNAP. **Confirm at T7 (The Nature Conservancy).**
24. FWS Little Portage Unit — **partial resolution T3:** PDOC Portage River Water Trail page lists "Little Portage Unit" at Mile 3.7 with an Eagle Scout kayak launch (constructed 2023). This contradicts prior "view from roadside only" status (T2-FLAG-4). If the kayak launch is on FWS land, the unit now has public water access. **Re-evaluate T2-FLAG-4 at normalization; may qualify as T1 FWS child entity of Ottawa NWR.**
25. Middle Bass Island East Point Preserve trail — access by canoe/kayak only; walking path length not specified in brochure. **Obtain GPS and length at GPS acquisition pass.**
26. Burgundy Bay walking trail — length not stated in PIBTPD brochure. **Obtain at GPS acquisition pass.**
27. Duff Homestead and Bayfront Preserve — acquired 2023; visitor center converting (opening summer 2024). **Confirm visitor center/public access status; obtain GPS at GPS acquisition pass.**
28. PIBTPD non-public parcels — brochure lists 7 parcels not open to public (South Bass: Woischke Woods 2 ac, Gump Woods 0.5 ac, Knam Purchase 4 ac, Victory Woods–Foley 0.5 ac; Middle Bass: Prokesh/Watson 1 ac, Costello Tract 4 ac, Hahn Property ~8.3 ac). **Not staged as NAP entities (no public access). Note in pipeline for normalization review if access status changes.**
29. Hahn Property (Middle Bass, 8.3 ac) — listed as "under contract" in 2021 PIBTPD brochure. **Check 2023 Annual Report or current PIBTPD website to confirm acquisition status; if acquired, note as part of Forested Wetlands Preserve complex but not staged separately (no public access per 2021 status).**
30. Ottawa NWR Marinewood Unit — address confirm: SR 163 between Oak Harbor and Port Clinton (old Marinewood Golf Course, acquired FWS 2014). PRWT source lists launch at Mile 4.8 as "4640 W Harbor Rd., Port Clinton." **Confirm physical address and GPS at GPS acquisition pass.**
31. Ottawa NWR Turkey Run Unit — county uncertain: described as ~16 mi SE of main refuge, near Little Portage River. **Verify Ottawa vs. adjacent county (Sandusky?) via GIS at normalization.**
32. Ottawa NWR Upper Toussaint Unit — 77 ac, Toussaint River between Rocky Ridge and Lickert-Harder Roads. **Verify county at normalization — Toussaint River area could be Ottawa or Sandusky county.**
33. Ottawa NWR Turtle Creek Island Unit — Duff-Washa Rd, ~4 mi SE of main complex. **Confirm county and GPS at normalization.**
34. Ottawa NWR Little Portage Unit — FWS page now shows "access for paddlers is being installed"; open for fishing sunrise to sunset. Kayak launch confirmed at Mile 3.7 (Eagle Scout 2023). **Confirm whether T1-miss should be staged as child of Ottawa NWR or standalone unit; GPS 7899 W Little Portage East Rd., Oak Harbor.**
35. Ottawa County Home Cemetery — SR 163, Salem Township, 1/4 mile west of Co. Rd. 104. **Obtain GPS coordinates at GPS acquisition pass; confirm county ownership/operation vs. township management.**
36. Catawba Islander Trail — PDOC planned trail, ~5 mi Catawba Island N to S, master plan July 2023. Phase 1 route mapped. **Confirm build status and Phase 1 extent at next research cycle; update PLANNED flag when construction confirmed.**
37. Ottawa County Fairgrounds PRWT Launch address: PDOC grant page shows "770 SE Catawba Rd., Port Clinton, OH 43452" (phone 419-707-4051); PRWT source shows "7870 W State Route 163, Oak Harbor" (Mile 7.8). **These appear to be different addresses — verify physical location of PRWT kayak launch vs. fairgrounds main address. Use SR 163 address for AP record.**

---

## Pre-Discovery Checklist — Tier 2 (State)

*Written per IMP-029 before fetching any T2 pages. 2026-05-17.*

**ODNR Find-a-Property (§3.0 mandatory first — JS-rendered):**
- [ ] https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property — enumerate all Ottawa County properties by type

**ODNR State Parks:**
- [ ] East Harbor State Park — ~1831 ac; Danbury Twp; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/east-harbor-state-park
- [ ] South Bass Island State Park — ~677 ac; South Bass Island; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/south-bass-island-state-park
- [ ] Oak Point State Park — South Bass Island; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/oak-point-state-park
- [ ] Middle Bass Island State Park — ~124 ac; Middle Bass Island; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/middle-bass-island-state-park
- [ ] North Bass Island State Park — North Bass Island; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/north-bass-island-state-park
- [ ] Marblehead Lighthouse State Park — ~9 ac; Danbury Twp; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/marblehead-lighthouse-state-park
- [ ] Catawba Island State Park — ~677 ac; Catawba Island Twp; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/catawba-island-state-park
- [ ] Crane Creek State Park — baseline notes "dissolved/no longer a site"; CONFIRM dissolution; do NOT create entity unless contradicted

**ODNR Wildlife Areas:**
- [ ] Little Portage Wildlife Area — 357 ac; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/little-portage-wildlife-area
- [ ] Toussaint Creek Wildlife Area — 225 ac; https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/toussaint-creek-wildlife-area
- [ ] Mazurik Lake Erie Access Wildlife Area — 15.9 ac; 8957 North Shore Blvd, Lakeside-Marblehead
- [ ] Fox's Marsh Wildlife Area — 133.49 ac; North Bass Island (Île Saint George); https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property/foxs-marsh-wildlife-area
- [ ] Green Island Wildlife Area — 16 ac; Lake Erie island; confirm ODNR management
- [ ] Honey Point Wildlife Area — 7.87 ac; North Bass Island; confirm ODNR management
- [ ] Kuehnle Wildlife Area — 19 ac; Middle Bass Island; confirm ODNR management
- [ ] Ottawa County Wildlife Area 1 — 551 S Wonnell Rd, Port Clinton; confirm ODNR management
- [ ] Ottawa County Wildlife Area 2 — address TBD; confirm ODNR management
- [ ] West Harbor Wildlife Area — confirm ODNR management and acreage
- [ ] Magee Marsh Wildlife Area — KNOWN_MC:OH-MC-S-010 (Lucas;Ottawa); confirm Ottawa County portion; use existing ID — no new record
- [ ] ODNR Hunting Area Maps — scan for any additional Ottawa County hunting areas (§3.3)
- [ ] ODNR Fishing Lake Maps / River & Stream Fishing Maps — scan for Ottawa County fishing access sites (§3.3)

**ODNR Division of Natural Areas & Preserves (DNAP):**
- [ ] Lakeside Daisy State Nature Preserve — 19.09 ac (or 117 ac with buffer zone); permit required; Marblehead
- [ ] Great Egret Marsh Nature Preserve — 150 ac; listed as TNC in baseline — confirm if ODNR DNAP registered or TNC-only (if TNC: T7)
- [ ] ODNR DNAP Ottawa County search — https://ohiodnr.gov/go-and-do/plan-a-visit/find-a-property — check for additional SNPs

**ODNR Historic Sites (§4.1 — JS-rendered):**
- [ ] Marblehead Lighthouse — Ohio Historic Site #3; within Marblehead Lighthouse SP; https://ohiodnr.gov/discover-and-learn/history-culture/ohio-history-connection/ohio-historic-sites
- [ ] Hotel Victory Site at South Bass Island — Ohio Historic Site #11; within South Bass Island SP
- [ ] Lonz Winery at Middle Bass Island — Ohio Historic Site #12; within Middle Bass Island SP (~124 ac)
- [ ] Lockwood (Marshall) Cemetery — Ohio Historic Site #37; within East Harbor SP
- [ ] New Deal Era Sites scan — check for CCC/WPA-era structures in Ottawa County state parks (§4.1)

**Ohio EPA Scenic Rivers:**
- [ ] Sandusky River — confirm if designated reach extends into Ottawa County (headwaters upstream, drains to Sandusky Bay); check https://epa.ohio.gov/divisions-and-offices/surface-water/scenic-rivers
- [ ] Other Ottawa County streams — Toussaint Creek, Portage River — check for state scenic river designation

**Ohio Turnpike / OTIC (§4.5):**
- [ ] I-80/90 corridor — runs along southern edge of Ottawa County; check for rest areas or public access areas; https://www.ohioturnpike.org — applicable per §4.5

**Water Trail Confirmation (§4.6 — management tier governs):**
- [ ] Portage River Water Trail (OH-MC-TR-002) — already in DB; check if Ottawa County segment requires Trail Segment record; management entity is Ottawa County (Q12)
- [ ] Lake Erie Water Trail — check for any designated water trail segments in Ottawa County waters
- [ ] Sandusky Bay water trail — check for designated paddle routes

**Known MC Entities to confirm at T2:**
- [ ] OH-MC-S-010 (Magee Marsh Wildlife Area) — confirm appears at ODNR Wildlife Areas; use KNOWN_MC:OH-MC-S-010
- [ ] OH-MC-T-008 (Magee Marsh Boardwalk) — confirm appears within Magee Marsh WA; use KNOWN_MC:OH-MC-T-008
- [ ] OH-MC-TR-002 (Portage River Water Trail) — confirm management entity and Ottawa County segment status

**Public University Natural Areas (§4.7):**
- [ ] Bowling Green State University — Firelands Campus is in Huron County (not Ottawa); check if BGSU has any field stations or natural areas in Ottawa County
- [ ] Ohio State University Stone Lab — island research station on Gibraltar Island, Put-in-Bay; confirm if public-access entity or research-only

**ODOT Rest Areas:**
- [ ] Check I-80/90 rest areas in Ottawa County — if any, document as AP-type entities (§4.5)

---

## Next Steps

1. ~~T2 State discovery~~ ✅ COMPLETE
2. ~~T3 District discovery~~ ✅ COMPLETE
3. ~~T4 County discovery~~ ✅ COMPLETE
4. **→ Begin Tier 5 (Township) discovery** — 12 Ottawa County townships
   - Priority: Danbury Township (Lake Point Park 8.7 ac, Meadowbrook Marsh PDOC-funded, War of 1812 Battle Site, Benajah Wolcott House)
   - Catawba Island Township (Catawba Point Preserve, Cedar Meadow Preserve, Nehls Memorial Nature Preserve access trail)
   - Carroll Township, Allen Township, other rural townships
   - Use Website column from Townships_Officials2022-2023.xlsx; check county-hosted township pages (§3.7)
   - Johnson's Island (Q16): check Danbury Township for any public parks/open spaces on island
5. After T5: T6 (Municipal) — Port Clinton, Oak Harbor, Elmore, Genoa, Lakeside-Marblehead, Put-in-Bay; island municipalities; Waterworks Park (OT4), Port Clinton Lakefront Preserve (OT5), Port Clinton City Beach (OT6), DeRivera Park, Captain Alfred Parker Park, Genoa Veterans Park (NCIT terminus), Elmore-Riverbend Park, Harry Witty Memorial Park
6. After T6: T7 (Conservancy) — TNC (Great Egret Marsh Nature Preserve, Q23); Black Swamp Conservancy (Nehls Memorial Nature Preserve owner, Port Clinton Lakefront Preserve easement); Lake Erie Islands Conservancy (check if owns land separately from PIBTPD)
7. After T7: T8 (Private) — African Safari Wildlife Park, Winous Point Marsh (private hunting club), Schedel Arboretum (Elmore), Lakeside Chautauqua (walking trail, gated community)

---

## Captured Source Data

### T1 — Ottawa NWR Trails (from fws.gov/refuge/ottawa/visit-us/trails, 2026-05-17)

| Trail Name | Length (mi) | Difficulty | Surface | Season | Notes |
|-----------|------------|-----------|---------|--------|-------|
| VC Boardwalk Trail | 0.36 | Easy, ADA | Boards and stone | Year round | Behind visitor center; wetland + woods |
| Estuary Trail | 0.54 | Moderate | Stone, grass, sand | Dec–Oct (daily); Oct–Nov (Sat PM–Sun) | W of Magee Marsh beach; from Magee Marsh parking or Pool 1 trail Apr 15–Sep 1 |
| Grimm Prairie Trail | 0.39 | Easy | Gravel | Year round | Behind BSBO offices; access from Partnership Trail or BSBO |
| John Gallagher Trail | 0.99 | — | — | — | Distinct from Grimm Prairie Trail; see Q14 |
| Krause Road Trail | 0.27 | — | — | — | — |
| Lakeshore Preserve Trail | 1.30 | — | — | — | — |
| Marinewood Trail | 2.46 | — | — | — | — |
| Metzger Marsh Trail | 0.44 | — | — | — | Metzger Marsh Unit (Lucas Co?); see Q15 |
| Middle Toussaint Trail | 8.06 | — | — | — | Longest trail on refuge |
| Ottawa Wildlife Interpretive Trail | 1.22 | Easy | Grass | Year round | Between trailhead parking and Magee Marsh WA entrance |
| Partnership Trail | 1.41 | Easy | Grass | Year round | Connects trailhead to Magee Marsh; access Grimm Prairie and John Gallagher trails |
| Pool 1 West Trail | 0.22 | — | — | — | — |
| VC Fishing Pond Trail | 0.06 | — | — | — | Spur to fishing pond |
| West Harbor Landing Trail | 1.61 | Easy | Grass | Apr 1–Sep 15 | West Harbor Landing unit, Catawba Island |
| Woodies Roost Trail | 0.40 | Easy | Grass | Apr 1–Sep 15 | Length discrepancy: narrative 1.9 mi vs structured 0.40 mi |
| York Tract Trail | — | — | — | — | Length not on page |
| Wildlife Drive | 7.0 | — | Auto | — | Auto tour route from Visitor Center; TRAIL_TYPE_REVIEW |

GPS for Ottawa NWR (from FWS page meta): 41.6074975, -83.209608

### T1 — VA National Cemeteries in Ohio (from cem.va.gov/find-cemetery/state.asp?STATE=OH, 2026-05-17)

| Cemetery | Address | County | Status |
|---------|---------|--------|--------|
| Camp Chase Confederate Cemetery | 2900 Sullivant Ave, Columbus OH 43204 | Franklin | Closed |
| **Confederate Stockade Cemetery** | **Johnson's Island, Sandusky OH 44870** | **Ottawa (Danbury Twp)** | **Closed** |
| Dayton National Cemetery | 4400 West Third St, Dayton OH 45428 | Montgomery | Open |
| Ohio Western Reserve National Cemetery | 10175 Rawiga Rd, Seville OH 44273 | Medina | Open |
| Woodland Cemetery Soldiers' Lot | 6901 Woodland Ave, Cleveland OH 44104 | Cuyahoga | Closed |
| Ohio Veterans Home Cemetery (grant-funded) | 3416 Columbus Ave, Sandusky OH 44870 | Erie | Open |

Ottawa County finding: Confederate Stockade Cemetery only.

### T2 — ODNR Ottawa County Coastal Public Access Sites (from pag-le-02-ottawa-county.pdf, 2026-05-17)

| Site ID | Name | Acres | GPS (main) | Township | Notes |
|---------|------|-------|-----------|----------|-------|
| OT1 | Ottawa National Wildlife Refuge | 10,000+ (complex) | 41.6024, -83.2030 | Benton Twp (Ottawa); Jerusalem Twp (Lucas) | KNOWN_MC; T1 staged |
| OT2 | Magee Marsh Wildlife Area | 2,202 | 41.6120, -83.1887 | Benton/Carroll Twp (Ottawa); Jerusalem Twp (Lucas) | KNOWN_MC:OH-MC-S-010 |
| OT3 | Camp Perry Beach | 640 (reservation) | 41.5465, -83.0135 | Erie Twp | Ohio National Guard; beach publicly accessible |
| OT4 | Waterworks Park | — | 41.5143, -82.9355 | Port Clinton | Municipal; T6 |
| OT5 | Port Clinton Lakefront Preserve | — | 41.5141, -82.9308 | Port Clinton | City-owned; Black Swamp Conservancy easement; T6/T7 |
| OT6 | Port Clinton City Beach | — | 41.5140, -82.9248 | Port Clinton | Municipal; T6 |
| OT7 | Catawba Island State Park | ~10 | 41.5745, -82.8570 | Catawba Island Twp | ODNR Parks; day-use boat ramp; staged |
| OT8 | East Harbor State Park | 1,831 | 41.5452, -82.8176 | Danbury Twp | ODNR Parks; 11 trails; staged |
| OT9 | Mazurik Access Area | 15.9 | 41.5411, -82.7636 | Danbury Twp | ODNR; 4-lane boat ramp; staged |
| OT10 | Marblehead Lighthouse State Park | 13.5 | 41.5363, -82.7125 | Danbury Twp | ODNR Parks; lighthouse 1821; staged |
| OT11 | Lake Point Park | 8.7 | 41.5272, -82.7128 | Danbury Twp | Danbury Township-owned; T5 |
| OT12 | Johnson's Island Confederate Soldier Cemetery | 1.2 | 41.5007, -82.7300 | Danbury Twp | VA/NCA; T1 staged |
| OT13 | Dempsey Fishing Access | 66.8 | 41.5077, -82.7608 | Danbury Twp | ODNR; Sandusky Bay; staged |
| OT14 | Sandusky Bay Bridge Access — North | ~1 mi | 41.4842, -82.8293 | Danbury Twp | State; former bridge approach; staged |

### T2 — Lake Erie Islands Coastal Access (from CH3_LakeErieIslands_04142026_web.pdf, 2026-05-17)

**South Bass Island key data:**
- South Bass Island State Park: 33 ac, 1523 Catawba Ave, GPS: 41.6423, -82.8373, ODNR Parks
- Oak Point State Park: 1.5 ac, Bayview Ave at Portsmouth Ave, GPS: 41.6539, -82.8174, ODNR Parks
- Stone Lab Peach Point Campus: SR 357 / West Shore Blvd, ODNR Wildlife + OSU
- South Bass Island Water Trail: part of Lake Erie Islands Water Trail (T3, managed by Put-in-Bay Twp PD)

**Middle Bass Island key data:**
- Middle Bass Island State Park: 124 ac est, 1719 Fox Road, GPS: 41.6761, -82.8110, ODNR Parks
- 4 trails: ADA Lonz Trail (1.3 mi, paved), Campground Loop, Old Campground, Rocky Shore
- Kuehnle Wildlife Area: 20 ac, Deist Rd east of Fox Rd, GPS: 41.6905, -82.8068, ODNR Wildlife + Put-in-Bay Twp PD
- Petersen Woods: 2 ac, adjacent Kuehnle, ODNR Wildlife + Put-in-Bay Twp PD
- Middle Bass Island Water Trail: T3, managed by Put-in-Bay Township PD

**North Bass Island key data:**
- North Bass Island State Park: 593 ac, Put-in-Bay Township, GPS: 41.7074, -82.8162 (S), 41.7227, -82.8257 (N), 41.7185, -82.8119 (E)
- Fox's Marsh Wildlife Area: 132 ac, GPS: 41.7120, -82.8311, ODNR Wildlife; no road access
- Honey Point Wildlife Area: GPS: 41.7074, -82.8083, ODNR Wildlife; no road access
- North Bass Island Water Trail: T3, managed by Put-in-Bay Township PD

**T3 deferred (islands) — not staged at T2:**
- Scheeff East Point Nature Preserve: 9 ac, Columbus Ave terminus, Put-in-Bay Twp PD — T3
- Duff Homestead and Bayfront Preserve: 6.5 ac, Put-in-Bay Twp PD — T3
- Massie Cliffside Preserve: 11 ac, Ken's Trail (1,750 ft), management TBD — T3/T4
- Middle Bass Island East Point Preserve: 11 ac, North Shore Rd, Put-in-Bay Twp PD — T3
- Captain Alfred Parker Park: Put-in-Bay Twp, right-of-way — T6
- DeRivera Park: Village of Put-in-Bay + DeRivera Trust — T6
- West Shore Ice Ramps (2): ODNR Parks on South Bass Island — deferred; check if AP or Site

### T2 — Magee Marsh Wildlife Area Trail Map (from ODNR trail map, 2026-05-17)

| Trail Name | Length (mi) | Notes |
|-----------|------------|-------|
| Magee Marsh Walking Trail — West Loop | 0.5 | Accessible; wetland/woods |
| Magee Marsh Walking Trail — Bear Pond Loop | 0.7 | Bear Pond area |
| Wildlife Beach Trail | 0.7 | Scrub/beach vegetation |
| Gallagher Memorial Trail | 1.2 | Adjacent BSBO; "in Ottawa NWR" per source — see T1-FLAG-2; do NOT stage as Magee trail |
| Magee Marsh Boardwalk (Bird Trail) | 0.7 | = KNOWN_MC:OH-MC-T-008 |
| Crane Creek Estuary Trail | 0.6 | CROSS_SITE_FLAG with T1 Estuary Trail |
| Magee-Ottawa Partnership Trail — Magee segment | 0.5 | CROSS_SITE_FLAG with T1 Partnership Trail (1.41 mi) |
| Goose Haven Trail | 0.7 | Seasonal Apr 15–Aug 31 |
| Lakefront Levee Trail | 0.3 | Seasonal Apr 15–May 31 |

### T2 — East Harbor State Park Trails (from AllTrails/ODNR, 2026-05-17)

| Trail Name | Length (mi) | Notes |
|-----------|------------|-------|
| Middle Harbor Trail | 0.75 | Follows Middle Harbor bank |
| Middle Harbor Extension | 0.5 | To observation platforms |
| Meadow Trail | 0.75 | Meadow habitat |
| Blackberry Trail | 0.25 | Interior |
| Red Bird Trail | 0.25 | Interior |
| Rock Garden Loop | 0.3 | Rock garden |
| Wetlands Trail | 2.0 | Wetland; snowmobile allowed |
| South Beach Trail | 2.5 | South beach; snowmobile allowed |
| Water's Edge Trail | 1.0 | Between Lake Erie and East Harbor |
| Channel Dunes Loop | 0.5 | Channel dunes; snowmobile allowed |
| West Harbor Trail | 0.75 | West Harbor channel; connects to swimming beach |

### T2 — Lakeside Daisy State Nature Preserve (from search, 2026-05-17)

- Address: 309 Alexander Pike, Marblehead, OH 43440
- Total acreage: ~137 ac (19 ac original + 118 ac adjacent expansion; Ohio land purchase)
- Protected species: Lakeside Daisy (Hymenoxys herbacea), federally threatened — only natural U.S. population
- Features: alvar habitat, glacial grooves, accessible trails, ODNR guided tours (peak bloom early-mid May)

---

## Pre-Discovery Checklist — Tier 3 (District) ✅ COMPLETE

*Written per IMP-029 before staging T3 entities. Ohio Auditor pre-enumeration (IMP-072) executed first. 2026-05-17.*

**§3.0 — Ohio Auditor Pre-Enumeration (IMP-072 mandatory):**
- [x] Ohio Auditor of State entity search — https://ohioauditor.gov/auditsearch/search.aspx — searched by Ottawa County + entity type
  - [x] Park/Recreation District → 2 entities: **Put-In-Bay Township Park District** ✅; **Park District of Ottawa County** ✅
  - [x] Soil/Water Conservation District/Joint Board → 1 entity: **Ottawa County Soil and Water Conservation District** ✅
  - [x] Conservancy District → 1 entity: **Sand Beach Conservancy District** ✅
  - [x] Water/Sewer/Sanitary District → 1 entity: Carroll Water and Sewer District (utility; NAP null) ✅
  - Ohio Auditor SSL cert issue (`auditor.state.oh.us` blocked); resolved by using `ohioauditor.gov` domain

**Put-in-Bay Township Park District (PIBTPD):**
- [x] PIBTPD website — putinbayparks.com/about-us/ — confirmed government entity (created 2006 by Ottawa County Common Pleas Court per ORC 511.18); Lake Erie Islands Conservancy = Advisory Council (nonprofit, not same entity)
- [x] PIBTPD Nature Preserves Brochure (PDF, 2021) — full inventory of all PIBTPD properties
  - [x] South Bass Island: Ladd Carr Wildlife Woods (9.1 ac, 2,550 ft trail), Dodge Woods Preserve (3.6 ac, 852 ft mulched trail), Massie Cliffside Preserve (11 ac, 1,750 ft trail), Scheeff East Point Nature Preserve (9.1 ac, 2,205 ft trail) — all staged
  - [x] Middle Bass Island: Forested Wetlands Preserve — Burgundy Bay Tract (8 ac, walking trail), Schneider/Dieperink Tracts (7.3+7.6 ac), East Point Preserve (7.8 ac, walking path, kayak/canoe access only), Petersen Woods (1.5 ac — already staged at T2) — staged
  - [x] Non-public parcels (page 24): South Bass: Woischke Woods (2 ac), Gump Woods (0.5 ac), Knam Purchase (4 ac), Victory Woods–Foley (0.5 ac); Middle Bass: Prokesh/Watson (1 ac), Costello Tract (4 ac), Hahn (~8.3 ac, under contract 2021) — NOT staged (no public access; see Q28)
- [x] PDOC grant page — ottawacountyparksoh.org/grants/duff-homestead/ — **Duff Homestead and Bayfront Preserve** confirmed: 6.5 ac, acquired 2023, South Bass Island, PIBTPD-owned — staged
- [x] 2023 PIBTPD Annual Report — fetched; confirmed formation history and $10M+ grant total; Hahn Property status TBD (see Q29)

**Park District of Ottawa County (PDOC):**
- [x] PDOC website — ottawacountyparksoh.org — confirmed via Ohio Auditor (audit 01/01/2022–12/31/2023, released 09/17/2024)
- [x] Parks and Trails page — ottawacountyparksoh.org/parks-and-trails/ — 2 managed trails: North Coast Inland Trail, Portage River Water Trail
- [x] North Coast Inland Trail — ottawacountyparksoh.org/parks-and-trails/north-coast-inland-trail/ — ~100 mi, Lorain to Genoa, 4 counties (Erie;Huron;Sandusky;Ottawa); Ottawa segment: Sandusky Co. line to Veterans Park Genoa; also US Bike Route 30 — staged as CROSS_COUNTY_CANDIDATE
- [x] Portage River Water Trail — ottawacountyparksoh.org/parks-and-trails/portage-river-water-trail/ — **KNOWN_MC:OH-MC-TR-002** confirmed; 36 mi; officially designated 2022-07-19; 8 Ottawa County launch sites (Mile 0–23) — no new record; Q12 resolved
- [x] PDOC Grants page — PIBTPD grant recipients confirmed (Duff Homestead, Massie Cliffside, etc.); other grant recipients (municipalities, townships) deferred to T5/T6
- [x] PDOC does not own natural area Sites directly — trail/grant entity only; no Site records staged for PDOC

**Toledo Metroparks (KNOWN_MC confirmation):**
- [x] Howard Marsh Metropark — KNOWN_MC:OH-MC-S-021 confirmed (Lucas;Ottawa); Toledo Metroparks
- [x] IMP-104: OH-OTT-T-072 through -076 (Howard Marsh Sandpiper, Mallard, Madewell, Egret, Sora trails) — 5 trails confirmed from Lucas County run; no new records needed

**Ottawa County Soil and Water Conservation District (SWCD):**
- [x] Ohio Auditor confirmed — 1 entity (Ottawa County SWCD); active audit history
- [x] Per §4.7: SWCDs rarely own land; check website — ottawaswcd.wixsite.com/website; co.ottawa.oh.us/Directory.aspx?did=47
- [x] Result: **NAP NULL** — educational outreach entity; no known land holdings; documented tier_result record staged

**Sand Beach Conservancy District:**
- [x] Ohio Auditor confirmed — 1 entity; statutory (ORC 6101)
- [x] Website — sandbeachcd.com — mission: flood control and Lake Erie shoreline erosion prevention at "Sand Beach" community, Ottawa County
- [x] Result: **NAP NULL** — flood control/shoreline protection utility; no natural areas management or public recreational land; documented tier_result record staged

**Lake Erie Islands Water Trail (§4.6 water trail resolution):**
- [x] Confirmed T3 entity per §4.6 (management tier governs, not ODNR designation)
- [x] Managing entity = Put-in-Bay Township Park District (government district)
- [x] Staged as Trail entity (water trail, CROSS_COUNTY_CANDIDATE) under T3

**Cross-County Candidates (IMP-104):**
- [x] North Coast Inland Trail — CROSS_COUNTY_CANDIDATE; Erie;Huron;Sandusky;Ottawa; MULTI_COUNTY.xlsx listed; staged
- [x] Lake Erie Islands Water Trail — CROSS_COUNTY_CANDIDATE; island loops in Ottawa County waters; staged
- [x] Howard Marsh Metropark (OH-MC-S-021) — KNOWN_MC confirmed; IMP-104 PASS
- [x] Portage River Water Trail (OH-MC-TR-002) — KNOWN_MC confirmed; IMP-104 PASS

---

### T3 — PIBTPD Nature Preserves Brochure (from putinbayparks.com, 2026-05-17)

**South Bass Island Publicly Accessible Preserves:**

| Preserve | Acreage | Trail | Access |
|----------|---------|-------|--------|
| Ladd Carr Wildlife Woods (Jane Coates Wildflower Trail) | 9.1 ac | 2,550 ft looped | Foot only; no pets |
| Dodge Woods Preserve | 3.6 ac | 852 ft looped, mulched; StoryWalk® | Foot only; bike rack at Thompson Rd |
| Massie Cliffside Preserve | 11 ac | 1,750 ft; hazardous cliffs | Foot; canoe/kayak; dock |
| Scheeff East Point Nature Preserve | 9.1 ac | 2,205 ft looped | Foot; canoe/kayak; 1700 ft shoreline |
| Duff Homestead and Bayfront Preserve | 6.5 ac | No formal trail (2023 acquisition) | Foot; 150 ft Put-in-Bay harbor frontage; visitor center |

**Middle Bass Island Publicly Accessible Preserves:**

| Preserve | Acreage | Trail | Access |
|----------|---------|-------|--------|
| Forested Wetlands Preserve — Burgundy Bay Tract | 8 ac | Walking trail (length TBD) | Foot; bicycle rack at Fox Road |
| Forested Wetlands Preserve — Schneider Tract | 7.3 ac | None specified | — |
| Forested Wetlands Preserve — Dieperink Tract | 7.6 ac | None specified | — |
| East Point Preserve | 7.8 ac | Walking path (length TBD), looped | Canoe/kayak only; shallow-water dock |
| Petersen Woods (+ Lawrence Evans) | 1.5+0.75 ac | No formal trail | Foot; adjacent Kuehnle WA — **ALREADY STAGED at T2** |

**Non-Public PIBTPD Parcels (not staged — no public access):**
- South Bass: Woischke Woods (2 ac), Gump Woods (0.5 ac), Knam Purchase (4 ac), Victory Woods–Foley (0.5 ac)
- Middle Bass: Prokesh/Watson Property (1 ac), Costello Tract (4 ac), Hahn Property (~8.3 ac — status TBD per Q29)

### T3 — Park District of Ottawa County — Portage River Water Trail Ottawa County Launch Sites (from ottawacountyparksoh.org, 2026-05-17)

| Mile | Site Name | Address | Notes |
|------|-----------|---------|-------|
| 0 | Lake Erie Beach Access | Jefferson St at Waterworks Park, Port Clinton | PRWT northern terminus at Lake Erie |
| 2 | Portage River State Wildlife Area | 262 W. Lakeshore Dr. (SR 163), Port Clinton | T2 entity; walking trail also present |
| 3.7 | Little Portage Unit (FWS) | 7899 W Little Portage East Rd., Oak Harbor | Eagle Scout kayak launch 2023; T2-FLAG-4 review (Q24) |
| 4.8 | Marinewood Unit (FWS) | 4640 W Harbor Rd., Port Clinton | Ottawa NWR unit; limited parking |
| 5.5 | Little Portage State Wildlife Area | — | Limited access; no parking |
| 7.8 | Ottawa County Fairgrounds | 7870 W State Route 163, Oak Harbor | PDOC-funded shelter house |
| 12.7 | Oak Harbor Interurban Overlook | 146 N Church St., Oak Harbor | ADA paved walkway |
| 22 | Elmore-Riverbend Park | 715 Merle Harder Blvd., Elmore | — |
| 23 | Harry Witty Memorial Park | 358 Harris St., Elmore | BoardSafe kayak launch chute |

Note: Woodville-Trail Marker Park (Mile 28.5, Sandusky Co.), William Henry Harrison Park (Mile 36, Wood Co.), North Branch at Water Street (Wood Co.) are outside Ottawa County.

---

## Pre-Discovery Checklist — Tier 4 (County) ✅ COMPLETE

*Written per IMP-029. Ottawa County, Ohio. 2026-05-18.*

**Ottawa County Government Website (co.ottawa.oh.us — §3.1):**
- [x] Departments page (co.ottawa.oh.us/197/Departments) — enumerated all 34 departments; no county parks department found; PDOC listed as delegated parks authority
- [x] Recreational Programs (co.ottawa.oh.us/251/Recreational-Programs) — Health Dept inspections only (campgrounds, pools, beaches); no natural areas content
- [x] County GIS Web Maps (co.ottawa.oh.us/206/GIS-Web-Maps) — survey/plat data only; no parks or open space layer; no new entities
- [x] Regional Planning Commission (co.ottawa.oh.us/355/Regional-Planning-Commission) — planning/zoning only; no natural areas enumeration
- [x] Veterans Service — no county-owned veterans cemetery found on county site; Ottawa County Home Cemetery found via external search (SR 163, Salem Twp)
- [x] Ottawa County Fair (ottawacountyfair.org) — county-adjacent Agricultural Society entity; PRWT launch ramp at fairgrounds; PDOC grant established access

**Park District of Ottawa County — PDOC (ottawacountyparksoh.org — primary T4 authority):**
- [x] Parks and Trails directory (top-level per OBS-029) — 2 entries: North Coast Inland Trail (T3 CROSS_COUNTY_CANDIDATE, already staged); Portage River Water Trail (KNOWN_MC:OH-MC-TR-002, already in DB)
- [x] Introduction page — PDOC mission, history, levy structure; confirmed grants/planning body; does NOT own parks/sites directly
- [x] Outdoor Hiking Challenge — 13 hiking destinations enumerated; cross-referenced for T4 relevance
- [x] Projects → Catawba Islander Trail — PLANNED, ~5 mi, master plan July 2023; staged as T4 Trail (PLANNED)
- [x] Projects → Marblehead Peninsula Trail Feasibility Study — study phase only; no identity-bearing trail entity yet; deferred
- [x] Projects → North Coast Inland Trail Extension and Planning — extension planning; Ottawa County segment already staged at T3
- [x] Grants page — enumerated all grant recipients by municipality/township; confirmed grantees are third-party entities (not PDOC-owned); relevant grantees:
  - [x] Ottawa County Fairgrounds PRWT Launch — county-adjacent (Agricultural Society); staged as AP
  - [x] PIBTPD grants (Duff Homestead, Massie, etc.) — already staged at T3
  - [x] Danbury Township (Meadowbrook Marsh) — T5 entity; deferred
  - [x] Catawba Island Township (Cedar Meadow Preserve Trail) — T5 entity; deferred
  - [x] City of Port Clinton grants — T6 entities; deferred
  - [x] Village of Put-in-Bay (DeRivera Park) — T6 entity; deferred

**NRHP Ottawa County Bridges and Structures (§3.3 mandatory):**
- [x] Wikipedia NRHP listings for Ottawa County — 31 entries reviewed
- [x] SR 51 Bridge over Portage River (NRHP #94000239) — noted "Replace in 2020"; likely demolished; no current visitor entity
- [x] Ottawa County Courthouse — NRHP listed; administrative building; excluded per §6.1
- [x] All other NRHP entries — private residential, religious, or already-staged entities (Perry's Victory T1, Johnson Island T1, Marblehead Lighthouse T2, North Bass School within North Bass Island SP T2)
- [x] **Result: No new T4 NRHP bridge or structure entities**

**County Cemeteries (IMP-099 §4.9):**
- [x] Web search: "Ottawa County Ohio county-owned cemetery soldiers relief infirmary cemetery"
- [x] **Ottawa County Home Cemetery** — SR 163, 1/4 mi west of Co. Rd. 104, Salem Township — county infirmary/poorhouse cemetery — STAGED (T4 Site, category: Cemetery, subtype: Public Cemetery)
- [x] Riverview Cemetery (Port Clinton) — city-owned, 1883; T6 entity; deferred
- [x] Other cemeteries — township or privately owned; deferred to T5/T8

**County Golf Courses (IMP-099 §4.9):**
- [x] Web search for county park district golf courses — none found
- [x] Marinewood Golf Course — acquired by FWS 2014 (now Ottawa NWR Marinewood Unit); no longer county-operated
- [x] **Result: No county golf course entities**

**FWS Ottawa NWR Units — T1 Misses Discovered at T4:**
- [x] FWS Ottawa NWR visit-us page (fws.gov/refuge/ottawa/visit-us) — full unit inventory checked
- [x] Ottawa NWR Marinewood Unit — T1 miss; SR 163, old golf course, acquired 2014; mowed trail + fishing; STAGED as T1
- [x] Ottawa NWR Turkey Run Unit — T1 miss; 266 ac; near Little Portage River; hunting + hiking; STAGED as T1
- [x] Ottawa NWR Turtle Creek Island Unit — T1 miss; Duff-Washa Rd; Ducks Unlimited 2016; kayak launch + fishing; STAGED as T1
- [x] Ottawa NWR Upper Toussaint Unit — T1 miss; 77 ac; Toussaint River; hunting + fishing; STAGED as T1
- [x] Ottawa NWR Little Portage Unit — T1 miss; 30 ac; Little Portage River; paddler access being installed; fishing; STAGED as T1 (resolves T2-FLAG-4/T3-FLAG-7/Q20/Q24)
- [x] Nehls Memorial Nature Preserve — listed on FWS page; owned by Black Swamp Conservancy; FWS co-manages access; mowed trail + kayak launch + pavilion; **DEFERRED T7** (Black Swamp Conservancy)

**Visitors Bureau (shoresandislands.com — §3.6):**
- [ ] Web search rate-limited during session; primary parks/trails coverage confirmed via PDOC and county government; **verify at next session if any visitor-bureau-exclusive entities remain**

**Cross-County Candidates (IMP-104 at T4):**
- [x] No new cross-county candidates at T4
- [x] Ottawa NWR T1-miss units: Turkey Run and Upper Toussaint county locations to verify (Ottawa vs. Sandusky); flagged Q31–Q32
- [x] All other T4 entities confirmed Ottawa County only

---

### Tier 4 — County (2026-05-18) — 9 records staged

**Site Networks (1):**
| Raw Name | Governance | Key Notes |
|----------|-----------|-----------|
| Park District of Ottawa County | Ottawa County (semi-autonomous) | Created 1992 Ottawa Co. Probate Court; 5-member board; county-wide levy 2020; manages NCIT + PRWT + Catawba Islander Trail; grants body; 3979 E Knoll Crest Dr, Port Clinton OH 43452; ottawacountyparksoh.org |

**Sites (1 — T4 direct; 5 T1 misses staged as T1):**
| Raw Name | Governance | Key Notes |
|----------|-----------|-----------|
| Ottawa County Home Cemetery | Ottawa County (infirmary) | SR 163, 1/4 mi west of Co. Rd. 104, Salem Township; county poorhouse/infirmary cemetery; IMP-099 category: Cemetery, subtype: Public Cemetery; GPS TBD |

**Trails (1):**
| Raw Name | Managing Entity | Length | Status |
|----------|----------------|--------|--------|
| Catawba Islander Trail | Park District of Ottawa County | ~5 mi (planned; Phase 1 route mapped) | PLANNED — master plan July 2023 (Kleinfelder); multi-use trail, Catawba Island N to S; ottawacountyparksoh.org/projects/catawba-islander-trail/ |

**Access Points (1):**
| Raw Name | Parent Trail | Address | Key Notes |
|----------|-------------|---------|-----------|
| Ottawa County Fairgrounds — PRWT Launch | KNOWN_MC:OH-MC-TR-002 (PRWT, Mile 7.8) | 7870 W State Route 163, Oak Harbor OH (physical); alt: 770 SE Catawba Rd, Port Clinton OH 43452 (address discrepancy — Q37) | Ottawa County Agricultural Society; kayak/canoe launch; gravel ramp; parking; PDOC grant; installed by Elite Excavation |

**T1-Miss Sites discovered at T4 (staged as tier: 1):**
| Raw Name | Parent | Key Notes |
|----------|--------|-----------|
| Ottawa NWR — Marinewood Unit | Ottawa NWR (OTT-S-001) | SR 163, Oak Harbor/Port Clinton; old Marinewood Golf Course; acquired FWS 2014; pollinator + tree restoration; mowed trail; fishing in Portage River; PRWT Mile 4.8 launch (4640 W Harbor Rd) |
| Ottawa NWR — Turkey Run Unit | Ottawa NWR (OTT-S-001) | ~16 mi SE of main refuge; 266 ac; woods/prairie/pools; hunting + hiking + wildlife obs + photography; gravel parking; no defined trails; open daylight hours; Little Portage River fishing; county Q31 |
| Ottawa NWR — Turtle Creek Island Unit | Ottawa NWR (OTT-S-001) | Duff-Washa Rd, ~4 mi SE of main; purchased Ducks Unlimited 2016; parking + canoe/kayak launch (Friends of Ottawa, 2017); fishing; open sunrise to sunset |
| Ottawa NWR — Upper Toussaint Unit | Ottawa NWR (OTT-S-001) | 77 ac; Toussaint River, Rocky Ridge–Lickert-Harder Rds; hunting N of river + fishing; county Q32 |
| Ottawa NWR — Little Portage Unit | Ottawa NWR (OTT-S-001) | 30 ac; Little Portage River SE of Oak Harbor; mix of former ag fields, shrubland, river, marshland; paddler access being installed; fishing sunrise to sunset; GPS: 7899 W Little Portage East Rd., Oak Harbor; resolves T2-FLAG-4/T3-FLAG-7/Q20/Q24 |

**T7 Deferred (noted at T4):**
| Raw Name | Owner | Key Notes |
|----------|-------|-----------|
| Nehls Memorial Nature Preserve | Black Swamp Conservancy | East Muggy Rd, Catawba Island Twp; 21 ac land + 18 ac submerged (West Harbor); 7.7 ac prairie/pollinator, 8.2 ac woodland; mowed trail + ADA kayak/canoe launch + pavilion; FWS co-manages public access; DEFER T7 |

**T4 NULL Results:**
- NRHP Ottawa County — no county-managed bridge/structure entity (SR 51 bridge replaced 2020)
- County golf course (IMP-099) — none found; Marinewood Golf Course transferred to FWS 2014
- County GIS — survey/plat data only; no new parks entities

---

### T4 — Ottawa NWR Units Inventory (from fws.gov/refuge/ottawa/visit-us, 2026-05-18)

| Unit | Acreage | Location | Public Access | Notes |
|------|---------|----------|---------------|-------|
| Ottawa NWR (main) | 8,000+ (complex) | 14000 W SR-2, Oak Harbor | Full | Already staged T1 |
| Navarre Marsh Unit | ~820 | Near Davis-Besse | Restricted/permit | Already staged T1 |
| West Harbor Landing | 16 | SR 53 E of Port Clinton | Kayak launch, fishing deck, parking | Already staged T1; GPS: 41.5765N, -82.8488W approx |
| Little Portage Unit | 30 | 7899 W Little Portage East Rd, Oak Harbor | Paddler access being installed; fishing | **T1 MISS — staged at T4** |
| Marinewood Unit | ~30 est | SR 163, Oak Harbor/Port Clinton | Mowed trail, fishing, parking | **T1 MISS — staged at T4**; old Marinewood Golf Course; acquired 2014 |
| Turkey Run Unit | 266 | ~16 mi SE of main, near Little Portage R. | Hunting, hiking, gravel parking | **T1 MISS — staged at T4**; county Q31 |
| Turtle Creek Island Unit | est ~50 | Duff-Washa Rd, ~4 mi SE of main | Kayak/canoe launch, fishing, parking | **T1 MISS — staged at T4**; Ducks Unlimited 2016 |
| Upper Toussaint Unit | 77 | Toussaint River, Rocky Ridge area | Hunting, fishing | **T1 MISS — staged at T4**; county Q32 |
| Metzger Marsh Unit | 182 | Co-owned with ODNR; E portion of 740 ac Metzger Marsh | Hunting, fishing | Partly Ottawa/Lucas; T1-FLAG-3; county verify |
| Nehls Memorial Nature Preserve | 21 land + 18 submerged | E. Muggy Rd, Catawba Island Twp | Mowed trail, ADA kayak launch, pavilion | BSC-owned; FWS partner; **T7 — deferred** |

### T4 — PDOC Outdoor Hiking Challenge — 13 Destinations (from ottawacountyparksoh.org/outdoor-hiking-challenge/, 2026-05-18)

| # | Destination | Managing Entity | Tier |
|---|-------------|----------------|------|
| 1 | Scheeff East Point Preserve | PIBTPD | T3 ✅ |
| 2 | Meadowbrook Marsh | Danbury Township | T5 → defer |
| 3 | Great Egret Marsh Nature Preserve | The Nature Conservancy | T7 → defer |
| 4 | Ottawa NWR Fox Unit | FWS (unofficial name; may = Turtle Creek / other unit) | T1 — investigate |
| 5 | Lakeside Daisy State Nature Preserve | ODNR DNAP | T2 ✅ |
| 6 | North Coast Inland Trail | PDOC | T3 ✅ CROSS_COUNTY_CANDIDATE |
| 7 | Portage River Fishing Access | ODNR | T2 — verify vs. Toussaint Creek WA |
| 8 | Nature/Walking Trail adj. Train Station, Central Ave | Lakeside Chautauqua | T8 private/gated — defer |
| 9 | Ottawa NWR Marinewood Unit | FWS | T1 MISS ✅ staged |
| 10 | Magee Marsh Wildlife Area Boardwalk | ODNR (KNOWN_MC:OH-MC-T-008) | T2 ✅ |
| 11 | Clay Center Village Park | Village of Clay Center | T6 → defer |
| 12 | Waterworks Park | City of Port Clinton | T6 → defer |
| 13 | Catawba Point Preserve | Catawba Island Township | T5 → defer |

Note: Item 4 "Ottawa NWR Fox Unit" — PDOC page cites "Fox Nature Preserve - Friends of Ottawa NWR"; Friends of Ottawa NWR is the nonprofit partner, not FWS. This may refer to the area around the main refuge informally called "Fox" or could be a separate parcel. **Flag for FWS verification — may be informal name for existing staged unit.**
