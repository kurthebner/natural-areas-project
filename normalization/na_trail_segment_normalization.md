# NATURAL AREAS PROJECT — TRAIL SEGMENT NORMALIZATION CONTRACT v4.0
Authoritative, deterministic, field‑by‑field normalization contract for transforming  
**Resolved Trail Segment Entities** into fully normalized Trail Segment entities  
under the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Segment Vocabulary Module v4.0**.

Normalization must be deterministic, provenance‑preserving, and aligned with:

- Trail Segment Schema Module v4.0  
- Trail Schema Module v4.0 (for parent validation)  
- Trail Network Schema Module v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- TSV Output Specification (Trail Segments) v4.0  
- Audit & Logging Module v4.0  

No invented data is permitted.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How resolved Trail Segment entities are normalized  
- How each Trail Segment Schema v4.0 field is populated  
- How Segment Type, Surface, Status, and Use are validated  
- How parent Trail relationships are validated  
- How geometry, GPS, Plus Code, and URL rules are applied  
- How multi‑county segments are normalized  
- How conflicts and uncertainties are surfaced  
- How Derived Label is computed (v4.0)  
- How normalization integrates with audit and provenance  

This module is authoritative for Trail Segment normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Trail Segment Entity (from Resolution Engine v4.0)
Including:

- name_resolved  
- parent_trail_resolved  
- counties_resolved  
- municipalities_resolved, townships_resolved  
- surface_resolved, status_resolved, use_resolved  
- gps_resolved  
- geometry_resolved  
- length_resolved  
- url_primary_resolved, url_all_resolved  
- notes_resolved  
- description_resolved  
- provenance metadata  
- conflict metadata  
- uncertainty metadata  

## 2.2 Vocabulary Modules v4.0
- Segment Types  
- Segment Surfaces  
- Segment Uses  
- Segment Status  

## 2.3 Schema Modules v4.0
- Trail Segment Schema Module v4.0  
- Trail Schema Module v4.0  
- Trail Network Schema Module v4.0  

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Segment Entity** conforming to Trail Segment Schema v4.0  
- A complete normalization provenance record  
- A record ready for TSV Output and Entity Upsert Engine v4.0  

Derived Label **is computed during normalization** (v4.0 rule).

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Validate identity  
2. Normalize segment name  
3. Normalize parent Trail  
4. Normalize Segment Type, Surface, Use, Status  
5. Normalize jurisdiction fields  
6. Normalize geometry and GPS  
7. Normalize length  
8. Normalize Trail Network associations  
9. Normalize description  
10. Normalize notes  
11. Normalize URLs and sources  
12. Compute Derived Label  
13. Validate against schema  
14. Emit normalized Trail Segment entity  

If any critical step fails → surface to Resolution Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Segment Name

- Use `name_resolved` exactly as resolved.  
- Minimal whitespace cleanup only.  
- Alternate names → Description.  
- Never infer names from geometry or map labels alone.

Audit:
- Log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Parent Trail

- Required.  
- Must match the exact normalized name of a Trail entity.  
- If parent Trail unresolved → Resolution Engine handles identity resolution.  
- Never infer parentage from proximity or geometry alone.  
- A Trail Segment must have exactly one parent Trail.

Audit:
- Log all parent conflicts and unverifiable relationships.

------------------------------------------------------------
## 5.3 Segment Type

- Must match Segment Type vocabulary v4.0.  
- Never infer from surface or status.  
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.4 Surface

- Must match vocabulary values.  
- Semicolon‑delimit if multiple surfaces documented.  
- Never infer from imagery alone.

------------------------------------------------------------
## 5.5 Use

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer from signage or amenities alone.

------------------------------------------------------------
## 5.6 Status

- Must match vocabulary values.  
- “Closed” = permanently closed.  
- “Proposed” must be officially documented.  
- Never infer from imagery.

------------------------------------------------------------
## 5.7 Description

- 1–3 sentences.  
- Must describe identity‑defining characteristics of the segment.  
- Include naming history and alternate identifiers.  
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.8 Length (Miles)

- Numeric only.  
- No units.  
- Never estimate.  
- Leave blank if unknown.

------------------------------------------------------------
## 5.9 County List

- Required.  
- Must match official county list.  
- Semicolon‑delimited.  
- Alphabetized.  
- No duplicates.  
- Never infer counties.  
- A multi‑county segment is **one entity**, never segmented.

------------------------------------------------------------
## 5.10 Township & Municipality

- Must match authoritative jurisdiction names.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  
- If many jurisdictions → use jurisdiction of Address (if present).

------------------------------------------------------------
## 5.11 GPS Coordinates

- Format: `lat,lon` (no space).  
- Accept only authoritative coordinates.  
- Reject placeholders, centroids, or unverifiable coordinates.  
- Leave blank if verification fails.

------------------------------------------------------------
## 5.12 Geometry

- Use `geometry_resolved` exactly as provided.  
- Do not simplify, smooth, or infer geometry.  
- Preserve coordinate precision.  
- If geometry is malformed → leave blank and flag uncertainty.  
- All geometry conflicts must be preserved in provenance.

------------------------------------------------------------
## 5.13 Plus Code

- Generate only from accepted GPS.  
- If GPS blank → Plus Code blank.

------------------------------------------------------------
## 5.14 Trail Network Membership

- Must match normalized Trail Network names.  
- Semicolon‑delimit if multiple.  
- Never infer membership.  
- If ambiguous → flag uncertainty.

Audit:
- Log all membership conflicts.

------------------------------------------------------------
## 5.15 Notes

- Optional free‑text.  
- Must not include identity‑defining characteristics.  
- Must not include internal features or Access Point details.  
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.16 URLs

- Full `https://` URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- No placeholders or inferred URLs.  
- Normalize by removing tracking parameters.

------------------------------------------------------------
## 5.17 Derived Label (computed during normalization)

### Rules

- Derived Label **is computed here** in v4.0.  
- Must be derived solely from normalized fields.  
- Must be deterministic.  
- Must follow the Derived Label rules in TSV Output Specification v4.0.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail Segment spanning multiple counties produces **one normalized entity**.  
- County List must be semicolon‑delimited and alphabetized.  
- Boundary metadata must reflect all counties traversed.  
- Never segment multi‑county Trail Segments.

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

### 9.1 Conflicting Names or Identifiers
- Use the most authoritative source.  
- Record alternates in Description.

### 9.2 Conflicting Length
- Use the most authoritative source.  
- If conflict persists → Resolution Engine v4.0.

### 9.3 Conflicting Surface, Use, or Status
- Use authoritative trail system sources.  
- If unclear → Resolution Engine v4.0.

### 9.4 Conflicting Geometry
- Preserve all geometry claims in metadata.  
- Use the most authoritative geometry for normalization.  
- If unclear → Resolution Engine v4.0.

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
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Vocabulary Module v4.0  
- Trail Segment Schema Module v4.0  
- Trail Schema Module v4.0  
- TSV Output Specification (Trail Segments) v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Trail Normalization Contract v4.0  
- Trail Network Normalization Contract v4.0  
- Resolution Engine v4.0  
- Audit & Logging Module v4.0  
- Processing / Orchestration Module v4.0  

------------------------------------------------------------
# END OF TRAIL SEGMENT NORMALIZATION CONTRACT v4.0