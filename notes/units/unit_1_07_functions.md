# Unit 1.7 — Functions

`def` vs call, parameters and arguments, return values, scope (LEGB),
`global` and `nonlocal`, first-class functions, closures, `*args`/`**kwargs`,
lambdas, docstrings, recursion, pure functions, and edge-case analysis.

---

## 1. `def` time versus CALL time — the heart of the unit

When the **`def` line executes**, Python builds a **function object** and
binds a name to it. That is all. **The body does not run, and no local
namespace exists yet.**

When you **call** it, a **local namespace** is created fresh for that call,
the body runs, and the namespace is destroyed when the call ends.

```python
def greet():
    print("hi")

print(greet)       # <function greet at 0x7f3c8c1e5bc0>  — object exists, body has not run
greet()            # hi  — now the local namespace exists
```

> **Definition time builds the object. Call time builds the namespace.**

The object comes first and the name is a label attached to it — the 1.2 rule
applied to functions. A `def` at module level binds the name in the module
namespace, which is how other functions find it.

---

## 2. Parameters vs arguments

```python
def add(x, y):      # x and y are PARAMETERS — named empty slots, declared at definition
    return x + y

add(3, 5)           # 3 and 5 are ARGUMENTS — the actual values supplied at the call
```

**A parameter is a NAME. An argument is a VALUE.** One is the slot, the other
is what goes in it. Passing an argument is an assignment: the parameter name
is bound to the same object the caller passed (1.4 §3).

### 2.1 Positional vs keyword arguments

- A **positional argument** is a bare value, matched **by position**, left to
  right.
- A **keyword argument** is `name=value` in the **call**, matched **by name**,
  so order stops mattering.

```python
def intro(name, role):
    print(name, "-", role)

intro("Ankur", "robotics")              # Ankur - robotics
intro(role="robotics", name="Ankur")    # Ankur - robotics
```

`name=value` on the **call** line is a keyword argument; `name=value` on the
**`def`** line is a **default** (§3). Same shape, different side. And inside a
dict literal it is `{"a": 99}` — a **colon**; `{"a"=99}` is wrong.

**The matching rule:** bare values first, left to right; then each named one
into the parameter of that name; every parameter filled exactly once. Two
ways to break it:

```python
def f(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

f(arg1=1, 10, 20)
# SyntaxError: positional argument follows keyword argument   (compile time)

f(10, 20, arg1=99)
# TypeError: f() got multiple values for argument 'arg1'        (at the call)

f(10, arg3=99, arg2=20)     # 10 20 99 — named ones in any order among themselves
```

### 2.2 The bare `*` — a keyword-only fence

Everything to the right of a bare `*` in a signature must be passed by
keyword; positional filling stops at the star.

```python
def clamp(value, low, high, *, verbose=False):
    if verbose:
        print("clamping", value, "into", low, high)
    return max(low, min(value, high))

print(clamp(150, 0, 100))                   # 100
print(clamp(150, 0, 100, verbose=True))     # clamping 150 into 0 100 / 100
print(clamp(150, 0, 100, True))
# TypeError: clamp() takes 3 positional arguments but 4 were given
```

Why it exists: `bisect_left(a, x, 0, 4, len)` is unreadable; the fence forces
`key=`.

---

## 3. Default arguments and `__defaults__`

```python
def power(base, exp=2):
    return base ** exp

print(power(5), power(5, 3))    # 25 125
print(power.__defaults__)       # (2,)
```

A parameter with a default becomes optional. If you supply it, yours wins;
otherwise the value in `__defaults__` is used.

`__defaults__` is an **attribute on the function object** holding a **tuple**
of the default values. Built at **`def` time**, it lives as long as the
function object. The local namespace is built at **call time** and dies with
the call. One is durable, one is momentary — and that is exactly why a
mutable default accumulates across calls (1.4 §6): the default expression is
evaluated once and stored on the durable thing.

```python
def greet(name="world"):
    return "hello " + name
print(greet.__defaults__)       # ('world',)
```

---

## 4. Return values — explicit and implicit `None`

`return x` sends a value back to the caller and ends the call. **No function
returns nothing; every function returns at least `None`.**

```python
def f():
    pass            # no return at all        -> implicit None

def g():
    return          # bare return             -> None

def h():
    return None     # explicit

print(f(), g(), h())    # None None None
```

This is why `l.sort()` evaluates to `None`: it mutates and never returns a
value. A function that falls off the end of a loop without hitting `return`
returns `None` implicitly.

**A function returns exactly one object.** `return a, b` builds one **tuple**
and returns that; "returning multiple values" is tuples in a costume (1.8).

```python
def limits():
    return -170.0, 170.0

result = limits()
print(type(result), result)     # <class 'tuple'> (-170.0, 170.0)
low, high = limits()            # unpacking
```

Argument count and return value are unrelated: a five-argument function can
return `None`; a zero-argument one can return a dict. Whether `None` is a
problem depends only on what the **caller** does with it — the function is
happy, the caller explodes, and the traceback points at the caller's line.

---

## 5. Scope and the LEGB rule

When Python resolves a name it searches four namespaces **inside out** and
**stops at the first hit**:

| | Namespace | What it is |
|---|---|---|
| **L** | Local | this call's own namespace |
| **E** | Enclosing | the namespace of a function this one is written **inside** |
| **G** | Global | module top level |
| **B** | Built-in | `print`, `len`, `range`, … |

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)        # not local -> found in ENCLOSING
    inner()

outer()         # enclosing
print(x)        # global
```

Two precision points:

1. **Enclosing is LEXICAL, not dynamic.** It is decided by where the function
   is **written** in the source, not by who calls it. This is the fact
   closures stand on.
2. **Global is not "module-level local".** Local means inside a function.
   Global is the module's top level.

"Function scope, not block scope" (1.6 §5) is the **L** of LEGB.

---

## 6. Compile-time locality, `global`, and `UnboundLocalError`

```python
count = 0

def bump():
    print(count)        # line 4: READ
    count = 1           # line 5: ASSIGN

bump()
```
```
  File "ubl.py", line 4, in bump
    print(count)
UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

**The rule:** when the file is compiled, Python scans each function's **whole
body** before any of it runs. Any name that is **assigned anywhere** in the
body is marked **local for the entire function** — including lines above the
assignment. A name classified local never gets the LEGB walk; reads go only to
the local slot. At line 4 the slot is empty: **local + unbound =
`UnboundLocalError`**. Decided at compile time, not line by line.

**Proof by deletion:** remove line 5 and the same line 4 prints `0`, because
nothing assigns `count`, so it is not local, so the lookup walks to the module.

**Three errors, three causes:**

| Error | Cause | When |
|---|---|---|
| `TypeError` | a required argument was not supplied | at the call, before the body runs |
| `NameError` | the name exists nowhere in LEGB | while the body runs |
| `UnboundLocalError` | the name IS local, but no value is bound yet | while the body runs |

### 6.1 `global` — rebinding a module name from inside a function

```python
count = 0

def tick():
    global count            # assignments now target the module namespace
    count = count + 1

tick(); tick()
print(count)                # 2
```

> **`global` is about REBINDING A NAME, not about touching an object.
> Read: free. Mutate: free. Rebind: needs `global`.**

```python
count = 0
def show():
    print(count)            # read only -> works, no global needed

scores = [1, 2, 3]
def add_score():
    scores.append(4)        # mutation of the object, no rebinding -> works, no global
```

---

## 7. `nonlocal` — writing into an enclosing function's variable

The broken counter:

```python
def make_counter():
    count = 0
    def increment():
        count = count + 1       # assignment -> count is LOCAL to increment
        return count
    return increment

c = make_counter()
print(c())
# UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
```

The fix:

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count          # do not make it local — use the enclosing cell
        count = count + 1
        return count
    return increment

c = make_counter()
print(c())                                  # 1
print(c())                                  # 2
print(c.__closure__[0].cell_contents)       # 2  — the cell was WRITTEN to
```

`count` survived between calls even though the first call's frame died: the
cell persisted. **State that outlives the call** — the real payoff.

Three routes, three behaviours:

- read only, no assignment → reads the enclosing cell (plain LEGB, E step);
- assignment without `nonlocal` → the name becomes local →
  `UnboundLocalError`;
- `nonlocal` → the cell itself is the target, for reading and writing.

`nonlocal` targets the **enclosing** cell only; `global` targets the module
namespace. The pair: `nonlocal` says "don't create a local — target the
enclosing function's cell"; `global` says the same one level higher.

---

## 8. Functions are first-class objects

A function is an ordinary object: bindable to a name, passable as an
argument, returnable from another function.

```python
def greet():
    print("hi")

f = greet               # NO brackets — an alias; nothing runs
print(f is greet)       # True
f()                     # hi — brackets are the operator that RUNS it
```

**Bare name = the object. Name + brackets = call it, and what sits in that
spot is whatever it returned.** That is why `sorted(values, key=f())` fails:
it runs `f` immediately with no argument, before `sorted` has an element to
give it. `key=` wants the object `f`, which `sorted` will call itself.

---

## 9. Nested functions

A function written inside another. The outer is the inner's **enclosing**
scope (the E of LEGB).

```python
def outer():
    def inner():
        print("inner ran")
    inner()

outer()     # inner ran
```

---

## 10. Closures

### 10.1 The problem

Return the inner function **without brackets**, so it outlives its
birthplace:

```python
def outer():
    n = 10
    def inner():
        return n * 2
    return inner        # the function OBJECT itself

double = outer()        # outer has finished; its frame — and n — should be gone
print(double())         # 20
```

`outer` is dead by the time `double()` runs, yet `20` comes back. "It checks
its enclosing namespace" breaks here: there is **no live enclosing frame to
check**.

### 10.2 The mechanism

When Python sees at `def` time that an inner function uses a name from the
enclosing function, it does not store that value in the frame. It creates a
separate object — a **cell** — and puts the value in it. Two things reference
the cell: the enclosing frame and the function object being built. **The
frame dies; the cell does not, because the function object still holds it.**

- The bond is a **closure**.
- The captured name (`n`) is a **free variable** — a name the inner function
  *uses* but does not define itself and did not receive as a parameter.
- The cell lives on the function object's attribute **`__closure__`**: a
  tuple with **one cell per free variable**; the value sits in
  `cell.cell_contents`.

```python
print(double.__closure__)                      # (<cell at 0x...: int object at 0x...>,)
print(double.__closure__[0].cell_contents)     # 10
```

> **Definition:** a closure is a function object that binds a free variable
> from its enclosing scope into a cell, so the value **survives** after the
> enclosing function's frame has died.

**The four layers:**

| Expression | What it is |
|---|---|
| `double` | a **name** → the **function object** |
| `double.__closure__` | a **tuple** — one entry per free variable |
| `double.__closure__[0]` | one **cell** — a type, a one-slot box |
| `.cell_contents` | the **value** inside that cell |

```python
def make(a, b):
    def inner():
        return a + b
    return inner

f = make(1, 2)
print(type(f.__closure__))                  # <class 'tuple'>
print(type(f.__closure__[0]))               # <class 'cell'>
print(len(f.__closure__))                   # 2 — one cell per free variable
print(f.__closure__[1].cell_contents)       # 2
```

**Nesting is necessary but not sufficient.** No capture ⇒ no cells ⇒
`__closure__` is `None` (not `()`):

```python
def outer():
    def inner():
        return 5            # captures nothing
    return inner
print(outer().__closure__)  # None
```

### 10.3 Per-object cells

```python
def make_multiplier(x):
    def multiply(num):
        return num * x
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))                     # 10 15
print(double.__closure__[0].cell_contents)      # 2
```

Every call to the factory re-runs `def multiply`, producing **a new function
object with a new cell**. Cells are per-object, never shared. The name `inner`
appears once in the source, but each call pours a new casting from the mould:

```python
a = make_multiplier(10)
b = make_multiplier(10)         # same argument value
print(a is b)                                   # False
print(a.__closure__[0] is b.__closure__[0])     # False
```

**Sharing comes from the same CALL, never from equal values.**

### 10.4 Alias vs new object vs return value

```python
a = make_counter()      # from §7
b = a                   # ALIAS — same object, same cell -> a(), b(), a() gives 1, 2, 3
b = make_counter()      # NEW object, new cell           -> a(), a(), b() gives 1, 2, 1
b = a()                 # the RETURN VALUE (an int)      -> b() raises TypeError: 'int' object is not callable
```

**Brackets give you the return value, not the function.**

### 10.5 The locality trap inside a closure

```python
def make_counter(start):
    def bump():
        start = start + 1       # assignment -> start is LOCAL to bump
        return start
    return bump

print(make_counter(10)())       # UnboundLocalError
```

Assignment anywhere in the body classifies `start` local at compile time → it
is **not** a free variable → no cell, the closure never forms → the read hits
an unbound local. `nonlocal start` fixes it.

### 10.6 Why closures exist at all

**A closure gives no new power.** Anything it does can be done with a dict
plus passing both values every time. What it gives is a **shape**: a function
that needs only **one** argument from outside, with the extra value sealed
inside. Wherever *you* are the caller, the two-parameter version is simpler
and better.

The shape becomes a **necessity** in exactly one situation: **when you are not
the one calling the function** — some other code is, and it will only ever
pass one argument.

```python
def apply(price, pct):
    return price - price * pct / 100

prices = [200, 50, 120]
sorted(prices, key=apply)       # BREAKS — sorted only ever passes ONE argument
```

`sorted` calls `apply(200)`, `apply(50)`, `apply(120)`. It does not know `pct`
exists and there is nowhere to inject it.

```python
def make_discounter(pct):        # pct sealed in a cell
    def apply(price):            # one argument — the shape sorted wants
        return price - price * pct / 100
    return apply

sorted(prices, key=make_discounter(10))     # fits
```

A single closure is fixed. The dynamism is that **the factory can mint any
number of closures at runtime**, each sealing a value unknown at write time,
in a count also unknown at write time:

```python
discounters = {}
for name, p in zip(customers, percents):
    discounters[name] = make_discounter(p)
```

**The class/instance resemblance is real:** behaviour carrying private data.
A class puts data in attributes and behaviour in methods; a closure puts data
in a cell and behaviour in the body. A closure is a function object, not a
class — but "a closure is a poor man's object, and an object is a poor man's
closure."

---

## 11. `sorted` and `key=`

```
sorted(iterable, key=None, reverse=False)
```

- Returns a **new list** in ascending order; the original is untouched
  (`l.sort()` is the in-place mutator, returns `None`). Takes any iterable
  — set, tuple, dict — and always returns a list.
- **`key=`** takes a **function object**. Meaning: do not order elements by
  their own value — first pass each element through this function and order
  by whatever it returns.
- **You do not call that function. `sorted` calls it, internally, once per
  element, passing exactly ONE argument.**
- `reverse=True` flips the order.

```python
def negate(num):
    return -num

print(sorted([10, 4, 8, 2], key=negate))    # [10, 8, 4, 2]
```

**The returned list holds the ORIGINAL elements in a new order — not the key
values.** Keys are readings used to decide order, then discarded.

How `sorted(key=)` works underneath — a list of `(key, element)` pairs (a
dict would break on duplicate keys):

```python
def my_sorted(items, key):
    pairs = [(key(x), x) for x in items]   # key() called once per element, ONE argument
    pairs.sort()                            # sorts on the first slot
    return [x for (k, x) in pairs]          # real elements, new order
```

`list.sort(key=...)` accepts the same `key=`. A method as a key gives a fixed
custom order: `faults.sort(key=record_struct.index)`.

---

## 12. `*args` and `**kwargs`

**Motivation:** `print("a")` and `print("a", "b", "c")` both work. No fixed
parameter list can accept an unknown number of arguments.

- **`*args`** in a signature collects all **leftover positional** arguments
  into a **tuple**.
- **`**kwargs`** collects all **leftover keyword** arguments into a **dict**
  (keys are the names as strings).
- Signature order is fixed: normal parameters, then `*args`, then `**kwargs`.
- `args` and `kwargs` are conventional names; the `*` and `**` are the
  syntax.

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

**The empty cases are `()` and `{}`, never `None`** — one type in all cases,
so the body can loop over them without a special case.

**The mirror rule — the same symbols in a CALL unpack instead of collecting:**

```python
def intro(name, role):
    print(name, "-", role)

pair = ("Ankur", "robotics")
intro(*pair)                                    # spreads a tuple into positional args

info = {"name": "Ankur", "role": "robotics"}
intro(**info)                                   # spreads a dict into keyword args
```

> **Signature side = COLLECT many into one. Call side = SPREAD one into
> many.** Unpacking feeds the call with arguments — as if you had typed them —
> it creates no variables.

The design hole to know about: `def clamp_joints(*angles, **limits)` collects
angles anonymously and limits by name; nothing in that signature pairs an
angle with a joint. Pairing them needs `zip(angles, limits)`, which works
because a dict iterated bare yields its keys in insertion order (1.8).

---

## 13. Lambdas

**A lambda is the EXPRESSION form of a function**: it evaluates to a function
object where it stands, with no name and no statement.

```python
double = lambda x: x * 2
print(double(4))        # 8
print(double)           # <function <lambda> at 0x...>

mul = lambda x, y: x * y    # the parameter list works exactly like a def's
print(mul(3, 4))        # 12
```

Hard limits: the body is **one expression** (no `=`, no blocks, no
statements); its value is **auto-returned**; there is no `return` and there
cannot be one.

Where it earns its keep — a function demanded as an argument:

```python
robots = ["ur12e", "Panda", "kinova"]
print(sorted(robots))                               # ['Panda', 'kinova', 'ur12e']
print(sorted(robots, key=lambda s: s.lower()))      # ['kinova', 'Panda', 'ur12e']

nums = [-3, 7, -1, 4]
print(sorted(nums, key=lambda n: n * n))            # [-1, -3, 4, 7]   original items, ordered by squares
```

Lambdas close over variables exactly like `def`:

```python
def make_adder(k):
    return lambda n: n + k

add5 = make_adder(5)
print(add5(10))                             # 15
print(add5.__closure__[0].cell_contents)    # 5
```

(`key=len` does the length case with no lambda at all.)

---

## 14. Docstrings

A string literal as the **first statement** of a body is stored on the
function object as **`__doc__`** at `def` time — the third member of the
def-time attribute family: `__defaults__`, `__closure__`, `__doc__`.

```python
def clamp(n, limit):
    """Return n capped to the range -limit ... +limit."""
    if n > limit:
        return limit
    if n < -limit:
        return -limit
    return n

print(clamp.__doc__)    # Return n capped to the range -limit ... +limit.
```

- A `#` comment is discarded before the code runs; a docstring is **data on
  the object** — `help()`, editor tooltips and doc tools read it.
- **Position makes it, not the quotes.** A string literal anywhere else in the
  body is an ordinary expression statement: evaluated, result discarded.

```python
def second(x):
    y = x
    """I am NOT the first statement."""
    return y

print(second.__doc__)   # None
```

- Absent docstring → `__doc__` **is `None`**, not `""`. The attribute always
  exists (`"__doc__" in dir(second)` is `True`); "missing" would raise
  `AttributeError`.
- **The absence discriminator:** collectors give back **empty containers**
  (`()`, `{}`) — the thing exists, empty. Optional attributes give back
  **`None`** — never created. `""` would mean "documented as blank".
- Convention: triple quotes, imperative one-liner ("Return …", not "This
  function returns …").

---

## 15. Recursion

**Definition:** a function that calls itself, where each call gets a
**strictly smaller** version of the same problem, and at least one input is
small enough to answer with no further call.

- **Base case** — answered outright, no recursive call.
- **Recursive case** — calls itself on a smaller input and builds its answer
  from what comes back.

**Nothing new is happening in the machinery.** Every call gets its own frame
with its own locals (1.1). Recursion just means **several frames of the same
function are alive at once** — each holding its own `n`. There is no single
mutating `n`.

### 15.1 Pre-order vs post-order

Same function, same base case; the only difference is which side of the call
the `print` sits on.

```python
def countdown(n):              # work on the way DOWN (pre-order)
    if n == 0:
        print("liftoff")
        return
    print(n)
    countdown(n - 1)
# countdown(3) -> 3 2 1 liftoff

def countdown(n):              # work on the way BACK UP (post-order)
    if n == 0:
        print("liftoff")
        return
    countdown(n - 1)
    print(n)
# countdown(3) -> liftoff 1 2 3
```

Why the second reverses: each frame parks mid-body waiting for the call below
it; when that returns, the frame resumes on the next line — deepest first.
`0` never prints in either: that frame hits the base case and returns before
reaching `print(n)`.

### 15.2 Value-returning recursion — assembled on the unwind

```python
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

# total(4) -> 4 + total(3)        parked, waiting for a number
#   total(3) -> 3 + total(2)      parked
#     total(2) -> 2 + total(1)    parked
#       total(1) -> 1 + total(0)  parked
#         total(0) -> 0           base case answers outright
# unwinding: 1 -> 3 -> 6 -> 10
```

`n + total(n - 1)` cannot finish until the inner call returns, so every frame
sits half-evaluated holding its own `n`.

### 15.3 The identity-value rule

**The base case must return the IDENTITY for the operation being used:** `0`
for `+`, `1` for `*`, `[]` for list concatenation, `""` for strings. Return
`0` from `factorial`'s base and the entire product collapses to zero.

### 15.4 Termination — two conditions, both required

1. A base case exists that returns without recursing.
2. Every recursive call moves the input **strictly closer** to it.

Missing either ⇒ `RecursionError`. `broken(5)` with base `n == 0` and step
`n - 2` runs 5, 3, 1, −1, −3, … and steps straight past zero. **A base case
that exists but is never landed on is not a base case.** `RecursionError`
fires at CPython's default depth of 1000 — a guard against runaway memory,
not a law of recursion.

### 15.5 Printer vs calculator

Does the function **print**, or does it **return**?

```python
# printer                              # calculator — the testable design
def count_down_by(n, step):            def count_down_by(n, step):
    if n <= 0:                             if n <= 0:
        return                                 return []
    print(n)                               return [n] + count_down_by(n - step, step)
    count_down_by(n - step, step)

# assert count_down_by(10, 3) == [10, 7, 4, 1]   works only for the calculator
```

A printer: bare `return` at the base, recursive call made **without**
`return` in front, implicit `None` overall. A calculator: returns on every
branch. Mixing them produces stray values nobody uses. A calculator can be
printed, summed, sliced, fed onward — and **tested**. `n <= 0` was the right
base here: from 10 by 3 the values run 10, 7, 4, 1, −2 and never touch zero.

### 15.6 The boundary bug

```python
def digit_sum(n):
    if n < 10:                  # n <= 10 would return 10 whole: digit_sum(10) -> 10
        return n
    return n % 10 + digit_sum(n // 10)

# digit_sum(472) -> 2 + digit_sum(47) -> 2 + (7 + digit_sum(4)) -> 2 + 7 + 4 = 13
```

One character in the comparison is the whole bug, and only testing the exact
boundary value finds it.

---

## 16. Pure functions vs side effects

- **Pure** = two conditions: output depends **only** on the arguments, AND
  nothing outside the function changes. Same input, same output, forever.
- **Side effect** = anything a function does beyond returning a value:
  printing, writing a file, mutating something it was handed, changing a
  global.

Neither is better. Side effects are the point of a program — a program that
touches nothing is a heater. The rule: **don't hide them, don't mix them.** A
function that both computes and mutates is hard to test, because you cannot
check its answer without triggering its damage.

The disguised mutator — takes input, returns output, still impure:

```python
def add_item(basket, item):
    basket.append(item)     # mutates the caller's list
    return basket           # hands back the SAME object

def add_item(basket, item):
    return basket + [item]  # pure: new list, original untouched
```

The `is` check exposes it: `scaled = scale(data)` then `scaled is data` →
`True` means you got your own object back, not a fresh result.

---

## 17. Edge-case analysis — the five checks

Not a knack. **A checklist run against the structure of the code.** Bugs
cluster in five places:

| Hook | Check | What you try |
|---|---|---|
| **Boundary** | 1 | Any `<`, `<=`, `>`, `>=` has one exact value where the branches meet. Test **that** value, not values near it. |
| **Khaali** | 2 | Empty / zero / nothing: `0`, `""`, `[]`, `None`. |
| **Ek** | 3 | Exactly **one** — the smallest non-empty case. A loop that runs once takes a different path. |
| **Bahar** | 4 | Outside what you silently assumed: negative when you assumed non-negative; **float when you assumed int**; wrong type. Noticing the assumption is the skill. |
| **Mila** | 5 | Two things that must agree: base case ↔ step; **spec ↔ code**. Read the docstring one sentence at a time and point at the line that keeps it. No line behind a sentence ⇒ bug. |

> *"Boundary pe khaali ek bahar mila."*

Applied:

```python
def first_char(word):
    if len(word) <= 1:      # == 1 loops forever on "": ""[:-1] is "" and never shrinks
        return word
    return first_char(word[:-1])
```

`Mila` also rules things *not* bugs: `take_last([])` raising `IndexError` is
fine if the spec says the list may be assumed non-empty. Check 5 is the only
one that compares your own words against the code; the other four operate on
the input.

**A check is a case you RAN and a value you looked at.** An `if` in the body
is not a check. Scan all five; report the ones that bite.

---

## 18. Design rules that came out of this unit

- **One copy of a decision (DRY).** A rule written in four places does not
  fail today; it fails the day the rule changes, in the copy with no test on
  it. One function owns the rule; everyone else calls it. The mechanical
  test: count the places that compare against the same constant — it must
  be 1.
- **Compute once, name it.** Calling `clamp_one(...)` three times with the
  same arguments is the same duplication one level down. `safe = clamp_one(...)`
  then use `safe`; the name also documents what the value is.
- **A sentinel must be something the data can never contain.** `None` for
  "not found" in a list that may hold `None` is a bug; walking positions
  makes it impossible. `0` and `-1` are both real indices in Python.
- **Dead code** — present, reachable-looking, unable to affect the result:
  a guard left behind when the spec changed; an `except TypeError` behind a
  short-circuit guard that guarantees the comparison never raises. Passing
  tests never reveal it; only reasoning about the guard does.
- **Green tests are not evidence of a model.** Code can be right for the
  wrong reason; keep asking *why does this work* about code that already
  passes.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| `def` | builds a function object, binds a name | the body does not run; no local namespace yet |
| call `f()` | builds a fresh local namespace, runs the body | the namespace dies when the call ends |
| parameter / argument | the name in the `def` / the value at the call | not interchangeable words |
| keyword argument | `name=value` in a **call**, matched by name | on the `def` line the same shape is a default |
| ordering rule | positional first, then named; each slot once | bare after named = `SyntaxError`; double-fill = `TypeError` |
| bare `*` | positional filling stops; right side keyword-only | 4th positional → `TypeError ... 3 positional arguments` |
| default argument | value used when omitted; stored in `__defaults__` | evaluated once at `def`; mutable defaults accumulate |
| `__defaults__` | tuple on the function object | an attribute, not the local namespace |
| implicit `None` | no `return` / bare `return` / `return None` are the same | the caller is where `None` becomes a problem |
| `return a, b` | builds **one** tuple | a function never returns more than one object |
| LEGB | Local → Enclosing → Global → Built-in; stops at first hit | E is lexical — where written, not where called |
| compile-time locality | assignment anywhere in the body ⇒ local everywhere in it | the line above the assignment is already local |
| `UnboundLocalError` | local name, no value yet | not `NameError` — the name exists |
| `global x` | assignments target the module namespace | read and mutate never need it; only rebinding |
| `nonlocal x` | assignments target the enclosing cell | never module-level; that is `global` |
| `f` vs `f()` | the object vs the return value | `key=f()` runs it immediately and fails |
| free variable | used by the inner function, defined outside it | the thing that triggers a closure |
| cell / `__closure__` | a one-slot box per free variable; `__closure__` is the tuple | `None` when nothing is captured; sharing needs the same CALL |
| closure | function object + cell surviving a dead frame | nesting alone is not enough |
| why closures | a one-argument shape for a caller you do not control | for your own calls, two parameters is better |
| `sorted(x, key=f)` | new list; `f` called once per element with one argument | returns original items, not key values |
| `*args` / `**kwargs` | collect leftovers → tuple / dict | empty is `()` / `{}`, never `None` |
| `*x` / `**d` in a call | unpack into separate arguments | the mirror of collecting |
| lambda | expression that evaluates to a function object | one expression, auto-returned, no statements |
| docstring / `__doc__` | first-statement string, stored at `def` time | position makes it; absent → `None`, not `""` |
| recursion | several frames of one function alive at once | each frame has its own `n` |
| pre-/post-order | work before / after the recursive call | post-order runs on the unwind, deepest first |
| base case | returns the identity for the operation | `0` for `+`, `1` for `*`, `[]` for lists |
| termination | base case exists AND every step lands closer to it | stepping past the base is `RecursionError` too |
| `RecursionError` | CPython's 1000-frame guard | not a law of recursion |
| printer vs calculator | prints / returns on every branch | only the calculator is testable |
| pure function | output from arguments only; nothing outside changes | returning the object you mutated is not pure |
| five checks | boundary · khaali · ek · bahar · mila | a check is a case you ran, not an `if` in the body |
| DRY | one copy of a decision | the untested copy drifts and the suite stays green |
| sentinel | a value the data can never contain | `None` in a list of `None`s; `-1` is a real index |
| dead code | cannot affect the result on any input | tests never find it |
