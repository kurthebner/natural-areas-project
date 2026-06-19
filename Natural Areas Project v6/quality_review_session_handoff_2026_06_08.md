# NAP v6 Quality Review — Session Handoff
**Date:** 2026-06-08
**Status:** Quality review phase complete for Van Wert, Williams, Wood, Hardin. Batch resolution phase not yet started.

---

## Session Context Prompt (paste at start of next session)

> **Continuing Natural Areas Project v6 quality review batch resolution.**
>
> We completed quality reviews for four counties (Van Wert, Williams, Wood, Hardin) across two sessions on 2026-06-08. Each county has a review document in its County_Spreadsheets folder. The review documents contain the full issues list and batch actions. Now we need to execute the batch actions — DB fixes, GPS acquisition, trail_parents, supplemental discovery staging, and duplicate cleanup.
>
> **IMPORTANT POLICIES established this session:**
> - Village/small municipal parks are MEDIUM priority (not low)
> - PAD-US queries use the na_padus_query.py script with GDB spatial queries (not CSV name-matching)
> - IMP-027 has been logged: replace bbox filter in na_padus_query.py with actual county polygon intersection (TIGER/Line 2024) — not yet implemented
> - Bbox bleed false positives: always coordinate-check PAD-US entities that seem to belong to an adjacent county before treating as a gap
>
> **Run orientation protocol first (CLAUDE.md §1), then read this file.**

---

## What Was Done This Session

### DB Fixes Applied (already in DB — do not re-apply)

| County | Fix |
|---|---|
| Van Wert | AP-0001 parent_entity_id OH-VNW-S-007 → OH-VNW-S-0007 |
| Wood | UPDATE sites SET counties='Fulton;Henry;Lucas;Wood' WHERE site_id='OH-MC-S-0031' |
| Hardin | AP-0001/0004/0005/0006/0007/0008 parent_entity_id: 3-digit → 4-digit |
| Hardin | TT-0001/0002/0003/0004 site_parent_id: 3-digit → 4-digit |
| Hardin | SN-0001 member_site_ids: all 6 members 3-digit → 4-digit |

### IMP Items Logged

- **IMP-027** (Section 1 — Open): Replace bbox filter in na_padus_query.py with county polygon intersection using TIGER/Line 2024. Same source as na_township_lookup.py; use "intersects" operator. Eliminates false positives from adjacent counties while correctly surfacing genuine cross-county entities.

### Review Documents Created

| County | File | Status |
|---|---|---|
| Van Wert | `County_Spreadsheets/v5 and earlier county results/Van Wert/van_wert_oh_quality_review_2026_06_08.md` | PARTIAL FAIL |
| Williams | `County_Spreadsheets/v5 and earlier county results/Williams/williams_oh_quality_review_2026_06_08.md` | PARTIAL FAIL |
| Wood | `County_Spreadsheets/v5 and earlier county results/Wood/wood_oh_quality_review_2026_06_08.md` | PARTIAL FAIL |
| Hardin | `County_Spreadsheets/Hardin/hardin_oh_quality_review_2026_06_08.md` | PARTIAL FAIL |

---

## Batch Actions — By County

Read the individual review documents for full context. This is a consolidated action list.

### Van Wert

- [ ] DB: `INSERT INTO trail_parents VALUES ('OH-VNW-T-0003', 'OH-VNW-S-0016')` (Warrior Trail → Ohio City Fireman's Park)
- [ ] GPS: Acquire precision GPS for OH-VNW-S-0001 (Whitey Case WPA — currently 40.8, -84.79, single decimal)
- [ ] GPS: Acquire precision GPS for OH-VNW-S-0019 (Van-Del Drive-In — 3 decimal places)
- [ ] GPS: Verify source confidence for OH-VNW-S-0008 (Van Wert Reservoir 1)
- [ ] Supplemental T6 discovery: Wesley Park (3ac), Bresler Park (8ac), Grover Hill Community Park (18ac)
- [ ] Verify: Little Auglaize Wildlife Reserve against ODNR — T2 supplemental if not in DB
- [ ] Verify: Rotary Park actual acreage (PAD-US shows 172ac — implausible for a dog park; likely PAD-US aggregation error)
- [ ] Resolve open run flags: STORYBOOK_TRAIL_CONFIRM_NEEDED (S-0003), LENGTH_VERIFY_NEEDED (T-0001), DETAILS_INCOMPLETE (S-0016), FIELD_VERIFY_NEEDED (S-0018)
- [ ] Ohio City T6 supplemental: confirm Warrior Trail / Ohio City Greenway relationship to S-0016

### Williams

- [ ] GPS: Acquire precision GPS for 42 of 46 sites (S-0002/0003/0006/0008–0046 — all have ≤3 decimal place coordinates)
- [ ] DB: Add trail_parent OH-WIL-T-0002 → confirm correct Bryan riverside park (S-0026 Miller Park, S-0027 Gerhart Park, or S-0028 Downtown Park)
- [ ] DB: Add trail_parents for OH-MC-T-0001, T-0002, T-0219, T-0221 → identify Williams County site parents for each
- [ ] Supplemental discovery: Williams County Conservation League area (69ac) — verify T3 vs T7 tier based on org structure
- [ ] Supplemental T6: Montpelier Memorial Park (27ac), Superior Athletic Complex (25ac, Bryan area)
- [ ] Verify acreages: George Bible Park (DB 95.5ac vs PAD-US 60ac), Goldie Newman WA (DB 50ac vs PAD-US 80ac), Opdycke Park (DB 50ac vs PAD-US 64ac)

### Wood

- [ ] DB: `DELETE FROM sites WHERE site_id='OH-WOD-S-0015'` (Van Tassel WA — superseded by OH-MC-S-0029); check trail_parents and APs first
- [ ] DB: `DELETE FROM sites WHERE site_id='OH-LUC-S-0045'` (Maumee State Forest — superseded by OH-MC-S-0031); check trail_parents and APs first
- [ ] DB: Remove OH-WOD-SI-0073 "Mishe Monoto Preserve" from held_entities; note for Pickaway/Hocking T7 supplemental
- [ ] DB: Add trail_parents: T-0002 → S-0077 (Pat & Clint Mauk's Prairie Trail); T-0038 → MC-S-0027 (Providence); T-0039 → MC-S-0027; identify T-0001 parent (Slippery Elm Trail — Wood County Park District)
- [ ] GPS: Precision GPS for 9 low-precision sites (S-0002/0010/0014/0016/0022/0037/0038/0041/0074); resolve S-0016 and S-0037 shared coordinate (41.368, -83.6247)
- [ ] Verify: 4 unconfirmed_baseline_seeds in held_entities (S-0078 Devils Hole Prairie, S-0079 Hulls Prairie, S-0080 Tontogany Prairie, S-0081 North Baltimore Reservoir) against ODNR; release or delete
- [ ] Supplemental T3: Nona Park Stone Quarry and Ball Fields (80ac, Metroparks of Toledo Area)
- [ ] Supplemental T6: Bowling Green Training & Community Center (81ac — verify park vs rec facility), Whitehouse Village Park (14ac), West Poe Recreation Area (12ac), Conneaut/Haskins Park (7ac), Conrad Park (7ac), Stitt Park (5ac), Waterworks Park (6ac), Memorial Field (6ac), Pray Park (1ac)
- [ ] Investigate: Wood County Historical Center (54ac) — same as Wood County Museum (S-0037, 51ac) or distinct entity?
- [ ] Investigate: Providence/Bend View/Farnsworth PAD-US 451ac record — does Wood County have land beyond Providence Metropark (MC-S-0027)?
- [ ] DB: Populate NULL acreages for Wood County WA entities (S-0003–S-0012) and matched parks from PAD-US values
- [ ] Document: T-0038/0039 sequence gap anomaly (v5.2 pipeline artifact) in Wood County session log

### Hardin

- [ ] GPS: GNIS acquisition for 34 cemetery sites via `utilities/na_gnis_query.py`; populate gps_lat/gps_lon; route unresolvable to held_entities with hold_reason=gps_missing
- [ ] GPS: Acquire GPS for 11 non-cemetery GPS-missing sites (parks, rec facilities, memorials, historic sites); route unresolvable to held_entities
- [ ] GPS: Precision GPS for S-0004 (Veterans Memorial Park), S-0005 (Boy Scout Lake), S-0045 (Memorial Park Golf Club) — all three currently share centroid coordinate 40.647, -83.6095
- [ ] Supplemental T2: WPA 32 (47ac), WPA 43 (40ac) — confirm Hardin County before cataloging
- [ ] Supplemental T4/TT: Marion Tallgrass Trail corridor (30ac rail trail) — likely Trailthing entity
- [ ] Supplemental T6: ONU campus site Ada OH (needed for TT-0005 site_parent); Ball Park (6ac); Glendale Skate Park (1ac); confirm Roundhead Community Park identity (S-0029)
- [ ] Review: 24 unconfirmed_baseline_seed held entities (S-0112–0136) against v6 site qualification rules; release or delete
- [ ] DB: Populate NULL acreages from PAD-US: Saulisberry Park (169ac), Gormley Park (16ac), Dunkirk Community Park (6ac), C.E. Wharton Memorial Park (19ac)
- [ ] Flag: Hardin upsert script for IMP-026 remediation (GPS gate bypassed; 45 sites upserted with NULL GPS directly to sites table)
- [ ] NOTE for Wyandot County run: Killdeer Plains Wildlife Area (8,581ac, GAP2, ODNR) — confirmed bbox false positive; centroid 40.709°N, -83.321°W; entirely in Wyandot County (Crane Township); catalog as T2 ODNR entity in Wyandot run

---

## Previously Accumulated Batch Actions (from prior sessions)

These were identified before this session and are not yet resolved:

### Paulding County
- AP-0001 reparent to MC-T-0216
- GPS acquisition for 11 sites
- Trail_parents for Paulding trails
- Forrest Woods T7 discovery
- Village parks T6 supplemental

### Putnam County
- GPS acquisition for WPA entities
- Trail_parents for Putnam trails
- Ottawa city parks T6 supplemental

### Sandusky County
- Trail_parents for Sandusky trails
- WPA individual catalog entries
- Green Springs State Forest, Little Portage WA, Knobbys Prairie — verify/supplement
- Municipal parks T6 supplemental

### Scioto County
- MC-T-0006 trail_parent
- Glade Wetland T7 discovery
- Arc Biodiversity preserve — verify/supplement

### Seneca County
- Delete 5 Franklin County cemeteries from held_entities (wrong county)
- Rock Creek Trail trail_parent
- WPA entries review
- Tiffin and Fostoria city parks T6 supplemental

---

## Key Technical Notes

**3-digit FK padding bug:** Systematic across all counties run on pre-v6 pipeline. Every county reviewed has had APs (and some TTs, SNs) with 3-digit non-padded parent_entity_id values. Check for this in any county not yet reviewed.

**GPS gate bypass (IMP-026):** Hardin County (v6 pipeline) upserted 45 sites with NULL GPS directly to sites table, bypassing Stage 4c. The gps_unresolvable flag was in the discovery YAML only — no column exists in DB schema. Remediation: run GNIS acquisition, then route remaining nulls to held_entities.

**Bbox false positives:** Adjacent-county entities appear in rectangular bbox queries. Confirmed false positives this session: Goll Woods + Harrison Lake SP (Fulton, appeared in Williams query), Killdeer Plains WA (Wyandot, appeared in Hardin query). IMP-027 will fix this systematically.

**County codes:** VNW=Van Wert, WIL=Williams (NOT WMS), WOD=Wood, HAR=Hardin. Check DB with `SELECT DISTINCT substr(site_id,1,6) FROM sites` if unsure of a county's code.

**DB path:** `NASqlite/natural_areas_v6.db` at v6 project root. Shell path: `/sessions/.../mnt/Natural Areas Project v6/NASqlite/natural_areas_v6.db`

**na_padus_query.py:** Located in `utilities/`. Uses GDB spatial queries against `PADUS4_0_StateOH.gdb` (note underscore before "State" in filename). Layer: `PADUS4_0Fee_State_OH`. Projection: ESRI:102039. Fuzzy match threshold ≥80 (token_set_ratio).
