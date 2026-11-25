#!/usr/bin/env python3
"""Entrypoint for the 25 November news-image entry.

The front page is rendered ahead of time by draw_frontpage.py and shipped
in this repository as entry.png. This file only puts that finished image
where the grader looks for it. It uses nothing but Python's standard
library, so it runs the same way in the grader's sandbox as it does here.
"""
import os
import shutil

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(SOURCE_DIR, "entry.png")
TARGET = os.path.join(TARGET_DIR, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main():
    if not os.path.isfile(SOURCE):
        raise SystemExit("entry.png is missing from the entry")
    # A PNG must open with its eight-byte signature; refuse anything else
    # rather than handing the grader a file it cannot read.
    with open(SOURCE, "rb") as f:
        magic = f.read(8)
    if magic != PNG_SIGNATURE:
        raise SystemExit("entry.png does not start with a PNG signature")
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f"front page copied to {TARGET}")


if __name__ == "__main__":
    main()
