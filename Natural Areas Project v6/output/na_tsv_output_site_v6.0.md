# NATURAL AREAS PROJECT
# SITE TSV OUTPUT SPECIFICATION v6.0
(Authoritative Formatting-Layer Specification for Normalized Site Entities)

This module defines the authoritative, deterministic rules for serializing
normalized Site entities into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v6.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v6.0.
All field definitions are defined in the Site Schema Module v6.0.
All normalization rules are defined in the Site Normalization Contract v6.0.

This module supersedes Site TSV Output Specification v5.2.

------------------------------------------------------------
# CHANGES FROM v5.2 → v6.0

- **Four new fields added** (IMP-011, IMP-012, IMP-013):
  - `habitat_type` (position 11) — ecological/natural character; open vocabulary
  - `access_notes` (position 13) — seasonal access caveats and access restrictions
  - `last_verified_date` (position 25) — DATE format (YYYY-MM-DD)
  - `field_verified` (position 26) — boolean
- **`parent_site_name` added alongside `parent_site_id`** (positions 27–28):
  Human-readable name of the parent Site. ID-only references are insufficient for
  human-readable output; every cross-entity ID reference in TSV output must be
  paired with the referenced entity's name.
- **Field count changed**: 25 → 30 fields; 24 → 29 tab delimiters per row.
- **Field order updated**: follows Site Schema Module v6.0 canonical order.
  `features` moved from position 19 to position 12 (between habitat_type and
  access_notes, reflecting schema group "Character").
  `notes` moved from position 20 to position 22 (after Plus Code).
- **`site_id` remains DB-only**: not included in TSV output.
- **All v5.2 structural rules carried forward**: delimiter rules, blank-field
  rules, whitespace rules, GPS pairing, multi-county representation.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The canonical TSV field order for Sites
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Multi-county representation rules
- Parent Site placement rules
- GPS field representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v6.x

This specification is authoritative for Site TSV formatting.

------------------------------------------------------------
# 2. FIELD ORDER (CANONICAL v6.0)

Site TSV output must contain exactly **31 fields** in the following order:

1.  name
2.  category
3.  subtype
4.  designation
5.  status
6.  ownership
7.  governance
8.  partner_agencies
9.  coordination
10. description
11. habitat_type *(new v6.0)*
12. features
13. access_notes *(new v6.0)*
14. location
15. acres
16. counties
17. municipality
18. township
19. gps_lat
20. gps_lon
21. plus_code
22. notes
23. url_primary
24. urls
25. last_verified_date *(new v6.0)*
26. field_verified *(new v6.0)*
27. parent_site_id
28. parent_site_name *(new v6.0 — human-readable name of parent Site)*
29. created_at
30. updated_at
31. ebird_hotspot_id *(new v6.0)*

This order is absolute and must never change.
No fields may be removed or reordered.

`site_id` is a DB-only field and must NOT appear in TSV output.

**Cross-entity reference rule**: Every field that references another entity by ID
must be immediately followed by a field containing that entity's human-readable
name. `parent_site_id` (position 27) is immediately followed by `parent_site_name`
(position 28). Both are blank for top-level Sites.

------------------------------------------------------------
# 3. FIELD NOTES

## Counties
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Multi-county Sites remain single rows

## Municipality / Township
- Populated by GIS spatial lookup during normalization
- Never collected during discovery
- May be blank if GIS lookup returns no result

## GPS Lat / GPS Lon
- Numeric values in WGS84 decimal degrees
- Both must be present or both blank
- No directional suffixes, no degree symbols

## Plus Code
- Derived from GPS Lat + GPS Lon
- Blank if GPS fields are blank

## Habitat Type
- Open vocabulary — no controlled value list
- Free-text ecological or natural character description
- Blank if not documented at discovery

## Features
- Semicolon-delimited; controlled vocabulary (Site Vocabulary Module v6.0 §6.2)
- Alphabetized
- Blank if no amenities documented

## Access Notes
- Free-text seasonal/public access caveats
- Blank if no access conditions documented

## URLs
- Semicolon-delimited list of additional URLs (from urls_raw)
- Represents the urls array from the normalized entity

## Last Verified Date
- ISO 8601 DATE format (YYYY-MM-DD)
- Populated at discovery with the discovery date
- Blank if not captured

## Field Verified
- Boolean: true or false
- Always false at discovery
- true indicates post-discovery physical field verification

## Parent Site ID / Parent Site Name
- `parent_site_id`: must match a valid site_id of a parent Site; blank for top-level Sites
- `parent_site_name`: the Name field of the referenced parent Site; blank for top-level Sites
- Both fields must be blank together or populated together — a Site with a parent_site_id
  must also have a parent_site_name and vice versa

## eBird Hotspot ID
- Optional; blank if no eBird hotspot exists for this site
- Format: eBird location code, typically `L` followed by digits (e.g., `L123456`)
- Captured during discovery; not normalized — passed through verbatim
- Enables joining this Site record to eBird sighting data in external systems

------------------------------------------------------------
# 4. MULTI-COUNTY REPRESENTATION RULES

Sites are not segmented by county.

- Multi-county Sites appear as a single TSV row.
- The Counties field contains a semicolon-delimited, alphabetized list.

Example: `Franklin;Union`

------------------------------------------------------------
# 5. DELIMITER RULES

- TSV uses tab characters only.
- Each row must contain exactly **30 tab characters** (31 fields → 30 delimiters).
- No field may contain a tab.
- No field may contain newline characters.

------------------------------------------------------------
# 6. BLANK-FIELD RULES

- Blank fields must be represented as true blanks: `\t\t`
- No spaces inside blank fields.
- No placeholder values (NULL, _, "", BLANK).

------------------------------------------------------------
# 7. WHITESPACE RULES

- No leading or trailing spaces in any field.
- No trailing spaces at end of line.
- Internal spaces allowed only when part of the field value.

------------------------------------------------------------
# 8. ROW CONSTRUCTION RULES

- Each row must contain exactly 31 fields.
- Each row must contain exactly 30 tabs.
- No field may be omitted.
- No field may be duplicated.
- Multi-county Sites remain single rows.

------------------------------------------------------------
# 9. TSV GENERATION ALGORITHM

1.  Receive normalized 31-field Site record.
2.  Validate GPS Lat / GPS Lon pairing.
3.  Validate Plus Code derivation.
4.  Validate Counties formatting (semicolon-delimited, alphabetized, no "County").
5.  Validate Features formatting (semicolon-delimited, alphabetized, vocabulary).
6.  Validate habitat_type (free-text or blank; no vocabulary enforcement).
7.  Validate access_notes (free-text or blank).
8.  Validate last_verified_date (YYYY-MM-DD or blank).
9.  Validate field_verified (boolean: true or false).
10. Validate Parent Site ID / Parent Site Name pairing (both blank or both populated).
11. Validate no internal tabs.
12. Validate no internal newlines.
13. Validate whitespace rules.
14. Join fields with tab characters.
15. Validate delimiter count (must be 30).
16. Validate blank-field representation.
17. Emit row.

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 10. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 30 tabs
- A field contains a tab or newline
- A blank field contains spaces
- A field contains trailing spaces
- GPS fields violate pairing rules
- Plus Code is inconsistent with GPS
- Counties field is not semicolon-delimited and alphabetized, or contains "County"
- Features field contains invalid vocabulary values
- last_verified_date contains non-DATE content
- field_verified contains a non-boolean value
- Vocabulary-controlled fields (category, subtype, designation, status) contain
  invalid values
- Organizational fields violate schema rules
- Parent Site ID is invalid (references nonexistent entity)
- Parent Site ID and Parent Site Name are not in sync (one blank, other populated)
- created_at or updated_at is missing
- Field order is incorrect
- A field is missing or duplicated

All errors must be logged in the Audit & Logging Module v6.x.

------------------------------------------------------------
# 11. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters (expect 29 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting
- Validate Features vocabulary values
- Validate GPS pairing and numeric format
- Validate Plus Code derivation
- Validate last_verified_date format
- Validate field_verified boolean
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 12. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0
- Site Vocabulary Module v6.0
- Site Normalization Contract v6.0
- TSV Integrity Check Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF SITE TSV OUTPUT SPECIFICATION v6.0
