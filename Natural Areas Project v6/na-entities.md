---
name: na-entities
description: Compact reference for all four Natural Areas Project v6 entity types — schemas, identity anchors, parent rules, key fields, and vocabulary pointers. Triggers on entity type questions, field definitions, schema reference, what counts as a site/trailthing/network, or identity questions.
---

# Natural Areas Project — Entities Reference Skill v6.0

Compact reference for all four entity types. For full field definitions read the relevant Schema Module v6.x.

## Core Ontology Rules

- **Trailthings are not Sites** — a named trail-related entity is always a Trailthing, never a Site, regardless of location, governance, or naming
- **Access Points are never Sites** — trailheads, parking areas, boat launches are Access Points
- **Do not classify Trailthings** — never decide whether a Trailthing is a trail, trail segment, or trail network; capture `source_term_raw` verbatim and stop there (IMP-007)
- **Site Networks are not physical land units** — Site Networks are organizational collections of Sites, not physical places
- **Features are not entities** — playgrounds, shelters, overlooks are Features unless explicitly identity-bearing
- **No inference** — identity must never be inferred from layout, proximity, GIS geometry, or marketing language
- **Governance ≠ Identity** — ownership and management do not determine entity type

## Entity Type Definitions

### Site
A named, bounded, identity-bearing land unit recognized by authoritative sources.
- Child Sites are Sites with a `parent_site_id`
- Category must be explicitly documented — never inferred from ecology
- New v6 fields: `habitat_type` (ecological character), `access_notes` (access caveats), `last_verified_date`, `field_verified`
- Schema: `na_site_schema.md` | Vocabulary: `na_site_vocabulary.md`

### Trailthing
A named, identity-bearing trail-related entity — what was previously Trail, Trail Segment, or Trail Network.
- "Trailthing" is a working name carrying no hierarchical connotation
- The discoverer's job: capture `source_term_raw` verbatim and record parent relationships only when explicitly stated
- Classification (trail vs. segment vs. network) is deferred to after sufficient v6 county runs (IMP-007)
- May have: a parent Trailthing (`parent_id`), a Site parent (`site_parent_id`), a Site Network parent (`parent_site_network_id`)
- No GPS, Plus Code, township, or municipality — multi-location entity
- Schema: `na_trailthing_schema.md` | Vocabulary: `na_trailthing_vocabulary.md`

### Site Network
A named organization or designation that manages, coordinates, or encompasses two or more Sites.
- Must be explicitly documented — cannot be inferred from proximity or shared governance
- Four threshold rules determine when a record is created (keyed on org_type and network_type)
- Create SITE_NETWORK_PROVISIONAL at first member site encounter; remove when threshold met
- Schema: `na_site_network_schema.md` | Vocabulary: `na_site_network_vocabulary.md`

### Access Point
A visitor-facing entrance associated with one or more parent entities.
- Includes: trailheads, parking areas, boat launches, documented entrances
- Identity parents: Site and/or Trailthing (at least one required)
- Schema: `na_access_point_schema.md` | Vocabulary: `na_access_point_vocabulary.md`

## Identity Anchors (used for deduplication)

| Entity Type | Identity Anchor |
|---|---|
| Site | Fuzzy-normalized name + county overlap |
| Trailthing | Fuzzy-normalized name + county overlap (source term similarity contributes to signature but is not a prerequisite) |
| Access Point | Identity parent match + fuzzy-normalized name + county overlap (GPS proximity removed in v6) |
| Site Network | Fuzzy-normalized network name + network type |

## Key Field Notes (v6.0)

**GPS fields**: `gps_lat_raw` and `gps_lon_raw` (separate fields). Sites and APs: GPS required (GPS Gate). Trailthings and Site Networks: GPS optional; most are `gps_unresolvable` by nature.
**Trailthing source term**: `source_term_raw` is REQUIRED — verbatim term from authoritative source. Do not invent or normalize it.
**parent_site_network_raw**: The field for a Trailthing's Site Network parent. `external_parent_id`/`external_parent_type` are retired v5 names — do not use.
**New Site fields**: `habitat_type_raw` (ecological/natural character; open vocabulary), `access_notes_raw` (seasonal/access caveats), `last_verified_date` (date confirmed accurate), `field_verified` (boolean; physical visit only).
**Organizational model** (four-tier, all entity types):
- `ownership` — legal title holder
- `governance` — managing organization(s)
- `partner_agencies` — formal documented co-operators; must not duplicate ownership/governance
- `coordination` — community-based, volunteer, advisory, or informal partners

## TSV Field Counts (v6.0)

| Entity Type | Fields | Tab Delimiters |
|---|---|---|
| Site | 31 | 30 |
| Trailthing | 31 | 30 |
| Site Network | 18 | 17 |
| Access Point | 20 | 19 |

## Parent/Child Rules

**Site parent/child**:
- Child Sites must be named, identity-bearing, documented, and internal to parent
- No features, temporary labels, habitat types, administrative zones, or Trailthing-type entities as child Sites
- Child Site counties must be a subset of parent counties (unless documented otherwise)
- No circular parent relationships
- A child Site may itself have Trailthings, Access Points, and Site Network memberships

**Trailthing hierarchy**:
- A Trailthing may have at most one parent Trailthing (`parent_id`)
- Record parent_id only when the authoritative source explicitly frames the relationship
- A Trailthing contained within a Site uses `site_parent_id` — it is never a child Site
- A Trailthing that is an explicit member of a Site Network uses `parent_site_network_id`

**Access Point parents**:
- Identity parents: Site and/or Trailthing (at least one required)
- Site Networks and Trailthings-as-networks are never valid AP parents in the identity sense

**Held-Entity Children (IMP-086)**:
- Any Access Point whose identity parent is a held entity → held with `hold_reason = "parent_held"`
- Any child Site whose `parent_site_id` references a held Site → held with `hold_reason = "parent_held"`
- Any Trailthing whose `parent_id` references a held Trailthing → held with `hold_reason = "parent_held"`
- Site Networks with `member_site_ids` referencing held Sites → network is **not** automatically held; dangling member references log as INFO

---
# END OF NA_ENTITIES_SKILL
