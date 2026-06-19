# Paulding County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range |
|---|---|---|
| Sites | 22 | OH-PAU-S-0001 – OH-PAU-S-0022 |
| Trails | 5 | OH-MC-T (all multi-county) |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 5 | OH-PAU-AP-0001 – OH-PAU-AP-0005 |
| Held Entities | 0 | table empty (4 from run_metadata resolved) |

**Run metadata:** `paulding_oh_2026_04_08` — input=32, normalized=28, held=4

All 5 trails are multi-county (OH-MC-T): Maumee River Water Trail (0001), North Country NST (0200), Miami and Erie Canal Towpath (0216), Buckeye Trail — Delphos Section (0218), Buckeye Trail — Defiance Section (0219).

---

## 2. FK Integrity

### Fixes applied this session

| AP | Old value | New value | Issue |
|---|---|---|---|
| OH-PAU-AP-0001 | OH-PAU-TN-001 | OH-PAU-TN-0001 | Zero-padding fix |
| OH-PAU-AP-0005 | OH-MC-TR-003 | OH-MC-T-0216 | Ghost TR-003 → Miami and Erie Canal Towpath |

### Remaining broken FK (batch phase)

**OH-PAU-AP-0001** (Canal Park Trailhead) — `parent_entity_id = OH-PAU-TN-0001`, `parent_entity_type = Trail Network`. **OH-PAU-TN-0001 does not exist** in the trail_networks table; no Paulding trail networks were upserted. The zero-padding fix corrected the format but not the substance. Canal Park Trailhead provides access to the Miami and Erie Canal Towpath. Recommended fix: reparent to OH-MC-T-0216, type Trail.

```sql
-- Batch fix
UPDATE access_points
SET parent_entity_id = 'OH-MC-T-0216', parent_entity_type = 'Trail'
WHERE access_point_id = 'OH-PAU-AP-0001';
```

---

## 3. GPS Status

All 22 sites have GPS values (0 missing, 0 gps_unresolvable). GPS Gate: passed.

**Data quality concern — placeholder-quality coordinates.** Several sites share suspiciously round or repeated coordinates suggesting centroid approximations rather than precise park GPS:

- 41.137, -84.573 (Paulding village centroid): OH-PAU-S-0006, -0010, -0012, -0013, -0014, -0015, -0016 (7 sites)
- 41.1283, -84.7023 (Canal Park coord): OH-PAU-S-0003, -0005 (2 sites share this)
- 41.1969, -84.5775 (Cecil Bridge coord): OH-PAU-S-0004, -0007 (2 sites share this)

These may represent discovery-time centroid entries. Precision GPS acquisition needed for all 11 sites in the batch phase.

---

## 4. Trail Parents

**0 of 5 trails have trail_parents entries.** All 5 are multi-county MC trails — trail_parents records linking them to sites in Paulding County were not created. This is consistent with the multi-county trail parent gap identified in Lucas and Ottawa reviews.

Paulding-specific trail_parents to add in batch phase:
- OH-MC-T-0216 → OH-PAU-S-0003 (Canal Park), OH-PAU-S-0004 (Cecil Bridge Park), OH-PAU-S-0005 (Five Span Park), OH-PAU-S-0006 (Flat Rock Trail Park), OH-PAU-S-0020 (Forder Bridge Conservation Area)
- OH-MC-T-0001 (Maumee River Water Trail) → OH-PAU-S-0003, OH-PAU-S-0004, OH-PAU-S-0020

---

## 5. Partial Upsert Check

No site_networks or trail_networks to upsert — Paulding County has none in the TSV files. No partial upsert issue.

---

## 6. PAD-US Spatial Audit

**Bbox:** Paulding County bounding box. 42 PAD-US fee records in bbox; 12 matched (score ≥ 80); 23 unmatched; 7 skipped (closed access).

### 6a. Wrong matches (false positives in matched list)

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Antwerp Community Park (5ac, City) | OH-PAU-S-0017 Payne Community Park | 86 | Wrong village — Antwerp ≠ Payne |
| Cecil Community Park (4ac, City) | OH-PAU-S-0013 Herb Monroe Community Park | 82 | Wrong — Cecil is a different location |
| Charloe Community Park (2ac, City) | OH-PAU-S-0017 Payne Community Park | 82 | Wrong village — Charloe ≠ Payne |
| Ney Community Park (10ac, City) | OH-PAU-S-0017 Payne Community Park | 89 | Wrong county — Ney is in Defiance County (bbox bleed) |
| Oxbow Lake Wildlife Area (386ac, ODNR, GAP2) | OH-PAU-S-0001 Lake Wayne R. Carr WA | 86 | Wrong — Oxbow Lake WA is OH-DEF-S-0002 (Defiance County) |

**Near-miss false negative:** Lela McGuire Jeffrey Park (15ac) — unmatched, score 68. This IS in DB as OH-PAU-S-0012 "Lela McGuire-Jeffery Park" (spelling variant "Jeffrey" vs "Jeffery" dropped score below threshold). Not a gap.

### 6b. Bbox false positives in unmatched list

The northeast portion of Paulding County's bbox overlaps Defiance County. The following unmatched records are **Defiance County entities**, not Paulding gaps:

- Camp Lakota (474ac, NGO) — OH-DEF-S-0030
- Bronson Park (23ac, City) — Defiance City
- Diehl Park (40ac, City) — Napoleon (Henry County)
- Second Ward Park (1ac), Legion Field (2ac) — Henry County
- Hicksville Recreation Park (67ac, City) — Hicksville (Defiance County)
- Independence Dam State Park (188ac, ODNR) — OH-DEF-S-0001
- Maumee SR parcels (2ac + 51ac, ODNR) — Defiance County
- Flatrock Creek Wildlife Area (4ac, ODNR) — Defiance County (also in Defiance review)
- Six Mile Wildlife Area (4ac, ODNR) — Defiance County (also in Defiance review)

### 6c. Genuine Paulding gaps

**HIGH priority:**

| PAD-US Record | Acres | Owner | GAP | Notes |
|---|---|---|---|---|
| Forrest Woods NP: Harper-Forrest Expansion | 77 | NGO | 2 | Parcel of Forrest Woods SNP (OH-PAU-S-0002); T7 supplemental discovery |
| Forrest Woods NP: Land Acquisition | 78 | NGO | 2 | Same; appears in Defiance bbox too — cross-county entity |
| Forrest Woods NP: Rooks-Harper Expansion | 60 | NGO | 2 | Same |
| Forrest Woods NP: Shaffer Property Expansion | 40 | NGO | 2 | Same |

4 expansion parcels totaling ~255ac, all managed by Black Swamp Conservancy (OH-PAU-S-0010 manager), associated with Forrest Woods State Nature Preserve (OH-PAU-S-0002). These parcels also appeared in the Defiance County PAD-US bbox. May be multi-county (Paulding;Defiance); verify county boundary. T7 supplemental discovery. Could be cataloged as child sites of OH-PAU-S-0002 or as separate sites with ODNR/BSC governance.

**MEDIUM priority:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Antwerp Community Park | 5 | City | Village of Antwerp park; not in DB; T6 supplemental |
| UAW Park | 37 | Local Gov | Appears in Defiance bbox too; verify which county; if Paulding: T6 supplemental |

**Village parks not discovered (T6 supplemental):**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Cecil Community Park | 4 | City | Village of Cecil; distinct from Cecil Bridge Park (T3) |
| Charloe Community Park | 2 | City | Unincorporated community of Charloe |
| Melrose Town Park & Ballfield | 8 | City | Village of Melrose |
| Paulding Athletic Fields | 18 | City | Village of Paulding; may be Paulding Water/Skate Park parcel |
| Moats Park | 13 | Local Gov | Village of Paulding area |
| School Park | 4 | Local Gov | Village of Paulding area |
| Oakwood Ball Field | 13 | City | Village of Oakwood; distinct from Oakwood Community Park (OH-PAU-S-0018) |
| Lafountain Park | 6 | City | Small Paulding County municipality |

---

## 7. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | AP-0001 dangling FK: OH-PAU-TN-0001 doesn't exist | HIGH | Batch: reparent to OH-MC-T-0216 |
| 2 | 7 sites share Paulding village centroid GPS (41.137, -84.573) | MEDIUM | Batch: precision GPS acquisition |
| 3 | 4 sites share repeated coordinates (Canal Park / Cecil Bridge) | MEDIUM | Batch: precision GPS acquisition |
| 4 | 0 trail_parents for 5 MC trails | MEDIUM | Batch: add trail_parents per §4 above |
| 5 | Forrest Woods expansion parcels (~255ac, 4 parcels, GAP2) not cataloged | HIGH | Supplemental T7 discovery; cross-county check vs Defiance |
| 6 | Antwerp Community Park (5ac) not cataloged | MEDIUM | Supplemental T6 discovery |
| 7 | UAW Park (37ac) county unclear; not cataloged if Paulding | MEDIUM | Supplemental discovery; verify county |
| 8 | 8 village parks not cataloged (~68ac total) | MEDIUM | Supplemental T6 discovery |

---

## 8. Batch Phase Actions

- [ ] Reparent OH-PAU-AP-0001 to OH-MC-T-0216 (type Trail)
- [ ] Acquire precision GPS for 11 sites using placeholder coordinates
- [ ] Add trail_parents for 5 MC trails in Paulding
- [ ] Supplemental discovery: Forrest Woods expansion parcels (T7; cross-county verify)
- [ ] Supplemental discovery: Antwerp Community Park (T6)
- [ ] Supplemental discovery: UAW Park — verify Paulding vs Defiance County
- [ ] Supplemental discovery: Cecil CP, Charloe CP, Melrose Town Park, Paulding Athletic Fields, Moats Park, School Park, Oakwood Ball Field, Lafountain Park (T6)
