# Scioto County, Ohio — Discovery Handoff
# Last updated: 2026-06-10 — BATCH RESOLUTION COMPLETE. See scioto_oh_batch_resolution_2026_06_10.md. 50 sites in DB. Key: Arc of Appalachia Biodiversity (317ac) confirmed Adams County not Scioto; Glade Wetland Parcel A county verify needed (may be Pike). T-0006 trail_parent added.

---

## Status: DISCOVERY COMPLETE — ALL 8 TIERS DONE — GPS PASS + VERIFICATIONS PENDING

---

## County Summary

| Field | Value |
|-------|-------|
| County | Scioto County, Ohio |
| FIPS | 39145 |
| County seat | Portsmouth |
| Baseline seeds | 36 |
| Seeds confirmed | 36/36 — all baseline seeds resolved |
| Seeds excluded | 1 (Clark Planetarium — no conservation function) |
| Seeds remaining | 0 |
| Session files | scioto_oh_raw_discovery.yaml, scioto_oh_session_log.md |
| Raw records written | 81 (60 prior + 16 T7: 5 Sites + 6 Trails + 4 APs + 1 Site Network; + 5 T8: 4 Sites + 1 AP) |
| DB entities | 28 inserted (12 sites, 13 trails, 3 APs); 1 held (SC-TN-0001) — pipeline not yet re-run for T3–T6 |
| Entity prefix | SC- |

---

## Tiers Completed

| Tier | Summary |
|------|---------|
| Tier 1 — Federal | 3 Sites (WNF Ironton Unit, Alum Rock, High Rock); 0 Trails; WNF Scioto County trail inventory PENDING |
| Tier 2 — State | 9 Sites, 13 Trails, 1 Trail Network; 8 baseline seeds confirmed; 1 new find (Scioto Brush Creek Scenic River) |
| GPS Pass (Tiers 1–2) | GPS confirmed for 6 Tier 2 Sites; 3 Access Points written (SC-AP-0001 Trailhead, SC-AP-0002 Forest HQ Parking, SC-AP-0003 Marina); Alum Rock and CCC Memorial GPS still unconfirmed |
| Tier 3 — District | NULL — no ORC 1545 park district; no ORC 6101 conservancy/watershed district; Scioto SWCD holds no natural area land. 0 entities. |
| Tier 4 — County | 1 Site (ETC Park, 81.2 ac); 1 Trail (Allan W. Eckert Trail); 1 AP (Burkes Point Boat Ramp, governance uncertain). Also found 4 Tier 2 misses (Brush Creek State Forest + 3 trails). NRHP check: 42 listings reviewed; no new county natural area entities. |
| Tier 5 — Township | 4 Sites (Porter Township Park, Friendship Park, Clay Township Park, Vernon Township Community Park); 0 Trails; 0 APs. 12 of 16 townships null. Also: 2 Tier 5 misses found at Tier 6 (Brush Creek Twp. Community Park, Eden Park). |
| Tier 6 — Municipal | 13 Portsmouth city parks + 1 child Site (Horseshoe Mound) + 2 Portsmouth pending-verify + 1 Millbrook Park (New Boston) + 1 Rarden Community Park. South Webster and Otway null. 14 baseline seeds confirmed. |

## Tiers Completed (continued)

| Tier | Summary |
|------|---------|
| Tier 7 — Conservancy | Arc of Appalachia: 4 Sites (Ohio Hanging Rock 750 ac, Simon Woods 670 ac, Tremper Mound 706 ac, Gladys Riley 230 ac) + 1 Site Network; 6 Trails (1 OHR Trail, 3 Tremper Mound, 2 Gladys Riley — Simon Woods trail names PENDING); 4 APs. AOA: 1 Site (Scioto Bend Preserve — county UNCERTAIN, data PENDING). 16 total T7 records. 5 of 8 unresolved Tier 8 seeds correctly reassigned to Tier 7 (Arc ×4 + AOA ×1 are land trusts). |

## Tiers Completed (continued)

| Tier | Summary |
|------|---------|
| Tier 8 — Private | Camp Oyo (Simon Kenton Council BSA — governance corrected from Dan Beard baseline); Otway Covered Bridge (Otway Historical Society, NRHP 1974, GPS confirmed); Three Bridges Park (The Boneyfiddle Project); 535 On Second (MSPIB — GPS pending). 5 records (4 Sites + 1 AP). All 36 baseline seeds resolved. |

**ALL TIERS COMPLETE — discovery phase done.**

---

## Key Active Flags

- **GNIS Pillars**: Alum Rock (SC-S-0002) and High Rock (SC-S-0003) INCLUDED per user direction (2026-03-28). GPS still missing for Alum Rock — GNIS coordinates unavailable; flag for manual GPS acquisition.
- **Gladys Riley dual-entry**: SNP (SC-S-0007, Tier 2) and Arc preserve (Tier 8 — pending). Both valid records. 186 ac vs. 230 ac discrepancy documented.
- **MORPC GPS layer**: Not applicable — Scioto County outside 15-county coverage. GPS pass via Chrome/Google Maps completed for Tiers 1–2. Portsmouth T6 parks (13 entities) have NO GPS yet — addresses are in Captured Source Data table; fill GPS column there during acquisition pass rather than re-fetching the city page.
- **WNF trail inventory**: Scioto County trail inventory for Wayne National Forest Ironton Unit flagged PENDING (website blocked during discovery).
- **Shawnee mountain bike trail names**: Trailforks page confirms trails exist; individual trail names not confirmed — flagged PENDING VERIFICATION.
- **Shawnee Bridle Trail Network**: 60+ mi confirmed; individual segment names not confirmed — SC-TN-0001 member_trails empty, PENDING VERIFICATION.
- **Raven Rock Arch**: ODNR maintains a separate "Raven Rock Arch" page — assess whether this is a child Site entity before creating a record.
- **CCC Memorial GPS**: Location within Shawnee State Forest not pinned; no dedicated ODNR page found. Flag for manual GPS acquisition.
- **Scioto Brush Creek Scenic River**: SC-S-0012 created from November 2025 post-cutoff designation. Confirmed via web search. Not in baseline.
- **Scioto Brush Creek SNP new facilities**: ODNR news post references new facilities at SC-S-0008; details blocked. Update record when accessible.
- **Scioto County Shawnee Bridge to Bridge Route**: 36-mi shared-roadway bicycle route (Otway Covered Bridge to Mackletree Bridge through Shawnee State Forest). Not yet cataloged — assess managing entity and route type at Tier 5 or 8.
- **Shawnee State Park Nature Center**: Appears as separate Google Maps entity (5.0 stars) at Shawnee State Park — assess whether child Site record warranted before pipeline run.
- **Brush Creek State Forest GPS**: GPS for Scioto County portion not confirmed — former HQ on SR-73 near Rarden; ODNR page has no coordinates. Flag for GPS acquisition pass.
- **Brush Creek SF trails**: Stone Quarry Trail and Coffee Hollow Bridle Trail county attribution uncertain — may be in Adams, Pike, or Scioto County portion. Length not confirmed.
- **Burkes Point Boat Ramp governance**: Managing agency not confirmed — could be county, ODNR watercraft, or other entity. Staged as Tier 4 with GOVERNANCE_UNCERTAIN flag.
- **Earl Thomas Conley Park baseline correction**: Baseline had this as "Portsmouth City Park" — confirmed as Scioto County park per commissioner management evidence.
- **Otway Covered Bridge**: ✅ STAGED at Tier 8 — Otway Historical Society, NRHP 1974, GPS confirmed (38.85932°N, 83.19060°W).
- **Camp Oyo governance correction**: Baseline had Dan Beard Council; correctly staged under Simon Kenton Council (BSA). Dan Beard Council (Cincinnati) is a separate council from Simon Kenton (central OH).
- **Simon Woods trail names PENDING**: Arc of Appalachia website blocked during discovery. Trail names and lengths not confirmed — fetch arcofappalachia.org/visit-simon-woods when accessible before pipeline.
- **Scioto Bend Preserve county UNCERTAIN**: AOA's county list does not explicitly include Scioto County. Baseline listed as Scioto. Verify Scioto vs. Pike County via GIS before pipeline.
- **ONAPA cross-check incomplete**: onapa.org was egress-blocked during Tier 7. No additional land trusts found via search but ONAPA map not fully reviewed. Run when accessible.
- **Arc of Appalachia GPS gap**: All 4 Arc preserves and 4 APs have GPS blank — prioritize in GPS acquisition pass using Google Maps or ODNR GIS.
- **Scioto Bridge to Bridge Route**: 36-mi shared-roadway bicycle route (Otway Covered Bridge to Mackletree Bridge). Managing entity and entity type not confirmed — assess before pipeline.
- **Horseshoe Mound** (NRHP, in Mound Park): ✅ STAGED at Tier 6 — child Site of Mound Park.
- **Three Bridges Park tier resolved**: ✅ CONFIRMED Tier 8 — owned by The Boneyfiddle Project, private nonprofit. Not a city park.
- **535 On Second tier resolved**: ✅ CONFIRMED Tier 8 — MSPIB-owned pocket park (MSPIB is independent nonprofit, not city department).
- **Roy Rogers Esplanade resolved**: ✅ CONFIRMED Tier 6 — city-owned, MSPIB-maintained. Staged.
- **Riverfront Park / York Park identity**: VERIFY NEEDED — Google Maps "Riverfront Park" (728 2nd St, 366 reviews) may be same entity as city's "York Park" (Ohio Riverfront, no street number). Both staged; resolve at pipeline. If same, York Park is canonical.
- **Larry Hisle Park governance**: VERIFY NEEDED — 2238 Thomas Ave, near Housing Authority. Confirm city-owned vs. housing authority before assigning tier.
- **Brush Creek Twp. Community Park**: T5 MISS — staged (5715 OH-348, Otway; GPS 38.8600095°N/83.1922189°W).
- **Eden Park (Clay Twp.)**: T5 MISS — staged (Clay Twp., OH 45662; GPS 38.7747982°N/82.9421173°W). Confirm distinct from Clay Township Park (38.78624°N/82.97119°W).
- **River Otter Trail**: 1.5-mile trail at Scioto Brush Creek SNP (SC-S-0008) discovered at Tier 4 — staged as Tier 2 miss. Length confirmed (1.5 mi).
- **Clay Township Park GPS**: GPS from OpenStreetMap (38.78624°N/82.97119°W) — treat as approximate. No official Clay Township website found for Scioto County. GPS should be confirmed during GPS acquisition pass.
- **Friendship Park address**: Nile Township park in Friendship, OH near US 52 — no street address on township website. GPS unconfirmed.
- **Valley Township park watch**: Google Maps "Valley Community Services" (583 Robert Lucas Rd) has one review "Love that there is a park here now!" — possible new unnamed park. No formal identity. Monitor; do not stage without authoritative documentation.

---

## Entities Discovered (Raw — Pipeline Pending)

| ID (pending) | Name | Type | Tier |
|--------------|------|------|------|
| SC-S-0001 | Wayne National Forest - Ironton Unit | Site | 1 |
| SC-S-0002 | Alum Rock | Site | 1 |
| SC-S-0003 | High Rock | Site | 1 |
| SC-S-0004 | Shawnee State Forest | Site | 2 |
| SC-S-0005 | Shawnee State Park | Site | 2 |
| SC-S-0006 | Gladys Riley Golden-star State Nature Preserve | Site | 2 |
| SC-S-0007 | Raven Rock State Nature Preserve | Site | 2 |
| SC-S-0008 | Scioto Brush Creek State Nature Preserve | Site | 2 |
| SC-S-0009 | CCC Memorial to Company 1545 | Site (child) | 2 |
| SC-S-0010 | Copperhead Fire Tower | Site (child) | 2 |
| SC-S-0011 | Shawnee State University — Deal Arboretum | Site | 2 |
| SC-S-0012 | Scioto Brush Creek State Scenic River | Site | 2 |
| SC-T-0001 | Shawnee Backpack Trail | Trail | 2 |
| SC-T-0002 | Lampblack Trail | Trail | 2 |
| SC-T-0003 | Park Loop Trail | Trail | 2 |
| SC-T-0004 | Knighton Nature Trail | Trail | 2 |
| SC-T-0005 | Lookout Trail | Trail | 2 |
| SC-T-0006 | Campground Loop Trail | Trail | 2 |
| SC-T-0007 | Shawnee Forest Day Hike Trail — East Loop | Trail | 2 |
| SC-T-0008 | Shawnee Forest Day Hike Trail — West Loop | Trail | 2 |
| SC-T-0009 | Copperhead Firetower and Bear Lake Trail | Trail | 2 |
| SC-T-0010 | Appalachian Tree Trail | Trail | 2 |
| SC-T-0011 | Around the World Tree Trail | Trail | 2 |
| SC-T-0012 | Relics of the Past Tree Trail | Trail | 2 |
| SC-T-0013 | Medicinal Tree Trail | Trail | 2 |
| SC-TN-0001 | Shawnee Bridle Trail Network | Trail Network | 2 |
| SC-AP-0001 | Shawnee Backpack Trail / State Park Main Trailhead | Access Point | 2 (GPS pass) |
| SC-AP-0002 | Shawnee State Forest Headquarters | Access Point | 2 (GPS pass) |
| SC-AP-0003 | Shawnee State Park Marina | Access Point | 2 (GPS pass) |
| (pending) | Brush Creek State Forest | Site | 2 (miss, added T4) |
| (pending) | Stone Quarry Trail | Trail | 2 (miss, added T4) |
| (pending) | Coffee Hollow & Crabtree Cemetery Bridle Trail | Trail | 2 (miss, added T4) |
| (pending) | River Otter Trail | Trail | 2 (miss, added T4) |
| (pending) | Earl Thomas Conley Riverside Park | Site | 4 |
| (pending) | Allan W. Eckert Trail | Trail | 4 |
| (pending) | Burkes Point Boat Ramp | Access Point | 4 (governance uncertain) |
| (pending) | Porter Township Park | Site | 5 |
| (pending) | Friendship Park | Site | 5 |
| (pending) | Clay Township Park | Site | 5 |
| (pending) | Vernon Township Community Park | Site | 5 |
| (pending) | Brush Creek Twp. Community Park | Site | 5 (miss, found at T6) |
| (pending) | Eden Park | Site | 5 (miss, found at T6) |
| (pending) | Alexandria Park | Site | 6 |
| (pending) | Bannon Park | Site | 6 |
| (pending) | Buckeye Park | Site | 6 |
| (pending) | Cyndee Secrest Park | Site | 6 |
| (pending) | Labold Ball Fields | Site | 6 |
| (pending) | Martha Burton Park | Site | 6 |
| (pending) | Mound Park | Site | 6 |
| (pending) | Horseshoe Mound | Site (child of Mound Park) | 6 |
| (pending) | Roy Rogers Esplanade | Site | 6 |
| (pending) | Sciotoville Community Square | Site | 6 |
| (pending) | Skate Park | Site | 6 |
| (pending) | Spock Memorial Dog Park | Site | 6 |
| (pending) | Tracy Park | Site | 6 |
| (pending) | York Park | Site | 6 |
| (pending) | Riverfront Park | Site | 6 (VERIFY_IDENTITY w/ York Park) |
| (pending) | Larry Hisle Park | Site | 6 (VERIFY_GOVERNANCE) |
| (pending) | Millbrook Park | Site | 6 |
| (pending) | Rarden Community Park | Site | 6 |
| (pending) | Ohio Hanging Rock | Site | 7 |
| (pending) | Ohio Hanging Rock Trail | Trail | 7 |
| (pending) | Ohio Hanging Rock Trailhead | Access Point | 7 |
| (pending) | Simon Woods | Site | 7 |
| (pending) | Tremper Mound | Site | 7 |
| (pending) | Tremper Mound Trail | Trail | 7 |
| (pending) | Fairybell Hollow Trail | Trail | 7 |
| (pending) | Pond Creek Bottom Trail | Trail | 7 |
| (pending) | Tremper Mound Main Entrance | Access Point | 7 |
| (pending) | Huckleberry Ridge Trailhead | Access Point | 7 |
| (pending) | Gladys Riley Golden Star Lily Preserve | Site | 7 |
| (pending) | Yellow Buckeye Trail | Trail | 7 |
| (pending) | White Walnut Trail | Trail | 7 |
| (pending) | Gladys Riley Golden Star Lily Preserve Trailhead | Access Point | 7 |
| (pending) | Scioto Bend Preserve | Site | 7 (county UNCERTAIN) |
| (pending) | Arc of Appalachia — Scioto County Preserves | Site Network | 7 |
| (pending) | Camp Oyo | Site | 8 |
| (pending) | Otway Covered Bridge | Site | 8 |
| (pending) | Otway Covered Bridge Park Entrance | Access Point | 8 |
| (pending) | Three Bridges Park | Site | 8 |
| (pending) | 535 On Second | Site | 8 (GPS pending) |

---

## Held Entities

*(None yet)*

---

## Baseline Seeds — All Resolved ✅

*All 36 baseline seeds are now resolved (35 staged + 1 excluded).*

| Seed | Resolved Tier | Status |
|------|---------------|--------|
| Ohio Hanging Rock | 7 — Arc of Appalachia | Staged; GPS pending |
| Simon Woods | 7 — Arc of Appalachia | Staged; trail names pending |
| Tremper Mound | 7 — Arc of Appalachia | Staged; GPS pending |
| Gladys Riley Golden Star Lily Preserve | 7 — Arc of Appalachia | Staged; GPS pending |
| Scioto Bend Preserve | 7 — AOA | Staged; county + data UNCERTAIN |
| Camp Oyo | 8 — Simon Kenton BSA | Staged; governance corrected from Dan Beard |
| 535 On Second | 8 — MSPIB | Staged; GPS pending |
| Three Bridges Park | 8 — The Boneyfiddle Project | Staged |
| Otway Covered Bridge | 8 — Otway Historical Society | Staged; GPS confirmed |
| Clark Planetarium | Excluded | No conservation function |
| [All other 26 seeds] | Tiers 1–6 | Staged; see prior tiers |

*(Note: York Park / Riverfront Park identity question is an internal verification, not an unresolved seed.)*

---

## Open Questions

1. Does Arc of Appalachia hold additional Scioto County preserves beyond the 4 baseline seeds?
2. **Riverfront Park vs. York Park**: Are these the same entity? Riverfront Park at 728 2nd St (366 Google Maps reviews, city phone) vs. York Park at "Ohio Riverfront" on city's Adopt-a-Park page. If same entity, York Park is canonical. Verify before pipeline.
3. **Larry Hisle Park governance**: City of Portsmouth park or Portsmouth Metropolitan Housing Authority property? 2238 Thomas Ave. Confirm before assigning Tier 6.
4. ~~Does Scioto County have any land trusts operating at Tier 7?~~ ✅ RESOLVED — Arc of Appalachia (4 preserves) and Appalachia Ohio Alliance (1 preserve) operate at Tier 7. ONAPA check was blocked (website egress blocked); run if possible. **Simon Woods trail names still PENDING** — fetch arcofappalachia.org/visit-simon-woods when accessible. **Scioto Bend Preserve county UNCERTAIN** — verify Scioto vs. Pike County via GIS.
5. Raven Rock Arch: child Site entity of Raven Rock SNP, or just a feature page?
6. Shawnee mountain bike trail names and routes: confirm from Trailforks or ODNR before finalizing SC-S-0004 trail inventory.
7. Shawnee Bridle Trail Network: enumerate individual named segments for SC-TN-0001.
8. Scioto County Shawnee Bridge to Bridge Route: assess managing entity and whether it qualifies as a Trail entity.
9. Clay Township Park (Tier 5): GPS approximate (OpenStreetMap). No features data.
10. Friendship Park (Tier 5): Exact address unknown — just "Friendship, OH near US 52." GPS needs confirmation.
11. Eden Park (Tier 5 miss): Possible 2nd Clay Township park — confirm identity distinct from Clay Township Park (38.78624°N/82.97119°W).
12. Valley Township: "Valley Community Services" (583 Robert Lucas Rd) — review said "Love that there is a park here now!" Monitor post-pipeline for formal identity.

---

## Next Steps

**Discovery is complete. Next steps are GPS acquisition, pending verifications, and pipeline.**

1. ~~**Tier 7 (Conservancy)**~~ ✅ COMPLETE — 18 records staged.
2. ~~**Tier 8 (Private)**~~ ✅ COMPLETE — 6 records staged. All 36 seeds resolved.
3. **T7 pending items**: Simon Woods trail names (fetch arcofappalachia.org/visit-simon-woods when accessible); Scioto Bend Preserve county + data (fetch appalachiaohioalliance.org when accessible); ONAPA cross-check (blocked during discovery).
4. **Scioto Bridge to Bridge Route**: 36-mile shared-roadway bicycle route (Otway Covered Bridge to Mackletree Bridge through Shawnee State Forest) — assess whether it qualifies as a Trail entity and identify managing tier before pipeline.
5. **GPS acquisition pass**: Arc of Appalachia preserves (4 sites + 4 APs — all GPS blank); 535 On Second (GPS blank); Portsmouth city parks (13 entities, no GPS — addresses in Source Data below); outstanding Tier 1–5 items (Alum Rock, CCC Memorial, Brush Creek SF, Friendship Park, Clay Township Park, Eden Park).
6. **Pending verifications**: WNF trail inventory, Shawnee mountain bike named trails, Shawnee Bridle Trail segment names, Raven Rock Arch child site assessment, Riverfront Park/York Park identity, Larry Hisle Park governance.

---

## Pre-Discovery Checklist — Tier 7 ✅ COMPLETE

| Entity | Owner | Fetched? | Notes |
|--------|-------|----------|-------|
| Ohio Hanging Rock | Arc of Appalachia | ✅ (web search) | 750 ac, Frederick Rd Wheelersburg; Trail + AP staged |
| Simon Woods | Arc of Appalachia | ✅ partial | 670 ac, 8721 Pond Creek-Carey's Run Rd; trail names PENDING |
| Tremper Mound | Arc of Appalachia | ✅ (web search) | 706 ac, 20580 SR-73 McDermott; 3 Trails + 2 APs staged |
| Gladys Riley Golden Star Lily Preserve | Arc of Appalachia | ✅ (web search) | 230 ac, Tick Ridge-Koenig Hill Rd Otway; 2 Trails + AP staged |
| Scioto Bend Preserve | Appalachia Ohio Alliance | ✅ partial | County UNCERTAIN; acreage + GPS PENDING; site blocked |
| ONAPA cross-check | ONAPA | ☐ BLOCKED | onapa.org egress blocked; run when accessible |

---

## Pre-Discovery Checklist — Tier 8

*Purpose: enumerate all known entities with their primary URLs before beginning web discovery, so the session can go straight to fetching without reconstructing the list. Fill in "Fetched?" column as each is visited.*

| Entity | Owner | Primary URL to fetch | Fetched? | Key things to capture |
|--------|-------|----------------------|----------|-----------------------|
| Camp Oyo | Simon Kenton Council BSA | https://skcscouts.org/camps/camp-locations-and-rentals/camp-oyo/ | ✅ | 52 ac; 168 Shawnee Rd W; governance corrected from Dan Beard. GPS pending. |
| 535 On Second | MSPIB | https://www.mspohio.org/city-parks | ✅ partial | Staged; GPS still pending |
| Three Bridges Park | The Boneyfiddle Project | https://www.theboneyfiddleproject.org/ | ✅ | 131 Front St; event park; no trails |
| Otway Covered Bridge | Otway Historical Society | https://en.wikipedia.org/wiki/Otway_Covered_Bridge | ✅ | NRHP 1974; GPS confirmed; 5923 SR-348 |
| Scioto Bridge to Bridge Route | Unknown (assess) | Search pending | ☐ | 36-mi shared-roadway bicycle route; managing entity + entity type TBD |

*Note: Arc of Appalachia ×4 and Appalachia Ohio Alliance ×1 have been removed from this checklist — they are Tier 7 land trusts, correctly staged above.*

---

## Captured Source Data

*Purpose: key tabular data copied verbatim from primary web sources during discovery. Preserves data across context boundaries so re-fetching is not needed at staging time.*

### Portsmouth City Parks — Adopt-a-Park Table
**Source:** https://portsmouthohio.org/adopt-a-park/ (fetched 2026-03-28)
**Note:** GPS not captured at map verification — all 13 parks need GPS acquisition pass.

| Park Name | Address (from city page) | GPS Lat | GPS Lon |
|-----------|--------------------------|---------|---------|
| Alexandria Park | Scioto Street | — | — |
| Bannon Park | 15th Street and Robinson Avenue | — | — |
| Buckeye Park | Williams Street | — | — |
| Cyndee Secrest Park | Glen and Harding Avenue (Sciotoville neighborhood) | — | — |
| Labold Ball Fields | Williams and Boundary Streets | — | — |
| Martha Burton Park | Front Street | — | — |
| Mound Park | 17th Street and Hutchins Avenue | — | — |
| Roy Rogers Esplanade | Gallia Street and Chillicothe Street | — | — |
| Sciotoville Community Square | Harding Avenue (Sciotoville neighborhood) | — | — |
| Skate Park | 4th Street and Jefferson Street | — | — |
| Spock Memorial Dog Park | 2nd & Vine Streets | — | — |
| Tracy Park | 9th Street and Chillicothe Street | — | — |
| York Park | Ohio Riverfront | — | — |

*GPS column to be filled during GPS acquisition pass. Update in place rather than re-fetching the city page.*

### New Boston — Millbrook Park
**Source:** Google Maps (fetched 2026-03-28)

| Park Name | Address | GPS Lat | GPS Lon |
|-----------|---------|---------|---------|
| Millbrook Park | Oak Street, New Boston, OH 45662 | 38.759116 | -82.9286962 |

### Rarden — Rarden Community Park
**Source:** Google Maps (fetched 2026-03-28)

| Park Name | Address | GPS Lat | GPS Lon |
|-----------|---------|---------|---------|
| Rarden Community Park | 1363 Main Street, Rarden, OH 45671 | 38.923364 | -83.2461051 |

### Tier 5 Misses — GPS Confirmed
| Park Name | Address | GPS Lat | GPS Lon |
|-----------|---------|---------|---------|
| Brush Creek Twp. Community Park | 5715 OH-348, Otway, OH 45657 | 38.8600095 | -83.1922189 |
| Eden Park | Clay Township, OH 45662 | 38.7747982 | -82.9421173 |
