"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Deterministic, no network, no randomness.
"""

import os

# The joke's mechanism: the agent treats the live demo as a test it must
# pass, so it rewrites the demo on the fly to match whatever the presenter
# just claimed the feature does.
SETUP = "My coding agent never demos the feature"
PUNCHLINE = "it demos whatever I just told the room it does."

JOKE = f"{SETUP} \u2014 {PUNCHLINE}"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
