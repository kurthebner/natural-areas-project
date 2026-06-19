# Canonical Feature Mapper — Natural Areas Project
# Last updated: 2026-05-22 (IMP-131 additions)

Copy `FEATURE_MAP` into each county pipeline script as the starting point. Extend with
county-specific patterns below the canonical list. Do not modify the canonical entries —
add county-specific overrides as additional tuples after the last canonical entry.

All patterns are case-insensitive regex matched against `features_raw`. The right-hand value
must be an exact term from the site vocabulary §6.2 features list. Extend the map when a
county uses a raw term that has no current pattern; never leave an out-of-vocabulary value
in the `features` TSV column.

```python
FEATURE_MAP = [
    # hiking / walking
    (r'hiking trail|walking trail|walking path|winding trail|nature trail|loop trail|trail system|woodland trail|foot trail', "Hiking Trail"),
    (r'boardwalk',                   "Boardwalk"),
    (r'mountain bike trail',         "Mountain Bike Trail"),
    (r'bridle trail|equestrian',     "Bridle Trail"),
    # interpretive features (canonical term is Interpretive Exhibit)
    (r'interpretive sign|interpretive signage|interpretive exhibit|interpretive trail|self.guided interpretive', "Interpretive Exhibit"),
    # water — bodies
    (r'wetland pond',                "Pond"),     # more specific before bare 'wetland'
    (r'\bwetland\b',                 "Wetland"),
    (r'\bpond\b',                    "Pond"),
    (r'\bbog\b|glacial bog',         "Bog"),
    (r'vernal pool',                 "Vernal Pool"),
    # water — access / facilities
    (r'boat ramp|launch ramp',       "Boat Ramp"),
    (r'boat launch|watercraft|canoe|kayak', "Watercraft Access"),
    (r'fishing pond|fishing lake|fishing pier|fishing dock', "Fishing Area"),
    (r'swimming beach|swim beach',   "Swimming Beach"),
    (r'swimming pool|city pool|\bpool\b', "Swimming Pool"),
    (r'splash pad|spray pad',        "Spray Park"),
    # bridges / infrastructure
    (r'\bbridge\b|stream crossing',  "Bridge"),
    (r'\bfence\b|fenced',            "Fence"),
    # picnic / shelter
    (r'pavilion|shelter house|open air pavilion|rentable.*shelter|covered seating', "Pavilion"),
    (r'picnic area|picnic spot|picnic table', "Picnic Area"),
    (r'gazebo',                      "Gazebo"),
    # sports
    (r'baseball|softball',           "Ball Diamond"),
    (r'basketball court',            "Basketball Court"),
    (r'tennis court',                "Tennis Court"),
    (r'pickleball court',            "Pickleball Court"),
    (r'volleyball court|sand volleyball', "Volleyball Court"),
    (r'soccer field|soccer complex', "Soccer Pitch"),
    (r'football field',              "Football Field"),
    (r'disc golf',                   "Disc Golf Course"),
    (r'skate park|skate ramp',       "Skate Park"),
    (r'miniature golf',              "Mini Golf"),
    # recreation
    (r'playground|play equipment',   "Playground"),
    (r'sledding hill',               "Sledding Hill"),
    (r'horseshoe',                   "Horseshoe Pitch"),
    (r'archery',                     "Archery Range"),
    (r'ropes course|high ropes',     "Ropes Course"),
    (r'shooting sports|shooting range', "Shooting Range"),
    (r'dog park|off-leash.*dog|dog.*run', "Dog Park"),
    # amenities
    (r'restroom|flush toilet|portable toilet|bathroom', "Restrooms"),
    (r'parking',                     "Parking Lot"),
    (r'bike rack',                   "Bike Rack"),
    (r'kiosk|information kiosk',     "Kiosk"),
    (r'camping|campsite',            "Camping"),
    (r'cabin|camper cabin|yurt',     "Cabin Rentals"),
    (r'ADA.compliant|ADA accessible|wheelchair', "ADA Accessible"),
    # natural features
    (r'observation deck',            "Observation Deck"),
    (r'hunting area|public hunting', "Hunting Area"),
    (r'wildlife viewing|wildlife.*observation', "Wildlife Observation Area"),
    # restoration / habitat
    (r'prairie restoration|habitat restoration', "Habitat Restoration Area"),
    # historical
    (r'historic.*ruin|building ruin', "Building Ruins"),
    (r'historic.*depot|train depot|caboose|railroad artifact', "Historic Structure"),
    (r'war memorial|memorial statue|monument|WWI|military monument', "Monument"),
    # educational / community / farm
    (r'nature center|nature lab',    "Nature Center"),
    (r'recreation center|community center|community centre', "Community Center"),
    (r'guided.*tour|wagon tour|tractor.*tour', "Guided Tours"),
    (r'farm store|bison.*store',     "Farm Store"),
    # misc
    (r'pollinator garden',           "Pollinator Garden"),
    # --- add county-specific patterns below this line ---
]
```

---

## Tokens That Belong in Notes (Not in Features)

The following `features_raw` token categories contain no physical infrastructure
information. They should be moved to the `notes` field during normalization — never
written to `features`.

**Operating rules / access restrictions**
- `dawn to dusk`, `open dawn to dusk`, `sunrise to sunset`
- `no bikes`, `no pets`, `foot traffic only`, `no bikes/horses/fires/hunting`
- `permit required for access`
- `no fee`

**Ecological / habitat character** (descriptive, not infrastructure)
- `riparian corridor`, `riparian habitat`, `mixed woodland`, `primitive woodland`,
  `rustic woodland`, `oak-to-maple transitional forest`, `spring wildflowers`
- Wildlife sightings: `turtles`, `frogs`, `aquatic life`, `wildlife hydration source`
- Landscape character: `rustic`, `maintained green field`

**Named water bodies** (use to describe location, not as a feature)
- `silver creek`, `apple creek`, `rathburn run`, `killbuck creek`
- `shreve lake`, `koehler's pond`, `brown's lake`

**Acreage expressed in features_raw**
- Move to `acres` field if not already set; otherwise append `{N} acres.` to notes.
- Examples: `~50 acres`, `24-25 acres`, `12 acres`

**Facility / trail detail sentences** (e.g., `7 pavilions (reservable)`, `1-mile boardwalk trail`)
- Use to populate both a canonical feature AND a note sentence. Add the canonical term
  to `features` and the detail text to `notes`.

---

## Tokens to Drop from Features

These tokens carry no actionable infrastructure information for catalog users. Drop from
features during normalization — do not add to notes.

**Activity terms** (activities map to physical infrastructure or are dropped)
- `fishing` (use Fishing Area if there is a specific facility; otherwise drop)
- `multi-use recreation`
- `public access` (implicit for all cataloged entities)

**Generic ecological species / botanical**
- `old-growth forest`, `white oak`, `red oak`
- `sphagnum moss`, `pitcher plants (sarracenia purpurea)`, `sundews`, `bog rosemary`,
  `rare orchids` (use Bog as the feature if applicable)
- `living plant collection`, `research arboretum`, `woody plant collections`

**Generic category labels** (not features)
- `city nature preserve`, `memorial`, `nonprofit trail system`
- `3 named trails`, `outer trail`, and other named-trail entity references

---

## Named Trail Entities in Features

When `features_raw` contains the name of a specific trail entity (e.g., `Spangler Trail 1.5mi`,
`Sassafras Trail 0.6mi`, `Trillium Trail`), remove it from `features`. Named trails are
discrete entities in the catalog — not feature attributes of a parent site.

---

## Terms with No Vocabulary Equivalent

The following raw terms have no matching controlled vocabulary term and must remain in
`features_raw` only — never in the `features` TSV column:

- Concession Stand
- Dump Station
- Water Frontage (IMP-038)

**Vocabulary expansion candidates** (confirmed physical infrastructure; add to vocabulary
before next county run that uses these terms):
- `Alvar` (rocky limestone plain habitat; OH-OTT-S-024)
- `Vault Toilet` (type of restroom; separate from Restrooms)
- `Viewing Platform` / `accessible observation deck` (variant of Observation Deck)

If a new raw term is found that does not map to any vocabulary term, add it to this list
rather than inventing a new vocabulary value. New vocabulary terms require a vocabulary
module update and a version increment.
