# NATURAL AREAS PROJECT — TSV INTEGRITY CHECK MODULE v3.1
A deterministic validation module ensuring that all TSV output for all seven
entity types meets strict delimiter‑integrity, blank‑field, whitespace, and
field‑alignment requirements before finalization.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How TSV rows are validated
- How delimiter counts are checked
- How blank fields must be represented
- How whitespace rules are enforced
- How field alignment is validated for each entity type
- How anomalies are surfaced
- How failures halt finalization
- How results integrate with the Audit & Logging Module v1.1
- How results integrate with the Processing / Orchestration Module v3.1

This module ensures:

- Zero delimiter drift
- Zero misalignment
- Zero silent formatting errors
- Deterministic, reproducible TSV output
- Full compatibility with the v3.1 ontology

------------------------------------------------------------
# 2. SCOPE

This module applies to **all seven TSV output types**:

- **Site** (25 fields, 24 delimiters)
- **Sub‑Site** (14 fields, 13 delimiters)
- **Access Point** (11 fields, 10 delimiters)
- **Trail** (16 fields, 15 delimiters)
- **Trail Segment** (15 fields, 14 delimiters)
- **Trail Network** (12 fields, 11 delimiters)
- **Site Network** (12 fields, 11 delimiters)

It governs:

- Delimiter rules
- Blank‑field rules
- Whitespace rules
- Field‑position rules
- Integrity‑anchor rules
- Multi‑county expansion validation
- Error surfacing

------------------------------------------------------------
# 3. DELIMITER REQUIREMENTS (ENTITY‑SPECIFIC)

Each TSV row must contain **exactly** the following number of tab characters:

- **Site**: 24 tabs
- **Sub‑Site**: 13 tabs
- **Access Point**: 10 tabs
- **Trail**: 15 tabs
- **Trail Segment**: 14 tabs
- **Trail Network**: 11 tabs
- **Site Network**: 11 tabs

No more, no fewer.

## 3.1 No internal tabs
If a field contains a tab, the row fails integrity.

## 3.2 No newline characters
If a field contains a newline, the row fails integrity.

------------------------------------------------------------
# 4. BLANK‑FIELD REQUIREMENTS

## 4.1 Blank fields must be true blanks
Represented as:

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

## 4.4 No collapsed blanks
Adjacent blanks must remain `\t\t`.

------------------------------------------------------------
# 5. WHITESPACE REQUIREMENTS

## 5.1 No leading or trailing spaces in any field
Invalid:

- `" Park"`
- `"Park "`
- `" Park "`  

## 5.2 No trailing spaces at end of line
Line must end immediately after the final field.

## 5.3 Internal spaces allowed only when part of the value
Valid:

- `"Ohio History Connection"`

Invalid:

- `"  Ohio History Connection"`

------------------------------------------------------------
# 6. FIELD‑POSITION REQUIREMENTS (ENTITY‑SPECIFIC)

The following fields must appear in the exact positions defined in the v3.1 TSV
Output Specifications.

## 6.1 Site (25 fields)
- Derived Label → field 24
- Parent Site → field 25

## 6.2 Sub‑Site (14 fields)
- Derived Label → field 13
- Parent Site (integrity anchor) → field 14

## 6.3 Access Point (11 fields)
- Derived Label → field 11
- Parent Site → field 3

## 6.4 Trail (16 fields)
- Derived Label → field 15
- Trail Name (integrity anchor) → field 16

## 6.5 Trail Segment (15 fields)
- Derived Label → field 14
- Parent Trail (integrity anchor) → field 15

## 6.6 Trail Network (12 fields)
- Derived Label → field 11
- Network Name (integrity anchor) → field 12

## 6.7 Site Network (12 fields)
- Derived Label → field 11
- Network Name (integrity anchor) → field 12

If any field is out of position, the row fails integrity.

------------------------------------------------------------
# 7. MULTI‑COUNTY EXPANSION VALIDATION

For all entities that support multi‑county expansion:

- Each row must contain **exactly one county**.
- Rows must be emitted in alphabetical county order.
- All non‑county fields must remain identical across expanded rows.

Entities supporting multi‑county expansion:

- Site
- Sub‑Site
- Access Point
- Trail
- Trail Segment
- Trail Network
- Site Network

Failure to meet these rules results in an integrity failure.

------------------------------------------------------------
# 8. VALIDATION ALGORITHM (DETERMINISTIC)

### Step 1 — Identify entity type  
Based on expected delimiter count.

### Step 2 — Count delimiters  
Must match the entity’s required count.

### Step 3 — Validate blank‑field representation  
All blanks must be true blanks.

### Step 4 — Validate no internal tabs  
### Step 5 — Validate no internal newlines  
### Step 6 — Validate field alignment  
### Step 7 — Validate whitespace rules  
### Step 8 — Validate integrity‑anchor fields  
### Step 9 — Validate multi‑county expansion (if applicable)  
### Step 10 — Surface anomalies  
### Step 11 — Halt finalization if any row fails  

If any step fails, TSV generation must not proceed.

------------------------------------------------------------
# 9. ERROR CONDITIONS

A row fails integrity if:

- Delimiter count is incorrect
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Derived Label is misaligned
- Integrity‑anchor field is misaligned
- Parent Site / Parent Trail / Parent Network is misaligned
- Any field is missing
- Any field is duplicated
- Any field is out of order
- Multi‑county expansion is invalid

All failures must be logged in the Audit & Logging Module v1.1.

------------------------------------------------------------
# 10. OUTPUT OF THIS MODULE

For each row:

- Pass / Fail
- Expected delimiter count
- Actual delimiter count
- List of anomalies (if any)
- Whether the pipeline halted

This output is consumed by:

- Processing / Orchestration Module v3.1
- Audit & Logging Module v1.1

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **All seven TSV Output Specifications v3.1**
- **Processing / Orchestration Module v3.1**
- **Audit & Logging Module v1.1**

------------------------------------------------------------
# END OF TSV INTEGRITY CHECK MODULE v3.1