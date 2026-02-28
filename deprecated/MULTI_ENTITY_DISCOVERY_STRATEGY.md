# MULTI-ENTITY DISCOVERY STRATEGY
## Comprehensive Approach for All Six Entity Types

**Date:** February 16, 2026  
**Project:** Natural Areas Project v4.0  
**Version:** 5.0 Discovery Methodology  
**Status:** COMPREHENSIVE PROPOSAL

---

## 🎯 THE SIX ENTITY TYPES

All identity-bearing entities with unique IDs:

1. **Site** - Parks, preserves, forests, wildlife areas, recreation areas
2. **Trail** - Named trails within or across sites  
3. **Trail Segment** - Distinct sections of trails
4. **Trail Network** - Collections of related trails
5. **Site Network** - Collections of related sites
6. **Access Point** - Parking areas, trailheads, entrances

---

## 📊 ENTITY RELATIONSHIPS

```
Site Networks ──contains──> Sites
                             │
Sites ──────────contains────>│──> Trails ──composed-of──> Trail Segments
│                            │                            │
└──has──> Access Points <────┤                            │
                              │                            │
Trail Networks ──contains────┴────────────────────────────┘
```

**Key Relationships:**
- Sites can belong to Site Networks
- Trails have a Primary Site (where they primarily exist)
- Trails can belong to Trail Networks
- Trail Segments belong to specific Trails
- Access Points serve Sites, Trails, or Trail Segments (many-to-many)

---

## 🗂️ FILE STRUCTURE PER COUNTY

```
/discovery/{county}/
  
  # Raw discovery outputs (JSON primary format)
  tier1/
    sites.json
    trails.json
    access_points.json
    site_networks.json
    trail_networks.json
    
  tier3/
    sites.json
    trails.json
    trail_segments.json
    access_points.json
    
  tier6/
    sites.json
    site_networks.json
    access_points.json
    
  # Generated outputs (auto-created from JSON)
  outputs/
    all_sites.tsv
    all_trails.tsv
    all_trail_segments.tsv
    all_access_points.tsv
    all_site_networks.tsv
    all_trail_networks.tsv
    
    combined.xlsx           # All entities, separate sheets
    combined.db             # SQLite with all tables
    
  # Generated summaries (auto-created from JSON)
  summaries/
    tier1_summary.md
    tier3_summary.md
    tier6_summary.md
    county_master_summary.md
```

---

## 📋 ENTITY-SPECIFIC DISCOVERY STRATEGIES

### **1. SITES** (Primary Discovery Focus)

**Discovery Phase:** ALL TIERS (1-8)

**Identity Anchor (Required):**
- `name` ✓
- `county_list` ✓

**High Priority Fields:**
- `category` (State Park, County Park, Municipal Park, etc.)
- `ownership` (actual legal owner name)
- `governance` (actual manager name)
- `url_primary`
- `source_primary`

**Medium Priority Fields:**
- `subtype`
- `address`
- `acres`
- `description`
- `features`
- `designation`
- `status`

**Low Priority / Post-Discovery:**
- `gps_primary` (batch geocoding)
- `plus_code` (auto-generated)
- `municipality` (GIS lookup)
- `township` (GIS lookup)

**Discovery Workflow:**
```
1. Identify site from official source
2. Create JSON entry with name + county_list
3. Add category, ownership, governance immediately
4. Add other fields if readily available on page
5. Continue to next site
6. [POST-DISCOVERY] Batch geocode all sites
```

---

### **2. SITE NETWORKS** (Organizational Discovery)

**Discovery Phase:** ALL TIERS (systems exist at multiple levels)

**Examples:**
- "Ohio State Park System"
- "Wood County Park District"
- "Bowling Green Municipal Parks System"
- "Black Swamp Conservancy Preserves"

**Identity Anchor (Required):**
- `name` ✓
- `network_type` ✓

**High Priority Fields:**
- `ownership`
- `governance`
- `member_count`
- `url_primary`

**Medium Priority Fields:**
- `description`
- `member_site_ids` (list of site IDs)

**Discovery Criteria:**

**CREATE Site Network when:**
- Official source explicitly names the system/collection
- System has 5+ member sites
- System has unified governance/branding
- Network has its own identity (not just administrative grouping)

**DO NOT create Site Network when:**
- Just an administrative category (e.g., "all state parks in county")
- No unified governance or identity
- Fewer than 5 sites unless exceptionally significant

**Discovery Workflow:**
```
1. Identify system/network from official source
2. Note member count and governance
3. Create site_networks.json entry
4. Link member sites via member_site_ids (after sites discovered)
5. Continue
```

---

### **3. TRAILS** (Linear Feature Discovery)

**Discovery Phase:** ALONGSIDE Sites (continuous discovery)

**Examples:**
- "Slippery Elm Trail" (13.1 miles, Bowling Green to North Baltimore)
- "Maumee River Trail" (107 miles, multi-county)
- "Buckeye Trail" (1,444 miles, statewide)

**Identity Anchor (Required):**
- `trail_name` ✓
- `counties_traversed` ✓

**High Priority Fields:**
- `trail_use_type` (Multi-Use, Hiking, Biking, Water, etc.)
- `trail_surface_type` (Paved, Natural, Gravel, etc.)
- `total_length_miles`
- `primary_managing_agency`
- `primary_site_id` (if trail primarily in one site)

**Medium Priority Fields:**
- `trail_origin_type` (Rail Trail, Canal Towpath, Purpose-Built)
- `status`
- `description`
- `url`
- `map_url`

**Discovery Triggers:**

**Discover trails when:**
- Official source names specific trail
- Trail has its own page/identity
- Trail is named on maps
- Trail crosses multiple sites

**DO NOT create trail entity for:**
- Unnamed paths
- Internal park paths without names
- Informal/social trails
- Features (e.g., "boardwalk" is a feature, not a trail)

**Discovery Workflow:**
```
1. While discovering site, note if named trails mentioned
2. If trail is primary feature → Create trail.json entry immediately
3. If trail is incidental → Add to trail_discovery_notes.txt for batch processing
4. Record: name, length, surface, primary site
5. [POST-SITE-DISCOVERY] Process trail_discovery_notes.txt
6. Create trail entries in batch
```

**Wood County Example:**
```json
{
  "trail_name": "Slippery Elm Trail",
  "alternate_names": [],
  "trail_use_type": "Multi-Use",
  "trail_surface_type": "Paved",
  "trail_origin_type": "Rail Trail",
  "total_length_miles": 13.1,
  "counties_traversed": ["Wood"],
  "primary_managing_agency": "Wood County Park District; City of Bowling Green",
  "status": "Open",
  "description": "13.1-mile paved rail trail from Bowling Green to North Baltimore following former railroad corridor.",
  "url": "https://wcparks.org/trails/slippery-elm-trail/",
  "notes": "Connects multiple city and county parks. Co-managed by WCPD and Bowling Green."
}
```

---

### **4. TRAIL SEGMENTS** (Sub-Trail Discovery)

**Discovery Phase:** ONLY if explicitly documented

**Examples:**
- "Buckeye Trail - Wood County Section"
- "North Country Trail - Wayne National Forest Segment"

**Identity Anchor (Required):**
- `segment_name` ✓
- `parent_trail_id` ✓

**High Priority Fields:**
- `segment_length_miles`
- `surface_type`
- `difficulty`
- `primary_site_id` (if segment within specific site)

**Discovery Criteria:**

**CREATE Trail Segment when:**
- Trail officially divided into named segments
- Segment has distinct characteristics (surface, difficulty, management)
- Segment is documented with specific name/designation
- Long trails with county-specific sections

**DO NOT create segments for:**
- Informal divisions
- Undocumented sections
- Simple distance markers
- Short trails (<5 miles total)

**Discovery Workflow:**
```
1. If trail has officially named segments → Document immediately
2. Otherwise → Skip segment creation unless user requests
3. Most trails will NOT have segments
```

---

### **5. TRAIL NETWORKS** (Trail Collection Discovery)

**Discovery Phase:** RARELY (most trails are standalone)

**Examples:**
- "Buckeye Trail System" (multiple interconnected trails)
- "Great Lakes Water Trail Network"

**Identity Anchor (Required):**
- `network_name` ✓
- `network_type` ✓

**Discovery Criteria:**

**CREATE Trail Network when:**
- Official designation as network/system
- Multiple named trails formally connected
- Network has unified branding/governance
- Network has its own website/identity

**DO NOT create for:**
- Individual trails (even long ones)
- Informal connections between trails
- Administrative groupings

**Discovery Workflow:**
```
1. Rarely encountered - most trails are standalone
2. If found → Create trail_networks.json entry
3. Link member trails via member_trail_ids
```

---

### **6. ACCESS POINTS** (Entry Point Discovery)

**Discovery Phase:** POST-SITE-DISCOVERY or CONCURRENT

**Examples:**
- "Carter Historic Farm Main Entrance"
- "Slippery Elm Trail - Bowling Green Trailhead"
- "City Park Parking Lot A"

**Identity Anchor (Required):**
- `name` ✓
- `identity_parent_entity_type` ✓ (Site, Trail, or Trail Segment)
- `identity_parent_entity_id` ✓

**High Priority Fields:**
- `access_point_type` (Trailhead, Parking, Entrance, Boat Launch, etc.)
- `gps_primary` (REQUIRED for access points)
- `address`

**Medium Priority Fields:**
- `access_level` (Primary, Secondary, Emergency, etc.)
- `role` (Main Entrance, Alternative Access, etc.)
- `status` (Open, Closed, Seasonal)
- `access_notes`

**Discovery Strategy:**

**OPTION A: Concurrent Discovery (Intensive)**
- Discover access points WHILE discovering sites
- Add to access_points.json immediately
- Pro: Complete data
- Con: Significantly slower site discovery

**OPTION B: Separate Phase (Recommended)**
- Focus on sites first
- After site discovery complete → Dedicated access point pass
- Pro: Faster site discovery
- Con: Requires second pass

**OPTION C: Opportunistic (Pragmatic)**
- If access point prominently mentioned → Capture immediately
- Otherwise → Note for later research
- Pro: Balance of speed and completeness
- Con: May miss some access points

**Recommendation:** **OPTION C - Opportunistic**

**Discovery Workflow:**
```
1. While on site page, if prominent parking/trailhead mentioned → Capture
2. Otherwise → Continue with site discovery
3. [POST-DISCOVERY] Optional dedicated access point research phase
```

---

## 🔄 UNIFIED DISCOVERY WORKFLOW

### **Phase 1: Site-Focused Discovery (PRIMARY)**

**For each tier:**

```
1. Load or create sites.json
2. Load or create site_networks.json  
3. Create trail_discovery_notes.txt

4. FOR EACH site discovered:
   a. Add site to sites.json immediately
      - name, county_list, category, ownership (required)
      - Add other fields if readily available
   
   b. IF site mentions system/network:
      - Add note to create/update site_networks.json entry
   
   c. IF site mentions named trail:
      - Append to trail_discovery_notes.txt
   
   d. IF prominent access point visible:
      - Add note to access_point_notes.txt
   
   e. Continue to next site

5. After all sites in tier discovered:
   - Review site_networks.json, fill in member_site_ids
   - Save tier completion
```

---

### **Phase 2: Trail Discovery (SECONDARY)**

**After site discovery complete:**

```
1. Load or create trails.json
2. Review trail_discovery_notes.txt
3. FOR EACH trail noted:
   a. Research trail details
   b. Add to trails.json
   c. If trail has named segments → Add to trail_segments.json
   d. If trail part of network → Update trail_networks.json

4. Validate all trail.primary_site_id references
```

---

### **Phase 3: Access Point Discovery (OPTIONAL/POST)**

**If access points needed:**

```
1. Load or create access_points.json
2. Review access_point_notes.txt
3. FOR EACH site without documented access:
   a. Research parking/trailheads
   b. Add to access_points.json with GPS
   
4. Validate all identity_parent references
```

---

### **Phase 4: Output Generation (AUTOMATIC)**

**After discovery phases complete:**

```
1. Run generation scripts:
   - generate_tsvs.py → Creates all_*.tsv files
   - generate_xlsx.py → Creates combined.xlsx
   - generate_sqlite.py → Creates combined.db
   - generate_summaries.py → Creates markdown summaries

2. Outputs:
   - TSV files for each entity type
   - Excel workbook with separate sheets
   - SQLite database with all tables
   - Narrative summaries by tier and county-wide
```

---

## 📊 DISCOVERY PRIORITY MATRIX

### **By Entity Type:**

| Entity Type | Priority | Discovery Phase | Completeness Target |
|-------------|----------|-----------------|---------------------|
| **Sites** | 🔴 HIGHEST | Tier 1-8 | 95%+ |
| **Site Networks** | 🟡 HIGH | Tier 1-8 | 90%+ |
| **Trails** | 🟡 MEDIUM | Post-Site | 80%+ |
| **Access Points** | 🟢 LOW | Post-Trail | 50%+ |
| **Trail Segments** | 🟢 LOW | If documented | 25%+ |
| **Trail Networks** | 🟢 LOW | If documented | 25%+ |

### **By Tier:**

| Tier | Sites | Networks | Trails | Access Points |
|------|-------|----------|--------|---------------|
| 1 (State) | ✓ High | ✓ High | ✓ Medium | ○ Low |
| 2 (Federal) | ✓ High | ✓ High | ✓ Medium | ○ Low |
| 3 (County) | ✓ High | ✓ High | ✓ High | ○ Medium |
| 4 (District) | ✓ High | ✓ High | ✓ Medium | ○ Low |
| 5 (Township) | ✓ High | ○ Low | ○ Low | ○ Low |
| 6 (Municipal) | ✓ High | ✓ Medium | ✓ Medium | ○ Low |
| 7 (Conservancy) | ✓ High | ✓ Medium | ○ Low | ○ Low |
| 8 (Private) | ✓ High | ○ Low | ○ Low | ○ Low |

---

## 🎯 ENTITY-SPECIFIC JSON SCHEMAS

### **sites.json Structure:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "tier": 3,
    "entity_type": "Site",
    "discovery_date": "2026-02-16",
    "count": 21
  },
  "sites": [
    {
      "name": "Carter Historic Farm",
      "category": "County Park",
      "subtype": "Historic Farm",
      "ownership": "Wood County Park District",
      "governance": "Wood County Park District",
      "address": "18331 Carter Road, Bowling Green, OH 43402",
      "acres": 80,
      "county_list": ["Wood"],
      "municipality": null,
      "township": null,
      "description": "80-acre working farm and living history museum...",
      "features": ["Historic Buildings", "Farm Animals", "Trails"],
      "designation": null,
      "status": "Open",
      "gps_primary": null,
      "plus_code": null,
      "url_primary": "https://wcparks.org/parks/carter-historic-farm/",
      "notes": "Donated 2001, Carter family farm since 1901",
      "parent_site_id": null,
      "source_primary": "https://wcparks.org/parks/carter-historic-farm/",
      "discovery_tier": 3
    }
  ]
}
```

### **trails.json Structure:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "entity_type": "Trail",
    "discovery_date": "2026-02-16",
    "count": 1
  },
  "trails": [
    {
      "trail_name": "Slippery Elm Trail",
      "alternate_names": [],
      "trail_use_type": "Multi-Use",
      "trail_surface_type": "Paved",
      "trail_origin_type": "Rail Trail",
      "total_length_miles": 13.1,
      "counties_traversed": ["Wood"],
      "primary_managing_agency": "Wood County Park District; City of Bowling Green",
      "secondary_managing_agencies": null,
      "status": "Open",
      "description": "13.1-mile paved rail trail...",
      "trail_history": "Former railroad corridor",
      "url": "https://wcparks.org/trails/slippery-elm-trail/",
      "map_url": null,
      "notes": "Connects multiple city and county parks",
      "network_affiliation": null,
      "primary_site_id": null
    }
  ]
}
```

### **site_networks.json Structure:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "tier": 6,
    "entity_type": "Site Network",
    "discovery_date": "2026-02-16",
    "count": 11
  },
  "networks": [
    {
      "name": "Bowling Green Municipal Parks System",
      "network_type": "Municipal Park System",
      "ownership": "City of Bowling Green",
      "governance": "Bowling Green Parks & Recreation",
      "county_list": ["Wood"],
      "member_count": 9,
      "member_site_ids": null,
      "description": "Comprehensive municipal park system...",
      "url_primary": "https://www.bgohio.org/parks",
      "notes": "Includes: Bellard Park, Carter Park, City Park..."
    }
  ]
}
```

### **access_points.json Structure:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "entity_type": "Access Point",
    "discovery_date": "2026-02-16",
    "count": 5
  },
  "access_points": [
    {
      "name": "Carter Historic Farm Main Entrance",
      "access_point_type": "Entrance",
      "access_level": "Primary",
      "role": "Main Entrance",
      "status": "Open",
      "identity_parent_entity_type": "Site",
      "identity_parent_entity_id": "carter-historic-farm",
      "additional_parent_ids": null,
      "county": "Wood",
      "township": null,
      "municipality": "Bowling Green",
      "address": "18331 Carter Road, Bowling Green, OH 43402",
      "gps_primary": "41.3734,-83.6501",
      "plus_code": "9F7F+59 Bowling Green, Ohio",
      "access_notes": "Parking lot with 50 spaces",
      "url": null,
      "map_url": null
    }
  ]
}
```

---

## 🔧 DISCOVERY TOOLS & FUNCTIONS

**Required Python utilities:**

```python
# entity_discovery.py

def init_entity_json(county, tier, entity_type):
    """Initialize JSON file for entity type"""
    
def add_site(json_file, site_data):
    """Append site to sites.json"""
    
def add_trail(json_file, trail_data):
    """Append trail to trails.json"""
    
def add_site_network(json_file, network_data):
    """Append network to site_networks.json"""
    
def add_access_point(json_file, ap_data):
    """Append access point to access_points.json"""
    
def validate_entity(entity_data, entity_type):
    """Validate against JSON Schema"""
    
def link_entities(sites_json, networks_json):
    """Link sites to networks via IDs"""
    
def generate_all_outputs(county_dir):
    """Generate TSV, XLSX, SQLite, MD from JSON"""
```

---

## 📝 DECISION MATRIX: WHEN TO CREATE EACH ENTITY

### **Site:**
- ✅ Named, bounded land unit
- ✅ Identity-bearing
- ✅ Documented in sources
- ❌ NOT a trail, access point, or network

### **Site Network:**
- ✅ Explicit system/collection name
- ✅ 5+ member sites (or significant smaller collection)
- ✅ Unified governance/branding
- ✅ Has own identity
- ❌ NOT just administrative grouping

### **Trail:**
- ✅ Named linear corridor
- ✅ Documented in sources
- ✅ Identity-bearing
- ❌ NOT unnamed path
- ❌ NOT internal park path without name

### **Trail Segment:**
- ✅ Officially named segment of trail
- ✅ Distinct characteristics
- ✅ Documented
- ❌ NOT informal division

### **Trail Network:**
- ✅ Official network designation
- ✅ Multiple connected trails
- ✅ Unified branding
- ✅ Own website/identity
- ❌ NOT single trail

### **Access Point:**
- ✅ Visitor-facing entry location
- ✅ Named or describable
- ✅ Has GPS coordinates
- ✅ Serves a parent entity
- ❌ NOT the site/trail itself

---

## 🎯 IMPLEMENTATION RECOMMENDATIONS

### **For Wood County (Current):**

**Option A: Continue Sites-Only**
- Complete all Site discovery first
- Defer Trails, Access Points to later
- Pro: Maintains momentum
- Con: Incomplete multi-entity model

**Option B: Hybrid Approach** ⭐ **RECOMMENDED**
- Complete Sites (already mostly done)
- Add major trails opportunistically (Slippery Elm, Maumee River Trail)
- Defer Access Points
- Pro: Balanced, captures obvious trails
- Con: Not comprehensive

**Option C: Full Multi-Entity**
- Go back and systematically add trails + access points
- Pro: Complete reference implementation
- Con: Significant time investment (8-10 hours)

### **For Future Counties:**

**Use full multi-entity approach from start:**
- Sites + Site Networks (primary focus)
- Trails (opportunistic during site discovery)
- Trail Segments (only if documented)
- Access Points (optional post-discovery phase)
- Trail Networks (rarely encountered)

---

## ❓ OPEN QUESTIONS

**1. Discovery Depth:**
- Should we aim for 100% trail coverage or just major trails?
- Should access points be mandatory or optional?

**2. Wood County Trails:**
- Re-discover to add trails systematically?
- Or just capture major trails (Slippery Elm, Maumee River) and move on?

**3. Tool Development Priority:**
- Build multi-entity tools before next county?
- Or continue sites-only and add tools incrementally?

**4. Validation Strictness:**
- Require all high-priority fields before saving?
- Or allow minimal saves and progressive enhancement?

**5. Entity Linking:**
- Link entities during discovery (add IDs immediately)?
- Or link in post-processing (faster discovery, separate linking phase)?

---

## 📊 SUMMARY COMPARISON

### **Sites Only (Current):**
- Entities: 1 type
- Complexity: Low
- Time per county: 15-20 hours
- Completeness: 95% sites, 0% trails/access points

### **Sites + Networks (Minimal Multi-Entity):**
- Entities: 2 types
- Complexity: Low-Medium
- Time per county: 18-22 hours
- Completeness: 95% sites, 90% networks, 0% trails/access points

### **Sites + Networks + Trails (Recommended):** ⭐
- Entities: 3-4 types (Sites, Networks, Trails, maybe Segments)
- Complexity: Medium
- Time per county: 22-28 hours
- Completeness: 95% sites, 90% networks, 80% trails, 0% access points

### **Full Multi-Entity:**
- Entities: All 6 types
- Complexity: High
- Time per county: 30-40 hours
- Completeness: 95% sites, 90% networks, 90% trails, 60% access points, 50% segments/networks

---

## 🎯 RECOMMENDATION

**Adopt Sites + Networks + Trails approach:**

1. **Sites** - Full discovery (already doing)
2. **Site Networks** - Opportunistic (when systems identified)
3. **Trails** - Opportunistic (major/named trails during site discovery)
4. **Access Points** - Optional post-discovery phase
5. **Trail Segments** - Only if explicitly documented
6. **Trail Networks** - Only if explicitly documented

**This balances completeness with efficiency.**

---

**Ready for your feedback on:**
1. Discovery depth preferences
2. Entity priority decisions
3. Tool development timeline
4. What to do with Wood County specifically

