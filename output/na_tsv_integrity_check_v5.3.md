# NATURAL AREAS PROJECT
# TSV INTEGRITY CHECK MODULE v5.3
Authoritative, deterministic validation module ensuring that all TSV output for
all six entity types meets strict delimiter-integrity, blank-field, whitespace,
field-alignment, identity-anchor, multi-county representation, and provenance
exclusion rules before finalization.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.x.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-030**: New §8 Step 11 — Provenance field exclusion check. No field from
  any provenance table (`discovery_provenance`, `resolution_provenance`,
  `normalization_provenance`, `run_metadata`) may appear in an entity TSV column
  set. The column set must match the canonical field list for the entity type exactly.
  If a TSV includes a header row, every column name is validated against the
  canonical list. Any field not in the canonical list is a provenance leakage error.
- **IMP-030**: §9 Error Conditions updated — added "TSV column list contains a field
  not in the canonical field list for its entity type (provenance leakage)" as an
  error condition.
- Steps renumbered: former Step 11 (Surface anomalies) → Step 12;
  former Step 12 (Halt finalization) → Step 13.
- §10 Output section updated to reference v5.3.
- §11 Module Dependencies updated to reference Normalization Engine v5.6.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- Updated module version to v5.2.
- Fully reconciled all five non-Site entity sections against their authoritative
  TSV Output Specifications v5.1. The v5.1 note that Sections 6.2–6.6 were
  "carried forward from v5.0 and should be verified" is now resolved.

**Access Point (Section 6.2):**
- Field count corrected: 18 → 17 fields; delimiter count 17 → 16 tabs.
- Removed Derived Label (no longer a field).
- Removed Map URL (merged into URL field in v5.1).
- Added Identity Notes (Field 14).
- Corrected GPS Lat position: Field 8 → Field 10.
- Corrected GPS Lon position: Field 9 → Field 11.
- Added Plus Code anchor (Field 12).
- Corrected Features position: Field 16 → Field 13.
- Corrected Access Point ID position: Field 18 → Field 17.

**Trail (Section 6.3):**
- Field count corrected: 20 → 19 fields; delimiter count 19 → 18 tabs.
- Removed Derived Label (no longer a field).
- Added Identity Notes anchor (Field 15).
- Corrected Counties position: Field 3 → Field 7 (accurate label: Counties, not County).
- Corrected Difficulty position: Field 10 (unchanged but label verified).
- Corrected Accessibility position: Field 11 (unchanged but label verified).
- Corrected Trail ID position: Field 20 → Field 19.

**Trail Segment (Section 6.4):**
- Field count corrected: 18 → 17 fields; delimiter count 17 → 16 tabs.
- Removed Derived Label (no longer a field).
- Removed GPS Lat and GPS Lon (Trail Segments do not have GPS point fields in v5.1).
- Added Identity Notes anchor (Field 12).
- Added Geometry anchor (Field 16).
- Corrected Segment ID position: Field 18 → Field 17.

**Trail Network (Section 6.5):**
- Field count: 17 fields, 16 delimiters (count unchanged; composition changed).
- Removed Derived Label (no longer a field).
- Added Identity Notes anchor (Field 13).
- Corrected Network ID position: Field 17 (unchanged but now accurate with new composition).
- County label corrected to Counties (Field 7).

**Site Network (Section 6.6):**
- Field count corrected: 15 fields, 14 delimiters (count unchanged; composition changed).
- Removed Derived Label (no longer a field).
- Added Identity Notes anchor (Field 12).
- County label corrected to Counties (Field 7).
- Network ID confirmed at Field 15.

**Section 2 (Scope) and Section 3 (Delimiter Requirements):**
- Updated Access Point: 18 fields/17 tabs → 17 fields/16 tabs.
- Updated Trail: 20 fields/19 tabs → 19 fields/18 tabs.
- Updated Trail Segment: 18 fields/17 tabs → 17 fields/16 tabs.
- Trail Network and Site Network counts confirmed correct (no change).

**Section 9 (Error Conditions):**
- Removed "Derived Label is misaligned" — Derived Label is no longer a field for any entity type.
- Added "Identity Notes is misaligned (all entity types)" as an error condition.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- Updated module version to v5.1.
- Updated all cross-module references to v5.x.
- Updated Site field count from 26 to 25 (TSV Site v5.x removed Derived Label).
- Updated Site delimiter count from 25 tabs to 24 tabs.
- Updated Section 6.1 Site field positions to match TSV Site v5.x canonical order.
- Added plus_code (Field 18) to Site field-position anchor list.
- Removed Derived Label from Site anchor list (no longer a Site TSV field).

------------------------------------------------------------
# CHANGES FROM v4.0

- Field counts updated for all six entity types to reflect v5.x schema changes
  (authoritative counts as of v5.2):
  - Site: 22 → 25 fields
  - Access Point: 13 → 17 fields
  - Trail: 18 → 19 fields
  - Trail Segment: 14 → 17 fields
  - Trail Network: 13 → 17 fields
  - Site Network: 15 → 15 fields (unchanged)
- Multi-state validation simplified — county list is the standard; state list applies only when entities cross state lines
- All version references updated to v5.x

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How TSV rows are validated
- How delimiter counts are checked
- How blank fields must be represented
- How whitespace rules are enforced
- How field alignment is validated for each entity type
- How identity-anchor fields are validated
- How parent-entity fields are validated
- How **multi-county representation** is validated
- How **provenance field exclusion** is enforced
- How anomalies are surfaced
- How failures halt finalization
- How results integrate with the Audit & Logging Module v5.x

This module ensures:

- Zero delimiter drift
- Zero misalignment
- Zero silent formatting errors
- Zero provenance field leakage
- Deterministic, reproducible TSV output
- Full compatibility with the v5.x ontology

------------------------------------------------------------
# 2. SCOPE

This module applies to **all six TSV output types**:

- **Site** (25 fields, 24 delimiters)
- **Access Point** (17 fields, 16 delimiters)
- **Trail** (19 fields, 18 delimiters)
- **Trail Segment** (17 fields, 16 delimiters)
- **Trail Network** (17 fields, 16 delimiters)
- **Site Network** (15 fields, 14 delimiters)

It governs:

- Delimiter rules
- Blank-field rules
- Whitespace rules
- Field-position rules
- Identity-anchor rules
- Parent-entity rules
- Multi-county representation validation
- Provenance field exclusion
- Error surfacing

------------------------------------------------------------
# 3. DELIMITER REQUIREMENTS (ENTITY-SPECIFIC)

Each TSV row must contain **exactly** the following number of tab characters:

- **Site**: 24 tabs
- **Access Point**: 16 tabs
- **Trail**: 18 tabs
- **Trail Segment**: 16 tabs
- **Trail Network**: 16 tabs
- **Site Network**: 14 tabs

No more, no fewer.

## 3.1 No internal tabs
If a field value contains a tab character, the row fails integrity.

## 3.2 No newline characters
If a field value contains a newline character, the row fails integrity.

------------------------------------------------------------
# 4. BLANK-FIELD REQUIREMENTS

## 4.1 Blank fields must be true blanks
Represented as adjacent tab delimiters with nothing between them:

`\t\t`

## 4.2 No spaces inside blank fields
Invalid:
- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

## 4.3 No placeholder values
Invalid:
- `_`
- `NULL`
- `""`
- `BLANK`
- `N/A`

## 4.4 No collapsed blanks
Adjacent blank fields must each remain `\t\t`. Blanks may not be collapsed or merged.

------------------------------------------------------------
# 5. WHITESPACE REQUIREMENTS

## 5.1 No leading or trailing spaces in any field
Invalid:
- `" Park"`
- `"Park "`
- `" Park "`

## 5.2 No trailing spaces at end of line
The line must end immediately after the final field value.

## 5.3 Internal spaces allowed only when part of the value
Valid: `"Ohio History Connection"`
Invalid: `"  Ohio History Connection"`

------------------------------------------------------------
# 6. FIELD-POSITION REQUIREMENTS (ENTITY-SPECIFIC)

The following anchor fields must appear in the exact positions defined in the
v5.x TSV Output Specifications.

## 6.1 Site (25 fields)
- Site Name (identity anchor) → Field 1
- Counties → Field 13
- Municipality → Field 14 (GIS-derived)
- Township → Field 15 (GIS-derived)
- GPS Lat → Field 16
- GPS Lon → Field 17
- Plus Code → Field 18 (derived from GPS)
- Features → Field 19
- Parent Site ID → Field 23

## 6.2 Access Point (17 fields)
- Access Point Name (identity anchor) → Field 1
- Identity Parent Entity Type → Field 4
- Identity Parent Entity Name → Field 5
- GPS Lat → Field 10
- GPS Lon → Field 11
- Plus Code → Field 12 (derived from GPS)
- Features → Field 13
- Identity Notes → Field 14
- Access Point ID → Field 17

## 6.3 Trail (19 fields)
- Trail Name (identity anchor) → Field 1
- Counties → Field 7
- Difficulty → Field 11
- Accessibility → Field 12
- Identity Notes → Field 15
- Trail ID → Field 19

## 6.4 Trail Segment (17 fields)
- Parent Trail (identity anchor) → Field 1
- Segment Name → Field 2
- Counties → Field 3
- Difficulty → Field 9
- Accessibility → Field 10
- Identity Notes → Field 12
- Geometry → Field 16
- Trail Segment ID → Field 17

## 6.5 Trail Network (17 fields)
- Network Name (identity anchor) → Field 1
- Counties → Field 7
- Identity Notes → Field 13
- Trail Network ID → Field 17

## 6.6 Site Network (15 fields)
- Network Name (identity anchor) → Field 1
- Counties → Field 7
- Identity Notes → Field 12
- Site Network ID → Field 15

If any anchor field is out of position, the row fails integrity.

------------------------------------------------------------
# 7. MULTI-COUNTY REPRESENTATION VALIDATION

### Universal rule (v5.x):
**All entities are single-row entities.
No entity expands into multiple rows.**

### For all six entities:

- County / Counties field must contain a **semicolon-delimited, alphabetized list** of counties.
- No row may contain more than one TSV record for the same entity.
- No entity may emit multiple rows based on county.
- No county may appear twice in the list.
- No trailing semicolons.
- No spaces around semicolons.

### A row fails integrity if:

- A county list is not alphabetized
- A county list is not semicolon-delimited
- Any entity attempts multi-row expansion
- A county appears more than once in the list
- A trailing semicolon is present
- Spaces appear around semicolons

------------------------------------------------------------
# 7a. PROVENANCE FIELD EXCLUSION

Entity TSV files must contain only the canonical fields defined in the TSV Output
Specification for each entity type. Fields from any provenance table must never
appear in entity TSVs.

**Provenance tables whose fields are prohibited in entity TSVs:**

- `discovery_provenance`
- `resolution_provenance`
- `normalization_provenance`
- `run_metadata`

**Canonical field counts (authoritative):**

- Site: 25 fields (see `na_tsv_output_site.md`)
- Access Point: 17 fields (see `na_tsv_output_access_point.md`)
- Trail: 19 fields (see `na_tsv_output_trail.md`)
- Trail Segment: 17 fields (see `na_tsv_output_trail_segment.md`)
- Trail Network: 17 fields (see `na_tsv_output_trail_network.md`)
- Site Network: 15 fields (see `na_tsv_output_site_network.md`)

**Validation rule:**
When a TSV file includes a header row, every column name in that header must match
the canonical field list for its entity type, in the canonical order. Any column
name not in the canonical list is a provenance leakage error. A TSV with more
columns than the canonical count fails regardless of whether a header is present.

------------------------------------------------------------
# 8. VALIDATION ALGORITHM (DETERMINISTIC)

### Step 1 — Identify entity type
Based on expected delimiter count.

### Step 2 — Count delimiters
Must match the entity's required count exactly.

### Step 3 — Validate blank-field representation
All blanks must be true blanks (`\t\t`).

### Step 4 — Validate no internal tabs

### Step 5 — Validate no internal newlines

### Step 6 — Validate field alignment
Check all anchor fields are in correct positions.

### Step 7 — Validate whitespace rules
No leading/trailing spaces in any field.

### Step 8 — Validate identity-anchor fields
Must be populated; must not be blank.

### Step 9 — Validate parent-entity fields
Must be populated where required by entity type.

### Step 10 — Validate multi-county representation
Semicolon-delimited, alphabetized, no duplicates, no trailing semicolons.

### Step 11 — Validate provenance field exclusion
If a header row is present, validate every column name against the canonical
field list for the entity type (§7a). If the delimiter count matches the canonical
count but a header row contains any column name not in the canonical list, the row
fails. If the delimiter count exceeds the canonical count for the entity type, the
file fails regardless of header presence. No field from any provenance table
(`discovery_provenance`, `resolution_provenance`, `normalization_provenance`,
`run_metadata`) may appear in the column set.

### Step 12 — Surface anomalies
Collect all failures found in Steps 1–11.

### Step 13 — Halt finalization if any row fails
If any step fails for any row, TSV finalization must not proceed.
All failures must be logged before halting.

------------------------------------------------------------
# 9. ERROR CONDITIONS

A row fails integrity if:

- Delimiter count is incorrect
- A field value contains a tab character
- A field value contains a newline character
- A blank field contains spaces or placeholder values
- A field has leading or trailing whitespace
- Identity Notes is misaligned (all entity types)
- Identity-anchor field is misaligned or blank
- Parent Site / Parent Trail is misaligned
- Identity Parent Entity Type or Name is misaligned (Access Points)
- GPS Lat or GPS Lon is misaligned (Sites, Access Points)
- Plus Code is misaligned (Sites, Access Points)
- Features field is misaligned (Sites, Access Points)
- Difficulty or Accessibility field is misaligned (Trails, Trail Segments)
- Geometry field is misaligned (Trail Segments)
- Any field is missing
- Any field is duplicated
- Any field is out of order
- **County field is not a semicolon-delimited, alphabetized list**
- **Any entity attempts multi-row expansion**
- **TSV column list contains a field not in the canonical field list for its entity type (provenance leakage)**

All failures must be logged in the Audit & Logging Module v5.x.

------------------------------------------------------------
# 10. OUTPUT OF THIS MODULE

For each row:

- Pass / Fail
- Expected delimiter count
- Actual delimiter count
- List of anomalies (if any)
- Whether the pipeline halted

This output is consumed by:

- Normalization Engine v5.x (pipeline halt signal)
- Audit & Logging Module v5.x

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **All six TSV Output Specifications v5.x**
- **Normalization Engine v5.6**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF TSV INTEGRITY CHECK MODULE v5.3
