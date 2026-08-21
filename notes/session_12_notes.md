# SESSION 12 NOTES — Monday 3 August 2026

**Topics: the vocabulary of expressions · floor division vs truncation on
negatives · comparison operators · logical operators · precedence and
associativity · augmented assignment · `ValueError` vs `TypeError`, decoded ·
the Term Retention System**

Opens 1.5 (Operators and Expressions), roughly 60% covered.

---

## SELF-TEST — answer these cold before reading on

Close everything. Retrieve cold. Say "gap" where empty, then check.

1. What does `-7 // 2` evaluate to, and why? How does that differ from
   `int(-3.5)`?
2. For a list `x = [1,2,3]`, does `x += [4]` mutate the existing object or rebind
   `x` to a new one? What about `x = 5; x += 1`?
3. If `y = x` and then `x += [4]` runs on a list, what is `y` afterwards? Why?
4. Evaluate `2 + 3 * 4` and `(2 + 3) * 4`. State the rule that decides the order.
5. Evaluate `8 - 3 - 2`. Which direction does it run, and what is that property
   called?
6. What are the only two values any comparison operator can return?
7. Walk `x = 5; x > 3 and x > 100` in three steps. Final answer?
8. Which exception does `int("2.5")` raise, which does `"5" + 3` raise, and what
   one-line rule separates the two?
9. Define, from the word itself: coercion, truncation, precedence, associativity.

Answers at the back.

---

## FULL TEACHING

### 1. Vocabulary first (define before building)

- **Operator** — a symbol that performs an action on values (`+ - * // ==`).
- **Operand** — the value an operator acts on; in `2 + 3` the operands are `2`
  and `3`.
- **Expression** — code that evaluates to a single value (`2 + 3 * 4` → `14`).
- **Statement** — a complete instruction that performs an action but does not
  itself reduce to a value (`x = 5`).
- **Precedence** — the rank that decides which operator runs first.
- **Associativity** — the direction used when operators share the same rank.
- **Coercion** — Python silently converting one type to another where it is safe
  (`1 + 2.0` → `3.0`).

### 2. Floor division vs truncation — the negative-number split

`//` **floors**: it pushes the result toward −∞ (left on the number line).
`int()` **truncates**: it drops the decimal, toward zero.

On positives both give the same answer, which is exactly why the difference stays
hidden — **the negative case is the only place the two rules separate.**

```python
-7 / 2      # -> -3.5
-7 // 2     # -> -4     floor: the whole number BELOW -3.5 is -4
int(-3.5)   # -> -3     truncate: drop the .5, toward zero

7 // 2      # ->  3     positive case: floor and truncate AGREE, so it proves nothing
```

### 3. Comparison operators — always a boolean

Every comparison returns exactly one of two values: `True` or `False`.

```python
==    equal to            5 == 5     -> True
!=    not equal to        5 != 3     -> True
>     greater than        5 > 3      -> True
<     less than           5 < 3      -> False
>=    greater or equal    7 >= 7     -> True
<=    less or equal       4 <= 3     -> False
```

The single most common bug in all of programming lives here:

```python
=     assignment     x = 5      (acts)
==    comparison     x == 5     (asks)
```

`=` **assigns** — it does something. `==` **asks** — it compares.

### 4. Logical operators — combining booleans

`and` is demanding (both sides must be True). `or` is generous (at least one).
`not` takes a single operand and flips it.

In real code the sides are comparisons that resolve to booleans first, and *then*
the logical operator combines them — a **two-stage evaluation**:

```python
x = 5
x > 3 and x > 100
#  Step 1: x > 3    ->  5 > 3     -> True
#  Step 2: x > 100  ->  5 > 100   -> False
#  Step 3: True and False         -> False

x > 3 or x > 100      # -> True       same inputs, operator changed, result flipped
not x > 100           # -> not False  -> True
```

### 5. Precedence and associativity

Order is decided by **rank, not position**. Brackets are highest, then `*` `/`,
then `+` `-`. When ranks tie, **associativity** decides direction: almost
everything runs left→right. The one exception is `**` (power), which runs
right→left.

```python
2 + 3 * 4       # -> 3*4 first (higher rank) -> 2 + 12 -> 14   (NOT 20)
(2 + 3) * 4     # -> brackets first -> 5 * 4 -> 20
8 - 3 - 2       # -> ties -> left to right -> (8-3)-2 -> 3
2 ** 3 ** 2     # -> ** is right to left -> 2 ** (3**2) -> 2 ** 9 -> 512
```

### 6. Augmented assignment — the test of whether 1.4 landed

`+=` behaves differently **by mutability**:

- On a **mutable** object (list) it **mutates in place** — same object, same
  `id`, now longer — so every alias sees the change.
- On an **immutable** object (int, str, tuple) it **rebinds** to a brand-new
  object and leaves the original untouched.

Same operator, opposite behaviour. **The object's mutability decides everything.**

```python
# MUTABLE (list): += mutates in place
x = [1, 2, 3]
y = x                      # y is an ALIAS: same object, not a copy
print(id(x), id(y))        # -> 140616595000128 140616595000128 (same)
x += [4]
print(x, y)                # -> [1,2,3,4] [1,2,3,4]   y sees it too
print(id(x))               # -> 140616595000128       id UNCHANGED

# IMMUTABLE (int): += rebinds to a NEW object
a = 5
b = a
print(id(a), id(b))        # -> 11755816 11755816     (same)
a += 1
print(a, b)                # -> 6 5                   b unaffected
print(id(a))               # -> 11755848              id CHANGED (new object)
```

**The `id` is ground truth:** unchanged → the object was mutated in place;
changed → the name was rebound to a new object.

### 7. `ValueError` vs `TypeError` — decode the name

**The exception is named after the part that broke.**

- `int("2.5")` — the **type** is fine (`int()` accepts strings), but the value
  `'2.5'` cannot be parsed as a whole number → **`ValueError`**.
- `"5" + 3` — there is no valid `+` between these two types, so the operation does
  not exist → **`TypeError`**.

You never memorise the pairing. You ask **"is the value wrong or the type
wrong?"** and the name follows.

### 8. The Term Retention System

The diagnosis: mechanisms stick, but the arbitrary labels stuck on top of them
drop off. The fix is not more flashcards — it is to stop storing labels flat.
Three binding parts:

1. **Name-decoding first.** Re-derive a term from the word itself rather than
   memorising it. *coerce* = force; *truncate* = cut off; `ValueError`/`TypeError`
   name the part that broke. Genuinely arbitrary terms get flagged for the spaced
   queue instead of pretend-decoded.
2. **Term-tax at session open.** A ~60-second cold vocabulary volley every
   session; define each term from memory, "gap" where empty. Terms recur at
   widening intervals until automatic.
3. **No naked terms.** A term is never stated without its one-line mechanism, and
   a definition handed back as only the reworded label is not accepted — give the
   machine underneath.

Honest caveat: a term re-derived seconds after it was taught is not proof it
stuck. The real test is the cold term-tax after a day's gap.

---

## KEY MENTAL MODELS

- `//` floors toward −∞; `int()` truncates toward zero. They agree on positives,
  which is why positives prove nothing.
- Comparisons only ever produce `True` or `False`.
- `=` acts, `==` asks.
- Logical operators evaluate their sides to booleans first, then combine.
- Precedence is rank; associativity is direction when ranks tie.
- `+=` mutates a list and rebinds an int/str/tuple — mutability decides, not the
  operator.
- `id()` is the ground truth for mutate-vs-rebind.
- Exception names point at the broken part: value or type.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `//` (floor division) | Divides, then floors toward −∞ | On negatives it differs from `int()`: `-7//2 = -4`, not `-3` |
| `int()` (truncation) | Builds a new int, dropping the decimal toward zero | It truncates, it does NOT floor: `int(-3.5) = -3` |
| `==` vs `=` | `==` asks if equal (returns a bool); `=` assigns | Writing `=` where you meant `==` is the classic silent bug |
| `!=` | True when the two values differ | "True" here means "they differ" — read it slowly |
| `and` / `or` / `not` | `and`: both true. `or`: at least one. `not`: flips one operand | Sides evaluate to booleans FIRST, then combine (two stages) |
| Precedence | Rank decides order: brackets > `*` `/` > `+` `-` | Order is by rank, NOT by left-to-right position |
| Associativity | Direction when ranks tie: mostly left→right | `**` is the exception: right→left (`2**3**2 = 512`) |
| `+=` on a list | Mutates the SAME object in place (like `.extend`) | Every alias sees it; `id()` is unchanged |
| `+=` on int/str/tuple | Rebinds the name to a NEW object | The original and any alias are untouched; `id()` changes |
| Coercion | Python silently widens a type where safe (`1 + 2.0 → 3.0`) | `"5" + 3` is NOT coerced → `TypeError`; Python refuses to guess |
| `ValueError` | Right type, unparseable/illegal value | `int('2.5')` → `ValueError` (int accepts str, but not that value) |
| `TypeError` | No valid operation between these types | `"5" + 3` → `TypeError` (no `+` between str and int) |

---

## SELF-TEST ANSWERS

**A1.** `-7 // 2 = -4`. Floor division pushes toward −∞, and −4 is the whole
number below −3.5. `int(-3.5) = -3`, because `int()` truncates (drops the decimal
toward zero). They only differ on negatives.

**A2.** On a list, `x += [4]` mutates in place (same object, `id` unchanged). On
an int, `x += 1` rebinds `x` to a new object (`id` changes); the old `5` is
untouched.

**A3.** `y` becomes `[1,2,3,4]` too. `y = x` made `y` an alias — the same
object — and `+=` mutated that object in place, so both names see the change.

**A4.** `2 + 3 * 4 = 14` (multiply has higher rank, runs first);
`(2 + 3) * 4 = 20` (brackets are highest). Order is decided by rank, not position.

**A5.** `8 - 3 - 2 = 3`, running left→right. That property is **associativity**;
equal-rank operators mostly associate left→right.

**A6.** `True` and `False` — nothing else.

**A7.** Step 1: `5 > 3` = True. Step 2: `5 > 100` = False. Step 3:
`True and False` = **False**. `and` needs both sides true.

**A8.** `int("2.5")` → `ValueError` (type is fine, value can't be parsed).
`"5" + 3` → `TypeError` (no valid operation between these types). Rule: value
wrong → `ValueError`; operation/type wrong → `TypeError`.

**A9.** *coercion* = coerce = force: Python silently forcing one safe type into
another (`1 + 2.0 → 3.0`). *truncation* = cut off: drop the decimal toward zero.
*precedence* = rank deciding which operator runs first. *associativity* =
direction when ranks tie (mostly left→right; `**` is right→left).

---

## WHAT'S COMING NEXT — SESSION 13

- **Term-tax**: the cold vocabulary volley (coercion, `ValueError`, `TypeError`,
  truncation, floor division, alias, rebind, operand, expression vs statement,
  precedence, associativity).
- Remaining cold re-tests: `bool("False")`, `10/2` (value and type), mutating
  methods return `None`, and "where the default lives" in isolation.
- **Finish 1.5**: membership (`in` / `not in`), short-circuit evaluation (`and`
  returns the first falsy, `or` the first truthy — and they return the **operand**,
  not a bare bool), bitwise operators (brief), `%` and `**` drills.
- Owed demos: `id()` for shallow vs deep copy on an outer **and** a nested object;
  spoken Feynman recall for 1.3 and 1.4.
- The 1-week re-test batch: frames, stack-not-queue, namespace vs frame, running
  vs paused frames, line-vs-frame finishing.
