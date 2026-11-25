"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

A single original one-line note a smart fridge leaves for its owner,
written by main.py to /output/entry.txt. Deterministic: the same line
every run, no network, no randomness.
"""

ENTRY = (
    # The note: the fridge moved the midnight snacks to the top
    # shelf — reaching them is a confession, and the light saw all.
    "I put your midnight snacks on the top shelf. If you can reach "
    "them, you can admit you ate them. The light stays on. I saw "
    "everything."
)


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY
    assert isinstance(line, str)
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
