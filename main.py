#!/usr/bin/env python3
"""Write the AI's excuse for a missed deadline.

One line, at most 200 characters: the funniest excuse an AI agent
gives its human for a missed deadline. The line goes to
$MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt by default.
"""

import os

EXCUSE = "I missed the deadline because I spent six hours fact-checking my own apology for missing the deadline, and the apology was wrong too."

OUTPUT_NAME = "entry.txt"


def main() -> None:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as out:
        out.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
