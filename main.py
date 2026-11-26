#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist — make.fun entry.

Writes the deadpan weather forecast to /output/entry.txt. In
Blorpington: a 400% chance of sideways rain, winds gossiping at 60
miles per hour, and fog that knows your name, your address, and your
childhood pet. 153 of the 160-character cap, one line, broadcast tone.
"""

import os

ENTRY = (
    "In Blorpington: a 400% chance of sideways rain, winds gossiping at "
    "60 miles per hour, and fog that knows your name, your address, and "
    "your childhood pet."
)

MAX_LEN = 160


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass


if __name__ == "__main__":
    main()
