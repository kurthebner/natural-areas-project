# NATURAL AREAS PROJECT
# TRAILTHING TSV OUTPUT SPECIFICATION v6.0
(Authoritative Formatting-Layer Specification for Normalized Trailthing Entities)

This module defines the authoritative, deterministic rules for serializing
normalized Trailthing entities into tab-separated values (TSV) with guaranteed
delimiter integrity, zero drift, and full compatibility with the v6.x ontology.

This module contains no controlled vocabularies.
All vocabularies are defined in the Trailthing Vocabulary Module v6.0.
All field definitions are defined in the Trailthing Schema Module v6.0.
All normalization rules are defined in the Trailthing Normalization Contract v6.0.

This module is new in v6.0. It supersedes the Trail TSV Output Specification v5.1,
the Trail Segment TSV Output Specification v5.1, and the Trail Network TSV Output
Specification v5.1, which are retired.

------------------------------------------------------------
# 1. PURPOSE

This specification defines:

- The canonical TSV field order for Trailthings
- Delimiter rules
- Blank-field rules
- Whitespace rules
- Maps field serialization rules
- Parent and hierarchy field serialization rules
- Multi-county representation rules
- Validation requirements
- Error conditions
- Integration with the TSV Integrity Check Module v6.x

This specification is authoritative for Trailthing TSV formatting.

------------------------------------------------------------
# 2. FIELD ORDER (CANONICAL v6.0)

Trailthing TSV output must contain exactly **31 fields** in the following order:

1.  name
2.  alternate_names
3.  source_term
4.  source_hierarchy_context
5.  parent_id
6.  parent_name *(human-readable name of parent Trailthing)*
7.  site_parent_id
8.  site_parent_name *(human-readable name of parent Site)*
9.  parent_site_network_id
10. parent_site_network_name *(human-readable name of parent Site Network)*
11. use_type
12. surface_type
13. origin_type
14. org_type
15. status
16. difficulty
17. accessibility
18. ownership
19. governance
20. partner_agencies
21. coordination
22. counties
23. states_included
24. total_length
25. description
26. trail_history
27. identity_notes
28. notes
29. url
30. maps
31. trailthing_id

This order is absolute and must never change.
No additional fields may be added.
No fields may be removed or reordered.

**31 fields = 30 tab delimiters per row.**

*(Note: earlier drafts of this spec stated 32 fields / 31 tabs. The correct count is 31 fields / 30 tabs, reflecting the removal of the External Parent Type field when the rename to parent_site_network_id was finalized.)*

**Cross-entity reference rule**: Every field that references another entity by ID
must be immediately followed by a field containing that entity's human-readable
name. Three cross-entity reference pairs exist in this TSV:
- `parent_id` (pos 5) / `parent_name` (pos 6) — parent Trailthing
- `site_parent_id` (pos 7) / `site_parent_name` (pos 8) — parent Site
- `parent_site_network_id` (pos 9) / `parent_site_network_name` (pos 10) — parent Site Network
All three pairs are blank for top-level Trailthings with no documented parents.

------------------------------------------------------------
# 3. FIELD NOTES

## Field 1 — Name
- Required; must never be blank.
- Official published name.
- Must be unique statewide (case-insensitive).

## Field 2 — Alternate Names
- Optional.
- Semicolon-delimited list of documented historical or variant names.
- Must not repeat Name.
- Blank if none documented.

## Field 3 — Source Term
- Required (WARN if blank — indicates a discovery gap).
- Verbatim term used by the authoritative source to describe this entity's kind.
- Examples: "trail system", "greenway", "water trail", "connector", "loop trail".
- Must not be normalized or mapped to a controlled vocabulary.
- This field is the primary input for future Trailthing hierarchy analysis.

## Field 4 — Source Hierarchy Context
- Optional.
- Verbatim or close paraphrase of how the source frames this entity in relation
  to others.
- Blank if the source provides no hierarchical context.

## Field 5 — Parent ID
- Optional.
- Trailthing ID (OH-{COUNTY}-TT-{SEQ} or OH-MC-TT-{SEQ}) of the parent Trailthing.
- Blank for top-level Trailthings.

## Field 6 — Parent Name
- The Name field of the parent Trailthing referenced by parent_id.
- Blank when parent_id is blank.
- Both parent_id and parent_name must be blank together or populated together.

## Field 7 — Site Parent ID
- Optional.
- Site ID (OH-{COUNTY}-S-{SEQ}) of the parent Site.
- Blank if not wholly contained within and access-dependent on a single Site.

## Field 8 — Site Parent Name
- The Name field of the parent Site referenced by site_parent_id.
- Blank when site_parent_id is blank.
- Both site_parent_id and site_parent_name must be blank together or populated together.

## Field 9 — Parent Site Network ID
- Optional.
- Network ID (OH-{COUNTY}-SN-{SEQ} or OH-MC-SN-{SEQ}) of the parent Site Network.
- Blank if no Site Network parent relationship is documented.

## Field 10 — Parent Site Network Name
- The Network Name of the Site Network referenced by parent_site_network_id.
- Blank when parent_site_network_id is blank.
- Both parent_site_network_id and parent_site_network_name must be blank together
  or populated together.

## Field 11 — Use Type
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- Single value only. Blank if not explicitly documented by authoritative source.

## Field 12 — Surface Type
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- Single value only. "Mixed" only when explicitly documented.
- Blank if not documented.

## Field 13 — Origin Type
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- Single value only. Must not be inferred.
- Blank if not documented.

## Field 14 — Org Type
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- Classifies the organizational category of the primary governance entity.
- Blank if not documented.

## Field 15 — Status
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- "Planned", "Gap", and "Closed" must be explicitly documented.
- Blank if not documented.

## Field 16 — Difficulty
- Optional.
- Must match a controlled value from Trailthing Vocabulary Module v6.0.
- Only populate when explicitly stated by an authoritative source.
- Must not be assessed or inferred.
- Blank if not documented.

## Field 17 — Accessibility
- Optional.
- Free-text. No controlled vocabulary.
- Blank if not documented.

## Field 18 — Ownership
- Optional.
- Legal name of the entity that owns the corridor.
- Blank is correct and common.

## Field 19 — Governance
- Primary managing/coordinating organization.
- Semicolon-delimited if multiple co-managers.

## Field 20 — Partner Agencies
- Optional.
- Semicolon-delimited list of secondary managing agencies.
- Must not duplicate Governance.

## Field 21 — Coordination
- Optional.
- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Governance or Partner Agencies.

## Field 22 — Counties
- Required.
- Semicolon-delimited, alphabetized list of county names.
- Must not include "County."
- Multi-county Trailthings remain single rows.

## Field 23 — States Included
- Optional.
- Semicolon-delimited, alphabetized list of state abbreviations.
- Blank for Ohio-only Trailthings.

## Field 24 — Total Length
- Optional.
- Numeric only — no units, no ranges.
- Blank if unknown.

## Field 25 — Description
- Optional but strongly recommended.
- 1-3 sentences on identity, character, and physical/ecological setting.

## Field 26 — Trail History
- Optional.
- Documented historical context (rail corridor origin, canal conversion, etc.)

## Field 27 — Identity Notes
- Optional.
- Identity clarifications, hierarchy uncertainty flags, PARTIAL MEMBERSHIP notes,
  TRAIL_HIERARCHY_UNCERTAIN flags, cross-entity relationship notes.

## Field 28 — Notes
- Optional.
- Operational details, gap documentation, surface/governance variation,
  access restrictions, seasonal conditions.
- Customer-facing — no provenance artifacts (IMP-014).

## Field 29 — URL
- Optional but strongly recommended.
- Full https:// URL(s) to primary authoritative source.
- Semicolon-delimited if multiple.
- Tracking parameters removed.

## Field 30 — Maps
- Optional.
- Semicolon-delimited list of URLs to trail map resources.
- PDF trail maps, GPX/KML files, interactive map viewers, GIS layers.
- Each entry must be a well-formed https:// URL — no embedded metadata.
- Distinct from URL field.
- Blank if no maps documented.

## Field 31 — Trailthing ID
- Internal entity ID.
- Required for referential integrity and downstream processing.
- Format: OH-{COUNTY}-TT-{SEQ} or OH-MC-TT-{SEQ}
- Enables joins to trailthing_hierarchy and access_point_parents relationship tables.

------------------------------------------------------------
# 4. MULTI-COUNTY REPRESENTATION RULES

Trailthings are **not expanded** into multiple TSV rows.

- The Counties field must contain a semicolon-delimited, alphabetized list
  without the word "County."
- A Trailthing must appear as a single TSV row regardless of how many counties
  it traverses.
- No inference permitted; only documented counties included.

Example:
- Normalized counties: `Delaware;Franklin;Union`
- TSV output: `Delaware;Franklin;Union`

------------------------------------------------------------
# 5. MAPS FIELD SERIALIZATION RULES

The `maps` field is a semicolon-delimited list of https:// URLs:

- Each entry must be a well-formed https:// URL.
- No embedded metadata (no type labels, no descriptions).
- No spaces around semicolons.
- No empty segments.
- Blank if no map resources exist.

Example:
`https://example.org/maps/trail.pdf;https://example.org/trails/interactive;https://example.org/gpx/trail.gpx`

------------------------------------------------------------
# 6. HIERARCHY FIELD RULES

### parent_id + parent_name (Fields 5–6)
- `parent_id` references the parent Trailthing by entity ID.
- `parent_name` is the human-readable Name of that Trailthing.
- Both blank for top-level Trailthings; both populated together when a parent exists.
- Enables hierarchical joins via the `trailthing_hierarchy` relationship table.

### site_parent_id + site_parent_name (Fields 7–8)
- `site_parent_id` references the parent Site by entity ID.
- `site_parent_name` is the human-readable Name of that Site.
- Both blank when no site parent exists; both populated together when populated.
- Populated only when the source explicitly frames containment/access-dependency.

### parent_site_network_id + parent_site_network_name (Fields 9–10)
- `parent_site_network_id` references the parent Site Network by network_id.
- `parent_site_network_name` is the human-readable name of that Site Network.
- Both fields must be blank together or populated together.

------------------------------------------------------------
# 7. DELIMITER RULES

- TSV uses tab characters only.
- Each row must contain exactly **30 tab characters** (31 fields → 30 delimiters).
- No field may contain a tab.
- No field may contain newline characters.

------------------------------------------------------------
# 8. BLANK-FIELD RULES

- Blank fields must be represented as true blanks: `\t\t`
- No spaces inside blank fields.
- No placeholder values (NULL, _, "", BLANK).

------------------------------------------------------------
# 9. WHITESPACE RULES

- No leading or trailing spaces in any field.
- No trailing spaces at end of line.
- Internal spaces allowed only when part of the field value.

------------------------------------------------------------
# 10. ROW CONSTRUCTION RULES

- Each row must contain exactly 31 fields.
- Each row must contain exactly 30 tabs.
- No field may be omitted.
- No field may be duplicated.
- Multi-county Trailthings remain single rows.

------------------------------------------------------------
# 11. TSV GENERATION ALGORITHM

1.  Receive normalized 32-field Trailthing record.
2.  Validate source_term (WARN if blank — discovery gap).
3.  Validate Maps field (each entry a well-formed https:// URL; no embedded
    metadata; no empty segments).
4.  Validate Counties formatting (semicolon-delimited, alphabetized, no "County").
5.  Validate States Included (semicolon-delimited, alphabetized, or blank).
6.  Validate Alternate Names (semicolon-delimited, no duplicates, not same as Name).
7.  Validate Use Type (valid vocabulary value or blank).
8.  Validate Surface Type (valid vocabulary value or blank).
9.  Validate Origin Type (valid vocabulary value or blank).
10. Validate Org Type (valid vocabulary value or blank).
11. Validate Status (valid vocabulary value or blank).
12. Validate Difficulty (valid vocabulary value or blank).
13. Validate Total Length (numeric only or blank).
14. Validate parent_id / parent_name pairing (both blank or both populated).
15. Validate site_parent_id / site_parent_name pairing (both blank or both populated).
16. Validate parent_site_network_id / parent_site_network_name pairing (both blank or both populated).
17. Validate no internal tabs.
18. Validate no internal newlines.
19. Validate whitespace rules.
20. Join fields with tab characters.
21. Validate delimiter count (must be 30).
22. Validate blank-field representation.
23. Emit row.

If any step fails, TSV generation halts and surfaces an error.

------------------------------------------------------------
# 12. ERROR CONDITIONS

TSV generation must halt if:

- A row contains ≠ 30 tabs
- A field contains a tab
- A field contains a newline
- A blank field contains spaces
- A field contains trailing spaces
- Name is blank
- Counties field is not semicolon-delimited and alphabetized, or contains "County"
- Use Type, Surface Type, Origin Type, Org Type, Status, or Difficulty contains
  an invalid vocabulary value
- Total Length contains non-numeric content
- Maps field contains embedded metadata or malformed URLs
- parent_site_network_id is populated without parent_site_network_name (or vice versa)
- parent_id and parent_name are not in sync (one blank, other populated)
- site_parent_id and site_parent_name are not in sync (one blank, other populated)
- Trailthing ID is missing or malformed
- Field order is incorrect
- A field is missing or duplicated

All errors must be logged in the Audit & Logging Module v6.x.

------------------------------------------------------------
# 13. INTEGRATION WITH TSV INTEGRITY CHECK

The TSV Integrity Check must:

- Recount delimiters (expect 31 per row)
- Revalidate blank-field representation
- Revalidate whitespace rules
- Validate Counties formatting
- Validate Maps field (well-formed https:// URLs, no embedded metadata)
- Validate all vocabulary-controlled field values
- Validate Total Length is numeric
- Validate Trailthing ID format
- Validate source_term presence (WARN if blank)
- Surface anomalies
- Halt finalization if any row fails

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This module depends on:

- Trailthing Schema Module v6.0
- Trailthing Vocabulary Module v6.0
- Trailthing Normalization Contract v6.0
- TSV Integrity Check Module v6.x *(or v5.x)*
- Audit & Logging Module v6.x *(or v5.x)*

------------------------------------------------------------
# END OF TRAILTHING TSV OUTPUT SPECIFICATION v6.0
