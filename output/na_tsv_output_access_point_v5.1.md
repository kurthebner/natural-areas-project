# NATURAL AREAS PROJECT
# ACCESS POINT TSV OUTPUT SPECIFICATION v5.1
Authoritative, deterministic formatting-layer specification defining exactly
how **Normalized Access Point Entities v5.1** are serialized into
tab-separated values (TSV) with guaranteed delimiter integrity, zero drift,
and full compatibility with the v5.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v5.x**.
All field definitions are defined in the **Access Point Schema Module v5.x**.
All normalization rules are defined in the
**Access Point Normalization Contract v5.x**.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored at any stage;
  consistent with Site entity architectural decision
- **Map URL removed**: Map URLs now included in URL field
  (semicolon-delimited with other authoritative URLs)
- **identity_notes added**: New field between Features and Notes; surfaced
  from identity_notes_raw at discovery stage
- **Field count updated**: 17 fields (was 18), 16 tab delimiters (was 17)
- **TSV generation algorithm updated**: Steps revised for removed and
  added fields
- **Error conditions updated**: Derived Label and Map URL conditions
  removed; identity_notes conditions added
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `access_level` removed
- `role` removed
- `gps_primary` → `gps_lat` + `gps_lon` (two separate numeric fields)
- `features` added
- `map_url` retained as simple optional field (removed in v5.1)
- `source_primary` removed
- `access_point_id` added as final field for referential integrity

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Access Points
- Delimiter rules
- Blank-field rules
- Whitespace rules
- GPS field representation rules
- Parent entity serialization rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for **Access Point TSV formatting**.

------------------------------------------------------------
# 2. FIELD ORDER (AUTHORITATIVE, v5.1)

Access Point TSV output must contain exactly **17 fields** in the
following order:

1.  Access Point Name
2.  Access Point Type
3.  Status
4.  Identity Parent Entity Type
5.  Identity Parent Entity Name
6.  County
7.  Township
8.  Municipality
9.  Address
10. GPS Lat
11. GPS Lon
12. Plus Code
13. Features
14. Identity Notes
15. Notes
16. URL
17. Access Point ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**17 fields = 16 tab delimiters per row.**

------------------------------------------------------------
# 3. FIELD NOTES

### Field 1 — Access Point Name
- Required; must never be blank
- Must be a human-readable, unique name within the set of parent entities
- If unnamed but identifiable, normalization contract constructs a name
- Must not be invented beyond normalization contract rules

### Field 2 — Access Point Type
- Required
- Must match a valid value from the Access Point Vocabulary Module v5.x
- Must not be inferred from amenities, geometry, or proximity alone
- One value only; no semicolon-delimited lists

### Field 3 — Status
- Optional
- Must match a valid value from the Access Point Vocabulary Module v5.x:
  Active, Closed, Seasonal, Restricted
- Describes the access point itself, not the parent entity
- Blank if ambiguous or unverifiable

### Field 4 — Identity Parent Entity Type
- Required; must never be blank
- Must be exactly one of: `Site`, `Trail`, `Trail Segment`
- Represents the single identity-defining parent relationship
- Additional parent relationships stored in access_point_parents table
  and not represented in TSV output

### Field 5 — Identity Parent Entity Name
- Required; must never be blank
- Must match the exact Name field of the identity parent entity
- No abbreviations, synonyms, or inferred names
- Enables human-readable traceability without requiring ID lookups

### Field 6 — County
- Required; must never be blank
- Single county name — Access Points are point locations
- Must not include the word "County"
- Must not be inferred from parent entity counties

### Fields 7–8 — Township / Municipality
- Both optional
- Populated via GIS spatial lookup during normalization
- Must never be collected during web discovery
- Blank if GIS lookup returns no result

### Field 9 — Address
- Optional
- Must be an authoritative or defensible address or road description
- Allowed fallback patterns: "Forest Road ###", "Township Road ###",
  "County Road ###", "Park Entrance Drive" (when supported by
  authoritative mapping)
- Must never be USPS-normalized
- Must never contain an invented street number

### Fields 10–11 — GPS Lat / GPS Lon
- Numeric values in WGS84 decimal degrees
- GPS Lat: positive = north, negative = south
- GPS Lon: positive = east, negative = west (Ohio values are negative)
- Written as bare decimal numbers — no degree symbols, no directional
  suffixes
- Both fields must be populated together; neither may appear without
  the other
- May be blank pending GPS Acquisition Module resolution
- Required before inclusion in statewide database

### Field 12 — Plus Code
- Derived from GPS Lat + GPS Lon by the Normalization Engine
- Must not be manually constructed
- Blank if GPS fields are blank

### Field 13 — Features
- Optional
- Semicolon-delimited flat list of documented facilities and amenities
  at the access point
- Metadata may appear in parentheses: `Parking (50 spaces, 4 ADA)`
- Must not include features of the parent entity
- Must not be inferred

### Field 14 — Identity Notes
- Optional
- Free-text field for identity clarifications, access point type
  uncertainty flags, parent entity assignment notes, and vocabulary
  type flags
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)

### Field 15 — Notes
- Optional
- Short, factual, non-invented operational details specific to this
  access point
- Captures entrance-specific information: gate conditions, seasonal
  constraints, parking limits, surface or grade issues, fees, signage,
  visibility
- Must not duplicate parent entity information
- Must not include ecological or narrative descriptions

### Field 16 — URL
- Optional
- Full https:// URLs only
- Semicolon-delimit if multiple authoritative URLs exist, including
  any map URLs (authoritative maps, GIS viewers, PDF maps)
- Must reference authoritative sources

### Field 17 — Access Point ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's access_point_id
- Enables joins to the access_point_parents relationship table

------------------------------------------------------------
# 4. PARENT ENTITY SERIALIZATION RULES

Access Points have exactly one identity parent entity. The TSV output
represents this identity parent using two fields:

- **Field 4 — Identity Parent Entity Type**: the entity class
  (Site, Trail, or Trail Segment)
- **Field 5 — Identity Parent Entity Name**: the exact Name of the
  parent entity

Additional parent relationships (non-identity parents stored in
`access_point_parents`) are **not represented in TSV output**. Full
parent relationship data is available via the `access_point_parents`
relationship table.

------------------------------------------------------------
# 5. SINGLE-COUNTY RULE

Access Points are point locations and must always reside in exactly one
county.

- The **County** field must contain a single county name
- No semicolon-delimited lists
- No multi-county representations
- County must be where the access point physically resides
- Must not be inferred from parent entity county data

------------------------------------------------------------
# 6. DELIMITER RULES

### 6.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs

### 6.2 Each row must contain exactly **16 tab characters**
- 17 fields → 16 delimiters
- No more, no fewer

### 6.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 6.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

------------------------------------------------------------
# 7. BLANK-FIELD RULES

### 7.1 Blank fields must be represented as true blanks
A blank field is `\t\t` with nothing between the tabs.

### 7.2 No spaces inside blank fields
Invalid: `\t \t`, `\t  \t`

### 7.3 No placeholder values
Invalid: `_`, `NULL`, `""`, `BLANK`

### 7.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`.

------------------------------------------------------------
# 8. WHITESPACE RULES

### 8.1 No leading or trailing spaces in any field

### 8.2 No trailing spaces at end of line
Lines must end immediately after the Access Point ID field.

### 8.3 Internal spaces allowed only when part of the field value

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **17 fields**

### 9.2 Each row must contain exactly **16 tabs**
This is the primary delimiter-integrity invariant.

### 9.3 No field may be omitted
If unknown or inapplicable, represent as a blank field.

### 9.4 No field may be duplicated

### 9.5 Access Points are always single-row entities
No row expansion occurs. Each access point is one TSV row.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1**  — Receive normalized 17-field Access Point record
**Step 2**  — Validate GPS Lat / GPS Lon (numeric, WGS84; both
              populated or both blank)
**Step 3**  — Validate Plus Code (blank if GPS blank)
**Step 4**  — Validate County field (single value, no "County" suffix)
**Step 5**  — Validate Identity Parent Entity Type
              (Site, Trail, or Trail Segment only)
**Step 6**  — Validate Identity Parent Entity Name
              (matches a valid normalized entity Name)
**Step 7**  — Validate Access Point Type (valid vocabulary value)
**Step 8**  — Validate Status (valid vocabulary value or blank)
**Step 9**  — Validate Features (semicolon-delimited, no empty segments)
**Step 10** — Validate Identity Notes (free text or blank)
**Step 11** — Validate no internal tabs
**Step 12** — Validate no internal newlines
**Step 13** — Validate whitespace rules
**Step 14** — Join fields with tab characters
**Step 15** — Validate delimiter count (must be 16)
**Step 16** — Validate blank-field representation
**Step 17** — Emit row

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 16 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Access Point Name is blank
- Identity Parent Entity Type is blank or not one of:
  Site, Trail, Trail Segment
- Identity Parent Entity Name is blank or does not match a valid
  normalized entity Name
- County is blank, contains the word "County", or contains a
  semicolon-delimited list
- GPS Lat is populated without GPS Lon or vice versa
- Plus Code is populated when GPS fields are blank
- GPS Lat or GPS Lon contains non-numeric content or directional suffixes
- Access Point Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Access Point ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK v5.x

The TSV Integrity Check must:

- Recount delimiters (expect 16 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate GPS Lat / GPS Lon pairing and numeric format
- Validate Plus Code derivation consistency
- Validate County field (single value, no "County" suffix, no semicolons)
- Validate Identity Parent Entity Type and Name references
- Validate Access Point Type and Status vocabulary values
- Flag any Access Point with blank GPS that has been promoted to the
  statewide dataset (GPS required for statewide inclusion)
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. DESIGN NOTES

### 13.1 Identity Parent Entity Name vs. ID
This spec uses **Identity Parent Entity Name** (Field 5) rather than
the raw `identity_parent_entity_id`. This provides human-readable
traceability in TSV output without requiring ID lookups. The Access Point
ID (Field 17) enables joins back to `access_point_parents` for full
relationship data.

### 13.2 Additional Parent Relationships
The `access_point_parents` table may contain multiple parent relationships
beyond the identity parent. These are intentionally excluded from TSV
output to keep the row model clean. Multi-parent reporting is handled at
the reporting layer, not the TSV layer.

### 13.3 GPS Blank During Discovery
Access Points commonly have blank GPS fields during initial web discovery —
this is expected and correct. Blank GPS fields trigger routing to the GPS
Acquisition Module (Stage 3 of pipeline). The TSV Integrity Check flags
any Access Point with blank GPS that has been promoted to the statewide
dataset, as GPS is required for statewide inclusion per the schema.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Access Point Schema Module v5.x
- Access Point Vocabulary Module v5.x
- Access Point Normalization Contract v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing Orchestration Module v5.x

------------------------------------------------------------
# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v5.1
