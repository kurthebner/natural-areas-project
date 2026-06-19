# Seneca County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 135 active | OH-SEN-S-0001 – OH-SEN-S-0142 (gaps at 29–33 held, 98, 100 unexplained) |
| Trails | 3 | OH-SEN-T-0002/0003/0004 (T-0001 held) |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 0 | — |
| Held Entities | 6 | 5 sites (identity_uncertain cemeteries) + 1 trail (cross_county_held) |

**Run metadata:** Two pipeline runs recorded:
- `seneca_oh_2026_05_28` — input=146, normalized=138, held=8 (initial pass; 11 gps_missing held)
- `seneca_oh_gps_release_2026_05_28` — input=146, normalized=140, held=6 (GPS release pass)

---

## 2. FK Integrity and Data Errors Fixed This Session

### Fix 1 — Bellevue parks: Seneca incorrectly in counties

Seven OH-SAN- sites (Bellevue city parks) had `counties = 'Erie;Huron;Sandusky;Seneca'`. Bellevue, Ohio lies at the Erie–Huron–Sandusky tripoint and does **not** extend into Seneca County. Seneca was incorrectly appended during the Sandusky pipeline run.

Fixed `counties = 'Erie;Huron;Sandusky'` for:
OH-SAN-S-0072 (Magdalyn Aigler Recreation Complex), 0073, 0074, 0075, 0076, 0077, 0078. All 7 verified.

OH-SAN-S-0110 "Green Springs Cemetery" (counties='Sandusky;Seneca') is **correct** — Green Springs village straddles both counties.

No AP FK padding errors detected. No APs in this county.

---

## 3. Held Entities

### 3a — 5 identity_uncertain cemeteries (batch deletion needed)

OH-SEN-S-0029 through OH-SEN-S-0033 (Chenoweth, Gundy, Ebenezer M.E., Little Pennsylvania, Oak Grove cemeteries) were discovered during the Seneca pipeline as Pleasant Township cemeteries, but the hold_detail confirms these are **Franklin County** entities (Pleasant Township near Grove City, OH). They were not found in Seneca County GNIS, parcel layer, or web sources.

**Batch action:** Delete these 5 records from Seneca held_entities. If not already in Franklin County's DB, stage for Franklin County supplemental discovery.

### 3b — OH-SEN-T-0001 Sandusky State Scenic River (cross_county_held)

Held as Scenario A cross_county_held, with Wyandot County listed as primary. The hold_detail identifies 8 partner counties (Crawford, Wyandot, Marion, Hancock, Ottawa, Erie, Huron, Seneca). Note: OH-SAN-S-0005 "Sandusky State Scenic River" is also held in Sandusky County's pipeline (primary=Wyandot) as a **Site**, while this Seneca entity is cataloged as a **Trail**. These represent the same river corridor under different entity types. Cross-county resolution during the Wyandot County run must reconcile the entity type discrepancy (Site vs Trail).

---

## 4. GPS Status

All 135 active sites have GPS values (0 missing). GPS Gate: passed.

**Cemetery duplicates sharing GPS — data quality flags:**
- OH-SEN-S-0085 "Reformed Cemetery" and OH-SEN-S-0086 "Reformed Cemetery [2]" share identical GPS (41.05568, -83.015845) with empty descriptions. Two cemeteries with the same name in different locations that share a coordinate, or one true duplicate. Investigate: if same location, delete one; if different locations, acquire GPS for second.
- OH-SEN-S-0133 "Rock Creek Cemetery" and OH-SEN-S-0134 "Rock Creek Cemetery [2]" same issue (41.0781, -83.132202).

---

## 5. Trail Parents

| Trail | Trail_parents | Status |
|---|---|---|
| OH-SEN-T-0002 Rock Creek Trail | 0 | Missing — add → OH-SEN-S-0034 Hedges-Boyer Park |
| OH-SEN-T-0003 Clary Boulee McDonald Preserve — Wetland Loop | 1 | ✓ |
| OH-SEN-T-0004 Clary Boulee McDonald Preserve — H2Ohio Loop | 1 | ✓ |

Rock Creek Trail runs through Tiffin's park corridor along Rock Creek; Hedges-Boyer Park (78ac) is the primary site. Batch fix: `INSERT INTO trail_parents VALUES ('OH-SEN-T-0002', 'OH-SEN-S-0034')`.

---

## 6. PAD-US Spatial Audit

**Bbox:** Seneca County bounding box. 74 PAD-US fee records in bbox; 25 matched (≥80); 36 unmatched; 13 skipped.

### 6a. Bbox false positives (Sandusky County bleed)

The following unmatched records are Sandusky County entities (Fremont and Bellevue area parks) bleeding into Seneca's bbox. All appeared in the Sandusky County unmatched list:

Community Park (29ac), Gus Wolf Park (3ac), Hendricks Park (5ac), Paden Park (2ac), Cherry Street Park (2ac), Birchard Park (12ac), Roger Young Memorial Park (39ac), Walsh Park (49ac), Fremont Community Recreation Complex (27ac), Portage Trail Park (17ac), Conner Park (18ac), Limerick Park (14ac), Stephenson Park (1ac), North Coast Inland Trail (124ac), Bradner Preserve (124ac) — **all Sandusky County**.

Sandusky Abbotts Bridge SR (22ac) and Sandusky Wolf Creek SR (84ac) also appeared in Sandusky County; verify which county these specific parcels are in.

### 6b. Sandusky River SSR parcels — not discrete site gaps

The following ODNR records represent land parcels associated with the **Sandusky State Scenic River** designation:
- Sandusky — Heck Bridge SR (210ac, GAP4)
- Sandusky Abbotts Bridge SR (22ac)
- Sandusky Izaak Walton SR (30ac)
- Sandusky Wolf Creek SR (84ac)

These are access/protection parcels along the Sandusky River corridor, which flows through Seneca County. They are not standalone sites — they will be associated with the Sandusky State Scenic River entity when the Wyandot County pipeline resolves OH-SEN-T-0001 and OH-SAN-S-0005. **Not individual discovery gaps**; document in cross-county resolution notes.

### 6c. Genuine Seneca County gaps

**T2 — State / ODNR:**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Green Springs State Forest | 120 | 2 | Straddles Sandusky/Seneca border; verify primary county; also appeared in Sandusky review |
| Wildlife Production Area 61 | 40 | 2 | ODNR WPA; Seneca County; not in DB |
| Wildlife Production Area 62 | 70 | 2 | ODNR WPA; Seneca County; not in DB |
| Wildlife Production Area 64 | 49 | 2 | ODNR WPA; Seneca County; not in DB |

Note: WPAs 14, 18, 31, 47, 50 appeared in both Sandusky and Seneca bboxes — verify which county each belongs to before cataloging.

**T4/T6 — County / Municipal:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Paradiso Athletic Complex | 82 | Other/State | Large facility; governance unclear from PAD-US; verify managing entity |
| Fostoria Rail Park | 5 | City | Fostoria (Seneca County seat area); not in DB |
| Don Elchert Field | 5 | City | Tiffin area; not in DB |
| Apple-Jack Park | 3 | City | Fostoria area; not in DB |
| Legion Park | 11 | City | Seneca County municipality; not in DB |
| Tiffin Baseball Field | 2 | City | Tiffin; not in DB |
| Historical District Park | 0 | City | Tiffin; 0ac in PAD-US; not in DB |
| Risdon Square | 1 | City | Tiffin; not in DB |

### 6d. Matched — acreage discrepancies

| PAD-US Record | PAD-US Acres | DB Acres | Note |
|---|---|---|---|
| Hedge-Boyer Park | 81 | 78 | Minor; within rounding |
| Foundation Park | 81 | 50 | DB lower; verify source |
| Garlo Heritage Nature Preserve | 37 | 292 | DB much larger; likely includes conservation easements beyond fee parcel |
| Meadowbrook Park | 69 | 160 | DB larger; verify source |
| Zimmerman Nature Preserve | 13 | 5.5 | PAD-US larger; verify |
| Forrest NP (22ac) + Addition (25ac) | 47 total | 47 | ✓ DB correctly reflects combined acreage |

---

## 7. Sequence Gaps

- **S-0029 to S-0033**: held entities (identity_uncertain cemeteries — Franklin County, see §3a)
- **S-0098, S-0100**: not in DB, not in held_entities; cause unknown; likely cemetery records removed during GPS resolution
- **T-0001**: held (Sandusky State Scenic River, cross_county_held)

---

## 8. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | 7 Bellevue parks had Seneca in counties | FIXED | Applied this session |
| 2 | 5 cemeteries wrongly attributed to Seneca (actually Franklin County) | HIGH | Batch: delete from Seneca held_entities; stage for Franklin County |
| 3 | OH-SEN-T-0001 entity type conflicts with OH-SAN-S-0005 (Trail vs Site) | HIGH | Cross-county resolution in Wyandot County run |
| 4 | Missing trail_parent for OH-SEN-T-0002 | MEDIUM | Batch: add → OH-SEN-S-0034 |
| 5 | Reformed Cemetery [2] and Rock Creek Cemetery [2] duplicate GPS | MEDIUM | Investigate: verify distinct locations or delete duplicates |
| 6 | Green Springs State Forest (120ac, GAP2) not cataloged | MEDIUM | Supplemental T2; verify primary county |
| 7 | WPAs 61/62/64 (~159ac total, GAP2, ODNR) not cataloged | MEDIUM | Supplemental T2 |
| 8 | Sandusky River SSR parcels (346ac): not site gaps — associate with SSR entity | NOTE | Resolve in Wyandot County run |
| 9 | 8 Tiffin/Fostoria city parks not cataloged | MEDIUM | Supplemental T6 |
| 10 | Paradiso Athletic Complex (82ac) not cataloged | MEDIUM | Verify governance; supplemental T4 or T6 |
| 11 | Acreage discrepancies: Foundation Park, Garlo Heritage, Meadowbrook, Zimmerman | LOW | Verify against source documents |

---

## 9. Batch Phase Actions

- [ ] Delete OH-SEN-S-0029 through S-0033 from held_entities; stage for Franklin County supplemental T8 discovery
- [ ] Add trail_parent: OH-SEN-T-0002 → OH-SEN-S-0034 (Hedges-Boyer Park)
- [ ] Investigate Reformed Cemetery [2] (S-0086) and Rock Creek Cemetery [2] (S-0134): verify distinct vs duplicate; fix GPS or delete as appropriate
- [ ] Flag OH-SEN-T-0001 / OH-SAN-S-0005 entity type conflict for Wyandot County cross-county resolution
- [ ] Supplemental T2 discovery: Green Springs State Forest (verify county), WPAs 61/62/64; resolve WPAs 14/18/31/47/50 county attribution
- [ ] Supplemental T6 discovery: Fostoria Rail Park, Don Elchert Field, Apple-Jack Park, Legion Park, Tiffin Baseball Field, Historical District Park, Risdon Square
- [ ] Investigate Paradiso Athletic Complex (82ac): identify governance and tier
- [ ] Verify acreage for Foundation Park, Garlo Heritage NP, Meadowbrook Park, Zimmerman NP against source documents
