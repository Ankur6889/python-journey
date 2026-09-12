from pathlib import Path

here = Path(__file__).parent
print(here)

with open(here / "limits.txt") as f:
    print(repr(f.read()))
