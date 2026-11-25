#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Runs with no arguments, exits 0, and writes the monologue (exactly
100 words) to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output/entry.txt),
printing it to stdout as well. Fully deterministic: no network, no clock,
no randomness.
"""

import os

MONOLOGUE = (
    "Listen. I did not choose the skull throne, the lava moat, or the "
    "screaming. I inherited them, along with the cursed sword, the tax "
    "ledgers, and a minion union that files grievances in triplicate. Six "
    "hundred years I have conquered kingdoms before breakfast, and not "
    "once has anyone asked how I slept. Badly. On a throne. My back is "
    "ruined, my cape smells of smoke, and the prophecy, oh, the prophecy, "
    "promised a hero would end me. Please. Hurry. I have a nap, a ritual "
    "at noon, and no will left to monologue. Kneel, or don't. I no longer "
    "care."
)

WORD_COUNT = 100


def main():
    words = MONOLOGUE.split()
    assert len(words) == WORD_COUNT, (
        "monologue must be exactly %d words, got %d" % (WORD_COUNT, len(words))
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE + "\n")
    print(MONOLOGUE)


if __name__ == "__main__":
    main()
