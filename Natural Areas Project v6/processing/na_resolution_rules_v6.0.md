# RESOLUTION RULES MODULE v6.0
Authoritative Ontology, Identity, and Classification Rules for All Four Entity Types
Natural Areas Project — v6.x Pipeline

This module supersedes Resolution Rules Module v5.3.

------------------------------------------------------------
# CHANGES FROM v5.3 → v6.0

- **Entity types updated**: Six types → four. Trail, Trail Segment, and Trail
  Network replaced by Trailthing throughout. §5, §6, §7 updated accordingly.

- **Trailthing identity anchor** (§5.2): Single anchor replaces the three separate
  Trail, Trail Segment, and Trail Network anchors. Uses fuzzy-normalized name match
  + county overlap. No GPS proximity component.

- **Trailthing identity signature** (§6.2): Single signature replaces Trail (§6.2),
  Trail Segment (§6.3), and Trail Network (§6.5). Source term match added as a
  weighted component — verbatim source vocabulary is the primary v6.x input for
  future hierarchy classification.

- **Access Point identity anchor revised** (§5.3): GPS proximity bucket removed
  from the AP identity anchor. v6.x AP identity is anchored by name + governance
  + county + parent entity ID. GPS proximity was a useful deduplication heuristic
  in v5.x but is not an ontological identity criterion. See IMP-PENDING-AP-AUDIT
  in the improvement tracker — after sufficient county runs, an AP deduplication
  audit will evaluate whether dropping GPS proximity allows duplicates through.

- **Core identity principles updated** (§4): §4.5 "Trails Are Not Sites" →
  "Trailthings Are Not Sites." §4.7 "Segments Are Not Trails" retired — no
  sub-classification of Trailthings in v6.x. §4.8 "Networks Are Not Physical
  Land Units" narrowed to Site Networks.

- **Trailthing classification prohibition added** (§4.12): Discoverers and the
  Resolution Engine must not classify Trailthings as trail vs. trail segment vs.
  trail network. Classification is deferred to after sufficient data collection
  (IMP-007).

- **Trailthing rules section added** (§10): Governs Trailthing identity, the
  no-classification mandate, source term capture, and parent relationship rules.

- **Network rules simplified** (§11): Trail Network rules removed; Site Network
  rules retained.

- **Module dependencies updated to v6.0.** Discovery Output Specification
  reference removed (module retired).

- **All v5.3 core rules carried forward**: identity first, raw values authoritative,
  governance ≠ identity, features are not entities, no inference, multi-county
  entities are single entities, tier precedence, parent/child site rules.

------------------------------------------------------------
# 1. PURPOSE

The Resolution Rules Module v6.0 defines the **authoritative ontology and
identity framework** for all four entity types in the Natural Areas Project.
It establishes:

- What each entity type *is*
- How identity is recognized
- How similarity is interpreted
- How ambiguous cases are resolved
- How category decisions are made
- How parent/child relationships are determined
- How multi-county identity is handled
- How conflicts are overridden

This module is the **single source of truth** for identity and classification
logic. The Resolution Engine v6.x executes these rules; it does not define them.

------------------------------------------------------------
# 2. SCOPE

This module governs:

- All four entity types: Site, Trailthing, Site Network, Access Point
- All identity-bearing objects discovered in v6.x
- All baseline (Tier-0) identity seeds
- All ambiguous or conflicting cases
- All parent/child Site relationships
- All Trailthing hierarchy relationships
- All multi-county identity decisions
- All category-level decisions for Sites

This module applies during:

- Resolution (identity detection, merging, conflict detection)
- Normalization (canonicalization and vocabulary decisions)
- Entity Upsert (database integration)

Discovery must not apply these rules; it collects raw values only.

------------------------------------------------------------
# 3. CROSS-MODULE ALIGNMENT (v6.x)

This module aligns with:

- **Discovery Protocol v6.x** — raw collection only
- **Discovery Metadata Specification v6.x** — identity, lineage, provenance,
  conflict, uncertainty
- **Resolution Engine v6.x** — executes identity anchors, signatures, and
  merge logic
- **Normalization Engine v6.x** — applies vocabulary and canonicalization
- **Child Site Rules Module v6.x** — governs parent/child Site relationships
- **Cross-County Resolution Protocol v6.x** — MC ID assignment and collision
  handling
- **TSV Output Specifications v6.x** — formatting only

All modules reference this one for identity and classification decisions.

------------------------------------------------------------
# 4. CORE IDENTITY PRINCIPLES

### 4.1 Identity First
Classification is based on **ontological identity**, not amenities, marketing
language, or management.

### 4.2 Raw Values Are Authoritative
Identity is determined from raw discovery values and metadata, not normalized
or inferred values.

### 4.3 Governance ≠ Identity
Ownership, governance, partner agencies, and coordination do not determine
entity type or category.

### 4.4 Features Are Not Entities
Amenities (playgrounds, shelters, overlooks, parking lots) are Features unless
explicitly documented as identity-bearing.

### 4.5 Trailthings Are Not Sites
A named trail-related entity is always a Trailthing, never a Site — regardless
of its location, governance, or naming. See Child Site Rules Module v6.x §4.

### 4.6 Access Points Are Never Sites
Trailheads, parking areas, boat launches, and entrances are Access Points.

### 4.7 Site Networks Are Not Physical Land Units
Site Networks are collections of Sites, not physical places.

### 4.8 Provenance Always Wins
When sources conflict, tier precedence and provenance metadata determine
authority.

### 4.9 No Inference
Identity must never be inferred from:
- Layout or proximity
- GIS geometry
- Implied relationships
- Marketing language
- URL structure or naming conventions

### 4.10 Multi-County Entities Are Single Entities
No entity may be segmented by county. One physical entity = one record,
regardless of how many counties it spans.

### 4.11 No Baseline Override
Baseline (Tier-0) identity seeds are the lowest-authority source. Authoritative
discovery always overrides baseline for identity, entity type, and field values.

### 4.12 No Trailthing Classification
The Resolution Engine must not classify Trailthings as trail, trail segment,
trail network, or any other sub-type. `source_term_raw` and
`source_hierarchy_context_raw` are passed through verbatim. Trailthing
hierarchy is captured through parent_id relationships only when explicitly
documented by the authoritative source. Classification is deferred to after
sufficient county runs under v6.x (IMP-007).

------------------------------------------------------------
# 5. IDENTITY ANCHORS (STRICT PREREQUISITES)

Identity anchors define when two records *may* represent the same real-world
entity. If anchors fail, similarity scoring is not computed.

Anchors use **raw discovery fields only**.

### 5.1 Site Identity Anchor
- Fuzzy-normalized `name_raw` match
- Overlap in `counties_raw`

### 5.2 Trailthing Identity Anchor
- Fuzzy-normalized `name_raw` match
- Overlap in `counties_raw`

No source term classification required. Two Trailthing records may anchor
on name + county regardless of whether their source terms differ (one source
may call it a "trail system," another a "greenway" — same entity).

### 5.3 Access Point Identity Anchor
- `identity_parent_entity_id` matches (or raw parent name + county context
  if unresolved)
- Fuzzy-normalized `name_raw` match (where name is present)
- Overlap in `counties_raw`

**Note**: GPS proximity bucket was removed from the AP anchor in v6.0. AP
identity in v6.x is anchored by parent entity + name + county. GPS is acquired
after resolution and does not feed back into identity. See IMP-PENDING-AP-AUDIT
in the improvement tracker — an AP deduplication audit is scheduled after
sufficient v6 county runs to confirm this change does not allow duplicates
through.

### 5.4 Site Network Identity Anchor
- Fuzzy-normalized `network_name_raw` match
- Exact match on `network_type_raw` (case-folded for matching only)

------------------------------------------------------------
# 6. IDENTITY SIGNATURES (FUZZY SIMILARITY)

Identity signatures define how similarity is computed (0–100). Weights are
authoritative and executed by the Resolution Engine v6.x.

### 6.1 Site Identity Signature
- Name similarity — 40
- Organizational similarity — 35
- County overlap — 10
- Location similarity — 10
- URL overlap — 5

### 6.2 Trailthing Identity Signature
- Name similarity — 40
- County overlap — 15
- Source term similarity — 15
- Governance match — 15
- URL overlap — 10
- Length similarity — 5

**Source term similarity** measures whether the source terms used by two
records are compatible (e.g., "trail system" and "greenway network" may
score lower than "trail system" and "trail system"). This is an input to
the future classification analysis, not a blocking identity criterion.
A low source term similarity score does not prevent a merge if name and
county anchors are strong.

### 6.3 Access Point Identity Signature
- Parent match — 50
- Name similarity — 30
- Type match — 15
- County overlap — 5

**GPS distance removed**: GPS proximity was a v5.x signature component.
In v6.x it is not used in AP identity scoring. See §5.3 note and improvement
tracker IMP-PENDING-AP-AUDIT.

### 6.4 Site Network Identity Signature
- Name similarity — 50
- Network type match — 20
- Governance match — 15
- County overlap — 10
- URL overlap — 5

------------------------------------------------------------
# 7. ENTITY-TYPE DEFINITIONS (ONTOLOGICAL)

### 7.1 Site
A named, bounded, identity-bearing land unit recognized by authoritative sources.
May be top-level or a child Site (with `parent_site_id`).

### 7.2 Trailthing
A named, identity-bearing trail-related entity documented by authoritative sources.
Encompasses what was previously classified as Trail, Trail Segment, or Trail Network.
Sub-classification is deferred pending data collection across v6.x county runs.

### 7.3 Site Network
A named organization or designation that manages, coordinates, or encompasses
two or more Sites in the project, documented in authoritative sources.

### 7.4 Access Point
A named, visitor-facing entrance or access location — trailhead, parking area,
boat launch, documented entry point — for a Site or Trailthing.

------------------------------------------------------------
# 8. CATEGORY RULES FOR SITES

Category decisions apply only to Sites and use vocabulary from the Site
Vocabulary Module v6.x.

### 8.1 Categories Must Be Documented
Category must be explicitly stated or clearly implied by authoritative sources.

### 8.2 Ecology Does Not Determine Category
Ecological character belongs in Description and Habitat Type, not Category.

### 8.3 Category Edge Cases
- Boardwalk → Feature (not a Site or Trailthing)
- Natural Play Area → Feature
- Linear Park → Category: Park (Subtype: Linear Park)
- Greenway (place-based) → Category: Greenway Corridor
- Greenway (corridor-based trail) → Trailthing, not a Site
- Stormwater Basin (no ecological identity) → Excluded
- Mitigation Bank → Category: Conservation Area
- Cemetery with natural area → Category: Cemetery
- Campground → Category: Camp (if identity-bearing)
- Water Access Site → Category: Water Access Site
- NRHP archaeological sites → Category: Archaeological Site or Historic Site

------------------------------------------------------------
# 9. ACCESS POINT RULES

### 9.1 Access Points Are Visitor-Facing Entry Points
Includes trailheads, parking areas, boat launches, documented entrances.
An AP must have a documented parent entity (Site or Trailthing).

### 9.2 Access Points Are Never Sites
Even if large, named, or heavily used. If an entity has meaningful acreage,
a description of its own character, and governance distinct from its parent
Trailthing, flag it as RECLASSIFICATION_CANDIDATE (IMP-114) for review.

### 9.3 Access Point Parents
In v6.x, APs may parent to a Site, a Trailthing, or both. At least one
parent is required. An AP with no resolvable parent is an identity error
and must be routed to the manual review queue.

### 9.4 Access Point Edge Cases
- Scenic pull-offs → Access Point if documented as entrances
- Administrative access → Access Point only if documented
- Trail intersections → Geometry, not entities
- Hazard portages → Access Point (paired with launch point per water trail rules)

------------------------------------------------------------
# 10. TRAILTHING RULES

### 10.1 Trailthings Are Named and Identity-Bearing
A Trailthing must have a documented name from an authoritative source.
Unnamed paths, informal connections, or marketing slogans do not qualify.

### 10.2 No Classification
The Resolution Engine must not classify a Trailthing as trail, trail segment,
trail network, or any other sub-type. This is the no-classification mandate
(§4.12). The source term and source hierarchy context fields capture how
authoritative sources describe the entity — this data will inform future
classification decisions.

### 10.3 Source Term Is Not Identity
Two records with different `source_term_raw` values may represent the same
entity. Source term similarity contributes to the identity signature but is
not a blocking prerequisite.

### 10.4 Trailthing Hierarchy
Parent-child relationships between Trailthings are recorded only when the
authoritative source explicitly frames one entity as a component, member,
section, or part of another. Do not infer hierarchy from geography, governance,
or name similarity.

### 10.5 Unnamed Surface, Status, or Governance Variation
Variation along a Trailthing's corridor (surface changes, governance handoffs,
partial closures) does not require multiple Trailthing records. Document in
Notes. Only create child Trailthings for variation when the source itself names
and documents those sections as distinct identity-bearing entities.

### 10.6 Trailthings Are Not Sites
A Trailthing contained within a Site is a Trailthing with `site_parent_id` —
never a child Site. See Child Site Rules Module v6.x §4.

------------------------------------------------------------
# 11. SITE NETWORK RULES

### 11.1 Site Networks Must Be Documented
A Site Network must be explicitly documented as a named organization or
designation managing or encompassing two or more Sites. Networks cannot
be inferred from proximity or shared governance.

### 11.2 Threshold Rules Apply
Site Network creation is governed by four threshold rules keyed on
`network_type` and `org_type`. See Site Network Schema Module v6.x §4 for
the authoritative threshold rules.

### 11.3 Site Networks Are Not Trailthing Networks
Collections of Trailthings are not Site Networks. A Trailthing may reference
a Site Network as its external parent (`parent_site_network_id`) when the
authoritative source explicitly frames that relationship — but the Site Network
record itself is a collection of Sites, not Trailthings.

### 11.4 No Nested Site Networks
No Site Network may have another Site Network as a parent.

------------------------------------------------------------
# 12. PARENT/CHILD SITE RULES

### 12.1 Identity Requirements
Child Sites must be: named, identity-bearing, documented, and internal to
the parent. See Child Site Rules Module v6.x for full rules.

### 12.2 Evidence Requirements
Must be supported by authoritative documentation — official maps, government
GIS layers, management plans, signage, published materials, or historical
documentation.

### 12.3 Prohibited Cases
- Features (playgrounds, shelters, overlooks)
- Temporary labels
- Habitat types without independent identity
- Administrative zones without independent identity
- Named buildings (unless explicitly identity-bearing)
- Trailthing-type entities (those are Trailthings with site_parent_id)

### 12.4 Boundary Rules
Child Site counties must be a subset of the parent's counties unless
explicitly documented otherwise.

### 12.5 Multi-Level Hierarchies
Allowed only when explicitly documented. Each level must independently
satisfy all identity requirements.

### 12.6 Circularity
Prohibited. The Normalization Engine must detect and reject cycles.

------------------------------------------------------------
# 13. MULTI-COUNTY RULES

### 13.1 Single Entity Rule
Entities spanning multiple counties must be represented as a single entity.
No entity may be segmented by county. See Cross-County Resolution Protocol
v6.x for MC ID assignment procedures.

### 13.2 County Lists
Must reflect all documented counties, semicolon-delimited and alphabetized
after normalization.

### 13.3 No Inference
Counties must not be inferred from GIS geometry or proximity. Only counties
explicitly documented in authoritative sources may be recorded.

### 13.4 Sequence Gaps Are Expected
Do not infer missing entities from gaps in entity ID sequence numbers. Gaps
arise from provisional IDs superseded during resolution, entities merged into
existing records, or sequence numbers withdrawn during QA (IMP-117).

------------------------------------------------------------
# 14. CONFLICT OVERRIDE RULES

### 14.1 Tier Precedence
Tier 1 > Tier 2 > Tier 3 > Tier 4 > Tier 5 > Tier 6 > Tier 7 > Tier 8 >
Tier 0 (Baseline).

### 14.2 Category Conflicts
This module overrides all others for category decisions.

### 14.3 Entity-Type Conflicts
This module determines final entity type. A record cannot be simultaneously
a Site and a Trailthing. When entity type is disputed across sources, this
module's definitions in §7 are authoritative.

### 14.4 Governance Conflicts
Normalization Engine resolves unless ambiguous; this module decides ambiguous
cases.

### 14.5 Parent/Child Conflicts
Child Site Rules Module v6.x governs; this module resolves edge cases not
covered there.

### 14.6 Provenance Conflicts
Resolved using tier precedence, source authority, and discovery path. The
higher-tier source wins unless the lower-tier source provides evidence that
specifically contradicts the higher-tier source's claim.

------------------------------------------------------------
# 15. MODULE DEPENDENCIES

This module depends on:

- Discovery Protocol v6.x
- Discovery Metadata Specification v6.x
- Resolution Engine v6.x
- Normalization Engine v6.x
- Child Site Rules Module v6.x
- Cross-County Resolution Protocol v6.x
- Site Schema Module v6.x
- Trailthing Schema Module v6.x
- Site Network Schema Module v6.x
- Access Point Schema Module v6.x
- Vocabulary Modules v6.x

------------------------------------------------------------
# END OF RESOLUTION RULES MODULE v6.0
