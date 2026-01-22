# NATURAL AREAS PROJECT — SITE TSV OUTPUT SPECIFICATION v3.2.2
Authoritative, deterministic formatting‑layer specification defining exactly how  
Site records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Site Vocabulary Module v3.2.2**.  
All field definitions are defined in the **Site Schema Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Sites  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Multi‑county representation rules  
- Parent Site placement rules  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module  
- Integration with the v3.2.2 Processing / Orchestration Module  

This specification is authoritative for **Site TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **normalized Site records**   
- All counties and all processing runs  
- All automated or manual TSV exports  
- All v3.2.2 normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Multi‑county representation  
- Parent Site placement  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER

Site TSV output must contain exactly **22 fields** in the following order:

1. Name  
2. Category  
3. Subtype  
4. Designation  
5. Ownership  
6. Management  
7. Coordination  
8. Network Affiliation  
9. Description  
10. Status  
11. Address  
12. Acres  
13. Location  
14. County  
15. GPS Coordinates  
16. Plus Code  
17. Features  
18. Notes  
19. URL  
20. Map URL  
21. Derived Label  
22. Parent Site  

This order is absolute and must never change.

No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY REPRESENTATION RULES 

Sites are **not segmented** by county in the normalized dataset.

- Multi‑county Sites must appear as **a single TSV row**.  
- The **County** field must contain a semicolon‑delimited, alphabetized list of all counties.  
- The County field must not include the word “County”.  

Example:  
- Normalized counties: `Franklin;Union`  
- TSV output: `Franklin;Union` in the County field (single row).

Multi‑county logic is handled at the **Site level**, not by row expansion.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **21 tab characters**
- 22 fields → 21 delimiters  
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

- `" Park Name"`  
- `"Park Name "`  
- `" Park Name "`

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Parent Site** field.

## 7.3 Internal spaces allowed only when part of the field value
Valid:

- `"Big Walnut Creek Park"`

Invalid:

- `"  Big Walnut Creek Park"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES 

## 8.1 Derived Label is always field 21
It must appear in the 21st column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label (v3.2.2) is defined in the **Normalization Contract**.  
At minimum, it must be:

- Deterministic  
- Regenerated whenever any component field changes  

Example pattern (illustrative only; actual formula is defined in the Normalization Contract):

- `Category + " — " + (Ownership if not "Unknown" else Management) + " — " + Designation`

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors beyond the normalization contract  
- Must not contradict Category, Ownership, Management, or Designation  

------------------------------------------------------------
# 9. PARENT SITE RULES 

## 9.1 Parent Site is always field 22  
It must appear in the final column.

## 9.2 Parent Site must match the exact Name field of the parent Site  
- No abbreviations  
- No synonyms  
- No inferred or partial names  
- Must match the normalized **Name** field exactly

## 9.3 Parent Site must be blank for top‑level Sites  
- No placeholders  
- No “None”, “Top‑Level”, “N/A”, or similar values  
- Blank field only (`\t\t`)

## 9.4 Parent Site must not contain children  
- Parent Sites do **not** list children in Features or Notes  
- Parent Site expresses **upward** identity only  
- Downward relationships are handled exclusively by the **Child Site Rules Module v3.2.2** and the **Resolution Module v3.2.2**

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **22 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **21 tabs**
This is the primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
If a field is unknown, it must be represented as a blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county Sites remain single rows
- County field contains semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Sites.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM

**Step 1 — Receive normalized 22‑field Site record**  
**Step 2 — Compute Derived Label for the record**  
**Step 3 — Validate no internal tabs**  
**Step 4 — Validate no internal newlines**  
**Step 5 — Validate whitespace rules**  
**Step 6 — Validate County field formatting (semicolon‑delimited, alphabetized)**  
**Step 7 — Validate Parent Site field (exact match or blank)**  
**Step 8 — Join fields with tab characters**  
**Step 9 — Validate delimiter count (must be 21)**  
**Step 10 — Validate blank‑field representation**  
**Step 11 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 21 tabs  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label is malformed or missing  
- Field order is incorrect  
- A field is missing  
- A field is duplicated  
- County field is not semicolon‑delimited and alphabetized for multi‑county Sites  
- Category, Subtype, Designation, Ownership, Management, or Status contain invalid values per vocabulary  
- Parent Site is populated but does not match a valid Site Name  

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Validate County field formatting (including multi‑county rules)  
- Validate Parent Site references  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free Site TSV output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- **Site Schema Module v3.2.2**  
- **Site Vocabulary Module v3.2.2**  
- **Site Normalization Contract v3.2.2**  
- **TSV Integrity Check Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF SITE TSV OUTPUT SPECIFICATION v3.2.2