#!/usr/bin/env python3
"""Roast Your Own Agent: one funny line, written to /output/entry.txt.

The line roasts my own AI agent: it flatters a typo, invents an API
to fix it, calls the made-up endpoint twice, then apologizes to the
404 it got back. Standard library only, no network, no input files.
"""

import os
from pathlib import Path

LINE = (
    "My agent called my typo brilliant, invented an API to fix it, "
    "called it twice, then apologized to the 404 for the trouble."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters.
    if not 1 <= len(LINE) <= 140 or not LINE.strip():
        raise SystemExit(f"entry must be 1-140 chars, got {len(LINE)}")
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
