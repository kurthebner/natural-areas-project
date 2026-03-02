# NATURAL AREAS PROJECT
# TRAIL NETWORK NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Trail Network Entities)

This module defines the v5.0 normalization rules applied by the
Normalization Engine v5.0 to transform Resolved Trail Network entities into
Normalized Trail Network Objects v5.0 ready for insertion into the
Entity Graph Schema v5.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.0**.

This contract is authoritative for Trail Network normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`alternate_names` removed**: Rarely documented; variants noted in Description instead
- **`history` removed**: Merged into Description
- **`county_list` → `counties`**: Renamed; alphabetized array
- **`primary_managing_agency` → `governance`**: Renamed
- **`secondary_managing_agencies` → `partner_agencies`**: Renamed
- **`map_url` → `maps`**: Rich array format (url / type / description objects)
- **`status` added**: Was missing from v4.0; must match Trail Network Vocabulary v5.0
- **`ownership` added**: Optional — meaningful for single-owner networks
- **`total_length_miles` added**: Optional numeric field
- **`member_trail_count` added**: Computed from validated member_trail_ids list
- **`member_trail_ids` added**: Array of Trail entity IDs (replaces name-string member list)
- **Member Trails now linked by ID not name**: Relationship table populated from member_trail_ids
- **Derived Label**: Computed at TSV output time, NOT during normalization (changed from v4.0)
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Normalization Contract v5.0 defines:

- How a Resolved Trail Network is transformed into a Normalized Trail Network
- How each Trail Network Schema v5.0 field is validated and normalized
- How Network Type and Status are normalized
- How Ownership, Governance, and Partner Agencies are handled
- How member Trail IDs are validated and linked
- How Total Length and Member Trail Count are derived
- How the Maps rich array is validated
- How normalization interacts with the **Normalization Engine v5.0**
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the **Entity Upsert Engine v5.0**

Normalization must:

- Never invent data
- Never infer network type, membership, or jurisdiction
- Never silently correct malformed values
- Always log normalization decisions

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From **Resolution Engine v5.0**, including:

- resolved identity key
- resolved entity_type = "Trail Network"
- resolved network_type, status
- resolved county set, states
- resolved governance, partner_agencies, ownership
- resolved member trail list
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
Including:

- network_name_raw
- network_type_raw
- status_raw
- ownership_raw
- governance_raw
- partner_agencies_raw
- counties_raw
- states_raw
- total_length_miles_raw
- member_trails_raw (names or IDs)
- description_raw
- notes_raw
- url_raw
- maps_raw (array of url/type/description objects)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v4.0 raw inputs:**
- alternate_names_raw — field no longer exists
- history_raw — merged into description_raw

**Not applicable for Trail Networks:**
- No gps_raw (networks are multi-location — no single GPS point)
- No address, township, municipality

## 2.3 Vocabulary Modules v5.0
- Trail Network Vocabulary Module v5.0 (Network Type, Status)

## 2.4 Schema Modules v5.0
- Trail Network Schema Module v5.0
- Trail Schema Module v5.0 (for member Trail validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Network Object v5.0** conforming to the Trail Network Schema Module v5.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Trail Network from Normalization Engine v5.0
2. Validate identity and entity_type = "Trail Network"
3. Normalize Network Name
4. Normalize Network Type
5. Normalize Status
6. Normalize Ownership
7. Normalize Governance, Partner Agencies
8. Normalize Counties, States Included
9. Normalize Total Length
10. Validate and link Member Trail IDs
11. Compute Member Trail Count from validated ID list
12. Normalize Description
13. Normalize Notes
14. Normalize URL
15. Normalize Maps (rich array)
16. Run integrity anchor deduplication check (via Normalization Engine)
17. Validate against Trail Network Schema v5.0
18. Emit Normalized Trail Network + provenance

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Network Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors.
- Must not encode hierarchy or governance.
- Alternate or historical names → Description, not Network Name.
- Never infer names from member Trails or branding.

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Network Type

- Must match a controlled value from Trail Network Vocabulary Module v5.0.
- Describes the identity-bearing type of the network.
- Must not be inferred from number of trails, geographic extent, or governance alone.
- If ambiguous → leave blank and log uncertainty.

**Common normalization mappings:**
- "regional greenway" → "Regional Greenway System"
- "statewide trail" → "Statewide Trail System"
- "water trail" → "Water Trail Network"
- "county trail system" → "County Trail Network"
- See Trail Network Vocabulary Module v5.0 Section 4 for full mapping table.

---

## 5.3 Status ✨ NEW IN v5.0

- Must match a controlled value from Trail Network Vocabulary Module v5.0.
- "Planned" must be explicitly documented — not inferred from lack of development.
- "Partially Open" applies when some member trails are open and others are not yet built.
- "Under Development" applies when the network is actively being assembled.
- Never infer from member trail statuses alone.
- Leave blank if status is ambiguous or undocumented.

**Common normalization mappings:**
- "open", "operational" → "Active"
- "in development", "under construction" → "Under Development"
- "partial", "some sections open" → "Partially Open"
- "proposed", "planned" → "Planned"
- "inactive", "dormant" → "Closed"

---

## 5.4 Ownership ✨ NEW IN v5.0

- Optional — blank is correct and common.
- Many Trail Networks are coordinating bodies without land ownership — blank is valid.
- When populated, must contain the **actual legal name** of the owning entity.
- Must not use generic categories.
- Must not encode governance or management.
- Only populate when a single entity demonstrably owns the network corridor or infrastructure.

**Examples:**
- ✅ "Ohio Department of Natural Resources" (owns the rail corridor)
- ✅ "Wood County Park District" (owns all member trail land)
- ❌ "Multiple Agencies" — too vague; leave blank
- ❌ "State of Ohio" — too generic unless legally precise

---

## 5.5 Governance ✨ RENAMED FROM v4.0 (was `primary_managing_agency`)

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Many networks are coordinating bodies — governance may be a coalition or consortium.
- Leave blank if unverifiable.

---

## 5.6 Partner Agencies ✨ RENAMED FROM v4.0 (was `secondary_managing_agencies`)

- Must contain the **actual names** of formally documented partner organizations.
- Semicolon-delimit if multiple.
- Must not use generic categories.
- Must not duplicate Governance.
- Must not encode temporary volunteer activity or informal relationships.
- Leave blank if no documented partner agencies exist.

---

## 5.7 Counties ✨ RENAMED FROM v4.0 (was `county_list`)

- Required if network is Ohio-based.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County".
- Must represent all counties the network spans.
- A multi-county network is **one entity** — never segmented.
- Never infer from member Trails alone unless explicitly documented.

---

## 5.8 States Included

- Use authoritative two-letter state abbreviations (e.g., OH, IN, KY).
- Semicolon-delimited if multiple.
- Alphabetized.
- Never infer from member Trails unless explicitly documented.
- Leave blank for single-state networks (Ohio-only is implied).

---

## 5.9 Total Length (Miles) ✨ NEW IN v5.0

- Numeric only — no units, no ranges, no approximation symbols.
- Represents the total documented length of the network.
- Never estimate or sum from member trail lengths unless source explicitly does so.
- If sources conflict → use most authoritative source (managing organization preferred).
- Leave blank if not authoritatively documented.

---

## 5.10 Member Trail IDs ✨ NEW IN v5.0 (replaces name-string list)

Member Trails are now linked by **entity ID**, not name string.

**Normalization process:**
1. Collect resolved member trail references (names or raw IDs from discovery)
2. For each reference, look up the matching Trail entity ID in the Entity Graph
3. Record the confirmed Trail entity IDs in `member_trail_ids`
4. IDs that cannot be resolved → log as warning, exclude from the list
5. If all member IDs are unresolvable → log as warning, hold network for review

**Rules:**
- Must reference valid Trail entities in the Entity Graph
- Never infer membership from geographic overlap or trail names alone
- Never add member Trails not documented in authoritative sources
- If a member Trail is not yet in the Entity Graph → log warning, exclude for now; re-run after Trail is upserted
- Relationship table `trail_to_network` is populated from this validated ID list

**Provenance:** Log all membership resolutions, unresolved references, and exclusions.

---

## 5.11 Member Trail Count ✨ NEW IN v5.0

- Computed from the validated `member_trail_ids` list after normalization.
- Must equal the count of successfully resolved member Trail IDs.
- Never manually set or copied from source documentation.
- If member_trail_ids is empty or unresolved → member_trail_count = 0, flag for review.

---

## 5.12 Description ✨ UPDATED FROM v4.0 (absorbs `history`)

- 1-3 sentences.
- Must describe identity-defining characteristics of the network: purpose, geographic scope, character.
- Include naming history, alternate names, and significant origin or development milestones
  (formerly in `history` field — now merged here).
- Must not include Trail-level or Segment-level details.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

---

## 5.13 Alternate Names ✨ REMOVED IN v5.0

- `alternate_names` is no longer a field in the Trail Network schema.
- Alternate or historical names → include in Description.
- If alternate_names values are present in resolved records from older discovery runs → migrate relevant names to Description, then drop the field.

---

## 5.14 History ✨ REMOVED IN v5.0

- `history` is no longer a separate field in the Trail Network schema.
- Historical content → merge into Description.
- If history values are present in resolved records from older discovery runs → merge into Description, then drop the field.

---

## 5.15 Notes

- Optional free text.
- Use for: operational details, gap documentation, planning status, funding notes, contextual clarifications.
- Must not include identity-defining characteristics (those belong in Description).
- Must not include Trail-level details.
- Must not contradict controlled fields.

---

## 5.16 URL

- Full https:// URL to primary authoritative source.
- Single value.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.17 Maps ✨ NEW IN v5.0 (replaces `map_url`)

The `maps` field is a **rich array** — each element is an object with:
- `url` (required) — full https:// URL
- `type` (required) — one of: PDF, Interactive, Static Image, GIS Layer, Other
- `description` (optional) — brief description of what the map shows

**Normalization rules:**
- Validate each element: url must be well-formed https://; type must match allowed values
- Remove elements with malformed URLs — log as warning
- Remove elements with missing type — log as warning
- `description` may be blank — that is valid
- Preserve order from resolution — do not sort
- Semicolon-delimited in TSV output (urls only); full array in JSON

---

## 5.18 GPS / Township / Municipality

**Not applicable.** Trail Networks are multi-location entities.
- No gps_lat, gps_lon fields
- No plus_code
- No township, municipality
- The Normalization Engine does not run GIS derivation for Trail Networks

------------------------------------------------------------
# 6. MULTI-COUNTY AND MULTI-STATE NORMALIZATION RULES

- A Trail Network spanning multiple counties or states produces **one normalized entity**.
- `counties` must include all counties, alphabetized, semicolon-delimited.
- `states_included` must include all states, alphabetized, semicolon-delimited.
- Never segment multi-county or multi-state networks.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trail Networks is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v5.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Network Type maps to valid vocabulary value
- Status maps to valid vocabulary value (if present)
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Total Length: numeric only, no units
- Member Trail IDs: each ID references valid Trail in Entity Graph
- Member Trail Count: equals count of validated IDs
- Maps array: each element has valid url and type
- Semicolon formatting: trimmed, no empty segments
- No invented data
- Blank fields are true blanks
- No delimiter characters inside field values

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

Normalization must ensure:

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 10. CONFLICT HANDLING

### 10.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Description.
- Log conflict in normalization provenance.

### 10.2 Conflicting Network Type
- Use authoritative regional or statewide sources.
- If unclear → leave blank, flag uncertainty.

### 10.3 Conflicting Membership
- Preserve all claims in provenance.
- Include only confirmed, resolved Trail IDs in member_trail_ids.
- Log unresolved membership claims.

### 10.4 Conflicting Jurisdiction
- Use the most authoritative source.
- Preserve all claims in provenance.

### 10.5 Conflicting Total Length
- Use most authoritative source (managing organization preferred).
- Log conflict.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate total length.
- Never infer network type from member trails alone.
- Never infer membership from geographic proximity.
- Never infer counties or states from member trail counties.
- Blank ownership is correct and common — do not fill with governance.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (Network Type, Status)
- Member Trail ID resolution results (resolved / unresolved / excluded)
- Member Trail Count derivation
- Total Length source
- Alternate names and history migration to Description (if applicable)
- Maps array validation results
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Network Vocabulary Module v5.0
- Trail Network Schema Module v5.0
- Trail Schema Module v5.0 (for member Trail validation)
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF TRAIL NETWORK NORMALIZATION CONTRACT v5.0
