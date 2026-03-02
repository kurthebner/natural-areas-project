# NATURAL AREAS PROJECT
# SITE NETWORK TSV OUTPUT SPECIFICATION v5.1
Authoritative, deterministic formatting-layer specification defining exactly
how **Normalized Site Network Entities v5.1** are serialized into
tab-separated values (TSV) with guaranteed delimiter integrity, zero drift,
and full compatibility with the v5.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.x**.
All field definitions are defined in the **Site Network Schema Module v5.x**.
All normalization rules are defined in the
**Site Network Normalization Contract v5.x**.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **Map URL field removed**: Map URLs now included in URL field
  (semicolon-delimited with other authoritative URLs)
- **Derived Label removed**: No longer computed or stored at any stage
- **identity_notes added**: New field between Description and Notes;
  surfaced from identity_notes_raw at discovery stage
- **Field count updated**: 15 fields (was 16), 14 tab delimiters (was 15)
- **TSV generation algorithm updated**: Steps revised for removed and
  added fields
- **Error conditions updated**: Map URL and Derived Label conditions removed;
  identity_notes conditions added
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed
- `history` removed — merged into description
- `network_affiliation` removed
- `counties_traversed` → `counties`
- `primary_managing_agency` → `governance`
- `secondary_managing_agencies` → `partner_agencies`
- `ownership` added
- `member_count` added
- `member_site_ids` serialized as semicolon-delimited integer list
- `states_included` added for multi-state networks
- `network_id` added as final field for referential integrity

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Site Networks
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Member Site IDs serialization rules
- Multi-county and multi-state representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.x

This specification is authoritative for **Site Network TSV formatting**.

------------------------------------------------------------
# 2. FIELD ORDER (AUTHORITATIVE, v5.1)

Site Network TSV output must contain exactly **15 fields** in the
following order:

1.  Network Name
2.  Network Type
3.  Status
4.  Ownership
5.  Governance
6.  Partner Agencies
7.  Counties
8.  States Included
9.  Member Count
10. Member Site IDs
11. Description
12. Identity Notes
13. Notes
14. URL
15. Network ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**15 fields = 14 tab delimiters per row.**

------------------------------------------------------------
# 3. FIELD NOTES

### Field 1 — Network Name
- Required; must never be blank
- Use the official published name
- Must be unique statewide (case-insensitive)
- Must not include unofficial descriptors

### Field 2 — Network Type
- Required
- Must match a valid value from the Site Network Vocabulary Module v5.x
- Must not be inferred from member sites, geography, or governance
- One value only; no semicolon-delimited lists

### Field 3 — Status
- Optional
- Must match a valid value from the Site Network Vocabulary Module v5.x:
  Active, Proposed, Under Development, Inactive, Dissolved
- Blank if not documented
- "Proposed" and "Dissolved" must be explicitly documented — never inferred

### Field 4 — Ownership
- Optional free-text — no controlled vocabulary
- Must contain the legal name of the entity that owns or established
  the network
- Must not use generic categories
- Blank when ownership is distributed, undocumented, or when the network
  is a coordinating/designating body without land ownership
- Blank is correct and common for NHAs, scenic river corridors,
  heritage corridors

### Field 5 — Governance
- Required
- Primary agency or organization responsible for coordinating or
  managing the network
- Must be an authoritative name; must not use generic categories

### Field 6 — Partner Agencies
- Optional
- Semicolon-delimited list of secondary managing agencies or documented
  organizational partners
- Must not duplicate Governance
- Blank if none documented

### Field 7 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Must include all counties the network spans
- Site Networks remain single rows regardless of number of counties

### Field 8 — States Included
- Optional
- Semicolon-delimited, alphabetized list of state abbreviations
- Only used for multi-state networks
- Blank for Ohio-only networks — do not write "Ohio"

### Field 9 — Member Count
- Optional but strongly recommended
- Integer representing the number of member Sites
- Record the officially published count when available
- Blank if truly unknown
- Must never be recomputed by counting member_site_ids during TSV
  generation — use the normalized value

### Field 10 — Member Site IDs
- Optional
- Semicolon-delimited list of integer site_id values referencing
  normalized Site entities
- Blank if no member Site IDs have been resolved yet
- Must not contain non-integer values or placeholder text

### Field 11 — Description
- Optional but strongly recommended
- 1-3 sentences describing the network's identity, scope, and purpose
- May include brief establishment history or origin context
- Must not include Site-level, Trail-level, or Access Point details

### Field 12 — Identity Notes
- Optional
- Free-text field for identity clarifications, disambiguation notes,
  alternate names, SITE_NETWORK_UNCERTAIN flags, and governance
  verification notes
- Must not duplicate Description content
- Must not contain operational or contextual notes (those go in Notes)
- SITE_NETWORK_UNCERTAIN flags must be preserved here if set

### Field 13 — Notes
- Optional
- Free-text for operational details, designation history, funding notes,
  boundary clarifications, contextual notes, discovery gaps
- Must not include identity-defining characteristics (those go in
  Description or Identity Notes)

### Field 14 — URL
- Optional but strongly recommended
- Full https:// URL to the primary authoritative network page
- Semicolon-delimit if multiple authoritative URLs exist, including
  any map URLs (system-wide maps, GIS viewers, PDF maps)
- Must not include placeholders or inferred URLs

### Field 15 — Network ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's network_id
- Enables joins to the site_network_members relationship table

------------------------------------------------------------
# 4. MULTI-COUNTY AND MULTI-STATE REPRESENTATION RULES

Site Networks are **not expanded** into multiple TSV rows.

- Multi-county Site Networks must appear as **a single TSV row**
- The **Counties** field must contain a **semicolon-delimited,
  alphabetized list** without the word "County"
- The **States Included** field follows the same pattern for
  multi-state networks
- Blank States Included for Ohio-only networks

Example:
- Normalized counties: `Lucas;Wood`
- TSV Counties output: `Lucas;Wood`
- Ohio-only → States Included: *(blank)*

------------------------------------------------------------
# 5. MEMBER SITE IDS SERIALIZATION RULES

The `member_site_ids` array from the normalized entity is serialized as a
semicolon-delimited list of integers:

- Each value must be a valid integer site_id
- No spaces around semicolons
- Alphabetical ordering not required — preserve normalization order
- Blank if the array is empty or no IDs have been resolved
- Must not contain placeholder values

Example:
- Normalized: `[101, 247, 388]`
- TSV output: `101;247;388`

------------------------------------------------------------
# 6. DELIMITER RULES

### 6.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs

### 6.2 Each row must contain exactly **14 tab characters**
- 15 fields → 14 delimiters
- No more, no fewer

### 6.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 6.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

------------------------------------------------------------
# 7. BLANK-FIELD RULES

### 7.1 Blank fields must be represented as true blanks
A blank field is represented as `\t\t` with nothing between the tabs.

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
Lines must end immediately after the Network ID field.

### 8.3 Internal spaces allowed only when part of the field value

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **15 fields**

### 9.2 Each row must contain exactly **14 tabs**
This is the primary delimiter-integrity invariant.

### 9.3 No field may be omitted
If unknown or inapplicable, represent as a blank field.

### 9.4 No field may be duplicated

### 9.5 Site Networks remain single rows
No row expansion regardless of member count or county span.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1**  — Receive normalized Site Network record
**Step 2**  — Serialize Member Site IDs array to semicolon-delimited
              integer list
**Step 3**  — Validate Counties formatting (semicolon-delimited,
              alphabetized, no "County" suffix)
**Step 4**  — Validate States Included (semicolon-delimited,
              alphabetized, or blank)
**Step 5**  — Validate Network Type (valid vocabulary value)
**Step 6**  — Validate Status (valid vocabulary value or blank)
**Step 7**  — Validate Member Site IDs (integers only, or blank)
**Step 8**  — Validate Member Count (integer or blank)
**Step 9**  — Validate Identity Notes (free text or blank;
              SITE_NETWORK_UNCERTAIN flags preserved)
**Step 10** — Validate no internal tabs
**Step 11** — Validate no internal newlines
**Step 12** — Validate whitespace rules
**Step 13** — Join fields with tab characters
**Step 14** — Validate delimiter count (must be 14)
**Step 15** — Validate blank-field representation
**Step 16** — Emit row

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 14 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Network Name is blank
- Governance is blank
- Network Type is blank or contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Counties field is not semicolon-delimited and alphabetized, or
  contains the word "County"
- States Included contains "Ohio" for an Ohio-only network
  (should be blank)
- Member Site IDs contains non-integer values
- Member Count is non-integer
- Network ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK v5.x

The TSV Integrity Check must:

- Recount delimiters (expect 14 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting
- Validate States Included formatting
- Validate Member Site IDs are integers and reference known site_id values
- Validate Network Type and Status vocabulary values
- Verify SITE_NETWORK_UNCERTAIN flags are preserved in Identity Notes
  if present
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Site Network Schema Module v5.x
- Site Network Vocabulary Module v5.x
- Site Network Normalization Contract v5.x
- TSV Integrity Check Module v5.x
- Audit & Logging Module v5.x
- Processing Orchestration Module v5.x

------------------------------------------------------------
# END OF SITE NETWORK TSV OUTPUT SPECIFICATION v5.1
