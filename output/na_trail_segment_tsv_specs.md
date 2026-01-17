# NATURAL AREAS PROJECT — TRAIL SEGMENT TSV OUTPUT SPECIFICATION v3.1
A deterministic, formatting‑layer specification defining exactly how Trail Segment
records are serialized into tab‑separated values (TSV) with guaranteed delimiter
integrity, zero drift, and full compatibility with the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Segment Vocabulary Module v3.1.
All field definitions are defined in the Trail Segment Schema Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical v3.1 Trail Segment TSV field order
- Delimiter rules
- Blank‑field rules
- Whitespace rules
- Derived Label placement rules
- Parent Trail placement rules
- Multi‑county expansion rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check and Audit & Logging Module
- Integration with the v3.1 Processing / Orchestration Module

This specification is authoritative for Trail Segment TSV formatting.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All normalized Trail Segment records (v3.1)
- All counties and all processing runs
- All automated or manual TSV exports
- All Trail Segment normalization workflows
- All multi‑entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank‑field representation
- Derived Label placement
- Parent Trail placement
- Multi‑county expansion
- Validation requirements

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.1)

TSV output must contain exactly **15 fields** in the following order:

1. Segment Name  
2. Parent Trail  
3. Segment Identifier  
4. Segment Length (Miles)  
5. Surface Type  
6. Status  
7. Counties  
8. Managing Agency  
9. Managing Agencies (Secondary)  
10. Description  
11. URL  
12. Map Link  
13. Notes  
14. Derived Label  
15. Parent Trail (Integrity Anchor)  

This order is absolute and must never change.

------------------------------------------------------------
# 4. MULTI‑COUNTY EXPANSION RULES (v3.1)

If a Trail Segment spans multiple counties:

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

## 5.2 Each row must contain exactly **14 tab characters**
- 15 fields → 14 delimiters
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

- `" North Section"`
- `"North Section "`
- `" North Section "`  

## 7.2 No trailing spaces at end of line
Lines must end immediately after the integrity‑anchor Parent Trail field.

## 7.3 Internal spaces allowed only when part of the field value
Valid: `"North Loop Section"`  
Invalid: `"  North Loop Section"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v3.1)

## 8.1 Derived Label is always field 14
It must appear in the 14th column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Segment Identifier + " Segment"**  
If no identifier →  
**Segment Name + " Segment"**

## 8.3 Formatting rules
- No parentheses
- No trailing punctuation
- No extra descriptors

Invalid:

- `"North Section Segment (Main)"`
- `"Riverside Segment,"`

------------------------------------------------------------
# 9. PARENT TRAIL RULES (v3.1)

## 9.1 Parent Trail appears in fields 2 and 15
- Field 2: semantic parent
- Field 15: integrity anchor

## 9.2 Both fields must match exactly
No abbreviations or synonyms.

## 9.3 Parent Trail must be a valid normalized Trail
If not → halt TSV generation.

## 9.4 Parent Trail must never be blank
Trail Segments always have exactly one parent.

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **15 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **14 tabs**
Primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
Unknown fields → blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county expansion occurs **before** delimiter validation
Each expanded row must independently pass all checks.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM (DETERMINISTIC, v3.1)

**Step 1 — Receive normalized 15‑field Trail Segment record**  
**Step 2 — Expand into multiple rows if multi‑county**  
**Step 3 — Compute Derived Label for each row**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 14)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**

If any step fails → halt TSV generation.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 14 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Derived Label malformed
- Parent Trail misaligned
- Field order incorrect
- Field missing
- Field duplicated
- Multi‑county expansion fails

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK (v3.1)

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank‑field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement
- Revalidate Parent Trail placement
- Revalidate multi‑county expansion
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift‑free output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- **Trail Segment Schema Module v3.1**
- **Trail Segment Vocabulary Module v3.1**
- **Trail Segment Normalization Contract v3.1**
- **TSV Integrity Check Module v3.1**
- **Audit & Logging Module v1.1**
- **Processing / Orchestration Module v3.1**

------------------------------------------------------------
# END OF TRAIL SEGMENT TSV OUTPUT SPECIFICATION v3.1