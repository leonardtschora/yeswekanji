# ADR 0005: Host on Streamlit Community Cloud

Date: 2026-09-23. Status: Accepted.

## Context

Interaction is one click per card plus audio output. The brief asks: can this run
on Streamlit, what similar alternatives exist, and how long an OVH server would
take. The metric is time to deploy.

## Decision

Build the app in **Streamlit** and deploy on **Streamlit Community Cloud**, from
this public GitHub repository. Deploy is a form on share.streamlit.io: pick repo,
branch, `app.py`. Redeploys happen on push.

Answers to the brief's three questions:

1. **Can this be on Streamlit?** Yes. Cards are buttons in a column grid, flip
   state lives in `st.session_state`, and audio plays through `st.audio` (ADR 0006).
2. **Alternatives similar to Streamlit.** Gradio on Hugging Face Spaces is the
   closest and equally fast; NiceGUI and Reflex are nicer for custom UI but need a
   server you run. A plain static page on GitHub Pages is the cheapest of all and
   would also work here since data and audio are static files. Details in
   `doc/notes/hosting-alternatives.md`.
3. **OVH path.** About half a day of agent time plus DNS waits. Estimate in
   `doc/notes/ovh-path-estimate.md`. Not for the prototype.

## Alternatives rejected

- **Static site on GitHub Pages.** Genuinely as fast, and better long-term for a
  click-only app. Rejected only because the brief prefers Python/Streamlit and the
  data pipeline is Python anyway. Revisit when the flip animation matters.
- **Gradio on HF Spaces.** Equivalent. No reason to switch stacks.
- **OVH VPS + Docker.** Half a day and ongoing ops for zero prototype benefit.
- **Render / Fly / Railway free tiers.** Fine, but one more account to set up
  and no advantage over Streamlit's own cloud for a Streamlit app.

## Consequences

- Free. Public repo required, which this is.
- App sleeps after 12 h idle and shows a wake-up page. Acceptable for a demo.
- Roughly 1 GB RAM, shared CPU. The app holds 100 cards; irrelevant.
- No custom domain on the free tier. Fine for now.
- A human step remains: linking the GitHub account on share.streamlit.io the first
  time. About five minutes.
