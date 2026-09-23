# Smoke test, 2026-09-23 (S6)

App: https://yeswekanji.streamlit.app/. Tester: the repo owner. Check: flip cards,
audio plays French then Japanese without a second tap.

| Device | Browser | Result |
|---|---|---|
| Ubuntu desktop | Chrome | OK |
| Ubuntu desktop | Firefox | OK |
| Android phone | Firefox | OK |
| iPhone | Safari | OK, autoplay worked on flip |

No fixes needed. The iOS autoplay risk noted in ADR 0006 did not materialise.
