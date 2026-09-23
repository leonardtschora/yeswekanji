"""Validate data/themes.json against data/kanji.json (ADR 0002, 0004).

Checks: every theme has an id, French and English names, exactly 10 kanji;
every kanji exists in kanji.json (so it is joyo and has a French meaning and
readings); no kanji appears twice across themes; theme ids are unique.
Exits 1 and lists the problems on failure.

Run from the repository root:  python scripts/validate_themes.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KANJI = ROOT / "data" / "kanji.json"
THEMES = ROOT / "data" / "themes.json"
PER_THEME = 10


def validate(themes: list[dict], kanji: dict) -> list[str]:
    errors: list[str] = []
    ids = Counter(t.get("id") for t in themes)
    errors += [f"duplicate theme id: {i}" for i, n in ids.items() if n > 1]
    seen: Counter[str] = Counter()
    for t in themes:
        tid = t.get("id", "?")
        for key in ("id", "name_fr", "name_en", "kanji"):
            if not t.get(key):
                errors.append(f"{tid}: missing {key}")
        chars = t.get("kanji", [])
        if len(chars) != PER_THEME:
            errors.append(f"{tid}: {len(chars)} kanji, expected {PER_THEME}")
        for c in chars:
            seen[c] += 1
            k = kanji.get(c)
            if k is None:
                errors.append(f"{tid}: {c} not in kanji.json")
            elif not (k["kun"] or k["on"]):
                errors.append(f"{tid}: {c} has no reading")
    errors += [f"{c} appears in {n} themes" for c, n in seen.items() if n > 1]
    return errors


def main() -> int:
    kanji = json.loads(KANJI.read_text(encoding="utf-8"))
    themes = json.loads(THEMES.read_text(encoding="utf-8"))
    errors = validate(themes, kanji)
    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for e in errors:
            print(" -", e)
        return 1
    total = sum(len(t["kanji"]) for t in themes)
    print(f"OK: {len(themes)} themes, {total} distinct kanji, all in kanji.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
