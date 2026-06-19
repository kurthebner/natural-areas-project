# Defiance County, Ohio — Session Log
**RUN_ID:** `defiance_oh_2026_04_19`
**PREFIX:** `DEF`
**County:** Defiance, Ohio
**Run date:** 2026-04-19 / 2026-04-20
**Status:** PIPELINE COMPLETE ✓

---

## County Context

- **County:** Defiance County, Ohio
- **FIPS:** 39039
- **County seat:** Defiance (city)
- **Major municipalities:** Defiance (city), Hicksville (village), Sherwood (village), Ney (village)
- **Townships (12):** Adams, Defiance, Delaware, Farmer, Hicksville, Highland, Mark, Milford, Noble, Richland, Tiffin, Washington
- **Major waterways:** Maumee River (east-flowing), Auglaize River (confluence with Maumee at Defiance), Tiffin River (confluence with Maumee at Defiance), Flatrock Creek
- **Park district:** No countywide park district. Defiance Soil and Water Conservation District manages Penney Nature Center.
- **Metropark affiliation:** None — Defiance County is outside Toledo Metroparks coverage.
- **Cross-county entities:** North Country NST/Buckeye Trail (multi-state/county); Maumee River Water Trail (Paulding–Defiance–Henry–Wood–Lucas); Hicksville Nature Trail (GOVERNANCE_UNCERTAIN).

---

## Baseline Pre-Analysis (2026-04-19)

Baseline file: `County_Spreadsheets/Defiance/Defiance.xlsx`
- Sheet1: 40 seeds (raw list)
- Sheet2: 41 seeds (enriched with GPS/URLs — treated as prompt, not fact)

**Seed audit result:** 27 confirmed, 9 excluded (dams/infrastructure/private/wrong-county), 3 resolved-as-infrastructure, 1 WRONG_COUNTY, 1 UNVERIFIED → full table in handoff document.

---

## Discovery — Tier Yield

| Tier | Source Type | Entities Found |
|------|-------------|----------------|
| T1 | Federal (NPS / NCT) | 1 Trail (North Country NST) |
| T2 | State (ODNR Parks, Wildlife, Water Trails) | 3 Sites, 2 Trails, 3 Access Points |
| T3 | District (Defiance SWCD) | 1 Site, 1 Trail, 1 Access Point |
| T4 | County (DCHS / Auglaize Village) | 1 Site |
| T5 | Township | NULL — 0 entities (all 12 townships confirmed) |
| T6 | Municipal (City of Defiance + Villages) | 23 Sites, 2 Trails, 2 Access Points |
| T7 | Conservancy / Land Trust | 1 Site, 1 Trail |
| T8 | Private / BSA | 3 Sites |
| **TOTAL** | | **32 Sites, 7 Trails, 0 Segments, 0 Networks, 6 Access Points = 45 entities** |

---

## Normalization Decisions

Key decisions made during Stage 2 normalization:

| Entity | category_raw | Normalized Category | Normalized Subtype | Rationale |
|--------|-------------|--------------------|--------------------|-----------|
| Independence Dam SP | State Park | Park | (none) | State Park = category Park + designation; no Park subtype applies |
| Oxbow Lake WA | Wildlife Area | Wildlife Area | State Wildlife Area | ODNR state-owned; §3.2 Wildlife Area subtype list |
| Winchester's Camp | Historic Site | Historic Site | Historic Landmark | ODNR Historic Site #24; encampment/burial site |
| Penney Nature Center | Nature Center; Nature Preserve | Nature Preserve | County Nature Preserve | County-owned land; §3.2 Nature Preserve subtype list |
| Auglaize Village | Living History Village; Heritage Village | Cultural Facility | Heritage Center | Living history/museum complex; §3.2 Cultural Facility subtype |
| Fort Grounds | Historic Park; Historic Site | Park | Historic Park | City-managed park on fort site; primary identity = park |
| Diehl Park | Community Park | Park | Sports Park | Multiple athletic fields dominate |
| Kingsbury | Community Park; Waterfront Park | Park | Waterfront Park | Auglaize River frontage is primary character |
| Bronson Park | Community Park | Park | Neighborhood Park | 25-ac multi-purpose residential park |
| Splash Park | Splash Pad; Community Park | Recreation Facility | (none) | Splash pad = no Recreation Facility subtype match; null subtype |
| Canal Park | Historic Park | Park | Historic Park | Historic Lock No. 37 ruins; city-managed |
| Reservoir and Disc Golf | Municipal Park; Water Recreation; Disc Golf | Park | Greenspace | Large multi-use reservoir park; no dominant sport |
| Pontiac Metro Park | Waterfront Park; Historic Park | Park | Waterfront Park | River confluence; boat ramp primary feature |
| Hometown Heroes Park | Memorial Park | Memorial | Veterans Memorial | Active duty recognition boards; §3.2 Memorial subtype |
| Veterans Memorial at Latty's Grove | Memorial Park; Historic Park | Memorial | Veterans Memorial | 1947 Veterans Memorial Grove designation |
| Hicksville Community Park | Community Park; Municipal Park | Park | Sports Park | Extensive multi-sport complex |
| Thoreau Wildlife Reserve | (none) | Nature Preserve | Private Nature Preserve | Private foundation; Audubon Sanctuary; public access since 2020 |
| Camp Lakota | (none) | Campground | Group Campground | BSA group camping; 14 campsites; aquatic program |
| Bark & Run Dog Park | (none) | Park | Dog Park | 501c3 nonprofit dog park; fenced areas |
| Shallow Creek Hunting Preserve | (none) | Hunting Area | (none) | ODNR-licensed hunting preserve; no subtype defined |
| Hicksville Veterans Memorial | Memorial Park | Memorial | Veterans Memorial | Village-maintained veterans memorial |

**Designation notes:**
- Independence Dam SP → `State Park`
- Oxbow Lake → `State Wildlife Area`
- Fort Grounds → blank (NRHP not in `ALLOWED_DESIGNATIONS` constants despite §4.2 of vocab markdown listing it; left blank with note)
- North Country NST → no designation field in trails table; noted in identity_notes

**Features normalization:** All `features` values validated against §6.2 ALLOWED_FEATURES. No violations. Key mappings applied:
- "historical marker" → `Historic Marker`
- "Lock Number 13 ruins" → `Historic Lock`
- "lock no. 37 remains" → `Historic Lock`
- "splash pad" → `Spray Park`
- "pavilion / shelter house" → `Pavilion`
- "shelter house" → `Pavilion`
- "boat launch" → `Boat Ramp`
- "historical miami and erie canal section" → `Canal Structure`

---

## GPS Acquisition (Stage 3)

| Method | Count | Notes |
|--------|-------|-------|
| Pre-populated (MED, §4.4 map verification) | 25 sites, 1 trail, 2 APs | All T6 entities from Google Maps URL capture |
| Nominatim (HIGH) | 5 sites, 1 trail, 2 APs | Auglaize Village, Hometown Heroes Park, Camp Lakota, Bark & Run, Shallow Creek; Hicksville Nature Trail; Five-Mile Creek AP, OH-111 AP |
| Fallback (LOW) | 4 sites, 2 APs | Independence Dam SP, Oxbow Lake WA, Penney NC, Thoreau Reserve; Independence Dam Boat Launch, Bend Road Bridge |
| Propagated from parent (LOW) | 2 sites, 4 trails, 1 AP | Winchester's Camp ← DEF-S-001; Trails DEF-T-003/T-004/T-005 ← parent sites; Penney NC Trailhead ← DEF-S-004 |
| **Final coverage** | **32/32 sites, 7/7 trails, 6/6 APs** | All entities have GPS |

LOW-confidence GPS entities requiring field verification or future geocoding pass:
- DEF-S-001 Independence Dam SP (41.268, -84.311)
- DEF-S-002 Oxbow Lake WA (41.330, -84.395)
- DEF-S-004 Penney Nature Center (41.225, -84.360) — Ashpacher Road not in Nominatim
- DEF-S-029 Thoreau Wildlife Reserve (41.280, -84.410) — Haller Road not in Nominatim

---

## Errors and Fixes

| Issue | Discovery | Fix |
|-------|-----------|-----|
| T7/T8 entities staged into wrong YAML key (`tier_6_entity_type_results` instead of `records`) | 2026-04-20 | Resolved via Python restructuring script that sorted by `discovery_tier` field; rebuilt all five top-level keys |
| Missing T6 City of Defiance null results for Trail Segments, Trail Networks, Site Networks | 2026-04-20 | Added 3 null result records to `tier_6_entity_type_results` |
| NRHP not in `ALLOWED_DESIGNATIONS` constants | 2026-04-20 | Left blank for all NRHP-only sites (Fort Grounds); noted in `notes` field |
| DEF-AP-001 Nominatim returned suspicious location (41.43) for County Rd 424 address | 2026-04-20 | Removed Nominatim query for DEF-AP-001; used fallback (LOW) + parent propagation |
| DEF-S-004 and DEF-S-029 Nominatim geocode failure (rural road addresses) | 2026-04-20 | Added LOW-confidence fallback coordinates; both entity notes flag for GPS field verification |

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1 — Resolution | COMPLETE | All 45 Defiance entities are unique within run; no merge decisions required |
| Stage 2 — Normalization | COMPLETE | 32 Sites, 7 Trails, 6 APs fully normalized; see Normalization Decisions above |
| Stage 3 — GPS Acquisition | COMPLETE | 32/32 sites, 7/7 trails, 6/6 APs have GPS; 4 sites LOW-confidence (flag for field verify) |
| Stage 4 — TSV Output | COMPLETE | 6 files written: defiance_oh_sites.tsv (32), defiance_oh_trails.tsv (7), defiance_oh_trail_segments.tsv (0), defiance_oh_trail_networks.tsv (0), defiance_oh_site_networks.tsv (0), defiance_oh_access_points.tsv (6) |
| Stage 4.5 — Vocab Gate | PASSED | All category, subtype, designation, status, features values validated; zero violations |
| Stage 5 — Integrity Check | PASSED | No integrity issues; all parent IDs resolve within run |
| Stage 6 — DB Upsert | COMPLETE | 32 sites, 7 trails, 6 APs committed to `natural_areas_v5.db`; 2 site_parent rows, 4 trail_parent rows, run_metadata inserted |

**Run completed:** 2026-04-20

---

## Entity ID Assignments

### Sites (32)
| ID | Name | Tier |
|----|------|------|
| DEF-S-001 | Independence Dam State Park | T2 |
| DEF-S-002 | Oxbow Lake Wildlife Area | T2 |
| DEF-S-003 | Winchester's Camp No. 3 / Fort Starvation | T2 (child of DEF-S-001) |
| DEF-S-004 | Penney Nature Center | T3 |
| DEF-S-005 | Auglaize Village | T4 |
| DEF-S-006 | Fort Grounds | T6 |
| DEF-S-007 | Diehl Park | T6 |
| DEF-S-008 | Kingsbury Riverfront Park, Pool, and Pickleball Facilities | T6 |
| DEF-S-009 | Bronson Park | T6 |
| DEF-S-010 | Splash Park | T6 (child of DEF-S-009) |
| DEF-S-011 | Canal Park | T6 |
| DEF-S-012 | Eastside Park | T6 |
| DEF-S-013 | Riverside Park | T6 |
| DEF-S-014 | Reservoir and Disc Golf | T6 |
| DEF-S-015 | Palmer Park | T6 |
| DEF-S-016 | Pontiac Metro Park | T6 |
| DEF-S-017 | William C. Holgate Park | T6 |
| DEF-S-018 | Hometown Heroes Park | T6 |
| DEF-S-019 | Triangle Park | T6 |
| DEF-S-020 | Veteran's Memorial Park at Latty's Grove | T6 |
| DEF-S-021 | Buchman Park on the Glaize | T6 |
| DEF-S-022 | Memory Park | T6 |
| DEF-S-023 | Hicksville Community Park | T6 |
| DEF-S-024 | Froggy Park | T6 |
| DEF-S-025 | Hicksville Veterans Memorial | T6 |
| DEF-S-026 | Little Reservation Station Park | T6 |
| DEF-S-027 | Moats Park | T6 |
| DEF-S-028 | Ney Park | T6 |
| DEF-S-029 | Thoreau Wildlife Reserve | T7 |
| DEF-S-030 | Camp Lakota / Camp Neil Armstrong | T8 |
| DEF-S-031 | Bark & Run Dog Park | T8 |
| DEF-S-032 | Shallow Creek Hunting Preserve | T8 |

### Trails (7)
| ID | Name | Tier |
|----|------|------|
| DEF-T-001 | North Country National Scenic Trail | T1 |
| DEF-T-002 | Maumee River Water Trail | T2 |
| DEF-T-003 | Miami and Erie Canal Towpath Trail | T2 (parent: DEF-S-001) |
| DEF-T-004 | Storybook Trail | T3 (parent: DEF-S-004) |
| DEF-T-005 | StoryWalk Trail | T6 (parent: DEF-S-009) |
| DEF-T-006 | Reservoir Nature Trail | T6 (parent: DEF-S-014) |
| DEF-T-007 | Hicksville Nature Trail | T7 |

### Access Points (6)
| ID | Name | Tier | Parent |
|----|------|------|--------|
| DEF-AP-001 | Independence Dam State Park Boat Launch | T2 | DEF-S-001 |
| DEF-AP-002 | Bend Road Bridge | T2 | (none) |
| DEF-AP-003 | Five-Mile Creek Access Area | T2 | (none) |
| DEF-AP-004 | Penney Nature Center Trailhead | T3 | DEF-S-004 |
| DEF-AP-005 | Pontiac Metro Park Boat Launch | T6 | DEF-S-016 |
| DEF-AP-006 | Reservoir Boat Ramp and Dock | T6 | DEF-S-014 |

---

## Open Flags (post-pipeline)

| Flag ID | Entity | Issue | Status |
|---------|--------|-------|--------|
| DEF-F-05 | Auglaize Village | County ownership vs. DCHS management not fully confirmed | Open — note in `notes` field |
| DEF-F-06 | Oxbow Lake WA | "Western agreement parcel" — no evidence found | Open — contact ODNR Wildlife |
| VERIFY_GOVERNANCE | DEF-S-016, DEF-AP-005 | Pontiac Metro Park ownership unclear (city manages but states "not city-owned") | Open — retained in `notes`; no blocking impact |
| GOVERNANCE_UNCERTAIN | DEF-T-007 | Hicksville Trail Association — no IRS registration; land ownership unknown | Open — retained in `identity_notes` |
| GPS_LOW | DEF-S-001, DEF-S-002, DEF-S-004, DEF-S-029 | LOW-confidence fallback coordinates | Field verification recommended |
| NRHP_GAP | DEF-S-006 (Fort Grounds) | NRHP listed 1980 but NRHP not in `ALLOWED_DESIGNATIONS` constants | Vocabulary constants need update OR designation intentionally excluded |

---

## Status

**PIPELINE COMPLETE** — All 8 discovery tiers complete; 45 entities normalized and committed to `natural_areas_v5.db`.

Output files in `County_Spreadsheets/Defiance/`:
- `defiance_oh_pipeline.py`
- `defiance_oh_sites.tsv`
- `defiance_oh_trails.tsv`
- `defiance_oh_trail_segments.tsv` (header only)
- `defiance_oh_trail_networks.tsv` (header only)
- `defiance_oh_site_networks.tsv` (header only)
- `defiance_oh_access_points.tsv`

Discovery staging: `defiance_oh_raw_discovery.yaml`
Handoff document: `defiance_oh_handoff.md`
