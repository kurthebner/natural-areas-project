# TRAIL SEGMENT SCHEMA ANALYSIS v4.0 → v5.0

**Date:** February 16, 2026  
**Current:** Trail Segment Schema v4.0 (14 fields)  
**Focus:** Identifying issues and proposing v5.0 improvements

---

## 📊 CURRENT V4.0 TRAIL SEGMENT SCHEMA

### **14 Fields (Authoritative Order):**

1. **Parent Trail** (required)
2. **Segment Name** (optional)
3. **County List** (required)
4. **Managing Agency** (required)
5. **Segment Length (Miles)** (optional)
6. **Surface Type** (required)
7. **Status** (required)
8. **GPS Geometry** (optional)
9. **Description** (optional)
10. **Notes** (optional)
11. **URL** (optional)
12. **Map URL** (optional)
13. **Derived Label** (computed)
14. **Parent Trail Network** (optional)

---

## 🎯 PURPOSE OF TRAIL SEGMENTS

**From Schema:**
> "A Trail Segment is a continuous, mappable operational portion of a Trail. Segments represent stretches that differ in surface, management, jurisdiction, condition, geometry, or operational characteristics."

**When to create Trail Segments:**
- Trail sections with different surfaces (paved → gravel)
- Trail sections with different managers (crosses jurisdictions)
- Trail sections with different conditions (Active → Gap → Planned)
- Named sections of long trails ("Buckeye Trail - Wood County Section")

**When NOT to create:**
- Every minor surface change
- Synthetic divisions for convenience
- Unnamed sections unless functionally distinct

---

## 🔍 ISSUES IDENTIFIED

### **Issue 1: "GPS Geometry" Field Name**

**Current v4.0:**
- Field 8: "GPS Geometry"

**Problem:**
- Confusing name - this isn't "GPS" data (point locations)
- It's geometry data (LineString for linear segments)
- "GPS" suggests lat/lon point coordinates
- Actually contains: WKT, GeoJSON, or polyline

**Comparison to other entities:**
- Site: "geometry" (not "GPS geometry")
- Trail: "geometry" (not "GPS geometry")
- Access Point: "gps_primary" (actual GPS coordinates)

**Discovery reality:**
- Segments almost NEVER have geometry during web discovery
- Geometry requires GIS tracing or GPX file
- This is a GIS phase field, not discovery

**RECOMMENDATION:** 
✅ **Rename "GPS Geometry" → "geometry"**
- Consistent with Site and Trail schemas
- Clearer purpose
- Still WKT/GeoJSON/polyline format
- Still optional, populated in GIS phase

---

### **Issue 2: Map URL**

**Current v4.0:**
- Field 12: "Map URL"
- Semicolon-delimited if multiple

**Trail decision:** We decided to KEEP and enhance to rich array for Trails

**Trail Segment consideration:**

**When do segments have separate maps?**
- Long trail with officially published segment maps
- Example: "Buckeye Trail - Wood County Section Map"
- GIS layers showing individual segments
- Downloadable GPX files per segment

**Reality:**
- Less common than trail-level maps
- Usually segments inherit trail's maps
- But some long trails DO publish segment-specific maps

**Example - Buckeye Trail:**
```
Trail: "Buckeye Trail" (1,444 miles)
Maps: [Full trail map, interactive viewer, GPX downloads]

Segment: "Buckeye Trail - Wood County Section" (37 miles)
Maps: [Section-specific PDF, GPX for this section only]
```

**RECOMMENDATION:**
✅ **KEEP Map URL, make it rich array like Trails**

**JSON Format:**
```json
{
  "maps": [
    {
      "url": "https://buckeyetrail.org/maps/wood-county-section.pdf",
      "type": "pdf",
      "description": "Wood County section map"
    },
    {
      "url": "https://buckeyetrail.org/gpx/wood-county.gpx",
      "type": "gpx",
      "description": "GPS track for Wood County section"
    }
  ]
}
```

---

### **Issue 3: Managing Agency Terminology**

**Current v4.0:**
- Field 4: "Managing Agency"

**Trail decision:** We changed to "governance" for consistency

**Trail Segment:**
- Currently: "Managing Agency"
- Should be: "governance" (consistent with Trail, Site)

**RECOMMENDATION:**
✅ **Rename "Managing Agency" → "governance"**

---

### **Issue 4: Parent Trail Network**

**Current v4.0:**
- Field 14: "Parent Trail Network"

**Purpose from schema:**
> "Used only when the segment is a documented member of a Trail Network."

**Question:** When would a SEGMENT be in a network but not its parent TRAIL?

**Possible scenarios:**
- Trail partially in network (only some segments)
- Segment shared between multiple trails in different networks
- Network membership changes mid-trail

**Analysis:**
- If trail is in network → all segments inherit network membership
- Segment-level network affiliation seems edge case
- Better handled via relationship tables

**But wait - schema says:**
> "Must not be used to represent Trail → Trail Segment relationships"

So this is specifically for segments that are network members independently of their parent trail.

**RECOMMENDATION:**
❌ **Remove "Parent Trail Network" field**
✅ **Use relationship tables instead**

**Rationale:**
- Relationship: Segment → Parent Trail (via parent_trail_id)
- Relationship: Trail → Network (via trail_network_members table)
- Segment inherits network through parent trail
- Edge cases handled via explicit relationship table entries
- Cleaner architecture

---

### **Issue 5: Missing Fields from Trail**

**Trail has these fields that Segment doesn't:**

**From Trail schema:**
- alternate_names
- trail_use_type (Multi-Use, Hiking, MTB)
- trail_origin_type (Rail Trail, Canal Towpath)
- difficulty (we're adding)
- accessibility (we're adding)
- trail_history
- partner_agencies (secondary managing)

**Should Trail Segments have any of these?**

#### **alternate_names**
- Segments rarely have alternate names
- Usually just "Section A" or "Mile 0-5"
- **RECOMMENDATION:** ❌ Don't add

#### **trail_use_type**
- Could segments have different uses than parent trail?
- Example: "Multi-use trail but MTB prohibited on segment through park"
- **CONSIDERATION:** Might be useful but rare
- **RECOMMENDATION:** 🤔 Probably not needed (use notes)

#### **trail_origin_type**
- Segments inherit origin from parent trail
- Rail trail segment is still a rail trail
- **RECOMMENDATION:** ❌ Don't add (redundant with parent)

#### **difficulty** ⭐
- **Can segments have different difficulty than parent trail?**
- **YES!** Common scenario:
  - Trail overall: Moderate
  - Segment 1 (flat rail trail section): Easy
  - Segment 2 (steep hill climb): Difficult
- **RECOMMENDATION:** ✅ **ADD difficulty to segments**

#### **accessibility** ⭐
- **Can segments have different accessibility?**
- **YES!** Very common:
  - Trail overall: Partially accessible
  - Segment 1 (paved section): ADA compliant
  - Segment 2 (natural surface): Not wheelchair accessible
- **RECOMMENDATION:** ✅ **ADD accessibility to segments**

#### **trail_history**
- Segments don't have independent history
- History belongs to parent trail
- **RECOMMENDATION:** ❌ Don't add

#### **partner_agencies**
- **Can segments have different managers than parent trail?**
- **YES!** This is explicitly in current schema (field 4: Managing Agency)
- Long trails crossing jurisdictions often have different managers per segment
- **RECOMMENDATION:** ✅ **Keep governance field (single or semicolon-delimited)**
- **QUESTION:** Do we need partner_agencies (secondary) for segments?

---

### **Issue 6: Segment Type vs Segment Role**

**Vocabulary has TWO classification systems:**

**Segment Type:**
- Linear, Loop, Connector, Access Segment, Crossing, Spur

**Segment Role:**
- Primary Segment, Secondary Segment, Connector Segment, Access Segment, Scenic Segment, Interpretive Segment

**Problem:** Overlap! "Connector" and "Access Segment" appear in both!

**Current schema ONLY has:**
- Surface Type (field 6)

**Schema does NOT have:**
- Segment Type
- Segment Role

**But vocabulary defines them!**

**Analysis:**
- Vocabulary suggests these were planned but not implemented in schema
- Or removed from schema but vocabulary not updated
- Segment Type (geometric/functional form) could be useful
- Segment Role (functional purpose) could be useful

**RECOMMENDATION:**
🤔 **Should we add Segment Type and/or Segment Role to schema?**

**Examples where it matters:**

**Segment Type:**
```
Trail: "City Park Loop Trail"
Segment 1: "Main Loop" - type: Loop
Segment 2: "Connector to Parking" - type: Connector
```

**Segment Role:**
```
Trail: "Nature Trail"
Segment 1: "Main Trail" - role: Primary Segment
Segment 2: "Interpretive Loop" - role: Interpretive Segment
Segment 3: "Scenic Overlook Spur" - role: Scenic Segment
```

**Your input:** Should we add segment_type and/or segment_role fields?

---

## 📋 PROPOSED TRAIL SEGMENT SCHEMA V5.0

### **Changes from v4.0:**

**Renamed:**
1. 🔄 "GPS Geometry" → **"geometry"**
2. 🔄 "Managing Agency" → **"governance"**
3. 🔄 "County List" → **"counties"** (array)
4. 🔄 "Map URL" → **"maps"** (rich array)

**Added:**
5. ✨ **difficulty** (NEW - can vary by segment)
6. ✨ **accessibility** (NEW - can vary by segment)
7. ✨ **segment_type** (NEW? - from vocabulary: Linear, Loop, Connector, etc.)
8. ✨ **segment_role** (NEW? - from vocabulary: Primary, Scenic, Interpretive, etc.)

**Removed:**
9. ❌ "Parent Trail Network" (use relationship tables)

**Consider:**
10. 🤔 **partner_agencies** (secondary managing agencies - do segments need this?)

---

### **Proposed v5.0 Field List:**

**Core Identity:**
1. parent_trail_id (FK to trails)
2. segment_name (optional)

**Location:**
3. counties (array)
4. segment_length_miles

**Classification:**
5. surface_type
6. segment_type (NEW - Linear/Loop/Connector/Spur) - IF WE ADD
7. segment_role (NEW - Primary/Scenic/Interpretive) - IF WE ADD
8. difficulty (NEW - Easy/Moderate/Difficult)
9. accessibility (NEW - text description)
10. status

**Governance:**
11. governance
12. partner_agencies (NEW? - secondary managers)

**Spatial:**
13. geometry (WKT/GeoJSON - GIS phase)

**Descriptive:**
14. description
15. notes

**URLs:**
16. url
17. maps (rich array)

**Auto-generated:**
18. segment_id
19. derived_label
20. created_at, updated_at

**Result: 14 → 17-19 fields (depending on decisions)**

---

## ❓ DECISIONS NEEDED

### **1. Geometry Field Name**
✅ **Rename "GPS Geometry" → "geometry"?**
- More accurate (it's not GPS data)
- Consistent with Site/Trail
- Clearer purpose

**My vote:** YES

---

### **2. Map URL**
✅ **Keep and enhance to rich array?**
- Like we decided for Trails
- Support multiple maps per segment
- PDF, GPX, interactive viewers

**My vote:** YES (following Trail pattern)

---

### **3. Difficulty**
✅ **Add difficulty field?**
- Segments can have different difficulty than parent trail
- Important for user planning
- Common scenario (easy section + difficult section)

**My vote:** YES

---

### **4. Accessibility**
✅ **Add accessibility field?**
- Segments can have different accessibility than parent
- Critical for inclusive access
- Very common (paved section accessible, natural section not)

**My vote:** YES

---

### **5. Segment Type** ⭐
🤔 **Add segment_type field?**
- From vocabulary: Linear, Loop, Connector, Access Segment, Crossing, Spur
- Describes geometric/functional form
- Could be useful for complex trail systems

**Examples where it matters:**
- Distinguishing main loop from connector segments
- Identifying access spurs vs main trail
- Road crossings mapped as segments

**Your input needed:** Add this field or not?

---

### **6. Segment Role** ⭐
🤔 **Add segment_role field?**
- From vocabulary: Primary, Secondary, Connector, Scenic, Interpretive
- Describes functional purpose
- Could be useful for trail planning

**Examples where it matters:**
- Main trail vs interpretive side loops
- Primary corridor vs scenic detours
- Functional vs educational segments

**Your input needed:** Add this field or not?

---

### **7. Partner Agencies** ⭐
🤔 **Add partner_agencies (secondary managing agencies)?**
- Trail has: governance + partner_agencies
- Segment has: governance only
- Long trails crossing jurisdictions might need both

**Example:**
```
Segment: "Buckeye Trail - Wayne National Forest Section"
Governance: "Buckeye Trail Association"
Partner Agencies: "USDA Forest Service; Ohio DNR"
```

**Your input needed:** Add partner_agencies to segments?

---

### **8. Parent Trail Network Field**
❌ **Remove and use relationship tables instead?**
- Cleaner architecture
- Network membership through parent trail
- Edge cases via explicit relationships

**My vote:** Remove

---

## 📊 SUMMARY

**Trail Segment is simpler than Trail but needs similar enhancements:**

**Clear decisions:**
- ✅ Rename GPS Geometry → geometry
- ✅ Rename Managing Agency → governance
- ✅ Keep Map URL as rich array
- ✅ Add difficulty
- ✅ Add accessibility
- ✅ Remove Parent Trail Network field

**Need your input:**
- 🤔 Add segment_type field?
- 🤔 Add segment_role field?
- 🤔 Add partner_agencies field?

**What are your thoughts?**

