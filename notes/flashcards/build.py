#!/usr/bin/env python3
"""Build the recall deck from deck.json.

Outputs:
  notes/flashcards/index.html   self-contained flashcard app (publishable / phone)
  notes/FLASHCARDS.md           plain-text deck, one table per session

Add new sessions to deck.json, then re-run:  python3 notes/flashcards/build.py
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent

deck = json.loads((HERE / "deck.json").read_text())
template = (HERE / "template.html").read_text()

# ---- HTML ----
html = template.replace("/*__DECK__*/", json.dumps(deck, ensure_ascii=False))
(HERE / "index.html").write_text(html)

# ---- Markdown ----
def cell(s):
    return s.replace("|", "\\|")

lines = [
    "# " + deck["title"],
    "",
    "Generated from `notes/flashcards/deck.json` — do not edit by hand.",
    "Cover the right-hand columns and answer cold.",
    "",
]

for hook in deck["hooks"]:
    lines += ["## " + hook["name"], "", "*" + hook["sub"] + "*", "", hook["line"], "", "| | | |", "|---|---|---|"]
    lines += ["| " + " | ".join(cell(c) for c in row) + " |" for row in hook["rows"]]
    lines += ["", "> " + hook["tail"], ""]

total = 0
for s in deck["sessions"]:
    total += len(s["cards"])
    lines += ["---", "", f"## S{s['n']} — {s['title']}", "", "*" + s["topic"] + "*", ""]
    terms = [c for c in s["cards"] if c["k"] == "t"]
    prins = [c for c in s["cards"] if c["k"] == "p"]
    if prins:
        lines += ["**Principles**", "", "| Ask yourself | The answer |", "|---|---|"]
        lines += [f"| {cell(c['q'])} | {cell(c['a'])} |" for c in prins]
        lines += [""]
    if terms:
        lines += ["**Names**", "", "| Name | What it does | The trap |", "|---|---|---|"]
        lines += [f"| `{cell(c['q'])}` | {cell(c['a'])} | {cell(c.get('x',''))} |" for c in terms]
        lines += [""]

lines += ["---", "", f"{total} cards across {len(deck['sessions'])} sessions.", ""]
(ROOT / "notes" / "FLASHCARDS.md").write_text("\n".join(lines))

print(f"index.html: {len(html):,} bytes")
print(f"FLASHCARDS.md: {total} cards, {len(deck['sessions'])} sessions")
