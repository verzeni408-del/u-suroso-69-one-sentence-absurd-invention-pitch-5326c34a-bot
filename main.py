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

MAX_CHARS = 220


def main() -> None:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(f"entry too long: {len(ENTRY)} chars > {MAX_CHARS}")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence ending with a period")
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
