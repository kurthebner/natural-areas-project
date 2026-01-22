# NATURAL AREAS PROJECT — SITE NETWORK NORMALIZATION CONTRACT v3.2.2
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Site Network Raw Candidate Records into fully normalized Site Network entities
under the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Network Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Site Network discoveries are normalized  
- How each Site Network Schema v3.2.2 field is populated  
- How Network Type, Status, and Designation are validated  
- How member Sites are validated and linked  
- How multi‑county and multi‑state networks are normalized  
- How URLs, notes, and metadata are handled  
- How Derived Label is constructed **only at TSV output time**  
- How normalization integrates with the Audit & Logging Module v3.2.2  
- How conflicts and uncertainties are surfaced to the Resolution Module v3.2.2  

This module is authoritative for Site Network normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record  
From **Discovery Output Specification v3.2.2**, including:

- name_raw  
- network_type_raw  
- counties_raw  
- states_raw  
- managing_agency_raw  
- managing_agencies_secondary_raw  
- url_primary_raw, url_all_raw  
- member_sites_raw  
- notes_raw  
- description_raw  
- source_datasets_raw  
- source_maps_raw  
- source_gis_layers_raw  
- discovery_tier  
- discovered_in_tiers  
- seeded_from_baseline  
- baseline_id_raw  
- discovery_metadata (v3.2.2)

## 2.2 Discovery Metadata  
From **Discovery Metadata Specification v3.2.2**, including:

- Identity metadata  
- Tier metadata  
- Source metadata  
- Conflict metadata  
- Uncertainty metadata  
- Boundary metadata  
- Parent/relationship metadata  
- Baseline metadata  

## 2.3 Vocabulary Modules  
- **Site Network Vocabulary Module v3.2.2**  
  - Network Types  
  - Network Status  
  - Network Designations  

## 2.4 Schema Modules  
- **Site Network Schema Module v3.2.2**  
- **Site Schema Module v3.2.2** (for member validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Site Network entity conforming to the **Site Network Schema Module v3.2.2**  
- A record ready for export via the **TSV Output Specification (Site Networks) v3.2.2**  
- Full audit trail entries via the **Audit & Logging Module v3.2.2**  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize network name  
4. Normalize Network Type  
5. Normalize jurisdiction fields (counties, states)  
6. Normalize managing agencies  
7. Normalize member Sites  
8. Normalize description  
9. Normalize notes  
10. Normalize URLs and sources  
11. Apply multi‑county and multi‑state rules  
12. Validate against schema  
13. Emit normalized Site Network entity  

**Derived Label is not constructed here.**  
It is computed only during TSV output.

If any critical step fails → surface to **Resolution Module v3.2.2**.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Network Name

### Rules
- Use `name_raw` exactly as discovered, with minimal whitespace cleanup.  
- If multiple authoritative names exist → choose the most authoritative.  
- Alternate names go in Description.  
- Never invent names.  
- Never infer names from member Sites or branding alone.

### Audit
- Log all name conflicts.  
- Log all corrections.

------------------------------------------------------------
## 5.2 Network Type

### Rules
- Must match a value from the **Network Type vocabulary v3.2.2**.  
- Never infer from member Sites alone.  
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.3 Network Status (if schema supports)

### Rules
- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer.  
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.4 Network Designation (if schema supports)

### Rules
- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer.  
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.5 Managing Agency (Primary)

### Rules
- Use `managing_agency_raw` if authoritative.  
- Must match vocabulary values (Federal, State, Park District, County, Municipal, Land Trust, Private, etc.).  
- Never infer from member Sites.  
- Leave blank if unknown.

------------------------------------------------------------
## 5.6 Managing Agencies (Secondary)

### Rules
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- Never infer from Site‑level management.

------------------------------------------------------------
## 5.7 Counties

### Rules
- Normalize using the **official Ohio county list**.  
- Semicolon‑delimit if multi‑county.  
- Alphabetical order.  
- Omit the word “County.”  
- Never infer from member Sites unless explicitly documented.  
- Never segment multi‑county networks.

------------------------------------------------------------
## 5.8 States (if multi‑state)

### Rules
- Use authoritative state abbreviations (e.g., OH, IN, KY).  
- Semicolon‑delimit if multiple.  
- Never infer from member Sites unless explicitly documented.

------------------------------------------------------------
## 5.9 Member Sites

### Rules
- Must match **normalized Site names**.  
- Semicolon‑delimit if multiple.  
- Never infer membership.  
- If a member Site is not yet normalized → create a placeholder for Resolution.  
- If membership is ambiguous → flag uncertainty.

### Audit
- Log all membership conflicts.  
- Log unverifiable membership claims.

------------------------------------------------------------
## 5.10 Description

### Rules
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the network.  
- Include naming history and alternate names.  
- Must not include amenities or temporary conditions.  
- Must not include Site‑level descriptions.

------------------------------------------------------------
## 5.11 Notes

### Rules
- Optional free‑text.  
- Must not include identity‑defining ecology.  
- Must not include Site‑level or child‑Site‑level details.  
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.12 URLs

### Rules
- Full https:// URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.13 Derived Label (computed at TSV output)

### Rules
- Derived Label is **not stored** in normalized entities.  
- Derived Label is computed only during TSV output using the **TSV Output Specification v3.2.2**.  
- Must be derived solely from normalized fields.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. MULTI‑COUNTY AND MULTI‑STATE NORMALIZATION RULES

- A Site Network spanning multiple counties or states produces **one normalized entity**, not multiple.  
- The County field contains a **semicolon‑delimited, alphabetized list**.  
- The State field contains a **semicolon‑delimited, alphabetized list**.  
- Boundary metadata must reflect all counties and states included.  
- Never segment multi‑county or multi‑state networks.

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
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- **Site Network Vocabulary Module v3.2.2**  
- **Site Network Schema Module v3.2.2**  
- **Site Schema Module v3.2.2**  
- **TSV Output Specification (Site Networks) v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Resolution Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v3.2.2