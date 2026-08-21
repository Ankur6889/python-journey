# SESSION 14 NOTES — Saturday 8 August 2026

**Topics: shallow vs deep copy proved with `id()` · the 1.3 and 1.4 models in
compressed form · control flow opened (1.6) · truthy/falsy · the `if` block, and
why a block creates no scope**

Loops deliberately deferred to Session 15.

---

## SELF-TEST — answer these cold before reading on

1. A shallow copy of `[[1,2,3], ['a','b']]`: which ids match the original and
   which don't? Append to the nested list through the shallow copy — who sees it?
2. Say what a variable is, without using the word "box".
3. For an immutable, what does `x = x + 1` actually do — to the object, and to the
   name?
4. What is control flow, in one sentence? What bends the default flow?
5. State the truthy/falsy rule in one line.
6. Does a name assigned inside an `if` block survive after the block? Why or why
   not?
7. `result = q.append(4)` — what is `result`, and what is `q`?

---

## FULL TEACHING

### 1. Shallow vs deep copy — the `id()` proof

A **shallow** copy makes a new **outer** container but fills it with the **same
inner references** (aliases). A **deep** copy rebuilds everything recursively.

```python
import copy
original = [[1, 2, 3], ['a', 'b']]
shallow = copy.copy(original)
deep    = copy.deepcopy(original)

# inner ids: original[0] == shallow[0]   (shared alias)
#            deep[0]     != original[0]  (new object)

shallow[0].append(99)
# original -> [[1,2,3,99], ['a','b']]    99 shows
# shallow  -> [[1,2,3,99], ['a','b']]    99 shows
# deep     -> [[1,2,3],    ['a','b']]    untouched
```

The mechanism, stated exactly: **the append followed the shared reference.** The
new outer wrapper is irrelevant to the inner object's fate.

### 2. The 1.3 model, compressed

A variable is **not a box**. Python builds the **object first**, then binds a name
to it like a tag; the name→object mapping lives in a dictionary-like
**namespace**. That is why one object can carry two names — an **alias**.

### 3. The 1.4 model, compressed

**Mutable** = the object itself can change (`list`, `dict`). **Immutable** = it
cannot (`int`, `float`, `str`, `tuple`).

For immutables, `x = x + 1` *cannot* change the old object, so a new object is
made and the name is rebound to it.

> **Immutable → the name moves. Mutable → the object changes and the name stays.**

### 4. Control flow (1.6, opened)

**Control flow** = steering which line runs next. The default flow is
top-to-bottom; control flow bends it — to **choose** or to **repeat**.

A **conditional** gates a block on a condition: true → run it, false → skip it.
The condition is **coerced to a bool**.

**Truthy / falsy** — non-bool values treated as `True`/`False` by `if`:

> **Emptiness is falsy, zero is falsy, everything else is truthy.**

### 5. The `if` block — the syntax mechanism

The **colon opens** a block; **indentation delimits** it; **dedent ends** it.
That is Python's replacement for braces.

**A block creates no new frame and no new namespace — only a function call does.**
So a name assigned inside an `if` survives after the block:

```python
if True:
    y = 10
print(y)       # 10   — same frame, block makes no scope

def f():
    z = 10
f()
print(z)       # NameError — z died with f's frame
```

The discriminator to hold for this: **"Did I call a function? No? Then no new
frame, same namespace."**

### 6. Mutate vs build, restated

```python
result = q.append(4)
# q      -> [1, 2, 3, 4]   (mutated in place)
# result -> None           (append builds nothing)
```

The test: does the call **MUTATE** (→ `None`, don't assign) or **BUILD** (→ new
object, do assign)?

**Don't memorise method lists.** Hold the model and look the specific method up.
Strings are immutable, so every string method builds.

### 7. `ValueError` vs `TypeError` — the decode hook

Named after **the part that broke**:

- **`ValueError`** — the value can't be parsed; the type is fine.
- **`TypeError`** — the operation is undefined between these types.

---

## KEY MENTAL MODELS

- Shallow copies share their inner objects; mutation through one is visible
  through the other. `id()` settles it.
- Objects come first, names are tags attached afterwards.
- Immutable → the name moves; mutable → the object changes and the name stays.
- Emptiness is falsy, zero is falsy, everything else is truthy.
- Colon opens a block, indentation delimits it, dedent ends it — and a block makes
  no scope. Only a call does.
- Mutate → `None`, don't assign. Build → new object, do assign.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Item | What it does | The trap |
|---|---|---|
| shallow copy | New outer box, same inner refs (aliases) | Mutating a nested object shows in the original too |
| deep copy | Rebuilds everything recursively | Slower, but fully independent |
| `id()` match | Same object (alias) | An `id` mismatch means a genuinely new object |
| truthy / falsy | Non-bool value read as `True`/`False` by `if` | Empty/zero = falsy; everything else truthy |
| `if` block | Colon opens, indent delimits, dedent ends | A block makes NO scope — only a call does |
| mutating method | Changes the object in place, returns `None` | Never assign its result (`result = lst.append(x)` is `None`) |
| building method | Returns a NEW object (e.g. `str.upper`) | You MUST assign its result to keep it |
| rebinding | `=` points a name at a (possibly new) object | The old object is unchanged; this is not mutation |

---

## WHAT'S COMING NEXT — SESSION 15

- **Term-tax:** `ValueError`/`TypeError`, coercion, the new 1.6 terms,
  short-circuit and the modulo identity.
- **Promotion pass:** one confirming cold re-test each for `+=`, aliasing,
  conversion-returns-new, `"5"+3` `TypeError`, `result = q.append(4)`, shallow vs
  deep with `id()`, and the S13 operator drills.
- **Continue 1.6 — loops, defined first:** the iteration protocol, then `range()`
  (defined before use), then `while`; then re-pose the block-scope rule with a
  loop as the fair re-test. Formalise `print()`.
- Housekeeping: re-test negative `%` cold, and `__defaults__` — where the default
  lives — in isolation.
