# NATURAL AREAS PROJECT
# TRAIL NETWORK TSV OUTPUT SPECIFICATION v5.1
Authoritative, deterministic formatting-layer specification defining exactly
how **Normalized Trail Network Entities v5.1** are serialized into
tab-separated values (TSV) with guaranteed delimiter integrity, zero drift,
and full compatibility with the v5.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.x**.
All field definitions are defined in the **Trail Network Schema Module v5.x**.
All normalization rules are defined in the
**Trail Network Normalization Contract v5.x**.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Derived Label removed**: No longer computed or stored at any stage;
  consistent with Site entity architectural decision
- **identity_notes added**: New field between Description and Notes;
  surfaced from identity_notes_raw at discovery stage
- **maps simplified**: TSV output was already URLs-only in v5.0; now
  authoritative at all stages — no rich object format exists anywhere
- **Field count**: 17 fields (was 17 in v5.0 — removed Derived Label,
  added identity_notes; net zero change in count)
- **Tab delimiters**: 16 (same as v5.0)
- **TSV generation algorithm updated**: Steps revised for removed and
  added fields; Derived Label computation step removed
- **Error conditions updated**: Derived Label conditions removed;
  identity_notes and maps URL validation added
- **Design Notes updated**: Derived Label section removed
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed
- `history` removed (merged into description)
- `county_list` → `counties`
- `primary_managing_agency` → `governance`
- `secondary_managing_agencies` → `partner_agencies`
- `map_url` → `maps` (URL list)
- `status` added
- `ownership` added
- `total_length_miles` added
- `member_trail_count` added
- `member_trail_ids` added
- `states_included` added
- Network ID added as final field

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Trail Networks
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Maps field serialization rules
- Member Trail IDs serialization rules
- Multi-county and multi-state representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for **Trail Network TSV formatting**.

------------------------------------------------------------
# 2. FIELD ORDER (AUTHORITATIVE, v5.1)

Trail Network TSV output must contain exactly **17 fields** in the
following order:

1.  Network Name
2.  Network Type
3.  Status
4.  Ownership
5.  Governance
6.  Partner Agencies
7.  Counties
8.  States Included
9.  Total Length (Miles)
10. Member Trail Count
11. Member Trail IDs
12. Description
13. Identity Notes
14. Notes
15. URL
16. Maps
17. Network ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**17 fields = 16 tab delimiters per row.**

------------------------------------------------------------
# 3. FIELD NOTES

### Field 1 — Network Name
- Required; must never be blank
- Official published name
- Must be unique statewide (case-insensitive)
- Must not include unofficial descriptors or hierarchy encoding

### Field 2 — Network Type
- Required
- Must match a valid value from Trail Network Vocabulary Module v5.x
- One value only; no semicolon-delimited lists
- Must not be inferred from member count or geographic extent

### Field 3 — Status
- Optional
- Must match a valid value from Trail Network Vocabulary Module v5.x:
  Active, Planned, Under Development, Partially Open, Closed
- Blank if not documented; Active is implied for operational networks
- "Planned" and "Closed" must be explicitly documented

### Field 4 — Ownership
- Optional free-text — no controlled vocabulary
- Legal name of entity that owns or established the network
- Must not use generic categories
- Must not encode management or governance
- Blank when ownership is distributed, when the network is a
  coordinating body without land ownership, or when unclear
- Blank is correct and common

### Field 5 — Governance
- Required
- Primary agency or organization coordinating or managing the network
- Must be an authoritative name
- Semicolon-delimited if multiple co-managers

### Field 6 — Partner Agencies
- Optional
- Semicolon-delimited list of secondary managing agencies or
  documented organizational partners
- Must not duplicate Governance
- Blank if none documented

### Field 7 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Must include all counties through which any part of the network
  passes
- Trail Networks remain single rows regardless of county span

### Field 8 — States Included
- Optional
- Semicolon-delimited, alphabetized list of state abbreviations
- Only used for multi-state networks
- **Blank for Ohio-only networks** — do not write "Ohio"

### Field 9 — Total Length (Miles)
- Optional
- Numeric value only — no units, no ranges
- Use officially published network length
- Blank if unknown or undocumented

### Field 10 — Member Trail Count
- Optional but strongly recommended
- Integer representing number of member Trails
- Officially published count preferred; may be estimated from
  enumerated member list
- Blank if truly unknown
- Must not be computed by counting Member Trail IDs at TSV
  generation time — use the normalized value

### Field 11 — Member Trail IDs
- Optional
- Semicolon-delimited list of integer trail_id values
- Populated during normalization as member Trails are resolved
- Blank if no IDs have been resolved yet
- Must not contain non-integer values or placeholder text

### Field 12 — Description
- Optional but strongly recommended
- 1-3 sentences describing the network's identity, scope, and
  purpose
- May include brief establishment history or origin context
- Must not include Trail-level or Segment-level details

### Field 13 — Identity Notes
- Optional
- Free-text field for identity clarifications, network vs. trail
  boundary questions, name conflicts, and membership uncertainty
- Must not duplicate Notes content
- Must not contain operational or contextual notes

### Field 14 — Notes
- Optional
- Free-text for gap documentation, planning status, partial
  completion notes, funding status, contextual clarifications
- Must not include identity-defining characteristics

### Field 15 — URL
- Optional but strongly recommended
- Full https:// URLs only
- Semicolon-delimit if multiple authoritative URLs
- Tracking parameters removed

### Field 16 — Maps
- Optional
- Semicolon-delimited list of URLs to network map resources
- Trail Networks are linear spatial systems — multiple map formats
  (PDF strip maps, interactive viewers, GPX/KML files) are common
- Each entry must be a well-formed https:// URL — no embedded
  metadata
- Blank if no maps documented

### Field 17 — Network ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's network_id
- Enables joins to the `trail_network_members` relationship table

------------------------------------------------------------
# 4. MULTI-COUNTY AND MULTI-STATE REPRESENTATION RULES

Trail Networks are **not expanded** into multiple TSV rows.

- The **Counties** field must contain a **semicolon-delimited,
  alphabetized list** without the word "County"
- The Trail Network must appear as **a single TSV row** regardless
  of how many counties it spans
- **States Included** is blank for Ohio-only networks
- No inference permitted — only documented counties and states
  included

Example:
- Normalized counties: `Fulton;Henry;Lucas;Wood`
- TSV output: `Fulton;Henry;Lucas;Wood`
- Ohio-only → States Included: *(blank)*

------------------------------------------------------------
# 5. MAPS FIELD SERIALIZATION RULES

The `maps` field is a semicolon-delimited list of https:// URLs:

- Each entry must be a well-formed https:// URL
- No embedded metadata (no type labels, no descriptions)
- No spaces around semicolons
- No empty segments
- Blank if no map resources exist

Example:
`https://ncta.org/map.pdf;https://ncta.org/interactive;https://ncta.org/gpx/route.gpx`

------------------------------------------------------------
# 6. MEMBER TRAIL IDS SERIALIZATION RULES

The `member_trail_ids` field is a semicolon-delimited list of
integers:

- Each value must be a valid integer trail_id
- No spaces around semicolons
- Preserve normalization order (not alphabetized)
- Blank if no IDs have been resolved yet
- Must not contain non-integer values or placeholder text

Example: `34;89;112`

------------------------------------------------------------
# 7. DELIMITER RULES

### 7.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs

### 7.2 Each row must contain exactly **16 tab characters**
- 17 fields → 16 delimiters
- No more, no fewer

### 7.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 7.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

------------------------------------------------------------
# 8. BLANK-FIELD RULES

### 8.1 Blank fields must be represented as true blanks
A blank field is `\t\t` with nothing between the tabs.

### 8.2 No spaces inside blank fields
Invalid: `\t \t`, `\t  \t`

### 8.3 No placeholder values
Invalid: `_`, `NULL`, `""`, `BLANK`

### 8.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`.

------------------------------------------------------------
# 9. WHITESPACE RULES

### 9.1 No leading or trailing spaces in any field

### 9.2 No trailing spaces at end of line
Lines must end immediately after the Network ID field.

### 9.3 Internal spaces allowed only when part of the field value

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

### 10.1 Each row must contain exactly **17 fields**

### 10.2 Each row must contain exactly **16 tabs**
This is the primary delimiter-integrity invariant.

### 10.3 No field may be omitted
If unknown or inapplicable, represent as a blank field.

### 10.4 No field may be duplicated

### 10.5 Trail Networks remain single rows
No row expansion regardless of member count or county span.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM

**Step 1**  — Receive normalized 17-field Trail Network record
**Step 2**  — Validate Network Name (must not be blank)
**Step 3**  — Serialize Maps field (each entry a well-formed
              https:// URL; no embedded metadata; no empty
              segments)
**Step 4**  — Serialize Member Trail IDs (integers only,
              semicolon-delimited)
**Step 5**  — Validate Counties formatting (semicolon-delimited,
              alphabetized, no "County" suffix)
**Step 6**  — Validate States Included (two-letter abbreviations,
              alphabetized, or blank; "Ohio" must not appear for
              Ohio-only networks)
**Step 7**  — Validate Network Type (valid vocabulary value)
**Step 8**  — Validate Status (valid vocabulary value or blank)
**Step 9**  — Validate Total Length (numeric only or blank)
**Step 10** — Validate Member Trail Count (integer or blank)
**Step 11** — Validate Member Trail IDs (integers only or blank)
**Step 12** — Validate Identity Notes (free text or blank)
**Step 13** — Validate no internal tabs
**Step 14** — Validate no internal newlines
**Step 15** — Validate whitespace rules
**Step 16** — Join fields with tab characters
**Step 17** — Validate delimiter count (must be 16)
**Step 18** — Validate blank-field representation
**Step 19** — Emit row

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 16 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Network Name is blank
- Governance is blank
- Network Type is blank or contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Counties field is not semicolon-delimited and alphabetized,
  or contains the word "County"
- States Included contains "Ohio" for an Ohio-only network
- Total Length contains non-numeric content
- Member Trail Count is non-integer
- Member Trail IDs contain non-integer values
- Maps field contains embedded metadata or malformed URLs
- Network ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK v5.x

The TSV Integrity Check must:

- Recount delimiters (expect 16 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting (semicolon-delimited, alphabetized)
- Validate States Included formatting
- Validate Maps field (well-formed https:// URLs, no embedded
  metadata)
- Validate Member Trail IDs are integers
- Validate Network Type and Status vocabulary values
- Validate Total Length is numeric
- Validate Network ID is integer
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 14. DESIGN NOTES

### 14.1 Maps Field
Trail Networks use a semicolon-delimited URL list for maps —
consistent with all other v5.1 entities. Trail Networks are
linear spatial systems for which multiple map formats (PDF strip
maps, interactive web maps, downloadable GPX/KML files) are
routinely published. The URL list captures all of these without
embedded metadata.

### 14.2 States Included — Ohio-Only Rule
Blank for Ohio-only networks. "Ohio" is never written for
in-state networks. The blank signals single-state implicitly.
Consistent with Site Network v5.1.

### 14.3 Member Count vs. Member Trail IDs
These are independent fields populated from different sources:
Member Trail Count from officially published counts; Member Trail
IDs from normalization resolution. They may not match during
active discovery phases. The Integrity Check should flag
significant discrepancies but not treat mismatches as hard errors
during active discovery.

### 14.4 Total Length — Published vs. Computed
When an authoritative source publishes a total network length,
use that value. Do not compute by summing member trail lengths —
published lengths may reflect planned extensions, shared segments,
or rounding conventions. If published and computed lengths differ,
log the discrepancy in the Audit & Logging Module for manual
review.

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- Trail Network Schema Module v5.x
- Trail Network Vocabulary Module v5.x
- Trail Network Normalization Contract v5.x
- Trail Schema Module v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing Orchestration Module v5.x

------------------------------------------------------------
# END OF TRAIL NETWORK TSV OUTPUT SPECIFICATION v5.1
