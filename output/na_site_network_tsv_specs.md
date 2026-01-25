# NATURAL AREAS PROJECT — SITE NETWORK TSV OUTPUT SPECIFICATION v4.0
Authoritative, deterministic formatting‑layer specification defining exactly how  
Site Network records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Network Vocabulary Module v4.0**.  
All field definitions are defined in the **Site Network Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical TSV field order for Site Networks  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- **Multi‑county and multi‑state representation rules**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module v4.0  
- Integration with the Processing / Orchestration Module v4.0  

This specification is authoritative for **Site Network TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **normalized Site Network records** (v4.0)  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All Site Network normalization workflows  
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

Site Network TSV output must contain exactly **15 fields** in the following order:

1. Network Name  
2. Alternate Names  
3. Network Type  
4. Status  
5. Counties Traversed  
6. States Included  
7. Primary Managing Agency  
8. Secondary Managing Agencies  
9. Network Affiliation  
10. Description  
11. History  
12. URL  
13. Map URL  
14. Notes  
15. Derived Label  

This order is absolute and must never change.

No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY AND MULTI‑STATE REPRESENTATION RULES (v4.0)

Site Networks are **not expanded** into multiple TSV rows.

If a Site Network spans multiple counties:

- The **Counties Traversed** field must contain a **semicolon‑delimited, alphabetized list** of all counties.  
- The field must not include the word “County”.  
- The Site Network must appear as **a single TSV row**, regardless of how many counties it spans.  
- Must follow the **universal multi‑county rule v4.0**.

If a Site Network spans multiple states:

- The **States Included** field must contain a **semicolon‑delimited, alphabetized list** of all states.  
- State names or abbreviations must follow the normalization contract.  

Example:

- Counties Traversed: `Delaware;Franklin;Union`  
- States Included: `Ohio;Pennsylvania`  

Multi‑county and multi‑state logic is handled at the **Site Network level**, not by row expansion.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **14 tab characters**
- 15 fields → 14 delimiters  
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

- `" Heritage Corridor"`  
- `"Heritage Corridor "`  
- `" Heritage Corridor "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Derived Label** field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"National Heritage Area"`  
Invalid: `"  National Heritage Area"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES

## 8.1 Derived Label is always field 15
It must appear in the final column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label (v4.0) is defined in the **Site Network Normalization Contract v4.0**.  
The schema specifies the formula:

**Network Type + " — " + Primary Managing Agency**

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match normalized field values exactly  

Invalid:

- `"Heritage Corridor — NPS (Multi‑State)"`  
- `"Watershed Network — ODNR,"`

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

## 9.1 Each row must contain exactly **15 fields**
No more, no fewer.

## 9.2 Each row must contain exactly **14 tabs**
Primary delimiter‑integrity invariant.

## 9.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 9.4 No field may be duplicated
Each field appears exactly once.

## 9.5 Multi‑county and multi‑state Site Networks remain single rows
- **Counties Traversed** is a semicolon‑delimited, alphabetized list.  
- **States Included** is a semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Site Networks.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 15‑field Site Network record**  
**Step 2 — Normalize Counties Traversed into a semicolon‑delimited, alphabetized list**  
**Step 3 — Normalize States Included into a semicolon‑delimited, alphabetized list**  
**Step 4 — Compute Derived Label for the record**  
**Step 5 — Validate no internal tabs**  
**Step 6 — Validate no internal newlines**  
**Step 7 — Validate whitespace rules**  
**Step 8 — Validate Network Affiliation formatting**  
**Step 9 — Join fields with tab characters**  
**Step 10 — Validate delimiter count (must be 14)**  
**Step 11 — Validate blank‑field representation**  
**Step 12 — Emit row**  

If any step fails, TSV generation must halt and surface an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 14 tabs  
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
# 12. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- **Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
- **Validate States Included formatting (semicolon‑delimited, alphabetized)**  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the Integrity Check guarantee drift‑free Site Network TSV output.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- **Site Network Schema Module v4.0**  
- **Site Network Vocabulary Module v4.0**  
- **Site Network Normalization Contract v4.0**  
- **TSV Integrity Check Module v4.0**  
- **Audit & Logging Module v4.0**  
- **Processing / Orchestration Module v4.0**  

------------------------------------------------------------
# END OF SITE NETWORK TSV OUTPUT SPECIFICATION v4.0