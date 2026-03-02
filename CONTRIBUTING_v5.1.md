# NATURAL AREAS PROJECT — CONTRIBUTING v5.1
Internal contribution protocol for a two-person, high-discipline, ontology-driven
system. This document defines how Skippy and Claude maintain, update, and evolve
the Natural Areas System v5.x without architectural drift.

This is not a community document.
It is an internal engineering contract.

------------------------------------------------------------
# CHANGES FROM v5.0

- Updated header version to v5.1
- §4 Editing Rules: added cross-module reference convention (v5.x suffix)
- §4 Editing Rules: added versioned filename convention
- §7 Manifest: clarified when manifest update is required
- §9 Versioning: added v5.x cross-reference suffix rule
- Module count updated to 52

------------------------------------------------------------
# CHANGES FROM v3.2.2

- Updated for v5.0 architecture
- "Copilot" replaced by "Claude" throughout
- Added v5.0-specific editing rules (township/municipality, GPS, raw fields)
- Added skills system as the active module-loading mechanism
- Added Resolution Rules Module to the change cascade table
- Processing Orchestration Module added to cascade table
- Version bumped to v5.0

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
   Example: "We need to update the Trail Segment Identity Rule because X."

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
   Required only if the module inventory changes (new module, retired module,
   moved module). Minor version increments within v5.x do not require manifest
   changes — the manifest is version-agnostic within the v5 family.

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

### Cross-module reference convention
All references from one module to another must use the **v5.x suffix**, not a
specific version number. For example:

  Correct:   "See Discovery Protocol Module v5.x"
  Incorrect: "See Discovery Protocol Module v5.3"

This ensures references remain valid as individual modules increment independently.
The only exception is within a module's own changelog, where specific prior versions
may be named (e.g., "supersedes v5.2").

### Versioned filename convention
Module filenames carry their exact current version number. For example:

  na_state_discovery_subproc_v5.2.md

When a module is updated, the file is renamed to the new version. The previous
version is moved to /deprecated. The manifest uses v5.x suffixes and does not
track specific filenames.

### Discovery changes
If you change discovery output structure, also update:
- Discovery Output Spec
- Discovery Metadata Spec
- All relevant discovery sub-procedures

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
GPS fields are gps_lat_raw and gps_lon_raw at discovery stage (string, as found).
Normalized fields are gps_lat and gps_lon (numeric, WGS84 decimal degrees).
If GPS handling changes, update:
- Schema module
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
| Pipeline stage change | Processing Orchestration Module |
| New module | Module Manifest, README, CONTRIBUTING |
| Retired module | Module Manifest, README |
| Moved module | Module Manifest, README |

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
- No adding new entity types without architectural review
- No modifying discovery tier order without updating the protocol
- No modifying schema field order without updating TSV specs
- No populating `township` or `municipality` during discovery
- No normalization decisions during discovery
- No using specific version numbers in cross-module references (use v5.x)

------------------------------------------------------------
# 8. HOW WE COMMUNICATE CHANGES

- **Skippy:** "We need to update X because Y."
- **Claude:** Generates the full updated module.
- **Skippy:** Reviews and installs.

No PRs, no branches, no ceremony — disciplined, explicit collaboration.

------------------------------------------------------------
# 9. VERSIONING

Every module is versioned independently using the format v5.N where N increments
with each update.

- **Major** — breaking change (e.g., v6.0)
- **Minor** — new rules or clarifications
- **Patch** — formatting or non-semantic edits

Cross-module references always use the **v5.x suffix** regardless of a module's
specific current version. This decouples references from version churn.

The manifest is version-agnostic within the v5 family — it does not require
updates for minor version increments.

------------------------------------------------------------
# 10. SKILLS SYSTEM

The v5.x system uses Claude's custom skills feature for module loading.
The five skills are:

| Skill | Purpose |
|-------|---------|
| `na-complete-system` | End-to-end orchestration |
| `na-discovery-workflow` | All discovery modules |
| `na-schema-vocabulary` | Schemas and vocabularies |
| `na-normalization-output` | Normalization and TSV output |
| `na-processing-quality` | Processing, audit, resolution, best practices |

When modules are updated, the corresponding skill references must be updated.
Skills are maintained by Skippy; Claude generates updated module content.
Skills files are not counted as modules and are not tracked in the manifest.

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
- Systematic completeness (systematic beats smart)

This CONTRIBUTING document exists to protect those principles.

------------------------------------------------------------
# END OF CONTRIBUTING v5.1
