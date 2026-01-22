# NATURAL AREAS PROJECT — SITE NORMALIZATION CONTRACT v3.2.2
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Raw Candidate Records into fully normalized Site entities under the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Vocabulary Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Site discoveries are normalized  
- How each Site Schema v3.2.2 field is populated  
- How Category, Subtype, Designation, Status, Features, and Network Affiliation are validated  
- How parent relationships (Site → Site) are validated using the **Child Site Rules Module v3.2.2**  
- How GPS, Plus Code, Address, and URL rules are applied  
- How normalization integrates with the Audit & Logging Module v3.2.2  
- How conflicts and uncertainties are surfaced to the Resolution Module v3.2.2  

**Derived Label is not constructed during normalization.**  
It is computed only during TSV output.

This module is authoritative for Site normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record  
From **Discovery Output Specification v3.2.2**, including:

- name_raw  
- counties_raw  
- municipalities_raw, townships_raw  
- ownership_raw, access_level_raw  
- gps_raw, address_raw  
- url_primary_raw, url_all_raw  
- network_affiliations_raw  
- parent_site_raw  
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
- **Site Vocabulary Module v3.2.2**  
  - Category  
  - Subtype  
  - Designation  
  - Status  
  - Features  
  - Network Affiliation  

## 2.4 Schema Modules  
- **Site Schema Module v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Site Network Schema Module v3.2.2** (for affiliation validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Site entity conforming to the **Site Schema Module v3.2.2**  
- A record ready for export via the **TSV Output Specification (Sites) v3.2.2**  
- Full audit trail entries via the **Audit & Logging Module v3.2.2**  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize name  
4. Normalize Category, Subtype, Designation, Status  
5. Normalize ownership, management, coordination  
6. Normalize Network Affiliation  
7. Normalize jurisdiction fields (County, Municipality, Township)  
8. Normalize location fields (GPS, Plus Code, Address)  
9. Normalize acreage  
10. Normalize features  
11. Normalize notes  
12. Normalize URLs and sources  
13. Validate Parent Site relationship using **Child Site Rules Module v3.2.2**  
14. Validate against schema  
15. Emit normalized Site entity  

**Derived Label is not constructed here.**  
It is computed only during TSV output.

If any critical step fails → surface to **Resolution Module v3.2.2**.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Name

- Use `name_raw` exactly as discovered, with minimal whitespace cleanup.  
- If multiple authoritative names exist → choose the most authoritative.  
- Former names go in Description.  
- Never invent names.  
- Never infer names from amenities or features.

Audit:
- Log all name conflicts.  
- Log all corrections.

------------------------------------------------------------
## 5.2 Category

- Must match a value from the Site Vocabulary Module v3.2.2.  
- Never infer from amenities, features, or trail presence.  
- If ambiguous → leave blank and flag uncertainty.

------------------------------------------------------------
## 5.3 Subtype

- Optional.  
- Must match the Category‑dependent subtype list.  
- Must not describe habitat conditions or temporary states.  
- Leave blank if no subtype applies.

------------------------------------------------------------
## 5.4 Designation

- Must match vocabulary values.  
- Semicolon‑delimit if multiple.  
- Never infer.  
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.5 Status

- Must match vocabulary values.  
- “Closed” = permanently closed.  
- “Proposed” must be officially documented.  
- Never infer from imagery.

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
## 5.9 Network Affiliation

- Normalize only documented affiliations.  
- Semicolon‑delimit if multiple.  
- Must match known organizations or networks.  
- Must not be used for parent–child relationships.  
- Must not imply hierarchy or ownership.  
- Must be supported by authoritative sources.

------------------------------------------------------------
## 5.10 Description

- 1–3 sentences.  
- Must describe identity‑defining ecological, historical, or cultural characteristics.  
- Include naming history and former names.  
- Must not include amenities or temporary conditions.

------------------------------------------------------------
## 5.11 Address

- Use authoritative address if available.  
- Partial address allowed if verifiable.  
- Never invent.  
- Leave blank if none.

------------------------------------------------------------
## 5.12 Acres

- Numeric only.  
- No units.  
- Never estimate.  
- Leave blank if unknown.

------------------------------------------------------------
## 5.13 Jurisdiction (Municipality/Township)

- Must match authoritative jurisdiction names.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  
- If many jurisdictions → use jurisdiction of Address.

------------------------------------------------------------
## 5.14 County

- Required.  
- Must match official Ohio county list.  
- Semicolon‑delimit if multi‑county.  
- Alphabetical order.  
- Omit the word “County.”  
- A Site spanning multiple counties must have **one normalized entity**.

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
## 5.17 Features

- Semicolon‑delimited list.  
- Must match vocabulary values.  
- Features describe internal components, not identity‑bearing units.  
- Named trails are never Features.  
- Minor connectors → Notes, not Features.

------------------------------------------------------------
## 5.18 Notes

- Optional free‑text.  
- Must not include identity‑defining ecology.  
- Must not include internal features.  
- Use for temporary closures, access restrictions, historical notes.

------------------------------------------------------------
## 5.19 URLs

- Full https:// URLs only.  
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
## 5.21 Parent Site

- Leave blank for top‑level Sites.  
- Must match normalized parent Site name.  
- A Site may have only one parent.  
- Parent–child relationships must be explicit in authoritative sources.  
- Must follow the **Child Site Rules Module v3.2.2**.

------------------------------------------------------------
# 6. VALIDATION LOGIC

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
# 7. DELIMITER‑INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks  
- No spaces between delimiters  
- No trailing spaces  
- No collapsed delimiters  
- No missing or extra delimiters  

All anomalies must be logged.

------------------------------------------------------------
# 8. CONFLICT RESOLUTION RULES

### 8.1 Conflicting Names
- Use the most authoritative source.  
- Record alternates in Description.

### 8.2 Conflicting Ownership
- Flag for Resolution; never infer.

### 8.3 Conflicting Acreage
- Use the most authoritative source.  
- If conflict persists → Resolution.

### 8.4 Conflicting Network Affiliations
- Use authoritative documentation.  
- If unclear → Resolution.

------------------------------------------------------------
# 9. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.  
- Never estimate.  
- Never infer ownership, designation, acreage, or affiliation.  
- Never generate GPS without verification.

------------------------------------------------------------
# 10. AUDITABILITY REQUIREMENTS

Normalization must:

- Record all sources used  
- Record conflicts  
- Record unverifiable claims  
- Record normalization decisions  
- Record delimiter‑integrity validation  
- Never overwrite user‑provided data without surfacing the change  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **Site Vocabulary Module v3.2.2**  
- **Site Schema Module v3.2.2**  
- **TSV Output Specification (Sites) v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Resolution Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v3.2.2