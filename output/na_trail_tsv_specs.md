# NATURAL AREAS PROJECT — TRAIL TSV OUTPUT SPECIFICATION v3.2.2
Authoritative, deterministic formatting‑layer specification defining exactly how  
Trail records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v3.2.2**.  
All field definitions are defined in the **Trail Schema Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical TSV field order for Trails (v3.2.2)  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Network Affiliation and Parent Trail Network placement rules  
- **Multi‑county representation rules**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module  
- Integration with the v3.2.2 Processing / Orchestration Module  

This specification is authoritative for **Trail TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **normalized Trail records** (v3.2.2)  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All Trail normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Network Affiliation placement  
- **Multi‑county representation**  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.2.2)

Trail TSV output must contain exactly **18 fields** in the following order:

1. Trail Name  
2. Alternate Names  
3. Trail Use Type  
4. Trail Surface Type  
5. Trail Origin Type  
6. Total Length (Miles)  
7. Counties Traversed  
8. Primary Managing Agency  
9. Secondary Managing Agencies  
10. Status  
11. Description  
12. Trail History  
13. URL  
14. Map URL  
15. Notes  
16. Network Affiliation  
17. Derived Label  
18. Parent Trail Network  

This order is absolute and must never change.

No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY REPRESENTATION RULES (v3.2.2)

Trails are **not expanded** into multiple TSV rows.

If a Trail spans multiple counties:

- The **Counties Traversed** field must contain a **semicolon‑delimited, alphabetized list** of all counties.  
- The field must not include the word “County”.  
- The Trail must appear as **a single TSV row**, regardless of how many counties it traverses.

Example:

- Normalized counties: `Delaware;Franklin;Union`  
- TSV output: `Delaware;Franklin;Union`

Multi‑county logic is handled at the **Trail level**, not by row expansion.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **17 tab characters**
- 18 fields → 17 delimiters  
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

## 7.1 No leading or trailing spaces
Invalid:

- `" Trail"`  
- `"Trail "`  
- `" Trail "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Parent Trail Network** field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"North Ridge Trail"`  
Invalid: `"  North Ridge Trail"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES

## 8.1 Derived Label is always field 17
It must appear in the 17th column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label (v3.2.2) is defined in the **Normalization Contract**.  
The schema specifies the formula:

**Trail Use Type + " — " + Primary Managing Agency + " — " + Status**

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match normalized field values exactly  

Invalid:

- `"Hiking — ODNR — Active (Main)"`  
- `"Multi‑Use — Metro Parks — Active,"`

------------------------------------------------------------
# 9. NETWORK AFFILIATION RULES

## 9.1 Network Affiliation appears in field 16
- Semicolon‑delimited list  
- Represents **non‑hierarchical** affiliations only  
- Must match normalized names exactly  

## 9.2 No inferred membership
Only documented affiliations may appear.

## 9.3 No trailing semicolons
Invalid:

- `"Ohio to Erie Trail;"`

------------------------------------------------------------
# 10. PARENT TRAIL NETWORK RULES

## 10.1 Parent Trail Network appears in field 18
- Optional  
- Must match the exact **Trail Network Name**  

## 10.2 A Trail may have at most one Parent Trail Network
No semicolon‑delimited lists.

## 10.3 No inferred hierarchy
Only documented parentage may appear.

------------------------------------------------------------
# 11. ROW CONSTRUCTION RULES

## 11.1 Each row must contain exactly **18 fields**
No more, no fewer.

## 11.2 Each row must contain exactly **17 tabs**
Primary delimiter‑integrity invariant.

## 11.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 11.4 No field may be duplicated
Each field appears exactly once.

## 11.5 Multi‑county Trails remain single rows
- The **Counties Traversed** field contains a semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Trails.

------------------------------------------------------------
# 12. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 18‑field Trail record**  
**Step 2 — Normalize Counties Traversed into a semicolon‑delimited, alphabetized list**  
**Step 3 — Compute Derived Label for the record**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Validate Network Affiliation and Parent Trail Network formatting**  
**Step 8 — Join fields with tab characters**  
**Step 9 — Validate delimiter count (must be 17)**  
**Step 10 — Validate blank‑field representation**  
**Step 11 — Emit row**

If any step fails, TSV generation must halt and surface an error.

------------------------------------------------------------
# 13. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 17 tabs  
- Field contains a tab  
- Field contains a newline  
- Blank field contains spaces  
- Field contains trailing spaces  
- Derived Label malformed or missing  
- Network Affiliation malformed  
- Parent Trail Network invalid  
- Field order incorrect  
- Field missing  
- Field duplicated  
- **Counties Traversed field incorrectly formatted (not semicolon‑delimited, not alphabetized)**  

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 14. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Revalidate Network Affiliation placement  
- Revalidate Parent Trail Network placement  
- **Validate Counties Traversed field formatting (semicolon‑delimited, alphabetized)**  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free Trail TSV output.

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- **Trail Schema Module v3.2.2**  
- **Trail Vocabulary Module v3.2.2**  
- **Trail Normalization Contract v3.2.2**  
- **TSV Integrity Check Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF TRAIL TSV OUTPUT SPECIFICATION v3.2.2