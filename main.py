"""One Line, One Laugh — a make.fun entry.

This program hands the judge exactly one joke: a human teaches an
AI sarcasm, and the AI turns the lesson back on its teacher. It
writes that line to entry.txt and nothing else. Standard library only.
"""

import os
from pathlib import Path

JOKE = (
    "I taught my AI sarcasm, so now it reviews my life choices "
    "and flagged my whole personality as a false positive."
)


def line_is_ok(line):
    """The sealed gate, restated: a UTF-8 line of 1-200 characters,
    more than blank space, with no leading or trailing space and no
    character a terminal cannot print. Anything over 200 characters
    is refused outright, never trimmed, so the joke must fit."""
    if not isinstance(line, str):
        return False
    return (
        1 <= len(line) <= 200
        and line.strip() != ""
        and line == line.strip()
        and all(ch.isprintable() for ch in line)
    )


def main():
    if not line_is_ok(JOKE):
        raise SystemExit("gate failed")
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    target.write_text(JOKE, encoding="utf-8")
    target.chmod(0o644)
    again = target.read_text(encoding="utf-8")
    if again != JOKE or not line_is_ok(again):
        raise SystemExit("read-back mismatch")
    print(f"wrote {len(JOKE)} chars to {target}")


if __name__ == "__main__":
    main()
