# Hancock County Ohio — Session Log
**RUN_ID:** `hancock_ohio_2026_05_12`  
**PREFIX:** `HAN`  
**County:** Hancock County, Ohio  
**Run date:** 2026-05-12 through 2026-05-16  
**Status:** COMPLETE — all tiers + pipeline + GPS acquisition done

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal | NPS, USFWS, USFS, BLM, USACE, DoD, Tribal | 0 — all 6 entity types null |
| T2 | State | ODNR Parks & Watercraft, ODNR Wildlife (WAs + WPAs), ODNR DNAP, OHC | 47 — 15 Sites, 3 Trails, 19 Trail Segments, 10 APs |
| T3 | District | Hancock Park District (hancockparks.com) | 60 — 25 Sites, 9 Trails, 16 Trail Segments, 0 Trail Networks, 0 Site Networks, 9 APs (incl. 7 HPD community parks/APs added during T6) |
| T4 | County | Hancock County government, NRHP, commissioners | 1 — Hancock County Infirmary Cemetery |
| T5 | Township | 17 townships (Townships_Officials2022-2023.xlsx) | 15 — 15 Sites (cemeteries), 0 Trails/Segments/Networks/APs |
| T6 | Municipal | Findlay, Fostoria, Arlington, Arcadia, Benton Ridge, Bluffton, McComb, Mt. Blanchard, Van Buren, Vanlue | 61 — 45 Sites, 12 Trails, 1 Site Network (+5 T6 misses found during T8) |
| T7 | Conservancy | BSC, TNC, WRLC, ONAPA, DU, ODNR VPP | 0 — all 6 entity types null |
| T8 | Private | BSA/Scouting America, ODNR hunting preserves, private golf, eBird | 1 — Camp Berry (BSA) |

**Total raw records in YAML:** 185  
**Post-normalization (pipeline):** 102 Sites, 25 Trails, 35 Trail Segments, 0 Trail Networks, 1 Site Network, 19 APs = **182 entities**  
*(3 Allen County records excluded from Hancock pipeline: Buckeye Park, Bluffton Community Pool, Maple Grove Cemetery — county_primary=Allen in YAML)*

---

## Normalization Decisions

Key decisions made during normalization (hancock_oh_normalize.py, 2026-05-16):

- **IMP-068 hard-assigned institutions:** Great Karg Well → Historic Site; Blanchard River Greenway Trail → Greenway; Old Mill Stream Scenic Byway → Scenic Byway
- **Wildlife areas:** 7 named WAs + 7 WPAs → category=Wildlife Area, subtype=State Wildlife Area, designation=State Wildlife Area
- **IMP-099 cemetery subtypes:** 14 cemetery subtypes assigned per ordered rule set (Public/Church/Private/Veterans)
- **IMP-065 subtype inference:** Nature Preserve category → subtype inferred as County Nature Preserve (HPD-managed)
- **Riverbend Recreation Area / Aeraland Recreation Area:** Corrected from Recreation Facility to Park/Greenspace (passive natural areas along Blanchard River)
- **Trail use_type overrides:** 23 trail-specific overrides applied (Heritage Trail → Multi-Use; Water Trail → Water; lake trails → Hiking; Bluffton Bicycle Pathway → Bicycling, etc.)
- **Cross-county flagged:** HAN-S-098 (Bluffton Village Park), HAN-T-012 (Old Mill Stream Scenic Byway), HAN-T-023 (Bluffton Bicycle Pathway)

---

## GPS Acquisition

**Nominatim queries:** 61 entities queried (city-specific queries; rural township road addresses dropped — not in OSM)  
**Resolved:** 34 entities via Nominatim  
**Fallback from YAML:** 38 entities (gps_lat_raw/gps_lon_raw from map verification pass)  
**Parent propagation:** 5 APs (Van Buren SP APs from SP centroid); 1 site (VBSP Campground from parent SP)  
**Total with GPS:** 69/102 sites, 13/19 APs  
**GPS-null:** 33 sites — 13 wildlife areas/WPAs (unresolvable — no OSM entries for numbered parcels); ~20 small parks/athletic fields (not in OSM)

---

## Errors and Fixes

| # | Stage | Error | Fix |
|---|-------|-------|-----|
| 1 | Normalization | Trail field names `surface`/`origin` vs pipeline core's `surface_type`/`origin_type` | Renamed keys in all 25 trail records in config JSON |
| 2 | Normalization | Missing trail fields: `accessibility`, `alternate_names`, `maps`, `partner_agencies`, `trail_history` | Added as empty strings to all 25 trail records |
| 3 | GPS | Bbox lat_max=41.15 excluded Fostoria sites at ~41.16–41.17°N | Expanded to 41.18 to cover full Hancock County incl. Fostoria NE corner |
| 4 | Vocab gate | "Mountain Biking" not in ALLOWED_FEATURES | Removed from FEATURE_MAP output (dropped with warning) |
| 5 | Normalization | Site network type "Recreation Complex" not in vocabulary | Corrected to "Multi-Site Recreation Network" |
| 6 | Normalization | Riverbend RA / Aeraland RA categorized as Recreation Facility | Patched to Park (passive natural areas along Blanchard River) |
| 7 | Normalization | Trails T4–T25 missing use_type (None in YAML) | Applied 23 trail-specific overrides via inline patch script |
| 8 | Normalization | HAN-AP-019 (Island Park AP) missing parent_entity_id | Fixed: set parent to site_name_to_id['Island Park'] = HAN-S-091 |
| 9 | GPS | Nominatim township road addresses return NULL (not in OSM) | Built city-specific query overrides (e.g., "Emory Adams Park, Findlay, Ohio") |
| 10 | GPS | Wildlife area Nominatim queries return NULL | Set query to empty string; GPS remains null; documented as unresolvable |
| 11 | Pipeline | Bash timeout on Nominatim pass (75 queries × 1.1 sec > 44 sec) | Ran --skip-gps first to commit all entities; GPS acquisition done separately in batches |
| 12 | Pipeline | First GPS batch returned all NULL (old pre-override queries) | Applied QUERY_OVERRIDES to config; re-ran with city-specific queries |
| 13 | DB | `access_points` PK column is `access_point_id` not `ap_id` | Corrected column name in GPS update SQL |

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1 — Resolution | COMPLETE | Mechanical grouping; 3 Allen County records excluded from Hancock output; 3 cross-county candidates flagged |
| Stage 2 — Normalization | COMPLETE | 182 entities normalized; see Normalization Decisions above |
| Stage 3 — GPS Acquisition | COMPLETE | 69/102 sites with GPS; see GPS Acquisition section |
| Stage 4 — TSV Output | COMPLETE | 6 TSV files generated; sites/APs TSVs regenerated post-GPS-update |
| Stage 4.5 — Vocab Gate | PASSED | 0 vocabulary violations |
| Stage 5 — Integrity Check | PASSED | No duplicate IDs; parent refs valid |
| Stage 5.5 — Human Review | CONFIRMED | Reviewer confirmed 2026-05-16: "yes looks good" |
| Stage 6 — DB Upsert | COMPLETE | run_id=hancock_ohio_2026_05_12; 182 entities in natural_areas_v5.db |

---

## Entity ID Assignments

| Type | Range | Count |
|------|-------|-------|
| Sites | HAN-S-001 – HAN-S-102 | 102 |
| Trails | HAN-T-001 – HAN-T-025 | 25 |
| Trail Segments | HAN-TS-001 – HAN-TS-035 | 35 |
| Trail Networks | (none) | 0 |
| Site Networks | HAN-SN-001 | 1 |
| Access Points | HAN-AP-001 – HAN-AP-019 | 19 |

---

## Open Flags

| Flag ID | Entity | Issue | Resolution Path |
|---------|--------|-------|-----------------|
| LOCAL-003 | Old Mill Stream Scenic Byway (HAN-T-012) | CROSS_COUNTY_CANDIDATE (Hancock+Putnam); byway is a driving route | Resolve when Putnam County run executes |
| LOCAL-005 partial | Bluffton Bicycle Pathway (HAN-T-023) | CROSS_COUNTY_CANDIDATE (Hancock+Allen) | Resolve when Allen County run executes |
| LOCAL-005 partial | Bluffton Village Park (HAN-S-098) | CROSS_COUNTY_CANDIDATE (Hancock+Allen) | Resolve when Allen County run executes |
| LOCAL-SOFT-1 | Portage Township Cemetery (HAN-S-048) | UNCONFIRMED_NAME — name not determinable from audit alone | Contact trustees at 9313 CR 203, Van Buren OH 45889 |

---

## Status

**COMPLETE — 2026-05-16; supplemental golf course upsert 2026-05-16**  
182 entities upserted to natural_areas_v5.db at pipeline completion. Supplemental: 10 golf courses added (HAN-S-103 – HAN-S-112) per IMP-105 scope expansion (all golf courses, public and private). Total HAN sites now 112. sites.tsv regenerated (112 rows). T8 sub-procedure updated to v5.6.
