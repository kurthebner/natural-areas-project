# DISCOVERY METHODOLOGY REDESIGN PROPOSAL
## From Narrative Docs to Structured Data Collection

**Date:** February 16, 2026  
**Project:** Natural Areas Project v4.0  
**Status:** PROPOSAL for Discussion  

---

## 🎯 PROBLEM STATEMENT

**Current Discovery Process (v4.0):**
```
Discovery Phase → Narrative Docs → [MANUAL EXTRACTION] → TSV → JSON → SQLite
                                    ↑
                                    Time-intensive bottleneck
                                    Error-prone
                                    Duplicates effort
```

**Issues:**
1. **Two-step process** - Discover, then structure (wastes time)
2. **Entity conflation** - Mixed Sites and Site Networks in same table
3. **Incomplete data** - 60+ parks discovered, only 25 structured
4. **Manual extraction** - 2-3 hours post-processing per tier
5. **No validation** - Schema violations not caught until later

---

## ✅ PROPOSED SOLUTION

**New Discovery Process (v5.0):**
```
Discovery Phase → JSON (immediate) → TSV (generated) → Narrative (generated)
                  ↓
                  Schema validation in real-time
                  Structured from the start
                  Ready for normalization
```

### **Key Changes:**

1. **Real-time structured capture** - Create entity records AS we discover
2. **Separate entity types** - Sites, Site Networks, Trails, Access Points in separate files
3. **JSON as primary format** - Native support for nested data, validation
4. **Generated outputs** - TSV and narratives auto-generated from JSON
5. **Progressive field collection** - Collect what's available now, enhance later

---

## 📊 FORMAT DECISION: JSON

**Why JSON over TSV/SQLite:**

| Requirement | TSV | JSON | SQLite |
|-------------|-----|------|--------|
| Human-readable | ✅ | ✅ | ❌ |
| Nested data (arrays, objects) | ❌ | ✅ | ✅ |
| Schema validation | ❌ | ✅ (JSON Schema) | ✅ |
| Excel-compatible | ✅ | ❌ (needs conversion) | ❌ |
| Git-friendly diffs | ✅ | ✅ | ❌ (binary) |
| Append operations | ✅ | ✅ | ✅ |
| API-ready | ❌ | ✅ | ❌ |
| Programmatic editing | Medium | ✅ Easy | ✅ Easy |

**Decision:** 
- **Primary: JSON** (during discovery)
- **Generated: TSV** (for Excel compatibility)
- **Generated: SQLite** (for final database)
- **Generated: Markdown** (narrative summaries)

---

## 📁 FILE STRUCTURE

**Per-County Discovery Directory:**

```
/discovery/wood-county/
  tier1/
    sites.json                    ← Primary discovery output
    sites.tsv                     ← Generated from JSON
    tier1_summary.md              ← Generated narrative
    
  tier3/
    sites.json                    ← 21 county parks
    sites.tsv
    tier3_summary.md
    
  tier6/
    sites.json                    ← Individual parks (60+)
    site_networks.json            ← Park systems (11)
    sites.tsv
    site_networks.tsv
    tier6_summary.md
    
  tier7/
    sites.json                    ← Conservancy preserves
    sites.tsv
    tier7_summary.md
    
  county_summary.md               ← Master narrative (generated)
  county_combined.xlsx            ← All entities (generated)
  county.db                       ← SQLite database (generated)
```

---

## 🗂️ JSON SCHEMA STRUCTURE

### **Sites JSON Format:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "tier": 3,
    "tier_name": "County Parks",
    "discovery_date": "2026-02-16",
    "discoverer": "Claude",
    "entity_type": "Site",
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
      "description": "80-acre working farm and living history museum depicting 1930s-1940s Depression era rural life.",
      "features": ["Historic Buildings", "Farm Animals", "Educational Programs", "Trails"],
      "designation": null,
      "status": "Open",
      "gps_primary": null,
      "plus_code": null,
      "url_primary": "https://wcparks.org/parks/carter-historic-farm/",
      "url_all": ["https://wcparks.org/parks/carter-historic-farm/"],
      "notes": "Donated by Sally & Lyle Loomis in 2001. Carter family farm since 1901. Includes Zimmerman Schoolhouse moved to site in 2016.",
      "parent_site_id": null,
      "source_primary": "https://wcparks.org/parks/carter-historic-farm/",
      "source_all": ["https://wcparks.org/parks/carter-historic-farm/"],
      "discovery_tier": 3
    }
  ]
}
```

### **Site Networks JSON Format:**

```json
{
  "metadata": {
    "county": "Wood County",
    "state": "Ohio",
    "tier": 6,
    "tier_name": "Municipal Parks",
    "discovery_date": "2026-02-16",
    "discoverer": "Claude",
    "entity_type": "Site Network",
    "count": 11
  },
  "networks": [
    {
      "network_id": null,
      "name": "Bowling Green Municipal Parks System",
      "network_type": "Municipal Park System",
      "ownership": "City of Bowling Green",
      "governance": "Bowling Green Parks & Recreation",
      "county_list": ["Wood"],
      "member_count": 9,
      "member_site_ids": null,
      "description": "Comprehensive municipal park system operated by City of Bowling Green Parks & Recreation Department.",
      "url_primary": "https://www.bgohio.org/parks",
      "notes": "System includes: Bellard Park, Carter Park, City Park, Conneaut Park, Dunbridge Soccer Fields, Jack Raney Park, Ridge Park, Simpson Garden Park, and others. City Park includes pool, skatepark, and community center."
    }
  ]
}
```

---

## 📋 FIELD COLLECTION STRATEGY

### **Phase 1: Discovery (MINIMUM VIABLE)**

**Required during initial discovery:**
- `name` ← REQUIRED (identity anchor)
- `county_list` ← REQUIRED (identity anchor)
- `category` ← HIGH PRIORITY (ontology)
- `ownership` ← HIGH PRIORITY (governance)
- `url_primary` ← HIGH PRIORITY (source)
- `source_primary` ← HIGH PRIORITY (provenance)
- `discovery_tier` ← AUTO-POPULATED

**Goal:** Get entity into system with identity + basic classification

### **Phase 2: Enhancement (PROGRESSIVE)**

**Collected when readily available:**
- `subtype`
- `governance`
- `address`
- `acres`
- `description`
- `features`
- `designation`
- `status`
- `notes`

**Goal:** Add depth without blocking discovery progress

### **Phase 3: Precision (POST-DISCOVERY)**

**Collected via dedicated research/geocoding:**
- `gps_primary` ← Batch geocoding
- `plus_code` ← Auto-generated from GPS
- `municipality` ← GIS lookup
- `township` ← GIS lookup
- `geometry` ← GIS tracing

**Goal:** Add precision data requiring specialized tools

---

## 🔄 REVISED DISCOVERY WORKFLOW

### **Example: Tier 6 Municipal Discovery**

**OLD WORKFLOW:**
```
1. Search "Bowling Green Ohio parks" [5 min]
2. Fetch official parks page [2 min]
3. Write narrative: "Bowling Green has 9 parks..." [10 min]
4. [LATER] Extract 9 park names from narrative [20 min]
5. [LATER] Create TSV rows [15 min]
---
TOTAL: 52 minutes per municipality
```

**NEW WORKFLOW:**
```python
# 1. Load JSON file (or create if first entity)
sites = load_json('tier6/sites.json') or new_sites_json()

# 2. Search and fetch page
fetch('https://www.bgohio.org/parks')

# 3. FOR EACH park found:
for park_name in ['Bellard Park', 'Carter Park', 'City Park', ...]:
    site = {
        'name': park_name,
        'category': 'Municipal Park',
        'ownership': 'City of Bowling Green',
        'county_list': ['Wood'],
        'url_primary': park_url,
        'source_primary': park_url,
        'discovery_tier': 6
    }
    
    # Add optional fields if available
    if park_address_found:
        site['address'] = park_address
    if park_acres_found:
        site['acres'] = park_acres
    if park_features_found:
        site['features'] = park_features
    
    # Append to JSON
    sites['sites'].append(site)
    save_json('tier6/sites.json', sites)

# 4. Auto-generate TSV
generate_tsv('tier6/sites.json', 'tier6/sites.tsv')

# 5. Auto-generate summary
generate_summary('tier6/sites.json', 'tier6/tier6_summary.md')
---
TOTAL: 25 minutes per municipality (including all 9 park entries)
52% time savings + complete structured data
```

---

## ✅ BENEFITS

### **Immediate Benefits:**

1. **50%+ time savings** - No post-processing extraction phase
2. **Zero entity conflation** - Sites and Networks in separate files
3. **Real-time validation** - JSON Schema catches errors immediately
4. **Progressive enhancement** - Add fields as discovered, not all-or-nothing
5. **Multiple output formats** - One source (JSON) → Many outputs (TSV, SQLite, MD, XLSX)

### **Long-term Benefits:**

1. **Reproducible** - Discovery process is code + data, not narrative
2. **Auditable** - Every entity has provenance trail
3. **Scalable** - Same workflow for 1 county or 88 counties
4. **Collaborative** - JSON diffs show exactly what changed
5. **API-ready** - JSON can be directly served via API

---

## 🛠️ IMPLEMENTATION PLAN

### **Phase 1: Tool Development (1-2 hours)**

**Create discovery helper functions:**

```python
# discovery_tools.py

def init_sites_json(county, tier):
    """Initialize a new sites.json file"""
    
def add_site(json_file, site_data):
    """Append a new site to sites.json"""
    
def validate_site(site_data):
    """Validate against Site Schema v4.0"""
    
def generate_tsv(json_file, tsv_file):
    """Convert JSON to TSV format"""
    
def generate_summary(json_file, md_file):
    """Generate narrative summary from JSON"""
    
def generate_combined_xlsx(county_dir):
    """Combine all tiers into single Excel file"""
```

### **Phase 2: Schema Definition (30 min)**

**Create JSON Schema files:**
- `site_schema.json` - Validates Site entities
- `site_network_schema.json` - Validates Site Network entities
- `trail_schema.json` - Validates Trail entities
- `access_point_schema.json` - Validates Access Point entities

### **Phase 3: Update Discovery Skills (1 hour)**

**Modify na-discovery-workflow skill:**
- Remove narrative generation steps
- Add JSON creation/append steps
- Add validation checkpoints
- Add auto-generation of TSV/MD outputs

### **Phase 4: Pilot Test (1 county tier)**

**Test new workflow on a fresh tier:**
- Apply to next county (not Wood County)
- Measure time savings
- Validate outputs
- Refine as needed

### **Phase 5: Rollout**

**Apply to all future discovery:**
- Update all discovery skills
- Document new workflow
- Create discovery templates

---

## 🤔 OPEN QUESTIONS

### **1. Field Collection Timing**

**Question:** Should we enforce field minimums during discovery?

**Options:**
- **A. Strict minimum** - REQUIRE name, county_list, category, ownership during discovery
- **B. Flexible minimum** - REQUIRE only name, county_list; suggest others
- **C. Progressive** - REQUIRE nothing beyond name; collect what's available

**Recommendation:** **Option A** - Strict minimum ensures usable data

---

### **2. Site vs. Site Network Decision**

**Question:** When do we create a Site Network vs. individual Sites?

**Criteria:**
- If official source lists individual parks → Create individual Sites
- If official source only mentions "park system" → Create Site Network, note member count
- If system has 10+ parks → Create Site Network entry + individual Sites (both)
- If system has <5 parks → Just create individual Sites (no network entry)

**Your preference?**

---

### **3. Validation Enforcement**

**Question:** Should validation errors BLOCK discovery or just WARN?

**Options:**
- **A. Block** - Invalid entities cannot be saved to JSON
- **B. Warn** - Save but mark as "needs_review: true"
- **C. Flexible** - Block for required fields, warn for optional

**Recommendation:** **Option C**

---

### **4. GPS Coordinate Collection**

**Question:** When should GPS be collected?

**Current approach:** Post-discovery batch geocoding (your preference)

**Alternatives:**
- Collect during discovery if readily available on page
- Always defer to post-discovery batch process
- Hybrid: Collect if present, batch geocode if missing

**Keep current approach?** Yes / No / Hybrid?

---

### **5. Multi-Entity Sites**

**Question:** How do we handle sites with child sites?

**Example:** "State Park" with 3 named campgrounds

**Options:**
- **A. Flat structure** - All as top-level Sites, note parent in notes
- **B. Hierarchical** - Parent Site with child Sites via parent_site_id
- **C. Hybrid** - Parent Site + child Sites when formally documented

**Recommendation:** **Option C** per Child Site Rules Module

---

## 📊 COMPARISON: OLD vs NEW

### **Wood County Tier 6 Example:**

| Metric | OLD Method | NEW Method |
|--------|------------|------------|
| **Time per municipality** | 52 min | 25 min |
| **Time for 26 municipalities** | 22.5 hours | 10.8 hours |
| **Entities structured** | 25 of 60+ | 60+ of 60+ |
| **Entity types separated** | ❌ No | ✅ Yes |
| **Post-processing needed** | ✅ 2-3 hours | ❌ None |
| **Schema validation** | ❌ Manual | ✅ Automatic |
| **Output formats** | 1 (TSV) | 4 (JSON, TSV, MD, XLSX) |
| **Total time** | ~25 hours | ~11 hours |
| **Time savings** | - | **56%** |

---

## 🎯 RECOMMENDATION

**ADOPT NEW METHODOLOGY** for all future discovery work.

**For Wood County specifically:**
- **Option 1:** Re-do Tier 6 using new method (~11 hours for complete data)
- **Option 2:** Keep current Tier 6 as-is, apply new method to next county
- **Option 3:** Hybrid - Extract Tier 6 individual parks using new tools, leave structure

**Your preference?**

---

## 📝 NEXT STEPS

**If approved:**

1. **Create discovery tools** (2 hours)
2. **Define JSON schemas** (30 min)
3. **Update na-discovery-workflow skill** (1 hour)
4. **Pilot test on next county tier** (varies)
5. **Document new workflow** (1 hour)

**Total setup:** ~4.5 hours
**Payback:** After 1 county (saves 14+ hours)

---

## 🗳️ DECISION REQUIRED

**Questions for you:**

1. **Approve new JSON-based discovery methodology?** Yes / No / Modify
2. **Field collection strategy?** Strict minimum / Flexible / Progressive
3. **Site Network criteria?** (see question 2 above)
4. **Validation approach?** Block / Warn / Flexible
5. **GPS timing?** Keep current / Hybrid / Change
6. **What to do with Wood County Tier 6?** Re-do / Keep / Hybrid

---

**Ready to discuss and refine this proposal!**
