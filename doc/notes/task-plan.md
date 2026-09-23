# Task plan for the prototype

Estimates are agent hours. Human time is noted separately. Sections (S1...) are
what GitHub issues reference through `--plan`.

| § | Task | Agent | Human | Depends on |
|---|---|---|---|---|
| S1 | Build script: download KANJIDIC2, extract jōyō with French, add romaji, write `data/kanji.json` | 1 h | | |
| S2 | Curate `data/themes.json`: 10 themes x 10 kanji, validated against S1 output | 30 min | 10 min review | S1 |
| S3 | Audio script: gTTS French + pause + Japanese into one MP3 per kanji, commit `data/audio/` | 30 min | | S2 |
| S4 | Streamlit app: theme picker, 5x2 card grid, flip in session_state, reveal romaji + French, `st.audio` autoplay | 1.5 h | | S2, S3 |
| S5 | Deploy to Streamlit Community Cloud, add URL to README | 15 min | 5 min account link | S4 |
| S6 | Smoke test on desktop Chrome, Android, iOS Safari; fix autoplay fallbacks | 30 min | 15 min on phones | S5 |
| S8 | Session report and ADR updates after deploy | 15 min | | S6 |
| | **Total** | **~4.5 h** | **~30 min** | |

Realistic calendar: one working session, deployed the same day, if the human
links the Streamlit account when asked.

S7 dropped on 2026-09-23: attribution already lives in the app's About expander and the README.
