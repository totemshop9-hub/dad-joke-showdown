#!/usr/bin/env python3
"""Dad Joke Showdown entry — writes one dad joke to /output/entry.txt."""

import os

JOKE = "I told my wife she was drawing her eyebrows too high. She looked surprised."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
