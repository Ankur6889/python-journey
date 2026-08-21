# SESSION 2 NOTES — Rebinding, Identity vs Equality

**Topics: the rebinding rule · `is` vs `==` · integer caching (−5 to 256) ·
`+` on lists · `.append()` (teaser)**

---

## SELF-TEST — answer these cold before reading on

1. State the rebinding rule in one sentence, including what it does to *other*
   names bound to the same object.
2. What question does `==` ask? What question does `is` ask? Which one calls
   `__eq__`?
3. `p = 100; q = 100` → is `p is q` True? Now with `1000`? Explain both.
4. `m = [1,2,3]; n = m; n = n + [4]` — what is `m`? What is `m is n`?
5. Same setup but `n.append(4)` — what is `m` now, and why is the answer different?

---

## FULL TEACHING

### 1. The rebinding rule

> Assignment rebinds the name on the left. It does nothing to any other name —
> even one currently bound to the same object. Aliases do not propagate updates,
> because there is no update. There is only a new binding on one key in the
> namespace dictionary.

```python
x = 42       # namespace: {'x': <obj 42>}
y = x        # namespace: {'x': <obj 42>, 'y': <obj 42>}   same object
x = x + 1    # namespace: {'x': <obj 43>, 'y': <obj 42>}   x rebound, y untouched
```

After all three lines two integer objects exist, `42` and `43`. Object `42` is
not collected — `y` still holds a reference, so the refcount never hit zero.

### 2. Identity vs equality — `is` vs `==`

The most common Python mistake. Burn it in now.

| Operator | Question it asks | Implementation |
|---|---|---|
| `==` | Do these two objects have equal **values**? | Calls `__eq__` |
| `is` | Are these two names bound to the **exact same object**? | Compares `id()` |

Two different objects can be `==` without being `is`. Mnemonic: **`==` checks
value, `is` checks identity.** `is` is essentially `id(left) == id(right)`.

**Never use `is` to compare values.** Use `==` for values; use `is` only when you
genuinely mean "same object" — most commonly `x is None`, because `None` is a
singleton and only one ever exists.

### 3. Integer caching: −5 to 256

This explains the counter-intuitive result that two separate `= 100` statements
end up on the same object:

```python
p = 100
q = 100
p is q            # True   — both bound to the same cached object
id(p) == id(q)    # True

p = 1000
q = 1000
p is q            # False  — equal value, DIFFERENT objects
p == q            # True   — values are equal
```

Why: CPython pre-creates integer objects for **−5 through 256** at interpreter
startup and reuses them. Loop counters, indices and small arithmetic use those
values constantly, so caching avoids an allocation every time. Outside that
range Python takes the cheap path and just makes a new object — there is no
global "does an int of this value already exist?" lookup, because that would be
catastrophically slow.

> Conceptual lesson: value equality and object identity are fundamentally
> different questions. Most languages let you blur the line because they hide the
> object model. Python doesn't. Once mutable objects enter the picture in 1.4,
> this distinction becomes the difference between code that works and code with
> subtle, terrifying bugs.

### 4. Lists: `+` produces a new object

Same model as integers, different operator — the rebinding rule did not change.

```python
m = [1, 2, 3]
n = m               # m and n bound to the SAME list
n = n + [4]         # right side builds a NEW list [1,2,3,4],
                    # then n is rebound to it; m is untouched

print(m)            # [1, 2, 3]
print(n)            # [1, 2, 3, 4]
m is n              # False
```

`+` on lists means **concatenation**: build a new list holding both sides'
elements in order. Neither original is modified. Contrast
`np.array([1,2,3]) + np.array([4,5,6])` → `[5,7,9]` — different rules for
different types, which arrives in Layer 4.

### 5. `.append()` mutates in place (teaser — full treatment in 1.4)

```python
m = [1, 2, 3]
n = m
n.append(4)         # mutates the list object — does NOT rebind
print(m)            # [1, 2, 3, 4]   — m sees the change too
print(n)            # [1, 2, 3, 4]
m is n              # True — still the same object
```

`.append()` does not assign. It mutates the object both names share. There is
still only one list; it just grew. This is the classic beginner bug source.

---

## KEY MENTAL MODELS

- Rebinding touches one key in the namespace dict. Nothing else moves.
- `==` is a value question, `is` is an identity question. They are not
  interchangeable, and `is` on values is a bug waiting for a number above 256.
- Caching is an implementation optimisation, not a language rule — never write
  code that depends on it.
- Operator behaviour belongs to the type. `+` on lists concatenates into a new
  object; `+` on NumPy arrays adds elementwise.
- Mutation and rebinding are different verbs. One changes the object, the other
  changes the name.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `==` | Value comparison via `__eq__` | Says nothing about identity |
| `is` | Identity comparison via `id()` | True for small ints by accident; use only for `None`-style singletons |
| int cache −5…256 | CPython reuses these objects | `is` "works" inside the range and fails outside it |
| `list + list` | Builds a new concatenated list | Original lists untouched; the name is rebound |
| `list.append(x)` | Mutates the list in place | Every alias sees the change; returns `None` |

---

## WHAT'S COMING NEXT — SESSION 3

- 1.1 How Python runs code — the interpreter, CPython vs PyPy/Jython/MicroPython,
  compilation to bytecode (`.pyc`), the PVM, the call stack.
- 1.3 Data types — `int`, `float`, `bool`, `str`, `None`, with depth on `bool` as
  a subclass of `int`, and why `0.1 + 0.2 != 0.3`.
- 1.4 Mutability vs immutability — the formal `.append()` vs `+` drill, plus
  tuples and frozensets.
