# Hancock County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline runs:** hancock_ohio_2026_05_12 (main); hancock_ohio_LOCAL007_cem_suppl (cemetery supplemental)
**DB state at review:** post-remediation fixes applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 159 | OH-HAN-S-0001–0166 with gaps; 0 MC |
| Trails | 25 | All OH-HAN-T-; OH-HAN-T-0012 (Old Mill Stream Scenic Byway) is cross-county Hancock;Putnam |
| Trail segments | 0 | **MISSING — 35 records in TSV but never upserted to DB** |
| Trail networks | 0 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | **MISSING — 1 record in TSV (Flag City Sports Complex SN) but never upserted** |
| Access points | 19 | OH-HAN-AP-0001–0019 |
| Held entities | 0 | — |

Run metadata: hancock_ohio_2026_05_12: input=182, normalized=182, held=0.
Run metadata (cemetery suppl): hancock_ohio_LOCAL007_cem_suppl: input=54, normalized=54, held=0.

**Handoff note:** "DB Upsert ✅ COMPLETE 2026-05-16 — 182 entities in natural_areas_v5.db." Reference to v5.db in handoff is a copy-paste artifact; run_metadata is confirmed in v6 DB. However, the trail_segments table (35 records) and site_networks table (1 record) were NOT upserted. These entities exist in the TSV output files in the county spreadsheet folder but are absent from the DB. The upsert script did not include these table types, or they failed silently.

Site sequence: max OH-HAN-S-0166, count=159; gaps at S-0009, S-0011–0015, S-0048 (7 gaps) — consistent with discovery retirements (IMP-117).

---

## GPS Audit

**Sites:** All 159 sites have GPS coordinates. No nulls. ✓

**GPS clusters (legitimate co-location):**
- OH-HAN-S-0057, 0058, 0059 share GPS (41.0824789, −83.6529375) — Roethlisberger Field, The Cube Ice Arena, Marathon Diamonds — all sub-facilities of Flag City Sports Complex at 3430 N. Main St, Findlay. Acceptable.
- OH-HAN-S-0065, 0066, 0069 share GPS (41.0244774, −83.626416) — Guthrie Field, Hancock Field, Remington Field — individual ball fields within the same complex. Acceptable.
- OH-HAN-S-0091, 0096 share GPS (40.901014, −83.558647) — Island Park and Mt. Blanchard Pool (adjacent facilities in Village of Mt. Blanchard). Acceptable.

**Access points:** 6 of 19 APs have null GPS — OH-HAN-AP-0005 through 0010 (Wildlife Area 1, 3–7 parking areas). These parent sites themselves have GPS but the specific parking lot coordinates were not acquired. Acceptable given WA access is informal; flag for GPS acquisition pass.

---

## Held Entities

None. ✓

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Hancock` on 2026-06-08.

- PAD-US records in bbox: 49
- Matched (score ≥ 80): 27
- Unmatched: 11
- Skipped (private/excluded): 11

**Skipped correctly:** 8 private golf courses (already in DB as T8 private sites S-0103–0112), Hancock County Fairgrounds (excluded keyword), Enright Park (private), YMCA Campsite (private). All appropriate. ✓

**Near-miss false misses (in DB, below threshold):**

| PAD-US name | Score | DB record | Notes |
|---|---|---|---|
| Riverbend Park (128ac) | 79 | OH-HAN-S-0018 Riverbend Recreation Area (129ac) | Same entity — different PAD-US vs local name; 1ac acreage difference confirms match |
| Allen Township Sportsplex (20ac) | 67 | OH-HAN-S-0093 Van Buren Sportsplex | Same entity — Allen Township Van Buren Sportsplex; different name in PAD-US vs handoff |

**Bbox false positives:**
- "Wood County Historical Center" (54ac, Regional Agency Land) — Bowling Green, Wood County; bbox extends south into Wood County
- "Slippery Elm Trail" (100ac, Regional Agency Land) — Wood County trail; same bbox issue

**Multiple PAD-US WPA records all matching S-0010:**
PAD-US lists 11 individual Wildlife Production Areas (WPAs 6, 8, 9, 11, 20, 21, 25, 41, 42, 46, 58) ranging from 39–77ac each, all scoring ≥ 94 to OH-HAN-S-0010 "Wildlife Production Area 25 Wildlife Area." Only WPA 25 is individually cataloged. The other 10 WPAs exist as distinct ODNR-managed parcels and should each be a separate T2 site record. Cumulative area ~600ac of ODNR-managed wildlife production land not individually cataloged.

**Indian Green acreage discrepancy:**
PAD-US "Indian Green Preserve" (81ac, GAP2) matched to OH-HAN-S-0021 "Indian Green–Worden Family Conservation Area" (27.3ac) at score 62 — below threshold, but likely the same entity. The 53.7ac difference suggests PAD-US includes expansion parcels beyond the original discovery record. Verify actual acreage and update if expansion confirmed.

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Sponsler Property Acquisition - Cricket Frog Cove | 2 | 156 | County Land | T4 | HIGH — 156ac county-owned conservation land, GAP2 |
| Rudolph-Savanna Preserve | 2 | 52 | County Land | T4 | HIGH — 52ac county savanna preserve, GAP2 |
| District 2 — Findlay Wildlife Area | 2 | 6 | ODNR | T2 | MEDIUM — ODNR wildlife area, GAP2 |
| Anchor Park | 4 | 5 | City Land | T6 | LOW — Findlay city park |
| Douglas Park | 4 | 1 | City Land | T6 | LOW — Findlay city park |
| Civitan Park | 4 | 2 | County Land | T4 | LOW — small county park |
| Wildlife Production Areas 6, 8, 9, 11, 20, 21, 41, 42, 46, 58 | 2 | ~550ac total | ODNR | T2 | MEDIUM — 10 individual WPA parcels not individually cataloged |

**PAD-US result: PARTIAL FAIL — two HIGH-severity county conservation land gaps (Cricket Frog Cove 156ac, Rudolph-Savanna Preserve 52ac), ODNR District 2 WA, and 10+ Wildlife Production Areas not individually cataloged.**

---

## Relationship Table Audit

**trail_parents:** 0 Hancock trails have trail_parents entries. All 25 trails are without parent site links. This is a partial upsert issue — the trail_parents table was not populated during the Hancock pipeline run. Key missing links:

| Trail | Expected parent |
|---|---|
| OH-HAN-T-0001 (Van Buren Hiking Trails) | OH-HAN-S-0001 (Van Buren State Park) |
| OH-HAN-T-0002 (Van Buren MTB Trails) | OH-HAN-S-0001 |
| OH-HAN-T-0003 (Van Buren Bridle Trails) | OH-HAN-S-0001 |
| OH-HAN-T-0004 (Heritage Trail) | OH-HAN-S-0018 (Riverbend Recreation Area) |
| OH-HAN-T-0005 (Blanchard River Water Trail) | No single parent expected |
| OH-HAN-T-0006 (Blanchard River Greenway Trail) | OH-HAN-S-0018 |
| OH-HAN-T-0016–0021 (Reservoir walking trails) | OH-HAN-S-0080–0085 (respective reservoirs) |

**site_parent:** No Hancock parent-child site relationships — consistent with pipeline (all sub-facilities are separate sites, not child sites). Acceptable.

**access_point_parents:** All 19 APs now reference valid site IDs after this session's fixes. ✓

**Trail segments:** 35 records exist in TSV (`hancock_ohio_2026_05_12_trail_segments.tsv`) but are absent from DB:
- 19 Van Buren State Park segments (hiking, MTB, and bridle color loops + connectors) — parents: OH-HAN-T-0001/0002/0003
- 16 Heritage Trail named segments (Segment 1–16) — parent: OH-HAN-T-0004

TSV schema does not include `segment_id` or `parent_trail_id` columns — IDs and parent links must be assigned at upsert time. Batch phase action.

**Flag City Sports Complex SN:** 1 site network record in TSV (`hancock_ohio_2026_05_12_site_networks.tsv`) with 10 member sites (OH-HAN-S-0055/0057/0059/0060/0056/0062/0065/0066/0067/0069). Not in DB. Note: TSV member_site_ids use 3-digit format (OH-HAN-S-055) — must be corrected to 4-digit (OH-HAN-S-0055) at upsert. Batch phase action.

---

## Open Flags from Pipeline Run / Handoff

| Flag | Entity | Status |
|---|---|---|
| Cross-county candidate | OH-HAN-S-0098 Bluffton Village Park | counties corrected from malformed "Hancock, Ohio;Allen, Ohio" to "Allen;Hancock" this session. CROSS_COUNTY_CANDIDATE flag in identity_notes. |
| Cross-county candidate | OH-HAN-T-0023 Bluffton Bicycle Pathway | counties = "Hancock;Allen". Pending Allen County run. |
| Cross-county candidate | OH-HAN-T-0012 Old Mill Stream Scenic Byway | counties = "Hancock;Putnam". Also identity-flagged as driving byway. Pending Putnam County run. |
| LOCAL-006 | 7 Copilot-flagged speculative entries | Open — not staged. Revisit when Hancock supplemental pass is run. |

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | 19 APs with non-padded parent_entity_ids (OH-HAN-S-001 format) — all 19 referencing non-existent site IDs | **Fixed 2026-06-08** — corrected all 19 to zero-padded format; all 19 parents now verified as existing |
| 2 | ~~MEDIUM~~ FIXED | OH-HAN-S-0098 counties malformed ("Hancock, Ohio;Allen, Ohio") | **Fixed 2026-06-08** — corrected to "Allen;Hancock" |
| 3 | HIGH | 35 trail_segment records in TSV not upserted to DB | Batch phase: assign segment_ids OH-HAN-TS-0001 onward, assign parent_trail_ids, upsert to trail_segments |
| 4 | HIGH | 1 site_network record (Flag City Sports Complex SN) in TSV not upserted to DB | Batch phase: assign OH-HAN-SN-0001, correct member_site_ids to 4-digit, upsert to site_networks |
| 5 | HIGH | PAD-US — Sponsler Property / Cricket Frog Cove (156ac, GAP2, County Land) not in DB | Supplemental T4 discovery — Hancock County conservation land |
| 6 | HIGH | PAD-US — Rudolph-Savanna Preserve (52ac, GAP2, County Land) not in DB | Supplemental T4 discovery — county savanna preserve |
| 7 | MEDIUM | 25 trails have 0 trail_parents entries — partial upsert | Batch phase: add trail_parents for Van Buren trails → S-0001, Heritage Trail → S-0018, reservoir trails → respective reservoir sites |
| 8 | MEDIUM | PAD-US — 10 WPAs (6, 8, 9, 11, 20, 21, 41, 42, 46, 58) individually in PAD-US but not individually cataloged; all matching S-0010 | Supplemental T2 discovery — enumerate individual WPA records; ~550ac ODNR land |
| 9 | MEDIUM | PAD-US — District 2 Findlay Wildlife Area (6ac, GAP2, ODNR) not in DB | Supplemental T2 discovery |
| 10 | MEDIUM | Indian Green-Worden CA acreage: DB=27.3ac vs PAD-US Indian Green Preserve=81ac | Verify HPD parcel area; update if expansion parcels confirmed |
| 11 | LOW | 6 WA parking APs (AP-0005–0010) missing GPS | GPS acquisition pass for wildlife area parking lots |
| 12 | LOW | PAD-US — Anchor Park (5ac), Douglas Park (1ac), Civitan Park (2ac) not in DB | Supplemental T4/T6 discovery — small parks |
| 13 | LOW | Flag City Sports Complex SN member_site_ids in TSV use 3-digit format (e.g., OH-HAN-S-055) | Fix during upsert — pad to 4 digits |

---

## Actions Taken This Session

- Fixed all 19 OH-HAN-AP-000x parent_entity_id values from non-padded (OH-HAN-S-001/003/004/005/006/007/008/025/028/029/031/032/033/034/091) to zero-padded format. All 19 parents verified as existing sites. ✓
- Fixed OH-HAN-S-0098 counties from "Hancock, Ohio;Allen, Ohio" to "Allen;Hancock". ✓

---

## Pending Actions

**Batch upsert (critical — data in TSV, not in DB):**
- Upsert 35 trail_segment records from `hancock_ohio_2026_05_12_trail_segments.tsv` with proper segment_ids (OH-HAN-TS-0001+) and parent_trail_ids assigned
- Upsert Flag City Sports Complex site_network from TSV with OH-HAN-SN-0001 and corrected member_site_ids

**Supplemental discovery (batch):**
- T2: Sponsler Property/Cricket Frog Cove (156ac, GAP2) — Hancock County conservation land
- T2: Rudolph-Savanna Preserve (52ac, GAP2) — county-owned savanna
- T2: District 2 Findlay Wildlife Area (6ac, GAP2, ODNR)
- T2: Individual WPA records (WPAs 6, 8, 9, 11, 20, 21, 41, 42, 46, 58)
- T4/T6: Anchor Park (5ac), Douglas Park (1ac), Civitan Park (2ac)

**Data corrections (batch):**
- Add trail_parents for all 25 Hancock trails
- GPS acquisition for AP-0005–0010 (WA parking areas)
- Verify Indian Green-Worden Family CA acreage (27.3ac vs PAD-US 81ac)
- Resolve OLD MILL STREAM identity flag (driving byway vs trail)
- Resolve LOCAL-006 speculative entries

---

## Quality Review Outcome

**Status: FAIL — HIGH-severity partial upsert (trail_segments and site_network missing from DB); HIGH-severity county conservation land gaps from PAD-US (Cricket Frog Cove 156ac, Rudolph-Savanna Preserve 52ac). FK integrity is now clean after this session's 20 fixes (19 AP parents + 1 counties field). Core site and trail tables are complete and accurate; the missing trail_segment and site_network records need a targeted re-upsert from the existing TSVs.**

*Review completed 2026-06-08 by Claude. FK and counties fixes applied to DB during review.*
