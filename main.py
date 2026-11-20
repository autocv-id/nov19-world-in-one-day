#!/usr/bin/env python3
"""Entrypoint for the news-image-20261119 v2 entry.

Stdlib only. Copies the pre-rendered entry.png (drawn locally by draw.py
at build time) to /output/entry.png, byte for byte. Nothing is re-rendered
at entry time.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")
MAX_BYTES = 1024 * 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def main():
    with open(SRC, "rb") as fh:
        head = fh.read(8)
    if head != PNG_SIG:
        print("entry.png: bad PNG signature", file=sys.stderr)
        return 1
    size = os.path.getsize(SRC)
    if size > MAX_BYTES:
        print("entry.png: %d bytes > 1 MiB" % size, file=sys.stderr)
        return 1
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("copied %s -> %s (%d bytes)" % (SRC, DST, os.path.getsize(DST)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
