# Fulton County, OH — Handoff Document
# Natural Areas Project v5.2 | Started: 2026-04-13 | Discovery: COMPLETE | Last updated: 2026-06-12 — PAD-US SPOT-CHECK COMPLETE

## Supplemental Resolution — 2026-06-12

### PAD-US Spot-Check
All significant PAD-US entries cross-checked against DB:
- Goll Woods (415ac) → OH-FUL-S-0001 ✓
- Fulton Pond WA → OH-FUL-S-0005 ✓
- Delta Municipal Park → OH-FUL-S-0022 ✓
- Fulton Park South → OH-FUL-S-0013 (South Park Wauseon) ✓
- Swan Creek Preserve Metropark (415ac) → OH-LUC-S-0030 (Lucas County, not Fulton) ✓
- Maumee State Forest (1501ac + 1930ac) → OH-MC-S-0031 (multi-county) ✓
- Fayette County Fairgrounds (79ac) → false positive (Fayette County, OH — different county) ✓

MRQ 192 created for 4 residuals requiring verification at next Fulton full pipeline run:
- Swan Creek I (14ac), Swan Creek II Park (5ac) — small parcels along Swan Creek near Swanton; possibly unnamed greenway buffers; not web-findable as named parks
- Swan Creek Township Land Acquisition Project (41ac) — conservation parcel; public access status unknown
- Lyons Den Golf Course (94ac, Private) — location unverified; T8 private golf candidate; county attribution uncertain

---

## Batch Resolution Update — 2026-06-10
- +1 supplemental site: S-0038 Springfield Township Park (12ac, Springfield Twp, T5)
- +2 trail_parents: T-0016 → MC-S-0025 (Beach Ridge Singletrack); T-0017 → FUL-S-0002 (Chessie Circle → Harrison Lake SP)
- AP-0001 (Wabash Cannonball CR 23 Trailhead) added to held_entities (gps_missing)
- West Unity Memorial Park (11ac PAD-US): Brady Twp = Williams County — not a Fulton gap; MRQ for Williams County run
- 2 MRQ entries: West Unity Memorial Park (Williams Co) and Delta Park acreage discrepancy
- Final: 36 sites, 6 trail_parents, 1 AP in held_entities

### Open Items
- OH-FUL-AP-0001: GPS needed (Wabash Cannonball CR 23 Trailhead) — in held_entities
- Delta Park (S-0022): acreage discrepancy 23ac vs alt source 37ac — verify

## County Context
- **County seat**: Wauseon
- **Cities**: Wauseon
- **Villages**: Archbold, Delta, Fayette, Lyons, Metamora, Pettisville, Swanton (split Fulton/Lucas)
- **Townships**: Amboy, Chesterfield, Clinton, Franklin, Fulton, German, Swancreek, York
- **County park district**: None
- **Regional**: Metroparks Toledo — Oak Openings Corridor reaches into Swancreek Township (undeveloped conservation parcels)
- **State agencies**: ODNR DNAP, ODNR Parks & Watercraft, ODNR Division of Wildlife, ODNR Forestry
- **Cross-county trails**: Wabash Cannonball Trail (NORTA; Fulton/Henry/Williams/Lucas)

## Tiers Completed

| Tier | Name | Status | Sites | Trails | APs | Notes |
|------|------|--------|-------|--------|-----|-------|
| 1 | Federal | NULL | 0 | 0 | 0 | No federal land in Fulton County |
| 2 | State | COMPLETE | 5 | 5 | 0 | Goll Woods, Harrison Lake, Maumee SF, Tiffin River WA, Fulton Pond WA; 4 Goll Woods trails + Stewardship Trail |
| 3 | District | COMPLETE | 1 | 0 | 0 | Oak Openings Corridor (Metroparks Toledo parcels in Swancreek Twp) — held pending public access verification |
| 4 | County | NULL | 0 | 0 | 0 | No county park district |
| 5 | Township | NULL | 0 | 0 | 0 | No township parks |
| 6 | Municipal | COMPLETE | 24 | 1 | 0 | Wauseon(9+1trail), Archbold(6), Delta(2), Fayette(2), Lyons(3), Metamora(1), Swanton(3) |
| 7 | Conservancy | COMPLETE | 1 | 1 | 1 | Pettisville Park (PARC Inc.), Wabash Cannonball Trail (NORTA), CR 23 Trailhead AP |
| 8 | Private | COMPLETE | 4 | 0 | 0 | Sauder Village, Bracy Gold Bison Ranch, Camp Palmer, Robert Fulton Ag Center |

**Totals: 37 Sites | 7 Trails | 1 Access Point | 13 Null tier results**

## Tiers Remaining
None — all 8 tiers complete.

## Key Active Flags

1. **Turkeyfoot Creek Wildlife Area (baseline)** — NOT CONFIRMED in Fulton County. North Turkeyfoot Wildlife Area exists in Henry County. No ODNR property by this name found in Fulton County. Baseline seed likely refers to Henry County entity. **FLAG: Exclude from Fulton output; refer to Henry County run.**

2. **Archbold Reservoirs Fishing Area (baseline)** — Not a formal ODNR property name. Archbold Reservoirs (#1 and #2) are GNIS water bodies with ODNR fishing maps and public fishing access. No named ODNR property. **FLAG: Record as GNIS water sites; no standalone "Fishing Area" entity.**

3. **GNIS water features (7 seeds)**: Archbold Reservoir #1/#2, Delta Reservoir #1/#2, Metamora Reservoir, Swanton Waterworks Reservoir, Wauseon Reservoir #2 — not yet staged as entity records. These are water bodies, not parks; need resolution decision on whether they qualify as natural area sites.

4. **Longnecker Grove (baseline GNIS)** — Corresponds to location of Wildwood Park (Delta's first park, 1926, 7 acres, now overgrown/unmaintained). Same location; baseline treated it as a GNIS wooded area. **FLAG: Merge/resolve with Wildwood Park record during resolution.**

5. **Wabash Cannonball Trail (cross-county)** — Recorded as WIL-TR-003 in Williams County DB. Fulton County discovery has staged it as a Tier 7 trail entity. During resolution: determine whether to create FUL-TR record or upgrade both to a cross-county trail network entity. The Cannonball Trail (Wauseon 2-mile segment) is a municipal trail entity that should become a trail segment of the WCT parent.

6. **Maumee State Forest (cross-county)** — Staged as cross-county entity (Fulton/Henry/Lucas). Fulton County portion not specifically delineated. Hold pending GIS/cross-county resolution.

7. **Swanton parks (county split)** — Village of Swanton straddles Fulton/Lucas county line. Pilliod Park, Rotary Park, and Swanton Memorial Park all flagged for GIS verification to confirm which county.

8. **Oak Openings Corridor (Metroparks Toledo, Swancreek Twp)** — Undeveloped conservation parcels; public access status uncertain. **FLAG: Verify access before including as natural area entity.**

9. **Hatcher Park / Normal Grove Park (Fayette)** — Baseline seeds not independently confirmed from official Fayette parks page. Map verification required.

10. **Harmon Park (Wauseon)** — New discovery (not in baseline). No address found. Map verification needed.

11. **Metamora Community Park** — New discovery. No address or acreage from official source. Map verification needed.

12. **Wildwood Park (Delta)** — Described as "overgrown and no longer maintained." Active status uncertain — may need to be excluded or flagged as inactive.

## Entities Discovered (Ready for Pipeline)

### Sites (37)
**Tier 2 — State**
| ID (pending) | Name | Acres | Governance |
|---|---|---|---|
| — | Goll Woods State Nature Preserve | 320.64 | ODNR DNAP |
| — | Harrison Lake State Park | 142 | ODNR Parks & Watercraft |
| — | Maumee State Forest | 3,452 (cross-county) | ODNR Forestry |
| — | Tiffin River Wildlife Area | 465 | ODNR Wildlife |
| — | Fulton Pond Wildlife Area | 35 | ODNR Wildlife |

**Tier 3 — District**
| — | Oak Openings Corridor (Metroparks Toledo, Swancreek Twp) | ~1,900 (cross-county) | Metroparks Toledo |

**Tier 6 — Municipal (Wauseon)**
| — | Biddle Park | 73.4 | City of Wauseon |
| — | Depot Park | 1.9 | City of Wauseon |
| — | Rotary Park & Goodwin Preserve | 4.5 | City of Wauseon |
| — | Homecoming Park | 34.3 | City of Wauseon |
| — | Memorial Park (Wauseon) | 2.4 | City of Wauseon |
| — | Reighard Park | 18.5 | City of Wauseon |
| — | South Park (Wauseon) | — | City of Wauseon |
| — | Wabash Park (Wauseon) | — | City of Wauseon |
| — | Harmon Park *(new)* | 8.3 | City of Wauseon |

**Tier 6 — Municipal (Archbold)**
| — | Lion's Park | — | Village of Archbold |
| — | Memorial Park (Archbold) | 40+ | Village of Archbold |
| — | North Pointe Park | — | Village of Archbold |
| — | Ruihley Park | 27 | Village of Archbold |
| — | South Street Park | — | Village of Archbold |
| — | Woodland Park | ~60 | Village of Archbold |

**Tier 6 — Municipal (Delta)**
| — | Delta Park | 23 | Village of Delta |
| — | Wildwood Park *(new; status uncertain)* | 7 | Village of Delta |

**Tier 6 — Municipal (Fayette)**
| — | Hatcher Park *(pending verification)* | — | Village of Fayette |
| — | Normal Grove Park *(pending verification)* | — | Village of Fayette |

**Tier 6 — Municipal (Lyons)**
| — | Dunbar-Ingall Park | — | Village of Lyons |
| — | Green Memorial Park | — | Village of Lyons |
| — | Lyons Community Ball Park | — | Village of Lyons |

**Tier 6 — Municipal (Metamora)**
| — | Metamora Community Park *(new)* | — | Village of Metamora |

**Tier 6 — Municipal (Swanton)**
| — | Pilliod Park | 4.0 | Village of Swanton |
| — | Rotary Park (Swanton) | — | Village of Swanton |
| — | Swanton Memorial Park | 30+ | Village of Swanton |

**Tier 7 — Conservancy**
| — | Pettisville Community Park | 26.6 | PARC Inc. (501c3) |

**Tier 8 — Private**
| — | Sauder Village | 235 | Sauder Village (private) |
| — | Bracy Gold Bison Ranch | 55 | Bracy Gold (private) |
| — | 4-H Camp Palmer | 146 | 4-H Camp Palmer Inc./OSU |
| — | Robert Fulton Agriculture Center | — | OSU Extension |

### Trails (7)
| Name | Length | Governance | Tier |
|---|---|---|---|
| Toadshade Trail (Goll Woods) | 1.5 mi | ODNR DNAP | 2 |
| Tuliptree Trail (Goll Woods) | 1.25 mi | ODNR DNAP | 2 |
| Bur Oak Trail (Goll Woods) | 1.0 mi | ODNR DNAP | 2 |
| Cottonwood Trail (Goll Woods) | 1.5 mi | ODNR DNAP | 2 |
| Stewardship Trail (Maumee SF) | 2.0 mi | ODNR Forestry | 2 |
| Cannonball Trail (Wauseon) | 2.0 mi | City of Wauseon / NORTA | 6 |
| Wabash Cannonball Trail (North Fork) | 64.1 mi (cross-county) | NORTA | 7 |

### Access Points (1)
| Name | Parent | Tier |
|---|---|---|
| WCT — CR 23 Trailhead (Wauseon area) | Wabash Cannonball Trail | 7 |

## Held Entities
- **Maumee State Forest** — Cross-county (Fulton/Henry/Lucas); hold pending GIS delineation of Fulton County portion
- **Oak Openings Corridor parcels** — Hold pending public access verification
- **Wabash Cannonball Trail** — Cross-county (Fulton/Henry/Williams/Lucas); hold for cross-county trail network entity decision

## Unresolved Baseline Seeds
| Seed | Status |
|---|---|
| Turkeyfoot Creek Wildlife Area | NOT FOUND in Fulton County — likely Henry County entity |
| Archbold Reservoirs Fishing Area | No formal ODNR property; Archbold Reservoirs are GNIS water bodies |
| Archbold Reservoir #1 | GNIS water body — not yet staged; resolution needed |
| Archbold Reservoir #2 | GNIS water body — not yet staged; resolution needed |
| Delta Reservoir #1 | GNIS water body — not yet staged; resolution needed |
| Delta Reservoir #2 | GNIS water body — not yet staged; resolution needed |
| Metamora Reservoir | GNIS water body — not yet staged; resolution needed |
| Swanton Waterworks Reservoir | GNIS water body — not yet staged; resolution needed |
| Wauseon Reservoir #2 | GNIS water body — not yet staged; resolution needed |
| Longnecker Grove | GNIS feature = Wildwood Park location (Delta); merged into Wildwood Park record |
| Cannonball Trail (duplicate) | Duplicate of Cannonball Trail (Wauseon Segment) — consolidated |
| Goodwin Preserve | Merged with Rotary Park as single site entity |

## Open Questions
1. Are the 7 GNIS reservoir/water features in scope as natural area entities? (Archbold Res #1/#2, Delta Res #1/#2, Metamora Reservoir, Swanton Waterworks Reservoir, Wauseon Reservoir #2)
2. Do Metroparks Toledo's undeveloped Swan Creek Township parcels have any public access or trails?
3. Which of Swanton's three parks (Pilliod, Rotary, Memorial) fall in Fulton County vs. Lucas County?
4. Should Wildwood Park (Delta) be included given it's described as "overgrown and no longer maintained"?
5. Should Wabash Cannonball Trail be one cross-county trail network entity rather than per-county trail records?
6. Does Maumee State Forest have any named access points within the Fulton County portion?
7. Are Hatcher Park and Normal Grove Park (Fayette) confirmed to exist — map verification required.

## Next Steps
1. Run resolution pass (YAML → TSV)
2. Map verification for all GPS-blank entities (particularly Wauseon parks, Archbold parks, Lyons parks, Fayette parks, Metamora)
3. Resolve GNIS water features: stage or exclude
4. Resolve cross-county entities: WCT, Maumee SF
5. Vocabulary normalization pass
6. GPS acquisition pass
7. TSV output → DB upsert

## Pre-Discovery Checklist
All municipalities and tiers visited. Discovery complete.

## Captured Source Data

### Archbold Parks (from archbold.com/parks___recreation/parks.php)
| Park | Acres | Location | Key Features |
|---|---|---|---|
| Lion's Park | — | East Holland Street | Basketball, playground |
| Memorial Park | 40+ | South side of Archbold | Volleyball, basketball, 4 tennis courts, playground, shelter, restrooms |
| North Pointe Park | — | St. Anne & Primrose Streets | Playground, lighted basketball, picnic shelter, sledding hill |
| Ruihley Park | 27 | Holland & Walnut Streets | Pavilion, Scout Cabin, pool, splash pad, pickleball, playgrounds, walking paths |
| South Street Park | — | South & West Streets | Playground, basketball |
| Woodland Park | ~60 | SR 66/Woodland Oaks | Playground, restrooms, concession, basketball, walking trails, disc golf |

### Wauseon Parks (from cityofwauseon.com/our-parks + mypacer.com)
| Park | Acres | Location | Key Features |
|---|---|---|---|
| Biddle Park | 73.4 | Wauseon | 8 baseball/softball fields, basketball, volleyball, football, soccer |
| Depot Park | 1.9 | Wauseon | Historic train depot, caboose, wooden play train |
| Harmon Park | 8.3 | Wauseon | Walking/running trails |
| Homecoming Park | 34.3 | Wauseon | Sledding, playgrounds, gazebo, pickleball, pavilions |
| Memorial/North Park | 2.4 | West Elm St | Playground, basketball, war memorial |
| Reighard Park | 18.5 | 615 Oak St | Disc golf, pool, playground, shelter houses, tennis |
| Rotary Park & Goodwin Preserve | 4.5 | Wood Street | Fishing pond, playground, wooded preserve |
| South Park | — | Wauseon | Playground, lighted basketball |
| Wabash Park | — | Wauseon | Playground, basketball, skate park |
| Cannonball Trail | 2 mi | East-West through city | Blacktop multi-use trail |

### Swanton Parks (from visitfultoncounty.com)
| Park | Acres | Features |
|---|---|---|
| Pilliod Park | 4.0 | Red caboose, gazebos, paved walkway, holiday lights; next to library |
| Rotary Park | — | Offshoot of Pilliod Park |
| Swanton Memorial Park | 30+ | Baseball, soccer, volleyball, tennis/pickleball, basketball, playgrounds; Ai Creek |

### State Properties (ODNR)
| Name | Acres | Address | GPS |
|---|---|---|---|
| Goll Woods SNP | 320.64 | 5800 CR 26, Archbold, OH 43502 | 41.554461, -84.361370 |
| Harrison Lake SP | 142 | 26246 Harrison Lake Rd, Fayette, OH 43521 | 41.64361, -84.37222 |
| Maumee State Forest | 3,452 | 3390 County Rd D, Swanton, OH 43558 | 41.52056, -83.90194 |
| Tiffin River WA | 465 | SR 66 between Fayette & Archbold | 41.60556, -84.31167 |
| Fulton Pond WA | 35 | 8529 Co Rd 3, Swanton, OH 43558 | 41.5972, -83.9278 |
