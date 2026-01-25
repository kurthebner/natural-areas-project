# NATURAL AREAS PROJECT
# NORMALIZATION ENGINE v4.0
(Cross‑Entity Normalization Orchestrator for Resolved Entities)

The Normalization Engine v4.0 is the **orchestrator** that transforms
**Resolved Entities** into **Normalized Entities** ready for:

- Entity Graph Schema v4.0
- TSV Output Specifications v4.0

It sits between:

- Resolution Engine v4.0 (input)
- Entity Upsert Engine v4.0 (output)

This module defines:

- Engine responsibilities
- Cross‑entity normalization rules
- Per‑entity routing
- Validation requirements
- Integration with Schema & Vocabulary Modules
- Logging and provenance requirements

------------------------------------------------------------
# 1. PURPOSE

The Normalization Engine v4.0:

- Applies schema rules to all resolved entities
- Applies vocabulary rules to all controlled fields
- Applies formatting rules (including semicolon rules)
- Computes Derived Labels
- Validates integrity anchors
- Validates parent/child relationships
- Validates multi‑county normalization
- Produces normalized entity objects for all six entity types

It does **not**:

- Discover entities
- Resolve identity conflicts
- Merge entities
- Write TSVs directly

------------------------------------------------------------
# 2. INPUTS AND OUTPUTS

## 2.1 Inputs

- Resolved entity objects from Resolution Engine v4.0
- Schema Modules v4.0 (6)
- Vocabulary Modules v4.0 (6)
- Normalization Contracts v4.0 (6)
- Discovery Metadata v4.0 (for provenance and context)

## 2.2 Outputs

- Normalized entity objects (one per entity)
- Normalization provenance records
- Validation results (warnings, errors)
- Objects ready for Entity Upsert Engine v4.0

------------------------------------------------------------
# 3. ENGINE WORKFLOW (HIGH‑LEVEL)

For each resolved entity:

1. Determine entity type (Site, Trail, Trail Segment, Trail Network, Site Network, Access Point).
2. Route to the appropriate **Normalization Contract v4.0**.
3. Apply:
   - Schema validation
   - Vocabulary normalization
   - Formatting normalization
   - Derived Label computation
   - Integrity anchor validation
   - Multi‑county normalization
   - Parent/child validation
4. Produce a normalized entity object.
5. Log normalization provenance.
6. Pass normalized entity to Entity Upsert Engine v4.0.

------------------------------------------------------------
# 4. CROSS‑ENTITY NORMALIZATION RULES

These rules apply to **all six entity types**.

## 4.1 Schema Validation

- All required fields must be present.
- Field types must match Schema Modules v4.0.
- Unknown fields must be ignored or logged as warnings.

## 4.2 Vocabulary Normalization

- All vocabulary‑governed fields must:
  - Map to a controlled value
  - Preserve raw value in provenance if mapping is lossy
- Unmappable values:
  - Must be logged
  - Must not be silently coerced

## 4.3 Formatting Rules

- Semicolon‑delimited lists:
  - Must be trimmed
  - Must not contain empty segments
  - Must be alphabetized where required (e.g., county_list)
- Blank fields:
  - Must be true blanks (no placeholders)

## 4.4 Derived Label Computation

- Each entity type has a **Derived Label** rule in its Normalization Contract.
- Derived Label must:
  - Be deterministic
  - Use normalized fields only
  - Be stable across runs given identical inputs

## 4.5 Integrity Anchors

- Each entity type has one or more integrity anchors (e.g., name + county_list).
- Anchors must:
  - Be present
  - Be valid
  - Be logged in normalization provenance

## 4.6 Multi‑County Normalization

- `county_list` must be:
  - Semicolon‑delimited
  - Alphabetized
  - Derived from resolved county set
- No entity may be duplicated per county.

## 4.7 Parent/Child Validation

- Parent Site relationships must:
  - Respect Child Site Rules Module v4.0
  - Not create cycles
  - Not create self‑parenting

- Access Point parents must:
  - Reference valid entities
  - Use allowed parent types (Site, Trail, Trail Segment)

------------------------------------------------------------
# 5. PER‑ENTITY NORMALIZATION ROUTING

## 5.1 Sites

- Use **Site Normalization Contract v4.0**.
- Normalize:
  - Category, Subtype
  - Ownership, Management, Coordination
  - Access Level
  - County list
  - Parent Site
  - Features, Description
  - GPS, Plus Code

## 5.2 Trails

- Use **Trail Normalization Contract v4.0**.
- Normalize:
  - Trail Type
  - Use, Surface, Origin
  - County list
  - Length
  - GPS, Plus Code

## 5.3 Trail Segments

- Use **Trail Segment Normalization Contract v4.0**.
- Normalize:
  - Segment Type
  - Segment Role
  - Parent Trail
  - County list
  - Length
  - GPS, Plus Code

## 5.4 Trail Networks

- Use **Trail Network Normalization Contract v4.0**.
- Normalize:
  - Network Type
  - County list
  - Ownership, Management, Coordination
  - GPS

## 5.5 Site Networks

- Use **Site Network Normalization Contract v4.0**.
- Normalize:
  - Network Type
  - County list
  - Ownership, Management, Coordination
  - GPS

## 5.6 Access Points

- Use **Access Point Normalization Contract v4.0**.
- Normalize:
  - Access Point Type
  - Access Level
  - County list
  - Address
  - GPS, Plus Code
  - Parent relationships

------------------------------------------------------------
# 6. ERROR HANDLING AND LOGGING

## 6.1 Non‑Fatal Errors

- Missing optional fields
- Unmappable vocabulary values
- Minor formatting issues

→ Log as warnings in normalization provenance.

## 6.2 Fatal Errors

- Missing required fields
- Invalid field types
- Broken integrity anchors
- Invalid parent references

→ Entity is rejected for upsert, logged as error, and flagged in Audit & Logging.

## 6.3 Provenance

For each entity, record:

- Normalization run ID
- Fields modified
- Vocabularies applied
- Formatting corrections
- Integrity anchor status
- Errors and warnings

------------------------------------------------------------
# 7. INTEGRATION POINTS

The Normalization Engine v4.0 integrates with:

- Resolution Engine v4.0 (input)
- Schema Modules v4.0 (validation)
- Vocabulary Modules v4.0 (controlled values)
- Normalization Contracts v4.0 (per‑entity rules)
- Entity Graph Schema v4.0 (output shape)
- Entity Upsert Engine v4.0 (consumer)
- Audit & Logging Module v4.0 (provenance)

------------------------------------------------------------
# 8. VERSIONING

- This module is **Normalization Engine v4.0**.
- Any change to cross‑entity rules requires v4.1, v4.2, etc.

------------------------------------------------------------
# END OF NORMALIZATION ENGINE v4.0