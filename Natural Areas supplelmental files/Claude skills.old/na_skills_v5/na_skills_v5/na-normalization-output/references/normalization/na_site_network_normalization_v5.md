# NATURAL AREAS PROJECT
# SITE NETWORK NORMALIZATION CONTRACT v5.0
(Authoritative Field-Level Rules for Normalizing Resolved Site Network Entities)

This module defines the v5.0 normalization rules applied by the
Normalization Engine v5.0 to transform Resolved Site Network entities into
Normalized Site Network Objects v5.0 ready for insertion into the
Entity Graph Schema v5.0.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.0**.

This contract is authoritative for Site Network normalization only.

------------------------------------------------------------
# CHANGES FROM v4.0

- **`alternate_names` removed**: Rarely documented; variants noted in Description instead
- **`history` removed**: Merged into Description
- **`network_affiliation` removed**: Cleaner architecture without nested affiliations
- **`counties_traversed` → `counties`**: Renamed; alphabetized array
- **`primary_managing_agency` → `governance`**: Renamed
- **`secondary_managing_agencies` → `partner_agencies`**: Renamed
- **`ownership` added**: Optional — who legally owns or established the network
- **`member_count` added**: Computed from validated member_site_ids list
- **`member_site_ids` added**: Array of Site entity IDs (replaces name-string member list)
- **`map_url` retained**: Simple URL field — no rich array (unlike Trail Networks)
- **Status vocabulary differs from Trail Network**: Active, Proposed, Under Development, Inactive, Dissolved
- Updated all version references to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Site Network Normalization Contract v5.0 defines:

- How a Resolved Site Network becomes a Normalized Site Network
- How each Site Network Schema v5.0 field is validated and normalized
- How Network Type and Status are normalized
- How Ownership, Governance, and Partner Agencies are handled
- How member Site IDs are validated and linked
- How Member Count is derived
- How normalization interacts with the **Normalization Engine v5.0**
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the **Entity Upsert Engine v5.0**

Normalization must:

- Never invent data
- Never infer membership, governance, or identity
- Never silently correct malformed values
- Always log normalization decisions

Derived Label is not computed here.
It is computed only during TSV output.

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From **Resolution Engine v5.0**, including:

- resolved identity key
- resolved entity_type = "Site Network"
- resolved network_type, status
- resolved county set, state set
- resolved governance, partner_agencies, ownership
- resolved member Site set (if any)
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v5.0
Including:

- name_raw
- network_type_raw
- status_raw
- ownership_raw
- governance_raw
- partner_agencies_raw
- counties_raw
- states_raw
- member_sites_raw (names or IDs)
- description_raw
- notes_raw
- url_raw
- map_url_raw
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v4.0 raw inputs:**
- alternate_names_raw — field no longer exists
- history_raw — merged into description_raw
- network_affiliation_raw — field no longer exists

**Not applicable for Site Networks:**
- No gps_raw (networks are multi-location — no single GPS point)
- No address, township, municipality

## 2.3 Vocabulary Modules v5.0
- Site Network Vocabulary Module v5.0 (Network Type, Status)

## 2.4 Schema Modules v5.0
- Site Network Schema Module v5.0
- Site Schema Module v5.0 (for member Site validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Network Object v5.0** conforming to the Site Network Schema Module v5.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.0**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1. Receive Resolved Site Network from Normalization Engine v5.0
2. Validate identity and entity_type = "Site Network"
3. Normalize Network Name
4. Normalize Network Type
5. Normalize Status
6. Normalize Ownership
7. Normalize Governance, Partner Agencies
8. Normalize Counties, States Included
9. Validate and link Member Site IDs
10. Compute Member Count from validated ID list
11. Normalize Description
12. Normalize Notes
13. Normalize URL
14. Normalize Map URL
15. Run integrity anchor deduplication check (via Normalization Engine)
16. Validate against Site Network Schema v5.0
17. Emit Normalized Site Network + provenance

If any critical step fails → return error to Normalization Engine v5.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Network Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors or hierarchy encodings.
- Alternate or historical names → Description, not Network Name.
- Never infer names from member Sites or branding.

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Network Type

- Must match a controlled value from Site Network Vocabulary Module v5.0.
- Describes the identity-bearing classification of the network.
- Must not encode governance, ownership, or hierarchy.
- Must not be inferred from member Sites, geography, or management alone.
- If ambiguous → leave blank and log uncertainty.

**Common normalization mappings:**
- "national heritage area" → "National Heritage Area"
- "local historic district" → "Local Historic District"
- "scenic river corridor" → "Scenic River Corridor"
- "watershed network" → "Watershed Network"
- "greenway network" → "Greenway Network"
- "land trust preserve network" → "Multi-Site Conservation Network"
- See Site Network Vocabulary Module v5.0 Section 4 for full mapping table.

---

## 5.3 Status

- Must match a controlled value from Site Network Vocabulary Module v5.0.
- Site Network status vocabulary differs from Trail Network — use the correct module.

**Allowed values and guidance:**
- **Active** — network is currently operational and recognized
- **Proposed** — must be explicitly documented; not inferred from planning activity
- **Under Development** — actively being assembled; not yet operational
- **Inactive** — network exists but is no longer actively maintained or promoted
- **Dissolved** — network has been formally disbanded; use only when explicitly documented

**Key distinctions from Trail Network status:**
- No "Partially Open" value — Site Networks are formal designations, not trail systems being built out
- "Dissolved" is specific to Site Networks — formal designations can be revoked or disbanded
- "Inactive" covers dormant networks that still formally exist

Never infer status from member Site statuses alone.
Leave blank if status is ambiguous or undocumented.

---

## 5.4 Ownership ✨ NEW IN v5.0

- Optional — blank is correct and common.
- Many Site Networks are formal designations (NHAs, historic districts) without land ownership — blank is valid.
- When populated, must contain the **actual legal name** of the entity that owns or established the network.
- Must not use generic categories.
- Must not encode governance or management.

**Examples:**
- ✅ "National Park Service" (for a NPS-administered NHA)
- ✅ "Maumee Valley Land Trust" (owns all member preserve lands)
- ❌ "Federal Government" — too generic
- ❌ "Multiple Owners" — leave blank instead

---

## 5.5 Governance ✨ RENAMED FROM v4.0 (was `primary_managing_agency`)

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Many networks are formal designations managed by coordinating bodies — governance may be a partnership.
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

## 5.7 Counties ✨ RENAMED FROM v4.0 (was `counties_traversed`)

- Required if network is Ohio-based.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County".
- Must represent all counties the network spans.
- A multi-county network is **one entity** — never segmented.
- Never infer from member Sites alone unless explicitly documented.

---

## 5.8 States Included

- Use authoritative two-letter state abbreviations (e.g., OH, IN, KY).
- Semicolon-delimited if multiple.
- Alphabetized.
- Never infer from member Sites unless explicitly documented.
- Leave blank for single-state networks (Ohio-only is implied).

---

## 5.9 Member Site IDs ✨ NEW IN v5.0 (replaces name-string list)

Member Sites are now linked by **entity ID**, not name string.

**Normalization process:**
1. Collect resolved member site references (names or raw IDs from discovery)
2. For each reference, look up the matching Site entity ID in the Entity Graph
3. Record the confirmed Site entity IDs in `member_site_ids`
4. IDs that cannot be resolved → log as warning, exclude from the list
5. If all member IDs are unresolvable → log as warning, flag for review

**Rules:**
- Must reference valid Site entities in the Entity Graph
- Member Sites must be identity-bearing Sites — not Features or Access Points
- Never infer membership from geographic proximity or shared governance alone
- Never add member Sites not documented in authoritative sources
- If a member Site is not yet in the Entity Graph → log warning, exclude for now; re-run after Site is upserted
- Relationship table `site_to_network` is populated from this validated ID list

**Provenance:** Log all membership resolutions, unresolved references, and exclusions.

---

## 5.10 Member Count ✨ NEW IN v5.0

- Computed from the validated `member_site_ids` list after normalization.
- Must equal the count of successfully resolved member Site IDs.
- Never manually set or copied from source documentation.
- If member_site_ids is empty or unresolved → member_count = 0, flag for review.

---

## 5.11 Description ✨ UPDATED FROM v4.0 (absorbs `history` and `alternate_names`)

- 1-3 sentences.
- Must describe identity-defining characteristics of the network: purpose, scope, designation character.
- Include naming history, alternate names, and significant origin or milestone events
  (formerly in `history` and `alternate_names` — now merged here).
- Must not include Site-level descriptions or individual member Site details.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

---

## 5.12 Alternate Names ✨ REMOVED IN v5.0

- `alternate_names` is no longer a field in the Site Network schema.
- Alternate or historical names → include in Description.
- If alternate_names values are present in resolved records from older discovery runs → migrate relevant names to Description, then drop the field.

---

## 5.13 History ✨ REMOVED IN v5.0

- `history` is no longer a separate field in the Site Network schema.
- Historical content → merge into Description.
- If history values are present in resolved records from older discovery runs → merge into Description, then drop the field.

---

## 5.14 Network Affiliation ✨ REMOVED IN v5.0

- `network_affiliation` is no longer a field in the Site Network schema.
- If network affiliation values are present in resolved records from older discovery runs → silently drop.
- Do not migrate to any other field.

---

## 5.15 Notes

- Optional free text.
- Use for: operational details, designation history, funding notes, boundary clarifications, contextual notes.
- Must not include identity-defining characteristics (those belong in Description).
- Must not include Site-level details.
- Must not contradict controlled fields.

---

## 5.16 URL

- Full https:// URL to primary authoritative source.
- Single value.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.17 Map URL

- Full https:// URL to a map of the network or its member Sites.
- Single value (unlike Trail Networks which use a rich maps array).
- Leave blank if none.

---

## 5.18 GPS / Township / Municipality

**Not applicable.** Site Networks are multi-location entities.
- No gps_lat, gps_lon fields
- No plus_code
- No township, municipality
- The Normalization Engine does not run GIS derivation for Site Networks

------------------------------------------------------------
# 6. MULTI-COUNTY AND MULTI-STATE NORMALIZATION RULES

- A Site Network spanning multiple counties or states produces **one normalized entity**.
- `counties` must include all counties, alphabetized, semicolon-delimited.
- `states_included` must include all states, alphabetized, semicolon-delimited.
- Never segment multi-county or multi-state networks.

------------------------------------------------------------
# 7. IDENTITY ANCHOR VALIDATION

The integrity anchor for Site Networks is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v5.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Network Type maps to valid vocabulary value
- Status maps to valid vocabulary value (if present) — use Site Network vocabulary, not Trail Network
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Member Site IDs: each ID references valid Site in Entity Graph
- Member Count: equals count of validated IDs
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
- Use the most authoritative source (Resolution decides).
- Record alternates in Description.
- Log conflict.

### 10.2 Conflicting Network Type
- Must defer to Resolution.
- Never infer.
- Leave blank if unresolvable.

### 10.3 Conflicting Status
- Use authoritative documentation.
- If unclear → leave blank, log conflict.

### 10.4 Conflicting Counties or States
- Use authoritative documentation.
- If conflict persists → log, flag for review.

### 10.5 Conflicting Membership
- Must defer entirely to Resolution for identity conflicts.
- Normalization resolves member Site references to IDs — it does not adjudicate whether a Site belongs.
- Unresolvable references → log and exclude.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer Network Type, Status, or membership.
- Never infer counties or states from member Sites.
- Blank ownership is correct and common — do not fill with governance.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- All vocabulary mappings applied (Network Type, Status)
- Member Site ID resolution results (resolved / unresolved / excluded)
- Member Count derivation
- Alternate names and history migration to Description (if applicable)
- Network affiliation drop (if applicable)
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Site Network Vocabulary Module v5.0
- Site Network Schema Module v5.0
- Site Schema Module v5.0 (for member Site validation)
- Discovery Output Specification v5.0
- Resolution Engine v5.0
- Normalization Engine v5.0
- Entity Graph Schema v5.0
- Audit & Logging Module v5.0

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v5.0
