# Williams County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 46 | OH-WIL-S-0001 – OH-WIL-S-0046 (no gaps) |
| Trails | 1 WIL + 4 MC | OH-WIL-T-0002 (Iron Horse River Trail); OH-MC-T-0001/0002/0219/0221 include Williams |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 3 | OH-WIL-AP-0001/0002/0003 |
| Held Entities | 1 | OH-WIL-T-0001 (North Country NST, cross_county_held) |

**Run metadata:** `williams_oh_2026_04_12` — input=52, normalized=50, held=2

Notes: "46 sites, 1 trails, 3 APs, 2 held." The second held entity (beyond T-0001 which remains in held_entities) was subsequently resolved or removed — current held count is 1.

---

## 2. FK Integrity

No fixes required. All AP parent FKs are valid:

| AP | Name | Parent | Status |
|---|---|---|---|
| OH-WIL-AP-0001 | Dreamers Meadow | OH-MC-T-0002 (Trail) | ✓ |
| OH-WIL-AP-0002 | West Unity Trail Head | OH-MC-T-0002 (Trail) | ✓ |
| OH-WIL-AP-0003 | Knight's Landing | NULL | Intentional — watercraft access point, no parent site in DB |

No zero-padding errors or ghost FK references detected.

---

## 3. Sequence Gaps

None. OH-WIL-S-0001–0046 are all present. OH-WIL-T-0001 is held (cross_county_held); T-0002 is the only active Williams trail. No unexplained gaps.

---

## 4. GPS Status

All 46 active sites have GPS values (0 missing). GPS Gate: passed.

**SYSTEMIC data quality issue — low-precision coordinates.** 42 of 46 sites have GPS rounded to 3 decimal places or fewer, indicating centroid approximations rather than precision coordinates. Only 4 sites have high-precision GPS:

- OH-WIL-S-0001 Lake La Su An Wildlife Area (6 decimal places) ✓
- OH-WIL-S-0004 St. Joseph River Wildlife Area (6 decimal places) ✓
- OH-WIL-S-0005 Nettle Lake Wildlife Area (6 decimal places) ✓
- OH-WIL-S-0007 Opdycke Park (6 decimal places) ✓

The remaining 42 sites — comprising essentially all municipal parks and smaller preserves — need precision GPS acquisition in the batch phase. This is the most significant data quality issue in this county.

---

## 5. Trail Parents

No trail_parents entries exist for any of the 5 trails that pass through Williams County:

| Trail | Status | Notes |
|---|---|---|
| OH-WIL-T-0002 Iron Horse River Trail | 0 parents | Rail trail along St. Joseph River in Bryan; batch: add → Bryan riverside parks (S-0026/0027/0028) |
| OH-MC-T-0001 Maumee River Water Trail | 0 Williams parents | Maumee headwaters area; identify WIL sites on corridor |
| OH-MC-T-0002 Wabash Cannonball Trail | 0 Williams parents | AP-0001/0002 access this trail; add trail_parents linking to relevant WIL sites |
| OH-MC-T-0219 Buckeye Trail — Defiance Section | 0 Williams parents | Passes through Williams County; identify WIL site parents |
| OH-MC-T-0221 Wabash Cannonball Trail (North Fork) | 0 Williams parents | North Fork corridor; identify WIL site parents |

**Iron Horse River Trail parent recommendation:** The trail follows the St. Joseph River through Bryan. Primary parent candidates: OH-WIL-S-0027 (Gerhart Park, 41.45, -84.748), OH-WIL-S-0028 (Downtown Park), or OH-WIL-S-0026 (Miller Park). Confirm correct riverside park association during batch phase.

---

## 6. Held Entities

| Record ID | Name | Hold Reason | Hold Detail |
|---|---|---|---|
| OH-WIL-T-0001 | North Country National Scenic Trail | cross_county_held | Multi-county; partner counties: Fulton, Henry, Lucas, Williams |

Hold is valid. Will resolve when all partner county pipeline runs complete (Fulton ✓, Henry ✓, Lucas ✓ — pending final cross-county resolution pass).

---

## 7. PAD-US Spatial Audit

**Bbox:** Williams County bounding box. 20 PAD-US fee records in bbox; 10 matched (≥80); 3 unmatched; 7 skipped.

### 7a. Wrong match

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Montpelier Memorial Park (27ac, City) | OH-WIL-S-0038 Pioneer Memorial Park | 84 | Wrong — "Memorial Park" tokens drove match; Pioneer is in Pioneer, OH; Montpelier Memorial Park is in Montpelier, OH. Genuine gap (see §7d). |

### 7b. Bbox false positives in unmatched list

The eastern edge of Williams County's bbox overlaps Fulton County. Two significant unmatched records are Fulton County entities, not Williams gaps:

- **Harrison Lake State Park** (245ac, ODNR) — OH-FUL-S-0002 (Fulton County, 41.64361, -84.37222). Confirmed in DB under Fulton. Not a Williams gap.
- **Goll Woods Dedicated Nature Preserve** (skipped as closed access) — OH-FUL-S-0001 (Fulton County, 41.554461, -84.36137). Confirmed in DB under Fulton. Not a Williams gap.

### 7c. Skipped — notes

- **Mud Lake Bog Dedicated Nature Preserve** (closed access): in DB as OH-WIL-S-0006. Correct — skipped because it's restricted access but already cataloged. Not a gap.
- **St Joseph Confluence** (closed access): relates to OH-WIL-S-0041/0042 (St. Joseph River Confluence/Floodplain Preserves). Already in DB. Not a gap.

### 7d. Genuine Williams County gaps

**T2 — State / ODNR:**

None. All ODNR wildlife areas matched correctly.

**T3/T4 — Conservation:**

| PAD-US Record | Acres | Owner | GAP | Notes |
|---|---|---|---|---|
| Williams County Conservation League | 69 | County Land | 4 | County conservation area; not in DB; verify whether T3 (conservation district) or T7 (land trust) based on org structure |

**T6 — Municipal:**

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Montpelier Memorial Park | 27 | City | Montpelier, OH; wrong match above; not in DB |
| Superior Athletic Complex | 25 | City | Bryan area; not in DB |

### 7e. Matched — acreage discrepancies

| PAD-US Record | PAD-US Acres | DB Acres | DB Entity | Note |
|---|---|---|---|---|
| George Bible Park | 60 | 95.5 | OH-WIL-S-0008 | DB higher; verify source — may include adjacent managed land |
| Goldie Newman Wildlife Area | 80 | 50 | OH-WIL-S-0009 | DB lower; PAD-US may include additional ODNR parcels |
| Opdycke Park | 64 | 50 | OH-WIL-S-0007 | DB lower; verify against county parks source |
| Nettle Lake Wildlife Area | 1 | 115 | OH-WIL-S-0005 | PAD-US fee parcel only 1ac; DB 115ac likely includes total managed area; not an error — known PAD-US limitation for multi-parcel WAs |
| Lake La Su An Wildlife Area | 2,592 | 2,616 | OH-WIL-S-0001 | Minor 24ac difference; within rounding |

---

## 8. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | 42 of 46 sites have low-precision GPS (3 decimal places or fewer) | HIGH | Batch: precision GPS acquisition for all 42 sites |
| 2 | 0 trail_parents for 5 trails (Iron Horse + 4 MC) | MEDIUM | Batch: add trail_parents; identify WIL site parents for each trail |
| 3 | Williams County Conservation League area (69ac) not cataloged | MEDIUM | Supplemental T3 or T7 discovery; verify org structure |
| 4 | Montpelier Memorial Park (27ac) not cataloged | MEDIUM | Supplemental T6 discovery |
| 5 | Superior Athletic Complex (25ac) not cataloged | MEDIUM | Supplemental T6 discovery |
| 6 | Iron Horse River Trail: parent site not confirmed | MEDIUM | Batch: confirm which Bryan park(s) are parents; add trail_parent |
| 7 | George Bible Park acreage (PAD-US 60ac vs DB 95.5ac) | LOW | Verify against county parks source |
| 8 | Goldie Newman WA acreage (PAD-US 80ac vs DB 50ac) | LOW | Verify against ODNR source |
| 9 | Opdycke Park acreage (PAD-US 64ac vs DB 50ac) | LOW | Verify against county parks source |

---

## 9. Batch Phase Actions

- [ ] Acquire precision GPS for 42 sites with low-precision coordinates (S-0002/0003/0006/0008–0046)
- [ ] Add trail_parent: OH-WIL-T-0002 Iron Horse River Trail → confirm Bryan riverside park (S-0026/0027/0028); add entry once confirmed
- [ ] Add trail_parents for OH-MC-T-0001, OH-MC-T-0002, OH-MC-T-0219, OH-MC-T-0221 → identify WIL site parents for each
- [ ] Supplemental discovery: Williams County Conservation League area (69ac) — verify T3 vs T7 tier
- [ ] Supplemental T6 discovery: Montpelier Memorial Park (27ac), Superior Athletic Complex (25ac)
- [ ] Verify acreages: George Bible Park (DB 95.5ac vs PAD-US 60ac), Goldie Newman WA (DB 50ac vs PAD-US 80ac), Opdycke Park (DB 50ac vs PAD-US 64ac)
