"""Build data/kanji.json from KANJIDIC2 (ADR 0001, 0004).

Downloads kanjidic2.xml.gz into data/raw/ if absent, keeps the joyo kanji
(grade 1 to 8) that have at least one French meaning, adds Hepburn romaji
with pykakasi, and writes data/kanji.json keyed by the character.

Run from the repository root:  python scripts/build_kanji.py
Build-time deps: requirements-dev.txt.
"""

from __future__ import annotations

import gzip
import json
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import pykakasi

URL = "http://www.edrdg.org/kanjidic/kanjidic2.xml.gz"
ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "kanjidic2.xml.gz"
OUT = ROOT / "data" / "kanji.json"

_kks = pykakasi.kakasi()


def download() -> None:
    if RAW.exists():
        print(f"Using cached {RAW.relative_to(ROOT)}")
        return
    RAW.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading {URL} ...")
    tmp = RAW.with_suffix(".part")
    urllib.request.urlretrieve(URL, tmp)
    tmp.rename(RAW)


def clean_kana(reading: str) -> str:
    """Strip the suffix marker '-' and the okurigana marker '.'."""
    return reading.replace("-", "").replace(".", "")


def to_romaji(kana: str) -> str:
    return "".join(item["hepburn"] for item in _kks.convert(clean_kana(kana)))


def _int_or_none(el: ET.Element | None) -> int | None:
    return int(el.text) if el is not None and el.text else None


def parse() -> tuple[dict, int]:
    kanji: dict[str, dict] = {}
    total = 0
    with gzip.open(RAW, "rb") as fh:
        root = ET.parse(fh).getroot()
    for ch in root.iter("character"):
        total += 1
        misc = ch.find("misc")
        grade = _int_or_none(misc.find("grade"))
        if grade is None or not 1 <= grade <= 8:
            continue
        on, kun, fr, en = [], [], [], []
        rm = ch.find("reading_meaning")
        if rm is not None:
            for group in rm.iter("rmgroup"):
                for r in group.findall("reading"):
                    if r.get("r_type") == "ja_on":
                        on.append(r.text)
                    elif r.get("r_type") == "ja_kun":
                        kun.append(r.text)
                for m in group.findall("meaning"):
                    lang = m.get("m_lang")
                    if lang is None:
                        en.append(m.text)
                    elif lang == "fr":
                        fr.append(m.text)
        if not fr:
            continue
        literal = ch.findtext("literal")
        kanji[literal] = {
            "literal": literal,
            "grade": grade,
            "jlpt": _int_or_none(misc.find("jlpt")),
            "freq": _int_or_none(misc.find("freq")),
            "stroke_count": _int_or_none(misc.find("stroke_count")),
            "on": on,
            "kun": kun,
            "romaji_on": [to_romaji(r) for r in on],
            "romaji_kun": [to_romaji(r) for r in kun],
            "meanings_fr": fr,
            "meanings_en": en,
        }
    return kanji, total


def main() -> int:
    start = time.time()
    download()
    kanji, total = parse()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8") as fh:
        json.dump(kanji, fh, ensure_ascii=False, indent=1, sort_keys=True)
        fh.write("\n")
    no_kun = sum(1 for k in kanji.values() if not k["kun"])
    print(f"Characters in file: {total}")
    print(f"Kept (grade 1-8 with French): {len(kanji)}")
    print(f"  without kun reading: {no_kun}")
    print(f"  with JLPT level: {sum(1 for k in kanji.values() if k['jlpt'])}")
    print(f"Wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes) in {time.time() - start:.1f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
