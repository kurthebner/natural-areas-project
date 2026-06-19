# Putnam County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_PUT_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PARTIAL FAIL

---

## 1. GPS Precision Updates (4 sites)

| Site ID | Name | Old GPS | New GPS | Source |
|---------|------|---------|---------|--------|
| OH-PUT-S-0001 | Cascade Wayside Wildlife Area | 41.018, -84.205 | 41.017972, -84.284284 | PAD-US 4.0 GDB (47ac) |
| OH-PUT-S-0002 | WPA 1 | 41.0, -84.205 | 41.026049, -84.214813 | PAD-US (WPA 51, 39ac) |
| OH-PUT-S-0003 | WPA 2 | 41.0, -84.275 | 41.007566, -84.238606 | PAD-US (WPA 52, 41ac) |
| OH-PUT-S-0004 | WPA 3 | 40.975, -84.23 | 41.010768, -84.334797 | PAD-US (WPA 54, 41ac) |

WPA PAD-US numeric IDs (51/52/54) match DB sequence (1/2/3) by geographic order (W→E: 54→52→51).

---

## 2. GPS Still Low-Precision — manual_review_queue

| Site ID | Name | Issue |
|---------|------|-------|
| OH-PUT-S-0008 | The Diversion Channel | GPS 41.052,-84.048 rounded (3dp); City of Ottawa wetland on OG Road; no PAD-US/OSM record |
| OH-PUT-S-0016 | Saint Barbara's Catholic Church Cemetery | GPS 41.018,-84.205 = Cascade Wayside placeholder — WRONG. No GNIS record. Need county auditor parcel lookup. |

---

## 3. Trail Parents Added (12 entries)

M&E Canal Towpath (T-0216), BT Delphos Section (T-0218), and NCT (T-0200) all co-route along the canal corridor through western Putnam County. Canal corridor sites: S-0001 through S-0004.

| Trail | Parent Site |
|-------|-------------|
| OH-MC-T-0216 (M&E Canal Towpath) | OH-PUT-S-0001, S-0002, S-0003, S-0004 |
| OH-MC-T-0218 (BT Delphos Section) | OH-PUT-S-0001, S-0002, S-0003, S-0004 |
| OH-MC-T-0200 (NCT) | OH-PUT-S-0001, S-0002, S-0003, S-0004 |

**OH-HAN-T-0012 (Old Mill Stream Scenic Byway):** Deferred — scenic byway, not a trail corridor; trail_parents relationship unclear without route map.

---

## 4. Supplemental Ottawa T6 Parks (4 sites, S-0030 through S-0033)

| Site ID | Name | Acres | GPS | Source |
|---------|------|-------|-----|--------|
| OH-PUT-S-0030 | Lords Park | 0 (fee parcel) | 41.018842, -84.049268 | PAD-US |
| OH-PUT-S-0031 | Waterworks Park | 5 | 41.020965, -84.036175 | PAD-US |
| OH-PUT-S-0032 | West End Water Tower Park | 2 | 41.020835, -84.053102 | PAD-US |
| OH-PUT-S-0033 | Memorial Park | 30 | 41.026677, -84.041413 | PAD-US |

**Deters Park: SKIPPED** — Putnam handoff (PUT-F-10) confirms this is a future/planned development per glandorfpark.org. Not a NAP entity.

**Waterworks Park identity note (S-0031):** PAD-US "Waterworks Park" at 41.021, -84.036 is ~1.2km from S-0007 "The Ottawa Reservoir" at 41.012, -84.023 (1972 S Agner St). Coordinates differ sufficiently to suggest these are two distinct entities. The handoff references "Waterworks Park" at 1035 E 3rd St as a separate facility (PUT-F-09). Added MRQ note to confirm identity before treating as distinct.

---

## 5. Attribution Correction — Charloe CP / Melrose Town Park

**Putnam QR incorrectly attributed these to Putnam County.** The QR states "Charloe and Melrose are both in Auglaize Township, Putnam County." However:
- Township lookup (TIGER/Line 2024): Charloe CP (41.131875, -84.434729) → Brown Township; Melrose Town Park (41.091649, -84.415697) → Brown Township
- GNIS: both returned under Paulding County query
- Longitude -84.43W / -84.42W is well inside Paulding County (Paulding/Putnam border ≈ -84.33W)

Both are Paulding County entities, already inserted as OH-PAU-S-0025 (Charloe Community Park) and OH-PAU-S-0026 (Melrose Town Park and Ballfield). **NOT Putnam County gaps.**

---

## 6. Acreage Discrepancy — manual_review_queue

- OH-PUT-S-0001 Cascade Wayside WA: DB=36ac vs PAD-US=47ac vs SORP25=62.78ac — likely ODNR acquisition since original entry. Added to MRQ.

---

## 7. Open Items

- S-0008 Diversion Channel GPS (low-precision) — MRQ
- S-0016 Saint Barbara Cemetery GPS (placeholder) — MRQ
- Cascade Wayside WA acreage verification — MRQ
- OH-HAN-T-0012 trail_parents (Old Mill Stream Scenic Byway) — deferred
- Waterworks Park / Ottawa Reservoir identity confirm — MRQ note on S-0031
- PUT-F-05 (Higher Education parcel, ~58ac) — still open
- PUT-F-08 (Union Township Cemetery Kalida) — still open
