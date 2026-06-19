# NATURAL AREAS PROJECT — CONTRIBUTING v6.0
Internal contribution protocol for a two-person, high-discipline,
ontology-driven system. This document defines how Skippy and Claude
maintain, update, and evolve the Natural Areas System v6.x without
architectural drift.

This is not a community document.
It is an internal engineering contract.

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- Updated for v6.0 architectural changes: four entity types, Trailthing
  unified entity, new Site fields, single resolution pass, single GPS gate
- Change cascade table updated: Trail/Segment/Network rows removed;
  Trailthing row added
- Forbidden changes updated: no classification of Trailthings; no use of
  external_parent_id/external_parent_type (use parent_site_network_id)
- Skills system updated to reflect five v6 skills
- Discovery Output Specification retirement documented
- Document collection system added to discovery change rules

------------------------------------------------------------
# 1. PURPOSE

This document ensures that all changes:

- Preserve the four-entity v6 ontology
- Preserve the Trailthing no-classification mandate
- Preserve module boundaries
- Preserve determinism
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
   Example: "We need to update the Trailthing Identity Anchor because X."

3. **Claude generates the updated module**
   Full replacement for substantial changes; Edit tool for targeted changes.

4. **Skippy reviews for correctness**
   Checks for:
   - Ontological alignment
   - Boundary correctness
   - No duplication
   - No drift

5. **Increment the module version**
   - Major = breaking change
   - Minor = new rules, clarifications, expansions
   - Patch = formatting or typo

6. **Update the manifest**
   Required whenever module versions change or modules are added/retired.

------------------------------------------------------------
# 4. EDITING RULES

These rules prevent cascading breakage.

### General rules
- Never invent data
- Never add rules to multiple modules
- Never change TSV field order
- Never change delimiter rules
- Never populate `township` or `municipality` during discovery — GIS-derived only
- Never collect `township` or `municipality` in any `_raw` field
- Never classify a Trailthing as trail, trail segment, or trail network
- Never use `external_parent_id` or `external_parent_type` — use
  `parent_site_network_id` / `parent_site_network_raw`

### Discovery changes
If you change discovery output structure, also update:
- Discovery Metadata Spec
- All relevant entity and tier discovery sub-procedures
- CLAUDE.md raw record templates (§6)

### Schema changes
If you change schema fields, also update:
- Schema module
- Normalization module for that entity
- TSV Output Spec for that entity
- TSV Integrity Check
- Vocabulary module (if the field is vocabulary-governed)
- Discovery Metadata Spec §15 raw field preservation section
- CLAUDE.md raw record template for that entity type

### Vocabulary changes
If you change vocabulary values, also update:
- Vocabulary module
- Normalization contract for that entity
- `na_vocab_constants_v6.py`

### GPS changes
GPS raw fields are `gps_lat_raw` and `gps_lon_raw`. Normalized fields are
`gps_lat` and `gps_lon` (numeric, WGS84 decimal degrees). If GPS handling
changes, update:
- GPS Acquisition Module
- Processing Orchestration Module
- Entity-specific normalization module
- TSV Output Spec

### Trailthing parent field changes
The three Trailthing parent fields are `parent_id` (parent Trailthing),
`site_parent_id` (parent Site), and `parent_site_network_id` (parent Site
Network). If these change, update:
- Trailthing Schema Module
- Trailthing Discovery Sub-Procedure (raw record template)
- Trailthing Normalization Contract
- Trailthing TSV Output Spec
- TSV Integrity Check
- Resolution Engine
- Entity Upsert Engine
- Discovery Metadata Spec §15.2

### Document collection changes
If the document log format or naming convention changes, update:
- Discovery Orchestration Module §4
- Discovery Metadata Spec §7
- CLAUDE.md §6
- na-bootstrap skill
- na-discovery skill

------------------------------------------------------------
# 5. CHANGE CASCADE TABLE

| Change Type | Must Also Update |
|---|---|
| New schema field | Normalization, TSV Spec, Vocabulary (if enum), Integrity Check, Discovery Metadata Spec §15, CLAUDE.md |
| Removed schema field | Normalization, TSV Spec, Integrity Check |
| New vocabulary value | Vocabulary, Normalization, na_vocab_constants_v6.py |
| Removed vocabulary value | Vocabulary, Normalization, na_vocab_constants_v6.py |
| New discovery raw field | Discovery sub-proc, Discovery Metadata Spec, Schema |
| Trailthing parent field change | Trailthing Schema, Discovery sub-proc, Normalization, TSV Spec, Integrity Check, Resolution Engine, Upsert Engine, Discovery Metadata Spec §15.2 |
| Entity-type rule change | Resolution Rules Module |
| Category edge case | Resolution Rules Module |
| Pipeline stage change | Processing Orchestration Module, README, na-pipeline skill |
| GPS Acquisition change | GPS Acquisition Module, Processing Orchestration Module, na-pipeline skill |
| New module | Module Manifest, README, CONTRIBUTING |
| Retired module | Module Manifest, README |
| Skill update | Skills changelog (na_skills_changelog.md if maintained) |

------------------------------------------------------------
# 6. TESTING CHANGES

After any change, verify:

- Discovery still produces valid raw output for all four entity types
- Resolution still identifies entities correctly (single pass)
- All four normalization contracts align with schemas
- TSV outputs match specs (field counts: Site 31, Trailthing 31, Site Network 18, AP 20)
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
- No classifying Trailthings as trail, trail segment, or trail network
- No use of `external_parent_id` / `external_parent_type` — retired in v6
- No adding new entity types without architectural review
- No modifying discovery tier order without updating the protocol
- No modifying schema field order without updating TSV specs
- No populating `township` or `municipality` during discovery
- No normalization decisions during discovery
- No GPS inference or estimation

------------------------------------------------------------
# 8. HOW WE COMMUNICATE CHANGES

- **Skippy:** "We need to update X because Y."
- **Claude:** Generates the full updated module or targeted edit.
- **Skippy:** Reviews and confirms.

No PRs, no branches, no ceremony — disciplined, explicit collaboration.

------------------------------------------------------------
# 9. VERSIONING

Every module is versioned independently.

- **Major** — breaking change
- **Minor** — new rules or clarifications
- **Patch** — formatting or non-semantic edits

The manifest must always reflect current module versions.

------------------------------------------------------------
# 10. SKILLS SYSTEM

The v6.x system uses five operational skills:

| Skill | Purpose |
|---|---|
| `na-bootstrap` | County run initialization; session files, document log, MC entity check |
| `na-discovery` | Tier-based discovery (8 tiers); Trailthing no-classification; document collection |
| `na-entities` | Compact entity type reference; four types, anchors, parent rules |
| `na-pipeline` | Post-discovery pipeline (Stages 3–10); single resolution pass, single GPS gate |
| `na-quality` | QA, integrity checks, audit logging, PAD-US gate, AP deduplication audit |

Skills are maintained as `.md` files in the v6 project root. When modules are
updated, verify that skills referencing those modules do not become stale.

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
- Collection-decision separation (Discovery = Collection, Normalization = Decisions)
- Ecological priority — land character before amenity inventory
- Source vocabulary preservation — what the source says, verbatim

This CONTRIBUTING document exists to protect those principles.

------------------------------------------------------------
# END OF CONTRIBUTING v6.0
