# NATURAL AREAS PROJECT
# TRAIL SEGMENT TSV OUTPUT SPECIFICATION v5.1
Authoritative, deterministic formatting-layer specification defining exactly
how **Normalized Trail Segment Entities v5.1** are serialized into
tab-separated values (TSV) with guaranteed delimiter integrity, zero drift,
and full compatibility with the v5.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.x**.
All field definitions are defined in the **Trail Segment Schema Module v5.x**.
All normalization rules are defined in the
**Trail Segment Normalization Contract v5.x**.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored at any stage;
  consistent with Site entity architectural decision
- **Parent Trail Network removed**: Network membership inherited via
  parent Trail and tracked in trail_network_members relationship table;
  not a TSV output field
- **identity_notes added**: New field between Description and Notes;
  surfaced from identity_notes_raw at discovery stage
- **maps simplified**: TSV output was already URLs-only; now authoritative
  at all stages — no rich object format exists anywhere
- **Field count**: 17 fields (was 18 in v5.0 but with different composition:
  removed Derived Label and Parent Trail Network, added identity_notes,
  net zero change in count)
- **Tab delimiters**: 16 (was 17 in v5.0)
- **Schema discrepancy resolved**: v5.0 header said "17 FIELDS" but body
  listed 16 named fields with Segment ID undocumented; v5.1 header states
  authoritative count of 17 fields
- **TSV generation algorithm updated**: Steps revised for removed and
  added fields
- **Error conditions updated**: Derived Label and Parent Trail Network
  conditions removed; identity_notes and maps URL validation added
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `managing_agency` → `governance`
- `county_list` → `counties`
- `map_url` → `maps` (URL list)
- `segment_role` removed
- `difficulty` and `accessibility` added
- `segment_type` added
- `geometry` retained
- Segment ID added as final field

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Trail Segments
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Maps field serialization rules
- Multi-county representation rules
- Parent Trail placement rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for **Trail Segment TSV formatting**.

------------------------------------------------------------
# 2. FIELD ORDER (AUTHORITATIVE, v5.1)

Trail Segment TSV output must contain exactly **17 fields** in the
following order:

1.  Parent Trail
2.  Segment Name
3.  Counties
4.  Governance
5.  Segment Length (Miles)
6.  Surface Type
7.  Segment Type
8.  Status
9.  Difficulty
10. Accessibility
11. Description
12. Identity Notes
13. Notes
14. URL
15. Maps
16. Geometry
17. Segment ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**17 fields = 16 tab delimiters per row.**

------------------------------------------------------------
# 3. FIELD NOTES

### Field 1 — Parent Trail
- Required; must never be blank
- Must match the exact Trail Name of a valid normalized Trail
- No abbreviations, synonyms, or inferred names
- Trail Segments always have exactly one parent Trail

### Field 2 — Segment Name
- Optional
- Only used when the segment has a documented, identity-bearing name
- Must be unique within the parent Trail
- Blank for unnamed segments — no placeholder values

### Field 3 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Multi-county segments remain single rows — no row expansion
- Only documented counties; none inferred from geometry

### Field 4 — Governance
- Primary agency or organization responsible for this specific segment
- Must not be inferred from the parent Trail's governance
- Semicolon-delimited if multiple
- Blank if no segment-specific governance documentation exists

### Field 5 — Segment Length (Miles)
- Optional
- Numeric value only — no units, no ranges, no approximation symbols
- Blank if unknown

### Field 6 — Surface Type
- Required
- Must match a valid value from Trail Segment Vocabulary Module v5.x
- One value only
- Often the primary reason the segment exists as a distinct entity

### Field 7 — Segment Type
- Optional
- Must match a valid value from Trail Segment Vocabulary Module v5.x:
  Linear, Loop, Connector, Spur, Crossing, Access Segment, Other
- Most segments are Linear — only populate when explicitly documented
  or clearly distinct
- Blank if not documented

### Field 8 — Status
- Required
- Must match a valid value from Trail Segment Vocabulary Module v5.x:
  Active, Planned, Gap, Closed
- "Gap" = documented missing portion of trail
- Blank if status is ambiguous or undocumented

### Field 9 — Difficulty
- Optional
- Must match a valid value from Trail Segment Vocabulary Module v5.x:
  Easy, Moderate, Difficult, Strenuous, Expert
- Blank if not explicitly documented for this specific segment
- Must never be assessed or inferred
- May differ from the parent Trail's overall difficulty

### Field 10 — Accessibility
- Optional
- Free-text description of ADA compliance, wheelchair accessibility,
  surface grade, width, and accessible facilities for this segment
- Blank if not documented for this specific segment
- Must not be inherited from parent Trail without explicit documentation

### Field 11 — Description
- Optional
- 1-3 sentences describing identity-defining characteristics of this
  segment specifically

### Field 12 — Identity Notes
- Optional
- Free-text field for identity clarifications, segment vs. trail
  boundary questions, shared-corridor documentation, parent Trail
  assignment uncertainty, and vocabulary type flags
- Must not duplicate Notes content
- Must not contain operational or contextual notes

### Field 13 — Notes
- Optional
- Free-text for temporary conditions, surface details, access
  restrictions, construction updates, gap details
- Must not include identity-defining characteristics
- Must not include Access Point details

### Field 14 — URL
- Optional
- Full https:// URL to primary authoritative source for this segment
- Single value; tracking parameters removed

### Field 15 — Maps
- Optional
- Semicolon-delimited list of URLs to segment map resources
- Includes PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles
- Each entry must be a well-formed https:// URL — no embedded metadata
- Blank if no maps documented

### Field 16 — Geometry
- Optional
- WKT LineString or GeoJSON LineString stored as text
- Populated in GIS phase — expected to be blank for most segments
  during initial web discovery
- Must be authoritative; no inferred or smoothed geometry

### Field 17 — Segment ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's segment_id

------------------------------------------------------------
# 4. MULTI-COUNTY REPRESENTATION RULES

Trail Segments are **not expanded** into multiple TSV rows.

- The **Counties** field must contain a **semicolon-delimited,
  alphabetized list** without the word "County"
- The Trail Segment must appear as **a single TSV row** regardless of
  how many counties it spans
- No inference permitted; only documented counties included

Example:
- Normalized counties: `Lucas;Wood`
- TSV output: `Lucas;Wood`

------------------------------------------------------------
# 5. MAPS FIELD SERIALIZATION RULES

The `maps` field is a semicolon-delimited list of https:// URLs:

- Each entry must be a well-formed https:// URL
- No embedded metadata (no type labels, no descriptions)
- No spaces around semicolons
- No empty segments
- Blank if no map resources exist

Example:
`https://buckeyetrail.org/maps/wood-county-section.pdf;https://buckeyetrail.org/gpx/section-5.gpx`

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
Lines must end immediately after the Segment ID field.

### 8.3 Internal spaces allowed only when part of the field value

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **17 fields**

### 9.2 Each row must contain exactly **16 tabs**
This is the primary delimiter-integrity invariant.

### 9.3 No field may be omitted
If unknown or inapplicable, represent as a blank field.

### 9.4 No field may be duplicated

### 9.5 Multi-county Trail Segments remain single rows
No row expansion regardless of county count.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1**  — Receive normalized 17-field Trail Segment record
**Step 2**  — Validate Parent Trail (valid Trail Name; must not be
              blank)
**Step 3**  — Validate Maps field (each entry a well-formed https://
              URL; no embedded metadata; no empty segments)
**Step 4**  — Validate Counties formatting (semicolon-delimited,
              alphabetized, no "County" suffix)
**Step 5**  — Validate Surface Type (valid vocabulary value)
**Step 6**  — Validate Segment Type (valid vocabulary value or blank)
**Step 7**  — Validate Status (valid vocabulary value or blank)
**Step 8**  — Validate Difficulty (valid vocabulary value or blank)
**Step 9**  — Validate Segment Length (numeric only or blank)
**Step 10** — Validate Identity Notes (free text or blank)
**Step 11** — Validate Geometry (valid LineString or blank)
**Step 12** — Validate no internal tabs
**Step 13** — Validate no internal newlines
**Step 14** — Validate whitespace rules
**Step 15** — Join fields with tab characters
**Step 16** — Validate delimiter count (must be 16)
**Step 17** — Validate blank-field representation
**Step 18** — Emit row

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 16 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Parent Trail is blank or does not match a valid Trail Name
- Counties field is not semicolon-delimited and alphabetized, or
  contains the word "County"
- Surface Type is blank or contains an invalid vocabulary value
- Segment Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Difficulty contains an invalid vocabulary value
- Segment Length contains non-numeric content
- Maps field contains embedded metadata or malformed URLs
- Geometry is malformed (if populated)
- Segment ID is missing or non-integer
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
- Validate Parent Trail (non-blank, valid Trail Name)
- Validate Counties formatting (semicolon-delimited, alphabetized)
- Validate Maps field (well-formed https:// URLs, no embedded metadata)
- Validate all vocabulary-controlled field values
- Validate Segment Length is numeric
- Validate Geometry format (if populated)
- Validate Segment ID is integer
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Schema Module v5.x
- Trail Segment Vocabulary Module v5.x
- Trail Segment Normalization Contract v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing Orchestration Module v5.x

------------------------------------------------------------
# END OF TRAIL SEGMENT TSV OUTPUT SPECIFICATION v5.1
