---
name: na-quality
description: Quality assurance, integrity checks, error handling, audit logging, and manual review for the Natural Areas Project. Triggers on quality check, integrity check, audit, errors, review queue, conflicts, or pipeline failures.
---

# Natural Areas Project — Quality Skill v5.3

Covers integrity validation, error handling, conflict resolution, audit logging, and manual review workflows.

## TSV Integrity Check

Run before every database upsert. A single failing row halts the pipeline.

**Delimiter requirements (exact):**

| Entity Type | Fields | Tabs Required |
|-------------|--------|---------------|
| Site | 25 | 24 |
| Trail | 19 | 18 |
| Trail Segment | 17 | 16 |
| Trail Network | 17 | 16 |
| Site Network | 15 | 14 |
| Access Point | 17 | 16 |

**Field position anchors — key fields to verify:**

*Site:* Name→1, Counties→13, Municipality→14, Township→15, GPS Lat→16, GPS Lon→17, Plus Code→18, Features→19, Parent Site ID→23

*Trail:* Name→1, Counties→7, Difficulty→11, Accessibility→12, Identity Notes→15, Trail ID→19

*Trail Segment:* Parent Trail→1, Segment Name→2, Counties→3, Difficulty→9, Accessibility→10, Identity Notes→12, Geometry→16, Segment ID→17

*Trail Network:* Network Name→1, Counties→7, Identity Notes→13, Network ID→17

*Site Network:* Network Name→1, Counties→7, Identity Notes→12, Network ID→15

*Access Point:* Name→1, Parent Type→4, Parent Name→5, GPS Lat→10, GPS Lon→11, Plus Code→12, Features→13, Identity Notes→14, AP ID→17

**A row fails if:**
- Delimiter count is wrong
- Any field contains a tab or newline character
- A blank field contains spaces or placeholder values (NULL, N/A, _, "")
- Any field has leading or trailing whitespace
- Any anchor field is misaligned or blank
- Identity Notes is misaligned (all entity types)
- GPS Lat/Lon misaligned (Sites, Access Points)
- Plus Code misaligned (Sites, Access Points)
- Features misaligned (Sites, Access Points)
- Difficulty/Accessibility misaligned (Trails, Trail Segments)
- Geometry misaligned (Trail Segments)
- Counties not semicolon-delimited and alphabetized
- Any entity attempts multi-row expansion

Reference: `na_tsv_integrity_check.md`

## Vocabulary Compliance Audit (IMP-085)

### Vocabulary Source Rule

All vocabulary used for compliance checks must be loaded from the current authoritative vocabulary modules — **never hardcoded** in audit scripts. Before running any compliance check, read the vocabulary module for each entity type:

- Sites: `na_site_vocabulary.md`
- Trails: `na_trail_vocabulary.md`
- Access Points: `na_access_point_vocabulary.md`

Hardcoded vocabulary lists produce false positives (flagging valid terms absent from the hardcoded list) and false negatives (missing invalid terms added after the list was written). The authoritative module is always the source of truth.

### Free-Text Field Exclusion Rule

The following fields have **no controlled vocabulary** and must **never** be checked against a vocabulary list:

- Trail `accessibility` field
- Trail `identity_notes` field
- Trail Segment `accessibility` field
- Trail Segment `identity_notes` field
- Access Point `features` field (AP vocabulary §1 explicitly has no controlled vocabulary for AP features)
- Access Point `identity_notes` field
- Site `notes` field
- Site `description` field

Only fields that are explicitly designated as controlled in their vocabulary module may be checked. The controlled/free-text distinction for each field is documented in the vocabulary modules under their "Purpose" sections.

### Empty TSV Rule

An empty TSV file (zero data rows, header row only) is **expected behavior** for entity types not present in a given county — it is not a warning. Flag only if the TSV file itself is missing entirely:

- ✅ Correct: TSV file present, header row only → no flag
- ⚠️ Flag: TSV file missing from output entirely

### Held-Parent Access Point FK Rule

When checking AP parent FK integrity, cross-reference the `held_entities` table before classifying the error:

- If the AP's parent `entity_id` appears in `held_entities` → classify as **WARNING** (`"parent held — will resolve cross-county"`)
- If the AP's parent `entity_id` is absent from both the live graph and `held_entities` → classify as **FATAL** (dangling FK)

Do not reject APs with held parents — they are correctly structured entities waiting for cross-county resolution.


## Error Classification

**Warnings** (pipeline continues):
- Unmappable vocabulary values
- Minor formatting issues
- Plus Code computation failures
- GIS lookup failures with valid GPS
- Member IDs referencing entities not yet in graph

**Fatal Errors — Rejections** (entity rejected):
- Missing required fields
- Invalid field types
- Broken integrity anchors
- Invalid parent references (cycles, self-parenting)
- GPS out of valid range when required

**Held** (entity valid but incomplete):
- Site or Access Point missing GPS after GPS Acquisition (GPS Gate, IMP-069)
- Network with unresolved member IDs
- Entity with parent not yet in graph

## Manual Review Queue

Entities routed to `manual_review_queue` when:
- Two normalized entities share the same integrity anchor (collision)
- Resolution flagged a near-match but did not auto-merge
- High-confidence fields (name, category, GPS) disagree materially with existing graph entity

### County Mismatch Review (IMP-067)

Entities flagged `county_mismatch` appear in the manual review queue when HIGH or MED confidence GPS places them outside their documented `counties` value. Three resolution options:

1. **Confirm GPS county** — update `counties`; correct entity ID prefix via cascading update across all relationship tables in a single transaction (permitted before cross-county run completes; immutable after).
2. **Confirm documented county** — GPS is wrong or imprecise; close flag, keep `counties`, add explanation to `identity_notes`.
3. **Multi-county** — entity spans county lines; add GPS county to `counties` if missing, close flag.

These are not fatal errors — the entity proceeds to output with its current `counties` value regardless of the flag.

## PAD-US Completeness Gate (IMP-088)

Run after the pipeline closes a county (post-upsert). Cross-checks the county's discovered entities against the Protected Areas Database of the United States (PAD-US), a free USGS federal dataset covering all governance tiers with spatial and name data.

### Purpose

PAD-US provides an independent enumeration of protected areas. Comparing NAP output against PAD-US catches entities that were missed during discovery — particularly large, well-documented sites that should have been found.

### Data Source

- **PAD-US**: https://www.usgs.gov/programs/gap/pad-us (free download, GeoJSON or FGDB)
- Filter to the county bounding box using the county's `bbox` field from the pipeline config
- Use the `Unit_Nm` (unit name) and `Mng_Agency` (managing agency) fields for matching

### Procedure

1. Load all PAD-US records whose centroid or bounding box intersects the county bbox
2. For each PAD-US record, attempt a name match against the NAP `sites` table using fuzzy name matching (token-set ratio ≥ 80)
3. Records with no NAP match are flagged as **PAD-US unmatched** and written to `manual_review_queue` with `flag='padus_unmatched'`
4. Log: count of PAD-US records checked, count matched, count flagged

### Known Limitations

PAD-US coverage is uneven by governance tier:

| Tier | PAD-US Coverage | Supplemental Source |
|---|---|---|
| Tier 1–2 (Federal, State) | Strong | — |
| Tier 3 (District/Metropark) | Good | — |
| Tier 4 (County) | Moderate | County auditor parcel data |
| Tier 5 (Township) | Weak | Ohio Auditor parcel data |
| Tier 6 (Municipal) | Weak — small parks often absent | Ohio Auditor parcel data |
| Tier 7–8 (Conservancy, Private) | Sparse | Site-specific research |

For Tier 5–6 gaps, supplement with Ohio Auditor parcel data (ohioauditor.gov) — use the same `padus_unmatched` flag but note the source as `source='ohio_auditor'` in `manual_review_queue`.

### Resolving PAD-US Unmatched Flags

Three outcomes per flagged record:

1. **Confirmed miss** — entity was not discovered; add to handoff as a discovery defect for remediation
2. **Name mismatch** — entity exists in NAP under a different name; close flag, note in `identity_notes`
3. **Out of scope** — PAD-US record is a management unit (not a discrete site), private land, or otherwise excluded by NAP scope rules; close flag with explanation

PAD-US unmatched flags do not block upsert and do not affect entity status in the DB. They are review queue items only.

### Validation Note

Validate on Van Wert County first (IMP-088 decision) before applying to other counties. Van Wert has a small, well-bounded entity set (19 sites) that makes manual verification straightforward.

---

## Parks & Open Space Completeness Gate (IMP-097)

Run after the PAD-US gate for counties covered by the regional GIS layer. This gate catches local and municipal parks that PAD-US misses at Tier 5–6.

**Covered counties**: DEL, FAI, FAY, FRA, HOC, KNO, LIC, LOG, MAD, MAR, MRW, PER, PIC, ROS, UNI

### Purpose

`Parks_and_Open_Space_7241389496048841555.csv` (project root, updated July 2025) is an independent enumeration of parks and open spaces maintained by a regional GIS authority. It complements PAD-US by covering smaller municipal and township parks that PAD-US typically omits.

### Data Source

- **File**: `Parks_and_Open_Space_7241389496048841555.csv` (project root)
- **Fields used**: `Name`, `Jurisdiction`, `County`, `Type`, `Sub_Type`, `Status`, `Acres`
- **Filter**: `County = [current county abbreviation]` and `Status = "Public"`
- Exclude records where `Sub_Type = "NOS"` only (no-show/planning parcels — these are zoning designations, not sites)
- **All other Types are in scope**, including `CEMETERY` and `GOLF` — these are NAP-scope entities per IMP-099

### Procedure

1. Load all Parks & Open Space records for the county with `Status = "Public"` (excluding cemeteries and NOS sub-type)
2. For each record, attempt a name match against the NAP `sites` table using fuzzy name matching (token-set ratio ≥ 80), filtered to the same jurisdiction
3. Records with no NAP match are flagged as **P&OS unmatched** and written to `manual_review_queue` with `flag='parks_os_unmatched'` and `source='parks_and_open_space_gis'`
4. Log: count of records checked, count matched, count flagged

### Known Limitations

| Consideration | Note |
|---|---|
| No GPS coordinates | Cannot be used as a GPS fallback source — use MORPC centroids for Franklin County GPS |
| Sub_Type vocabulary differs from NAP | Do not map Sub_Type values directly to NAP category/subtype |
| Planning parcels | `Sub_Type = "NOS"` entries are planning designations, not sites — exclude |
| Cemeteries | In scope for NAP but may produce false positives if cemetery naming differs; review carefully |
| Coverage gaps | Private preserves and Tier 7–8 conservancy lands are sparse in this dataset |

### Resolving P&OS Unmatched Flags

Same three outcomes as PAD-US:

1. **Confirmed miss** — entity not discovered; add to handoff as a discovery defect for remediation
2. **Name mismatch** — entity exists in NAP under a different name; close flag, note in `identity_notes`
3. **Out of scope** — record is a planning parcel, management sub-unit, or otherwise excluded by NAP scope; close flag with explanation

P&OS unmatched flags do not block upsert. They are review queue items only.

---
# END OF NA_QUALITY_SKILL
