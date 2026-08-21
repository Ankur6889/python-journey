# SESSION 15 NOTES — Saturday 8 August 2026 (second block)

**Topics: the iteration protocol (`iter`/`next`/`StopIteration`) · iterable vs
iterator · `list()` as a consumer of the protocol · `range()` — half-open and lazy
· function scope, not block scope · the empty `range(0)` case · traceback and
`NameError`**

---

## SELF-TEST — answer these cold before reading on

Notes closed. Say the answer aloud, then say the mechanism underneath it.

1. When Python runs `for c in colors:` over a 3-item list, how many times is
   `iter()` called and how many times `next()`? Why is the second number not 3?
2. What is the difference between an iterable and an iterator? Which can be used
   twice, and what is it about the other that makes it single-use?
3. `box = iter(colors)`, then `list(box)` twice. What does each call print? What
   does `colors` look like afterwards?
4. What does `list()` actually do to an iterator? Is it part of the iteration
   protocol or something else?
5. `range(3)` gives which numbers? Name the two properties of `range`.
6. Is `range` an iterable or an iterator? What follows from your answer?
7. `for i in range(3): last = i`, then `print(last)` and `print(i)`. Give both
   outputs and justify each.
8. Why can `StopIteration` never be the value of `i`? State the general rule about
   when a name gets bound.
9. Does Python have block scope? Which construct is the only one that creates a
   new scope?
10. `for i in range(0): last = i`, then `print(last)`. What happens, and on which
    line?
11. What is a traceback? In `print(next(box))` on an exhausted iterator, does
    `print` run?
12. What is `NameError` named after? Distinguish "scoped away" from "never
    created".

Answers at the back.

---

## FULL TEACHING

### 1. The iteration protocol — what a `for` loop actually is

A `for` loop looks like one thing and is really two. `for x in <iterable>:` means:

- **Stage A, once:** call `iter()` on the thing you were given. It hands back an
  **iterator**. Think of it as asking a container for a dispensing nozzle.
- **Stage B, every pass:** call `next()` on that iterator. Whatever comes back is
  bound to `x`, then the indented block runs. Repeat.
- **The end:** when nothing is left, `next()` raises **`StopIteration`**. The
  `for` loop catches that signal internally and stops quietly. You never see it.

```python
colors = ["red", "green", "blue"]
for c in colors:
    print(c)

# red
# green
# blue
```

The same thing with the machinery exposed — the version worth being able to write
from memory, because it is what the loop conceptually compiles down to:

```python
colors = ["red", "green", "blue"]
box = iter(colors)          # Stage A - once
print(next(box))            # red
print(next(box))            # green
print(next(box))            # blue
print(next(box))            # raises StopIteration

# red
# green
# blue
# Traceback (most recent call last):
#   File "demo.py", line 6, in <module>
#     print(next(box))
#           ~~~~^^^^^
# StopIteration
```

**The N+1 trap.** A 3-item list costs one `iter()` call and **four** `next()`
calls, not three. The last call is the one that raises. **The loop has to ask and
be refused in order to know it is finished** — there is no counter telling it the
length in advance. (So `range(4)` costs one `iter()` and five `next()`.)

### 2. Iterable vs iterator — the load-bearing distinction

Decode the names before memorising anything. **Iterable** = *able to be
iterated*: it can hand you an iterator when asked — lists, strings, dictionaries,
tuples, ranges. **Iterator** = *the thing that does the iterating*: it gives you
the next item on demand and raises `StopIteration` when it has nothing left.

> **THE RULE: iterables are reusable, iterators are consumed.**

```python
colors = ["red", "green", "blue"]
box = iter(colors)

print(list(box))    # ['red', 'green', 'blue']   - drains the iterator
print(list(box))    # []                          - nothing left
print(colors)       # ['red', 'green', 'blue']    - the LIST is untouched
```

```python
colors = ["red", "green", "blue"]

print(list(colors)) # ['red', 'green', 'blue']
print(list(colors)) # ['red', 'green', 'blue']    - same again, forever
```

**Why is the iterator consumed?** Not "because it gives one item at a time" —
something could dispense slowly and still rewind. The real cause is that an
iterator carries **forward-only state**: a position that only ever moves forward,
with no way back. **That parked position is the consumption.** The list was never
touched; only the marker moved, and the marker cannot go home.

The phrasing that interviews listen for: when a loop ends, **the iterator is
exhausted** — not "the iterable has no more items". The iterable still has
everything it ever had.

### 3. `list()` — a consumer of the protocol, not part of it

`list(x)` takes something iterable, runs `next()` on its iterator over and over
until `StopIteration` arrives, and collects everything it received into a
**brand-new list**.

So it is not a piece of the iteration protocol; it is a **customer** of it, one of
many. The contrast: **`next()` takes one spoonful; `list()` empties the pot in one
go.** That is why `list(box)` flattens an iterator to nothing in a single call.

### 4. `range()` — defined before use

Name-decode: a *range* is a stretch — from a start, up to a stop. Two properties
lock it down.

**Lock 1 — half-open.** The stop value is excluded.

```python
for i in range(4):
    print(i)

# 0
# 1
# 2
# 3
```

`range(4)` gives 0, 1, 2, 3 — four numbers, and 4 is not one of them. The mental
image: **stop is a fence, not a fencepost.** You walk up to it and stop; you do
not stand on it.

**Lock 2 — lazy.** A range does **not** build a list. It computes each number on
demand. `range(10_000_000)` costs essentially nothing to create, because nothing
has been generated yet — compare actually building a ten-million-element list.
This is the first encounter with **laziness as a design idea**, and it returns in
generators (1.13) and in PyTorch's `DataLoader`.

**The tie-back:** `range` is an **iterable**, not an iterator. So it is reusable,
and every `for` loop over it asks for a fresh iterator of its own.

```python
r = range(3)

print(iter(r) is iter(r))   # False - two separate iterators
print(list(r), list(r))     # [0, 1, 2] [0, 1, 2]  - reusable
```

### 5. Scope — function scope, not block scope

```python
for i in range(3):
    last = i

print(last)     # 2
print(i)        # 2
```

`print(last)` is `2`: the loop ran three times, binding `last` to 0, then 1, then
2. **The block ending does not delete anything.**

`print(i)` is **also 2** — not `StopIteration`. Two reasons, and both are the
lesson:

- **Binding happens only on a successful return.** `i` gets a new value when
  `next()` *returns* something. On the final call `next()` does not return — it
  **raises**. Nothing is produced, so nothing is bound, so `i` quietly keeps 2.
- **An exception is a signal, not a value.** It travels; it never lands in a
  variable. There is no assignment anywhere in that mechanism.

> **Python has function scope, not block scope.** `for`, `if`, `while` and `try`
> create no new scope. Names born inside them survive in the enclosing scope after
> the block ends. **Only a `def` makes a new scope.** Coming from C++ or Java this
> feels wrong, which is exactly why it is worth drilling.

### 6. The empty case — `range(0)`

`range(0)` is a perfectly legal **empty** stretch. Zero items, so the body runs
zero times. Nothing wrong with that at all.

But the code *around* it does break, and the distinction is the lesson:

```python
for i in range(0):
    last = i

print(last)

# Traceback (most recent call last):
#   File "demo.py", line 4, in <module>
#     print(last)
#           ^^^^
# NameError: name 'last' is not defined
```

Read the traceback: **the failure is on the `print` line, not the loop.** The loop
was fine. The body never ran, so `last` was never created.

**Two ways a name can be missing, and Python only has one of them:**

- **"Scoped away"** — the name existed but the block hid it or destroyed it on
  exit. **Python does not do this.**
- **"Never created"** — the line that would have created the name never executed.
  **This is Python's only failure mode.**

So: blocks don't hide names — but they don't guarantee creation either. Both
halves matter.

### 7. Traceback and `NameError`

**Traceback.** The crash report the interpreter writes when an exception is not
caught anywhere. It goes to the error stream, shows the call path that led to the
failure, and its **last line names the exception**.

The subtlety that resolves a common confusion: seeing `StopIteration` on screen
after a `print(next(box))` line does **not** mean it was printed. `print` never
ran at all. Python evaluates the argument first: `next(box)` raised, and the raise
aborted the whole line before `print` was reached. What you saw was the
interpreter's crash report, not program output. **That is the cleanest proof that
an exception travels rather than lands.**

**`NameError`.** Decodes like the others — named after the part that broke. **The
name is what is wrong**: you used one that does not exist. Same family as
`ValueError` (type fine, value unusable) and `TypeError` (operation undefined
between these types). Ask what broke, and the name follows.

---

## KEY MENTAL MODELS

- A `for` loop is `iter()` once, then `next()` every pass, until `StopIteration`.
- N items cost N+1 `next()` calls — the loop learns it is done by being refused.
- Iterables are reusable; iterators are consumed, because they hold forward-only
  state.
- `list()` is a consumer of the protocol, not part of it.
- `range` is lazy and half-open, and it is an iterable, not an iterator.
- Python has function scope. Only `def` creates a new one.
- Binding happens only on a successful return; a raise binds nothing.
- An exception is a signal that travels, never a value that lands.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| iterable | Can hand you an iterator when asked: `list`, `str`, `dict`, `tuple`, `range` | Reusable. Saying "the iterable is exhausted" is wrong — it never is |
| iterator | Gives the next item on demand; raises `StopIteration` when spent | Consumed because it holds forward-only state — *not* because it yields one at a time |
| `iter()` | Called ONCE by a `for` loop, at the start, to get the iterator | Two `iter()` calls on one iterable give two independent iterators |
| `next()` | Called once per pass; returns the item, which is then bound to the loop variable | N items cost N+1 calls; the last one raises |
| `StopIteration` | The signal raised by an exhausted iterator; `for` catches it internally | A SIGNAL, never a value. It is never bound to a name |
| `list(x)` | Runs `next()` to exhaustion and collects everything into a NEW list | A consumer of the protocol, not part of it. Drains an iterator in one call |
| `range(n)` | A lazy, half-open stretch of integers from 0 up to (not including) `n` | Stop is a fence, not a fencepost. And it is an ITERABLE, not an iterator |
| `range(0)` | A legal empty range; body runs zero times | Not an error — but names created only in the body then never exist |
| function scope | `for`/`if`/`while`/`try` create NO scope. Only `def` does | From C++/Java this feels wrong. `i` survives the loop with its last value |
| binding | A name is bound when the right-hand side successfully RETURNS a value | A raise returns nothing, so it binds nothing — this is why `i` stays 2 |
| traceback | The interpreter's crash report for an uncaught exception; last line names it | Not program output. On a failing `print(f(x))`, `print` never ran at all |
| `NameError` | Named after what broke: the NAME does not exist | "Never created" is Python's only failure mode here — there is no "scoped away" |

---

## SELF-TEST ANSWERS

**A1.** `iter()` once, `next()` four times. Not three, because the loop only
discovers it is finished by asking and being refused — the fourth call raises
`StopIteration`. N items cost N+1 calls.

**A2.** An iterable can hand you an iterator when asked; an iterator gives the
next item and raises `StopIteration` when spent. The iterable is reusable. The
iterator is single-use because it holds **forward-only state** — a position that
only moves forward, with no rewind. Not because it yields one at a time.

**A3.** First `list(box)` prints `['red', 'green', 'blue']`; the second prints
`[]`. `colors` is unchanged — still all three items. Only the iterator's position
moved.

**A4.** It runs `next()` repeatedly until `StopIteration` and collects everything
into a new list. It is a **consumer** of the protocol, not part of it.

**A5.** 0, 1, 2. The two properties: **half-open** (stop excluded — a fence, not a
fencepost) and **lazy** (computed on demand, no list built).

**A6.** An iterable. So it is reusable, and each `for` loop over it gets a fresh
iterator of its own.

**A7.** Both print `2`. `last` is 2 because the loop bound it three times and
blocks don't delete names. `i` is 2 because the final `next()` raised instead of
returning, so no new binding happened and `i` kept its last successful value.

**A8.** Because an exception is a **signal that travels**, never a value that
lands. A name is bound only when the right-hand side successfully returns a value —
a raise produces nothing, so it binds nothing.

**A9.** No. Python has **function scope**. `for`, `if`, `while` and `try` create
no scope; only `def` does.

**A10.** `NameError`, and it happens on the `print(last)` line — not the loop.
`range(0)` is legal; the body simply never ran, so `last` was never created.

**A11.** A traceback is the interpreter's crash report for an uncaught exception;
its last line names the exception. And no — `print` never runs. Python evaluates
the argument first, `next()` raises, and the line aborts before `print` is called.

**A12.** Named after the part that broke: the name doesn't exist. "Scoped away"
means a block hid or destroyed the name — Python doesn't do this. "Never created"
means the creating line never ran — Python's only failure mode here.

---

## WHAT'S COMING NEXT — SESSION 16

- **Term-tax first**, weighted to the labels above: indentation, iterable,
  iterator, `StopIteration`, `range`, traceback, `NameError`. Then the two
  unreliable veterans, `ValueError` vs `TypeError`, and coercion.
- **Cold re-test of the whole protocol** — especially
  iterables-reusable/iterators-consumed with the forward-only causation, and the
  `print(i)` question.
- **The promotion pass** — seven items one confirming re-test away: `+=`
  mutation-vs-rebind, aliasing, conversion-returns-new-object, `"5"+3`
  `TypeError`, mutating-methods-return-`None`, shallow-vs-deep copy, and the
  Session 13 operator drills.
- **Then close 1.6** — `print()`, `while`, nested loops, loop `else`, `pass`,
  ternaries, and common loop pitfalls. Teach `while` directly against `for`: **a
  `for` loop asks an iterator for the next item; a `while` loop re-evaluates a
  condition.** That contrast is why they are taught adjacently.
- Still owed: the negative `%` case cold, and where a default argument actually
  lives (`__defaults__`) in isolation.

**One forward pointer.** The protocol here is deliberately at model level — what
`iter()` and `next()` do and how to predict outcomes. How an object *declares*
itself iterable (`__iter__` / `__next__`), and generators as lazy iterator
factories, are the implementation-level payoff, scheduled in 1.13. And when you
reach PyTorch, every `DataLoader` loop you have ever run is exactly this protocol
underneath.
