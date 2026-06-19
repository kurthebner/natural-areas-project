# NATURAL AREAS PROJECT — TRAIL SEGMENT TSV OUTPUT SPECIFICATION v5.0
Authoritative, deterministic formatting-layer specification defining exactly how
**Normalized Trail Segment Entities v5.0** are serialized into tab-separated values (TSV)
with guaranteed delimiter integrity, zero drift, and full compatibility with the
v5.0 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the **Trail Segment Vocabulary Module v5.0**.
All field definitions are defined in the **Trail Segment Schema Module v5.0**.

---

## v5.0 Changes from v4.0

- `managing_agency` → `governance` (renamed)
- `county_list` → `counties` (renamed; still semicolon-delimited, alphabetized)
- `map_url` → `maps` serialized as semicolon-delimited URL list
- `segment_role` removed from schema and vocabulary
- `difficulty` and `accessibility` added as new fields
- `segment_type` added (replaces segment_role with a cleaner vocabulary)
- `geometry` retained (WKT / GeoJSON LineString; populated in GIS phase)
- **Derived Label** now computed at TSV output time, NOT during normalization (changed from v4.0)
- Segment ID added as final field for referential integrity
- Field count: 14 → 18

---

## 1. PURPOSE

This module defines:

- The canonical TSV field order for Trail Segments (v5.0)
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Derived Label computation rules (TSV output time only)
- Maps field serialization rules
- Multi-county representation rules
- Parent Trail placement rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v5.0

This specification is authoritative for **Trail Segment TSV formatting**.

---

## 2. SCOPE

This specification applies to:

- All **Normalized Trail Segment Entities v5.0**
- All counties and all processing runs
- All automated or manual TSV exports
- All Trail Segment normalization workflows
- All multi-entity orchestration pipelines

---

## 3. FIELD ORDER (AUTHORITATIVE, v5.0)

Trail Segment TSV output must contain exactly **18 fields** in the following order:

1. Parent Trail
2. Segment Name
3. Counties
4. Governance
5. Segment Length (Miles)
6. Surface Type
7. Segment Type
8. Status
9. Difficulty
10. Accessibility
11. Description
12. Notes
13. URL
14. Maps
15. Geometry
16. Derived Label
17. Parent Trail Network
18. Segment ID

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

---

## 4. FIELD NOTES

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

### Field 4 — Governance
- Primary agency or organization responsible for this specific segment
- Must not be inferred from the parent Trail's governance
- Semicolon-delimited if multiple

### Field 7 — Segment Type
- Optional; must match a valid value from Trail Segment Vocabulary Module v5.0
- Allowed values: Linear, Loop, Connector, Spur, Crossing, Access Segment
- Most segments are Linear — only populate when explicitly documented or clearly distinct
- Blank if not documented

### Field 9 — Difficulty
- Optional; must match a valid value from Trail Segment Vocabulary Module v5.0
- Blank if not explicitly documented by an authoritative source
- Must never be assessed or inferred
- May differ from the parent Trail's overall difficulty

### Field 10 — Accessibility
- Free-text description of ADA compliance, wheelchair accessibility, grade, width, accessible facilities
- Blank if not documented
- May differ from the parent Trail's overall accessibility

### Field 14 — Maps
- Serialized from the `maps` array in the normalized entity
- In TSV: semicolon-delimited list of URLs only — type and description metadata are dropped
- Blank if no maps documented
- Example: `https://wcparks.org/trail-segment-map.pdf;https://www.example.com/trail/`

### Field 15 — Geometry
- WKT LineString or GeoJSON LineString stored as text
- Populated in GIS phase — expected to be blank for most segments during initial web discovery
- Must be authoritative; no inferred or smoothed geometry

### Field 16 — Derived Label
- Computed at TSV output time from normalized fields
- Must not be pre-stored in the normalized entity
- Deterministic: the same normalized input always produces the same Derived Label
- Must be regenerated whenever any component field changes
- No parentheses, no trailing punctuation, no invented descriptors

### Field 17 — Parent Trail Network
- Optional; identifies the Trail Network the parent Trail belongs to
- Must match the exact Name of a valid Trail Network entity
- Inherited from the parent Trail relationship — not stored independently on the segment
- Blank if parent Trail has no Trail Network membership

### Field 18 — Segment ID
- Internal entity ID
- Required for referential integrity and downstream processing
- Must be a valid integer matching the entity's `segment_id`

---

## 5. MULTI-COUNTY REPRESENTATION RULES (v5.0)

Trail Segments are **not expanded** into multiple TSV rows.

If a Trail Segment spans multiple counties:

- The **Counties** field must contain a **semicolon-delimited, alphabetized list**.
- The field must not include the word "County".
- The Trail Segment must appear as **a single TSV row**, regardless of how many counties it spans.
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

### 6.2 Each row must contain exactly **17 tab characters**
- 18 fields → 17 delimiters
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
Invalid: `" North Section"`, `"North Section "`, `" North Section "`

### 8.2 No trailing spaces at end of line
Lines must end immediately after the **Segment ID** field.

### 8.3 Internal spaces allowed only when part of the value
Valid: `"North Loop Section"`
Invalid: `"  North Loop Section"`

---

## 9. ROW CONSTRUCTION RULES

### 9.1 Each row must contain exactly **18 fields**
No more, no fewer.

### 9.2 Each row must contain exactly **17 tabs**
Primary delimiter-integrity invariant.

### 9.3 No field may be omitted
Unknown or inapplicable fields → blank field (`\t\t`).

### 9.4 No field may be duplicated
Each field appears exactly once.

### 9.5 Multi-county Trail Segments remain single rows
- Counties field contains semicolon-delimited, alphabetized list.
- No row expansion occurs for Trail Segments.

---

## 10. TSV GENERATION ALGORITHM (v5.0)

**Step 1 — Receive normalized 18-field Trail Segment entity (excluding Derived Label)**
**Step 2 — Compute Derived Label from normalized fields**
**Step 3 — Serialize Maps array to semicolon-delimited URL list**
**Step 4 — Validate Parent Trail (valid Trail Name; must not be blank)**
**Step 5 — Validate Counties formatting (semicolon-delimited, alphabetized)**
**Step 6 — Validate Parent Trail Network (valid Trail Network Name or blank)**
**Step 7 — Validate no internal tabs**
**Step 8 — Validate no internal newlines**
**Step 9 — Validate whitespace rules**
**Step 10 — Join fields with tab characters**
**Step 11 — Validate delimiter count (must be 17)**
**Step 12 — Validate blank-field representation**
**Step 13 — Emit row**

If any step fails, TSV generation must halt and surface an error.

---

## 11. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 17 tabs
- Field contains a tab
- Field contains a newline
- Blank field contains spaces
- Field contains trailing spaces
- Parent Trail is blank or does not match a valid Trail Name
- Derived Label malformed, missing, or pre-stored (not computed at output time)
- Maps field contains raw objects rather than serialized URLs
- Counties not semicolon-delimited and alphabetized
- Parent Trail Network invalid or not a recognized Trail Network Name
- Segment ID missing or non-integer
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
- Revalidate Parent Trail placement (non-blank, valid Trail Name)
- Revalidate Counties formatting (semicolon-delimited, alphabetized)
- Validate Parent Trail Network references
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift-free Trail Segment TSV output.

---

## 13. SCHEMA DISCREPANCY NOTE

The Trail Segment Schema Module v5.0 header states "17 FIELDS" but lists 16 named fields (Parent Trail through Derived Label). The 17th field — Segment ID — is referenced in the schema's relationship section but was omitted from the numbered field list. Additionally, a Parent Trail Network field (field 17 in this spec) was added to the TSV output layer to maintain network traceability from segments, following the v4.0 pattern. This brings the total to 18 TSV output fields. The Trail Segment Schema should be updated to add Segment ID explicitly to the numbered field list and correct the count accordingly.

---

## 14. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Schema Module v5.0
- Trail Segment Vocabulary Module v5.0
- Trail Segment Normalization Contract v5.0
- TSV Integrity Check Module v5.0
- Audit & Logging Module v5.0
- Processing / Orchestration Module v5.0

---

# END OF TRAIL SEGMENT TSV OUTPUT SPECIFICATION v5.0
