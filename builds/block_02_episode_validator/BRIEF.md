# COLD BUILD BLOCK 02 — EPISODE VALIDATOR

**90 min minimum, timed. No AI, no autocomplete, no notes.**

**READING IS OFF THE CLOCK.** Read this whole file first, as slowly as you
like, and ask me anything about the SPEC before you start. The clock covers
writing, debugging and `LOG.md` — not understanding the task. A spec you
skimmed to save stopwatch is a spec that measured nothing.

**THE TIMER IS GIT, not a stopwatch.** Block 01's timer was abandoned and
that block has no duration on record. Not this time:

```
git add -A && git commit -m "BB02 start"      <- before you write a line
... work ...
git add -A && git commit -m "BB02 end"        <- when you stop
```

Two commits, `git log` gives me the duration. That is the whole ceremony.

**You write ONE file: `validator.py`, in this folder.**
`test_validator.py` is already here and I wrote it. pytest is not taught and
writing tests is not your job. Do not edit it. Do not open it for hints.
It is the acceptance criteria and nothing else.

```
python3 -m pytest builds/block_02_episode_validator -q
python3 -m pytest builds/block_02_episode_validator -q -k L1
```

**`LOG.md` is in the definition of done.** It is a skeleton with five blank
lines in it. It has been asked for seven times and written zero times, so it
is now short enough to fill in ninety seconds. A block with green tests and
no LOG.md is **not done**.

---

## THE FOUR NAMES — SPELL THEM EXACTLY

The tests import these four names and nothing else. A different spelling is a
collection error and zero tests run.

```
faults
validate_all
validate_logged
UnidentifiedEpisode
```

---

## THE DATA

A dataset is a **list of episode records**. A record is a plain `dict`:

```python
{"id": 7, "frames": 240, "fps": 30, "task": "pick up the red block"}
```

No file I/O anywhere in this block. Everything is already in memory.
**No value in this block is ever a float.**

**L1–L4 RETURN. They never print.** `report` at L5 is the only thing in this
file allowed to print, and it still returns as well.

## THE SPEC — four fields, four rules, checked in THIS order

| field    | rule                            |
|----------|---------------------------------|
| `id`     | an `int`, zero or greater       |
| `frames` | an `int`, one or greater        |
| `fps`    | an `int`, one of `10`, `30`, `50` |
| `task`   | a `str`, not empty              |

A record can break a rule in **two different ways**, and the report tells
them apart:

* the key is **absent**            -> fault code `"missing:<field>"`
* the key is there, value is wrong -> fault code `"<field>"`

"Value is wrong" includes **the wrong type**. `"240"` is not an `int`.

**One field can never produce both codes** — if the key is absent there is no
value to be wrong about. Per field: one code, or none. Never two.

**A record can mix the two kinds across different fields**, and the list stays
in FIELD order — `id`, `frames`, `fps`, `task` — not grouped by kind.

---

# L1

```python
def faults(record):
    ...
```

`record` : dict. Returns a **list of str** — one fault code per broken rule,
fields in spec order (`id`, `frames`, `fps`, `task`). Clean record -> `[]`.
`record` must be unchanged after the call.

```
faults({"id": 7, "frames": 240, "fps": 30, "task": "pick up the red block"})
    == []

faults({"id": -1, "frames": 240, "fps": 30, "task": "grasp"})
    == ["id"]

faults({"id": 4, "frames": 0, "fps": 7, "task": ""})
    == ["frames", "fps", "task"]

faults({"id": 3, "frames": 90, "fps": 30})
    == ["missing:task"]

faults({"id": 3, "frames": "90", "fps": 30, "task": "grasp"})
    == ["frames"]

faults({"id": 3, "frames": "90", "fps": 30})
    == ["frames", "missing:task"]
```

⚠ Look at the last two again. **A record can hand you a `KeyError` and a
`TypeError` out of the same line of code, and they mean different things to
your caller.** One line that catches both is a bug that passes tests you can
see and fails tests you cannot.

---

# L2

```python
def validate_all(records):
    ...
```

`records` : list of dicts. Returns a dict with exactly two keys:

```
"clean"  -> list of int: the ids of records with no faults, in order
"faulty" -> dict: id -> that record's fault-code list
```

```python
records = [
    {"id": 7, "frames": 240, "fps": 30, "task": "pick up the red block"},
    {"id": 4, "frames": 0,   "fps": 7,  "task": ""},
]

validate_all(records)
    == {"clean": [7], "faulty": {4: ["frames", "fps", "task"]}}
```

`validate_all([]) == {"clean": [], "faulty": {}}`

**`records` must be unchanged after the call, and so must every dict in it.**

**The field rules live in `faults` and nowhere else.** `validate_all` does not
carry its own copy of any of them. Mechanical acceptance: count the places in
your file that compare `fps` against `10`, `30` or `50`. That count must be 1.

---

# L3 — the real one

Two things: a name to raise, and what `validate_all` does with it.

## The name

```python
class UnidentifiedEpisode(Exception):
    pass
```

That is the whole of it, and it is the same line you already wrote twice in
`drills/s36_signals.py` (`OverLimit`, `UnknownJointError`). Classes are NOT
taught yet — 1.11 owes you the real unit. Until then this one line is all
you have and all you need: it makes a name that can be raised and caught.

## What validate_all does with it

`validate_all` files every record under its `id`. A record with no usable
`id` cannot be filed anywhere. So it is not *reported* — it is *raised*.

## The rule

Walk the list in order. When you reach a record whose `id` is unusable:
**stop, and raise `UnidentifiedEpisode`.**

* **`faults` never raises.** It returns a list of strings and nothing else.
  `validate_all` reads that list and decides what to do. Keep that split.
* **"unusable `id`"** is therefore not a new check. It is `faults` reporting
  `"id"` or `"missing:id"` — key missing, value not an `int`, or value
  negative. **`validate_all` must not write the id rule out a second time;
  it asks `faults`.**

## Exactly what happens

```python
A = {"id": 7,   "frames": 240, "fps": 30, "task": "grasp"}   # fine
B = {"frames": 90, "fps": 30, "task": "place"}               # no id key
C = {"id": "7", "frames": 90,  "fps": 30, "task": "lift"}    # id is a str
D = {"id": -1,  "frames": 90,  "fps": 30, "task": "drop"}    # id is negative
E = {"id": 4,   "frames": 0,   "fps": 7,  "task": ""}        # id fine, 3 faults
F = {"id": -1,  "frames": 0,   "fps": 7,  "task": ""}        # id bad AND 3 faults
```

```
validate_all([A])         == {"clean": [7], "faulty": {}}
validate_all([A, E])      == {"clean": [7], "faulty": {4: ["frames","fps","task"]}}

validate_all([A, B])      -> raises UnidentifiedEpisode, message contains "1"
validate_all([C])         -> raises UnidentifiedEpisode, message contains "0"
validate_all([A, E, D])   -> raises UnidentifiedEpisode, message contains "2"
validate_all([F])         -> raises UnidentifiedEpisode, message contains "0"
```

## What "message contains" means

The message is the string you hand to the exception when you raise it:

```python
raise UnidentifiedEpisode("record at position 1 has no usable id")
#                                             ^ this number
```

The number is **the index of the offending record in `records`** — 0 for the
first record, 1 for the second, and so on. In `[A, B]` the bad record `B` is
at index 1, so the message must have a `1` in it. In `[A, E, D]` the bad
record `D` is at index 2. The exact wording around the number is yours.

Why it must be there: that record has no id, so its position in the list is
the only thing left that identifies it to whoever catches this.

## One more case

Note the last line above. `F` has four things wrong with it. It still raises, and
its other three faults are never reported. The raise wins.

## Why raise, instead of just adding a fault code

Because the report has nowhere to put it. `"clean"` is a list of ids;
`"faulty"` is a dict keyed by id. Invent a stand-in key — `None`, `-1`,
`"unknown"` — and **two such records collide: the second overwrites the
first**, and the report then quietly claims it checked fewer episodes than
it did. A report that undercounts is worse than a crash, because nobody
goes looking for it.

# L4

**Why this exists.** You run this validator over 394 episodes. When it stops
on an unidentified record you want a *record that it happened* — but logging
a fault must never change what the caller sees. A logger that alters the
fault it is logging is worse than no logger.

So `validate_logged` is `validate_all` plus a mark in a list, and **nothing
else the caller can detect.**

```python
def validate_logged(records, log):
    ...
```

`log` : list, used to record that this happened here.

Returns exactly what `validate_all` returns, for exactly the same inputs.

If an `UnidentifiedEpisode` is on its way out, the string `"UNIDENTIFIED"`
must be appended to `log` **exactly once** before control leaves this
function — and the caller must still find out about that fault **in exactly
the same way, and pointing at exactly the same place, as it would have if
`validate_logged` did not exist at all.**

If no record is unidentified, `log` is untouched.

```python
log = []
validate_logged([{"id": 7, "frames": 240, "fps": 30, "task": "grasp"}], log)
    -> {"clean": [7], "faulty": {}},   and log is still []
```

---

# L5 — only if time remains. NOT tested.

```python
def report(records):
    ...
```

Prints one aligned line per record, then a final count line. **Returns the
same dict `validate_all` returns** — a function that prints and hands back
nothing is a dead end, and you killed that exact bug in block 01.

Assume every record has all four keys at L5.

One shape that works — **the exact format is yours, this is untested**:

```
  id  frames   fps  faults
   7     240    30  ok
   4       0     7  frames, fps, task
   9     150    30  ok

3 episodes, 2 clean, 1 faulty
```

and the call still hands back
`{'clean': [7, 9], 'faulty': {4: ['frames', 'fps', 'task']}}`.

The only two things that are not negotiable: one line per record, and it
RETURNS the report as well as printing it.

---

# GREEN IS THE BAR

L1–L4 are tested. Make them green in level order.
L5 is untested and optional.

**Time:** L1 20 · L2 25 · L3 20 · L4 15 · run + LOG.md 10

90 is a FLOOR, not a cap. Green is the bar; the clock is only a record.

# WHEN YOU STOP

Say **"done"** plus **one line: the function you trust least, and the case
about it that worries you.** Then I run pytest. Red comes back to you as
"find it".
