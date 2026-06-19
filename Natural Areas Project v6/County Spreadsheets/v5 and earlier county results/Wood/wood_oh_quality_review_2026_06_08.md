# Wood County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 71 active WOD + 5 MC | OH-WOD-S-0002–0077 (gaps); MC: OH-MC-S-0027/0028/0029/0030/0031 reference Wood |
| Trails | 4 WOD + 5 MC | OH-WOD-T-0001/0002/0038/0039; MC: T-0001/0201/0202/0204/0217 reference Wood |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 3 | OH-WOD-AP-0001/0002/0003 |
| Held Entities | 5 | 4 unconfirmed_baseline_seeds + 1 legacy SI entity (see §3) |

**Run metadata:** `wood_oh_2026_04_14` — input=84, normalized=84, held=7 (pipeline_version=5.2)

Note: "pipeline_version=5.2" — Wood County ran on the v5 pipeline. The held count of 7 in run_metadata vs 5 currently in held_entities indicates 2 entities resolved or removed since the pipeline run. A supplemental run on 2026-05-16 added +2 sites (BSC Bell Woods NP, Mauks Prairie) and +1 trail.

---

## 2. FK Integrity

No FK errors detected. All three APs have valid parent references:

| AP | Name | Parent | Status |
|---|---|---|---|
| OH-WOD-AP-0001 | Fort Meigs Access | OH-MC-T-0001 (Trail) | ✓ |
| OH-WOD-AP-0002 | Maple Street Boat Launch | OH-MC-T-0001 (Trail) | ✓ |
| OH-WOD-AP-0003 | Louisiana Avenue Boat Dock | OH-MC-T-0001 (Trail) | ✓ |

### Fix applied this session

**OH-MC-S-0031 "Maumee State Forest" — Wood County missing from counties field.**

Counties was `'Fulton;Henry;Lucas'`. PAD-US shows two fee parcels (1,501ac + 1,930ac = 3,431ac total) in the Wood County bbox. Fixed to `'Fulton;Henry;Lucas;Wood'`. Verified post-update.

---

## 3. Sequence Gaps and Trail ID Anomaly

**Site gaps:** S-0001, 0013, 0028, 0034, 0035, 0073 — none in held_entities; removed during resolution (out-of-scope, merged, or reclassified).

Note: OH-WOD-S-0073 slot is vacated; OH-WOD-SI-0073 (legacy "SI" prefix) exists in held_entities as "Mishe Monoto Preserve" — see §3b below.

**Trail ID gap — T-0002 to T-0038:** Active WOD trails are T-0001, T-0002, T-0038, T-0039. No T-0003 through T-0037 exist in any table. The Providence Metropark trails (T-0038, T-0039) appear to have been assigned sequence numbers based on a counter initialized at 37, likely reflecting prior trail records that were removed from the DB or an unresolved pipeline v5.2 sequencing bug. Not a missing-data issue but warrants documentation in the Wood County session log.

---

## 4. Held Entities

### 4a — 4 unconfirmed_baseline_seeds

| Record ID | Name | Notes |
|---|---|---|
| OH-WOD-S-0078 | Devils Hole Prairie | Baseline seed; needs authoritative source confirmation |
| OH-WOD-S-0079 | Hulls Prairie | Baseline seed; needs authoritative source confirmation |
| OH-WOD-S-0080 | Tontogany Prairie | Baseline seed; needs authoritative source confirmation |
| OH-WOD-S-0081 | North Baltimore Reservoir | Baseline seed; needs authoritative source confirmation |

Batch action: confirm each against ODNR or authoritative source; release or delete as appropriate.

### 4b — OH-WOD-SI-0073 "Mishe Monoto Preserve" (legacy SI prefix, unconfirmed_baseline_seed)

Hold detail states the governance entity is Appalachia Ohio Alliance, which operates in southeast Ohio (Athens/Hocking/Pickaway area) — not Wood County. Cannot confirm as a Wood County entity. Legacy "SI" ID prefix predates v6 conventions.

Batch action: remove from Wood County held_entities; stage for Pickaway County or Hocking County T7 supplemental discovery if not already cataloged there.

---

## 5. Duplicate Entities (batch deletion needed)

### 5a — Van Tassel Wildlife Area

Two entities for the same wildlife area:
- **OH-WOD-S-0015** "Van Tassel Wildlife Area" — `counties='Wood'`, `acres=NULL`
- **OH-MC-S-0029** "Van Tassel Wildlife Area" — `counties='Lucas;Wood'`, `acres=88.0`

Van Tassel WA straddles Lucas and Wood counties. OH-MC-S-0029 is the correct representation. OH-WOD-S-0015 was created during the Wood County pipeline without detecting the pre-existing MC entity.

Batch action: delete OH-WOD-S-0015; confirm any trail_parents or APs referencing it are updated to OH-MC-S-0029.

### 5b — Maumee State Forest (Lucas County duplicate)

- **OH-MC-S-0031** "Maumee State Forest" — `counties='Fulton;Henry;Lucas;Wood'` (fixed this session), `acres=3452.0` — correct representation
- **OH-LUC-S-0045** "Maumee State Forest" — `counties='Lucas'`, `acres=NULL` — single-county duplicate created during Lucas County pipeline

Batch action: delete OH-LUC-S-0045; confirm no trail_parents or APs reference it.

---

## 6. GPS Status

All 71 active WOD sites have GPS values (0 missing). GPS Gate: passed.

**9 sites with low-precision GPS (≤3 decimal places):**

| Site ID | Name | GPS |
|---|---|---|
| OH-WOD-S-0002 | Fort Meigs State Memorial | 41.572, -83.6625 |
| OH-WOD-S-0010 | Wood County Wildlife Area 9 | 41.525, -83.5009 |
| OH-WOD-S-0014 | Maumee River Weir Rapids Wildlife Area | 41.402, -83.876 |
| OH-WOD-S-0016 | Adam Phillips Pond | 41.368, -83.6247 |
| OH-WOD-S-0022 | Buttonwood/Betty C. Black Recreation Area | 41.545, -83.5795 |
| OH-WOD-S-0037 | Wood County Museum | 41.368, -83.6247 |
| OH-WOD-S-0038 | City Park | 41.382, -83.6513 |
| OH-WOD-S-0041 | Wintergarden/St. John's Nature Preserve | 41.372, -83.668 |
| OH-WOD-S-0074 | 577 Foundation | 41.554, -83.6218 |

Note: S-0016 (Adam Phillips Pond) and S-0037 (Wood County Museum) share identical GPS 41.368, -83.6247. These are different sites — S-0037 may have inherited S-0016's coordinate. Verify both in precision GPS pass.

---

## 7. Trail Parents

| Trail | Status | Recommended parent |
|---|---|---|
| OH-WOD-T-0001 Slippery Elm Trail | 0 parents | Rail trail corridor managed by Wood County Park District; no dedicated site in DB for the corridor — identify or create parent before adding trail_parent |
| OH-WOD-T-0002 Pat & Clint Mauk's Prairie Trail | 0 parents | → OH-WOD-S-0077 (Pat & Clint Mauk's Prairie) |
| OH-WOD-T-0038 Providence River Bluff Trail | 0 parents | → OH-MC-S-0027 (Providence Metropark) |
| OH-WOD-T-0039 Providence Wolf Rapids | 0 parents | → OH-MC-S-0027 (Providence Metropark) |
| MC trails (×5) | 0 Wood parents | Identify Wood County site parents per trail corridor |

---

## 8. PAD-US Spatial Audit

**Bbox:** Wood County bounding box. 66 PAD-US fee records in bbox; 36 matched (≥80); 20 unmatched; 10 skipped.

### 8a. Wrong matches

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Baer Park (8ac, City) | OH-WOD-S-0040 Carter Park | 80 | Wrong — Baer Park is OH-LUC-S-0207 (Lucas County bbox bleed); Carter Park is correctly cataloged |

### 8b. False negatives (in DB, score below threshold)

| PAD-US Record | DB Entity | Score | Note |
|---|---|---|---|
| Rudolph-Savanna Preserve (52ac) | OH-WOD-S-0031 Rudolph Savanna | 72 | Hyphen + "Preserve" suffix dropped score; IS in DB; NOT a gap |
| Slippery Elm Trail (100ac) | OH-WOD-T-0001 | 49 | Trail corridor parcel; entity in DB as trail; NOT a gap |
| Wabash-Cannonball Trail (395ac) | OH-MC-T-0002 | 42 | Trail right-of-way; entity in DB as trail; NOT a gap |

### 8c. Bbox false positives in unmatched list

- **Lanker Wildlife Area** (26ac, GAP2) — OH-LUC-S-0009 (Lucas County); not a Wood gap
- **Blue Creek Conservation Area** (242ac, GAP2) — OH-LUC-S-0014 Blue Creek Metropark (Lucas County); not a Wood gap

### 8d. Genuine Wood County gaps

**T2 — State:**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Maumee State Forest (×2 parcels) | 3,431 | 2 | Exists as OH-MC-S-0031; Wood County was missing from counties — **FIXED this session**. No cataloging gap. |

**T3/T4 — District / Regional Agency:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Nona Park Stone Quarry and Ball Fields | 80 | Regional Agency | Not in DB; likely Metroparks of Toledo Area; significant T3 supplemental |
| Wood County Historical Center | 54 | Regional Agency | Score 76 near-miss; DB has S-0037 Wood County Museum (51ac); verify whether same campus or distinct entity |

**Investigate — Providence area:**

| PAD-US Record | Acres | Notes |
|---|---|---|
| Providence, Bend View, Farnsworth Metroparks | 451 | Score 62; Providence Metropark = OH-MC-S-0027 (in DB); "Bend View" and "Farnsworth" are additional Toledo Metroparks units; verify whether Wood County has land holdings beyond the Providence Metropark DB entity, or whether this is the same parcel under a combined PAD-US name |

**T6 — Municipal (city parks not cataloged):**

| PAD-US Record | Acres | Notes |
|---|---|---|
| Bowling Green Training and Community Center | 81 | City; large; verify if park or rec facility only |
| Whitehouse Village Park | 14 | Village of Whitehouse |
| West Poe Recreation Area | 12 | City park; municipality TBD |
| Conneaut/Haskins Park | 7 | May relate to S-0043 "Conneaut Park Sledding Hill" — Haskins portion not cataloged |
| Conrad Park | 7 | City |
| Stitt Park | 5 | City |
| Waterworks Park | 6 | City |
| Memorial Field | 6 | City |
| Pray Park | 1 | City |

### 8e. Matched — data quality flags

Many matched WOD sites have NULL acreage in the DB. PAD-US values can serve as a baseline:

| PAD-US Record | PAD-US Acres | DB Entity | DB Acres |
|---|---|---|---|
| Black Swamp Preserve | 64 | OH-WOD-S-0020 | NULL |
| City Park | 77 | OH-WOD-S-0038 | NULL |
| Carter Park | 59 | OH-WOD-S-0040 | NULL |
| Wintergarden/St. John's NP | 103 | OH-WOD-S-0041 | NULL |
| Adam Phillips Pond | 55 | OH-WOD-S-0016 | NULL |
| Otsego Park | 20 | OH-WOD-S-0029 | NULL |
| Conneaut Park | 3 | OH-WOD-S-0043 | NULL |
| Dunbridge Road Soccer Fields | 13 | OH-WOD-S-0044 | NULL |
| Raney Playground | 0 | OH-WOD-S-0045 | NULL |
| Ridge Park | 3 | OH-WOD-S-0046 | NULL |
| Cricket Frog Cove | 156 | OH-WOD-S-0025 | 160.0 (close) |

Also: OH-MC-S-0027 Providence Metropark has NULL acreage; PAD-US "Providence/Bend View/Farnsworth" combined record shows 451ac — that figure may cover multiple parks, so use with caution.

**WPA / Wood County WA cross-reference:** PAD-US returns 10 WPA records (statewide IDs: 3, 6, 7, 8, 11, 12, 20, 21, 42, 58), all scoring ≥94 against OH-WOD-S-0012 "Bairdstown Wildlife Production Area" due to shared token. DB separately catalogs Wood County Wildlife Areas 1–10 (S-0003–S-0011) individually. All WPA/WA entities are in DB; the multi-match is a fuzzy-match artifact. However, **all Wood County WA entities (S-0003 through S-0012) have NULL acreage** — batch: populate from PAD-US or ODNR source.

---

## 9. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | OH-MC-S-0031 Maumee State Forest missing Wood from counties | FIXED | Applied this session |
| 2 | OH-WOD-S-0015 Van Tassel WA duplicate (superseded by OH-MC-S-0029) | HIGH | Batch: delete WOD entity |
| 3 | OH-LUC-S-0045 Maumee State Forest duplicate (superseded by OH-MC-S-0031) | HIGH | Batch: delete LUC entity |
| 4 | OH-WOD-SI-0073 Mishe Monoto Preserve: wrong county (SE Ohio, not Wood) | HIGH | Batch: remove from Wood held; stage for Pickaway/Hocking T7 |
| 5 | 0 trail_parents for 4 WOD trails + 5 MC trails | MEDIUM | Batch: add trail_parents per §7 |
| 6 | T-0038/0039 trail ID gap (T-0002 → T-0038): pipeline v5.2 sequencing anomaly | MEDIUM | Document in session log; IDs are stable, no renumbering needed |
| 7 | 4 unconfirmed_baseline_seed held entities (S-0078–0081) | MEDIUM | Batch: verify each against ODNR/authoritative source; release or delete |
| 8 | 9 sites with low-precision GPS; S-0016 and S-0037 share identical coordinate | MEDIUM | Batch: precision GPS acquisition; verify S-0037 coordinate |
| 9 | Nona Park Stone Quarry and Ball Fields (80ac, Regional Agency) not cataloged | MEDIUM | Supplemental T3 discovery |
| 10 | 9 municipal parks not cataloged (~135ac total) | MEDIUM | Supplemental T6 discovery |
| 11 | Wood County Historical Center (54ac) vs Wood County Museum (S-0037): same or distinct? | MEDIUM | Investigate; supplement T4 if distinct |
| 12 | Providence/Bend View/Farnsworth PAD-US record (451ac): verify vs OH-MC-S-0027 scope | MEDIUM | Investigate; supplement if Bend View/Farnsworth have Wood County land beyond Providence |
| 13 | NULL acreage on ~15 matched sites (WAs, parks, preserves) | LOW | Batch: populate from PAD-US values or ODNR/parks source |
| 14 | Bowling Green Training and Community Center (81ac): park vs rec facility | LOW | Verify scope; supplement T6 if a park entity |

---

## 10. Batch Phase Actions

- [ ] Delete OH-WOD-S-0015 (Van Tassel WA — duplicate of OH-MC-S-0029); update any trail_parents or APs
- [ ] Delete OH-LUC-S-0045 (Maumee State Forest — duplicate of OH-MC-S-0031); update any trail_parents or APs
- [ ] Remove OH-WOD-SI-0073 from held_entities; stage Mishe Monoto Preserve for Pickaway/Hocking T7
- [ ] Add trail_parents: T-0002 → S-0077; T-0038 → MC-S-0027; T-0039 → MC-S-0027; identify T-0001 parent; add MC trail parents for Wood County sites
- [ ] Verify 4 unconfirmed_baseline_seeds (S-0078–0081); release or delete
- [ ] Precision GPS for 9 low-precision sites; resolve S-0016/S-0037 shared coordinate
- [ ] Supplemental T3 discovery: Nona Park Stone Quarry and Ball Fields (80ac)
- [ ] Supplemental T6 discovery: Bowling Green Training Center (verify), Whitehouse Village Park, West Poe Recreation Area, Conneaut/Haskins Park, Conrad Park, Stitt Park, Waterworks Park, Memorial Field, Pray Park
- [ ] Investigate: Wood County Historical Center vs Wood County Museum (same campus?)
- [ ] Investigate: Providence/Bend View/Farnsworth 451ac PAD-US record vs OH-MC-S-0027 scope
- [ ] Populate NULL acreages on WA entities (S-0003–S-0012) and matched parks from PAD-US values
- [ ] Document T-0038/0039 sequence anomaly in Wood County session log
