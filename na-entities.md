---
name: na-entities
description: Compact reference for all six Natural Areas Project entity types — schemas, identity anchors, parent rules, key fields, and vocabulary pointers. Triggers on entity type questions, field definitions, schema reference, what counts as a site/trail/network, or identity questions.
---

# Natural Areas Project — Entities Reference Skill v5.3

Compact reference for all six entity types. For full field definitions read the relevant Schema Module v5.x.

## Core Ontology Rules

- **Trails are not Sites** — a named trail is always a Trail, never a Site
- **Access Points are never Sites** — trailheads, parking areas, boat launches are Access Points
- **Segments are not Trails** — Trail Segments are identity-bearing subdivisions of Trails
- **Networks are not physical land units** — networks are collections, not places
- **Features are not entities** — playgrounds, shelters, overlooks are Features unless explicitly identity-bearing
- **No inference** — identity must never be inferred from layout, proximity, GIS geometry, or marketing language
- **Governance ≠ Identity** — ownership and management do not determine entity type

## Entity Type Definitions

### Site
A named, bounded, identity-bearing land unit recognized by authoritative sources.
- Child Sites are Sites with a `parent_site_id`
- Category must be explicitly documented — never inferred from ecology
- Schema: `na_site_schema.md` | Vocabulary: `na_site_vocabulary.md`

### Trail
A named, linear, identity-bearing route.
- Schema: `na_trail_schema.md` | Vocabulary: `na_trail_vocabulary.md`

### Trail Segment
A named or identity-bearing subdivision of a Trail.
- Must have a parent Trail
- Schema: `na_trail_segment_schema.md` | Vocabulary: `na_trail_segment_vocabulary.md`

### Trail Network
A documented collection of Trails with a shared identity.
- Must be explicitly documented as a network — cannot be inferred from proximity or shared governance
- Schema: `na_trail_network_schema.md` | Vocabulary: `na_trail_network_vocabulary.md`

### Site Network
A documented collection of Sites with a shared identity.
- Must be explicitly documented as a network with system-level identity
- When uncertain, flag with `SITE_NETWORK_UNCERTAIN` in identity_notes_raw
- Schema: `na_site_network_schema.md` | Vocabulary: `na_site_network_vocabulary.md`

### Access Point
A visitor-facing entrance associated with one or more parent entities.
- Includes: trailheads, parking areas, boat launches, documented entrances
- Has exactly one identity parent (Site, Trail, or Trail Segment)
- May have additional non-identity parents in `access_point_parents` table
- Schema: `na_access_point_schema.md` | Vocabulary: `na_access_point_vocabulary.md`

## Identity Anchors (used for deduplication)

| Entity Type | Identity Anchor |
|-------------|----------------|
| Site | Fuzzy-normalized name + county overlap |
| Trail | Fuzzy-normalized name + county overlap |
| Trail Segment | Parent trail match + segment name (if named) |
| Access Point | Identity parent match + GPS proximity bucket (lat/lon rounded to 3 decimal places) |
| Trail Network | Fuzzy-normalized network name + network type |
| Site Network | Fuzzy-normalized network name + network type |

## Key Field Notes (v5.2)

**GPS fields**: `gps_lat_raw` and `gps_lon_raw` (separate fields). `gps_raw` is retired.
**Notes field**: `identity_notes_raw` replaces `notes_raw`.
**Maps field**: Plain semicolon-delimited URL list. Rich array format is retired.
**Derived Label**: Removed from all entity types. No entity type computes or stores a Derived Label.
**Organizational model** (four-tier, all entity types):
- `ownership` — legal title holder
- `governance` — managing organization(s)
- `partner_agencies` — formal documented co-operators; must not duplicate ownership/governance
- `coordination` — community-based, volunteer, advisory, or informal partners

## TSV Field Counts (v5.2)

| Entity Type | Fields | Tab Delimiters |
|-------------|--------|----------------|
| Site | 25 | 24 |
| Trail | 19 | 18 |
| Trail Segment | 17 | 16 |
| Trail Network | 17 | 16 |
| Site Network | 15 | 14 |
| Access Point | 17 | 16 |

## Parent/Child Rules

**Site parent/child**:
- Child Sites must be named, identity-bearing, documented, and internal to parent
- No features, temporary labels, habitat types, or administrative zones as child sites
- Child Site counties must be a subset of parent counties (unless documented otherwise)
- No circular parent relationships

**Access Point parents**:
- Identity parent: exactly one — Site, Trail, or Trail Segment
- Additional parents stored in `access_point_parents` relationship table
- Site Networks and Trail Networks are never valid Access Point parents

**Trail Segments**:
- Must have exactly one parent Trail

**Held-Entity Children (IMP-086)**:
When a parent entity is held (pending cross-county resolution), its children are also held:
- Any Access Point whose identity parent is a held entity → held with `hold_reason = "parent_held"`. Not rejected — correctly structured, waiting for cross-county run.
- Any child Site whose `parent_site_id` references a held Site → held with `hold_reason = "parent_held"`.
- Trail Networks with `member_trail_ids` referencing held Trails → network is **not** held; dangling member references log as INFO and resolve at cross-county run. Do not flag as WARNING.
- Held children are listed in `held_entities` alongside their parent; `hold_detail` must reference the parent's `entity_id`.
---
# END OF NA_ENTITIES_SKILL
