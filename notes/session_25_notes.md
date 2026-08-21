# Session 25 — Friday 21 Aug 2026
## The recall block: eleven promotions, one demotion, four hooks

---

## SELF-TEST FIRST (close these notes, answer cold, then read on)

1. What makes a function a closure? Nesting is not the answer.
2. A `for` loop walks a list. What does it call to start, what does it call for
   each item, and what stops it?
3. `def f(): x = 1; """hi"""; return x` — what is `f.__doc__`, and why?
4. Name the five checks. Then say what `ek` and `bahar` actually mean.
5. `nums.sort()` and `sorted(nums)` — what does each evaluate to, and what
   happens to `nums`?
6. A method returns `None`. What follows? Does the rule run backwards?
7. `pass`, `continue`, `break` — three different jobs. State each.
8. When does a loop's `else` run?
9. `2 ** 3 ** 2` is 512, not 64. Which concept decides that?
10. What does `list(some_iterator)` do to the iterator?

---

## FULL TEACHING

### 1. Closures — what actually makes one

A **closure** is a function object that **binds a free variable from its
enclosing scope into a cell**, so the value survives after the enclosing frame
has died.

A **free variable** is a name the inner function *uses* but does not define
itself and did not receive as a parameter.

**Nesting is necessary but not sufficient.** Proof:

```python
def outer():                     def outer2():
    def inner():                     limit = 90
        return 5                     def inner2():
    return inner                         return limit
                                     return inner2

print(outer().__closure__)       print(outer2().__closure__)
```
```
None
(<cell at 0x7862...: int object at 0xb37bc8>,)
```

Same nesting, different result. `inner` captures nothing, so there is nothing
to store and `__closure__` is `None`. `inner2` uses `limit`, so Python creates
**one cell per free variable** and hangs the tuple of cells on the function
object.

**The four layers, in order:**

| Layer | What it is |
|---|---|
| `inner2` | a **name** |
| the object it points at | a **function object** |
| `inner2.__closure__` | a **tuple** — one entry per free variable |
| each entry | a **cell** — a one-slot box (a TYPE, not a label) |
| `cell.cell_contents` | the **value** inside that box |

The trap that cost two sessions: `cell_contents` is **not** the tuple.
`__closure__` is the tuple; `cell_contents` is what one cell holds.

### 2. The iteration protocol

Three moving parts, and a `for` loop is built out of them:

1. `iter(iterable)` — called **once**, at the top. Hands back an **iterator**.
2. `next(iterator)` — called **once per pass**. Hands back the next item.
3. `StopIteration` — the **exception** `next()` raises when there is nothing
   left. The `for` loop catches it and exits quietly.

```python
box = iter([1, 2])
print(next(box))
print(next(box))
print(next(box))
```
```
1
2
Traceback (most recent call last):
  File "si.py", line 4, in <module>
    print(next(box))
          ^^^^^^^^^
StopIteration
```

**Iterable vs iterator:** the iterable is reusable and hands out iterators; the
iterator is forward-only and gets consumed. Its *position* is what runs off the
end — the iterable still holds everything.

**`list()` on a partially consumed iterator drains what is LEFT**, not the whole
original:

```python
val = iter([10, 20, 30, 40])
next(val)              # position moves past 10
print(list(val))       # [20, 30, 40]
```

### 3. Docstrings — position, not quotes

```python
def alpha():            def beta():
    """first"""             x = 1
    return 1                """second"""
                            return x

print(alpha.__doc__)    print(beta.__doc__)
```
```
first                   None
```

**Triple quotes do not make a docstring. POSITION does** — the first statement
of the body. Anywhere else the string is an **expression statement**: evaluated,
result discarded.

⚠ **Precision that cost a mark:** `beta` does **not** lack the attribute.
`beta.__doc__` exists and holds `None`.

```python
print("__doc__" in dir(beta))   # True
```

"The attribute is missing" would raise `AttributeError`. "The attribute is
`None`" returns a value. Different claims.

**A comment is not the same thing.** A comment is deleted by the tokenizer and
never becomes anything. A bare value — `5` on its own line, or a misplaced
string — is an expression Python evaluates and throws away.

### 4. The five checks

> **"Boundary pe khaali ek bahar mila"**

| Hook | Check | What it means |
|---|---|---|
| **Boundary** | the exact value where branches meet | Any `<`, `<=`, `>`, `>=` has one value sitting on the line. Test **that** one, not values near it. |
| **Khaali** | empty / zero / nothing | `0`, `""`, `[]`, `None`. |
| **Ek** | **exactly ONE** | Smallest non-empty case. A loop that runs once takes a different path. **Not "small inputs".** |
| **Bahar** | outside what you silently assumed | Negative when you assumed non-negative; **float when you assumed int**. Noticing the assumption is the skill. |
| **Mila** | does the code match its promise? | Read the docstring one sentence at a time: *"iske peeche kaunsi line hai?"* No line behind a sentence ⇒ bug. |

`mila` also rules things **not** bugs: `take_last([])` raising was fine, because
the spec said the list may be assumed non-empty.

### 5. `sort` vs `sorted`, and the tell

```python
nums = [3, 1, 2]              more = [3, 1, 2]
a = nums.sort()               b = sorted(more)
print(a)      # None          print(b)      # [1, 2, 3]
print(nums)   # [1, 2, 3]     print(more)   # [3, 1, 2]
```

**The tell is ONE-DIRECTIONAL:**

- returns `None` ⇒ mutating ✅
- mutating ⇒ returns `None` ❌ — **`pop` mutates and returns the removed item**

**TYPE FIRST, always.** Immutable type ⇒ mutation is not even possible ⇒ the
return-value question never arises. The return value is the *second* filter.

### 6. `pass` / `continue` / `break`

A block cannot be empty:

```python
for n in [1, 2]:
print(n)
```
```
IndentationError: expected an indented block after 'for' statement on line 1
```

Same loop, one word changed:

```python
for n in [1, 2, 3]:        for n in [1, 2, 3]:        for n in [1, 2, 3]:
    if n == 2:                 if n == 2:                 if n == 2:
        pass                       continue                   break
    print(n)                   print(n)                   print(n)
```
```
1                          1                          1
2                          3
3
```

- **`pass`** does nothing; execution carries on to the next line. Not a loop
  keyword at all — a placeholder that satisfies "this block needs a statement."
- **`continue`** ends **this iteration**; jumps back for the next item.
- **`break`** ends **the whole loop**.

> **HOOK: `pass` = jagah bharo. `continue` = agla chakkar. `break` = bahar niklo.**

⚠ **Why this one needs a hook: the name decodes to the WRONG keyword.** "pass"
sounds like "skip it" — but skipping is `continue`'s job.

### 7. Loop `else`

```python
for n in [1, 3, 5]:              for n in [1, 4, 5]:
    if n % 2 == 0:                   if n % 2 == 0:
        break                            break
else:                            else:
    print("no even number")          print("no even number")
```
```
no even number                   (nothing)
```

**Runs only if the loop finished WITHOUT hitting `break`.** Unrelated to the
`if`/`else` you know — that `else` means "the condition was false"; this one
means "we never broke out."

> **HOOK: read the keyword as `nobreak`. Break nahi hua, tabhi else chalega.**

Empty iterable ⇒ body never runs ⇒ `break` never encountered ⇒ **`else` runs.**

### 8. The ternary (conditional expression)

```python
angle = 120
label = "out of range" if angle > 90 else "ok"      # EXPRESSION form
```

It exists for **placement**, not brevity — it **evaluates to a value**, so it
goes anywhere a value goes. A four-line `if` block cannot:

```python
print("angle is " + ("high" if angle > 90 else "low"))   # angle is high
```

**Reading order is the trap.** Three beats:

> **`A if C else B`** → **"A — agar C sach hai — warna B."** The **middle** is
> the condition; the value you want comes **first**.

> **HOOK: `ternary` = `ter-` = THREE.** Binary takes two operands; this takes
> three — value, condition, value.

### 9. Associativity

```python
print(10 - 3 - 2)      # 5     = (10 - 3) - 2      LEFT to right
print(2 ** 3 ** 2)     # 512   = 2 ** (3 ** 2)     RIGHT to left
```

Both lines have two operators of **equal rank**, so precedence cannot decide.
**Associativity is the direction that breaks the tie.**

> **Precedence = kaun pehle (rank, between DIFFERENT operators).**
> **Associativity = barabari pe kis taraf se (direction, SAME rank).**
> **HOOK: sab left se, sirf `**` right se.**

`associate` = to group with. Associativity answers *"this operand groups with
which side?"*

---

## THE DRILLS

### `drills/s25_closure.py` — 10/10, unaided

Four forcing constraints: the tool takes exactly one argument; no `global`;
`make_clamp` has returned before the tool is used; two clamps coexist.

```python
def make_clamp(limit):
    def impose_limit(given_value):
        if abs(given_value) > limit:
            if given_value < 0:
                return -limit
            else:
                return limit
        return given_value
    return impose_limit


def clamp_all(angles, limit):
    imposed_limit = make_clamp(limit)
    clamped_angles = angles[:]
    for i in range(len(clamped_angles)):
        clamped_angles[i] = imposed_limit(clamped_angles[i])
    return clamped_angles
```

Two things done right without prompting: `abs(...) > limit` collapses both
directions into one test, and `>` rather than `>=` means the boundary case
`shoulder(90) == 90` passes.

### `drills/s25_iteration.py` — 7/7, `list()` from notes

`for`, `while`, indexing, slicing, `.pop()`, `.remove()`, `.index()` and
`enumerate` all banned, with the ban enforced by a test that reads the source.
That leaves exactly one route.

```python
def first_two(items):
    val = iter(items)
    f_t = []
    f_t.append(next(val))
    f_t.append(next(val))
    return f_t


def drop_first(items):
    val = iter(items)
    next(val)
    remaining = list(val)
    return remaining
```

---

## THINKING GAPS THIS SESSION

| # | Gap | Error type | Note |
|---|---|---|---|
| 1 | A misplaced string literal called "a comment" | **Knowledge gap** | Repaired completely on one probe. Comments are removed by the tokenizer; a bare value is an expression evaluated and discarded. |
| 2 | One-directional tell given without the counterexample | **Lazy thinking / depth-before-answer** | `pop` came instantly on the re-ask. |
| 3 | `print()` — `sep` and `end` given, return value skipped | **Lazy thinking / depth-before-answer** | `None` on the re-ask. |
| 4 | `associativity` — flat "gap" | **Knowledge gap (system-caused)** | Ticked `[x]` in S16 bundled with precedence and never asked alone. **Demoted.** |
| 5 | `pass` mechanism — flat "gap" | **Knowledge gap** | Declared honestly, not guessed. Re-taught with a hook. |
| 6 | "no docstring attribute" | **Structural flaw (language precision)** | The attribute exists holding `None`; missing would raise `AttributeError`. |
| 7 | Closure opened as "a function inside a function" | **Knowledge gap** | Corrected in one [PREDICT]: capture, not nesting. |

**THE PATTERN, AND IT IS THE HEADLINE:** items 1, 2 and 3 all recovered
**in a single line** on a re-ask. Across S24–S25 the re-ask has worked six times
out of six. **The knowledge is present; the probing pass is skipped.**
**Intervention: re-ask, do not re-teach.**

---

## TEACHING MISTAKES THIS SESSION

1. **The `clamp_all` spec was unintelligible — and this is the second
   consecutive session.** "Oldest order preserved" (meaningless here, copied
   from a time-ordered drill), "a NEW list of the same angles, each pulled
   inside the limit" (self-contradictory), and four requirements in one
   sentence. **Fixed by rewriting as lettered sub-requirements — now a standing
   format rule for every drill spec.**
2. **`list()` was defined in S15 and never entered in the re-test queue** —
   nine sessions with the system never once asking for it. Any term defined
   mid-session goes into the queue **that same session**.
3. **A list comprehension and a bool-as-index trick reached the first draft of
   the ternary demo**, neither taught. Caught before delivery; should not have
   been drafted.
4. **The parked "[RECALL] budget" rule was offered a third time** against
   STATE.md's own "do not nag a third time". Dropped, record closed.

---

## REFERENCE CHECKLIST

| Name | What it does | The trap |
|---|---|---|
| closure | function object binding a free variable into a cell | **Nesting alone is not enough** — no capture ⇒ `__closure__` is `None` |
| free variable | name used, not defined locally, not a parameter | The thing that *triggers* the closure |
| cell | a TYPE — one-slot box | `cell_contents` is the value; **`__closure__` is the tuple** |
| `iter()` | called **once**, returns an iterator | Not once per item |
| `next()` | called **once per pass** | Advances position permanently |
| `StopIteration` | exception raised when exhausted | It is an **exception**, not a return value |
| `list(it)` | drains an iterator into a new list | On a **partly consumed** iterator you get only what's LEFT |
| docstring | first statement of the body | **Position makes it, not the quotes**; elsewhere ⇒ `__doc__` is `None` |
| `__doc__` | attribute holding the docstring | **Always exists**; absent docstring ⇒ `None`, not `AttributeError` |
| `sort()` | mutates in place | returns **`None`** |
| `sorted()` | builds a **new** list | leaves the original alone |
| the tell | returns `None` ⇒ mutating | **One-directional** — `pop` mutates and returns a value |
| `pass` | no-op placeholder | Name suggests "skip" — **that is `continue`** |
| `continue` | ends **this iteration** | Not the whole loop |
| `break` | ends the **whole loop** | Also suppresses loop `else` |
| loop `else` | runs if no `break` happened | **Nothing to do with `if`/`else`**; read it as `nobreak` |
| ternary | `A if C else B`, an **expression** | Middle is the condition; value comes first |
| precedence | rank between **different** operators | Cannot break ties |
| associativity | direction on the **same** rank | **`**` is right-to-left**; everything else left-to-right |
| five checks | boundary / khaali / ek / bahar / mila | `ek` = exactly ONE; `bahar` covers **type** as well as sign |

---

## WHAT'S COMING NEXT (Session 26)

- **Opens on 1.8 content at his explicit instruction — no recall block first.**
  tuple → dict → set → when-to-use-which.
- **Comprehensions are unblocked** — the iteration protocol reached `[x]`.
  Declare the gate open out loud; it was declared shut in S24.
- **Later in the session:** cold tests on the four hooked items — `pass`,
  loop `else`, ternary, associativity (**alone, never bundled**). Plus `list()`,
  queued for the first time.
- Still owed inside 1.8: `zip`, f-strings, nested structures, `reversed()`, and
  the shallow-copy point — a slice copies the **references**.
- **Saturday 22 Aug: cold build block**, ≥90 min, timed, no AI, git + pytest.
  His own chosen task — the multi-joint clamp with `*args`/`**kwargs`. Unanswered
  by design: how do positional angles pair with named limits?
