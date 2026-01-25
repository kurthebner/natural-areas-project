# NATURAL AREAS PROJECT
# ACCESS POINT NORMALIZATION CONTRACT v4.0 (REVISED)
(Authoritative Field‑Level Rules for Normalizing Resolved Access Point Entities)

This module defines the v4.0 normalization rules applied by the
Normalization Engine v4.0 to transform Resolved Access Point entities into
Normalized Access Point Objects v4.0 ready for insertion into the
Entity Graph Schema v4.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Access Point Vocabulary Module v4.0.

This module is authoritative for Access Point normalization only.

------------------------------------------------------------
# 1. PURPOSE

The Access Point Normalization Contract v4.0 defines:

- How a Resolved Access Point becomes a Normalized Access Point  
- How each Access Point Schema v4.0 field is validated and normalized  
- How Access Point Type, Access Level, Role, and Status are normalized  
- How identity parents (Site or Trail Segment) are validated  
- How additional parent associations are normalized for the Entity Graph  
- How County, Township, and Municipality are normalized  
- How GPS, Plus Code, and Address rules are applied  
- How URLs and source fields are normalized  
- How normalization interacts with the Normalization Engine v4.0  
- How provenance, conflicts, and uncertainties are recorded  
- How normalized entities integrate with the Entity Upsert Engine v4.0  

Normalization must:
- Never invent data  
- Never infer Access Point Type, Access Level, or parent entity  
- Never silently correct malformed values  
- Always log normalization decisions  

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Entity Object
From Resolution Engine v4.0, including:

- resolved identity key  
- resolved entity_type = "Access Point"  
- resolved access_point_type  
- resolved access_level  
- resolved role (if any)  
- resolved identity parent (Site or Trail Segment)  
- resolved additional parent associations (if any)  
- resolved county  
- resolved jurisdiction fields  
- resolved conflicts and uncertainties  

## 2.2 Raw Discovery Record v4.0
Including:

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
- source_* fields  
- discovery_tier, discovered_in_tiers  
- seeded_from_baseline, baseline_id  
- discovery_metadata  

## 2.3 Vocabulary Modules v4.0
- Access Point (Type, Access Level, Role, Status)

## 2.4 Schema Modules v4.0
- Access Point Schema Module v4.0  
- Site Schema Module v4.0  
- Trail Segment Schema Module v4.0  
- Child Site Rules Module v4.0 (for parent validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Access Point Object v4.0 conforming to the Access Point Schema Module v4.0  
- A Normalization Provenance Record  
- A Validation Result Object (warnings, errors)  
- A normalized entity ready for the Entity Upsert Engine v4.0  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Resolved Access Point  
2. Validate identity and entity_type  
3. Normalize name  
4. Normalize Access Point Type  
5. Normalize Access Level, Role, and Status  
6. Resolve and validate identity parent (Site or Trail Segment)  
7. Normalize additional parent associations  
8. Normalize jurisdiction fields (County, Municipality, Township)  
9. Normalize location fields (GPS, Plus Code, Address)  
10. Normalize notes  
11. Normalize URLs and sources  
12. Validate against Access Point Schema v4.0  
13. Emit Normalized Access Point + provenance  

Derived Label is not constructed here.
It is computed only during TSV output.

If any critical step fails → return error to Normalization Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

## 5.1 Name

Rules:
- Use name_raw with minimal whitespace cleanup.  
- Never invent names.  
- Never infer names from amenities or context.  
- Placeholder names (e.g., “Unnamed Access Point”) are preserved and flagged.  

Audit:
- Log all corrections and conflicts.

------------------------------------------------------------
## 5.2 Access Point Type

Rules:
- Must match a controlled value from Access Point Vocabulary v4.0.  
- Known synonyms may be mapped to canonical values (log all mappings).  
- If unmappable → leave blank and flag uncertainty.  
- Never infer type from amenities alone.  

Audit:
- Log all mappings and unmappable values.

------------------------------------------------------------
## 5.3 Role (Optional)

Rules:
- If present, map to Access Point Role vocabulary.  
- If vocabulary does not define roles → preserve raw value.  
- If malformed → leave blank and flag uncertainty.  

Audit:
- Log all role mappings.

------------------------------------------------------------
## 5.4 Parent Entity (Identity Parent)

Rules:
- An Access Point must have exactly one identity parent:  
  - A Site, or  
  - A Trail Segment  
- Identity parent must be a normalized entity.  
- If multiple candidates exist:  
  - Prefer the Trail Segment if the AP is clearly a trailhead.  
  - Otherwise prefer the Site supported by authoritative sources.  
  - If ambiguity remains → leave parent blank and surface to Resolution.  

Prohibited:
- Assigning multiple identity parents.  
- Using Trail, Trail Network, or Site Network as identity parents.  
- Inferring parents from proximity alone.  

Audit:
- Log all parent resolutions and conflicts.

------------------------------------------------------------
## 5.5 Additional Parent Associations (v4.0)

Rules:
- Additional parents (Site, Trail, Trail Segment) may be preserved.  
- These are written to the access_point_parents relationship table.  
- Must not contradict the identity parent.  
- Must be supported by authoritative sources.  
- Never infer additional parents from proximity or geometry.  

Audit:
- Log all additional parent associations.

------------------------------------------------------------
## 5.6 Jurisdiction Fields

### County
- Required.  
- Must match official Ohio county list.  
- Must represent the county where the Access Point physically resides.  
- Must not be inferred solely from parent entity.  
- Multi‑county logic does not apply to Access Points.  

### Township & Municipality
- Include if validated.  
- Must not be invented or guessed.  
- Preserve both if both exist.  

Audit:
- Log all jurisdiction sources and conflicts.

------------------------------------------------------------
## 5.7 Location Fields

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
## 5.8 Access Level and Status

### Access Level
- Must match Access Level vocabulary v4.0.  
- If unmappable → leave blank and flag uncertainty.  

### Status
- Must match vocabulary values (if defined).  
- Leave blank if ambiguous.  

Audit:
- Log all mappings and conflicts.

------------------------------------------------------------
## 5.9 URLs and Sources

### URLs
- Must be full https:// URLs.  
- No placeholders or partial URLs.  
- Semicolon‑delimit if multiple.  

### Sources
- Preserve all datasets, maps, and GIS layers.  
- Must match Discovery Metadata where possible.  

Audit:
- Log URL corrections and all source lists.

------------------------------------------------------------
## 5.10 Notes

Rules:
- Preserve access‑related notes.  
- Do not move identity‑defining information into notes.  
- Notes may be concatenated from multiple raw sources.  

Audit:
- Log any structural changes to notes.

------------------------------------------------------------
## 5.11 Derived Label (TSV‑only)

Rules:
- Derived Label is not stored in normalized entities.  
- Derived Label is computed only during TSV output.  
- Must be derived solely from normalized fields.  
- All construction steps must be logged.  

------------------------------------------------------------
# 6. VALIDATION LOGIC

Normalization must validate:

- Vocabulary‑controlled fields  
- GPS format  
- Plus Code generation  
- Semicolon formatting  
- Field types  
- No invented data  
- Blank fields are true blanks  
- No delimiter characters inside fields  
- Parent entity validity  
- Additional parent association validity  

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

8.1 Conflicting Names:
- Use the most authoritative source.  
- Record alternates in metadata.  

8.2 Conflicting Access Levels:
- Use authoritative documentation.  
- If unclear → Resolution.  

8.3 Conflicting Parent Entities:
- Preserve all claims in metadata.  
- Do not assign a parent until resolved.  

8.4 Conflicting Jurisdiction:
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
- Never overwrite user‑provided data without logging the change  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Access Point Vocabulary Module v4.0  
- Access Point Schema Module v4.0  
- Site Schema Module v4.0  
- Trail Segment Schema Module v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Entity Graph Schema v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF ACCESS POINT NORMALIZATION CONTRACT v4.0 (REVISED)