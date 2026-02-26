#!/usr/bin/env python3

"""
[DETECT WHICH WEEK TO GRADE]

Checks the git diff of the last 2 commits. 
If no submission is detected, it exits with error.
"""

from __future__ import annotations

import os
import re
import subprocess

WEEK_RE = re.compile(r"^submissions/(w\d{2})/")

def get_changed_files() -> list[str]:
    try:
        out = subprocess.check_output(["git", "diff", "--name-only", "HEAD^", "HEAD"], text=True)
        return [l.strip() for l in out.splitlines() if l.strip()]
    except Exception:
        out = subprocess.check_output(["git", "ls-files"], text=True)
        return [l.strip() for l in out.splitlines() if l.strip()]

def main() -> None:
    changed = get_changed_files()
    touched = sorted({m.group(1) for f in changed if (m := WEEK_RE.match(f))})

    if len(touched) == 1:
        week = touched[0]
    elif len(touched) > 1:
        raise SystemExit(f"Your push changed multiple weeks: {touched}. Please submit changes for only ONE week at a time.")
    else:
        print("Error: No active submission week detected in the recent commits.")
        exit(1)

    out = os.environ.get("GITHUB_OUTPUT")
    if out:
        with open(out, "a", encoding="utf-8") as f:
            f.write(f"week={week}\n")
            f.write("max_score=100\n")

if __name__ == "__main__":
    main()
