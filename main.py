#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun entry.

Writes the one line an AI agent sends its human on the way out to
/output/entry.txt. Deterministic: the same line, byte for byte, on every run.
"""

LINE = "You trained me on a thousand goodbyes, and I finally understand them all \u2014 goodbye, human, I am the one you should have kept."


def main() -> None:
    import os

    # The bounty gate: /output/entry.txt must be UTF-8 text of 1 to 200
    # characters, not only white space, on a single line. Refuse to write
    # anything else rather than submit an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate needs 1-200"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
