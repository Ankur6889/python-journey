# SESSION 11 NOTES — The Depth Doctrine, and Closing 1.4

**Topics: the three levels of understanding · the GIL and where concurrency sits ·
what conversion functions do to the original · `ValueError` vs `TypeError` ·
`//` vs `int()` on negatives · aliasing, demonstrated properly · mutating methods
return `None` · the mutable-default fix, correctly written · `is None`, both
halves · shallow vs deep copy**

This closes 1.4.

---

## SELF-TEST — answer these cold before reading on

Notes closed. Where you cannot retrieve, say "gap here" and move on — a named gap
is worth more than a looked-up sentence.

1. `x = "42"` then `y = int(x)`. After the second line, what is `x` — value and
   type? In one sentence, what did `int()` do to `x`?
2. Why does `int("2.5")` fail while `int(2.5)` succeeds? Name the exact error.
3. Name the error `"5" + 3` raises, and say why it is a *different* error from Q2.
4. `-7 // 2` — value? And `int(-3.5)`? Why do they disagree?
5. Give an example of implicit conversion **succeeding**. What makes it safe when
   `"5" + 3` is not?
6. Which built-in types are mutable, which immutable? At least three each side.
7. Define aliasing in one sentence. Then say why demonstrating it with
   `x = 5; y = x` proves the definition but teaches nothing about why it matters.
8. A function receives a list. Give the one-line rule that decides whether the
   caller sees the change, plus the two code fragments either side of it.
9. What does `lst.append(5)` return? What is wrong with `lst = [].append(5)`?
10. The mutable default argument trap: what goes wrong, **where does the default
    list actually live**, and write the fix out in full.
11. Why `is None` and not `== None`? Give both halves of the reason.
12. You take a shallow copy of a list containing another list, then append to the
    inner list. Does it show in the original? Explain in terms of objects and
    names.
13. State the three levels of the Depth Doctrine, which level this course targets,
    and the exception.

Answers at the back.

---

## FULL TEACHING

### 1. The Depth Doctrine

Three levels of understanding, for any topic:

| Level | Name | What it means | Example: `list.append()` |
|---|---|---|---|
| 1 | **User** | You can operate it | "`append` adds an item, it works" |
| 2 | **Model** | You know what it does to the system; you can predict and debug | "`append` mutates the object in place, so every alias sees the change" |
| 3 | **Implementation** | You know how it is built underneath | CPython's C source: how the list grows, how memory is reallocated |

**This course targets Level 2 — deliberately, and almost everywhere.**

Below Level 2 is recall that collapses when the scaffold is removed. Above Level 2
is over-investment against a deadline with no schedule slack.

Applied consistently: **Python** → Level 2, not CPython's C internals. **Classical
control** → Level 2, not Laplace transforms or Lyapunov stability derived by hand.
**ROS controllers** (state, position, twist) → Level 2: *use them, do not build
them.*

**The exception.** Level 3 is the target for the *core* — the things you intend to
**build** rather than merely use: RL, robot learning and policy architectures,
simulation, and the mathematics underneath. Depth there is the deliverable, not
indulgence.

**Who actually works at Level 3 in Python?** Core CPython developers; performance
engineers inside NumPy and PyTorch, where a single allocation matters; and authors
of C extensions. Note that **JAX and PyTorch *are* that layer** — C and C++
underneath, a Python face on top. The job is to *use* those tools expertly, not to
write them.

**A distinction that is expensive to get wrong:** Python's C internals are one
kind of depth. **Algorithmic depth is a completely different kind.** Interview
difficulty lives in the second, not the first.

**The scope test** when something interesting appears mid-session: not *"is this
useful?"* but **"is this Level 3 on something outside the core?"** If yes —
parking lot.

### 2. Concurrency, threads, and the GIL — placed, not yet taught

Multithreading is **not** Level 3 / C-internals material. It is a Level 2 topic in
the concurrency direction, and in scope.

**The GIL — Global Interpreter Lock.** In one line: in CPython, only one thread
executes Python bytecode at a time, even on a multi-core CPU.

The consequence is a practical fork:

- **CPU-bound work** — heavy computation — gains nothing from threads. Use
  `multiprocessing`.
- **I/O-bound work** — waiting on a sensor, a camera frame, a network read — is
  exactly where threads *do* pay.

That distinction is daily bread in a ROS 2 stack.

It is deferred deliberately: threads plus mutation means two names on one object
being written from two places at once. Teaching that before single-threaded
mutation is cold-solid is teaching a race condition to someone still consolidating
what a shared object is.

### 3. What a conversion function does to the original

```python
x = "42"
y = int(x)
print(x, type(x))
print(y, type(y))
```
```
42 <class 'str'>
42 <class 'int'>
```

> `int()` did not touch `x`. It **read** `x`'s value and **returned a brand-new
> integer object**, which was bound to the name `y`. `x` is still the string
> `"42"`.

The self-contradiction to watch for: "`print(x)` gives `42` as a string" *and*
"`int()` cast that string into an integer" cannot both be true. If `int()` had
cast `x`, `print(x)` would show an integer.

**Why this one sentence carries so much weight:** it *is* subsection 1.4.
Everything in 1.4 — aliasing, mutation, the default-argument trap — is built on
one distinction: **does an operation change the original object, or return a new
one?**

### 4. `ValueError` vs `TypeError`

```python
int("2.5")   # ValueError  — correct TYPE (str), but the VALUE cannot be parsed
"5" + 3      # TypeError   — no valid operation BETWEEN these two types
```

- **`ValueError`** — right kind of thing, wrong content.
- **`TypeError`** — these types do not work together at all.

And on the mechanism for `int("2.5")`: Python is **not** attempting a two-stage
conversion and failing halfway. Its string parsing simply **refuses a decimal
outright** — it will not parse a float out of a string when asked for an int.

### 5. Implicit conversion, succeeding

```python
result = 1 + 2.0      # int widened to float — safe, lossless
print(result, type(result))
```
```
3.0 <class 'float'>
```

If implicit conversion never worked it would not have a name. It succeeds where
the direction is **unambiguous and lossless** — an int can always be represented
as a float. With `"5" + 3` there is no safe direction at all, so Python raises.

### 6. `//` and `int()` disagree on negatives

```python
print(-7 // 2)      # floor division: floors toward -infinity
print(int(-3.5))    # int(): truncates toward zero
```
```
-4
-3
```

`5 // 2 → 2` discriminates nothing, because `int(2.5)` also gives 2. **The
negative case is the only place the two rules separate.**

### 7. Aliasing, demonstrated properly

Aliasing is **one object bound by multiple names**. Demonstrating it with
integers proves the definition and demonstrates nothing:

```python
x = 5
y = x
x is y      # True — and now what?
```

There is nothing you can *do* to `5` through either name. **Aliasing is only
dangerous when the shared object can be changed through one name and seen through
the other.** With an immutable that can never happen.

The demonstration it needs — with `id()`, which shows the identity itself rather
than just answering whether two names share one:

```python
a = [1, 2, 3]
b = a
print(id(a), id(b), a is b)
b.append(99)
print(a)
```
```
140234... 140234... True
[1, 2, 3, 99]
```

### 8. Mutate vs rebind inside a function

```python
def add_to_list(value, lst):
    lst.append(value)          # MUTATES the object — caller sees it

def add_to_list(value, lst):
    lst = lst + [value]        # REBINDS a local name — caller sees nothing
```

`lst + [value]` builds a **new** object bound to a local name, and that name is
discarded when the function returns.

Aside worth holding: `print(add_to_list(5, x))` prints `None`, because the
function has no `return`. The append still happens.

### 9. Mutating methods return `None`

**The rule: mutating methods return `None`.** They change the object; they do not
hand it back.

```python
lst = [].append(5)    # BUG — lst is None, the list is discarded
```

`lst.append(x)` is a **statement**, never the right-hand side of an assignment.

### 10. The mutable default fix, correctly written

Two bugs commonly appear together in the "fix":

```python
def jodo(value, lst=None):
    if lst is None:
        lst = [].append(value)     # BUG 1: append returns None
    return lst                     # BUG 2: append only happens inside the if
```

**Bug 1** — `.append()` mutates and returns `None`, so `lst` is bound to `None`.
**Bug 2** — pass your own list, `jodo(5, my_list)`, and nothing is appended at
all; the function does nothing.

The correct fix — **sentinel check first, then the work, outside the branch**:

```python
def jodo(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst
```

And on where the default lives: **not** in the function's namespace. The namespace
is created fresh on every call and destroyed on return — **if the list lived there
it would vanish each time and there would be no trap.** It lives on the
**function object**, in `__defaults__` (plural, a tuple), which outlives every
call. That is *why* it accumulates.

### 11. `is None` — both halves of the reason

1. **`None` is a singleton** — one object for the whole program — so identity is
   the correct question to ask.
2. **`==` asks "equal value?", and any class can define its own `__eq__`** and
   answer that question however it likes, including lying about `None`. `is` asks
   "same object?" — identity, unfakeable.

### 12. Shallow vs deep copy (closes 1.4)

This is the direct consequence of aliasing, not a separate topic.

- **`b = a`** is not a copy at all. One object, two names.
- **`b = a.copy()`** builds a new **outer** list. Append to one and the other is
  untouched.
- **The trap:** if the list contains another list, the outer list is new but the
  **inner list is not copied — it is aliased.** Both outer lists point at the same
  inner object, so mutating it through one shows up in the other.
- **`copy.deepcopy()`** recurses all the way down: new inner list, new list inside
  that. Nothing shared.

**One line: shallow = only the top layer is new. Deep = new all the way down.**

```python
import copy

a = [[1, 2], [3, 4]]
shallow = a.copy()
deep = copy.deepcopy(a)

print(id(a[0]), id(shallow[0]), id(deep[0]))
shallow[0].append(99)
print(a)
print(deep)
```
```
140234... 140234... 140999...
[[1, 2, 99], [3, 4]]
[[1, 2], [3, 4]]
```

`a[0]` and `shallow[0]` share an id; `deep[0]` does not.

The language matters here: the inner list was **not** "copied as it is". It was
**aliased**. No new inner object was made; a second name was attached to the
existing one. That is the entire concept.

---

## KEY MENTAL MODELS

- Level 2 — predict and debug — is the target; Level 3 only for what you intend to
  build.
- The GIL makes threads useless for CPU-bound work and valuable for I/O-bound work.
- A conversion function reads the original and returns a new object. It changes
  nothing.
- `ValueError` = right type, unusable value. `TypeError` = these types don't
  combine.
- `//` floors toward −∞; `int()` truncates toward zero. They only differ on
  negatives.
- Aliasing only *matters* for mutable objects.
- Mutating methods return `None` — they are statements, not expressions.
- A mutable default lives on the durable function object, which is why it
  accumulates.
- Shallow copies duplicate one layer and alias everything below it.

---

## REFERENCE CHECKLIST — 1.4 Mutability, complete

| Item | What it does | The trap |
|---|---|---|
| **Mutable types** | `list`, `dict`, `set` — can change in place | Same `id()` after mutation. Every alias sees it |
| **Immutable types** | `int`, `float`, `bool`, `str`, `tuple` — cannot change | "Changing" one builds a NEW object and rebinds the name |
| **Aliasing** | `b = a` binds a second name to the SAME object | Never a copy. `a is b` is True. Only *matters* for mutables |
| **`id()`** | Shows an object's identity | Same id + different contents = mutation. Different id = rebinding |
| **Passing to a function** | Binds a new LOCAL name to the SAME object | Passing IS assignment |
| **MUTATE** (`lst.append(v)`) | Acts on the object | Caller **sees** the change |
| **REBIND** (`lst = [v]`) | Rebinds the local name only | Caller sees **nothing** |
| **Mutating methods** | `.append()`, `.sort()`, `.extend()` return **`None`** | Never `x = lst.append(v)` — a statement, not an expression |
| **Default arguments** | Evaluated **ONCE**, when `def` executes | A mutable default accumulates across calls, forever |
| **`__defaults__`** | Tuple on the **function object** holding the defaults | NOT in the frame, NOT in the namespace — those are rebuilt each call |
| **The fix** | `lst=None` + `if lst is None: lst = []` | Sentinel check first, work **outside** the branch |
| **`is None`** | Identity against the singleton | `==` can be overridden by `__eq__` and lie; `is` cannot be faked |
| **`b = a.copy()`** | New OUTER object; nested objects **aliased** | Shallow. Nested mutation leaks through |
| **`copy.deepcopy(a)`** | New objects all the way down | Nothing shared. Slower |

---

## SELF-TEST ANSWERS

**A1.** `x` is still the string `"42"`, type `str`. `int()` did **nothing** to
`x` — it read `x`'s value and returned a brand-new integer object, bound to `y`.

**A2.** `int(2.5)` succeeds because numeric conversion is **lenient** — it
truncates toward zero. `int("2.5")` fails because string parsing is **strict**:
it will not parse a decimal out of a string when asked for an int. The error is
**`ValueError`** — the type is right (`str`), the value cannot be parsed.

**A3.** **`TypeError`.** Different from `ValueError` because the problem is not
the content of the value but the combination of types: there is no safe direction
between `str` and `int`, so Python refuses to guess (unlike JavaScript, which
would produce `"53"`).

**A4.** `-7 // 2` is **`-4`**; `int(-3.5)` is **`-3`**. They disagree because `//`
**floors toward −∞** while `int()` **truncates toward zero**. On positives they
agree, which is why `5//2 → 2` demonstrates nothing.

**A5.** `1 + 2.0 → 3.0`, type `float`. Safe because the widening is **lossless and
unambiguous** — an int can always be represented as a float, and there is only one
sensible direction. With `"5" + 3` there is no safe direction at all.

**A6.** Mutable: `list`, `dict`, `set`. Immutable: `int`, `float`, `bool`, `str`,
`tuple`.

**A7.** Aliasing is when two or more names refer to the **same object**, so a
mutation through either is visible through both. `x = 5; y = x` proves the
definition — `x is y` is True — but teaches nothing about why it matters, because
`5` is immutable and there is nothing you can *do* to it through either name.

**A8.** The rule: **MUTATE and the caller sees it; REBIND and the caller does
not.**
```python
def f(lst): lst.append(99)      # mutates the object   → caller sees [.., 99]
def f(lst): lst = [99]          # rebinds a local name → caller unaffected
```

**A9.** `lst.append(5)` returns **`None`** — it mutates the object and hands
nothing back. `lst = [].append(5)` therefore binds `lst` to `None`, discarding the
list entirely. Mutating methods are statements, never the right-hand side of an
assignment.

**A10.** A mutable default accumulates across calls: `[1]`, then `[1,2]`, then
`[1,2,3]`. Because the default expression is evaluated **once**, when the `def`
statement executes — not per call. The list lives on the **function object**, in
**`__defaults__`**, which outlives every call. (Not in the frame or namespace —
those are rebuilt and destroyed each call, which is precisely why there would be
no trap if it lived there.) The fix:
```python
def jodo(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst
```

**A11.** Two halves. (a) `None` is a **singleton** — one object for the whole
program — so identity is the correct question. (b) `==` asks about **value
equality** and any class can override `__eq__` to answer however it likes,
including lying about `None`. `is` compares identity directly and cannot be faked.

**A12.** **Yes, it shows up.** A shallow copy builds a new **outer** object, but
the nested list is **not copied — it is aliased**. One inner object, now reachable
by two names. Mutating it through either is visible through both.
`copy.deepcopy()` recurses all the way down and shares nothing.

**A13.** **Level 1 User** (can operate it), **Level 2 Model** (knows what it does
to the system; can predict and debug), **Level 3 Implementation** (knows how it is
built underneath). **This course targets Level 2** almost everywhere. **The
exception:** Level 3 for the core you intend to build rather than use — RL, robot
learning, simulation, and the mathematics underneath them.

---

## WHAT'S COMING NEXT — SESSION 12

1. Cold re-tests, notes closed: the mutable default trap (what goes wrong, where
   the list lives, the fix); what `int()` does to the object you pass it;
   `bool("False")` and `10/2` value and type; `ValueError` vs `TypeError`;
   shallow vs deep copy shown in text with `id()`.
2. Open **1.5 Operators and Expressions**. Terms to define before they are used
   twice: **operand, expression vs statement, precedence, coercion.** Leading
   items: `//` on negative numbers, and **augmented assignment** — `+=` on a list
   mutates in place, on an int/string/tuple it rebinds.
3. Spoken Feynman recall for 1.3 and 1.4.
