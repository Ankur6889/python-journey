# SESSION 37 NOTES — Tuesday 1 September 2026, 00:18 → 05:35

**COLD BUILD BLOCK 02 — the episode validator.**
Scheduled as the August gauntlet; moved by the interval gate inside the first
minute. No new material was taught. One cold recall was fired and missed.

---

## SELF-TEST — do this first, notes closed

1. `x = "90"`. What does `print(type(x) != int or x < 0)` do — print, or raise?
2. Why is the answer to (1) the reason a `try` / `except TypeError:` around that
   line can never run?
3. A file is 80 lines. Line 20 has a `try:` with no `except`. Lines 60–80 define
   two perfect functions. How much of the file executes when you run it?
4. What is the difference between *catching* an exception and *handling* one?
5. `validate_all` returns a report keyed by episode id. Why can a record with no
   usable id not simply be given a fault code like every other problem?
6. In `except SomeError: log.append("X"); raise` — what does the bare `raise`
   do that `raise SomeError(str(e))` does not?
7. Why does a validator function return a list of strings rather than printing
   them?

Answers in the teaching section. Rate yourself before you look.

---

## 1. WHAT RAN THIS SESSION

**The interval gate came first and it decided the session.** S36's commit landed
31 Aug 23:51; this session opened 1 Sep 00:18. Twenty-seven minutes.

The rule (RULES.md, S17 rule 1): a recall test is only evidence if enough time
has passed for forgetting to have been possible. A gauntlet is *nothing but*
cold recall. Run at that interval it would have promoted material that had not
been retained — the S17 finding is that a passed same-day recall does not merely
fail to inform, **it actively corrupts.**

So the gauntlet moved to S38 and the build block ran instead. **A build block
does not ask what you remember. It asks what shows up in a file you write.**
That measurement is valid at any interval.

**Result: `validator.py`, 81 lines, four names, 2h 55m, 27/27.**

---

## 2. FULL TEACHING

### 2.1 Short-circuit evaluation — the miss of the session

**The mechanism (S13, and it is in the S13 notes verbatim):**

> `and` / `or` **return an operand and stop as soon as the answer is settled.**
> `2 or 1/0` → `2`, and `1/0` never runs.

For `A or B`: if `A` is truthy the answer is already settled — **`B` is never
evaluated at all.** Not evaluated-and-ignored. Never evaluated.

```python
x = "90"
print(type(x) != int or x < 0)
```
```
True
```

`type(x) != int` is `True`. Done. `x < 0` is never reached.

And on its own, that same comparison really does blow up:

```python
x = "90"
print(x < 0)
```
```
TypeError: '<' not supported between instances of 'str' and 'int'
```

**Both facts are true at once, and that is the whole point.** The comparison is
dangerous in isolation and unreachable behind the guard.

**S13's own summary line, worth re-reading:** *short-circuiting is what makes a
guard expression safe.* This is the entire idiom:

```python
if type(value) != int or value < 0:      # safe: the type check protects the comparison
```

**Consequence in this session's code:** three `except TypeError:` blocks in
`faults` are **dead code**. They cannot execute. The `or` in front of them
guarantees it.

⚠ **And the same file got it right once.** On the `fps` branch the comment reads
*"I believe no need of checking exception for this"* — correct, for exactly the
reason the other three branches are wrong. Same structure, twelve lines apart.

### 2.2 Catching is not handling

This is the idea that makes `validate_logged` make sense, and it was derived
from the spec by the student before it was named.

```python
def validate_logged(records, log):
    try:
        output = validate_all(records)
    except UnidentifiedEpisode:
        log.append("UNIDENTIFIED")
        raise                        # <- puts it straight back
    return output
```

**`validate_logged` catches the exception. It does not handle it.** It leaves a
mark that the fault occurred and then returns the fault to the air for somebody
else to decide about. Retry, skip, page someone, abort — none of that is its
business.

**A witness, not a handler.** Same doctrine as `check_limit` from S36 refusing
to decide what its caller prints: a function that decides on its caller's behalf
has taken a decision it does not own.

### 2.3 The bare `raise`, and why the traceback is the acceptance test

`raise` alone, inside an `except` block, **re-raises the exception that is
already travelling** — same object, same message, same origin.

`raise UnidentifiedEpisode(str(e))` creates a **new** exception. Same text, and
a different origin.

Run with nobody catching, same input, both functions:

```
=== validate_all([A, B]) ===
  File "case3a.py", line 4, in <module>
    validate_all([A, B])
  File "validator.py", line 35, in validate_all
    raise UnidentifiedEpisode(...)
UnidentifiedEpisode: record at position 1 has no usable id

=== validate_logged([A, B], []) ===
  File "case3b.py", line 4, in <module>
    validate_logged([A, B], [])
  File "validator.py", line 46, in validate_logged
    return validate_all(records)
  File "validator.py", line 35, in validate_all
    raise UnidentifiedEpisode(...)
UnidentifiedEpisode: record at position 1 has no usable id
```

**Read the bottom frame of each.** Both say `validate_all`. `validate_logged`
added a frame on the way through, which is unavoidable — but it did not become
the *origin* of the fault.

**Why it matters at work:** get it wrong and the person debugging a 394-episode
run is pointed at the logger instead of the bad record.

### 2.4 Why an exception rather than a fault code

The general rule the block was built to teach:

> **A problem gets reported when the report can express it. It gets raised when
> the report cannot.**

`validate_all` returns `{"clean": [ids], "faulty": {id: [codes]}}`. Both halves
are addressed **by id**. A record with no usable id has nowhere to live in that
structure.

**And a placeholder is worse than a crash.** File two id-less records under
`None` and the second overwrites the first — the report then quietly claims it
checked fewer episodes than it did. **A report that undercounts is worse than a
crash, because nobody goes looking for it.**

### 2.5 Exceptions detect; return values report

```python
faults({"id": 3, "frames": "90", "fps": 30})   ->  ['frames', 'missing:task']
```

| field | what's there | what happens | list becomes |
|---|---|---|---|
| `id` | `3` | fine | `[]` |
| `frames` | `"90"` | comparison would raise `TypeError` | `["frames"]` |
| `fps` | `30` | fine | `["frames"]` |
| `task` | absent | reaching for it raises `KeyError` | `["frames", "missing:task"]` |

**`"TypeError"` and `"KeyError"` appear nowhere in the returned list.** The
exception is *how you found out*; the string is *what you report*. Only the
second one leaves the function.

The caller doesn't care how you discovered `frames` was bad. `"TypeError"` would
describe your implementation; `"frames"` describes their data.

### 2.6 The compile/run split — asked twice, unanswered, carried forward

A `try:` with no `except` is a **`SyntaxError`**, and a `SyntaxError` is found
before any of the file runs. The question that was asked and not answered:

> Your file is 80 lines. You deleted three lines in the middle. `validate_all`
> and `validate_logged` at the bottom were untouched. **How far did Python get?**

The cause was named correctly and instantly — *"I deleted the except block
without deleting try"* — which is a different question. **Owed cold in S38.**

---

## 3. THE ASSIGNMENT AND HIS SOLUTION

**Build block 02** — `builds/block_02_episode_validator/`, brief in `BRIEF.md`,
27 mentor-written tests in `test_validator.py`.

| level | name | result |
|---|---|---|
| L1 | `faults(record)` → list of fault codes, field order | green, 15 tests |
| L2 | `validate_all(records)` → `{"clean": [...], "faulty": {...}}` | green |
| L3 | `UnidentifiedEpisode`, raised on an unusable id, message carries the index | green |
| L4 | `validate_logged(records, log)` — log without altering the fault | **1 bug** |
| L5 | `report(records)` — print and return | not attempted, optional |

**The bug:**

```python
    return output, log        # returns a TUPLE
```

Two L4 tests red, twenty-five green. Returned as *"find it"* with the raw
assertion and no explanation. Fixed unaided.

**What went right without being asked for:**

- `fps_defaults` defined once, read once — DRY held **structurally**, not by
  patching. `validate_all` never re-checks an id; it reads what `faults` said.
- **Nothing prints.** 81 lines.
- `faults_to_be_returned.sort(key=record_struct.index)` — S23 `key=` material,
  reused unprompted fourteen sessions later.
- The `KeyError` was **designed out of existence**: missing fields computed up
  front with a comprehension, then a loop over `record.keys()` that cannot miss.
- **Zero bare `except:` or `except Exception:`.**

**The done line (RULES v6):** *"function with least clarity is L4, because I
didn't have a clear picture in mind."* **Both failures were in L4.** Third
firing of the rule and the first one that landed on the actual failure.

---

## 4. THINKING GAPS THIS SESSION — with error-type classification

1. **`short-circuit` evaluation — KNOWLEDGE GAP (genuine).** Said
   `type(x) != int or x < 0` raises; it returns `True`. S13 material, 24-day
   gap, rated 6/10. Conceded unprompted. **Demoted [x] → [~], due 2 Sep.**

2. **RIGHT CODE, WRONG MODEL — STRUCTURAL, and the important one.** The guard he
   wrote is correct and idiomatic. His account of why it was needed was wrong,
   and he wrote three unreachable `except` blocks defending it. **Green tests are
   not evidence of a model.** This is the same family as
   right-answer-without-mechanism and it is now the reason to keep asking *why
   does this work* about code that already passes.

3. **`return output, log` — LAZY THINKING, self-corrected.** The spec said
   *returns exactly what `validate_all` returns*. Returning the log alongside it
   is the kind of "helpfully add one more thing" move that changes an interface.
   Found by test, fixed off the assertion in one pass, no help given.

4. **Deleted the `except` and left the `try` — CHANNEL / EXECUTION, not
   comprehension.** He named the cause instantly with no output in front of him.
   The *editing* slip is real and cheap; the diagnosis was immediate.

5. **The compile/run split — NOT CLASSIFIABLE, because it was never answered.**
   He answered a different question correctly. Carried to S38 as an open ask.

**NOT gaps, and logged here so they are not mis-read later:**

- The seven spec questions before starting. **Three exposed holes in the brief
  and a fourth found a case the tests did not cover.**
- *"Am I bad at reading?"* / *"I feel like I am slow in building logic."*
  **Both are under-ratings**, answered with his own record: 35/35, 29/29, 25/25,
  and 27/27 here.

---

## 5. TEACHING MISTAKES THIS SESSION

1. **FRAME FIRST breached on L4** (pushback 69). The level was issued with
   mechanics and no statement of what it buys. His challenge was correct, and so
   was the counter-argument underneath it — at four functions, the caller could
   just write the `try`/`except` itself. The honest frame, given late: **L4 is a
   measurement, not a design.**

2. **Three defects in a spec issued under SPEC BEFORE PUZZLE.** An undefined
   term ("message"); a rule stated argument-first and four-things-at-once (L3);
   and a case — wrong value on one field, absent key on another — covered by
   neither the examples nor the 26 tests. **Roughly half the pre-block time went
   on repairing the brief.** Better than S29's four versions and the same failure
   mode. The fix each time was the same: state the rule, then the exact values,
   then the argument — never the other order.

3. **The compile/run ask was let go after one re-ask.** Depth-before-answer part
   (a) says a correct diagnosis does not discharge a traced mechanism. It lapsed
   into the closing exchange. **Second session running that this ask went
   unpaid.**

4. **The green state was never committed.** 27/27 was verified at ~05:22; the
   next commit captured the file only after it had been broken. **A verified
   result that lives in no commit cannot be cited.** Commit green when green.

---

## 6. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | The trap |
|---|---|---|
| **short-circuit (`or`)** | Returns an operand and STOPS as soon as the answer is settled | The right-hand side is **never evaluated**, so a guard in front of a dangerous comparison makes it unreachable — and any `try` around it dead |
| **short-circuit (`and`)** | Same, settled by the first falsy operand | `and` → first falsy else last; `or` → first truthy else last. **They return an operand, not `True`/`False`** |
| **dead code** | Code that cannot execute on any input | Passing tests never reveal it. Only reasoning about the guard in front of it does |
| **bare `raise`** | Re-raises the exception already travelling — same object, same origin | `raise Err(str(e))` looks identical in the message and moves the origin to your line. Read the **bottom** frame of the traceback |
| **catching vs handling** | Catching intercepts; handling decides | A function that catches and then decides has taken a decision belonging to its caller. A logger should be a **witness** |
| **report vs raise** | Report what the return value can express; raise what it cannot | Inventing a placeholder key silently **collides** and undercounts. Undercounting is worse than crashing |
| **`SyntaxError`** | Raised before any of the file runs | A `try:` with no `except` kills the whole file, including perfect functions 60 lines below it |
| **fault codes** | Plain strings in a returned list | The exception type must never appear in them: it describes your implementation, not the caller's data |
| **`sort(key=...)`** | Sorts in place by a computed key; returns `None` | `record_struct.index` as a key gives a fixed custom order. `.sort()` returns `None` — never assign it |
| **DRY** | One copy of a decision | The mechanical test: count the places that compare against the same constant. That count must be 1 |

---

## 7. WHAT'S NEXT

**S38 is the August gauntlet** — pure mixed recall, no new material, ARCHIVE and
the master loaded at the open. It carries the strict-legend audit of every `[x]`,
the re-baseline arithmetic against 30 Sep, and the overdue cold asks.

**First five minutes of S38, before anything else:** the working tree is red.
Three `try:` with no `except` at lines 16, 22 and 32 of `validator.py` — closed
in this state by explicit ruling. Repair, re-run, commit green.

**Owed cold, in order:** the compile/run split (third asking) · `short-circuit`
(due 2 Sep) · `StopIteration`'s label alone · the transfer gap re-run at a real
gap · `while` mechanics (eleven sessions overdue, the oldest debt in the file).

**Then 1.10, modules and imports.**
