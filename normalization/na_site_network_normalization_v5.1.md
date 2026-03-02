# NATURAL AREAS PROJECT
# SITE NETWORK NORMALIZATION CONTRACT v5.1
(Authoritative Field-Level Rules for Normalizing Resolved Site Network Entities)

This module defines the v5.1 normalization rules applied by the
Normalization Engine v5.x to transform Resolved Site Network entities into
Normalized Site Network Objects ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.x**.

This contract is authoritative for Site Network normalization only.

------------------------------------------------------------
# CHANGES FROM v5.0 → v5.1

- **identity_notes added**: New normalized field surfaced from identity_notes_raw;
  distinct from notes; used for identity clarifications, disambiguation, and
  SITE_NETWORK_UNCERTAIN flags
- **Map URL removed**: map_url_raw no longer a raw input; map URLs captured
  in urls_raw at discovery and url at normalized stage
- **Raw input field renames**:
  - notes_raw → identity_notes_raw (identity clarifications)
  - url_all → urls_raw (all URLs including map URLs)
  - url_primary → url_primary_raw
  - map_url_raw removed
- **Derived Label removed**: No longer computed or stored at any stage
- **Normalization workflow updated**: Step 15 now normalizes identity_notes;
  Map URL normalization step removed
- **All cross-module references updated to v5.x**

------------------------------------------------------------
# CHANGES FROM v4.0 → v5.0

- `alternate_names` removed — variants noted in Description instead
- `history` removed — merged into Description
- `network_affiliation` removed — cleaner architecture
- `counties_traversed` → `counties` — renamed; alphabetized array
- `primary_managing_agency` → `governance` — renamed
- `secondary_managing_agencies` → `partner_agencies` — renamed
- `ownership` added — optional
- `member_count` added — computed from validated member_site_ids list
- `member_site_ids` added — array of Site entity IDs

------------------------------------------------------------
# 1. PURPOSE

The Site Network Normalization Contract v5.1 defines:

- How a Resolved Site Network becomes a Normalized Site Network
- How each Site Network Schema v5.x field is validated and normalized
- How Network Type and Status are normalized
- How Ownership, Governance, and Partner Agencies are handled
- How Identity Notes are surfaced from identity_notes_raw
- How member Site IDs are validated and linked
- How Member Count is derived
- How normalization interacts with the **Normalization Engine v5.x**
- How provenance, conflicts, and uncertainties are recorded
- How normalized entities integrate with the **Entity Upsert Engine v5.x**

Normalization must:

- Never invent data
- Never infer membership, governance, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From **Resolution Engine v5.x**, including:

- resolved identity key
- resolved entity_type = "Site Network"
- resolved network_type, status
- resolved county set, state set
- resolved governance, partner_agencies, ownership
- resolved member Site set (if any)
- resolved conflicts and uncertainties
- SITE_NETWORK_UNCERTAIN flag (if set during discovery)

## 2.2 Raw Discovery Record v5.1
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
- identity_notes_raw
- url_primary_raw
- urls_raw (all URLs including any map URLs)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata
- source_map

**Removed from v5.0 raw inputs:**
- notes_raw — renamed to identity_notes_raw
- url_all — renamed to urls_raw
- map_url_raw — removed; map URLs now in urls_raw
- url_primary — renamed to url_primary_raw

**Not applicable for Site Networks:**
- No gps fields (networks are multi-location — no single GPS point)
- No address, township, municipality

## 2.3 Vocabulary Modules v5.x
- Site Network Vocabulary Module v5.x (Network Type, Status)

## 2.4 Schema Modules v5.x
- Site Network Schema Module v5.x
- Site Schema Module v5.x (for member Site validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Network Object v5.1** conforming to the
  Site Network Schema Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Site Network from Normalization Engine v5.x
2.  Validate identity and entity_type = "Site Network"
3.  Normalize Network Name
4.  Normalize Network Type
5.  Normalize Status
6.  Normalize Ownership
7.  Normalize Governance, Partner Agencies
8.  Normalize Counties, States Included
9.  Validate and link Member Site IDs
10. Compute Member Count from validated ID list
11. Normalize Description
12. Normalize Identity Notes
13. Normalize Notes
14. Normalize URL (including any map URLs from urls_raw)
15. Run integrity anchor deduplication check (via Normalization Engine)
16. Validate against Site Network Schema v5.x
17. Emit Normalized Site Network + provenance

If any critical step fails → return error to Normalization Engine v5.x.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Network Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors or hierarchy encodings.
- Alternate or historical names → Identity Notes or Description, not Network Name.
- Never infer names from member Sites or branding.

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Network Type

- Must match a controlled value from Site Network Vocabulary Module v5.x.
- Describes the identity-bearing classification of the network.
- Must not encode governance, ownership, or hierarchy.
- Must not be inferred from member Sites, geography, or management alone.
- If ambiguous → leave blank and log uncertainty.

**Common normalization mappings:**
- "national heritage area" → "National Heritage Area"
- "scenic river corridor" → "Scenic River Corridor"
- "county park system" → "Multi-Site Recreation Network"
- "municipal park system" → "Multi-Site Recreation Network"
- "preserve network" → "Multi-Site Conservation Network"
- See Site Network Vocabulary Module v5.x Section 6 for full mapping table.

---

## 5.3 Status

- Must match a controlled value from Site Network Vocabulary Module v5.x.
- Site Network status vocabulary: Active, Proposed, Under Development,
  Inactive, Dissolved.
- Use Site Network vocabulary — not Trail Network vocabulary.

**Allowed values and guidance:**
- **Active** — currently operational and recognized
- **Proposed** — must be explicitly documented; not inferred
- **Under Development** — actively being assembled; not yet operational
- **Inactive** — exists but no longer actively maintained or promoted
- **Dissolved** — formally disbanded; use only when explicitly documented

Never infer status from member Site statuses alone.
Leave blank if status is ambiguous or undocumented.

---

## 5.4 Ownership

- Optional — blank is correct and common.
- Many Site Networks are formal designations without land ownership — blank is valid.
- When populated, must contain the **actual legal name** of the entity that
  owns or established the network.
- Must not use generic categories.
- Must not encode governance or management.

**Examples:**
- ✅ "National Park Service"
- ✅ "Maumee Valley Land Trust"
- ❌ "Federal Government" — too generic
- ❌ "Multiple Owners" — leave blank instead

---

## 5.5 Governance

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Many networks are formal designations managed by coordinating bodies —
  governance may be a partnership.
- Leave blank if unverifiable.

---

## 5.6 Partner Agencies

- Must contain the **actual names** of formally documented partner organizations.
- Semicolon-delimit if multiple.
- Must not use generic categories.
- Must not duplicate Governance.
- Must not encode temporary volunteer activity or informal relationships.
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
- Never infer from member Sites alone unless explicitly documented.

---

## 5.8 States Included

- Use authoritative two-letter state abbreviations (e.g., OH, IN, KY).
- Semicolon-delimited if multiple.
- Alphabetized.
- Never infer from member Sites unless explicitly documented.
- Leave blank for single-state networks (Ohio-only is implied).

---

## 5.9 Member Site IDs

Member Sites are linked by **entity ID**, not name string.

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
- If a member Site is not yet in the Entity Graph → log warning, exclude for
  now; re-run after Site is upserted
- Relationship table `site_network_members` is populated from this validated
  ID list

**Provenance:** Log all membership resolutions, unresolved references, and
exclusions.

---

## 5.10 Member Count

- Computed from the validated `member_site_ids` list after normalization.
- Must equal the count of successfully resolved member Site IDs.
- Never manually set or copied from source documentation.
- If member_site_ids is empty or unresolved → member_count = 0, flag for review.

---

## 5.11 Description

- 1-3 sentences.
- Must describe identity-defining characteristics: purpose, scope, designation
  character.
- Include naming history, alternate names, and significant origin or milestone
  events (formerly in `history` and `alternate_names` — now merged here).
- Must not include Site-level descriptions or individual member Site details.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

---

## 5.12 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Disambiguation notes (e.g., why this is a Site Network rather than a
  parent Site)
- Alternate or historical names
- SITE_NETWORK_UNCERTAIN flags — preserve and surface here; do not resolve
  silently
- Governance verification notes
- Vocabulary type uncertainty
- Rationale for inclusion of gray-area candidates

**Rules:**
- Must not duplicate Description content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve SITE_NETWORK_UNCERTAIN flags — do not remove; flag for
  downstream review
- May include notes added during Resolution or Normalization passes

---

## 5.13 Notes

- Optional free text.
- Use for: operational details, designation history, funding notes, boundary
  clarifications, contextual notes, discovery gaps.
- Must not include identity-defining characteristics (those belong in
  Description or Identity Notes).
- Must not include Site-level details.
- Must not contradict controlled fields.

---

## 5.14 URL

- Full https:// URL to primary authoritative source.
- Semicolon-delimit if multiple authoritative URLs exist.
- Include map URLs (system-wide maps, GIS viewers, PDF maps) as additional
  semicolon-delimited values — no separate Map URL field exists.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.15 GPS / Township / Municipality

**Not applicable.** Site Networks are multi-location entities.
- No gps_lat, gps_lon fields
- No plus_code
- No township, municipality
- The Normalization Engine does not run GIS derivation for Site Networks

------------------------------------------------------------
# 6. MULTI-COUNTY AND MULTI-STATE NORMALIZATION RULES

- A Site Network spanning multiple counties or states produces
  **one normalized entity**.
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

The Normalization Engine v5.x runs the deduplication check after this
validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Network Type maps to valid vocabulary value
- Status maps to valid vocabulary value (if present) — use Site Network
  vocabulary, not Trail Network
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Member Site IDs: each ID references valid Site in Entity Graph
- Member Count: equals count of validated IDs
- No invented data
- Blank fields are true blanks
- No delimiter characters inside field values
- SITE_NETWORK_UNCERTAIN flags preserved in identity_notes

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
- Record alternates in Identity Notes or Description.
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
- Normalization resolves member Site references to IDs — it does not
  adjudicate whether a Site belongs.
- Unresolvable references → log and exclude.

### 10.6 SITE_NETWORK_UNCERTAIN Flag
- Do not attempt to resolve during normalization.
- Preserve in identity_notes field.
- Flag for downstream manual review.

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
- Identity Notes content surfaced from identity_notes_raw
- SITE_NETWORK_UNCERTAIN flag status
- Alternate names and history migration to Description (if applicable)
- Network affiliation drop (if applicable, from older records)
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Site Network Vocabulary Module v5.x
- Site Network Schema Module v5.x
- Site Schema Module v5.x (for member Site validation)
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v5.1
