# Van Wert County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 19 | OH-VNW-S-0001 – OH-VNW-S-0019 (no gaps) |
| Trails | 3 | OH-VNW-T-0001/0002/0003 |
| Trail Segments | 0 | — |
| Trail Networks | 0 | — |
| Site Networks | 0 | — |
| Access Points | 1 | OH-VNW-AP-0001 |
| Held Entities | 0 | table empty |

**Run metadata:** `van_wert_oh_2026_04_14` — input=23, normalized=23, held=0

Run flags recorded: GPS_VERIFY_NEEDED (S-001, S-008), STORYBOOK_TRAIL_CONFIRM_NEEDED (S-003), LENGTH_VERIFY_NEEDED (T-001), DETAILS_INCOMPLETE (S-016), FIELD_VERIFY_NEEDED (S-018).

---

## 2. FK Integrity

### Fix applied this session

| AP | Old value | New value | Issue |
|---|---|---|---|
| OH-VNW-AP-0001 | OH-VNW-S-007 | OH-VNW-S-0007 | Zero-padding |

Fix verified post-update. No additional broken FKs detected.

---

## 3. Sequence Gaps

None. OH-VNW-S-0001 through S-0019 are all present with no gaps. OH-VNW-T-0001 through T-0003 are all present.

---

## 4. GPS Status

All 19 active sites have GPS values (0 missing). GPS Gate: passed.

**Data quality concern — low-precision coordinates:**

- OH-VNW-S-0001 (Whitey Case Wildlife Production Area): GPS 40.8, -84.79 — single decimal place; clear centroid approximation. Flagged in run_metadata as GPS_VERIFY_NEEDED.
- OH-VNW-S-0019 (Van-Del Drive-In): GPS 40.852, -84.448 — 3 decimal places; rounded.

Run flag GPS_VERIFY_NEEDED also applies to S-0008 (Van Wert Reservoir 1); coordinate at 40.847197, -84.57695 looks adequate (6 decimal places) but may have been flagged for source confidence reason. Verify in batch phase.

---

## 5. Trail Parents

| Trail | Trail_parents | Status |
|---|---|---|
| OH-VNW-T-0001 Tully Monster Trail | 1 (→ OH-VNW-S-0002) | ✓ |
| OH-VNW-T-0002 Wildcat Trail | 1 (→ OH-VNW-S-0007) | ✓ |
| OH-VNW-T-0003 Warrior Trail | 0 | Missing |

**Warrior Trail:** 2.6-mile rail trail in Ohio City, Van Wert County (a/k/a Ohio City Greenway). Managed by Village of Ohio City (T6 Municipal). The DB entity for Ohio City is OH-VNW-S-0016 (Ohio City Fireman's Park — flagged DETAILS_INCOMPLETE). Warrior Trail runs through Ohio City and is the logical parent candidate; no other Ohio City site is in the DB.

Batch fix: `INSERT INTO trail_parents VALUES ('OH-VNW-T-0003', 'OH-VNW-S-0016')`.

**Note:** S-0016 is flagged DETAILS_INCOMPLETE. If the Warrior Trail / Ohio City Greenway is distinct from Fireman's Park (i.e., a separate greenway corridor rather than a park trail), S-0016 may need a supplemental discovery record and T-0003 may need a dedicated site entity. Verify during Ohio City T6 supplemental discovery.

---

## 6. PAD-US Spatial Audit

**Bbox:** Van Wert County bounding box. 15 PAD-US fee records in bbox; 7 matched (≥80); 2 unmatched; 6 skipped.

### 6a. Wrong match

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Wesley Park (3ac, City) | OH-VNW-S-0005 Smiley Park | 82 | Wrong — Wesley Park and Smiley Park are distinct Van Wert city parks; the score is driven by shared geographic metadata, not name similarity. Wesley Park is a genuine gap. |

### 6b. Acreage discrepancy in matched records

| PAD-US Record | PAD-US Acres | DB Entity | Note |
|---|---|---|---|
| Rotary Park (172ac) | 172 | OH-VNW-S-0015 Rotary Dog Park | 172ac is implausibly large for an urban dog park. PAD-US likely aggregates multiple city parcels under this record or has a data entry error. Verify actual acreage against city records. |

### 6c. Skipped — note

"Little Auglaize Wildlife Reserve" appeared in the PAD-US bbox as closed access and was skipped by the query. This is an ODNR-managed parcel (restricted/limited access). If this is a Tier 2 natural area not already in the DB, it warrants supplemental T2 discovery regardless of the closed-access flag. Verify against ODNR source.

### 6d. Unmatched — genuine Van Wert gaps

Both unmatched records are municipal parks (City/Local Gov land, GAP4); T6 supplemental discovery:

| PAD-US Record | Acres | Owner | Notes |
|---|---|---|---|
| Bresler Park | 8 | City | Van Wert city park; not in DB |
| Grover Hill Community Park | 18 | City | Village of Grover Hill, Van Wert County; not in DB |
| Wesley Park | 3 | City | Van Wert city park; wrong match above; genuine gap |

---

## 7. Open Run Flags

| Flag | Entity | Action Needed |
|---|---|---|
| GPS_VERIFY_NEEDED | OH-VNW-S-0001 | Acquire precision GPS for Whitey Case WPA |
| GPS_VERIFY_NEEDED | OH-VNW-S-0008 | Verify GPS source confidence for Van Wert Reservoir 1 |
| STORYBOOK_TRAIL_CONFIRM_NEEDED | OH-VNW-S-0003 | Confirm Storybook Trail scope / entity type during batch phase |
| LENGTH_VERIFY_NEEDED | OH-VNW-T-0001 | Verify total length for Tully Monster Trail |
| DETAILS_INCOMPLETE | OH-VNW-S-0016 | Ohio City Fireman's Park: complete description; confirm whether Warrior Trail runs through it |
| FIELD_VERIFY_NEEDED | OH-VNW-S-0018 | Entity requires field verification before data is considered reliable |

---

## 8. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | AP-0001 3-digit non-padded parent_entity_id | FIXED | Applied this session |
| 2 | Missing trail_parent for OH-VNW-T-0003 Warrior Trail | MEDIUM | Batch: add → OH-VNW-S-0016; verify S-0016 identity during Ohio City T6 |
| 3 | S-0001 GPS single decimal place (40.8, -84.79) | MEDIUM | Batch: precision GPS for Whitey Case WPA |
| 4 | S-0019 GPS low precision (40.852, -84.448) | MEDIUM | Batch: precision GPS for Van-Del Drive-In |
| 5 | Rotary Park PAD-US acreage 172ac vs expected small city park | MEDIUM | Verify actual acreage; likely PAD-US aggregation error |
| 6 | Wesley Park (3ac, City) not cataloged | MEDIUM | Supplemental T6 discovery |
| 7 | Bresler Park (8ac, City) not cataloged | MEDIUM | Supplemental T6 discovery |
| 8 | Grover Hill Community Park (18ac, City) not cataloged | MEDIUM | Supplemental T6 discovery |
| 9 | Little Auglaize Wildlife Reserve (PAD-US skipped, closed access) | MEDIUM | Verify against ODNR; supplemental T2 if not already in DB |
| 10 | 5 open run flags (GPS, details, field verify) | MEDIUM | Resolve in batch phase |

---

## 9. Batch Phase Actions

- [ ] Add trail_parent: OH-VNW-T-0003 → OH-VNW-S-0016 (Warrior Trail → Ohio City Fireman's Park)
- [ ] Acquire precision GPS for OH-VNW-S-0001 (Whitey Case WPA) and OH-VNW-S-0019 (Van-Del Drive-In)
- [ ] Verify GPS source confidence for OH-VNW-S-0008 (Van Wert Reservoir 1)
- [ ] Supplemental T6 discovery: Wesley Park, Bresler Park, Grover Hill Community Park
- [ ] Verify Little Auglaize Wildlife Reserve against ODNR; supplement T2 if warranted
- [ ] Verify Rotary Park actual acreage (PAD-US 172ac is implausible for a dog park)
- [ ] Resolve open run flags: STORYBOOK_TRAIL_CONFIRM_NEEDED (S-0003), LENGTH_VERIFY_NEEDED (T-0001), DETAILS_INCOMPLETE (S-0016), FIELD_VERIFY_NEEDED (S-0018)
- [ ] Ohio City T6 supplemental: confirm Warrior Trail / Ohio City Greenway relationship to S-0016; complete S-0016 description
