# NATURAL AREAS PROJECT — TRAIL NETWORK TSV OUTPUT SPECIFICATION v3.1
A deterministic, formatting‑layer specification defining exactly how Trail Network
records are serialized into tab‑separated values (TSV) with guaranteed delimiter
integrity, zero drift, and full compatibility with the v3.1 ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trail Network Vocabulary Module v3.1.
All field definitions are defined in the Trail Network Schema Module v3.1.

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- The canonical v3.1 Trail Network TSV field order
- Delimiter rules
- Blank‑field rules
- Whitespace rules
- Derived Label placement rules
- Member Trail placement rules
- Multi‑county and multi‑state expansion rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check and Audit & Logging Module
- Integration with the v3.1 Processing / Orchestration Module

This specification is authoritative for Trail Network TSV formatting.

------------------------------------------------------------
# 2. SCOPE

This specification applies to:

- All normalized Trail Network records (v3.1)
- All counties and all processing runs
- All automated or manual TSV exports
- All Trail Network normalization workflows
- All multi‑entity orchestration pipelines

It governs:

- Field ordering
- Delimiter behavior
- Blank‑field representation
- Derived Label placement
- Member Trail placement
- Multi‑county and multi‑state record expansion
- Validation requirements

------------------------------------------------------------
# 3. FIELD ORDER (AUTHORITATIVE, v3.1)

TSV output must contain exactly **12 fields** in the following order:

1. Network Name  
2. Network Type  
3. Counties  
4. States  
5. Managing Agency  
6. Managing Agencies (Secondary)  
7. Member Trails  
8. Description  
9. Notes  
10. URL  
11. Derived Label  
12. Network Name (Integrity Anchor)  

This order is absolute and must never change.

------------------------------------------------------------
# 4. MULTI‑COUNTY AND MULTI‑STATE EXPANSION RULES (v3.1)

If a Trail Network spans multiple counties or states:

- One TSV row must be emitted **per county**.
- The “States” field may contain multiple states, but “County” must contain exactly one.
- Rows must be emitted in alphabetical county order.
- All other fields remain identical across rows.

Each row must independently satisfy all delimiter‑integrity rules.

------------------------------------------------------------
# 5. DELIMITER RULES

## 5.1 TSV uses tab characters only
- The delimiter is the ASCII tab (`\t`).
- No spaces may appear before or after tabs.
- No spaces may appear between tabs.

## 5.2 Each row must contain exactly **11 tab characters**
- 12 fields → 11 delimiters
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

- `" Greenway Network"`
- `"Greenway Network "`
- `" Greenway Network "`

## 7.2 No trailing spaces at end of line
Lines must end immediately after the final Network Name (integrity anchor) field.

## 7.3 Internal spaces allowed only when part of the field value
Valid:

- `"Ohio to Erie Trail System"`

Invalid:

- `"  Ohio to Erie Trail System"`

------------------------------------------------------------
# 8. DERIVED LABEL RULES (v3.1)

## 8.1 Derived Label is always field 11
It must appear in the 11th column.

## 8.2 Derived Label is computed but not stored in the normalized dataset
Derived Label =  
**Network Type + " Network"**

## 8.3 Formatting rules
- No parentheses
- No trailing punctuation
- No additional descriptors

Invalid:

- `"Greenway Network (Regional)"`
- `"Bikeway Network,"`

------------------------------------------------------------
# 9. MEMBER TRAIL RULES (v3.1)

## 9.1 Member Trails appear in field 7
- Semicolon‑delimited list of normalized Trail names.
- Must match normalized Trail names exactly.

## 9.2 No inferred membership
Only documented members may appear.

## 9.3 No trailing semicolons
Invalid:

- `"Trail A;Trail B;"`

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

## 10.1 Each row must contain exactly **12 fields**
No more, no fewer.

## 10.2 Each row must contain exactly **11 tabs**
This is the primary delimiter‑integrity invariant.

## 10.3 No field may be omitted
If a field is unknown, it must be represented as a blank field (`\t\t`).

## 10.4 No field may be duplicated
Each field appears exactly once.

## 10.5 Multi‑county expansion must occur **before** delimiter validation
Each expanded row must independently pass all checks.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM (DETERMINISTIC, v3.1)

**Step 1 — Receive normalized 12‑field Trail Network record**  
**Step 2 — Expand into multiple rows if multi‑county**  
**Step 3 — Compute Derived Label for each row**  
**Step 4 — Validate no internal tabs**  
**Step 5 — Validate no internal newlines**  
**Step 6 — Validate whitespace rules**  
**Step 7 — Join fields with tab characters**  
**Step 8 — Validate delimiter count (must be 11)**  
**Step 9 — Validate blank‑field representation**  
**Step 10 — Emit row**

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains fewer or more than 11 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Derived Label is malformed
- Member Trails are misaligned
- Field order is incorrect
- A field is missing
- A field is duplicated
- Multi‑county expansion fails

All errors must be logged in the Audit & Logging Module.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK (v3.1)

The TSV Integrity Check must:

- Recount delimiters
- Revalidate blank‑field representation
- Revalidate whitespace rules
- Revalidate Derived Label placement
- Revalidate Member Trail placement
- Revalidate multi‑county expansion
- Surface anomalies
- Halt finalization if any row fails

Together, this specification and the TSV Integrity Check guarantee drift‑free output.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- **Trail Network Schema Module v3.1**
- **Trail Network Vocabulary Module v3.1**
- **Trail Network Normalization Contract v3.1**
- **TSV Integrity Check Module v3.1**
- **Audit & Logging Module v1.1**
- **Processing / Orchestration Module v3.1**

------------------------------------------------------------
# END OF TRAIL NETWORK TSV OUTPUT SPECIFICATION v3.1