# SESSION 16 NOTES — Sunday 9 August 2026

**Topics: `print()` formally · `while` · `break` and `continue` · nested loops ·
loop `else` · the operator drill worked (`//`, `%`, `**`, `==`/`is`, chained
comparison, `/`)**

1.6 Control Flow nearly closed.

---

## SELF-TEST — answer these cold before reading on

Write your answers before reading anything below. "Gap" is a valid answer and a
better one than a guess.

1. Three exceptions, one line each: when does `NameError` fire? `ValueError`?
 `TypeError`?
2. *Why* is an iterator consumed? Not "what happens" — the cause.
3. What category of thing is `StopIteration`? (One word.)
4. What is a traceback, and which line of it names the exception?
5. What does `print()` return? What are `sep` and `end`, and what are their
 defaults?
6. `for` asks an iterator for the next item. What does `while` ask?
7. In a `while` loop, why is `continue` dangerous in a way it never is in a
 `for` loop?
8. Loop `else` — when does it run?
9. Write the modulo identity as a formula.
10. `5 > 3 > 1` — what does Python expand this to, and how many times is the
 middle operand evaluated?

Answers are in section 3 and the checklist in section 8.

---


## FULL TEACHING

### 1. `print()` — formally, at last

`print()` had been used since Session 1 and never defined. It is a **function**
that writes its arguments to standard output.

**It returns `None`.** The tell: nobody ever writes `x = print(...)`
meaningfully, so it is not producing a value. File it with `append` and `sort`:
*do something, return `None`*.

**It calls `str()` on each argument before writing.** This is why `print(5)`
works with no complaint even though `5` is not a string:

```python
print(5)          # 5      — print converts
print("5" + 3)    # TypeError — + refuses
```

`print` converts; `+` refuses. Worth holding as a pair.

**The two parameters that explain its output.** Both have the same answer:

```python
print("a", "b", "c", sep=" ", end="\n")   # the defaults, written out
```

- **`sep`** — goes **between** the items. Default is a single space. That is
 the mystery space in `print("a", "b", "c")` → `a b c`. It is not in the
 strings; `print` inserts it.
- **`end`** — goes **after** everything. Default is `"\n"`, the newline. That
 is why consecutive `print` calls land on separate lines.

Both are changeable:

```python
print("a", "b", "c", sep="-")     # a-b-c
print("a", "b", "c", sep="")      # abc
print("a", end="")                # no newline — next output continues here
print("a", end=" ")               # "a " then next output follows
```

**Symbol note:** the newline is `\n`, **backslash**-n, not `/n`. Forward slash
is division. In a symbol-heavy language that distinction bites.

**The check:**

```python
print("x", "y", sep="", end="")
print("z")
# xyz
```

One line, `xyz`. The subtlety worth spelling out: the *second* `print` still
adds its own default `"\n"`. The output ends with a newline — you just cannot
see it, because nothing follows.

---

### 2. `while`

`for` walks **through** something. It needs an iterable, gets an iterator from
it, and stops when that iterator raises `StopIteration`.

`while` walks through nothing. **It repeats as long as a condition stays true.**

```python
count = 0
while count < 3:
    print(count)
    count = count + 1
# 0
# 1
# 2
```

After the loop, `count == 3` — the loop exits the moment the check fails, and
it fails at 3, so 3 is the value sitting there when you leave.

**The contrast is the point of teaching them adjacently:**

> `for` asks an iterator for the next item.
> `while` re-evaluates a condition.

**What `while` can do that `for` cannot.** Not an abstract distinction — a
concrete shape:

```python
while True:
    user_input = input("Enter a command: ")
    if user_input == "quit":
        break
    print("You said:", user_input)
```

There is no sequence to walk. You do not know how many inputs are coming — zero,
or four hundred. The stopping point is not "we ran out of items", it is "a
condition became true". Sensor readings until a threshold; retry until a
connection succeeds; a control loop until shutdown. **That is the shape you will
meet constantly in robotics.**

---

### 3. `break` and `continue`

- **`break`** exits the loop it is directly inside. In nested loops that means
 the **innermost only** — the outer loop carries on. There is no `break 2` in
 Python.
- **`continue`** abandons **this iteration only** and jumps back to the
 condition check. **Loop lives; iteration dies.** They are not variations on
 each other; in this respect they are opposites.

**The trap.** Two loops that differ only in where
the increment sits:

```python
# SAFE — increment above the continue
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        continue
    print(count)
# 1
# 2
# 4
# 5
```

```python
# INFINITE — increment below the continue
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
# 0
# 1
# 2
# ...then hangs forever, printing nothing
```

`continue` jumps to the **condition check**, skipping everything below it —
including your increment. In a `for` loop this is harmless, because the iterator
advances regardless of what the body does. In a `while` loop it is a hang.

> **RULE: in a `while` loop, put the state update where `continue` cannot skip
> it.**

**The trace tail.** On the safe version, follow it to the end: count reaches 4
and prints; `4 < 5` is still true, so you *enter the body again*, count becomes
5, and 5 prints; *then* `5 < 5` fails and you exit. The condition guards
**entry**, not the value that gets printed. With the increment at the top of the
body, **the last printed value is one past what the condition appears to
allow.**

---

### 4. Nested loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
# 0 0
# 0 1
# 1 0
# 1 1
# 2 0
# 2 1
```

Six lines. The inner loop runs to **completion** for every single value of the
outer — that is where the multiplication comes from, and why nested loops get
expensive fast. 3 × 2 is nothing; two nested loops over a thousand items each is
a million iterations.

**Why does the inner loop restart at 0 every time?** Because `range(2)` is an
**iterable**. Each time the outer loop comes round, `for j in range(2)` calls
`iter()` on it again and gets a **fresh iterator**, starting at position zero.
The old iterator was exhausted, but that never touched the iterable.

**The version that breaks — keep this image.**

```python
it = iter(range(2))          # ONE iterator, made once

for i in range(3):
    for j in it:             # looping over the ITERATOR, not the iterable
        print(i, j)
# 0 0
# 0 1
# (and then nothing)
```

The iterator is consumed on the first pass. Passes two and three find it already
at `StopIteration`, and the inner body never runs again — silently, with no
error.

**That is forward-only state made visible as a bug rather than as a
definition.**
Carry the broken loop, not the sentence.

---

### 5. Loop `else`

Loops can have an `else`. It has **nothing to do with the `else` of `if`** — do
not read it as "otherwise".

```python
for n in [1, 2, 3]:
    if n == 10:
        print("found")
        break
else:
    print("not found")
# not found
```

Change the list to `[1, 2, 10]` and it prints `found`.

**The rule:** the `else` block runs **if the loop finished without hitting
`break`**. Break out, and `else` is skipped.

**Where it earns its place:** search. It distinguishes "I searched the whole
thing and found nothing" from "I found it and stopped early" without a flag
variable.

> **The exercise that earns this:** write the same search *without* loop `else`,
> using only `for`, `if`, `break` and a variable. Once the found-flag pattern is
> written out by hand, the reason loop `else` exists becomes obvious.

---

### 6. Operators — the drill, worked

```python
17 // 4     # 4
17 % 4      # 1

-7 // 2     # -4
-7 % 2      # 1

2 ** 3 ** 2 # 512   — right-associative: 2 ** (3 ** 2) = 2 ** 9

a = [1, 2]
b = [1, 2]
a == b      # True   — compares VALUE
a is b      # False  — compares IDENTITY: id(a) == id(b)

5 > 3 > 1   # True

10 / 2      # 5.0   — / always returns float
```

**The modulo identity:**

```
a == b * (a // b) + (a % b)
```

Quotient × divisor, plus remainder, gives back the original. Worked through on
`-11 % 5`:

- `-11 / 5 = -2.2`
- `//` floors **toward −∞**, so `-2.2 → -3` (not `-2`, which is what truncation
 toward zero would give)
- `5 × (-3) + r = -11` → `-15 + r = -11` → **`r = 4`**

**Phrasing fix:** floor is not "the lowest number", it is **the largest integer
not greater than** the value. Sounds pedantic; it is the wording that keeps you
correct on negatives. For `-3.5`, "lowest" is ambiguous; "largest integer not
above `-3.5`" is unambiguously `-4`.

**Consequence worth carrying:** because `//` floors toward −∞, the remainder
always takes the **sign of the divisor**. `-11 % 5` is `4` (positive divisor);
`11 % -5` is `-4`.

**Chained comparison — the part beyond the rule.** `5 > 3 > 1` expands to
`5 > 3 and 3 > 1`. But in `f() > 3 > 1`, **`f()` is called exactly once.** The
middle operand is evaluated a single time and reused, which is why chaining is
not merely syntactic sugar for the `and` rewrite. Short-circuit still applies: if
`f() > 3` is False, `3 > 1` never runs.

---

## KEY MENTAL MODELS

1. **`for` asks; `while` checks.** One consumes items from an iterator; the
 other re-evaluates a condition.
2. **`break` kills the loop; `continue` kills the iteration.** Opposites, not
 variants.
3. **`continue` skips downward.** Anything below it in the body — including
 your state update — does not run.
4. **A fresh `for` gets a fresh iterator.** That is why inner loops restart and
 why a hoisted iterator silently breaks.
5. **Floor toward −∞, not toward zero.** The whole negative-`%` story falls out
 of this one fact.
6. **`print` converts, `+` refuses.** Two different policies on type mismatch.
7. **The condition guards entry, not the printed value.** Trace to the last
 cycle, always.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `print()` | Writes arguments to stdout after calling `str()` on each | Returns `None`, not the text |
| `sep` | Goes between printed items; default `" "` | People assume the space is in the strings |
| `end` | Goes after everything; default `"\n"` | It is `\n`, not `/n`; the last newline is invisible |
| `while` | Repeats while a condition stays true | Needs its own state update — nothing advances automatically |
| `break` | Exits the innermost loop entirely | Only one level; no `break 2` |
| `continue` | Ends this iteration, jumps to the condition check | Skips the state update below it → infinite `while` |
| Nested loop | Inner runs fully for each outer value | Cost multiplies; a hoisted iterator silently dies |
| Loop `else` | Runs if the loop ended without `break` | It is not "otherwise" — nothing to do with `if`/`else` |
| `//` | Floors toward −∞ | Not truncation: `-7 // 2` is `-4`, not `-3` |
| `%` | Remainder consistent with `//` | Sign follows the **divisor** |
| `**` | Exponentiation | Right-associative: `2**3**2` is `2**9` |
| `/` | True division | Always float, even `10 / 2 → 5.0` |
| `is` | Identity — `id(a) == id(b)` | Not "same value", not "same variable" |
| Chained comparison | `a > b > c` → `a > b and b > c` | Middle operand evaluated **once** |
| `NameError` | The name does not exist | Not the same as a bad value |
| `ValueError` | Right type, wrong value | Not the same as a missing name |
| `TypeError` | Operation undefined between these types | Python is not confused — it is refusing to guess |
| `StopIteration` | Signal that an iterator is spent | It is an **exception**, not a state |
| `traceback` | The crash report: where, which line, what path | Its **last** line names the exception |

---

## WHAT'S COMING NEXT — SESSION 17

1. **[RECALL] The exception family, cold, in mixed order.** `NameError` /
 `ValueError` / `TypeError`; exceptions-are-signals; `StopIteration`'s
 category; `traceback`. This is now the weakest cluster in the file and it
 opens the session.
2. **[RECALL] Iterator causation** — forward-only state. Via the broken nested
 loop, not the definition.
3. **[RECALL] The modulo identity in symbolic form.** Text mode. One clean cold
 statement promotes it.
4. **[RECALL] `if` / `elif` / `else` confirmation** — owed, and it gates the
 next item.
5. **Close 1.6:** the owed found-flag exercise · `pass` · ternary · common loop
 patterns (fold in the `while`+`continue` hang and trace-tail truncation) · the
 mutating-vs-non-mutating method drill.
6. **Then 1.7 — Functions.** Opened by cashing in function-scope, which is now
 `[x]`, and is already half the LEGB story.

**Standing:** the first monthly gauntlet is end of August, carrying the
strict-legend audit of every `[x]` in Layer 1. The re-baseline arithmetic is due
31 August.
