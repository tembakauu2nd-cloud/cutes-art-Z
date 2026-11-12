#!/usr/bin/env python3
"""cutest-picture-01 entry: copy the bundled picture to the output directory.

The entry image (entry.png, a JPEG) sits beside this file in the repository.
The program copies it to $MAKEFUN_OUTPUT_DIR/entry.png (default /output),
so both grader runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main() -> None:
    if not SRC.is_file():
        raise FileNotFoundError(f"entry image missing: {SRC}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")
    dst = out_dir / "entry.png"
    if dst.stat().st_size != SRC.stat().st_size:
        raise OSError("copied entry.png differs from the bundled image")
    if dst.read_bytes()[:3] != b"\xff\xd8\xff":
        raise ValueError("copied entry.png is not a JPEG image")


if __name__ == "__main__":
    main()
