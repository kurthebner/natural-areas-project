# NATURAL AREAS PROJECT
# TRAIL TSV OUTPUT SPECIFICATION v5.1
Authoritative, deterministic formatting-layer specification defining exactly
how **Normalized Trail Entities v5.1** are serialized into tab-separated
values (TSV) with guaranteed delimiter integrity, zero drift, and full
compatibility with the v5.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.x**.
All field definitions are defined in the **Trail Schema Module v5.x**.
All normalization rules are defined in the
**Trail Normalization Contract v5.x**.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored at any stage;
  consistent with Site entity architectural decision
- **Parent Trail Network removed**: Network membership tracked exclusively
  via trail_network_members relationship table; not a TSV output field
- **identity_notes added**: New field between Trail History and Notes;
  surfaced from identity_notes_raw at discovery stage
- **maps simplified**: TSV output was already URLs-only; now authoritative
  — no rich object format exists at any stage
- **Field count updated**: 18 fields (was 20), 17 tab delimiters (was 19)
- **Schema discrepancy resolved**: v5.0 header said "19 fields" but body
  listed 18 named fields plus undocumented Trail ID; v5.1 states
  authoritative count of 18 named fields + Trail ID = 19 total output
  fields (see Section 2)
- **TSV generation algorithm updated**: Steps revised for removed and
  added fields
- **Error conditions updated**: Derived Label and Parent Trail Network
  conditions removed; identity_notes and maps URL validation added
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `counties_traversed` → `counties`
- `management` → `governance`
- `secondary_managing_agencies` → `partner_agencies`
- `network_affiliation` removed
- `map_url` → `maps` (URL list)
- `difficulty` and `accessibility` added
- `trail_history` added
- Trail ID added as final field

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Trails
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Maps field serialization rules
- Multi-county representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for **Trail TSV formatting**.

------------------------------------------------------------
# 2. FIELD ORDER (AUTHORITATIVE, v5.1)

Trail TSV output must contain exactly **19 fields** in the following
order:

1.  Trail Name
2.  Alternate Names
3.  Trail Use Type
4.  Trail Surface Type
5.  Trail Origin Type
6.  Total Length (Miles)
7.  Counties
8.  Governance
9.  Partner Agencies
10. Status
11. Difficulty
12. Accessibility
13. Description
14. Trail History
15. Identity Notes
16. Notes
17. URL
18. Maps
19. Trail ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**19 fields = 18 tab delimiters per row.**

------------------------------------------------------------
# 3. FIELD NOTES

### Field 1 — Trail Name
- Required; must never be blank
- Official published name
- Must be unique statewide (case-insensitive)

### Field 2 — Alternate Names
- Optional
- Semicolon-delimited list of documented historical or variant names
- Must not repeat Trail Name
- Blank if none documented

### Field 3 — Trail Use Type
- Required
- Must match a valid value from Trail Vocabulary Module v5.x
- One value only; no semicolon-delimited lists
- Must not be inferred

### Field 4 — Trail Surface Type
- Required
- Must match a valid value from Trail Vocabulary Module v5.x
- One value only
- "Mixed" only when explicitly documented

### Field 5 — Trail Origin Type
- Optional
- Must match a valid value from Trail Vocabulary Module v5.x
- One value only
- Must not be inferred

### Field 6 — Total Length (Miles)
- Optional
- Numeric value only — no units, no ranges, no approximation symbols
- Blank if unknown or undocumented

### Field 7 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Multi-county Trails remain single rows — no row expansion
- Only documented counties; none inferred from geometry

### Field 8 — Governance
- Required
- Primary agency or organization managing the trail
- Semicolon-delimited if multiple co-managers with equal authority
- Must not use generic categories

### Field 9 — Partner Agencies
- Optional
- Semicolon-delimited list of secondary managing agencies
- Must not duplicate Governance
- Blank if none documented

### Field 10 — Status
- Required
- Must match a valid value from Trail Vocabulary Module v5.x:
  Active, Planned, Under Construction, Gap, Closed
- Blank if status is ambiguous or undocumented

### Field 11 — Difficulty
- Optional
- Must match a valid value from Trail Vocabulary Module v5.x:
  Easy, Moderate, Difficult, Strenuous, Expert
- Blank if not explicitly documented by an authoritative source
- Must never be assessed or inferred

### Field 12 — Accessibility
- Optional
- Free-text description of ADA compliance, wheelchair accessibility,
  surface grade, width, and accessible facilities
- Blank if not documented

### Field 13 — Description
- Optional but strongly recommended
- 1-3 sentences describing identity-defining characteristics

### Field 14 — Trail History
- Optional
- 1-3 sentences of documented historical context
- Blank if none documented

### Field 15 — Identity Notes
- Optional
- Free-text field for identity clarifications, trail vs. segment
  boundary questions, alternate name conflicts, network membership
  uncertainty, and vocabulary type flags
- Must not duplicate Notes content
- Must not contain operational or contextual notes

### Field 16 — Notes
- Optional
- Free-text for temporary closures, access restrictions, parking
  details, gap locations, construction updates
- Must not include identity-defining characteristics

### Field 17 — URL
- Optional but strongly recommended
- Full https:// URL to primary authoritative source
- Single value; tracking parameters removed

### Field 18 — Maps
- Optional
- Semicolon-delimited list of URLs to trail map resources
- Includes PDF maps, GPX files, KML files, interactive map viewers,
  GIS layers, elevation profiles
- Each entry must be a well-formed https:// URL — no embedded metadata
- Blank if no maps documented

### Field 19 — Trail ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's trail_id
- Enables joins to the trail_network_members relationship table

------------------------------------------------------------
# 4. MULTI-COUNTY REPRESENTATION RULES

Trails are **not expanded** into multiple TSV rows.

- The **Counties** field must contain a **semicolon-delimited,
  alphabetized list** without the word "County"
- The Trail must appear as **a single TSV row** regardless of how many
  counties it traverses
- No inference permitted; only documented counties included

Example:
- Normalized counties: `Delaware;Franklin;Union`
- TSV output: `Delaware;Franklin;Union`

------------------------------------------------------------
# 5. MAPS FIELD SERIALIZATION RULES

The `maps` field is a semicolon-delimited list of https:// URLs:

- Each entry must be a well-formed https:// URL
- No embedded metadata (no type labels, no descriptions)
- No spaces around semicolons
- No empty segments
- Blank if no map resources exist

Example:
`https://wcparks.org/maps/slippery-elm-trail.pdf;https://wcparks.org/trails/interactive-map;https://wcparks.org/gpx/slippery-elm.gpx`

------------------------------------------------------------
# 6. DELIMITER RULES

### 6.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs

### 6.2 Each row must contain exactly **18 tab characters**
- 19 fields → 18 delimiters
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
Lines must end immediately after the Trail ID field.

### 8.3 Internal spaces allowed only when part of the field value

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **19 fields**

### 9.2 Each row must contain exactly **18 tabs**
This is the primary delimiter-integrity invariant.

### 9.3 No field may be omitted
If unknown or inapplicable, represent as a blank field.

### 9.4 No field may be duplicated

### 9.5 Multi-county Trails remain single rows
No row expansion regardless of county count.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1**  — Receive normalized 19-field Trail record
**Step 2**  — Validate Maps field (each entry a well-formed https://
              URL; no embedded metadata; no empty segments)
**Step 3**  — Validate Counties formatting (semicolon-delimited,
              alphabetized, no "County" suffix)
**Step 4**  — Validate Alternate Names (semicolon-delimited, no
              duplicates, does not repeat Trail Name)
**Step 5**  — Validate Trail Use Type (valid vocabulary value)
**Step 6**  — Validate Trail Surface Type (valid vocabulary value)
**Step 7**  — Validate Trail Origin Type (valid vocabulary value
              or blank)
**Step 8**  — Validate Status (valid vocabulary value or blank)
**Step 9**  — Validate Difficulty (valid vocabulary value or blank)
**Step 10** — Validate Total Length (numeric only or blank)
**Step 11** — Validate Identity Notes (free text or blank)
**Step 12** — Validate no internal tabs
**Step 13** — Validate no internal newlines
**Step 14** — Validate whitespace rules
**Step 15** — Join fields with tab characters
**Step 16** — Validate delimiter count (must be 18)
**Step 17** — Validate blank-field representation
**Step 18** — Emit row

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 18 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Trail Name is blank
- Counties field is not semicolon-delimited and alphabetized, or
  contains the word "County"
- Trail Use Type is blank or contains an invalid vocabulary value
- Trail Surface Type is blank or contains an invalid vocabulary value
- Trail Origin Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Difficulty contains an invalid vocabulary value
- Total Length contains non-numeric content
- Maps field contains embedded metadata or malformed URLs
- Trail ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK v5.x

The TSV Integrity Check must:

- Recount delimiters (expect 18 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting (semicolon-delimited, alphabetized)
- Validate Maps field (well-formed https:// URLs, no embedded metadata)
- Validate all vocabulary-controlled field values
- Validate Total Length is numeric
- Validate Trail ID is integer
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Trail Schema Module v5.x
- Trail Vocabulary Module v5.x
- Trail Normalization Contract v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing Orchestration Module v5.x

------------------------------------------------------------
# END OF TRAIL TSV OUTPUT SPECIFICATION v5.1
