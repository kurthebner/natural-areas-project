# NATURAL AREAS PROJECT — SITE NETWORK TSV OUTPUT SPECIFICATION v5.0
Authoritative, deterministic formatting-layer specification defining exactly how
**Normalized Site Network Entities v5.0** are serialized into tab-separated values (TSV)
with guaranteed delimiter integrity, zero drift, and full compatibility with the
v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.0**.
All field definitions are defined in the **Site Network Schema Module v5.0**.
All normalization rules are defined in the **Site Network Normalization Contract v5.0**.

---

## v5.0 Changes from v4.0

- `alternate_names` removed — rarely documented; variants noted in description
- `history` removed — merged into description
- `network_affiliation` removed — cleaner architecture without nested affiliations
- `counties_traversed` → `counties` (renamed; still semicolon-delimited, alphabetized)
- `primary_managing_agency` → `governance` (renamed)
- `secondary_managing_agencies` → `partner_agencies` (renamed)
- `ownership` added (who legally owns or established the network)
- `member_count` added (number of member Sites)
- `member_site_ids` serialized as semicolon-delimited integer list in TSV
- `states_included` added for multi-state networks
- `map_url` retained as simple optional field (not rich array — Site Networks are not inherently linear)
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- `network_id` added as final field for referential integrity
- Field count updated to 15

---

## 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Site Networks
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- Member Site IDs serialization rules
- Multi-county and multi-state representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Site Network TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **normalized Site Network entities v5.0**
- All counties and all processing runs
- All automated or manual TSV exports
- All v5.0 normalization workflows
- All multi-entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank-field representation
- Derived Label computation and placement
- Member Site IDs serialization
- Multi-county and multi-state representation

---

## 3. FIELD ORDER (AUTHORITATIVE, v5.0)

Site Network TSV output must contain exactly **15 fields** in the following order:

1. Network Name
2. Network Type
3. Status
4. Ownership
5. Governance
6. Partner Agencies
7. Counties
8. States Included
9. Member Count
10. Member Site IDs
11. Description
12. Notes
13. URL
14. Map URL
15. Derived Label
16. Network ID

> **Note:** The Site Network Schema Module v5.0 header lists 13 fields but the
> field-by-field section enumerates 15 named fields (Network Name through Derived Label),
> plus Network ID as the final referential field. This TSV spec treats Network ID as
> the canonical 16th field. The schema header should be updated to reflect the correct
> count of 16 fields.

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

### Field 1 — Network Name
- Required; must never be blank
- Use the official published name
- Must be unique statewide (case-insensitive)
- Must not include unofficial descriptors
- Must align with identity determined by the Resolution Engine v5.0

### Field 2 — Network Type
- Required
- Must match a valid value from the Site Network Vocabulary Module v5.0
- Must not be inferred from member sites, geography, or governance
- One value only; no semicolon-delimited lists

### Field 3 — Status
- Optional
- Must match a valid value from the Site Network Vocabulary Module v5.0: Active, Proposed, Under Development, Inactive, Dissolved
- Blank if not documented; Active is the implied default for operational networks
- "Proposed" and "Dissolved" must be explicitly documented — never inferred

### Field 4 — Ownership
- Optional free-text field — no controlled vocabulary
- Must contain the legal name of the entity that owns or established the network
- Must not use generic categories (e.g., "County Government")
- Must not encode management or governance (those go in Fields 5–6)
- Blank when ownership is distributed among member sites, when the network is a coordinating or designating body without land ownership, or when unclear
- Blank is correct and common for formally designated networks (NHAs, heritage corridors)

### Field 5 — Governance
- Required
- Primary agency or organization responsible for coordinating or managing the network
- Must be an authoritative name
- Must not use generic categories
- Must not be inferred

### Field 6 — Partner Agencies
- Optional
- Semicolon-delimited list of secondary managing agencies or documented organizational partners
- Must not duplicate Governance
- Must not include inferred partners
- Blank if none documented

### Field 7 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Must include all counties through which any part of the network passes
- Site Networks remain single rows regardless of number of counties — no row expansion

### Field 8 — States Included
- Optional
- Semicolon-delimited, alphabetized list of state names
- Only used for multi-state networks
- Blank for Ohio-only networks — do not write "Ohio" for in-state networks
- Must not be inferred

### Field 9 — Member Count
- Optional but strongly recommended
- Integer representing the number of member Sites
- Record the officially published count when available
- May be estimated from enumerated member list if published count is unavailable
- Blank if truly unknown
- Must never be computed by counting `member_site_ids` during TSV generation — use the normalized value

### Field 10 — Member Site IDs
- Optional
- Semicolon-delimited list of integer site_id values referencing normalized Site entities
- Populated during normalization as member Sites are resolved; may be incomplete during initial discovery
- Blank if no member Site IDs have been resolved yet
- Must not contain non-integer values or placeholder text
- Provides a convenience cache; full membership is queryable via `site_network_members` relationship table

### Field 11 — Description
- Optional but strongly recommended
- 1–3 sentences describing the network's identity, scope, and purpose
- May include brief establishment history or origin context
- Must not include Site-level, Trail-level, or Access Point details
- Must not be blank if the network has an authoritative self-description

### Field 12 — Notes
- Optional
- Free-text field for clarifications, gaps, or contextual notes
- Must not include identity-defining characteristics (those go in Description)
- Must not include Site-level or Trail-level details

### Field 13 — URL
- Optional but strongly recommended
- Full https:// URL to the primary authoritative network page
- Semicolon-delimit if multiple authoritative URLs
- Must not include placeholders or inferred URLs

### Field 14 — Map URL
- Optional
- Full https:// URL to an authoritative system-wide map or GIS viewer
- May include PDF maps, static images, or interactive GIS layers
- Semicolon-delimit if multiple
- Blank if none — Site Networks are not inherently linear and may lack a system map

### Field 15 — Derived Label
- Computed at TSV output time from normalized fields; must never be pre-stored
- Formula: **Network Type + " — " + Governance**
- Example: `National Heritage Area — National Park Service`
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors

### Field 16 — Network ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `network_id`
- Enables joins to the `site_network_members` relationship table

---

## 5. MULTI-COUNTY AND MULTI-STATE REPRESENTATION RULES

Site Networks are **not expanded** into multiple TSV rows.

- Multi-county Site Networks must appear as **a single TSV row**
- The **Counties** field must contain a **semicolon-delimited, alphabetized list**
- The Counties field must not include the word "County"
- The **States Included** field follows the same pattern for multi-state networks
- Blank States Included for Ohio-only networks

Example:
- Normalized counties: `Lucas;Wood`
- TSV Counties output: `Lucas;Wood`
- Ohio-only → States Included: *(blank)*

---

## 6. MEMBER SITE IDS SERIALIZATION RULES

The `member_site_ids` array from the normalized entity is serialized as a
semicolon-delimited list of integers:

- Each value must be a valid integer site_id
- No spaces around semicolons
- Alphabetical ordering is not required — preserve normalization order
- Blank if the array is empty or no IDs have been resolved
- Must not contain placeholder values

Example:
- Normalized: `[101, 247, 388]`
- TSV output: `101;247;388`

---

## 7. DELIMITER RULES

### 7.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs
- No spaces may appear between tabs

### 7.2 Each row must contain exactly **15 tab characters**
- 16 fields → 15 delimiters
- No more, no fewer

### 7.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 7.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

---

## 8. BLANK-FIELD RULES

### 8.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

### 8.2 No spaces inside blank fields
Invalid:
- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

### 8.3 No placeholder values
Invalid: `_`, `NULL`, `""`, `BLANK`

### 8.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`.

---

## 9. WHITESPACE RULES

### 9.1 No leading or trailing spaces in any field
Invalid: `" Heritage Area"`, `"Heritage Area "`, `" Heritage Area "`

### 9.2 No trailing spaces at end of line
Lines must end immediately after the **Network ID** field.

### 9.3 Internal spaces allowed only when part of the field value
Valid: `"Black Swamp Conservancy"`
Invalid: `"  Black Swamp Conservancy"`

---

## 10. ROW CONSTRUCTION RULES

### 10.1 Each row must contain exactly **16 fields**
No more, no fewer.

### 10.2 Each row must contain exactly **15 tabs**
This is the primary delimiter-integrity invariant.

### 10.3 No field may be omitted
If a field is unknown or inapplicable, it must be represented as a blank field (`\t\t`).

### 10.4 No field may be duplicated
Each field appears exactly once.

### 10.5 Site Networks remain single rows
No row expansion occurs regardless of member count or county span.

---

## 11. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized Site Network record (excluding Derived Label)**
**Step 2 — Compute Derived Label: Network Type + " — " + Governance**
**Step 3 — Serialize Member Site IDs array to semicolon-delimited integer list**
**Step 4 — Validate Counties formatting (semicolon-delimited, alphabetized, no "County" suffix)**
**Step 5 — Validate States Included (semicolon-delimited, alphabetized, or blank)**
**Step 6 — Validate Network Type (valid vocabulary value)**
**Step 7 — Validate Status (valid vocabulary value or blank)**
**Step 8 — Validate Member Site IDs (integers only, or blank)**
**Step 9 — Validate Member Count (integer or blank)**
**Step 10 — Validate no internal tabs**
**Step 11 — Validate no internal newlines**
**Step 12 — Validate whitespace rules**
**Step 13 — Join fields with tab characters**
**Step 14 — Validate delimiter count (must be 15)**
**Step 15 — Validate blank-field representation**
**Step 16 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

## 12. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 15 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Network Name is blank
- Governance is blank
- Network Type is blank or contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Counties field is not semicolon-delimited and alphabetized, or contains the word "County"
- States Included contains "Ohio" for an Ohio-only network (should be blank)
- Member Site IDs contains non-integer values
- Member Count is non-integer
- Derived Label is malformed, missing, or pre-stored (not computed at output time)
- Network ID is missing or non-integer
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
- Validate Counties formatting (semicolon-delimited, alphabetized, no "County" suffix)
- Validate States Included formatting
- Validate Member Site IDs are integers and reference known site_id values
- Validate Network Type and Status vocabulary values
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free
Site Network TSV output.

---

## 14. DESIGN NOTES AND SUGGESTIONS

### 14.1 Map URL vs. Maps Array
Site Networks use a simple `map_url` field (not the rich `maps` array used by
Trail Networks). This reflects the fact that Site Networks are not inherently
linear spatial entities — a system-wide map is useful but multiple map formats
are less commonly needed than for trail networks. If this assumption proves
incorrect in practice (e.g., for large multi-county Site Networks with
published PDF maps and interactive GIS layers), consider upgrading this field
to a rich `maps` array in a future version.

### 14.2 States Included — Ohio-Only Rule
The States Included field is intentionally left blank for Ohio-only networks.
Writing "Ohio" creates noise and implies the field is required for all networks.
The blank signals "single-state, implicitly Ohio" cleanly. This aligns with
the Counties field pattern, which also excludes the word "County."

### 14.3 Member Count vs. Member Site IDs
Member Count and Member Site IDs are related but independent:
- Member Count is the official or best-available count from authoritative sources
- Member Site IDs is the resolved list of normalized site_id values

These may not match during active discovery (IDs not yet resolved) or when
some member Sites are outside the current processing scope. Both fields should
be populated independently; the Integrity Check should flag significant
discrepancies but not treat them as hard errors during active discovery phases.

### 14.4 Schema Field Count Discrepancy
The Site Network Schema Module v5.0 lists "13 FIELDS" in its header but
enumerates 15 named fields (Network Name through Derived Label) in Section 2,
plus Network ID as the final referential field. This TSV spec uses 16 as the
authoritative field count. The schema header should be corrected.

---

## 15. MODULE DEPENDENCIES

This module depends on:

- Site Network Schema Module v5.0
- Site Network Vocabulary Module v5.0
- Site Network Normalization Contract v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF SITE NETWORK TSV OUTPUT SPECIFICATION v5.0
