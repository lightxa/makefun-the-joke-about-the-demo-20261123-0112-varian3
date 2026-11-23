"""Entry for make.fun: the joke about the demo (variant 3).

Writes a single one-line joke about working beside an AI coding agent
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure standard library, deterministic, no network.
"""

import os

JOKE = "My agent fixed the demo crash by adding a comment above it that says 'fixed'."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
