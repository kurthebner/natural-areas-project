# NATURAL AREAS PROJECT
# SITE NETWORK NORMALIZATION CONTRACT v4.0
(Authoritative Field‑Level Rules for Normalizing Resolved Site Network Entities)

This module defines the v4.0 normalization rules applied by the
Normalization Engine v4.0 to transform Resolved Site Network entities into
Normalized Site Network Objects v4.0 ready for insertion into the
Entity Graph Schema v4.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Site Network Vocabulary Module v4.0.

This module is authoritative for Site Network normalization only.

------------------------------------------------------------
# 1. PURPOSE

The Site Network Normalization Contract v4.0 defines:

- How a Resolved Site Network becomes a Normalized Site Network  
- How each Site Network Schema v4.0 field is validated and normalized  
- How Network Type and Status are normalized  
- How multi‑county and multi‑state networks are normalized  
- How URLs, notes, and description fields are normalized  
- How normalization interacts with the Normalization Engine v4.0  
- How provenance, conflicts, and uncertainties are recorded  
- How normalized entities integrate with the Entity Upsert Engine v4.0  

Normalization must:

- Never invent data  
- Never infer membership, governance, or identity  
- Never silently correct malformed values  
- Always log normalization decisions  

Derived Label is **not** computed here.  
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

Normalization consumes:

## 2.1 Resolved Entity Object
From Resolution Engine v4.0, including:

- resolved identity key  
- resolved entity_type = "Site Network"  
- resolved network_type  
- resolved county set  
- resolved state set  
- resolved status  
- resolved member Site set (if any)  
- resolved conflicts and uncertainties  

## 2.2 Raw Discovery Record v4.0
Including:

- name_raw  
- network_type_raw  
- counties_raw  
- states_raw  
- status_raw  
- url_primary_raw, url_all_raw  
- member_sites_raw  
- notes_raw  
- description_raw  
- source_* fields  
- discovery_tier, discovered_in_tiers  
- seeded_from_baseline, baseline_id  
- discovery_metadata  

## 2.3 Vocabulary Modules v4.0
- Site Network Vocabulary Module v4.0  
- Site Vocabulary Module v4.0 (for member validation)

## 2.4 Schema Modules v4.0
- Site Network Schema Module v4.0  
- Site Schema Module v4.0 (for member validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Site Network Object v4.0 conforming to the Site Network Schema Module v4.0  
- A Normalization Provenance Record  
- A Validation Result Object (warnings, errors)  
- A normalized entity ready for the Entity Upsert Engine v4.0  

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH‑LEVEL)

1. Receive Resolved Site Network  
2. Validate identity and entity_type  
3. Normalize Network Name  
4. Normalize Network Type  
5. Normalize Status  
6. Normalize jurisdiction fields (Counties Traversed, States Included)  
7. Normalize member Sites  
8. Normalize Description  
9. Normalize Notes  
10. Normalize URLs  
11. Validate against Site Network Schema v4.0  
12. Emit Normalized Site Network + provenance  

Derived Label is not constructed here.  
It is computed only during TSV output.

If any critical step fails → return error to Normalization Engine v4.0.

------------------------------------------------------------
# 5. FIELD‑BY‑FIELD NORMALIZATION RULES

## 5.1 Network Name

Rules:
- Use name_raw with minimal whitespace cleanup.  
- If multiple authoritative names exist → Resolution chooses.  
- Alternate names must not be merged into the name field.  
- Never infer names from member Sites or branding.  
- Never invent names.

Audit:
- Log all name conflicts.  
- Log all corrections.

------------------------------------------------------------
## 5.2 Network Type

Rules:
- Must match a controlled value from the Site Network Vocabulary Module v4.0.  
- Never infer from member Sites, geography, or management.  
- If ambiguous → leave blank and log uncertainty (Resolution should have resolved this).  
- Must not encode governance or hierarchy.

------------------------------------------------------------
## 5.3 Status

Rules:
- Must match a controlled value from the Site Network Vocabulary Module v4.0.  
- “Proposed” must be explicitly documented.  
- Never infer status from member Sites or planning documents.  
- Leave blank if unverifiable.

------------------------------------------------------------
## 5.4 Counties Traversed

Rules:
- Required.  
- Must match official Ohio county names (minus the word “County”).  
- Alphabetized.  
- Semicolon‑delimited.  
- Must reflect the **resolved county set**.  
- Never infer from member Sites unless explicitly documented.  
- Never segment multi‑county networks.  
- Must follow the universal multi‑county rule v4.0.

------------------------------------------------------------
## 5.5 States Included (if multi‑state)

Rules:
- Use authoritative state names or abbreviations as defined in the schema.  
- Alphabetized.  
- Semicolon‑delimited.  
- Must reflect the **resolved state set**.  
- Never infer from member Sites unless explicitly documented.

------------------------------------------------------------
## 5.6 Member Sites

Rules:
- Must reference **normalized Site IDs**, not names.  
- Semicolon‑delimit if multiple.  
- Never infer membership.  
- Normalization must accept the resolved member Site set exactly as provided.  
- If a member Site is unresolved → this is a Resolution error, not a normalization decision.  
- Member Sites must be identity‑bearing Sites, not Features or Access Points.

Audit:
- Log all membership conflicts.  
- Log unverifiable membership claims.

------------------------------------------------------------
## 5.7 Description

Rules:
- 1–3 sentences.  
- Must describe identity‑defining characteristics of the network.  
- May include naming history and alternate names.  
- Must not include amenities or temporary conditions.  
- Must not include Site‑level descriptions.  
- Must not describe individual member Sites.

------------------------------------------------------------
## 5.8 Notes

Rules:
- Optional free text.  
- Must not include identity‑defining ecology.  
- Must not include Site‑level or child‑Site‑level details.  
- Use for temporary closures, access restrictions, or contextual notes.

------------------------------------------------------------
## 5.9 URLs

Rules:
- Full https:// URLs only.  
- Semicolon‑delimit if multiple.  
- Must be authoritative.  
- No placeholders or inferred URLs.  
- Must not include broken or malformed URLs.

------------------------------------------------------------
# 6. VALIDATION LOGIC

Normalization must validate:

- All vocabulary‑controlled fields  
- Semicolon formatting  
- Field types  
- No invented data  
- Blank fields are true blanks  
- No delimiter characters inside fields  
- Member Site references are valid normalized Site IDs  

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

8.1 Conflicting Names:  
- Use the most authoritative source (Resolution decides).  
- Record alternates in Description.

8.2 Conflicting Network Type:  
- Must defer to Resolution.  
- Never infer.

8.3 Conflicting Status:  
- Use authoritative documentation.  
- If unclear → Resolution Engine v4.0.

8.4 Conflicting County or State Lists:  
- Use authoritative documentation.  
- If conflict persists → Resolution Engine v4.0.

8.5 Conflicting Membership:  
- Must defer entirely to Resolution.  
- Normalization does not adjudicate membership.

------------------------------------------------------------
# 9. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.  
- Never estimate.  
- Never infer Network Type, Status, or membership.  
- Never infer counties or states from member Sites.  

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

- Site Network Vocabulary Module v4.0  
- Site Network Schema Module v4.0  
- Site Schema Module v4.0  
- Discovery Protocol Module v4.0  
- Discovery Output Specification v4.0  
- Discovery Metadata Specification v4.0  
- Resolution Engine v4.0  
- Normalization Engine v4.0  
- Entity Graph Schema v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v4.0