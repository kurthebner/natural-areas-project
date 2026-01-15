# NATURAL AREAS PROJECT — ACCESS POINT TSV OUTPUT SPECIFICATION v1
A deterministic, formatting‑layer specification defining exactly how Access Point records are serialized into a tab‑separated values (TSV) file with guaranteed delimiter integrity and zero drift.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Access Point Vocabulary Module v1.  
All field definitions are defined in the Access Point Schema Module v1.

---

# 1. PURPOSE
This module defines:

- The Access Point TSV field order  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check and Audit & Logging Module  

This module is authoritative for Access Point TSV formatting.

---

# 2. SCOPE
This specification applies to:

- All Access Point records  
- All counties  
- All automated or manual TSV exports  
- All Access Point normalization workflows  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Validation requirements  

---

# 3. FIELD ORDER (AUTHORITATIVE)
Access Point TSV output must contain exactly **10 fields** in the following order:

1. Access Point Name  
2. Access Point Type  
3. Parent Site  
4. GPS Coordinates  
5. Plus Code  
6. Road Name  
7. Access Notes  
8. URL  
9. Status  
10. Derived Label  

This order is absolute and must never change.

---

# 4. DELIMITER RULES

## 4.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 4.2 Each row must contain exactly **9 tab characters**
- 10 fields → 9 delimiters  
- No more, no fewer

## 4.3 No field may contain a tab character
If a tab is detected inside a field, TSV generation must halt and surface an error.

## 4.4 No field may contain newline characters
If present, TSV generation must halt and surface an error.

---

# 5. BLANK‑FIELD RULES

## 5.1 Blank fields must be represented as true blanks
A blank field is represented as:

`\t\t`

with nothing between the tabs.

## 5.2 No spaces inside blank fields
Invalid examples:

- `\t \t`  
- `\t  \t`  
- `\t\t `  
- ` \t\t`

## 5.3 No placeholder values
Invalid:

- `_`  
- `NULL`  
- `""`  
- `BLANK`

## 5.4 No collapsing of adjacent blanks
Adjacent blanks must remain:

`\t\t`

Never:

- `\t`  
- `\t \t`

---

# 6. WHITESPACE RULES

## 6.1 No leading or trailing spaces in any field
Invalid:

- `" Trailhead"`  
- `"Trailhead "`  
- `" Trailhead "`  

## 6.2 No trailing spaces at end of line
Lines must end immediately after the Derived Label field.

## 6.3 Internal spaces allowed only when part of the field value
Valid:

- `"County Road 12"`

Invalid:

- `"  County Road 12"`

---

# 7. DERIVED LABEL RULES

## 7.1 Derived Label is always field 10
It must appear in the final column.

## 7.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Access Point Type + " Access Point"**

## 7.3 Formatting rules
- No parentheses  
- No trailing punctuation  
- No additional descriptors

Invalid:

- `"Trailhead Access Point (Main)"`  
- `"Boat Ramp Access Point,"`

---

# 8. ROW CONSTRUCTION RULES

## 8.1 Each row must contain exactly **10 fields**
No more, no fewer.

## 8.2 Each row must contain exactly **9 tabs**
This is the primary delimiter‑integrity invariant.

## 8.3 No field may be omitted
If a field is unknown, it must be represented as a blank field (`\t\t`).

## 8.4 No field may be duplicated
Each field appears exactly once.

---

# 9. TSV GENERATION ALGORITHM (DETERMINISTIC)

**Step 1 — Receive normalized 10‑field Access Point record**  
**Step 2 — Compute Derived Label**  
**Step 3 — Validate no internal tabs**  
**Step 4 — Validate no internal newlines**  
**Step 5 — Join fields with tab characters**  
**Step 6 — Validate delimiter count (must be 9)**  
**Step 7 — Validate blank‑field representation**  
**Step 8 — Validate whitespace rules**  
**Step 9 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

# 10. ERROR CONDITIONS
TSV generation must halt if:

- A row contains fewer or more than 9 tabs  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label is malformed  
- Field order is incorrect  
- A field is missing  
- A field is duplicated  

All errors must be logged in the Audit & Logging Module.

---

# 11. INTEGRATION WITH TSV INTEGRITY CHECK
The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free output.

---

# 12. MODULE DEPENDENCIES
This module depends on:

- **Access Point Schema Module v1**  
- **Access Point Vocabulary Module v1**  
- **Access Point Normalization Contract v1**  
- **TSV Integrity Check Module**  
- **Audit & Logging Module**

---

# END OF ACCESS POINT TSV OUTPUT SPECIFICATION v1