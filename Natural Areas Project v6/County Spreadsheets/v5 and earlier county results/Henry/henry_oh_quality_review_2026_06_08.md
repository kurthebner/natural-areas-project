# Henry County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline run:** henry_oh_2026_04_20 (v5 schema)
**DB state at review:** post-remediation fixes applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 33 | 30 OH-HEN-S- + 3 OH-MC- (Maumee Scenic River, Mary Jane Thurston SP, Maumee State Forest) |
| Trails | 11 | 4 OH-HEN-T- + 7 OH-MC- (WCT, NCNST, Miami & Erie Canal, Tow Path, Stewardship, WCT North Fork, Maumee RWWT) |
| Trail segments | 6 | 3 OH-HEN-TS- + 3 OH-MC-TS- |
| Trail networks | 0 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | — |
| Access points | 6 | OH-HEN-AP-0001–0006 |
| Held entities | 0 | — |

Run metadata: henry_oh_2026_04_20: input=50, normalized=49, held=1. Note: the 1 held entity (HEN_S_019 Maumee Scenic River — linear feature) appears to have been resolved and upserted as OH-MC-S-0028; held_entities table is currently empty.

Site sequence: max OH-HEN-S-0031, count=30; gap at S-0019 (the held/merged Maumee Scenic River) — expected per IMP-117.

Trail sequence: OH-HEN-T-0001, 0003, 0004, 0007; gaps at 0002, 0005, 0006 — expected per IMP-117.

---

## Duplicate Site — Mary Jane Thurston State Park

**MEDIUM-HIGH:** Two records exist for the same park:
- OH-HEN-S-0018: "Mary Jane Thurston State Park", counties='Henry', 105ac, GPS 41.411925, −83.884997
- OH-MC-S-0030: "Mary Jane Thurston State Park", counties='Henry;Wood', 105ac, GPS 41.41028, −83.87778

MJTP straddles the Henry-Wood county line; OH-MC-S-0030 is the correct record. OH-HEN-S-0018 is a single-county stub that should be retired. OH-HEN-AP-0001 and AP-0002 (Boat Launch Ramp and Marina) currently reference OH-HEN-S-0018 (valid FK after this session's zero-padding fix), but in batch phase should be reparented to OH-MC-S-0030 before S-0018 is retired.

---

## GPS Audit

**Sites:** 1 site missing GPS — OH-MC-S-0028 (Maumee State Scenic River). Linear feature; GPS is `gps_unresolvable` by nature. Acceptable.

**All other 32 sites have GPS.** No out-of-Ohio values. ✓

**Access points:** All 6 APs have GPS. ✓

---

## Held Entities

None currently. 1 entity was held during pipeline run (Maumee Scenic River, linear feature) and resolved as OH-MC-S-0028. ✓

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Henry` on 2026-06-08.

- PAD-US records in Henry bbox: 45
- Matched (score ≥ 80): 20
- Unmatched: 20
- Skipped (private/excluded): 5

**Skipped correctly:** 2 private golf courses, private Compo Park, Tecumseh Park (private), Henry County Fairgrounds (excluded keyword — see Scope Note below). ✓

**Scope note — OH-HEN-S-0011 Henry County Fairgrounds:** PAD-US correctly excluded this with "fairground" keyword. The DB contains this record (category='Recreation Facility'). Fairgrounds are generally outside NAP scope; document for scope review in batch phase.

**Wrong match — Holgate Community Park → Hamler Community Park:**
PAD-US "Holgate Community Park" (7ac) scored 84 to OH-HEN-S-0009 "Hamler Community Park" due to dominant "Community Park" tokens. The correct match is OH-HEN-S-0016 "Holgate Village Park" — which IS in the DB. Not a discovery gap.

**Wrong match — Maumee SR → Maumee State Forest:**
PAD-US "Maumee SR" (51ac, GAP4) scored 80 to OH-MC-S-0031 "Maumee State Forest". "SR" abbreviates "Scenic River" — this parcel is likely a riparian corridor parcel under the Maumee State Scenic River designation (OH-MC-S-0028), not the Forest. Low impact — scenic river is in DB; this is a PAD-US naming artifact.

**Bbox false positives (Defiance County entities falling in Henry's bbox):**
Defiance City sits at the western edge of Henry County's bbox. The following PAD-US records are Defiance County entities, all confirmed in the Defiance DB:
- "Camp Lakota" (474ac, NGO) → OH-DEF-S-0030 "Camp Lakota / Camp Neil Armstrong" (Defiance)
- "Bronson Park" (23ac) → OH-DEF-S-0009 (Defiance City)
- "Kingsbury Park" (14ac) → OH-DEF-S-0008 Kingsbury Riverfront Park (Defiance City)
- "Latty Grove Park" (5ac) → OH-DEF-S-0020 (Defiance City)
- "Old Fort Defiance Park" (1ac) → Defiance City (noted in Defiance review)
- "Independence Dam State Park" (188ac, ODNR) → OH-DEF-S-0001 (Defiance County)
- "Pontiac Park" (8ac) → likely Defiance City (OH-DEF-S-0016 Pontiac Metro Park); name variant

**Near-miss false misses (in DB, below threshold):**
- "East River Downs" (15ac, score 61) → OH-HEN-S-0005 "East Riverdowns Park" — same park, PAD-US name variant

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Camp Libbey | 4 | 321 | NGO | T7 | HIGH — Girl Scouts camp; 321ac NGO property not in DB |
| Woodland Park | 4 | 43 | City Land | T6 | HIGH — Napoleon city park, 43ac not in DB |
| Diehl Park | 4 | 40 | City Land | T6 | HIGH — Napoleon city park, 40ac not in DB |
| Riverside Park | 4 | 32 | City Land | T6 | HIGH — Napoleon city park, 32ac not in DB |
| VFW 3360 Park | 4 | 24 | City Land | T7 | MEDIUM — VFW post park; public access expected |
| Cherry Street Park | 4 | 11 | City Land | T6 | MEDIUM — Napoleon area city park |
| Wildlife Production Area 28 | 2 | 39 | ODNR | T2 | MEDIUM — ODNR WPA, GAP2 |
| Wildlife Production Area 29 | 2 | 40 | ODNR | T2 | MEDIUM — ODNR WPA, GAP2 |
| Dry Creek Wildlife Area | 2 | 2 | ODNR | T2 | LOW — small ODNR parcel, GAP2 |
| Second Ward Park | 4 | 1 | City Land | T6 | LOW |
| South Street Park | 4 | 1 | City Land | T6 | LOW |
| Legion Field | 4 | 2 | City Land | T6 | LOW |

**Note on Napoleon T6 gaps:** Napoleon is the Henry County seat (~8,700 population) and its park system appears substantially undercatalogued. Riverside Park (32ac), Woodland Park (43ac), and Diehl Park (40ac) are substantial parks that were not discovered in the original pipeline run. Combined with Cherry Street Park, VFW 3360, and smaller parks, this represents a significant T6 supplemental discovery need.

**PAD-US result: PARTIAL FAIL — Camp Libbey (321ac NGO) and multiple Napoleon city parks (including 43ac, 40ac, 32ac) are genuine discovery gaps.**

---

## Relationship Table Audit

**trail_parents:** Only 1 of 11 Henry trails has trail_parents — OH-MC-T-0220 (Stewardship Trail → OH-MC-S-0031 Maumee State Forest). The 4 OH-HEN-T trails (Blue, Orange, Storybook, Yellow) should be parented to MJTP; none have trail_parents entries. Multi-county MC trails (WCT, NCNST, Maumee RWWT) appropriately have no single site parent.

**trail_segments — parent_trail_id errors (fixed this session):**

| Segment | Old parent | New parent | Notes |
|---|---|---|---|
| OH-HEN-TS-0001 Damascus Leg | OH-MC-T-002 | OH-MC-T-0002 | Non-padded → padded |
| OH-HEN-TS-0003 Napoleon Leg | OH-MC-T-002 | OH-MC-T-0002 | Non-padded → padded |
| OH-HEN-TS-0004 Renegade Leg | OH-MC-T-002 | OH-MC-T-0002 | Non-padded → padded |
| OH-MC-TS-0006 WideWater Section | OH-MC-T-002 | OH-MC-T-0002 | Non-padded → padded |
| OH-MC-TS-0005 WCT South Fork | HEN_T_006 | OH-MC-T-0002 | Invalid local ID → Wabash Cannonball Trail |

**access_point_parents — fixed this session:**

| AP | Old parent | New parent |
|---|---|---|
| OH-HEN-AP-0001 (MJTP Boat Launch) | OH-HEN-S-018 | OH-HEN-S-0018 |
| OH-HEN-AP-0002 (MJTP Marina) | OH-HEN-S-018 | OH-HEN-S-0018 |
| OH-HEN-AP-0003 (Oberhaus Dock) | OH-HEN-S-025 | OH-HEN-S-0025 |
| OH-HEN-AP-0004 (Ritter Park Launch) | OH-HEN-S-027 | OH-HEN-S-0027 |

AP-0005 and AP-0006 reference OH-MC-T-0002 (Trail type) — verified correct. ✓

**site_parent:** No Henry parent-child site relationships — expected.

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | 4 APs with non-padded parent_entity_ids (OH-HEN-S-018/025/027) | **Fixed 2026-06-08** — all 4 corrected to zero-padded; all parents verified as existing |
| 2 | ~~HIGH~~ FIXED | 5 trail_segments with invalid parent_trail_ids (OH-MC-T-002 ×4; HEN_T_006 ×1) | **Fixed 2026-06-08** — all corrected to OH-MC-T-0002 (Wabash Cannonball Trail) |
| 3 | MEDIUM-HIGH | Duplicate Mary Jane Thurston SP: OH-HEN-S-0018 (Henry only) vs OH-MC-S-0030 (Henry;Wood) | Batch: retire OH-HEN-S-0018; reparent AP-0001/0002 from S-0018 to OH-MC-S-0030 |
| 4 | HIGH | PAD-US — Camp Libbey (321ac, NGO) not in DB | Supplemental T7 discovery — Girl Scouts camp |
| 5 | HIGH | PAD-US — Woodland Park (43ac), Diehl Park (40ac), Riverside Park (32ac) — Napoleon city parks not in DB | Supplemental T6 Napoleon discovery pass |
| 6 | MEDIUM | PAD-US — VFW 3360 Park (24ac), Cherry Street Park (11ac) not in DB | Supplemental T6/T7 discovery |
| 7 | MEDIUM | PAD-US — Wildlife Production Areas 28 (39ac) and 29 (40ac), Dry Creek WA (2ac) — ODNR sites not in DB | Supplemental T2 discovery |
| 8 | MEDIUM | 4 OH-HEN-T trails (Blue, Orange, Storybook, Yellow) have no trail_parents → expected parent OH-HEN-S-0018 / OH-MC-S-0030 | Batch: add trail_parents; use MC-S-0030 after S-0018 is retired |
| 9 | LOW | OH-HEN-S-0011 Henry County Fairgrounds in DB; fairgrounds are generally excluded from NAP scope | Batch: scope review; if out of scope, retire record |
| 10 | LOW | PAD-US — Second Ward Park (1ac), South Street Park (1ac), Legion Field (2ac) not in DB | Supplemental T6 Napoleon parks |

---

## Actions Taken This Session

- Fixed OH-HEN-AP-0001, 0002, 0003, 0004: corrected parent_entity_id from non-padded to zero-padded IDs.
- Fixed OH-HEN-TS-0001, 0003, 0004 and OH-MC-TS-0006: corrected parent_trail_id from 'OH-MC-T-002' (non-padded, non-existent) to 'OH-MC-T-0002' (Wabash Cannonball Trail).
- Fixed OH-MC-TS-0005: corrected parent_trail_id from 'HEN_T_006' (invalid local ID) to 'OH-MC-T-0002' (Wabash Cannonball Trail). The South Fork segment is part of the WCT system.

---

## Pending Actions

**Data corrections (batch):**
- Retire OH-HEN-S-0018 (duplicate Mary Jane Thurston SP — Henry-only record); reparent AP-0001/0002 to OH-MC-S-0030 first
- Add trail_parents: OH-HEN-T-0001/0003/0004/0007 → OH-MC-S-0030 (Mary Jane Thurston SP, the MC record)
- Scope review: OH-HEN-S-0011 (Henry County Fairgrounds) — retire if out of scope

**Supplemental discovery (batch):**
- T7: Camp Libbey (321ac, NGO — Girl Scouts of Western Ohio)
- T6: Napoleon city parks supplemental pass — Riverside Park (32ac), Woodland Park (43ac), Diehl Park (40ac), Cherry Street Park (11ac), VFW 3360 Park (24ac), Second Ward Park, South Street Park, Legion Field
- T2: Wildlife Production Area 28 (39ac), Wildlife Production Area 29 (40ac), Dry Creek Wildlife Area (2ac)

---

## Quality Review Outcome

**Status: FAIL — 9 FK integrity issues fixed this session (4 AP parents, 5 trail segment parents); duplicate site record for Mary Jane Thurston SP; significant T6 discovery gaps in Napoleon (Riverside Park 32ac, Woodland Park 43ac, Diehl Park 40ac) and Camp Libbey (321ac NGO) not discovered in original pipeline.** FK integrity is clean after this session's fixes. The Napoleon city park gap is the most operationally significant issue — the county seat's parks system was substantially undercatalogued.

*Review completed 2026-06-08 by Claude. FK fixes applied to DB during review.*
