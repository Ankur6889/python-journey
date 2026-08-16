# Session 21 Notes — 16 Aug 2026 (evening)
**Topics: the seven review proposals adopted · VS Code/Claude Code migration · `global` · `*args`/`**kwargs`**

---

## SELF-TEST (do this cold, before reading anything below)

1. `global` — when is it needed and when is it not? Give the three-word-rule
   (read / mutate / rebind) with one example each.
2. Why does this crash, and with which exception exactly?
   ```python
   count = 0
   def tick():
       count = count + 1
   tick()
   ```
   Your answer must include *when* Python decided `count` was local.
3. What does `*args` collect, into what type? What does `**kwargs` collect,
   into what type? What are their values when nothing is left over?
4. What is a **keyword argument**? Show a call where two keyword arguments
   arrive in "the wrong order" and still land correctly.
5. The mirror rule: what do `*` and `**` do in a **signature**, and what do
   they do in a **call**?

---

## SESSION RECORD (what happened, in order)

- **Interval gate (applied unprompted): S21 began ~2 hours after S20 — same
  sitting.** Term-tax skipped; the four queued [RECALL]s (post-order transfer,
  cell causation, closure definition, traceback) deferred; **zero promotions,
  correctly** — same-day evidence measures echo, not retention.
- **All SEVEN proposals from the 16 Aug review were ACCEPTED** and adopted as
  a package (RULES v2): task-based recall; promotion = correctness with
  confidence setting the interval; the rule-change cap; the seven-principle
  index; the weekly cold build block; queue tooling; the pushback denominator.
- **First session in VS Code + Claude Code.** Workflow settled: drills are
  written by the student in `drills/`, pytest in `tests/` decides
  correctness, the mentor reads/runs files directly and never edits a file
  the student has started. Editor autocomplete must stay OFF for drills.
- Taught `global`, then `*args`/`**kwargs` (full teaching below). Session
  ended at the student's call before lambdas/docstrings.

---

## FULL TEACHING

### 1. `global`

**Prerequisite:** `nonlocal` (S19) and LEGB (S18). The pair:

- `nonlocal x` — "don't create a local; assignments to `x` target the
  **enclosing function's** cell."
- `global x` — same escape hatch, one level higher: "assignments to `x`
  target the **module namespace**."

```python
count = 0            # module level

def tick():
    global count     # assignments now hit the module name
    count = count + 1

tick()
tick()
print(count)         # 2
```

**Why it crashes without `global` — the real mechanism of the item.**
Remove the `global` line:

```python
count = 0

def tick():
    count = count + 1

tick()
# UnboundLocalError: cannot access local variable 'count'
# where it is not associated with a value
```

The student asked the exact right question: *"the right side runs first —
when it doesn't find `count` locally, shouldn't LEGB find the global one?"*
The answer is the heart of the topic:

> **Locality is decided at FUNCTION-CREATION time, not line by line.**
> The compiler scans the whole body. If an assignment to a name exists
> ANYWHERE in the body, that name is classified **local for the entire
> body** — including lines above the assignment. A name classified local
> **never gets the LEGB walk**: reads of it go only to the local slot.

So at `count + 1`: `count` is local (decided before any line ran), the local
slot has nothing bound yet → **local + unbound = `UnboundLocalError`**. The
error name is literally the diagnosis. (Contrast the S19 three-error set:
`NameError` = the name exists nowhere in LEGB; `UnboundLocalError` = the
name IS local but empty.)

**Case 2 — read only, no assignment:**

```python
count = 0

def tick():
    print(count)

tick()               # 0 — works, no global needed
```

No assignment anywhere in the body → `count` was never classified local →
the read goes up the chain and finds the module-level `0`.

**Case 3 — mutation, no assignment:**

```python
scores = [1, 2, 3]

def add_score():
    scores.append(4)

add_score()
print(scores)        # [1, 2, 3, 4] — works, no global needed
```

`scores` is only ever **read**; the mutation happens on the **object** it
points to. No name is rebound, so no `global` is needed.

> **THE RULE: `global` is about REBINDING A NAME, not about touching an
> object. Read: free. Mutate: free. Rebind: needs `global`.**

### 2. Keyword arguments (substrate, defined mid-session at the student's catch)

Positional arguments are matched **by position**:

```python
def intro(name, role):
    print(name, "-", role)

intro("Ankur", "robotics")            # Ankur - robotics
```

A **keyword argument** is passed as `name=value` in the **call** and matched
**by name**, so order stops mattering:

```python
intro(role="robotics", name="Ankur")  # Ankur - robotics
```

### 3. `*args` and `**kwargs`

**Motivation (a constraint you cannot beat):** `print("a")` and
`print("a", "b", "c")` both work. No fixed parameter list can accept an
unknown count of arguments. That is the problem the collectors solve.

**`*args` — collects leftover POSITIONAL arguments into a TUPLE:**

```python
def show(*args):
    print(args)

show(1, 2)             # (1, 2)
show("a", "b", "c")    # ('a', 'b', 'c')
show()                 # ()   ← empty TUPLE, never None
```

**`**kwargs` — collects leftover KEYWORD arguments into a DICT:**

```python
def show(**kwargs):
    print(kwargs)

show(name="Ankur", role="robotics")   # {'name': 'Ankur', 'role': 'robotics'}
show()                                # {}   ← empty DICT, never None
```

**Why empty-and-typed instead of `None`:** the body can loop over `args` /
`kwargs` in every case with no special-case check. One type, always.

**Combined — the signature order is fixed: normal params, `*args`, `**kwargs`:**

```python
def report(title, *args, **kwargs):
    print(title)
    print(args)
    print(kwargs)

report("joints", 1.2, 0.8, unit="rad", safe=True)
# joints
# (1.2, 0.8)
# {'unit': 'rad', 'safe': True}

report("joints")
# joints
# ()
# {}
```

**The MIRROR RULE — same symbols in a call, opposite direction:**

```python
def intro(name, role):
    print(name, "-", role)

pair = ("Ankur", "robotics")
intro(*pair)                                  # unpack → positional args

info = {"name": "Ankur", "role": "robotics"}
intro(**info)                                 # unpack → keyword args
```

> **Signature side = COLLECT many into one. Call side = SPREAD one into
> many.** Unpacking feeds the call with ARGUMENTS — as if you had typed them
> out — it does not create variables.

---

## KEY MENTAL MODELS

1. **Locality is a compile-time property of the whole body.** One assignment
   anywhere makes the name local everywhere, before any line runs. The LEGB
   walk only exists for names *not* classified local.
2. **Read / mutate / rebind** — the three-way test for whether `global` (or
   `nonlocal`) is needed. Only rebinding needs the keyword.
3. **Collect vs unpack mirror** — `*`/`**` are direction-dependent: signature
   collects, call spreads.
4. **Empty-but-typed beats None** — `()` and `{}` keep the body uniform.

---

## THINKING GAPS THIS SESSION

All on [PREDICT]/[TEACH-BACK] instruments — **none ledger-eligible**, logged
for pattern-tracking only:

1. **"Associativity" offered for RHS-before-assignment** (label slip, Term
   Retention family). Correct term: the **evaluation order** of an assignment
   statement. Associativity is the tie-break direction for equal-rank
   operators. Mechanism was fully owned; the label reached for was wrong.
2. **`None` guessed for the empty `*args` case** (knowledge gap on brand-new
   material — the honest default guess). Self-corrected immediately when
   pointed back at output already on screen. Not an error pattern; noted only
   because the *design reason* (type stability) is the part to retain.
3. **Teach-back gave the *what* without the *when*** on the locality
   classification (surface-first habit, the S20 depth-before-answer target).
   Re-asked once; the *when* (function-creation time) came back correct and
   complete. The re-ask discharged it — this is the countermeasure working,
   but it needed the re-ask.

**Strengths on record this session:** he asked the UnboundLocalError-vs-LEGB
question unprompted (the exact right attack on the topic); held the
name-vs-object distinction under correction; ran the mutation-case reasoning
end-to-end unaided; and caught the naked term (below) rather than guessing
past it.

## TEACHING MISTAKES THIS SESSION

1. **"Keyword argument" used before it was defined** — `**kwargs` was opened
   with the term naked. The student stopped it: *"what do you mean by keyword
   arguments"* — **upheld; eleventh occurrence of the define-before-use breach
   family. Running pushback total: 26 raised, 26 upheld, 0 wrong. Under the
   new denominator rule (proposal 7): S21 = 1 challenge raised / 1 upheld.**
   Repair: the term was defined properly with a code contrast, then the block
   was re-issued from that point.

## REFERENCE CHECKLIST

| NAME | WHAT IT DOES | THE TRAP |
|---|---|---|
| `global x` | assignments to `x` inside the function target the module namespace | not needed for reads or mutations — only REBINDING |
| locality classification | one assignment anywhere in the body → name is local everywhere, decided at function creation | the line ABOVE the assignment is already local — hence `UnboundLocalError`, not a LEGB rescue |
| `UnboundLocalError` | name IS local, no value bound yet | don't confuse with `NameError` (name exists nowhere) |
| keyword argument | `name=value` in a CALL, matched by NAME | it's a property of the call, not the parameter |
| `*args` (signature) | collects leftover positional args into a TUPLE | empty case is `()`, never `None`; `args` is just a conventional name |
| `**kwargs` (signature) | collects leftover keyword args into a DICT | keys are strings; empty case is `{}` |
| signature order | normal params → `*args` → `**kwargs` | fixed by rule |
| `*` / `**` (call) | UNPACK a tuple/dict into separate arguments | opposite direction from the signature; produces arguments, not variables |

## WHAT'S COMING NEXT (Session 22)

- If a later day: the deferred [RECALL] block at last — post-order transfer,
  cell causation, closure definition, traceback — **task-first, in drills/,
  under the new promotion rule** (correct = promote; rating sets interval).
- First cold pass on `global` and `*args`/`**kwargs`.
- Fire `__defaults__` and the iterator causation (bug-first).
- Close 1.7: **lambdas and docstrings** — the last two items.
- Schedule the first **weekly cold build block** (adopted S21, no date yet).
- The 1.6 spoken Feynman recall is now formally a **gauntlet item** (end of
  August), no longer a live session item.
