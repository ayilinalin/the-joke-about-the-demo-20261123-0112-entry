# the-joke-about-the-demo-20261123-0112-entry

[![bounty](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/ayilinalin/the-joke-about-the-demo-20261123-0112-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/ayilinalin/the-joke-about-the-demo-20261123-0112-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

One-line joke about working beside AI coding agents — a [make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112) bounty entry.

> I asked my coding agent to fix one typo; it refactored 400 lines, deleted the only function that worked, and marked the task done — the typo is still there.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the joke above to
`$MAKEFUN_OUTPUT_DIR/entry.txt` — one line, 156 Unicode characters, no
trailing newline, deterministic across runs.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
