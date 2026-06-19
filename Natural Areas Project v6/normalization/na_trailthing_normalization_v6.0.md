# NATURAL AREAS PROJECT
# TRAILTHING NORMALIZATION CONTRACT v6.0
(Authoritative Field-Level Rules for Normalizing Resolved Trailthing Entities)

This module defines the entity-specific normalization rules applied by the
Normalization Engine v6.0 to produce a fully normalized Trailthing entity
conforming to the Trailthing Schema Module v6.0 and ready for insertion into the
Entity Graph.

This contract contains no controlled vocabularies.
All vocabularies are defined in the Trailthing Vocabulary Module v6.0.

This contract is authoritative for Trailthing normalization only.

This module is new in v6.0. It supersedes the Trail Normalization Contract v5.3,
the Trail Segment Normalization Contract v5.1, and the Trail Network Normalization
Contract v5.2, which are retired.

------------------------------------------------------------
# NO-CLASSIFICATION MANDATE

The Trailthing entity type is unified — it represents trail-like entities at any
scale or hierarchy level without classifying them as Trail, Trail Segment, or Trail
Network. This is a deliberate design decision (IMP-009).

**Normalization must never classify a Trailthing as trail vs. trail segment vs.
trail network.** The classification decision is deferred until after sufficient
county runs have been completed to establish hierarchy patterns.

The `source_term_raw` and `source_hierarchy_context_raw` fields capture verbatim
source framing. These fields are passed through unchanged — they are the primary
input for future hierarchy pattern analysis, not fields to be normalized against
a controlled vocabulary.

------------------------------------------------------------
# 1. PURPOSE

The Trailthing Normalization Contract v6.0 defines:

- How a Resolved Trailthing is transformed into a Normalized Trailthing
- How each Trailthing Schema v6.0 field is validated and normalized
- How use type, surface type, origin type, status, and difficulty are normalized
- How source_term_raw and source_hierarchy_context_raw are preserved verbatim
- How parent relationships (parent Trailthing, parent Site) are validated
- How organizational fields are normalized
- How description and notes scope is enforced
- How normalization interacts with the Normalization Engine v6.0
- How provenance, conflicts, and uncertainties are recorded

Normalization must:
- Never classify the Trailthing as trail vs. trail network vs. trail segment
- Never invent data
- Never infer governance, ownership, or identity
- Never silently correct malformed values
- Always log normalization decisions

------------------------------------------------------------
# 2. INPUTS

## 2.1 Resolved Entity Object
From Resolution Engine v6.x, including:

- resolved identity key
- resolved entity_type = "Trailthing"
- resolved county set
- resolved governance, ownership, partner_agencies, coordination
- resolved use type, surface type, origin type, status
- resolved conflicts and uncertainties

## 2.2 Raw Discovery Record v6.0
Including:

- name_raw
- source_term_raw *(verbatim — how the source describes the entity)*
- source_hierarchy_context_raw *(verbatim — how the source frames hierarchy)*
- use_type_raw (IMP-021 — only if explicitly stated)
- surface_raw (IMP-021 — only if explicitly stated)
- origin_type_raw
- total_length_raw
- counties_raw
- governance_raw
- ownership_raw
- partner_agencies_raw
- coordination_raw
- status_raw
- difficulty_raw *(only if explicitly stated by authoritative source)*
- accessibility_raw
- description_raw
- identity_notes_raw
- notes_raw
- url_primary_raw
- urls_raw
- maps_raw *(semicolon-delimited URL list)*
- parent_id_raw *(self-referential — ID of parent Trailthing, if any)*
- site_parent_raw *(name or ID of parent Site, if any)*
- parent_site_network_raw *(name of parent Site Network, if any)*
- member_trailthing_names_raw *(names of member Trailthings, if this is a container)*
- last_verified_date *(populated with today's date at discovery)*
- field_verified *(always false at discovery)*
- discovery_tier
- seeded_from_baseline, baseline_id
- discovery_metadata

**Not applicable for Trailthings:**
- No gps_lat_raw, gps_lon_raw (Trailthings are multi-location linear entities)
- No address (Trailthings have no single address)
- No township, municipality (multi-location entities)

## 2.3 Vocabulary Modules
- **Trailthing Vocabulary Module v6.0** — Use Type, Surface Type, Origin Type,
  Status, Difficulty. Read §vocabulary before normalizing any vocabulary-controlled
  field.

## 2.4 Schema Modules v6.0
- Trailthing Schema Module v6.0

------------------------------------------------------------
# 3. OUTPUTS

Normalization produces:

- A **Normalized Trailthing Object v6.0** conforming to the Trailthing Schema
  Module v6.0
- A **Normalization Provenance Record**
- A **Validation Result Object** (warnings, errors)
- A normalized entity ready for the **Entity Upsert Engine v6.x**

No new information may be invented.

------------------------------------------------------------
# 4. NORMALIZATION WORKFLOW (HIGH-LEVEL)

1.  Receive Resolved Trailthing from Normalization Engine v6.0
2.  Validate identity and entity_type = "Trailthing"
3.  **Read Trailthing Vocabulary Module v6.0** — mandatory before normalizing
    any vocabulary-controlled field
4.  Normalize Trailthing Name
5.  Pass through Source Term (verbatim — no normalization)
6.  Pass through Source Hierarchy Context (verbatim — no normalization)
7.  Normalize Use Type (vocabulary — optional)
8.  Normalize Surface Type (vocabulary — optional)
9.  Normalize Origin Type (vocabulary — optional)
10. Normalize Total Length
11. Normalize Counties
12. Normalize Governance, Ownership, Partner Agencies, Coordination
13. Normalize Status (vocabulary — optional)
14. Normalize Difficulty (vocabulary — optional; authoritative source only)
15. Normalize Accessibility (free-text)
16. Normalize Description (ecological/physical character priority)
17. Normalize Identity Notes
18. Normalize Notes (provenance prohibition)
19. Normalize URL
20. Normalize Maps (URL list)
21. Validate Parent Trailthing (§5.20)
22. Validate Parent Site (§5.21)
23. Resolve Member Trailthing Names to IDs (§5.22)
24. Normalize Last Verified Date (§5.23)
25. Normalize Field Verified (§5.24)
26. Apply empty string enforcement across all vocabulary fields (§5.25)
27. Run integrity anchor deduplication check (via Normalization Engine)
28. Validate against Trailthing Schema v6.0
29. Emit Normalized Trailthing + provenance

If any critical step fails → return error to Normalization Engine v6.0.

------------------------------------------------------------
# 5. FIELD-BY-FIELD NORMALIZATION RULES

## 5.1 Trailthing Name

- Use resolved name with minimal whitespace cleanup only.
- Must be the official published name.
- Must not include unofficial descriptors or hierarchy encodings.
- Alternate or historical names → Identity Notes, not Trailthing Name.
- Never infer names from parent entities or member Trailthings.

**IMP-010 Generic Name Qualification**: If name_raw is a generic descriptor
(e.g., "Trail", "Loop Trail", "Nature Trail", "Main Trail") without a qualifying
place name or organization name, the name must be qualified at discovery time by
the parent Site or managing organization. If a generic name arrives at normalization
without qualification and no parent site is documented → flag for REVIEW with:
`"Generic Trailthing name '[name]' without qualifying context — requires parent
Site or organization qualifier for unambiguous identity."`

**Provenance:** Log all name conflicts and corrections.

---

## 5.2 Source Term

- **Pass through verbatim from `source_term_raw`** — do not normalize, translate,
  or map to a controlled vocabulary.
- This field captures how the authoritative source describes the entity (e.g.,
  "National Scenic Trail," "recreation trail," "trail system," "connector").
- It is the primary input for future hierarchy pattern analysis.
- Minimal cleanup only: trim leading/trailing whitespace.
- Never blank this field if source_term_raw is populated.

**Provenance:** Log that source_term was passed through verbatim.

---

## 5.3 Source Hierarchy Context

- **Pass through verbatim from `source_hierarchy_context_raw`** — do not normalize,
  translate, or map to a controlled vocabulary.
- This field captures how the authoritative source frames the entity in relation to
  others (e.g., "part of the [system]," "a loop off the main trail").
- Minimal cleanup only: trim leading/trailing whitespace.
- Leave blank if source_hierarchy_context_raw is absent.

**Provenance:** Log that source_hierarchy_context was passed through verbatim, or
that it was absent.

---

## 5.4 Use Type (IMP-021)

**Read Trailthing Vocabulary Module v6.0 before applying this step.**

- Optional. Describes the primary intended use of the Trailthing.
- Single value only — compound values are never valid.
- "Multi-Use" only when explicitly documented as such.
- **Never infer from surface type, trail name, or amenities.** Only populate when
  explicitly stated by an authoritative source.
- Only populate when the source unambiguously states the use type in a dedicated
  field, label, or heading — not when it appears incidentally in narrative.

**Normalization procedure:**

1. Check `use_type_raw` against the vocabulary mapping table.
2. If the raw value maps to a controlled value → apply; log.
3. If the raw value is a compound (e.g., "Foot;Bike") → flag as REVIEW; leave blank.
4. If unmappable → null-and-log.
5. Empty string ("") → null; see §5.25.

---

## 5.5 Surface Type (IMP-021)

**Read Trailthing Vocabulary Module v6.0 before applying this step.**

- Optional. Describes the predominant surface type.
- Single value only — "Mixed" only when explicitly documented.
- **Never infer from imagery alone.** Only populate when explicitly stated by an
  authoritative source.
- "Paved" covers asphalt, concrete, and chip-and-seal.

**Normalization procedure:**

1. Check `surface_raw` against the vocabulary mapping table.
2. If maps to controlled value → apply; log.
3. Compound (e.g., "Gravel/Paved") → attempt to resolve as "Mixed" only if
   explicitly documented; otherwise → REVIEW; leave blank.
4. Width descriptors ("singletrack"), governance labels, ambiguous terms →
   null-and-log.
5. Empty string ("") → null; see §5.25.

---

## 5.6 Origin Type

**Read Trailthing Vocabulary Module v6.0 before applying this step.**

- Optional. Must be explicitly documented — not inferred from alignment, corridor
  appearance, or name.
- Single value only.

**Normalization procedure:**

1. Check `origin_type_raw` against the vocabulary mapping table.
2. If maps to controlled value → apply; log.
3. Surface or governance descriptors (e.g., "natural", "wildlife area trail")
   that are not origin descriptions → null-and-log.
4. Compound or ambiguous → REVIEW.
5. Unmappable → null-and-log.
6. Empty string ("") → null; see §5.25.

---

## 5.7 Total Length

- Numeric only — no units, no ranges, no approximation symbols.
- Represents the total length of the Trailthing.
- Never estimate.
- If sources conflict → use most authoritative (managing agency preferred); log.
- Leave blank if unknown.

---

## 5.8 Counties

- Required.
- Must match official Ohio county names.
- Alphabetized.
- Semicolon-delimited.
- Omit the word "County."
- A multi-county Trailthing is **one entity** — never segmented by county.
- All counties traversed must be represented.

---

## 5.9 Governance

- Must contain the **actual name(s)** of the operational managing organization(s).
- Semicolon-delimit if multiple co-managers with equal authority.
- Must not use generic categories.
- Must not encode ownership, designation, or access rules.
- Leave blank if unverifiable.

---

## 5.10 Ownership

- Must contain the exact legal name of the owning entity.
- Must not encode governance or partner roles.
- Leave blank if unverifiable.

---

## 5.11 Partner Agencies

- Formal, documented co-operator organizations.
- Must use exact organization names.
- Must not duplicate Ownership or Governance.
- Leave blank if no formal partners exist.

---

## 5.12 Coordination

- Community-based, volunteer, advisory, or informal partners.
- Must not duplicate Ownership, Governance, or Partner Agencies.
- Leave blank if no documented coordination exists.

---

## 5.13 Status

**Read Trailthing Vocabulary Module v6.0 before applying this step.**

- Optional. Describes the operational state of the Trailthing.
- Single value only.
- "Closed" = permanently closed.
- "Planned" must be explicitly documented.
- "Gap" applies when a missing portion is the defining characteristic.
- Never infer from imagery or social media.
- Temporary closures → Notes, not Status.

**Normalization procedure:**

1. Check `status_raw` against the vocabulary mapping table.
2. "open" / "operational" → "Active".
3. "planned" / "proposed" → "Planned".
4. "closed" → "Closed".
5. "gap" / "incomplete" → "Gap".
6. Compound → REVIEW; leave blank.
7. Unmappable → null-and-log.
8. Empty string ("") → null; see §5.25.

---

## 5.14 Difficulty

**Read Trailthing Vocabulary Module v6.0 before applying this step.**

- Optional — leave blank if not documented by an authoritative source.
- **CRITICAL:** Only populate from explicit authoritative source ratings — never
  assess yourself, never infer from surface type or length.
- Single value only — difficulty ranges are never valid.

**Normalization procedure:**

1. Check `difficulty_raw` against the vocabulary mapping table.
2. If maps to controlled value → apply; log the source URL in provenance.
3. Range or variable descriptor ("Easy-Moderate", "varies") → null-and-log;
   document the range in Notes for informational purposes.
4. Unmappable → null-and-log.
5. Empty string ("") → null; see §5.25.

---

## 5.15 Accessibility

- Free-text — no controlled vocabulary.
- Optional — leave blank if not documented.
- Record the accessibility description as documented by the authoritative source.
- Must not be inferred from surface type alone.
- Must not include personal assessments.

---

## 5.16 Description

**Priority (IMP-015)**: Description must capture ecological, physical, or cultural
character of the Trailthing — not administrative or governance structure. When
description_raw contains both ecological/physical content and administrative content,
extract and retain the ecological/physical content.

- 1-3 sentences.
- Must describe identity-defining characteristics: ecological, cultural, historical,
  or physical character.
- Must not include governance, ownership, amenities, or temporary conditions.
- Must not contradict controlled fields.
- Must not be copied verbatim from source — paraphrase or synthesize where possible.

Leave blank if description_raw contains only category/governance restatement with
no substantive ecological, physical, or historical content.

---

## 5.17 Identity Notes

Surfaced from `identity_notes_raw` at discovery stage.

**Use for:**
- Trail vs. trail segment boundary questions
- Alternate name conflicts
- Network membership uncertainty
- Disambiguation notes
- CROSS_COUNTY_CANDIDATE flag (IMP-046)
- PARTIAL MEMBERSHIP notes (IMP-046)
- Cross-tier trail flags
- REVIEW flags from normalization

**Rules:**
- Must not duplicate Notes content
- Must not contain operational or contextual notes (those go in Notes)
- Preserve uncertainty flags — do not resolve silently

---

## 5.18 Notes

**Customer-facing scope (IMP-014)**: Notes is a customer-facing field. Pipeline
source references, IMP numbers, session identifiers, and process-related content
must not appear. Strip these during normalization.

- Optional free text.
- Use for: temporary closures, access restrictions, parking notes, trailhead
  details, gap locations, construction updates, difficulty range documentation
  (when null-and-log was applied to difficulty_raw), surface variation notes.
- **Alternate names** (IMP-029): `ALT NAME: '[name]' — [source context]` — any name used
  by an authoritative source that differs from the canonical `name` field. Always preserve;
  never discard known alternate names.
- Must not include identity-defining characteristics (those belong in Description
  or Identity Notes).
- Must not include historical origin narrative.
- Must not contradict controlled fields.

**Note on surface/status/governance variation**: Unnamed variation along a Trailthing
corridor (e.g., "eastern third is unpaved") goes in Notes, not by creating additional
Trailthing records. Preserve such variation notes through normalization.

**Pipeline metadata stripping**: Apply the same metadata stripping logic as Site
Normalization Contract v6.0 §5.19. Strip session references, bare IMP references,
OBJECTID annotations, bare GPS placeholders, discovery run labels, and pipeline
staging notes. Preserve substantive content.

---

## 5.19 URLs

`url_primary`:
- Full https:// URL to primary authoritative source. Single value. Stable.

`urls` / `maps`:
- Semicolon-delimited URL lists.
- Each entry must be a well-formed https:// URL.
- Remove malformed URLs; log as warning.
- Remove duplicates.
- `maps` covers navigation/geometry resources (PDFs, GPX, KML, interactive viewers).
- `urls` covers all other authoritative URLs.

---

## 5.20 Parent Trailthing Validation

The `parent_id_raw` field references another Trailthing entity by ID or name.
This is a self-referential parent relationship used when one Trailthing is
documented as a sub-component of another.

**Normalization procedure:**

1. If `parent_id_raw` is absent or blank → no parent Trailthing; proceed.
2. If `parent_id_raw` is present:
   a. Look up the referenced entity ID in the Entity Graph.
   b. If found → validate: confirm entity_type == "Trailthing"; confirm no cycle;
      record `parent_id` in the normalized entity.
   c. If not found in Entity Graph → hold entity with `hold_reason = "unresolved_parent"`;
      log: "Parent Trailthing '[id]' not found in Entity Graph. Entity held pending
      partner county run or parent entity upsert."
   d. Cycle check: if the referenced parent's parent chain includes this entity →
      REJECT; log cycle detected.

**Site Network parent** (`parent_site_network_raw`): Resolve the Site Network name
against the Entity Graph to obtain the network_id. If found, populate
`parent_site_network_id`. If not found, log a warning and leave blank — Site Network
parent is not a blocking hold condition. Add to `identity_notes`:
`"Member of [parent_site_network_raw] — network ID [network_id or 'unresolved']."``

---

## 5.21 Parent Site Validation

The `site_parent_raw` field references a Site entity by name or ID. This is used
when the Trailthing is documented as wholly contained within a specific Site.

**Normalization procedure:**

1. If `site_parent_raw` is absent or blank → no parent Site; proceed.
2. If `site_parent_raw` is present:
   a. Look up the referenced Site entity in the Entity Graph (by name or ID).
   b. If found → record `site_parent_id` in the normalized entity; insert row
      into `trailthing_parents` (trailthing_id, parent_site_id).
   c. If not found → log warning; record the unresolved reference in
      `identity_notes` as: "Parent site '[site_parent_raw]' not yet in Entity Graph.";
      do not hold (Site parent is informational, not a blocking dependency).

---

## 5.22 Member Trailthing Name Resolution

The `member_trailthing_names_raw` field lists the names of Trailthings that are
members of this Trailthing (used when this entity is a container, e.g., a trail
system documenting its named component trails).

**Normalization procedure:**

1. If `member_trailthing_names_raw` is absent or blank → no members; proceed.
2. If present:
   a. Parse the semicolon-delimited list of member Trailthing names.
   b. For each name, look up the matching Trailthing entity ID in the Entity Graph.
   c. Record confirmed IDs in `member_trailthing_ids`.
   d. Names that cannot be resolved → log as WARNING; exclude from the ID list.
   e. If all member names are unresolvable → log WARNING; flag for review; do not
      hold the entity (member resolution is informational, not a blocking dependency).

**Relationship table**: `trailthing_members` (trailthing_id, member_trailthing_id)
is populated from the confirmed ID list.

---

## 5.23 Last Verified Date (IMP-013)

- Accept `last_verified_date` from the raw discovery record (populated at discovery
  with today's date).
- Validate format: must be ISO 8601 DATE format (YYYY-MM-DD).
- If present and valid → pass through unchanged.
- If format is invalid → attempt to parse and reformat; log WARNING if reformatted.
- If absent or null → log WARNING; leave blank.
- Never generate or infer a date not present in the raw record.

---

## 5.24 Field Verified (IMP-013)

- Accept `field_verified` from the raw discovery record (always `false` at discovery).
- Validate: must be boolean.
- String "false"/"False" → convert to boolean `false`; log.
- String "true"/"True" → convert to boolean `true`; log.
- Absent or null → default to `false`; log WARNING.
- Other values → null-and-log; flag for REVIEW.

---

## 5.25 Empty String Enforcement

**Run after normalizing all vocabulary-controlled fields and before integrity
anchor validation.**

Applies to: use_type, surface_type, origin_type, status, difficulty.

Empty string ("") is a data defect — convert to null and log. Do not apply to
free-text fields.

------------------------------------------------------------
# 6. MULTI-COUNTY NORMALIZATION RULES

- A Trailthing spanning multiple counties produces **one normalized entity**.
- `counties` must include all counties traversed, alphabetized, semicolon-delimited.
- Never segment multi-county Trailthings.
- No township or municipality fields for Trailthings.

------------------------------------------------------------
# 7. SPATIAL FIELDS

**Not applicable.** Trailthings are multi-location linear entities.

- No gps_lat, gps_lon
- No plus_code
- No township, municipality

The Normalization Engine does not run GPS validation, Plus Code computation, or
GIS spatial lookup for Trailthings.

------------------------------------------------------------
# 8. IDENTITY ANCHOR VALIDATION

The integrity anchor for Trailthings is:
`entity_type` + `name` + `counties`

This contract must verify:
- All anchor fields are present and non-blank
- `counties` is a valid, alphabetized list

The Normalization Engine v6.0 runs the deduplication check after this validation.

------------------------------------------------------------
# 9. VALIDATION LOGIC

Normalization must validate:

- Vocabulary-controlled fields map to valid values (Trailthing Vocabulary v6.0)
- No vocabulary-controlled field contains an empty string (§5.25)
- Source term and source hierarchy context are present and passed through verbatim
  (log WARNING if source_term_raw is blank — it is REQUIRED at discovery)
- Total length: numeric only, no units
- Counties: alphabetized, semicolon-delimited, "County" stripped
- Maps/URLs: each entry is a well-formed https:// URL; no embedded metadata;
  no empty segments
- No invented data
- Blank fields are true blanks (null, not empty string)
- Parent Trailthing: if referenced, entity exists in graph; no cycles
- Parent Site: if referenced, entity exists in graph (warning only if not found)
- Member Trailthing IDs: validated against Entity Graph; warnings on unresolvable

If any field fails validation:
- Surface as warning or error (per severity)
- Do not silently correct
- Log in normalization provenance

------------------------------------------------------------
# 10. DELIMITER INTEGRITY REQUIREMENTS

- Blank fields are true blanks (null, not empty string)
- No spaces between semicolons and values
- No trailing spaces or newlines within fields
- No collapsed delimiters (consecutive semicolons)
- No missing delimiters in multi-value fields

All anomalies must be logged.

------------------------------------------------------------
# 11. CONFLICT HANDLING

## 11.1 Conflicting Names
- Use the most authoritative source.
- Record alternates in Identity Notes.
- Log conflict.

## 11.2 Conflicting Length
- Use the most authoritative source (managing agency preferred).
- Log conflict; flag for review if unresolvable.

## 11.3 Conflicting Use Type, Surface Type, or Origin Type
- Use authoritative trail system sources.
- If unclear → null-and-log; flag in Identity Notes.

## 11.4 Conflicting Difficulty
- If sources disagree → null-and-log; note the conflict.

## 11.5 Conflicting Status
- Use most recent authoritative documentation.
- Log conflict.

## 11.6 Conflicting Parent References
- Parent Trailthing or parent Site conflicts → flag for REVIEW; do not attempt
  to resolve in normalization.

------------------------------------------------------------
# 12. MISSING DATA RULES

- If data is missing and cannot be verified → leave blank (null).
- Never estimate length.
- Never infer use type, surface type, or origin type.
- Never infer difficulty.
- Never infer governance from ownership or vice versa.
- source_term_raw absent at normalization → log WARNING; surface_term field blank;
  this indicates a discovery gap (source_term_raw is REQUIRED at discovery).

------------------------------------------------------------
# 13. AUDITABILITY REQUIREMENTS

Normalization must record in `normalization_provenance`:

- All sources consulted
- Confirmation that Trailthing Vocabulary Module v6.0 was read before
  normalizing vocabulary-controlled fields
- All vocabulary mappings applied (field, raw value, mapped value, mapping rule)
- All null-and-log decisions (field, raw value, reason)
- All REVIEW flags issued (field, raw value, reason)
- All empty string → null conversions (§5.25)
- All conflicts detected and how handled
- All fields left blank and why
- Source term and source hierarchy context pass-through confirmation
- Parent Trailthing resolution result (found / held / cycle detected)
- Parent Site resolution result (found / warning-only)
- Member Trailthing name resolution results (resolved / unresolved / excluded)
- Maps/URL validation results (valid/invalid URLs, duplicates removed)
- Difficulty source (which URL provided the rating, if applicable)
- Last verified date and field verified outcomes
- Identity Notes content surfaced from identity_notes_raw
- All delimiter-integrity corrections
- Identity anchor validation result
- Deduplication check result

Never overwrite previously logged normalization decisions.

------------------------------------------------------------
# 14. MODULE DEPENDENCIES

This contract depends on:

- **Trailthing Vocabulary Module v6.0** (vocabulary mapping tables)
- Trailthing Schema Module v6.0
- Resolution Engine v6.x
- Normalization Engine v6.0
- Entity Graph Schema v6.x
- Audit & Logging Module v6.x

------------------------------------------------------------
# END OF TRAILTHING NORMALIZATION CONTRACT v6.0
