# SESSION 9 NOTES — Friday 31 July 2026

**Topics: the object model from both sides · four `str`/identity worked examples ·
the `==`/`is` conflation, mechanically · `None` · frames, `return`, and what
happens during `print`**

1.3 stays open — type conversion and implicit-vs-explicit conversion come next.

---

## SELF-TEST — answer these cold before reading on

Say each answer aloud, then add the spoken cross-check: "my rule says X, my
answer is Y, they agree." Rate confidence /5. Answers at the back.

1. `a = Config(); b = a; a.speed = 5; print(b.speed)` — what prints, or does it
   raise? Why?
2. `a = "reading"; b = a; a = a.upper(); print(b)` — what prints? Did any object
   change?
3. `name = "  culham  "; name.strip(); print(repr(name))` — what prints, and why?
4. `x = "abc"; before = id(x); x = x + "d"; after = id(x)` — is
   `before == after`? Rebinding or mutation, and which side of the `=` told you?
5. What does `None` mean, and how is it different from `0` and from `False`?
6. Why is `x is None` safer than `x == None`? Give the mechanism, not the habit.
7. A function has no `return` statement. When does its frame leave the stack, and
   what value does the call produce?
8. During `print(greet())`, how many frames does the call to `print` add, and
   what happens to the caller's frame while `print` runs?

> Questions 2, 4 and 6 are the ones where a correct rule has historically been
> written down and then contradicted one clause later. Those are exactly the
> answers to cross-check aloud before they are final.

---

## FULL TEACHING

### 1. The object model, seen from both sides

Everything in Python is an object with its own identity — an address you can read
with `id()`. A name is not a box holding the object; it is a **label bound to**
the object.

The correct phrasing, and it matters in interviews: **"bind the object to a
name"**, never "bind the name with the object". The object is the thing that
exists; the name is one of possibly several labels pointing at it.

Two operations look similar and are not:

- **Mutation** — the object itself changes in place; its `id()` stays the same.
  Every other name bound to that object sees the change.
- **Rebinding** — a name is pointed at a different object. The old object is
  untouched; any other name still bound to it is unaffected.

The rule that decides which one you are looking at is **the LEFT of the `=`**,
not the presence of `=`:

- a **bare name** on the left (`x = ...`) → **rebinding**;
- a name with `.attr` or `[index]` on the left (`a.speed = ...`, `lst[0] = ...`)
  → **mutation** of the object that name is bound to.

The right-hand side only tells you what the new or updated value is. **It never
tells you whether you rebound or mutated** — only the left side answers that.

### 2. Four worked examples

**P1 — attribute mutation through a shared reference**

```python
class Config:
    pass

a = Config()
b = a                  # b and a are the SAME object (one object, two labels)
a.speed = 5            # LEFT side is a.speed -> mutation of that object
print(b.speed)         # -> 5
```

`b = a` did not copy anything; it bound a second name to the one object.
`a.speed = 5` has an attribute on the left, so it mutates that shared object and
its `id()` is unchanged. Because `b` points at the same object, `b.speed` is `5`.

**P2 — a string method builds a new object; the old name is untouched**

```python
a = "reading"
b = a                  # same object, two labels
a = a.upper()          # upper() BUILDS a new "READING"; bare name a -> rebinding
print(b)               # -> reading
```

No object changed. `str` is immutable, so `.upper()` cannot alter the original —
it returns a brand-new object. The left of line 3 is the bare name `a`, so that
line rebinds. `b` still points at the original `"reading"`.

**P3 — the most common string bug: throwing away the return value**

```python
name = "  culham  "
name.strip()                # returns a stripped COPY -- and it is discarded
print(repr(name))           # -> '  culham  '   (spaces still there)
```

`.strip()` does not modify `name`; it returns a new stripped string. Nothing
captured that return value, so it is computed and immediately thrown away.
`repr()` is used so the surrounding whitespace is visible. **The fix is always
`name = name.strip()`.**

**P4 — rebinding is not mutation; the left side is the tell**

```python
x = "abc"
before = id(x)
x = x + "d"      # builds a new "abcd"; bare name x -> REBINDING
after = id(x)
# before == after -> False
```

`str` is immutable, so `x + "d"` cannot change the original object; it produces a
new one, and the bare name `x` is then pointed at it, at a different address. The
left side told you. The right side (`x + "d"`) only says *what* the new object
is; it is not what decides rebind-vs-mutate.

### 3. The `==`/`is` conflation, mechanically

The conflation in its purest form is this chain of reasoning: *"both `True` and
`1` have the value 1, therefore they must be the same object."* Identity is being
**inferred from value equality**, which does not follow. Equal values say nothing
about how many objects exist.

Note that the rule can be perfectly well known and the conclusion still come out
wrong — the rule simply never gets checked against the answer.

Hence the spoken cross-check: *"my rule says identity needs the same address; my
answer says they are identical; do they agree?"* Said out loud, rule and
conclusion land in the same breath and the contradiction becomes audible. Written
one clause apart, it hides.

### 4. `None`

`None` means **"no value present"** — not empty, not zero, not false. It is the
single object of its own type, `NoneType`, and there is exactly one `None` in the
whole program.

- `None`, `False` and `0` are three different objects of three different types.
  All three are falsy, but none is `==` to another: `None == False` is `False`,
  `None == 0` is `False`.
- `0` is an `int` that *has* a value (zero). `None` is a `NoneType` that means
  *there is no value*. A different kind of thing, not a different number.
- **A function with no `return` returns `None`.**

**Why `is None`, not `== None`.** Because `NoneType` has exactly one object
program-wide, an identity check is exact. More importantly: **`==` can be
overridden** by a class's `__eq__`, so a hostile or buggy object could define
`__eq__` to return `True` when compared to `None` — `==` can be made to lie. `is`
checks the address and cannot be faked or overridden. That override point is the
mechanism, and it is the half that is usually missed.

```python
def f():
    pass                            # no return

x = f()
print(x)                            # None
print(type(x))                      # <class 'NoneType'>

a = None
b = None
print(a is b)                       # True   -- one object program-wide
print(id(a) == id(b))               # True

print(None == False)                # False
print(None == 0)                    # False
```

### 5. Three doubts about frames and `print`, cleared

**(a) When does a frame finish if there is no `return`?**

A function returns — and its frame is removed — either when it hits an explicit
`return`, or when its last line finishes with nothing left to do, at which point
it **auto-returns `None`**.

The earlier confusion was a case where the last line was itself calling another
function. **That call-line is not "done" until the callee returns**, so the frame
stayed open. **"Line reached" is not "line completed."**

**(b) The stack picture during a `print(...)` call**

`print` is itself a call, so it gets its own new **top** frame. The function that
called `print` sits one frame below, its line still in progress — paused
mid-line, waiting. When `print` returns (handing back `None`), only `print`'s
frame is removed; the caller's frame becomes the top frame again and resumes from
exactly where it paused.

So the caller's frame is alive the whole time `print` runs, and it is the top of
the stack again the instant `print` is done.

**(c) Scope note.** `print` gets its own proper treatment later, and functions
are a full upcoming topic (1.7). They were touched here only as far as the frame
picture required.

---

## KEY MENTAL MODELS

- Bind the **object to a name** — never "the name to the object".
- Mutation keeps `id()`; rebinding changes which object a name points at.
- The **left** of the `=` decides which one it was. The right side never does.
- Immutable types can't be edited: every "change" is a new object.
- Discarding a string method's return value is the classic string bug.
- Identity cannot be faked; equality can be overridden. That is why `is None`.
- A function with no `return` still returns something: `None`.
- Every call, including `print`, gets its own frame; the caller stays alive and
  paused underneath it.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Item | What it does | The trap |
|---|---|---|
| `.strip()` | Returns a copy with leading/trailing whitespace removed | Returns a **new** string; discarding the return value is the single most common string bug. Use `s = s.strip()` |
| `.upper()` / `.lower()` | Returns a new case-changed copy | New object at a new `id()`; the original is unchanged because `str` is immutable |
| `.replace(a, b)` | Returns a copy with `a` replaced by `b` | Also returns a new object — assign it or it is lost |
| `s[0] = "X"` | (Attempted) item assignment on a string | Raises `TypeError`; `str` has no item assignment at all — contrast `obj.attr = ...`, which succeeds and mutates |
| `repr(x)` | The unambiguous printable form of an object | Use it to *see* whitespace and quotes that `print` hides (`'  culham  '`) |
| `id(x)` | The object's identity (its address) | Same value before/after = same object (mutation); different = a new object (rebinding) |
| `None` | The sole `NoneType` object; "no value present" | Not equal to `0` or `False` even though all are falsy; a function with no `return` yields it |
| `is None` | Identity test against the single `None` object | Prefer over `== None`: `==` calls `__eq__` and can be made to lie; `is` checks the address |
| rebind vs mutate | Which operation an assignment performs | Decided by the **LEFT** of `=`: bare name → rebind; `.attr`/`[idx]` → mutate |

---

## SELF-TEST ANSWERS

1. Prints `5`. `b = a` binds a second name to the one object; `a.speed = 5` has
   an attribute on the left so it mutates that shared object (`id` unchanged);
   `b` sees it.
2. Prints `reading`. No object changed. `.upper()` built a new string and the
   bare name `a` was rebound to it; `b` still points at the original.
3. Prints `'  culham  '`, spaces intact. `.strip()`'s return value was discarded,
   so `name` is unchanged. `repr()` makes the spaces visible.
4. `before == after` is `False` — rebinding, not mutation. The left side (bare
   name `x`) told you; the right side only says what the new object is.
5. `None` means "no value present" and is the only `NoneType` object. `0` is an
   `int` with the value zero; `False` is a `bool`. All three are falsy but none is
   `==` to another.
6. `is None` checks identity/address, which cannot be overridden. `==` calls
   `__eq__`, which a class can redefine to return `True` against `None` — so
   `== None` can be made to lie. Plus there is only one `None` program-wide, so
   identity is exact.
7. The frame leaves the stack when the last line finishes with nothing left to do
   (or on an explicit `return`). With no `return`, the call produces `None`.
   Caveat: if the last line is itself a call, the frame stays open until that
   callee returns — line reached ≠ line completed.
8. `print` adds one new top frame. The caller's frame sits one below, paused
   mid-line. When `print` returns `None`, only its frame is removed and the
   caller's frame becomes the top again and resumes.

---

## WHAT'S COMING NEXT — SESSION 10

Type conversion — `int()`, `str()`, `float()`, `bool()` — then implicit vs
explicit conversion. Then, and only then, 1.3 closes. `None` still needs an
unaided from-cold re-test on a later day before it earns a full tick.
