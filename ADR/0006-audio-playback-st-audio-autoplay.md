# ADR 0006: Audio playback through st.audio(autoplay=True)

Date: 2026-09-23. Status: Accepted.

## Context

Flipping a card must play audio without a second click. Streamlit reruns the
script on each click, so the audio element is created during a rerun.

## Decision

On flip, render `st.audio(path, format="audio/mp3", autoplay=True)` for that card
only, once, keyed on the card. Streamlit has supported `autoplay` since April 2024
(1.34); the current release is 1.64. Browsers allow autoplay after the user has
interacted with the page, and the card click is that interaction.

## Alternatives rejected

- **Inject `<audio autoplay>` through `st.components.v1.html`.** Works, but it is
  an iframe, so autoplay policy is stricter and styling is fiddly. Fallback if
  `st.audio` misbehaves.
- **Web Speech API from a component.** Rejected with the voice decision (ADR 0003).

## Consequences

- One combined MP3 per kanji (French, pause, Japanese) avoids sequencing two
  players. Generated at build time (ADR 0003).
- Known issue: two `st.audio(autoplay=True)` calls with identical arguments raise a
  duplicate-widget error (streamlit issue 11360). Rendering the player only for the
  card just flipped sidesteps it.
- Safari on iOS: verified 2026-09-23, autoplay works on flip. Visible player
  controls remain as fallback.
