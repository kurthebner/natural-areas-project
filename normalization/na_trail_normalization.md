# NATURAL AREAS PROJECT — TRAIL NORMALIZATION CONTRACT v3.2.2
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Trail Raw Candidate Records into fully normalized Trail entities under the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Trail discoveries are normalized  
- How each Trail Schema v3.2.2 field is populated  
- How Trail Type, Surface, Use, Status, and Designation are validated  
- How Trail → Trail Network relationships are validated  
- How GPS, Plus Code, Address, and URL rules are applied  
- How multi‑county Trails are normalized  
- How normalization integrates with the Audit & Logging Module v3.2.2  
- How conflicts and uncertainties are surfaced to the Resolution Module v3.2.2  

**Derived Label is not constructed during normalization.**  
It is computed only during TSV output.

This module is authoritative for Trail normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record  
From **Discovery Output Specification v3.2.2**, including:

- name_raw  
- counties_raw  
- municipalities_raw, townships_raw  
- ownership_raw, management_raw  
- gps_raw, address_raw  
- url_primary_raw, url_all_raw  
- source_datasets_raw  
- source_maps_raw  
- source_gis_layers_raw  
- parent_trail_networks_raw  
- notes_raw  
- description_raw  
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
- **Trail Vocabulary Module v3.2.2**  
  - Trail Types  
  - Trail Surfaces  
  - Trail Uses  
  - Trail Status  
  - Trail Designations  

## 2.4 Schema Modules  
- **Trail Schema Module v3.2.2**  
- **Trail Segment Schema Module v3.2.2**  
- **Trail Network Schema Module v3.2.2**

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Trail entity conforming to the **Trail Schema Module v3.2.2**  
- A record ready for export via the **TSV Output Specification (Trails) v3.2.2**  
- Full audit trail entries via the **Audit & Logging Module v3.2.2**  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize name  
4. Normalize Trail Type, Surface, Use, Designation  
5. Normalize ownership, management, coordination  
6. Normalize jurisdiction fields  
7. Normalize location fields (GPS, Plus Code, Address)  
8. Normalize length  
9. Normalize Trail Network membership  
10. Normalize description  
11. Normalize notes  
12. Normalize URLs and sources  
13. Validate against schema  
14. Emit normalized Trail entity  

**Derived Label is not constructed here.**  
It is computed only during TSV output.

If any critical step fails → surface to **Resolution Module v3.2.2**.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Name

- Use `name_raw` exactly as discovered, with minimal whitespace cleanup.  
- If multiple authoritative names exist → choose the most authoritative.  
- Alternate names go in Description.  
- Never invent names.  
- Never infer names from segments, networks, or amenities.

Audit:
- Log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Trail Type

- Must match a value from the Trail Type vocabulary v3.2.2.  
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
- Never infer from amenities or signage alone.

------------------------------------------------------------
## 5.5 Designation

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer.  
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.6 Ownership

- Use `ownership_raw` if authoritative.  
- Must match vocabulary values (Federal, State, Park District, County, Township, Municipal, Land Trust, Private, Foundation, Corporate, HOA).  
- Never infer ownership.  
- Leave blank if unknown.

------------------------------------------------------------
## 5.7 Management

- Use operational manager(s).  
- Semicolon‑delimit if multiple.  
- If same as Ownership → repeat explicitly.  
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
## 5.13 County

- Required.  
- Must match official Ohio county list.  
- Semicolon‑delimit if multi‑county.  
- Alphabetical order.  
- Omit the word “County.”  
- A Trail spanning multiple counties must have **one normalized entity**.

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

------------------------------------------------------------
## 5.20 Derived Label (computed at TSV output)

### Rules

- Derived Label is **not stored** in normalized entities.  
- Derived Label is computed only during TSV output using the **TSV Output Specification v3.2.2**.  
- Must be derived solely from normalized fields.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. MULTI‑COUNTY NORMALIZATION RULES

- A Trail spanning multiple counties produces **one normalized entity**, not multiple.  
- The County field contains a **semicolon‑delimited, alphabetized list**.  
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
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- **Trail Vocabulary Module v3.2.2**  
- **Trail Schema Module v3.2.2**  
- **TSV Output Specification (Trails) v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Trail Network Normalization Contract v3.2.2**  
- **Trail Segment Normalization Contract v3.2.2**  
- **Resolution Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF TRAIL NORMALIZATION CONTRACT v3.2.2