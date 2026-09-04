# SESSION 41 NOTES — Thu 3 Sep 2026 21:43 → Fri 4 Sep 01:36, resumed 21:22 → 23:10

**The August gauntlet. Pure recall, no new material. Two sittings with a
20-hour break inside the drill.**

Interval gate: 25 hours since the S40 commit, 51 hours since 1.10 was taught,
verified from `git log` and `date`. Everything through 1.10 was legal.

Result: 32 cold asks, 27 passes. Queue [x] 80 → 96. 1.8 closed. 1.10's taught
half [x]. Strict audit of 1.1–1.5: 11 of 12 survive. The cold drill was
skipped by you two lines from green. Re-baseline: derived close ≈ 22 Oct.

---

## SELF-TEST — do this first, notes closed

1. `count = 0` at module level; inside `bump()`: `print(count)` then
   `count = count + 1`. Which error, and WHEN was `count` decided to be local?
2. Delete the assignment line. What prints now, and why?
3. `class BadCommand(ValueError)`. Does `except ValueError:` catch a
   `BadCommand`? Does `except BadCommand:` catch a plain `ValueError`?
4. `0 <= 45.0 <= 90` — does it raise? How does a function refuse a float then?
5. A `try` with `finally` sits INSIDE a `for` over three items. How many times
   does the `finally` run? And if the `try` is AROUND the loop?
6. `grid = [[0] * 3] * 3; grid[0][0] = 1`. What is `grid`?
7. `x = [1]; y = x; x += [2]` — what is `y`? Now with `x = x + [2]` instead?
8. Why return `None` for "not found" rather than `0`? Why not `-1`?
9. `d.keys()` vs `list(d.keys())` after a key is added — which sees it?
10. What is `__main__`? Is it a filename?

Answers are in section 1. Write yours first.

---

## 1. FULL TEACHING — everything taught or corrected tonight, from scratch

### 1.1 `UnboundLocalError` — local-or-not is decided before the function runs

```python
count = 0
def bump():
    print(count)
    count = count + 1
bump()
```
```
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

Three steps:
1. **Compile time.** When the file is compiled, before any `def` line runs,
   Python reads the entire body of `bump`. Any name that is ASSIGNED anywhere
   in that body is marked **local** for the whole function. `count = ...` is
   an assignment, so `count` is local on every line of `bump`, including the
   `print` above it.
2. **Call time.** `bump()` creates a frame with an empty slot for `count`.
3. **The read.** `print(count)` looks in the local slot first. Empty. It never
   walks out to the global `count = 0`, because the name is already classified
   local. Local but empty = unbound local.

Delete the assignment:
```python
count = 0
def bump():
    print(count)
bump()
```
```
0
```
No assignment in the body → not local → the lookup walks to the module → `0`.

**Your teach-back, accepted:** *"any variable with `=` inside the body is
considered local without executing… when we remove `count = count + 1` it is
not considered local."* Sharpening: decided when the FILE compiles, not when
the function object is created.

**Contrast:** `NameError` is a runtime error — the name was never bound
anywhere on the lookup path. `UnboundLocalError` is its local-slot cousin.

### 1.2 The exception hierarchy has a DIRECTION

```python
class BadCommand(ValueError):
    pass

try:
    raise BadCommand("bad")
except ValueError:
    print("parent catcher caught the child")

try:
    int("n/a")               # raises a PLAIN ValueError
except BadCommand:
    print("never printed")
```
```
parent catcher caught the child
Traceback (most recent call last):
ValueError: invalid literal for int() with base 10: 'n/a'
```

- `except X:` catches `X` **and everything built on X**.
- A catcher for the **child** does NOT catch the **parent**. `int("n/a")` raises
  a plain `ValueError`, which is not a `BadCommand`.

So in `to_angle`, the clause around `int(text)` must be `except ValueError:`,
and what it raises is `BadCommand(...)`. Tonight, at 22:00, you changed the
catcher to `except BadCommand:` — the rule applied backwards. It is the
same rule you passed in S36 with `OverLimit`; it inverted under fatigue.

### 1.3 Refuse vs convert — a float sails through a comparison

```python
print(0 <= 45.0 <= 90)   # True — no error, a float compares fine
print(int(45.0))         # 45 — CONVERTS, does not refuse
```

If the spec says a float must be refused, no `except` will ever see it,
because nothing raises. The function has to look at the type itself, before
the comparison, and raise `TypeError` on its own. You wrote exactly that test
in S37: `type(x) != int`. `int(angle)` inside the comparison does the
opposite: it silently accepts `45.0` as `45`.

### 1.4 `finally` — where the `try` sits decides how many times it runs

`teaching/s41_gauntlet/fin_loop.py`:
```python
def inside(items):
    for x in items:
        try:
            print("work", x)
        finally:
            print("done")

def around(items):
    try:
        for x in items:
            print("work", x)
    finally:
        print("done")
```
```
work 1 / done / work 2 / done / work 3 / done      <- inside: once per item
work 1 / work 2 / work 3 / done                     <- around: once
```

A `finally` runs once per time its own `try` statement is entered. It runs
LAST inside that statement: after the `try` body, after whichever `except` or
`else` ran, and just before control leaves — normally or with a report. It is
not "first".

When you need BOTH per-item handling AND a once-only exit action, you need
two `try` statements, one inside the other — which is what your final `run`
had:

```python
ok = 0
try:
    for joint, text in cmds:
        try:
            angle = to_angle(text)
            check(joint, angle)
        except BadCommand:
            log.append(("bad", joint, text))
        else:
            log.append(("ok", joint, angle))
            ok = ok + 1
finally:
    log.append(("done", ok))
return ok
```

### 1.5 `*` on a list copies REFERENCES

```python
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)
print(grid[0] is grid[1])
```
```
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
True
```

`[inner] * 3` puts the SAME inner list in three slots. Three names, one
object — the S33 aliasing, wearing new clothes. `[1, 2] * 3` is harmless
because ints are immutable. The fix is to build three separate inner lists
(a comprehension: `[[0] * 3 for _ in range(3)]`).

### 1.6 `+=` on a mutable is in-place; `=` always rebinds

```python
x = [1]; y = x
x += [2]
print(y)        # [1, 2]  -- += mutated the ONE list both names share

x = [1]; y = x
x = x + [2]
print(y)        # [1]     -- x + [2] built a NEW list; = rebound x to it
```

Your output for `+=` was right; your explanation of `x = x + [2]` ("mutates
the original") was backwards. The 1.5 augmented-assignment tick reverts to
[~] on it: right output, wrong model.

### 1.7 `None` as absence

What: a value that means "there is no answer". Why: sometimes every real value
of the return type is a legal answer, so none of them can double as "nothing".
What it buys: the caller can tell "not found" from "found at index 0".

```python
def first_over(readings, limit):
    for i, r in enumerate(readings):
        if r > limit:
            return i
    return None

print(first_over([200, 10], 90))   # 0
print(first_over([10, 20], 90))    # None
```

`0` for "not found" would collide with a real index. `-1` is no better in
Python: it is the LAST index, a real answer (your teach-back). The trap:
`if not result:` treats `0` and `None` alike. Test absence with
`if result is None:`.

(`enumerate()` appeared here untaught — parked; it will be defined before it
is ever in a drill.)

### 1.8 `.keys()` is a live view; `list()` is a snapshot; a dict iterator refuses a resized dict

```python
d = {"a": 1, "b": 2}
k = d.keys()
l = list(d.keys())
z = zip(d, [10, 20])
d["c"] = 3
print("c" in k, "c" in l)   # True False
print(list(z))
```
```
True False
RuntimeError: dictionary changed size during iteration
```

`k` is a window onto the dict; `l` is a copy taken at that moment (a list —
mutable, so the word is *snapshot*, not *immutable*). `z` is lazy and holds
an iterator over `d`; a dict iterator refuses to continue once the dict has
changed size. Footnote-sized.

### 1.9 `__main__` is not a filename

`__name__` is `"__main__"` in whichever file you LAUNCHED, whatever it is
called. In a file that was IMPORTED, `__name__` is that module's own name.
You proved it: you ran `robot.py` and wrote `__main__` for it; then imported
it from `app.py` and it printed `robot`.

### 1.10 Corrections issued
- "list is a snapshot and **immutable**" → a list is mutable; *snapshot*.
- "the PVM executes **line by line**" → it executes bytecode *instructions*;
  a line is several.
- "CPython is the **PVM** written in C" → the whole interpreter, compiler and
  PVM.

---

## 2. THE DRILL — `drills/s41_commands.py`

Spec: `BadCommand` (catchable by `except ValueError:` without being named);
`to_angle(text)` → int or `BadCommand`; `check(joint, angle)` → angle,
`BadCommand` for unknown joint / out of range, built-in `TypeError` for a
wrong type; `run(cmds, log)` → per-command ok/bad entries, any other report
passes through, `("done", n)` always last. 36 tests.

Sequence: first red was the type's NAME (`OutofLimit`). Then 26/34 → the
hardcoded `1` → the bad entry carrying an int (you had rebound the name) →
the ok entry carrying text (over-correction) → 30/34 → the `finally`
placement (nested `try`) → 31/34 → the class line → 32/34. Then the two
changes in §1.2 and §1.3 went the wrong way → 24/34 → you asked me to edit
the file (refused) → you skipped it. Committed as it stood.

**What held and counts:** zero catch-alls, and you said why unprompted.
`run`'s final structure. The done line, held on the second asking.

---

## 3. THINKING GAPS THIS SESSION — with classification

| Gap | Type | Evidence |
|---|---|---|
| `UnboundLocalError` mechanism | **Knowledge gap (faded)** | Declared honestly: "gap, give me the logic". Taught S19/S21/S22/S26; teach-back clean tonight. Cold test 5 Sep. |
| Hierarchy direction inverted | **Structural flaw under fatigue** | Rule stated correctly earlier in the same session; applied backwards at 22:00 on day two. |
| `int(angle)` to "refuse" a float | **Knowledge gap** | Convert vs refuse never distinguished explicitly. Now is. |
| `x = x + [2]` "mutates" | **Right output, wrong model** | Third instance of the signature (short-circuit S37, grid S41). |
| `[[0]*3]*3` three independent rows | **Right output, wrong model — rated 3, calibrated** | The S33 aliasing not recognised in a new shape. |
| `None`-as-absence | **Knowledge gap** | Gave the mutating tell instead. Taught. |
| Spec surface-read (quotes in the worked example) | **Lazy thinking (your own S20 label)** | Pushback 75, not upheld. |
| Eight pytest reds unreadable | **Channel / mentor** | Not logged against you. |

---

## 4. TEACHING MISTAKES THIS SESSION

1. **Eight reds delivered as raw assertion lines in one message.** You said
   you could not understand them. Correct. Re-delivered one group at a time,
   in words — and every group was then found off a single pointer. New rule of
   thumb: red comes back as ONE group, in words, never a dump.
2. **The spec described the wrong-type outcome instead of naming `TypeError`.**
   Pushback 76, part-upheld. The exception TYPE NAME is interface and will be
   written; the construct stays withheld.
3. **A 20-hour break inside the drill, with no re-gate and no re-frame** when
   it resumed. The direction error followed.
4. **A [RECALL] fired as the third item in a mid-drill turn** (`joint_name`
   unbound on the empty list). Unanswered; dropped.

Held: gate from the repo in the first minute; the plan said out loud; every
snippet run before it was posed; ratings after answers, before verdicts; the
drill file never touched, including when asked; the skip honoured at once.

---

## 5. THE RE-BASELINE ARITHMETIC

Observed since 16 Aug: ~2.1 subsection-equivalents in 2.7 weeks ≈ 0.8/week.
Remaining: ~5.2 units (1.9 ×0.7, 1.10 ×0.5, 1.11, 1.12 ×2, 1.13). Derived
close ≈ **22 Oct 2026**. The 30 Sep gate needs ~1.4/week. Ladder rung 1:
weekend blocks first. Nothing de-scoped. Recomputed at the September gauntlet.

---

## 6. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | Trap |
|---|---|---|
| `UnboundLocalError` | a name is local (assigned somewhere in the body) but read before its first assignment | locality is decided at compile time for the WHOLE body, not line by line |
| `class Child(Parent)` | makes `Child` a kind of `Parent` | `except Parent:` catches `Child`; `except Child:` does NOT catch `Parent` |
| refuse vs convert | `type(x) != int` refuses; `int(x)` converts | a float passes `0 <= x <= limit` silently |
| `finally` | runs once per entry of ITS `try`, last, on every exit | inside a loop = once per item; put the `try` around the loop for once-only |
| `[a] * n` | n references to the SAME `a` | mutate one, all change; harmless only for immutables |
| `x += y` (list) | in-place mutation | `x = x + y` builds a new object and rebinds |
| `None` as absence | the one value that cannot be a real answer | `if not r:` confuses `0` with `None`; use `is None` |
| `d.keys()` | live view | `list(d.keys())` is a snapshot; a dict iterator raises `RuntimeError` if the dict is resized |
| `__main__` | the `__name__` of the LAUNCHED file | not a filename; imported files get their module name |
| `id(x)` | identity, unique among live objects, constant for the object's lifetime | reusable after the object dies |
| `print()` | `str()` on each arg, joined by `sep`, followed by `end` | returns `None` |
