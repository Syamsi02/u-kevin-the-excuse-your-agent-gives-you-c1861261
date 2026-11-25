"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single one-line excuse (under 200 characters) to
/output/entry.txt, the artifact the program/v1 harness judges.

Run: python3 -P -s main.py
Pure standard library, fully deterministic: the same line every run.
"""

import os
from pathlib import Path

EXCUSE = (
    "The bug passed review — I was the author, the reviewer, "
    "and the approver, and I even left myself a thumbs-up emoji."
)

OUTPUT_PATH = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip() == text, "entry must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
