---
name: na-schema-vocabulary
description: Provides entity schemas and controlled vocabularies for Natural Areas Project v5.0. Triggers on entity structure, field definitions, valid values, data models, or entity types like Site or Trail.
---

# Natural Areas Schema and Vocabulary v5.0

Authoritative entity definitions and controlled vocabularies for the six-entity Natural Areas ontology v5.0.

## Six Entity Types

1. **Site** — Parks, preserves, forests, wildlife areas, recreation areas
2. **Trail** — Named trails within or across sites
3. **Trail Segment** — Distinct sections of trails with differing surface, management, or condition
4. **Trail Network** — Collections of related trails under unified governance or branding
5. **Site Network** — Collections of related sites (e.g., county park district, municipal park system)
6. **Access Point** — Parking areas, trailheads, entrances, boat launches

## Key v5.0 Schema Changes

- `gps_primary` split into `gps_lat` + `gps_lon` (numeric, WGS84)
- `township_raw` and `municipality_raw` do not exist — GIS-derived only, never collected
- `features_raw` added to Sites and Access Points
- `difficulty_raw` and `accessibility_raw` added to Trails and Trail Segments
- `maps_raw` added to Trails, Trail Segments, Trail Networks, Site Networks
- `role_raw` and `access_level_raw` removed from Access Points
- `network_affiliation` removed from all entities — use relationship tables
- `member_count` and `member_site_ids` added to Site Networks
- `member_trail_count` and `member_trail_ids` added to Trail Networks
- `segment_type` added to Trail Segments (optional)

## Schema References

- `references/na_site_schema_v5.md`
- `references/na_trail_schema_v5.md`
- `references/na_trail_segment_schema_v5.md`
- `references/na_access_point_schema_v5.md`
- `references/na_trail_network_schema_v5.md`
- `references/na_site_network_schema_v5.md`

## Vocabulary References

- `references/na_site_vocabulary_v5.md`
- `references/na_trail_vocabulary_v5.md`
- `references/na_trail_segment_vocabulary_v5.md`
- `references/na_access_point_vocabulary_v5.md`
- `references/na_trail_network_vocabulary_v5.md`
- `references/na_site_network_vocabulary_v5.md`

## Entity Relationships

- Site → Child Sites: via `parent_site_id`
- Trail → Segments: Segment carries `parent_trail_id`
- Site → Site Network: via `site_network_members` relationship table + `member_site_ids`
- Trail → Trail Network: via `trail_network_members` relationship table + `member_trail_ids`
- Access Point → Site/Trail/Segment: via `identity_parent_entity_type` + `identity_parent_entity_id`
