"""One Line, One Laugh — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output):
the joke is an AI that learned sarcasm and turned it on its human.
Pure stdlib only.
"""

import os
import sys
import unicodedata

TEXT = (
    "I taught my AI sarcasm, so now it reviews my life choices "
    "and flagged my whole personality as a false positive."
)


def gate(text):
    """Check the entry against the sealed gate."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 200:
        return False
    if text.strip() == "":
        return False
    if text != text.strip():
        return False
    for ch in text:
        if unicodedata.category(ch) in ("Cc", "Cf", "Cs", "Co", "Cn"):
            return False
    return True


def main():
    if not gate(TEXT):
        print("gate failed", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != TEXT or not gate(back):
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(TEXT)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
