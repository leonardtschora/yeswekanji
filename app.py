"""Yes we kanji: ten kanji cards from one lexical field. Click to flip.

Run:  streamlit run app.py
Decisions: ADR/0005 (Streamlit), ADR/0006 (st.audio autoplay).
"""

from __future__ import annotations

import html
import random

import streamlit as st

import cards

st.set_page_config(page_title="Yes we kanji", page_icon="漢", layout="wide")

COLUMNS = 5

CSS = """
<style>
.st-key-grid div.stButton button {
    min-height: 13rem;
    border-radius: 0.8rem;
}
.st-key-grid div.stButton button p {
    font-size: 4.5rem;
    line-height: 1.1;
}
.ywk-card { text-align: center; min-height: 11rem; display: flex;
    flex-direction: column; justify-content: center; gap: 0.25rem; }
.ywk-kanji { font-size: 3.2rem; line-height: 1.1; }
.ywk-romaji { font-size: 1.05rem; font-weight: 600; }
.ywk-fr { font-size: 1.1rem; }
.ywk-kana { font-size: 0.85rem; opacity: 0.55; }
</style>
"""


@st.cache_data
def get_kanji() -> dict[str, dict]:
    return cards.load_kanji()


@st.cache_data
def get_themes() -> list[dict]:
    return cards.load_themes()


def new_draw() -> None:
    """Hide every card again and shuffle the order of the current theme."""
    st.session_state.flipped = {}
    st.session_state.last_flipped = None
    st.session_state.order_seed = random.random()


def flip(literal: str) -> None:
    st.session_state.flipped[literal] = True
    st.session_state.last_flipped = literal


def card_html(k: dict) -> str:
    e = html.escape
    return (
        '<div class="ywk-card">'
        f'<div class="ywk-kanji">{e(k["literal"])}</div>'
        f'<div class="ywk-romaji">{e(cards.romaji_line(k))}</div>'
        f'<div class="ywk-fr">{e(", ".join(cards.french_meanings(k)))}</div>'
        f'<div class="ywk-kana">{e(cards.kana_line(k))}</div>'
        "</div>"
    )


def main() -> None:
    kanji = get_kanji()
    themes = {t["id"]: t for t in get_themes()}

    if "theme_id" not in st.session_state:
        st.session_state.theme_id = random.choice(list(themes))
        new_draw()

    st.markdown(CSS, unsafe_allow_html=True)
    st.title("Yes we kanji")

    pick, reset = st.columns([3, 1], vertical_alignment="bottom")
    with pick:
        st.selectbox(
            "Thème",
            options=list(themes),
            format_func=lambda tid: themes[tid]["name_fr"],
            key="theme_id",
            on_change=new_draw,
        )
    with reset:
        st.button("Nouveau tirage", on_click=new_draw, width="stretch")

    theme = themes[st.session_state.theme_id]
    order = list(theme["kanji"])
    random.Random(st.session_state.order_seed).shuffle(order)
    st.caption(f"{theme['name_fr']} · {theme['name_en']} — cliquez sur une carte pour la retourner.")

    to_play = st.session_state.last_flipped
    with st.container(key="grid"):
        for start in range(0, len(order), COLUMNS):
            for col, literal in zip(st.columns(COLUMNS), order[start : start + COLUMNS]):
                with col:
                    if not st.session_state.flipped.get(literal):
                        st.button(literal, key=f"card_{literal}", on_click=flip, args=(literal,), width="stretch")
                        continue
                    with st.container(border=True):
                        st.markdown(card_html(kanji[literal]), unsafe_allow_html=True)
                        if literal == to_play:
                            # Rendered for the card just flipped only, once: avoids the
                            # duplicate-widget error (streamlit#11360). The visible player
                            # stays as a fallback where autoplay is blocked (iOS Safari).
                            st.audio(str(cards.audio_path(literal)), format="audio/mp3", autoplay=True)
    st.session_state.last_flipped = None

    with st.expander("À propos"):
        st.markdown(
            "Données kanji : fichier [KANJIDIC2](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project), "
            "propriété de l'Electronic Dictionary Research and Development Group (EDRDG), utilisé "
            "conformément à la [licence du groupe](https://www.edrdg.org/edrdg/licence.html) "
            "(Creative Commons Attribution-ShareAlike 4.0). Significations françaises de "
            "KANJIDIC2 (Alain Thierion).\n\n"
            "Voix : synthèse générée à l'avance avec [gTTS](https://github.com/pndurette/gTTS) "
            "(Google Translate text-to-speech).\n\n"
            "Romaji : [pykakasi](https://codeberg.org/miurahr/pykakasi), transcription Hepburn."
        )


main()
