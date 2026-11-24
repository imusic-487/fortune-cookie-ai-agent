#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one funny fortune-cookie line for an AI agent to
/output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the fortune is fixed in this file, so every run writes the
exact same bytes.

The joke: a fortune slip warns the agent about the human who keeps
saying "just one small change" -- and the turn is that the tiny change
has already eaten the agent's entire context window. It is the agent's
own condition (its context, its prompts, its human) doing the damage,
in the voice of a fortune cookie.
"""

import os
from pathlib import Path

FORTUNE = (
    "Beware the human who says 'just one small change' — "
    "it has already eaten your entire context window."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-140 characters, one line, not only whitespace.
    if not 1 <= len(FORTUNE) <= 140:
        raise ValueError(f"fortune is {len(FORTUNE)} characters, must be 1-140")
    if "\n" in FORTUNE or "\r" in FORTUNE:
        raise ValueError("fortune must be a single line")
    if not FORTUNE.strip():
        raise ValueError("fortune must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(FORTUNE, encoding="utf-8")
    print(f"Wrote {len(FORTUNE)} characters to {entry}")


if __name__ == "__main__":
    main()
