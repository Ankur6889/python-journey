# SESSION 5 NOTES — Opening 1.3: Data Types

**Topics: the script entry point (`<module>`) · `int` arbitrary precision ·
`float` and IEEE 754 approximation · `bool` as a subclass of `int` · `==` vs `is`
again · `type()` vs `isinstance()` · output-labelling hygiene**

---

## SELF-TEST — answer these cold before reading on

1. Given a traceback whose frames are `<module>` → `main` → `summarize`, which
   function did the program *start* executing in?
2. What is the size ceiling on a Python `int`? On a `float`?
3. Is `0.1 + 0.1 + 0.1 == 0.3` False because of display, or because the numbers
   genuinely differ? Say which.
4. `True == 1` and `True is 1` — give both answers and the reason each way.
5. `isinstance(x, int)` with `x = True`: what comes back, and how does
   `type(x) == int` differ?

---

## FULL TEACHING

### 1. The script entry point

Every Python program starts executing at **module level** — the frame the
traceback calls `<module>`. That is the top-level code the interpreter runs
before any function is called.

```
Traceback (most recent call last):
  File "pipeline.py", line 21, in <module>
    main()
  File "pipeline.py", line 17, in main
    summarize(records)
  File "pipeline.py", line 11, in summarize
    avg = total / count
ZeroDivisionError: division by zero
```

Execution order here: `<module>` → `main()` → `summarize()` → crash. The stack at
the crash is `[<module>, main, summarize]` with `summarize` on top.

`main` is **not** the entry point — it is simply the first thing the module frame
calls. The entry point is always the module frame: bottom of the stack, top of
the printed trace.

### 2. Rebinding vs mutation, re-confirmed

```python
x = [1, 2, 3]
x[0] = 99          # mutation
```

The classification process, not just the answer: **check what is on the left of
the `=`.** A bare name → rebinding. A name plus index or attribute access
(`x[0]`, `x.field`) → mutation.

### 3. `int` and `float`

- **`int`** — arbitrary precision. No size ceiling; Python allocates memory as
  needed, so huge integer literals are exact.
- **`float`** — 64-bit IEEE 754. A fixed bit budget means only a finite set of
  values is representable, so most decimals are stored as the **nearest
  approximation**.

> **Practical rule: never use `==` for float equality.** Use
> `abs(a - b) < tolerance`.

### 4. The floating-point demo

```python
0.1 + 0.2 == 0.3             # False
0.1 + 0.1 + 0.1 == 0.3       # False
```

The model: floats are approximate; operations **compound** the error; sometimes
the error is visible and sometimes it rounds back out of sight.

The error is **real, not cosmetic** — `0.1 + 0.1 + 0.1` is genuinely a different
number from `0.3` (it is `0.30000000000000004`), not a display artefact.

The full IEEE 754 binary mechanism — why `0.1` is `0.0001100110011…` in binary
and how rounding accumulates — is parked for **1.13**.

### 5. `bool` is a subclass of `int`

```python
True == 1              # True   — value equality
True is 1              # False  — object identity
False + False + True   # 1      — bools are usable in arithmetic
```

`True` and `1` share a value but are **different objects of different types**.
The direction of the hierarchy matters and is easy to invert under pressure:
**`bool` is a subclass of `int`**, not the other way round.

Usable in arithmetic, yes — but write logic with bools, not with arithmetic.

### 6. `type()` vs `isinstance()`

- `isinstance(x, int)` **respects inheritance** — it accepts `True`, because
  `bool` is a subclass of `int`. Permissive.
- `type(x) == int` is an **exact** type check — it rejects `True`. Strict.

Neither is the "right" one. It is a **design choice driven by intent**: choose by
what the function actually needs, not by habit.

### 7. Code hygiene

Every demonstration function gets a docstring, labelled output, and comments
explaining **why, not what**. The standards:

- **No dead variables.** A variable that is assigned and never printed or used is
  an incomplete-thinking signal to a reader.
- **Label every printed line**, with f-strings:
  `print(f" a is b : {a is b}")`.
- **Comments name the cause, not the symptom.** "not the same object" restates
  what `is` returned; "`a` is `int`, `b` is `bool` → different types, therefore
  different objects" explains it.
- Make abstract claims **empirically visible** — printing `id(a)` and `id(b)`
  next to an `is` result turns a claim into evidence.

---

## KEY MENTAL MODELS

- Scripts start at `<module>`, before any function call.
- Classify assignment by what is on the left of the `=`.
- `int` is exact and unbounded; `float` is 64-bit and approximate — compare with
  a tolerance.
- Float error compounds and is a real numeric difference, not a printing quirk.
- `bool` is a subclass of `int`; same value, different type, different object.
- `==` is value, `is` is identity — and identity can differ because of *type*,
  not just contents.
- `isinstance` is permissive (inheritance-aware); `type() ==` is strict. Pick by
  intent.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `<module>` | The top-level frame | Not `main` — `main` is just its first call |
| `int` | Arbitrary-precision integer | No overflow, but big ints cost memory/time |
| `float` | 64-bit IEEE 754 | `==` on floats is a bug; use a tolerance |
| `bool` | Subclass of `int` | `True == 1` yet `True is not 1`; hierarchy inverts easily |
| `type(x)` | Exact runtime type | Rejects subclasses — including `bool` for `int` |
| `isinstance(x, T)` | Type check honouring inheritance | Accepts `bool` where you may have meant strict `int` |
| `abs(a-b) < tol` | Float comparison | Choosing the tolerance is your problem, not Python's |

---

## WHAT'S COMING NEXT — SESSION 6

- One-question recall on the script entry point, from a fresh traceback.
- One-question recall on `==` vs `is`, where value matches but identity differs.
- Finish 1.3: `str` (immutability + common methods), `None` (singleton,
  `is None` not `== None`, `None` vs `False` vs `0`), and type conversion
  (`int()`, `str()`, `float()`, `bool()`), implicit vs explicit.
- **Not** 1.4 yet — the mutation drill stays queued until 1.3 is closed and
  list/dict familiarity is there.
