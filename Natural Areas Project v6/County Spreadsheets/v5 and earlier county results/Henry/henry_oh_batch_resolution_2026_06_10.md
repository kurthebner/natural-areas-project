# Henry County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_HEN_OTT_WAY_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: FAIL

---

## 1. AP Reparenting and S-0018 Retirement

**Problem:** OH-HEN-S-0018 (Mary Jane Thurston State Park, Henry-only 105ac Active) is a
duplicate of OH-MC-S-0030 (MJTP, Henry;Wood, cross-county). AP-0001 and AP-0002 both
referenced S-0018.

**Actions:**
- Updated `parent_entity_id` for AP-0001 (Boat Launch Ramp) and AP-0002 (Marina) → `OH-MC-S-0030`
- Set `status='Retired'` on OH-HEN-S-0018

---

## 2. Trail Parents Added (4 entries)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-HEN-T-0001 Blue Trail | OH-MC-S-0030 Mary Jane Thurston SP | MJTP is cross-county |
| OH-HEN-T-0003 Orange Trail | OH-MC-S-0030 | |
| OH-HEN-T-0004 Storybook Trail | OH-MC-S-0030 | |
| OH-HEN-T-0007 Yellow Trail | OH-MC-S-0030 | |

---

## 3. Supplemental Sites (3 new, S-0032–S-0034)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-HEN-S-0032 | Napoleon Veterans Memorial Park | 1 | Napoleon | 41.386300, -84.121900 |
| OH-HEN-S-0033 | Cherry Street Park | 11 | Liberty | 41.445939, -84.014383 |
| OH-HEN-S-0034 | Dry Creek Wildlife Area | 2 | Washington | 41.420271, -83.971486 |

**Notes:**
- S-0032 (Napoleon VMP): distinct from S-0029 (Liberty Center VMP). PAD-US Napoleon Township.
- S-0033 (Cherry Street Park): Liberty Township, Henry County. Likely Liberty Center village.
  PAD-US 11ac City Land confirmed Henry/Liberty via TIGER FIPS 069.
- S-0034 (Dry Creek WA): ODNR, GAP2. Washington Township. Distinct from S-0023 North
  Turkeyfoot WA (458ac same township).

---

## 4. QR Gap Analysis — False Positives

**WPA 28 and WPA 29:** Already in DB as S-0014 (Henry County WA 2, Flatrock Twp) and S-0015
(Henry County WA 3, Monroe Twp) — GPS coordinates match exactly. Not new gaps.

**Camp Libbey (321ac, NGO):** QR identified as Henry T7 gap. TIGER spatial audit places the
PAD-US centroid (41.287°N, -84.275°W) in **Defiance County** Richland Township (FIPS 039),
NOT Henry County. Camp Libbey is not a Henry County entity. MRQ-flagged for Defiance T7
supplemental discovery. Not yet in Defiance DB.

**Napoleon T6 gaps (QR list):** Riverside Park 32ac, Woodland Park 43ac, Diehl Park 40ac,
VFW 3360 Park 24ac, Second Ward Park 1ac, South Street Park 1ac, Legion Field 2ac — all
PAD-US matches for these names fall in Defiance County or Fulton County (Archbold), not
Henry/Napoleon. These parks appear to be QR items from municipal website research that either:
(a) are in the DB under different names, or (b) are not in PAD-US. Most Napoleon city parks
confirmed already in DB (S-0005/0008/0020/0024/0025/0027/0028/0031 etc). Napoleon VMP S-0032
inserted. Remaining QR-listed parks require municipal website verification.

---

## 5. MRQ Entries (2)

1. Camp Libbey → Defiance County attribution; stage for Defiance T7 run
2. Napoleon T6 parks QR false positives → document attribution findings

---

## 6. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites (HEN) | 30 (excl. retired) | 33 |
| Sites (Henry-touching incl. MC) | 33 | 36 |
| Trail parents (HEN) | 0 | 4 |
| APs reparented | 0 | 2 |
| Sites retired | 0 | 1 (S-0018) |

---

## 7. Open Items

- Cherry Street Park (S-0033): municipality confirm — Liberty Center or unincorporated Liberty Twp?
- Napoleon T6 parks from QR: verify via City of Napoleon parks page — may exist but not in PAD-US
- Camp Libbey: stage for Defiance County T7 batch (Defiance Co, 321ac NGO, GAP4)
- Henry County WA 1 (S-0013, Richfield Twp): acres blank — fill from ODNR
- S-0011 Henry County Fairgrounds: scope review per QR — confirm this is in-scope as natural area
