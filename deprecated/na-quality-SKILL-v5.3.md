---
name: na-quality
description: Quality assurance, integrity checks, error handling, audit logging, and manual review for the Natural Areas Project. Triggers on quality check, integrity check, audit, errors, review queue, conflicts, or pipeline failures.
---

# Natural Areas Project — Quality Skill v5.3

Covers integrity validation, error handling, conflict resolution, audit logging, and manual review workflows.

## TSV Integrity Check v5.2

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

Reference: `na_tsv_integrity_check_v5.2.md`

## Vocabulary Compliance Audit (IMP-085)

### Vocabulary Source Rule

All vocabulary used for compliance checks must be loaded from the current authoritative vocabulary modules — **never hardcoded** in audit scripts. Before running any compliance check, read the vocabulary module for each entity type:

- Sites: `na_site_vocabulary_v5.5.md`
- Trails: `na_trail_vocabulary_v5.1.md`
- Access Points: `na_access_point_vocabulary_v5.3.md`

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
- Access Point missing GPS after GPS Acquisition
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

**Resolution options for each queued pair:**
- `merged` — combine into single entity, upsert
- `split` — confirm distinct entities, upsert both with distinct anchors
- `dismissed` — one record is wrong, discard it, upsert the other

## Conflict Handling

Conflicts recorded by Resolution Engine are preserved through normalization and stored in `entity_conflicts` table. Normalization resolves conflicts using:
- Tier precedence (Tier 1 > Tier 2 > ... > Tier 8 > Tier 0)
- Source authority
- Discovery path

Unresolved conflicts after normalization go to manual review.

## Audit Logging

All pipeline events logged to `run_metadata` and provenance tables:
- `discovery_provenance` — source URLs, tier, field mappings
- `resolution_provenance` — merge decisions, similarity scores, conflicts
- `normalization_provenance` — vocabulary mappings, GPS results, GIS results, integrity anchor status

All provenance tables are append-only. Never overwrite prior run records.

## Quality Targets

- Discovery coverage: 95%+ of known entities in a county
- Required field completeness: 100%
- Vocabulary compliance: 98%+
- TSV delimiter integrity: 100%
- GPS coverage (Sites): 90%+ after GPS Acquisition
- GPS coverage (Access Points): 85%+ after GPS Acquisition

## Common Failure Patterns

**Discovery failures:**
- Skipping small villages without map verification
- Using search snippets instead of fetching full pages
- Marking villages complete when browser unavailable (must mark PENDING/UNVERIFIED)
- Not documenting null tier results with evidence
- Recording GPS from map pins without authoritative source confirmation

**Pipeline failures:**
- Trailing spaces in TSV fields
- Placeholder values in blank fields
- Counties not alphabetized
- Derived Label present for Trail, Trail Segment, Trail Network, or Site Network (must not exist)
- `gps_raw` field present (retired — use `gps_lat_raw` and `gps_lon_raw`)
- `notes_raw` field present (retired — use `identity_notes_raw`)
- `maps_raw` field present (retired — use `urls_raw`)

## Cross-County Entity Quality Notes

Cross-county networks (metropark systems, national trail networks, heritage areas) will appear as held entities after a single county run. This is correct behavior, not a quality failure. Flag in the session log and handoff document. Do not attempt to force-resolve member IDs from incomplete data.
