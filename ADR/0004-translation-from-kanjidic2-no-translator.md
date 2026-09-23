# ADR 0004: French comes from KANJIDIC2, no translation service

Date: 2026-09-23. Status: Accepted.

## Context

The brief plans a fallback to Linguee or Google Translate when French is missing.

## Decision

Do not connect a translator. Restrict the prototype's themes (ADR 0002) to the
1,987 jōyō kanji that already carry a French meaning in KANJIDIC2. Where a kanji
has several French meanings, the card shows the first two.

## Alternatives rejected

- **Google Translate / DeepL API.** Account, key, quota, and a single-word
  translation without context is often wrong (行 as "go" vs "line" vs "bank").
- **Linguee.** No public API; scraping is against its terms.
- **LLM translation at build time.** Viable and cheap, but unnecessary today since
  coverage is 93% of jōyō. Noted as the fix for the 149 missing ones later.

## Consequences

- Zero external services in the whole prototype.
- The 149 jōyō kanji without French are excluded from themes for now. A list is
  easy to produce from the build script when needed.
