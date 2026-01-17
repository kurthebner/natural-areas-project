# NATURAL AREAS PROJECT — SUB‑SITE NORMALIZATION CONTRACT v3.1
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Sub‑Site Raw Candidate Records into fully normalized Sub‑Site entities under the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Sub‑Site Vocabulary Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Sub‑Site discoveries are normalized
- How each Sub‑Site Schema v3.1 field is populated
- How Sub‑Site Type, Status, and Designation are validated
- How parent Site relationships are validated
- How geometry, GPS, Plus Code, and URL rules are applied
- How multi‑county Sub‑Sites are normalized
- How Derived Label is constructed (if required by TSV)
- How normalization integrates with the Audit & Logging Module
- How conflicts and uncertainties are surfaced to the Resolution Module

This module is authoritative for Sub‑Site normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record
From Discovery Output Specification v3.1, including:

- name_raw
- parent_site_raw
- subsite_type_raw
- county_raw, township_raw, municipality_raw
- gps_raw, geometry_raw
- url_primary, url_all
- notes_raw
- description_raw
- source_datasets, source_maps, source_gis_layers
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
- Sub‑Site Vocabulary Module v3.1
  - Sub‑Site Types
  - Sub‑Site Status (if defined)
  - Sub‑Site Designations (if defined)

## 2.4 Schema Modules
- Sub‑Site Schema Module v3.1
- Site Schema Module v3.1 (for parent validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Sub‑Site entity conforming to the Sub‑Site Schema Module v3.1
- A record ready for export via the Sub‑Site TSV Output Specification v3.1
- Full audit trail entries via the Audit & Logging Module v1.1

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize Sub‑Site name  
4. Normalize parent Site  
5. Normalize Sub‑Site Type, Status, Designation  
6. Normalize jurisdiction fields  
7. Normalize geometry and GPS  
8. Normalize notes and description  
9. Normalize URLs and sources  
10. Validate multi‑county logic  
11. Construct Derived Label (if required)  
12. Apply formatting rules  
13. Emit normalized Sub‑Site entity  

If any critical step fails → surface to Resolution Module v3.1.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Sub‑Site Name

### Rules
- Use name_raw exactly as discovered, with minimal whitespace cleanup.
- If multiple authoritative names exist → choose the most authoritative.
- Alternate names go in Description.
- Never invent names.
- Never infer names from amenities or map labels alone.

### Audit
- Log all name conflicts.
- Log all corrections.

------------------------------------------------------------
## 5.2 Parent Site

### Rules
- Required.
- Must match the exact normalized name of a Site entity.
- A Sub‑Site must have exactly one parent Site.
- Never infer parentage from proximity or geometry alone.
- If parent Site is not yet normalized → create placeholder Site for Resolution.

### Audit
- Log all parent conflicts.
- Log unverifiable parent relationships.

------------------------------------------------------------
## 5.3 Sub‑Site Type

### Rules
- Must match a value from the Sub‑Site Type vocabulary.
- Examples: “Preserve Unit,” “Historic District Unit,” “Ecological Unit,” “Recreation Area.”
- Never infer from features or amenities.
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.4 Designation (if schema supports)

### Rules
- Must match vocabulary values.
- Semicolon‑delimit if multiple.
- Never infer.
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.5 Description

### Rules
- 1–3 sentences.
- Must describe identity‑defining characteristics of the Sub‑Site.
- Include naming history and alternate names.
- Must not include amenities or temporary conditions.
- Must not include Site‑level or Trail‑level descriptions.

------------------------------------------------------------
## 5.6 Notes

### Rules
- Optional free‑text.
- Must not include identity‑defining ecology.
- Must not include internal features (those belong to Site normalization).
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.7 County

### Rules
- Must match official Ohio county list.
- Semicolon‑delimit if multi‑county.
- Alphabetical order.
- Omit the word “County.”
- Never infer from parent Site unless explicitly documented.

------------------------------------------------------------
## 5.8 Township & Municipality

### Rules
- Must match authoritative jurisdiction names.
- Semicolon‑delimit if multiple.
- Must not include county names.
- If many jurisdictions → use jurisdiction of Address (if present).

------------------------------------------------------------
## 5.9 GPS Coordinates

### Rules
- Format: lat,lon (no space).
- Accept only authoritative coordinates.
- Reject placeholders, centroids, or unverifiable coordinates.
- Leave blank if verification fails.

------------------------------------------------------------
## 5.10 Geometry

### Rules
- Use geometry_raw exactly as discovered.
- Do not simplify, smooth, or infer geometry.
- Preserve coordinate precision.
- If geometry is malformed → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.11 Plus Code

### Rules
- Generate only from accepted GPS.
- If GPS blank → Plus Code blank.

------------------------------------------------------------
## 5.12 URL

### Rules
- Full https:// URLs only.
- Semicolon‑delimit if multiple.
- Must be authoritative.
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.13 Derived Label (computed, not stored)

### Formula
Sub‑Site Type + " Sub‑Site"

### Rules
- Must be derived solely from normalized fields.
- Log all construction steps.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Sub‑Site spanning multiple counties must produce one normalized record per county.
- Each record must:
  - Use the same Sub‑Site name
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

### 9.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Description.

### 9.2 Conflicting Sub‑Site Type
- Use authoritative Site‑level or district‑level sources.
- If unclear → Resolution.

### 9.3 Conflicting Geometry
- Preserve all geometry claims in metadata.
- Use the most authoritative geometry for normalization.
- If unclear → Resolution.

### 9.4 Conflicting Parent Site
- Preserve all claims.
- Flag for Resolution.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer parent Site, designation, or jurisdiction.
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

- Sub‑Site Vocabulary Module v3.1
- Sub‑Site Schema Module v3.1
- Site Schema Module v3.1
- TSV Output Specification (Sub‑Sites) v3.1
- Discovery Protocol Module v3.1
- Discovery Output Specification v3.1
- Discovery Metadata Specification v1.0
- Resolution Module v3.1
- Audit & Logging Module v1.1
- Processing / Orchestration Module v3.1

------------------------------------------------------------
# END OF SUB‑SITE NORMALIZATION CONTRACT v3.1