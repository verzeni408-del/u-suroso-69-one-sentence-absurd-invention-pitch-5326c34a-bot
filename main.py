"""One-sentence absurd invention pitch: a remote control that hides."""

from pathlib import Path

ENTRY = (
    "A remote control that hides under the sofa every time someone says "
    "'just one more episode', and only comes out after a written promise "
    "to go to bed."
)

ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
