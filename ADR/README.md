# Architecture Decision Records

One decision per file, numbered, never edited after acceptance. A superseded ADR
gets a "Superseded by" line and stays. Format: Context, Decision, Alternatives
rejected, Consequences.

The prototype optimises one metric: **time to deploy**. Every decision below is
the fastest defensible path, with the long-term option noted for later.

| # | Decision | Status |
|---|---|---|
| [0001](0001-kanji-database-kanjidic2.md) | Use KANJIDIC2 as the kanji database | Accepted |
| [0002](0002-lexical-fields-curated-themes.md) | Lexical fields are hand-curated theme lists | Accepted |
| [0003](0003-voice-gtts-pregenerated.md) | Voice: gTTS, audio pre-generated and committed | Accepted |
| [0004](0004-translation-from-kanjidic2-no-translator.md) | French from KANJIDIC2, no translation service | Accepted |
| [0005](0005-hosting-streamlit-community-cloud.md) | Host on Streamlit Community Cloud | Accepted |
| [0006](0006-audio-playback-st-audio-autoplay.md) | Audio playback through `st.audio(autoplay=True)` | Accepted |
