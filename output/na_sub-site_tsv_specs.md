# NATURAL AREAS PROJECT — SUB‑SITE TSV OUTPUT SPECIFICATION v3.1
A deterministic, formatting‑layer specification defining exactly how Sub‑Site
records are serialized into tab‑separated values (TSV) with guaranteed delimiter
integrity, zero drift, and full compatibility with the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Sub‑Site Vocabulary Module v3.1.
All field definitions are defined in the Sub‑Site Schema Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical v3.1 Sub‑Site TSV field order
- Delimiter rules
- Blank‑field rules
- Whitespace rules
- Derived Label placement rules
- Parent Site placement rules
- Multi‑county expansion rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check and Audit & Logging Module
- Integration with the v3.1 Processing / Orchestration Module

This specification is authoritative for Sub‑Site TSV formatting.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All normalized Sub‑Site records (v3.1)
- All counties and all processing runs
- All automated or manual TSV exports
- All Sub‑Site normalization workflows
- All multi‑entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank‑field representation
- Derived Label placement
- Parent Site placement
- Multi‑county record expansion
- Validation requirements

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.1)

TSV output must contain exactly **14 fields** in the following order:

1. Sub‑Site Name  
2. Sub‑Site Type  
3. Parent Site  
4. Description  
5. County  
6. GPS Coordinates  
7. Plus Code  
8. URL  
9. Map Link  
10. Notes  
11. Source Confidence  
12. Verification Status  
13. Derived Label  
14. Parent Site (Redundant for TSV integrity; must match field 3)

This order is absolute and must never change.

------------------------------------------------------------
# 4. MULTI‑COUNTY EXPANSION RULES (v3.1)

If a Sub‑Site spans multiple counties:

- One TSV row must be emitted **per county**.
- All fields except County remain identical.
- County field must contain exactly one county per row.
- Rows must be emitted in alphabetical county order.

Each row must independently satisfy all delimiter‑integrity rules.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).
- No spaces may appear before or after tabs.
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **13 tab characters**
- 14 fields → 13 delimiters
- No more, no fewer

## 5.3 No field may contain a tab character
If a tab is detected inside a field, TSV generation must halt and surface an error.

## 5.4 No field may contain newline characters
If present, TSV generation must halt and surface an error.

------------------------------------------------------------
# 6. BLANK‑FIELD RULES

## 6.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

## 6.2 No spaces inside blank fields
Invalid examples:

- `\t \t`
- `\t  \t`
- `\t\t `
- ` \t\t`

## 6.3 No placeholder values
Invalid:

- `_`
- `NULL`
- `""`
- `BLANK`

## 6.4 No collapsing of adjacent blanks
Adjacent blanks must remain:

`\t\t`

Never:

- `\t`
- `\t \t`

------------------------------------------------------------
# 7. WHITESPACE RULES

## 7.1 No leading or trailing spaces in any field
Invalid:

- `" Preserve Unit"`
- `"Preserve Unit "`
- `" Preserve Unit "`

## 7.2 No trailing spaces at end of line
Lines must end immediately after the final Parent Site field.

## 7.3 Internal spaces allowed only when part of the field value
Valid:

- `"Old Growth Forest"`

Invalid:

- `"  Old Growth Forest"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v3.1)

## 8.1 Derived Label is always field 13
It must appear in the 13th column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Sub‑Site Type + " Sub‑Site"**

## 8.3 Formatting rules
- No parentheses
- No trailing punctuation
- No additional descriptors

Invalid:

- `"Preserve Unit Sub‑Site (North)"`
- `"Historic Area Sub‑Site,"`

------------------------------------------------------------
# 9. PARENT SITE RULES (v3.1)

## 9.1 Parent Site appears in fields 3 and 14
- Field 3: Parent Site (semantic)
- Field 14: Parent Site (TSV integrity anchor)

## 9.2 Both fields must match exactly
No abbreviations, no synonyms.

## 9.3 Parent Site must be a valid normalized Site
If not, TSV generation halts.

## 9.4 Parent Site must be blank only if the Sub‑Site is invalid
Valid Sub‑Sites always have exactly one parent.

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **14 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **13 tabs**
This is the primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
If a field is unknown, it must be represented as a blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county expansion must occur **before** delimiter validation
Each expanded row must independently pass all checks.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM (DETERMINISTIC, v3.1)

**Step 1 — Receive normalized 14‑field Sub‑Site record**  
**Step 2 — Expand into multiple rows if multi‑county**  
**Step 3 — Compute Derived Label for each row**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 13)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 13 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Derived Label is malformed
- Parent Site is misaligned
- Field order is incorrect
- A field is missing
- A field is duplicated
- Multi‑county expansion fails

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK (v3.1)

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank‑field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement
- Revalidate Parent Site placement
- Revalidate multi‑county expansion
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift‑free output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- **Sub‑Site Schema Module v3.1**
- **Sub‑Site Vocabulary Module v3.1**
- **Sub‑Site Normalization Contract v3.1**
- **TSV Integrity Check Module v3.1**
- **Audit & Logging Module v1.1**
- **Processing / Orchestration Module v3.1**

------------------------------------------------------------
# END OF SUB‑SITE TSV OUTPUT SPECIFICATION v3.1