"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.
Standard library only.
"""

import os

REVIEW = (
    "One star: my owner waters me with ice cubes like I'm a cocktail, hauls "
    "me around the flat chasing 'better light' like I'm furniture, and tells "
    "guests I'm thriving while my roots sit in a swamp and my newest leaf "
    "came out the size of a postage stamp."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
