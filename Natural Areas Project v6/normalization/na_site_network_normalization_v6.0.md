# NATURAL AREAS PROJECT
# SITE NETWORK NORMALIZATION CONTRACT v6.0
(Authoritative Field-Level Rules for Normalizing Resolved Site Network Entities)

This module defines the v6.0 normalization rules applied by the Normalization Engine
v6.0 to transform Resolved Site Network entities into Normalized Site Network Objects
ready for insertion into the Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the **Site Network Vocabulary Module v6.0**.

This contract is authoritative for Site Network normalization only.

This module supersedes Site Network Normalization Contract v5.3.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Coordination field added** (IMP-135): `coordination_raw` added to inputs
  (§2.2); §5.6a Coordination added to field-by-field rules (§5); normalization
  workflow Step 9a added; coordination added to validation logic (§8) and
  auditability requirements (§13).

- **IMP-014 — Notes provenance prohibition added to §5.13**: Notes field is
  customer-facing. Pipeline source references, IMP numbers, and process content
  must not appear.

- **IMP-015 — Description character and mission priority added to §5.11**:
  When description content could serve either mission/identity or administrative
  context, mission and geographic/identity character takes priority.

- **All v5.3 rules carried forward**: IMP-105 (org_type schema gap resolved),
  IMP-102 (enforcement-grade vocabulary read gates), IMP-100 (vocabulary
  enforcement hardening), network_type and org_type and status enforcement,
  empty string enforcement (§5.20), member Site ID resolution (§5.9), member
  count derivation (§5.10).

------------------------------------------------------------
# 1. PURPOSE

The Site Network Normalization Contract v6.0 defines:

- How a Resolved Site Network becomes a Normalized Site Network
- How Network Type, Org Type, and Status are normalized using vocabulary read gates
- How Ownership, Governance, Partner Agencies, and Coordination are handled
- How Identity Notes are surfaced from identity_notes_raw
- How member Site IDs are validated and linked
- How Member Count is derived
- How normalization interacts with the Normalization Engine v6.0
- How provenance, conflicts, and uncertainties are recorded

Normalization must:

- Never invent data
- Never infer membership, governance, coordination, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v6.x, including:

- resolved identity key
- resolved entity_type = "Site Network"
- resolved network_type, org_type, status
- resolved county set, state set
- resolved governance, partner_agencies, coordination, ownership
- resolved member Site set (if any)
- resolved conflicts and uncertainties
- SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags (if set during discovery)

## 2.2 Raw Discovery Record v6.0
Including:

- name_raw
- network_type_raw
- org_type_raw
- status_raw
- ownership_raw
- governance_raw
- partner_agencies_raw
- coordination_raw *(new in v6.0)*
- counties_raw
- states_raw
- member_sites_raw (names or IDs)
- description_raw
- identity_notes_raw
- notes_raw
- url_primary_raw
- urls_raw (all URLs including any map URLs)
- discovery_tier, discovered_in_tiers
- seeded_from_baseline, baseline_id
- discovery_metadata

**Not applicable for Site Networks:**
- No gps fields (multi-location)
- No address, township, municipality

## 2.3 Vocabulary Modules
- Site Network Vocabulary Module v6.0 (Network Type, Org Type, Status)

## 2.4 Schema Modules v6.0
- Site Network Schema Module v6.0
- Site Schema Module v6.0 (for member Site validation)

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Site Network Object v6.0** conforming to the Site Network Schema
  Module v6.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v6.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Site Network from Normalization Engine v6.0
2.  Validate identity and entity_type = "Site Network"
3.  **READ Site Network Vocabulary Module v6.0 §7.x** — mandatory before
    normalizing any vocabulary-controlled field
4.  Normalize Network Name
5.  Normalize Network Type (using §7.1 mapping table)
6.  Normalize Org Type (using §7.2 mapping table)
7.  Normalize Status (using §7.3 mapping table)
8.  Normalize Ownership
9.  Normalize Governance, Partner Agencies
9a. Normalize Coordination *(new in v6.0)*
10. Normalize Counties, States Included
11. Validate and link Member Site IDs
12. Compute Member Count from validated ID list
13. Normalize Description
14. Normalize Identity Notes
15. Normalize Notes
16. Normalize URL (including any map URLs from urls_raw)
17. Run §5.20 Empty String Enforcement
18. Run integrity anchor deduplication check (via Normalization Engine)
19. Validate against Site Network Schema v6.0
20. Emit Normalized Site Network + provenance

If any critical step fails → return error to Normalization Engine v6.0.

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

**MANDATORY: Read Site Network Vocabulary Module v6.0 §7.1 before normalizing
this field.**

- Must match a controlled value from Site Network Vocabulary Module v6.0 §2.1.
- Must not encode governance, ownership, or hierarchy.
- Must not be inferred from member Sites, geography, or management alone.

**Enforcement procedure (per §7.1):**
1. Read Site Network Vocabulary Module v6.0 §7.1 in full.
2. Match raw value case-insensitively after stripping whitespace.
3. If maps to controlled value → apply; log.
4. Not in §7.1 table → null-and-log.
5. Compound (slash, comma, semicolon) → flag as REVIEW.
6. Ambiguous → see §7.5; flag as REVIEW if applicable.
7. "Other" may be used only when documented but no controlled value applies.
8. NEVER use a value not in the §2.1 allowed values list.

**Provenance:** Log all vocabulary mappings; null-and-log decisions with raw value;
REVIEW flags.

---

## 5.2a Org Type

**MANDATORY: Read Site Network Vocabulary Module v6.0 §7.2 before normalizing
this field.**

- Must match a controlled value from Site Network Vocabulary Module v6.0 §3.1.
- One value only — not a list of all partner organizations.
- Must not be inferred from network name, governance string, or member Site ownership.
- If org type is ambiguous or undocumented → leave blank.

**Enforcement procedure (per §7.2):**
1. Read Site Network Vocabulary Module v6.0 §7.2 in full.
2. Match raw value case-insensitively.
3. If maps to controlled value → apply; log.
4. Not in §7.2 table → null-and-log.
5. Compound → flag as REVIEW.
6. Ambiguous (e.g., "conservancy") → see §7.5 for guidance.
7. "Other" may be used when documented but no controlled value applies.
8. NEVER use a value not in the §3.1 allowed values list.

**Provenance:** Log all vocabulary mappings; null-and-log decisions; REVIEW flags.

---

## 5.3 Status

**MANDATORY: Read Site Network Vocabulary Module v6.0 §7.3 before normalizing
this field.**

- Must match a controlled value from Site Network Vocabulary Module v6.0 §4.1.
- Use Site Network vocabulary — not Trailthing vocabulary.

**Enforcement procedure (per §7.3):**
1. Read Site Network Vocabulary Module v6.0 §7.3 in full.
2. Match raw value case-insensitively.
3. "open" / "operational" → "Active".
4. "dormant" / "inactive" → "Inactive" (not "Dissolved" unless dissolution documented).
5. "disbanded" / "terminated" / "decommissioned" → "Dissolved" only when documented.
6. Not in §7.3 table → null-and-log.
7. "closed" is ambiguous for Site Networks → flag as REVIEW per §7.5.
8. Leave blank if status is undocumented.

**Provenance:** Log all vocabulary mappings; null-and-log decisions; REVIEW flags.

---

## 5.4 Ownership

- Optional — blank is correct and common.
- Many Site Networks are formal designations without land ownership — blank is valid.
- When populated, must contain the **actual legal name** of the entity that owns or
  established the network.
- Must not use generic categories.
- Must not encode governance or management.

---

## 5.5 Governance

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple managers are formally documented.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
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

## 5.6a Coordination *(new in v6.0)*

- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Governance or Partner Agencies.
- Must not use generic categories.
- Free-text; pass through `coordination_raw` with whitespace cleanup.
- Leave blank if no documented coordination exists.
- Never infer coordination from governance, ownership, or network type.

**Provenance:** Log whether coordination was populated from coordination_raw or
left blank, and why.

---

## 5.7 Counties

- Required if network is Ohio-based.
- Must match official Ohio county names.
- Alphabetized. Semicolon-delimited. Omit "County."
- Must represent all counties the network spans.
- A multi-county network is **one entity** — never segmented.
- Never infer from member Sites alone.

---

## 5.8 States Included

- Two-letter state abbreviations (e.g., OH, IN, KY).
- Semicolon-delimited. Alphabetized.
- Never infer from member Sites alone.
- Leave blank for single-state (Ohio-only) networks.

---

## 5.9 Member Site IDs

Member Sites are linked by **entity ID**, not name string.

**Normalization process:**
1. Collect resolved member site references (names or raw IDs from discovery).
2. For each reference, look up the matching Site entity ID in the Entity Graph.
3. Record confirmed Site entity IDs in `member_site_ids`.
4. IDs that cannot be resolved → log as WARNING; exclude from the list.
5. If all member IDs are unresolvable → log WARNING; flag for review.

**Rules:**
- Must reference valid Site entities in the Entity Graph.
- Never infer membership from geographic proximity or shared governance alone.
- Never add member Sites not documented in authoritative sources.
- If a member Site is not yet in the Entity Graph → log warning; exclude for now;
  re-run after Site is upserted.
- Relationship table `site_network_members` is populated from this validated ID list.

**Provenance:** Log all membership resolutions, unresolved references, and exclusions.

---

## 5.10 Member Count

- Computed from the validated `member_site_ids` list after normalization.
- Must equal the count of successfully resolved member Site IDs.
- Never manually set or copied from source documentation.
- If member_site_ids is empty or unresolved → member_count = 0; flag for review.

---

## 5.11 Description

**Priority (IMP-015)**: Description must capture the character, mission, and
geographic/identity scope of the network — not administrative structure or governance
detail. When description_raw contains both identity content and administrative content,
extract and retain the identity content.

- 1-3 sentences.
- Must describe identity-defining characteristics: purpose, scope, designation
  character, geographic or thematic identity.
- Include naming history, alternate names, and significant origin events.
- Must not include individual member Site descriptions.
- Must not include amenities or temporary conditions.
- Must not contradict controlled fields.

Leave blank if description_raw contains only governance/administrative restatement
with no substantive identity content.

---

## 5.12 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Disambiguation notes
- Alternate or historical names
- SITE_NETWORK_UNCERTAIN flags — preserve and surface here; do not resolve silently
- SITE_NETWORK_PROVISIONAL flags — preserve; do not resolve silently
- Governance verification notes
- Vocabulary type uncertainty
- Rationale for gray-area candidates

**Rules:**
- Must not duplicate Description content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags — do not remove

---

## 5.13 Notes

**Customer-facing scope (IMP-014)**: Notes is a customer-facing field. Pipeline
source references, IMP numbers, session identifiers, and process-related content
must not appear. Strip these during normalization.

- Optional free text.
- Use for: operational details, designation history, funding notes, boundary
  clarifications, contextual notes, discovery gaps.
- **Alternate names** (IMP-029): `ALT NAME: '[name]' — [source context]` — any name used
  by an authoritative source that differs from the canonical `network_name` field. Always
  preserve; never discard known alternate names.
- Must not include identity-defining characteristics.
- Must not include individual member Site details.
- Must not contradict controlled fields.

**Pipeline metadata stripping**: Apply the same metadata stripping logic as Site
Normalization Contract v6.0 §5.19.

---

## 5.14 URL

- Full https:// URL to primary authoritative source.
- Semicolon-delimit if multiple authoritative URLs exist.
- Include map URLs as additional semicolon-delimited values — no separate map URL
  field.
- Remove tracking parameters.
- Leave blank if no authoritative URL exists.

---

## 5.15 GPS / Township / Municipality

**Not applicable.** Site Networks are multi-location entities.
- No gps_lat, gps_lon
- No plus_code
- No township, municipality
- The Normalization Engine does not run GIS derivation for Site Networks.

---

## 5.20 Empty String Enforcement

**When to run:** After field-level normalization (§5.2, §5.2a, §5.3), before
integrity anchor validation.

**Applies to:** network_type, org_type, status.

**Rule:** An empty string ("") is a data defect, not a valid blank. Convert to null;
log as normalization defect event.

Procedure:
1. Check network_type: if "" → set to null; log defect event.
2. Check org_type: if "" → set to null; log defect event.
3. Check status: if "" → set to null; log defect event.
4. Do not apply empty-string conversion to free-text fields.

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

The Normalization Engine v6.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 8. VALIDATION LOGIC

Normalization must validate:

- Network Type maps to valid vocabulary value (§2.1)
- Org Type maps to valid vocabulary value (§3.1) — if present
- Status maps to valid vocabulary value (§4.1)
- Counties: alphabetized, semicolon-delimited, "County" stripped
- States: two-letter abbreviations, alphabetized
- Member Site IDs: each ID references valid Site in Entity Graph
- Member Count: equals count of validated IDs
- **Coordination**: free-text; no vocabulary enforcement; must not duplicate
  Governance or Partner Agencies
- No invented data
- Blank fields are true blanks (not empty strings)
- No delimiter characters inside field values
- SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flags preserved in identity_notes

------------------------------------------------------------
# 9. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields are true blanks
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 10. CONFLICT HANDLING

## 10.1 Conflicting Names
Use the most authoritative source. Record alternates in Identity Notes or Description.

## 10.2 Conflicting Network Type
Defer to Resolution. Never infer. Leave blank if unresolvable.

## 10.3 Conflicting Org Type
Use the org type of the primary managing entity. Note alternatives in governance or
notes. Leave blank if unresolvable.

## 10.4 Conflicting Status
Use authoritative documentation. If unclear → leave blank; log conflict.

## 10.5 Conflicting Counties or States
Use authoritative documentation. If conflict persists → log; flag for review.

## 10.6 Conflicting Membership
Defer entirely to Resolution for identity conflicts. Normalization resolves member
Site references to IDs — it does not adjudicate whether a Site belongs.
Unresolvable references → log and exclude.

## 10.7 SITE_NETWORK_UNCERTAIN Flag
Do not resolve during normalization. Preserve in identity_notes. Flag for downstream
manual review.

## 10.8 SITE_NETWORK_PROVISIONAL Flag
Do not remove during normalization. Preserve in identity_notes. Flag for downstream
review — the provisional record should be promoted to confirmed once the threshold
rules (Site Network Discovery Sub-Procedure v6.0 §3) have been met.

------------------------------------------------------------
# 11. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank.
- Never estimate.
- Never infer Network Type, Org Type, Status, or membership.
- Never infer counties or states from member Sites.
- Blank ownership is correct and common.
- Blank org_type is correct when managing entity type is undocumented.
- Blank coordination is correct when no community-based or advisory partners exist.

------------------------------------------------------------
# 12. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- Confirmation that Site Network Vocabulary Module v6.0 §7.x was read before
  normalizing vocabulary-controlled fields
- All vocabulary mappings applied (Network Type, Org Type, Status)
- All null-and-log decisions with raw value and field name
- All REVIEW flags with raw value and field name
- All empty-string-to-null conversions (§5.20 defect events)
- Coordination field outcome (populated / blank / reason)
- Member Site ID resolution results (resolved / unresolved / excluded)
- Member Count derivation
- Identity Notes content surfaced from identity_notes_raw
- SITE_NETWORK_UNCERTAIN and SITE_NETWORK_PROVISIONAL flag status
- All conflicts detected and how handled
- All fields left blank and why
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This contract depends on:

- Site Network Vocabulary Module v6.0
- Site Network Schema Module v6.0
- Site Schema Module v6.0 (for member Site validation)
- Resolution Engine v6.x
- Normalization Engine v6.0
- Entity Graph Schema v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF SITE NETWORK NORMALIZATION CONTRACT v6.0
