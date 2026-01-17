# NATURAL AREAS PROJECT — TRAIL TSV OUTPUT SPECIFICATION v3.1
A deterministic, formatting‑layer specification defining exactly how Trail records
are serialized into tab‑separated values (TSV) with guaranteed delimiter integrity,
zero drift, and full compatibility with the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Vocabulary Module v3.1.
All field definitions are defined in the Trail Schema Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical v3.1 Trail TSV field order
- Delimiter rules
- Blank‑field rules
- Whitespace rules
- Derived Label placement rules
- Parent Trail Network placement rules
- Multi‑county expansion rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check and Audit & Logging Module
- Integration with the v3.1 Processing / Orchestration Module

This specification is authoritative for Trail TSV formatting.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All normalized Trail records (v3.1)
- All counties and all processing runs
- All automated or manual TSV exports
- All Trail normalization workflows
- All multi‑entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank‑field representation
- Derived Label placement
- Parent Trail Network placement
- Multi‑county expansion
- Validation requirements

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.1)

TSV output must contain exactly **16 fields** in the following order:

1. Trail Name  
2. Trail Type  
3. Trail Subtype  
4. Status  
5. Length (Miles)  
6. Surface Type  
7. Counties  
8. Managing Agency  
9. Managing Agencies (Secondary)  
10. Parent Trail Network  
11. Description  
12. URL  
13. Map Link  
14. Notes  
15. Derived Label  
16. Trail Name (Integrity Anchor)  

This order is absolute and must never change.

------------------------------------------------------------
# 4. MULTI‑COUNTY EXPANSION RULES (v3.1)

If a Trail spans multiple counties:

- Emit **one TSV row per county**.
- All fields except County remain identical.
- County field must contain exactly one county per row.
- Rows must be emitted in alphabetical county order.

Each row must independently satisfy all delimiter‑integrity rules.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).
- No spaces may appear before or after tabs.
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **15 tab characters**
- 16 fields → 15 delimiters
- No more, no fewer.

## 5.3 No field may contain a tab character
If detected → halt TSV generation.

## 5.4 No field may contain newline characters
If detected → halt TSV generation.

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
Line ends immediately after the integrity‑anchor Trail Name field.

## 7.3 Internal spaces allowed only when part of the value
Valid: `"North Ridge Trail"`  
Invalid: `"  North Ridge Trail"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v3.1)

## 8.1 Derived Label is always field 15
It must appear in the 15th column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Trail Type + " Trail"**

## 8.3 Formatting rules
- No parentheses
- No trailing punctuation
- No extra descriptors

Invalid:

- `"Hiking Trail (Main)"`
- `"Shared‑Use Trail,"`

------------------------------------------------------------
# 9. PARENT TRAIL NETWORK RULES (v3.1)

## 9.1 Parent Trail Network appears in field 10
- Semicolon‑delimited list of normalized Trail Network names.
- Must match normalized names exactly.

## 9.2 No inferred membership
Only documented networks may appear.

## 9.3 No trailing semicolons
Invalid:

- `"Ohio to Erie Trail Network;"`

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **16 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **15 tabs**
Primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county expansion occurs **before** delimiter validation
Each expanded row must independently pass all checks.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM (DETERMINISTIC, v3.1)

**Step 1 — Receive normalized 16‑field Trail record**  
**Step 2 — Expand into multiple rows if multi‑county**  
**Step 3 — Compute Derived Label for each row**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 15)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**

If any step fails → halt TSV generation.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- Row contains ≠ 15 tabs  
- Field contains a tab  
- Field contains a newline  
- Blank field contains spaces  
- Field contains trailing spaces  
- Derived Label malformed  
- Parent Trail Network misaligned  
- Field order incorrect  
- Field missing  
- Field duplicated  
- Multi‑county expansion fails  

All errors must be logged.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK (v3.1)

Integrity Check must:

- Recount delimiters  
- Revalidate blank‑field representation  
- Revalidate whitespace rules  
- Revalidate Derived Label placement  
- Revalidate Parent Trail Network placement  
- Revalidate multi‑county expansion  
- Surface anomalies  
- Halt finalization if any row fails  

Together, this spec + the Integrity Check guarantee drift‑free output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Trail Schema Module v3.1  
- Trail Vocabulary Module v3.1  
- Trail Normalization Contract v3.1  
- TSV Integrity Check Module v3.1  
- Audit & Logging Module v1.1  
- Processing / Orchestration Module v3.1  

------------------------------------------------------------
# END OF TRAIL TSV OUTPUT SPECIFICATION v3.1