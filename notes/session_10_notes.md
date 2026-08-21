# SESSION 10 NOTES — Saturday 1 August 2026

**Topics: type conversion (`int`/`str`/`float`/`bool`) · strict parsing vs lenient
numeric conversion · truthiness · implicit conversion (coercion) · `/` vs `//` ·
mutability · aliasing · mutable arguments in functions · the mutable-default trap**

This closes 1.3 and 1.4.

---

## SELF-TEST — answer these cold before reading on

Say each answer aloud before checking. Where a question asks for a rule and a
verdict, use the short-form cross-check: rule in one line, answer in one line, do
they agree.

1. What does `int("3.5")` return?
2. What does `int(3.9)` return? Why is that different from Q1, given both involve
   a decimal?
3. What is `bool("False")`? Explain the rule that produces it.
4. What is `bool("")`? Explain precisely, in terms of what kind of object is
   being passed in.
5. `True + 1` — what is the value, and what is the type?
6. `"5" + 3` — what happens, and why does Python behave this way when JavaScript
   does not?
7. `10 / 2` — value and type? What would `10 // 2` give?
8. Define aliasing in one sentence.
9. `p = [1, 2, 3]; q = p; q.append(4)` — what does `p` show? State the rule, then
   the answer.
10. Inside a function, what is the difference in effect on the caller between
    `lst.append(99)` and `lst = [99]`?
11. For `def add_item(item, bucket=[]): bucket.append(item); return bucket` —
    what do three successive calls `add_item(1)`, `add_item(2)`, `add_item(3)`
    return? Where does the list that causes this actually live?
12. Write the fixed version. Why `is None` rather than `== None`?
13. In the broken version, why does `add_item(5, [])` behave correctly?
14. Which are safe as default arguments and which are not: `0`, `[]`, `""`, `{}`,
    `None`, `(1, 2)`?

Answers at the back.

---

## FULL TEACHING — TYPE CONVERSION

### 1. The core model

There are four explicit conversion functions: `int()`, `str()`, `float()`,
`bool()`.

The most important property, and the one that ties back to everything in 1.2: **a
conversion function RETURNS a new object of the new type. It does not modify the
original.** Same behaviour as the `str` methods from Session 7, for the same
reason — the original object is not being edited, a new object is built and
handed back.

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

`x` is untouched. If you do not capture the return value, the conversion is
thrown away — exactly the trap `.strip()` set in Session 7.

### 2. The asymmetry — this is the whole lesson

**Python is strict when parsing a string and lenient when converting a number.**

```python
print(int(3.9))         # numeric conversion — lenient
```
```
3
```

```python
print(int("3.5"))       # string parsing — strict
```
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.5'
```

Both involve a decimal. One truncates silently, one raises. Why:

- `int(3.9)` receives a **float** object. A float already *is* a number, and there
  is exactly one defensible integer conversion — drop the fractional part,
  **truncating toward zero**. So `int(3.9)` is `3` and `int(-3.9)` is `-3` (toward
  zero, *not* "round down" — this matters for negatives).
- `int("3.5")` receives a **string**. A string is not a number; it is a sequence
  of characters Python must **parse**, and `"3.5"` is not a valid integer literal.
  Python will not silently decide you meant `3` — you might have meant `4`, or
  made a typo. It raises rather than guess.

> **The rule to carry: parsing is strict, numeric conversion is lenient.**

### 3. `bool()` — the trap

```python
print(bool(""))        # False
print(bool("False"))   # True
print(bool("0"))       # True
print(bool(0))         # False
print(bool([]))        # False
print(bool([0]))       # True
```

**`bool()` never reads the contents of a string.** It asks one question only: is
this container empty or not? An empty string is falsy. Any non-empty string is
truthy — including `"False"`, including `"0"`, including `" "` (a single space is
a character, so the string is not empty).

Two things to unlearn:

1. `bool("False")` is `True`. The characters spell "False" but `bool()` does not
   read them.
2. `bool("")` is `False` **because the string is empty**, not because it "is
   `None`" or "receives `None`". An empty string is a perfectly real `str` object:
   it exists, it has an `id`, `type("")` is `<class 'str'>`. It is falsy purely
   because it has zero length. `None` is a different object of a different type
   and is not involved.

```python
print(type(""), id("") is not None, "" is None)
# <class 'str'> True False
```

**Falsy values worth memorising:** `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`,
`set()`. Everything else is truthy — including `"False"`, `"0"`, `[0]`, `" "`.

---

## FULL TEACHING — IMPLICIT VS EXPLICIT CONVERSION

### 4. Explicit

You calling one of the four functions. You asked for it, so Python does it, and
if it cannot, it raises.

### 5. Implicit (coercion)

Python doing it silently, on its own — and **only where there is one obvious,
safe, lossless direction**.

```python
result = 1 + 2.0
print(result, type(result))     # 3.0 <class 'float'>
```

`1` is an int, `2.0` is a float. To add them Python must make them the same type.
Widening int → float is safe and lossless; narrowing float → int would throw away
information. So Python widens.

### 6. Why `"5" + 3` raises

```python
print("5" + 3)
```
```
TypeError: can only concatenate str (not "int") to str
```

There is no safe or obvious direction. Python could convert `3` to `"3"` and give
`"53"`, or convert `"5"` to `5` and give `8`. Both are defensible and they give
completely different answers, so **Python refuses to guess**. JavaScript picks one
and returns `"53"` — which is why JS has a reputation for silent type surprises.

Worth being able to state in an interview: **Python coerces only where the
direction is unambiguous and lossless; otherwise it raises rather than choosing
for you.**

### 7. The `bool`-is-an-`int` consequence

```python
result = True + 1
print(result, type(result))     # 2 <class 'int'>
```

`bool` is a subclass of `int`; `True` is 1, `False` is 0. So `True + 1` is
arithmetic, giving `2`, and the type is **`int`**, not `bool`. The value is easy;
the type is the twist.

### 8. The division trap

```python
print(10 / 2, type(10 / 2))     # 5.0 <class 'float'>
print(10 // 2, type(10 // 2))   # 5   <class 'int'>
print(7 // 2)                   # 3
print(-7 // 2)                  # -4
```

`/` **always** returns a float, even when the division is exact. `//` is floor
division and returns an `int` for int operands.

Note the last line: `//` **floors** (rounds toward negative infinity), so
`-7 // 2` is `-4`, not `-3`. That is different from `int()`'s **truncation toward
zero**, which would give `-3`. Two different rounding behaviours in the same
language — hold them separately.

---

## FULL TEACHING — MUTABILITY (1.4)

### 9. What mutability means

**Mutable** = the object can be changed in place: same object, same `id()`,
different contents. **Immutable** = the object cannot be changed; any "change"
builds a new object and rebinds the name to it, and the original is untouched.

- Immutable: `int`, `float`, `bool`, `str`, `tuple`.
- Mutable: `list`, `dict`, `set`.

```python
lst = [1, 2, 3]
print("before:", lst, id(lst))
lst.append(4)
print("after: ", lst, id(lst))

s = "hello"
print("before:", s, id(s))
s = s + " world"
print("after: ", s, id(s))
```

```
before: [1, 2, 3] 140234891234567
after:  [1, 2, 3, 4] 140234891234567
before: hello 140234889112345
after:  hello world 140234887654321
```

The list keeps the same `id` — one object, mutated. The string gets a new `id` —
a second object was built and `s` was rebound to it. The original `"hello"` still
exists, unchanged, until nothing refers to it.

### 10. Aliasing

**Aliasing is when two or more names refer to the same object.** The second name
is an *alias* of the first.

The key fact: **assignment never copies.** `b = a` does not duplicate anything; it
binds a second name to the same object.

```python
a = [1, 2, 3]
b = a

print(a is b)       # True
b.append(4)
print("a:", a)      # a: [1, 2, 3, 4]
print("b:", b)      # b: [1, 2, 3, 4]
```

One object, two names. Mutating through either name is visible through both,
because there is only one object to mutate.

Contrast with an immutable type:

```python
x = "hello"
y = x
y = y + " world"

print("x:", x)      # x: hello
print("y:", y)      # y: hello world
print(x is y)       # False
```

`y = x` also created an alias — but `y = y + " world"` then **rebound** `y` to a
brand-new object. `x` still points at the original.

Worth noticing the counterfactual: if strings were mutable, `x is y` would have
been `True` and `x` would have changed too. **The immutability of `str` is what
makes the second line safe.**

### 11. Mutable arguments in functions

**Passing an argument to a function is an assignment.** It binds a new local name
inside the function's frame to the same object the caller passed in. That single
fact produces the whole behaviour:

```python
def mutate(lst):
    lst.append(99)       # acts on the OBJECT
    print("  inside:", lst, id(lst))

def rebind(lst):
    lst = [99]           # rebinds the LOCAL NAME
    print("  inside:", lst, id(lst))

data = [1, 2, 3]
print("before mutate:", data, id(data))
mutate(data)
print("after mutate: ", data, id(data))

data2 = [1, 2, 3]
print("before rebind:", data2, id(data2))
rebind(data2)
print("after rebind: ", data2, id(data2))
```

```
before mutate: [1, 2, 3] 140234891000001
  inside: [1, 2, 3, 99] 140234891000001
after mutate:  [1, 2, 3, 99] 140234891000001
before rebind: [1, 2, 3] 140234891000002
  inside: [99] 140234891999999
after rebind:  [1, 2, 3] 140234891000002
```

The deciding line is **mutate vs rebind**:

- `lst.append(99)` — a dot-method acting on the object. One object, mutated. The
  caller's name points at that same object, so the caller sees it.
- `lst = [99]` — an `=` rebinding the **local name** to a different object. The
  caller's name is untouched.

This is a **semantic** reading, not a syntactic one. Do not classify by "is there
an `=`". Classify by what the statement does to the **object** versus what it
does to the **name**.

### 12. Frames, namespaces and the heap

A doubt worth recording: every function call gets its own frame with its own
namespace — so how can two frames see the same list?

Because **namespaces hold names, not objects**. Objects live on the **heap**. A
namespace maps a name to a *reference* to a heap object, and two different frames
can each hold a name referencing the same heap object. The frames are separate;
the object is shared.

Frames and their namespaces are **ephemeral** — created on call, destroyed on
return. Objects on the heap survive as long as something still refers to them.

### 13. The mutable default argument — the centrepiece

A genuine interview classic, and the single best test of whether the object model
has landed.

**The broken version:**

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item(1))     # [1]
print(add_item(2))     # [1, 2]
print(add_item(3))     # [1, 2, 3]
```

Most people expect `[1]`, `[2]`, `[3]`. It accumulates instead.

**Why:** the default expression `[]` is evaluated **ONCE** — when the `def`
statement executes, not on each call. That single list object is stored on the
**function object**, in its `__defaults__` attribute, and reused by every call
that omits the argument.

Prove it:

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print("defaults before:", add_item.__defaults__)    # ([],)
add_item(1)
print("defaults after: ", add_item.__defaults__)    # ([1],)
```

The default itself was mutated. There is one list, living on the function object,
being appended to forever.

**Four doubts, resolved:**

1. *Is the default list bound to the parameter name `bucket`?* No. It lives in the
   function object's `__defaults__`. At call time, if the argument is omitted,
   `bucket` is bound to whatever object is sitting there.
2. *If I supply my own list, does the default get garbage-collected?* No. The
   function object still holds a reference to it, so it survives — it just sits
   unused for that call.
3. *Where does the `def` statement bind the function object?* In the enclosing
   namespace — the module namespace (globals) if `def` is at top level.
4. *Why does the default persist when frames don't?* Because the function object
   and its `__defaults__` are **durable**, living as long as the module. Per-call
   frames and their local namespaces are ephemeral. The default list is stored on
   the durable thing, so it outlives every call.

**The fix:**

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item(1))     # [1]
print(add_item(2))     # [2]
print(add_item(3))     # [3]
```

`None` is immutable, so there is nothing to accumulate into. A fresh list is built
inside the body on every call that needs one.

Note `is None`, **not** `== None` — the Session 9 identity rule cashing out: `==`
can be overridden by a class's `__eq__` and made to lie; `is` compares object
identity and cannot be faked. For a sentinel check, always `is None`.

**Why `add_item(5, [])` works even in the broken version:** supplying an argument
means the parameter name is bound to *your* object, not to the poisoned default.
`bucket.append(5)` appends to your list; the shared default is never touched on
that call. **The bug only bites when you let the default apply.**

> **The rule: never use a mutable object as a default argument.** Immutable
> defaults — `0`, `""`, `None`, tuples — are safe, because there is nothing to
> accumulate into. When you need a mutable default, use `None` as a sentinel and
> build the object inside the function.

---

## REFERENCE CHECKLIST — name / what it does / the trap

### Conversion functions

| Name | What it does | The trap |
|---|---|---|
| `int(x)` from a number | Converts to integer | Truncates **toward zero**, silently: `int(3.9)`→3, `int(-3.9)`→-3. Not rounding |
| `int(x)` from a string | Parses an integer literal | **Strict.** `int("3.5")` raises `ValueError`; whitespace is tolerated, a decimal point is not |
| `float(x)` | Converts to floating point | `float("3.5")` works — unlike `int`. `float("nan")`/`float("inf")` are valid and break comparisons (`nan != nan`) |
| `str(x)` | Builds the string representation | Almost never raises. `str(3) + str(4)` is `"34"` — concatenation, not addition |
| `bool(x)` | Truthiness test | Never reads string content. Empty→False, non-empty→True. `bool("False")`, `bool("0")`, `bool(" ")` are all `True` |
| all four | Return a **new** object of the new type | Don't modify the original; uncaptured return value is lost |

### Implicit conversion

| Case | Result | The trap |
|---|---|---|
| `1 + 2.0` | `3.0`, float | Python widens int→float because it is safe and lossless |
| `True + 1` | `2`, int | `bool` subclasses `int`; the value is obvious, the type is the twist |
| `"5" + 3` | `TypeError` | No safe direction — `"53"` and `8` are both defensible, so Python refuses to guess |
| `10 / 2` | `5.0`, float | `/` always returns a float, even on exact division |
| `10 // 2` | `5`, int | `//` floors toward −∞: `-7 // 2` is `-4`, whereas `int(-7/2)` is `-3` |

### Mutability

| Concept | What it means | The trap |
|---|---|---|
| Mutable | Object changes in place; `id()` unchanged | `list`, `dict`, `set` |
| Immutable | "Change" builds a new object and rebinds; `id()` changes | `int`, `float`, `bool`, `str`, `tuple` |
| Aliasing | Two or more names referring to the same object | `b = a` **never** copies — mutate via either, see it via both |
| Passing an argument | Is an assignment — binds a new local name to the same object | The function can mutate the caller's object |
| `lst.append(x)` in a function | Mutates the shared object | Caller sees the change |
| `lst = [x]` in a function | Rebinds the local name only | Caller sees nothing |
| Namespaces | Hold names, not objects | Objects live on the heap; several frames can name one object |
| Frames | Ephemeral — destroyed on return | Function objects are durable and outlive every call |

### Default arguments

| Item | What it does | The trap |
|---|---|---|
| `def f(x, bucket=[])` | Default evaluated **once**, at `def` time | Accumulates across calls; one shared list in `f.__defaults__` |
| `f.__defaults__` | Tuple of the function's default values | Inspect it to see the bug: `([],)` becomes `([1],)` |
| `bucket=None` + `if bucket is None: bucket = []` | The correct pattern | Use `is None`, never `== None` |
| Safe defaults | `0`, `""`, `None`, tuples | Immutable — nothing to accumulate into |
| Unsafe defaults | `[]`, `{}`, `set()`, any mutable object | Shared across every call that omits the argument |
| Supplying your own argument | Binds the parameter to your object | Works even in the broken version — the bug only bites when the default applies |

---

## SELF-TEST ANSWERS

1. Raises `ValueError`. String parsing is strict; `"3.5"` is not a valid integer
   literal.
2. `3`. Different because `int(3.9)` receives a float — already a number, with one
   defensible conversion (truncate toward zero) — whereas `int("3.5")` receives a
   string that must be parsed, and Python will not guess.
3. `True`. `bool()` never reads a string's contents; it only asks whether the
   string is empty. `"False"` is non-empty, therefore truthy.
4. `False` — because the string is **empty**, not because it is or receives
   `None`. An empty string is a real `str` object with an id and a type; it is
   falsy purely because its length is zero.
5. Value `2`, type `int`. `bool` is a subclass of `int` and `True` is 1.
6. `TypeError`. There is no unambiguous, lossless direction between `str` and
   `int` — `"53"` and `8` are both defensible — so Python raises rather than
   choosing. JavaScript picks concatenation and returns `"53"`.
7. `5.0`, type `float` — `/` always returns a float. `10 // 2` gives `5`, an
   `int`.
8. Aliasing is when two or more names refer to the same object.
9. Rule: `q = p` binds a second name to the same list object; assignment never
   copies. Answer: `q.append(4)` mutates that one shared object, so `p` shows
   `[1, 2, 3, 4]`.
10. `lst.append(99)` mutates the shared object, so the caller sees the change.
    `lst = [99]` rebinds only the function's local name, so the caller sees
    nothing.
11. `[1]`, `[1, 2]`, `[1, 2, 3]`. The list lives on the function object, in
    `add_item.__defaults__` — created once when the `def` executed, reused by
    every call that omits the argument.
12. ```python
    def add_item(item, bucket=None):
        if bucket is None:
            bucket = []
        bucket.append(item)
        return bucket
    ```
    `is None` rather than `== None` because `==` can be overridden by a class's
    `__eq__` and made to return something misleading, whereas `is` compares object
    identity and cannot be faked.
13. Because supplying an argument binds `bucket` to your list, not to the shared
    default. The append hits your list; the poisoned default is never touched. The
    bug only appears when the default is allowed to apply.
14. Safe: `0`, `""`, `None`, `(1, 2)` — all immutable. Unsafe: `[]`, `{}` — both
    mutable, and both shared across every call that omits the argument.

---

## WHAT'S COMING NEXT — SESSION 11

1. Cold recall, unaided: the mutable-default trap (what goes wrong, where the list
   lives, the fix); `bool("False")`; `10 / 2` value and type.
2. **Shallow vs deep copy** — the one 1.4 item carried. It follows directly from
   aliasing: `b = a` is not a copy at all; `b = a.copy()` copies one level, so the
   outer list is independent but nested objects are still shared;
   `copy.deepcopy(a)` copies all the way down. This closes 1.4 completely.
3. Open **1.5 Operators and Expressions**, leading with the two items that test
   whether 1.4 landed: `/` vs `//`, and **augmented assignment** — `+=` on a list
   mutates in place, `+=` on an int, string or tuple rebinds.
4. Two written Feynman pages are due — one for 1.3, one for 1.4.
