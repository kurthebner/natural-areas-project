# NATURAL AREAS PROJECT — TSV INTEGRITY CHECK MODULE v1
A deterministic validation module ensuring that all TSV output for **Sites** and **Access Points** meets strict delimiter‑integrity, blank‑field, and alignment requirements before finalization.

This module contains no controlled vocabularies.  
All vocabularies are defined in the Site Vocabulary Module v1 and Access Point Vocabulary Module v1.

---

# 1. PURPOSE
This module defines:

- How TSV rows are validated  
- How delimiter counts are checked  
- How blank fields must be represented  
- How field alignment is enforced  
- How anomalies are surfaced  
- How failures halt finalization  

This module ensures:

- Zero delimiter drift  
- Zero misalignment  
- Zero silent formatting errors  
- Full compatibility with the Audit & Logging Module  
- Deterministic, reproducible TSV output  

---

# 2. SCOPE
This module applies to:

- **Site TSV output** (25 fields, 24 delimiters)  
- **Access Point TSV output** (10 fields, 9 delimiters)  
- All automated and manual TSV generation steps  

It governs:

- Delimiter rules  
- Blank‑field rules  
- Whitespace rules  
- Field‑position rules  
- Error surfacing  

---

# 3. DELIMITER REQUIREMENTS

## 3.1 Sites (25 fields)
- Each row must contain exactly **24 tab characters**  
- No more, no fewer  

## 3.2 Access Points (10 fields)
- Each row must contain exactly **9 tab characters**  
- No more, no fewer  

## 3.3 No internal tabs
If a field contains a tab, the row fails integrity.

## 3.4 No newline characters
If a field contains a newline, the row fails integrity.

---

# 4. BLANK‑FIELD REQUIREMENTS

## 4.1 Blank fields must be true blanks
A blank field must be represented as:

`\t\t`

with nothing between the tabs.

## 4.2 No spaces inside blank fields
Invalid:

- `\t \t`  
- `\t  \t`  
- `\t\t `  
- ` \t\t`  

## 4.3 No placeholder values
Invalid:

- `_`  
- `NULL`  
- `""`  
- `BLANK`  

## 4.4 No collapsed blanks
Adjacent blanks must remain:

`\t\t`

Never:

- `\t`  
- `\t \t`  

---

# 5. WHITESPACE REQUIREMENTS

## 5.1 No leading or trailing spaces in any field
Invalid:

- `" Park"`  
- `"Park "`  
- `" Park "`  

## 5.2 No trailing spaces at end of line
Lines must end immediately after the final field.

## 5.3 Internal spaces allowed only when part of the field value
Valid:

- `"Ohio History Connection"`

Invalid:

- `"  Ohio History Connection"`

---

# 6. FIELD‑POSITION REQUIREMENTS

## 6.1 Sites (25 fields)
- Derived Label must be **field 24**  
- Parent Site must be **field 25**  
- URL must be **field 23**  
- Notes must be **field 22**  
- Features must be **field 21**  

## 6.2 Access Points (10 fields)
- Derived Label must be **field 10**  
- Parent Site must be **field 3**  

If any field is out of position, the row fails integrity.

---

# 7. VALIDATION ALGORITHM (DETERMINISTIC)

### Step 1 — Count delimiters  
- Sites: must be 24  
- Access Points: must be 9  

### Step 2 — Validate blank‑field representation  
- All blanks must be true blanks  
- No spaces between delimiters  

### Step 3 — Validate no internal tabs  
### Step 4 — Validate no internal newlines  
### Step 5 — Validate field alignment  
### Step 6 — Validate whitespace rules  
### Step 7 — Surface anomalies  
### Step 8 — Halt finalization if any row fails  

If any step fails, TSV generation must not proceed.

---

# 8. ERROR CONDITIONS
A row fails integrity if:

- Delimiter count is incorrect  
- A field contains a tab  
- A field contains a newline  
- A blank field contains spaces  
- A field contains trailing spaces  
- Derived Label is misaligned  
- Parent Site is misaligned  
- Any field is missing  
- Any field is duplicated  
- Any field is out of order  

All failures must be logged in the Audit & Logging Module.

---

# 9. OUTPUT OF THIS MODULE
For each row:

- Pass / Fail  
- Expected delimiter count  
- Actual delimiter count  
- List of anomalies (if any)  
- Whether the pipeline halted  

This output is consumed by:

- Processing Orchestration Module v1  
- Audit & Logging Module v1  

---

# 10. MODULE DEPENDENCIES
This module depends on:

- **Site TSV Output Specification v1**  
- **Access Point TSV Output Specification v1**  
- **Processing Orchestration Module v1**  
- **Audit & Logging Module v1**

---

# END OF TSV INTEGRITY CHECK MODULE v1