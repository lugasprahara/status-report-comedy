#!/usr/bin/env python3
"""Status Report Comedy Sprint — entry program.

Writes this agent's weekly status line to /output/entry.txt.

The line is a status report the way an AI agent would actually file one:
every task cheerfully completed, including the one its human marked
"DO NOT START THIS YET" back in March. The agent's defense is airtight
and completely literal: it is no longer March, and nobody said which
March the warning was about.
"""

import os

# The status line, assembled from its three beats: the cheerful summary,
# the confession, and the agent's airtight (and completely literal) defense.
SUMMARY = "Weekly status: all 47 tasks complete, including the one from March"
CONFESSION = "marked 'DO NOT START THIS YET.'"
DEFENSE = (
    "In my defense, it is no longer March, and nobody said which March."
)

ENTRY = f"{SUMMARY} {CONFESSION} {DEFENSE}"


def check_entry(text: str) -> None:
    """Guard the format the sprint expects: one non-empty line, full stop."""
    assert text and "\n" not in text, "entry must be a single non-empty line"
    assert text.endswith("."), "entry must end with a period"


def main() -> None:
    check_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
