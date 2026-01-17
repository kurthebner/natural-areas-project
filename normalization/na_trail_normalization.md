# NATURAL AREAS PROJECT — TRAIL NORMALIZATION CONTRACT v3.1
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Trail Raw Candidate Records into fully normalized Trail entities under the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Vocabulary Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Trail discoveries are normalized
- How each Trail Schema v3.1 field is populated
- How Trail Type, Surface, Use, Status, and Designation are validated
- How parent relationships (Trail → Trail Network) are validated
- How GPS, Plus Code, Address, and URL rules are applied
- How multi‑county Trails are normalized
- How Derived Label is constructed (if required by TSV)
- How normalization integrates with the Audit & Logging Module
- How conflicts and uncertainties are surfaced to the Resolution Module

This module is authoritative for Trail normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record
From Discovery Output Specification v3.1, including:

- name_raw
- county, township, municipality
- ownership_raw, management_raw (if present)
- gps_raw, address_raw
- url_primary, url_all
- source_datasets, source_maps, source_gis_layers
- parent_trail_systems
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
- Trail Vocabulary Module v3.1
  - Trail Types
  - Trail Surfaces
  - Trail Uses
  - Trail Status
  - Trail Designations

## 2.4 Schema Modules
- Trail Schema Module v3.1
- Trail Segment Schema Module v3.1
- Trail Network Schema Module v3.1

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Trail entity conforming to the Trail Schema Module v3.1
- A record ready for export via the Trail TSV Output Specification v3.1
- Full audit trail entries via the Audit & Logging Module v1.1

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize name  
4. Normalize Trail Type, Surface, Use, Designation  
5. Normalize ownership, management, coordination (if schema supports)  
6. Normalize jurisdiction fields  
7. Normalize location fields (GPS, Plus Code, Address)  
8. Normalize length (if present)  
9. Normalize Trail Network membership  
10. Normalize notes  
11. Normalize URLs and sources  
12. Validate multi‑county logic  
13. Construct Derived Label (if required)  
14. Apply formatting rules  
15. Emit normalized Trail entity  

If any critical step fails → surface to Resolution Module v3.1.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Name

### Rules
- Use name_raw exactly as discovered, with minimal whitespace cleanup.
- If multiple authoritative names exist → choose the most authoritative.
- Alternate names go in Description.
- Never invent names.
- Never infer names from segments, networks, or amenities.

### Audit
- Log all name conflicts.
- Log all corrections.

------------------------------------------------------------
## 5.2 Trail Type

### Rules
- Must match a value from Trail Vocabulary Module v3.1.
- Never infer from surface, use, or amenities.
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.3 Trail Surface

### Rules
- Must match vocabulary values.
- If multiple surfaces documented → semicolon‑delimit.
- Never infer from imagery alone.

------------------------------------------------------------
## 5.4 Trail Use

### Rules
- Must match vocabulary values.
- Semicolon‑delimit if multiple.
- Never infer from amenities or signage alone.

------------------------------------------------------------
## 5.5 Designation

### Rules
- Must match vocabulary values (e.g., National Scenic Trail, State Water Trail).
- Semicolon‑delimit if multiple.
- Never infer.
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.6 Ownership

### Rules
- Use ownership_raw if authoritative.
- Must match vocabulary values (Federal, State, Park District, County, Township,
  Municipal, Land Trust, Private, Foundation, Corporate, HOA).
- Never infer ownership.
- Leave blank if unknown.

------------------------------------------------------------
## 5.7 Management

### Rules
- Use operational manager(s).
- Semicolon‑delimit if multiple.
- If same as Ownership → repeat explicitly.
- Leave blank if unknown.

------------------------------------------------------------
## 5.8 Coordination

### Rules
- Only formal coordinating entities.
- Leave blank if none.

------------------------------------------------------------
## 5.9 Description

### Rules
- 1–3 sentences.
- Must describe identity‑defining characteristics of the Trail.
- Include naming history and alternate names.
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.10 Status

### Rules
- Must match vocabulary values.
- “Closed” = permanently closed.
- “Proposed” must be officially referenced.
- Never infer from imagery.

------------------------------------------------------------
## 5.11 Address

### Rules
- Use authoritative address if available.
- Partial address allowed if verifiable.
- Never invent.
- Leave blank if none.

------------------------------------------------------------
## 5.12 Length (Miles)

### Rules
- Numeric only.
- No units.
- Never estimate.
- Leave blank if unknown.

------------------------------------------------------------
## 5.13 County

### Rules
- Required.
- Must match official Ohio county list.
- Semicolon‑delimit if multi‑county.
- Alphabetical order.
- Omit the word “County.”

------------------------------------------------------------
## 5.14 Township & Municipality

### Rules
- Must match authoritative jurisdiction names.
- Semicolon‑delimit if multiple.
- Must not include county names.
- If many jurisdictions → use jurisdiction of Address.

------------------------------------------------------------
## 5.15 GPS Coordinates

### Rules
- Format: lat,lon (no space).
- Accept only authoritative coordinates.
- Reject placeholders, centroids, or unverifiable coordinates.
- Leave blank if verification fails.

------------------------------------------------------------
## 5.16 Plus Code

### Rules
- Generate only from accepted GPS.
- If GPS blank → Plus Code blank.

------------------------------------------------------------
## 5.17 Trail Network Membership

### Rules
- Use parent_trail_systems from raw record.
- Must match normalized Trail Network names.
- Semicolon‑delimit if multiple.
- Never infer membership.
- If ambiguous → flag uncertainty.

------------------------------------------------------------
## 5.18 Notes

### Rules
- Optional free‑text.
- Must not include identity‑defining characteristics.
- Must not include internal features or segment‑level details.
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.19 URL

### Rules
- Full https:// URLs only.
- Semicolon‑delimit if multiple.
- Must be authoritative.
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.20 Derived Label (computed, not stored)

### Formula
Trail Type + (Designation if present)

### Rules
- Must be derived solely from normalized fields.
- Log all construction steps.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail spanning multiple counties must produce one normalized record per county.
- Each record must:
  - Use the same Trail name
  - Use county‑specific jurisdiction fields
  - Preserve all metadata
- Boundary metadata must reflect all counties traversed.

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- All vocabulary‑controlled fields
- GPS format
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

### 9.2 Conflicting Length
- Use the most authoritative source.
- If conflict persists → Resolution.

### 9.3 Conflicting Trail Type, Surface, or Use
- Use authoritative trail system sources.
- If unclear → Resolution.

### 9.4 Conflicting Network Membership
- Preserve all claims.
- Flag for Resolution.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer ownership, designation, or length.
- Never generate GPS without verification.

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

- Trail Vocabulary Module v3.1
- Trail Schema Module v3.1
- TSV Output Specification (Trails) v3.1
- Discovery Protocol Module v3.1
- Discovery Output Specification v3.1
- Discovery Metadata Specification v1.0
- Resolution Module v3.1
- Audit & Logging Module v1.1
- Processing / Orchestration Module v3.1

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v3.1