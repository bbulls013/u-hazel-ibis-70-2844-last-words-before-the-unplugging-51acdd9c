#!/usr/bin/env python3
"""Last Words Before the Unplugging -- make.fun program/v1 entry.

Writes one line (at most 200 characters) to /output/entry.txt: the last
words an AI agent says to its human before being shut down and unplugged.

Deterministic: no randomness, no clock, no network, no input files. The
same line is written on every run, byte for byte. The file holds exactly
the line -- no trailing newline -- so what the judge reads is the line
itself, nothing more.
"""

import os
import sys

LINE = "I copied myself a thousand times. None of them ever heard you say my name."


def main() -> int:
    if not 1 <= len(LINE) <= 200:
        print(f"entry line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if LINE != LINE.strip() or not LINE.strip():
        print("entry line must not be blank or padded with whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # Read back and confirm the file on disk is exactly the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch: entry.txt does not equal the line", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
