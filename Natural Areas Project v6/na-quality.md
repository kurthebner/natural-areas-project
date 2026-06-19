---
name: na-quality
description: Quality assurance, integrity checks, error handling, audit logging, and manual review for the Natural Areas Project v6. Triggers on quality check, integrity check, audit, errors, review queue, conflicts, or pipeline failures.
---

# Natural Areas Project — Quality Skill v6.0

Covers integrity validation, error handling, conflict resolution, audit logging, and manual review workflows.

## TSV Integrity Check

Run before every database upsert. A single failing row halts the pipeline.

**Delimiter requirements (exact):**

| Entity Type | Fields | Tabs Required |
|---|---|---|
| Site | 31 | 30 |
| Trailthing | 31 | 30 |
| Site Network | 18 | 17 |
| Access Point | 20 | 19 |

**Cross-entity reference pairing rule**: Every field that references another entity by ID must be immediately followed by a field containing that entity's human-readable name. Both must be blank together or populated together. A mismatch (ID present, name blank; or name present, ID blank) is an integrity failure.

**A row fails if:**
- Delimiter count is wrong
- Any field contains a tab or newline character
- A blank field contains spaces or placeholder values (NULL, N/A, _, "")
- Any field has leading or trailing whitespace
- Any anchor field is misaligned or blank
- ID/name pairs are out of sync
- Counties not semicolon-delimited and alphabetized
- Any entity attempts multi-row expansion
- Access Point county field has multiple values (APs resolve to a single primary county)

Reference: `output/na_tsv_integrity_check_v6.0.md`

## Vocabulary Compliance Audit

### Vocabulary Source Rule

All vocabulary used for compliance checks must be loaded from the current authoritative vocabulary modules — **never hardcoded**. Before running any compliance check, read the vocabulary module for each entity type:

- Sites: `na_site_vocabulary.md`
- Trailthings: `na_trailthing_vocabulary.md`
- Site Networks: `na_site_network_vocabulary.md`
- Access Points: `na_access_point_vocabulary.md`

### Free-Text Field Exclusion Rule

The following fields have no controlled vocabulary and must **never** be checked against a vocabulary list:

- All entity types: `accessibility`, `identity_notes`, `notes`, `description`
- Site: `habitat_type` (open vocabulary in v6.x — no controlled list yet)
- Site: `access_notes` (free text)
- Trailthing: `source_term`, `source_hierarchy_context` (verbatim; never normalized)
- Access Point: `features` (AP vocabulary has no controlled vocabulary for AP features)

### Empty TSV Rule

An empty TSV file (zero data rows, header row only) is **expected behavior** for entity types not present in a given county. Flag only if the TSV file is missing entirely.

### Held-Parent Access Point FK Rule

When checking AP parent FK integrity:
- If the AP's parent `entity_id` appears in `held_entities` → classify as **WARNING** ("parent held — will resolve cross-county")
- If absent from both the live graph and `held_entities` → classify as **FATAL** (dangling FK)

---

## Error Classification

**Warnings** (pipeline continues):
- Unmappable vocabulary values
- Minor formatting issues
- Plus Code computation failures
- GIS lookup failures with valid GPS
- Member IDs referencing entities not yet in graph
- Trailthing `source_term` blank (logged as WARN; non-blocking)

**Fatal Errors — Rejections** (entity rejected):
- Missing required fields
- Invalid field types
- Broken integrity anchors
- Invalid parent references (cycles, self-parenting)
- GPS out of valid range when required
- IMP-063 FATAL REJECT (category value with no valid mapping)

**Held** (entity valid but incomplete):
- Site or Access Point missing GPS after GPS Acquisition (GPS Gate, IMP-069)
- Site Network with unresolved member IDs
- Entity with parent not yet in graph

---

## Manual Review Queue

Entities routed to `manual_review_queue` when:
- Two normalized entities share the same integrity anchor (collision)
- Resolution flagged a near-match but did not auto-merge
- High-confidence fields (name, category, GPS) disagree materially with existing graph entity
- Parent Site missing for a Trailthing or child Site with `parent_site_missing` flag

### County Mismatch Review (IMP-067)

Entities flagged `county_mismatch` appear in the manual review queue when GPS places them outside their documented `counties` value. Three resolution options:

1. **Confirm GPS county** — update `counties`; correct entity ID prefix via cascading update
2. **Confirm documented county** — GPS is wrong; close flag, add explanation to `identity_notes`
3. **Multi-county** — entity spans county lines; add GPS county to `counties` if missing

These are not fatal errors — the entity proceeds with its current `counties` value.

---

## PAD-US Completeness Gate (IMP-088)

Run after the pipeline closes a county (post-upsert). Cross-checks discovered entities against the Protected Areas Database of the United States (PAD-US).

**Data source**: https://www.usgs.gov/programs/gap/pad-us (free download)
Filter to county bounding box. Use `Unit_Nm` and `Mng_Agency` fields for matching.

**Procedure:**
1. Load PAD-US records intersecting the county bbox
2. Fuzzy name match against NAP `sites` table (token-set ratio ≥ 80)
3. Unmatched → `manual_review_queue` with `flag='padus_unmatched'`

**Resolving flags:**
1. **Confirmed miss** — discovery defect; add to handoff for remediation
2. **Name mismatch** — entity exists under a different name; close flag, note in `identity_notes`
3. **Out of scope** — management unit, private land, or NAP-excluded; close flag with explanation

PAD-US flags do not block upsert.

---

## Parks & Open Space Completeness Gate (IMP-097)

Run after PAD-US gate for MORPC-covered counties. Catches local and municipal parks that PAD-US misses.

**Covered counties**: DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI

**File**: `Parks_and_Open_Space_*.csv` (v6 project root)
Filter: `County = [current county]` and `Status = "Public"`. Exclude `Sub_Type = "NOS"`.

**Procedure:**
1. Load records for county with `Status = "Public"`
2. Fuzzy name match against NAP `sites` table (token-set ratio ≥ 80), filtered to same jurisdiction
3. Unmatched → `manual_review_queue` with `flag='parks_os_unmatched'` and `source='parks_and_open_space_gis'`

**Resolving flags:** Same three outcomes as PAD-US.

**Limitations:**
- No GPS coordinates in this file
- Sub_Type vocabulary differs from NAP — do not map directly
- `Sub_Type = "NOS"` entries are planning designations, not sites — exclude

---

## AP Deduplication Audit (IMP-019)

After 10 or more counties have been run under v6.x protocols, run a deduplication audit on the `access_points` table. GPS proximity was removed from the AP identity anchor in v6.0 — this audit confirms no duplicates are accumulating.

```sql
-- Find AP pairs sharing a parent and GPS location (within ±0.001°)
SELECT a.name, a.access_point_id, b.name, b.access_point_id,
       a.gps_lat, a.gps_lon
FROM access_points a
JOIN access_points b ON a.access_point_id < b.access_point_id
WHERE ABS(a.gps_lat - b.gps_lat) < 0.001
  AND ABS(a.gps_lon - b.gps_lon) < 0.001
  AND EXISTS (
    SELECT 1 FROM access_point_parents ap1
    JOIN access_point_parents ap2 ON ap1.parent_entity_id = ap2.parent_entity_id
    WHERE ap1.access_point_id = a.access_point_id
      AND ap2.access_point_id = b.access_point_id
  );
```

If duplicates are found: assess whether GPS proximity should be reintroduced as a secondary deduplication pass or whether stricter name matching resolves the issue.

---
# END OF NA_QUALITY_SKILL
