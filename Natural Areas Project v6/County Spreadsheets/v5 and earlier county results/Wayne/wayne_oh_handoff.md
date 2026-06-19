# Wayne County, Ohio — Handoff Document
**PREFIX:** `WA`
**Status:** PIPELINE COMPLETE — BATCH RESOLUTION APPLIED 2026-06-10 | PAD-US SPOT-CHECK COMPLETE 2026-06-12 | MRQ 199 created
**Last updated:** 2026-06-12

---

## Supplemental Resolution — 2026-06-12

### PAD-US Spot-Check

PAD-US 4.0 Ohio fee layer cross-checked against Wayne DB (47 Sites, 12 Trails).

**Confirmed matches:**

| PAD-US Unit_Nm | GIS_Acres | DB Match | Notes |
|----------------|-----------|----------|-------|
| Brown's Lake Bog Fee (×2) | 83 + 19 | S-0001 (102ac) | ✓ two parcels sum to 102ac; confirmed |
| Johnson Woods Dedicated Nature Preserve | 206 | S-0002 | ✓ confirmed |
| Shreve Lake Wildlife Area | 228 | S-0003 | ✓ confirmed |
| Burbank Park | 26 | Burbank Community Park | ✓ confirmed |
| Shreve Community Park | 5 | Shreve Village Park | ✓ PAD-US naming variant; same entity |
| Wooster Memorial Park | 81 | S-0007 (422ac) | ✓ confirmed; PAD-US 81ac = partial polygon only |
| Creston Community Park | 48 | S-0023 | ✓ confirmed |

**False positives:** All Chippewa Lake entries (Medina County Park District); Wooster Country Club; Wayne County Fairgrounds (event venue).

**Residuals → MRQ 199:**

| PAD-US Unit_Nm | GIS_Acres | Assessment |
|----------------|-----------|------------|
| Dalton Park | 4 | T6 gap in Dalton village; not in DB |
| Killbuck Marsh WA (×2) | 4547 + 1258 | Cross-county ODNR entity; primarily Holmes County; stage for Holmes County run |
| Lower Killbuck Creek WA | 151 | ODNR; Holmes/Wayne/Coshocton area; stage for Holmes County run |
| Killbuck Walhonding WA | 20 | Small ODNR parcel in Killbuck corridor; stage for Holmes County run |

---

## Batch Resolution Summary — 2026-06-10
Source: Quality review 2026-06-08 (QR status: PASS with pipeline work)
See `wayne_oh_batch_resolution_2026_06_10.md` for full detail.

- +3 supplemental sites: S-0045 Schellin Park (13ac, Wooster), S-0046 Cohan Park (6ac, Wooster),
  S-0047 Kinney Trail Park (49ac, Wooster) — all City of Wooster, GPS from PAD-US
- 5 trail parents added: T-0001→S-0001, T-0002→S-0002, T-0003→S-0004, T-0004→S-0007, T-0011→S-0044
- MRQs: AP-0001/AP-0002 shared GPS; Cohan Park 1ac vs 6ac parcel check
- Final: 47 WA sites | 5 trail_parents

## Open Items
- AP-0001/AP-0002: resolve shared GPS coordinates
- S-0005 child-site GPS = parent GPS — non-blocking; review when field-verifying
- Cohan Park: verify S-0046 (6ac) vs separate 1ac PAD-US parcel at same location
- 8 cross-county held entities pending partner county runs (see Held Entities below)

## Held Entity Resolution Update — 2026-06-11

**OH-WA-T-0013 Chippewa Township Nature Preserve trails — RESOLVED**
- Research: Authoritative source (chippewatwp.com) describes "nature preserve trails" collectively — no individual trail names published by the township
- Resolution: Recorded as single Trailthing for the trail complex
- Source term: "nature preserve trails" (verbatim from source)
- Site parent: OH-WA-S-0006 (Chippewa Township Nature Preserve)
- Address discrepancy noted: original hold noted 17500 Galehouse Rd; current website shows 14228 Galehouse Rd, Doylestown, OH 44230. Both reference same preserve; possible address update or alternate entrance.
- Inserted into trailthings table, removed from held_entities ✓

**Remaining Wayne held (8) — all require partner county runs:**
| Record ID | Name | Hold Reason | Resolves When |
|-----------|------|-------------|---------------|
| OH-WA-S-0045 | Killbuck Marsh Wildlife Area | cross_county_held | Coshocton/Holmes/Knox/Cuyahoga County run |
| OH-WA-S-0046 | Funk Bottoms Wildlife Area | cross_county_held | Holmes County run |
| OH-WA-T-0014 | Sippo Valley Trail | cross_county_held | Stark County run |
| OH-WA-T-0015 | Holmes County Trail (Fredericksburg / Wayne County section) | cross_county_held | Holmes County run |
| OH-WA-AP-0003 | Killbuck Marsh — Carrie Lane Parking Area | parent_held | When S-0045 released |
| OH-WA-AP-0004 | Killbuck Marsh — Wright Marsh Parking Area | parent_held | When S-0045 released |
| OH-WA-AP-0013 | Sippo Valley Trail — Dalton Trailhead | parent_held | When T-0014 released |
| OH-WA-AP-0015 | Holmes County Trail — Fredericksburg Trailhead | parent_held | When T-0015 released |

## Prior Pipeline Status (pre-batch)
From QR 2026-06-08:
- 44 sites (max seq=0044), 11 trails, 0 trail_parents pre-batch
- 9 held entities (gps_missing)
- Staged supplemental: Schellin Park, Cohan Park, Kinney Trail Park (now inserted)
- Township/municipality fields: all derived from GPS via township lookup; populated in TSV
