# SITE NETWORK SCHEMA ANALYSIS v4.0 → v5.0

**Date:** February 16, 2026  
**Current:** Site Network Schema v4.0 (15 fields)  
**Focus:** Identifying issues and proposing v5.0 improvements

---

## 📊 CURRENT V4.0 SITE NETWORK SCHEMA

### **15 Fields (Authoritative Order):**

1. **Network Name**
2. **Alternate Names**
3. **Network Type**
4. **Status**
5. **Counties Traversed**
6. **States Included**
7. **Primary Managing Agency**
8. **Secondary Managing Agencies**
9. **Network Affiliation**
10. **Description**
11. **History**
12. **URL**
13. **Map URL**
14. **Notes**
15. **Derived Label** (computed)

---

## 🎯 PURPOSE OF SITE NETWORKS

**From Schema:**
> "A Site Network is a named, identity-bearing umbrella entity composed of multiple Sites, documented in authoritative sources."

**Examples:**
- National Heritage Areas
- Local Historic Districts
- Scenic River Corridors
- Watershed-scale conservation networks
- Multi-site conservation or cultural systems

**Real-World Ohio Examples:**
- "Ohio State Park System" (all state parks)
- "Wood County Park District" (21 county parks)
- "Bowling Green Municipal Parks System" (9+ city parks)
- "Black Swamp Conservancy Preserves" (multiple preserves)
- "Cuyahoga Valley National Heritage Area" (multi-site cultural landscape)

---

## 🔍 ISSUES IDENTIFIED

### **Issue 1: Alternate Names**

**Field 2: Alternate Names**

**From earlier Trail decision:** We kept alternate_names for Trails because they commonly have abbreviations and variant names.

**For Site Networks:**

**When do networks have alternate names?**
- "Ohio State Park System" = "Ohio State Parks"
- "Wood County Park District" = "WCPD" (but that's an abbreviation)
- "Cuyahoga Valley National Heritage Area" = "CVNHA"

**Analysis:**
- Rarely needed
- When present, usually just abbreviations
- Can note in description: "commonly known as..."

**From Trail Segment decision:** We removed alternate_names from segments as rarely used.

**RECOMMENDATION:**
❌ **Remove alternate_names from Site Networks**
- Rarely documented
- Can note variants in description
- Simplifies schema

---

### **Issue 2: History Field**

**Field 11: History**

**From Trail decision:** We KEPT trail_history as separate field because rail trails have important historical context.

**For Site Networks:**

**When do networks have distinct history?**
- Establishment dates
- Designation history
- Evolution of network
- Example: "National Heritage Area designated by Congress in 2000"

**But:**
- Usually 1-2 sentences
- Could merge into description
- Not as critical as trail history (rail trail conversions are defining feature)

**RECOMMENDATION:**
❌ **Remove history, merge into description**
- Less critical than for trails
- Usually brief anyway
- Keeps description focused but can include origin

**Example:**
```
Description: "System of 21 county parks established in 1958, managed by Wood County Park District, spanning 1,200 acres across Wood County."
```

---

### **Issue 3: Map URL**

**Field 13: Map URL**

**From Trail decision:** We KEPT map_url for trails because trail maps are critical.

**From Access Point decision:** We KEPT map_url for access points (simple field).

**For Site Networks:**

**When do networks have maps?**
- System-wide maps showing all member sites
- Example: "Wood County Parks Map" showing all 21 parks
- Ohio State Parks map showing all state parks
- Heritage Area boundary maps

**Analysis:**
- More common than for individual sites
- Networks often have overview maps
- Useful for showing spatial extent

**RECOMMENDATION:**
✅ **KEEP map_url (simple field, not rich array)**
- Networks commonly have overview maps
- Important for understanding spatial extent
- Not as critical as trails (simple field sufficient)

---

### **Issue 4: Network Affiliation**

**Field 9: Network Affiliation**

**From schema:**
> "Represents formal affiliations with larger regional, federal, or thematic systems."

**Problem:** Can Site Networks have parent networks?

**Examples:**
- Network: "Cuyahoga Valley National Heritage Area"
- Affiliation: "National Heritage Areas Program"

But wait - is "National Heritage Areas Program" a Site Network?
- If YES → Should use relationship table
- If NO → What is it? A program, not a network?

**From earlier decisions:**
- We removed network_affiliation from Sites (use Site Network entity)
- We removed network_affiliation from Trails (use Trail Network entity)

**Question:** Can networks have network affiliations?

**Analysis:**
- Creates potential for nested networks
- Unclear semantics
- Better to just document in description/notes

**RECOMMENDATION:**
❌ **Remove network_affiliation**
- Potential for confusion
- If network is part of larger system, note in description
- Cleaner architecture without nested affiliations

---

### **Issue 5: Primary vs Secondary Managing Agencies**

**Fields 7-8:**
- Primary Managing Agency
- Secondary Managing Agencies

**From Trail decision:** We kept both for trails (primary coordinator + multiple land managers).

**For Site Networks:**

**Governance patterns for networks:**

**Simple network (single manager):**
```
Network: "Wood County Park District"
Primary: "Wood County Park District"
Secondary: (none)
```

**Complex network (coordinating body + members):**
```
Network: "Ohio to Erie Trail" (this is actually a trail network, but similar pattern)
Primary: "Ohio to Erie Trail Fund" (coordination)
Secondary: "Cleveland Metroparks; Columbus Metro Parks; [20+ agencies]"
```

**Real Site Network example:**
```
Network: "Cuyahoga Valley National Heritage Area"
Primary: "Conservancy for Cuyahoga Valley National Park"
Secondary: "National Park Service; Ohio DNR; City of Cleveland; [many partners]"
```

**Analysis:**
- Networks almost ALWAYS have this pattern
- Coordinating organization + member/partner agencies
- Both fields needed

**RECOMMENDATION:**
✅ **KEEP both primary and secondary managing agencies**

**But rename for consistency:**
- "Primary Managing Agency" → **"governance"**
- "Secondary Managing Agencies" → **"partner_agencies"**

---

### **Issue 6: Missing Member Tracking!**

**CRITICAL MISSING FIELDS:**

**Current schema has NO way to track:**
- How many sites are in the network
- Which sites are members
- Network composition

**This is a major gap!**

**Example:**
```
Network: "Wood County Park District"
(No field showing it has 21 member sites!)
(No field listing the site IDs!)
```

**RECOMMENDATION:**
✅ **ADD member tracking fields:**
- `member_count` (integer - how many sites)
- `member_site_ids` (array - list of site IDs for linking)

**These are CRITICAL for:**
- Understanding network scale
- Building relationships
- Validating membership
- Querying "show all sites in this network"

---

### **Issue 7: Ownership Field - Missing!**

**Current schema has governance but NOT ownership!**

**For Sites, we have both:**
- ownership (legal owner)
- governance (manager)

**For Site Networks, we only have:**
- Primary Managing Agency (manager)

**But who OWNS the network?**

**Examples:**
- "Wood County Park District" → Owned by Wood County
- "Black Swamp Conservancy" → Owned by nonprofit organization
- "Ohio State Park System" → Owned by State of Ohio

**This matters for:**
- Legal structure
- Funding sources
- Governance authority

**RECOMMENDATION:**
✅ **ADD ownership field**
- Parallel to Sites schema
- Important for understanding network structure

---

### **Issue 8: Counties Traversed**

**Field 5: Counties Traversed**

**From earlier decisions:**
- Rename "counties_traversed" → **"counties"** (simpler)
- Array in JSON, semicolon in TSV

**RECOMMENDATION:**
✅ **Rename to "counties" (array)**

---

## 📋 PROPOSED SITE NETWORK SCHEMA V5.0

### **Changes from v4.0:**

**Removed:**
1. ❌ **alternate_names** (rarely used, note variants in description)
2. ❌ **history** (merge into description)
3. ❌ **network_affiliation** (cleaner without nested networks)

**Renamed:**
4. 🔄 "Counties Traversed" → **counties** (array)
5. 🔄 "Primary Managing Agency" → **governance**
6. 🔄 "Secondary Managing Agencies" → **partner_agencies**

**Added:**
7. ✨ **ownership** (NEW - who owns the network)
8. ✨ **member_count** (NEW - number of member sites)
9. ✨ **member_site_ids** (NEW - array of site IDs)

---

### **Complete v5.0 Field List (13 fields):**

**Core Identity:**
1. network_name
2. network_type (National Heritage Area, Conservation Network, etc.)
3. status

**Ownership & Governance:**
4. **ownership** (NEW - legal owner)
5. governance (rename from primary_managing_agency)
6. partner_agencies (rename from secondary_managing_agencies)

**Geographic Scope:**
7. counties (array - rename from counties_traversed)
8. states_included (array - for multi-state networks)

**Member Tracking:**
9. **member_count** (NEW - integer)
10. **member_site_ids** (NEW - array for relationships)

**Descriptive:**
11. description (can include history/origin)
12. notes

**URLs:**
13. url
14. map_url

**Auto-generated:**
15. network_id
16. derived_label (computed)
17. created_at, updated_at

**Result: 15 fields → 13 fields (-2, but added 3 critical ones)**

---

## 🎯 REAL-WORLD EXAMPLES

### **Example 1: County Park System**

```json
{
  "network_name": "Wood County Park District",
  "network_type": "Multi-Site Recreation Network",
  "status": "Active",
  "ownership": "Wood County",
  "governance": "Wood County Park District",
  "partner_agencies": null,
  "counties": ["Wood"],
  "states_included": null,
  "member_count": 21,
  "member_site_ids": [
    "adam-phillips-pond",
    "arrowwood-archery",
    "carter-historic-farm",
    "...17 more..."
  ],
  "description": "System of 21 county parks established in 1958, managed by Wood County Park District. Includes natural areas, historic sites, and recreational facilities spanning over 1,200 acres.",
  "notes": null,
  "url": "https://wcparks.org/",
  "map_url": "https://wcparks.org/maps/system-map.pdf"
}
```

### **Example 2: Municipal Park System**

```json
{
  "network_name": "Bowling Green Municipal Parks System",
  "network_type": "Multi-Site Recreation Network",
  "status": "Active",
  "ownership": "City of Bowling Green",
  "governance": "Bowling Green Parks & Recreation Department",
  "partner_agencies": null,
  "counties": ["Wood"],
  "states_included": null,
  "member_count": 9,
  "member_site_ids": [
    "bellard-park",
    "carter-park",
    "city-park",
    "conneaut-park",
    "dunbridge-soccer-fields",
    "jack-raney-park",
    "ridge-park",
    "simpson-garden-park",
    "wintergarden-park"
  ],
  "description": "Comprehensive municipal park system operated by City of Bowling Green Parks & Recreation Department. Nine parks offering diverse recreational opportunities including sports fields, playgrounds, pools, and natural areas.",
  "notes": "City Park includes community center, pool, and skate park.",
  "url": "https://www.bgohio.org/parks",
  "map_url": null
}
```

### **Example 3: Conservation Preserves**

```json
{
  "network_name": "Black Swamp Conservancy Preserves",
  "network_type": "Multi-Site Conservation Network",
  "status": "Active",
  "ownership": "Black Swamp Conservancy",
  "governance": "Black Swamp Conservancy",
  "partner_agencies": null,
  "counties": ["Wood", "Lucas", "Hancock", "Fulton"],
  "states_included": null,
  "member_count": 12,
  "member_site_ids": [
    "bell-woods",
    "pat-clint-mauks-prairie",
    "...10 more preserves..."
  ],
  "description": "Network of nature preserves protecting remnant Black Swamp habitat and other ecologically significant lands. Black Swamp Conservancy founded 1993, has protected over 2,500 acres across northwest Ohio.",
  "notes": "Also holds conservation easements on other properties not owned outright.",
  "url": "https://blackswamp.org/",
  "map_url": "https://blackswamp.org/preserve-map/"
}
```

### **Example 4: State Park System**

```json
{
  "network_name": "Ohio State Park System",
  "network_type": "Multi-Site Recreation Network",
  "status": "Active",
  "ownership": "State of Ohio",
  "governance": "Ohio Department of Natural Resources - Division of Parks and Watercraft",
  "partner_agencies": null,
  "counties": ["Wood", "...87 more counties..."],
  "states_included": null,
  "member_count": 75,
  "member_site_ids": [
    "mary-jane-thurston-state-park",
    "...74 more state parks..."
  ],
  "description": "Ohio's state park system established in 1949, comprising 75 state parks across Ohio totaling over 174,000 acres. Managed by ODNR Division of Parks and Watercraft.",
  "notes": "System includes state parks, state nature preserves, and state forests under unified management.",
  "url": "https://ohiodnr.gov/wps/portal/gov/odnr/go-and-do/plan-a-visit/find-a-property",
  "map_url": "https://ohiodnr.gov/static/documents/parks/stateparks_allmap.pdf"
}
```

---

## ❓ DECISIONS NEEDED

### **1. Alternate Names**
❌ **Remove?**
- Rarely documented for networks
- Can note variants in description
- Simplifies schema

**My vote:** Remove

---

### **2. History Field**
❌ **Remove and merge into description?**
- Less critical than for trails (where origin IS the identity)
- Networks can include establishment date in description
- Simplifies schema

**My vote:** Remove, merge into description

---

### **3. Network Affiliation**
❌ **Remove?**
- Potential for nested network confusion
- Better to document affiliations in description/notes
- Cleaner architecture

**My vote:** Remove

---

### **4. Map URL**
✅ **Keep as simple field?**
- Networks commonly have overview maps
- Important for showing spatial extent
- Not as critical as trails (simple field sufficient, not rich array)

**My vote:** Keep (simple field)

---

### **5. Member Tracking**
✅ **Add member_count and member_site_ids?**
- CRITICAL missing functionality
- Essential for relationships
- Enables queries

**My vote:** Definitely add

---

### **6. Ownership Field**
✅ **Add ownership?**
- Parallel to Sites
- Important for legal structure
- Who owns vs who manages

**My vote:** Add

---

### **7. Rename Managing Agencies**
✅ **Rename to governance + partner_agencies?**
- Consistent with Trail schema
- Clearer terminology
- "governance" not "managing agency"

**My vote:** Rename

---

## 📊 SUMMARY

**Site Networks are organizational entities that need:**

**Critical additions:**
- ✅ Member tracking (count + IDs)
- ✅ Ownership field
- ✅ Simplified schema (remove rarely-used fields)

**Key changes:**
- ❌ Remove alternate_names, history, network_affiliation
- ✅ Add ownership, member_count, member_site_ids
- 🔄 Rename to governance/partner_agencies
- ✅ Keep map_url (simple field)

**Result:**
- 15 → 13 fields (cleaner)
- Better member tracking
- Consistent terminology

**What are your thoughts on these decisions?**

