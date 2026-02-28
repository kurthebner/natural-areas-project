# NATURAL AREAS PROJECT — TRAIL TSV OUTPUT SPECIFICATION v5.0
Authoritative, deterministic formatting-layer specification defining exactly how
**Normalized Trail Entities v5.0** are serialized into tab-separated values (TSV)
with guaranteed delimiter integrity, zero drift, and full compatibility with the
v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Vocabulary Module v5.0**.
All field definitions are defined in the **Trail Schema Module v5.0**.

---

## v5.0 Changes from v4.0

- `counties_traversed` → `counties` (renamed; still semicolon-delimited, alphabetized)
- `management` / `primary_managing_agency` → `governance`
- `secondary_managing_agencies` → `partner_agencies` (new field)
- `network_affiliation` removed — membership tracked via relationship tables
- `map_url` → `maps` serialized as semicolon-delimited URL list
- `difficulty` and `accessibility` added as new fields
- `trail_history` added as new field
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- Trail ID added as final field for referential integrity
- Field count: 18 → 20

---

## 1. PURPOSE

This module defines:

- The canonical TSV field order for Trails (v5.0)
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- Maps field serialization rules
- Multi-county representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Trail TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **Normalized Trail Entities v5.0**
- All counties and all processing runs
- All automated or manual TSV exports
- All normalization workflows
- All multi-entity orchestration pipelines

---

## 3. FIELD ORDER (AUTHORITATIVE, v5.0)

Trail TSV output must contain exactly **20 fields** in the following order:

1. Trail Name
2. Alternate Names
3. Trail Use Type
4. Trail Surface Type
5. Trail Origin Type
6. Total Length (Miles)
7. Counties
8. Governance
9. Partner Agencies
10. Status
11. Difficulty
12. Accessibility
13. Description
14. Trail History
15. Notes
16. URL
17. Maps
18. Derived Label
19. Parent Trail Network
20. Trail ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

### Field 2 — Alternate Names
- Semicolon-delimited list of documented historical or variant names
- Blank if no alternate names are documented
- Must not repeat Trail Name

### Field 7 — Counties
- Semicolon-delimited, alphabetized list of county names
- Must not include the word "County"
- Multi-county Trails remain single rows — no row expansion
- Must not be inferred from geometry; only documented counties included

### Field 8 — Governance
- Primary agency or organization managing the trail
- Semicolon-delimited if multiple co-managers with equal authority

### Field 9 — Partner Agencies
- Semicolon-delimited list of secondary managing agencies or land managers
- Must not duplicate Governance
- Blank if none documented

### Field 11 — Difficulty
- Must match a valid value from Trail Vocabulary Module v5.0
- Blank if not explicitly documented by an authoritative source
- Must never be assessed or inferred

### Field 12 — Accessibility
- Free-text description of ADA compliance, wheelchair accessibility, grade, width, and accessible facilities
- Blank if not documented

### Field 14 — Trail History
- 1–3 sentences of documented historical context
- Blank if none documented

### Field 17 — Maps
- Serialized from the `maps` array in the normalized entity
- In TSV: semicolon-delimited list of URLs only — type and description metadata are dropped
- Blank if no maps documented
- Example: `https://wcparks.org/trail-map.pdf;https://www.traillink.com/trail/example/`

### Field 18 — Derived Label
- Computed at TSV output time from normalized fields
- Must not be pre-stored in the normalized entity
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors

### Field 19 — Parent Trail Network
- Optional; must match the exact Name of a valid Trail Network entity
- A Trail may have at most one Parent Trail Network
- No semicolon-delimited lists
- Blank if not documented

### Field 20 — Trail ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `trail_id`

---

## 5. MULTI-COUNTY REPRESENTATION RULES (v5.0)

Trails are **not expanded** into multiple TSV rows.

If a Trail spans multiple counties:

- The **Counties** field must contain a **semicolon-delimited, alphabetized list**.
- The field must not include the word "County".
- The Trail must appear as **a single TSV row**, regardless of how many counties it traverses.
- No inference is permitted; only documented counties may be included.

Example:
- Normalized counties: `Delaware;Franklin;Union`
- TSV output: `Delaware;Franklin;Union`

---

## 6. DELIMITER RULES

### 6.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).
- No spaces may appear before or after tabs.
- No spaces may appear between tabs.

### 6.2 Each row must contain exactly **19 tab characters**
- 20 fields → 19 delimiters
- No more, no fewer.

### 6.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

### 6.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

---

## 7. BLANK-FIELD RULES

### 7.1 Blank fields must be true blanks
Represented as: `\t\t`

### 7.2 No spaces inside blank fields
Invalid:
- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

### 7.3 No placeholder values
Invalid: `_`, `NULL`, `""`, `BLANK`

### 7.4 No collapsing of adjacent blanks
Adjacent blanks must remain `\t\t`.

---

## 8. WHITESPACE RULES

### 8.1 No leading or trailing spaces in any field
Invalid: `" Trail"`, `"Trail "`, `" Trail "`

### 8.2 No trailing spaces at end of line
Lines must end immediately after the **Trail ID** field.

### 8.3 Internal spaces allowed only when part of the value
Valid: `"North Ridge Trail"`
Invalid: `"  North Ridge Trail"`

---

## 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **20 fields**
No more, no fewer.

### 9.2 Each row must contain exactly **19 tabs**
Primary delimiter-integrity invariant.

### 9.3 No field may be omitted
Unknown or inapplicable fields → blank field (`\t\t`).

### 9.4 No field may be duplicated
Each field appears exactly once.

### 9.5 Multi-county Trails remain single rows
- Counties field contains semicolon-delimited, alphabetized list.
- No row expansion occurs for Trails.

---

## 10. TSV GENERATION ALGORITHM (v5.0)

**Step 1 — Receive normalized 20-field Trail entity (excluding Derived Label)**
**Step 2 — Compute Derived Label from normalized fields**
**Step 3 — Serialize Maps array to semicolon-delimited URL list**
**Step 4 — Validate Counties formatting (semicolon-delimited, alphabetized)**
**Step 5 — Validate Parent Trail Network (valid Trail Network Name or blank)**
**Step 6 — Validate Alternate Names formatting**
**Step 7 — Validate no internal tabs**
**Step 8 — Validate no internal newlines**
**Step 9 — Validate whitespace rules**
**Step 10 — Join fields with tab characters**
**Step 11 — Validate delimiter count (must be 19)**
**Step 12 — Validate blank-field representation**
**Step 13 — Emit row**

If any step fails, TSV generation must halt and surface an error.

---

## 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 19 tabs
- Field contains a tab
- Field contains a newline
- Blank field contains spaces
- Field contains trailing spaces
- Derived Label malformed, missing, or pre-stored (not computed at output time)
- Maps field contains raw objects rather than serialized URLs
- Counties not semicolon-delimited and alphabetized
- Parent Trail Network invalid or not a recognized Trail Network Name
- Trail ID missing or non-integer
- Field order incorrect
- Field missing
- Field duplicated

All errors must be logged in the Audit & Logging Module v5.0.

---

## 12. INTEGRATION WITH TSV INTEGRITY CHECK v5.0

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank-field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement and freshness (not pre-stored)
- Validate Maps serialization (URL list, no raw objects)
- Revalidate Counties formatting (semicolon-delimited, alphabetized)
- Validate Parent Trail Network references
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free Trail TSV output.

---

## 13. SCHEMA DISCREPANCY NOTE

The Trail Schema Module v5.0 header states "19 FIELDS" but lists 18 named fields (Trail Name through Derived Label). The 19th field — Trail ID — is documented in the schema's relationship section but was omitted from the numbered field list. This TSV spec treats Trail ID as the canonical 20th field (with Derived Label as field 18 and Parent Trail Network as field 19, per v4.0 pattern). The Trail Schema should be updated to add Trail ID explicitly to the numbered field list and correct the count to 20.

---

## 14. MODULE DEPENDENCIES

This module depends on:

- Trail Schema Module v5.0
- Trail Vocabulary Module v5.0
- Trail Normalization Contract v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF TRAIL TSV OUTPUT SPECIFICATION v5.0
