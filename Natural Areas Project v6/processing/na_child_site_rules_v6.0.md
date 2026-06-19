# NATURAL AREAS PROJECT
# CHILD SITE RULES MODULE v6.0
Authoritative Ontological Rules for Parent–Child Site Relationships
Natural Areas Project — v6.x Pipeline

This module supersedes Child Site Rules Module v5.4.

------------------------------------------------------------
# CHANGES FROM v5.4 → v6.0

- **Entity type model updated**: Trail, Trail Segment, and Trail Network references
  replaced throughout with Trailthing. The Trailthing prohibition (§4) is the
  primary substantive addition — the explicit rule that a Trailthing-type entity
  must never be modeled as a child Site.

- **Relationship boundary table added** (§5): Distinguishes three containment
  patterns — Site-in-Site (child site), Trailthing-in-Site (site_parent_id on
  Trailthing), and Sites-in-collection (Site Network membership). These are
  mutually exclusive and governed by separate modules.

- **Child Site capabilities clarified** (§6): A child Site is a full Site entity.
  It may have its own Trailthings, child Sites, Access Points, and Site Network
  memberships. Containment within a parent Site does not restrict its relationships.

- **All v5.4 rules carried forward**: identity rules, evidence requirements,
  prohibited cases, boundary rules, county inheritance rules, multi-level
  hierarchy rules, circularity rules, discovery rules, normalization rules.

- **Module dependencies updated to v6.0.**

------------------------------------------------------------
# 1. PURPOSE

Child Sites represent named, identity-bearing internal land units contained
within a parent Site. A child Site is a **Site** with a populated `parent_site_id`,
using the same schema as all Sites.

This module defines:

- Ontological rules
- Identity rules
- Evidence requirements
- The Trailthing prohibition
- Relationship boundary rules
- Prohibited cases
- Boundary rules
- County inheritance rules
- Multi-level hierarchy rules
- Circularity rules
- Discovery rules
- Normalization-phase validation rules

This module contains **no schema** and **no vocabularies**.
All fields are defined in the Site Schema Module v6.x.

------------------------------------------------------------
# 2. IDENTITY RULES

A Site may be assigned a Parent Site only if all of the following are true:

- The child has a documented, stable, name-based identity.
- The child exists within the spatial, cultural, historical, or administrative
  scope of the parent.
- The relationship is explicitly documented in authoritative sources.
- The child is not a feature, amenity, or administrative zone.
- The child is not a standalone Site in authoritative sources.
- The child is not a Trailthing-type entity (see §4).
- The relationship is not inferred from layout or proximity.

------------------------------------------------------------
# 3. EVIDENCE REQUIREMENTS

Acceptable evidence:

- Official maps
- Government GIS layers
- Management plans
- Signage
- Published materials
- Historical documentation

Unacceptable evidence:

- User-generated content
- Informal names
- Temporary labels
- Amenities lists
- Inferred relationships

------------------------------------------------------------
# 4. THE TRAILTHING PROHIBITION

**A Trailthing is not a Site. A child Site must never be created to represent
a trail, trail system, trail corridor, greenway, water trail, or any other
entity that would qualify as a Trailthing.**

This rule applies regardless of:
- Where the Trailthing is located (even if entirely within a single Site)
- Who manages it (even if managed by the same organization as the parent Site)
- How it is named (even if named after the Site it is contained within)
- Whether it is access-dependent on a specific Site

If a trail-related entity is contained within or access-dependent on a Site,
it is captured as a **Trailthing with `site_parent_id`** referencing that Site.
It is never captured as a child Site.

**Correct pattern:**
```
Pickerington Ponds Metro Park  (Site)
  └── Shorebird Loop Trail  (Trailthing, site_parent_id → Pickerington Ponds Metro Park)
```

**Prohibited pattern:**
```
Pickerington Ponds Metro Park  (Site)
  └── Shorebird Loop Trail  (child Site — WRONG: trail entities are always Trailthings)
```

**Corollary**: A child Site may itself have Trailthings referencing it via
`site_parent_id`. A child Site is a full Site entity in all respects — it may
have its own named trails, child Sites of its own, Access Points, and Site
Network memberships. Containment within a parent Site does not restrict its
relationships.

**Correct three-level example:**
```
Cuyahoga Valley National Park  (parent Site)
  └── Beaver Marsh Natural Area  (child Site, parent_site_id → CVNP)
        └── Beaver Marsh Boardwalk Trail  (Trailthing, site_parent_id → Beaver Marsh Natural Area)
```

------------------------------------------------------------
# 5. RELATIONSHIP BOUNDARY TABLE

Three distinct containment patterns exist in the v6.x entity model. They are
mutually exclusive. The entity type determines the correct pattern — not
geographic containment, governance, or naming.

| Situation | Correct pattern | Governed by |
|---|---|---|
| Named bounded land unit within a larger named bounded land unit | Child Site (`parent_site_id` on the child Site) | This module |
| Named trail-related entity within or access-dependent on a Site | Trailthing with `site_parent_id` referencing the Site | Trailthing Schema Module v6.x |
| Sites belonging to an organizational collection or formal designation | Site Network membership (`site_network_members` table) | Site Network Schema Module v6.x |

**Do not use `parent_site_id` to model Site Network membership.** A park
district managing multiple sites is a Site Network, not a parent Site.
The distinction: parent_site_id models physical or administrative containment
of one named land unit within another; Site Networks model organizational
collections where the sites are not contained within each other.

**Do not use Site Network membership to model physical containment.** If Site
A is physically inside Site B and documented as such, that is a child site
relationship, not a Site Network relationship.

------------------------------------------------------------
# 6. PROHIBITED CASES

A Site must not be assigned a Parent Site if:

- The name refers to a feature (playground, shelter, parking lot)
- The name refers to a temporary condition
- The name refers to a habitat type without independent documented identity
- The name refers to a trail, trail system, greenway, corridor, or any other
  Trailthing-type entity (see §4)
- The name refers to an administrative zone without independent documented identity
- The name is not identity-bearing
- The name is undocumented
- The name refers to a building or facility unless explicitly identity-bearing
  in authoritative sources

------------------------------------------------------------
# 7. BOUNDARY RULES

Child Sites may be spatially, conceptually, or administratively contained
within the parent.

A child Site must not:

- Span counties independently of the parent without documentation
- Contradict the parent's documented boundaries
- Represent a larger area than the parent
- Exist in a different state than the parent

------------------------------------------------------------
# 8. COUNTY INHERITANCE RULES

County rules apply to **normalized** county sets (`counties`), not raw values.

- A child Site's counties must be a **subset** of the parent's counties unless
  explicitly documented otherwise.
- Documented exceptions must trigger a Parent–Child Boundary Review.
- A child Site must not list counties not documented for the parent without
  explicit evidence.
- A child Site is not required to inherit all parent counties; it reflects its
  own documented footprint.

------------------------------------------------------------
# 9. MULTI-LEVEL HIERARCHY RULES

Multi-level hierarchies are allowed only when explicitly documented.

Each level must independently satisfy all identity rules in §2.

No inferred intermediate levels.

Depth is not constrained — the schema supports unlimited nesting — but each
level must be independently named and documented in authoritative sources.

------------------------------------------------------------
# 10. CIRCULARITY RULES

Circular parentage is prohibited:

- A → B → A
- A → B → C → A

The Normalization Engine must detect and reject cycles before upsert.

------------------------------------------------------------
# 11. DISCOVERY RULES

Discovery must:

- Create independent raw records for identity-bearing internal land units
- Never assign `parent_site_id` during discovery — note suspected parent
  relationships in `identity_notes_raw` only
- Reject undocumented names
- Flag ambiguous cases for normalization review
- Create Trailthing records (not child Site records) for any trail-related
  entity found within a site

Discovery must not:

- Infer parent relationships
- Suppress internal units
- Assign parent IDs
- Treat features as child Sites
- Treat Trailthings as child Sites

------------------------------------------------------------
# 12. NORMALIZATION RULES

Normalization must:

- Validate that the parent exists as a normalized Site
- Validate that the child meets all identity rules in §2
- Validate that the child is not a Trailthing-type entity (§4)
- Validate that the relationship is explicitly documented
- Validate that no circularity is introduced (§10)
- Validate county subset rules (§8)
- Validate state consistency (§7)
- Apply Child Site Rules before upsert
- Reject invented or inferred relationships

Normalization must not:

- Infer parent relationships
- Override Resolution identity decisions
- Modify lineage metadata

------------------------------------------------------------
# 13. MODULE DEPENDENCIES

This module depends on:

- Site Schema Module v6.0 (field definitions, `parent_site_id`, relationship tables)
- Trailthing Schema Module v6.0 (`site_parent_id` — the correct pattern for
  trail-related entities contained within a Site)
- Site Network Schema Module v6.0 (organizational collection relationships —
  distinct from child site containment)
- Resolution Engine v6.0
- Normalization Engine v6.0
- Discovery Protocol Module v6.0

------------------------------------------------------------
# END OF CHILD SITE RULES MODULE v6.0
