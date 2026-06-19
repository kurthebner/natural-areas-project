# NATURAL AREAS PROJECT
# ACCESS POINT TSV OUTPUT SPECIFICATION v6.0
(Authoritative Formatting-Layer Specification for Normalized Access Point Entities)

This module defines the authoritative, deterministic rules for serializing
normalized Access Point entities into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v6.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Access Point Vocabulary Module v6.0.
All field definitions are defined in the Access Point Schema Module v6.0.
All normalization rules are defined in the Access Point Normalization Contract v6.0.

This module supersedes Access Point TSV Output Specification v5.1.

------------------------------------------------------------
# CHANGES FROM v5.1 → v6.0

- **Identity Parent Entity Type updated** (Field 4): Allowed values changed from
  "Site, Trail, Trail Segment" to "Site, Trailthing".

- **Identity Parent Entity ID and Name both included** (Fields 5–6): v5.1 used
  entity Name only. v6.0 includes both the entity ID (OH-{COUNTY}-{TYPE}-{SEQ})
  and the entity Name, consistent with the rule that every cross-entity ID
  reference in TSV output must be paired with a human-readable name.

- **Two new fields added** (IMP-013):
  - `last_verified_date` (position 18) — ISO 8601 DATE format (YYYY-MM-DD)
  - `field_verified` (position 19) — boolean

- **Field count changed**: 17 → 21 fields; 16 → 20 tab delimiters per row.

- **All v5.1 structural rules carried forward**: delimiter rules, blank-field
  rules, whitespace rules, GPS pairing, single-county rule.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The canonical TSV field order for Access Points
- Delimiter rules
- Blank-field rules
- Whitespace rules
- GPS field representation rules
- Parent entity serialization rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v6.x

This specification is authoritative for Access Point TSV formatting.

------------------------------------------------------------
# 2. FIELD ORDER (CANONICAL v6.0)

Access Point TSV output must contain exactly **20 fields** in the following order:

1.  access_point_name
2.  access_point_type
3.  status
4.  identity_parent_entity_type
5.  identity_parent_entity_id
6.  identity_parent_entity_name *(human-readable name of the identity parent)*
7.  county
8.  township
9.  municipality
10. address
11. gps_lat
12. gps_lon
13. plus_code
14. features
15. identity_notes
16. notes
17. url
18. last_verified_date *(new)*
19. field_verified *(new)*
20. access_point_id

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**20 fields = 19 tab delimiters per row.**

**Cross-entity reference rule**: Every field that references another entity by ID
must be immediately followed by a field containing that entity's human-readable
name. `identity_parent_entity_id` (position 5) is immediately followed by
`identity_parent_entity_name` (position 6).

------------------------------------------------------------
# 3. FIELD NOTES

## Field 1 — Access Point Name
- Required; must never be blank.
- Human-readable, unique within the set of parent entities at the same location.
- If unnamed, normalization contract constructs a name using parent entity name +
  type (e.g., "Pickerel Creek Wildlife Area Boat Ramp").

## Field 2 — Access Point Type
- Required.
- Must match a valid value from Access Point Vocabulary Module v6.0.
- Single value only — compound types are never valid.

## Field 3 — Status
- Optional.
- Must match a valid value from Access Point Vocabulary Module v6.0:
  Active, Closed, Seasonal, Restricted.
- Describes the access point itself, not the parent entity.
- Blank if ambiguous or unverifiable.

## Field 4 — Identity Parent Entity Type
- Required; must never be blank.
- Must be exactly one of: **Site**, **Trailthing**
- Represents the single identity-defining parent relationship.
- Note: "Trail" and "Trail Segment" are no longer valid values — both are now
  Trailthing entities in v6.x.
- Additional parent relationships are stored in access_point_parents table
  and not represented in TSV output.

## Field 5 — Identity Parent Entity ID
- Required; must never be blank.
- Must match a valid entity ID in the project database.
- Format: OH-{COUNTY}-S-{SEQ} for Sites; OH-{COUNTY}-TT-{SEQ} for Trailthings.

## Field 6 — Identity Parent Entity Name *(new)*
- Required; must never be blank.
- The Name field of the entity referenced by identity_parent_entity_id.
- Both identity_parent_entity_id and identity_parent_entity_name must be populated
  together — neither may be blank without the other.

## Field 7 — County
- Required; must never be blank.
- Single county name — Access Points are point locations.
- Must not include the word "County."
- Must not be a semicolon-delimited list.

## Fields 8–9 — Township / Municipality
- Both optional.
- Populated via GIS spatial lookup during normalization.
- Must never be collected during web discovery.
- Blank if GIS lookup returns no result.

## Field 10 — Address
- Optional.
- Must be an authoritative or defensible address or road description.
- Must never be USPS-normalized.
- Must never contain an invented street number.

## Fields 11–12 — GPS Lat / GPS Lon
- Numeric values in WGS84 decimal degrees.
- Ohio GPS Lon values are negative.
- Both fields must be populated together; neither may appear without the other.
- May be blank pending GPS Acquisition Module resolution.

## Field 13 — Plus Code
- Derived from GPS Lat + GPS Lon by the Normalization Engine.
- Must not be manually constructed.
- Blank if GPS fields are blank.

## Field 14 — Features
- Optional.
- Semicolon-delimited flat list of documented facilities and amenities.
- Metadata may appear in parentheses: `Parking (50 spaces, 4 ADA)`
- Must describe features of the access point itself, not the parent entity.

## Field 15 — Identity Notes
- Optional.
- Type uncertainty flags, parent assignment notes, disambiguation notes,
  REVIEW flags from normalization, RECLASSIFICATION_CANDIDATE flag (IMP-114).

## Field 16 — Notes
- Optional.
- Short, factual, non-invented operational details specific to this access point.
- Gate conditions, seasonal constraints, parking limits, fees, signage.
- Customer-facing — no provenance artifacts (IMP-014).

## Field 17 — URL
- Optional.
- Full https:// URL(s) only. Semicolon-delimit if multiple.

## Field 18 — Last Verified Date *(new)*
- ISO 8601 DATE format (YYYY-MM-DD).
- Populated at discovery with the discovery date.
- Blank if not captured.

## Field 19 — Field Verified *(new)*
- Boolean: true or false.
- Always false at discovery.
- true indicates post-discovery physical field verification.

## Field 20 — Access Point ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid integer matching the entity's access_point_id.
- Enables joins to the access_point_parents relationship table.

------------------------------------------------------------
# 4. PARENT ENTITY SERIALIZATION RULES

Access Points have exactly one identity parent entity. The TSV output represents
this identity parent using two fields:

- **Field 4 — Identity Parent Entity Type**: "Site" or "Trailthing"
- **Field 5 — Identity Parent Entity ID**: the entity's full ID string
- **Field 6 — Identity Parent Entity Name**: the entity's Name field

Additional parent relationships (non-identity parents in `access_point_parents`)
are **not represented in TSV output**. Full parent relationship data is available
via the `access_point_parents` relationship table.

------------------------------------------------------------
# 5. SINGLE-COUNTY RULE

Access Points are point locations and must always reside in exactly one county.

- The County field must contain a single county name.
- No semicolon-delimited lists.
- County must be where the access point physically resides.
- Must not be inferred from parent entity county data.

------------------------------------------------------------
# 6. DELIMITER RULES

- TSV uses tab characters only.
- Each row must contain exactly **19 tab characters** (20 fields → 19 delimiters).
- No field may contain a tab.
- No field may contain newline characters.

------------------------------------------------------------
# 7. BLANK-FIELD RULES

- Blank fields must be represented as true blanks: `\t\t`
- No spaces inside blank fields.
- No placeholder values (NULL, _, "", BLANK).

------------------------------------------------------------
# 8. WHITESPACE RULES

- No leading or trailing spaces in any field.
- No trailing spaces at end of line.
- Internal spaces allowed only when part of the field value.

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

- Each row must contain exactly 20 fields.
- Each row must contain exactly 19 tabs.
- No field may be omitted.
- No field may be duplicated.
- Access Points are always single-row entities.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

1.  Receive normalized 20-field Access Point record.
2.  Validate GPS Lat / GPS Lon (numeric, WGS84; both populated or both blank).
3.  Validate Plus Code (blank if GPS blank).
4.  Validate County field (single value, no "County" suffix).
5.  Validate Identity Parent Entity Type (Site or Trailthing only).
6.  Validate Identity Parent Entity ID (valid OH-{COUNTY}-{TYPE}-{SEQ} format).
6a. Validate identity_parent_entity_id / identity_parent_entity_name pairing
    (both must be present or both blank).
7.  Validate Access Point Type (valid vocabulary value).
8.  Validate Status (valid vocabulary value or blank).
9.  Validate Features (semicolon-delimited, no empty segments).
10. Validate Identity Notes (free text or blank).
11. Validate last_verified_date (YYYY-MM-DD or blank).
12. Validate field_verified (boolean: true or false).
13. Validate no internal tabs.
14. Validate no internal newlines.
15. Validate whitespace rules.
16. Join fields with tab characters.
17. Validate delimiter count (must be 18).
18. Validate blank-field representation.
19. Emit row.

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 19 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Access Point Name is blank
- Identity Parent Entity Type is blank or not "Site" or "Trailthing"
- Identity Parent Entity ID is blank or not a valid entity ID format
- Identity Parent Entity Name is blank when Identity Parent Entity ID is populated
  (or vice versa)
- County is blank, contains "County", or contains a semicolon-delimited list
- GPS Lat is populated without GPS Lon or vice versa
- Plus Code is populated when GPS fields are blank
- GPS Lat or GPS Lon contains non-numeric content or directional suffixes
- Access Point Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- last_verified_date contains non-DATE content
- field_verified contains a non-boolean value
- Access Point ID is missing or non-integer
- Field order is incorrect
- A field is missing or duplicated

All errors must be logged in the Audit & Logging Module v6.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters (expect 19 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate GPS Lat / GPS Lon pairing and numeric format
- Validate Plus Code derivation consistency
- Validate County field (single value, no "County" suffix, no semicolons)
- Validate Identity Parent Entity Type (Site or Trailthing only)
- Validate Identity Parent Entity ID references known entities in the database
- Validate Identity Parent Entity ID / Name pairing (both present)
- Validate Access Point Type and Status vocabulary values
- Validate last_verified_date format
- Validate field_verified boolean
- Flag any Access Point with blank GPS that has been promoted to the statewide
  dataset (GPS required for statewide inclusion)
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. DESIGN NOTES

## 13.1 Identity Parent Entity — Both ID and Name
v5.1 used **Identity Parent Entity Name** only (Field 5).
v6.0 includes both **Identity Parent Entity ID** (Field 5) and **Identity Parent
Entity Name** (Field 6), satisfying two requirements simultaneously: the ID enables
reliable joins and unambiguous programmatic references; the Name provides
human-readable output that anyone can understand without a lookup.

The Access Point ID (Field 20) enables joins back to `access_point_parents` for
full relationship data.

## 13.2 Additional Parent Relationships
The `access_point_parents` table may contain multiple parent relationships beyond
the identity parent. These are intentionally excluded from TSV output. Multi-parent
reporting is handled at the reporting layer.

## 13.3 GPS Blank During Discovery
Access Points commonly have blank GPS fields during initial web discovery. This
is expected and correct. Blank GPS fields trigger routing to the GPS Acquisition
Module (Stage 3). The TSV Integrity Check flags any Access Point with blank GPS
that has been promoted to the statewide dataset.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Access Point Schema Module v6.0
- Access Point Vocabulary Module v6.0
- Access Point Normalization Contract v6.0
- TSV Integrity Check Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v6.0
