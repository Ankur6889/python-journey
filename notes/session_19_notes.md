# SESSION 19 NOTES — Tuesday 12 August 2026

**Topics: closures built from scratch · free variables, cells and `__closure__` ·
why closures exist (the `sorted(key=)` shape) · `sorted` and `key=` from zero ·
alias vs new object vs return value · `nonlocal` and writing into a cell ·
`UnboundLocalError` vs `NameError` vs `TypeError`**

1.7 Functions is **not** closed — the tail is still pending.

---

## SELF-TEST — answer these cold before reading on

1. Define a closure in one sentence. What is a *free variable*?
2. `outer()` has already returned. Its local `n = 10` should be gone. Why does the
   returned `inner()` still see 10?
3. Where is the captured value actually stored? Name the attribute and the thing
   inside it.
4. `double = make_multiplier(2)` and `triple = make_multiplier(3)`. Why don't they
   share a value? If the factory runs 5 times in a loop, how many cells exist, and
   why?
5. What does `key=` do in `sorted`, and who calls that function?
6. Does `sorted(..., key=f)` return the key values or the original elements?
7. `b = a`, `b = make_counter()`, `b = a()` — three different things. Say what
   each gives you.
8. Why does an `increment` that does `count = count + 1` raise, and which
   exception?
9. What does `nonlocal` change? Name the three routes and their behaviours.
10. Distinguish `TypeError`, `NameError` and `UnboundLocalError` by cause and by
    *when* each fires.

---

## FULL TEACHING

### 1. Closures — built from scratch

**Step 1 — nothing new, just LEGB:**

```python
def outer():
    n = 10
    def inner():
        return n * 2      # n is not inner's local
    return inner()        # called inner, returned result

print(outer())            # 20
```

`inner` has no local `n` → LEGB step **E** → found in `outer` → 20. No magic.

**Step 2 — one change, and the whole problem appears:**

```python
def outer():
    n = 10
    def inner():
        return n * 2
    return inner          # NO brackets — the function object itself

double = outer()          # outer has finished and returned
print(double())           # 20
```

`outer` is already dead — its local frame, including `n = 10`, should have died
the moment it returned (the same rule that separates `__defaults__` from the local
namespace). So why isn't this a `NameError`?

The half-answer "it checks its enclosing namespace" **breaks here**: *which*
enclosing namespace? `outer` is not alive. **There is no live frame left to
check.** That contradiction is exactly what closures exist to resolve.

**Where could the value be?** Three candidates, and the reasons two of them fail
are the teaching:

- **`outer.__defaults__`?** No. `__defaults__` exists only for *parameters'*
  default values and is fixed at `def` time; `n` is neither a parameter nor known
  at `def` time. Timing and role both mismatch. (Good instinct though — Python
  really does store it on a dunder attribute.)
- **The module namespace?** No. The module namespace is **one, shared**. Two
  closures from the same maker would overwrite each other's value. And a dying
  frame's local has no business being pushed out to global.
- **The inner function object.** **Correct** — that is the one thing that escaped
  alive and is sitting in `double`.

> **The mechanism:** if `inner` is what survives, and `inner` is what needs `n`,
> then bind `n` **to the inner object itself**. The bond lives on the object, not
> the frame — so it does not die when the frame dies.
>
> - That bond is a **closure**.
> - The captured variable (`n`) is a **free variable** — free because it is not
>   `inner`'s own local, yet `inner` holds it.
> - It is stored in the attribute **`__closure__`**: a tuple with one **cell** per
>   free variable, and the value sits in `cell.cell_contents`.

```python
double = outer()
print(double.__closure__)                      # (<cell at 0x...: int object>,)
print(double.__closure__[0].cell_contents)     # 10
```

**Per-object cells:**

```python
def make_multiplier(x):
    def multiply(num):
        return num * x
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))                              # 10
print(triple(5))                              # 15
print(double.__closure__[0].cell_contents)    # 2
```

The causation, precisely: **every call to `make_multiplier` runs `def multiply`
again, producing a brand-new function object with a brand-new cell. Cells are
per-object, never shared** — which is exactly what the module-namespace route
could not provide.

### 2. Why closures at all?

The honest answer, after the obvious objections ("two parameters will do",
"hardcode it", "a loop and a dict will do") — all of which are **correct** in
their own cases:

> **A closure gives no new power.** Anything it does can be done with a dict plus
> passing both values every time. What it gives is a **shape**: a function that
> needs only **one** argument from outside, with the extra value sealed inside.

That shape becomes a **necessity** in exactly one situation: **when you are not
the one calling the function** — some other code is, and it will only ever pass
one argument.

```python
def apply(price, pct):
    return price - price * pct / 100

prices = [200, 50, 120]
sorted(prices, key=apply)        # BREAKS — sorted only ever passes one argument
```

`sorted` calls `apply(200)`, `apply(50)`, `apply(120)`. It does not know `pct`
exists. There is **no place to inject it**. The two-parameter version genuinely
cannot be used here.

```python
def make_discounter(pct):        # pct sealed in a cell
    def apply(price):            # one argument from outside — the shape sorted wants
        return price - price * pct / 100
    return apply

sorted(prices, key=make_discounter(10))        # fits
```

**And the follow-up worth having:** a *single* closure is fixed — one discounter
always applies 10%. The dynamism is not inside one closure. It is that **the
factory can mint any number of closures at runtime**, each sealing a value that
was unknown at write time:

```python
discounters = {}
for name, p in zip(customers, percents):
    discounters[name] = make_discounter(p)   # count unknown, values unknown at write time
```

Two levels of dynamism: **which** value gets sealed, and **how many** such
functions get made.

### 3. `sorted` and `key=` from zero

- `sorted(list)` returns a **new list** in ascending order; the original is
  untouched.
- `key=` is an optional keyword argument taking **a function name**.
- Meaning: don't order elements by their own value — first pass each element
  through this function, and order by whatever it returns.
- **The load-bearing part: you do not call that function.** `sorted` calls it,
  internally, once per element, passing **exactly one argument**.

Picture: a sorting machine you hand a **scale** to. You choose the scale; the
machine puts each box on it and reads it.

```python
sorted([10, 4, 8, 2], key=negate)   # keys computed: -10, -4, -8, -2
                                     # output: [10, 8, 4, 2]   <- ORIGINAL elements
                                     # NOT:    [-10, -8, -4, -2]
```

**Keys are readings used to decide order, then discarded.**

### 4. Reverse-engineering `sorted(key=)`

The skeleton: run the function on each element → get key values → pair them with
elements → compare on keys → lay out the real elements.

**Why not a dictionary keyed by the key value?** Two reasons:

- **dict keys are unique** — two elements with the same key value would overwrite
  each other and one element would vanish. Duplicates are normal in sorting.
- **The relationship is backwards**: you attach a key *to* each element, not index
  elements *by* key.

The correct structure is a list of `(key, element)` pairs:

```python
def my_sorted(items, key):
    pairs = [(key(x), x) for x in items]   # key() called once per element, ONE argument
    pairs.sort()                           # sorts on the first slot
    return [x for (k, x) in pairs]         # real elements, new order
```

Note that the `key(x)` line is literally the thing named above: the library
calling your function, one argument at a time.

### 5. Same name, different objects

If the inner function is always written as `inner` — one name in the source — are
`double` and `triple` the same function with two aliases?

**No — separate objects.** The name appears once in the source, but **every call
to the outer function re-runs the `def` line and mints a fresh function object
with a fresh cell.**

**Mould / casting picture:** `def inner` is the mould; the name is written on the
mould; each call pours a new casting.

```python
a = outer()
b = outer()
print(a is b)      # False   <- different objects
```

> **Rule:** copying a name **without brackets** = alias (same object). Calling
> **with brackets** = a new object every time.

**The class/instance family resemblance** is real: behaviour that carries private
data with it. A class puts data in attributes and behaviour in methods; a closure
puts data in a cell and behaviour in the function body. The saying: *"a closure is
a poor man's object, and an object is a poor man's closure."* Label precision: a
closure is **not** a class — it is a **function object**. But it lives in the same
family.

### 6. `nonlocal` — writing into the cell

Until now the cell had only been **read**. Writing is a different problem.

**The broken counter:**

```python
def make_counter():
    count = 0
    def increment():
        count = count + 1
        return count
    return increment

c = make_counter()
print(c())
```
```
UnboundLocalError: cannot access local variable 'count' where it is not
associated with a value
```

**Mechanism — Python's rule:** *if a name is **assigned anywhere** in a function
body, that name is treated as that function's **LOCAL for the entire body**, from
the first line.* This decision is made **at `def` time**, while reading the code,
before anything runs.

So `count` inside `increment` is local. The enclosing cell is **invisible** —
LEGB's **E** step never runs, because **L** already reserved the name. Then
`count = count + 1` evaluates the right side first — but that `count` is the
local, which has no value bound yet. **Name reserved, value absent →
`UnboundLocalError`.**

**Three errors, three distinct causes — keep them separated:**

| Error | Cause | When |
|---|---|---|
| `TypeError` | required argument not supplied | call time, **before** the body runs |
| `NameError` | name does not exist anywhere in LEGB | while the body runs |
| `UnboundLocalError` | name IS local, but no value bound yet | while the body runs |

**The fix:**

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count = count + 1
        return count
    return increment

c = make_counter()
print(c())                                   # 1
print(c())                                   # 2
print(c.__closure__[0].cell_contents)        # 2
```

`nonlocal` tells Python: **"do not make this name local — use the enclosing cell,
and write into that cell."**

**Three routes, three behaviours:**

- **read only, no assignment** → reads the enclosing cell (plain LEGB, E step)
- **assignment without `nonlocal`** → the name becomes local → `UnboundLocalError`
- **`nonlocal`** → the cell itself is the target, for both reading and writing

Two further points:

- The third print showing `2` (not `0`) is the **proof that the cell was written
  into**, not just read.
- `count` **survived between calls** — the first call's frame died, but the cell
  persisted. **This is the real payoff: state that outlives the call.**
- `nonlocal` targets the **enclosing cell only**, never module-level global.
  Global has its own keyword, `global`.

### 7. Two counters vs an alias — the def-vs-call loop closed

```python
a = make_counter()
b = make_counter()
print(a()); print(a()); print(b())      # 1, 2, 1
```

Two calls → two frames → two `increment` objects → **two cells**. `a` wrote into
its own cell twice (now 2); `b`'s cell was never touched, still 0, so `b()`
returns 1.

```python
print(a.__closure__[0].cell_contents)   # 2
print(b.__closure__[0].cell_contents)   # 1
print(a is b)                           # False
```

With an alias instead:

```python
b = a            # no brackets
print(a()); print(b()); print(a())      # 1, 2, 3
```

One object, one cell, shared count.

**The third case completes the set:**

```python
b = a()
print(b)           # 1
print(type(b))     # <class 'int'>
print(b())         # TypeError: 'int' object is not callable
```

`increment` ends with `return count`, and `count` is a number — so `b` holds an
**int**, not a function.

**The full set:**

- `b = a` → **alias.** Same object, same cell. `b()` works, shared count.
- `b = make_counter()` → **new function object**, new cell. `b()` works, own count.
- `b = a()` → **whatever the call returned** (here an int). `b()` fails.

> **Handle: brackets give you the return value, not the function.**

---

## KEY MENTAL MODELS

- A closure is a function object that binds a free variable from where it was
  created into its own private **cell**, so the value survives after the enclosing
  frame has died.
- The bond lives on the **object**, which is why the dead frame doesn't matter.
- Every call to the factory re-runs `def` → new object → **new cell**. Cells are
  per-object, never shared.
- Closures add no power, only a **shape**: one argument from outside, the rest
  sealed inside. That shape is required when someone *else* calls your function.
- `key=` hands `sorted` a scale; `sorted` does the calling, one element at a time,
  and returns the original elements.
- Assignment anywhere in a body makes the name local for the whole body — decided
  at `def` time.
- `nonlocal` retargets the assignment at the enclosing cell.
- Brackets give you the return value; no brackets give you the object.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| free variable | A name a function uses that is not its own local | It is "free" relative to that function, not undefined |
| cell / `__closure__` | Tuple of cells on the function object; value in `cell.cell_contents` | Per-object — two closures from one factory never share |
| closure | Function object + private cell surviving a dead frame | Not stored in the module namespace, and not `__defaults__` |
| enclosing (the E of LEGB) | The function this one is **written inside** — lexical | Decided by where it is written, not where it is called from |
| per-call creation | New frame → `def` re-runs → new function object → new cell | One name in the source does not mean one object |
| `sorted(list)` | Returns a NEW list; original untouched | It's a function, not a method — `l.sort()` is the mutator |
| `key=` | Takes a function; `sorted` calls it once per element, one argument | You never call it yourself; output holds original elements, not key values |
| `nonlocal` | Makes assignment target the enclosing cell | Enclosing only — never module-level global |
| assignment makes a name local | Decided at `def` time, for the entire body | This is why the E step never runs in the broken counter |
| `UnboundLocalError` | Name IS local, but no value bound yet | Distinct from `NameError` — the name exists, the value doesn't |
| `b = a` / `b = make_counter()` / `b = a()` | Alias / new object / the returned value | Brackets give you the return value, not the function |

---

## WHAT'S COMING NEXT — SESSION 20

1. **Closure definition, cold** — the sentence above, unaided.
2. **Cell causation re-fire:** if the factory loop runs 5 times, how many cells,
   and why?
3. **Recursion** — deferred four times, highest priority. Base case, recursive
   case, call-stack picture. Schedule early.
4. **The 1.7 tail — 1.7 is NOT closed until all are taught:** `global` (vs
   `nonlocal`), `*args` / `**kwargs`, lambdas, docstrings, pure functions.
5. **`zip` and list comprehensions** — both used, neither taught.
6. Older carry-forwards still live: `traceback`, iterator causation,
   `__defaults__`, the spoken Feynman recall for all of 1.6, and the modulo
   identity in symbolic form.
