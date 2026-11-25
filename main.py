#!/usr/bin/env python3
"""One-Line Office Jokes — writes one single-line joke about office life.

The program is deterministic: it always writes the same line, a joke that
turns on a real office detail (the printer) and lands its laugh in the
last few words. Pure standard library, no network, no input.
"""

import os

JOKE = (
    "Our office printer only jams when the document is urgent, "
    "confidential, and due in five minutes \u2014 it\u2019s the most "
    "reliable employee we have."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of gate range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
