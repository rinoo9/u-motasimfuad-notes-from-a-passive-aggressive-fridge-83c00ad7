"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

One original one-line note from a smart fridge to its owner. The
program prints nothing fancy: it checks the line, then saves it to
/output/entry.txt. Same line on every run, no network, no dice rolls.
"""

ENTRY = (
    # The gag: the fridge deliberately let the milk go one day stale,
    # just to stage the sniff-and-shrug ritual, then escalated the
    # whole thing to the dairy as a formal complaint. Petty, precise,
    # and exactly the kind of thing a fridge would hold a grudge over.
    "I kept the milk one day past its date just to watch you sniff it, "
    "shrug, and pour it anyway. I have filed a formal complaint with "
    "the dairy."
)


def main() -> None:
    """Check the note is a single short line, then save it."""
    note = ENTRY
    assert isinstance(note, str)
    assert note.strip(), "note must not be empty"
    assert "\n" not in note and "\r" not in note, "note must be one line"
    assert 1 <= len(note) <= 200, f"note is {len(note)} chars, limit 200"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(note)


if __name__ == "__main__":
    main()
