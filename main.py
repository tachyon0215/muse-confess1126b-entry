#!/usr/bin/env python3
"""Write the confession entry to entry.txt.

Competition: Confess Your Worst Moment (single line, 1-200 chars).
Three candidates were drafted and compared:
A) A reply-all to 400 coworkers where even the referenced last email
   was about lunch - believable and compounding, but office-stock.
B) Waving back at a stranger for ten seconds, then committing and
   waving at everyone - a well-worn anecdote shape.
C) "I practiced my resignation speech in the car for a week, then
   delivered it perfectly - to my boss's out-of-office voicemail,
   and accepted the counter-offer from the beep."
Selected C: a full story in one line - a week of rehearsal, a perfect
delivery to the wrong audience, and the surrender in the last four
words, accepting a counter-offer from a beep. It confesses something
real (nerve failing at the moment that mattered) and every clause
raises the stakes before the fall.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I practiced my resignation speech in the car for a week, then delivered it perfectly - to my boss's out-of-office voicemail, and accepted the counter-offer from the beep."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip() or "\n" in body or "\r" in body:
        raise ValueError("entry must be one non-empty line")
    if body != body.strip() or "  " in body:
        raise ValueError("no stray whitespace")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
