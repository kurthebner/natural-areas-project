# NATURAL AREAS PROJECT — SITE TSV OUTPUT SPECIFICATION v1
A deterministic, formatting‑layer specification defining exactly how the 25‑field Site dataset is serialized into a tab‑separated values (TSV) file with guaranteed delimiter integrity and zero drift.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1.  
All field definitions are defined in the Site Schema Module v1.

---

# 1. PURPOSE
This module defines:

- The Site TSV field order  
- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Derived Label placement rules  
- Parent Site placement rules  
- Validation requirements  
- Error conditions  
- Integration with the TSV Integrity Check and Audit & Logging Module  

This module is authoritative for Site TSV formatting.

---

# 2. SCOPE
This specification applies to:

- All Site records  
- All counties  
- All automated or manual TSV exports  
- All Site normalization workflows  

It governs:

- Field ordering  
- Delimiter behavior  
- Blank‑field representation  
- Derived Label placement  
- Parent Site placement  
- Validation requirements  

---

# 3. FIELD ORDER (AUTHORITATIVE)
TSV output must contain exactly **25 fields** in the following order:

1. Name  
2. Category  
3. Subtype  
4. Designation  
5. Ownership  
6. Management  
7. Coordination  
8. Description  
9. Status  
10. Address  
11. Acres  
12. Location  
13. County  
14. GPS Coordinates  
15. Plus Code  
16. Trail Role  
17. Parent Trail Name  
18. Trail Segment Type  
19. Trail Access Type  
20. Trail Length (Miles)  
21. Features  
22. Notes  
23. URL  
24. Derived Label  
25. Parent Site  

This order is absolute and must never change.

---

# 4. DELIMITER RULES

## 4.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).  
- No spaces may appear before or after tabs.  
- No spaces may appear between tabs.

## 4.2 Each row must contain exactly **24 tab characters**
- 25 fields → 24 delimiters  
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

- `" Park"`  
- `"Park "`  
- `" Park "`  

## 6.2 No trailing spaces at end of line
Lines must end immediately after the **Parent Site** field.

## 6.3 Internal spaces allowed only when part of the field value
Valid:

- `"Ohio History Connection"`

Invalid:

- `"  Ohio History Connection"`

---

# 7. DERIVED LABEL RULES

## 7.1 Derived Label is always field 24
It must appear in the 24th column.

## 7.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Category + (Ownership if present else Management) + Designation**

## 7.3 Formatting rules
- Category only → `"Category"`  
- Category + Designation → `"Category (Designation)"`  
- Category + Management → `"Category (Management)"`  
- Category + Ownership → `"Category (Ownership)"`  
- Category + Ownership/Management + Designation → `"Category (Ownership/Management, Designation)"`  

## 7.4 No trailing punctuation
Invalid:

- `"Historic Site ()"`  
- `"Wildlife Area (, State Wildlife Area)"`

---

# 8. PARENT SITE RULES

## 8.1 Parent Site is always field 25
It must appear in the final column.

## 8.2 Parent Site must match the exact Name field of the parent site
No abbreviations, no synonyms.

## 8.3 Parent Site must be blank for top‑level sites
No placeholders.

## 8.4 Parent Site must not contain children
Parent sites do not list children in Features or Notes.

---

# 9. ROW CONSTRUCTION RULES

## 9.1 Each row must contain exactly **25 fields**
No more, no fewer.

## 9.2 Each row must contain exactly **24 tabs**
This is the primary delimiter‑integrity invariant.

## 9.3 No field may be omitted
If a field is unknown, it must be represented as a blank field (`\t\t`).

## 9.4 No field may be duplicated
Each field appears exactly once.

---

# 10. TSV GENERATION ALGORITHM (DETERMINISTIC)

**Step 1 — Receive normalized 25‑field Site record**  
**Step 2 — Compute Derived Label**  
**Step 3 — Validate no internal tabs**  
**Step 4 — Validate no internal newlines**  
**Step 5 — Join fields with tab characters**  
**Step 6 — Validate delimiter count (must be 24)**  
**Step 7 — Validate blank‑field representation**  
**Step 8 — Validate whitespace rules**  
**Step 9 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

---

# 11. ERROR CONDITIONS
TSV generation must halt if:

- A row contains fewer or more than 24 tabs  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label is malformed  
- Parent Site is misaligned  
- Field order is incorrect  
- A field is missing  
- A field is duplicated  

All errors must be logged in the Audit & Logging Module.

---

# 12. INTEGRATION WITH TSV INTEGRITY CHECK
The TSV Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Revalidate Parent Site placement  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this specification and the TSV Integrity Check guarantee drift‑free output.

---

# 13. MODULE DEPENDENCIES
This module depends on:

- **Site Schema Module v1**  
- **Site Vocabulary Module v1**  
- **Site Normalization Contract v1**  
- **TSV Integrity Check Module**  
- **Audit & Logging Module**

---

# END OF SITE TSV OUTPUT SPECIFICATION v1