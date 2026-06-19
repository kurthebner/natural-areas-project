# Sandusky OH — Session Log
**RUN_ID:** `sandusky_ohio_2026_05_21`
**PREFIX:** `SAN`
**County:** Sandusky, Ohio
**Run date:** 2026-05-20 through 2026-05-22
**Status:** COMPLETE — DB upsert committed 2026-05-22

---

## Discovery — Tier Yield

| Tier | Source Type | Query / Source | Entities Found |
|------|-------------|----------------|----------------|
| T1 | Federal & Tribal | NPS state page, USFWS Ohio refuges, USACE Sandusky River, VA NCA cem.va.gov, BLM Eastern States, DoD OH installations, tribal registry | 0 — null across all entity types |
| T2 | State | ODNR Find-a-Property, ODNR Wildlife/Parks/Forestry/DNAP/Scenic Rivers, OHC, ODOT, OTIC (ohioturnpike.org), OSU Extension | 11 — Spiegel Grove, Pickerel Creek WA, Resthaven WA, Willow Point WA, Sandusky Scenic River, Ron Abraham Forest, Aldrich Pond WA, SAN WA 1-7 group, 3 APs |
| T3 | District (Sandusky County Park District) | SCPD lovemyparks.com; Ohio Auditor pre-enum; sanduskycoswcd.org | 25 — 20 Sites (16 SCPD parks + 4 White Star child), 2 Trails (NCIT + WSP Quarry Loop), 3 APs; SWCD null |
| T4 | County | sanduskycountyoh.gov; sanduskycounty.org (CVB); NRHP Wikipedia; ohiodnr.gov; OHGenWeb cemeteries | 0 direct county entities — NULL; 2 cross-tier misses caught (Waggoner's Run → T3, Darr-Root AP → T2); Sand Docks + Raccoon Creek Res flagged for T6 |
| T5 | Township (12 townships) | OTA roster; individual township websites (8 with websites); search for 4 without; OHGenWeb; Find A Grave | 34 — 4 parks (Ballville×3 + Sandusky Twp); 30 cemeteries across 12 townships; Green Creek cem unconfirmed |
| T6 | Municipal | fremontohio.org/parks; clydeohio.org/165/Parks; gibsonburgohio.org/parks-recreation; villageofwoodville.com/parks; bellevuerec.com/parks; individual village searches | 39 — Fremont (9 parks + 2 APs); Clyde (5 parks + Raccoon Creek Res + McPherson Cem); Gibsonburg (4 parks + 1 trail); Woodville village (4 parks + cemetery); Bellevue 7 parks GIS_VERIFY; Elmore 3 parks GIS_VERIFY; Lindsey 1 park; Burgoon/Helena nulls; Green Springs null pending human contact |
| T7 | Conservancy & Land Trust | blackswamp.org; ncolc.org; wrlandconservancy.org; ONAPA; LTA directory; westernwildlifecorridor.org | 0 new entities — NULL. BSC properties already at T3/SCPD; agricultural easements excluded §4.2; ONAPA: 0 state preserves in Sandusky County; WWC resolved as Cincinnati-area org; 7 null blocks |
| T8 | Private | OhioGenealogyExpress sandusky cemetery list; PGA.com; CVB; wrhuntclub.com; schedel-gardens.org; direct searches | 44 records — 7 golf courses (Sycamore Hills, Fremont CC, Green Hills, Hidden Hills, River Cliff uncertain, Sugar Creek GIS_VERIFY, Sleepy Hollow CLOSED); WR Hunt Club; Schedel Arboretum (GIS_VERIFY); 10 church cemeteries + 1 commercial + 21 family + 3 governance-uncertain (GNIS-enumerated); 6 null blocks |

**Total raw records:** 155 (T2: 12, T3: 26, T4: 0, T5: 34, T6: 39, T7: 0, T8: 44)
**By entity type (raw):** 142 Sites, 4 Trails, 9 Access Points, 0 Trail Segments, 0 Trail Networks, 0 Site Networks
**Post-resolution:** PENDING — to be determined after Stage 1 Resolution Engine

---

## Normalization Decisions

- **SAN-S-001 designation:** Multi-value `NRHP;State Memorial;State Park` (from normalization script) corrected to `National Historic Landmark` (NHL 1964, confirmed from identity_notes_raw).
- **SAN-T-001 → OH-MC-T-0110:** NCIT provisional ID retired at upsert; trail stored in DB as OH-MC-T-0110.
- **CATEGORY_OVERRIDES applied** to 23 sites where name/governance-based classification differed from default rules (Historic Sites, Wildlife Areas, Conservation Areas, Parks, Water Sites, Campgrounds, Cemeteries).
- **gps_unresolvable=True** applied to: SAN-S-008 (ODNR numbered wildlife areas — distributed non-point tracts); SAN-T-001 (NCIT — linear corridor).

---

## GPS Acquisition

| Pass | Method | Acquired | Cumulative |
|------|--------|----------|-----------|
| Pass 1 | Nominatim batch (address queries from YAML) | 68 | 68 |
| Pass 2 | Alternate queries (name+city, name+county) | 18 | 86 |
| Pass 3 | Corrected SCPD addresses + targeted lookups | 13 | 99 |
| **Gate** | GPS Gate (Stage 2c/2d) | filled 99 into entity records | — |
| Still null after 3 passes | | 18 entities (held for gps_missing) | — |

---

## Errors and Fixes

- **Normalization run 1:** `clean_org()` regex only matched `(inferred)` and `(inferred from GNIS)`. Fixed to `r'\s*\(inferred[^)]*\)'` to catch all variants.
- **Normalization run 1:** Missing FEATURE_MAP patterns for Arboretum, Museum Building, Historic Structure, Grave/Burial Site, Fire Ring. Added in run 2.
- **Vocab gate:** SAN-S-001 designation was multi-value semicolon string; corrected to `National Historic Landmark` before pipeline re-run.
- **Unicode error on Windows console:** `na_pipeline_core.py` contains `→` (U+2192). Resolved by running `python -X utf8`.

---

## Pipeline Stage Log

| Stage | Result | Notes |
|-------|--------|-------|
| Stage 1a/1b | COMPLETE | Resolution Engine: 155 raw → 142 sites, 4 trails, 9 APs after ID assignment; 10 cross_county_held at Phase 0 |
| Stage 2a | COMPLETE | GPS fill-forward: 99 fallback_gps entries preserved from 3-pass acquisition |
| Stage 2b | COMPLETE | GPS Gate: 99 GPS filled; 2 gps_unresolvable (SAN-S-008, SAN-T-001); 44 held for gps_missing |
| Stage 2c/2d | COMPLETE | GPS Gate applied to Sites and APs; 55 total held |
| Stage 3 | COMPLETE | Normalization: 100 active entities (94 sites, 2 trails, 4 APs) normalized via `_stage_normalization.py` |
| Stage 4.5 | PASSED | Vocabulary Validation Gate: all vocab checks passed after SAN-S-001 designation fix |
| Stage 4 | COMPLETE | TSV Output: 94 sites, 2 trails, 4 APs written to `sandusky_*.tsv` |
| Stage 5 | COMPLETE (warnings) | Integrity Check: 2 expected warnings — SAN-S-008 GPS null (gps_unresolvable), SAN-AP-004 parent OH-MC-T-0110 not in site IDs (trail parent) |
| Stage 5.5 | PASSED | Human Review Gate: confirmed by user 2026-05-22 |
| Stage 6 | COMPLETE | DB Upsert: 94 sites, 2 trails, 4 APs committed; 55 held_entities inserted; 2 access_point_parents inserted; run_metadata.held corrected to 55 |
| Stage 1 — Resolution | COMPLETE | 155 raw → 145 active; 10 held (cross_county_held); NCIT → OH-MC-T-0110; 5 manual review; 9 CROSS_COUNTY_CANDIDATE |
| Stage 2 — GPS Fill-Forward | COMPLETE — NULL | DB empty (first county run); no prior GPS to fill |
| Stage 3 — GPS Acquisition | IN PROGRESS | |
| Stage 4 — Normalization | PENDING | |
| Stage 5 — TSV Output | PENDING | |
| Stage 5.5 — Vocab Gate | PENDING | |
| Stage 6 — Integrity Check | PENDING | |
| Stage 6.5 — Human Review | PENDING | |
| Stage 7 — DB Upsert | PENDING | |

---

## Entity ID Assignments

*(to be populated post-resolution)*

---

## Open Flags

None yet.

---

## Status

**IN PROGRESS**
Bootstrap complete. Beginning Tier 1 (Federal & Tribal) discovery.
