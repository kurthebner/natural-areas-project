# NATURAL AREAS PROJECT
# TSV INTEGRITY CHECK MODULE v6.0
Authoritative, deterministic validation module ensuring that all TSV output for
all four entity types meets strict delimiter-integrity, blank-field, whitespace,
field-alignment, identity-anchor, cross-entity reference pairing, multi-county
representation, and provenance exclusion rules before finalization.

This module contains no controlled vocabularies.
All vocabularies are defined in the respective Vocabulary Modules v6.x.

This module supersedes TSV Integrity Check Module v5.3.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Entity types reduced from six to four**: Trail, Trail Segment, and Trail
  Network are unified into the single Trailthing entity type. §2 Scope, §3
  Delimiter Requirements, §6 Field-Position Requirements, and §7a Provenance
  Field Exclusion updated accordingly. §6.3 Trail, §6.4 Trail Segment, and §6.5
  Trail Network replaced by §6.3 Trailthing.

- **Field counts updated** to match v6.0 TSV Output Specifications:
  - Site: 25 → 30 fields; 24 → 29 delimiters
  - Trailthing: new — 31 fields; 30 delimiters
  - Site Network: 15 → 18 fields; 14 → 17 delimiters
  - Access Point: 17 → 20 fields; 16 → 19 delimiters

- **Cross-entity reference pairing validation added** (§6 and §8 Step 6a):
  Every cross-entity ID field must be paired with a corresponding name field.
  Both must be blank together or populated together. Mismatch is an integrity
  failure. Affected field pairs by entity type:
  - Site: parent_site_id / parent_site_name (Fields 27–28)
  - Trailthing: parent_id / parent_name (Fields 5–6),
    site_parent_id / site_parent_name (Fields 7–8),
    parent_site_network_id / parent_site_network_name (Fields 9–10)
  - Site Network: member_site_ids / member_site_names (Fields 12–13) —
    additionally, both lists must have equal semicolon-delimited value counts
  - Access Point: identity_parent_entity_id / identity_parent_entity_name
    (Fields 5–6)

- **New field validations** added for v6.0 fields:
  - Site: habitat_type (free-text, pos 11), access_notes (free-text, pos 13),
    last_verified_date (DATE YYYY-MM-DD, pos 25), field_verified (boolean, pos 26)
  - Trailthing: source_term (WARN if blank, pos 3), last_verified_date (pos —
    not in Trailthing TSV)
  - Access Point: last_verified_date (DATE YYYY-MM-DD, pos 18),
    field_verified (boolean, pos 19)

- **All v5.3 rules carried forward**: delimiter integrity, blank-field rules,
  whitespace rules, identity-anchor validation, multi-county representation,
  provenance field exclusion (§7a, IMP-030).

------------------------------------------------------------
# 1. PURPOSE

This module defines:

- How TSV rows are validated
- How delimiter counts are checked
- How blank fields must be represented
- How whitespace rules are enforced
- How field alignment is validated for each entity type
- How identity-anchor fields are validated
- How cross-entity reference ID / Name pairings are validated
- How parent-entity fields are validated
- How **multi-county representation** is validated
- How **provenance field exclusion** is enforced
- How anomalies are surfaced
- How failures halt finalization
- How results integrate with the Audit & Logging Module v6.x

This module ensures:

- Zero delimiter drift
- Zero misalignment
- Zero silent formatting errors
- Zero provenance field leakage
- Zero unpaired cross-entity references
- Deterministic, reproducible TSV output
- Full compatibility with the v6.x ontology

------------------------------------------------------------
# 2. SCOPE

This module applies to **all four TSV output types**:

- **Site** (31 fields, 30 delimiters)
- **Trailthing** (31 fields, 30 delimiters)
- **Site Network** (18 fields, 17 delimiters)
- **Access Point** (20 fields, 19 delimiters)

It governs:

- Delimiter rules
- Blank-field rules
- Whitespace rules
- Field-position rules
- Identity-anchor rules
- Cross-entity reference pairing rules
- Parent-entity rules
- Multi-county representation validation
- Provenance field exclusion
- Error surfacing

------------------------------------------------------------
# 3. DELIMITER REQUIREMENTS (ENTITY-SPECIFIC)

Each TSV row must contain **exactly** the following number of tab characters:

- **Site**: 30 tabs
- **Trailthing**: 30 tabs
- **Site Network**: 17 tabs
- **Access Point**: 19 tabs

No more, no fewer.

## 3.1 No internal tabs
If a field value contains a tab character, the row fails integrity.

## 3.2 No newline characters
If a field value contains a newline character, the row fails integrity.

------------------------------------------------------------
# 4. BLANK-FIELD REQUIREMENTS

## 4.1 Blank fields must be true blanks
Represented as adjacent tab delimiters with nothing between them:

`\t\t`

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
- `N/A`

## 4.4 No collapsed blanks
Adjacent blank fields must each remain `\t\t`. Blanks may not be collapsed or merged.

------------------------------------------------------------
# 5. WHITESPACE REQUIREMENTS

## 5.1 No leading or trailing spaces in any field
Invalid:
- `" Park"`
- `"Park "`
- `" Park "`

## 5.2 No trailing spaces at end of line
The line must end immediately after the final field value.

## 5.3 Internal spaces allowed only when part of the value
Valid: `"Ohio History Connection"`
Invalid: `"  Ohio History Connection"`

------------------------------------------------------------
# 6. FIELD-POSITION REQUIREMENTS (ENTITY-SPECIFIC)

The following anchor fields must appear in the exact positions defined in the
v6.0 TSV Output Specifications.

## 6.1 Site (31 fields)
- Name (identity anchor) → Field 1
- Category → Field 2
- Habitat Type → Field 11 (free-text, no vocabulary enforcement)
- Features → Field 12
- Access Notes → Field 13 (free-text)
- Counties → Field 16
- Municipality → Field 17 (GIS-derived)
- Township → Field 18 (GIS-derived)
- GPS Lat → Field 19
- GPS Lon → Field 20
- Plus Code → Field 21 (derived from GPS)
- Last Verified Date → Field 25 (DATE format YYYY-MM-DD or blank)
- Field Verified → Field 26 (boolean: true / false)
- Parent Site ID → Field 27
- Parent Site Name → Field 28 (must be blank when Field 27 blank; must be populated when Field 27 populated)
- eBird Hotspot ID → Field 31 (optional; blank or eBird L-code format; no vocabulary enforcement)

## 6.2 Access Point (20 fields)
- Access Point Name (identity anchor) → Field 1
- Access Point Type → Field 2
- Identity Parent Entity Type → Field 4 (Site or Trailthing only)
- Identity Parent Entity ID → Field 5
- Identity Parent Entity Name → Field 6 (must be blank when Field 5 blank; must be populated when Field 5 populated)
- County → Field 7 (single value only — no semicolons)
- GPS Lat → Field 11
- GPS Lon → Field 12
- Plus Code → Field 13 (derived from GPS)
- Features → Field 14
- Identity Notes → Field 15
- Last Verified Date → Field 18 (DATE format YYYY-MM-DD or blank)
- Field Verified → Field 19 (boolean: true / false)
- Access Point ID → Field 20

## 6.3 Trailthing (31 fields)
- Name (identity anchor) → Field 1
- Source Term → Field 3 (WARN if blank — discovery gap indicator)
- Parent ID → Field 5 (Trailthing entity ID or blank)
- Parent Name → Field 6 (must be blank when Field 5 blank; must be populated when Field 5 populated)
- Site Parent ID → Field 7 (Site entity ID or blank)
- Site Parent Name → Field 8 (must be blank when Field 7 blank; must be populated when Field 7 populated)
- Parent Site Network ID → Field 9 (Site Network entity ID or blank)
- Parent Site Network Name → Field 10 (must be blank when Field 9 blank; must be populated when Field 9 populated)
- Counties → Field 22
- Trailthing ID → Field 31

## 6.4 Site Network (18 fields)
- Network Name (identity anchor) → Field 1
- Network Type → Field 2
- Org Type → Field 3
- Counties → Field 9
- Member Count → Field 11 (integer or blank)
- Member Site IDs → Field 12 (semicolon-delimited entity IDs or blank)
- Member Site Names → Field 13 (must be blank when Field 12 blank; must be populated when Field 12 populated; semicolon-delimited value count must equal Field 12 value count)
- Identity Notes → Field 15
- Network ID → Field 18

If any anchor field is out of position, the row fails integrity.

------------------------------------------------------------
# 6a. CROSS-ENTITY REFERENCE PAIRING REQUIREMENTS

Every cross-entity reference in TSV output consists of an ID field immediately
followed by a corresponding Name field. Both fields must be blank together or
populated together. A mismatch (one blank, one populated) is an integrity failure.

**Required pairs by entity type:**

| Entity | ID Field | Position | Name Field | Position |
|---|---|---|---|---|
| Site | parent_site_id | 27 | parent_site_name | 28 |
| Trailthing | parent_id | 5 | parent_name | 6 |
| Trailthing | site_parent_id | 7 | site_parent_name | 8 |
| Trailthing | parent_site_network_id | 9 | parent_site_network_name | 10 |
| Site Network | member_site_ids | 12 | member_site_names | 13 |
| Access Point | identity_parent_entity_id | 5 | identity_parent_entity_name | 6 |

**Additional rule for Site Network member lists:**
When member_site_ids (Field 12) is populated, member_site_names (Field 13) must
contain exactly the same number of semicolon-delimited values. Count mismatch is
an integrity failure.

------------------------------------------------------------
# 7. MULTI-COUNTY REPRESENTATION VALIDATION

**Universal rule:** All entities are single-row entities. No entity expands into
multiple rows.

For all four entities:

- Counties field must contain a **semicolon-delimited, alphabetized list** of
  county names.
- No row may contain more than one TSV record for the same entity.
- No entity may emit multiple rows based on county.
- No county may appear twice in the list.
- No trailing semicolons.
- No spaces around semicolons.

**Exception — Access Point County field:**
Access Points are point locations and must have exactly **one county** (no
semicolon-delimited list). A semicolon in the Access Point County field is an
integrity failure.

A row fails integrity if:

- A county list is not alphabetized
- A county list is not semicolon-delimited
- Any entity attempts multi-row expansion
- A county appears more than once in the list
- A trailing semicolon is present
- Spaces appear around semicolons
- An Access Point County field contains a semicolon

------------------------------------------------------------
# 7a. PROVENANCE FIELD EXCLUSION

Entity TSV files must contain only the canonical fields defined in the TSV Output
Specification for each entity type. Fields from any provenance table must never
appear in entity TSVs.

**Provenance tables whose fields are prohibited in entity TSVs:**

- `discovery_provenance`
- `resolution_provenance`
- `normalization_provenance`
- `run_metadata`

**Canonical field counts (authoritative — v6.0):**

| Entity | Field Count | Reference |
|---|---|---|
| Site | 31 | na_tsv_output_site_v6.0.md |
| Trailthing | 31 | na_tsv_output_trailthing_v6.0.md |
| Site Network | 18 | na_tsv_output_site_network_v6.0.md |
| Access Point | 20 | na_tsv_output_access_point_v6.0.md |

**Validation rule:**
When a TSV file includes a header row, every column name in that header must match
the canonical field list for its entity type, in the canonical order. Any column
name not in the canonical list is a provenance leakage error. A TSV with more
columns than the canonical count fails regardless of whether a header is present.

------------------------------------------------------------
# 8. VALIDATION ALGORITHM (DETERMINISTIC)

### Step 1 — Identify entity type
Based on expected delimiter count:
- 30 tabs → Site
- 30 tabs → Trailthing
- 17 tabs → Site Network
- 19 tabs → Access Point

If the delimiter count matches none of the above, the row fails.

### Step 2 — Count delimiters
Must match the entity's required count exactly.

### Step 3 — Validate blank-field representation
All blanks must be true blanks (`\t\t`).

### Step 4 — Validate no internal tabs

### Step 5 — Validate no internal newlines

### Step 6 — Validate field alignment
Check all anchor fields are in correct positions (§6).

### Step 6a — Validate cross-entity reference pairings (§6a)
For each ID / Name pair:
- If ID field is blank, Name field must also be blank.
- If ID field is populated, Name field must also be populated.
- Fail if either condition is violated.

For Site Network member list pair additionally:
- Count semicolon-delimited values in member_site_ids and member_site_names.
- Fail if counts are unequal.

### Step 7 — Validate whitespace rules
No leading/trailing spaces in any field.

### Step 8 — Validate identity-anchor fields
Must be populated; must not be blank.

### Step 9 — Validate parent-entity fields
- Site: if parent_site_id is populated, verify it has the OH-{COUNTY}-S-{SEQ}
  format; verify parent_site_name is also populated.
- Trailthing: validate each parent ID field format (TT or S ID format as appropriate).
- Access Point: verify identity_parent_entity_type is "Site" or "Trailthing";
  verify identity_parent_entity_id has valid entity ID format.

### Step 10 — Validate multi-county representation
Semicolon-delimited, alphabetized, no duplicates, no trailing semicolons.
Access Point County: single value, no semicolons.

### Step 11 — Validate vocabulary-controlled fields
- Site: category, subtype, designation, status (required vocabulary);
  features (semicolon-delimited vocabulary terms, alphabetized)
- Trailthing: use_type, surface_type, origin_type, org_type, status, difficulty
  (optional vocabulary — warn on blank if discovery metadata indicates a value
  was present; error on invalid value)
- Site Network: network_type (required), org_type, status (optional vocabulary)
- Access Point: access_point_type (required), status (optional vocabulary)

### Step 11a — Validate new v6.0 fields
- last_verified_date (Site pos 25, AP pos 18): if populated, must match YYYY-MM-DD.
- field_verified (Site pos 26, AP pos 19): if populated, must be boolean true/false.
- source_term (Trailthing pos 3): if blank, log WARNING (discovery gap).
- parent_site_network_id (Trailthing pos 9): must be paired with parent_site_network_name (pos 10).

### Step 12 — Validate provenance field exclusion
If a header row is present, validate every column name against the canonical
field list for the entity type (§7a). If the delimiter count matches the canonical
count but a header row contains any column name not in the canonical list, the row
fails. A TSV with more columns than the canonical count fails regardless of header
presence.

### Step 13 — Surface anomalies
Collect all failures found in Steps 1–12.

### Step 14 — Halt finalization if any row fails
If any step fails for any row, TSV finalization must not proceed.
All failures must be logged before halting.

------------------------------------------------------------
# 9. ERROR CONDITIONS

A row fails integrity if:

- Delimiter count is incorrect for the identified entity type
- Delimiter count matches no known entity type
- A field value contains a tab character
- A field value contains a newline character
- A blank field contains spaces or placeholder values
- A field has leading or trailing whitespace
- Identity-anchor field (name) is misaligned or blank
- Identity Parent Entity Type is not "Site" or "Trailthing" (Access Points)
- Identity Parent Entity ID is misaligned (Access Points)
- Identity Parent Entity ID is populated but Identity Parent Entity Name is blank
- Identity Parent Entity Name is populated but Identity Parent Entity ID is blank
- Parent Site ID is populated but Parent Site Name is blank (Sites)
- Parent Site Name is populated but Parent Site ID is blank (Sites)
- Any Trailthing parent ID is populated but its paired name field is blank
- Any Trailthing parent name is populated but its paired ID field is blank
- Member Site IDs and Member Site Names have unequal semicolon-delimited value counts
- GPS Lat or GPS Lon is misaligned (Sites, Access Points)
- Plus Code is misaligned (Sites, Access Points)
- Plus Code is populated when GPS fields are blank
- Features field is misaligned (Sites, Access Points)
- last_verified_date contains non-DATE content (Sites, Access Points)
- field_verified contains a non-boolean value (Sites, Access Points)
- parent_site_network_id is populated without parent_site_network_name (or vice versa)
- Any field is missing
- Any field is duplicated
- Any field is out of order
- **County field is not a semicolon-delimited, alphabetized list**
- **Access Point County field contains a semicolon (multi-county not valid for APs)**
- **Any entity attempts multi-row expansion**
- **TSV column list contains a field not in the canonical field list for its entity type (provenance leakage)**

Warnings (non-halting):
- source_term is blank on a Trailthing row (discovery gap indicator)
- last_verified_date is blank (expected for older records)

All failures must be logged in the Audit & Logging Module v6.x.

------------------------------------------------------------
# 10. OUTPUT OF THIS MODULE

For each row:

- Pass / Fail / Warning
- Expected delimiter count
- Actual delimiter count
- List of anomalies (if any)
- List of warnings (if any)
- Whether the pipeline halted

This output is consumed by:

- Normalization Engine v6.0 (pipeline halt signal)
- Audit & Logging Module v6.x

------------------------------------------------------------
# 11. MODULE DEPENDENCIES

This module depends on:

- **Site TSV Output Specification v6.0**
- **Trailthing TSV Output Specification v6.0**
- **Site Network TSV Output Specification v6.0**
- **Access Point TSV Output Specification v6.0**
- **Normalization Engine v6.0**
- **Audit & Logging Module v6.x** *(or v5.x)*

------------------------------------------------------------
# END OF TSV INTEGRITY CHECK MODULE v6.0
