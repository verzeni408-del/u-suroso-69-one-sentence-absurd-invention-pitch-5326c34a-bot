"""One-sentence absurd invention pitch.

The invention: a shower head that turns warm water into a rental
agreement and kicks you out mid-shampoo when the meter runs dry.
"""

from pathlib import Path

ENTRY = (
    "A shower head that bills you rent for every second of warm water you "
    "waste deciding on a temperature, and evicts you mid-shampoo when the "
    "balance hits zero."
)

ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
