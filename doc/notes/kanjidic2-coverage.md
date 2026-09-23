# KANJIDIC2 coverage, measured 2026-09-23

Source: `http://www.edrdg.org/kanjidic/kanjidic2.xml.gz`, downloaded today.
Uncompressed 15,641,823 bytes. Parsed with the standard library `xml.etree`.

| Measure | Value |
|---|---|
| Characters in file | 13,108 |
| With at least one `<meaning m_lang="fr">` | 2,066 |
| Jōyō (`<grade>` 1 to 8) | 2,136 |
| Jōyō with French | 1,987 (93%) |
| Jōyō without French | 149 |
| With a `<jlpt>` level | 2,230 |

## Fields the prototype uses

```xml
<literal>日</literal>
<misc><grade>1</grade><stroke_count>4</stroke_count><freq>1</freq><jlpt>4</jlpt></misc>
<reading r_type="ja_on">ニチ</reading>
<reading r_type="ja_kun">ひ</reading>
<meaning>day</meaning>
<meaning m_lang="fr">jour</meaning>
```

Note the JLPT levels in KANJIDIC2 are the old four-level scale (pre-2010).

## Romaji

`pykakasi` 2.3.0, Hepburn output, tested on kana readings:

```
にち -> nichi, ひ -> hi, び -> bi, か -> ka
```

Kun readings carry a `.` marking the okurigana boundary (e.g. `あ.かり`) and a
leading `-` for suffix readings. Strip both before conversion.

## Licence

EDRDG licence, which is Creative Commons Attribution-ShareAlike 4.0. Attribution
text required in any product. Included in the repo README.

## French translator

Alain Thierion authored the French meanings, added to KANJIDIC2 in 2008. Quality
is single-word dictionary glosses, adequate for flash cards.
