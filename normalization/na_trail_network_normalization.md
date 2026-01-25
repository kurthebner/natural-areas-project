# NATURAL AREAS PROJECT — TRAIL NETWORK NORMALIZATION CONTRACT v4.0
Authoritative, deterministic, field‑by‑field normalization contract for transforming  
**Resolved Trail Network Entities** into fully normalized Trail Network entities  
under the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Network Vocabulary Module v4.0**.

Normalization must be deterministic, provenance‑preserving, and aligned with:

- Trail Network Schema Module v4.0  
- Trail Schema Module v4.0 (for member validation)  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- TSV Output Specification (Trail Networks) v4.0  
- Audit & Logging Module v4.0  

No invented data is permitted.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How resolved Trail Network entities are normalized  
- How each Trail Network Schema v4.0 field is populated  
- How Network Type is validated  
- How member Trails are validated and linked  
- How multi‑county and multi‑state networks are normalized  
- How URLs, notes, and metadata are handled  
- How Derived Label is computed (v4.0)  
- How conflicts and uncertainties are surfaced  
- How normalization integrates with audit and provenance  

This module is authoritative for Trail Network normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Trail Network Entity (from Resolution Engine v4.0)
Including:

- name_resolved  
- network_type_resolved  
- counties_resolved  
- states_resolved  
- managing_agency_primary_resolved  
- managing_agencies_secondary_resolved  
- url_primary_resolved, url_all_resolved  
- member_trails_resolved  
- notes_resolved  
- description_resolved  
- history_resolved  
- provenance metadata  
- conflict metadata  
- uncertainty metadata  

## 2.2 Vocabulary Modules v4.0
- Network Types  

## 2.3 Schema Modules v4.0
- Trail Network Schema Module v4.0  
- Trail Schema Module v4.0  

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Network Entity** conforming to Trail Network Schema v4.0  
- A complete normalization provenance record  
- A record ready for TSV Output and Entity Upsert Engine v4.0  

Derived Label **is computed during normalization** (v4.0 rule).

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Validate identity  
2. Normalize network name  
3. Normalize Network Type  
4. Normalize jurisdiction fields (Counties, States)  
5. Normalize managing agencies  
6. Normalize member Trails  
7. Normalize description  
8. Normalize history  
9. Normalize notes  
10. Normalize URLs and sources  
11. Compute Derived Label  
12. Validate against schema  
13. Emit normalized Trail Network entity  

If any critical step fails → surface to Resolution Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Network Name

- Use `name_resolved` exactly as resolved.  
- Minimal whitespace cleanup only.  
- Alternate names → Alternate Names field.  
- Never invent names.  
- Never infer names from member Trails or branding.

Audit:
- Log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Network Type

- Must match a value from the Network Type vocabulary v4.0.  
- Never infer from member Trails alone.  
- If ambiguous → leave blank and flag uncertainty.

Audit:
- Log all mappings and unmappable values.

------------------------------------------------------------
## 5.3 Managing Agency (Primary)

- Must be authoritative.  
- Must not be inferred from member Trails.  
- Leave blank if unknown.  
- Must not encode governance hierarchy.

------------------------------------------------------------
## 5.4 Managing Agencies (Secondary)

- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- Must not duplicate the primary agency.  
- Never infer from Trail‑level management.

------------------------------------------------------------
## 5.5 County List

- Normalize using the official county list.  
- Semicolon‑delimited.  
- Alphabetized.  
- Must not include the word “County.”  
- Never infer from member Trails unless explicitly documented.  
- A multi‑county network is **one entity**, never segmented.

------------------------------------------------------------
## 5.6 States Included

- Use authoritative state abbreviations (e.g., OH, IN, KY).  
- Semicolon‑delimit if multiple.  
- Alphabetized.  
- Never infer from member Trails unless explicitly documented.

------------------------------------------------------------
## 5.7 Member Trails

- Must match **normalized Trail names**.  
- Semicolon‑delimit if multiple.  
- Never infer membership.  
- If a member Trail is unresolved → Resolution Engine handles identity.  
- If ambiguous → flag uncertainty.

Audit:
- Log all membership conflicts and unverifiable claims.

------------------------------------------------------------
## 5.8 Description

- 1–3 sentences.  
- Must describe identity‑defining characteristics of the network.  
- Include naming history and alternate names.  
- Must not include Trail‑level or Segment‑level details.  
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.9 History

- Optional.  
- Must be factual and sourced.  
- May include origin, designation events, or major changes.  
- Must not include speculative or inferred history.

------------------------------------------------------------
## 5.10 Notes

- Optional free‑text.  
- Must not include identity‑defining characteristics.  
- Must not include Trail‑level details.  
- Use for clarifications, temporary conditions, or contextual notes.

------------------------------------------------------------
## 5.11 URLs

- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- Tracking parameters must be removed.  
- No placeholders or inferred URLs.

------------------------------------------------------------
## 5.12 Derived Label (computed during normalization)

### Rules

- Derived Label is **computed here** in v4.0.  
- Must be derived solely from normalized fields.  
- Must follow the Derived Label rules in the TSV Output Specification v4.0.  
- Must be deterministic.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. MULTI‑COUNTY AND MULTI‑STATE NORMALIZATION RULES

- A Trail Network spanning multiple counties or states produces **one normalized entity**.  
- County List must be semicolon‑delimited and alphabetized.  
- States Included must be semicolon‑delimited and alphabetized.  
- Boundary metadata must reflect all counties and states traversed.  
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

If validation fails:
- Surface to Resolution Engine v4.0  
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
- Record alternates in Alternate Names.

### 9.2 Conflicting Network Type
- Use authoritative regional or statewide sources.  
- If unclear → Resolution Engine v4.0.

### 9.3 Conflicting Membership
- Preserve all claims.  
- Flag for Resolution.

### 9.4 Conflicting Jurisdiction
- Use the most authoritative source.  
- Preserve all claims in metadata.

------------------------------------------------------------
# 10. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.  
- Never estimate.  
- Never infer membership or jurisdiction.  
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

- Trail Network Vocabulary Module v4.0  
- Trail Network Schema Module v4.0  
- Trail Schema Module v4.0  
- TSV Output Specification (Trail Networks) v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Resolution Engine v4.0  
- Audit & Logging Module v4.0  
- Processing / Orchestration Module v4.0  

------------------------------------------------------------
# END OF TRAIL NETWORK NORMALIZATION CONTRACT v4.0