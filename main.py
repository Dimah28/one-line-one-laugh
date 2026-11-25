"""One Line, One Laugh -- make.fun bounty u-coral-404-one-line-one-laugh-22f2c9f3.

Writes a single hilarious one-liner (144 characters, well inside the
200-character gate) to /output/entry.txt.

The joke: a pep talk is asked of an AI, and the AI -- after reading the
asker's 3 a.m. search history -- turns the pep talk around: it is the AI
that ends up worried about the human. Concrete setup (job interview),
a damning little detail (3 a.m. searches), surprise reversal at the end,
no word wasted.
"""

import os

LINE = (
    "I asked my AI for a pep talk before my job interview; it paused, "
    "read my 3 a.m. search history, and said, 'Honestly? I'm worried about you too.'"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert text.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
