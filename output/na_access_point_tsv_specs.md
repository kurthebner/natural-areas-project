# NATURAL AREAS PROJECT — ACCESS POINT TSV OUTPUT SPECIFICATION v4.0
Authoritative, deterministic formatting‑layer specification defining exactly how  
Access Point records are serialized into tab‑separated values (TSV) with guaranteed  
delimiter integrity, zero drift, and full compatibility with the v4.0 ontology.

This module contains no controlled vocabularies.  
All vocabularies are defined in the **Access Point Vocabulary Module v4.0**.  
All field definitions are defined in the **Access Point Schema Module v4.0**.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The **canonical TSV field order** for Access Points (v4.0)  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- County / jurisdiction representation rules  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check Module v4.0  
- Integration with the Processing / Orchestration Module v4.0  

This specification is authoritative for **Access Point TSV formatting**.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All **normalized Access Point records** (v4.0)  
- All counties and all processing runs  
- All automated or manual TSV exports  
- All v4.0 normalization workflows  
- All multi‑entity orchestration pipelines  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Jurisdiction representation  
- Validation requirements  

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v4.0)

Access Point TSV output must contain exactly **15 fields** in the following order:

1. Access Point Name  
2. Access Point Type  
3. Access Level  
4. Status  
5. Role  
6. Identity Parent  
7. Additional Parents  
8. County  
9. Township  
10. Municipality  
11. GPS Coordinates  
12. Plus Code  
13. Address  
14. URL(s)  
15. Derived Label  

This order is absolute and must never change.

No additional fields may be added.  
No fields may be removed or reordered.

------------------------------------------------------------
# 4. JURISDICTION REPRESENTATION RULES (v4.0)

Access Points physically exist at a single point.  
Therefore:

### County
- Must contain **exactly one** normalized county.  
- Must not include the word “County”.  
- Must not be a semicolon‑delimited list.  
- If unverifiable → leave blank and flag in provenance.

### Township & Municipality
- Include if validated.  
- Must not be invented or inferred.  
- Must not be semicolon‑delimited lists.

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

- `" Trailhead"`  
- `"Trailhead "`  
- `" Trailhead "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the **Derived Label** field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"County Road 12"`  
Invalid: `"  County Road 12"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v4.0)

## 8.1 Derived Label is always field 15
It must appear in the final column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label (v4.0) is defined in the **Access Point Normalization Contract v4.0**:

**Access Point Type + " Access Point"**

## 8.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors  
- Must match normalized Access Point Type exactly  

Invalid:

- `"Trailhead Access Point (Main)"`  
- `"Boat Ramp Access Point,"`

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

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM (DETERMINISTIC, v4.0)

**Step 1 — Receive normalized 15‑field Access Point record**  
**Step 2 — Validate County (must be a single normalized county)**  
**Step 3 — Compute Derived Label**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 14)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**  

If any step fails, TSV generation halts and surfaces an error.

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
- **County field contains multiple counties**  
- **GPS or Plus Code fields contain invalid formats**  
- **Parent fields contain invalid or unresolvable parent IDs**  
- **URL field contains invalid delimiters**  

All errors must be logged in the Audit & Logging Module v4.0.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK (v4.0)

The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Validate County formatting (single county only)  
- Validate URL formatting  
- Validate parent‑entity formatting  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the Integrity Check guarantee drift‑free Access Point TSV output.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- **Access Point Schema Module v4.0**  
- **Access Point Vocabulary Module v4.0**  
- **Access Point Normalization Contract v4.0**  
- **TSV Integrity Check Module v4.0**  
- **Audit & Logging Module v4.0**  
- **Processing / Orchestration Module v4.0**  

------------------------------------------------------------
# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v4.0