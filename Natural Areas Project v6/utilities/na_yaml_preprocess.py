#!/usr/bin/env python3
"""
na_yaml_preprocess.py — Natural Areas Project
Pre-processor for raw discovery YAML files.

PROBLEM (IMP-089): Values containing ' #' (space + hash) in YAML fields are
treated as inline comments by yaml.safe_load(), silently truncating the value.
  Example:  features_raw: Pavilion #1; Shelter #3
  Parsed as: features_raw: "Pavilion"      ← #1; Shelter #3 is eaten as comment

SOLUTION: Scan each line before YAML parsing. If a bare (unquoted) field value
contains ' #' or starts with '#', wrap the value in single quotes, escaping
any internal single quotes as ''. This produces valid YAML that parses correctly.

USAGE (pre-process before parsing):
    from utilities.na_yaml_preprocess import preprocess_yaml_text, preprocess_yaml_file
    import yaml

    # From text already in memory:
    clean_text = preprocess_yaml_text(raw_text)
    records = list(yaml.safe_load_all(clean_text))

    # From a file (writes .yaml.bak backup, then modifies in place):
    clean_path = preprocess_yaml_file("van_wert_oh_raw_discovery.yaml")
    with open(clean_path, encoding="utf-8") as f:
        records = list(yaml.safe_load_all(f))

SAFE TO RUN MULTIPLE TIMES: Already-quoted values are not re-quoted.
"""

import re
import shutil
from pathlib import Path

# Matches: leading whitespace + word/underscore key + colon + one-or-more spaces + value
# Group 1 = "  key: "  (key part including trailing space)
# Group 2 = value text (everything after, stripped of trailing whitespace)
_KEY_VALUE_RE = re.compile(r'^(\s*[\w_]+:\s+)(.*?)(\s*)$')


def _needs_quoting(value: str) -> bool:
    """Return True if the value contains a YAML inline-comment trigger."""
    return ' #' in value or value.startswith('#')


def preprocess_yaml_text(text: str) -> str:
    """
    Scan YAML text and quote any unquoted field values that contain bare '#'.

    Rules applied per line:
    - Blank lines, document markers (--- / ...), and full-line comments are skipped.
    - Lines that do not match the "key: value" pattern are skipped (list items,
      block-scalar continuation lines, etc.).
    - Values already wrapped in single or double quotes are skipped.
    - Values containing ' #' or starting with '#' are wrapped in single quotes;
      any existing single quotes in the value are escaped as ''.

    Returns the preprocessed text, ready for yaml.safe_load_all().
    """
    lines = text.splitlines(keepends=True)
    result = []

    for line in lines:
        stripped = line.strip()

        # Skip blank lines, YAML document markers, and full-line comments
        if not stripped or stripped.startswith('#') or stripped in ('---', '...'):
            result.append(line)
            continue

        # Try to match a key: value line
        m = _KEY_VALUE_RE.match(line.rstrip('\n'))
        if m:
            key_part = m.group(1)
            value    = m.group(2)       # value without trailing whitespace
            trailing = '\n' if line.endswith('\n') else ''

            # Only act on non-empty, unquoted values
            if value and not (value.startswith("'") or value.startswith('"')):
                if _needs_quoting(value):
                    escaped = value.replace("'", "''")
                    result.append(f"{key_part}'{escaped}'{trailing}")
                    continue

        result.append(line)

    return ''.join(result)


def preprocess_yaml_file(yaml_path: str | Path, backup: bool = True) -> Path:
    """
    Pre-process a raw discovery YAML file, modifying it in place.

    Args:
        yaml_path: Path to the raw discovery YAML file.
        backup:    If True (default), write a .yaml.bak copy before modifying.

    Returns:
        Path to the (now-clean) YAML file.

    Raises:
        FileNotFoundError: If yaml_path does not exist.
    """
    yaml_path = Path(yaml_path)
    if not yaml_path.exists():
        raise FileNotFoundError(f"YAML file not found: {yaml_path}")

    original_text = yaml_path.read_text(encoding='utf-8')
    clean_text    = preprocess_yaml_text(original_text)

    if clean_text == original_text:
        # No bare-# values found; file unchanged
        return yaml_path

    if backup:
        backup_path = yaml_path.with_suffix('.yaml.bak')
        shutil.copy2(yaml_path, backup_path)
        print(f"Backup written: {backup_path}")

    yaml_path.write_text(clean_text, encoding='utf-8')
    print(f"Preprocessed:  {yaml_path}")
    return yaml_path


# ---------------------------------------------------------------------------
# Self-test (run as: python utilities/na_yaml_preprocess.py)
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    import yaml

    print("Running na_yaml_preprocess self-test...\n")

    # --- Line-level quoting tests ---
    LINE_TESTS = [
        # (description, raw_line, expected_line)
        (
            "Space-hash in value → quoted",
            "  features_raw: Pavilion #1; Shelter\n",
            "  features_raw: 'Pavilion #1; Shelter'\n",
        ),
        (
            "No # in value → unchanged",
            "  name: Elm Street Park\n",
            "  name: Elm Street Park\n",
        ),
        (
            "Already single-quoted → unchanged",
            "  notes: '# already quoted'\n",
            "  notes: '# already quoted'\n",
        ),
        (
            "Already double-quoted → unchanged",
            '  name: "Park #2 (East)"\n',
            '  name: "Park #2 (East)"\n',
        ),
        (
            "Mid-value # with space → quoted",
            "  description: Park #2 has a lot\n",
            "  description: 'Park #2 has a lot'\n",
        ),
        (
            "Full-line comment → unchanged",
            "# This is a comment line\n",
            "# This is a comment line\n",
        ),
        (
            "Document separator → unchanged",
            "---\n",
            "---\n",
        ),
        (
            "No # at all → unchanged",
            "  governance_raw: City of Columbus\n",
            "  governance_raw: City of Columbus\n",
        ),
        (
            "Internal single quote with # → escaped",
            "  features_raw: Shelter #'s 1 and 2\n",
            "  features_raw: 'Shelter #''s 1 and 2'\n",
        ),
        (
            "Inline # without preceding space → unchanged (not a comment trigger)",
            "  url_primary: https://example.com/park#section\n",
            "  url_primary: https://example.com/park#section\n",
        ),
    ]

    all_pass = True
    for desc, raw, expected in LINE_TESTS:
        result = preprocess_yaml_text(raw)
        if result == expected:
            print(f"  PASS  {desc}")
        else:
            print(f"  FAIL  {desc}")
            print(f"        Expected: {expected!r}")
            print(f"        Got:      {result!r}")
            all_pass = False

    # --- Round-trip YAML parse test ---
    SAMPLE_YAML = """\
---
entity_type: site
name: Elm Street Park
features_raw: Pavilion #1; Shelter #3
notes: Site # referenced by IMP-089
---
entity_type: site
name: Normal Park
features_raw: Picnic Shelter; Playground
notes: ''
"""
    clean   = preprocess_yaml_text(SAMPLE_YAML)
    records = list(yaml.safe_load_all(clean))

    checks = [
        (records[0]['features_raw'] == 'Pavilion #1; Shelter #3',
         "Round-trip: features_raw with two # values"),
        (records[0]['notes'] == 'Site # referenced by IMP-089',
         "Round-trip: notes with # value"),
        (records[1]['features_raw'] == 'Picnic Shelter; Playground',
         "Round-trip: unaffected record unchanged"),
        (records[1]['notes'] == '',
         "Round-trip: empty-string value unchanged"),
    ]
    for passed, desc in checks:
        if passed:
            print(f"  PASS  {desc}")
        else:
            print(f"  FAIL  {desc}")
            all_pass = False

    print()
    print("All tests passed." if all_pass else "SOME TESTS FAILED.")
