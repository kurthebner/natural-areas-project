# NATURAL AREAS PROJECT  
# TSV INTEGRITY CHECK MODULE v4.0  
Authoritative, deterministic validation module ensuring that all TSV output for  
all six entity types meets strict delimiter‑integrity, blank‑field, whitespace,  
field‑alignment, identity‑anchor, and multi‑county/state representation rules  
before finalization.

This module contains no controlled vocabularies.  
All vocabularies are defined in the respective Vocabulary Modules v4.0.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How TSV rows are validated  
- How delimiter counts are checked  
- How blank fields must be represented  
- How whitespace rules are enforced  
- How field alignment is validated for each entity type  
- How identity‑anchor fields are validated  
- How parent‑entity fields are validated  
- How **multi‑county and multi‑state representation** is validated  
- How anomalies are surfaced  
- How failures halt finalization  
- How results integrate with the Audit & Logging Module v4.0  
- How results integrate with the Processing / Orchestration Module v4.0  

This module ensures:

- Zero delimiter drift  
- Zero misalignment  
- Zero silent formatting errors  
- Deterministic, reproducible TSV output  
- Full compatibility with the v4.0 ontology  

------------------------------------------------------------
# 2. SCOPE

This module applies to **all six TSV output types**:

- **Site** (22 fields, 21 delimiters)  
- **Access Point** (13 fields, 12 delimiters)  
- **Trail** (18 fields, 17 delimiters)  
- **Trail Segment** (14 fields, 13 delimiters)  
- **Trail Network** (13 fields, 12 delimiters)  
- **Site Network** (15 fields, 14 delimiters)  

It governs:

- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Field‑position rules  
- Identity‑anchor rules  
- Parent‑entity rules  
- **Multi‑county and multi‑state representation validation**  
- Error surfacing  

------------------------------------------------------------
# 3. DELIMITER REQUIREMENTS (ENTITY‑SPECIFIC)

Each TSV row must contain **exactly** the following number of tab characters:

- **Site**: 21 tabs  
- **Access Point**: 12 tabs  
- **Trail**: 17 tabs  
- **Trail Segment**: 13 tabs  
- **Trail Network**: 12 tabs  
- **Site Network**: 14 tabs  

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
Valid: `"Ohio History Connection"`  
Invalid: `"  Ohio History Connection"`

------------------------------------------------------------
# 6. FIELD‑POSITION REQUIREMENTS (ENTITY‑SPECIFIC)

The following fields must appear in the exact positions defined in the  
v4.0 TSV Output Specifications.

## 6.1 Site (22 fields)
- Derived Label → field 21  
- Parent Site → field 22  

## 6.2 Access Point (13 fields)
- Derived Label → field 13  
- Parent Entities → field 3  

## 6.3 Trail (18 fields)
- Derived Label → field 17  
- Trail Name (identity anchor) → field 1  

## 6.4 Trail Segment (14 fields)
- Derived Label → field 13  
- Parent Trail (identity anchor) → field 1  

## 6.5 Trail Network (13 fields)
- Derived Label → field 13  
- Network Name (identity anchor) → field 1  

## 6.6 Site Network (15 fields)
- Derived Label → field 15  
- Network Name (identity anchor) → field 1  

If any field is out of position, the row fails integrity.

------------------------------------------------------------
# 7. MULTI‑COUNTY AND MULTI‑STATE REPRESENTATION VALIDATION

### Universal rule (v4.0):
**All entities are single‑row entities.  
No entity expands into multiple rows.**

### For all six entities:

- County / Counties / Counties Included fields must contain a  
  **semicolon‑delimited, alphabetized list** of counties.  
- State / States Included fields must contain a  
  **semicolon‑delimited, alphabetized list** of states (if applicable).  
- No row may contain more than one TSV record for the same entity.  
- No entity may emit multiple rows based on counties or states.  
- No county or state may appear twice.  
- No trailing semicolons.  
- No spaces around semicolons.

### A row fails integrity if:

- A county list is not alphabetized  
- A county list is not semicolon‑delimited  
- A state list is not semicolon‑delimited  
- A state list is not alphabetized  
- Any entity attempts multi‑row expansion  

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
### Step 8 — Validate identity‑anchor fields  
### Step 9 — Validate parent‑entity fields  
### Step 10 — Validate multi‑county and multi‑state representation  
### Step 11 — Surface anomalies  
### Step 12 — Halt finalization if any row fails  

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
- Identity‑anchor field is misaligned  
- Parent Site / Parent Trail / Parent Network is misaligned  
- Any field is missing  
- Any field is duplicated  
- Any field is out of order  
- **County or State fields are not semicolon‑delimited, alphabetized lists**  
- **Any entity attempts multi‑row expansion**  

All failures must be logged in the Audit & Logging Module v4.0.

------------------------------------------------------------
# 10. OUTPUT OF THIS MODULE

For each row:

- Pass / Fail  
- Expected delimiter count  
- Actual delimiter count  
- List of anomalies (if any)  
- Whether the pipeline halted  

This output is consumed by:

- Processing / Orchestration Module v4.0  
- Audit & Logging Module v4.0  

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **All six TSV Output Specifications v4.0**  
- **Processing / Orchestration Module v4.0**  
- **Audit & Logging Module v4.0**  

------------------------------------------------------------
# END OF TSV INTEGRITY CHECK MODULE v4.0