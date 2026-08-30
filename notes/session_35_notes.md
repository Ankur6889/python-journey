# Session 35 — 1.9 Error Handling (opened)
**Sunday 30 August 2026** · ~4 hours · `drills/s35_faults.py` **29/29 first run**

---

## 0. SELF-TEST — do this cold, before reading anything below

No notes, no scrolling. Say the answer out loud, then check.

1. A file's line 5 is missing a colon. Line 1 is `print("hello")`. What appears
   on screen when you run it?
2. Why does a `SyntaxError` traceback have no frames in it?
3. `a` and `b` are dicts. Write one expression giving the keys in both, without
   calling `set()`.
4. What does `a.keys()` **build**?
5. What does `reversed(x)` hand back? Does it sort?
6. `d.clear()` empties a dict. What does it hand back, and how do you know
   without running it?
7. When does `finally` run?
8. `except ValueError as e` — what is `e`?
9. What is the danger of `except:` with no exception type after it?
10. Change only the value and it works ⇒ which error? Change only the type and
    it works ⇒ which error?

---

## 1. FULL TEACHING

### 1.1 The instrument: **"HOW FAR DID PYTHON GET?"**

The four-station hook (NAAM → DOT → TYPE → CHEEZ) was **retired this session**.
It was five arbitrary words stacked on machinery you already own, and it did not
survive. It is replaced by a single question you ask the code:

> **How far did Python get before it stopped?**

Every error name is just an answer to that. It is a **timeline you walk**, not a
list you memorise:

| how far it got | what broke | error |
|---|---|---|
| did not even parse | grammar | `SyntaxError`, `IndentationError` |
| parsed, looked up a name, no name | the NAME | `NameError` |
| found the object, looked after the dot | the ATTRIBUTE | `AttributeError` |
| tried the operation, not defined for that type | the TYPE | `TypeError` |
| operation fine, this particular value is not | the VALUE / key / index | `ValueError`, `KeyError`, `IndexError` |

**A traceback is literally the record of how far Python got.**

### 1.2 Compile time vs run time — *your own derivation, confirmed*

Python **parses the entire file before executing a single line of it.**

```python
print("checking limits")

angles = {"elbow": 45, "wrist": 30}

for name in angles          # <-- missing colon
    print(name)
```
```
  File "syn.py", line 5
    for name in angles
                      ^
SyntaxError: expected ':'
```

**`checking limits` never printed.** Line 1 never had the chance to run.
And notice what is *missing*: there is **no `Traceback (most recent call last)`
line, no `<module>`, no frames** — because there was never a running program to
have frames.

**But the compiler only checks GRAMMAR, never MEANING.** A typo'd name compiles
perfectly:

```python
print("checking limits")
angles = {"elbow": 45}
print(rbot["joint"])         # rbot does not exist
```
```
checking limits                          <-- line 1 DID run
Traceback (most recent call last):
  File "names.py", line 5, in <module>
    print(rbot["joint"])
NameError: name 'rbot' is not defined
```

| stage | what is checked | errors |
|---|---|---|
| **compile** | grammar only | `SyntaxError`, `IndentationError` |
| **run** | everything else | `NameError`, `TypeError`, `KeyError`, `ValueError`, … |

> **THE TELL: `SyntaxError` is the only error you meet with no traceback frames.
> If you see frames, something ran.**

*(What the bytecode actually is, and `.pyc` — parked to 1.10.)*

### 1.3 `.keys()` is a **VIEW**

`a.keys()` does not return a list and does not return a set. It returns a
`dict_keys` object — **a live window onto the dict's keys.**

```python
a = {"shoulder": 90, "elbow": 45, "wrist": 30}
b = {"elbow": 60, "wrist": 15, "base": 180}

print(type(a.keys()))        # <class 'dict_keys'>
print(a.keys() & b.keys())   # {'wrist', 'elbow'}
print(a.keys() - b.keys())   # {'shoulder'}

v = a.keys()
a["gripper"] = 5
print(v)   # dict_keys(['shoulder', 'elbow', 'wrist', 'gripper'])  <-- LIVE
```

| | what it does | cost |
|---|---|---|
| `set(a)` | **BUILDS** a new set, copying every key | a full copy |
| `a.keys()` | **BUILDS NOTHING** — a window onto the dict's own keys | nothing |

Set operations work on a view directly because dict keys are unique and
hashable — which is what makes anything set-like. **And `&` is not "for sets
only": `&` works on any TYPE that defines it.** That is your `TypeError` rule
(*operation not defined for the type*) read forwards instead of backwards.

### 1.4 The collided-name table: `sorted` / `sort` / `reversed` / `reverse`

Python offers the same job in **two forms**, and they differ in exactly two ways
every time.

| | mutates the original? | hands back |
|---|---|---|
| `sorted(x)` — **function** | no | a **new list** |
| `x.sort()` — **method** | **yes** | **`None`** |
| `reversed(x)` — **function** | no | a **new iterator** |
| `x.reverse()` — **method** | **yes** | **`None`** |

**The third fact, and it is the one that broke in S34:** a mutating method hands
back `None` **because it has nothing useful to give you** — it already changed
your object. Returning `None` serves no other purpose, **so `None` coming back is
the proof that it mutated.**

**Two traps:**
- **`reversed()` does not ORDER, it REVERSES.** `["c","a","b"]` → `["b","a","c"]`.
- **`reversed()` does not hand back a list**, it hands back an **iterator** —
  which is why `print(reversed(x))` shows you an object, not values.

### 1.5 `try` / `except`

**WHAT:** run this; if it raises, run that instead of dying.

```python
readings = ["45", "90", "n/a", "30"]

total = 0
for r in readings:
    try:
        total += int(r)
    except ValueError:
        print("skipping bad reading:", r)

print("total:", total)     # 165
```

Without it, `int("n/a")` kills the loop and you lose the `45` and `90` you had
already counted, plus the `30` that was fine.

**WHEN NOT TO USE IT — the honest half.** Where you *can* check cheaply in
advance, you should: `.get()` beats `try` on a dict lookup. `try` earns its place
in exactly two situations:

1. **You cannot ask in advance.** There is no `"n/a".can_be_int()`. Checking a
   file exists and *then* opening it is a lie — it can vanish between the lines.
2. **The failure is deep.** The thing that breaks is five calls below you, and
   you cannot write an `if` around a possibility you cannot see from here.

### 1.6 Specific vs bare `except` — **the most important thing in this session**

Same file, one typo'd variable, two ways of "handling" it.

```python
    except ValueError:              # SPECIFIC
```
```
Traceback (most recent call last):
  File "t3.py", line 6, in <module>
    total += int(rdg)
NameError: name 'rdg' is not defined
```
Dies on the first reading. **Good.** The bug is screaming.

```python
    except:                         # BARE
```
```
skipping bad reading: 45
skipping bad reading: 90
skipping bad reading: n/a
skipping bad reading: 30
total: 0
```
**No crash. Exit code 0.** Two perfectly good readings reported as junk, and
`total: 0` handed back as if it were an answer.

> **THE RULE: catch the exception you are EXPECTING. Never catch everything.**
>
> `except ValueError:` says *"I know `int()` can fail on junk text and I have a
> plan."* Bare `except:` says *"whatever goes wrong, pretend it didn't"* —
> including the bugs you have not found yet.

**This is your own raise-vs-shrug rule one level up: shrug at what you expect,
let the unexpected raise.**

### 1.7 `raise` — and exception classes are **TYPES**

Python raises `ValueError` for `int("2.6")` because Python knows what an integer
looks like. **Python has no idea 200° is illegal for your shoulder joint.**

```python
def check_angle(angle, limit):
    if angle > limit:
        raise ValueError(f"angle {angle} exceeds limit {limit}")
    return angle
```

**The substrate, which had never been taught before this session:**

- **Every error name is a CLASS** — `ValueError`, `KeyError`, `TypeError` — just
  like `list` or `dict`.
- **`ValueError("...")` is a CONSTRUCTOR CALL.** It *builds* an exception object.
- **The text after the colon in every traceback you have ever read IS that
  constructor's argument:**

```
ValueError: invalid literal for int() with base 10: 'n/a'
^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
the TYPE     the string handed to the constructor
```

| | what it is | what it does |
|---|---|---|
| `ValueError("too big")` | an **expression** — a constructor call | **builds** an object |
| `raise <object>` | a **statement** | **throws** it |

**WHY IT EXISTS — the division of labour:**

```python
def check_angle(angle, limit):     # DETECTS
    ...
for a in readings:                 # DECIDES
    try:
        safe.append(check_angle(a, limit))
    except ValueError as e:
        print("rejected:", e)      # -> rejected: angle 200 exceeds limit 180
```

`check_angle` knows 200 is illegal. It does **not** know whether the right
response is skip, clamp, or abort — that depends on the caller.
**`raise` reports a problem upward without deciding the response.**

Returning `-1` or `None` instead is worse: the caller has to *remember* to check,
and if they forget, `None` goes straight into your data and poisons everything
downstream, silently.

**`except ValueError as e`** binds the **exception object itself** to `e` — the
same object the constructor built.

### 1.8 `else` and `finally`

**`finally` is load-bearing. `else` is a scoping tool worth about one line.**

| clause | when it runs |
|---|---|
| `try` | always attempted |
| `except` | only if a **matching** exception was raised |
| `else` | only if **no** exception was raised |
| `finally` | **always** |

**"Always" is stronger than it looks.** Here there is no `except` at all, and a
`return` is in the way:

```python
def read(text):
    try:
        return int(text)
    finally:
        print("  brake released")
```

```
read("45")                      read("n/a")
------------                    ------------
  brake released                  brake released
returns 45                        ValueError propagates, program dies
```

`finally` ran **on the way out through a `return`**, and **on the way out through
an uncaught exception that killed the program.** It also runs when the raised
exception matches no `except` clause you wrote.

**Why the cleanup cannot just go after the block:** an exception leaves the
function *before* reaching those lines. Cleanup in `finally` is not skipped.
Close the file. Release the brake. Disconnect the arm.

*(This is the seed of the `with` statement in 1.11.)*

**`else`** keeps the `try` down to the one line you actually meant to guard, so a
`ValueError` from an unrelated later line does not get swallowed and blamed on
your input. **`except X` narrows by TYPE; `else` narrows by SCOPE.** Same
instinct as not writing a bare `except`.

---

## 2. THE ASSIGNMENT — `drills/s35_faults.py`

Four functions, constraints only, 29 mentor-written tests. **29/29 on the first
run.** Also written: `drills/s35_check.py`, a runner that calls your functions
with the five-check cases and prints what came back.

**Your code, with the two things worth changing:**

```python
def total_valid(readings):
    filtered_readings = []
    for i in readings:
        try:
            filtered_readings.append(int(i))
        except:                 # <-- BARE. total_valid(["45", None]) -> 45, silently
            pass
    return sum(filtered_readings)


def check_angle(angle, limit):
    if angle > limit:
        raise ValueError(f"The angle :{angle:4.1f} should not be greater than {limit:4.1f}")
    return angle            # ^ why render an int reading as 200.0?


def safe_angles(readings, limit):
    checked_readings = []
    for r in readings:
        try:
            checked_readings.append(check_angle(r, limit))
        except ValueError as e:
            print(e)        # <-- a library function deciding the caller's output policy
    return checked_readings


def measure(text, log):
    try:
        return int(text)
    finally:
        log.append("closed")
        print(f"...")       # <-- leftover debug print
```

**What went right, and it is most of it:** `measure` correct after one pointing
question; `check_angle` raising rather than returning a sentinel; and
`safe_angles` holding **no second copy of the limit rule** — enforced by a test
that inspects the source, and it passed first run.

---

## 3. THINKING GAPS — with error-type classification

| # | gap | classification |
|---|---|---|
| 1 | **Wrote a bare `except:` forty minutes after correctly judging it the most dangerous option.** | ⚠⚠ **TRANSFER GAP — a new category for this file.** Not knowledge (it was live and correct in your mouth the same hour), not laziness. The idea did not survive the trip from PREDICT to PRODUCTION. |
| 2 | Could not recall the four-station hook at all. | **Artefact failure, not a student failure.** Logged against the tool; the tool was retired. |
| 3 | `SyntaxError`: said line 1 prints before the error. | **Knowledge gap**, on the load-bearing half of the row. And it was **rated 7** — first over-rating in a long while. |
| 4 | Called `1 + "a"` a `ValueError`. | **Decay**, self-diagnosed: *"old content, not being revised for long."* Recovered in full on one narrowing. |
| 5 | Reversed a correct answer because the mentor singled the case out. | **Structural** — the framing of a question is not evidence. Will cost you in an interview. |
| 6 | *"the program will pause"* for an uncaught exception. | **Language precision.** It **terminates**. Exit code 1. Nothing is waiting to resume. |

**What went right and should be said as loudly:** you derived the compile→run
split unprompted; you named your unknown on `.keys()` with real precision
(*"I don't know what the datatype of dict.keys() is"*); you refused to answer a
question built on undefined substrate; and you flagged `bahar`-by-TYPE on
`check_angle` without being asked.

---

## 4. TEACHING MISTAKES THIS SESSION

1. **Define-before-use, eleventh occurrence.** `raise ValueError(f"...")` was put
   in a [PREDICT] before exception classes had ever been defined as types.
   **You caught it and refused to answer — first time you have invoked the
   eligibility rule yourself.** Upheld in full.
2. **A defective snippet.** The first bare-`except:` example typo'd a variable as
   `reading`, one character from `readings`. It tested attention, not the
   concept. Re-posed with an unmistakable name.
3. **An accidental [TEACH-BACK] tag cost a promotion.** You said *"the constructor
   of the set **builds** the set object"* — the exact first word the
   `constructors` row has waited for since S33 — inside a block tagged
   [TEACH-BACK], which is never ledger-eligible. Not bankable. My tag, my cost.
4. **The five-checks ask was escalated past your own S24 ruling** (scan five,
   report the ones that bite). You objected, correctly. Fixed with a tool.
5. ⚠⚠ **The interval gate may have been ruled on the wrong date.** "Same sitting"
   was declared from a context header; every file mtime says Sunday 30 August.
   If so, S34's material was testable and was deferred for nothing.
   **No promotion is corrupted** — everything promoted was S27 material, seven
   days cold either way. **Verify the date from `git log` and mtimes, not from
   memory.**

---

## 5. REFERENCE CHECKLIST — name · what it does · the trap

| name | what it does | ⚠ the trap |
|---|---|---|
| `try` / `except` | run this; if it raises, run that instead of dying | it is not "safer code" — a `try` around a bug hides the bug |
| **bare `except:`** | catches **everything** | **turns a typo into a silent wrong answer with exit code 0** |
| `except X as e` | binds the exception **object** to `e` | `e` is an object, not a string; `str(e)` is the message |
| `else` (on a try) | runs only if the `try` did **not** raise | narrows by SCOPE, not by type |
| `finally` | runs on **every** way out | including through a `return` and through an **uncaught** exception |
| `raise` | throws an exception object | the function **detects**; the **caller decides** |
| `ValueError("...")` | a **constructor call** — builds an exception object | the error name is a **CLASS**, not a label |
| `SyntaxError` | grammar broke, so nothing ran | **no frames in the traceback** — and line 1 does **not** print |
| compile vs run | grammar checked for the whole file first | the compiler never checks whether a **name** exists |
| `.keys()` | a live **view** onto the dict's keys | it **builds nothing**; `set(a)` copies everything |
| `reversed(x)` | new **iterator**, reversed | it does **not** sort, and it is **not** a list |
| `x.reverse()` / `x.sort()` | mutate in place | hand back **`None`** — that is the tell |
| `ValueError` vs `TypeError` | which part broke | **change only the value and it works ⇒ ValueError; change only the type and it works ⇒ TypeError** |

---

## 6. WHAT'S NEXT (Session 36 — Monday 31 August)

1. Fix the bare `except:` in your own `total_valid`.
2. `.keys()` as a view, cold — **it closes the 1.8 `dict` bullet.**
3. `SyntaxError`'s no-frames half, cold.
4. Finish 1.9: custom exceptions, the exception hierarchy, exceptions as control
   flow (the iteration protocol *is* this), defensive programming.
5. **Tuesday 1 September: the August gauntlet.** Pure mixed recall, no new
   material, plus the re-baseline arithmetic.
