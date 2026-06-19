# NATURAL AREAS PROJECT — TRAIL NETWORK TSV OUTPUT SPECIFICATION v5.0
Authoritative, deterministic formatting-layer specification defining exactly how
**Normalized Trail Network Entities v5.0** are serialized into tab-separated values (TSV)
with guaranteed delimiter integrity, zero drift, and full compatibility with the
v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.0**.
All field definitions are defined in the **Trail Network Schema Module v5.0**.
All normalization rules are defined in the **Trail Network Normalization Contract v5.0**.

---

## v5.0 Changes from v4.0

- `alternate_names` removed — rarely documented; variants noted in description
- `history` removed — merged into description
- `county_list` → `counties` (renamed; still semicolon-delimited, alphabetized)
- `primary_managing_agency` → `governance` (renamed)
- `secondary_managing_agencies` → `partner_agencies` (renamed)
- `map_url` → `maps` (rich array serialized as semicolon-delimited URL list — Trail Networks are spatial; multiple map formats common)
- `status` added (was missing from v4.0)
- `ownership` added (optional — meaningful for single-owner networks)
- `total_length_miles` added (important metric, usually published)
- `member_trail_count` added (number of member Trails)
- `member_trail_ids` added (array linking to member Trail IDs)
- `states_included` added for multi-state networks
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- `network_id` added as final field for referential integrity
- Field count updated to 17

---

## 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Trail Networks
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- Maps field serialization rules
- Member Trail IDs serialization rules
- Multi-county and multi-state representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Trail Network TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **normalized Trail Network entities v5.0**
- All counties and all processing runs
- All automated or manual TSV exports
- All v5.0 normalization workflows
- All multi-entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank-field representation
- Derived Label computation and placement
- Maps array serialization
- Member Trail IDs serialization
- Multi-county and multi-state representation

---

## 3. FIELD ORDER (AUTHORITATIVE, v5.0)

Trail Network TSV output must contain exactly **17 fields** in the following order:

1. Network Name
2. Network Type
3. Status
4. Ownership
5. Governance
6. Partner Agencies
7. Counties
8. States Included
9. Total Length (Miles)
10. Member Trail Count
11. Member Trail IDs
12. Description
13. Notes
14. URL
15. Maps
16. Derived Label
17. Network ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

### Field 1 — Network Name
- Required; must never be blank
- Use the official published name
- Must be unique statewide (case-insensitive)
- Must not include unofficial descriptors or hierarchy encoding
- Must align with identity determined by the Resolution Engine v5.0

### Field 2 — Network Type
- Required
- Must match a valid value from the Trail Network Vocabulary Module v5.0
- Must not be inferred from member count, geographic extent, or governance structure
- One value only; no semicolon-delimited lists

### Field 3 — Status
- Optional
- Must match a valid value from the Trail Network Vocabulary Module v5.0: Active, Planned, Under Development, Partially Open, Closed
- Blank if not documented; Active is the implied default for operational networks
- "Planned" and "Closed" must be explicitly documented — never inferred

### Field 4 — Ownership
- Optional free-text field — no controlled vocabulary
- Must contain the legal name of the entity that owns or established the network
- Must not use generic categories
- Must not encode management or governance (those go in Fields 5–6)
- Blank when ownership is distributed across multiple agencies, when the network is a coordinating body without land ownership, or when unclear
- Blank is correct and common for networks that are coordinating or designating bodies rather than land owners

### Field 5 — Governance
- Required
- Primary agency or organization responsible for coordinating or managing the Trail Network
- Must be an authoritative name
- Must not encode ownership or hierarchy
- Must not be inferred

### Field 6 — Partner Agencies
- Optional
- Semicolon-delimited list of secondary managing agencies, land managers, or documented organizational partners
- Important for networks crossing multiple jurisdictions
- Must not duplicate Governance
- Must not include inferred partners
- Blank if none documented

### Field 7 — Counties
- Required
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Must include all counties through which any part of the network passes
- Must not include inferred counties
- Trail Networks remain single rows regardless of county span — no row expansion

### Field 8 — States Included
- Optional
- Semicolon-delimited, alphabetized list of state names
- Only used for multi-state networks
- Blank for Ohio-only networks — do not write "Ohio" for in-state networks
- Must not include inferred states

### Field 9 — Total Length (Miles)
- Optional
- Numeric value only — no units suffix, no range notation
- Represents the total documented length of all member trails
- Use officially published length when available
- If computed vs. published lengths differ, note discrepancy in normalization log — do not average or blend
- Blank if unknown or undocumented

### Field 10 — Member Trail Count
- Optional but strongly recommended
- Integer representing the number of member Trails
- Record the officially published count when available
- May be estimated from an enumerated member list if published count is unavailable
- Blank if truly unknown
- Must never be computed by counting `member_trail_ids` during TSV generation — use the normalized value

### Field 11 — Member Trail IDs
- Optional
- Semicolon-delimited list of integer trail_id values referencing normalized Trail entities
- Populated during normalization as member Trails are resolved; may be incomplete during initial discovery
- Blank if no member Trail IDs have been resolved yet
- Must not contain non-integer values or placeholder text
- Provides a convenience cache; full membership is queryable via `trail_network_members` relationship table

### Field 12 — Description
- Optional but strongly recommended
- 1–3 sentences describing the network's identity, scope, and purpose
- May include brief establishment history or origin context
- Must not include Trail-level or Segment-level details
- Must not include temporary conditions

### Field 13 — Notes
- Optional
- Free-text field for clarifications, gaps, planned extensions, or contextual notes
- Must not include identity-defining characteristics (those go in Description)
- Must not include Trail-level or Segment-level details

### Field 14 — URL
- Optional but strongly recommended
- Full https:// URLs only
- Semicolon-delimit if multiple authoritative URLs
- Must reference authoritative sources
- Tracking parameters must be removed

### Field 15 — Maps
- Optional
- Serialized from the `maps` array in the normalized entity
- In TSV: semicolon-delimited list of URLs only — type and description metadata are dropped
- Trail Networks are linear spatial systems; multiple map formats (PDF, interactive, GPX, KML) are common
- Blank if no maps documented
- Example: `https://ncta.org/map.pdf;https://traillink.com/trail/north-country-trail/`

### Field 16 — Derived Label
- Computed at TSV output time from normalized fields; must never be pre-stored
- Formula: **Network Type + " — " + Governance**
- Example: `Water Trail Network — Maumee River Watershed Council`
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors

### Field 17 — Network ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `network_id`
- Enables joins to the `trail_network_members` relationship table

---

## 5. MULTI-COUNTY AND MULTI-STATE REPRESENTATION RULES

Trail Networks are **not expanded** into multiple TSV rows.

- Multi-county Trail Networks must appear as **a single TSV row**
- The **Counties** field must contain a **semicolon-delimited, alphabetized list**
- The Counties field must not include the word "County"
- The **States Included** field follows the same pattern for multi-state networks
- Blank States Included for Ohio-only networks
- No inference permitted — only documented counties and states may be included

Example:
- Normalized counties: `Fulton;Henry;Lucas;Wood`
- TSV Counties output: `Fulton;Henry;Lucas;Wood`
- Ohio-only → States Included: *(blank)*

---

## 6. MAPS FIELD SERIALIZATION RULES

The `maps` array from the normalized entity is serialized for TSV as a
semicolon-delimited list of URLs only. Type and description metadata are dropped.

- Each value must be a full https:// URL
- No spaces around semicolons
- Order is preserved from the normalized array
- Blank if the array is empty
- Must not contain raw map objects or metadata

Example:
- Normalized: `[{url: "https://ncta.org/map.pdf", type: "pdf"}, {url: "https://ncta.org/interactive", type: "interactive"}]`
- TSV output: `https://ncta.org/map.pdf;https://ncta.org/interactive`

---

## 7. MEMBER TRAIL IDS SERIALIZATION RULES

The `member_trail_ids` array from the normalized entity is serialized as a
semicolon-delimited list of integers:

- Each value must be a valid integer trail_id
- No spaces around semicolons
- Alphabetical ordering is not required — preserve normalization order
- Blank if the array is empty or no IDs have been resolved
- Must not contain non-integer values or placeholder text

Example:
- Normalized: `[34, 89, 112]`
- TSV output: `34;89;112`

---

## 8. DELIMITER RULES

### 8.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`)
- No spaces may appear before or after tabs
- No spaces may appear between tabs

### 8.2 Each row must contain exactly **16 tab characters**
- 17 fields → 16 delimiters
- No more, no fewer

### 8.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 8.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

---

## 9. BLANK-FIELD RULES

### 9.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

### 9.2 No spaces inside blank fields
Invalid:
- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

### 9.3 No placeholder values
Invalid: `_`, `NULL`, `""`, `BLANK`

### 9.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`.

---

## 10. WHITESPACE RULES

### 10.1 No leading or trailing spaces in any field
Invalid: `" Maumee Water Trail"`, `"Maumee Water Trail "`, `" Maumee Water Trail "`

### 10.2 No trailing spaces at end of line
Lines must end immediately after the **Network ID** field.

### 10.3 Internal spaces allowed only when part of the field value
Valid: `"North Country Trail Association"`
Invalid: `"  North Country Trail Association"`

---

## 11. ROW CONSTRUCTION RULES

### 11.1 Each row must contain exactly **17 fields**
No more, no fewer.

### 11.2 Each row must contain exactly **16 tabs**
This is the primary delimiter-integrity invariant.

### 11.3 No field may be omitted
If a field is unknown or inapplicable, it must be represented as a blank field (`\t\t`).

### 11.4 No field may be duplicated
Each field appears exactly once.

### 11.5 Trail Networks remain single rows
No row expansion occurs regardless of member count or county span.

---

## 12. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized Trail Network record (excluding Derived Label)**
**Step 2 — Compute Derived Label: Network Type + " — " + Governance**
**Step 3 — Serialize Maps array to semicolon-delimited URL list**
**Step 4 — Serialize Member Trail IDs array to semicolon-delimited integer list**
**Step 5 — Validate Counties formatting (semicolon-delimited, alphabetized, no "County" suffix)**
**Step 6 — Validate States Included (semicolon-delimited, alphabetized, or blank)**
**Step 7 — Validate Network Type (valid vocabulary value)**
**Step 8 — Validate Status (valid vocabulary value or blank)**
**Step 9 — Validate Total Length (numeric or blank)**
**Step 10 — Validate Member Trail Count (integer or blank)**
**Step 11 — Validate Member Trail IDs (integers only, or blank)**
**Step 12 — Validate Maps (URLs only, no raw objects)**
**Step 13 — Validate no internal tabs**
**Step 14 — Validate no internal newlines**
**Step 15 — Validate whitespace rules**
**Step 16 — Join fields with tab characters**
**Step 17 — Validate delimiter count (must be 16)**
**Step 18 — Validate blank-field representation**
**Step 19 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

## 13. ERROR CONDITIONS

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
- Counties field is not semicolon-delimited and alphabetized, or contains the word "County"
- States Included contains "Ohio" for an Ohio-only network (should be blank)
- Total Length contains non-numeric content
- Member Trail Count is non-integer
- Member Trail IDs contain non-integer values
- Maps field contains raw objects rather than serialized URLs
- Derived Label is malformed, missing, or pre-stored (not computed at output time)
- Network ID is missing or non-integer
- Field order is incorrect
- A field is missing
- A field is duplicated

All errors must be logged in the Audit & Logging Module v5.0.

---

## 14. INTEGRATION WITH TSV INTEGRITY CHECK v5.0

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank-field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement and freshness (not pre-stored)
- Validate Maps serialization (URL list only, no raw objects)
- Revalidate Counties formatting (semicolon-delimited, alphabetized, no "County" suffix)
- Validate States Included formatting
- Validate Member Trail IDs are integers and reference known trail_id values
- Validate Network Type and Status vocabulary values
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free
Trail Network TSV output.

---

## 15. DESIGN NOTES AND SUGGESTIONS

### 15.1 Maps vs. Map URL
Trail Networks use the rich `maps` array (serialized to semicolon-delimited URLs
in TSV) rather than a simple `map_url` field. This reflects the fact that Trail
Networks are linear spatial systems for which multiple map formats — PDF strip
maps, interactive web maps, downloadable GPX/KML files — are routinely published
by managing agencies. The richer array is the correct model here. Site Networks,
by contrast, use a simple `map_url` because they are not inherently linear.

### 15.2 States Included — Ohio-Only Rule
Follows the same convention as Site Networks: blank for Ohio-only networks.
"Ohio" is never written for in-state networks. The blank signals single-state
implicitly.

### 15.3 Member Count vs. Member Trail IDs
Same pattern as Site Networks: these are independent fields, populated from
different sources (official published counts vs. resolved normalization IDs).
They may not match during active discovery. The Integrity Check should flag
significant discrepancies but not treat mismatches as hard errors during
active discovery phases.

### 15.4 Total Length Published vs. Computed
When an authoritative source publishes a total network length, use that value.
Do not compute a length by summing member trail lengths, as published network
lengths may reflect planned extensions, shared segments, or rounding conventions
that differ from summed values. If computed and published lengths differ
significantly, log the discrepancy in the Audit & Logging Module v5.0 for
manual review. Do not silently average or blend.

### 15.5 Derived Label Formula
The formula **Network Type + " — " + Governance** produces labels like:
- `Water Trail Network — Maumee River Watershed Council`
- `National Scenic Trail System — North Country Trail Association`
- `County Trail Network — Wood County Park District`

These are compact and informative for both human review and downstream processing.
If Governance contains a very long agency name, consider whether an abbreviated
form should be standardized in normalization — but the formula itself must not
be modified.

---

## 16. MODULE DEPENDENCIES

This module depends on:

- Trail Network Schema Module v5.0
- Trail Network Vocabulary Module v5.0
- Trail Network Normalization Contract v5.0
- Trail Schema Module v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF TRAIL NETWORK TSV OUTPUT SPECIFICATION v5.0
