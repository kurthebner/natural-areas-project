# NATURAL AREAS PROJECT
# TRAIL NORMALIZATION CONTRACT v4.0
(Authoritative, Deterministic Normalization Rules for Trail Entities)

This module defines the authoritative, deterministic rules for transforming
**Resolved Trail Entities** into **Normalized Trail Entities** under the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v4.0**.

Normalization must be deterministic, provenance‑preserving, and fully aligned with:

- Trail Schema Module v4.0  
- Resolution Module v4.0  
- Normalization Engine v4.0  
- TSV Output Specification (Trails) v4.0  
- Audit & Logging Module v4.0  
- TSV Integrity Check Module v4.0  

No invented data is permitted.

------------------------------------------------------------
# 1. PURPOSE

The Trail Normalization Contract v4.0 defines:

- How each Trail field is normalized  
- How vocabulary‑controlled fields are validated  
- How multi‑county Trails are normalized  
- How GPS, Plus Code, and Address fields are validated  
- How Trail Network membership is normalized  
- How Derived Labels are computed  
- How normalization integrates with audit and provenance  
- How conflicts and unverifiable claims are surfaced  

Normalization produces:

- A **Normalized Trail Entity**  
- A complete normalization provenance record  
- A record ready for Entity Upsert Engine v4.0  

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Trail Entity (from Resolution Engine v4.0)
Including:

- name_resolved  
- trail_type_resolved  
- surface_resolved  
- use_resolved  
- designation_resolved  
- ownership_resolved  
- management_resolved  
- coordination_resolved  
- counties_resolved  
- gps_resolved  
- address_resolved  
- parent_trail_networks_resolved  
- description_resolved  
- notes_resolved  
- provenance metadata  
- conflict metadata  

## 2.2 Vocabulary Modules v4.0
- Trail Types  
- Trail Surfaces  
- Trail Uses  
- Trail Designations  
- Status values  

## 2.3 Schema Modules v4.0
- Trail Schema Module v4.0  
- Trail Segment Schema Module v4.0  
- Trail Network Schema Module v4.0  

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Entity** conforming to Trail Schema v4.0  
- A complete normalization provenance record  
- A record ready for TSV Output and Entity Upsert Engine v4.0  

Derived Label **is computed here** in v4.0 (not in TSV output).

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Validate identity  
2. Normalize name  
3. Normalize Trail Type, Surface, Use, Designation  
4. Normalize Ownership, Management, Coordination  
5. Normalize counties  
6. Normalize GPS, Plus Code, Address  
7. Normalize length  
8. Normalize Trail Network membership  
9. Normalize description and notes  
10. Normalize URLs and sources  
11. Compute Derived Label  
12. Validate against schema  
13. Emit normalized Trail entity  

If any critical step fails → surface to Resolution Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Name

- Use `name_resolved` exactly as resolved.  
- Minimal whitespace cleanup only.  
- Alternate names → Description.  
- Never infer names from segments, networks, or amenities.  

Audit:
- Log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Trail Type

- Must match Trail Type vocabulary v4.0.  
- Never infer from surface, use, or amenities.  
- If ambiguous → leave blank and flag uncertainty.  

------------------------------------------------------------
## 5.3 Trail Surface

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer from imagery alone.  

------------------------------------------------------------
## 5.4 Trail Use

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer from signage alone.  

------------------------------------------------------------
## 5.5 Designation

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer.  
- Leave blank if unverifiable.  

------------------------------------------------------------
## 5.6 Ownership

- Must match vocabulary values.  
- Never infer ownership.  
- Leave blank if unknown.  

------------------------------------------------------------
## 5.7 Management

- Use operational manager(s).  
- Semicolon‑delimit if multiple.  
- Leave blank if unknown.  

------------------------------------------------------------
## 5.8 Coordination

- Only formal coordinating entities.  
- Leave blank if none.  

------------------------------------------------------------
## 5.9 Description

- 1–3 sentences.  
- Must describe identity‑defining characteristics of the Trail.  
- Include naming history and alternate names.  
- Must not include amenities or temporary conditions.  

------------------------------------------------------------
## 5.10 Status

- Must match vocabulary values.  
- “Closed” = permanently closed.  
- “Proposed” must be officially documented.  
- Never infer from imagery.  

------------------------------------------------------------
## 5.11 Address

- Use authoritative address if available.  
- Partial address allowed if verifiable.  
- Never invent.  
- Leave blank if none.  

------------------------------------------------------------
## 5.12 Length (Miles)

- Numeric only.  
- No units.  
- Never estimate.  
- Leave blank if unknown.  

------------------------------------------------------------
## 5.13 County List

- Required.  
- Must match official county list.  
- Semicolon‑delimited.  
- Alphabetized.  
- No duplicates.  
- Never infer counties.  
- A multi‑county Trail is **one entity**, never segmented.  

------------------------------------------------------------
## 5.14 Township & Municipality

- Must match authoritative jurisdiction names.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  
- If many jurisdictions → use jurisdiction of Address.  

------------------------------------------------------------
## 5.15 GPS Coordinates

- Format: `lat,lon` (no space).  
- Accept only authoritative coordinates.  
- Reject placeholders, centroids, or unverifiable coordinates.  
- Leave blank if verification fails.  

------------------------------------------------------------
## 5.16 Plus Code

- Generate only from accepted GPS.  
- If GPS blank → Plus Code blank.  

------------------------------------------------------------
## 5.17 Trail Network Membership

- Must match normalized Trail Network names.  
- Semicolon‑delimit if multiple.  
- Never infer membership.  
- If ambiguous → flag uncertainty.  

Audit:
- Log all membership conflicts.

------------------------------------------------------------
## 5.18 Notes

- Optional free‑text.  
- Must not include identity‑defining characteristics.  
- Must not include internal features or segment‑level details.  
- Use for temporary closures, access restrictions, historical notes.  

------------------------------------------------------------
## 5.19 URLs

- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- No placeholders or inferred URLs.  
- Normalize by removing tracking parameters.  

------------------------------------------------------------
## 5.20 Derived Label (computed during normalization)

### Rules

- Derived Label **is computed here** in v4.0.  
- Must be derived solely from normalized fields.  
- Must be deterministic.  
- Must follow the Derived Label rules in TSV Output Specification v4.0.  
- All construction steps must be logged.  

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail spanning multiple counties produces **one normalized entity**.  
- County list must be semicolon‑delimited and alphabetized.  
- Boundary metadata must reflect all counties traversed.  
- Never segment multi‑county Trails.  

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
- Record alternates in Description.  

### 9.2 Conflicting Length
- Use the most authoritative source.  
- If conflict persists → Resolution Engine v4.0.  

### 9.3 Conflicting Trail Type, Surface, or Use
- Use authoritative trail system sources.  
- If unclear → Resolution Engine v4.0.  

### 9.4 Conflicting Network Membership
- Preserve all claims.  
- Flag for Resolution Engine v4.0.  

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
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Trail Vocabulary Module v4.0  
- Trail Schema Module v4.0  
- TSV Output Specification (Trails) v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Trail Network Normalization Contract v4.0  
- Trail Segment Normalization Contract v4.0  
- Resolution Module v4.0  
- Audit & Logging Module v4.0  
- Processing / Orchestration Module v4.0  

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v4.0