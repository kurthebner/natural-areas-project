# NATURAL AREAS PROJECT — TRAIL NETWORK TSV OUTPUT SPECIFICATION v4.0
Authoritative, deterministic formatting‑layer specification defining exactly how  
Trail Network records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Network Vocabulary Module v4.0**.  
All field definitions are defined in the **Trail Network Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical TSV field order for Trail Networks  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- **Multi‑county and multi‑state representation rules**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module v4.0  
- Integration with the Processing / Orchestration Module v4.0  

This specification is authoritative for **Trail Network TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **Normalized Trail Network Entities v4.0**  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All Trail Network normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- **Multi‑county and multi‑state representation**  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v4.0)

Trail Network TSV output must contain exactly **13 fields** in the following order:

1. Trail Network Name  
2. Alternate Names  
3. Network Type  
4. Description  
5. History  
6. **Counties Traversed**  
7. States Included  
8. Primary Managing Agency  
9. Secondary Managing Agencies  
10. URL  
11. Map URL  
12. Notes  
13. Derived Label  

This order is absolute and must never change.  
No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY AND MULTI‑STATE REPRESENTATION RULES (v4.0)

Trail Networks are **not expanded** into multiple TSV rows.

If a Trail Network spans multiple counties:

- The **Counties Traversed** field must contain a **semicolon‑delimited, alphabetized list** of all counties.  
- The field must not include the word “County”.  
- The Trail Network must appear as **a single TSV row**, regardless of how many counties it spans.  

If a Trail Network spans multiple states:

- The **States Included** field must contain a **semicolon‑delimited, alphabetized list** of all states.  
- State abbreviations or full names must follow the normalization contract.  

Example:

- Counties Traversed: `Delaware;Franklin;Union`  
- States Included: `Ohio;Pennsylvania`  

Multi‑county and multi‑state logic is handled at the **Trail Network level**, not by row expansion.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **12 tab characters**
- 13 fields → 12 delimiters  
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

- `" Greenway System"`  
- `"Greenway System "`  
- `" Greenway System "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Derived Label** field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"Ohio to Erie Trail System"`  
Invalid: `"  Ohio to Erie Trail System"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v4.0)

## 8.1 Derived Label is always field 13
It must appear in the final column.

## 8.2 Derived Label is computed during normalization, not TSV output
Derived Label (v4.0) is defined in the **Trail Network Normalization Contract v4.0**.  
TSV output must not modify or recompute Derived Label.

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match the normalized Derived Label exactly  

Invalid:

- `"Regional Greenway System — Metro Parks (Main)"`  
- `"Water Trail Network — ODNR,"`

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

## 9.1 Each row must contain exactly **13 fields**
No more, no fewer.

## 9.2 Each row must contain exactly **12 tabs**
Primary delimiter‑integrity invariant.

## 9.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 9.4 No field may be duplicated
Each field appears exactly once.

## 9.5 Multi‑county and multi‑state Trail Networks remain single rows
- **Counties Traversed** is a semicolon‑delimited, alphabetized list.  
- **States Included** is a semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Trail Networks.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 13‑field Trail Network entity**  
**Step 2 — Validate Counties Traversed as semicolon‑delimited, alphabetized**  
**Step 3 — Validate States Included as semicolon‑delimited, alphabetized**  
**Step 4 — Validate Derived Label (already computed)**  
**Step 5 — Validate no internal tabs**  
**Step 6 — Validate no internal newlines**  
**Step 7 — Validate whitespace rules**  
**Step 8 — Join fields with tab characters**  
**Step 9 — Validate delimiter count (must be 12)**  
**Step 10 — Validate blank‑field representation**  
**Step 11 — Emit row**  

If any step fails, TSV generation must halt and surface an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 12 tabs  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label malformed or missing  
- Field order incorrect  
- Field missing  
- Field duplicated  
- **Counties Traversed incorrectly formatted (not semicolon‑delimited, not alphabetized)**  
- **States Included incorrectly formatted (not semicolon‑delimited, not alphabetized)**  

All errors must be logged in the Audit & Logging Module v4.0.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK v4.0

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- **Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
- **Validate States Included formatting (semicolon‑delimited, alphabetized)**  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the Integrity Check guarantee drift‑free Trail Network TSV output.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- **Trail Network Schema Module v4.0**  
- **Trail Network Vocabulary Module v4.0**  
- **Trail Network Normalization Contract v4.0**  
- **TSV Integrity Check Module v4.0**  
- **Audit & Logging Module v4.0**  
- **Processing / Orchestration Module v4.0**  

------------------------------------------------------------
# END OF TRAIL NETWORK TSV OUTPUT SPECIFICATION v4.0