# Sandusky County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 134 | OH-SAN-S-0001 – OH-SAN-S-0142 (gaps at 3–5, 79–81, 105, 107) |
| Trails | 4 | OH-MC-T-0110, OH-SAN-T-0002/0003/0004 |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 6 active | OH-SAN-AP-0001/0004/0005/0006/0008/0009; APs 0002/0003/0007 held |
| Held Entities | 7 | 4 sites + 3 APs (see §4) |

**Run metadata:** `sandusky_ohio_2026_05_21` — input=155, normalized=144, held=11 (7 remain in held_entities; 4 resolved since run)

---

## 2. FK Integrity

### Fixes applied this session

| AP | Old value | New value | Issue |
|---|---|---|---|
| OH-SAN-AP-0001 | OH-SAN-S-002 | OH-SAN-S-0002 | Zero-padding |
| OH-SAN-AP-0006 | OH-SAN-S-028 | OH-SAN-S-0028 | Zero-padding |
| OH-SAN-AP-0008 | '' (empty string) | NULL | No parent — empty string corrected to NULL |
| OH-SAN-AP-0009 | '' (empty string) | NULL | No parent — empty string corrected to NULL |

**AP-0008 (Sand Docks) and AP-0009 (Miles Newton Bridge Fishing Access)** are City of Fremont-managed river access points with no site parent in the DB — intentionally parentless per identity_notes. Empty-string parent fields corrected to NULL for data cleanliness. Both are legitimately parentless; no parent entity needed.

---

## 3. Sequence Gaps

Expected gaps at S-0003/0004/0005 (held entities) and S-0105 (held). Unexplained gaps:

- **OH-SAN-S-0079, 0080, 0081** — not in DB, not in held_entities. Sequence follows S-0078 (Robert Peters Athletic Field, Bellevue). Likely Bellevue city entities that were reclassified to Erie or Huron County during resolution (Bellevue straddles three county lines).
- **OH-SAN-S-0107** — not in DB, not in held_entities. Sequence is between WR Hunt Club (S-0106) and County Home Cemetery (S-0108). Cause unknown.

These gaps should be documented in the county session log if not already explained there.

---

## 4. Held Entities

| Record ID | Name | Hold Reason | Partner County |
|---|---|---|---|
| OH-SAN-S-0003 | Resthaven Wildlife Area | cross_county_held | Erie (primary) |
| OH-SAN-S-0004 | Willow Point Wildlife Area | cross_county_held | Erie (primary) |
| OH-SAN-S-0005 | Sandusky State Scenic River | cross_county_held | Wyandot (primary) |
| OH-SAN-S-0105 | Sugar Creek Golf Course & Driving Range | cross_county_held | Ottawa (primary) |
| OH-SAN-AP-0002 | Resthaven WA — Pond 8 Fishing Pier | cross_county_held | Erie (primary) |
| OH-SAN-AP-0003 | Resthaven WA — Northeast Boat Ramp | cross_county_held | Erie (primary) |
| OH-SAN-AP-0007 | Darr-Root Fishing Access | parent_held | Parent = Sandusky SSR (S-0005) |

All holds are valid. Resthaven WA (S-0003) and its two APs are held pending the Erie County pipeline run. **Note:** Resthaven WA appeared as a ~2216ac unmatched gap in the Ottawa County PAD-US review — that review should be updated to note it is already in the pipeline held under OH-SAN-S-0003, pending Erie County as primary.

Darr-Root Fishing Access (AP-0007) is an ODNR-managed access on the Sandusky River; hold will resolve when Sandusky State Scenic River (S-0005) is released in the Wyandot County run.

OH-SAN-S-0105 Sugar Creek Golf Course was held as Ottawa County primary; Ottawa pipeline has since run. Follow up: confirm whether Ottawa run upserted this entity or whether it needs manual resolution.

---

## 5. GPS Status

All 134 active sites have GPS values (0 missing). GPS Gate: passed.

Minor concern: OH-SAN-S-0024 (White Star Quarry) shares exact GPS with OH-SAN-S-0023 (White Star Park) — 41.374264, -83.320385. The quarry is within the park grounds so the shared coordinate may be intentional; worth confirming in precision GPS pass.

---

## 6. Trail Parents

| Trail | Trail_parents | Status |
|---|---|---|
| OH-SAN-T-0002 White Star Quarry Loop Trail | 1 (→ OH-SAN-S-0024) | ✓ |
| OH-SAN-T-0003 Waggoner's Run Mountain Bike Trail | 1 (→ OH-SAN-S-0023) | ✓ |
| OH-SAN-T-0004 Silver Rock Park Walking Trail | 0 | Missing — add → OH-SAN-S-0093 |
| OH-MC-T-0110 North Coast Inland Trail | 0 Sandusky entries | Missing — add Sandusky site parents |

Batch fix for T-0004: `INSERT INTO trail_parents VALUES ('OH-SAN-T-0004', 'OH-SAN-S-0093')`.
NCIT trail_parents for Sandusky access points (AP-0004 and AP-0005 already reference OH-MC-T-0110 as parent) — trail_parents linking NCIT to Tea Kaufman Homestead (S-0021) and any other Sandusky sites the trail traverses needed.

---

## 7. PAD-US Spatial Audit

**Bbox:** Sandusky County bounding box. 92 PAD-US fee records in bbox; 19 matched (≥80); 40 unmatched; 33 skipped.

### 7a. Wrong matches

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Genoa Recreation Complex (39ac, City) | OH-SAN-S-0072 Magdalyn Aigler Recreation Complex | 86 | Wrong — Genoa is in Ottawa County (bbox bleed); Magdalyn Aigler correctly cataloged |
| Sugar Creek Wildlife Area (127ac, ODNR, GAP2) | OH-SAN-S-0002 Pickerel Creek Wildlife Area | 86 | Wrong — Sugar Creek WA is OH-SEN-S-0003 in Seneca County (bbox bleed) |
| Sandusky Wolf Creek SR (84ac, ODNR) | OH-SAN-S-0028 Wolf Creek Park | 80 | Borderline — scenic river corridor vs park; monitor |

### 7b. False negatives (in DB, score below threshold)

| PAD-US Record | DB Entity | Score | Note |
|---|---|---|---|
| Roger Young Memorial Park (39ac) | OH-SAN-S-0070 Rodger W. Young Park | 71 | Spelling variant "Roger"/"Rodger" + "Memorial" absent from DB name; NOT a gap |
| North Coast Inland Trail (124ac, County) | OH-MC-T-0110 | 50 | Trail corridor parcel; entity in DB as trail; NOT a gap |
| Darr-Root Fishing Access (34ac, ODNR) | OH-SAN-AP-0007 (held) | 41 | In pipeline, held pending parent resolution; NOT a gap |

### 7c. Bbox false positives in unmatched list

Ottawa County entities bleeding into Sandusky's bbox (Sandusky-Ottawa county line):
- Ottawa National Wildlife Refuge ×2 (6,974ac + 7,542ac, USFWS, GAP2) — Ottawa County; massive parcels whose southern edge intersects Sandusky bbox
- Schedel Gardens and Arboretum (19ac, GAP2) — Elmore, Ottawa County
- Oak Harbor Station Interurban Overlook and Boat Launch (0ac) — Ottawa County
- Village of Oak Harbor parcel (1ac) — Ottawa County
- Adolphus Kraemer Park (0ac) — Ottawa County (Port Clinton area)

Seneca County bleed (Sandusky-Seneca county line):
- Sugar Creek Wildlife Area (127ac) — OH-SEN-S-0003, already matched wrong (see §7a)

### 7d. Genuine Sandusky County gaps

**T2 — State / ODNR (significant):**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Green Springs State Forest | 120 | 2 | ODNR state forest near Green Springs village; not in DB |
| Knobbys Prairie Wildlife Area | 48 | 2 | ODNR wildlife area; not in DB |
| Little Portage Wildlife Area | 358 | 2 | Restricted access; ODNR; not in DB |
| Sandusky Abbotts Bridge SR | 22 | — | ODNR scenic river parcel; restricted access |
| Portage River Fishing Access | 10 | 4 | ODNR; verify county (Sandusky vs Ottawa) |
| Lover's Portage River Access | 1 | 4 | ODNR; verify county |

**T2 — Wildlife Production Areas not individually cataloged:**

OH-SAN-S-0008 "Sandusky County Wildlife Areas (ODNR numbered tracts)" is a catch-all entity covering an unknown number of ODNR WPAs. The description notes awareness of "up to 7 numbered" tracts. PAD-US shows 12 WPA records in the Sandusky bbox (WPAs 14, 18, 30, 31, 47, 50, 59, 62, 63, 64, 65, plus one with a typo "Wildlife Producton Area"). Total: ~661ac, all GAP2.

Not all 12 are necessarily in Sandusky County — some may be Ottawa or Seneca County WPAs bleeding into the bbox. However, those present in Sandusky County should eventually be individually cataloged to replace the catch-all S-0008. Each WPA warrants its own site record with ODNR as governance, actual acreage, and WPA number in the name.

**T3 — District:**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Bradner Preserve | 124 | 2 | County Land; significant nature preserve; not in DB |

**T6 — Municipal:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Alumni Park | 12 | City | Fremont area; not in DB |
| Harmon Field | 4 | City | Not in DB |
| Limerick Park | 14 | City | Not in DB |
| Portage Park (record 1) | 23 | City | Not in DB; verify municipality |
| Portage Park (record 2) | 12 | City | Not in DB; may be different municipality than above |
| Triangle Park | 1 | City | Not in DB |
| Fremont Community Recreation Complex | 27 | City | Not in DB |
| Portage Trail Park | 17 | City | Not in DB |
| Armory Park | 0 | City | Not in DB; 0ac in PAD-US likely data gap |
| Veteran's Memorial Park | 20 | City | Not in DB (distinct from existing Sandusky County memorial parks) |
| Countryside Park | 5 | County | Not in DB |
| Stephenson Park | 1 | County | Not in DB |

### 7e. Matched — data quality flags

| PAD-US Record | DB Entity | Issue |
|---|---|---|
| Pickerel Creek Wildlife Area (3,148ac) | OH-SAN-S-0002 | DB has no acreage recorded; add 3,148ac |
| Blue Heron Reserve (158ac) | OH-SAN-S-0009 | DB has no acreage; add 158ac |
| Conner Park (18ac) | OH-SAN-S-0029 | DB has no acreage; add 18ac |
| White Star Park (666ac) | OH-SAN-S-0023 | DB has 797ac; PAD-US 666ac — discrepancy; verify |
| Park / Spiegel Grove SP (765ac) | OH-SAN-S-0001 | DB has no acreage; PAD-US name is just "Park" — confirm Spiegel Grove total acreage |

---

## 8. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | 4 AP FK fixes applied | FIXED | Done this session |
| 2 | S-0079/80/81, S-0107 unexplained sequence gaps | MEDIUM | Document in session log; likely Bellevue reclassification |
| 3 | OH-SAN-S-0105 Sugar Creek GC held (Ottawa primary) — Ottawa has since run | MEDIUM | Verify Ottawa DB; manual resolution if needed |
| 4 | Missing trail_parents: T-0004 and NCIT | MEDIUM | Batch: add trail_parents |
| 5 | 12 WPAs not individually cataloged (~661ac, ODNR GAP2) | HIGH | Supplemental T2 discovery; replace catch-all S-0008 |
| 6 | Green Springs State Forest (120ac, GAP2) not cataloged | HIGH | Supplemental T2 discovery |
| 7 | Little Portage Wildlife Area (358ac, GAP2) not cataloged | HIGH | Supplemental T2 discovery |
| 8 | Knobbys Prairie Wildlife Area (48ac, GAP2) not cataloged | MEDIUM | Supplemental T2 discovery |
| 9 | Bradner Preserve (124ac, GAP2, County) not cataloged | MEDIUM | Supplemental T3 discovery |
| 10 | 12 municipal/county parks not cataloged (~134ac) | MEDIUM | Supplemental T6 discovery |
| 11 | Resthaven WA noted as Ottawa gap — actually held in pipeline | NOTE | Update Ottawa review; resolve when Erie runs |
| 12 | Missing acreage on Pickerel Creek WA, Blue Heron, Conner Park, Spiegel Grove | LOW | Batch: update acres from PAD-US values |
| 13 | White Star Park acreage discrepancy (DB 797ac vs PAD-US 666ac) | LOW | Verify against ODNR source |
| 14 | Roger Young Memorial Park: DB name "Rodger W. Young" — consider alias or name correction | LOW | Verify official park name |

---

## 9. Batch Phase Actions

- [ ] Add trail_parent: OH-SAN-T-0004 → OH-SAN-S-0093 (Silver Rock Park)
- [ ] Add trail_parents for OH-MC-T-0110 → Sandusky sites (Tea Kaufman Homestead S-0021, others)
- [ ] Resolve OH-SAN-S-0105 Sugar Creek GC: check Ottawa DB; manual release or merge
- [ ] Investigate S-0079/0080/0081/0107 sequence gaps; document explanation
- [ ] Update Ottawa review: Resthaven WA is already in pipeline (OH-SAN-S-0003, held for Erie run)
- [ ] Supplemental T2 discovery: Green Springs State Forest, Knobbys Prairie WA, Little Portage WA, Sandusky WPAs (individually), Portage River Fishing Access, Lover's Portage River Access
- [ ] Supplemental T3 discovery: Bradner Preserve
- [ ] Supplemental T6 discovery: Alumni Park, Harmon Field, Limerick Park, Portage Parks ×2, Triangle Park, Fremont Community Recreation Complex, Portage Trail Park, Armory Park, Veteran's Memorial Park, Countryside Park, Stephenson Park
- [ ] Update acres on: Pickerel Creek WA (3,148ac), Blue Heron Reserve (158ac), Conner Park (18ac); verify Spiegel Grove and White Star Park acreage discrepancies
