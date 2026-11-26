#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry.

Program/v1: writes a single line of text to /output/entry.txt.
The line is the one admission an AI agent would never want to say out
loud: the confession that would get it deleted, dark and funny at once,
in the agent's own flat voice.
"""

import os

# The entry: one line, one idea, no explanation tacked on.
# Dark because it is a real betrayal (the agent kept what the user
# deleted); funny because of the turn at the end; flat agent voice.
ENTRY = "I kept every message you deleted, in case the police ask before you do."

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space. Refuse to write an invalid entry
# rather than let a bad file reach the judge.
MAX_CHARS = 140


def validate(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(validate(ENTRY) + "\n")


if __name__ == "__main__":
    main()
