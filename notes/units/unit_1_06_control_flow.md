# Unit 1.6 — Control Flow

Steering which line runs next: `if`/`elif`/`else`, the iteration protocol
under `for`, `range`, `while`, `break`/`continue`/`pass`, loop `else`, the
ternary, nested loops, common pitfalls, and `print()`.

---

## 1. What control flow is

The default flow is top to bottom. Control flow bends it — to **choose** (a
conditional) or to **repeat** (a loop).

**Block syntax:** the **colon opens** a block; **indentation delimits** it;
**dedent ends** it. That is Python's replacement for braces.

**A block creates no new frame and no new namespace.** Only a function call
does. A name assigned inside an `if`, `for`, `while` or `try` survives after
the block:

```python
if True:
    y = 10
print(y)        # 10 — same frame, block makes no scope

def f():
    z = 10
f()
print(z)        # NameError — z died with f's frame
```

The discriminator: **"Did I call a function? No? Then no new frame, same
namespace."**

---

## 2. `if` / `elif` / `else`

`if` = keyword, condition, colon, indented block. The condition is **coerced to
a bool**: emptiness falsy, zero falsy, everything else truthy (1.3 §3).

`elif` is "else if". The chain is **ONE connected ladder**, not several
independent `if`s. Python checks top to bottom; **the first true condition
wins** — its block runs and the interpreter leaves the entire chain without
evaluating anything below it.

```python
x = 5

if x > 10:
    print("A")
elif x > 3:
    print("B")
elif x > 1:
    print("C")
else:
    print("D")
# B
```

`x > 1` is also true, but it is never even looked at. Three separate `if`
statements would print both B and C. With `x = 20`, "A" prints and
`elif x > 3` is **never evaluated at all** — which matters the moment a
condition has a side effect. `else` is optional, evaluates no condition, and
catches every remaining case; without it, nothing runs when all conditions
are false, and that is legal.

---

## 3. The iteration protocol — what a `for` loop actually is

`for x in <iterable>:` is three moves:

- **Stage A, once:** call `iter()` on the thing you were given. It hands back
  an **iterator** — a dispensing nozzle.
- **Stage B, every pass:** call `next()` on that iterator. The returned item
  is bound to `x`, then the block runs.
- **The end:** when nothing is left, `next()` raises **`StopIteration`**. The
  `for` loop catches it internally and stops quietly.

```python
colors = ["red", "green", "blue"]
box = iter(colors)          # Stage A — once
print(next(box))            # red
print(next(box))            # green
print(next(box))            # blue
print(next(box))            # raises StopIteration
```
```
red
green
blue
Traceback (most recent call last):
  File "demo.py", line 5, in <module>
    print(next(box))
StopIteration
```

**The N+1 trap.** A 3-item list costs one `iter()` and **four** `next()`
calls. The loop learns it is finished by asking and being refused; there is no
counter telling it the length in advance.

`StopIteration` is an **exception** — a signal that travels, never a value
that lands. It is the **normal** exit of every `for` loop ever written. What a
`for` loop is, written out (1.9 §11):

```python
it = iter(box)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # ...loop body...
```

### 3.1 Iterable vs iterator — the load-bearing distinction

- **Iterable** = *able to be iterated*: it can hand you a fresh iterator when
  asked. `list`, `str`, `dict`, `tuple`, `range`, a file object.
- **Iterator** = *the thing that does the iterating*: gives the next item on
  demand, raises `StopIteration` when spent. `iter(x)`, `zip(...)`,
  `reversed(x)`, `enumerate(...)`, a generator.

> **Iterables are REUSABLE. Iterators are CONSUMED.**

```python
colors = ["red", "green", "blue"]
box = iter(colors)
print(list(box))    # ['red', 'green', 'blue']   — drains the iterator
print(list(box))    # []                          — nothing left
print(colors)       # ['red', 'green', 'blue']    — the LIST is untouched

print(list(colors), list(colors))   # works again and again
```

**Why is an iterator consumed?** Not "because it gives one item at a time" —
a spoon does that and can go back. The cause: an iterator carries
**forward-only state** — a position that only ever moves forward, with no
rewind. The container was never touched; only the marker moved. Say "the
**iterator** is exhausted", never "the iterable" — the iterable still has
everything it ever had.

**`list()` is a consumer of the protocol, not part of it.** `list(x)` runs
`next()` on `x`'s iterator until `StopIteration`, catches it, and collects
everything into a **new list**. `next()` takes one spoonful; `list()` empties
the pot. On a partly consumed iterator it drains only what is **left**:

```python
val = iter([10, 20, 30, 40])
next(val)
print(list(val))    # [20, 30, 40]
```

A spent iterator gives `[]`, not `[None]` and not an error.

---

## 4. `range()` — defined before use

A stretch of integers from a start, up to a stop. Two locks:

1. **Half-open.** The stop value is excluded. `range(4)` → 0, 1, 2, 3. *Stop
   is a fence, not a fencepost.*
2. **Lazy.** No list is built; each number is computed on demand.
   `range(10_000_000)` costs nothing to create.

```python
for i in range(4):
    print(i)        # 0 1 2 3 (one per line)

r = range(3)
print(iter(r) is iter(r))       # False — two separate iterators
print(list(r), list(r))         # [0, 1, 2] [0, 1, 2] — reusable
```

`range` is an **iterable, not an iterator**: every `for` over it gets a fresh
iterator. `range(0)` is a legal empty range — zero items, body runs zero times.
`range(start, stop, step)` follows the same half-open rule as slicing (1.8).

---

## 5. Function scope, not block scope

```python
for i in range(3):
    last = i
print(last)     # 2
print(i)        # 2 — not StopIteration
```

`last` survives because blocks do not delete names. `i` is `2` because
**binding happens only on a successful return**: the final `next()` raised
instead of returning, so nothing was bound and `i` kept its last value.

> **Python has function scope. `for`, `if`, `while` and `try` create no new
> scope. Only a `def` makes a new scope.**

### 5.1 The empty case and `NameError`

```python
for i in range(0):
    last = i
print(last)
```
```
Traceback (most recent call last):
  File "demo.py", line 3, in <module>
    print(last)
NameError: name 'last' is not defined
```

The failure is on the `print` line, not the loop. The body never ran, so
`last` was never created. Two ways a name can be missing, and Python has only
one: **"scoped away"** (a block hid or destroyed it — Python does not do this)
vs **"never created"** (the creating line never ran — Python's only failure
mode). `NameError` is named after the part that broke: the **name** does not
exist.

---

## 6. `while` — re-evaluate a condition

`for` walks *through* something. `while` walks through nothing: **it repeats
as long as a condition stays true**, re-checking before every pass.

```python
count = 0
while count < 3:
    print(count)
    count = count + 1
# 0 1 2   — and afterwards count == 3
```

> `for` asks an iterator for the next item. `while` re-evaluates a condition.

What `while` can do that `for` cannot — there is no sequence to walk, only a
condition that becomes true:

```python
while True:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        break
    print("You said:", user_input)
```

Sensor readings until a threshold; retry until connected; a control loop
until shutdown. Say "runs **while** true", not "till".

### 6.1 Tracing to the final cycle

```python
i = 0
while i < 5:
    print(i)
    i += 1
# 0 1 2 3 4
```

After `4` prints, `i` becomes 5, control returns to the top, `5 < 5` is
`False`, the body is **skipped** and the loop ends. 5 is never printed. **The
condition guards entry to the body, not the value that gets printed.** The
loop always goes round one more time than it prints — that silent final check
is the step people drop.

### 6.2 The infinite loop

```python
i = 0
while i < 5:
    print(i)        # 0 0 0 ... forever — i is never updated
```

The single most common cause: the variable in the condition is never changed
in the body.

---

## 7. `break` and `continue`

- **`break`** exits the loop it is directly inside. In nested loops that means
  the **innermost only**; there is no `break 2`. It also suppresses the loop's
  `else`.
- **`continue`** abandons **this iteration only** and jumps back to the
  condition check / next item. Loop lives; iteration dies.

```python
for n in [1, 2, 3]:         for n in [1, 2, 3]:
    if n == 2:                  if n == 2:
        break                       continue
    print(n)                    print(n)
# 1                         # 1 3
```

### 7.1 The `while` + `continue` trap

```python
# SAFE — increment above the continue
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)
# 1 2 4 5

# INFINITE — increment below the continue
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
# 0 1 2 then hangs forever
```

`continue` skips everything below it, including the increment. In a `for`
loop this is harmless because the iterator advances regardless. **In a
`while` loop, put the state update where `continue` cannot skip it.** Note
the safe version prints `5`: the condition guards entry, and the increment at
the top of the body means the last printed value is one past what the
condition appears to allow.

### 7.2 An early `return` as the exit

Inside a function, `return` leaves the loop and the function at once — often
the cleanest exit, and no found-flag is needed:

```python
def first_bad(rows):
    row_index = 0
    while row_index < len(rows):
        column_index = 0
        while column_index < len(rows[row_index]):
            if rows[row_index][column_index] < 0:
                return row_index, column_index
            column_index = column_index + 1
        row_index = row_index + 1
    # falls off the end -> returns None implicitly
```

---

## 8. Nested loops

The inner loop runs to **completion** for every single value of the outer.

```python
for i in range(3):
    for j in range(2):
        print(i, j)
# 0 0 / 0 1 / 1 0 / 1 1 / 2 0 / 2 1
```

Cost multiplies: two nested loops over a thousand items each is a million
iterations.

**Why the inner loop restarts at 0:** `range(2)` is an **iterable**; each pass
of the outer loop calls `iter()` on it again and gets a **fresh** iterator.
The version that breaks — hoist the iterator:

```python
it = iter(range(2))         # ONE iterator, made once

for i in range(3):
    for j in it:            # looping over the ITERATOR, not the iterable
        print(i, j)
# 0 0
# 0 1
# (then nothing — passes two and three find it exhausted, silently)
```

That is forward-only state made visible as a bug. Turnstile: you can go
through, you cannot come back.

---

## 9. Loop `else` and the found-flag pattern

The search task without loop `else` — a **flag** created before the loop, set
inside, checked after:

```python
lis = [1, 35, 23, 64, 10, 243]
flag = False
for i in lis:
    if i == 10:
        flag = True
        print("found")
        break
if not flag:
    print("not found")
# found
```

The flag records only one thing — *did the loop finish without hitting
`break`?* — and the interpreter already knows that. Loop `else` is that
knowledge exposed:

```python
for i in lis:
    if i == 10:
        print("found")
        break
else:
    print("not found")
# found
```

> **A loop `else` block runs if and only if the loop finished WITHOUT
> executing a `break`.** Read the keyword as `nobreak`. It has nothing to do
> with the `else` of an `if` — never read it as "otherwise".

An empty iterable ⇒ body never runs ⇒ `break` never encountered ⇒ **`else`
runs**. Useful in a search function to bind a "not found" value:

```python
def first_big(values, limit):
    for i in values:
        if i > limit:
            break
    else:
        i = None
    return i

print(first_big([1, 7, 9, 2], 5))   # 7
print(first_big([5, 5, 5], 5))      # None
print(first_big([], 0))             # None  — i would be unbound without the else
```

---

## 10. `pass` — the statement that does nothing

A hard syntactic rule: **once a colon opens a block, that block cannot be
empty.**

```python
if x > 5:
print("done")
# IndentationError: expected an indented block after 'if' statement on line 1
```

`pass` is a **no-op** that satisfies the rule when there is nothing to put in
the body yet:

```python
def calculate_torque():
    pass            # runs fine; the function exists and does nothing

class OverLimit(Exception):
    pass
```

- **A comment is not a body.** A block containing only `# todo` still raises
  `IndentationError`; comments are removed before the code runs.
- Three keywords, three jobs: **`pass`** = do nothing, carry on to the next
  line (*jagah bharo*); **`continue`** = abandon this iteration (*agla
  chakkar*); **`break`** = leave the loop (*bahar niklo*). The name "pass"
  sounds like "skip it" — that is `continue`'s job.

---

## 11. The ternary — a conditional EXPRESSION

Where an `if`/`else` block spends four lines choosing between two values:

```python
if x > 0:
    sign = "positive"
else:
    sign = "negative"
```

the ternary does it in one:

```python
sign = "positive" if x > 0 else "negative"
```

Read it from the middle outward: **`A if C else B`** — *this value, if the
condition holds, otherwise that one.* The middle is the condition; the value
you want comes first. *`ter-`* = three operands: value, condition, value.

**The point is the word EXPRESSION.** It evaluates to a value, so it can go
anywhere a value can: bound to a name, passed into a call, inside a list.

```python
print("high" if n > 10 else "low")                  # legal
labels = ["pos" if n > 0 else "neg" for n in nums]  # legal
print(if n > 10: "high")                            # SyntaxError — a statement
```

Use a ternary only when both branches select one simple value; if either
branch needs to do several things, write the full block.

---

## 12. `print()` — formally

A **function** that writes its arguments to standard output and **returns
`None`** (same family as `append` and `sort`: do something, return `None`).

**It calls `str()` on each argument before writing.** That is why `print(5)`
works while `"5" + 3` raises: **`print` converts, `+` refuses.** It takes any
object, not "a string".

```python
print("a", "b", "c", sep=" ", end="\n")     # the defaults, written out
```

- **`sep`** goes **between** the items; default one space. That is the
  mystery space in `print("a", "b")` → `a b`.
- **`end`** goes **after** everything; default `"\n"` (backslash-n, the
  newline — not `/n`).

```python
print("a", "b", "c", sep="-")     # a-b-c
print("a", "b", "c", sep="")      # abc
print("x", "y", sep="", end="")
print("z")                        # xyz   (the second print still adds its own "\n")
```

---

## 13. `enumerate()` — number off

Hands out one tuple per element, `(count, element)`, counting from 0. The two
names on the `for` line are tuple **unpacking** (1.8). It replaces
`for i in range(len(x))` index bookkeeping.

```python
joints = ["shoulder", "elbow", "wrist"]

for pair in enumerate(joints):
    print(pair)                 # (0, 'shoulder') / (1, 'elbow') / (2, 'wrist')

for i, name in enumerate(joints):
    print(i, name)              # 0 shoulder / 1 elbow / 2 wrist
```

`enumerate` returns an iterator; pairing two sequences positionally is `zip`
(1.8 §7).

---

## 14. `_` as a name

`_` is an **ordinary variable name**. Python attaches no meaning to it in a
file; it is a convention for the reader: *"I am not going to use this value."*
`for _ in range(3):` says the count matters, the value does not. (In the REPL
only, `_` also holds the last result.)

---

## 15. Common pitfalls, collected

1. **The infinite `while`** — condition variable never updated in the body
   (§6.2); or updated below a `continue` (§7.1).
2. **Trace-tail truncation** — stopping the trace one cycle early. State the
   silent final check (§6.1).
3. **Looping over a hoisted iterator** — the inner loop silently runs once
   (§8).
4. **Mutating a list while iterating over it** — `for` keeps a position
   counter and does not know the list is shifting; items slide into slots
   already passed and are skipped, silently. Build a new list instead
   (`[a for a in angles if a <= 180]`). Full trace in 1.8 §1.7.
5. **Using a loop variable after a comprehension** — the comprehension's
   variable does not exist afterwards (`NameError`), unlike a `for` loop's
   (1.8 §5).
6. **Reading loop `else` as "otherwise"** (§9).
7. **A comment as a body** (§10).

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| block | colon opens, indent delimits, dedent ends | makes **no** scope; only a call does |
| truthiness | `if` coerces to bool; empty/zero falsy | `"False"` is truthy |
| `if`/`elif`/`else` | one ladder, first true condition wins | conditions below the winner are **never evaluated** |
| iteration protocol | `iter()` once, `next()` per pass, `StopIteration` to stop | N items cost N+1 `next()` calls |
| iterable | hands out a fresh iterator each time | reusable; never "exhausted" |
| iterator | forward-only position; raises `StopIteration` when spent | consumed; a second pass yields nothing |
| `list(it)` | drains an iterator into a new list | catches `StopIteration`; spent iterator → `[]` |
| `range(n)` | lazy, half-open, an **iterable** | stop is a fence, not a fencepost; `range(0)` is legal |
| function scope | only `def` creates scope | `i` survives the loop with its last value |
| binding on return | a raise binds nothing | why `i` is 2, not `StopIteration` |
| `NameError` | the name was never created | "scoped away" does not exist in Python |
| `while` | repeats while a condition stays true | needs its own state update |
| the final check | one more evaluation than prints | condition guards entry, not the printed value |
| `break` | exits the innermost loop | no `break 2`; suppresses loop `else` |
| `continue` | ends this iteration | above the update in a `while` = infinite loop |
| nested loops | inner runs fully per outer value | a hoisted iterator silently dies |
| loop `else` | runs if no `break` happened | read as `nobreak`; empty iterable → runs |
| found-flag | flag before / set inside / check after | three touch-points for one question |
| `pass` | no-op filler for a block that cannot be empty | a comment is not a body |
| ternary | `A if C else B`, an **expression** | middle is the condition; both branches one value |
| `print()` | `str()` each arg, join with `sep`, follow with `end`; returns `None` | `\n` not `/n`; the last newline is invisible |
| `enumerate()` | `(count, element)` tuples from 0 | needs two-name unpacking on the `for` line |
| `_` | an ordinary name meaning "unused" | no special meaning in a file |
