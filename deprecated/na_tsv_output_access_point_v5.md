# NATURAL AREAS PROJECT — ACCESS POINT TSV OUTPUT SPECIFICATION v5.0
Authoritative, deterministic formatting-layer specification defining exactly how
**Normalized Access Point Entities v5.0** are serialized into tab-separated values (TSV)
with guaranteed delimiter integrity, zero drift, and full compatibility with the
v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Access Point Vocabulary Module v5.0**.
All field definitions are defined in the **Access Point Schema Module v5.0**.
All normalization rules are defined in the **Access Point Normalization Contract v5.0**.

---

## v5.0 Changes from v4.0

- `access_level` removed — redundant with Access Point Type and Status vocabularies
- `role` removed — not needed
- `gps_primary` (single string) → `gps_lat` + `gps_lon` (two separate numeric fields)
- `features` added (semicolon-delimited facilities and amenities at the access point)
- `map_url` retained as simple optional field (not rich array)
- `source_primary` removed — provenance tracked via provenance tables
- `municipality` and `township` retained — populated via GIS spatial lookup only, not during discovery
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- `access_point_id` added as final field for referential integrity
- Field count updated to 18

---

## 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Access Points
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- GPS field representation rules
- Parent entity serialization rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Access Point TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **normalized Access Point entities v5.0**
- All counties and all processing runs
- All automated or manual TSV exports
- All v5.0 normalization workflows
- All multi-entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank-field representation
- Derived Label computation and placement
- GPS field representation
- Parent entity field serialization

---

## 3. FIELD ORDER (AUTHORITATIVE, v5.0)

Access Point TSV output must contain exactly **18 fields** in the following order:

1. Access Point Name
2. Access Point Type
3. Status
4. Identity Parent Entity Type
5. Identity Parent Entity Name
6. County
7. Township
8. Municipality
9. Address
10. GPS Lat
11. GPS Lon
12. Plus Code
13. Features
14. Notes
15. URL
16. Map URL
17. Derived Label
18. Access Point ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

### Field 1 — Access Point Name
- Required; must never be blank
- Must be a human-readable, unique name within the set of parent entities
- If unnamed but identifiable, the normalization contract constructs a name — see Access Point Normalization Contract v5.0
- Must not be invented beyond normalization contract rules

### Field 2 — Access Point Type
- Required
- Must match a valid value from the Access Point Vocabulary Module v5.0
- Must not be inferred from amenities, geometry, or proximity alone
- One value only; no semicolon-delimited lists

### Field 3 — Status
- Optional
- Must match a valid value from the Access Point Vocabulary Module v5.0: Active, Closed, Seasonal, Restricted
- Describes the access point itself, not the parent entity
- Blank if ambiguous or unverifiable

### Field 4 — Identity Parent Entity Type
- Required; must never be blank
- Must be exactly one of: `Site`, `Trail`, `Trail Segment`
- Represents the single identity-defining parent relationship
- Additional parent relationships are stored in the `access_point_parents` relationship table and are not represented in TSV output

### Field 5 — Identity Parent Entity Name
- Required; must never be blank
- Must match the exact Name field of the identity parent entity (Site Name, Trail Name, or Segment Name)
- No abbreviations, synonyms, or inferred names
- Enables human-readable traceability without requiring ID lookups

### Field 6 — County
- Required; must never be blank
- Single county name — Access Points are point locations; no semicolon-delimited lists
- Must not include the word "County"
- Must not be inferred from parent entity counties

### Fields 7–8 — Township / Municipality
- Both optional
- Populated via GIS spatial lookup during normalization
- Must never be collected during web discovery or populated from raw source data
- Blank if GIS lookup returns no result or if outside any township or municipality boundary

### Field 9 — Address
- Optional
- Must be an authoritative or defensible address or road description
- Allowed fallback patterns: "Forest Road ###", "Township Road ###", "County Road ###", "Park Entrance Drive" (when supported by authoritative mapping)
- Must never be USPS-normalized
- Must never contain an invented street number
- Blank if no authoritative or defensible designation exists

### Fields 10–11 — GPS Lat / GPS Lon
- Numeric values in WGS84 decimal degrees
- GPS Lat: positive = north, negative = south
- GPS Lon: positive = east, negative = west (Ohio values are negative)
- Written as bare decimal numbers — no degree symbols, no directional suffixes
- Both fields must be populated together; neither may appear without the other
- May be blank during initial web discovery — required before inclusion in statewide database
- Must never be inferred; must represent the physical location of the access point

### Field 12 — Plus Code
- Derived from GPS Lat + GPS Lon by the Normalization Engine
- Must not be manually constructed
- Blank if GPS fields are blank

### Field 13 — Features
- Optional
- Semicolon-delimited flat list of documented facilities and amenities at the access point
- Must match Features vocabulary values from the Access Point Vocabulary Module v5.0
- Metadata may appear in parentheses: `parking (50 spaces, 4 ADA)`
- Must not include features of the parent entity
- Must not be inferred

### Field 14 — Notes
- Optional
- Short, factual, non-invented operational details specific to this access point
- Captures entrance-specific information: gate conditions, seasonal constraints, parking limits, surface or grade issues, fees, signage, visibility
- Must not duplicate parent entity information
- Must not include ecological or narrative descriptions

### Field 15 — URL
- Optional
- Full https:// URLs only
- Semicolon-delimit if multiple
- Must reference authoritative sources

### Field 16 — Map URL
- Optional
- Full https:// URL to an authoritative map or GIS viewer specific to this access point
- May include PDF maps, static images, or interactive GIS layers
- Semicolon-delimit if multiple
- Blank if none

### Field 17 — Derived Label
- Computed at TSV output time from normalized fields; must never be pre-stored
- Formula: **Access Point Type + " — " + Identity Parent Entity Name**
- Example: `Trailhead — Slippery Elm Trail`
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors

### Field 18 — Access Point ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `access_point_id`
- Enables joins to the `access_point_parents` relationship table

---

## 5. PARENT ENTITY SERIALIZATION RULES

Access Points have exactly one identity parent entity. The TSV output represents
this identity parent relationship using two fields:

- **Field 4 — Identity Parent Entity Type**: the entity class (Site, Trail, or Trail Segment)
- **Field 5 — Identity Parent Entity Name**: the exact Name of the parent entity

Additional parent relationships (non-identity parents stored in `access_point_parents`)
are **not represented in TSV output**. The TSV row captures the primary navigational
identity of the access point. Full parent relationship data is available via the
`access_point_parents` relationship table.

---

## 6. SINGLE-COUNTY RULE

Access Points are point locations and must always reside in exactly one county.

- The **County** field must contain a single county name
- No semicolon-delimited lists
- No multi-county representations
- County must be the county in which the access point physically resides
- Must not be inferred from parent entity county data

---

## 7. DELIMITER RULES

### 7.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs
- No spaces may appear between tabs

### 7.2 Each row must contain exactly **17 tab characters**
- 18 fields → 17 delimiters
- No more, no fewer

### 7.3 No field may contain a tab character
If a tab is detected inside a field, TSV generation must halt and surface an error.

### 7.4 No field may contain newline characters
If present, TSV generation must halt and surface an error.

---

## 8. BLANK-FIELD RULES

### 8.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

### 8.2 No spaces inside blank fields
Invalid examples:
- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

### 8.3 No placeholder values
Invalid:
- `_`
- `NULL`
- `""`
- `BLANK`

### 8.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`. Never `\t` or `\t \t`.

---

## 9. WHITESPACE RULES

### 9.1 No leading or trailing spaces in any field
Invalid: `" Trailhead"`, `"Trailhead "`, `" Trailhead "`

### 9.2 No trailing spaces at end of line
Lines must end immediately after the **Access Point ID** field.

### 9.3 Internal spaces allowed only when part of the field value
Valid: `"North Parking Lot"`
Invalid: `"  North Parking Lot"`

---

## 10. ROW CONSTRUCTION RULES

### 10.1 Each row must contain exactly **18 fields**
No more, no fewer.

### 10.2 Each row must contain exactly **17 tabs**
This is the primary delimiter-integrity invariant.

### 10.3 No field may be omitted
If a field is unknown or inapplicable, it must be represented as a blank field (`\t\t`).

### 10.4 No field may be duplicated
Each field appears exactly once.

### 10.5 Access Points are always single-row entities
No row expansion occurs for Access Points. Each access point is one TSV row.

---

## 11. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 18-field Access Point record (excluding Derived Label)**
**Step 2 — Compute Derived Label: Access Point Type + " — " + Identity Parent Entity Name**
**Step 3 — Validate GPS Lat / GPS Lon (numeric, WGS84; both populated or both blank)**
**Step 4 — Validate Plus Code (blank if GPS blank)**
**Step 5 — Validate County field (single value, no "County" suffix)**
**Step 6 — Validate Identity Parent Entity Type (Site, Trail, or Trail Segment only)**
**Step 7 — Validate Identity Parent Entity Name (matches a valid normalized entity Name)**
**Step 8 — Validate Access Point Type (valid vocabulary value)**
**Step 9 — Validate Status (valid vocabulary value or blank)**
**Step 10 — Validate Features (valid vocabulary values or blank)**
**Step 11 — Validate no internal tabs**
**Step 12 — Validate no internal newlines**
**Step 13 — Validate whitespace rules**
**Step 14 — Join fields with tab characters**
**Step 15 — Validate delimiter count (must be 17)**
**Step 16 — Validate blank-field representation**
**Step 17 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

## 12. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 17 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Access Point Name is blank
- Identity Parent Entity Type is blank or not one of: Site, Trail, Trail Segment
- Identity Parent Entity Name is blank or does not match a valid normalized entity Name
- County is blank, contains the word "County", or contains a semicolon-delimited list
- Derived Label is malformed, missing, or pre-stored (not computed at output time)
- GPS Lat is populated without GPS Lon or vice versa
- Plus Code is populated when GPS fields are blank
- GPS Lat or GPS Lon contains non-numeric content or directional suffixes
- Access Point Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Features contains invalid vocabulary values
- Access Point ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.0.

---

## 13. INTEGRATION WITH TSV INTEGRITY CHECK v5.0

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank-field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement and freshness (not pre-stored)
- Validate GPS Lat / GPS Lon pairing and numeric format
- Validate Plus Code derivation consistency
- Validate County field (single value, no "County" suffix, no semicolons)
- Validate Identity Parent Entity Type and Name references
- Validate Access Point Type and Status vocabulary values
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free
Access Point TSV output.

---

## 14. DESIGN NOTES AND SUGGESTIONS

### 14.1 Identity Parent Entity Name vs. ID
This spec uses **Identity Parent Entity Name** (Field 5) rather than the raw
`identity_parent_entity_id` from the schema. This provides human-readable
traceability in the TSV output without requiring ID lookups. The Access Point ID
(Field 18) enables joins back to `access_point_parents` for full relationship data.

This pattern follows the same approach used by Trail Segments (which carry
Parent Trail as a name reference) and is preferable for TSV files intended for
human review and web-sweep validation.

### 14.2 Additional Parent Relationships
The `access_point_parents` table may contain multiple parent relationships beyond
the identity parent. These are intentionally excluded from TSV output to keep the
row model clean. If multi-parent reporting is needed, it should be handled at the
reporting layer, not the TSV layer.

### 14.3 GPS Blank During Discovery
Access Points commonly have blank GPS fields during initial web discovery — this
is expected and correct. The TSV output spec allows blank GPS fields. However,
the TSV Integrity Check should flag any Access Point with blank GPS fields that
has been promoted to the statewide dataset, as GPS is required for statewide
inclusion per the schema.

### 14.4 Features Vocabulary
The Features vocabulary is defined in the Access Point Vocabulary Module v5.0.
Unlike free-text notes, Features values must match the controlled vocabulary.
Metadata in parentheses (e.g., `parking (50 spaces, 4 ADA)`) is permitted within
a Features entry to capture capacity or specifics without fragmenting the vocabulary.

---

## 15. MODULE DEPENDENCIES

This module depends on:

- Access Point Schema Module v5.0
- Access Point Vocabulary Module v5.0
- Access Point Normalization Contract v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v5.0
