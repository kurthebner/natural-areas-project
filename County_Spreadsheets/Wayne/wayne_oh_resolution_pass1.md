# Resolution Pass 1 — Wayne County, Ohio
**Date:** 2026-03-08  
**Input:** `wayne_oh_raw_discovery.yaml`  
**Engine:** Resolution Engine v5.4  
**Status: COMPLETE — no blocking conflicts; 3 items flagged for Normalization**

---

## Record Inventory

| Entity Type | Count |
|-------------|-------|
| Site | 46 |
| Trail | 15 |
| Trail Network | 1 |
| Access Point | 17 |
| **Total** | **79** |

Tiers represented: 2, 3, 5, 6, 7, 8 (Tiers 1 and 4 returned null).

---

## Phase 1 — Grouping

All 79 records partitioned by `(entity_type, county_primary)`. All records carry `county_primary: Wayne County`. Multi-county records (Killbuck Marsh WA, Funk Bottoms WA, Sippo Valley Trail, Holmes County Trail) are also present in their partner counties' future discovery runs; they are processed here as Wayne County primary.

---

## Phase 2 — Duplicate Record ID Detection

**6 duplicate IDs found and resolved.**

During discovery, record IDs were recycled when the Rittman session (T6-021 through T6-026) was followed by Doylestown and Marshallville sessions that reused the same ID sequence. Resolved as follows:

| Original ID | First Occurrence (kept) | Second Occurrence → Renamed |
|-------------|------------------------|------------------------------|
| T6-021 | Martin Fritz Memorial Park (Rittman) | Memorial Park (Doylestown) → **T6-D-001** |
| T6-022 | First Street Ashton Hall Park (Rittman) | Paridon Park (Doylestown) → **T6-D-002** |
| T6-023 | Central Park (Rittman) | Gilcrest Park (Doylestown) → **T6-D-003** |
| T6-024 | E.J. Young Grand View Park (Rittman) | Robert Brooker Nature Preserve (Marshallville) → **T6-M-001** |
| T6-025 | Washington Street Park (Rittman) | Marshallville Tigers Trail → **T6-M-002** |
| T6-026 | William J. Robertson Nature Preserve (Rittman) | Dwayne Groll Trail → **T6-M-003** |

All renamed records have been updated in the YAML. No entity identity conflict — these are entirely distinct entities discovered in different municipalities.

**Post-resolution: 0 duplicate record IDs.**

---

## Phase 3 — Identity Matching

No cross-tier duplicates detected. The "same name" hits from the regex scan were false positives (truncated names: "Brown" matched both T2-001 and T2-005 due to name truncation; "Vulture" matched T8-002, T8-TR-001, and T8-AP-002 — all are correctly distinct entity types within the same parent complex).

No merger candidates identified. All 79 records are distinct entities.

---

## Phase 4 — Scope and County Validity

**T5 records (Chippewa Township):** T5-001, T5-002, T5-003 are valid. The Tier 5 "null" in session memory referred to the other 14 townships. Chippewa Township actively manages Chippewa Township Nature Preserve (17500 Galehouse Rd, Doylestown, 24–25 acres), confirmed via chippewatwp.com. Records are correctly scoped.

**Multi-county records:** 4 records span Wayne County plus adjacent counties.

| Record | Name | Counties |
|--------|------|---------|
| T2-004 | Killbuck Marsh Wildlife Area | Wayne + Holmes |
| T2-012 | Funk Bottoms Wildlife Area | Wayne + Ashland |
| T7-002 | Sippo Valley Trail | Wayne + Stark |
| T7-004 | Holmes County Trail | Wayne + Holmes |

These records are correctly flagged `multi_county: true` and will be held in the cross-county resolution queue until partner counties are processed.

---

## Phase 5 — Parent Reference Validation

No orphaned parent references. All child entities referencing parent IDs (T2-005 → T2-001, T2-006 → T2-002, T2-007 → T2-004, T3-002 → T3-001, T3-003 → T3-001, T5-002 → T5-001, T5-003 → T5-001, T6-002 → T6-001, T6-006 → T6-005, T6-M-002 → T6-M-001, T6-M-003 → T6-M-001, T8-TR-001 → T8-002) resolve to records present in this run.

Trail-to-network relationships (T7-001 through T7-004 → T7-TN-001) all resolve correctly.

---

## Phase 6 — GPS Audit

During this pass, a systematic GPS backfill was performed. The raw discovery YAML had captured GPS in `map_verification_status` notes but not always written them to `gps_lat_raw` / `gps_lon_raw` fields. All 79 records now have GPS populated.

**GPS status by source:**

| Count | Source |
|-------|--------|
| 52 | Google Maps place listing or address geocode |
| 11 | GPS inherited from parent site/access point |
| 9 | Satellite right-click verification |
| 4 | Area-coordinate approximation (primitive pull-offs, not Maps-indexed) |
| 3 | Address geocode (Chippewa Township Nature Preserve — approximate) |
| **79** | **Total** |

**4 records flagged for field verification (GPS-APPROXIMATE, area coordinate only):**
- T2-010 — Killbuck Marsh, Carrie Lane Parking Area
- T2-011 — Killbuck Marsh, Wright Marsh Parking (OH-226)
- T5-001 — Chippewa Township Nature Preserve (address geocode, no Maps pin)
- T5-002 / T5-003 — inherit from T5-001

These will pass to Normalization as GPS-APPROXIMATE; flagged in `map_verification_status`.

---

## Resolution Flags for Normalization

Three items are passed forward to Normalization as conflicts to resolve:

**Flag N-001 — T3-002 entity type ambiguity**  
Record T3-002 (Koehler's Pond at Barnes Preserve) is staged as a `Site` but may be better classified as an `Access Point` or a site feature rather than a standalone site. Normalization should evaluate against the Site vs. Access Point routing rules.

**Flag N-002 — T5-002 identity uncertain**  
Chippewa Township Nature Preserve trails (T5-002) has `IDENTITY_UNCERTAIN` in its identity_notes_raw — source describes "several short hiking trails" with no individual names. This may resolve to a single unnamed trail or multiple unnamed segments. Normalization should route to `held` pending field verification unless the single-trail interpretation is adopted.

**Flag N-003 — T2-007 identity uncertain**  
Killbuck Marsh Wildlife Observation Trail (T2-007) has `IDENTITY_UNCERTAIN` — ODNR does not list this trail by name in any indexed source. Trail existence inferred from habitat type and multi-source description of viewing area. Normalization should apply the `identity_uncertain` hold pathway.

---

## Summary

| Check | Result |
|-------|--------|
| Total records | 79 |
| Duplicate IDs found | 6 |
| Duplicate IDs resolved | 6 |
| Merger candidates | 0 |
| Scope violations | 0 |
| Orphaned parent references | 0 |
| Records with GPS | 79 / 79 |
| GPS-APPROXIMATE records | 4 |
| Flags to Normalization | 3 |
| **Pass 1 outcome** | **CLEAN — ready for Normalization** |

**Next stage:** Normalization Engine v5.5
