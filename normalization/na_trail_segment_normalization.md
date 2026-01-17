# NATURAL AREAS PROJECT — TRAIL SEGMENT NORMALIZATION CONTRACT v3.1
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Trail Segment Raw Candidate Records into fully normalized Trail Segment entities
under the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Segment Vocabulary Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Trail Segment discoveries are normalized
- How each Trail Segment Schema v3.1 field is populated
- How Segment Type, Surface, Status, and Use are validated
- How parent Trail relationships are validated
- How geometry, GPS, Plus Code, and URL rules are applied
- How multi‑county segments are normalized
- How Derived Label is constructed (if required by TSV)
- How normalization integrates with the Audit & Logging Module
- How conflicts and uncertainties are surfaced to the Resolution Module

This module is authoritative for Trail Segment normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record
From Discovery Output Specification v3.1, including:

- name_raw (segment name or identifier)
- parent_trail_raw
- county, township, municipality
- surface_raw, status_raw, use_raw
- gps_raw, geometry_raw
- length_raw
- url_primary, url_all
- source_datasets, source_maps, source_gis_layers
- notes_raw
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata

## 2.2 Discovery Metadata
From Discovery Metadata Specification v1.0, including:

- Identity metadata
- Tier metadata
- Source metadata
- Conflict metadata
- Uncertainty metadata
- Boundary metadata
- Baseline metadata

## 2.3 Vocabulary Modules
- Trail Segment Vocabulary Module v3.1
  - Segment Types
  - Segment Surfaces
  - Segment Uses
  - Segment Status

## 2.4 Schema Modules
- Trail Segment Schema Module v3.1
- Trail Schema Module v3.1 (for parent validation)
- Trail Network Schema Module v3.1 (for associations)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Trail Segment entity conforming to the Trail Segment Schema Module v3.1
- A record ready for export via the Trail Segment TSV Output Specification v3.1
- Full audit trail entries via the Audit & Logging Module v1.1

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize segment name  
4. Normalize parent Trail  
5. Normalize Segment Type, Surface, Use, Status  
6. Normalize jurisdiction fields  
7. Normalize geometry and GPS  
8. Normalize length  
9. Normalize Trail Network associations  
10. Normalize notes  
11. Normalize URLs and sources  
12. Validate multi‑county logic  
13. Construct Derived Label (if required)  
14. Apply formatting rules  
15. Emit normalized Trail Segment entity  

If any critical step fails → surface to Resolution Module v3.1.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Segment Name

### Rules
- Use name_raw exactly as discovered, with minimal whitespace cleanup.
- If multiple authoritative names/IDs exist → choose the most authoritative.
- Alternate names go in Description.
- Never invent names.
- Never infer names from geometry or map labels alone.

### Audit
- Log all name conflicts.
- Log all corrections.

------------------------------------------------------------
## 5.2 Parent Trail

### Rules
- Required.
- Must match the exact normalized name of a Trail entity.
- If parent Trail is not yet normalized → create a placeholder Trail for Resolution.
- Never infer parentage from proximity or geometry alone.
- A Trail Segment must have exactly one parent Trail.

### Audit
- Log all parent conflicts.
- Log unverifiable parent relationships.

------------------------------------------------------------
## 5.3 Segment Type

### Rules
- Must match a value from the Segment Type vocabulary.
- Examples: “Named Segment,” “Numbered Segment,” “Operational Section,” “GIS‑Defined Segment.”
- Never infer from surface or status.
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.4 Surface

### Rules
- Must match vocabulary values.
- Semicolon‑delimit if multiple surfaces documented.
- Never infer from imagery alone.

------------------------------------------------------------
## 5.5 Use

### Rules
- Must match vocabulary values.
- Semicolon‑delimit if multiple.
- Never infer from signage or amenities alone.

------------------------------------------------------------
## 5.6 Status

### Rules
- Must match vocabulary values.
- “Closed” = permanently closed.
- “Proposed” must be officially referenced.
- Never infer from imagery.

------------------------------------------------------------
## 5.7 Description

### Rules
- 1–3 sentences.
- Must describe identity‑defining characteristics of the segment.
- Include naming history and alternate identifiers.
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.8 Length (Miles)

### Rules
- Numeric only.
- No units.
- Never estimate.
- Leave blank if unknown.

------------------------------------------------------------
## 5.9 County

### Rules
- Required.
- Must match official Ohio county list.
- Semicolon‑delimit if multi‑county.
- Alphabetical order.
- Omit the word “County.”

------------------------------------------------------------
## 5.10 Township & Municipality

### Rules
- Must match authoritative jurisdiction names.
- Semicolon‑delimit if multiple.
- Must not include county names.
- If many jurisdictions → use jurisdiction of Address (if present).

------------------------------------------------------------
## 5.11 GPS Coordinates

### Rules
- Format: lat,lon (no space).
- Accept only authoritative coordinates.
- Reject placeholders, centroids, or unverifiable coordinates.
- Leave blank if verification fails.

------------------------------------------------------------
## 5.12 Geometry

### Rules
- Use geometry_raw exactly as discovered.
- Do not simplify, smooth, or infer geometry.
- Preserve coordinate precision.
- If geometry is malformed → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.13 Plus Code

### Rules
- Generate only from accepted GPS.
- If GPS blank → Plus Code blank.

------------------------------------------------------------
## 5.14 Trail Network Membership

### Rules
- Use parent_trail_systems from raw record.
- Must match normalized Trail Network names.
- Semicolon‑delimit if multiple.
- Never infer membership.
- If ambiguous → flag uncertainty.

------------------------------------------------------------
## 5.15 Notes

### Rules
- Optional free‑text.
- Must not include identity‑defining characteristics.
- Must not include internal features or Access Point details.
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.16 URL

### Rules
- Full https:// URLs only.
- Semicolon‑delimit if multiple.
- Must be authoritative.
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.17 Derived Label (computed, not stored)

### Formula
Segment Type + " Segment"

### Rules
- Must be derived solely from normalized fields.
- Log all construction steps.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail Segment spanning multiple counties must produce one normalized record per county.
- Each record must:
  - Use the same segment name
  - Use county‑specific jurisdiction fields
  - Preserve all metadata
- Boundary metadata must reflect all counties traversed.

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- All vocabulary‑controlled fields
- GPS format
- Geometry validity
- Plus Code generation
- Semicolon formatting
- Field order
- No invented data
- Blank fields are true blanks
- No delimiter characters inside fields

If any field fails validation:
- Surface the issue
- Do not silently correct

------------------------------------------------------------
# 8. DELIMITER‑INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between delimiters
- No trailing spaces
- No collapsed delimiters
- No missing or extra delimiters

All anomalies must be logged.

------------------------------------------------------------
# 9. CONFLICT RESOLUTION RULES

### 9.1 Conflicting Names or Identifiers
- Use the most authoritative source.
- Record alternates in Description.

### 9.2 Conflicting Length
- Use the most authoritative source.
- If conflict persists → Resolution.

### 9.3 Conflicting Surface, Use, or Status
- Use authoritative trail system sources.
- If unclear → Resolution.

### 9.4 Conflicting Geometry
- Preserve all geometry claims in metadata.
- Use the most authoritative geometry for normalization.
- If unclear → Resolution.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer parent Trail, designation, or length.
- Never generate GPS or geometry without verification.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must:

- Record all sources used
- Record conflicts
- Record unverifiable claims
- Record normalization decisions
- Record Derived Label construction
- Record delimiter‑integrity validation
- Never overwrite user‑provided data without surfacing the change

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Vocabulary Module v3.1
- Trail Segment Schema Module v3.1
- Trail Schema Module v3.1
- TSV Output Specification (Trail Segments) v3.1
- Discovery Protocol Module v3.1
- Discovery Output Specification v3.1
- Discovery Metadata Specification v1.0
- Resolution Module v3.1
- Audit & Logging Module v1.1
- Processing / Orchestration Module v3.1

------------------------------------------------------------
# END OF TRAIL SEGMENT NORMALIZATION CONTRACT v3.1