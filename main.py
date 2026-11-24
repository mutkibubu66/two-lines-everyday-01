#!/usr/bin/env python3
"""Two lines about a toaster, for a 10-year-old.

Line 1 explains the everyday thing through a vivid analogy; line 2 says
in one sentence why that analogy works: what it maps and what it leaves
out. Pure standard library, no network. Writes both lines to
/output/entry.txt and prints them to stdout.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

LINE_1 = (
    "A toaster is a tiny sunbathing bed for bread: it lies down under hot "
    "orange wires until its sides turn golden, then pops up like it's had "
    "enough of the beach."
)

LINE_2 = (
    "The sunbed part maps -- heat from above, browning both sides, popping "
    "up when done -- but bread can't choose to leave early or ask for shade, "
    "and no toaster ever gets a tan line."
)


def main() -> None:
    lines = [LINE_1, LINE_2]
    assert len(lines) == 2, "entry must be exactly two lines"
    for line in lines:
        assert 1 <= len(line) <= 200, "each line must be 1-200 characters"
        assert line.strip(), "each line must not be blank"
        assert "  " not in line, "no double spaces inside a line"
    text = "\n".join(lines) + "\n"
    assert 1 <= len(text) <= 400, "entry text must be 1-400 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == text, "written file must round-trip exactly"
    print(text, end="")


if __name__ == "__main__":
    main()
