# Unit 1.5 — Operators and Expressions

Vocabulary, expression vs statement, arithmetic, comparison, logical and
short-circuit, identity, membership, bitwise, precedence and associativity,
augmented assignment.

---

## 1. Vocabulary

- **Operator** — a symbol that performs an action on values: `+ - * / // % **
  == is in`.
- **Operand** — the value an operator acts on; in `2 + 3` the operands are
  `2` and `3`.
- **Expression** — code that evaluates to a single **value**.
- **Statement** — a complete instruction that **does** something and
  evaluates to nothing.
- **Precedence** — the rank that decides which operator runs first between
  *different* operators.
- **Associativity** — the direction used when operators share the *same*
  rank.
- **Coercion** — Python silently converting one type to another where it is
  safe (1.3 §8).
- **Truncation** — cutting off the fraction toward zero (`int()`).
- **Floor** — the largest integer not greater than the value (`//`).

---

## 2. Expression vs statement

- An **EXPRESSION evaluates to a VALUE**: `n > 10`, `"high"`, `n + 1`,
  `len(x)`, a ternary, a comprehension, `a | b` on sets, `d.pop(k)`, a
  function call.
- A **STATEMENT DOES something and evaluates to nothing**: `x = 5`,
  `if n > 10:`, `for i in values:`, `while`, `return i`, `break`,
  `continue`, `pass`, `del d[k]`, `d[k] = v`, `import x`, `def`, `class`.

> **The test: can it go inside `print(...)`?** Values can; actions cannot.

```python
n = 12
print(if n > 10: "high")
print("this line exists")
```
```
  File "synt.py", line 2
    print(if n > 10: "high")
          ^^
SyntaxError: invalid syntax
```
Note what did **not** happen: `n = 12` never ran and line 3 never printed. Not
one line of the file executed — the `SyntaxError` tell (1.1 §2).

Consequences that recur across the course:

- A ternary fits inside `print()`; an `if`/`else` block does not (1.6).
- A comprehension fits inside `sum(...)` or an f-string; a `for` loop does not
  (1.8).
- `d.pop(k)` can be assigned from; `del d[k]` cannot (1.8).
- Set operations `|`, `&`, `-` build new sets, so they are expressions.

---

## 3. Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | add; on sequences, **concatenate** into a new object | `[1] + [2]` → `[1, 2]` |
| `-` | subtract; on sets, difference | |
| `*` | multiply; on sequences, **repeat** into a new object | `"ab" * 3` → `'ababab'` |
| `/` | true division — **always a float** | `10 / 2` → `5.0` |
| `//` | floor division — floors toward −∞ | `-7 // 2` → `-4` |
| `%` | modulo — remainder consistent with `//` | `-7 % 3` → `2` |
| `**` | exponentiation — **right-to-left** | `2 ** 3 ** 2` → `512` |

Operator behaviour belongs to the **type**: `+` on lists concatenates, on ints
adds, on NumPy arrays adds elementwise; `/` on a `pathlib.Path` joins paths
(1.11). The object decides what the operator does.

### 3.1 `/` vs `//` vs `int()`

```python
print(10 / 2, type(10 / 2))     # 5.0 <class 'float'>
print(10 // 2, type(10 // 2))   # 5 <class 'int'>
print(7 // 2)                   # 3
print(-7 // 2)                  # -4   floor: toward -infinity
print(int(-3.5))                # -3   truncate: toward zero
```

`//` and `int()` both throw the fraction away, in different directions. On
positives they agree, which is why the difference only shows on negatives.
Floor is not "the lowest number": it is **the largest integer not greater
than** the value — for `-3.5` that is `-4`.

### 3.2 `%` — the value, not just the sign

`%` is **not** school remainder. It is the leftover forced by the **floored**
quotient. The identity always holds:

```python
a == b * (a // b) + (a % b)
```

Worked, `-7 % 3`: `-7 / 3 = -2.33…` → floor → `-3`; `3 * (-3) + r = -7` →
`r = 2`. So `-7 % 3` is **2**, not 1.

Worked, `17 % -5`: `17 / -5 = -3.4` → floor → `-4`; `(-5) * (-4) + r = 17` →
`r = -3`.

```python
print(-7 // 2, -7 % 2)      # -4 1
print(-11 % 5)              # 4
print(11 % -5)              # -4
print(17 // -5, 17 % -5)    # -4 -3
print(-13 % 10)             # 7
print(17 == -5 * (17 // -5) + (17 % -5))    # True
```

Order matters: get the **floored quotient first**, then solve the identity for
`r`. Free check: **the sign of `a % b` always follows `b`** (the divisor).
That shortcut gives only the sign; for the value, run the identity.

### 3.3 `**` — the one common right-associative operator

```python
print(2 ** 3 ** 2)      # 512  = 2 ** (3 ** 2) = 2 ** 9   (NOT 64)
print(2 ** 2 ** 3)      # 256  = 2 ** (2 ** 3) = 2 ** 8
```

### 3.4 `*` on a sequence repeats the REFERENCE

```python
print([0] * 5)          # [0, 0, 0, 0, 0]
print(["home"] * 3)     # ['home', 'home', 'home']
print([1, 2] * 2)       # [1, 2, 1, 2]

grid = [[0] * 3] * 3
grid[0][0] = 99
print(grid)             # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]
print(grid[0] is grid[1])   # True — three slots, ONE inner list
```

`* n` is **safe when the element is immutable** (sharing a `0` is invisible)
and a **trap when it is mutable**. The fix is a comprehension,
`[[0] * 3 for _ in range(3)]`, because the expression re-runs once per pass
while `*` evaluates its operand once (1.8).

---

## 4. Comparison operators — always a boolean

Every comparison returns exactly `True` or `False`.

```python
5 == 5      # True     equal to
5 != 3      # True     not equal ("True" means they DIFFER)
5 > 3       # True
5 < 3       # False
7 >= 7      # True
4 <= 3      # False
```

The single most common bug in programming: **`=` acts (assigns), `==` asks
(compares).**

**Chained comparison:** `5 > 3 > 1` expands to `5 > 3 and 3 > 1` → `True`. In
`f() > 3 > 1` **the middle operand is evaluated exactly once** and reused, so
chaining is not merely sugar for the `and` rewrite. Short-circuit still
applies: if `f() > 3` is `False`, `3 > 1` never runs.

A float sails through a comparison: `0 <= 45.0 <= 90` is `True`, no error.
To **refuse** a float you must test the type yourself (`type(x) != int`);
`int(x)` **converts** `45.0` to `45` silently — the opposite of refusing.

---

## 5. Logical operators: `and`, `or`, `not`

`and` is demanding (both sides), `or` is generous (at least one), `not` flips
a single operand. In real code the sides are comparisons that resolve to
booleans first, then the logical operator combines them — a **two-stage
evaluation**:

```python
x = 5
x > 3 and x > 100       # step 1: True; step 2: False; step 3: True and False -> False
x > 3 or x > 100        # True
not x > 100             # not False -> True
```

### 5.1 Short-circuit evaluation

`and` / `or` **stop the moment the answer is settled**, and they return **the
operand that settled it** — not a manufactured `True`/`False`.

```python
0 and 5         # 0     — 0 is falsy: settled, return 0, never look at 5
3 and 5         # 5     — 3 truthy, must check on, return the LAST operand
0 or "hi"       # 'hi'  — 0 falsy, check on, "hi" truthy -> return it
"a" or "b"      # 'a'   — settled at "a"; "b" never evaluated
2 or 1 / 0      # 2     — settled at 2; 1/0 is NEVER evaluated -> no error
```

Rules:

- `and` returns the **first falsy** operand, or the **last** operand if none
  are falsy.
- `or` returns the **first truthy** operand, or the **last** if none are
  truthy.

You see a real `True`/`False` only when the operand is itself a bool (usually
from a comparison): `(4 > 2) and (1 > 9)` → `False`.

**Why "stops" matters — the guard idiom.** The right-hand side is *never
evaluated*, not evaluated-and-ignored:

```python
x = "90"
print(type(x) != int or x < 0)      # True   — x < 0 is never reached
print(x < 0)
# TypeError: '<' not supported between instances of 'str' and 'int'
```

Both facts are true at once: the comparison is dangerous in isolation and
unreachable behind the guard. `if x and x[0] > 5` never touches `x[0]` when
`x` is empty. Consequence: a `try`/`except TypeError` around a guarded
comparison is **dead code** — it can never run. The default idiom
`name = user_input or "guest"` is the same mechanism.

---

## 6. Identity operators: `is`, `is not`

`is` compares object identity (`id(a) == id(b)`); `==` compares value. Use
`is` only for `None` and other singletons. Full treatment in 1.2 §11.

```python
a = [1, 2]
b = [1, 2]
print(a == b, a is b)       # True False
```

---

## 7. Membership: `in`, `not in`

Answers "is this value present in that container?" — always a bool. **What it
checks depends on the container:**

```python
3 in [1, 2, 3]              # True   list / tuple / set -> elements
"ell" in "hello"            # True   str -> SUBSTRING
"apple" in {"apple": 50}    # True   dict -> KEYS
50 in {"apple": 50}         # False  50 is a VALUE, not a key
50 in {"apple": 50}.values()    # True
```

---

## 8. Bitwise operators (awareness only)

`&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` / `>>` (shift) operate on the
**binary bits** of integers: `5 & 3` → `1`, `5 | 3` → `7`. **Do not confuse
`&` (bitwise) with `and` (logical).** On sets the same symbols mean
intersection, union and symmetric difference — `&` works on any type that
defines it (1.8).

---

## 9. Precedence and associativity

Order is decided by **rank, not position**. Brackets highest; then `**`; then
`*` `/` `//` `%`; then `+` `-`; then comparisons; then `not`, `and`, `or`.

```python
2 + 3 * 4           # 14   — * outranks +      (NOT 20)
(2 + 3) * 4         # 20   — brackets first
2 + 3 * 4 ** 2      # 50   — 2 + (3 * (4 ** 2))
```

When ranks tie, **associativity** decides the direction: everything runs
left→right **except `**`**, which runs right→left.

```python
8 - 3 - 2           # 3    = (8 - 3) - 2   left to right
10 - 3 - 2          # 5
2 ** 3 ** 2         # 512  = 2 ** (3 ** 2)  right to left
```

- **Precedence** = rank between **different** operators (who goes first).
- **Associativity** = direction within the **same** rank (which operand
  groups with which side).

Not the same thing as evaluation order of an assignment: in `x = x + 1` the
right-hand side is evaluated first, then the name is bound — that is the
statement's **evaluation order**, not associativity.

---

## 10. Augmented assignment: `+=`, `-=`, `*=`, …

`x += y` behaves **by mutability**:

- On a **mutable** object it **mutates in place** — same object, same `id`,
  every alias sees it (on a list it is `.extend()`).
- On an **immutable** object it **rebinds** to a new object; the original and
  any alias are untouched.

```python
a = [1, 2]
b = a
print(id(a) == id(b))       # True
a += [3]
print(b, id(a) == id(b))    # [1, 2, 3] True    — in place; b sees it
a = a + [4]
print(b, id(a) == id(b))    # [1, 2, 3] False   — a + [4] built a NEW list; a rebound
```

```python
x = 5
y = x
x += 1
print(x, y, x is y)         # 6 5 False   — immutable: had no choice but to rebind
```

`x = x + y` **always** builds a new object and rebinds. Discriminator: look at
the **type** first, the same rule as for methods (1.4 §5).

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| expression | evaluates to a value | test: can it go inside `print(...)`? |
| statement | does something, yields nothing | `d[k] = v`, `del d[k]` cannot be caught in a variable |
| `/` | true division | always a float, even `10 / 2` |
| `//` | floor division, toward −∞ | `-7 // 2` is `-4`, not `-3` |
| `int()` | truncation, toward zero | disagrees with `//` only on negatives |
| `%` | remainder consistent with `//`: `a == b*(a//b) + a%b` | `-7 % 3` is `2`; sign follows the **divisor** |
| `**` | exponentiation | the only common right-associative operator: `2**3**2` is 512 |
| `+` on sequences | concatenates into a **new** object | originals untouched |
| `*` on sequences | repeats the **reference** | `[[0]*3]*3` shares one row |
| `==` vs `=` | asks vs assigns | writing `=` for `==` is the classic silent bug |
| `!=` | true when the values differ | read it slowly |
| chained comparison | `a > b > c` → `a > b and b > c` | the middle operand is evaluated **once** |
| `and` / `or` | return an **operand**, stop when settled | `2 or 1/0` → `2`; bools only when the operands are bools |
| short-circuit guard | `A or B` never evaluates `B` if `A` is truthy | a `try` around the guarded part is dead code |
| `not` | flips one operand | |
| `is` / `is not` | identity | not for values; for `None` |
| `in` / `not in` | membership | dict → **keys**; str → **substring** |
| bitwise `& \| ^ ~ << >>` | operate on bits | `&` is not `and` |
| precedence | rank between different operators | order is by rank, not position |
| associativity | direction within the same rank | all left→right except `**` |
| `+=` | in place on mutables; rebind on immutables | `x = x + y` always rebinds |
| refuse vs convert | `type(x) != int` refuses; `int(x)` converts | a float passes `0 <= x <= 90` silently |
