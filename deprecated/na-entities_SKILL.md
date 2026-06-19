---
name: na-entities
description: Compact reference for all six Natural Areas Project entity types — schemas, identity anchors, parent rules, key fields, and vocabulary pointers. Triggers on entity type questions, field definitions, schema reference, what counts as a site/trail/network, or identity questions.
---

# Natural Areas Project — Entities Reference Skill v5.2

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
- Schema: `na_site_schema_v5.x.md` | Vocabulary: `na_site_vocabulary_v5.x.md`

### Trail
A named, linear, identity-bearing route.
- Schema: `na_trail_schema_v5.x.md` | Vocabulary: `na_trail_vocabulary_v5.x.md`

### Trail Segment
A named or identity-bearing subdivision of a Trail.
- Must have a parent Trail
- Schema: `na_trail_segment_schema_v5.x.md` | Vocabulary: `na_trail_segment_vocabulary_v5.x.md`

### Trail Network
A documented collection of Trails with a shared identity.
- Must be explicitly documented as a network — cannot be inferred from proximity or shared governance
- Schema: `na_trail_network_schema_v5.x.md` | Vocabulary: `na_trail_network_vocabulary_v5.x.md`

### Site Network
A documented collection of Sites with a shared identity.
- Must be explicitly documented as a network with system-level identity
- When uncertain, flag with `SITE_NETWORK_UNCERTAIN` in identity_notes_raw
- Schema: `na_site_network_schema_v5.x.md` | Vocabulary: `na_site_network_vocabulary_v5.x.md`

### Access Point
A visitor-facing entrance associated with one or more parent entities.
- Includes: trailheads, parking areas, boat launches, documented entrances
- Has exactly one identity parent (Site, Trail, or Trail Segment)
- May have additional non-identity parents in `access_point_parents` table
- Schema: `na_access_point_schema_v5.x.md` | Vocabulary: `na_access_point_vocabulary_v5.x.md`

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
**Derived Label**: Removed from Trails, Trail Segments, Trail Networks, Site Networks. Retained for Sites and Access Points only.
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

## Multi-County Rules

- Entities spanning multiple counties are single entities — never segmented by county
- All counties recorded in `counties` field as semicolon-delimited alphabetized list
- No entity duplicated per county in TSV output
- Counties must not be inferred from GIS or proximity — only documented counties

## Access Point GPS Policy

- GPS is required for statewide database inclusion
- Access Points with missing GPS are held, not rejected
- GPS Acquisition Module (Stage 3) handles missing coordinates
- TSV Integrity Check flags any Access Point with blank GPS promoted to statewide dataset
