# SESSION 23 NOTES — Wednesday 19 August 2026

**Gap since S22: 2 days.** Interval gate applied — all cold work today was
promotable. Sixth session running that the gate was applied by the mentor
without being asked.

**Yield:** term-tax backlog cleared, **8 promotions**, **1 demotion**, two
drills passed, **lambdas closed to [x]**. **1.8 did not open.**

---

## SELF-TEST — answer these cold before reading on

1. `int(-5.98)` and `-5.98 // 1`. Both values, and *why* they differ.
2. A `for` loop is handed an iterator that is already exhausted. How many
   times does the body run, and what makes the loop stop?
3. Define a closure in one line. The line must contain the word *survives*.
4. What is a **cell**? Name its type.
5. Why is `__closure__` a **tuple** rather than a single object?
6. `key=f` and `key=f()`. What is the difference, and which does `sorted`
   want?
7. A string literal sits on the **second** line of a function body. What does
   `__doc__` return?
8. Name the five checks. (Hook: *Boundary pe khaali ek bahar mila.*)
9. `-13 % 10` — the value, and the identity that proves it.
10. What does `next()` raise when the iterator is finished? Spell it.

---

## FULL TEACHING

### 1. Truncation vs floor division — the direction is the whole distinction

Both throw away the fractional part. **They throw it away in different
directions**, and that is the only thing worth remembering.

```python
print(int(-5.98))
print(-5.98 // 1)
```
```
-5
-6
```

- **`int()` truncates — cuts toward ZERO.** `-5.98` → `-5`. The magnitude
  always gets smaller.
- **`//` floors — goes toward −∞.** `-5.98` → `-6`. For negatives this is a
  *bigger* magnitude, which is the counter-intuitive half.

For positive numbers the two agree, which is exactly why the trap only ever
shows up on negatives.

### 2. The iteration protocol — two functions and one exception

A `for` loop is not magic. It is three moves:

1. **`iter(x)`** — asks an iterable for a **fresh** iterator. Called **once**,
   at the top of the loop.
2. **`next(it)`** — asks the iterator for the next item. Called **once per
   pass**.
3. When nothing is left, `next()` **raises `StopIteration`**. The `for` loop
   catches it silently and ends.

```python
it = iter(range(2))

print(next(it))
print(next(it))
print(next(it))
```
```
0
1
Traceback (most recent call last):
  File "proto.py", line 5, in <module>
    print(next(it))
          ^^^^^^^^
StopIteration
```

**`StopIteration` is the normal exit of every `for` loop in Python**, not an
error case. That is worth sitting with: the mechanism that ends every loop
you have ever written is an exception being raised and swallowed.

**Why the two-loop program prints nothing the second time:**

```python
it = iter(range(2))

print("first pass")
for x in it:
    print(x)

print("second pass")
for x in it:
    print(x)
```
```
first pass
0
1
second pass
```

Both loops end via `StopIteration`. The first raises it *after* handing over
`0` and `1`; the second raises it **immediately**, so the body runs **zero
times** and `x` is never bound to anything.

The iterator's **position** is past the end. There is no "exhausted state"
flag — there is just a position that only ever moves forward.

### 3. What a cell actually is — the thing S22 never gave you

**The problem.** A name lives in a frame. When `make_distance_key(9)` returns,
its frame is destroyed and every name in it dies. But the inner function still
needs `target` afterwards. The normal mechanism cannot work.

**The fix.** When Python sees at `def`-time that an inner function uses a name
from the enclosing function, it does **not** store the value in the frame. It
creates a separate object — a **cell** — and puts the value in there. Two
things then reference that cell: the enclosing frame, and the function object
being built. **The frame dies; the cell does not, because the function object
is still holding it.**

**A cell is a type**, exactly like `int` or `list`:

```python
def make(a):
    def inner():
        return a
    return inner

f = make(9)
g = make("hello")

print(type(f.__closure__))
print(type(f.__closure__[0]))
print(type(f.__closure__[0].cell_contents))
print(type(g.__closure__[0]))
print(type(g.__closure__[0].cell_contents))
```
```
<class 'tuple'>
<class 'cell'>
<class 'int'>
<class 'cell'>
<class 'str'>
```

**A cell is a box with exactly one slot.** The box is always a `cell`. What is
in the slot can be any object at all — `f` closed over an int, `g` over a
string, and both cells are still `<class 'cell'>`.

**Why `__closure__` is a tuple:** one cell **per free variable**.

```python
def make(a, b):
    def inner():
        return a + b
    return inner

f = make(1, 2)

print(f.__closure__)
print(len(f.__closure__))
print(f.__closure__[0].cell_contents)
print(f.__closure__[1].cell_contents)
```
```
(<cell at 0x754ec5f558d0: ...>, <cell at 0x754ec5f93640: ...>)
2
1
2
```

**And with no free variables there are no cells, so there is no tuple:**

```python
def plain(x):
    return x

print(plain.__closure__)
```
```
None
```

`None`, not `()`. Same absence discriminator as `__doc__`.

**THE FOUR LAYERS — and now they have structure under them:**

| Expression | What it is |
|---|---|
| `f` | the **function object** |
| `f.__closure__` | a **tuple** — one slot per free variable |
| `f.__closure__[0]` | one **cell** — indexing a tuple gives an *element*, never a tuple |
| `.cell_contents` | the **value** inside that cell |

**The one-line definition:** *a function object that binds a free variable
from its enclosing scope into a cell, so the value survives after the
enclosing frame has died.*

### 4. Function object vs call — `f` and `f()`

```python
def double(n):
    return n * 2

f = double

print(f)
print(f(5))
```
```
<function double at 0x7d5388ead300>
10
```

**The parentheses are the operator that RUNS a function.**

- `f` — no parens. The function **object**. Nothing runs; you are handing the
  thing over.
- `f()` — parens. Python runs it **right now, on this line**, and what sits in
  that spot is whatever it **returned**.

This is why `sorted(values, key=calculate_distance())` fails: it runs the
function immediately, before `sorted` has a single element to give it.
`key=` wants something `sorted` will call **itself**, later, once per element.

### 5. `sorted` and `key=` — the signature

```
sorted(iterable, key=None, reverse=False)
```

- **`iterable`** — the thing to sort. Returns a **new list**; the original is
  untouched.
- **`key`** — a callable, called once per element with **exactly one
  argument**. Sorts by the **results**, returns the **original items**.
- **`reverse`** — `True` flips the order.

**That one-argument rule is the entire reason closures exist in this drill.**
There is no way to pass a second value in, so the second value has to be
carried *by the function itself*.

### 6. Lambdas

```python
last_digit = lambda x : x % 10
```

The **expression** form of a function. Body is **one expression**, and its
value is **auto-returned** — there is no `return`, and there cannot be one.
Statements are not allowed in there at all; that is what "expression form"
means.

The parameter list works exactly like a `def`'s.

### 7. Docstrings — position, not punctuation

```python
def first(x):
    """I am the first statement."""
    return x


def second(x):
    y = x
    """I am NOT the first statement."""
    return y


print(first.__doc__)
print(second.__doc__)
```
```
I am the first statement.
None
```

**Triple quotes do not make a docstring. POSITION does.** A string literal
becomes `__doc__` **only if it is the first statement of the body**; Python
attaches it to the function object at `def` time.

Anywhere else, that same string is an ordinary expression: evaluated, result
discarded, nothing happens. It is a comment that costs you bytecode.

Absent docstring → `__doc__` is **`None`**, not `""`.

### 8. The five checks — where bugs actually live

> ### **"Boundary pe khaali ek bahar mila"**

| Word | Check | What you try |
|---|---|---|
| **Boundary** | 1 | the exact value sitting on the `<` / `<=` / `>` / `>=` |
| **Khaali** | 2 | empty / zero / nothing — `0`, `""`, `[]`, `None` |
| **Ek** | 3 | one — the smallest non-empty case |
| **Bahar** | 4 | outside your assumption — negative, float, wrong type |
| **Mila** | 5 | two things that must agree — base case ↔ step; **spec ↔ code** |

**The mnemonic gets you the list. It does not get you the thinking.** Check 4
asks you to notice an assumption you did not know you had made, and no
acronym does that for you.

**Check 5 generalises beyond recursion.** Any two things in your code that
make a claim about the same fact must agree. A docstring is such a claim:

```
docstring says:  "sorts based on the last digit"
code says:        x % 10
-13:              docstring implies 3, code gives 7
```

Two checks converging on the same bug is the signature of a real one.

---

## ASSIGNMENTS AND WHAT HAPPENED

### Drill 1 — `drills/s23_sort_key.py` (closure, forced by `key=`)

**Constraint:** order values by distance from a target chosen at call time,
using `sorted(..., key=...)`, where `key=` accepts exactly one argument.

**His final code:**

```python
def make_distance_key(target):
    def distance_from_target(val):
        return abs(val - target)
    return distance_from_target


def order_by_distance(values, target):
    calculate_distance = make_distance_key(target)
    return sorted(values, key=calculate_distance)
```

**6/6 pytest — but through three guided debug cycles:**

1. `make_distance_key()` called with no argument. His diagnosis was wrong in
   an instructive way: *"target comes from the outer function directly, from
   closure property isn't it?"* — he had merged "the inner function reads
   `target` from the enclosing scope" with "`target` gets a value from
   nowhere". The closure explains the **read**, never the **origin**.
2. `key=calculate_distance()` — call instead of object. Two Socratic attempts
   failed; taught directly.
3. `val - target` without `abs()`. Found by him after one traced value.

### Drill 2 — `drills/s23_ordering.py` (lambdas + docstrings)

**Constraint:** two orderings, exactly two `def`s allowed, no mutation of the
input, and documentation readable at runtime.

**His code — 6/6 pytest, COLD, FIRST ATTEMPT, UNAIDED:**

```python
def sort_by_last_digit(numbers):
    """ This function sorts the provided list based on the last digit of each number in the list"""
    last_digit = lambda x : x%10
    return sorted(numbers,key=last_digit)


def sort_by_length(words):
    """ This function sorts the provided list based on the length of the words"""
    length = lambda x : len(x)
    return sorted(words,key=length)
```

**This is the promotion evidence for lambdas.** The no-third-`def` constraint
made the lambda necessary rather than merely possible.

*(Idiom note for later, not a defect: `key=len` would do the second one on its
own, and a lambda can be written inline at the call site rather than bound to
a name first.)*

### The bug hunt — the best work of the session

Applying check 4 to his own lambda, unprompted:

> *"lets see a case -13%10 lets apply the rule -2*10 + r = -13 which gives r
> as 7 this will definitely cause problem"*

```python
print(-13 % 10)
print(sort_by_last_digit([-13, 5, 21]))
```
```
7
[21, 5, -13]
```

Correct, and **the modulo identity had been owed cold since S13**. He produced
it unprompted, in service of something else. **Promoted.**

---

## THINKING GAPS THIS SESSION (with error-type classification)

1. **`StopIteration` and `next()` — both names lost. [KNOWLEDGE GAP,
   arbitrary-label class.]** The causation was intact (exhausted iterator →
   body runs zero times) but he could not name the function the loop calls,
   and guessed *"EndofIterator"* then *"EndofIteration"*. `StopIteration` was
   [x] since S18 — **failed re-test, reverted to [~]**. Consistent with the
   S12 diagnosis: mechanism survives, arbitrary label does not.

2. **Closure definition — second consecutive failure, identical defects.
   [MENTOR STRUCTURAL FLAW, not a student gap — see Teaching Mistakes 1.]**
   `cell_contents` called a tuple; survival clause missing. Both S22, both
   again here.

3. **Closure *origin* vs closure *read*. [STRUCTURAL FLAW.]** He believed the
   closure supplied `target` a value, rather than supplying access to one.
   Worth a targeted re-test: *who gives a parameter its value?*

4. **Function object vs call. [KNOWLEDGE GAP.]** `key=f()` written where
   `key=f` was needed, and not recoverable Socratically. This is S18
   first-class-objects material.

5. **Docstring mechanism. [KNOWLEDGE GAP.]** Predicted a second-line string
   literal would still populate `__doc__`. Correct placement without the rule
   behind it — **working code, absent mechanism**, which is a new shape for
   this file and one that only task-first drills expose.

6. **Five checks — flat gap, three days after transferring on first use.
   [KNOWLEDGE GAP, list-class.]** Countermeasure adopted (mnemonic).

7. **Two flat term gaps: loop `else` and ternary. [KNOWLEDGE GAP.]** Both
   [~] since S17; both retrieved as nothing. Re-teach, do not re-test.

8. **`pass` given as a use, not a mechanism. [DEPTH.]** *"we use it when we
   know the function is going to exist but don't know the body"* — a correct
   use case, and he flagged the missing mechanism himself.

9. **`continue` phrased as "exits the current loop". [LANGUAGE PRECISION.]**
   It ends the current **iteration**. Correction issued.

10. **⚠ Depth-before-answer, fired hard. [HABIT — the named weakness.]** The
    five-checks report was requested **four times**, once as item 1 at the top
    of a short message, and skipped every time. And he declared drill 1
    *"works"* without running it — it crashed on the next line. **Running it
    is part of the answer.**

11. **⚠ Confidence calibration ran hot. [NEW WATCH AREA.]** 8/10 on precedence
    with associativity missing entirely; 8/10 on `sep`/`end` with `sep` wrong;
    **7/10 on a closure definition repeating both of S22's defects.** His
    ratings have been usable as a *targeting* signal since S17. Three
    over-ratings in one session is a first. If it drifts, the rating stops
    setting re-test intervals honestly.

---

## TEACHING MISTAKES THIS SESSION

1. **CELLS WERE TAUGHT AS LABELS IN S22, AND IT MANUFACTURED A FAKE STUDENT
   WEAKNESS. This is the session's most important finding.** The four-layer
   table was delivered with code and the survival clause, but **what a cell IS
   — a type, a one-slot box, one per free variable — was never given**. Four
   labels in a stack with nothing underneath is memorisation, and it collapsed
   twice. He asked directly: *"I am still unsure what a cell is, is it a
   memory cell?"* and then, once it was taught, *"why didn't you tell me all
   this when you used cell first time itself"* — **pushback 28, upheld.**
   **This is the same class of failure as the S20 traceback discovery: an item
   fired repeatedly as [RECALL] and logged as failure when the substrate had
   never been delivered. Second occurrence in four sessions. The check is
   cheap: before logging a second failure on the same item, ask whether the
   thing underneath it was ever taught.**

2. **1.8 did not open, for the second session running.** The recall queue
   consumed the teaching slot in both S22 and S23. Defensible once — the
   backlog was two sessions deep and the closure gap it surfaced was worth
   finding — but the arithmetic to 30 September does not survive a third. A
   **recall-budget rule is parked** for his decision rather than adopted
   unilaterally.

3. **The call-vs-object question was ground through two failed Socratic
   attempts before going direct.** Both hints pointed at evidence he could not
   yet interpret. The rule already exists — *direct when the question demands
   it* — and it should have been applied one turn earlier.

4. **Ambiguous rating input was not chased.** A bare `3` arrived where a
   confidence rating was expected and the thread moved on without resolving
   it. Minor, but the ratings are ledger inputs and an unresolved one is a
   hole in the evidence.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `int()` truncation | drops the fraction, **toward zero** | `int(-5.98)` is `-5`, not `-6` |
| `//` floor division | drops the fraction, **toward −∞** | agrees with `int()` only for positives |
| modulo identity | `a == b*(a//b) + (a%b)` | sign follows the **divisor**: `-13 % 10` is `7` |
| `iter(x)` | asks an iterable for a fresh iterator | called **once** per loop, not once per pass |
| `next(it)` | asks the iterator for the next item | moves the position **forward only** |
| `StopIteration` | what `next()` raises when finished | it is the **normal** end of every `for` loop |
| exhausted iterator | position sits past the end | the loop body runs **zero** times; no error |
| cell | a **type** — a one-slot box holding a free variable | `cell_contents` is the *value*; `__closure__` is the *tuple* |
| `__closure__` | tuple of cells, **one per free variable** | `None` when there are none — not `()` |
| closure | function object + cell keeping a value alive past its frame | the **survival** clause is the definition's point |
| `f` vs `f()` | object handed over vs function run now | `key=f()` runs it immediately and fails |
| `sorted(it, key=, reverse=)` | new list; key called once per element | key takes **exactly one** argument — that forces the closure |
| lambda | expression form; one expression, **auto-returned** | no statements, no `return`, ever |
| docstring | first statement of the body → `__doc__` at `def` time | **position** makes it, not the quotes; absent is `None` |
| five checks | boundary / empty / one / outside / agree | the mnemonic gives the list, never the thinking |
| `continue` | ends the current **iteration** | it does not exit the loop |

---

## WHAT'S COMING NEXT — SESSION 24

1. **Confirm the weekend cold build block** (Sat 22 / Sun 23 Aug), first thing.
2. **1.8 Data Structures — lists first, EARLY, before any long recall block.**
   The mutating-methods **roster** finally gets owned. **Slicing taught
   formally.** `zip` and list comprehensions are owed here and are marked
   seen-but-not-taught.
3. **Closure definition cold** — third attempt, now that the substrate exists.
4. **Iteration protocol cold** — `iter()` / `next()` / `StopIteration`.
5. **Docstring mechanism**, the five checks via the mnemonic, and the S23
   term failures: loop `else`, ternary, `pass`, `sep`, associativity.
