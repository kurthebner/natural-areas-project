# Defiance County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline run:** defiance_oh_2026_04_19 (v5 schema)
**DB state at review:** post-remediation fixes applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 33 | 32 OH-DEF-S- + 1 OH-MC-S- (Maumee State Scenic River) |
| Trails | 9 | 5 OH-DEF-T- + 4 OH-MC-T- (multi-county) |
| Trail segments | 1 | OH-MC-TS-0002 Independence Leg (Defiance;Henry) |
| Trail networks | 0 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | — |
| Access points | 6 | OH-DEF-AP-0001 through 0006 |
| Held entities | 0 | — |

Run metadata: defiance_oh_2026_04_19: input=59, normalized=45, held=0.
Open flags from run: VERIFY_GOVERNANCE (DEF-S-0016, DEF-AP-0005), GOVERNANCE_UNCERTAIN (DEF-T-0007), MINIMAL_DATA (multiple T6 village sites), DEF-F-06 UNRESOLVED (Oxbow Lake western parcel).

**Note:** Access points use `county` column (singular) rather than `counties` — standard v5 AP schema. All 6 APs confirmed in DB via `county='Defiance'` query.

---

## GPS Audit

**Sites:** 1 site missing GPS: OH-MC-S-0028 (Maumee State Scenic River). Scenic river is a linear water body — GPS is `gps_unresolvable` by nature. **Acceptable.**

**Shared GPS:** OH-DEF-S-0001 (Independence Dam State Park, 591ac) and OH-DEF-S-0003 (Winchester's Camp No. 3 / Fort Starvation) share GPS (41.268, −84.311). S-0003 is a child site within the park (noted in site record: "GPS propagated from parent site"); no distinct entrance exists. **Acceptable** — flag for individual GPS at field verification.

**Access points:** All 6 APs have GPS coordinates. ✓

**Sites with null acres:** 21 of 33 sites have null acres — primarily T6 village parks where acreage was not available from source. Consistent with MINIMAL_DATA flags in run metadata. Non-blocking.

---

## Held Entities

None. ✓

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Defiance` on 2026-06-08.

- PAD-US records in bbox: 55
- Matched (score ≥ 80): 15
- Unmatched: 31
- Skipped (private/closed): 9

**Near-miss false misses (in DB, just below threshold):**

| PAD-US name | Score | DB record | Notes |
|---|---|---|---|
| Kingsbury Park (14ac) | 78 | OH-DEF-S-0008 Kingsbury Riverfront Park, Pool, and Pickleball Facilities | Same park, PAD-US uses abbreviated name |
| Latty Grove Park (5ac) | 77 | OH-DEF-S-0020 Veteran's Memorial Park at Latty's Grove | Same park, PAD-US uses abbreviated name |
| East End Park (29ac) | 77 | OH-DEF-S-0012 Eastside Park | Likely same park under different local names |
| Hicksville Recreation Park (67ac) | 75 | OH-DEF-S-0023 Hicksville Community Park | Different PAD-US name — **may be distinct entity** (67ac vs unknown; see below) |

**Wrong match — flag for correction:**
PAD-US "Lick Creek Preserve" (51ac, GAP4) matched to OH-DEF-S-0032 "Shallow Creek Hunting Preserve" (score 85 on "preserve" token). These are distinct entities: Shallow Creek is a private fee-based hunting preserve; Lick Creek Preserve is a separate 51ac parcel. Genuine discovery miss.

**Bbox false positives:**
- "Antwerp Community Park" (5ac) — Antwerp is in Paulding County; bbox clips eastern Paulding border
- "Cecil Community Park" (4ac) — Cecil is in Paulding County; wrong match to Hicksville Community Park (score 82 on "community park" tokens)

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Fish Creek Wildlife Area | 2 | 156 | ODNR | T2 | HIGH — ODNR wildlife area, restricted access |
| Forrest Woods Nature Preserve expansions (×4 parcels) | 2 | ~255 combined | NGO | T7 | HIGH — open-access expansion parcels of a NGO preserve complex |
| Fish Creek Ecosystem Fee (×2 parcels) | 1 | 23 + 101 = 124 | NGO | T7 | HIGH — GAP Status 1; highest protection; NGO conservation land |
| Goldie Newman Wildlife Area | 2 | 80 | City Land | T6/T7 | MEDIUM — municipal wildlife area; verify governance |
| Lick Creek Preserve | 4 | 51 | City Land | T6/T7 | MEDIUM — distinct from Shallow Creek (private hunting); identity needs verification |
| Recreation Park | 4 | 76 | City Land | T6 | MEDIUM — large city park (76ac) not in DB; name too generic to fuzzy-match |
| Hicksville Recreation Park | 4 | 67 | City Land | T6 | MEDIUM — may be distinct from Hicksville Community Park; verify |
| UAW Park | 4 | 37 | City Land | T6/T7 | LOW — UAW union park; public access to verify |
| Flatrock Creek Wildlife Area | 2 | 4 | ODNR | T2 | LOW — small ODNR parcel |
| Six Mile Wildlife Area | 2 | 4 | ODNR | T2 | LOW — small ODNR parcel |
| Old Fort Defiance Park | 4 | 1 | County Land | T4 | LOW — historic fort site, 1ac |

**Note on Forrest Woods Nature Preserve:** Base preserve record is listed as "Closed" in PAD-US and was correctly skipped. However, four expansion parcels (Harper-Forrest, Land Acquisition, Rooks-Harper, Shaffer Property) carry "Open Access" and scored 46 — low match because "nature preserve expansion" tokens don't match any site name. Forrest Woods Nature Preserve is not in the DB at all. The preserve complex (base + expansions) totals roughly 500+ acres and appears to be a T7 NGO conservation site in Defiance County.

**PAD-US result: PARTIAL FAIL — multiple genuine T2 and T7 discovery gaps confirmed.**

---

## Relationship Table Audit

**site_parent:** 
- OH-DEF-S-0003 (Winchester's Camp) → OH-DEF-S-0001 (Independence Dam SP): ✓ correct (also confirmed in site_parent table)
- OH-DEF-S-0010 (Splash Park) → OH-DEF-S-0009 (Bronson Park): ✓ correct in site_parent table

**access_point_parents:** All 6 APs verified with correct parent references (after fixes — see Actions Taken).

**trail_parents:**
- OH-DEF-T-0003 through T-0006 have parent sites. ✓
- OH-DEF-T-0007 (Hicksville Nature Trail): no parent — consistent with GOVERNANCE_UNCERTAIN flag; location outside village limits, parcel owner unconfirmed.
- OH-MC-T-0001, 0200, 0201, 0219: no parent sites — expected for multi-county trail corridors.

**trail_segments:**
- OH-MC-TS-0002 (Independence Leg) → OH-MC-T-0201 (Miami & Erie Canal Towpath Hiking Trail): ✓ after fix.

---

## Open Flags from Pipeline Run

| Flag | Entity | Status |
|---|---|---|
| VERIFY_GOVERNANCE | OH-DEF-S-0016 Pontiac Metro Park | Partially addressed — City of Defiance Parks & Rec confirmed via contact email (cfeeney@cityofdefiance.gov); ownership (county vs. city) still unresolved. Remain open. |
| VERIFY_GOVERNANCE | OH-DEF-AP-0005 Pontiac Metro Park Boat Launch | Inherits from parent site. Remain open. |
| GOVERNANCE_UNCERTAIN | OH-DEF-T-0007 Hicksville Nature Trail | Hicksville Trail Association governance not confirmed; no IRS registration found; parcel at 9425 Casebeer Miller Rd may be private. Remain open — field verification needed. |
| MINIMAL_DATA | Multiple T6 village parks | Expected condition for rural county. 21 sites have null acres. Non-blocking. |
| DEF-F-06 UNRESOLVED | Oxbow Lake western parcel | Oxbow Lake Wildlife Area (OH-DEF-S-0002) has a western parcel under a different management agreement. PAD-US shows two parcels (386ac + 102ac) both matching S-0002. Unresolved governance boundary. |

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | AP parent_entity_id references — 4 of 6 APs had non-padded IDs (e.g., OH-DEF-S-001 instead of OH-DEF-S-0001) | **Fixed 2026-06-08** — corrected all 4 broken references |
| 2 | ~~HIGH~~ FIXED | AP-0002/0003 (Bend Road Bridge, Five-Mile Creek) had null parent references | **Fixed 2026-06-08** — assigned OH-MC-T-0001 (Maumee River Water Trail) as Trail parent |
| 3 | ~~HIGH~~ FIXED | OH-MC-TS-0002 trail segment parent_trail_id = "OH-MC-T-002" (does not exist) | **Fixed 2026-06-08** — corrected to OH-MC-T-0201 (Miami & Erie Canal Towpath Hiking Trail) |
| 4 | ~~MEDIUM~~ FIXED | sites.parent_site_id for OH-DEF-S-0003 and OH-DEF-S-0010 — non-padded IDs ("DEF-S-001", "DEF-S-009") | **Fixed 2026-06-08** — corrected to OH-DEF-S-0001 and OH-DEF-S-0009 |
| 5 | HIGH | PAD-US — Fish Creek Wildlife Area (156ac, ODNR, GAP2) not in DB | Supplemental T2 discovery |
| 6 | HIGH | PAD-US — Forrest Woods Nature Preserve (NGO, T7) + expansion parcels (~255ac open, GAP2) not in DB | Supplemental T7 discovery — verify access and stage base + open expansions |
| 7 | HIGH | PAD-US — Fish Creek Ecosystem Fee (124ac, NGO, GAP1) not in DB | Supplemental T7 discovery — GAP1 land; priority |
| 8 | MEDIUM | PAD-US — Goldie Newman Wildlife Area (80ac, GAP2, municipal) not in DB | Supplemental T6/T7 discovery — verify governance |
| 9 | MEDIUM | PAD-US — Recreation Park (76ac, City Land) not in DB | Supplemental T6 discovery — City of Defiance recreation complex |
| 10 | MEDIUM | PAD-US — Lick Creek Preserve (51ac) — wrong match to Shallow Creek Hunting Preserve | Supplemental T6/T7 discovery — verify identity; distinct from Shallow Creek |
| 11 | MEDIUM | PAD-US — Hicksville Recreation Park (67ac) — may be distinct from Hicksville Community Park | Supplemental T6 discovery — verify vs. OH-DEF-S-0023 |
| 12 | LOW | PAD-US — Flatrock Creek WA (4ac), Six Mile WA (4ac), UAW Park (37ac), Old Fort Defiance Park (1ac) not in DB | Supplemental discovery (T2 for WAs; T6/T7 for UAW and Fort park) |
| 13 | LOW | 21 sites with null acres | Backfill from GIS or source documents during next Defiance pass |
| 14 | LOW | VERIFY_GOVERNANCE / GOVERNANCE_UNCERTAIN open flags (DEF-S-0016, DEF-T-0007) | Field verification or direct authority contact |

---

## Actions Taken This Session

- Fixed OH-DEF-AP-0001, 0004, 0005, 0006: corrected parent_entity_id from non-padded to zero-padded IDs.
- Fixed OH-DEF-AP-0002, 0003: assigned parent_entity_type='Trail', parent_entity_id='OH-MC-T-0001' (Maumee River Water Trail).
- Fixed OH-MC-TS-0002: corrected parent_trail_id from "OH-MC-T-002" (invalid) to "OH-MC-T-0201" (Miami & Erie Canal Towpath Hiking Trail).
- Fixed OH-DEF-S-0003: corrected parent_site_id from "DEF-S-001" to "OH-DEF-S-0001".
- Fixed OH-DEF-S-0010: corrected parent_site_id from "DEF-S-009" to "OH-DEF-S-0009".

---

## Pending Actions

**Supplemental discovery (batch):**
- T2: Fish Creek Wildlife Area (156ac, ODNR) — Defiance County
- T2: Flatrock Creek Wildlife Area (4ac, ODNR), Six Mile Wildlife Area (4ac, ODNR)
- T7: Forrest Woods Nature Preserve + open expansion parcels (~255ac, NGO)
- T7: Fish Creek Ecosystem Fee parcels (124ac total, GAP1, NGO)
- T6/T7: Goldie Newman Wildlife Area (80ac)
- T6: Recreation Park (76ac, City of Defiance)
- T6: Lick Creek Preserve (51ac) — verify distinct identity
- T6: Hicksville Recreation Park (67ac) — verify vs. OH-DEF-S-0023
- T6: UAW Park (37ac); Old Fort Defiance Park (1ac)
- Flag Antwerp Community Park for Paulding County T6 discovery

**Data corrections (batch):**
- Resolve Pontiac Metro Park ownership (DEF-S-0016) — city vs. county/state
- Resolve Hicksville Nature Trail parcel owner (DEF-T-0007) — field visit to 9425 Casebeer Miller Rd
- Resolve DEF-F-06 Oxbow Lake western parcel governance
- Backfill acres for 21 sites with null values

---

## Quality Review Outcome

**Status: FAIL — multiple HIGH-severity FK issues fixed this session; multiple HIGH-severity discovery gaps remain pending supplemental work.** FK integrity is now clean after this session's fixes. The PAD-US gate reveals significant gaps in T2 (ODNR wildlife areas) and T7 (Forrest Woods Nature Preserve, Fish Creek Ecosystem) that were not discovered in the original pipeline. Three GAP2 and two GAP1 entities are missing. Supplemental discovery is required before this county can be considered complete.

*Review completed 2026-06-08 by Claude. FK fixes applied to DB during review.*
