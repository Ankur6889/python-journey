# SESSION 18 NOTES — Monday 10 August 2026 (evening)

**Topics: the exception family (`NameError`/`ValueError`/`TypeError`) ·
exceptions as signals · traceback and its trigger · iterator causation · the
modulo identity worked on a negative divisor · in-place mutators · `def` vs call ·
parameters vs arguments · return values and implicit `None` · LEGB ·
`__defaults__` · default arguments · first-class functions · nested functions**

Opens 1.7 Functions and takes it about two-thirds of the way.

---

## SELF-TEST — answer these cold before reading on

Say "gap" where you have nothing.

1. A name is used that was never created. Which exception?
2. `int("2.5")` — which exception, and why is it not the same as Q1?
3. `"5" + 3` — which exception, and what does Python do instead of guessing?
4. Is an exception a value that sits somewhere, or something else?
5. What category of thing is `StopIteration`?
6. Under exactly what condition does the interpreter print a traceback?
7. Why is an iterator consumed? (One reason only. Not "one item at a time".)
8. Write the modulo identity in symbols.
9. `l = [3,1,2]; x = l.reverse()`. What is `x`? What is `l`?
10. Name three list methods that mutate in place, and one that mutates and
    returns a value.
11. When the `def` line executes, what exists? What does not exist yet?
12. In `def add(x, y): …` and `add(3, 5)` — which are parameters, which arguments?
13. Name the three cases in which a function returns `None`.
14. Expand LEGB. What decides the E?
15. Which attribute on a function object holds its default values?
16. What does `f = greet` do, with no brackets?
17. What is a nested function?

---

## FULL TEACHING

### 1. The exception family — labels first

The three labels are **named after the part that broke**. That is the whole trick,
and it is why they do not need memorising.

| You did this | What broke | Exception |
|---|---|---|
| Used a name that was never created | the **name** | `NameError` |
| Gave a good type but a bad value: `int("2.5")` | the **value** | `ValueError` |
| Asked for an operation that doesn't exist between these types: `"5" + 3` | the **type** | `TypeError` |

```python
print(undefined_name)   # NameError: name 'undefined_name' is not defined
int("2.5")              # ValueError: invalid literal for int() with base 10: '2.5'
"5" + 3                 # TypeError: can only concatenate str (not "int") to str
```

**The precision point on `TypeError`, which matters in interviews:** Python does
not get "confused" and it does not "guess". **It refuses.** With `"5" + 3` it
cannot know whether you want `8` or `"53"`, so rather than pick one it declines
the operation entirely.

### 2. Exceptions are SIGNALS

An exception is **not a value that lands somewhere and sits there**. It is a
**signal that travels**: raised at the point of failure, propagating outward
looking for something to catch it. **It is never bound to a name.**

This is why, in `print(next(box))` on an exhausted iterator, `print` never runs at
all: Python evaluates the argument first, `next()` raises, and control leaves
before `print` is ever called.

`StopIteration` is an **exception**, not "a state". A state sits still; an
exception travels and announces. `for` catches `StopIteration` internally and
stops the loop quietly, which is why you normally never see it.

### 3. `traceback` — and the trigger word

A traceback is the crash report the interpreter writes when an exception goes
**UNCAUGHT**.

That trigger word is the load-bearing half. **Not** "when an error happens" —
errors get caught all the time and produce no traceback. Only when **nothing
catches it** does the interpreter give up, stop the program, and print the report.

Three facts:

1. **Trigger:** an exception went uncaught.
2. **Destination:** the error stream (stderr), not standard out.
3. **Shape:** the whole path of calls from where execution started to where it
   broke — and the last line names the exception.

```python
def a():
    b()

def b():
    int("2.5")

a()
```

```
Traceback (most recent call last):
  File "demo.py", line 7, in <module>
    a()
  File "demo.py", line 2, in a
    b()
  File "demo.py", line 5, in b
    int("2.5")
ValueError: invalid literal for int() with base 10: '2.5'
```

Read it bottom-up: last line = what went wrong; the frames above = how you got
there.

### 4. Iterator causation

An iterator is consumed because it holds **FORWARD-ONLY STATE**: a position that
only ever moves forward, with no rewind.

It is **not** because "it gives one item at a time". A vending machine gives one
item at a time and could be refilled; a spoon dispenses one at a time and can go
back. One-at-a-time describes *how you use it*. It explains nothing about *why it
runs out*.

"Consumed" is a **state** — the pointer has moved past. It does not require that
everything is finished; stop halfway and the part behind you is still gone.

The image to hold on to — **the bug, not the definition**:

```python
it = iter(range(2))       # ONE iterator, hoisted above both loops
for i in range(2):
    for j in it:          # looping over the SAME iterator every time
        print(i, j)
```
```
0 0
0 1
```

The outer loop runs twice, but the inner body runs only on the first pass and then
silently never again — the iterator's pointer reached the end and cannot go back.
Compare with the normal case, where `for j in range(2)` asks the **iterable** for
a fresh iterator on every pass:

```python
for i in range(2):
    for j in range(2):
        print(i, j)
```
```
0 0
0 1
1 0
1 1
```

Same loops, different behaviour — and the only difference is whether a new
iterator is created each pass.

**Turnstile mental model:** you can go through, you cannot come back.

### 5. The modulo identity

```python
a == b * (a // b) + (a % b)
```

This is **the definition**, not a trick. Everything about `//` and `%` on
negatives falls out of it.

Worked on the hard case, `a = 17`, `b = -5`:

1. Raw division: `17 / -5 = -3.4`
2. Floor means **down** the number line, i.e. toward more negative. So
   `floor(-3.4) = -4`. Therefore `17 // -5 = -4`.
3. Put it into the identity: `17 = (-5) * (-4) + r` → `17 = 20 + r` → `r = -3`.
4. So `17 % -5 = -3`.

```python
print(17 // -5, 17 % -5)
print(17 == -5 * (17 // -5) + (17 % -5))
```
```
-4 -3
True
```

**Order matters.** Get the **floored quotient first**, then solve the identity for
`r`. Guessing `r` first and working backwards happens to land sometimes, but it is
not the mechanism.

**Free check:** the sign of `a % b` always follows `b`. `b` was negative, so `r`
came out negative.

**Vocabulary:** `17 / -5 = -3.4` is the raw division; `//` floors that to `-4`.
Call `-4` the **floored quotient** — that is what `//` returns.

### 6. Mutating vs non-mutating — the discriminator, corrected

The starting rule: **check the type first.**

- **Immutable** (`str`, `int`, `tuple`) — mutation is impossible, so every method
  returns something new. Nothing to memorise.
- **Mutable** (`list`, `dict`, `set`) — mutation is possible, so you need a second
  test.

The second test is **not** "methods on mutable types return `None`". That is too
broad: `pop`, `index` and `count` all sit on a list and all return values.

> The rule is about **IN-PLACE MUTATORS** specifically. A method whose job is to
> change the object in place returns `None`, because returning `None` serves no
> other purpose — it exists to stop you believing a new object was made.

In-place mutators on `list`: `append`, `extend`, `insert`, `remove`, `sort`,
`reverse`, `clear`. All return `None`.

```python
l = [3, 1, 2]
x = l.reverse()
y = l.sort()
print(x, y, l)
print(l.pop(), l)
```
```
None None [1, 2, 3]
3 [1, 2]
```

The classic bug this prevents:

```python
l = [3, 1, 2]
l = l.sort()       # silently replaces your list with None
print(l)           # None
```

Python's deliberate **name-pairs** make the design visible: `sort` mutates /
`sorted` returns new; `reverse` mutates / `reversed` returns new.

### 7. `def` versus call — the heart of 1.7

When the **`def` line executes**:

- a **function object** is created, and
- a **name is bound** to it.

That is all. **The body does not run, and no local namespace exists.**

When you **call** it — `greet()` — then and only then:

- a **local namespace** is created, fresh, for that call,
- the body runs,
- the local namespace is **destroyed** when the call ends.

```python
def greet():
    print("hi")

print(greet)       # the object exists; the body has not run
greet()            # NOW the local namespace exists
```
```
<function greet at 0x7f3c8c1e5bc0>
hi
```

> **Definition time builds the object. Call time builds the namespace.**

One precision point carried from 1.2: **the object comes first, and the name is a
label attached to it.** Functions obey the same names-and-objects rule as
everything else in Python.

### 8. Parameters vs arguments

```python
def add(x, y):         # x and y are PARAMETERS — named empty slots
    return x + y

add(3, 5)              # 3 and 5 are ARGUMENTS — the actual values supplied
```

**A parameter is a NAME. An argument is a VALUE.** One is the slot, the other is
what goes in it.

### 9. Return values — and implicit `None`

`return` sends a value back to whoever called the function. **Three cases all
produce `None`:**

```python
def f():
    pass           # no return at all

def g():
    return         # bare return

def h():
    return None    # explicit

print(f(), g(), h())   # None None None
```

**No function returns nothing. Every function returns at least `None`.**

- **Implicit `None`** — the function ended without an explicit `return`, and
  Python supplied `None` without being asked.
- **Explicit `None`** — you wrote it yourself.

This is exactly why `l.sort()` and `l.reverse()` give you `None`: they do their
work and never return a value. Section 6 and this section are the same fact seen
from two directions.

### 10. Scope and the LEGB rule

When Python resolves a name, it searches four namespaces **from the inside out**
and stops at the first hit:

| | Namespace | What it is |
|---|---|---|
| **L** | Local | the current call's own namespace |
| **E** | Enclosing | the namespace of a function this one is written inside |
| **G** | Global | module top level |
| **B** | Built-in | `print`, `len`, `range`, … |

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)          # not local → found in ENCLOSING
    inner()

outer()
print(x)
```
```
enclosing
global
```

Two precision points, both of which matter later:

1. **Enclosing is LEXICAL, not dynamic.** It is decided by **where the function is
   written** in the source, not by where it is called from. If `inner` is written
   inside `outer`, then `outer` is its enclosing scope no matter who calls `inner`
   or from where. **This is the fact closures stand on.**
2. **Global is not "module-level local".** Drop the word *local* — local means
   inside a function. Global is the module's top level, full stop.

"Python has function scope, not block scope" — `if`, `for`, `while`, `try` create
no new scope; only a `def` does — is the **L** of LEGB. Now you have the other
three.

### 11. `__defaults__`

`__defaults__` is an **attribute on the function object** holding a **tuple** of
its default values.

```python
def power(base, exp=2):
    return base ** exp

print(power.__defaults__)          # (2,)
print(power(5), power(5, 3))       # 25 125
```

The confusion to kill:

| | `__defaults__` | the local namespace |
|---|---|---|
| Built when? | at **`def` time** | at **call time** |
| Lives how long? | as long as the function object | dies when the call ends |
| Attached to? | the **function object** | that one call |

One is durable, one is momentary. **When you are asked where a default lives, the
answer is the durable one.**

### 12. Default arguments

```python
def power(base, exp=2):
    return base ** exp

print(power(5))       # 25   — exp not supplied → default 2 used
print(power(5, 3))    # 125  — exp supplied → yours wins
```

A parameter with a default becomes **optional**. If you supply it, yours wins; if
you don't, the value sitting in `__defaults__` is used.

### 13. Functions as first-class objects

A function is an ordinary object. It can be bound to a name, passed as an
argument, and returned from another function.

```python
def greet():
    print("hi")

f = greet            # NO brackets — an alias; nothing runs
print(f is greet)    # True
f()                  # brackets — NOW it runs   -> hi
```

**Bare name = the object. Name + brackets = call it.**

### 14. Nested functions

A function written inside another function. Connecting straight back to LEGB: the
**outer is the inner's ENCLOSING scope**.

```python
def outer():
    def inner():
        print("inner ran")
    inner()

outer()      # inner ran
```

### 15. Closures — deliberately not covered

Closures cannot be understood without seeing code, indentation and a returned
function on screen, so they reopen from zero, in text.

But the argument that framed them is worth keeping, because the objection is
correct:

1. Why did anyone invent writing a function inside a function?
2. We could just write a multiply-by-two function directly.
3. Why not just write `multiply(n, x)` with two parameters?

The honest answer to (3):

> For most cases a two-parameter function is simpler and better, and **closures
> are over-applied**. Closures earn their place when something else is going to
> hand your function exactly **ONE** argument — a `sorted(key=…)` or `map`
> callback, for instance — so the second value has to already be packed inside; or
> when a setting is fixed once and then reused many times.

---

## KEY MENTAL MODELS

- Exception names point at the broken part: name, value, or type.
- `TypeError` is a refusal, not a confusion.
- An exception travels; it never lands in a variable.
- A traceback appears only when an exception goes **uncaught**.
- An iterator is consumed because its position is forward-only. The bug image
  teaches it; the definition doesn't stick.
- Floor the quotient first, then solve the modulo identity for the remainder.
- In-place mutators return `None`; that is what makes `l = l.sort()` a bug.
- `def` builds the object; the call builds the namespace.
- Parameter = name (slot). Argument = value.
- Every function returns at least `None`.
- LEGB stops at the first hit, and E is decided lexically.
- Defaults live on the durable function object, not in the momentary call.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it DOES | The TRAP in it |
|---|---|---|
| `NameError` | Raised when a name is used that was never created | Conflating it with `ValueError` — the name broke, not the value |
| `ValueError` | Right type, wrong value: `int("2.5")` | The type was fine; that's the whole distinction |
| `TypeError` | The operation doesn't exist between these types: `"5" + 3` | Python doesn't "guess" — it refuses |
| exception | A signal that travels outward from the failure | It is not a value that lands and sits |
| `StopIteration` | Signals an exhausted iterator; `for` catches it internally | It's an exception, not "a state" |
| traceback | Crash report written when an exception goes **uncaught** | The trigger is *uncaught*, not merely that an error occurred |
| iterator | Holds a forward-only position; consumed as it advances | "One item at a time" is not the cause |
| iterable | Hands you a fresh iterator each time it's asked | Reusable — unlike the iterator it produces |
| `a == b*(a//b) + (a%b)` | Defines `//` and `%` together | Floor the quotient first, then solve for `r` |
| `//` | Floors toward −∞ | `17 // -5` is `-4`, not `-3` |
| `%` | Remainder; sign follows the divisor | Negative `b` ⇒ negative result |
| in-place mutator | Changes the object, returns `None` | Not *all* methods on mutable types — `pop`/`index`/`count` return values |
| `sort` / `sorted` | Mutates / returns new | `l = l.sort()` silently sets `l` to `None` |
| `reverse` / `reversed` | Mutates / returns new | The name sounds like it produces something |
| `def` | Builds a function object, binds a name | The body does not run; no local namespace yet |
| call `f()` | Builds a fresh local namespace, runs the body | The namespace dies when the call ends |
| parameter | The named slot in the definition | It's a name |
| argument | The value supplied at the call | It's a value |
| implicit `None` | Returned when a function ends with no `return` | No `return`, bare `return`, and `return None` are all the same |
| LEGB | Local → Enclosing → Global → Built-in; stops at first hit | E is **lexical** — where it's written, not where it's called |
| function scope | Only `def` creates scope; `if`/`for`/`while`/`try` don't | That is the **L** only — a quarter of the story |
| `__defaults__` | Tuple on the function object holding default values | Not the local namespace; built at `def` time, not call time |
| default argument | Makes a parameter optional | The value lives on the object, not in the call |
| `f = greet` | Second name for the same object — an alias | No brackets means nothing runs |
| nested function | A function written inside another | Outer is the inner's enclosing scope |

---

## WHAT'S COMING NEXT — SESSION 19

1. A short cold **[RECALL]** block on the three items that didn't land:
   `traceback` (ask for the **trigger** first), iterator causation (shown as a
   bug, not asked as a definition), and `__defaults__` in isolation.
2. **CLOSURES**, from scratch, in text mode, with runnable code — including
   `make_multiplier`, the visible `__closure__`, and the case the objection
   demands: a callback that will only ever be handed one argument. `nonlocal`
   lands here too.
3. **RECURSION**, immediately after closures.
4. The 1.7 tail: `*args` / `**kwargs`, lambdas, docstrings, pure functions vs side
   effects. **1.7 cannot be marked closed until these are done.**

Also outstanding: the spoken Feynman recall for the whole of 1.6.
