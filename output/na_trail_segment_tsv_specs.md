# NATURAL AREAS PROJECT — TRAIL SEGMENT TSV OUTPUT SPECIFICATION v4.0
Authoritative, deterministic formatting‑layer specification defining exactly how  
**Normalized Trail Segment Entities v4.0** are serialized into tab‑separated values (TSV)  
with guaranteed delimiter integrity, zero drift, and full compatibility with the  
v4.0 ontology and Entity Graph Schema v4.0.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Segment Vocabulary Module v4.0**.  
All field definitions are defined in the **Trail Segment Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical TSV field order for Trail Segments (v4.0)  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Parent Trail placement rules  
- **Multi‑county representation rules (universal v4.0 rule)**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module v4.0  
- Integration with the Processing / Orchestration Module v4.0  

This specification is authoritative for **Trail Segment TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **Normalized Trail Segment Entities v4.0**  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All Trail Segment normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Parent Trail placement  
- **Multi‑county representation**  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v4.0)

Trail Segment TSV output must contain exactly **14 fields** in the following order:

1. Parent Trail  
2. Segment Name  
3. **Counties Traversed**  
4. Managing Agency  
5. Segment Length (Miles)  
6. Surface Type  
7. Status  
8. GPS Geometry  
9. Description  
10. Notes  
11. URL  
12. Map URL  
13. Derived Label  
14. Parent Trail Network  

This order is absolute and must never change.  
No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY REPRESENTATION RULES (v4.0)

Trail Segments are **not expanded** into multiple TSV rows.

If a Trail Segment spans multiple counties:

- The **Counties Traversed** field must contain a **semicolon‑delimited, alphabetized list**.  
- The field must not include the word “County”.  
- The Trail Segment must appear as **a single TSV row**, regardless of how many counties it spans.  
- No inference is permitted; only documented counties may be included.

Example:

- Normalized counties: `Delaware;Franklin;Union`  
- TSV output: `Delaware;Franklin;Union`

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **13 tab characters**
- 14 fields → 13 delimiters  
- No more, no fewer.

## 5.3 No field may contain a tab character
If detected, TSV generation must halt and surface an error.

## 5.4 No field may contain newline characters
If detected, TSV generation must halt and surface an error.

------------------------------------------------------------
# 6. BLANK‑FIELD RULES

## 6.1 Blank fields must be true blanks
Represented as:

`\t\t`

## 6.2 No spaces inside blank fields
Invalid:

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
Adjacent blanks must remain `\t\t`.

------------------------------------------------------------
# 7. WHITESPACE RULES

## 7.1 No leading or trailing spaces in any field
Invalid:

- `" North Section"`  
- `"North Section "`  
- `" North Section "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Parent Trail Network** field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"North Loop Section"`  
Invalid: `"  North Loop Section"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v4.0)

## 8.1 Derived Label is always field 13
It must appear in the 13th column.

## 8.2 Derived Label is computed during normalization (v4.0)
TSV output must not compute or modify Derived Label.

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match the normalized Derived Label exactly  

Invalid:

- `"Riverside Trail — Paved — Active (Main)"`  
- `"North Loop — Natural — Active,"`

------------------------------------------------------------
# 9. PARENT TRAIL RULES

## 9.1 Parent Trail appears only in field 1
Field 1 is authoritative.

## 9.2 Parent Trail must match the normalized Trail Name exactly
- No abbreviations  
- No synonyms  
- No inferred names  

## 9.3 Parent Trail must be a valid normalized Trail
If not, TSV generation must halt.

## 9.4 Parent Trail must never be blank
Trail Segments always have exactly one parent Trail.

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **14 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **13 tabs**
Primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county Trail Segments remain single rows
- The **Counties Traversed** field contains a semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Trail Segments.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM (v4.0)

**Step 1 — Receive normalized 14‑field Trail Segment entity**  
**Step 2 — Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
**Step 3 — Validate Derived Label (already computed)**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Validate Parent Trail and Parent Trail Network formatting**  
**Step 8 — Join fields with tab characters**  
**Step 9 — Validate delimiter count (must be 13)**  
**Step 10 — Validate blank‑field representation**  
**Step 11 — Emit row**  

If any step fails, TSV generation must halt and surface an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 13 tabs  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label malformed or missing  
- Parent Trail invalid  
- Field order incorrect  
- Field missing  
- Field duplicated  
- **Counties Traversed incorrectly formatted (not semicolon‑delimited, not alphabetized)**  

All errors must be logged in the Audit & Logging Module v4.0.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK v4.0

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Revalidate Parent Trail placement  
- **Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the Integrity Check guarantee drift‑free Trail Segment TSV output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Trail Segment Schema Module v4.0  
- Trail Segment Vocabulary Module v4.0  
- Trail Segment Normalization Contract v4.0  
- TSV Integrity Check Module v4.0  
- Audit & Logging Module v4.0  
- Processing / Orchestration Module v4.0  

------------------------------------------------------------
# END OF TRAIL SEGMENT TSV OUTPUT SPECIFICATION v4.0