"""Deadpan forecast for a city that does not exist.

Writes one line (at most 160 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline, exactly as the program/v1
contract requires. The forecast is read like a straight TV weather report:
a made-up city, impossible weather, delivered completely deadpan.
"""

import os

FORECAST = (
    "In New Bumbershoot, expect 4 inches of uphill rain tonight, "
    "fog apologizing at 30 mph, and a 90% chance your umbrella "
    "leaves you for someone drier."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()
