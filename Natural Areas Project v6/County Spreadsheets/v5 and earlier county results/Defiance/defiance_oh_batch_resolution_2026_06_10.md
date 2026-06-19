# Defiance County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_DEF_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: FAIL

---

## 1. Supplemental T2 — ODNR Wildlife Areas (3 new sites, S-0033–S-0035)

| Site ID | Name | Acres | Township | GPS |
|---------|------|-------|----------|-----|
| OH-DEF-S-0033 | Fish Creek Wildlife Area | 156 | St. Joseph Twp | 41.465757, -84.782207 |
| OH-DEF-S-0034 | Flatrock Creek Wildlife Area | 4 | Auglaize Twp | 41.171319, -84.455388 |
| OH-DEF-S-0035 | Six Mile Wildlife Area | 4 | Auglaize Twp | 41.207462, -84.457776 |

All confirmed Defiance County via centroid + township lookup (PAD-US GDB centroid transform → TIGER/Line MCD lookup).

---

## 2. Supplemental T7 — Fish Creek Ecosystem Fee Parcels (2 new sites, S-0036–S-0037)

| Site ID | Name | Acres | GAP | Township | GPS |
|---------|------|-------|-----|----------|-----|
| OH-DEF-S-0036 | Fish Creek Ecosystem Fee (Parcel A) | 23 | GAP1 | St. Joseph Twp | 41.474302, -84.761131 |
| OH-DEF-S-0037 | Fish Creek Ecosystem Fee (Parcel B) | 101 | GAP1 | St. Joseph Twp | 41.471467, -84.771814 |

Ownership: NGO (PAD-US). Governing organization unverified — governance left blank. Both MRQ-flagged for org identification.

---

## 3. Supplemental T6 — Municipal/County Parks (3 new sites, S-0038–S-0040)

| Site ID | Name | Acres | Municipality | GPS |
|---------|------|-------|--------------|-----|
| OH-DEF-S-0038 | UAW Park | 37 | Defiance | 41.278130, -84.402375 |
| OH-DEF-S-0039 | Hicksville Recreation Park | 67 | Hicksville | 41.296615, -84.772415 |
| OH-DEF-S-0040 | Old Fort Defiance Park | 1 | Defiance | 41.287533, -84.357142 |

---

## 4. Trail Parent Added (1 entry)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-DEF-T-0007 Hicksville Nature Trail | OH-DEF-S-0039 Hicksville Recreation Park | Trail located within 67ac city recreation park complex |

---

## 5. Forrest Woods — Bbox False Positives (Not Defiance Gaps)

QR listed "Forrest Woods NP + 4 expansion parcels (~255ac)" as Defiance T7 gap. Township lookup confirms all six Forrest Woods PAD-US parcels (main preserve 344ac, Forder Bridge 52ac, Harper-Forrest 77ac, Land Acquisition 78ac, Rooks-Harper 60ac, Shaffer 40ac) have centroids in **Crane Township = Paulding County**. All already in DB as OH-PAU-S-0002 and OH-PAU-S-0031–0034. Not Defiance gaps.

---

## 6. Williams County Bbox Bleeds (3 entities excluded)

| PAD-US Record | Acres | Reason |
|---|---|---|
| Goldie Newman Wildlife Area | 80 | Centroid 41.52N — north of Defiance Co. line; Jefferson Twp = Williams County |
| Lick Creek Preserve | 51 | Municipality = Bryan (Williams County seat) |
| Recreation Park | 76 | Municipality = Bryan (Williams County seat) |

All three MRQ-flagged for Williams County supplemental discovery.

---

## 7. MRQ Entries (5 total)

1. `WILLIAMS-GOLDIE-NEWMAN` — Goldie Newman WA, stage for Williams County T2
2. `WILLIAMS-LICK-CREEK` — Lick Creek Preserve, stage for Williams County T6
3. `WILLIAMS-RECREATION-PARK` — Recreation Park 76ac, stage for Williams County T6
4. `OH-DEF-S-0036` — Fish Creek Ecosystem Fee Parcel A, verify managing NGO
5. `OH-DEF-S-0037` — Fish Creek Ecosystem Fee Parcel B, verify managing NGO

---

## 8. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites | 32 | 40 |
| Trails | 5 | 5 |
| Trail parents | 4 | 5 |
| Access Points | 6 | 6 |

---

## 9. Open Items

- Fish Creek Ecosystem Fee parcels (S-0036/S-0037): identify governing NGO and update governance field
- Oxbow Lake parcel (S-0002): open governance flag from QR — verify managing entity
- S-0016 Pontiac Metro Park: open governance flag from QR
- Goldie Newman WA / Lick Creek Preserve / Recreation Park 76ac: stage for Williams County run
