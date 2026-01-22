# NATURAL AREAS PROJECT — ACCESS POINT TSV OUTPUT SPECIFICATION v3.2.2
Authoritative, deterministic formatting‑layer specification defining exactly how  
Access Point records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v3.2.2 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Access Point Vocabulary Module v3.2.2**.  
All field definitions are defined in the **Access Point Schema Module v3.2.2**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Access Points (v3.2.2)  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- **Multi‑county representation rules**  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module  
- Integration with the v3.2.2 Processing / Orchestration Module  

This specification is authoritative for **Access Point TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **normalized Access Point records** (v3.2.2)  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All v3.2.2 normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- **Multi‑county representation**  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.2.2)

Access Point TSV output must contain exactly **13 fields** in the following order:

1. Access Point Name  
2. Access Point Type  
3. Parent Entities  
4. Road Name  
5. County  
6. GPS Coordinates  
7. Plus Code  
8. Access Notes  
9. URL  
10. Map URL  
11. Network Affiliation  
12. Status  
13. Derived Label  

This order is absolute and must never change.

No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. MULTI‑COUNTY REPRESENTATION RULES (v3.2.2)

Access Points are **not expanded** into multiple TSV rows.

If an Access Point spans multiple counties:

- The **County** field must contain a **semicolon‑delimited, alphabetized list** of all counties.  
- The field must not include the word “County”.  
- The Access Point must appear as **a single TSV row**, regardless of how many counties it spans.

Example:

- Normalized counties: `Franklin;Union`  
- TSV output: `Franklin;Union`

Multi‑county logic is handled at the **Access Point level**, not by row expansion.

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
If a tab is detected inside a field, TSV generation must halt and surface an error.

## 5.4 No field may contain newline characters
If present, TSV generation must halt and surface an error.

------------------------------------------------------------
# 6. BLANK‑FIELD RULES

## 6.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

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

------------------------------------------------------------
# 7. WHITESPACE RULES

## 7.1 No leading or trailing spaces in any field
Invalid:

- `" Trailhead"`  
- `"Trailhead "`  
- `" Trailhead "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Derived Label** field.

## 7.3 Internal spaces allowed only when part of the field value
Valid: `"County Road 12"`  
Invalid: `"  County Road 12"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v3.2.2)

## 8.1 Derived Label is always field 13
It must appear in the final column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Access Point Type + " Access Point"**

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match Access Point Type exactly  

Invalid:

- `"Trailhead Access Point (Main)"`  
- `"Boat Ramp Access Point,"`

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

## 9.5 Multi‑county Access Points remain single rows
- The **County** field contains a semicolon‑delimited, alphabetized list.  
- No row expansion occurs for Access Points.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM (DETERMINISTIC, v3.2.2)

**Step 1 — Receive normalized 13‑field Access Point record**  
**Step 2 — Normalize County into a semicolon‑delimited, alphabetized list**  
**Step 3 — Compute Derived Label for the record**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 12)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

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
- **County field incorrectly formatted (not semicolon‑delimited, not alphabetized)**  
- **Parent Entities contains invalid or unresolvable parent names**  
- **Map URL or Network Affiliation contain invalid delimiters**  

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK (v3.2.2)

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- **Validate County field formatting (semicolon‑delimited, alphabetized)**  
- Validate Map URL and Network Affiliation formatting  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free Access Point TSV output.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- **Access Point Schema Module v3.2.2**  
- **Access Point Vocabulary Module v3.2.2**  
- **Access Point Normalization Contract v3.2.2**  
- **TSV Integrity Check Module v3.2.2**  
- **Audit & Logging Module v3.2.2**  
- **Processing / Orchestration Module v3.2.2**

------------------------------------------------------------
# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v3.2.2