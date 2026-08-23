# COLD BUILD BLOCK 01 — Sun 23 Aug 2026

90 min, timed. No AI, no autocomplete. git commit at start and end.
pytest decides whether it works.

**You write ONE file: `clamp.py`.**
`test_clamp.py` is already here and I wrote it — pytest has never been
taught, so writing tests is not your job. Do not edit it, do not read it
for hints. It is the acceptance criteria, nothing more.

Run it:  `python3 -m pytest builds/block_01_joint_clamp -q`
One level: add `-k L1`

Keep `LOG.md`: where you stalled, and what you had to look up.

## THE ARM

| joint    | low  | high |
|----------|------|------|
| shoulder | -90  | 90   |
| elbow    | 0    | 145  |
| wrist    | -180 | 180  |

## THE CLAMP RULE

below low -> low.  above high -> high.  otherwise unchanged.
**Exactly equal to a limit -> unchanged.**

---

# L1

```python
def clamp_one(angle, low, high):
    ...
```

Exact expected results:

```
clamp_one(120, -90, 90)    == 90
clamp_one(-90, -90, 90)    == -90
clamp_one(0, -90, 90)      == 0
clamp_one(-10, 0, 145)     == 0
clamp_one(145, 0, 145)     == 145
clamp_one(200, 0, 145)     == 145
clamp_one(90, -180, 180)   == 90
clamp_one(-400, -180, 180) == -180
```

# L2

```python
def clamp_all(low, high, *angles):
    ...
```

Returns a tuple, same order in as out.

```
clamp_all(-90, 90, 120, -90, 0, 200) == (90, -90, 0, 90)
clamp_all(-90, 90, 45)               == (45,)
clamp_all(-90, 90)                   == ()
```

# L3  <- the real one

```python
def clamp_joints(*angles, **limits):
    ...
```

Angles arrive positionally and anonymously.
Limits arrive by name, each as a `(low, high)` tuple.
**Returns a dict: joint name -> safe angle.**

```
clamp_joints(120, -10, 90,
             shoulder=(-90, 90),
             elbow=(0, 145),
             wrist=(-180, 180))
== {"shoulder": 90, "elbow": 0, "wrist": 90}
```

```
clamp_joints(0, 200, -400,
             shoulder=(-90, 90),
             elbow=(0, 145),
             wrist=(-180, 180))
== {"shoulder": 0, "elbow": 145, "wrist": -180}
```

⚠ The first angle belongs to the first named joint, the second to the
second, and so on. Working out HOW to line those two things up is the
whole point of this block. It is harder than it looks. Log the stall.

# L4

```
clamp_joints(120, -10, 90, 30,
             shoulder=(-90, 90),
             elbow=(0, 145),
             wrist=(-180, 180))
```

Four angles, three joints. `30` belongs to nothing.

You decide: raise an error, or ignore it. Write ONE line in LOG.md saying
why. The question to answer is whether this is a BUG in the caller or an
EXPECTED case.

# L5 — only if time remains

```python
def report(*angles, **limits):
    ...
```

Prints one line per joint, columns lined up:

```
shoulder :  120.0 ->   90.0  CLAMPED
elbow    :  -10.0 ->    0.0  CLAMPED
wrist    :   90.0 ->   90.0  ok
```

Then a final line: how many were clamped.

---

# GREEN IS THE BAR

13 tests. All red now. Make them green, in level order.
L4 and L5 are not tested — L4 is your decision, and it goes in LOG.md.

# TIME

L1 15 · L2 15 · L3 35 · L4 10 · tests and final run 15
