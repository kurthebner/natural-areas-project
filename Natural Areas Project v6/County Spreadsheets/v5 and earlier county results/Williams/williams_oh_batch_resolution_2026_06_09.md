# Williams County — Batch Resolution Log
**Date:** 2026-06-09
**Run ID:** `BATCH_WIL_2026-06-09`
**Source:** Quality review 2026-06-08; QR status: PARTIAL FAIL

---

## GPS Acquisitions Applied (27 sites)

All updates applied to `natural_areas_v6.db`. PAD-US 4.0 GDB centroids used as primary source (polygon-based, authoritative over Census/Nominatim for parks). Census geocoder used for sites with confirmed street addresses. Nominatim used where PAD-US had no coverage.

| Site ID | Name | New GPS | Source |
|---------|------|---------|--------|
| OH-WIL-S-0002 | Fish Creek Wildlife Area | 41.465757, -84.782207 | PAD-US 4.0 GDB |
| OH-WIL-S-0003 | Parkersburg Wildlife Area | 41.539625, -84.521906 | PAD-US 4.0 GDB |
| OH-WIL-S-0006 | Mud Lake Bog State Nature Preserve | 41.646924, -84.766219 | PAD-US 4.0 GDB |
| OH-WIL-S-0008 | George Bible Park | 41.555703, -84.577908 | PAD-US 4.0 GDB |
| OH-WIL-S-0009 | Goldie Newman Park/Wildlife Area | 41.517457, -84.549559 | PAD-US 4.0 GDB |
| OH-WIL-S-0010 | Springfield Township Park | 41.506024, -84.412247 | PAD-US 4.0 GDB |
| OH-WIL-S-0011 | Recreation Park | 41.467077, -84.569017 | PAD-US 4.0 GDB |
| OH-WIL-S-0012 | East End Park and Pool | 41.473947, -84.527224 | PAD-US 4.0 GDB |
| OH-WIL-S-0013 | Garver Park | 41.472511, -84.558644 | PAD-US 4.0 GDB |
| OH-WIL-S-0014 | Moore Park and Pool | 41.469958, -84.566832 | PAD-US 4.0 GDB |
| OH-WIL-S-0015 | Maple Grove Park | 41.461143, -84.540373 | PAD-US 4.0 GDB |
| OH-WIL-S-0016 | Roseland Park | 41.464734, -84.546569 | PAD-US 4.0 GDB |
| OH-WIL-S-0017 | Fountain City Park | 41.467676, -84.538018 | PAD-US 4.0 GDB |
| OH-WIL-S-0018 | Hitt Park | 41.482728, -84.548986 | PAD-US 4.0 GDB |
| OH-WIL-S-0019 | Mattie Marsh Park | 41.478329, -84.545488 | PAD-US 4.0 GDB (note: PAD-US spells "Maddie" — verify official spelling) |
| OH-WIL-S-0020 | Israel Gardens Butterfly Park | 41.457334, -84.552565 | PAD-US 4.0 GDB (listed as "Butterfly Park") |
| OH-WIL-S-0021 | Central Park | 41.469687, -84.556124 | PAD-US 4.0 GDB |
| OH-WIL-S-0022 | Montpelier Municipal Park | 41.573249, -84.605974 | Nominatim |
| OH-WIL-S-0023 | Main Street Park | 41.586549, -84.604544 | Census geocoder — 309 E Main St |
| OH-WIL-S-0024 | Robert A. Storrer Municipal Park | 41.584570, -84.606983 | Census geocoder — 300 S Platt St |
| OH-WIL-S-0025 | Founders Park | 41.586405, -84.611168 | Census geocoder — 400 W Main St |
| OH-WIL-S-0026 | Miller Park | 41.449362, -84.756023 | Census geocoder — 300 Miller Park Dr |
| OH-WIL-S-0031 | Edon Community Park | 41.560580, -84.772366 | Nominatim |
| OH-WIL-S-0036 | Crommer Park | 41.681107, -84.556287 | Nominatim |
| OH-WIL-S-0039 | West Unity Memorial Park | 41.591452, -84.432192 | PAD-US 4.0 GDB |
| OH-WIL-S-0041 | St. Joseph River Confluence Preserve | 41.647601, -84.567885 | PAD-US 4.0 GDB (St Joseph Confluence) |
| OH-WIL-S-0046 | Davis Woods | 41.520104, -84.550573 | Nominatim |

---

## GPS Still Low-Precision — manual_review_queue

15 sites remain at ≤3 decimal place precision. Not resolvable via PAD-US/Census/Nominatim. Added to `manual_review_queue` with specific research directions.

| Site ID | Name | Current GPS | Issue |
|---------|------|-------------|-------|
| OH-WIL-S-0027 | Gerhart Park | 41.45,-84.748 (2dp) | Village of Edgerton contact needed |
| OH-WIL-S-0028 | Downtown Park | 41.449,-84.747 (3dp) | Village of Edgerton contact |
| OH-WIL-S-0029 | Puppy Pound Park | 41.451,-84.749 (3dp) | Village of Edgerton contact |
| OH-WIL-S-0030 | Walz Park | 41.662,-84.768 (3dp) | Village of Edon contact |
| OH-WIL-S-0032 | Harold C Baker Park | 41.663,-84.766 (3dp) | Village of Edon contact |
| OH-WIL-S-0033 | Leanne Field | 41.66,-84.769 (2dp) | Village of Edon contact |
| OH-WIL-S-0034 | Beard Park | 41.681,-84.551 (3dp) | Village of Pioneer contact |
| OH-WIL-S-0035 | Cannonball Park | 41.681,-84.551 (3dp) | Shared coord with S-0034; needs individual GPS |
| OH-WIL-S-0037 | Fred Wyman Field | 41.68,-84.55 (2dp) | Village of Pioneer contact |
| OH-WIL-S-0038 | Pioneer Memorial Park | 41.683,-84.553 (3dp) | Village of Pioneer contact |
| OH-WIL-S-0040 | Alvordton Community Park | 41.659,-84.443 (3dp) | Village of Alvordton contact |
| OH-WIL-S-0042 | St. Joseph River Floodplain Preserve | 41.558,-84.507 (3dp) | Verify identity vs S-0041; may be same entity |
| OH-WIL-S-0043 | Pioneer Scout Reservation | — (none) | 7371 CR S, Pioneer — Census/Nominatim failed; BSA council contact |
| OH-WIL-S-0044 | Lake Seneca Beach | 41.629,-84.601 (3dp) | Lake Seneca HOA or parcel lookup |
| OH-WIL-S-0045 | Memory Point Park | 41.63,-84.601 (2dp) | Lake Seneca parcel lookup |

---

## Trail Parents Added

| Trail | Parent Site | Notes |
|-------|-------------|-------|
| OH-WIL-T-0002 Iron Horse River Trail | OH-WIL-S-0024 Robert A. Storrer Municipal Park | Trail runs along St. Joseph River in Montpelier |
| OH-WIL-T-0002 Iron Horse River Trail | OH-WIL-S-0025 Founders Park | Explicitly named as trailhead access point in trail identity notes |
| OH-MC-T-0002 Wabash Cannonball Trail | OH-WIL-S-0039 West Unity Memorial Park | Trail passes through West Unity; AP-0001/0002 access this trail |

**Note:** Quality review incorrectly identified Iron Horse River Trail parents as S-0026/0027/0028 (Edgerton parks). Trail identity notes confirm governance = Montpelier Parks & Recreation; trail is in Montpelier, not Edgerton or Bryan.

**MC trail parents still needed (manual_review_queue):** OH-MC-T-0001, OH-MC-T-0219, OH-MC-T-0221 — need route maps to identify WIL site parents.

---

## Supplemental Sites Added

| Site ID | Name | Tier | GPS | Source | Notes |
|---------|------|------|-----|--------|-------|
| OH-WIL-S-0047 | Williams County Conservation League Area | T4 | 41.560900,-84.576429 | PAD-US 4.0 GDB | 69ac; County Land near Bryan |
| OH-WIL-S-0048 | Montpelier Memorial Park | T6 | 41.573757,-84.605294 | PAD-US 4.0 GDB | 27ac; was wrongly matched to Pioneer Memorial Park in QR |
| OH-WIL-S-0049 | Superior Athletic Complex | T6 | 41.559222,-84.616432 | PAD-US 4.0 GDB | 25ac; Bryan |
| OH-WIL-S-0050 | Lick Creek Preserve | T6 | 41.470798,-84.578933 | PAD-US 4.0 GDB | 51ac; Bryan; PAD-US gap not in prior discovery |

**Note on Williams County Conservation League (S-0047):** QR flagged for T3 vs T7 determination. PAD-US lists as "County Land" — assigning T4 (County) as governance unit. If org structure reveals it is an independent conservancy with legal conservation mandate, reclassify to T7.

---

## Confirmed Bbox False Positives (Not Williams County Gaps)

- **Ney Community Park** (PAD-US 10ac, City Land, centroid 41.3797,-84.5251): Township lookup confirmed Defiance County Washington Township. Catalog under Defiance County T6 when processed.
- **Harrison Lake State Park** (245ac ODNR): Already in DB as Fulton County OH-FUL-S-0002.
- **Goll Woods Dedicated Nature Preserve**: Already in DB as Fulton County OH-FUL-S-0001.
- **Hillcrest Golf Course** (41.018,-83.659), **Riverside Golf Course** (40.650,-82.794): Centroids in unrelated counties — clear bbox bleed artifacts.

---

## Acreage Discrepancies — manual_review_queue (No DB Change)

| Site ID | Name | DB Acres | PAD-US Acres | Action |
|---------|------|----------|--------------|--------|
| OH-WIL-S-0007 | Opdycke Park | 50 | 64 | Verify vs Williams County Parks |
| OH-WIL-S-0008 | George Bible Park | 95.5 | 60 | DB higher; may include adjacent parcels |
| OH-WIL-S-0009 | Goldie Newman Park/WA | 50 | 80 | Verify vs ODNR DOW |

---

## Open Items

- GPS precision: 15 sites still at ≤3dp (see table above)
- MC trail parents: T-0001 Maumee Water Trail, T-0219 Buckeye Trail, T-0221 Wabash North Fork — in manual_review_queue
- S-0042 identity: verify vs S-0041 (St. Joseph River Floodplain vs Confluence)
- Williams County Conservation League: confirm T4 vs T7 tier assignment
- Acreage verification: S-0007, S-0008, S-0009
