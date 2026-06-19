# NATURAL AREAS PROJECT
# TSV INTEGRITY CHECK MODULE v5.1
Authoritative, deterministic validation module ensuring that all TSV output for
all six entity types meets strict delimiter-integrity, blank-field, whitespace,
field-alignment, identity-anchor, and multi-county representation rules before
finalization.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v5.x.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- Updated module version to v5.1.
- Updated all cross-module references to v5.x.
- Updated Site field count from 26 to 25 (TSV Site v5.x removed Derived Label).
- Updated Site delimiter count from 25 tabs to 24 tabs.
- Updated Section 6.1 Site field positions to match TSV Site v5.x canonical order.
- Added plus_code (Field 18) to Site field-position anchor list.
- Removed Derived Label from Site anchor list (no longer a Site TSV field).
- Note: Access Point, Trail, Trail Segment, Trail Network, and Site Network
  field positions in Section 6.2–6.6 are carried forward from v5.0 and should
  be verified against their respective updated TSV Output Specifications.

------------------------------------------------------------
# CHANGES FROM v4.0

- Field counts updated for all six entity types to reflect v5.x schema changes:
  - Site: 22 → 26 fields (added municipality, township, features, gps split)
  - Access Point: 13 → 18 fields (added features, gps split, removed role/access_level)
  - Trail: 18 → 20 fields (added difficulty, accessibility)
  - Trail Segment: 14 → 18 fields (added difficulty, accessibility, gps split)
  - Trail Network: 13 → 17 fields (added maps, ownership, operator)
  - Site Network: 15 → 15 fields (unchanged)
- Multi-state validation simplified — county list is the standard; state list applies only when entities cross state lines
- All version references updated to v5.0

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
- How anomalies are surfaced
- How failures halt finalization
- How results integrate with the Audit & Logging Module v5.x

This module ensures:

- Zero delimiter drift
- Zero misalignment
- Zero silent formatting errors
- Deterministic, reproducible TSV output
- Full compatibility with the v5.x ontology

------------------------------------------------------------
# 2. SCOPE

This module applies to **all six TSV output types**:

- **Site** (25 fields, 24 delimiters)
- **Access Point** (18 fields, 17 delimiters)
- **Trail** (20 fields, 19 delimiters)
- **Trail Segment** (18 fields, 17 delimiters)
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
- Error surfacing

------------------------------------------------------------
# 3. DELIMITER REQUIREMENTS (ENTITY-SPECIFIC)

Each TSV row must contain **exactly** the following number of tab characters:

- **Site**: 24 tabs
- **Access Point**: 17 tabs
- **Trail**: 19 tabs
- **Trail Segment**: 17 tabs
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

## 6.2 Access Point (18 fields)
- Access Point Name (identity anchor) → Field 1
- Identity Parent Entity Type → Field 4
- Identity Parent Entity Name → Field 5
- GPS Lat → Field 8
- GPS Lon → Field 9
- Features → Field 16
- Derived Label → Field 17
- Access Point ID → Field 18

## 6.3 Trail (20 fields)
- Trail Name (identity anchor) → Field 1
- County → Field 3
- Difficulty → Field 10
- Accessibility → Field 11
- Derived Label → Field 19
- Trail ID → Field 20

## 6.4 Trail Segment (18 fields)
- Parent Trail (identity anchor) → Field 1
- Segment Name → Field 2
- County → Field 3
- Difficulty → Field 10
- Accessibility → Field 11
- GPS Lat → Field 12
- GPS Lon → Field 13
- Derived Label → Field 17
- Trail Segment ID → Field 18

## 6.5 Trail Network (17 fields)
- Network Name (identity anchor) → Field 1
- County → Field 3
- Derived Label → Field 16
- Trail Network ID → Field 17

## 6.6 Site Network (15 fields)
- Network Name (identity anchor) → Field 1
- County → Field 3
- Derived Label → Field 14
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

### Step 11 — Surface anomalies
Collect all failures found in Steps 1–10.

### Step 12 — Halt finalization if any row fails
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
- Derived Label is misaligned
- Identity-anchor field is misaligned or blank
- Parent Site / Parent Trail is misaligned
- Identity Parent Entity Type or Name is misaligned (Access Points)
- GPS Lat or GPS Lon is misaligned
- Features field is misaligned (Sites, Access Points)
- Difficulty or Accessibility field is misaligned (Trails, Trail Segments)
- Any field is missing
- Any field is duplicated
- Any field is out of order
- **County field is not a semicolon-delimited, alphabetized list**
- **Any entity attempts multi-row expansion**

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
- **Normalization Engine v5.x**
- **Audit & Logging Module v5.x**

------------------------------------------------------------
# END OF TSV INTEGRITY CHECK MODULE v5.1
