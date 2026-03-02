# NATURAL AREAS PROJECT
# RESOLUTION ENGINE v5.0
(Authoritative Specification for Entity Resolution and Deduplication)

This module defines the complete resolution workflow for identifying and merging
duplicate entities discovered from multiple sources across all discovery tiers.

This document supersedes all v4.x resolution logic.

------------------------------------------------------------
# CHANGES FROM v4.0

- **Philosophy clarified**: Resolution detects conflicts, Normalization resolves them
- **Entity-specific rules**: Detailed identity matching rules for each entity type
- **Parent resolution**: Clear workflow for resolving parent relationships
- **Conflict preservation**: Explicit rules for what to flag vs. merge
- **Provenance tracking**: Complete audit trail of merge decisions
- All version references updated to v5.0

------------------------------------------------------------
# 1. PURPOSE

The Resolution Engine v5.0 provides the authoritative workflow for:

- Identifying duplicate entities across sources and tiers
- Merging duplicate records into single resolved records
- Detecting and preserving conflicts (not resolving them)
- Resolving parent entity relationships (names → IDs)
- Tracking merge provenance for audit trails
- Reducing raw discovery volume before normalization

**Key Principle:**
Resolution = Identity Detection + Merging + Conflict Detection

Resolution does NOT normalize vocabulary or choose between conflicting values.
That happens in Normalization.

------------------------------------------------------------
# 2. RESOLUTION PHILOSOPHY

## 2.1 Core Principle: Detect Conflicts, Don't Resolve Them

**Resolution Phase (THIS DOCUMENT):**
- Identify which raw records represent the same entity
- Merge complementary information (features, URLs)
- Detect conflicts (different values for same field)
- Preserve all conflicting values
- Flag for normalization to resolve

**Normalization Phase (LATER):**
- Choose canonical values from conflicts
- Apply tier authority rules
- Make final decisions

## 2.2 Why This Separation?

**Benefits:**
- Resolution can run without decision rules
- Can re-run normalization with different rules
- Audit trail shows what was detected vs. what was chosen
- Clear separation of concerns

**Example:**
```
Resolution detects:
  acres = {values: ["85", "87"], conflict: true}

Normalization resolves:
  acres = 85 (Tier 4 authority over Tier 8)
```

------------------------------------------------------------
# 3. RESOLUTION PIPELINE ARCHITECTURE

```
INPUT: Raw Discovery Records
  ↓
┌────────────────────────────────────┐
│ PHASE 1: GROUPING                 │
│ Group by entity type + county     │
└────────────────────────────────────┘
  ↓
┌────────────────────────────────────┐
│ PHASE 2: IDENTITY MATCHING        │
│ Compare records within groups     │
│ Calculate similarity scores       │
└────────────────────────────────────┘
  ↓
┌────────────────────────────────────┐
│ PHASE 3: MERGE DECISIONS          │
│ Auto-merge (≥80)                  │
│ Flag for review (50-79)           │
│ Keep separate (<50)               │
└────────────────────────────────────┘
  ↓
┌────────────────────────────────────┐
│ PHASE 4: FIELD MERGING            │
│ Union (features, URLs)            │
│ Conflict (acres, status)          │
│ Choose (name, description)        │
└────────────────────────────────────┘
  ↓
┌────────────────────────────────────┐
│ PHASE 5: PARENT RESOLUTION        │
│ Resolve parent names → IDs        │
│ Resolve network members → IDs     │
└────────────────────────────────────┘
  ↓
OUTPUT: Resolved Records (one per entity)
```

------------------------------------------------------------
# 4. PHASE 1: GROUPING

## 4.1 Purpose

Reduce comparison space by grouping similar records.

## 4.2 Grouping Algorithm

```python
def group_raw_records(raw_records):
    """
    Group records to reduce O(n²) comparisons
    """
    groups = defaultdict(list)
    
    for record in raw_records:
        key = (
            record.entity_type,      # "Site", "Trail", etc.
            record.county_primary    # "Wood"
        )
        groups[key].append(record)
    
    return groups
```

## 4.3 Why Group?

**Without grouping:**
- 100 records → 4,950 comparisons (n² / 2)

**With grouping:**
- Sites (40) + Trails (30) + Access Points (20) + Others (10)
- 780 + 435 + 190 + 45 = 1,450 comparisons (70% reduction)

## 4.4 Cross-County Entities

**Special handling for entities that span multiple counties:**

```python
if len(record.counties) > 1:
    # Add to all relevant county groups
    for county in record.counties:
        key = (record.entity_type, county)
        groups[key].append(record)
```

**Example:**
```
Trail: "Slippery Elm Trail"
Counties: ["Wood", "Lucas"]

Added to both:
  - ("Trail", "Wood") group
  - ("Trail", "Lucas") group

Can match with records from either county
```

------------------------------------------------------------
# 5. PHASE 2: IDENTITY MATCHING

## 5.1 Two-Level Matching Strategy

**Level 1: Identity Anchor (Strict)**
- Must match exactly for records to be compared
- Filters out obvious non-matches quickly

**Level 2: Identity Signature (Fuzzy)**
- Calculate similarity score 0-100
- Multiple fields contribute to score
- Thresholds determine merge decision

## 5.2 Entity-Specific Identity Rules

Each entity type has different identity characteristics.

------------------------------------------------------------
# 6. SITE RESOLUTION

## 6.1 Site Identity Anchor

**Must match for comparison:**
```python
def get_site_identity_anchor(record):
    return (
        normalize_name_fuzzy(record.name_raw),  # Fuzzy match
        frozenset(normalize_counties(record.counties_raw))
    )
```

**Examples:**
```
"Carter Historic Farm" + {"Wood"} 
  matches
"carter historic farm" + {"Wood"}

"Carter Historic Farm" + {"Wood"}
  doesn't match
"Carter Farm" + {"Lucas"}  (different county)
```

## 6.2 Site Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_site_similarity(site_A, site_B):
    score = 0
    
    # Name similarity (40 points)
    name_sim = fuzzy_string_match(site_A.name_raw, site_B.name_raw)
    score += name_sim * 40
    
    # Category match (15 points)
    if normalize(site_A.category_raw) == normalize(site_B.category_raw):
        score += 15
    
    # Ownership match (10 points)
    if normalize(site_A.ownership_raw) == normalize(site_B.ownership_raw):
        score += 10
    
    # Governance match (10 points)
    if normalize(site_A.governance_raw) == normalize(site_B.governance_raw):
        score += 10
    
    # Counties overlap (10 points)
    if set(site_A.counties) & set(site_B.counties):
        score += 10
    
    # Location similarity (10 points)
    if location_similar(site_A.location_raw, site_B.location_raw):
        score += 10
    
    # URL overlap (5 points)
    if url_overlap(site_A.url_all_raw, site_B.url_all_raw):
        score += 5
    
    return score
```

## 6.3 Site Merge Rules

**Field-specific merge strategies:**

```python
SITE_MERGE_RULES = {
    # Choose canonical (from highest tier)
    "name": "choose",
    "description": "choose",
    "location": "choose",
    
    # Choose or flag conflict if different
    "category": "choose_or_conflict",
    "subtype": "choose_or_conflict",
    "designation": "choose_or_conflict",
    "status": "choose_or_conflict",
    "ownership": "choose_or_conflict",
    "governance": "choose_or_conflict",
    
    # Always flag conflict if different
    "acres": "conflict",
    "parent_site": "conflict",
    
    # Union (collect all)
    "features": "union",
    "notes": "union",
    "counties": "union",
    "urls": "union",
    "maps": "union",
    
    # Coordination can be union
    "coordination": "union"
}
```

------------------------------------------------------------
# 7. TRAIL RESOLUTION

## 7.1 Trail Identity Anchor

**Must match for comparison:**
```python
def get_trail_identity_anchor(record):
    return (
        normalize_name_fuzzy(record.name_raw),
        frozenset(normalize_counties(record.counties_raw))
    )
```

## 7.2 Trail Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_trail_similarity(trail_A, trail_B):
    score = 0
    
    # Name similarity (40 points)
    name_sim = fuzzy_string_match(trail_A.name_raw, trail_B.name_raw)
    score += name_sim * 40
    
    # Trail use type match (15 points)
    if normalize(trail_A.trail_use_type_raw) == normalize(trail_B.trail_use_type_raw):
        score += 15
    
    # Total length similarity (15 points)
    if length_similar(trail_A.total_length_miles_raw, trail_B.total_length_miles_raw):
        score += 15
    
    # Governance match (10 points)
    if normalize(trail_A.governance_raw) == normalize(trail_B.governance_raw):
        score += 10
    
    # Counties overlap (10 points)
    if set(trail_A.counties) & set(trail_B.counties):
        score += 10
    
    # Surface type match (5 points)
    if normalize(trail_A.surface_type_raw) == normalize(trail_B.surface_type_raw):
        score += 5
    
    # URL overlap (5 points)
    if url_overlap(trail_A.url_all_raw, trail_B.url_all_raw):
        score += 5
    
    return score
```

## 7.3 Trail Merge Rules

```python
TRAIL_MERGE_RULES = {
    "name": "choose",
    "alternate_names": "union",
    "description": "choose",
    "trail_history": "choose",
    
    "trail_use_type": "choose_or_conflict",
    "trail_surface_type": "choose_or_conflict",
    "trail_origin_type": "choose_or_conflict",
    "status": "choose_or_conflict",
    
    "total_length_miles": "conflict",
    "difficulty": "conflict",
    "accessibility": "choose",
    
    "governance": "choose_or_conflict",
    "partner_agencies": "union",
    
    "counties": "union",
    "notes": "union",
    "urls": "union",
    "maps": "union"
}
```

------------------------------------------------------------
# 8. TRAIL SEGMENT RESOLUTION

## 8.1 Trail Segment Identity Anchor

**CRITICAL: Parent trail must match:**

```python
def get_segment_identity_anchor(record):
    return (
        record.parent_trail_id,  # MUST be same parent
        normalize_name_fuzzy(record.segment_name_raw) if record.segment_name_raw else None
    )
```

**Special rule:**
```python
# Cannot merge segments with different parents
if seg_A.parent_trail_id != seg_B.parent_trail_id:
    return 0  # Similarity = 0, never merge
```

## 8.2 Trail Segment Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_segment_similarity(seg_A, seg_B):
    # Parent must match first
    if seg_A.parent_trail_id != seg_B.parent_trail_id:
        return 0
    
    score = 0
    
    # Segment name similarity (50 points)
    if seg_A.segment_name_raw and seg_B.segment_name_raw:
        name_sim = fuzzy_string_match(seg_A.segment_name_raw, seg_B.segment_name_raw)
        score += name_sim * 50
    elif not seg_A.segment_name_raw and not seg_B.segment_name_raw:
        # Both unnamed - rely on other characteristics
        score += 25  # Partial credit
    
    # Length similarity (20 points)
    if length_similar(seg_A.segment_length_miles_raw, seg_B.segment_length_miles_raw):
        score += 20
    
    # Surface type match (15 points)
    if normalize(seg_A.surface_type_raw) == normalize(seg_B.surface_type_raw):
        score += 15
    
    # Counties overlap (10 points)
    if set(seg_A.counties) & set(seg_B.counties):
        score += 10
    
    # Segment type match (5 points)
    if seg_A.segment_type_raw == seg_B.segment_type_raw:
        score += 5
    
    return score
```

## 8.3 Trail Segment Merge Rules

```python
SEGMENT_MERGE_RULES = {
    "segment_name": "choose",
    "parent_trail_id": "must_match",  # Special - error if different
    
    "segment_length_miles": "conflict",
    "surface_type": "choose_or_conflict",
    "segment_type": "choose_or_conflict",
    "status": "choose_or_conflict",
    
    "difficulty": "conflict",
    "accessibility": "choose",
    
    "governance": "choose_or_conflict",
    
    "description": "choose",
    "notes": "union",
    "counties": "union",
    "urls": "union",
    "maps": "union"
}
```

------------------------------------------------------------
# 9. ACCESS POINT RESOLUTION

## 9.1 Access Point Identity Anchor

**Must match for comparison:**

```python
def get_access_point_identity_anchor(record):
    return (
        record.identity_parent_entity_id,  # Must serve same parent
        gps_proximity_group(record.gps_raw, tolerance=100)  # Within 100m
    )
```

**GPS proximity grouping:**
```python
def gps_proximity_group(gps_raw, tolerance=100):
    """
    Group GPS coordinates into 100m grid cells
    Returns grid cell ID (lat_bucket, lon_bucket)
    """
    if not gps_raw:
        return None
    
    lat, lon = parse_gps(gps_raw)
    
    # 100m ≈ 0.001 degrees
    lat_bucket = round(lat, 3)
    lon_bucket = round(lon, 3)
    
    return (lat_bucket, lon_bucket)
```

## 9.2 Access Point Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_access_point_similarity(ap_A, ap_B):
    score = 0
    
    # Parent entity must match (40 points)
    if ap_A.identity_parent_entity_id == ap_B.identity_parent_entity_id:
        score += 40
    else:
        return 0  # Different parents = not same access point
    
    # GPS proximity (30 points)
    if gps_distance(ap_A.gps_raw, ap_B.gps_raw) < 50:  # Within 50m
        score += 30
    elif gps_distance(ap_A.gps_raw, ap_B.gps_raw) < 100:  # Within 100m
        score += 20
    
    # Access point type match (20 points)
    if normalize(ap_A.access_point_type_raw) == normalize(ap_B.access_point_type_raw):
        score += 20
    
    # Name similarity (10 points) - if both named
    if ap_A.name_raw and ap_B.name_raw:
        name_sim = fuzzy_string_match(ap_A.name_raw, ap_B.name_raw)
        score += name_sim * 10
    
    return score
```

## 9.3 Access Point Merge Rules

```python
ACCESS_POINT_MERGE_RULES = {
    "name": "choose",
    "access_point_type": "choose_or_conflict",
    "status": "choose_or_conflict",
    
    "parent_sites": "union",
    "parent_trails": "union",
    "parent_trail_segments": "union",
    
    "gps": "conflict",  # Flag if different GPS
    "address": "choose",
    
    "features": "union",
    "notes": "union",
    "urls": "union",
    "map_url": "union"
}
```

------------------------------------------------------------
# 10. TRAIL NETWORK RESOLUTION

## 10.1 Trail Network Identity Anchor

**Must match for comparison:**

```python
def get_trail_network_identity_anchor(record):
    return (
        normalize_name_fuzzy(record.network_name_raw),
        normalize(record.network_type_raw)
    )
```

## 10.2 Trail Network Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_trail_network_similarity(net_A, net_B):
    score = 0
    
    # Name similarity (50 points)
    name_sim = fuzzy_string_match(net_A.network_name_raw, net_B.network_name_raw)
    score += name_sim * 50
    
    # Network type match (20 points)
    if normalize(net_A.network_type_raw) == normalize(net_B.network_type_raw):
        score += 20
    
    # Governance match (15 points)
    if normalize(net_A.governance_raw) == normalize(net_B.governance_raw):
        score += 15
    
    # Counties overlap (10 points)
    if set(net_A.counties) & set(net_B.counties):
        score += 10
    
    # URL overlap (5 points)
    if url_overlap(net_A.url_all_raw, net_B.url_all_raw):
        score += 5
    
    return score
```

## 10.3 Trail Network Merge Rules

```python
TRAIL_NETWORK_MERGE_RULES = {
    "network_name": "choose",
    "network_type": "choose_or_conflict",
    "status": "choose_or_conflict",
    
    "total_length_miles": "conflict",
    "member_trail_count": "conflict",
    "member_trail_names": "union",
    
    "governance": "choose_or_conflict",
    "partner_agencies": "union",
    "ownership": "choose_or_conflict",
    
    "description": "choose",
    "notes": "union",
    "counties": "union",
    "states": "union",
    "urls": "union",
    "maps": "union"
}
```

------------------------------------------------------------
# 11. SITE NETWORK RESOLUTION

## 11.1 Site Network Identity Anchor

**Must match for comparison:**

```python
def get_site_network_identity_anchor(record):
    return (
        normalize_name_fuzzy(record.network_name_raw),
        normalize(record.network_type_raw)
    )
```

## 11.2 Site Network Identity Signature

**Similarity scoring (100 points total):**

```python
def calculate_site_network_similarity(net_A, net_B):
    score = 0
    
    # Name similarity (50 points)
    name_sim = fuzzy_string_match(net_A.network_name_raw, net_B.network_name_raw)
    score += name_sim * 50
    
    # Network type match (20 points)
    if normalize(net_A.network_type_raw) == normalize(net_B.network_type_raw):
        score += 20
    
    # Governance match (15 points)
    if normalize(net_A.governance_raw) == normalize(net_B.governance_raw):
        score += 15
    
    # Counties overlap (10 points)
    if set(net_A.counties) & set(net_B.counties):
        score += 10
    
    # URL overlap (5 points)
    if url_overlap(net_A.url_all_raw, net_B.url_all_raw):
        score += 5
    
    return score
```

## 11.3 Site Network Merge Rules

```python
SITE_NETWORK_MERGE_RULES = {
    "network_name": "choose",
    "network_type": "choose_or_conflict",
    "status": "choose_or_conflict",
    
    "member_count": "conflict",
    "member_site_names": "union",
    
    "governance": "choose_or_conflict",
    "partner_agencies": "union",
    "ownership": "choose_or_conflict",
    
    "description": "choose",
    "notes": "union",
    "counties": "union",
    "states": "union",
    "urls": "union",
    "map_url": "union"
}
```

------------------------------------------------------------
# 12. PHASE 3: MERGE DECISIONS

## 12.1 Decision Thresholds

```python
def decide_merge(similarity_score):
    if similarity_score >= 80:
        return "auto_merge", "high"
    elif similarity_score >= 50:
        return "flag_for_review", "medium"
    else:
        return "keep_separate", "low"
```

## 12.2 Manual Review Queue

**Records flagged for review:**
```python
review_queue = {
    "record_pair": ["rec_001", "rec_002"],
    "similarity_score": 65,
    "confidence": "medium",
    "reason": "Name similar but different category",
    "comparison": {
        "name": ("Carter Historic Farm", "Carter Farm"),
        "category": ("Park", "Historic Site"),
        "ownership": ("Wood County", "Wood County")
    }
}
```

**Human reviewer decides:**
- Merge
- Keep separate
- Need more information

------------------------------------------------------------
# 13. PHASE 4: FIELD MERGING

## 13.1 Three Merge Strategies

### **Strategy 1: UNION**

**Collect all values from all sources:**

```python
def merge_union(records, field):
    all_values = []
    for record in records:
        if record[field]:
            values = record[field].split(';')
            all_values.extend(values)
    
    # Deduplicate and sort
    unique_values = sorted(set(all_values))
    return ';'.join(unique_values)
```

**Example:**
```python
rec_001.features_raw = "hiking;fishing"
rec_002.features_raw = "hiking;parking"
rec_003.features_raw = "restrooms"

merged.features = "fishing;hiking;parking;restrooms"
```

**Used for:**
- features
- notes
- urls
- maps
- counties
- parent_sites, parent_trails (access points)
- partner_agencies
- coordination

---

### **Strategy 2: CONFLICT**

**Flag disagreements, preserve all values:**

```python
def merge_conflict(records, field):
    values = [r[field] for r in records if r[field]]
    
    if len(set(values)) <= 1:
        # All agree (or only one value)
        return values[0] if values else None
    else:
        # Conflict detected
        return {
            "values": list(set(values)),
            "sources": [r.raw_discovery_record_id for r in records],
            "conflict": True
        }
```

**Example:**
```python
rec_001.acres_raw = "85"
rec_002.acres_raw = "87"

merged.acres = {
    "values": ["85", "87"],
    "sources": ["rec_001", "rec_002"],
    "conflict": True
}
```

**Used for:**
- acres
- total_length_miles
- segment_length_miles
- member_count
- member_trail_count
- gps (access points)
- difficulty
- parent_site (if different)
- parent_trail_id (segments - error if different)

---

### **Strategy 3: CHOOSE**

**Select canonical value (prefer higher tier):**

```python
def merge_choose(records, field):
    # Sort by tier (lower number = higher authority)
    sorted_records = sorted(records, key=lambda r: r.source_tier)
    
    # Return first non-null value
    for record in sorted_records:
        if record[field]:
            return record[field]
    
    return None
```

**Example:**
```python
rec_001 (Tier 4): name_raw = "Carter Historic Farm"
rec_002 (Tier 8): name_raw = "carter farm"

merged.name = "Carter Historic Farm"  # From Tier 4
```

**Used for:**
- name
- description
- location
- address
- trail_history

---

### **Strategy 4: CHOOSE_OR_CONFLICT**

**Choose if values agree (after normalization), conflict if different:**

```python
def merge_choose_or_conflict(records, field):
    values = [normalize(r[field]) for r in records if r[field]]
    
    if len(set(values)) <= 1:
        # All agree - choose from highest tier
        return merge_choose(records, field)
    else:
        # Disagree - flag conflict
        return merge_conflict(records, field)
```

**Example:**
```python
# Scenario A: Agree
rec_001.category_raw = "park"
rec_002.category_raw = "Park"
merged.category = "park"  # Agree after normalization

# Scenario B: Disagree
rec_001.category_raw = "Park"
rec_002.category_raw = "Historic Site"
merged.category = {
    "values": ["Park", "Historic Site"],
    "sources": ["rec_001", "rec_002"],
    "conflict": True
}
```

**Used for:**
- category
- subtype
- designation
- status
- ownership
- governance
- trail_use_type
- trail_surface_type
- trail_origin_type
- access_point_type
- network_type
- segment_type

------------------------------------------------------------
# 14. PHASE 5: PARENT RESOLUTION

## 14.1 Purpose

Resolve parent entity names to IDs.

## 14.2 Trail Segment Parent Resolution

```python
def resolve_segment_parent(segment):
    """
    Resolve parent_trail_raw → parent_trail_id
    """
    parent_trail_name = segment.parent_trail_raw
    
    # Search for trail by name
    parent_trail = find_trail_by_name(
        name=parent_trail_name,
        counties=segment.counties_raw
    )
    
    if parent_trail:
        segment.parent_trail_id = parent_trail.trail_id
        segment.parent_resolved = True
    else:
        # Create placeholder trail
        placeholder = create_placeholder_trail(
            name=parent_trail_name,
            counties=segment.counties_raw,
            placeholder_reason="Referenced by segment but not yet discovered"
        )
        segment.parent_trail_id = placeholder.trail_id
        segment.parent_unresolved = True
        
        log_unresolved_parent(segment, parent_trail_name)
```

## 14.3 Access Point Parent Resolution

```python
def resolve_access_point_parents(access_point):
    """
    Resolve parent site/trail/segment names → IDs
    """
    
    # Parent sites
    if access_point.parent_sites_raw:
        site_names = access_point.parent_sites_raw.split(';')
        parent_site_ids = []
        
        for site_name in site_names:
            site = find_site_by_name(site_name, access_point.counties_raw)
            if site:
                parent_site_ids.append(site.site_id)
            else:
                log_unresolved_parent(access_point, site_name, "Site")
        
        access_point.parent_site_ids = parent_site_ids
    
    # Parent trails (similar logic)
    if access_point.parent_trails_raw:
        # ... resolve trail names to IDs
    
    # Parent trail segments (similar logic)
    if access_point.parent_trail_segments_raw:
        # ... resolve segment names to IDs
    
    # Determine identity parent (primary parent for grouping)
    access_point.identity_parent_entity_id = determine_identity_parent(access_point)
```

## 14.4 Trail Network Member Resolution

```python
def resolve_trail_network_members(network):
    """
    Resolve member_trail_names_raw → member_trail_ids
    """
    if not network.member_trail_names_raw:
        return
    
    trail_names = network.member_trail_names_raw.split(';')
    member_trail_ids = []
    unresolved = []
    
    for trail_name in trail_names:
        trail = find_trail_by_name(
            name=trail_name,
            counties=network.counties_raw
        )
        
        if trail:
            member_trail_ids.append(trail.trail_id)
        else:
            unresolved.append(trail_name)
            log_unresolved_member(network, trail_name)
    
    network.member_trail_ids = member_trail_ids
    network.member_trail_count = len(member_trail_ids)
    
    if unresolved:
        network.members_unresolved = unresolved
        network.members_partially_resolved = True
```

## 14.5 Site Network Member Resolution

```python
def resolve_site_network_members(network):
    """
    Resolve member_site_names_raw → member_site_ids
    """
    if not network.member_site_names_raw:
        return
    
    site_names = network.member_site_names_raw.split(';')
    member_site_ids = []
    unresolved = []
    
    for site_name in site_names:
        site = find_site_by_name(
            name=site_name,
            counties=network.counties_raw
        )
        
        if site:
            member_site_ids.append(site.site_id)
        else:
            unresolved.append(site_name)
            log_unresolved_member(network, site_name)
    
    network.member_site_ids = member_site_ids
    network.member_count = len(member_site_ids)
    
    if unresolved:
        network.members_unresolved = unresolved
        network.members_partially_resolved = True
```

## 14.6 Placeholder Entities

**When parent not found, create placeholder:**

```python
def create_placeholder_trail(name, counties):
    """
    Create minimal placeholder trail for unresolved parent
    """
    return {
        "trail_id": generate_id(),
        "name": name,
        "counties": counties,
        "placeholder": True,
        "placeholder_reason": "Referenced by child entity but not yet discovered",
        "placeholder_created_at": now()
    }
```

**Placeholders are later:**
- Updated when real trail is discovered
- Or flagged for manual creation
- Or confirmed as legitimate but undiscoverable trail

------------------------------------------------------------
# 15. RESOLUTION OUTPUT

## 15.1 Resolved Record Format

```json
{
  "resolved_record_id": "resolved_001",
  "entity_type": "Site",
  
  "name": "Carter Historic Farm",
  "category": "Park",
  "ownership": "Wood County",
  "governance": "Wood County Park District",
  "description": "85-acre historic farm with trails and preserved buildings",
  "location": "18331 Carter Road, Bowling Green, OH 43402",
  
  "acres": {
    "values": ["85", "87"],
    "sources": ["rec_001", "rec_002"],
    "conflict": true
  },
  
  "counties": ["Wood County"],
  "features": "fishing;hiking;parking;restrooms",
  "urls": [
    "https://wcparks.org/carter/",
    "https://traillink.com/parks/carter/",
    "https://historicalsociety.org/carter/"
  ],
  
  "resolution_provenance": {
    "merged_from": ["rec_001", "rec_002", "rec_003"],
    "merge_method": "auto",
    "merge_confidence": 0.95,
    "similarity_score": 95,
    "conflicts_detected": ["acres"],
    "resolved_at": "2026-02-19T23:00:00Z",
    "resolver_version": "5.0"
  }
}
```

## 15.2 Conflict Log Format

```json
{
  "conflict_id": "conflict_001",
  "resolved_record_id": "resolved_001",
  "field": "acres",
  "values": [
    {"value": "85", "source": "rec_001", "tier": 4, "url": "https://wcparks.org/carter/"},
    {"value": "87", "source": "rec_002", "tier": 8, "url": "https://historicalsociety.org/"}
  ],
  "detected_at": "2026-02-19T23:00:00Z",
  "resolution_status": "pending_normalization"
}
```

## 15.3 Review Queue Format

```json
{
  "review_id": "review_001",
  "record_pair": ["rec_004", "rec_005"],
  "entity_type": "Site",
  "similarity_score": 65,
  "confidence": "medium",
  "reason": "Name similar but different category",
  "comparison": {
    "name": ["Carter Historic Farm", "Carter Farm"],
    "category": ["Park", "Historic Site"],
    "ownership": ["Wood County", "Wood County"],
    "counties": [["Wood"], ["Wood"]]
  },
  "flagged_at": "2026-02-19T23:00:00Z",
  "review_status": "pending"
}
```

------------------------------------------------------------
# 16. QUALITY METRICS

## 16.1 Resolution Effectiveness

**Metrics to track:**

```python
resolution_metrics = {
    "input_records": 100,
    "output_records": 35,
    "reduction_ratio": 0.65,  # 65% reduction
    
    "auto_merged": 60,  # 60 records auto-merged
    "flagged_for_review": 5,  # 5 records need manual review
    "kept_separate": 35,  # 35 unique entities
    
    "conflicts_detected": 8,
    "parents_resolved": 25,
    "parents_unresolved": 3,
    
    "average_merge_confidence": 0.87,
    "high_confidence_merges": 28,
    "medium_confidence_flags": 5,
    
    "processing_time_seconds": 12.5
}
```

## 16.2 Quality Checks

**Before outputting resolved records:**

```python
def validate_resolved_record(record):
    errors = []
    warnings = []
    
    # Must have at least one source
    if len(record.resolution_provenance.merged_from) == 0:
        errors.append("No source records")
    
    # Required fields must be present
    if not record.name:
        errors.append("Missing name")
    if not record.counties:
        errors.append("Missing counties")
    
    # Conflicts should be flagged properly
    for field, value in record.items():
        if isinstance(value, dict) and value.get('conflict'):
            if len(value.get('values', [])) < 2:
                warnings.append(f"Conflict flag on {field} but only one value")
    
    # Parent relationships should be valid
    if record.entity_type == "Trail Segment":
        if not record.parent_trail_id:
            errors.append("Segment missing parent trail ID")
    
    return errors, warnings
```

------------------------------------------------------------
# 17. INTEGRATION POINTS

This module integrates with:

- **Discovery Output Specification v5.0** (input format)
- **All Discovery Sub-Procedures v5.0** (source of raw records)
- **Normalization Engine v5.0** (receives resolved records)
- **All Entity Schemas v5.0** (field definitions)
- **Audit & Logging Module v5.0** (provenance tracking)

------------------------------------------------------------
# 18. IMPLEMENTATION NOTES

## 18.1 Processing Order

**Resolve in dependency order:**

1. Sites (no dependencies)
2. Trails (no dependencies)
3. Site Networks (depends on Sites)
4. Trail Networks (depends on Trails)
5. Trail Segments (depends on Trails)
6. Access Points (depends on Sites, Trails, Segments)

## 18.2 Performance Optimization

**For large datasets:**

- Use identity anchor to filter comparisons
- Parallelize within groups
- Cache normalized values
- Batch parent lookups
- Index by name for fast lookups

## 18.3 Error Handling

**Graceful degradation:**

- If parent not found → create placeholder
- If conflict detection fails → flag for manual review
- If merge fails → keep records separate
- Log all errors for investigation

------------------------------------------------------------
# END OF RESOLUTION ENGINE v5.0
