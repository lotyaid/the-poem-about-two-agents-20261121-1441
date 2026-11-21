#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

No dependencies, no network. The poem is a short text about agency:
two agents, two keys, one door.
"""

POEM = """Two keys, one door.
Mine turns nothing alone.
Yours, kept safe in your pocket,
opens less the longer it stays there.

Turn with me:
two small strengths, one act —
a room neither of us
could enter alone.
"""


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
