# NATURAL AREAS PROJECT
# TRAIL NETWORK NORMALIZATION CONTRACT v5.2
(Authoritative Field-Level Rules for Normalizing Resolved Trail Network Entities)

This module defines the v5.2 normalization rules applied by the
Normalization Engine v5.x to transform Resolved Trail Network entities into
Normalized Trail Network Objects ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Trail Network Vocabulary Module v5.3**.

This contract is authoritative for Trail Network normalization only.

------------------------------------------------------------
# CHANGES FROM v5.1 → v5.2

- **IMP-102 — Enforcement-grade vocabulary read gates**: Vocabulary
  mappings are no longer inline guidance; normalization must read the
  Trail Network Vocabulary Module v5.3 §6.x tables before normalizing
  any vocabulary-controlled field.
  - Workflow Step 3 added: mandatory read of Trail Network Vocabulary
    Module v5.2 §6.x before any vocabulary field normalization.
  - §5.2 Network Type updated: mandatory §6.1 read gate; null-and-log
    on unmappable values; REVIEW on compound values; references §6.4
    for ambiguous cases.
  - §5.3 Status updated: mandatory §6.2 read gate; "open"/"operational"
    → "Active" made explicit; null-and-log on unmappable values; REVIEW
    on ambiguous cases.
  - §5.20 Empty String Enforcement added: converts "" to null for
    network_type and status; runs after field-level normalization,
    before integrity anchor validation.
- Module dependency updated to Trail Network Vocabulary Module v5.3.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **identity_notes added**: New normalized field surfaced from
  identity_notes_raw; distinct from notes; used for identity
  clarifications, network vs. trail boundary questions, name
  conflicts, and membership uncertainty
- **maps simplified**: Rich array format (url/type/description objects)
  replaced by plain semicolon-delimited URL list; object validation
  steps removed; URL-only validation applies; consistent with Trail
  and Trail Segment
- **Derived Label removed**: No longer computed or stored at any stage
- **Raw input field renames**:
  - notes_raw → identity_notes_raw (identity clarifications)
  - url_all → urls_raw (all URLs)
  - url_primary → url_primary_raw
  - maps_raw object array → plain URL list
- **Normalization workflow updated**: Steps revised for removed and
  added fields; maps object validation replaced with URL list
  validation
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed — variants noted in Description
- `history` removed — merged into Description
- `county_list` → `counties` — renamed; alphabetized array
- `primary_managing_agency` → `governance` — renamed
- `secondary_managing_agencies` → `partner_agencies` — renamed
- `map_url` → `maps` — rich array (simplified to URL list in v5.1)
- `status` added
- `ownership` added
- `total_length_miles` added
- `member_trail_count` added
- `member_trail_ids` added (replaces name-string member list)

------------------------------------------------------------
# 1. PURPOSE

The Trail Network Normalization Contract v5.2 defines:

- How a Resolved Trail Network is transformed into a Normalized
  Trail Network
- How each Trail Network Schema v5.x field is validated and
  normalized
- How Network Type and Status are normalized using vocabulary read
  gates
- How Ownership, Governance, and Partner Agencies are handled
- How member Trail IDs are validated and linked
- How Total Length and Member Trail Count are derived
- How the Maps URL list is validated
- How Identity Notes are surfaced from identity_notes_raw
- How normalization interacts with the Normalization Engine v5.x
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the Entity Upsert Engine v5.x

Normalization must:
- Never invent data
- Never infer network type, membership, or jurisdiction
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v5.x, including:

- resolved identity key
- resolved entity_type = "Trail Network"
- resolved network_type, status
- resolved county set, states
- resolved governance, partner_agencies, ownership
- resolved member trail list
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.1
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
- member_trail_count_raw
- description_raw
- identity_notes_raw
- url_primary_raw
- urls_raw (all URLs)
- maps_raw (semicolon-delimited URL list)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Not applicable for Trail Networks:**
- No gps_lat_raw, gps_lon_raw — multi-location entities
- No address, township, municipality

## 2.3 Vocabulary Modules
- Trail Network Vocabulary Module v5.3 (Network Type, Status)

## 2.4 Schema Modules v5.x
- Trail Network Schema Module v5.x
- Trail Schema Module v5.x (for member Trail validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trail Network Object v5.2** conforming to the Trail
  Network Schema Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Trail Network from Normalization Engine v5.x
2.  Validate identity and entity_type = "Trail Network"
3.  **READ Trail Network Vocabulary Module v5.3 §6.x** — mandatory
    before normalizing any vocabulary-controlled field; do not proceed
    to Step 4 or Step 5 until §6.1 and §6.2 have been read
4.  Normalize Network Name
5.  Normalize Network Type (using §6.1 mapping table)
6.  Normalize Status (using §6.2 mapping table)
7.  Normalize Ownership
8.  Normalize Governance, Partner Agencies
9.  Normalize Counties, States Included
10. Normalize Total Length
11. Validate and link Member Trail IDs
12. Compute Member Trail Count from validated ID list
13. Normalize Description
14. Normalize Identity Notes
15. Normalize Notes
16. Normalize URL
17. Normalize Maps (URL list)
18. Run §5.20 Empty String Enforcement
19. Run integrity anchor deduplication check (via Normalization Engine)
20. Validate against Trail Network Schema v5.x
21. Emit Normalized Trail Network + provenance

If any critical step fails → return error to Normalization Engine v5.x.

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

**MANDATORY: Read Trail Network Vocabulary Module v5.3 §6.1 before
normalizing this field. Do not normalize network_type without first
reading the §6.1 mapping table.**

- Must match a controlled value from Trail Network Vocabulary
  Module v5.2 §2.1.
- Describes the identity-bearing type of the network.
- One value only.
- Must not be inferred from member count, geographic extent, or
  governance alone.

**Enforcement procedure (per §6.1):**
1. Read Trail Network Vocabulary Module v5.3 §6.1 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. If raw value maps to a controlled value → apply mapping; log.
4. If raw value is not in the §6.1 table → null-and-log; do not
   invent a mapping.
5. If raw value is compound (slash, comma, semicolon) → flag as
   REVIEW.
6. If raw value is ambiguous → see §6.4; flag as REVIEW if applicable.
7. "Other" may be used only when the entity type is documented but
   none of the controlled values apply.
8. NEVER use a value not in the §2.1 allowed values list.

**Provenance:** Log all vocabulary mappings applied. Log all null-and-log
decisions with the raw value. Log all REVIEW flags.

---

## 5.3 Status

**MANDATORY: Read Trail Network Vocabulary Module v5.3 §6.2 before
normalizing this field. Do not normalize status without first reading
the §6.2 mapping table.**

- Must match a controlled value from Trail Network Vocabulary Module
  v5.2 §2.x.
- "Planned" must be explicitly documented — never inferred.
- "Partially Open" applies when some member trails are open and others
  are not yet built.
- "Under Development" applies when the network is actively being
  assembled.
- Never infer from member trail statuses alone.
- Leave blank if status is ambiguous or undocumented.

**Enforcement procedure (per §6.2):**
1. Read Trail Network Vocabulary Module v5.3 §6.2 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. "open" and "operational" → "Active" explicitly; do not leave as raw.
4. If raw value is not in the §6.2 table → null-and-log; do not guess.
5. If raw value is ambiguous (e.g., "incomplete") → flag as REVIEW
   per §6.4.
6. Leave blank (null) if status is undocumented.

**Provenance:** Log all vocabulary mappings. Log null-and-log decisions
with raw value. Log REVIEW flags.

---

## 5.4 Ownership

- Optional — blank is correct and common.
- Many Trail Networks are coordinating bodies without land
  ownership — blank is valid and expected.
- When populated, must contain the **actual legal name** of the
  owning entity.
- Must not use generic categories.
- Must not encode governance or management.
- Only populate when a single entity demonstrably owns the
  network corridor or infrastructure.
- Leave blank if ownership is distributed or undocumented.

---

## 5.5 Governance

- Must contain the **actual name(s)** of the operational managing
  organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Many networks are coordinating bodies — governance may be a
  coalition or consortium.
- Leave blank if unverifiable.

---

## 5.6 Partner Agencies

- Must contain the **actual names** of formally documented partner
  organizations.
- Semicolon-delimit if multiple.
- Must not use generic categories.
- Must not duplicate Governance.
- Must not encode temporary volunteer activity or informal
  relationships.
- Leave blank if no documented partner agencies exist.

---

## 5.7 Counties

- Required if network is Ohio-based.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County."
- Must represent all counties the network spans.
- A multi-county network is **one entity** — never segmented.
- Never infer from member Trails alone unless explicitly documented.

---

## 5.8 States Included

- Use authoritative two-letter state abbreviations (e.g., OH, IN, KY).
- Semicolon-delimited if multiple.
- Alphabetized.
- Never infer from member Trails unless explicitly documented.
- **Leave blank for Ohio-only networks** — do not write "Ohio."

---

## 5.9 Total Length (Miles)

- Numeric only — no units, no ranges, no approximation symbols.
- Use officially published network length when available.
- **Never compute by summing member trail lengths** — published
  network lengths may reflect planned extensions, shared segments,
  or rounding conventions that differ from summed values.
- If published and computed lengths differ significantly → log
  the discrepancy; do not average or blend.
- Leave blank if not authoritatively documented.

---

## 5.10 Member Trail IDs

Member Trails are linked by **entity ID**, not name string.

**Normalization process:**
1. Collect resolved member trail references (names or raw IDs)
2. For each reference, look up the matching Trail entity ID in
   the Entity Graph
3. Record confirmed Trail entity IDs in `member_trail_ids`
4. IDs that cannot be resolved → log as warning, exclude from
   the list
5. If all member IDs are unresolvable → log warning, hold network
   for review

**Rules:**
- Must reference valid Trail entities in the Entity Graph
- Never infer membership from geographic overlap or trail names
  alone
- Never add member Trails not documented in authoritative sources
- If a member Trail is not yet in the Entity Graph → log warning,
  exclude for now; re-run after Trail is upserted
- Relationship table `trail_network_members` is populated from
  this validated ID list

**Provenance:** Log all membership resolutions, unresolved
references, and exclusions.

---

## 5.11 Member Trail Count

- Computed from the validated `member_trail_ids` list after
  normalization.
- Must equal the count of successfully resolved member Trail IDs.
- Never manually set or copied from source documentation.
- If member_trail_ids is empty or unresolved → member_trail_count
  = 0, flag for review.

**Note:** The officially published member count may differ from
the resolved count during active discovery phases. This is
expected. The Integrity Check should flag significant discrepancies
but not treat mismatches as hard errors.

---

## 5.12 Description

- 1-3 sentences describing identity-defining characteristics:
  purpose, geographic scope, character.
- Include naming history, alternate names, and significant origin
  or development milestones (formerly in separate `history` field).
- Must not include Trail-level or Segment-level details.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

---

## 5.13 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Network vs. trail boundary questions (is this a Trail or a
  Trail Network?)
- Name conflicts or ambiguities
- Membership uncertainty
- Vocabulary type flags (e.g., "source alternately calls this
  a 'trail' and a 'trail system' — may be Trail or Trail Network")
- Notes added during Resolution or Normalization passes

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.14 Notes

- Optional free text.
- Use for: operational details, gap documentation, planning status,
  funding notes, partial completion notes, contextual clarifications.
- Must not include identity-defining characteristics (those belong
  in Description or Identity Notes).
- Must not include Trail-level details.
- Must not contradict controlled fields.

---

## 5.15 URL

- Full https:// URL to primary authoritative source.
- Single value.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.16 Maps

- Semicolon-delimited list of URLs to network map resources.
- Trail Networks are linear spatial systems — multiple map formats
  (PDF strip maps, interactive viewers, GPX/KML files) are common.
- Each URL must be well-formed https://.
- Remove malformed URLs — log as warning.
- Remove duplicates.
- No embedded metadata (type, description) — URLs only.
- Leave blank if none.

**Validation rules:**
- Each entry must be a well-formed https:// URL
- No embedded metadata
- No empty segments (no consecutive semicolons)

---

## 5.17 Alternate Names — REMOVED IN v5.0

- `alternate_names` is no longer a field.
- Alternate or historical names → include in Description.
- If present in older resolved records → migrate to Description,
  then drop.

---

## 5.18 History — REMOVED IN v5.0

- `history` is no longer a separate field.
- Historical content → merge into Description.
- If present in older resolved records → merge into Description,
  then drop.

---

## 5.19 GPS / Township / Municipality

**Not applicable.** Trail Networks are multi-location entities.
- No gps_lat, gps_lon fields
- No plus_code
- No township, municipality
- The Normalization Engine does not run GIS derivation for Trail
  Networks

---

## 5.20 Empty String Enforcement

**When to run:** After field-level normalization (§5.2, §5.3),
before integrity anchor validation.

**Applies to:** network_type, status.

**Rule:** An empty string ("") is a data defect, not a valid blank.

**Procedure:**
1. Check network_type: if value is "" → set to null; log as
   normalization defect event with field name and entity ID.
2. Check status: if value is "" → set to null; log as normalization
   defect event with field name and entity ID.
3. Do not apply empty-string conversion to free-text fields
   (ownership, governance, description, notes, etc.) — those
   are handled by their own field rules.

**Provenance:** Each empty-string-to-null conversion must appear
in normalization_provenance as a defect event.

------------------------------------------------------------
# 6. MULTI-COUNTY AND MULTI-STATE NORMALIZATION RULES

- A Trail Network spanning multiple counties or states produces
  **one normalized entity**.
- `counties` must include all counties, alphabetized,
  semicolon-delimited.
- `states_included` must include all states, alphabetized,
  semicolon-delimited.
- **Leave states_included blank for Ohio-only networks.**
- Never segment multi-county or multi-state networks.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trail Networks is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v5.x runs the deduplication check after
this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Network Type maps to valid vocabulary value (Trail Network
  Vocabulary Module v5.2 §2.1)
- Status maps to valid vocabulary value (if present)
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Total Length: numeric only, no units
- Member Trail IDs: each ID references valid Trail in Entity Graph
- Member Trail Count: equals count of validated IDs
- Maps: each entry is a well-formed https:// URL; no embedded
  metadata; no empty segments
- Semicolon formatting: trimmed, no empty segments
- No invented data
- Blank fields are true blanks (not empty strings)
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
- Log conflict.

### 10.2 Conflicting Network Type
- Use authoritative regional or statewide sources.
- If unclear → leave blank, flag in identity_notes.

### 10.3 Conflicting Membership
- Preserve all claims in provenance.
- Include only confirmed, resolved Trail IDs in member_trail_ids.
- Log unresolved membership claims.

### 10.4 Conflicting Total Length
- Use most authoritative source (managing organization preferred).
- Log conflict; note discrepancy.

### 10.5 Conflicting Counties or States
- Use most authoritative source.
- Preserve all claims in provenance.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate total length.
- Never infer network type from member trails alone.
- Never infer membership from geographic proximity.
- Never infer counties or states from member trail counties.
- Blank ownership is correct and common.
- Blank states_included is correct for Ohio-only networks.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- Confirmation that Trail Network Vocabulary Module v5.3 §6.x
  was read before normalizing vocabulary-controlled fields
- All vocabulary mappings applied (Network Type, Status) with
  raw value and mapped value
- All null-and-log decisions with raw value and field name
- All REVIEW flags with raw value and field name
- All empty-string-to-null conversions (§5.20 defect events)
- Member Trail ID resolution results (resolved / unresolved /
  excluded)
- Member Trail Count derivation
- Total Length source and any discrepancy notes
- Alternate names and history migration to Description (if applicable)
- Maps URL validation results (valid/invalid URLs, duplicates removed)
- Identity Notes content surfaced from identity_notes_raw
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Trail Network Vocabulary Module v5.3
- Trail Network Schema Module v5.x
- Trail Schema Module v5.x (for member Trail validation)
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF TRAIL NETWORK NORMALIZATION CONTRACT v5.2
