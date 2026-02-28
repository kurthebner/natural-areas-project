# CROSS-ENTITY SCHEMA ANALYSIS v4.0 → v5.0
## All Six Entity Types - Comprehensive Review

**Date:** February 16, 2026  
**Scope:** Site, Trail, Trail Segment, Site Network, Trail Network, Access Point  
**Purpose:** Identify common patterns and entity-specific needs

---

## 📊 FIELD COUNT COMPARISON

| Entity Type | v4.0 Fields | Primary Identity | Key Relationships |
|-------------|-------------|------------------|-------------------|
| **Site** | 30 | name + county_list | → Site Networks, Child Sites, Access Points |
| **Trail** | 18 | trail_name + counties | → Sites, Trail Segments, Trail Networks, Access Points |
| **Trail Segment** | 14 | segment_name + parent_trail | → Parent Trail, Access Points |
| **Site Network** | 15 | network_name + network_type | → Member Sites |
| **Trail Network** | 13 | network_name + network_type | → Member Trails |
| **Access Point** | 17 | name + identity_parent | → Parent Site/Trail/Segment |

---

## 🔍 COMMON FIELDS ACROSS ENTITIES

### **Universal Identity Fields (ALL 6):**
1. ✅ **name** (or entity-specific variant)
2. ✅ **county_list** / **counties_traversed**
3. ✅ **description**
4. ✅ **notes**
5. ✅ **url**
6. ✅ **status**

### **Common Location Fields (4 of 6):**
- **Site**: address, location, municipality, township, gps, acres, geometry
- **Trail**: counties, total_length_miles, geometry
- **Trail Segment**: counties, segment_length_miles, gps_geometry
- **Access Point**: address, municipality, township, gps, plus_code

**Networks don't have direct location** (computed from members)

### **Common Governance Fields (5 of 6):**
- **Site**: ownership, governance, coordination
- **Trail**: primary_managing_agency, secondary_managing_agencies
- **Trail Segment**: managing_agency
- **Site Network**: primary_managing_agency, secondary_managing_agencies
- **Trail Network**: primary_managing_agency, secondary_managing_agencies

**Access Points don't have governance** (inherit from parent)

### **Common Classification Fields:**
- **Site**: category, subtype, designation, features
- **Trail**: trail_use_type, trail_surface_type, trail_origin_type
- **Trail Segment**: surface_type
- **Site Network**: network_type
- **Trail Network**: network_type
- **Access Point**: access_point_type, access_level, role

---

## 🎯 CROSS-ENTITY PATTERNS

### **Pattern 1: "Alternate Names" Field**

**Who has it:**
- Site Network (field 2)
- Trail (field 2)
- Trail Network (field 2)

**Who doesn't:**
- Site (NOT in schema!)
- Trail Segment
- Access Point

**Discovery experience:**
- Rarely documented (<5%)
- When present, usually informal/historical names

**Recommendation:**
- ❌ **Remove from networks** (use notes)
- ❌ **Remove from trails** (use notes)
- 💡 Consider adding to Sites IF we see patterns

---

### **Pattern 2: "History" Field**

**Who has it:**
- Site Network (field 11)
- Trail (field 12: "Trail History")
- Trail Network (field 5)

**Who doesn't:**
- Site (NOT in schema!)
- Trail Segment
- Access Point

**Discovery experience:**
- Sometimes available for trails (rail trail conversions, historic routes)
- Rarely separate from description

**Recommendation:**
- ✅ **Keep for trails** (rail trail origin is important)
- ❌ **Remove from networks** (merge into description)
- 💡 **Merge trail history into description** or keep separate?

---

### **Pattern 3: "Map URL" Field**

**Who has it:**
- Site (TSV field 20, but NOT in schema!)
- Trail (field 14)
- Trail Segment (field 12)
- Site Network (field 13)
- Trail Network (field 11)

**Who doesn't:**
- Access Point (only has URL)

**Discovery experience:**
- Rarely separate from main URL (<5%)
- When present, often Google Maps or embedded viewer

**Recommendation:**
- ❌ **Remove from ALL entities**
- Can generate map links from GPS/geometry
- Document exceptions in notes

---

### **Pattern 4: "Network Affiliation" Field**

**Who has it:**
- Site (field in schema)
- Trail (field 16)
- Site Network (field 9)

**Discovery experience:**
- Confusing overlap with Network entities
- When is it affiliation vs membership?

**Recommendation:**
- ❌ **Remove from ALL entities**
- Use relationship tables consistently
- Cleaner architecture

---

### **Pattern 5: GPS/Geometry Handling**

**Different approaches:**
- **Site**: gps_primary (string: "lat,lon"), geometry (WKT)
- **Trail**: No GPS, geometry (LineString)
- **Trail Segment**: gps_geometry (combined field?)
- **Access Point**: gps_primary (string: "lat,lon"), plus_code

**Issues:**
- Inconsistent GPS format (string vs what we want: numeric)
- Trail Segment "gps_geometry" is confusing name
- Access Points need GPS more than Sites (they ARE point locations)

**Recommendation:**
- ✅ **Standardize GPS**: gps_lat + gps_lon (numeric) for ALL point entities
- ✅ **Geometry separate**: Always WKT/blob field for spatial features
- ✅ **Trail Segment**: Rename gps_geometry → geometry (it's a LineString)
- ✅ **Plus Code**: Auto-generate from GPS for ALL point entities

---

### **Pattern 6: Ownership/Governance Terminology**

**Site uses:**
- ownership
- governance (was "management")
- coordination

**Trails/Networks use:**
- primary_managing_agency
- secondary_managing_agencies

**Issues:**
- Inconsistent terminology across entities
- "Primary managing agency" is long
- "Governance" vs "Management" vs "Managing Agency"

**Recommendation:**
- ✅ **Standardize terminology**:
  - **ownership** - Legal owner (Sites only - trails don't have clear ownership)
  - **governance** - Day-to-day manager (ALL entities that have management)
  - **coordination** - Partners (optional, rarely used)

**Proposed:**
- Sites: ownership, governance, coordination
- Trails: governance (rename from primary_managing_agency)
- Trail Segments: governance (rename from managing_agency)
- Networks: governance (rename from primary_managing_agency)
- Drop "secondary_managing_agencies" (use semicolon-delimited in governance)

---

### **Pattern 7: County Field Naming**

**Variations:**
- Site: county_list
- Trail: counties_traversed
- Trail Segment: county_list
- Site Network: counties_traversed
- Trail Network: county_list
- Access Point: county (singular!)

**Recommendation:**
- ✅ **Standardize to "counties"** (array in JSON)
- Simple, consistent, obvious plural
- Access Points: Still "county" (singular) - they're point locations

---

## 🚨 ENTITY-SPECIFIC ISSUES

### **SITE**

**Unique to Site:**
- ownership (legal title)
- governance vs management distinction
- parent_site_id (child sites)
- acres
- category/subtype/designation/features (complex classification)

**Issues:**
- address vs location redundancy ✓ (discussed)
- municipality/township not discoverable ✓ (discussed)
- Too many source fields ✓ (discussed)

---

### **TRAIL**

**Unique to Trail:**
- trail_use_type (Multi-Use, Hiking, Biking, Water)
- trail_surface_type (Paved, Natural, Gravel)
- trail_origin_type (Rail Trail, Canal Towpath, Purpose-Built)
- total_length_miles
- Geometry is ESSENTIAL (trails ARE linear features)

**Issues:**
- alternate_names rarely used → notes
- trail_history vs description → merge or keep?
- map_url rarely used → remove
- network_affiliation → use relationships

**Missing:**
- difficulty (Easy, Moderate, Difficult) - important for users!
- accessibility (ADA compliant, wheelchair accessible)

**Recommendation:**
- ✅ Add difficulty
- ✅ Add accessibility
- ❌ Remove alternate_names, map_url, network_affiliation
- 🤔 Keep trail_history separate or merge into description?

---

### **TRAIL SEGMENT**

**Unique to Trail Segment:**
- parent_trail (required relationship)
- segment_length_miles
- Represents portion of larger trail

**Issues:**
- "gps_geometry" confusing name → just "geometry"
- map_url rarely used → remove
- Minimal schema, seems OK

**Recommendation:**
- ✅ Rename gps_geometry → geometry
- ❌ Remove map_url
- ✅ Add difficulty (can vary by segment)
- ✅ Add accessibility (can vary by segment)

---

### **SITE NETWORK**

**Unique to Site Network:**
- network_type
- states_included (multi-state networks)
- Represents collection of Sites

**Issues:**
- alternate_names rarely used → notes
- history separate from description → merge
- map_url rarely used → remove
- network_affiliation creates recursion → remove
- Missing member tracking!

**Recommendation:**
- ❌ Remove alternate_names, history, map_url, network_affiliation
- ✅ Add member_count (number of sites)
- ✅ Add member_site_ids (array for linking)
- ✅ Add ownership (who owns/established the network)

---

### **TRAIL NETWORK**

**Same issues as Site Network:**
- alternate_names → remove
- history → merge into description
- map_url → remove
- Missing member tracking!

**Recommendation:**
- ❌ Remove alternate_names, history, map_url
- ✅ Add member_count (number of trails)
- ✅ Add member_trail_ids (array for linking)

---

### **ACCESS POINT**

**Unique to Access Point:**
- access_point_type (Trailhead, Parking, Entrance, Boat Launch)
- access_level (Primary, Secondary, Emergency)
- role (Main Entrance, Alternative Access) - redundant with access_level?
- identity_parent (Site, Trail, or Segment)
- GPS is REQUIRED (they ARE point locations)

**Issues:**
- role vs access_level distinction unclear
- municipality/township same discoverability issue as Sites
- No amenities field (restrooms, water, etc.)

**Recommendation:**
- 🤔 Merge role into access_level OR drop role
- ✅ Add amenities (important for users: restrooms, water, picnic, etc.)
- ✅ municipality/township handled like Sites (GIS-derived)

---

## 📋 CROSS-ENTITY V5.0 PROPOSALS

### **UNIVERSAL CHANGES (ALL ENTITIES):**

1. ✅ **Remove map_url** (all 5 entities that have it)
2. ✅ **Remove alternate_names** (networks + trails)
3. ✅ **Remove network_affiliation field** (use relationship tables)
4. ✅ **Standardize GPS format**: gps_lat + gps_lon (numeric) for point entities
5. ✅ **Standardize county field**: "counties" (array)
6. ✅ **Standardize governance terminology**: "governance" not "managing agency"

### **ENTITY-SPECIFIC CHANGES:**

**Sites (30 → 26 fields):**
- ❌ Remove: address (→ location), source_*, network_affiliation, geometry (→ GIS)
- 🔄 Modify: gps_primary → gps_lat + gps_lon, county_list → counties
- ✅ Keep: All classification fields (category, subtype, designation, features)

**Trails (18 → 17 fields):**
- ❌ Remove: alternate_names, map_url, network_affiliation
- ✅ Add: difficulty, accessibility
- 🤔 Consider: Merge trail_history into description OR keep separate?
- 🔄 Rename: primary_managing_agency → governance, counties_traversed → counties

**Trail Segments (14 → 13 fields):**
- ❌ Remove: map_url
- ✅ Add: difficulty, accessibility
- 🔄 Rename: gps_geometry → geometry, managing_agency → governance, county_list → counties

**Site Networks (15 → 12 fields):**
- ❌ Remove: alternate_names, history, map_url, network_affiliation, secondary_managing_agencies
- ✅ Add: ownership, member_count, member_site_ids
- 🔄 Rename: primary_managing_agency → governance, counties_traversed → counties

**Trail Networks (13 → 11 fields):**
- ❌ Remove: alternate_names, history, map_url, secondary_managing_agencies
- ✅ Add: member_count, member_trail_ids
- 🔄 Rename: primary_managing_agency → governance, county_list → counties

**Access Points (17 → 16 fields):**
- ❌ Remove: role (merge into access_level) OR keep both?
- ✅ Add: amenities
- 🔄 Modify: gps_primary → gps_lat + gps_lon
- 🔄 Municipality/township: GIS-derived like Sites

---

## 🎯 OPEN QUESTIONS FOR ALL ENTITIES

### **1. History Fields**

**Who has "History" or similar:**
- Trails: "Trail History" (field 12)
- Site Networks: "History" (field 11)
- Trail Networks: "History" (field 5)

**Question:** Merge into description or keep separate?

**Arguments for separate:**
- Rail trails have distinct origin story
- Historic trails have documented history
- Networks have establishment/evolution history

**Arguments for merge:**
- Rarely more than 1-2 sentences
- Description can accommodate: "13.1-mile paved rail trail from Bowling Green to North Baltimore following former railroad corridor built in 1873."

**Your preference?**

---

### **2. Secondary Managing Agencies**

**Current:**
- Trails: secondary_managing_agencies
- Networks: secondary_managing_agencies

**Options:**
- **A.** Remove secondary, allow governance to be semicolon-delimited
  - governance: "Wood County Park District; City of Bowling Green"
- **B.** Keep separate fields for primary vs secondary
- **C.** Use array in JSON with primary flag

**Your preference?**

---

### **3. Access Point Role vs Access Level**

**Current:**
- access_level: Primary, Secondary, Emergency
- role: Main Entrance, Alternative Access, Service Entrance

**Question:** Are these both needed or redundant?

**Options:**
- **A.** Merge: access_level becomes more descriptive (Primary/Main, Secondary/Alternative, Emergency, Service)
- **B.** Keep both: access_level for importance, role for function
- **C.** Drop role, keep access_level simple

**Your preference?**

---

### **4. Trail Difficulty**

**Should we add difficulty to:**
- ✅ Trails: Yes (definitely)
- ✅ Trail Segments: Yes (can vary by segment)
- ❓ Sites: No (not applicable)

**Values:**
- Easy, Moderate, Difficult, Expert (standard trail classification)

**Agreed?**

---

### **5. Accessibility**

**Should we add accessibility to:**
- ✅ Trails: Yes (ADA compliance matters)
- ✅ Trail Segments: Yes (can vary)
- ✅ Access Points: Maybe? (as part of amenities?)
- ❓ Sites: Maybe? (or just in notes?)

**Format:**
- Text field describing accessibility features
- OR boolean "wheelchair_accessible"
- OR array of accessibility features

**Your preference?**

---

### **6. Discovery Applicability**

**Which fields are discoverable from web sources?**

**Sites:**
- ✅ name, category, ownership, governance, description, features, url
- 🟡 acres (sometimes), location (usually)
- ❌ gps, municipality, township (GIS-derived)

**Trails:**
- ✅ name, use_type, surface_type, managing_agency, description, url
- 🟡 length (sometimes), difficulty (sometimes)
- ❌ geometry (GIS phase)

**Networks:**
- ✅ name, type, description, url
- 🟡 member_count (sometimes explicit)
- ❌ member_ids (relationship phase)

**Access Points:**
- 🟡 Sometimes documented (major trailheads)
- ❌ Often requires dedicated research phase
- ❌ GPS always requires geocoding

**Recommendation:** Separate discovery schemas by discoverability tier?

---

## 📊 V5.0 FIELD COUNT TARGETS

| Entity | v4.0 | v5.0 Target | Change | Key Additions | Key Removals |
|--------|------|-------------|--------|---------------|--------------|
| **Site** | 30 | 26 | -4 | None | address, source_*, network_affiliation |
| **Trail** | 18 | 17 | -1 | difficulty, accessibility | alternate_names, map_url, network_affiliation, trail_history |
| **Trail Segment** | 14 | 13 | -1 | difficulty, accessibility | map_url |
| **Site Network** | 15 | 12 | -3 | member_count, member_ids, ownership | alternate_names, history, map_url, network_affiliation |
| **Trail Network** | 13 | 11 | -2 | member_count, member_ids | alternate_names, history, map_url |
| **Access Point** | 17 | 16 | -1 | amenities | role (merged into access_level) |

---

## 🚀 NEXT STEPS

**To create complete v5.0 spec, I need your decisions on:**

1. ✅ **History fields**: Merge into description OR keep separate?
2. ✅ **Secondary managing agencies**: Remove OR keep OR array format?
3. ✅ **Access Point role**: Merge with access_level OR keep both OR drop?
4. ✅ **Difficulty**: Add to trails + segments?
5. ✅ **Accessibility**: Format and which entities?
6. ✅ **Any other cross-entity patterns I missed?**

**Then I can create:**
- Complete v5.0 schemas for all 6 entity types
- Cross-entity field mapping document
- Updated discovery/normalization/TSV specs for all entities
- JSON schema validators for all entities

**What are your preferences on the open questions?**

