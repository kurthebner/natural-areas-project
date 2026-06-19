#!/usr/bin/env python3
"""
na_vocab_constants.py — Natural Areas Project Vocabulary Constants
v1.0  |  2026-04-19

Single source of truth for all controlled vocabulary values across the six
entity types. Import this module during normalization (Stage 2) to validate
assignments before writing the pipeline script, and during the pipeline
itself via na_pipeline_core.

SOURCES (read these before normalization in every county run):
    vocabularies/na_site_vocabulary_v5.5.md
    vocabularies/na_trail_vocabulary_v5.1.md
    vocabularies/na_access_point_vocabulary.md

USAGE:
    import sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'utilities'))
    from na_vocab_constants import (
        ALLOWED_CATEGORIES, ALLOWED_SUBTYPES, ALLOWED_FEATURES,
        ALLOWED_DESIGNATIONS, ALLOWED_SITE_STATUSES,
        ALLOWED_TRAIL_USE_TYPES, ALLOWED_TRAIL_SURFACES,
        ALLOWED_TRAIL_ORIGINS, ALLOWED_TRAIL_STATUSES,
        ALLOWED_TRAIL_DIFFICULTIES, ALLOWED_AP_TYPES, ALLOWED_AP_STATUSES,
        subtypes_for, feature_valid, designation_valid,
    )

UPDATE POLICY:
    When a vocabulary module is revised, update this file and bump the
    version comment. Do not patch vocabulary values in county pipeline
    scripts — all changes belong here.
"""

from typing import Dict, FrozenSet, Optional


# ════════════════════════════════════════════════════════════════════════════
#  SITE VOCABULARY  (na_site_vocabulary_v5.5.md)
# ════════════════════════════════════════════════════════════════════════════

# §2.1 — 18 allowed categories
ALLOWED_CATEGORIES: FrozenSet[str] = frozenset({
    "Campground",
    "Cemetery",
    "Community Garden",
    "Conservation Area",
    "Cultural Facility",
    "Curated Biological Site",
    "Fishing Area",
    "Historic Site",
    "Hunting Area",
    "Memorial",
    "Museum",
    "Natural Area",
    "Nature Preserve",
    "Open Space",
    "Park",
    "Recreation Facility",
    "Water Site",
    "Wildlife Area",
})

# §3.2 — subtypes by category (category-specific; never globally interchangeable)
ALLOWED_SUBTYPES: Dict[str, FrozenSet[str]] = {
    "Park": frozenset({
        "Civic Park",
        "Dog Park",
        "Greenspace",
        "Historic Park",
        "Linear Park",
        "Neighborhood Park",
        "Playground Park",
        "Sports Park",
        "Waterfront Park",
    }),
    "Nature Preserve": frozenset({
        "Conservation Easement Preserve",
        "County Nature Preserve",
        "Land Trust Preserve",
        "Municipal Nature Preserve",
        "Private Nature Preserve",
        "State Nature Preserve",
    }),
    "Recreation Facility": frozenset({
        "Athletic Field",
        "BMX Track",
        "Disc Golf Course",
        "Golf Course",
        "Ice Rink",
        "Pickleball Complex",
        "Pump Track",
        "Recreation Center",
        "Skate Park",
        "Sports Complex",
        "Swimming Pool",
        "Tennis Complex",
    }),
    "Wildlife Area": frozenset({
        "Federal Wildlife Area",
        "Migratory Bird Area",
        "State Wildlife Area",
        "Waterfowl Area",
        "Wetland Management Area",
    }),
    "Conservation Area": frozenset({
        "Forest Management Area",
        "Habitat Management Area",
        "Resource Protection Area",
        "Restoration Area",
        "Watershed Protection Area",
    }),
    "Natural Area": frozenset({
        "Barrens",
        "Bog",
        "Cliff or Bluff",
        "Fen",
        "Floodplain Forest",
        "Forest",
        "Grassland",
        "Marsh",
        "Meadow",
        "Old Field",
        "Prairie",
        "Ravine",
        "Riparian Area",
        "Savanna",
        "Shrubland",
        "Successional Area",
        "Swamp",
        "Upland Forest",
        "Wetland",
    }),
    "Water Site": frozenset({
        "Boat Launch Area",
        "Fishing Lake",
        "Harbor",
        "Lake",
        "Marina",
        "Pond",
        "Reservoir",
        "Retention Pond",
        "River",
    }),
    "Open Space": frozenset({
        "Boulevard Median",
        "Civic Lawn",
        "Commons",
        "Greenbelt",
        "Suburban Open Space",
        "Urban Open Space",
    }),
    "Memorial": frozenset({
        "Civic Memorial",
        "Memorial Garden",
        "Memorial Plaza",
        "Monument",
        "Veterans Memorial",
        "War Memorial",
    }),
    "Cultural Facility": frozenset({
        "Art Center",
        "Cultural Center",
        "Heritage Center",
        "Interpretive Center",
        "Performing Arts Center",
        "Visitor Center",
    }),
    "Curated Biological Site": frozenset({
        "Aquarium",
        "Arboretum",
        "Aviary",
        "Biopark",
        "Botanical Garden",
        "Butterfly House",
        "Insectarium",
        "Living Museum",
        "Reptile House",
        "Zoo",
    }),
    "Historic Site": frozenset({
        "Archaeological Site",
        "Battlefield",
        "Historic Landscape",
        "Historic Landmark",
        "Historic Structure",
    }),
    "Cemetery": frozenset({
        "Church Cemetery",
        "Family Cemetery",
        "Private Cemetery",
        "Public Cemetery",
        "Veterans Cemetery",
        "Green Burial Cemetery",
    }),
    "Campground": frozenset({
        "Cabin Campground",
        "Group Campground",
        "Primitive Campground",
        "RV Campground",
        "Tent Campground",
    }),
    "Museum": frozenset({
        "Art Museum",
        "Children's Museum",
        "History Museum",
        "Natural History Museum",
        "Science Museum",
        "Cultural Museum",
    }),
    # Categories with no defined subtypes
    "Community Garden":  frozenset(),
    "Fishing Area":      frozenset(),
    "Hunting Area":      frozenset(),
}

# §4.x — allowed designations (source: na_site_vocabulary §4.2–§4.4)
ALLOWED_DESIGNATIONS: FrozenSet[str] = frozenset({
    # §4.2 Federal
    "National Park",
    "National Monument",
    "National Historic Site",
    "National Memorial",
    "National Historic Landmark",
    "National Natural Landmark",
    "National Recreation Area",
    "National Wildlife Refuge",
    "National Scenic Trail",
    "National Wild and Scenic River",
    "National Heritage Area",
    "National Battlefield",
    "National Cemetery",
    "National Register of Historic Places (NRHP)",
    "National Forest",
    "National Grassland",
    "National Historic Trail",
    "Wilderness Area",
    # §4.3 State
    "State Park",
    "State Nature Preserve",
    "State Wildlife Area",
    "State Fishing Area",
    "State Hunting Area",
    "State Memorial",
    "State Forest",
    "State Scenic River",
    "State Natural Landmark",
    "State Archaeological Preserve",
    "State Historic Site",
    "State Recreation Area",
    "State Nature Area",
    # §4.4 Local / Special
    "County Historic Landmark",
    "Municipal Historic Landmark",
    "Local Historic Landmark",
    "Local Nature Preserve",
    "Registered Cemetery",
    "Protected Wetland",
    "Mitigation Bank",
    "Conservation Easement",
    "Land Trust Preserve",
})

# §5 — allowed site statuses (source: na_site_vocabulary §5)
ALLOWED_SITE_STATUSES: FrozenSet[str] = frozenset({
    "Active",
    "Seasonal",
    "Access Permit Required",
    "No Public Entry",
    "Under Development",
    "Proposed",
    "Abandoned",
    "Closed",
    "Defunct",
    "Unknown",
})

# §6.2 — allowed features (complete list, na_site_vocabulary_v5.5)
# Note: Water Frontage is NOT in this list — retained in features_raw only (IMP-038).
# Note: Concession Stand, Dump Station also features_raw only — no vocabulary equivalent.
ALLOWED_FEATURES: FrozenSet[str] = frozenset({
    "ADA Accessible",
    "AED",
    "Alvar",
    "Amphibian Area",
    "Amphitheater",
    "Apiary",
    "Arboretum",
    "Archery Range",
    "Art Gallery",
    "Art Installation",
    "Athletic Field",
    "Ball Diamond",
    "Ballroom",
    "Bandstand",
    "Basketball Court",
    "Beach",
    "Bike Rack",
    "Bike Repair Station",
    "Bird Viewing Area",
    "Boardwalk",
    "Boat Dock",
    "Boat Ramp",
    "Bocce Court",
    "Bog",
    "Bluff",
    "Boathouse",
    "Bridge",
    "Bridle Trail",
    "Building Ruins",
    "Butterfly or Pollinator Garden",
    "Cabin Rentals",
    "Camping",
    "Canal Structure",
    "Cave or Cavern",
    "Cemetery Section",
    "Chapel",
    "Cliff",
    "Climbing Structure",
    "Community Center",
    "Community Garden",
    "Composting Station",
    "Conservatory",
    "Covered Shelter",
    "Cricket Pitch",
    "Culvert",
    "Dam",
    "Dance Floor",
    "Dance Performance Space",
    "Demonstration Farm Plot",
    "Demonstration Garden",
    "Disc Golf Course",
    "Dog Park",
    "Drainage Ditch",
    "Dune",
    "Educational Pavilion",
    "Electric Vehicle Charging",
    "Equestrian Arena",
    "Farm Store",
    "Fence",
    "Fen",
    "Fieldhouse",
    "Fire Ring",
    "Fire Tower",
    "Fishing Area",
    "Fitness Station",
    "Football Field",
    "Football Stadium",
    "Fountain",
    "Garage",
    "Garden",
    "Gate",
    "Gatehouse",
    "Gazebo",
    "Glacial Erratic",
    "Golf Course",
    "Gorge",
    "Greenhouse",
    "Grill",
    "Guided Tours",
    "Habitat Restoration Area",
    "Handball Court",
    "Hiking Trail",
    "Hilltop",
    "Historic Bridge",
    "Historic Canal Segment",
    "Historic Cemetery Section",
    "Historic Fence Line",
    "Historic Foundation",
    "Historic Lock",
    "Historic Marker",
    "Historic Marker Cluster",
    "Historic Millrace",
    "Historic Road Trace",
    "Historic Ruins",
    "Historic Structure",
    "Historic Well",
    "Horseshoe Pitch",
    "Hunting Area",
    "Ice Rink",
    "Information Board",
    "Insectarium",
    "Interpretive Exhibit",
    "Interpretive Garden",
    "Interpretive Sign",
    "Island",
    "Kiosk",
    "Kite Flying",
    "Lacrosse Field",
    "Lake",
    "Landmark Tree",
    "Levee",
    "Lodge",
    "Lookout Cabin",
    "Maintenance Building",
    "Marina",
    "Marsh",
    "Meadow",
    "Mini Golf",
    "Model Airplane Field",
    "Model Rocketry Field",
    "Monitoring Station",
    "Monument",
    "Mountain Bike Trail",
    "Multi-use Trail",
    "Museum Building",
    "Musical Instruments",
    "Musical Performance Space",
    "Native American Artifacts",
    "Native American Cultural Site",
    "Native American Earthwork",
    "Natural Arch",
    "Nature Center",
    "Nature Play Area",
    "Observation Deck",
    "Observation Tower",
    "Observatory",
    "Old-Growth Stand",
    "Orchard",
    "Outdoor Art Installation",
    "Outdoor Classroom",
    "Overflow Parking",
    "Overlook (built)",
    "Overlook (natural)",
    "Parking Lot",
    "Pavilion",
    "Peninsula",
    "Pickleball Court",
    "Picnic Area",
    "Picnic Shelter",
    "Picnic Table Cluster",
    "Pipeline Corridor",
    "Pioneer Historic Site",
    "Pioneer Re-creation",
    "Planetarium",
    "Playground",
    "Pollinator Garden",
    "Pond",
    "Powerline Corridor",
    "Prairie",
    "Prairie Restoration",
    "Public Art Installation",
    "Pump Station",
    "Pump Track",
    "Rain Garden",
    "Ravine",
    "Reforestation Area",
    "Reptile House",
    "Research Plot",
    "Restrooms",
    "Retaining Wall",
    "Retention Basin",
    "Ridge",
    "Rock Outcrop",
    "Ropes Course",
    "Scenic View",
    "Sculpture",
    "Sedge Meadow",
    "Shooting Range",
    "Shotgun Range",
    "Shuffleboard Court",
    "Silo",
    "Sinkhole",
    "Skate Park",
    "Ski Slopes",
    "Sledding Hill",
    "Slide",
    "Soccer Pitch",
    "Spillway",
    "Spray Park",
    "Spring",
    "Stable",
    "Stage",
    "Stormwater Basin",
    "Stream Segment",
    "Swimming Beach",
    "Swimming Pool",
    "Swing Set",
    "Tennis Court",
    "Theatre",
    "Topiary",
    "Trapping Area",
    "Transit Stop",
    "Trolley",
    "Tropical Garden",
    "Utility Corridor",
    "Valley",
    "Vegetable Garden",
    "Vernal Pool",
    "Via Ferrata",
    "Viewing Platform",
    "Vineyard",
    "Visitor Center",
    "Volleyball Court",
    "Wall",
    "Water Park",
    "Water Tower",
    "Watercraft Access",
    "Waterfall (built)",
    "Waterfall (natural)",
    "Waterslide",
    "Weather Station",
    "Weir",
    "Wetland",
    "Wetland Restoration",
    "Wild Animal Rehabilitation",
    "Wilderness Area",
    "Wildlife Observation Area",
    "Working Railway",
    "Zoo",
})


# ════════════════════════════════════════════════════════════════════════════
#  TRAIL VOCABULARY  (na_trail_vocabulary_v5.1.md)
# ════════════════════════════════════════════════════════════════════════════

ALLOWED_TRAIL_USE_TYPES: FrozenSet[str] = frozenset({
    "Bicycling",
    "BMX",
    "Bridle",
    "Cross Country Ski",
    "Hiking",
    "Mountain Bike",
    "Multi-Use",
    "Other",
    "Pump Track",
    "Snowmobile",
    "Water",
})

ALLOWED_TRAIL_SURFACES: FrozenSet[str] = frozenset({
    "Boardwalk",
    "Crushed Stone",
    "Gravel",
    "Mixed",
    "Natural Surface",
    "Other",
    "Paved",
    "Water",
})

ALLOWED_TRAIL_ORIGINS: FrozenSet[str] = frozenset({
    "Canal Towpath",
    "Greenway Corridor",
    "Historic Route",
    "Other",
    "Purpose-Built",
    "Rail Trail",
    "Roadside Corridor",
    "Utility Corridor",
})

ALLOWED_TRAIL_STATUSES: FrozenSet[str] = frozenset({
    "Active",
    "Closed",
    "Gap",
    "Planned",
    "Under Construction",
})

ALLOWED_TRAIL_DIFFICULTIES: FrozenSet[str] = frozenset({
    "Difficult",
    "Easy",
    "Expert",
    "Moderate",
    "Strenuous",
})


# ════════════════════════════════════════════════════════════════════════════
#  ACCESS POINT VOCABULARY  (na_access_point_vocabulary_v5.2.md)
# ════════════════════════════════════════════════════════════════════════════

ALLOWED_AP_TYPES: FrozenSet[str] = frozenset({
    "Administrative Access",
    "Bicycle Access",
    "Boat Launch",
    "Boat Ramp",
    "Cross Country Ski Access",
    "Equestrian Access",
    "Ferry Access",
    "Fishing Access",
    "Hazard Portage",
    "Other",
    "Parking Area",
    "Pedestrian Entrance",
    "River Access",
    "Roadside Pull-Off",
    "Shuttle Access",
    "Snowmobile Access",
    "Trailhead",
    "Transit Access",
    "Vehicle Entrance",
    "Watercraft Access Point",
})

ALLOWED_AP_STATUSES: FrozenSet[str] = frozenset({
    "Active",
    "Closed",
    "Restricted",
    "Seasonal",
})

# AP features are FREE TEXT — no controlled vocabulary (na_access_point_vocabulary §1)


# ════════════════════════════════════════════════════════════════════════════
#  CONVENIENCE HELPERS
# ════════════════════════════════════════════════════════════════════════════

def subtypes_for(category: str) -> FrozenSet[str]:
    """Return the allowed subtype set for a given category, or empty frozenset."""
    return ALLOWED_SUBTYPES.get(category, frozenset())


def feature_valid(term: str) -> bool:
    """True if term is an allowed §6.2 features value."""
    return term in ALLOWED_FEATURES


def designation_valid(designation: str) -> bool:
    """True if designation is an allowed §4.x value."""
    return designation in ALLOWED_DESIGNATIONS


def category_valid(category: str) -> bool:
    """True if category is one of the 18 allowed §2.1 values."""
    return category in ALLOWED_CATEGORIES


def subtype_valid(category: str, subtype: str) -> bool:
    """True if subtype is in the permitted list for that category."""
    return subtype in subtypes_for(category)
