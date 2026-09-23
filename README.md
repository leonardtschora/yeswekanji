# Yes we kanji

The app that helps you memorise Japanese kanji. Flexible exercises, your own
objectives, your own pace.

Status: **prototype, not yet built**. This repository currently holds the idea,
the architecture decisions and the task plan. Code lands next.

## The prototype (one feature)

Ten cards from one lexical field, kanji face up. Click a card: it flips and shows
the kanji, its romaji reading, its French meaning, and plays the French then the
Japanese out loud.

## Where things are

| Path | What |
|---|---|
| `input/idea.md` | The original brief, verbatim |
| `ADR/` | Architecture decisions, one file each, with the alternatives rejected |
| `doc/reports/` | One page per work session |
| `doc/notes/` | Supporting research the reports and ADRs cite |
| `.task.toml` | Config for `gh-task`; tasks live in GitHub Issues and the `yeswekanji` project board |

## Stack (decided, see ADR/)

- Data: KANJIDIC2 (EDRDG, CC BY-SA 4.0), French meanings included. ADR 0001, 0004.
- Voice: gTTS, audio pre-generated and committed. ADR 0003.
- Host: Streamlit Community Cloud. ADR 0005, 0006.

## Attribution

Kanji data comes from the [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project)
file, property of the Electronic Dictionary Research and Development Group, used
under the Group's [licence](https://www.edrdg.org/edrdg/licence.html).
