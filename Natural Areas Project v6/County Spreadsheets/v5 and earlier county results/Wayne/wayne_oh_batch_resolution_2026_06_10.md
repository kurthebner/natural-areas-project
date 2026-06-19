# Wayne County — Batch Resolution Log
**Date:** 2026-06-10
**Run ID:** `BATCH_HEN_OTT_WAY_2026-06-10`
**Source:** Quality review 2026-06-08; QR status: PASS with pipeline work

---

## 1. Supplemental Sites (3 new, S-0045–S-0047)

| Site ID | Name | Acres | Municipality | GPS |
|---------|------|-------|--------------|-----|
| OH-WA-S-0045 | Schellin Park | 13 | Wooster | 40.794237, -81.934206 |
| OH-WA-S-0046 | Cohan Park | 6 | Wooster | 40.827041, -81.943258 |
| OH-WA-S-0047 | Kinney Trail Park | 49 | Wooster | 40.831380, -81.942097 |

All three confirmed City of Wooster, Wayne County, via township lookup (mun=Wooster).
GPS from PAD-US centroids. All staged from QR 2026-06-08 (Schellin 13ac, Cohan 6ac,
Kinney 49ac from QR research; GPS confirmed via PAD-US).

Note on Cohan Park: PAD-US has two Cohan Park parcels near Wooster — 6ac (inserted, S-0046)
and a separate 1ac parcel at lat=40.8265, lon=-81.9412. MRQ-flagged for consolidation check.

---

## 2. Trail Parents Added (5 entries)

| Trail | Parent Site |
|-------|-------------|
| OH-WA-T-0001 Brown's Lake Bog Trail | OH-WA-S-0001 (Brown's Lake Bog SNP) |
| OH-WA-T-0002 Johnson Woods Boardwalk | OH-WA-S-0002 (Johnson Woods SNP) |
| OH-WA-T-0003 Casey's Trails | OH-WA-S-0004 (Barnes Preserve) |
| OH-WA-T-0004 WMP Trail System | OH-WA-S-0007 (Wooster Memorial Park) |
| OH-WA-T-0011 Vulture's Knob Trail System | OH-WA-S-0044 (Vulture's Knob) |

---

## 3. MRQ Entries (2)

1. AP-0001/AP-0002 share identical GPS — verify distinct physical locations
2. Cohan Park 1ac PAD-US parcel (lat=40.8265,-81.9412) — verify vs S-0046 (6ac)

---

## 4. Final Counts

| Entity Type | Before | After |
|---|---|---|
| Sites (WA) | 44 | 47 |
| Trail parents (WA) | 0 | 5 |

---

## 5. Open Items

- AP-0001/AP-0002: resolve shared GPS coordinates
- 9 held entities: release pending GPS acquisition or `gps_unresolvable=true` flag
- S-0005 child-site GPS = parent GPS — review (non-blocking per QR)
- Cohan Park: verify single vs dual-parcel entity
