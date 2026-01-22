# NATURAL AREAS PROJECT — ACCESS POINT NORMALIZATION CONTRACT v3.2.2
Authoritative, deterministic, field‑by‑field normalization contract for transforming
Access Point Raw Candidate Records into fully normalized Access Point entities
under the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Access Point Vocabulary Module v5**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How raw Access Point discoveries are normalized  
- How each Access Point Schema v3.2.2 field is populated  
- How Access Point Type, Role, Status, and Access Level are validated  
- How identity parents (Site or Trail Segment) are validated  
- How multi‑parent associations are preserved in metadata  
- How County, Township, and Municipality are normalized  
- How GPS, Plus Code, and Address rules are applied  
- How URLs and source fields are normalized  
- How normalization integrates with the Audit & Logging Module v3.2.2  
- How conflicts and uncertainties are surfaced to the Resolution Module v3.2.2  

**Derived Label is not constructed during normalization.**  
It is computed only during TSV output.

This module is authoritative for Access Point normalization.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Raw Candidate Record  
From **Discovery Output Specification v3.2.2**, including:

- name_raw  
- access_point_type_raw  
- access_level_raw  
- role_raw  
- counties_raw  
- municipalities_raw, townships_raw  
- parent_sites_raw  
- parent_trail_segments_raw  
- gps_raw, address_raw  
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
- **Access Point Vocabulary Module v5**  
  - Access Point Type  
  - Access Level  
  - Access Point Role  
  - Status (if defined)

## 2.4 Schema Modules  
- **Access Point Schema Module v3.2.2**  
- **Site Schema Module v3.2.2**  
- **Trail Segment Schema Module v3.2.2**  
- **Child Site Rules Module v3.2.2** (for parent validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A normalized Access Point entity conforming to the **Access Point Schema Module v3.2.2**  
- A record ready for export via the **TSV Output Specification (Access Points) v3.2.2**  
- Full audit trail entries via the **Audit & Logging Module v3.2.2**  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Raw Candidate Record  
2. Validate identity  
3. Normalize name  
4. Normalize Access Point Type  
5. Normalize Access Level and Status  
6. Resolve and validate identity parent (Site or Trail Segment)  
7. Normalize jurisdiction fields (County, Municipality, Township)  
8. Normalize location fields (GPS, Plus Code, Address)  
9. Normalize notes  
10. Normalize URLs and sources  
11. Validate against schema  
12. Emit normalized Access Point entity  

**Derived Label is not constructed here.**  
It is computed only during TSV output.

If any critical step fails → surface to **Resolution Module v3.2.2**.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

------------------------------------------------------------
## 5.1 Name

- Use `name_raw` exactly as discovered, with minimal whitespace cleanup.  
- Never invent names.  
- Never infer names from amenities or context.  
- If placeholder names appear (e.g., “Unnamed Access Point”), preserve them and flag uncertainty.

Audit:
- Log all corrections and conflicts.

------------------------------------------------------------
## 5.2 Access Point Type

- Must match a value from **Access Point Vocabulary v5**.  
- If raw value is a known synonym → map to canonical value and log.  
- If unmappable → leave blank and flag uncertainty.  
- Never infer type from amenities alone.

Audit:
- Log all mappings and unmappable values.

------------------------------------------------------------
## 5.3 Role (Optional)

- If present, map to the **Access Point Role** vocabulary.  
- If vocabulary does not define roles → preserve raw value.  
- If malformed → leave blank and flag uncertainty.

Audit:
- Log all role mappings.

------------------------------------------------------------
## 5.4 Parent Entity (Identity Parent)

### Rules

- An Access Point must have **exactly one identity parent**:  
  - A **Site**, or  
  - A **Trail Segment**  

- Identity parent must be a **normalized entity**.  
- If multiple candidates exist:  
  - Prefer the **Trail Segment** if the AP is clearly a trailhead for that segment.  
  - Otherwise prefer the **Site** supported by authoritative sources.  
  - If ambiguity remains → leave parent blank and surface to Resolution.

### Prohibited

- Assigning multiple identity parents.  
- Using Trail, Trail Network, or Site Network as identity parents.  
- Inferring parents from proximity alone.

Audit:
- Log all parent resolutions and conflicts.

------------------------------------------------------------
## 5.5 Jurisdiction Fields

### County

- Required.  
- Must match official Ohio county list.  
- Must represent the county where the Access Point physically resides.  
- Must not be inferred solely from parent entity.  
- Multi‑county logic does **not** apply to Access Points.

### Township & Municipality

- Include if validated.  
- Must not be invented or guessed.  
- Preserve both if both exist.

Audit:
- Log all jurisdiction sources and conflicts.

------------------------------------------------------------
## 5.6 Location Fields

### GPS

- Accept only authoritative coordinates.  
- Reject placeholders, centroids, or unverifiable coordinates.  
- Leave blank if verification fails.

### Plus Code

- Generate only from accepted GPS.  
- If GPS blank → Plus Code blank.

### Address

- Preserve as discovered with minimal cleanup.  
- Never invent or USPS‑normalize.

Audit:
- Log accepted/rejected GPS and Plus Code generation.

------------------------------------------------------------
## 5.7 Access Level and Status

### Access Level

- Must match **Access Level vocabulary v5**.  
- If unmappable → leave blank and flag uncertainty.

### Status

- Must match vocabulary values (if defined).  
- Leave blank if ambiguous.

Audit:
- Log all mappings and conflicts.

------------------------------------------------------------
## 5.8 URLs and Sources

### URLs

- Must be full `https://` URLs.  
- No placeholders or partial URLs.  
- Semicolon‑delimit if multiple.

### Sources

- Preserve all datasets, maps, and GIS layers.  
- Must match Discovery Metadata where possible.

Audit:
- Log URL corrections and all source lists.

------------------------------------------------------------
## 5.9 Notes

- Preserve access‑related notes.  
- Do not move identity‑defining information into notes.  
- Notes may be concatenated from multiple raw sources.

Audit:
- Log any structural changes to notes.

------------------------------------------------------------
## 5.10 Derived Label (computed at TSV output)

### Rules

- Derived Label is **not stored** in normalized entities.  
- Derived Label is computed only during TSV output using the **TSV Output Specification v3.2.2**.  
- Must be derived solely from normalized fields.  
- All construction steps must be logged.

------------------------------------------------------------
# 6. VALIDATION LOGIC

Normalization must validate:

- Vocabulary‑controlled fields  
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
- Record alternates in metadata.

### 8.2 Conflicting Access Levels
- Use authoritative documentation.  
- If unclear → Resolution.

### 8.3 Conflicting Parent Entities
- Preserve all claims in metadata.  
- Do not assign a parent until resolved.

### 8.4 Conflicting Jurisdiction
- Use the most authoritative source.  
- Preserve all claims in metadata.

------------------------------------------------------------
# 9. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.  
- Never estimate.  
- Never infer Access Point Type, Access Level, or parent entity.  
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

- **Access Point Vocabulary Module v5**  
- **Access Point Schema Module v3.2.2**  
- **TSV Output Specification (Access Points) v3.2.2**  
- **Discovery Protocol Module v3.2.2**  
- **Discovery Output Specification v3.2.2**  
- **Discovery Metadata Specification v3.2.2**  
- **Child Site Rules Module v3.2.2**  
- **Site Normalization Contract v3.2.2**  
- **Trail Segment Normalization Contract v3.2.2**  
- **Resolution Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF ACCESS POINT NORMALIZATION CONTRACT v3.2.2