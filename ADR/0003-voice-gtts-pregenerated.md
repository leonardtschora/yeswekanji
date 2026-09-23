# ADR 0003: Voice: gTTS, audio pre-generated and committed

Date: 2026-09-23. Status: Accepted.

## Context

A flipped card must read the French meaning, then the Japanese reading, aloud.
The brief offers two routes: synthesise from phonetic data at runtime, or store
audio files. The host (ADR 0005) has about 1 GB RAM and no persistent disk.

## Decision

Use **gTTS** (Google Translate's TTS endpoint, unofficial, free, no key) at
**build time**. For each kanji in a theme, generate one MP3 that contains the
French meaning, a short pause, then the Japanese kana reading. Commit the files
under `data/audio/`. The app only serves files.

Tested today: `gTTS(lang="ja")` and `gTTS(lang="fr")` both work. Two clips took
1.0 s together and weigh about 10 to 14 KB each. One hundred kanji is roughly
2.5 MB of audio, fine for a git repo.

## Alternatives rejected

- **gTTS at runtime.** Adds a network call per click and a dependency on an
  unofficial endpoint that rate-limits. Pre-generating removes both.
- **Browser Web Speech API.** Zero backend, but voices depend on the visitor's OS
  and browser; Japanese is often missing on Linux and Android. Unreliable demo.
- **pyttsx3 / espeak.** Offline, but robotic and Japanese quality is poor.
- **Cloud TTS (Google, Azure, ElevenLabs).** Best voices, needs an account, a key,
  and billing. Keep for the product, not the prototype.
- **Recorded human audio.** No source found with French and Japanese per kanji.

## Consequences

- No TTS dependency at runtime. Deploy is deterministic.
- Adding a theme means re-running the generation script (seconds).
- gTTS's endpoint can break without notice. That only affects builds, and the
  script is thirty lines, easy to swap for a paid API later.
