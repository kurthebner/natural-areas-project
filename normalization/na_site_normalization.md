# NATURAL AREAS PROJECT  
# SITE NORMALIZATION CONTRACT v4.0  
(Authoritative Field‑Level Rules for Normalizing Resolved Site Entities)

This module defines the entity‑specific normalization rules applied by the  
**Normalization Engine v4.0** to produce a fully normalized **Site** entity  
conforming to the **Site Schema Module v4.0** and ready for insertion into the  
**Entity Graph Schema v4.0**.

This contract contains no controlled vocabularies.  
All vocabularies are defined in the **Site Vocabulary Module v4.0**.

This contract is authoritative for Site normalization only.

------------------------------------------------------------
# 1. PURPOSE

The Site Normalization Contract v4.0 defines:

- How a Resolved Site is transformed into a Normalized Site  
- How each Site Schema v4.0 field is validated and normalized  
- How Category, Subtype, Designation, Status, Features, and Network Affiliation are normalized  
- How parent–child relationships are validated using the **Child Site Rules Module v4.0**  
- How GPS, Plus Code, Address, and jurisdiction fields are normalized  
- How normalization interacts with the **Normalization Engine v4.0**  
- How provenance, conflicts, and uncertainties are recorded  
- How normalized entities integrate with the **Entity Upsert Engine v4.0**

Normalization must:

- Never invent data  
- Never infer governance, ownership, or identity  
- Never silently correct malformed values  
- Always log normalization decisions  

Derived Label is not computed here.  
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Entity Object  
From **Resolution Engine v4.0**, including:

- resolved identity key  
- resolved entity_type = "Site"  
- resolved parent_site (if any)  
- resolved county set  
- resolved governance, ownership, category, subtype  
- resolved conflicts and uncertainties  

## 2.2 Raw Discovery Record v4.0  
Including:

- name_raw  
- counties_raw  
- township_raw, municipality_raw  
- ownership_raw, access_level_raw  
- gps_raw, geometry_raw  
- address_raw  
- url_primary, url_all  
- parent_site_raw  
- notes_raw  
- description_raw  
- source_* fields  
- discovery_tier, discovered_in_tiers  
- seeded_from_baseline, baseline_id  
- discovery_metadata  

## 2.3 Vocabulary Modules v4.0  
- Category  
- Subtype  
- Designation  
- Status  
- Features  
- Network Affiliation  

## 2.4 Schema Modules v4.0  
- Site Schema Module v4.0  
- Child Site Rules Module v4.0  
- Site Network Schema Module v4.0 (for affiliation validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Object v4.0** conforming to the Site Schema Module v4.0  
- A **Normalization Provenance Record**  
- A **Validation Result Object** (warnings, errors)  
- A normalized entity ready for the **Entity Upsert Engine v4.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Resolved Site  
2. Validate identity and entity_type  
3. Normalize name  
4. Normalize Category, Subtype, Designation, Status  
5. Normalize governance, ownership, coordination  
6. Normalize Network Affiliation  
7. Normalize jurisdiction fields (county_list, municipality, township)  
8. Normalize location fields (GPS, Plus Code, Address)  
9. Normalize acreage  
10. Normalize features  
11. Normalize description  
12. Normalize notes  
13. Normalize URLs and sources  
14. Validate Parent Site relationship (Child Site Rules v4.0)  
15. Validate against Site Schema v4.0  
16. Emit Normalized Site + provenance  

If any critical step fails → return error to Normalization Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

## 5.1 Name

- Use `name_raw` with minimal whitespace cleanup.  
- If multiple authoritative names exist → Resolution Engine v4.0 chooses.  
- Former names → appended to Description.  
- Never infer names.  
- Never derive names from amenities or features.

Provenance: log all name conflicts and corrections.

------------------------------------------------------------
## 5.2 Category

- Must match a controlled value from Site Vocabulary Module v4.0.  
- Never infer from amenities, features, or trail presence.  
- If ambiguous → leave blank and log uncertainty.

------------------------------------------------------------
## 5.3 Subtype

- Optional.  
- Must match subtype list for the chosen Category.  
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
- “Proposed” must be explicitly documented.  
- Never infer from imagery or social media.

------------------------------------------------------------
## 5.6 Ownership

- Use `ownership_raw` only if it contains the **actual legal name** of the owning entity.
- Must not use generic categories (e.g., “State Government”, “Municipal Agency”).
- Must not encode management, governance, designation, or temporary conditions.
- Must not be inferred from signage alone.
- Leave blank if ownership cannot be verified from authoritative sources.
- All decisions must be logged in normalization provenance.

------------------------------------------------------------

## 5.7 Governance / Management

- Use the **actual name(s)** of the operational managing organization(s).
- Semicolon‑delimit if multiple managers are formally documented.
- Must not use generic categories (e.g., “County Agency”, “Nonprofit Organization”).
- Must not encode ownership, designation, or access rules.
- If governance is identical to ownership, repeat explicitly.
- Leave blank if unverifiable.
- All decisions must be logged in normalization provenance.

------------------------------------------------------------

## 5.8 Coordination

- Use only **formally documented partner organization names**.
- Must not use generic categories (e.g., “Government Partner”, “Nonprofit Partner”).
- Must not duplicate Ownership or Governance.
- Must not encode temporary volunteer activity or informal relationships.
- Leave blank if no documented coordination exists.
- All decisions must be logged in normalization provenance.

------------------------------------------------------------
## 5.9 Network Affiliation

- Normalize only documented affiliations.  
- Semicolon‑delimit if multiple.  
- Must match known networks or organizations.  
- Must not imply hierarchy or ownership.  
- Must not be used for parent–child relationships.  
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
## 5.13 Jurisdiction (Municipality / Township)

- Must match authoritative jurisdiction names.  
- Semicolon‑delimit if multiple.  
- Must not include county names.  
- If multiple jurisdictions → use jurisdiction of Address.

------------------------------------------------------------
## 5.14 County List

- Required.  
- Must match official Ohio county list.  
- Alphabetized.  
- Semicolon‑delimited.  
- Omit the word “County.”  
- Multi‑county Sites must produce one normalized entity.

------------------------------------------------------------
## 5.15 GPS Coordinates

- Format: `lat,lon` (no space).  
- Accept only authoritative coordinates.  
- Reject placeholders, centroids, unverifiable coordinates.  
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

- Optional free text.  
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
## 5.20 Derived Label (TSV‑Only)

- Not stored in normalized entities.  
- Computed only during TSV output.  
- Derived solely from normalized fields.  
- All construction steps logged.

------------------------------------------------------------
## 5.21 Parent Site

- Leave blank for top‑level Sites.  
- Must match normalized parent Site ID (not name).  
- A Site may have only one parent.  
- Parent–child relationships must be explicit in authoritative sources.  
- Must follow **Child Site Rules Module v4.0**.

------------------------------------------------------------
# 6. VALIDATION LOGIC

Normalization must validate:

- All vocabulary‑controlled fields  
- GPS format  
- Plus Code generation  
- Semicolon formatting  
- Field types  
- No invented data  
- Blank fields are true blanks  
- No delimiter characters inside fields  

If any field fails validation:

- Surface the issue  
- Do not silently correct  
- Log in normalization provenance  

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
- Flag for Resolution Engine v4.0; never infer.

### 8.3 Conflicting Acreage
- Use the most authoritative source.  
- If conflict persists → Resolution Engine v4.0.

### 8.4 Conflicting Network Affiliations
- Use authoritative documentation.  
- If unclear → Resolution Engine v4.0.

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
- Never overwrite user‑provided data without logging the change  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- Site Vocabulary Module v4.0  
- Site Schema Module v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Child Site Rules Module v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Entity Graph Schema v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v4.0