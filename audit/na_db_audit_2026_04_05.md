# Natural Areas Database Audit
**Date:** 2026-04-05
**Database:** `natural_areas_v5.db`
**Counties processed:** Franklin, Scioto, Wayne

---

## Database Snapshot

| Entity Type    | Count |
|----------------|-------|
| Sites          | 1,131 |
| Trails         | 154   |
| Trail Segments | 3     |
| Trail Networks | 4     |
| Site Networks  | 18    |
| Access Points  | 79    |
| **Total**      | **1,389** |

**Pipeline runs on record:**

| Run ID | County | Date | Input | Normalized | Held | Rejected |
|--------|--------|------|-------|------------|------|----------|
| franklin_oh_2026_03_25 | Franklin | 2026-03-25 | 1,174 | 1,174 | 0 | 0 |
| scioto_oh_2026_03_28 | Scioto | 2026-03-28 | 29 | 28 | 1 | 0 |
| SC-2026-03-30 | Scioto | 2026-03-30 | 81 | 80 | 1 | 0 |
| wayne_oh_2026_03_08 | Wayne | 2026-03-08 | 79 | 73 | 6 | 0 |

---

## Issues Found

### 1. Confirmed Duplicate — Gladys Riley Preserve (Scioto) ⚠️ HIGH PRIORITY

Two records for the same entity with identical GPS coordinates:

| Field | SC-S-0006 | SC-S-0042 |
|-------|-----------|-----------|
| Name | Gladys Riley Golden-star State Nature Preserve | Gladys Riley Golden Star Lily Preserve |
| Category | Nature Preserve | Nature Preserve |
| GPS | 38.85062, -83.201882 | 38.85062, -83.201882 |
| Ownership | Arc of Appalachia (fee ownership) | Arc of Appalachia |
| Origin | scioto_oh_2026_03_28 run | SC-2026-03-30 run |

**Recommendation:** Merge. SC-S-0006 has the more complete description and correct ODNR name. SC-S-0042 should be absorbed into SC-S-0006 and deleted. The name discrepancy is because one source uses the ODNR-designated state nature preserve name and the other uses the Arc of Appalachia preserve name — they are the same physical site.

---

### 2. Duplicate Held Entry — Shawnee Bridle Trail Network ⚠️ HIGH PRIORITY

The Shawnee Bridle Trail Network appears **twice** in `held_entities` from two different Scioto runs:

| held_id | record_id | run_id | hold_reason |
|---------|-----------|--------|-------------|
| 7 | SC-TN-0001 | scioto_oh_2026_03_28 | unresolved_member_ids |
| 8 | HOLD-Trail Network-Shawnee Bridle Trail Network | SC-2026-03-30 | unresolved_member_ids |

held_id 8 has a malformed record_id (was never properly ID-assigned before holding). The 03/30 run also didn't check whether the entity was already held from the 03/28 run.

**Recommendation:** Delete held_id 8. Retain held_id 7 (SC-TN-0001). The correct behavior is to update the existing hold record if the entity is still unresolvable on a re-run, not create a new held entry.

---

### 3. Stale Member IDs — Wayne Trail Network ⚠️ HIGH PRIORITY

`WA-TN-0001` (Rails to Trails of Wayne County Trail System) stores member_trail_ids in an obsolete format:

- **Stored:** `T7-001;T7-003`
- **Neither ID exists** in the `trails` table

The actual Wayne trail records that correspond to these members are:
- `WA-T-0009` — County Line Trail (the 6.7-mile paved trail)
- `WA-T-0010` — Heartland Trail (the 3.7-mile built portion)

**Recommendation:** Update `WA-TN-0001.member_trail_ids` to `WA-T-0009;WA-T-0010`.

---

### 4. Sites Missing GPS (9 sites)

These sites have no GPS coordinates. The GPS target for sites is 90%+; current rate is **99.2%** so this is minor, but these specific sites need follow-up.

| Site ID | Name | County |
|---------|------|--------|
| FR-S-1040 | Finnell Park | Franklin |
| FR-S-1041 | O'Shaughnessy Reservoir | Franklin |
| FR-S-1042 | Blacklick Woods | Franklin |
| FR-S-1044 | James H. Kelley Preserve | Franklin |
| SC-S-0002 | Alum Rock | Scioto |
| SC-S-0009 | CCC Memorial to Company 1545 | Scioto |
| SC-S-0028 | Sciotoville Community Square | Scioto |
| SC-S-0043 | Scioto Bend Preserve | Scioto |
| SC-S-0012 | Scioto Brush Creek State Scenic River | Adams;Scioto |

Note: The four Franklin sites (FR-S-1040–1044) have high sequential IDs, suggesting they were late additions and possibly never went through GPS acquisition.

---

### 5. Sites Missing Category (2 sites)

| Site ID | Name | County | GPS |
|---------|------|--------|-----|
| SC-S-0002 | Alum Rock | Scioto | None |
| SC-S-0003 | High Rock | Scioto | 38.588413, -82.797389 |

Both are natural geological features in the Shawnee State Forest area. Suggested category: **Natural Feature** (matching the vocabulary used for WA-S-0005 Koehler's Pond).

---

### 6. Trails Missing Difficulty and Accessibility (significant gap)

| County | Missing Difficulty | Missing Accessibility |
|--------|--------------------|-----------------------|
| Franklin | 21 | ~25 |
| Scioto | 12 | ~18 |
| Delaware;Franklin | 2 | 2 |
| Adams;Pike;Scioto | 2 | 2 |
| **Total** | **37 (24%)** | **47 (31%)** |

This is a content quality issue rather than a pipeline integrity issue — these fields were left blank during discovery because source data didn't provide them. Water trails (where difficulty/accessibility don't apply in the traditional sense) account for some of these blanks.

---

### 7. Friendship Park — Two Distinct Parks (Not a Duplicate)

Two sites named "Friendship Park" in Franklin County appear at first to be a duplicate, but they are distinct entities:

| Site ID | Name | GPS | Ownership |
|---------|------|-----|-----------|
| FR-S-0047 | Friendship Park | 40.0147, -82.8755 | Prairie Township |
| FR-S-1026 | Friendship Park | 40.0164, -82.8772 | City of Gahanna |

These are ~0.2 miles apart and governed by different entities. **This is not a duplicate** — both records are correct. No action needed.

---

### 8. GPS Collisions — Co-located Entities (Expected / Informational)

Many Franklin County site pairs share the same GPS. Most represent **legitimate co-located entities** (a park and its embedded nature preserve, a park and its shelter, a parkland and its named access feature, etc.). A few warrant closer review:

**Possible precision issue (same GPS, different-sounding entities):**
- `FR-S-0011` (Glacier Ridge Metro Park) and `FR-S-0014` (Homestead Metro Park) share the same GPS — these are distinct Metro Parks separated by several miles. This GPS is likely a centroid placeholder shared during data entry rather than a true location. Both need corrected GPS.
- `FR-S-0001` (Gahanna Woods State Nature Preserve) and `FR-S-0192` (Griggs Nature Preserve) — same GPS; these are in different parts of Franklin County and should not share coordinates.
- `FR-S-0023` (Edward S. Thomas Scenic Nature Preserve) and `FR-S-0285` (Mock Nature Preserve) — these are separate preserves; shared GPS is suspect.
- `FR-S-0327` (Raymond Memorial Golf Course) and `FR-S-0434` (Wilson Road Golf Course) — these are on opposite sides of Columbus; shared GPS is clearly wrong for at least one of them.
- `FR-S-0453` (Trabue Nature Preserve) and `FR-S-0465` (ML "Red" Trabue Nature Reserve) — potential duplicate or near-duplicate under different names; both in the same area. Worth a resolution check.
- `FR-S-0804` (Smith Nature Park) and `FR-S-1020` (Alice Smith Nature Preserve) — different names, same GPS; may be a legitimate parent/child pair or a near-duplicate.

**Legitimate co-location (expected, no action needed):**
- Parks with embedded shelters, gazebos, or amenities sharing the park's GPS (e.g., FR-S-1026/1028/1029)
- Nature preserves adjacent to or embedded within parks (e.g., Webster Nature Preserve / Webster Park)
- WA-S-0004 (Barnes Preserve) and WA-S-0005 (Koehler's Pond) — Koehler's Pond is on the Barnes Preserve property
- SC-S-0025 (Mound Park) and SC-S-0026 (Horseshoe Mound) — the mound is located within or immediately adjacent to the park

---

### 9. Trail Networks — Incomplete Fields

Two Franklin trail networks are missing several fields that were captured for the other two networks:

| Network | Missing Fields |
|---------|---------------|
| FR-TN-0001 (Central Ohio Greenways) | network_type, status, ownership, length_mi |
| FR-TN-0002 (Dublin Bikepath and Park System) | network_type, status, ownership, length_mi, member_trail_count, member_trail_ids, description |

These appear to have been added with partial data and not fully normalized.

---

### 10. Held Entities Summary

8 held entities currently in queue — all are expected and properly documented:

| held_id | Name | County | Reason |
|---------|------|--------|--------|
| 1 | Killbuck Marsh Wildlife Area | Wayne | multi_county (waiting: Holmes) |
| 2 | Killbuck Marsh Wildlife Observation Trail | Wayne | identity_uncertain |
| 3 | Funk Bottoms Wildlife Area | Wayne | multi_county (waiting: Ashland) |
| 4 | Chippewa Township Nature Preserve trails | Wayne | identity_uncertain |
| 5 | Sippo Valley Trail | Wayne | multi_county (waiting: Stark) |
| 6 | Holmes County Trail (Wayne County section) | Wayne | multi_county (waiting: Holmes) |
| 7 | Shawnee Bridle Trail Network | Scioto | unresolved_member_ids |
| 8 | Shawnee Bridle Trail Network *(duplicate)* | Scioto | duplicate of held_id 7 — **delete** |

---

## Summary of Recommended Actions

| Priority | Action | Effort |
|----------|--------|--------|
| HIGH | Merge SC-S-0006 and SC-S-0042 (Gladys Riley duplicate) | 1 step |
| HIGH | Delete duplicate held_id 8 (Shawnee Bridle Trail Network) | 1 step |
| HIGH | Fix WA-TN-0001 member_trail_ids (T7-001/T7-003 → WA-T-0009/WA-T-0010) | 1 step |
| MEDIUM | Resolve GPS collisions: Glacier Ridge/Homestead, Gahanna Woods/Griggs, Raymond/Wilson Rd Golf, Trabue/Trabue | GPS research |
| MEDIUM | Review Trabue Nature Preserve vs. ML "Red" Trabue Nature Reserve for possible duplicate | Resolution check |
| MEDIUM | Add GPS to 9 sites missing coordinates | GPS acquisition |
| MEDIUM | Add category to SC-S-0002 (Alum Rock) and SC-S-0003 (High Rock) | Vocabulary lookup |
| MEDIUM | Complete missing fields for FR-TN-0001 and FR-TN-0002 | Normalization |
| LOW | Fill trail difficulty/accessibility gaps where source data permits (37/47 trails) | Discovery/research |
