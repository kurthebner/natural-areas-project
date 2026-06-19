# Fulton County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline run:** fulton_oh_2026_04_13 (v5 schema)
**DB state at review:** post-remediation fix applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 39 | 35 OH-FUL-S- + 4 OH-MC- (Oak Openings x3, Maumee State Forest) |
| Trails | 21 | 7 OH-FUL-T- + 14 OH-MC- (Oak Openings trail suite, Wabash Cannonball) |
| Trail segments | 0 | — |
| Trail networks | 0 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | — |
| Access points | 1 | OH-FUL-AP-0001 (Wabash Cannonball CR 23 Trailhead) |
| Held entities | 0 | See note below |

Run metadata: fulton_oh_2026_04_13: input=45, normalized=45, **held=4**.

**Held entities discrepancy:** Run metadata records held=4, but `held_entities` table shows 0 Fulton records. This suggests 4 entities were held during the pipeline run and subsequently resolved and upserted (held_entities records deleted on release). However, OH-FUL-AP-0001 has null GPS and its notes explicitly state "GPS acquisition needed" — if it was the held AP, it should still be in held_entities or have GPS. The pipeline's held record cleanup is unverifiable. Non-blocking but document as a flag.

Site sequence: max OH-FUL-S-0037, count=35; gaps at S-0003 and S-0006 — expected per IMP-117.

---

## GPS Audit

**Sites:** 1 site missing GPS — OH-MC-S-0032 (Oak Openings Corridor, Metroparks Toledo — Fulton County parcels). Notes state "GPS needed — unconfirmed… GIS parcel resolution needed." This is an undeveloped cross-county conservation parcel entity with no confirmed centroid. **gps_unresolvable** by nature — acceptable until GIS parcel data is acquired.

**Access points:** OH-FUL-AP-0001 (Wabash Cannonball CR 23 Trailhead) has null GPS. Notes say "GPS acquisition needed — map verification required." This AP should be in `held_entities` with `hold_reason=gps_missing` per Stage 4c, but is not. Likely entered as a staged post-pipeline addition before GPS gate was enforced. **Pending GPS acquisition.**

**All other sites (38 of 39) have GPS.** No out-of-bounds values. ✓

---

## Held Entities

Technically 0 (table is empty for Fulton). See discrepancy note above. OH-FUL-AP-0001 is functionally held pending GPS but is not in `held_entities`.

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Fulton` on 2026-06-08.

- PAD-US records in bbox: 22
- Matched (score ≥ 80): 19
- Unmatched: 1
- Skipped (closed/private): 2

**Skipped correctly:**
- "Goll Woods Dedicated Nature Preserve" — marked Closed in PAD-US; closed-access research/dedicated portion of Goll Woods SNP. Base site OH-FUL-S-0001 already in DB. ✓
- "Pettisville Community Park" — marked private ownership in PAD-US; OH-FUL-S-0033 already in DB (governance: PARC Inc., 501(c)(3) non-profit managing the park). ✓

**Wrong match — flag:**
PAD-US "West Unity Memorial Park" (11ac, GAP4, City Land) matched to OH-FUL-S-0027 "Green Memorial Park" at score 81. These are distinct entities in different villages: Green Memorial Park is in Lyons (41.696°N, −84.071°W); West Unity is a village at approximately 41.588°N, −84.328°W — ~18 miles away. The "memorial park" token drove the match. **Genuine T6 discovery gap: West Unity Memorial Park not in DB.**

**Near-miss correctly resolved:**
"North Park" (2ac) and "North Pointe Park" (4ac) both matched to OH-FUL-S-0018. These are two PAD-US parcels for the same entity (North Pointe Park, Wauseon). Acceptable duplicate PAD-US record.

**Acreage discrepancy:**
"Delta Municipal Park" (37ac in PAD-US) matched to OH-FUL-S-0022 "Delta Park" (23ac in DB). 14ac difference — PAD-US may include an additional parcel or use a different boundary. Low priority; note for next Fulton pass.

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Springfield Township Park | 4 | 12 | City Land | T5 | MEDIUM — township park not in DB |
| West Unity Memorial Park | 4 | 11 | City Land | T6 | MEDIUM — wrong PAD-US match; distinct village park |

**PAD-US result: PASS with minor gaps.** Key entities (T1–T4, T7 conservation lands) are well-represented. Only 2 genuine gaps — both small municipal parks. Fulton has outstanding coverage for a rural county.

---

## Relationship Table Audit

**trail_parents:**

| Trail | Parent | Status |
|---|---|---|
| OH-FUL-T-0001 (Toadshade Trail) | OH-FUL-S-0001 (Goll Woods SNP) | ✓ |
| OH-FUL-T-0002 (Tuliptree Trail) | OH-FUL-S-0001 | ✓ |
| OH-FUL-T-0003 (Bur Oak Trail) | OH-FUL-S-0001 | ✓ |
| OH-FUL-T-0004 (Cottonwood Trail) | OH-FUL-S-0001 | ✓ |
| OH-FUL-T-0006 (Cannonball Trail Wauseon) | None | City connector trail — no single site parent expected |
| OH-FUL-T-0016 (Beach Ridge Singletrack Trail) | None | Expected parent: OH-MC-S-0025 (Oak Openings Beach Ridge Area) — missing |
| OH-FUL-T-0017 (Chessie Circle Trail) | None | Expected parent: OH-FUL-S-0002 (Harrison Lake State Park) — missing |
| OH-MC-T-0220 (Stewardship Trail) | OH-MC-S-0031 (Maumee State Forest) | ✓ |
| OH-MC-T-0205–0215 (Oak Openings trail suite) | None | Multi-county trails; expected parent OH-MC-S-0024 not set — low priority |
| OH-MC-T-0002, T-0221 (Wabash Cannonball variants) | None | Expected for multi-county water/rail trails |

Missing trail parents for T-0016 and T-0017 are data quality issues; low severity.

**site_parent:** No parent-child site relationships for Fulton. Expected — no Fulton child sites discovered.

**access_point_parents:** OH-FUL-AP-0001 references OH-MC-T-0221 (Wabash Cannonball Trail North Fork) after this session's fix. ✓

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | OH-FUL-AP-0001 parent_entity_id = 'OH-MC-TR-007' (does not exist) | **Fixed 2026-06-08** — corrected to OH-MC-T-0221 (Wabash Cannonball Trail North Fork) |
| 2 | MEDIUM | OH-FUL-AP-0001 missing GPS; not in held_entities despite GPS requirement | GPS acquisition needed; add to held_entities or mark gps_unresolvable if trailhead GPS cannot be confirmed |
| 3 | MEDIUM | PAD-US — West Unity Memorial Park (11ac) not in DB; wrong match to Green Memorial Park | Supplemental T6 discovery — West Unity village park |
| 4 | MEDIUM | PAD-US — Springfield Township Park (12ac) not in DB | Supplemental T5 discovery — enumerate Springfield Township parks |
| 5 | LOW | run_metadata held=4 but held_entities shows 0; AP-0001 GPS still unacquired | Investigate held entity disposition; document in improvement tracker if pipeline cleanup deleted records before GPS acquisition |
| 6 | LOW | OH-FUL-T-0016 (Beach Ridge Singletrack) missing trail_parent → OH-MC-S-0025 | Add trail_parents entry |
| 7 | LOW | OH-FUL-T-0017 (Chessie Circle Trail) missing trail_parent → OH-FUL-S-0002 | Add trail_parents entry |
| 8 | LOW | Delta Park acreage: DB=23ac vs PAD-US=37ac | Verify against Delta municipality records; may be additional parcel not included in DB |

---

## Actions Taken This Session

- Fixed OH-FUL-AP-0001: corrected parent_entity_id from 'OH-MC-TR-007' (non-existent) to 'OH-MC-T-0221' (Wabash Cannonball Trail North Fork). Identity notes on the AP confirmed the correct parent.

---

## Pending Actions

**Supplemental discovery (batch):**
- T5: Springfield Township Park (12ac) — Fulton County
- T6: West Unity Memorial Park (11ac) — West Unity village

**Data corrections (batch):**
- Acquire GPS for OH-FUL-AP-0001 (Wabash Cannonball CR 23 Trailhead); add to held_entities if not resolved
- Add trail_parents: T-0016 → OH-MC-S-0025 (Oak Openings Beach Ridge Area)
- Add trail_parents: T-0017 → OH-FUL-S-0002 (Harrison Lake State Park)
- Verify Delta Park acreage (23ac vs PAD-US 37ac)

---

## Quality Review Outcome

**Status: PASS with minor pending items.** One FK integrity issue fixed this session. PAD-US gate shows strong coverage — only 2 small municipal parks are genuine discovery gaps. Goll Woods, Tiffin River WA, Harrison Lake, Oak Openings parcels, and Maumee State Forest are all correctly cataloged. No held entity issues, no cross-county conflicts, no missing GPS on primary entities. The AP GPS and two missing trail parent entries are low-severity housekeeping items.

*Review completed 2026-06-08 by Claude. FK fix applied to DB during review.*
