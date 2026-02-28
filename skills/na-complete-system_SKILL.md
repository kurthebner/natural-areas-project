---
name: na-complete-system
description: End-to-end Natural Areas Project v5.0 for county discovery, normalization, and TSV output of parks, trails, and natural areas. Triggers on county discovery, full pipeline, bootstrap, or cataloging.
---

# Natural Areas Complete System v5.0

End-to-end system for natural areas discovery, cataloging, and data management across U.S. counties.

## Core Principle

**Discovery = Collection. Normalization = Decisions.**

Raw fields collected during discovery exactly as found. All normalization, vocabulary enforcement, and GIS derivation happen after discovery is complete.

## System Architecture

**Six-Entity Ontology**: Sites, Trails, Trail Segments, Trail Networks, Site Networks, Access Points
**Eight-Tier Discovery**: Federal → State → District → County → Township → Municipal → Conservancy → Private
**Four-Stage Pipeline**: Discovery → Resolution → Normalization → Output

## Quick Start — Full County Project

1. **Bootstrap**: Load na-processing-quality skill, establish baseline, initialize session, create staging file (`{county}_{state}_raw_discovery.yaml`) and skill revision notes file (`{county}_{state}_skill_revision_notes.md`)
2. **Discover**: Load na-discovery-workflow skill, execute 8 tiers in order, append all raw records to staging file
3. **Resolve**: Run Resolution Engine (na-processing-quality skill)
4. **Normalize**: Load na-normalization-output skill, apply entity rules, run GIS spatial join for township/municipality
5. **Output**: Generate 6 TSV files, run integrity check
6. **Audit**: Generate quality report

## Skill Routing

| Task | Skill |
|------|-------|
| Entity schemas and field definitions | na-schema-vocabulary |
| Discovery — any tier, any entity type | na-discovery-workflow |
| Normalization, TSV output, validation | na-normalization-output |
| Bootstrap, baseline, audit, resolution | na-processing-quality |
| Database schema, SQL, triggers, upserts | na-database |

## Key v5.0 Changes from v4.0

- `township` and `municipality` never populated during discovery — GIS-derived only
- `gps_primary` split into `gps_lat` + `gps_lon` (numeric)
- `features_raw`, `difficulty_raw`, `accessibility_raw`, `maps_raw` added
- `role_raw` and `access_level_raw` removed from Access Points
- County Baseline runs as Tier-0 (after tiers 1-8, not before)
- Discovery Log and Normalization Log are strictly separate

## Quality Targets

- Discovery coverage: 95%+
- Required field completeness: 100%
- Vocabulary compliance: 98%+
- TSV integrity: 100%

## System Principles

- Exhaustive beats efficient: complete every tier 100% before advancing
- Fetch beats search: always web_fetch official pages, never rely on snippets
- View maps directly: open Google Maps and view — do not search for map references
- Document negatives: record "no parks found" with evidence, never assume

## Reference Documents

`view README_v5.md` — full architecture overview
`view na_module_manifest_v5.md` — complete module list (55 modules)
`view CONTRIBUTING_v5.md` — change protocols
