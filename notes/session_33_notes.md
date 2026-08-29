# SESSION 33 NOTES — Friday 28 August 2026, 16:00 → Saturday 29 August, ~12:00
**1.8 Data Structures — `copy.deepcopy`, `reversed()`, and the three pitfalls.
Seven promotions, one demotion. 1.8 at ~98%.**

---

## 0. SELF-TEST FIRST (close these notes and answer before reading on)

1. `defaults = {"elbow": [0, 150]}`, `session = dict(defaults)`. You then run
   `session["elbow"][1] = 90` and `session["wrist"] = [-90, 90]`. What is
   `defaults` now — and why do those two lines behave differently?
2. What does `copy.deepcopy` do that `dict()` does not?
3. Name three things `deepcopy` is **not** good for.
4. `reversed(path)` and `path.reverse()`. For each: does it mutate, and what
   does it hand back?
5. A method hands you back a real value, not `None`. What may you conclude
   about whether the object changed?
6. `angles = [10, 200, 250, 30]`; you loop over `angles` removing anything
   above 180. What is left, and why?
7. `grid = [[0] * 3] * 3`, then `grid[0][0] = 99`. What is `grid`? Why is
   `[0] * 3` safe but `[[0] * 3] * 3` not?
8. What single question decides whether you reach for a `list`, `dict`, `set`
   or `tuple`?
9. Name the five checks and say what `ek` and `bahar` actually mean.
10. `f"{name:10s}|{angle:8.1f}|"` — which field hugs left, which hugs right,
    and what does that buy you?

---

## 1. FULL TEACHING

### 1.1 `copy.deepcopy` — the copy with no floor

**What it is.** `copy.deepcopy(x)` builds a new outer container *and* new copies
of everything inside it, recursively, all the way down.

**Why it exists.** A shallow copy stops at one level. `dict(defaults)` gives you
a new dict whose values are the *same* list objects. When the data is nested,
one level of copying is not a copy — it is a trap that looks like one.

**What it buys you.** A **snapshot**: data you can hand away or mutate freely,
knowing the original cannot be touched at any depth.

**What it is NOT.** Three honest non-claims, all stated before the code:

- It is **not the better copy**. It is slower — it must walk your whole
  structure — and it copies things you may have wanted shared.
- On a **flat container of immutables** it buys nothing over `[:]`.
- Most of the time the right answer is **neither**. Build the data fresh. You
  copy when you did not build it and cannot trust who else is holding it.

**Substrate: `import`.** `import copy` binds the name `copy` in your namespace
to a **module object**. `copy.deepcopy` is then the same `.` you already own — a
name looked up on an object. (How import *finds* the module is 1.10.)

```python
import copy

defaults = {"elbow": [0, 150], "wrist": [-90, 90]}

shallow = dict(defaults)
deep    = copy.deepcopy(defaults)

shallow["elbow"][1] = 90
print("after editing shallow:", defaults)

deep["wrist"][0] = -45
print("after editing deep:   ", defaults)

print("shared inner list? ", defaults["elbow"] is shallow["elbow"])
print("shared inner list? ", defaults["wrist"] is deep["wrist"])
```

```
after editing shallow: {'elbow': [0, 90], 'wrist': [-90, 90]}
after editing deep:    {'elbow': [0, 90], 'wrist': [-90, 90]}
shared inner list?  True
shared inner list?  False
```

Line 2 is the point: editing `deep` changed **nothing**. The `[0, 90]` still
showing is the damage from the shallow edit on the line above.

### 1.2 `reversed()` — and the name that hides it

**What it is.** `reversed(x)` hands you an **iterator** that walks `x` back to
front.

**Why it exists.** `path[::-1]` also goes backwards — by **building an entire
second list**. On an 89k-frame episode you have paid for a full copy just to
read it in the other direction.

**What it buys you.** Backwards traversal with **no copy**, and it says what it
means at the point of reading.

It needs a **sequence** — an ordered container you can index with `[]`. List,
tuple, str. That is the `subscriptable` idea.

```python
path = ["home", "pick", "lift", "place"]

print(reversed(path))
print(list(reversed(path)))
print(path)

for step in reversed(path):
    print(step)
```

```
<list_reverseiterator object at 0x7c8037cf4b20>
['place', 'lift', 'pick', 'home']
['home', 'pick', 'lift', 'place']
place
lift
pick
home
```

Line 1 is the trap: **`reversed()` does not hand you a list.** Printing an
iterator prints the object. Line 3 proves the original is untouched.

**⚠ THE PAIR THAT MUST BE LEARNED AS A PAIR:**

| | what it is | mutates? | hands back |
|---|---|---|---|
| `steps.reverse()` | a **method on the list** | **yes** | `None` |
| `reversed(steps)` | a **built-in function** | **no** | an iterator |

To get a reversed list without touching the original: `list(reversed(steps))`.

### 1.3 The mutating tell — re-taught, in three parts

This row was **demoted this session**. It has now been broken three times in two
sessions, each time in a different direction, because it keeps getting rebuilt
as a **two-way** rule. It is not.

**1. TYPE FIRST.** On an **immutable** object, mutation is not on the table.
Anything that appears to change a `str` must be handing back a new object.

**2. THE TELL:**

> **returns `None` ⇒ it mutated.**

Because handing back `None` has no other purpose. If the method had something
useful to give you, it would have given it.

**3. THE DIRECTION IT DOES NOT RUN.** A value coming back is **not** proof the
object was left alone. `.pop()` hands you the item **and** mutates.

```python
path = ["home", "pick", "lift", "place"]

print(path.reverse())        # mutates
print(path.count("home"))    # reads
print(path.pop())            # mutates AND returns
print(path)

name = "elbow"
print(name.upper())          # immutable type
print(name)
```

```
None
1
home
['place', 'lift', 'pick']
ELBOW
elbow
```

`None` told you `reverse` mutated. `1` told you **nothing** about `count`.
`home` told you **nothing** about `pop` — and `pop` mutated anyway.

**Why no roster is given:** the discriminator predicts methods you have never
met. That is Level 2, and it is the whole point.

**`.count(x)`** — counts how many times `x` appears in the sequence, hands back
an `int`, changes nothing. A method, on a mutable object, that does not mutate.

### 1.4 Pitfall 1 — never mutate a container while iterating it

```python
angles = [10, 200, 250, 30]

for a in angles:
    if a > 180:
        angles.remove(a)

print(angles)          # [10, 250, 30]   <-- 250 SURVIVED
```

A `for` over a list keeps an internal **position counter**. It does not know the
list is changing underneath it.

| counter | list at that moment | `a` | action |
|---|---|---|---|
| 0 | `[10, 200, 250, 30]` | `10` | keep |
| 1 | `[10, 200, 250, 30]` | `200` | **remove** → `[10, 250, 30]` |
| 2 | `[10, 250, 30]` | `30` | keep |
| 3 | length is 3 → **loop stops** |

When `200` left, **`250` slid down into index 1** — a slot already passed.

**⚠ AND IT HIDES.** The same code on `[10, 200, 30, 250, 50]` returns
`[10, 30, 50]` — the correct answer. It skipped **two** elements there as well;
both happened to be keepers. **The bug was always present and the data hid it.**

**The pattern that replaces it — don't remove, SELECT:**

```python
angles = [a for a in angles if a <= 180]
```

Build a new list of what you want to keep and rebind the name. Nothing mutates
while it is being read.

### 1.5 `*` on a sequence, and the shared-row trap

**`seq * n` builds a new sequence with `seq`'s contents repeated `n` times.**
Same `*` character; on a sequence it means *repeat*, not *multiply*.

```python
print([0] * 5)        # [0, 0, 0, 0, 0]
print(["home"] * 3)   # ['home', 'home', 'home']
print("ab" * 3)       # ababab
print([1, 2] * 2)     # [1, 2, 1, 2]
```

```python
grid = [[0] * 3] * 3
grid[0][0] = 99
print(grid)
print(grid[0] is grid[1])

good = [[0] * 3 for _ in range(3)]
good[0][0] = 99
print(good)
print(good[0] is good[1])
```

```
[[99, 0, 0], [99, 0, 0], [99, 0, 0]]
True
[[99, 0, 0], [0, 0, 0], [0, 0, 0]]
False
```

**`*` repeats the REFERENCE, not the contents** — the same machinery as
`dict(defaults)`. New outer list; three slots pointing at **one** inner list.

**The discriminator:**

> **`* n` is SAFE when the element is immutable, and a TRAP when it is mutable.**

`[0] * 3` is fine because you cannot mutate a `0`, so sharing it is invisible —
the same fact as *"for a flat container of immutables, a shallow copy is
indistinguishable from a real copy."* `[[0] * 3] * 3` is not fine, because a
list can be mutated in place and `grid[0][0] = 99` reaches through and does it.

**The fix is a comprehension**, because the expression `[0] * 3` **re-runs once
per pass**, while `*` evaluates its operand once and repeats the result.

**`_`** is an ordinary variable name, used by convention to mean *"I am not
going to use this value."* Nothing special about it.

### 1.6 Pitfall 3 — when to use which container

**The four containers hold the same objects. They differ in what they make
CHEAP.** Pick wrong and the code still works; it just does far more work than it
needed to, invisibly, until the data gets big.

> ### **"What am I going to ASK this container?"**

Not *what am I putting in it*. What am I going to **ask it**, repeatedly, once
it is built.

| The question you will ask it | The container |
|---|---|
| *"Is this thing in here?"* | **set** |
| *"What is the value **for** this name?"* | **dict** |
| *"What came first? What is at position 3?"* | **list** |
| *"This must never change"* | **tuple** |

**The tell for a set:** you are storing keys with nothing on the other side. A
dict with the values thrown away **is** a set.

---

## 2. THE DRILL — `drills/s33_copies.py`

Four bodies, 25 mentor-written tests, **25/25 cold and unaided**, written the
morning after it was issued.

```python
import copy   # (belongs at the top of the file, not inside the function)

def snapshot(config):
    return copy.deepcopy(config)

def drop_unsafe(angles, ceiling):
    return [a for a in angles if a <= ceiling]

def replay_order(steps):
    return list(reversed(steps))        # <-- what was owed
    # written as: [steps[-(i+1)] for i in range(len(steps))]

def missing_joints(required, present):
    return set(required) - set(present)
```

**The boundary was deliberately kept out of the docstring and put in the tests.**
He found it anyway, off the promise — *"boundary is one thing I needed to take
care of, `<=` or `<`, otherwise `mila` would have come into action."*

---

## 3. THINKING GAPS THIS SESSION (with error-type classification)

| # | Gap | Type | Detail |
|---|---|---|---|
| 1 | **The mutating tell stated as a two-way rule, then not at all** | **Structural flaw** | *"A method on a mutable object mutates the object"* is false; `.count()` disproves it. Then, asked to restate the tell, he could not produce it. **THIRD BREAK IN TWO SESSIONS, three different directions.** He keeps rebuilding a one-directional rule as bidirectional. **Row demoted `[x]` → `[~]`.** |
| 2 | **`reversed()` not reached for, nine hours after being taught** | **Knowledge gap — LABEL, specifically a NAME COLLISION** | *"Couldn't use reverse because it mutates the list itself."* He described `steps.reverse()` and applied it to `reversed(steps)`. Machinery intact — his code is correct — and the tool was invisible behind a near-identical name. |
| 3 | **`range(len(...))` index bookkeeping** | **Habit** | Second occurrence; S29 caught the same shape and `zip` removed it there. When he computes indices to reach items, a built-in usually hands him the items. |
| 4 | **"Converts it to a dictionary"** | **Knowledge gap — LABEL** | Constructor vs type conversion. He produced the right mechanism only after the mentor pointed at the word. **Row held `[~]` deliberately.** |
| 5 | **Honest gap on `.count()`** | **Knowledge gap, declared** | *"I don't remember this method."* Not penalised — declaring the gap is the wanted behaviour. Feeds the list-roster row, still 3/6. |
| 6 | **"The iterable was empty"** | **Channel-adjacent label slip — SELF-REPAIRED** | Corrected himself unprompted to the iterator's forward-only state, and classified it precisely: *"not an error in my concept, was an error in saying."* |
| 7 | **`ek` and `bahar` both loose** | **Knowledge gap — partial** | `ek` given as "the number 1" (it is the smallest **non-empty case**); `bahar` given as sign only (it covers **TYPE** as well). |
| 8 | **Predicted the mutate-while-iterating bug wrong on the failing data** | **[PREDICT] — not ledger-eligible** | Reasoned from intent rather than tracing. Recovered on the counter trace. |
| 9 | **Three scenarios answered as one design** | **Comprehension — but caused by a missing frame** | See teaching mistake 2. Two thirds of the answer was correct. |

---

## 4. TEACHING MISTAKES THIS SESSION

| # | Mistake | Type | What it cost, and the fix |
|---|---|---|---|
| 1 | **`*` on a sequence used in a [PREDICT] having never been taught** | **DEFINE BEFORE USE, SUBSTRATE INCLUDED — TENTH OCCURRENCE, second night running** | He stopped it. The notes and curriculum were grepped rather than argued with; he was right; the snippet was withdrawn and repetition taught properly first. **Pushback 55, upheld in full. The check costs one command.** |
| 2 | **When-to-use-which fired as show-and-ask with NO FRAME** | **FRAME FIRST (RULES v4) breached** | He said *"I don't understand the question itself"*; the mentor **rephrased** — the wrong fix — and only after a second *"I still don't understand"* did it stop and state the unit in one sentence. **Two "I don't understand" replies in a row is a FRAME signal, not a comprehension signal.** Same first-fix-solves-the-wrong-half shape as S19 and S20. |
| 3 | **"That closes 1.8" — said in session, and false** | **Over-claim about the student's own progress** | Five bullets remain `[~]`. Caught during the closing procedure by counting them, and corrected to his face before any file was written. **The exact class the end-of-session section names: missing gets noticed, wrong gets believed.** |
| 4 | **A [PREDICT] whose data hid the bug it was meant to expose** | **Instrument design** | `[10, 200, 30, 250, 50]` genuinely returns the right answer, so his correct prediction measured nothing. Recovered by making the hiding *itself* the lesson — better teaching than the original plan — **but it was luck. Choose failing data deliberately.** |

---

## 5. REFERENCE CHECKLIST

| Name | What it DOES | The TRAP in it |
|---|---|---|
| `copy.deepcopy(x)` | new outer container **and** new contents, recursively | not "the better copy" — slower, and buys nothing on a flat container of immutables |
| `import copy` | binds the NAME to a **module object** | the `.` is an ordinary attribute lookup, nothing special |
| `reversed(x)` | **built-in**; returns an **iterator** back-to-front; mutates nothing | it is not a list — `print(reversed(x))` shows the object; and it exhausts |
| `x.reverse()` | **method**; mutates in place | returns `None`. **Merging it with `reversed()` is the S33 miss** |
| the mutating tell | returns `None` ⇒ it mutated | **ONE-DIRECTIONAL.** A value back tells you NOTHING — `.pop()` returns *and* mutates |
| `.count(x)` | counts occurrences, returns an `int` | a method on a mutable object that does **not** mutate |
| mutate-while-iterating | `for` holds a position counter | it does not raise — it silently skips, and on friendly data it returns the right answer |
| don't remove, SELECT | `[a for a in angles if a <= 180]` | rebinding the name, not mutating the list, is what makes it safe |
| `seq * n` | new sequence, contents repeated | **repeats the REFERENCE.** Safe for immutables, a trap for mutables |
| `[[0] * 3 for _ in range(3)]` | genuinely independent rows | the expression re-runs per pass; `*` evaluates once |
| `_` | an ordinary name | convention only: "I will not use this value" |
| the ASK question | *"what am I going to ask this container?"* | it is not *what am I putting in it* |
| set difference `-` | `set(a) - set(b)` builds a NEW set | it is an **expression**, and it is **not symmetric** |
| the five checks | boundary · khaali · ek · bahar · mila | **`ek` = smallest NON-EMPTY case. `bahar` = TYPE as well as sign.** They are the GATE on the word "done" |
| format spec alignment | text hugs **left**, numbers hug **right** | the number is TOTAL FIELD WIDTH, not padding |
| `None` vs nothing | `len([None]) == 1`, `len([]) == 0` | `None` is an object and fills a slot |

---

## 6. WHAT IS COMING NEXT

**1.8 is at ~98% and did NOT close.** Five bullets remain `[~]`, and all five are
cold-ask shaped rather than teaching shaped: `list` (method roster), `tuple`,
`dict` (`.keys()`/`.values()` as views), `set` (order instability, `{}` is a
dict), and when-to-use-which. **One focused block closes the subsection.**

**Then 1.9 — Error Handling**, where the overdue error-label work (`SyntaxError`,
`AttributeError`, the four-station hook by name) is not revision bolted on the
front but the subsection's own substrate.

**And the August gauntlet is the last session of the month. Only 30 and 31
remain.**
