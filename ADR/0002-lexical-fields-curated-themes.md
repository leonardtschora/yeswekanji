# ADR 0002: Lexical fields are hand-curated theme lists

Date: 2026-09-23. Status: Accepted.

## Context

The one feature is "ten kanji cards with lexical field similarities". KANJIDIC2
has no semantic grouping. It has grade, JLPT level, frequency rank and radical,
none of which is a lexical field (radical 72 "sun" groups 日 with 時 and 曜, but
also with 暇 and 昔).

## Decision

Ship a hand-written `data/themes.json`: about ten themes, ten kanji each, all
taken from the jōyō set with French meanings. Suggested first themes: numbers,
nature, body, family, time, directions, colours, school, food, verbs of motion.
The app picks a theme at random or lets the user pick one.

The list is written by the agent in the build task and checked against
KANJIDIC2 so that every kanji has readings and a French meaning.

## Alternatives rejected

- **Cluster on French meanings with embeddings.** Correct long-term answer, half a
  day of work, and needs quality review anyway. Later.
- **Group by radical or grade.** Available for free but not a lexical field, so it
  would misrepresent the feature.
- **Reuse WaniKani or Genki chapter lists.** Copyright of the curriculum.

## Consequences

- Ten themes cover 100 kanji. The rest of the 2,000 stay in the database, unused
  by this feature until grouping is automated.
- Themes are data, not code. Adding one is a JSON edit.
