# Paulding County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_PAU_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PARTIAL FAIL

---

## 1. AP-0001 Reparent

| AP | Old parent | New parent | Note |
|----|-----------|-----------|------|
| OH-PAU-AP-0001 Canal Park Trailhead | OH-PAU-TN-0001 (Trail Network — does not exist) | OH-MC-T-0216 (Miami and Erie Canal Towpath) | TN-0001 never upserted; AP provides BT/NCT access at Canal Park which is on the M&E Towpath corridor |

---

## 2. GPS Precision Updates (11 sites)

| Site ID | Name | New GPS | Source |
|---------|------|---------|--------|
| OH-PAU-S-0002 | Forrest Woods State Nature Preserve | 41.231367, -84.665613 | PAD-US 4.0 GDB (344ac polygon centroid) |
| OH-PAU-S-0007 | New Rochester Park | 41.231994, -84.594397 | GNIS L1961036 |
| OH-PAU-S-0008 | Fort Brown Park | 41.111850, -84.417968 | Census geocoder — 9597 Road 171, Oakwood OH |
| OH-PAU-S-0010 | Black Swamp Nature Center | 41.127947, -84.590712 | PAD-US 4.0 GDB (33ac polygon centroid) |
| OH-PAU-S-0012 | Lela McGuire-Jeffery Park | 41.140600, -84.598926 | PAD-US 4.0 GDB (15ac polygon centroid) |
| OH-PAU-S-0013 | Herb Monroe Community Park | 41.138304, -84.580433 | Census geocoder — 122 E Jackson St, Paulding OH |
| OH-PAU-S-0015 | Paulding Skate Park | 41.144944, -84.576172 | Nominatim OSM — Elm Street, Paulding |
| OH-PAU-S-0016 | Reservoir Park | 41.125613, -84.587265 | PAD-US 4.0 GDB (32ac polygon centroid) |
| OH-PAU-S-0017 | Payne Community Park | 41.085691, -84.729078 | PAD-US 4.0 GDB (16ac polygon centroid) |
| OH-PAU-S-0018 | Oakwood Community Park | 41.094081, -84.381416 | PAD-US 4.0 GDB (4ac polygon centroid) |
| OH-PAU-S-0020 | Forder Bridge Conservation Area | 41.219241, -84.672509 | PAD-US 4.0 GDB (Forrest Woods Forder Bridge, 52ac) |

---

## 3. GPS Still Low-Precision — manual_review_queue

PCPD parks not in PAD-US, GNIS, or OSM. Recommend PCPD contact or county auditor parcel lookup.

| Site ID | Name | Current GPS | Issue |
|---------|------|-------------|-------|
| OH-PAU-S-0003 | Canal Park | 41.1283, -84.7023 (shared placeholder) | PCPD park at St. Rt. 111 near Junction, OH — no digital record |
| OH-PAU-S-0004 | Cecil Bridge Park | 41.1969, -84.5775 (shared placeholder) | PCPD park on Road 105 at Cecil Bridge — no digital record |
| OH-PAU-S-0005 | Five Span Park | 41.1283, -84.7023 (shared placeholder) | PCPD park at SR 111/637 Auglaize River — no digital record |
| OH-PAU-S-0006 | Flat Rock Trail Park | 41.137, -84.573 (Paulding centroid) | PCPD, 12600 Rd 119 Paulding — Census could not resolve county road |
| OH-PAU-S-0014 | Paulding Water Park | 41.137, -84.573 (Paulding centroid) | Village of Paulding — no OSM/GNIS record |

---

## 4. Trail Parents Added (8 entries)

| Trail | Parent Site | Note |
|-------|-------------|------|
| OH-MC-T-0216 M&E Canal Towpath | OH-PAU-S-0003 Canal Park | BT/NCT terminus on Towpath |
| OH-MC-T-0216 M&E Canal Towpath | OH-PAU-S-0004 Cecil Bridge Park | Maumee River / canal corridor |
| OH-MC-T-0216 M&E Canal Towpath | OH-PAU-S-0005 Five Span Park | Canal corridor |
| OH-MC-T-0216 M&E Canal Towpath | OH-PAU-S-0006 Flat Rock Trail Park | Flat Rock Creek corridor |
| OH-MC-T-0216 M&E Canal Towpath | OH-PAU-S-0020 Forder Bridge Conservation Area | BSC property on Towpath route |
| OH-MC-T-0001 Maumee River Water Trail | OH-PAU-S-0003 Canal Park | Maumee River access at Junction |
| OH-MC-T-0001 Maumee River Water Trail | OH-PAU-S-0004 Cecil Bridge Park | Road 105 at Cecil Bridge water trail access |
| OH-MC-T-0001 Maumee River Water Trail | OH-PAU-S-0020 Forder Bridge Conservation Area | Forder Bridge Water Trail AP on BSC property |

**Not added (pending route map research):**
- OH-MC-T-0200 North Country NST: co-routes with BT Defiance Section through Canal Park; no dedicated Paulding County site parents beyond Canal Park (already covered via T-0216 trail_parents)
- OH-MC-T-0218 BT Delphos Section: same corridor as M&E Towpath in Paulding — same site parents as T-0216 (could add, deferred)
- OH-MC-T-0219 BT Defiance Section: same corridor; deferred

---

## 5. Supplemental Sites Added

### T6 — Village Parks (8 sites, S-0023 through S-0030)

| Site ID | Name | Acres | Municipality | Township | GPS | Source |
|---------|------|-------|--------------|----------|-----|--------|
| OH-PAU-S-0023 | Antwerp Community Park | 5 | Antwerp | Carryall | 41.183605, -84.744050 | PAD-US/GNIS |
| OH-PAU-S-0024 | Cecil Community Park | 4 | Cecil | Crane | 41.221161, -84.603286 | GNIS |
| OH-PAU-S-0025 | Charloe Community Park | 2 | Charloe | Brown | 41.131875, -84.434729 | PAD-US/GNIS |
| OH-PAU-S-0026 | Melrose Town Park and Ballfield | 8 | Melrose | Brown | 41.091649, -84.415697 | PAD-US/GNIS |
| OH-PAU-S-0027 | Paulding Athletic Fields | 18 | Paulding | Paulding | 41.146247, -84.576685 | PAD-US/GNIS |
| OH-PAU-S-0028 | Lafountain Park | 6 | Paulding | Paulding | 41.144567, -84.576904 | PAD-US/GNIS |
| OH-PAU-S-0029 | School Park | 4 | Payne | Benton | 41.076931, -84.732362 | PAD-US/GNIS |
| OH-PAU-S-0030 | Oakwood Ball Field | 13 | Oakwood | Brown | 41.096577, -84.372445 | PAD-US |

### T7 — Forrest Woods BSC Expansion Parcels (4 sites, S-0031 through S-0034)

All confirmed Crane Township, Paulding County (township lookup). All NGO ownership (Black Swamp Conservancy). Parent site: OH-PAU-S-0002.

| Site ID | Name | Acres | GPS |
|---------|------|-------|-----|
| OH-PAU-S-0031 | Forrest Woods Nature Preserve: Harper-Forrest Expansion | 77 | 41.230515, -84.667095 |
| OH-PAU-S-0032 | Forrest Woods Nature Preserve: Land Acquisition | 78 | 41.233957, -84.662338 |
| OH-PAU-S-0033 | Forrest Woods Nature Preserve: Rooks-Harper Expansion | 60 | 41.234953, -84.672032 |
| OH-PAU-S-0034 | Forrest Woods Nature Preserve: Shaffer Property Expansion | 40 | 41.235820, -84.667092 |

Note: QR flagged Land Acquisition parcel as potential cross-county candidate. Township lookup confirms all 4 parcels are in Crane Township, Paulding County — NOT Defiance County (bbox false positive concern resolved).

---

## 6. Confirmed Bbox False Positives (Not Paulding Gaps)

- **Moats Park** (PAD-US 13ac, City Land, 41.282873, -84.550979): Township lookup returns Delaware Township — not a Paulding County township. Bbox bleed from Defiance County. Added to manual_review_queue to verify if a separate Moats Park exists near Paulding village.
- **Ney Community Park** (10ac): Confirmed Defiance County in prior sessions.
- **Oxbow Lake Wildlife Area**: Defiance County (OH-DEF-S-0002).
- **Camp Lakota, Independence Dam SP, Bronson Park** and other Defiance/Henry County entities: confirmed not Paulding.

---

## 7. Open Items

- GPS precision: S-0003/0004/0005/0006 (PCPD parks), S-0014 (Paulding Water Park) — in manual_review_queue
- Moats Park county verification — in manual_review_queue
- UAW Park county verification — in manual_review_queue
- BT trail parents (T-0218, T-0219, T-0200) for Paulding sites — deferred (co-route with T-0216 already covered)
- Forrest Woods SNP acreage discrepancy (Open Q#12: 193/292/346ac) — still unresolved
- Meyerholtz WA baseline error (Open Q#11) — still unresolved
