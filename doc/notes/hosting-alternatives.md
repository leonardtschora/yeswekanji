# Hosting alternatives compared, 2026-09-23

Criterion: time from a working `app.py` to a public URL, for an app whose only
input is clicks and whose only output is text and audio.

| Option | Time to first URL | Audio | Cost | Verdict |
|---|---|---|---|---|
| Streamlit Community Cloud | 10 min after account link | `st.audio(autoplay=True)` | free | **Chosen** (ADR 0005) |
| Gradio on Hugging Face Spaces | 10 min | `gr.Audio(autoplay=True)` | free | Equivalent, different stack |
| Static HTML on GitHub Pages | 5 min | `<audio>` tag, full control | free | Fastest and best UX; no Python at runtime, so build pipeline outputs JSON + MP3 and page is vanilla JS |
| NiceGUI / Reflex | needs a server (Fly, Render) | yes | free tier | Nicer UI, more moving parts |
| Render / Railway / Fly free tier | 20 min, Dockerfile | yes | free with sleep | Same sleep behaviour as Streamlit Cloud, one more account |
| OVH VPS | half a day | yes | ~4 EUR/month | See ovh-path-estimate.md |

## Streamlit Community Cloud limits that matter

- Public GitHub repo required.
- About 1 GB RAM, shared CPU.
- Sleeps after 12 hours without a visitor; a wake button appears.
- At most five redeploys per minute from GitHub pushes.
- No custom domain.

## Why not static right away

It would work, and the flip animation would be a CSS transform instead of a
Streamlit rerun. The brief asks for Streamlit and the data prep is Python. If
the Streamlit UI feels clunky in the smoke test, moving to static costs about
two hours because data and audio are already static files.
