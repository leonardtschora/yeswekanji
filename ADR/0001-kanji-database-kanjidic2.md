# ADR 0001: Use KANJIDIC2 as the kanji database

Date: 2026-09-23. Status: Accepted.

## Context

The prototype needs, per kanji: the character, its readings in kana, a romaji
spelling, a French meaning, and enough metadata to build groups of ten. The brief
asks which database to use and whether phonetic data and French translations exist
or must be generated.

## Decision

Use **KANJIDIC2** from the EDRDG, downloaded as one XML file (15.6 MB, 13,108
characters) and reduced at build time to a small JSON the app reads.

Measured on the file downloaded today (see `doc/notes/kanjidic2-coverage.md`):

| Field | Coverage |
|---|---|
| Characters with a French meaning | 2,066 |
| Jōyō kanji (grade 1 to 8) | 2,136, of which 1,987 have French |
| Characters with a JLPT level | 2,230 |
| On and kun readings in kana | all |

Romaji is derived from the kana readings with `pykakasi` (Hepburn), tested today.

## Alternatives rejected

- **kanjiapi.dev / davidluzgouveia kanji-data / other JSON repackagings.** Same
  KANJIDIC2 data, English only. Using them would reintroduce the translation problem.
- **WaniKani, Jisho, Kanji Alive APIs.** API keys, rate limits, or no French. Slower.
- **Scraping a French kanji site.** Legal grey zone and fragile. No.

## Consequences

- No translation service needed for the prototype (ADR 0004).
- The 2,066 figure backs the "more than 2000 kanji" claim in the advert.
- Licence is CC BY-SA 4.0 via the EDRDG licence: attribution in the README and in
  the app's About text is mandatory. Already in the README.
- The raw XML is gitignored. The build script re-downloads it; the derived JSON is
  committed so the deployed app has no network dependency for data.
- Kanji "meanings" are single words, not sentences. Good enough for flash cards;
  vocabulary examples (JMdict) are a later feature.
