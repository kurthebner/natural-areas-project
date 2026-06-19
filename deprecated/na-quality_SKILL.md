---
name: na-quality
description: Quality assurance, integrity checks, error handling, audit logging, and manual review for the Natural Areas Project. Triggers on quality check, integrity check, audit, errors, review queue, conflicts, or pipeline failures.
---

# Natural Areas Project — Quality Skill v5.3

Covers integrity validation, error handling, conflict resolution, audit logging, manual review workflows, and post-pipeline content audit.

## TSV Integrity Check v5.3

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

Reference: `na_tsv_integrity_check_v5.3.md`

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

## Post-Pipeline Content Audit

Run after every county pipeline completion, before closing the session. These checks are in addition to the TSV Integrity Check and address content quality issues confirmed across multiple counties.

### Features Field Audit (Sites and Access Points)

**1. Activity prohibition check**
Query: any `features` value that is a pure activity with no physical infrastructure equivalent.

Activities that must NOT appear in `features`: Hiking, Fishing, Hunting, Horseback Riding, Mountain Biking, Swimming, Boating, Paddling, Kayaking, Canoeing, Wildlife Viewing, Birdwatching, Mushroom Foraging, Nature Study, Wildflower Study, Rock Climbing, Cross-Country Skiing, Snowshoeing, Geocaching, Photography.

Remediation: drop the activity term. If a physical infrastructure feature that enables the activity is documented (e.g., Fishing → Fishing Area, Paddling → Watercraft Access), use that vocabulary term instead. Document activity availability in `notes`.

**2. Operational detail prohibition check**
The following must NOT appear in `features`: hours of operation, parking descriptions, permit/reservation requirements, access policies, seasonal closure notes, event listings, facility sub-detail annotations (e.g., "Shelter A: near bathrooms, electrical outlets").

Remediation: move to `notes`. Permit-required status belongs in `status` ("Access Permit Required"). Physical features retain their identity (e.g., "Picnic Shelter") but must carry no operational annotation.

**3. Named entity prohibition check**
Named Trail entities, named Trail Segment entities, and named Access Point entities must NOT appear in `features`. Example violations: "Stone Quarry Trail", "Allan W. Eckert Trail", "Main Trailhead". Generic infrastructure descriptors are permitted: "Hiking Trail", "Bridle Trail", "Mountain Bike Trail", "Trailhead".

Remediation: remove named entity references from `features`. Express trail containment via `trail_parents` table (see Trail Parents Audit below).

**4. Vocabulary compliance check**
Every semicolon-delimited token in `features` must exactly match a value in Site Vocabulary §6.2 (current: v5.4). Pipe-delimited values, underscore-separated lowercase values, and any other format indicate a normalization failure — `features_raw` was written to `features` directly.

Remediation: re-run features normalization using `features_raw` as input for all affected records. If `features_raw` is absent for some records, flag them for manual review.

**5. Semicolon delimiter and alphabetical order check**
Multi-value `features` must use semicolon delimiters (not commas, pipes, or slashes) and values must be in alphabetical order.

### Description Field Audit (Sites)

Run a spot-check on descriptions, especially for newly normalized records. Flag any description that:
- Opens with "A [N]-acre [category]..." or "Located in [township/municipality]..."
- Re-states the site name verbatim
- Contains only information already in name, category, subtype, acres, counties, location, township, or municipality fields

Remediation: edit to remove redundant opener and retain only identity-defining content. If no identity-defining content remains after removing redundant content, blank the description entirely. A blank description is preferable to a wholly redundant one.

### Notes Field Audit (Sites)

Scan `notes` for pipeline provenance contamination:
- Tier markers: "TIER 2 MISS", "TIER 6", etc.
- Cross-reference markers: "[entity_id] pending", "see SC-T-0001"
- Discovery run markers: "batch 3 of 5", "discovered 2026-03-21"

Remediation: move identity-bearing clarifications to `identity_notes`. Move pipeline metadata to provenance tables (do not surface in any user-visible field). Drop all other pipeline markers.

### Trail Parents Audit (Trails)

After pipeline, verify `trail_parents` population for all Trail entities in the county:

1. For every Trail with `governance` matching a Site in the same county: confirm whether the trail is wholly contained within that site's geographic boundary. If yes and governance aligns, a `trail_parents` row is required.
2. Extra-limital trails (crossing multiple sites or governance units) must NOT have a `trail_parents` row.
3. Every Trail with a `trail_parents` row must have `identity_notes` containing: "Contained within [Site Name] ([site_id])."
4. No Trail should appear in `trail_parents` with more than one `parent_site_id`.

**SQL query to find contained trails missing a `trail_parents` row:**
```sql
SELECT t.trail_id, t.name, t.governance
FROM trails t
LEFT JOIN trail_parents tp ON t.trail_id = tp.trail_id
WHERE tp.trail_id IS NULL
ORDER BY t.trail_id;
```
Manually review results: extra-limital trails with no row are correct; contained trails with no row need a row added.

**SQL query to verify identity_notes alignment:**
```sql
SELECT t.trail_id, t.name, t.identity_notes, tp.parent_site_id
FROM trails t
JOIN trail_parents tp ON t.trail_id = tp.trail_id
WHERE t.identity_notes NOT LIKE '%Contained within%'
ORDER BY t.trail_id;
```

### Audit Checklist Summary

Before closing a county session, confirm:
- [ ] `features` contains no activity terms
- [ ] `features` contains no operational detail
- [ ] `features` contains no named Trail or AP entities
- [ ] All `features` tokens are vocabulary-compliant (Site Vocabulary v5.4 §6.2)
- [ ] All `features` values are semicolon-delimited and alphabetical
- [ ] No `description` field opens with a redundant acreage/category/location statement
- [ ] No `notes` field contains pipeline provenance metadata
- [ ] All wholly-contained trails have a `trail_parents` row
- [ ] All extra-limital trails have no `trail_parents` row
- [ ] All `trail_parents` trails have correct "Contained within..." identity_notes

## Cross-County Entity Quality Notes

Cross-county networks (metropark systems, national trail networks, heritage areas) will appear as held entities after a single county run. This is correct behavior, not a quality failure. Flag in the session log and handoff document. Do not attempt to force-resolve member IDs from incomplete data.
