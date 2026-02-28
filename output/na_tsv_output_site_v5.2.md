# NATURAL AREAS PROJECT
# SITE TSV OUTPUT SPECIFICATION v5.2
(Authoritative Formatting-Layer Specification for Normalized Site Entities)

This module defines the authoritative, deterministic rules for serializing
normalized Site entities into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v5.2 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Vocabulary Module v5.x.
All field definitions are defined in the Site Schema Module v5.2.
All normalization rules are defined in the Site Normalization Contract v5.x.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.2

- Added new field: partner_agencies (schema v5.2)
- Removed deprecated fields:
  - Map URL (removed from schema in v5.0)
  - Derived Label (removed from schema in v5.0; no longer computed)
- Updated field names to match schema:
  - URL → url_primary
  - Parent Site → parent_site_id
  - Site ID → site_id
- Updated canonical field order to match schema v5.2
- Field count changed from 26 → **25**
- Updated validation rules to reflect new organizational field cluster:
  ownership, governance, partner_agencies, coordination

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
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for Site TSV formatting.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All normalized Site records
- All counties and all processing runs
- All automated or manual TSV exports
- All v5.x normalization workflows
- All multi-entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank-field representation
- Multi-county representation
- Parent Site placement
- GPS field representation

------------------------------------------------------------
# 3. FIELD ORDER (CANONICAL v5.2)

Site TSV output must contain exactly **25 fields** in the following order:

1. name
2. category
3. subtype
4. designation
5. status
6. ownership
7. governance
8. partner_agencies
9. coordination
10. description
11. location
12. acres
13. counties
14. municipality
15. township
16. gps_lat
17. gps_lon
18. plus_code
19. features
20. notes
21. url_primary
22. urls
23. parent_site_id
24. created_at
25. updated_at

This order is absolute and must never change.

No additional fields may be added.
No fields may be removed or reordered.

------------------------------------------------------------
# 4. FIELD NOTES

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

## URLs
- Semicolon-delimited list of additional URLs
- Represents the urls array from the normalized entity

## Parent Site ID
- Must match a valid site_id of a parent Site
- Blank for top-level Sites

------------------------------------------------------------
# 5. MULTI-COUNTY REPRESENTATION RULES

Sites are not segmented by county.

- Multi-county Sites appear as a single TSV row.
- The Counties field contains a semicolon-delimited, alphabetized list.

Example:
Franklin;Union

------------------------------------------------------------
# 6. DELIMITER RULES

- TSV uses tab characters only.
- Each row must contain exactly **24 tab characters** (25 fields → 24 delimiters).
- No field may contain a tab.
- No field may contain newline characters.

------------------------------------------------------------
# 7. BLANK-FIELD RULES

- Blank fields must be represented as true blanks: \t\t
- No spaces inside blank fields.
- No placeholder values (NULL, _, "", BLANK).

------------------------------------------------------------
# 8. WHITESPACE RULES

- No leading or trailing spaces in any field.
- No trailing spaces at end of line.
- Internal spaces allowed only when part of the field value.

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

- Each row must contain exactly 25 fields.
- Each row must contain exactly 24 tabs.
- No field may be omitted.
- No field may be duplicated.
- Multi-county Sites remain single rows.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

1. Receive normalized 25-field Site record.
2. Validate GPS Lat / GPS Lon pairing.
3. Validate Plus Code derivation.
4. Validate Counties formatting.
5. Validate Parent Site ID.
6. Validate no internal tabs.
7. Validate no internal newlines.
8. Validate whitespace rules.
9. Join fields with tab characters.
10. Validate delimiter count (must be 24).
11. Validate blank-field representation.
12. Emit row.

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 24 tabs
- A field contains a tab or newline
- A blank field contains spaces
- A field contains trailing spaces
- GPS fields violate pairing rules
- Plus Code is inconsistent with GPS
- Counties field is not semicolon-delimited and alphabetized
- Vocabulary-controlled fields contain invalid values
- Organizational fields violate schema rules
- Parent Site ID is invalid
- created_at or updated_at is missing
- Field order is incorrect
- A field is missing or duplicated

All errors must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting
- Validate Parent Site ID
- Validate GPS pairing and numeric format
- Validate Plus Code derivation
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v5.2
- Site Vocabulary Module v5.x
- Site Normalization Contract v5.x
- Child Site Rules Module v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing / Orchestration Module v5.x

------------------------------------------------------------
# END OF SITE TSV OUTPUT SPECIFICATION v5.2