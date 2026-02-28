# NATURAL AREAS PROJECT
# SITE NORMALIZATION CONTRACT v5.2
(Authoritative Field-Level Rules for Normalizing Resolved Site Entities)

This module defines the entity-specific normalization rules applied by the
Normalization Engine v5.x to produce a fully normalized Site entity conforming
to the Site Schema Module v5.2 and ready for insertion into the Entity Graph
Schema v5.x.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v5.x.

This contract is authoritative for Site normalization only.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.2

- Added normalization rules for new field: partner_agencies
- Updated organizational field cluster to four-tier model:
  ownership, governance, partner_agencies, coordination
- Updated validation rules to reflect new field
- Updated dependencies to v5.2 schema
- No changes to identity anchor or identity signature
- No changes to GIS-derived fields or GPS handling
- No changes to discovery expectations

------------------------------------------------------------
# 1. PURPOSE

The Site Normalization Contract v5.2 defines:

- How a Resolved Site is transformed into a Normalized Site
- How each Site Schema v5.2 field is validated and normalized
- How Category, Subtype, Designation, Status, and Features are normalized
- How organizational fields (ownership, governance, partner_agencies, coordination) are separated
- How parent-child relationships are validated using the Child Site Rules Module v5.x
- How GPS, Plus Code, Location, and jurisdiction fields are handled
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:

- Never invent data
- Never infer governance, ownership, partner agencies, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Site"
- resolved parent_site_id (if any)
- resolved county set
- resolved governance, ownership, partner_agencies, coordination
- resolved category, subtype, designation, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.x
Including:

- name_raw
- counties_raw
- ownership_raw
- governance_raw
- partner_agencies_raw (optional; may be absent)
- coordination_raw
- gps_raw ("lat,lon")
- location_raw
- url_primary_raw
- urls_raw
- parent_site_raw
- notes_raw
- description_raw
- features_raw
- discovery_metadata

Not in raw discovery (GIS-derived):
- municipality
- township

## 2.3 Normalization Engine Pre-Populated Fields
Before this contract runs, the Normalization Engine v5.x has already:

- Parsed gps_raw → gps_lat, gps_lon
- Computed plus_code
- Derived township via GIS spatial lookup
- Derived municipality via GIS spatial lookup

## 2.4 Vocabulary Modules v5.x
- Category, Subtype, Designation, Status, Features

## 2.5 Schema Modules v5.2
- Site Schema Module v5.2
- Child Site Rules Module v5.x

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A Normalized Site Object v5.2 conforming to the Site Schema Module v5.2
- A Normalization Provenance Record
- A Validation Result Object
- A normalized entity ready for the Entity Upsert Engine v5.x

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Site
2. Validate identity and entity_type = "Site"
3. Normalize name
4. Normalize Category, Subtype, Designation, Status
5. Normalize organizational fields:
   ownership → governance → partner_agencies → coordination
6. Normalize Counties
7. Validate GPS (gps_lat / gps_lon)
8. Validate Plus Code
9. Validate Township, Municipality
10. Normalize Location
11. Normalize Acres
12. Normalize Features
13. Normalize Description
14. Normalize Notes
15. Normalize URLs
16. Validate Parent Site relationship
17. Run identity anchor deduplication check
18. Validate against Site Schema v5.2
19. Emit Normalized Site + provenance

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Name
- Use resolved name or name_raw with minimal whitespace cleanup.
- Never infer from amenities or nearby entities.
- Alternate names → Description or Notes.

## 5.2 Category
- Must match vocabulary.
- Never infer from features or governance.
- Leave blank if ambiguous.

## 5.3 Subtype
- Optional.
- Must match subtype list for chosen Category.
- Leave blank if unclear.

## 5.4 Designation
- Must match vocabulary.
- Semicolon-delimited.
- Never infer from name or category.

## 5.5 Status
- Must match vocabulary.
- "Closed" = permanently closed.
- "Proposed" must be documented.

------------------------------------------------------------
# 5.6 Ownership
- Must contain the exact legal name of the owning entity.
- Must not use generic categories.
- Must not encode governance or partner roles.
- Leave blank if unverifiable.

------------------------------------------------------------
# 5.7 Governance
- Must contain exact names of managing organizations.
- Semicolon-delimited if multiple.
- Must not encode ownership or partner roles.
- If governance = ownership → repeat explicitly.

------------------------------------------------------------
# 5.8 Partner Agencies (NEW IN v5.2)
- Formal, documented co‑operator organizations.
- Must use exact organization names.
- Must not duplicate Ownership or Governance.
- Must not include informal volunteer groups.
- Must be supported by authoritative documentation.
- Leave blank if no formal partners exist.

Examples:
- Ohio Department of Natural Resources (ODNR)
- U.S. Army Corps of Engineers (USACE)
- Metroparks Toledo (when acting as co‑operator)

------------------------------------------------------------
# 5.9 Coordination
- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Ownership, Governance, or Partner Agencies.
- Must not use generic categories.
- Leave blank if no documented coordination exists.

Examples:
- Friends of Caesar Creek Lake
- Local trail volunteer associations

------------------------------------------------------------
# 5.10 Description
- 1–3 sentences.
- Identity-defining ecological, historical, or physical character.
- Must not include governance, ownership, or amenities.
- Must not contradict controlled fields.

------------------------------------------------------------
# 5.11 Location
- Full address OR general geographic description.
- Never invent street numbers.
- Must not include county names.
- Must not encode governance or access rules.

------------------------------------------------------------
# 5.12 Acres
- Numeric only.
- Never estimate or average.
- Use most authoritative source.

------------------------------------------------------------
# 5.13 Counties
- Required.
- Alphabetized.
- Semicolon-delimited.
- Must omit the word "County".
- Multi-county Sites remain single entities.

------------------------------------------------------------
# 5.14 Municipality (GIS-derived)
- Must be GIS-derived.
- Must be a valid municipality name or blank.
- Never use discovery values.

------------------------------------------------------------
# 5.15 Township (GIS-derived)
- Must be GIS-derived.
- Must be a valid township name or blank.
- Never use discovery values.

------------------------------------------------------------
# 5.16 GPS (gps_lat / gps_lon)
- Both present or both blank.
- Must be numeric.
- Must be authoritative.
- If invalid → blank both fields.

------------------------------------------------------------
# 5.17 Plus Code
- Must be present if GPS present.
- Must be blank if GPS blank.
- Never manually entered.

------------------------------------------------------------
# 5.18 Features
- Semicolon-delimited.
- Must match vocabulary.
- Metadata in parentheses allowed.
- Trails, Trail Segments, Access Points, and child Sites are never Features.

------------------------------------------------------------
# 5.19 Notes
- Free text.
- Must not contradict controlled fields.
- Use for temporary closures, access nuance, historical context, parcel IDs, citations.

------------------------------------------------------------
# 5.20 URLs
url_primary:
- Single authoritative URL.
- Must be full https:// URL.

urls:
- Semicolon-delimited list of additional URLs.
- Remove duplicates.
- Full https:// URLs only.

------------------------------------------------------------
# 5.21 Parent Site
- Blank for top-level Sites.
- Must reference a valid parent_site_id.
- Must follow Child Site Rules Module v5.x.
- Must not be inferred from signage or layout.

------------------------------------------------------------
# 6. IDENTITY ANCHOR VALIDATION

Top-level Sites:
- entity_type + name + counties

Child Sites:
- entity_type + name + counties + parent_site_id

Normalization must verify:
- All anchor fields present
- Counties valid and alphabetized
- Parent Site ID valid if present

------------------------------------------------------------
# 7. VALIDATION LOGIC

Normalization must validate:

- Vocabulary-controlled fields
- Organizational field separation:
  ownership vs governance vs partner_agencies vs coordination
- GPS pairing and numeric format
- Plus Code derivation
- Acres numeric
- Semicolon formatting
- No invented data
- No placeholders
- No delimiter characters inside fields
- Parent Site validity
- Identity anchor completeness

------------------------------------------------------------
# 8. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields must be true blanks.
- No trailing spaces.
- No collapsed semicolons.
- No missing delimiters in multi-value fields.

------------------------------------------------------------
# 9. CONFLICT HANDLING

- Conflicting names → use most authoritative; log alternates.
- Conflicting ownership → flag; never infer.
- Conflicting acreage → use highest-authority source; log conflict.
- Conflicting category → leave blank; log conflict.

------------------------------------------------------------
# 10. MISSING DATA RULES

- Leave blank if unverifiable.
- Never estimate acres.
- Never infer ownership, governance, partner agencies, or designation.
- Never generate GPS without authoritative source.
- Never copy municipality or township from discovery.

------------------------------------------------------------
# 11. AUDITABILITY REQUIREMENTS

Normalization must record:

- All sources consulted
- All vocabulary mappings
- All conflicts
- All blank-field decisions
- All GPS parsing results
- All GIS derivations
- All delimiter corrections
- Identity anchor validation
- Deduplication check results

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This contract depends on:

- Site Vocabulary Module v5.x
- Site Schema Module v5.2
- Child Site Rules Module v5.x
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Graph Schema v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE NORMALIZATION CONTRACT v5.2