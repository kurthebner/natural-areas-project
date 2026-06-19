---
name: na-normalization-output
description: Normalizes raw natural areas discovery data and generates TSV output files. Triggers when normalizing, exporting, or validating natural areas data, or when TSV output or database import is mentioned.
---

# Natural Areas Normalization & Output v5.0

Transforms raw discovery data into clean, normalized entities and standardized TSV output files.

## Core Principle

**Discovery = Collection. Normalization = Decisions.**

All field decisions, vocabulary enforcement, conflict resolution, GPS derivation, and GIS-derived township/municipality assignment happen here — never during discovery.

## Normalization Workflow

```
Raw Discovery Output
  → Resolution Engine
  → Entity-Specific Normalization
  → GIS Derivation (township, municipality)
  → Entity Upsert Engine
  → TSV Output Generation
  → Integrity Check
```

Start here: `view references/na_normalization_engine_v5.md`

## Entity-Specific Normalization

Read for each entity type being normalized:

- `references/na_site_normalization_v5.md`
- `references/na_trail_normalization_v5.md`
- `references/na_trail_segment_normalization_v5.md`
- `references/na_access_point_normalization_v5.md`
- `references/na_trail_network_normalization_v5.md`
- `references/na_site_network_normalization_v5.md`

## Processing Engines

- `references/na_normalization_engine_v5.md` — orchestrator; read first
- `references/na_entity_upsert_engine_v5.md` — insert/update logic

## TSV Output Specifications

Read before generating each file:

- `references/na_tsv_output_site_v5.md`
- `references/na_tsv_output_trail_v5.md`
- `references/na_tsv_output_trail_segment_v5.md`
- `references/na_tsv_output_access_point_v5.md`
- `references/na_tsv_output_trail_network_v5.md`
- `references/na_tsv_output_site_network_v5.md`

After all files generated: `view references/na_tsv_integrity_check_v5.md`

## Key v5.0 Normalization Rules

- `township` and `municipality` are GIS-derived — never populated from discovery data
- `gps_lat` and `gps_lon` are separate numeric fields (WGS84 decimal degrees)
- `role_raw` and `access_level_raw` are removed — do not normalize these fields
- `member_count` and `member_site_ids` populated here for Site Networks
- Arrays serialized as semicolon-delimited strings in TSV

## TSV Format Requirements

- Tab-delimited, UTF-8 encoding
- Empty string for NULL (not "NULL")
- No embedded tabs or newlines in field content
- Arrays as semicolon-delimited strings

## Quality Targets

- Required field completeness: 100%
- Vocabulary compliance: 98%+
- Referential integrity: 99%+
- TSV integrity: 100%
