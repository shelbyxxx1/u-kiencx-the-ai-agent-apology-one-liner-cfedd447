import os
from pathlib import Path


LINE = "I accidentally sent your boss the rant. He blamed AI; I corrected him. Your voice matters."


def main() -> None:
    assert 1 <= len(LINE) <= 159
    assert LINE.strip()
    assert "\n" not in LINE and "\r" not in LINE
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
