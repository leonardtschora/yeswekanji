# Yes we kanji

The app that helps you memorise Japanese kanji. Flexible exercises, your own
objectives, your own pace.

Status: **prototype, live at https://yeswekanji.streamlit.app/** (Streamlit Community Cloud, sleeps after 12 h idle).

## Run locally

```bash
uv venv .venv -p 3.12
uv pip install -p .venv/bin/python -r requirements.txt
.venv/bin/streamlit run app.py
```

Then open http://localhost:8501. The app only reads committed files
(`data/kanji.json`, `data/themes.json`, `data/audio/`); it makes no network calls.

## Rebuild the data

Build-time dependencies (gTTS, pykakasi) are in `requirements-dev.txt`.

```bash
uv pip install -p .venv/bin/python -r requirements-dev.txt
.venv/bin/python scripts/build_kanji.py      # downloads KANJIDIC2, writes data/kanji.json
.venv/bin/python scripts/validate_themes.py  # checks data/themes.json against it
.venv/bin/python scripts/build_audio.py      # gTTS, writes missing data/audio/u<hex>.mp3
```

Themes are hand-written in `data/themes.json`. After adding one, run the validator
then the audio script; existing audio files are skipped.

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
| `app.py`, `cards.py` | Streamlit app and its data helpers |
| `scripts/` | Data build scripts (KANJIDIC2 extract, theme check, audio) |
| `data/` | Generated `kanji.json`, curated `themes.json`, `audio/` MP3s |
| `.task.toml` | Config for `gh-task`; tasks live in GitHub Issues and the `yeswekanji` project board |

## Stack (decided, see ADR/)

- Data: KANJIDIC2 (EDRDG, CC BY-SA 4.0), French meanings included. ADR 0001, 0004.
- Voice: gTTS, audio pre-generated and committed. ADR 0003.
- Host: Streamlit Community Cloud. ADR 0005, 0006.

## Attribution

Kanji data comes from the [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project)
file, property of the Electronic Dictionary Research and Development Group, used
under the Group's [licence](https://www.edrdg.org/edrdg/licence.html)
(CC BY-SA 4.0). French meanings by Alain Thierion, part of KANJIDIC2.
Audio in `data/audio/` was generated with [gTTS](https://github.com/pndurette/gTTS).
