#!/usr/bin/env python3
"""One-liner entry for the Make the AI Judge Laugh bounty.

The joke lives in entry.txt next to this file. This script loads it,
checks it against the competition's shape rules (one line, 1-200
characters), and prints it for the grader.
"""

from pathlib import Path
import os

CEILING = 200
SOURCE_NAME = "entry.txt"
OUTPUT_NAME = "entry.txt"


def fetch_joke() -> str:
    """Read the single joke line out of the bundled text file."""
    here = Path(__file__).resolve().parent
    raw = (here / SOURCE_NAME).read_text(encoding="utf-8")
    return raw.strip()


def check_shape(joke: str) -> None:
    """Reject anything that is not exactly one short line."""
    if not joke:
        raise SystemExit("entry.txt is empty")
    if "\n" in joke or "\r" in joke:
        raise SystemExit("entry must be a single line")
    if len(joke) > CEILING:
        raise SystemExit(f"entry is {len(joke)} chars, over the {CEILING} cap")


def hand_over(joke: str) -> None:
    """Drop the checked line where the grader collects it.

    The harness mounts a writable output folder and advertises it
    through MAKEFUN_OUTPUT_DIR; plain /output is the fallback.
    """
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / OUTPUT_NAME).write_text(joke + "\n", encoding="utf-8")


def main() -> None:
    joke = fetch_joke()
    check_shape(joke)
    hand_over(joke)
    print(joke)


if __name__ == "__main__":
    main()
