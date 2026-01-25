# NATURAL AREAS PROJECT — TRAIL TSV OUTPUT SPECIFICATION v4.0
Authoritative, deterministic formatting‑layer specification defining exactly how  
**Normalized Trail Entities v4.0** are serialized into tab‑separated values (TSV)  
with guaranteed delimiter integrity, zero drift, and full compatibility with the  
v4.0 ontology and Entity Graph Schema v4.0.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Trail Vocabulary Module v4.0**.  
All field definitions are defined in the **Trail Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical TSV field order for Trails (v4.0)  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Network Affiliation and Parent Trail Network placement rules  
- **Multi‑county representation rules (universal v4.0 rule)**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module v4.0  
- Integration with the Processing / Orchestration Module v4.0  

This specification is authoritative for **Trail TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **Normalized Trail Entities v4.0**  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Network Affiliation placement  
- Parent Trail Network placement  
- **Multi‑county representation**  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v4.0)

Trail TSV output must contain exactly **18 fields** in the following order:

1. Trail Name  
2. Alternate Names  
3. Trail Use Type  
4. Trail Surface Type  
5. Trail Origin Type  
6. Total Length (Miles)  
7. **Counties Traversed**  
8. Ownership  
9. Management  
10. Coordination  
11. Status  
12. Description  
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
# 4. MULTI‑COUNTY REPRESENTATION RULES (v4.0)

Trails are **not expanded** into multiple TSV rows.

If a Trail spans multiple counties:

- The **Counties Traversed** field must contain a **semicolon‑delimited, alphabetized list**.  
- The field must not include the word “County”.  
- The Trail must appear as **a single TSV row**, regardless of how many counties it traverses.  
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
# 8. DERIVED LABEL RULES (v4.0)

## 8.1 Derived Label is always field 17
It must appear in the 17th column.

## 8.2 Derived Label is computed during normalization (v4.0)
Derived Label is **not** computed during TSV output.

## 8.3 Derived Label must match the normalized value exactly
- No additional formatting  
- No trailing punctuation  
- No inferred descriptors  

## 8.4 Derived Label formula is defined in the Trail Normalization Contract v4.0
TSV output must not modify or reinterpret it.

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
# 12. TSV GENERATION ALGORITHM (v4.0)

**Step 1 — Receive normalized 18‑field Trail entity**  
**Step 2 — Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
**Step 3 — Validate Derived Label (already computed)**  
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
- **Counties Traversed incorrectly formatted (not semicolon‑delimited, not alphabetized)**  

All errors must be logged in the Audit & Logging Module v4.0.

------------------------------------------------------------
# 14. INTEGRATION WITH TSV INTEGRITY CHECK v4.0

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Revalidate Network Affiliation placement  
- Revalidate Parent Trail Network placement  
- **Validate Counties Traversed formatting (semicolon‑delimited, alphabetized)**  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free Trail TSV output.

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- Trail Schema Module v4.0  
- Trail Vocabulary Module v4.0  
- Trail Normalization Contract v4.0  
- TSV Integrity Check Module v4.0  
- Audit & Logging Module v4.0  
- Processing / Orchestration Module v4.0  

------------------------------------------------------------
# END OF TRAIL TSV OUTPUT SPECIFICATION v4.0