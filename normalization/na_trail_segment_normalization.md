# NATURAL AREAS PROJECT — TRAIL SEGMENT NORMALIZATION CONTRACT v3.2.2
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Trail Segment Raw Candidate Records into fully normalized Trail Segment entities
under the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Segment Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Trail Segment discoveries are normalized  
- How each Trail Segment Schema v3.2.2 field is populated  
- How Segment Type, Surface, Status, and Use are validated  
- How parent Trail relationships are validated  
- How geometry, GPS, Plus Code, and URL rules are applied  
- How multi‑county segments are normalized  
- How normalization integrates with the Audit & Logging Module v3.2.2  
- How conflicts and uncertainties are surfaced to the Resolution Module v3.2.2  

**Derived Label is not constructed during normalization.**  
It is computed only during TSV output.

This module is authoritative for Trail Segment normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record  
From **Discovery Output Specification v3.2.2**, including:

- name_raw  
- parent_trail_raw  
- counties_raw  
- municipalities_raw, townships_raw  
- surface_raw, status_raw, use_raw  
- gps_raw  
- geometry_raw  
- length_raw  
- url_primary_raw, url_all_raw  
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
- **Trail Segment Vocabulary Module v3.2.2**  
  - Segment Types  
  - Segment Surfaces  
  - Segment Uses  
  - Segment Status  

## 2.4 Schema Modules  
- **Trail Segment Schema Module v3.2.2**  
- **Trail Schema Module v3.2.2** (for parent validation)  
- **Trail Network Schema Module v3.2.2** (for association validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Trail Segment entity conforming to the **Trail Segment Schema Module v3.2.2**  
- A record ready for export via the **TSV Output Specification (Trail Segments) v3.2.2**  
- Full audit trail entries via the **Audit & Logging Module v3.2.2**  

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
10. Normalize description  
11. Normalize notes  
12. Normalize URLs and sources  
13. Validate against schema  
14. Emit normalized Trail Segment entity  

**Derived Label is not constructed here.**  
It is computed only during TSV output.

If any critical step fails → surface to **Resolution Module v3.2.2**.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Segment Name

- Use `name_raw` exactly as discovered, with minimal whitespace cleanup.  
- If multiple authoritative names/IDs exist → choose the most authoritative.  
- Alternate names go in Description.  
- Never invent names.  
- Never infer names from geometry or map labels alone.

Audit:
- Log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Parent Trail

- Required.  
- Must match the exact normalized name of a Trail entity.  
- If parent Trail is not yet normalized → create a placeholder Trail for Resolution.  
- Never infer parentage from proximity or geometry alone.  
- A Trail Segment must have exactly one parent Trail.

Audit:
- Log all parent conflicts and unverifiable relationships.

------------------------------------------------------------
## 5.3 Segment Type

- Must match a value from the Segment Type vocabulary v3.2.2.  
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
## 5.9 County

- Required.  
- Must match official Ohio county list.  
- Semicolon‑delimit if multi‑county.  
- Alphabetical order.  
- Omit the word “County.”  
- A Trail Segment spanning multiple counties must have **one normalized entity**.

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

- Use `geometry_raw` exactly as discovered.  
- Do not simplify, smooth, or infer geometry.  
- Preserve coordinate precision.  
- If geometry is malformed → leave blank and flag uncertainty.

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

------------------------------------------------------------
## 5.17 Derived Label (computed at TSV output)

### Rules

- Derived Label is **not stored** in normalized entities.  
- Derived Label is computed only during TSV output using the **TSV Output Specification v3.2.2**.  
- Must be derived solely from normalized fields.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail Segment spanning multiple counties produces **one normalized entity**, not multiple.  
- The County field contains a **semicolon‑delimited, alphabetized list**.  
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
- Surface to Resolution  
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
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- **Trail Segment Vocabulary Module v3.2.2**  
- **Trail Segment Schema Module v3.2.2**  
- **Trail Schema Module v3.2.2**  
- **TSV Output Specification (Trail Segments) v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Trail Normalization Contract v3.2.2**  
- **Trail Network Normalization Contract v3.2.2**  
- **Resolution Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF TRAIL SEGMENT NORMALIZATION CONTRACT v3.2.2