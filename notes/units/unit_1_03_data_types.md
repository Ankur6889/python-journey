# Unit 1.3 — Data Types: the Five Primitives

`int`, `float`, `bool`, `str`, `None`; `type()` vs `isinstance()`; the four
conversion functions; implicit vs explicit conversion; the small numeric
builtins.

---

## 1. `int` — arbitrary precision

No size ceiling. Python allocates memory as needed, so huge integer literals
are exact.

```python
print(2 ** 200)
# 1606938044258990275541962092341162602522202993782792835301376
```
The cost is memory and time on very big values, never overflow.

---

## 2. `float` — 64-bit IEEE 754, approximate

A fixed bit budget means only a finite set of values is representable; most
decimals are stored as the **nearest approximation**, and operations
**compound** the error.

```python
print(0.1 + 0.2 == 0.3)             # False
print(0.1 + 0.1 + 0.1 == 0.3)       # False
print(0.1 + 0.2)                    # 0.30000000000000004
```

The error is **real, not cosmetic** — `0.1 + 0.2` is genuinely a different
number from `0.3`, not a display artefact.

> **Never use `==` for float equality.** Compare with a tolerance:
> `abs(a - b) < 1e-9`. Choosing the tolerance is your problem, not Python's.

`float("nan")` and `float("inf")` are valid and break comparisons
(`nan != nan`). The binary mechanism (why `0.1` is `0.0001100110011…`) is
1.13.

---

## 3. `bool` — a subclass of `int`

```python
print(True == 1)                # True   — value equality
print(True is 1)                # False  — different objects, different types
print(False + False + True)     # 1      — bools work in arithmetic
print(True + 1, type(True + 1)) # 2 <class 'int'>  — the type is int, not bool
```

**`bool` is a subclass of `int`**, not the other way round; `True` is 1 and
`False` is 0. Write logic with bools, not with arithmetic.

**Truthiness.** `if` coerces its condition to a `bool`. The rule:
**emptiness is falsy, zero is falsy, everything else is truthy.**

Falsy values: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()`.
Everything else is truthy — including `"False"`, `"0"`, `" "`, `[0]`,
`[None]`.

---

## 4. `str` — immutable; every method returns a new object

A string is a fixed run of characters. Python will never edit one in place;
every operation that looks like editing builds a **new** string and hands it
back. There is no door into an existing `str` (no item assignment, no
attribute namespace to write into), so the only way to get different text is a
different object with a different `id`.

```python
s = "  Kinova Gen3  "
print(repr(s), id(s))                   # '  Kinova Gen3  ' 140565061446896

t = s.strip()
print(repr(t), id(t))                   # 'Kinova Gen3' 140565061451440
print(repr(s), id(s))                   # '  Kinova Gen3  ' 140565061446896  (unchanged)

print(repr(s.upper()))                  # '  KINOVA GEN3  '
print("3,4,5".split(","))               # ['3', '4', '5']
print("-".join(["3", "4", "5"]))        # 3-4-5
print(repr(s.replace("Gen3", "Gen7")))  # '  Kinova Gen7  '
print(repr(s))                          # '  Kinova Gen3  '  (still unchanged)

s[0] = "X"
# TypeError: 'str' object does not support item assignment
```

- `repr()` shows the quotes, which is the only way to *see* leading/trailing
  whitespace that `print` hides.
- **The most common string bug:** calling a method and discarding its return
  value. `name.strip()` on its own line does nothing to `name`; the fix is
  always `name = name.strip()`.
- `join` has an odd shape: the **separator** is the string you call it on;
  the list is the argument.
- Methods to have: `.strip()`, `.upper()`, `.lower()`, `.replace(old, new)`,
  `.split(sep)`, `sep.join(list)`, `.startswith(prefix)`, `.find(sub)`. All
  return new objects; none change the original. Because `str` is immutable,
  **no `str` method can mutate** — that is why none of this needs memorising.
- `"ab" * 3` → `'ababab'`; `+` concatenates into a new string; indexing and
  slicing work exactly as on lists (1.8): `"clamp"[:-1]` → `'clam'`,
  `"clamp"[::-1]` → `'pmalc'`.
- `in` on a string tests **substring**: `"ell" in "hello"` → `True`.

Nested-quote note for f-strings: from Python 3.12 (PEP 701) the same quote
character may appear inside an f-string's braces; on 3.11 and earlier it is a
`SyntaxError`.

---

## 5. `None` — "no value present"

`None` means **no value** — not empty, not zero, not false. It is the single
object of its own type, `NoneType`, and exactly one exists in the program.

```python
def f():
    pass                        # no return

x = f()
print(x, type(x))               # None <class 'NoneType'>

a = None
b = None
print(a is b)                   # True  — one object program-wide

print(None == False)            # False
print(None == 0)                # False
```

- `None`, `False` and `0` are three different objects of three different
  types. All three are falsy; none is `==` to another.
- `0` is an `int` that *has* a value; `None` is a `NoneType` that means *there
  is no value*. A different kind of thing, not a different number.
- **A function with no `return` returns `None`** (1.7).
- Test for it with `is None`, never `== None` (1.2 §11). And never with
  `if not x:` when `0` is a legal value — that confuses `0` with `None`.
- `None` is an **object**: `len([None])` is 1, `len([])` is 0. `[None]`
  contains something; `[]` contains nothing.
- **`None` as absence** (sentinel): when every real value of a return type is
  a legal answer, `None` is the one value that cannot be mistaken for data —
  "not found" vs "found at index 0". The sentinel must be something the data
  can never contain.

---

## 6. `type()` vs `isinstance()`

```python
x = True
print(type(x) == int)           # False — exact type check; bool is not int
print(isinstance(x, int))       # True  — honours inheritance; bool is a subclass of int
print(type(x))                  # <class 'bool'>
```

- `isinstance(x, T)` **respects inheritance** — permissive.
- `type(x) == T` is an **exact** check — strict; rejects subclasses.

Neither is "the right one". Choose by intent: to reject bools where you want a
strict `int`, use the exact check.

**"Type belongs to the object, not the name"** means `type(x)` reports the
type of whatever object `x` is bound to right now; the name itself has no
type.

---

## 7. Type conversion: `int()`, `str()`, `float()`, `bool()`

The most important property: **a conversion function returns a NEW object of
the new type. It does not modify the original.**

```python
x = "42"
y = int(x)
print(x, type(x))       # 42 <class 'str'>   — x untouched
print(y, type(y))       # 42 <class 'int'>
```
If you do not capture the return value, the conversion is thrown away — the
same trap as `.strip()`.

### 7.1 Strict when parsing a string, lenient when converting a number

```python
print(int(3.9))         # 3    — numeric conversion: lenient, truncates toward zero
print(int(-3.9))        # -3   — toward ZERO, not "round down"
print(int("3.5"))
# ValueError: invalid literal for int() with base 10: '3.5'
```

- `int(3.9)` receives a **float** — already a number, with exactly one
  defensible integer conversion: drop the fraction, **truncating toward
  zero**.
- `int("3.5")` receives a **string** that must be **parsed**, and `"3.5"` is
  not a valid integer literal. Python will not guess whether you meant `3` or
  `4`; it raises. It is not attempting a two-stage conversion and failing
  halfway — string parsing simply refuses a decimal outright. Whitespace is
  tolerated (`int(" 42 ")` → 42); a decimal point is not.
- `float("3.5")` works; `float` parses decimals.
- `str(x)` almost never raises. `str(3) + str(4)` is `"34"` — concatenation.

### 7.2 `bool()` never reads the contents of a string

```python
print(bool(""))         # False — empty
print(bool("False"))    # True  — non-empty; the characters are never read
print(bool("0"))        # True
print(bool(" "))        # True  — a space is a character
print(bool(0))          # False
print(bool([]))         # False
print(bool([0]))        # True  — one item
```

`bool()` asks one question only: is this thing empty (or zero)? `bool("")` is
`False` because the string has length zero — not because it "is `None`". An
empty string is a real `str` object with an `id`.

### 7.3 Truncation vs floor: `int()` vs `//`

```python
print(int(-5.98))       # -5   int() truncates toward zero
print(-5.98 // 1)       # -6.0 // floors toward -infinity
print(-7 // 2)          # -4
print(int(-7 / 2))      # -3
print(7 // 2)           # 3    positives: both agree, so they prove nothing
```

Two different rounding behaviours in the same language; they separate only
on negatives. Full treatment of `//` and `%` in 1.5.

---

## 8. Implicit vs explicit conversion

- **Explicit** — you call one of the four functions. You asked for it; if it
  cannot be done, it raises.
- **Implicit (coercion)** — Python converts silently, and **only where there
  is one obvious, safe, lossless direction**. *Coerce* = force.

```python
print(1 + 2.0, type(1 + 2.0))       # 3.0 <class 'float'>  — int widened to float
print(True + 1)                     # 2                    — bool is an int
print("5" + 3)
# TypeError: can only concatenate str (not "int") to str
```

`"5" + 3` has no safe direction: `"53"` and `8` are both defensible and give
completely different answers, so **Python refuses to guess**. JavaScript picks
one (`"53"`), which is why it has a reputation for silent type surprises.
Interview sentence: **Python coerces only where the direction is unambiguous
and lossless; otherwise it raises rather than choosing for you.**

`print(5)` works while `"5" + 3` does not because **`print` calls `str()` on
each argument; `+` refuses** (1.6 §12).

---

## 9. `ValueError` vs `TypeError` — decode the name

**The exception is named after the part that broke.**

- `int("2.5")` — the **type** is fine (`int()` accepts strings); the value
  `'2.5'` cannot be parsed → **`ValueError`**: right type, wrong value.
- `"5" + 3` — there is no `+` between these two types → **`TypeError`**: the
  operation does not exist for this combination of types.

The test: *change only the value and it works ⇒ `ValueError`; change only the
type and it works ⇒ `TypeError`.* Full error treatment in 1.9.

---

## 10. Division returns a float

```python
print(10 / 2, type(10 / 2))     # 5.0 <class 'float'>  — / ALWAYS returns a float
print(10 // 2, type(10 // 2))   # 5 <class 'int'>      — // floor division
```

---

## 11. Small numeric builtins

```python
print(abs(-7.5))            # 7.5   distance from zero, sign discarded
print(min(3, 9), max(3, 9)) # 3 9   smaller / larger argument
print(max(0, min(150, 100)))# 100   clamp 150 into [0, 100]
print(sum([1, 2, 3]))       # 6     total of an iterable of numbers; returns a new value
print(sum([]))              # 0     empty is not an error
print(len("abc"))           # 3     item count of a container / string
```

`sum`, `min`, `max`, `len` take an iterable or arguments and **build a new
value**; none of them mutates.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| `int` | arbitrary-precision integer | no overflow; big ints cost memory/time |
| `float` | 64-bit IEEE 754 | `==` on floats is a bug; use a tolerance |
| `bool` | subclass of `int`; `True` is 1 | `True == 1` yet `True is not 1`; `True + 1` is an `int` |
| truthiness | empty/zero falsy, else truthy | `"False"`, `"0"`, `" "`, `[0]` are all truthy |
| `str` | immutable sequence of characters | every method returns a new object; discarding it is the classic bug |
| `repr(x)` | unambiguous printable form | use it to see whitespace and quotes |
| `None` | the sole `NoneType` object; "no value" | not `==` to `0` or `False`; test with `is None`; `[None]` has length 1 |
| `type(x)` | exact runtime type | rejects subclasses (`bool` for `int`) |
| `isinstance(x, T)` | type check honouring inheritance | accepts `bool` where you may want strict `int` |
| `int(number)` | truncates toward zero | `int(-3.9)` is `-3`; not floor |
| `int(string)` | strict integer parse | `int("3.5")` → `ValueError`; whitespace ok, decimal not |
| `float(x)` | to float; parses decimals | `float("nan")` breaks comparisons |
| `str(x)` | string representation | almost never raises; `+` on the result concatenates |
| `bool(x)` | emptiness test | never reads string content |
| all four | return a **new** object | the original is untouched |
| coercion | silent, lossless widening only (`1 + 2.0`) | `"5" + 3` is refused with `TypeError` |
| `/` vs `//` | true division (float) vs floor division | `10 / 2` is `5.0`; `-7 // 2` is `-4` |
| `ValueError` / `TypeError` | value wrong / operation undefined for the types | named after the part that broke |
| `abs`, `min`, `max`, `sum`, `len` | numeric / size builtins, all non-mutating | `sum([])` is `0` |
