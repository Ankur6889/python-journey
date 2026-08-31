# Session 36 — 1.9 Error Handling (finished)
**Monday 31 August 2026** · ~11:00–23:30 · `drills/s36_signals.py` **35/35**
**RULES adopted to v6** · one promotion, one demotion, four bullets opened

---

## 0. SELF-TEST — do this cold, before reading anything below

No notes, no scrolling. Say the answer out loud, then check.

1. A file is 40 lines long. Lines 1–39 are ordinary working code. Line 40 is
   missing a colon. **How much of the file executes?**
2. What does `class OverLimit(Exception): pass` give you that `ValueError`
   doesn't?
3. You have four `except` blocks. Where does `except Exception` go, and what
   happens if you put it first?
4. What does a **bare** `raise` inside an `except` block do?
5. A re-raised exception — do the *other* `except` blocks on the same `try` get
   a chance at it?
6. Write out what `for x in box:` actually is, in terms of `iter`, `next` and
   `try`.
7. `next(it)` past the end of an iterator raises what? (Spell it exactly.)
8. Name the three ways a function can report a problem, and which one the caller
   cannot ignore.
9. `get_joint` returns `None` when a key is missing. What does that cost you?
10. What is worse than a bare `except:` — and why?

---

## 1. FULL TEACHING

### 1.1 The exception hierarchy — a family tree, not a flat list

The error names are **not** unrelated labels. They are a tree.

`ValueError`, `NameError`, `TypeError`, `KeyError`, `ZeroDivisionError` are all
**kinds of** `Exception` — its *children*, or *subclasses*.

That buys exactly one thing:

> **Naming an ancestor catches every descendant.**

```python
except Exception as e:
    print("caught:", e)
```

**What each part is worth** (rank facts out loud — S28 corollary):

| part | worth |
|---|---|
| the *word* `Exception` | cheap vocabulary |
| the *tree* | **load-bearing** — it is why `except ValueError` catches nothing else |
| `except Exception:` vs bare `except:` | a footnote; parked |

### 1.2 `except` ORDERING — specific first, general last

One `try` can carry several `except` blocks. **Python checks them top to bottom
and takes the first that matches. Then it stops.**

```python
class JointLimitError(Exception):
    pass

def check_angle(angle, limit):
    if angle > limit:
        raise JointLimitError(f"angle {angle} exceeds limit {limit}")
    return angle

def safe_angles(readings, limit):
    kept = []
    for r in readings:
        try:
            kept.append(check_angle(int(r), limit))
        except JointLimitError as e:
            print("SAFETY:", e)
        except ValueError as e:
            print("SENSOR:", e)
    return kept

print(safe_angles(["45", "90", "200", "n/a"], 180))
```

```
SAFETY: angle 200 exceeds limit 180
SENSOR: invalid literal for int() with base 10: 'n/a'
[45, 90]
```

Now move `except Exception` to the top:

```python
        except Exception as e:              # FIRST
            print("SENSOR:", e)
        except JointLimitError as e:        # SECOND
            print("SAFETY:", e)
```

```
SENSOR: angle 200 exceeds limit 180
SENSOR: invalid literal for int() with base 10: 'n/a'
[45, 90]
```

**The `except JointLimitError` block never ran. It is dead code. Python issued
no warning of any kind.**

> **THE RULE: specific first, general last — or the ancestor eats its own
> children.**

`except` blocks are **alternatives**, like `elif`. One runs, or none. Never two.

### 1.3 Custom exceptions — why they exist

The honest motivation is a **collision you can see**:

`int("n/a")` raises `ValueError`. Your own `raise ValueError(...)` in
`check_angle` raises `ValueError`. **One `except ValueError` cannot tell them
apart** — and they mean completely different things:

| reading | what actually happened | what it means |
|---|---|---|
| `"200"` | sensor works, number is out of range | **mechanical / safety** — the arm may be about to hit something |
| `"n/a"` | sensor sent no number at all | **hardware / comms** — you have gone blind on that joint |

Both vanished into the same bucket and the caller got a clean `[45, 90]`.

The fix is a type of your own:

```python
class OverLimit(Exception):
    pass
```

- **`class OverLimit(...)`** — creates a new *type* with that name. (Cheap. The
  real `class` unit is **1.11**; this one line is all exceptions need.)
- **`(Exception)`** — **load-bearing.** You are adding a leaf to the tree. This
  is what lets `raise` accept it and what keeps `except Exception` catching it.
- **`pass`** — the body needs nothing. It inherits everything, including
  message-carrying.

Ending the name in `Error` is convention only.

### 1.4 Re-raise — the middle position

`except` normally means *I am handling this, the caller never finds out*. But
often you want:

> *I want to **do something** about this — log it, close the gripper, flag it —
> but I am **not** the one who decides what happens next.*

That is a **bare `raise`** inside an `except` block:

```python
try:
    raise ValueError("boom")
except ValueError:
    print("first block ran")
    raise
except Exception as e:
    print("second block ran:", e)

print("after the try")
```

```
first block ran
Traceback (most recent call last):
  File "reraise.py", line 2, in <module>
    raise ValueError("boom")
ValueError: boom
```

**Two things to take from that output.**

1. **`except Exception` did NOT run.** It sits right there and it would match.
   > **Once Python enters an `except` block, that `try` is finished.** Anything
   > raised inside it goes **outward**, looking for an *enclosing* `try`. It is
   > never re-offered to the sibling blocks.
2. **The traceback says line 2, not line 5.** A bare `raise` re-throws the
   *original* exception with its *original* traceback — so it still points at
   where the fault actually happened, not at where you re-threw it. That is what
   it buys over `raise e`.

### 1.5 Exceptions as CONTROL FLOW — what a `for` loop really is

```python
it = iter(box)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # ...your loop body...
```

**Every `for` loop you have ever written catches an exception — on every
successful run — as its normal way of finishing.**

So "exceptions are for errors" is wrong. **An exception is a signal that
travels.** Whether it counts as an *error* is a judgement the **caller** makes,
not a property of the mechanism.

Spelling: **`StopIteration`**. Not "EndOfIteration". Re-derive it: the thing
that happens is that *iteration stops*, and Python named it in that order.

### 1.6 RAISE vs RETURN — the takeaway of 1.9

Three ways for a function to report a problem:

| | can the caller ignore it? |
|---|---|
| **return a value** (`None`, `-1`, `[]`) | **yes — silently** |
| **print** | yes — *and* you have stolen their output policy |
| **raise** | **no** |

> **A return value can be ignored. An exception cannot.**

**Proof, run live:**

```python
config = {"shoulder": 180, "elbow": 150, "wrist": 90}

def get_joint(config, name):
    if name not in config:
        return None
    return config[name]

angle = 200
limit = get_joint(config, "elbw")        # the typo
print("limit is:", limit)

if angle > limit:
    print("OVER LIMIT")
```

```
limit is: None
Traceback (most recent call last):
  File "sentinel.py", line 14, in <module>
    if angle > limit:
       ^^^^^^^^^^^^^
TypeError: '>' not supported between instances of 'int' and 'NoneType'
```

**It crashed on line 14. The mistake is on line 11.**

`get_joint` understood the problem perfectly (*this key doesn't exist*) and
reported it as `None` — a value the caller can carry around, store, pass on, and
only trip over much later in innocent code. Had it let `config["elbw"]` raise,
you would have got **`KeyError: 'elbw'` pointing at line 11**, naming the typo.

> **A sentinel return moves the failure away from its cause. `raise` keeps them
> together.**

**And the style corollary:** a library function that **prints** has decided its
caller's output policy for them. Maybe they wanted a log file, or silence, or a
robot with no terminal. Raise, or return, and let them choose.

---

## 2. THE ASSIGNMENT — `drills/s36_signals.py`

One type (`OverLimit`) and four functions: `check_limit`, `read_limit`,
`sort_faults`, `audited`. 35 tests. **Final: 35/35.**

His `sort_faults`, after the catch-all was removed:

```python
def sort_faults(readings, limit):
    state_dict = {"ok": [], "over": [], "broken": []}
    for r in readings:
        try:
            state_dict["ok"].append(check_limit(int(r), limit))
        except OverLimit:
            state_dict["over"].append(int(r))
        except ValueError:
            state_dict["broken"].append(r)
    return state_dict
```

His `audited` — the re-raise, correct first time:

```python
def audited(readings, limit, log):
    allowed = []
    for r in readings:
        try:
            allowed.append(check_limit(r, limit))
        except OverLimit:
            log.append("OVER")
            raise
    return allowed
```

**Got right first time:** `except Exception` ordered last; bare `raise`;
`check_limit` **called** rather than copied (no second copy of the rule);
`read_limit` raising with the joint named in the message.

---

## 3. THINKING GAPS THIS SESSION — with error-type classification

**1. THE CATCH-ALL IN FRESH CODE — *structural flaw / transfer gap*. The
headline.**
He passed both cold bare-`except:` recalls at 7/10, named the danger in his own
words, and fixed his own `total_valid`. **Then he shipped
`except Exception: state_dict["broken"].append(r)` in brand-new code the same
evening — ordered correctly, last.** He took the *ordering* lesson from ninety
minutes earlier and dropped the *catch-all* lesson from four hours earlier.
> **Not a knowledge gap. He does not lose the last thing taught — he loses the
> one before it.**
**And the sharpened version, which he derived himself once asked:** a bare
`except:` **hides** a fault; a catch-all filing into a **named** bucket actively
**lies** about one. `"broken"` means *this sensor sent garbage* — so a `NameError`
in his own code sends an engineer to swap a cable on a healthy sensor.

**2. TWO CONSECUTIVE IDENTIFIER MISSES — *lazy thinking*, and cheap to fix.**
The spec said `OverLimit`. He wrote `JointLimitError` (the name from the
teaching demo), then `OverLimitError` (the "convention" footnote applied over the
literal spec). **Two collection failures, zero tests run.**
> **Identifiers are not paraphrasable.** And note the shape: *the thing on
> screen five minutes ago beat the spec in front of him* — twice. Same mechanism
> as gap 1.

**3. `StopIteration` → "EndofIteration" — *knowledge gap, label only*. DEMOTED
[x] → [~].** After three weeks the mechanism was perfect (`10`, `20`, raise, and
the third `print` never runs) and **the word was gone.** His exact signature:
machinery holds, arbitrary label does not.

**4. THE ORDERING PREDICTION, MISSED FIRST TIME — *channel artefact, mostly*.**
*"The output will still be the same because the exception caught depends on the
inputs not on the try except block."* The swap had been described **in prose**,
and he rebuilt it without noticing that `print("SAFETY:")` moves *down* with its
block. **Re-posed as literal code, he got it immediately** — and supplied *"child
class"* from his own prior knowledge, flagging that it was his and not the
mentor's.

**5. RE-RAISE ROUTING — *knowledge gap*, caught and killed.** He believed a
re-raised exception is re-offered to the **sibling** `except` blocks. It is not.
Right outcome ("the program halts"), wrong mechanism — worth catching, because
the wrong model would have bitten later.

**6. `SyntaxError`, THE NO-FRAMES HALF — *reclassified to DETECTION MISS*.**
Asked whether line 1 printed above a missing colon, he said yes; it does not.
He pushed back that the ask was unfair — **part-upheld**: the framing pointed at
line 1 and asked a yes/no about printing rather than *what happens when you run
this*. **His claim "I know the rule" was tested immediately on a clean no-code
version and he answered correctly with the mechanism.** So this is **not a
knowledge gap.** Ask it as *"what happens when you run this?"*

**LANGUAGE CORRECTIONS ISSUED**
- *"no errors will be caught"* → **inverted.** The error **is** caught; that is
  the crime. Say **"no error is reported."**
- *"it is doing what it is expected to do"* → **what it was told to do.**
- *"let the Error raise an Exception"* → the error **is** the exception. Say
  **"let it propagate"**, or plainly **"let it crash."**
- *"if NameError occurs it will again stop"* → **that is not a downside, that is
  the feature.** A crash is a report.

---

## 4. TEACHING MISTAKES THIS SESSION — five, and one is a tool bug

**1. `tools/retest.py` HAD A SILENT PROMOTION BUG.** Built in S35, it demoted on
a fail and **never promoted on a pass** — every pass since would have been
silently under-recorded, in the one tool whose purpose is that the ledger stops
being hand-scheduled. Caught by noticing a `[~]` printed after a recorded pass;
fixed in session and **shown to him rather than quietly patched.** The file's own
principle: *an artefact that looks authoritative while being wrong is worse than
one that is missing.*

**2. A CONSOLIDATED QUESTION WITHOUT ITS CODE — S19's rule, breached.** The
raise-vs-return question went out as a fragment referencing `cfg` and `angle`,
neither defined; it was **not even runnable.** He stopped it: *"the whole code
should be in front of eyes … otherwise we need to waste time to go up and see."*
**Pushback 62, upheld in full.**

**3. FRAME FIRST, BREACHED.** He was told to edit line 30 of his own file with no
statement of what the edit was *for*, and asked directly: *"what is it you
actually want from this exercise?"* **Pushback 61, upheld.** The honest reason —
*this is the transfer test; the measure of a taught idea is whether it shows up in
your next file* — landed the moment it was given.

**4. HIS OWN CODE WAS MISQUOTED BACK AT HIM.** Restating `total_valid`, the
mentor wrote `return filtered_readings and sum(...)`; his file said
`return sum(...)`. **He did not catch it.** A wrong quote from the mentor is more
dangerous than no quote.

**5. NO CONFIDENCE RATINGS WERE TAKEN ON THE DRILL FUNCTIONS.** RULES S16-3
requires the student's own rating for a promotion. Without it, **`raise` could
not promote** despite being written cold and correctly a day after it was taught.
Take one per function at the next drill close.

**AND ONE THING THE MENTOR GOT RIGHT, RECORDED BECAUSE IT COST A TICK:** the
compile/run split was answered correctly — but the mentor had **quoted his own
S35 derivation back at him two turns earlier.** That is echo, not recall. **The
promotion was refused out loud**, with the S15 precedent named: he once refused a
confidence rating on freshly-taught material, and the same standard applies to
the mentor.

---

## 5. REFERENCE CHECKLIST — name · what it does · the trap

| Name | What it does | The trap |
|---|---|---|
| `Exception` | the ancestor of the ordinary error types | catching it catches **everything**, including your own typos |
| `class X(Exception): pass` | makes a new error type you can catch by name | **the `(Exception)` is the load-bearing part**, not the name |
| `except` ordering | checked top-to-bottom, first match wins | **the general one must go LAST** — or the block below is dead code, silently |
| bare `raise` | re-throws the **same** exception, original traceback intact | it is **not** re-offered to sibling `except` blocks — it goes outward |
| `raise e` vs `raise` | both re-throw | bare `raise` is the idiom; it keeps the traceback pointing at the real fault |
| `StopIteration` | the signal that iteration is over | **spell it exactly**; `for` catches it for you on every normal run |
| sentinel return (`None`, `-1`) | reports a problem as a value | **moves the failure away from its cause** — you crash far from the bug |
| `print` inside a library function | reports a problem to stdout | **you have decided the caller's output policy for them** |
| catch-all into a named bucket | e.g. `except Exception: broken.append(r)` | **worse than a bare `except:`** — it does not hide the fault, it lies about it |

---

## 6. WHAT'S COMING NEXT

**Session 37 is the AUGUST GAUNTLET.** Pure mixed recall, no new material. It
carries the strict-legend audit of every `[x]` in the file and the 31-Aug
re-baseline arithmetic against the 30 Sep deadline.

Owed and fired first, clean and cold: **the compile/run split** (a promotion that
has now waited twice), **`StopIteration`** (the label alone), **`while`
mechanics** (ten sessions overdue — the oldest debt in the file), and
**`constructors` as his first word** (one question from `[x]`).

Then **build block 02** — the episode validator, ≥90 min, timed, no AI, with
`LOG.md` in the definition of done — and then **1.10, modules and imports**, for
which S36 left a natural hook: `import` appeared in the test file, he correctly
flagged that it had never been taught, and got the one-line minimum only.
