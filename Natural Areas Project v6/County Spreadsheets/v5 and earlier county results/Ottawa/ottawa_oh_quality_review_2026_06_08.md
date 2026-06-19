# Ottawa County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline run:** ottawa_ohio_2026_05_18 (v6 schema)
**DB state at review:** post-remediation fixes applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 135 | 133 OH-OTT-S- + 2 OH-MC- (Magee Marsh WA, Ottawa NWR Complex) |
| Trails | 61 | 57 OH-OTT-T- + 4 OH-MC- (Metzger Marsh Trail, North Coast Inland Trail, Magee Marsh Boardwalk, Portage River Water Trail) |
| Trail segments | 0 | — |
| Trail networks | 0 | — |
| Trailthings | 0 | — (v6 pipeline; entities captured as legacy trail types from v5 schema) |
| Site networks | 2 | OH-OTT-SN-0002 (Park District of Ottawa County), OH-MC-SN-0002 (Ottawa NWR Complex) |
| Access points | 9 | OH-OTT-AP-0001–0009 |
| Held entities | 0 | — |

Run metadata: ottawa_ohio_2026_05_18: input=198, normalized=199, held=0. Run notes record "134 sites, 55 trails, 8 APs, 2 site networks" — minor discrepancy vs DB counts (+1 site, +2 trails, +1 AP). All entities share the same 2026-05-20 created_at timestamp; no post-pipeline additions detected. Discrepancy is a run notes artifact, not a missing-entity issue.

Site sequence: max OH-OTT-S-0133, count=133; gaps present (e.g., S-0124 used for Lake Erie Islands Water Trail in run; S-0125 gap) — consistent with IMP-117.

Trail sequence: OH-OTT-T-0072 through 0130 with gaps at 0084 and 0125 — expected per IMP-117.

---

## GPS Audit

**Sites:** 0 sites missing GPS. All 135 sites have coordinates. ✓

**Access points:** No AP GPS audit issues noted (APs with null GPS would be trailheads at parent-site location). ✓

---

## Held Entities

None. ✓

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Ottawa` on 2026-06-08.

- PAD-US records in bbox: 129
- Matched (score ≥ 80): 32
- Unmatched: 47
- Skipped (private/closed/excluded): 50

**Skipped correctly:** 44 private hunting/shooting clubs and golf courses (Ottawa County's Lake Erie shoreline has heavy private ownership); Nehls Memorial Preserve (closed/dedicated); Ladd-Carr (closed/dedicated); Ottawa County Fairgrounds (excluded keyword). ✓

**Confirmed bbox false positives (entities correctly in DB under another county):**

| PAD-US name | DB record | County |
|---|---|---|
| Pearson Metropark (613ac) | OH-LUC-S-0026 | Lucas ✓ |
| Maumee Bay State Park (1377ac) | OH-LUC-S-0003 | Lucas ✓ |
| Mallard Club Wildlife Area (386ac) | OH-LUC-S-0006 | Lucas ✓ |
| Oregon Recreation Complex (55ac) | — | Lucas (Oregon is Lucas County) |
| Pickerel Creek Wildlife Area (3148ac) | OH-SAN-S-0002 | Sandusky ✓ |
| Aldrich Pond Wildlife Area (40ac) | OH-SAN-S-0007 | Sandusky ✓ |
| White Star Park / White Star Addition III | OH-SAN-S-0023 | Sandusky ✓ |
| Blue Heron Reserve (158ac) | OH-SAN-S-0009 | Sandusky ✓ |
| Castalia Quarry Reserve (182ac) | — | Erie County (not yet run) |
| Cedar Point NWR (2593ac) | OH-LUC-S-0001 | Lucas ✓ (bbox overlap) |
| West Sister Island NWR (75ac) | OH-LUC-S-0002 | Lucas ✓ (bbox overlap) |

**Notable false match in MATCHED list:**
- "Metzger Marsh Wildlife Area" (570ac, GAP2) scored 88 to OH-MC-S-0010 "Magee Marsh Wildlife Area" — different entities. Metzger Marsh WA is in DB as OH-LUC-S-0007 (Lucas). Not a gap; false match on "marsh wildlife area" tokens.
- "Pickerel Creek Wildlife Area" scored 81 to OH-OTT-S-0013 "Toussaint Creek Wildlife Area" — different entities, different counties. Both correctly in DB. False match on "wildlife area" tokens.
- "Cedar Creeks Preserve" (39ac) scored 80 to OH-OTT-S-0042 "Cedar Meadow Preserve" — likely different entities. Cedar Creeks Preserve is an Erie County Parks property near Castalia; it is appearing in Ottawa bbox. Will be discovered when Erie is run. Not an Ottawa gap.

**Items needing investigation:**
- "Willow Point Wildlife Area" (391ac + 42ac, GAP2, ODNR) scored 86 to OH-OTT-S-0016 "Honey Point Wildlife Area." Willow Point WA and Honey Point WA may be distinct ODNR properties. If they are, ~433ac of ODNR land is missing. Verify against ODNR Division of Wildlife inventory.
- "Howard Farms Land Acquisition" (987ac, GAP2, County Land) — if this is an expansion parcel adjacent to OH-MC-S-0021 Howard Marsh Metropark (already in DB), it may need to be associated with or annexed to that record. If it is a distinct county-owned parcel, it is a HIGH-priority standalone gap.

**North Coast Inland Trail** (124ac, County Land) — trail corridor parcel already in DB as OH-MC-T-0110. Not a discovery gap.

**Oak Harbor Station Interurban Overlook and Boat Launch** (0ac) — already in DB as OH-OTT-AP-0007 (access point). Correctly captured as AP rather than site.

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Resthaven Wildlife Area (×2 parcels) | 2 | 2216 | ODNR | T2 | HIGH — major ODNR wildlife area near Oak Harbor; not in DB at all |
| Howard Farms Land Acquisition | 2 | 987 | County Land | T3/T4 | HIGH — large county conservation acquisition; may be Howard Marsh Metropark expansion (verify) |
| Bayview West Marsh | 2 | 221 | Unknown | T7 | MEDIUM-HIGH — large GAP2 wetland; owner unknown; verify access |
| Southwestern Lake Erie Marshes And Islands | 1 | 153 | NGO | T7 | MEDIUM-HIGH — GAP1 status; highest conservation level; NGO-held |
| Willow Point Wildlife Area (if distinct from Honey Point WA) | 2 | 433 | ODNR | T2 | MEDIUM-HIGH — if distinct from OH-OTT-S-0016; needs identity verification |
| Decoy Marsh Acquisition | 2 | 69 | County Land | T4 | MEDIUM — county conservation acquisition, GAP2 |
| Wildlife Production Area 30 | 2 | 56 | ODNR | T2 | MEDIUM — individual ODNR WPA |
| Wildlife Production Area (unnamed) | 2 | 64 | ODNR | T2 | MEDIUM — individual ODNR WPA |
| Wildlife Production Area 59 | 2 | 48 | ODNR | T2 | MEDIUM — individual ODNR WPA |
| Wildlife Production Area 63 | 2 | 40 | ODNR | T2 | MEDIUM — individual ODNR WPA |
| Wildlife Production Area 65 | 2 | 31 | ODNR | T2 | MEDIUM — individual ODNR WPA |
| Genoa Recreation Complex | 4 | 39 | City Land | T6 | MEDIUM — Genoa is Ottawa County; 39ac municipal rec complex |
| Darr-Root Fishing Access | 4 | 34 | ODNR | T2 | LOW — distinct from OH-OTT-S-0116 (Dr. L.J. Darr Memorial Wetlands); ODNR fishing access |
| Port Clinton Waterfront | 4 | 15 | ODNR | T2/T6 | LOW — Port Clinton is Ottawa County seat; waterfront parcel |
| Portage River Fishing Access | 4 | 10 | ODNR | T2 | LOW — ODNR fishing access parcel |
| Millers Blue Hole Wildlife Area | 2 | 13 | ODNR | T2 | LOW — small ODNR parcel, GAP2 |
| Alumni Park | 4 | 12 | City Land | T6 | LOW — small municipal park |
| Birchard Park | 4 | 12 | City Land | T6 | LOW — small municipal park |
| Firemans Park | 4 | 5 | City Land | T6 | LOW — small municipal park |

**PAD-US result: FAIL — Resthaven Wildlife Area (2216ac, ODNR, GAP2) is a HIGH-severity T2 discovery miss — the largest single gap of any county reviewed so far. Howard Farms Land Acquisition (987ac, GAP2) and Bayview West Marsh (221ac, GAP2) are additional large gaps.**

---

## Relationship Table Audit

**trail_parents:** 47 of 61 Ottawa-area trails have trail_parents entries. Well-populated relative to prior counties.

**Trails without trail_parents (10):**

| Trail | Notes |
|---|---|
| OH-OTT-T-0072 Howard Marsh Sandpiper Trail | Expected parent: OH-MC-S-0021 Howard Marsh Metropark (Lucas;Ottawa) — missing |
| OH-OTT-T-0073 Howard Marsh Mallard Trail | Same — missing |
| OH-OTT-T-0074 Howard Marsh Madewell Trail | Same — missing |
| OH-OTT-T-0075 Howard Marsh Egret Trail | Same — missing |
| OH-OTT-T-0076 Howard Marsh Sora Trail | Same — missing |
| OH-OTT-T-0124 Lake Erie Islands Water Trail | Water/island trail; no single site parent expected ✓ |
| OH-OTT-T-0126 Catawba Islander Trail | Expected parent: OH-OTT-S-0012 Catawba Island State Park; missing |
| OH-OTT-T-0127 Cedar Meadow Preserve Trail | Expected parent: OH-OTT-S-0042 Cedar Meadow Preserve; missing |
| OH-OTT-T-0128 Meadowbrook Marsh Trail | Expected parent: OH-OTT-S-0046 Meadowbrook Marsh; missing |
| OH-OTT-T-0129 Veterans Memorial Park Walking Trail | Expected parent: OH-OTT-S-0079 Veterans Memorial Park; missing |

**site_parent:** No Ottawa parent-child site relationships — consistent with pipeline approach. Acceptable (NWR sub-units are separate sites, not child sites).

**access_point_parents:** All 9 APs now reference valid entities after this session's fixes. ✓ One AP (OH-OTT-AP-0006) remains with null parent — see findings table.

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | AP-0001, AP-0002: parent_entity_id = 'OH-OTT-S-001' (non-padded, non-existent) | **Fixed 2026-06-08** → OH-OTT-S-0001 (Ottawa NWR) |
| 2 | ~~HIGH~~ FIXED | AP-0004: parent_entity_id = 'OH-OTT-S-006' (non-padded, non-existent) | **Fixed 2026-06-08** → OH-OTT-S-0006 (East Harbor SP) |
| 3 | ~~HIGH~~ FIXED | AP-0005, AP-0007: parent_entity_id = 'OH-MC-TR-002' (non-existent — trail network ID referenced but entity is in trails table) | **Fixed 2026-06-08** → OH-MC-T-0217 (Portage River Water Trail) |
| 4 | ~~HIGH~~ FIXED | AP-0008: parent_entity_id = 'OH-OTT-T-124' (non-padded, non-existent) | **Fixed 2026-06-08** → OH-OTT-T-0124 (Lake Erie Islands Water Trail) |
| 5 | ~~MEDIUM~~ FIXED | AP-0009: parent_entity_id = 'OH-OTT-S-097' (non-padded, non-existent) | **Fixed 2026-06-08** → OH-OTT-S-0097 (Nehls Memorial Preserve) |
| 6 | MEDIUM | AP-0006 "West Harbor Boat Launch" — no parent entity (both parent_entity_type and parent_entity_id are NULL) | Batch: determine whether parent is OH-OTT-S-0003 (West Harbor Landing NWR unit) or OH-MC-T-0217 (Portage River Water Trail); assign parent accordingly |
| 7 | HIGH | PAD-US — Resthaven Wildlife Area (~2216ac, ODNR, GAP2) not in DB | Supplemental T2 discovery — major ODNR WA near Oak Harbor |
| 8 | HIGH | PAD-US — Howard Farms Land Acquisition (987ac, GAP2, County Land) not in DB | Supplemental T3/T4 — verify if expansion of OH-MC-S-0021 Howard Marsh Metropark or standalone entity |
| 9 | MEDIUM-HIGH | PAD-US — Bayview West Marsh (221ac, GAP2, Unknown owner) not in DB | Supplemental T7 — verify access and owner; large wetland |
| 10 | MEDIUM-HIGH | PAD-US — Southwestern Lake Erie Marshes And Islands (153ac, NGO, GAP1) not in DB | Supplemental T7 — GAP1 conservation status; NGO-held |
| 11 | MEDIUM-HIGH | PAD-US — Willow Point Wildlife Area (~433ac, GAP2, ODNR) matched to Honey Point WA (score 86) — may be distinct entity | Verify against ODNR inventory: if distinct from OH-OTT-S-0016, stage as separate T2 site |
| 12 | MEDIUM | PAD-US — 5 individual WPAs (30, 59, 63, 65, unnamed; ~239ac total, GAP2, ODNR) not individually cataloged | Supplemental T2 — enumerate individual WPA records |
| 13 | MEDIUM | PAD-US — Decoy Marsh Acquisition (69ac, GAP2, County Land) not in DB | Supplemental T4 |
| 14 | MEDIUM | PAD-US — Genoa Recreation Complex (39ac, City Land) not in DB | Supplemental T6 |
| 15 | MEDIUM | 5 Howard Marsh trails (OH-OTT-T-0072–0076) missing trail_parents → expected OH-MC-S-0021 | Batch: add trail_parents |
| 16 | LOW | OH-OTT-T-0126–0129 missing trail_parents (Catawba Islander Trail, Cedar Meadow, Meadowbrook Marsh, Veterans Memorial) | Batch: add trail_parents to respective parent sites |
| 17 | LOW | PAD-US — Darr-Root Fishing Access (34ac), Portage River Fishing Access (10ac), Port Clinton Waterfront (15ac), Millers Blue Hole WA (13ac) not in DB | Supplemental T2/T6 discovery |
| 18 | LOW | PAD-US — Alumni Park (12ac), Birchard Park (12ac), Firemans Park (5ac), Triangle Park (1ac) not in DB | Supplemental T6 |

---

## Actions Taken This Session

- Fixed OH-OTT-AP-0001, 0002: corrected parent_entity_id from 'OH-OTT-S-001' to 'OH-OTT-S-0001' (Ottawa NWR). ✓
- Fixed OH-OTT-AP-0004: corrected parent_entity_id from 'OH-OTT-S-006' to 'OH-OTT-S-0006' (East Harbor SP). ✓
- Fixed OH-OTT-AP-0005, 0007: corrected parent_entity_id from 'OH-MC-TR-002' (non-existent trail_network ID) to 'OH-MC-T-0217' (Portage River Water Trail, in trails table). ✓
- Fixed OH-OTT-AP-0008: corrected parent_entity_id from 'OH-OTT-T-124' to 'OH-OTT-T-0124' (Lake Erie Islands Water Trail). ✓
- Fixed OH-OTT-AP-0009: corrected parent_entity_id from 'OH-OTT-S-097' to 'OH-OTT-S-0097' (Nehls Memorial Preserve). ✓

---

## Pending Actions

**Data corrections (batch):**
- Assign parent to OH-OTT-AP-0006 (West Harbor Boat Launch) — verify parent: OH-OTT-S-0003 or OH-MC-T-0217
- Add trail_parents: OH-OTT-T-0072–0076 → OH-MC-S-0021 (Howard Marsh Metropark)
- Add trail_parents: OH-OTT-T-0126 → OH-OTT-S-0012; T-0127 → OH-OTT-S-0042; T-0128 → OH-OTT-S-0046; T-0129 → OH-OTT-S-0079

**Supplemental discovery (batch):**
- T2: Resthaven Wildlife Area (~2216ac, ODNR) — Oak Harbor area
- T3/T4: Howard Farms Land Acquisition (987ac) — verify scope vs Howard Marsh Metropark
- T2: Wildlife Production Areas 30, 59, 63, 65 + unnamed (~303ac total, ODNR)
- T2: Willow Point Wildlife Area — verify identity vs Honey Point WA (OH-OTT-S-0016)
- T2: Darr-Root Fishing Access (34ac), Portage River Fishing Access (10ac), Port Clinton Waterfront (15ac), Millers Blue Hole WA (13ac)
- T7: Bayview West Marsh (221ac, GAP2), Southwestern Lake Erie Marshes And Islands (153ac, GAP1)
- T4: Decoy Marsh Acquisition (69ac, GAP2)
- T6: Genoa Recreation Complex (39ac), Alumni Park, Birchard Park, Firemans Park, Triangle Park

---

## Quality Review Outcome

**Status: FAIL — 7 FK integrity issues fixed this session; Resthaven Wildlife Area (~2216ac, ODNR, GAP2) is the largest single discovery gap in any county reviewed and was entirely missed in the original pipeline. Howard Farms Land Acquisition (987ac) and Bayview West Marsh (221ac) are additional substantial gaps.** FK integrity is clean after this session's fixes. Ottawa has strong T1 coverage (Ottawa NWR and its sub-units are excellently cataloged) but significant T2 (ODNR wildlife areas) and T7 (conservation lands) gaps in the interior of the county.

*Review completed 2026-06-08 by Claude. FK fixes applied to DB during review.*
