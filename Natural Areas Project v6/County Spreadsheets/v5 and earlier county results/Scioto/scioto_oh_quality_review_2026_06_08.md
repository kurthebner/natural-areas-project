# Scioto County Quality Review
**Date:** 2026-06-08
**Reviewer:** Claude (automated + PAD-US spatial audit)
**Status: PARTIAL FAIL**

---

## 1. Entity Counts

| Entity Type | Count | ID Range / Notes |
|---|---|---|
| Sites | 46 | 42 OH-SC-S-*, 4 OH-MC-S-* (Wayne NF, Shawnee SF, Scioto Brush Creek SSR, Brush Creek SF) |
| Trails | 23 | 20 OH-SC-T-*, 3 OH-MC-T-* |
| Trail Segments | 0 | — |
| Trail Networks | 1 | OH-MC-TN-0001 Shawnee Bridle Trail Network (Scioto;Adams) |
| Site Networks | 1 | OH-SC-SN-0001 Arc of Appalachia — Scioto County Preserves |
| Access Points | 9 | OH-SC-AP-0001 – 0009 |
| Held Entities | 0 | — |

**Run metadata:** Two pipeline runs recorded:
- `scioto_oh_2026_03_28` — input=29, normalized=28, held=1 (Tiers 1–2 only)
- `SC-2026-03-30` — input=81, normalized=80, held=1 (full post-discovery upsert)

**County code note:** Scioto uses the 2-letter prefix "SC" (e.g., OH-SC-S-0001) rather than the 3-letter convention used by other counties (OTT, PAU, SAN, etc.). This is established throughout all Scioto entity IDs and is consistent internally. Not an error, but deviates from the project convention.

---

## 2. FK Integrity

No AP parent_entity_id padding errors detected. All 9 APs have correctly formatted IDs or intentionally NULL parents.

**OH-SC-AP-0004 (Burkes Point Boat Ramp):** parent_entity_id = NULL, parent_entity_type = NULL — intentional. Per identity_notes: governance is unconfirmed (ODNR, Army Corps, or county management all possible). Flagged GOVERNANCE_UNCERTAIN. No fix needed; governance must be verified before a parent can be assigned.

### Fix applied this session

**OH-SC-SN-0001 member_site_ids:** Was `SC-S-0039;SC-S-0040;SC-S-0041;SC-S-0042` (missing "OH-" prefix on all four IDs). Fixed to `OH-SC-S-0039;OH-SC-S-0040;OH-SC-S-0041;OH-SC-S-0042`. Verified post-fix.

---

## 3. Sequence Gaps

**OH-SC-S- gaps:** 1, 4, 12, 13, 43
- Gaps 1, 4, 12: not in held_entities — entities likely removed during resolution (out-of-scope, merged, or reclassified)
- Gap 13: OH-SC-S-0013 was promoted to OH-MC-S-0013 (Brush Creek State Forest) when identified as multi-county during resolution; slot 13 in the SC series is vacated
- Gap 43: not in held_entities — cause unknown

**OH-SC-T- gaps:** 1, 14, 15
- Gap 1: not in DB; likely removed during resolution
- Gaps 14, 15: these trails were assigned MC IDs (OH-MC-T-0014, OH-MC-T-0015) when found to be multi-county; SC series slots vacated

---

## 4. GPS Status

All 46 active sites have GPS values (0 missing). GPS Gate: passed.

**Co-located sites (intentional):**
- OH-SC-S-0006 "Gladys Riley Golden-star State Nature Preserve" (186ac, ODNR) and OH-SC-S-0042 "Gladys Riley Golden Star Lily Preserve" (230ac, Arc of Appalachia) share GPS 38.85062, -83.201882. These are correctly cataloged as overlapping entities — the 186ac ODNR state nature preserve designation sits within the larger 230ac Arc of Appalachia fee parcel. Co-location is expected.
- OH-SC-S-0025 "Mound Park" and OH-SC-S-0026 "Horseshoe Mound" share GPS 38.743273, -82.976701. Horseshoe Mound is the Hopewell archaeological feature within the park. Co-location is expected; the mound's precise GPS may differ from the park centroid — flag for precision GPS pass.

---

## 5. Trail Parents

22 of 23 trails have trail_parents entries. Missing:

| Trail | Status | Recommended parent |
|---|---|---|
| OH-MC-T-0006 Shawnee Backpack Trail (Adams;Scioto) | 0 parents | OH-MC-S-0002 Shawnee State Forest |

Batch fix: `INSERT INTO trail_parents VALUES ('OH-MC-T-0006', 'OH-MC-S-0002')`.

All other trail_parents verified:
- Shawnee State Park trails (T-0002 through T-0006) → OH-SC-S-0005 ✓
- Shawnee State Forest trails (T-0007 through T-0009, MC-T-0014, MC-T-0015) → OH-MC-S-0002 ✓
- SSU Deal Arboretum trails (T-0010 through T-0013) → OH-SC-S-0011 ✓
- Arc of Appalachia preserve trails → respective site parents ✓

---

## 6. Site and Trail Networks

**OH-SC-SN-0001 (Arc of Appalachia — Scioto County Preserves):** 4 members now correctly referenced (see §2 fix). Members: Ohio Hanging Rock, Simon Woods, Tremper Mound, Gladys Riley Golden Star Lily Preserve.

**OH-MC-TN-0001 (Shawnee Bridle Trail Network, Scioto;Adams):** member_trail_ids = NULL. Per identity_notes, the network is managed as a unified undivided unit with no named sub-segments officially designated. NULL is intentional.

---

## 7. PAD-US Spatial Audit

**Bbox:** Scioto County bounding box. 32 PAD-US fee records in bbox; 17 matched (≥80); 9 unmatched; 6 skipped.

### 7a. Wrong match

| PAD-US Record | Matched To | Score | Issue |
|---|---|---|---|
| Washington Township Park (6ac, City) | OH-SC-S-0017 Clay Township Park | 84 | Wrong — different townships; both "Township Park" tokens drove match; Washington Township Park is a genuine gap |

### 7b. Acreage discrepancies in matched records

| PAD-US Record | PAD-US Acres | DB Acres | Note |
|---|---|---|---|
| Shawnee State Park (×2 records: 765ac + 1,280ac) | 2,045 total | 1,095 | PAD-US may include adjacent forest parcels managed with the park; verify against ODNR |
| Brush Creek State Forest (×2 records: 13,161 + 34) | 13,195 | 13,000 | Close; within rounding of source |
| Camp Oyo (23ac) | 23 | 52 | DB higher; may include leased/program land beyond fee parcel |
| Scioto Brush Creek NA (36ac) | 36 | 30 | DB lower; same source discrepancy pattern |

### 7c. Genuine Scioto County gaps

**T7 — Conservancy / Land Trust:**

| PAD-US Record | Acres | GAP | Notes |
|---|---|---|---|
| Glade Wetland Fee (parcel 1) | 215 | 1 | NGO-owned; GAP1 (highest protection); not in DB |
| Glade Wetland Fee (parcel 2) | 71 | 1 | Second parcel of same preserve; not in DB |
| Glade Wetland | 6 | 1 | Associated small parcel; not in DB |
| Arc of Appalachia Biodiversity | 317 | 2 | Arc of Appalachia preserve not in DB; also not a member of OH-SC-SN-0001; verify whether in Scioto County or adjacent county (Adams or Pike) |
| Molly Lauman Girl Scout Camp | 19 | 4 | NGO camp; not in DB |
| Unknown Park (5ac, NGO) | 5 | 4 | NGO-owned; name unknown in PAD-US; physical park exists |

The Glade Wetland parcels (292ac combined, GAP1) are the most significant gaps in this county — highest PAD-US protection level, not in DB.

**T6 — Municipal:**

| PAD-US Record | Acres | Notes |
|---|---|---|
| Washington Township Park | 6 | Wrong match above; genuine gap — Washington Township, Scioto County |
| Branch Rickey Park | 0 | 0ac in PAD-US (data gap); small Portsmouth city park; not in DB |
| Village Square Park | 1 | City park; not in DB |
| Unknown Ball Park | 3 | Name unknown in PAD-US; physical ballfield park; not in DB |

---

## 8. Summary of Issues

| # | Issue | Severity | Resolution |
|---|---|---|---|
| 1 | SN-0001 member_site_ids missing OH- prefix | FIXED | Applied this session |
| 2 | AP-0004 Burkes Point: GOVERNANCE_UNCERTAIN, no parent | OPEN | Verify managing agency before assigning parent |
| 3 | Missing trail_parent for OH-MC-T-0006 | MEDIUM | Batch: add → OH-MC-S-0002 |
| 4 | Glade Wetland / Glade Wetland Fee (~292ac, GAP1, NGO) not cataloged | HIGH | Supplemental T7 discovery |
| 5 | Arc of Appalachia Biodiversity (317ac, GAP2) not cataloged | HIGH | Supplemental T7 discovery; verify county |
| 6 | Washington Township Park (6ac) not cataloged | MEDIUM | Supplemental T6 discovery |
| 7 | Molly Lauman Girl Scout Camp (19ac, NGO) not cataloged | MEDIUM | Supplemental T7 discovery |
| 8 | Branch Rickey Park, Village Square Park, Unknown Ball Park, Unknown Park not cataloged | MEDIUM | Supplemental T6/T7 discovery |
| 9 | Shawnee State Park acreage discrepancy (DB 1,095ac vs PAD-US 2,045ac combined) | LOW | Verify against ODNR source |
| 10 | County code "SC" deviates from 3-letter convention | NOTE | Established; do not change |
| 11 | Sequence gaps S-0001/0004/0012/0043; T-0001 unexplained | LOW | Document in session log |

---

## 9. Batch Phase Actions

- [ ] Add trail_parent: OH-MC-T-0006 → OH-MC-S-0002 (Shawnee State Forest)
- [ ] Verify Burkes Point Boat Ramp governance; assign parent once confirmed
- [ ] Supplemental T7 discovery: Glade Wetland / Glade Wetland Fee (3 parcels, ~292ac, GAP1)
- [ ] Supplemental T7 discovery: Arc of Appalachia Biodiversity (317ac) — verify in Scioto County; if confirmed, add to OH-SC-SN-0001 as 5th member
- [ ] Supplemental T7 discovery: Molly Lauman Girl Scout Camp (19ac), Unknown Park (5ac, NGO)
- [ ] Supplemental T6 discovery: Washington Township Park, Branch Rickey Park, Village Square Park, Unknown Ball Park
- [ ] Verify Shawnee State Park total acreage against ODNR source (DB 1,095ac vs PAD-US 2,045ac)
- [ ] Precision GPS for Horseshoe Mound (OH-SC-S-0026) — currently shares centroid with Mound Park
