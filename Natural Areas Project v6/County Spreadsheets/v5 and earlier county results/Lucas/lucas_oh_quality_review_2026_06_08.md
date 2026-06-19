# Lucas County — Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + manual)
**Pipeline run:** lucas_oh_2026_04_27 (v5 schema)
**DB state at review:** post-remediation fixes applied 2026-06-08

---

## Entity Counts (live DB)

| Entity type | Count | Notes |
|---|---|---|
| Sites | 237 | 226 OH-LUC-S- + 11 OH-MC- (with Lucas in counties: Oak Openings parcels, Magee Marsh, Maumee State Forest, Missionary Island WA, Van Tassel WA, Maumee State Scenic River, Ottawa NWR, Providence Metropark, etc.) |
| Trails | 78 | 59 OH-LUC-T- + 19 OH-MC- (with Lucas in counties) |
| Trail segments | 1 | OH-MC-TS-0005 (WCT South Fork, Henry;Lucas) — **2nd segment (WCT North Fork) in TSV but not in DB** |
| Trail networks | 0 | — |
| Trailthings | 0 | v5 run — expected |
| Site networks | 0 | **MISSING — 3 records in TSV (Metroparks Toledo SN, Sylvania AJRD SN, Olander Park System SN) but never upserted to DB** |
| Access points | 21 | OH-LUC-AP-0001–0021 |
| Held entities | 0 | — |

Run metadata: lucas_oh_2026_04_27: input=348, normalized=342, held=0. Run notes record: "233 Sites, 83 Trails, 2 Trail Segments, 0 Trail Networks, 3 Site Networks, 21 APs."

**Partial upsert discrepancy:** Run metadata confirms 3 Site Networks and 2 Trail Segments were generated. DB contains 0 Lucas SNs (only OH-MC-SN-0002 Ottawa NWR Complex, which was upserted during the Ottawa run) and 1 Trail Segment. The 3 Lucas-originated SNs and 1 Trail Segment (WCT North Fork) are present in TSV files but absent from DB — same partial upsert pattern as Hancock County.

Site sequence: max OH-LUC-S-0233, count=226 OH-LUC-S-; gaps present — expected per IMP-117.

---

## GPS Audit

**Sites:** 2 sites missing GPS:
- OH-MC-S-0032 (Oak Openings Corridor, Metroparks Toledo — Fulton County parcels): "GPS needed — unconfirmed… GIS parcel resolution needed." Cross-county corridor parcel. `gps_unresolvable` by nature.
- OH-MC-S-0028 (Maumee State Scenic River): Linear water feature. `gps_unresolvable` by nature.

All other 235 sites have GPS coordinates. No out-of-Ohio values. ✓

**Access points:** 3 of 21 APs have null GPS:
- OH-LUC-AP-0012 (Fort Miamis Kayak Access): Described as "end of Corey Street" — specific coordinates needed
- OH-LUC-AP-0015 (Cannonball Prairie Pond Kayak Access): No GPS in source
- OH-LUC-AP-0016 (Oak Openings Beach Ridge Area Trailhead): No GPS in source

These are trailheads/access points requiring GPS acquisition. AP-0012 is likely locatable; AP-0015 and AP-0016 require GIS verification. Pending GPS acquisition pass.

---

## Held Entities

None currently. Run metadata shows held=0. ✓

---

## PAD-US Completeness Gate

Full GDB spatial query run via `na_padus_query.py Lucas` on 2026-06-08.

- PAD-US records in bbox: 336
- Matched (score ≥ 80): 229
- Unmatched: 79
- Skipped (private/closed): 28

**Skipped correctly:** 13 private golf courses (country clubs) and 15 closed/dedicated nature preserve parcels (Campbell Dedicated, Irwin Prairie Dedicated, "Tampa Strip", Side Cut and Pearson closed parcels, Camp Miakonda private, etc.). All appropriate. ✓

**Notable false 'name variant' match — W.W. Knight:**
PAD-US "W W Knight Nature Preserve" (47ac, GAP2) scored 80 to OH-LUC-S-0228 "Kitty Todd Nature Preserve" and was flagged as a name variant. W.W. Knight and Kitty Todd are distinct Metroparks Toledo properties. W.W. Knight Nature Preserve is in the DB as **OH-WOD-S-0033** (counties='Wood', 44ac) — a bbox false positive. Not a discovery gap; the Wood County DB record is the correct home.

**Bbox false positives (Wood County entities in Lucas bbox):**
- "Wood County Historical Center" (54ac, Regional Agency Land) — Bowling Green, Wood County
- "Slippery Elm Trail" — Wood County trail; bbox extends south

**Not genuine gaps — already in DB:**
- "Providence, Bend View, Farnsworth Metroparks" (bundled PAD-US parcel, 451ac) → three separate sites in DB: OH-MC-S-0027 Providence Metropark, OH-LUC-S-0013 Bend View Metropark, OH-LUC-S-0018 Farnsworth Metropark ✓
- "Blue Creek Conservation Area" (242ac, GAP2) → OH-LUC-S-0014 Blue Creek Metropark (678ac) ✓ — PAD-US name variant for same entity
- "University/Parks Trail" (141ac, County Land) → OH-LUC-T-0012 (trail entity already in DB) ✓ — PAD-US parcel is the trail corridor
- "Wabash-Cannonball Trail" (395ac, NGO) → OH-MC-T-0002 (Wabash Cannonball Trail, already in DB) ✓

**Confirmed genuine discovery gaps:**

| PAD-US name | GAP | Acres | Owner | Tier | Priority |
|---|---|---|---|---|---|
| Keil Farm | 2 | 165 | City Land | T6/T7 | HIGH — large GAP2 parcel; access status "Unknown"; likely conservation land pending development |
| Devilbliss Boy Scout Reservation | 4 | 153 | NGO | T7 | HIGH — large scout camp; open access listed; NGO-owned |
| Lucas County Recreation Center | 4 | 108 | County Land | T4/T6 | MEDIUM — large county rec complex; nature access unclear; scope TBD |
| International Park | 4 | 77 | City Land | T6 | MEDIUM — large Toledo waterfront park on Maumee River; not in DB |
| Wildlife Production Area 44 | 2 | 64 | ODNR | T2 | MEDIUM — ODNR wildlife production land, GAP2; distinct parcel not individually cataloged |
| Riverfront North | 4 | 63 | City Land | T6 | MEDIUM — large Toledo riverfront park; not in DB |
| Woodlands Park | 4 | 42 | City Land | T6 | MEDIUM — 42ac park (likely Northwood area); not in DB |
| Rogers Park | 4 | 41 | City Land | T6 | MEDIUM — 41ac Toledo city park; not in DB |
| Cedar Creeks Preserve | 4 | 39 | County Land | T4 | MEDIUM — county preserve; not in DB |
| Rivercrest Park | 4 | 34 | City Land | T6 | LOW — 34ac city park; not in DB |
| Orleans Park | 4 | 34 | City Land | T6 | LOW — 34ac park (municipality TBD within Lucas); not in DB |
| Harroun Park | 4 | 28 | City Land | T6 | LOW — 28ac park, likely Sylvania area; not in DB |
| Buttonwood/Betty C. Black Recreation Area | 4 | 24 | County Land | T4 | LOW — county rec area; not in DB |
| Jackman Park | 4 | 12 | City Land | T6 | LOW — 12ac, likely Sylvania area |
| Hawthorne Hills Park | 2 | 10 | City Land | T6 | LOW — GAP2 designation; 10ac |
| Horseshoe Island | 4 | 10 | City Land | T6 | LOW — island park on Maumee River |
| Imperial Woods Park | 2 | 2 | City Land | T6 | LOW — small GAP2 parcel |

**Note — WPA 44:** PAD-US lists Wildlife Production Area 44 as a distinct ODNR parcel in Lucas County. The DB contains WPA-named sites for Hancock, Henry, and other counties, but no Lucas County WPA 44 record. This is a genuine T2 gap.

**Note — Keil Farm:** Listed as City Land with GAP2 protection and "Unknown" public access in PAD-US. 165ac of GAP2 land is significant; likely a conservation acquisition in the Lucas County / Toledo metro area. Needs identity verification and access confirmation.

**Note — Numerous sub-10ac unmatched entries:** The 79-record unmatched list includes many small trail corridor parcels (Anthony Wayne Trail, Buckeye Basin Connector, etc.) already represented as trail entities in the DB, numerous sub-3ac mini-parks, school/athletic grounds (Stranahan Elementary, Whiteford Elementary), and cemeteries (Forest Cemetery 99ac, etc.). Most are not NAP scope or are already captured as trail entities. The substantive gaps are those listed in the table above.

**PAD-US result: PARTIAL FAIL — significant T6 and T7 discovery gaps confirmed; WPA 44 (ODNR) and Keil Farm (GAP2) are high-priority additions. Lucas County's urban density means many small parks were already cataloged (excellent city park coverage from T6), but large parks and outer-county parcels have gaps.**

---

## Relationship Table Audit

**trail_parents:** 16 of 78 Lucas-area trails have trail_parents entries:
- OH-LUC-T-0001 through 0007 → correctly parented to OH-LUC-S-0003 (Maumee Bay SP), S-0004 (Irwin Prairie), S-0005 (Campbell SNP)
- OH-MC-T-0203 (Magee Marsh Boardwalk) → OH-MC-S-0010 ✓
- OH-MC-T-0220 (Stewardship Trail) → OH-MC-S-0031 ✓
- OH-OTT-T-0111–0117 (Magee Marsh trails) → OH-MC-S-0010 ✓

**52 Lucas trails (OH-LUC-T-0008 through T-0075 range, with gaps) have no trail_parents entries.** Most are Toledo-area urban park trails where the parent site is clear (e.g., OH-LUC-T-0031–0034 Pearson trails → OH-LUC-S-0026 Pearson Metropark; OH-LUC-T-0016–0022 metropolitan area trails). This is a significant trail_parents gap — likely a partial upsert issue similar to Hancock (trail_parents table not populated in the Lucas pipeline run).

**site_parent:** No Lucas parent-child site relationships — consistent with separate-site approach used throughout v5 pipeline. Acceptable.

**access_point_parents:** All 21 APs reference valid entities after this session's fixes. ✓

**Trail Segments — partial upsert:**

TSV `LUC_trail_segments.tsv` (2 records):
1. "Wabash Cannonball Trail - North Fork" — counties: Fulton;Henry;Lucas;Williams; parent trail: OH-MC-T-0221 — **NOT in DB**
2. "Wabash Cannonball Trail - South Fork" — counties: Henry;Lucas — already in DB as OH-MC-TS-0005 ✓

WCT North Fork needs upsert; will require a new MC-TS sequence number (next available after cross-county audit).

**Site Networks — partial upsert:**

TSV `LUC_site_networks.tsv` (3 records):

| SN name | Counties | Members | Issues | Status |
|---|---|---|---|---|
| Metroparks Toledo | Fulton;Lucas;Ottawa;Wood | 23 members | Member site IDs use 3-digit format (OH-LUC-S-013 etc.); delimiter is "; " (space after semicolon) | NOT IN DB |
| Sylvania Area Joint Recreation District (AJRD) | "Lucas, Ohio" (malformed) | 4 members | Counties field malformed ("Lucas, Ohio" instead of "Lucas"); member IDs likely 3-digit | NOT IN DB |
| Olander Park System | Lucas | 6 members | Member IDs likely 3-digit | NOT IN DB |

All three SNs require corrected member_site_ids (3-digit → 4-digit zero-padded) and, for Sylvania AJRD, counties field fix ("Lucas, Ohio" → "Lucas") before upsert.

---

## Open Flags from Pipeline Run / Handoff

| Flag | Entity | Status |
|---|---|---|
| LUC-F-03 | GNIS marsh features — Cedar Point Marsh | Open — identity verification needed; may be subsurface/submerged feature vs discoverable access point |
| LUC-F-04 | GNIS marsh features — Mallard Club Marsh et al. | Open — multiple GNIS features without clear public access; verify against ODNR records |
| LUC-F-05 | GNIS marsh features — Douglas Marsh, others | Open — same as F-04 |
| LUC-F-07 | Grand Rapids Access — likely Wood County entity | Open — Grand Rapids is in Wood County; AP likely misassigned to Lucas; verify and reparent or reclassify |
| LUC-F-09 | Lucas County Recreation Ramp — identity unknown | Open — possible boat ramp distinct from OH-LUC-S-0190 William P. Coontz Recreation Complex; confirm identity |
| LUC-F-11 | FitPark Ride — Metroparks feature | Open — pending clarification: sub-facility of parent Metropark or distinct AP |
| LUC-F-12 | Cannaley Treehouse Village — Metroparks feature | Open — same as F-11; scope clarification needed |
| LUC-F-13 | Secret Forest — Metroparks feature | Open — same as F-11 |

---

## Data Quality Findings

| # | Severity | Finding | Action |
|---|---|---|---|
| 1 | ~~HIGH~~ FIXED | 16 APs with non-padded parent_entity_ids (OH-LUC-S-013 through S-228 format) — all referencing non-existent site IDs | **Fixed 2026-06-08** — corrected all 16 to zero-padded format; all 16 parents verified as existing |
| 2 | HIGH | 3 site_network records in TSV not upserted to DB (Metroparks Toledo, Sylvania AJRD, Olander Park System) | Batch: assign SN IDs (OH-LUC-SN-0001 onward), correct member_site_ids to 4-digit, fix Sylvania AJRD counties field, upsert to site_networks |
| 3 | HIGH | WCT North Fork trail_segment in TSV not upserted to DB | Batch: assign OH-MC-TS-? ID (after cross-county audit for next available), parent = OH-MC-T-0221, upsert to trail_segments |
| 4 | HIGH | PAD-US — Keil Farm (165ac, GAP2, City Land) not in DB; access status "Unknown" | Supplemental T6/T7 discovery — verify access and stage |
| 5 | HIGH | PAD-US — Devilbliss Boy Scout Reservation (153ac, NGO) not in DB | Supplemental T7 discovery — large open-access scout camp |
| 6 | MEDIUM | PAD-US — International Park (77ac), Riverfront North (63ac) — large Toledo waterfront parks not in DB | Supplemental T6 discovery — Toledo riverfront park system gaps |
| 7 | MEDIUM | PAD-US — Wildlife Production Area 44 (64ac, GAP2, ODNR) not in DB | Supplemental T2 discovery |
| 8 | MEDIUM | 52 OH-LUC-T trails have no trail_parents entries — partial upsert of trail_parents table | Batch: add trail_parents for all Pearson, Wildwood, Swan Creek, Ottawa Park, and other site-parented trails |
| 9 | MEDIUM | PAD-US — Woodlands Park (42ac), Rogers Park (41ac), Cedar Creeks Preserve (39ac), Rivercrest Park (34ac), Orleans Park (34ac) not in DB | Supplemental T4/T6 discovery — outer-county parks and preserves |
| 10 | MEDIUM | Lucas County Recreation Center (108ac, County Land) — not in DB; scope ambiguous | Supplemental T4 investigation — determine if outdoor recreation components qualify |
| 11 | LOW | PAD-US — Harroun Park (28ac), Buttonwood/Betty C. Black (24ac), Jackman Park (12ac), Hawthorne Hills (10ac, GAP2), Horseshoe Island (10ac), Imperial Woods (2ac, GAP2) not in DB | Supplemental T6 discovery — Sylvania-area and Toledo-area parks |
| 12 | LOW | 3 APs missing GPS (AP-0012, AP-0015, AP-0016) | GPS acquisition pass — trailheads and kayak access points |
| 13 | LOW | LUC-F-07 Grand Rapids Access — likely Wood County entity; county assignment unverified | Resolve entity scope; may require reparenting |
| 14 | LOW | Sylvania AJRD SN counties field in TSV: "Lucas, Ohio" (malformed) | Fix to "Lucas" at upsert |
| 15 | LOW | Metroparks Toledo SN member_site_ids in TSV use 3-digit format (e.g., OH-LUC-S-013) and "; " delimiter | Fix to 4-digit zero-padded, semicolon-only delimiter, at upsert |

---

## Actions Taken This Session

- Fixed all 16 OH-LUC-AP-000x parent_entity_id values from non-padded (OH-LUC-S-013 through S-228) to zero-padded format. All 16 parents verified as existing sites. ✓

---

## Pending Actions

**Batch upsert (critical — data in TSV, not in DB):**
- Upsert Metroparks Toledo site_network from `LUC_site_networks.tsv` with OH-LUC-SN-0001; correct 23 member_site_ids from 3-digit to 4-digit zero-padded; fix delimiter
- Upsert Sylvania AJRD site_network from TSV with OH-LUC-SN-0002; correct counties "Lucas, Ohio" → "Lucas"; correct 4 member_site_ids
- Upsert Olander Park System site_network from TSV with OH-LUC-SN-0003; correct member_site_ids
- Upsert WCT North Fork trail_segment from TSV with OH-MC-TS-? (next available MC TS sequence); parent = OH-MC-T-0221

**Data corrections (batch):**
- Add trail_parents for 52 OH-LUC-T trails (Pearson → S-0026, Wildwood Preserve → S-0033, Swan Creek → S-0030, Ottawa Park trails → S-0150, Secor → S-0028, Side Cut → S-0029, etc.)
- Acquire GPS for AP-0012 (Fort Miamis Kayak Access), AP-0015 (Cannonball Prairie), AP-0016 (Oak Openings Beach Ridge Trailhead)
- Resolve LUC-F-07 Grand Rapids Access county assignment (likely Wood County)
- Resolve LUC-F-09 Lucas County Recreation Ramp identity (distinct from S-0190?)
- Resolve LUC-F-11/12/13 Metroparks sub-features (FitPark Ride, Cannaley Treehouse Village, Secret Forest) — AP or note

**Supplemental discovery (batch):**
- T2: Wildlife Production Area 44 (64ac, GAP2, ODNR)
- T6/T7: Keil Farm (165ac, GAP2) — verify access
- T7: Devilbliss Boy Scout Reservation (153ac, NGO)
- T6: International Park (77ac), Riverfront North (63ac) — Toledo waterfront parks
- T4: Cedar Creeks Preserve (39ac), Buttonwood/Betty C. Black (24ac), Lucas County Recreation Center (108ac — scope TBD)
- T6: Woodlands Park (42ac), Rogers Park (41ac), Rivercrest Park (34ac), Orleans Park (34ac), Harroun Park (28ac), Jackman Park (12ac), Horseshoe Island (10ac)
- T6: Hawthorne Hills Park (10ac, GAP2), Imperial Woods Park (2ac, GAP2)
- Resolve open handoff flags LUC-F-03/04/05 (GNIS marsh features)

---

## Quality Review Outcome

**Status: FAIL — HIGH-severity partial upsert (3 site_networks, 1 trail_segment missing from DB); 16 FK integrity issues fixed this session; significant PAD-US discovery gaps confirmed (Keil Farm 165ac GAP2, Devilbliss BSA 153ac, International Park 77ac, Riverfront North 63ac, WPA 44 64ac).** Lucas County has the strongest city park coverage of any county reviewed (229 of 336 PAD-US records matched), reflecting an extensive pipeline run. Core weakness is: (1) the partial upsert of site_networks and trail segments, (2) the trail_parents table not populated for 52 trails, and (3) several outer-county conservation and recreation parcels not discovered in the original run.

*Review completed 2026-06-08 by Claude. FK fixes applied to DB during review.*
