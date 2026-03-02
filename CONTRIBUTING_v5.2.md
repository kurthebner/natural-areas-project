# NATURAL AREAS PROJECT — CONTRIBUTING v5.2
Internal contribution protocol for a two-person, high-discipline,
ontology-driven system. This document defines how Skippy and Claude
maintain, update, and evolve the Natural Areas System v5.x without
architectural drift.

This is not a community document.
It is an internal engineering contract.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- Updated for v5.1 architectural changes
- GPS raw field section updated: gps_lat_raw / gps_lon_raw are the
  authoritative raw field names
- Raw field renames documented: notes_raw → identity_notes_raw,
  url_all → urls_raw, url_primary → url_primary_raw
- identity_notes field added to raw field change rules
- maps field simplification documented
- GPS Acquisition stage added to change cascade table
- Derived Label removal documented in forbidden changes
- Processing module count updated to 5
- Discovery wrapper module count updated to 5 (resolution engine
  moved to /processing)
- Version bumped to v5.1

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- Updated for v5.0 architecture
- "Copilot" replaced by "Claude" throughout
- Added v5.0-specific editing rules (township/municipality, GPS,
  raw fields)
- Added skills system as the active module-loading mechanism
- Added Resolution Rules Module to the change cascade table
- Processing Orchestration Module added to cascade table

------------------------------------------------------------
# 1. PURPOSE

This document ensures that all changes:

- Preserve the six-entity ontology
- Preserve module boundaries
- Preserve determinism
- Preserve version integrity
- Avoid duplication of rules
- Avoid architectural drift
- Maintain full auditability

It defines how Skippy and Claude collaborate on system evolution.

------------------------------------------------------------
# 2. CONTRIBUTORS

There are only two contributors:

- **Skippy** — system architect, domain expert, steward of ontology
- **Claude** — system executor, module generator, consistency enforcer

No other contributors exist or will exist.

------------------------------------------------------------
# 3. HOW WE MAKE CHANGES

All changes follow this sequence:

1. **Identify the correct module**
   Never place a rule in more than one module.
   Never place a rule in the wrong module.

2. **State the change explicitly**
   Example: "We need to update the Trail Segment Identity Rule
   because X."

3. **Claude generates the updated module**
   Always as a full replacement.
   Never as a diff.

4. **Skippy reviews for correctness**
   Checks for:
   - Ontological alignment
   - Boundary correctness
   - No duplication
   - No drift

5. **Skippy installs the updated module**
   Via the skills system or local repository.
   Claude never edits skills files directly.

6. **Increment the module version**
   - Major = breaking change
   - Minor = new rules, clarifications, expansions
   - Patch = formatting or typo

7. **Update the manifest**
   Required if filenames or module counts change.

------------------------------------------------------------
# 4. EDITING RULES

These rules prevent cascading breakage.

### General rules
- Never invent data
- Never add rules to multiple modules
- Never change TSV field order
- Never change delimiter rules
- Never populate `township` or `municipality` during discovery —
  GIS-derived only
- Never collect `township` or `municipality` in any `_raw` field
- Never store Derived Label — it is a presentation-layer concern
  and must not appear in any schema, normalization contract, or
  TSV output spec

### Discovery changes
If you change discovery output structure, also update:
- Discovery Output Spec
- Discovery Metadata Spec
- All relevant entity and tier discovery sub-procedures

### Schema changes
If you change schema fields, also update:
- Schema module
- Normalization module for that entity
- TSV Output Spec for that entity
- TSV Integrity Check
- Vocabulary module (if the field is vocabulary-governed)

### Vocabulary changes
If you change vocabulary values, also update:
- Vocabulary module
- Normalization contract for that entity

### GPS changes
GPS raw fields are `gps_lat_raw` and `gps_lon_raw` (string at
discovery). Normalized fields are `gps_lat` and `gps_lon` (numeric,
WGS84 decimal degrees).
If GPS handling changes, update:
- Schema module
- Entity discovery sub-procedure
- Normalization Engine
- Entity-specific normalization module
- GPS Acquisition Module
- TSV Output Spec

### Raw field changes
If you add or remove a `_raw` field, update:
- Schema module
- Entity discovery sub-procedure
- Entity normalization module
- TSV Output Spec
- Vocabulary module (if vocabulary-governed after normalization)

**Authoritative raw field names (v5.1):**
- Identity clarifications: `identity_notes_raw`
  (previously `notes_raw` — do not use old name)
- All URLs: `urls_raw`
  (previously `url_all` — do not use old name)
- Primary URL: `url_primary_raw`
  (previously `url_primary` — do not use old name)
- Map URLs: `maps_raw` — plain semicolon-delimited URL list;
  no type or description metadata

### maps field changes
The maps field is a plain semicolon-delimited URL list at all
stages — discovery, normalization, and TSV output. If maps
handling changes, update:
- Entity discovery sub-procedure
- Entity normalization module
- TSV Output Spec

------------------------------------------------------------
# 5. CHANGE CASCADE TABLE

Use this table to identify which modules must be updated together.

| Change Type | Must Also Update |
|-------------|-----------------|
| New schema field | Normalization, TSV Spec, Vocabulary (if enum), Integrity Check |
| Removed schema field | Normalization, TSV Spec, Integrity Check |
| New vocabulary value | Vocabulary, Normalization |
| Removed vocabulary value | Vocabulary, Normalization |
| New discovery raw field | Discovery sub-proc, Discovery Output Spec, Schema |
| Discovery output format change | Discovery Output Spec, Metadata Spec, All sub-procs |
| Entity-type rule change | Resolution Rules Module |
| Category edge case | Resolution Rules Module |
| Pipeline stage change | Processing Orchestration Module, README |
| GPS Acquisition change | GPS Acquisition Module, Processing Orchestration Module |
| New module | Module Manifest, README, CONTRIBUTING |
| Retired module | Module Manifest, README |

------------------------------------------------------------
# 6. TESTING CHANGES

After any change, verify:

- Discovery still produces valid raw output
- Resolution still identifies entities correctly
- All six normalization contracts align with schema
- TSV outputs match specs
- Delimiter integrity passes
- Audit logs capture all decisions
- Manifest reflects reality

If any check fails, the change is incomplete.

------------------------------------------------------------
# 7. FORBIDDEN CHANGES

These are absolute:

- No invented data
- No silent corrections
- No silent exclusions
- No cross-module duplication
- No storing or computing Derived Label
- No adding new entity types without architectural review
- No modifying discovery tier order without updating the protocol
- No modifying schema field order without updating TSV specs
- No populating `township` or `municipality` during discovery
- No normalization decisions during discovery
- No type or description metadata in maps_raw entries

------------------------------------------------------------
# 8. HOW WE COMMUNICATE CHANGES

- **Skippy:** "We need to update X because Y."
- **Claude:** Generates the full updated module.
- **Skippy:** Reviews and installs.

No PRs, no branches, no ceremony — disciplined, explicit
collaboration.

------------------------------------------------------------
# 9. VERSIONING

Every module is versioned independently.

- **Major** — breaking change
- **Minor** — new rules or clarifications
- **Patch** — formatting or non-semantic edits

The manifest must always reflect current module versions.

------------------------------------------------------------
# 10. SKILLS SYSTEM

The v5.x system uses Claude's custom skills feature for module
loading. The five skills are:

| Skill | Purpose |
|-------|---------|
| `na-complete-system` | End-to-end orchestration |
| `na-discovery-workflow` | All discovery modules |
| `na-schema-vocabulary` | Schemas and vocabularies |
| `na-normalization-output` | Normalization and TSV output |
| `na-processing-quality` | Baseline, audit, resolution, best practices |

When modules are updated, the corresponding skill references must
be updated. Skills are maintained by Skippy; Claude generates
updated module content.

------------------------------------------------------------
# 11. PHILOSOPHY

This project is built on:

- Determinism
- Transparency
- Ontological rigor
- Zero improvisation
- Zero duplication
- Zero drift
- Explicit reasoning
- Document-driven architecture
- Collection-decision separation (Discovery = Collection,
  Normalization = Decisions)

This CONTRIBUTING document exists to protect those principles.

------------------------------------------------------------
# END OF CONTRIBUTING v5.2
