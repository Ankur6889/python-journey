# SESSION 40 NOTES — Wed 2 September 2026, 20:21 → 20:50

**Term-tax only. Thirty minutes. Ended by you to go and read the notes.**

Interval gate: 80 minutes since the S39 commit (19:01), verified from `date`
and `git log -1`. Same day for everything taught in S39, so nothing from 1.10
could be asked. **But 1.9 and older were last touched 23–48 hours ago, so
the term-tax was legal, and it ran — the first one since S36.** The August
gauntlet is deferred a fourth time: you had two hours, and then stopped at
thirty minutes to read notes tonight. Session length is your call.

Ruling taken: **breakpoint debugging goes to 1.11.** Ruling still open: the
weekly build block on a real LeRobot file once 1.10 lands.

---

## SELF-TEST — do this first, notes closed

1. `count = count + 1` inside a function, with `count = 0` at module level.
   Which line makes `count` local, and WHEN is that decided?
2. `NameError` vs `UnboundLocalError` — one line each, and the difference.
3. `finally` — name the four ways out of a `try` it runs after.
4. `[1, 2].push(3)` — which error, and which token failed?
5. `5[0]` — which error, and why is it not `IndexError`?
6. Two different values can have the same hash. True or false? Then: what
   MUST be true of equal values' hashes?
7. Is `_` special to Python, or to the reader?
8. "The iterable is exhausted." What is wrong with that sentence?

Answers are all in section 1. Write yours first.

---

## 1. FULL TEACHING

### 1.1 `UnboundLocalError` — the mechanism you could not reach

You had the WHERE (inside a function, on `count = count + 1`) and the
contrast (at module level the same line is `NameError`). You did not have
the WHY. Taught in S19, S21, S22 and S26; your own notes call it
**compile-time locality**. It had faded. Here it is again, from the ground.

```python
count = 0

def bump():
    print(count)      # line 4: READ count
    count = 1         # line 5: ASSIGN count

bump()
```
```
  File ".../ubl.py", line 4, in bump
    print(count)      # line 4: READ count
          ^^^^^
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

**Step 1 — the rule.** When Python compiles a function body it scans the
WHOLE body before any of it runs. Any name that is ASSIGNED anywhere in the
body is marked LOCAL for the entire function. Line 5 assigns `count`. So
`count` is local in `bump` — including on line 4, which sits ABOVE the
assignment.

**Step 2 — what that changes.** When `bump()` is called, a new frame is
made. `count` gets a slot in that frame because it was marked local. The
slot is empty.

**Step 3 — the crash.** Line 4 reads `count`. Python does NOT go up to the
module, because `count` is local here. It looks in the frame slot. Empty.
Local name, nothing bound to it. **Unbound + Local.** The name decodes.

**Why not `NameError`?** `NameError` = the name exists in NO scope. Here the
name exists, locally. It has no value yet. Different fault.

**The proof, by deletion.** Remove line 5 and the same line 4 works, because
now nothing in the body assigns `count`, so it is not local, so the lookup
goes to the module and finds `0`:

```python
count = 0

def bump():
    print(count)      # no assignment anywhere in the body -> count is GLOBAL here

bump()
```
```
0
```

**Where your instinct was right:** you said "the python sees this during
compilation". The LOCALITY decision IS made at compile time. Where it was
wrong: the `NameError` at module level is a RUNTIME error with a frame — the
compiler checks grammar, never whether a name exists (S35, your own
derivation).

### 1.2 `AttributeError` — the DOT failed

```python
robot = [1, 2]
robot.push(3)
```
```
AttributeError: 'list' object has no attribute 'push'
```

The object exists. The name `robot` resolved fine. What failed is the thing
AFTER the dot: this object has no attribute called `push`. Timeline ("how far
did Python get?"): parsed → found the name → tried the dot → stopped there.

### 1.3 `subscriptable` — able to take square brackets

```python
n = 5
print(n[0])
```
```
TypeError: 'int' object is not subscriptable
```

`x[...]` is called SUBSCRIPTION. An object is subscriptable if it supports
it. An `int` does not, so the OPERATION is impossible for this TYPE —
`TypeError`. It is not `IndexError`: `IndexError` means the type indexes
fine and THIS index does not exist. **The brackets do not decide the error.
The thing in front of them does** (S27, and you missed this same one in S38).

### 1.4 `finally` — what it GUARANTEES

You gave the shape (`try` / `except` / `finally`). The question was what it
guarantees. **It always runs.** Four exits, all covered:

1. `try` finishes normally.
2. `try` raises and an `except` catches it.
3. `try` raises and NOTHING catches it — `finally` runs on the way out, then
   the program dies.
4. `try` hits a `return` — `finally` runs BEFORE the value leaves.

Cases 3 and 4 in one file, no `except` anywhere:

```python
def read(text):
    try:
        return int(text)
    finally:
        print("finally ran for", repr(text))

print(read("45"))
print(read("n/a"))
```
```
finally ran for '45'
45
finally ran for 'n/a'
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'n/a'
```

Line 1 of the output: `finally` ran before the `return` delivered `45`.
Line 3: `finally` ran, THEN the uncaught `ValueError` killed the program.
This is the same demonstration as S35 (`measure`). You self-rated 3, and 3
was right.

### 1.5 `hashable` — the correction

You said: "all the non-mutable are hashable, hashing generates a unique
value." First half: the practical rule, right direction. Second half: wrong
word. A hash is a fixed-size number computed from a value. It is NOT unique
— two different values can share one (a collision). What matters at Level 2:

- **Equal values hash equal.** `hash(1) == hash(1.0)` is `True`.
- **The value must not change after hashing**, or the dict cannot find it
  again. That is why mutable ⇒ unhashable, which you had.

```python
print(hash(1) == hash(1.0))     # equal values hash equal
print(hash("a") == hash("a"))
try:
    hash([1, 2])
except TypeError as e:
    print("TypeError:", e)
```
```
True
True
TypeError: unhashable type: 'list'
```

### 1.6 `_` as a name — you had it and withdrew it

Your answer: "anything can be here but it's not important, e.g. `for _ in
range(...)`". Then: "actually this is also pass." The first answer was
correct. **`_` is an ordinary name.** Python attaches no meaning to it. It is
a convention for the READER: *I am not going to use this value.* You can
`print(_)` and it works. The one place it does something extra is the REPL,
which stores the last result in `_` — not relevant to files.

### 1.7 `StopIteration` — passed, one phrasing fix

You said it "marks the ending of an Iterable". The iterable never ends. It is
the ITERATOR that is exhausted — its position has run off the end. Your next
clause proved you know this: "the iterable can be used again and again." Say
it that way. (S15 correction (a), now issued for the third time.)

---

## 2. THINKING GAPS THIS SESSION (with error-type classification)

| # | What happened | Type | Note |
|---|---|---|---|
| 1 | `UnboundLocalError` WHY missing; WHERE intact | **Knowledge gap (faded)** | Taught 4×; declared honestly (*"can't come to it myself"*). Rated 4, calibrated. |
| 2 | `AttributeError` — gap | **Label loss** | Named it correctly BY INSTANCE in S27 (`robot.append` on a dict). The word went, not the machinery. |
| 3 | `subscriptable` — gap | **Label loss, second miss** | Missed in S38 too (`'int' object is not subscriptable` → said `IndexError`). Comes back 3 Sep. |
| 4 | `finally` — shape given, guarantee not | **Surface answer (depth-before-answer)** | Rated 3 — the rating knew before the verdict did. |
| 5 | `hashable` — "unique" | **Knowledge gap, minor** | Level-3 edge; the Level-2 discriminator was present. |
| 6 | `_` — right answer withdrawn | **Calibration, under-confidence** | The inverse of S38's over-rating. Not logged. |
| 7 | "ending of an Iterable" | **Language precision** | Third issue of the same correction. |
| 8 | "python sees this during compilation … throws NameError" | **Model slip, not logged** | `NameError` is runtime with frames; he derived that himself in S35. The item under test was different. |

**Pushback 74.** *"You are actually checking my memory, and naming it
mechanism."* Checked against the notes, not remembered: the mechanism was
taught in S19, S21, S22 and S26. So it was a check of a taught mechanism
that had faded, which is the queue's job. **Not upheld on the item. Upheld on
the remedy** you named — go back to the notes — which is step 3 of RECALL
FIRST, NOTES SECOND: ask cold, say gap, THEN read. Running total: **74
raised, 73 upheld or part-upheld.**

---

## 3. TEACHING MISTAKES THIS SESSION

1. **The verdict turn broke the response-length cap (S20 rule 2).** One
   message carried: an 8-row verdict table, two corrections, a runnable demo,
   a [PREDICT] AND a [TEACH-BACK]. You replied *"directly give the answer, I am
   unable to understand your explanation."* Correct. One teaching idea per
   turn; the [PREDICT] should have been its own message after the misses were
   cleared. **This is the mentor defect of S40.**
2. **The `[PREDICT]` on top of a declared gap was the wrong instrument.** You
   had just said you could not reach the reason. Asking you to predict it
   from a traceback was a puzzle where a definition was owed. Frame first,
   then ask.
3. **Three labels left naked for one turn** (`AttributeError`,
   `subscriptable`, `finally`'s guarantee) — verdicts were given before the
   one-line meanings. Fixed in the next message, but the order was wrong.

**Held:** interval gate from `git log` + `date`, first minute; term-tax at a
legal gap; ratings taken after your answers and before verdicts; queue script
used for every result; no drill file touched; the stop honoured immediately.

---

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | The trap |
|---|---|---|
| compile-time locality | assignment ANYWHERE in a body makes the name local EVERYWHERE in it | the line above the assignment is already local |
| `UnboundLocalError` | local name, no value bound yet | not `NameError` — the name exists |
| `NameError` | name exists in no scope | runtime, with frames — the compiler never checks names |
| `AttributeError` | the DOT failed; object has no such attribute | the name before the dot was fine |
| subscriptable | supports `x[...]` | on a non-subscriptable type it is `TypeError`, not `IndexError` |
| `finally` | always runs — normal exit, caught, uncaught, `return` | "uncaught" still runs it, then dies |
| hashable | a fixed number from a value; equal values hash equal | NOT unique; mutable ⇒ unhashable |
| `_` | an ordinary name; convention for "unused" | Python gives it no meaning outside the REPL |
| `StopIteration` | the stop signal; an exception | the ITERATOR is exhausted, never the iterable |
| `abs()` | distance from zero, sign discarded | — (passed, 7) |

---

## 5. WHAT'S COMING NEXT

**Session 41: if a real day has passed, it is THE GAUNTLET — deferred four
times now.** It fits in two hours if it is planned as pure mixed recall with
the queue script driving it. If you have less than that, say so at the open
and the gate will pick the largest legal instrument.

**Due cold on 3 Sep regardless:** the seven 1.10 rows (`import RUNS the
file` first), `.keys()` as a view (asked tonight, unanswered — still the
cheapest tick on the board), `short-circuit`, and the four labels that
failed tonight.

**You are reading the notes tonight.** That is legal and it is the rule's
step 3. Tomorrow's asks are still cold asks — a day is a day — but the
mentor will know the review happened.

**Still open in 1.9:** `raise ... from`, and `except Exception:` vs bare
`except:` — the 1.9 footnotes. **Still open for your ruling:** the build
block on a real LeRobot file.
