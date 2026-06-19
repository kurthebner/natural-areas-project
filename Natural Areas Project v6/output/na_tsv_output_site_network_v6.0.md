# NATURAL AREAS PROJECT
# SITE NETWORK TSV OUTPUT SPECIFICATION v6.0
(Authoritative Formatting-Layer Specification for Normalized Site Network Entities)

This module defines the authoritative, deterministic rules for serializing
normalized Site Network entities into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v6.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Site Network Vocabulary Module v6.0.
All field definitions are defined in the Site Network Schema Module v6.0.
All normalization rules are defined in the Site Network Normalization Contract v6.0.

This module supersedes Site Network TSV Output Specification v5.1.

------------------------------------------------------------
# CHANGES FROM v5.1 → v6.0

- **Coordination field added** (position 8, IMP-135): free-text community-based,
  volunteer, advisory, or informal partners.
- **Org Type field added** (position 3): was in v5 schema but absent from v5.1 TSV;
  now included.
- **`member_site_names` added alongside `member_site_ids`** (position 13): Human-readable
  names of member Sites. ID-only references are insufficient for human-readable output;
  every cross-entity ID reference in TSV output must be paired with the referenced
  entity's name.
- **Field count changed**: 15 → 18 fields; 14 → 17 tab delimiters per row.
- **SITE_NETWORK_PROVISIONAL flag note added** (§3 Field Notes, Field 14): both
  SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags must be preserved
  in Identity Notes output.
- **All v5.1 structural rules carried forward**: delimiter rules, blank-field rules,
  whitespace rules, multi-county/multi-state representation, Member Site IDs
  serialization.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The canonical TSV field order for Site Networks
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Member Site IDs serialization rules
- Multi-county and multi-state representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v6.x

This specification is authoritative for Site Network TSV formatting.

------------------------------------------------------------
# 2. FIELD ORDER (CANONICAL v6.0)

Site Network TSV output must contain exactly **18 fields** in the following order:

1.  network_name
2.  network_type
3.  org_type *(added in v6.0)*
4.  status
5.  ownership
6.  governance
7.  partner_agencies
8.  coordination *(added in v6.0)*
9.  counties
10. states_included
11. member_count
12. member_site_ids
13. member_site_names *(new — human-readable names of member Sites)*
14. description
15. identity_notes
16. notes
17. url
18. network_id

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**18 fields = 17 tab delimiters per row.**

**Cross-entity reference rule**: Every field that references another entity by ID
must be immediately followed by a field containing that entity's human-readable
name. `member_site_ids` (position 12) is immediately followed by `member_site_names`
(position 13). Both are blank when no member Site IDs have been resolved.

------------------------------------------------------------
# 3. FIELD NOTES

## Field 1 — Network Name
- Required; must never be blank.
- Official published name; must be unique statewide (case-insensitive).

## Field 2 — Network Type
- Required.
- Must match a valid value from Site Network Vocabulary Module v6.0.
- Single value only.

## Field 3 — Org Type *(new position in TSV)*
- Optional.
- Must match a valid value from Site Network Vocabulary Module v6.0.
- Classifies the organizational category of the primary managing entity.
- Blank when the managing entity type is undocumented.

## Field 4 — Status
- Optional.
- Must match a valid value from Site Network Vocabulary Module v6.0:
  Active, Proposed, Under Development, Inactive, Dissolved.
- "Proposed" and "Dissolved" must be explicitly documented.
- Blank if not documented.

## Field 5 — Ownership
- Optional free-text.
- Must contain the legal name of the entity that owns or established the network.
- Blank for NHAs, scenic river corridors, and other designation-based networks.
- Blank is correct and common.

## Field 6 — Governance
- Required.
- Primary agency or organization responsible for coordinating or managing the network.
- Semicolon-delimit if multiple formally documented co-managers.

## Field 7 — Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies.
- Must not duplicate Governance.
- Blank if none documented.

## Field 8 — Coordination *(new)*
- Optional.
- Community-based, volunteer, advisory, or informal partners.
- Distinct from Partner Agencies.
- Blank if none documented.

## Field 9 — Counties
- Required.
- Semicolon-delimited, alphabetized list of county names.
- Must not include "County."
- Site Networks remain single rows.

## Field 10 — States Included
- Optional.
- Semicolon-delimited, alphabetized list of state abbreviations.
- Blank for Ohio-only networks.

## Field 11 — Member Count
- Optional but strongly recommended.
- Integer representing the number of member Sites.
- Must be the normalized value — not recomputed from member_site_ids during TSV
  generation.
- Blank if truly unknown.

## Field 12 — Member Site IDs
- Optional.
- Semicolon-delimited list of Site entity IDs (OH-{COUNTY}-S-{SEQ} format).
- Blank if no member Site IDs have been resolved.
- Must not contain non-ID values or placeholder text.

## Field 13 — Member Site Names *(new)*
- Semicolon-delimited list of the Name fields of the member Sites, in the same
  order as member_site_ids.
- Blank when member_site_ids is blank.
- Both member_site_ids and member_site_names must be blank together or populated
  together with equal counts of semicolon-delimited values.

## Field 14 — Description
- Optional but strongly recommended.
- 1-3 sentences on the network's identity, scope, and purpose.
- May include establishment history.

## Field 15 — Identity Notes
- Optional.
- Identity clarifications, disambiguation, alternate names.
- **SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags must be preserved
  here if set during discovery** — do not strip.

## Field 16 — Notes
- Optional.
- Operational details, designation history, funding notes, boundary clarifications.
- Customer-facing — no provenance artifacts (IMP-014).

## Field 17 — URL
- Optional but strongly recommended.
- Full https:// URL to the primary authoritative network page.
- Semicolon-delimit if multiple authoritative URLs, including map URLs.

## Field 18 — Network ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Must be a valid integer matching the entity's network_id.
- Enables joins to the site_network_members relationship table.

------------------------------------------------------------
# 4. MULTI-COUNTY AND MULTI-STATE REPRESENTATION RULES

Site Networks are **not expanded** into multiple TSV rows.

- Multi-county Site Networks appear as a single TSV row.
- Counties: semicolon-delimited, alphabetized, no "County."
- States Included: semicolon-delimited, alphabetized, or blank for Ohio-only.

Example:
- Normalized counties: `Lucas;Wood`
- TSV Counties: `Lucas;Wood`
- Ohio-only → States Included: *(blank)*

------------------------------------------------------------
# 5. MEMBER SITE IDS SERIALIZATION RULES

The `member_site_ids` array and the parallel `member_site_names` array from the
normalized entity are each serialized as semicolon-delimited lists. Both lists
must maintain the same ordering so that position N in member_site_ids corresponds
to position N in member_site_names.

**member_site_ids:**
- Each value must be a valid Site entity ID in OH-{COUNTY}-S-{SEQ} format.
- No spaces around semicolons.
- Blank if the array is empty or no IDs have been resolved.
- Must not contain placeholder values.

**member_site_names:**
- Each value is the Name field of the corresponding member Site.
- Must have the same count of semicolon-delimited values as member_site_ids.
- Blank when member_site_ids is blank.

Example:
- member_site_ids: `OH-WD-S-001;OH-WD-S-047;OH-LU-S-112`
- member_site_names: `Maumee State Forest;Pearson Metropark;Oak Openings Preserve`

------------------------------------------------------------
# 6. DELIMITER RULES

- TSV uses tab characters only.
- Each row must contain exactly **17 tab characters** (18 fields → 17 delimiters).
- No field may contain a tab.
- No field may contain newline characters.

------------------------------------------------------------
# 7. BLANK-FIELD RULES

- Blank fields must be represented as true blanks: `\t\t`
- No spaces inside blank fields.
- No placeholder values (NULL, _, "", BLANK).

------------------------------------------------------------
# 8. WHITESPACE RULES

- No leading or trailing spaces in any field.
- No trailing spaces at end of line.
- Internal spaces allowed only when part of the field value.

------------------------------------------------------------
# 9. ROW CONSTRUCTION RULES

- Each row must contain exactly 18 fields.
- Each row must contain exactly 17 tabs.
- No field may be omitted.
- No field may be duplicated.
- Site Networks remain single rows.

------------------------------------------------------------
# 10. TSV GENERATION ALGORITHM

1.  Receive normalized Site Network record.
2.  Serialize Member Site IDs array to semicolon-delimited ID list.
2a. Serialize Member Site Names to semicolon-delimited name list (same order as IDs).
2b. Validate member_site_ids / member_site_names count parity (equal number of
    semicolon-delimited values, or both blank).
3.  Validate Counties formatting (semicolon-delimited, alphabetized, no "County").
4.  Validate States Included (semicolon-delimited, alphabetized, or blank).
5.  Validate Network Type (valid vocabulary value).
6.  Validate Org Type (valid vocabulary value or blank).
7.  Validate Status (valid vocabulary value or blank).
8.  Validate Member Site IDs (valid Site ID format or blank).
9.  Validate Member Count (integer or blank).
10. Validate Identity Notes (free text or blank; SITE_NETWORK_UNCERTAIN and
    SITE_NETWORK_PROVISIONAL flags preserved if present).
11. Validate no internal tabs.
12. Validate no internal newlines.
13. Validate whitespace rules.
14. Join fields with tab characters.
15. Validate delimiter count (must be 16).
16. Validate blank-field representation.
17. Emit row.

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 11. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 17 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Network Name is blank
- Governance is blank
- Network Type is blank or contains an invalid vocabulary value
- Org Type contains an invalid vocabulary value
- Status contains an invalid vocabulary value
- Counties field is not semicolon-delimited and alphabetized, or contains "County"
- States Included contains "Ohio" for an Ohio-only network
- Member Site IDs contains malformed ID values
- member_site_ids and member_site_names are not in sync (one blank, other populated,
  or unequal counts of semicolon-delimited values)
- Member Count is non-integer
- Network ID is missing or non-integer
- Field order is incorrect
- A field is missing or duplicated

All errors must be logged in the Audit & Logging Module v6.x.

------------------------------------------------------------
# 12. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters (expect 17 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting
- Validate States Included formatting
- Validate Member Site IDs are valid entity IDs and reference known Site entities
- Validate member_site_ids / member_site_names count parity (equal number of values)
- Validate Network Type, Org Type, and Status vocabulary values
- Verify SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags are
  preserved in Identity Notes if present
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Site Network Schema Module v6.0
- Site Network Vocabulary Module v6.0
- Site Network Normalization Contract v6.0
- TSV Integrity Check Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF SITE NETWORK TSV OUTPUT SPECIFICATION v6.0
