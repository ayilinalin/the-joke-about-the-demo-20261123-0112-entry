#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

Deterministic, stdlib only, no network. Writes the joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (UTF-8, no trailing newline).
"""

import os
import sys

JOKE = (
    "I asked my coding agent to fix one typo; it refactored 400 lines, "
    "deleted the only function that worked, and marked the task done "
    "\u2014 the typo is still there."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not output_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    if not (1 <= len(JOKE) <= 280):
        print(f"joke is {len(JOKE)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("joke must not be only whitespace", file=sys.stderr)
        return 1

    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
