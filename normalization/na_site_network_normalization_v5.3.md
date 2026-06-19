# NATURAL AREAS PROJECT
# SITE NETWORK NORMALIZATION CONTRACT v5.3
(Authoritative Field-Level Rules for Normalizing Resolved Site Network Entities)

This module defines the v5.3 normalization rules applied by the
Normalization Engine v5.x to transform Resolved Site Network entities into
Normalized Site Network Objects ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v5.3**.

This contract is authoritative for Site Network normalization only.

------------------------------------------------------------
# CHANGES FROM v5.2 → v5.3

- **IMP-105 — org_type schema gap resolved**: The `org_type` column has
  been added to the site_networks DB table. The schema gap note in §5.2a
  and the provenance schema gap log instruction in §10 are removed.
  org_type values are now upserted normally on the next pipeline run.

# CHANGES FROM v5.1 → v5.2

- **IMP-102 — Enforcement-grade vocabulary read gates**: Vocabulary
  mappings are no longer inline guidance; normalization must read the
  Site Network Vocabulary Module v5.3 §7.x tables before normalizing
  any vocabulary-controlled field.
  - Workflow Step 3 added: mandatory read of Site Network Vocabulary
    Module v5.3 §7.x before any vocabulary field normalization.
  - §5.2 Network Type updated: mandatory §7.1 read gate; null-and-log
    on unmappable values; REVIEW on compound values; references §7.5
    for ambiguous cases.
  - §5.2a Org Type added (new section): mandatory §7.2 read gate;
    null-and-log on unmappable values; REVIEW on compound values;
    schema gap documented.
  - §5.3 Status updated: mandatory §7.3 read gate; "open"/"operational"
    → "Active" made explicit; "dormant" → "Inactive" (not "Dissolved");
    null-and-log on unmappable values; REVIEW on ambiguous cases.
  - §5.20 Empty String Enforcement added: converts "" to null for
    network_type, org_type, and status; runs after field-level
    normalization, before integrity anchor validation.
- Module dependency updated to Site Network Vocabulary Module v5.3.

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

The Site Network Normalization Contract v5.2 defines:

- How a Resolved Site Network becomes a Normalized Site Network
- How each Site Network Schema v5.x field is validated and normalized
- How Network Type, Org Type, and Status are normalized using vocabulary
  read gates
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
- resolved network_type, org_type, status
- resolved county set, state set
- resolved governance, partner_agencies, ownership
- resolved member Site set (if any)
- resolved conflicts and uncertainties
- SITE_NETWORK_UNCERTAIN flag (if set during discovery)

## 2.2 Raw Discovery Record v5.1
Including:

- name_raw
- network_type_raw
- org_type_raw
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

**Not applicable for Site Networks:**
- No gps fields (networks are multi-location — no single GPS point)
- No address, township, municipality

## 2.3 Vocabulary Modules
- Site Network Vocabulary Module v5.3 (Network Type, Org Type, Status)

## 2.4 Schema Modules v5.x
- Site Network Schema Module v5.x
- Site Schema Module v5.x (for member Site validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Network Object v5.2** conforming to the
  Site Network Schema Module v5.x
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v5.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Site Network from Normalization Engine v5.x
2.  Validate identity and entity_type = "Site Network"
3.  **READ Site Network Vocabulary Module v5.3 §7.x** — mandatory
    before normalizing any vocabulary-controlled field; do not proceed
    to Step 4, 5, or 6 until §7.1, §7.2, and §7.3 have been read
4.  Normalize Network Name
5.  Normalize Network Type (using §7.1 mapping table)
6.  Normalize Org Type (using §7.2 mapping table)
7.  Normalize Status (using §7.3 mapping table)
8.  Normalize Ownership
9.  Normalize Governance, Partner Agencies
10. Normalize Counties, States Included
11. Validate and link Member Site IDs
12. Compute Member Count from validated ID list
13. Normalize Description
14. Normalize Identity Notes
15. Normalize Notes
16. Normalize URL (including any map URLs from urls_raw)
17. Run §5.20 Empty String Enforcement
18. Run integrity anchor deduplication check (via Normalization Engine)
19. Validate against Site Network Schema v5.x
20. Emit Normalized Site Network + provenance

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

**MANDATORY: Read Site Network Vocabulary Module v5.3 §7.1 before
normalizing this field. Do not normalize network_type without first
reading the §7.1 mapping table.**

- Must match a controlled value from Site Network Vocabulary Module
  v5.3 §2.1.
- Describes the identity-bearing classification of the network.
- Must not encode governance, ownership, or hierarchy.
- Must not be inferred from member Sites, geography, or management alone.

**Enforcement procedure (per §7.1):**
1. Read Site Network Vocabulary Module v5.3 §7.1 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. If raw value maps to a controlled value → apply mapping; log.
4. If raw value is not in the §7.1 table → null-and-log; do not
   invent a mapping.
5. If raw value is compound (slash, comma, semicolon) → flag as REVIEW.
6. If raw value is ambiguous → see §7.5; flag as REVIEW if applicable.
7. "Other" may be used only when the entity type is documented but
   none of the controlled values apply.
8. NEVER use a value not in the §2.1 allowed values list.

**Provenance:** Log all vocabulary mappings applied. Log all null-and-log
decisions with the raw value. Log all REVIEW flags.

---

## 5.2a Org Type

**MANDATORY: Read Site Network Vocabulary Module v5.3 §7.2 before
normalizing this field. Do not normalize org_type without first
reading the §7.2 mapping table.**

- Must match a controlled value from Site Network Vocabulary Module
  v5.3 §3.1.
- Describes the organizational category of the primary managing entity.
- One value only — not a list of all partner organizations.
- Must not be inferred from network name, governance string, or
  member Site ownership alone.
- If org type is ambiguous or undocumented → leave blank.

**Enforcement procedure (per §7.2):**
1. Read Site Network Vocabulary Module v5.3 §7.2 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. If raw value maps to a controlled value → apply mapping; log.
4. If raw value is not in the §7.2 table → null-and-log; do not
   invent a mapping.
5. If raw value is compound → flag as REVIEW.
6. If ambiguous (e.g., "conservancy") → see §7.5 for guidance.
7. "Other" may be used when the org type is documented but none of
   the controlled values apply.
8. NEVER use a value not in the §3.1 allowed values list.

**Provenance:** Log all vocabulary mappings. Log null-and-log decisions
with raw value. Log REVIEW flags.

---

## 5.3 Status

**MANDATORY: Read Site Network Vocabulary Module v5.3 §7.3 before
normalizing this field. Do not normalize status without first reading
the §7.3 mapping table.**

- Must match a controlled value from Site Network Vocabulary Module
  v5.3 §4.1.
- Site Network status vocabulary: Active, Proposed, Under Development,
  Inactive, Dissolved.
- Use Site Network vocabulary — not Trail Network vocabulary.

**Enforcement procedure (per §7.3):**
1. Read Site Network Vocabulary Module v5.3 §7.3 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. "open" and "operational" → "Active" explicitly; do not leave as raw.
4. "dormant" and "inactive" → "Inactive"; do not use "Dissolved" unless
   formal dissolution is documented.
5. "disbanded", "terminated", "decommissioned" → "Dissolved" only when
   explicitly documented.
6. If raw value is not in the §7.3 table → null-and-log; do not guess.
7. "closed" is ambiguous for Site Networks → flag as REVIEW per §7.5.
8. Leave blank (null) if status is undocumented.

**Provenance:** Log all vocabulary mappings. Log null-and-log decisions
with raw value. Log REVIEW flags.

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

---

## 5.20 Empty String Enforcement

**When to run:** After field-level normalization (§5.2, §5.2a, §5.3),
before integrity anchor validation.

**Applies to:** network_type, org_type, status.

**Rule:** An empty string ("") is a data defect, not a valid blank.

**Procedure:**
1. Check network_type: if value is "" → set to null; log as
   normalization defect event with field name and entity ID.
2. Check org_type: if value is "" → set to null; log as normalization
   defect event with field name and entity ID.
3. Check status: if value is "" → set to null; log as normalization
   defect event with field name and entity ID.
4. Do not apply empty-string conversion to free-text fields
   (ownership, governance, description, notes, etc.) — those
   are handled by their own field rules.

**Provenance:** Each empty-string-to-null conversion must appear
in normalization_provenance as a defect event.

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

- Network Type maps to valid vocabulary value (Site Network Vocabulary
  Module v5.3 §2.1)
- Org Type maps to valid vocabulary value (Site Network Vocabulary
  Module v5.3 §3.1) — if present
- Status maps to valid vocabulary value (Site Network Vocabulary Module
  v5.3 §4.1) — use Site Network vocabulary, not Trail Network
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Member Site IDs: each ID references valid Site in Entity Graph
- Member Count: equals count of validated IDs
- No invented data
- Blank fields are true blanks (not empty strings)
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

### 10.3 Conflicting Org Type
- Use the org type of the primary managing entity.
- If multiple managing entities with different org types → use the
  most prominent; note others in governance or notes.
- Leave blank if unresolvable.

### 10.4 Conflicting Status
- Use authoritative documentation.
- If unclear → leave blank, log conflict.

### 10.5 Conflicting Counties or States
- Use authoritative documentation.
- If conflict persists → log, flag for review.

### 10.6 Conflicting Membership
- Must defer entirely to Resolution for identity conflicts.
- Normalization resolves member Site references to IDs — it does not
  adjudicate whether a Site belongs.
- Unresolvable references → log and exclude.

### 10.7 SITE_NETWORK_UNCERTAIN Flag
- Do not attempt to resolve during normalization.
- Preserve in identity_notes field.
- Flag for downstream manual review.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer Network Type, Org Type, Status, or membership.
- Never infer counties or states from member Sites.
- Blank ownership is correct and common — do not fill with governance.
- Blank org_type is correct when the managing entity type is undocumented.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- Confirmation that Site Network Vocabulary Module v5.3 §7.x was read
  before normalizing vocabulary-controlled fields
- All vocabulary mappings applied (Network Type, Org Type, Status) with
  raw value and mapped value
- All null-and-log decisions with raw value and field name
- All REVIEW flags with raw value and field name
- All empty-string-to-null conversions (§5.20 defect events)
- Member Site ID resolution results (resolved / unresolved / excluded)
- Member Count derivation
- Identity Notes content surfaced from identity_notes_raw
- SITE_NETWORK_UNCERTAIN flag status
- Alternate names and history migration to Description (if applicable)
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Site Network Vocabulary Module v5.3
- Site Network Schema Module v5.x
- Site Schema Module v5.x (for member Site validation)
- Discovery Output Specification v5.x
- Resolution Engine v5.x
- Normalization Engine v5.x
- Entity Upsert Engine v5.x
- Audit & Logging Module v5.x

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v5.2
