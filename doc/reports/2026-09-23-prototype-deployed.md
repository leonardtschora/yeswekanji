# Session report, 2026-09-23: prototype deployed

Same day as kick-off. Live at https://yeswekanji.streamlit.app/.

## Done

- **S1** `scripts/build_kanji.py`: KANJIDIC2 to `data/kanji.json`. 1,987 jōyō kanji
  with French, kana and Hepburn romaji. 5.5 s including download.
- **S2** `data/themes.json`: 10 themes x 10 kanji (numbers, nature, body, family,
  time, directions, colours, school, food, motion). `scripts/validate_themes.py` passes.
- **S3** `scripts/build_audio.py`: 100 MP3s, French, 0.6 s hand-built silence,
  Japanese. 2.4 MB committed. No ffmpeg.
- **S4** `app.py`: theme picker, 5x2 grid, flip in session_state, one autoplaying
  `st.audio` per flip, About expander with EDRDG attribution.
- **S5** Deployed by the owner on Streamlit Community Cloud from `main`.
- **S6** Smoke test passed on Ubuntu Chrome and Firefox, Android Firefox, iPhone
  Safari. `doc/notes/smoke-test-2026-09-23.md`.
- **S7** Dropped: attribution shipped inside S4.

Effort: one agent run of about 7.5 minutes wall-clock for S1 to S4, plus the
owner's deploy and phone tests. The 4.5 h estimate was an upper bound.

## Decisions confirmed

All six ADRs held. ADR 0006's iOS autoplay risk did not show up.

## Known rough edges (data, not code)

- First-kun-reading rule picks rare readings for 銀 (しろがね), 肉 (しし), 金 (かね).
- 米 shows "Amérique" as second meaning. 乗 label contains a parenthesis gTTS
  reads awkwardly.
- Commits for S1 to S4 carry an Opus co-author trailer.

## Next candidates

- Per-kanji reading override in `themes.json` to fix the rare readings.
- Automated lexical grouping (ADR 0002 alternative) to use the other 1,887 kanji.
- Static GitHub Pages port if the Streamlit rerun flip feels slow.
