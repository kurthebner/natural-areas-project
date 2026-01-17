# NATURAL AREAS PROJECT — TRAIL NETWORK NORMALIZATION CONTRACT v3.1
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Trail Network Raw Candidate Records into fully normalized Trail Network entities
under the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Network Vocabulary Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Trail Network discoveries are normalized
- How each Trail Network Schema v3.1 field is populated
- How Network Type, Status, and Designation are validated
- How member Trails are validated and linked
- How multi‑county and multi‑state networks are normalized
- How URLs, notes, and metadata are handled
- How Derived Label is constructed (if required by TSV)
- How normalization integrates with the Audit & Logging Module
- How conflicts and uncertainties are surfaced to the Resolution Module

This module is authoritative for Trail Network normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record
From Discovery Output Specification v3.1, including:

- name_raw
- network_type_raw
- counties_raw
- states_raw
- managing_agency_raw
- managing_agencies_secondary_raw
- url_primary, url_all
- member_trails_raw
- notes_raw
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
- Trail Network Vocabulary Module v3.1
  - Network Types
  - Network Status (if defined)
  - Network Designations (if defined)

## 2.4 Schema Modules
- Trail Network Schema Module v3.1
- Trail Schema Module v3.1 (for member validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Trail Network entity conforming to the Trail Network Schema Module v3.1
- A record ready for export via the Trail Network TSV Output Specification v3.1
- Full audit trail entries via the Audit & Logging Module v1.1

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize network name  
4. Normalize Network Type  
5. Normalize jurisdiction fields (counties, states)  
6. Normalize managing agencies  
7. Normalize member Trails  
8. Normalize URLs and sources  
9. Normalize notes  
10. Apply multi‑county and multi‑state rules  
11. Construct Derived Label (if required)  
12. Apply formatting rules  
13. Emit normalized Trail Network entity  

If any critical step fails → surface to Resolution Module v3.1.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Network Name

### Rules
- Use name_raw exactly as discovered, with minimal whitespace cleanup.
- If multiple authoritative names exist → choose the most authoritative.
- Alternate names go in Description.
- Never invent names.
- Never infer names from member Trails or branding alone.

### Audit
- Log all name conflicts.
- Log all corrections.

------------------------------------------------------------
## 5.2 Network Type

### Rules
- Must match a value from the Network Type vocabulary.
- Examples: “Regional Greenway Network,” “Countywide Bikeway System,” “Statewide Trail System.”
- Never infer from member Trails alone.
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.3 Designation (if schema supports)

### Rules
- Must match vocabulary values.
- Semicolon‑delimit if multiple.
- Never infer.
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.4 Managing Agency (Primary)

### Rules
- Use managing_agency_raw if authoritative.
- Must match vocabulary values (Federal, State, Park District, County, Municipal, Land Trust, Private, etc.).
- Never infer from member Trails.
- Leave blank if unknown.

------------------------------------------------------------
## 5.5 Managing Agencies (Secondary)

### Rules
- Semicolon‑delimit if multiple.
- Must be authoritative.
- Never infer from Trail‑level management.

------------------------------------------------------------
## 5.6 Counties

### Rules
- Must match official Ohio county list.
- Semicolon‑delimit if multi‑county.
- Alphabetical order.
- Omit the word “County.”
- Never infer from member Trails unless explicitly documented.

------------------------------------------------------------
## 5.7 States (if multi‑state)

### Rules
- Use authoritative state abbreviations (e.g., OH, IN, KY).
- Semicolon‑delimit if multiple.
- Never infer from member Trails unless explicitly documented.

------------------------------------------------------------
## 5.8 Member Trails

### Rules
- Must match normalized Trail names.
- Semicolon‑delimit if multiple.
- Never infer membership.
- If a member Trail is not yet normalized → create placeholder Trail for Resolution.
- If membership is ambiguous → flag uncertainty.

### Audit
- Log all membership conflicts.
- Log unverifiable membership claims.

------------------------------------------------------------
## 5.9 Description

### Rules
- 1–3 sentences.
- Must describe identity‑defining characteristics of the network.
- Include naming history and alternate names.
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.10 Notes

### Rules
- Optional free‑text.
- Must not include identity‑defining characteristics.
- Must not include Trail‑level details.
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.11 URL

### Rules
- Full https:// URLs only.
- Semicolon‑delimit if multiple.
- Must be authoritative.
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.12 Derived Label (computed, not stored)

### Formula
Network Type + " Network"

### Rules
- Must be derived solely from normalized fields.
- Log all construction steps.

------------------------------------------------------------
# 6. MULTI‑COUNTY AND MULTI‑STATE NORMALIZATION RULES

- A Trail Network spanning multiple counties or states must produce one normalized record per county.
- Each record must:
  - Use the same network name
  - Use county‑specific jurisdiction fields
  - Preserve all metadata
- Boundary metadata must reflect all counties and states traversed.

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- All vocabulary‑controlled fields
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

### 9.2 Conflicting Network Type
- Use authoritative regional or statewide sources.
- If unclear → Resolution.

### 9.3 Conflicting Membership
- Preserve all claims.
- Flag for Resolution.

### 9.4 Conflicting Jurisdiction (Counties/States)
- Use the most authoritative source.
- Preserve all claims in metadata.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer membership, designation, or jurisdiction.
- Never generate URLs without verification.

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

- Trail Network Vocabulary Module v3.1
- Trail Network Schema Module v3.1
- Trail Schema Module v3.1
- TSV Output Specification (Trail Networks) v3.1
- Discovery Protocol Module v3.1
- Discovery Output Specification v3.1
- Discovery Metadata Specification v1.0
- Resolution Module v3.1
- Audit & Logging Module v1.1
- Processing / Orchestration Module v3.1

------------------------------------------------------------
# END OF TRAIL NETWORK NORMALIZATION CONTRACT v3.1