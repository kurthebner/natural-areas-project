# NATURAL AREAS PROJECT
# SITE TSV OUTPUT SPECIFICATION v5.0
(Authoritative Formatting-Layer Specification for Normalized Site Entities)

This module defines the authoritative, deterministic rules for serializing
**normalized Site entities** into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Vocabulary Module v5.0**.
All field definitions are defined in the **Site Schema Module v5.0**.
All normalization rules are defined in the **Site Normalization Contract v5.0**.

---

## v5.0 Changes from v4.0

- `county_list` → `counties` (field renamed)
- `gps_primary` (single string) → `gps_lat` + `gps_lon` (two separate numeric fields)
- `managing_agency` / `primary_managing_agency` → `governance`
- `secondary_managing_agencies` → `partner_agencies`
- `network_affiliation` removed — membership tracked via relationship tables
- `address` removed — merged into `location`
- `municipality` and `township` added as GIS-derived fields
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- Field count: 22 → 26

---

## 1. PURPOSE

This specification defines:

- The **canonical TSV field order** for Sites
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- Multi-county representation rules
- Parent Site placement rules
- GPS field representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Site TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **normalized Site records**
- All counties and all processing runs
- All automated or manual TSV exports
- All v5.0 normalization workflows
- All multi-entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank-field representation
- Derived Label computation and placement
- Multi-county representation
- Parent Site placement
- GPS field representation

---

## 3. FIELD ORDER

Site TSV output must contain exactly **26 fields** in the following order:

1. Name
2. Category
3. Subtype
4. Designation
5. Status
6. Ownership
7. Governance
8. Partner Agencies
9. Coordination
10. Description
11. Location
12. Acres
13. Counties
14. Municipality
15. Township
16. GPS Lat
17. GPS Lon
18. Plus Code
19. Features
20. Notes
21. URL
22. URLs
23. Map URL
24. Derived Label
25. Parent Site
26. Site ID

This order is absolute and must never change.

No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

### Field 13 — Counties
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Multi-county Sites remain single rows — no row expansion

### Fields 14–15 — Municipality / Township
- Populated by GIS spatial lookup during normalization
- Must never be collected from web discovery or raw source data
- May be blank if GIS lookup returns no result

### Fields 16–17 — GPS Lat / GPS Lon
- Numeric values in WGS84 decimal degrees
- GPS Lat: positive = north, negative = south
- GPS Lon: positive = east, negative = west (Ohio values are negative)
- Written as bare decimal numbers — no degree symbols, no directional suffixes
- Both fields must be populated together; neither may appear without the other
- If GPS is unavailable for the Site, both fields are blank

### Field 18 — Plus Code
- Derived from GPS Lat + GPS Lon by the Normalization Engine
- Must not be manually constructed
- Blank if GPS fields are blank

### Field 22 — URLs
- Semicolon-delimited list of additional URLs beyond the primary URL
- Represents the `urls` array from the normalized entity
- Blank if no additional URLs exist

### Field 23 — Map URL
- Single URL to the official or primary map for the Site
- Sites use a simple `map_url` (not a rich maps array)
- Blank if no map URL documented

### Field 24 — Derived Label
- Computed at TSV output time from normalized fields
- Must not be pre-stored in the normalized entity
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors
- Must not contradict Category, Ownership, Governance, or Designation

### Field 25 — Parent Site
- Must match the exact **Name** field of the parent Site
- No abbreviations, synonyms, or inferred names
- Blank for top-level Sites — no placeholders (no "None", "N/A", etc.)
- Parent Sites do not list children; relationship is upward only

### Field 26 — Site ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `site_id`

---

## 5. MULTI-COUNTY REPRESENTATION RULES

Sites are **not segmented** by county in the normalized dataset.

- Multi-county Sites must appear as **a single TSV row**.
- The **Counties** field must contain a semicolon-delimited, alphabetized list of all counties.
- The Counties field must not include the word "County."

Example:
- Normalized counties: `Franklin;Union`
- TSV output: `Franklin;Union` in the Counties field (single row)

Multi-county logic is handled at the Site level, not by row expansion.

---

## 6. DELIMITER RULES

### 6.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).
- No spaces may appear before or after tabs.
- No spaces may appear between tabs.

### 6.2 Each row must contain exactly **25 tab characters**
- 26 fields → 25 delimiters
- No more, no fewer

### 6.3 No field may contain a tab character
If a tab is detected inside a field, TSV generation must halt and surface an error.

### 6.4 No field may contain newline characters
If present, TSV generation must halt and surface an error.

---

## 7. BLANK-FIELD RULES

### 7.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

### 7.2 No spaces inside blank fields
Invalid examples:

- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

### 7.3 No placeholder values
Invalid:

- `_`
- `NULL`
- `""`
- `BLANK`

### 7.4 No collapsing of adjacent blanks
Adjacent blanks must remain:

`\t\t`

Never:

- `\t`
- `\t \t`

---

## 8. WHITESPACE RULES

### 8.1 No leading or trailing spaces in any field
Invalid:

- `" Park Name"`
- `"Park Name "`
- `" Park Name "`

### 8.2 No trailing spaces at end of line
Lines must end immediately after the **Site ID** field.

### 8.3 Internal spaces allowed only when part of the field value
Valid: `"Big Walnut Creek Park"`
Invalid: `"  Big Walnut Creek Park"`

---

## 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **26 fields**
No more, no fewer.

### 9.2 Each row must contain exactly **25 tabs**
This is the primary delimiter-integrity invariant.

### 9.3 No field may be omitted
If a field is unknown or inapplicable, it must be represented as a blank field (`\t\t`).

### 9.4 No field may be duplicated
Each field appears exactly once.

### 9.5 Multi-county Sites remain single rows
- Counties field contains semicolon-delimited, alphabetized list
- No row expansion occurs for Sites

---

## 10. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 26-field Site record (excluding Derived Label)**
**Step 2 — Compute Derived Label from normalized fields**
**Step 3 — Validate GPS Lat / GPS Lon (numeric, WGS84; both populated or both blank)**
**Step 4 — Validate Plus Code (blank if GPS blank)**
**Step 5 — Validate Counties field formatting (semicolon-delimited, alphabetized)**
**Step 6 — Validate Parent Site field (matches valid Site Name or blank)**
**Step 7 — Validate no internal tabs**
**Step 8 — Validate no internal newlines**
**Step 9 — Validate whitespace rules**
**Step 10 — Join fields with tab characters**
**Step 11 — Validate delimiter count (must be 25)**
**Step 12 — Validate blank-field representation**
**Step 13 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

## 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 25 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Derived Label is malformed, missing, or pre-stored (not computed at output time)
- GPS Lat is populated without GPS Lon or vice versa
- Plus Code is populated when GPS fields are blank
- GPS Lat or GPS Lon contains non-numeric content or directional suffixes
- Field order is incorrect
- A field is missing
- A field is duplicated
- Counties field is not semicolon-delimited and alphabetized
- Category, Subtype, Designation, Status, or Features contain invalid vocabulary values
- Ownership, Governance, or Coordination violate schema rules
- Parent Site is populated but does not match a valid Site Name
- Site ID is missing or non-integer

All errors must be logged in the Audit & Logging Module v5.0.

---

## 12. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank-field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement and freshness (not pre-stored)
- Validate Counties field formatting
- Validate Parent Site references
- Validate GPS Lat / GPS Lon pairing and numeric format
- Validate Plus Code derivation consistency
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free Site TSV output.

---

## 13. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v5.0
- Site Vocabulary Module v5.0
- Site Normalization Contract v5.0
- Child Site Rules Module v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF SITE TSV OUTPUT SPECIFICATION v5.0
