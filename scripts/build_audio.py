"""Generate one MP3 per themed kanji: French label, pause, Japanese reading.

ADR 0003 / 0006. For every kanji in data/themes.json:
  1. gTTS(lang="fr") speaks the French label (first two French meanings,
     "radical ..." notes skipped, joined by ", "; see cards.french_label).
  2. A 0.6 s pause.
  3. gTTS(lang="ja") speaks the kana reading (first kun reading with '.'
     and '-' removed, else the first on reading; see cards.spoken_reading).
Output: data/audio/u<codepoint hex>.mp3 (e.g. u65e5.mp3 for 日).

How the clips are joined, without ffmpeg or pydub: an MP3 file is a plain
sequence of independent frames, so byte concatenation of two gTTS clips is a
valid MP3 that browsers play straight through. gTTS returns ID3-less
MPEG-2 Layer III, 24 kHz, 64 kbit/s, mono (192-byte frames of 24 ms). The
pause is made of synthetic silent frames: the clip's own 4-byte frame header
(padding bit cleared) followed by zero bytes. All-zero side information means
part2_3_length = 0 and global_gain = 0, which decoders render as silence;
gTTS itself starts each clip with exactly such a frame. The frame size is
computed from the header, so a format change in gTTS still yields a valid
gap; if the header cannot be parsed the script falls back to plain
concatenation and says so.

Idempotent: existing files are skipped (delete one to regenerate it).
Sleeps 0.3 s between gTTS calls; a failed call is retried once after 5 s.

Run from the repository root:  python scripts/build_audio.py
Build-time deps: requirements-dev.txt.
"""

from __future__ import annotations

import io
import sys
import time
from pathlib import Path

from gtts import gTTS

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cards import AUDIO_DIR, audio_path, french_label, load_kanji, load_themes, spoken_reading  # noqa: E402

PAUSE_S = 0.6
SLEEP_S = 0.3
RETRY_S = 5.0

# Layer III bitrates (kbit/s) by index, and sample rates (Hz) by version.
_BITRATES = {
    "1": [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],
    "2": [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],
}
_RATES = {3: ("1", [44100, 48000, 32000]), 2: ("2", [22050, 24000, 16000]), 0: ("2", [11025, 12000, 8000])}


def tts(text: str, lang: str) -> bytes:
    for attempt in (1, 2):
        try:
            buf = io.BytesIO()
            gTTS(text, lang=lang).write_to_fp(buf)
            time.sleep(SLEEP_S)
            return buf.getvalue()
        except Exception as exc:  # gTTS raises gTTSError or requests errors
            if attempt == 2:
                raise
            print(f"   gTTS {lang} failed ({exc}); retrying in {RETRY_S:.0f} s")
            time.sleep(RETRY_S)
    raise AssertionError("unreachable")


def strip_id3(mp3: bytes) -> bytes:
    """Remove a leading ID3v2 tag so it does not end up mid-stream."""
    if mp3[:3] == b"ID3" and len(mp3) > 10:
        size = (mp3[6] << 21) | (mp3[7] << 14) | (mp3[8] << 7) | mp3[9]
        return mp3[10 + size :]
    return mp3


def silence(like: bytes, seconds: float) -> bytes:
    """Silent Layer III frames matching the format of the clip `like`."""
    h = like[:4]
    if len(h) < 4 or h[0] != 0xFF or (h[1] & 0xE0) != 0xE0 or ((h[1] >> 1) & 3) != 1:
        return b""  # not a Layer III frame header: fall back to no gap
    version_bits = (h[1] >> 3) & 3
    if version_bits not in _RATES:
        return b""
    version, rates = _RATES[version_bits]
    br_idx, sr_idx = h[2] >> 4, (h[2] >> 2) & 3
    if br_idx in (0, 15) or sr_idx == 3:
        return b""
    bitrate = _BITRATES[version][br_idx] * 1000
    rate = rates[sr_idx]
    coeff, samples = (144, 1152) if version == "1" else (72, 576)
    frame_len = coeff * bitrate // rate
    header = bytes([0xFF, h[1] | 0x01, h[2] & ~0x02 & 0xFF, h[3]])  # no CRC, no padding
    n_frames = round(seconds * rate / samples)
    return (header + bytes(frame_len - 4)) * n_frames


def main() -> int:
    kanji = load_kanji()
    themes = load_themes()
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    made = skipped = 0
    fallback: list[str] = []
    for theme in themes:
        for literal in theme["kanji"]:
            out = audio_path(literal)
            if out.exists():
                skipped += 1
                continue
            k = kanji[literal]
            fr_text, ja_text = french_label(k), spoken_reading(k)
            print(f"{literal} {out.name}: fr='{fr_text}' ja='{ja_text}'")
            fr = strip_id3(tts(fr_text, "fr"))
            ja = strip_id3(tts(ja_text, "ja"))
            gap = silence(fr, PAUSE_S)
            if not gap:
                fallback.append(literal)
            out.write_bytes(fr + gap + ja)
            made += 1
    files = sorted(AUDIO_DIR.glob("u*.mp3"))
    total = sum(f.stat().st_size for f in files)
    print(f"Generated {made}, skipped {skipped}. {len(files)} files, {total / 1e6:.2f} MB in {AUDIO_DIR}")
    if fallback:
        print(f"WARNING: no silent gap (unknown MP3 header) for: {''.join(fallback)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
