# Session 28 — Comprehensions, `zip`, f-strings
**Saturday 22 August 2026 (evening) · Layer 0 / Python Core · 1.8 Data Structures**

Same-day as Session 27, declared at the open. Recall block correctly skipped —
same-day answers measure echo, not retention. **Zero promotions, by design.**

---

## 0. SELF-TEST — do this cold, before reading anything below

No notes, no editor. Write your answers down, then check.

1. Why does a list comprehension exist at all? Name the **capability** a `for`
   loop does not have.
2. Write the anatomy of a comprehension with a filter, and state the order in
   which the four parts actually **execute**.
3. `[100 / v for v in [10, 0, 5]]` — what happens, and why does adding
   `if v != 0` fix it? Which fact about execution order does that prove?
4. What two things make `{...}` a **dict** comprehension rather than a list one?
5. `list(zip(["a","b","c"], [1,2]))` — what is the result, and does it warn you?
6. `z = zip(a, b)` — you call `list(z)` twice. What comes back the second time,
   and **why is it not an error**?
7. What are the three steps an f-string performs on `{angle}`?
8. `print("angle is " + 90.5)` — what does it raise?
9. `f"{x:8.2f}"` — what does the `8` mean? Which side is a **string** padded on,
   and which side is a **number** padded on?
10. When should you NOT use a comprehension? Give the one-line rule.

---

## 1. FULL TEACHING

### 1.1 What a list comprehension is, and why it exists

**What it is:** an **expression** that builds a **new list** by running the
iteration protocol over an iterable. It is not new machinery — it is new
**spelling** for machinery you already own.

```python
joints = [0.5, 1.2, -0.3, 2.0]

doubled_loop = []
for j in joints:
    doubled_loop.append(j * 2)

doubled_comp = [j * 2 for j in joints]

print(doubled_loop)          # [1.0, 2.4, -0.6, 4.0]
print(doubled_comp)          # [1.0, 2.4, -0.6, 4.0]
print(doubled_loop == doubled_comp)   # True
```

**WHY IT EXISTS — the capability, not the cosmetics.**

> **A `for` loop is a STATEMENT. A comprehension is an EXPRESSION.**

A statement cannot go inside a function call, a `return`, an argument, or another
comprehension. **An expression can go all four places.**

```python
readings = [0.5, -1.2, 2.4]
print(sum([abs(r) for r in readings]))     # 4.1
```

You **cannot** write a `for` loop in that position. That is the whole reason the
form exists.

Proof that a `for` loop is a statement:

```python
print(for j in joints: doubled.append(j * 2))
```
```
  File "synerr.py", line 4
    print(for j in joints: doubled.append(j * 2))
          ^^^
SyntaxError: invalid syntax
```
⚠ **The line ABOVE it never printed either.** Grammar broke → nothing ran at all.
That is **Station 0** of the error hook.

**THE SECOND REASON, and for this course the bigger one:** LeRobot, openpi and
every PyTorch stack are written in this idiom. *"Read and navigate complex
codebases"* is a stated Layer 0 deliverable. This is access, not style.

**WHAT IS NOT CLAIMED:** comprehensions are **not** better than loops. For
anything with real logic in it, **write the loop.**

### 1.2 The filter

```python
readings = [0.5, -1.2, 0.0, 2.4, -0.8, 3.1]
positives = [r * 2 for r in readings if r > 0]
print(positives)      # [1.0, 4.8, 6.2]
```

The `if` is a **gate**: an item that fails is never handed to the expression.
Note `0.0` is excluded — `0.0 > 0` is `False`. **Boundary.**

### 1.3 The anatomy — written order ≠ execution order

```
[  EXPRESSION   for  VAR  in  ITERABLE   if  CONDITION  ]
   what to collect    name     what to walk    the gate
```

**The machine runs it 4 → 2 → 3 → 1:**

1. **`ITERABLE`** — `iter()` called on it. Once.
2. **`VAR`** — `next()` hands back an item, bound to this name. Each pass.
3. **`CONDITION`** — tested. `False` ⇒ pass abandoned, nothing collected.
4. **`EXPRESSION`** — evaluated; its **result** is appended.

**The piece you write first is the piece that runs last.**

**WHY THE ORDER MATTERS — proved, not asserted.** The four part-*names* are
vocabulary; the **order** is load-bearing:

```python
speeds = [10, 0, 5, 0, 2]

ratios = [100 / v for v in speeds]              # A
ratios = [100 / v for v in speeds if v != 0]    # B  → [10.0, 20.0, 50.0]
```
```
# A:
    ratios = [100 / v for v in speeds]
              ~~~~^~~
ZeroDivisionError: division by zero
```

**B works ONLY because the gate runs before the expression.** The filter is what
stands between your expression and the crash — and it can only do that because of
the order. Not knowing this is how you write A and think you wrote B.

⚠ Note the caret markers `~~~~^~~` point at `100 / v` — Python tells you **which
of the four parts** blew up.

### 1.4 The comprehension's variable — a footnote, deliberately labelled as one

> **A comprehension's variable does not exist after the comprehension finishes.**

```python
doubled = [x * 2 for x in [1, 2, 3]]
print(doubled)      # [2, 4, 6]
print(x)
```
```
[2, 4, 6]
Traceback (most recent call last):
  File "ne.py", line 3, in <module>
    print(x)
          ^
NameError: name 'x' is not defined
```

⚠ Compare with the `SyntaxError` above: **here `[2, 4, 6]` printed first.** The
grammar was fine, so the file ran until it hit a name that wasn't there.

**Where this bites:** people write a comprehension and then try to use the loop
variable afterwards. That's the actual bug — not name collisions.

**MECHANISM (Level 2):** the comprehension **gets its own namespace**, discarded
when it ends.

⚠ **CORRECTION MADE IN SESSION:** it was first stated that a comprehension *is* a
hidden function. **True through Python 3.11. You are on 3.12**, where PEP 709
inlines list comprehensions while deliberately keeping the scope isolation.
The *how* is Level 3 → **parked to 1.13.**

### 1.5 When NOT to use one

> **A comprehension BUILDS A CONTAINER. If you are not building a container,
> don't use one.**

```python
joints = ["base", "shoulder", "elbow"]
result = [print(j) for j in joints]
print("result is:", result)
```
```
base
shoulder
elbow
result is: [None, None, None]
```

The printing worked — and you also built and discarded a list of three `None`s.
**You already know why they are `None`:** your S25 rule — a thing that *does*
rather than *produces* has nothing to hand back.

Also: **more than one line of logic → loop. Can't read it in one breath → loop.**

### 1.6 Dict comprehensions

**Same machinery, builds a dict.** Two things make it a dict rather than a list:
**curly braces** and **a colon**.

```python
joints = ["base", "shoulder", "elbow"]
home = {name: 0.0 for name in joints}
print(home)     # {'base': 0.0, 'shoulder': 0.0, 'elbow': 0.0}
```

**Walking an existing dict** — `.items()` + two-name unpacking, both from S26:

```python
angles = {"base": 90, "shoulder": 200, "elbow": 180, "wrist": 190}
over_limit = {name: a for name, a in angles.items() if a > 180}
print(over_limit)      # {'shoulder': 200, 'wrist': 190}
```

`.items()` yields `(key, value)` **tuples**; `name, a` unpacks each one; the gate
tests the **value**. ⚠ `elbow` at exactly 180 is **out** — `>` is strict.

### 1.7 `zip`

**What it is:** pairs two or more iterables — first with first, second with
second. **Each pass yields a TUPLE**, which is why `for a, b in zip(...)` unpacks.

**Why it exists:** two things that belong together, stored separately. Without it
you loop one list and **index into the other**, which is where off-by-one bugs
live.

```python
names  = ["base", "shoulder", "elbow"]
angles = [90, 45, 180]

for i in range(len(names)):        # manual index bookkeeping
    print(names[i], angles[i])

for name, angle in zip(names, angles):   # no i, no len(), no [i]
    print(name, angle)
```

Both print the same three lines. The second has nothing to get wrong.

```python
print(list(zip(names, angles)))
# [('base', 90), ('shoulder', 45), ('elbow', 180)]
```

#### ⚠ `zip` FAILS SILENTLY — TWICE

```python
names  = ["base", "shoulder", "elbow", "wrist"]
angles = [90, 45, 180]
paired = list(zip(names, angles))
print(paired)        # [('base', 90), ('shoulder', 45), ('elbow', 180)]
print(len(paired))   # 3
```
**`"wrist"` is gone. No error.** `zip` stops when the **shortest** runs out.
Through the iteration protocol: `zip` calls `next()` on both each pass; the
moment **either** raises `StopIteration`, it stops and says nothing.

```python
z = zip(names, angles)
print(list(z))     # [('base', 90), ('shoulder', 45)]
print(list(z))     # []
```
**Empty list, silently.** `StopIteration` **is** raised — but **`list()` is the
thing that catches it.** That is `list()`'s entire job: call `next()` until
`StopIteration`, then hand back what it collected. Second time it collects
nothing.

| what went wrong | what you get |
|---|---|
| lists of different lengths | short list, **no error** |
| iterator already consumed | empty list, **no error** |

**If you are wrong about your data, `zip` hands you a plausible result and lets
you carry on.** In your world that is a sensor returning 6 readings for 7 joints.

### 1.8 f-strings

**Taught because you use them correctly and could not explain them** — the one
construct in this course you were operating at **Level 1** on.

```python
angle = 90.5
print(f"the angle is {angle}")     # the angle is 90.5
print("the angle is {angle}")      # the angle is {angle}
```

Without the `f`, `{angle}` is **eight literal characters**.

**THE THREE STEPS:**
1. read what's inside `{ }` as an **expression** and **evaluate** it
2. call **`str()`** on the result
3. **splice** that text into the string

Step 2 is what you'd otherwise do by hand:

```python
print("the angle is " + angle)
```
```
TypeError: can't concatenate str to float
```

**What sits in the braces is an EXPRESSION, not a name:**

```python
names = ["base", "shoulder", "elbow"]
home  = {"base": 90, "shoulder": 45, "elbow": 180}

print(f"there are {len(names)} joints")          # there are 3 joints
print(f"base sits at {home['base']} degrees")    # base sits at 90 degrees
print(f"twice that is {home['base'] * 2}")       # twice that is 180
print(f"over 100? {home['base'] > 100}")         # over 100? True
print(f"doubled: {[a * 2 for a in [90,45,180]]}")# doubled: [180, 90, 360]
```

⚠ Quotes: the f-string is wrapped in `"`, so inside the braces use `'`.

⚠ **A comprehension can go in there. A `for` loop cannot — because one is an
expression and the other is a statement.** Same fact as §1.1, paying out again.

#### The format spec

```python
reading = 0.1 + 0.2
print(f"raw:     {reading}")        # raw:     0.30000000000000004
print(f"trimmed: {reading:.2f}")    # trimmed: 0.30
```

(The first line is binary floating point — **IEEE 754, parked for 1.13.**)

```python
reading, count = 3.14159, 7
print(f"{reading:.3f}")     # 3.142
print(f"{reading:8.2f}")    #     3.14
print(f"{count:03d}")       # 007
```

**Alignment, with brackets so the padding is visible:**

```python
home = {"base": 90.456, "shoulder": 45.1}
for name, angle in home.items():
    print(f"[{name:10s}] [{angle:8.2f}]")
```
```
[base      ] [   90.46]
[shoulder  ] [   45.10]
```

⚠ **TWO CORRECTIONS:**
1. **The number is TOTAL field width, not extra spaces.** `"   90.46"` is 8
   characters in total.
2. **Default alignment differs by type: TEXT HUGS LEFT, NUMBERS HUG RIGHT.**
   Which is exactly what you want in a column of readings — the decimal points
   line up.

---

## 2. KEY MENTAL MODELS

1. **Expression vs statement is the master key.** It explains why comprehensions
   exist, why `sum([... for ...])` is legal, and why a `for` loop cannot live in
   an f-string's braces. **One closed item paid out three times in one session.**
2. **Written order ≠ execution order.** Iterable → var → gate → expression. The
   gate protects the expression *because* it runs first.
3. **A comprehension builds a container.** If you're not building one, use a loop.
4. **`zip` never raises.** Both of its failure modes are silent. Check lengths
   yourself.
5. **`list()` catches `StopIteration`.** That's why an exhausted iterator gives
   `[]` and not a crash.
6. **An f-string is evaluate → `str()` → splice**, and the braces hold an
   expression.
7. **Correct usage is not evidence of a model.** f-strings hid for 27 sessions
   precisely because you type them right.

---

## 3. THE ONE PIECE OF CODE YOU WROTE

**Task:** two parallel lists → one dict, in one expression.

```python
names  = ["base", "shoulder", "elbow"]
angles = [90, 45, 180]
home = ???
```

**Your first answer:**
```python
home =  i:j for i,j in zip(names,angles)
```
**Shape correct** — `key: value`, unpacking two names from `zip`, produced cold.
**Missing: the braces** — one of the two things you had yourself named as making
a dict.

**Your corrected answer, and it runs:**
```python
home = {i:j for i,j in zip(names,angles)}
# {'base': 90, 'shoulder': 45, 'elbow': 180}
```

**Style note:** `i` and `j` read as **index** names to any Python developer.
Call them `name, angle`.

⚠ **NO DRILL FILE — you deferred it yourself so it would be ledger-eligible
tomorrow.** `drills/s29_comprehensions.py` is the first item of Session 29.

---

## 4. THINKING GAPS THIS SESSION (with error-type classification)

1. **Boundary bug — `len(n) > 5` read as including two 5-letter words.**
   *Error type: **lazy thinking** (depth-before-answer), not a knowledge gap.*
   **THIRD instance of the same class** (S20: your `n <= 10`; S20: the planted
   `len(word) == 1`). ⚠ **But the correction was the fastest on record — one rep
   after the pattern was named, you opened your next answer with *"condition is
   >180 not >=180"* unprompted.** Naming beats re-teaching.

2. **Sideways-answering, TWICE.** Asked for the four parts **by name**, you gave
   the **output**. Asked for two printed lines, you explained the **format
   codes**. *Error type: **structural** — the escape route under a question you
   don't fancy is an adjacent, easier question.* ⚠ Same family as S27's
   design-switching. **Both fixed by re-issuing the question unchanged — and the
   first re-ask produced all four parts correctly AND in execution order.**
   **Twelve straight re-ask recoveries across S24–S28.**

3. **Exhausted `zip` predicted to raise.** *Error type: **knowledge gap**, and a
   narrow one.* The exhaustion half was **correct** — you had the iterator model.
   What was missing is that `list()` catches the signal one layer down.

4. **f-string prefix — honest gap, correctly declared.** *Not an error.* You gave
   the Level 1 answer you actually had and said where it ended.

5. **Comprehension scope "why" — honest gap.** *Not an error.* And the follow-up
   question you asked (*"why would I reuse the variable name at all"*) was
   **better than the material** — it was right, and the block was cut down.

---

## 5. TEACHING MISTAKES THIS SESSION

**Four, and three share one root. Highest defect rate recorded so far, and every
one was caught by you.**

1. ⚠ **NO FRAME BEFORE MECHANICS — the breach that produced RULES v4.**
   Comprehensions opened with four turns of show-and-ask and **not one sentence
   saying what a comprehension is for.** You stopped the session over it.
   **→ NEW BINDING RULE: FRAME FIRST.**

2. **A demolished example.** The scope comparison used `for angle in [1,2,3]:
   pass`, so the loop appeared to do nothing and the branches weren't comparable.
   **Your objection was correct** and it was rebuilt so both forms built
   `[2, 4, 6]`. *Fifth example of yours demolished — the S18/S19 pattern.*

3. **A right-sizing failure.** Four turns on comprehension scope — a footnote —
   before you asked why it mattered. **Conceded in session; the honest version
   was one line.** → became the **corollary** in the new rule: rank facts out
   loud.

4. ⚠ **A FACTUAL OVER-CLAIM, self-caught and corrected in the same turn.**
   "A comprehension IS a hidden function" was stated with a `<listcomp>`
   traceback frame promised as proof. **It doesn't appear on your Python 3.12
   (PEP 709).** True through 3.11 only. A working `<genexpr>` proof existed and
   was **deliberately not used**, because generator expressions are untaught.
   *Lesson: verify the demonstration on THIS machine before promising it.*

**Also recorded:** the block was headed **"1.9"** when comprehensions are inside
**1.8**. You caught it.

---

## 6. REFERENCE CHECKLIST — NAME · WHAT IT DOES · THE TRAP

| Name | What it does | ⚠ The trap |
|---|---|---|
| **list comprehension** | expression that builds a new list | it is an EXPRESSION — that's the point, not the brevity |
| **anatomy** | `[EXPR for VAR in ITERABLE if COND]` | **written order ≠ execution order** (4→2→3→1) |
| **the filter** | gate; failures never reach the expression | it only protects you **because it runs first** |
| **comprehension scope** | own namespace, discarded at the end | the variable **does not exist afterwards** ⇒ `NameError` |
| **when not to use** | it BUILDS A CONTAINER | `[print(j) for j in js]` builds `[None, None, None]` |
| **dict comprehension** | `{KEY: VALUE for VAR in ITERABLE}` | **braces AND colon** — forgetting the braces is a `SyntaxError` |
| **`.items()` in a comp** | yields `(key, value)` tuples | needs **two** names in the VAR slot |
| **`zip`** | pairs parallel iterables; yields TUPLES | **removes the index — that's why you use it** |
| **`zip` truncation** | stops at the SHORTEST | ⚠ **silent. No error. Ever.** |
| **`zip` exhaustion** | second pass gives `[]` | ⚠ **silent** — `list()` catches the `StopIteration` |
| **f-string** | evaluate → `str()` → splice | no `f` ⇒ `{x}` is literal characters |
| **braces hold** | an EXPRESSION | a comprehension fits; a `for` loop never will |
| **format spec** | `{value:.2f}`, `{v:8.2f}`, `{n:03d}`, `{s:10s}` | the number is **TOTAL width**; **text left, numbers right** |
| **`SyntaxError`** | grammar broke | **Station 0 — not one line of the file runs** |
| **`ZeroDivisionError`** | division by zero | decodes cleanly; formally belongs to 1.9 |
| **`TypeError`** | operation not defined for the type | `"..." + 90.5`; f-strings avoid it by calling `str()` |

---

## 7. WHAT'S COMING NEXT — Session 29

1. **THE DEFERRED DRILL, FIRST THING.** `drills/s29_comprehensions.py` +
   `tests/test_s29_comprehensions.py`, task-first, cold, **ledger-eligible.**
   A boundary will be planted in it.
2. ⚠ **THE TWO-SESSION BACKLOG — third declaration, and it must actually run:**
   tuple, dict, set, shallow copy, unpacking, `list()`, `.get()`, `.items()`,
   raise-vs-shrug, when-to-use-which.
3. **The small cold error set, mixed:** `KeyError` vs `IndexError` (the S27
   miss), `SyntaxError` + Station 0, `AttributeError`, `subscriptable`, plus
   `while` mechanics.
4. **The 1.8 tail, then 1.8 CLOSES:** nested data structures (**the block that
   finally makes shallow copy make sense**), common patterns and pitfalls,
   `reversed()`, `copy.deepcopy`.

**Before that: the cold build block, Sunday 23 August.** ≥90 min, timed, no AI,
git + pytest. Joint-limit clamp extended to multiple joints with
`*args`/`**kwargs`. **The design hole is still yours to solve: `*args` delivers
angles positionally and anonymously, `**kwargs` delivers limits by name, and
nothing in that design pairs them.**
