#!/usr/bin/env python3
"""Sync the example.yml workflow into the README fenced block between:
<!-- snippet:example.yml:start --> and <!-- snippet:example.yml:end -->
"""

from pathlib import Path
import sys

EXAMPLE = Path("example.yml")
README = Path("README.md")
START = "<!-- snippet:example.yml:start -->"
END = "<!-- snippet:example.yml:end -->"


def main() -> int:
    if not EXAMPLE.exists():
        print(f"Missing {EXAMPLE}", file=sys.stderr)
        return 1
    if not README.exists():
        print(f"Missing {README}", file=sys.stderr)
        return 1

    md = README.read_text(encoding="utf-8")
    try:
        s = md.index(START)
        e = md.index(END, s)
    except ValueError:
        print("Markers not found; aborting.", file=sys.stderr)
        return 1

    yaml_text = EXAMPLE.read_text(encoding="utf-8").rstrip()
    replacement = (
        f"{START}\n```yaml\n"
        f"{yaml_text}\n```\n{END}"
    )
    new_md = md[:s] + replacement + md[e + len(END) :]
    if new_md == md:
        print("README already up to date.")
        return 0
    README.write_text(new_md, encoding="utf-8")
    print("README updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
