# SESSION 13 NOTES — Wednesday 5 August 2026

**Topics: mutating methods return `None` (mutate vs build) · membership `in` /
`not in` · short-circuit evaluation · bitwise operators (awareness) · modulo `%`
on negatives · exponentiation `**` and right-associativity**

Closes the 1.5 (Operators) tail — 1.5 is now covered end to end.

---

## SELF-TEST — answer these cold before reading on

1. What does `result = q.append(4)` put in `result`? And what is in `q`
   afterwards?
2. Why is `q = [].append(4)` broken — what is `q`, and what happened to the list?
3. Give the one-line test that decides whether a method call should be assigned
   or not.
4. `"apple" in {"apple": 50}` → ? And `50 in {"apple": 50}` → ? Why the
   difference?
5. `0 and 5` → ? `3 and 5` → ? `0 or "hi"` → ? State the rule for what `and`/`or`
   return.
6. Why does `2 or 1/0` NOT raise `ZeroDivisionError`?
7. When do `and`/`or` actually return `True`/`False` rather than a value?
8. `-9 % 4` → ? Show the floored quotient and the identity; don't guess.
9. `-1 % 5` → ? (floored quotient first)
10. `2 ** 3 ** 2` → ? and `2 ** 2 ** 3` → ? Which pair binds first?
11. What is the difference between `&` and `and`?

---

## FULL TEACHING

### 1. Mutating methods return `None`

A method call does two separate things, and they must not be confused: a **side
effect** (it may change an object in place) and a **return value** (what the call
hands back). For the mutating list methods, the return value is always `None`.

```python
q = [1, 2, 3]
result = q.append(4)

print(q)            # [1, 2, 3, 4]   <- the list WAS mutated in place
print(result)       # None           <- append returned None, NOT the list
```

`result` catches the return value, which is `None`. The mutation still happened to
`q`. **The two facts are independent.**

The classic broken "fix":

```python
q = [].append(4)
print(q)         # None   <- there is NO list left, just None
```

`[]` builds a fresh list, `.append(4)` mutates it to `[4]` and returns `None`;
since no name was bound to the list, `=` receives only the `None`. The `[4]` list
is unreachable and gets garbage-collected. A later `q.append(5)` would raise
`AttributeError: 'NoneType' object has no attribute 'append'`.

**Rule:** `append`, `sort`, `reverse`, `extend`, `insert`, `remove` mutate in
place and return `None` — statements in disguise. Never assign their result.

Contrast with calls that **build** a new object and *are* assigned:

```python
s2 = "hello".upper()         # str methods return NEW objects -> "HELLO"
nums_sorted = sorted(nums)   # sorted() is a function -> new list
nums.sort()                  # .sort() is a method   -> None, mutates in place
```

> **The durable test for any call: does it MUTATE or BUILD?** Mutate → returns
> `None`, don't assign. Build → returns a new object, do assign.
>
> This is **not** "methods return `None`, functions return values" —
> `str.upper()` is a method that builds. The split is **mutate-vs-build**, not
> method-vs-function.

### 2. Membership: `in` / `not in`

Answers "is this value present in that container?" and always returns a bool.
What it checks depends on the container:

```python
3 in [1, 2, 3]            # True   (list/tuple/set -> elements)
"ell" in "hello"          # True   (string -> SUBSTRING, not just chars)
"apple" in {"apple": 50}  # True   (dict -> KEYS)
50 in {"apple": 50}       # False  (50 is a VALUE, not a key)
```

**Trap:** `in` on a dict checks **keys**, never values. For values, use
`50 in prices.values()`.

### 3. Short-circuit evaluation

`and` / `or` **stop the moment the answer is settled**, and they return **the
operand that settled it** — not a manufactured `True`/`False`.

```python
0 and 5          # 0     <- 0 is falsy, settled, return 0 (never sees 5)
3 and 5          # 5     <- 3 truthy, must check on, return last operand
0 or "hi"        # hi    <- 0 falsy, check on, "hi" truthy -> return it
"a" or "b"       # a     <- "a" truthy, settled, never checks "b"
2 or 1/0         # 2     <- settled at 2; 1/0 is NEVER evaluated -> no error
```

**The rules:**

- `and` returns the **first falsy** operand, or the **last** operand if none are
  falsy.
- `or` returns the **first truthy** operand, or the **last** if none are truthy.

Either way you get an **operand** back.

**When do you actually see `True`/`False`?** Only when the operand is itself a
bool — usually because it came from a comparison. `(4 > 2) and (1 > 9)`: each side
evaluates to a bool first (`True`, `False`), so `and` returns the bool `False`.
`5 and 3` → operands are numbers, so you get `3`. **The operator never
manufactures a bool; it returns whatever operand it lands on.**

**Why "stops" matters:** it makes guards safe — `if x and x[0] > 5` never touches
`x[0]` when `x` is empty. And it powers the default idiom
`name = user_input or "guest"`.

### 4. Bitwise operators (awareness level)

Recognise the symbols, and that they operate on the **binary bits** of integers,
not the decimal value: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` / `>>`
(shift). `5 & 3 = 1`, `5 | 3 = 7`.

**Do not confuse `&` (bitwise) with `and` (logical).** Arithmetic deferred to
masks/flags work much later.

### 5. Modulo `%` — the value, not just the sign

`%` is **not** school-remainder. It is the leftover forced by **floored** `//`.
The ordinary division fact still holds:

```python
(a // b) * b + (a % b) == a          # always true
```

The one thing Python adds: the quotient is the **floored** one (round DOWN, toward
−∞), even for negatives. Once the quotient is pinned, the remainder has no
freedom.

Worked, `-7 % 3`:

```
-7 / 3 = -2.333...     ->  floor = -3        (down, not -2)
(-3) * 3 + r == -7     ->  -9 + r == -7      -> r = 2
```

So `-7 % 3` is **2**, not 1. On positives the floor matches the school quotient,
so you never notice.

**Sign-follows-divisor is a shortcut that gives only the SIGN. For the VALUE, run
the identity.**

### 6. Exponentiation `**` — right-to-left

`**` is the only common operator that binds **right-to-left**; the rightmost pair
evaluates first.

```python
2 ** 3 ** 2   =   2 ** (3 ** 2)   =   2 ** 9   =   512     (NOT 64)
2 ** 2 ** 3   =   2 ** (2 ** 3)   =   2 ** 8   =   256     (NOT 64)
```

---

## KEY MENTAL MODELS

- A call has a side effect and a return value; they are independent facts.
- Mutate → returns `None`. Build → returns a new object. That is the test, not
  method-vs-function.
- `in` on a dict means keys; on a string it means substring.
- `and`/`or` return an operand and stop as soon as the answer is settled.
- Short-circuiting is what makes guard expressions safe.
- `%` is defined by the floored quotient, so negatives shift the magnitude, not
  just the sign.
- `**` is the one common right-associative operator.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| Mutating methods (`append`, `sort`, `reverse`, `extend`, `insert`, `remove`) | Change the object in place; return `None` | Never assign the result — it's `None`, not the object. "dot-method" is NOT the test; MUTATE-vs-BUILD is |
| `in` / `not in` | Membership test, returns a bool. list/tuple/set → elements; str → substring; dict → keys | On a dict it checks KEYS, not values. Use `.values()` for values |
| `and` / `or` (short-circuit) | Return an OPERAND: `and` → first falsy else last; `or` → first truthy else last. Evaluation STOPS when settled | They return an operand, not `True`/`False`. `2 or 1/0` → `2` (`1/0` never runs). Bool only when the operands are bools |
| Bitwise `&` `\|` `^` `~` `<<` `>>` | Operate on the binary bits of ints (awareness level) | `&` is bitwise, `and` is logical — different animals |
| `%` (modulo) | Leftover forced by floored `//`: `(a//b)*b + r == a`. Floor the quotient, then solve for `r` | NOT school-remainder on negatives. `-7%3 = 2`, not 1. Sign-follows-divisor is only the SIGN |
| `**` (power) | Exponentiation; binds RIGHT-to-left, rightmost pair first | `2**3**2 = 512`, not 64. The only common right-associative operator |

---

## WHAT'S COMING NEXT — SESSION 14

- Owed, at the front of the session while cold: the `id()` shallow/deep-copy demo
  (outer **and** nested), the spoken Feynman recall for 1.3 and 1.4, and the due
  one-week re-test batch (frames, stack-not-queue, namespace-vs-frame,
  `<module>`, running-vs-paused, line-vs-frame).
- Re-ask cold: `result = q.append(4)`; the negative-`%` case; the
  where-the-default-lives sub-point.
- 1.5 items all sit at `[~]` until a later-day unaided re-test.
