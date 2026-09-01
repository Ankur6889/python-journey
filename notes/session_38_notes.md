# SESSION 38 NOTES — Tuesday 1 September 2026, 14:29 → 21:20

**PURE REVISION, OLDEST-FIRST — your session, your request.**
No new curriculum material was opened. Twenty ledger rows were fired in age
order, from S14 material forward. **15 passes, 5 fails, 11 promotions, two
curriculum bullets moved.**

---

## SELF-TEST — do this first, notes closed

1. A 5-line file. Lines 1–3 are perfect and print things. Line 4 is missing a
   colon. What appears on screen when you run it?
2. `d = {"a": 1}`. What is `x` after `x = d.clear()`, and what is `d`?
3. Why can `x = d.pop("a")` be written but `x = del d["a"]` cannot?
4. `k = d.keys()`, then `d["c"] = 3`. What does `print(k)` show?
5. Name the error: `d[["a","b"]] = 1`. Name the error: `n = 5; n[0]`.
   Name the error: `a, b = [1, 2, 3]`. Give the rule that separates them.
6. `data = [3,1,2]`; `out = data.extend([7,8])`; `out` is `None`. You have never
   seen `extend`. What do you now know about `data`, and how?
7. Does the tell run the other way — does every mutating method return `None`?
8. `pairs = zip(a, b)` where `a` has 3 items and `b` has 2. Name **both** ways
   this fails without raising anything.
9. Trace it: `outer()` sets `n = 1`, calls `inner()` which sets `n = 99`, then
   returns `n`. What prints, and what does the module namespace hold?
10. What does `list(reversed(x))` return that `reversed(x)` does not?

Answers throughout. Rate yourself **before** you look, and spread the numbers.

---

## 1. FULL TEACHING

### 1.1 Compile time vs run time

Python does not execute your file line by line from disk. It runs in two phases:

```
SOURCE  ──compile──▶  BYTECODE  ──execute──▶  OUTPUT
```

A `SyntaxError` is raised in the **first** phase. If the compile fails, no
bytecode is produced, so **nothing executes at all** — including lines that are
perfectly correct and appear before the broken one.

```python
print("starting")
x = 5
print(x * 2)
if x > 3
    print("big")
```
```
  File "run.py", line 4
    if x > 3
            ^
SyntaxError: expected ':'
```

**No `starting`. No `10`.** Contrast with a runtime error, where everything
above the failing line has already run and printed.

**The diagnostic question to carry:** *how far did Python get?* If the answer is
"nowhere", it is a syntax problem. If output appeared first, it is a runtime
problem, and the last line printed tells you where to look.

### 1.2 Frames and namespaces

Every function **call** creates a **frame**. The frame holds that call's local
namespace and dies when the call returns.

```python
def outer():
    n = 1
    inner()
    return n

def inner():
    n = 99

print(outer())
print(sorted(globals().keys()))
```
```
1
[..., 'inner', 'outer']
```

`inner`'s `n = 99` lands in `inner`'s own namespace and disappears with its
frame. `outer`'s `n` was never touched.

**Two precision points from your answer:**

- **The module namespace is not empty.** `def` **binds a name**. By the time
  `print(outer())` runs, the module namespace already holds `outer` and `inner`
  — and that is *how `inner()` is found at all*. The call fails to find `inner`
  locally, walks out to the module namespace, and finds it there. An empty
  module namespace would give `NameError`.
- **A frame's death destroys the BINDING, not the object.** The object is
  destroyed only if nothing else refers to it. With `99` nothing else did, so
  you were right by accident rather than by rule.

### 1.3 The mutating tell — and the order it runs in

**Step 1: the TYPE.** Immutable type ⇒ mutation is impossible ⇒ any method that
appears to change it must be returning a **new object**.

```python
s = "abc"
out = s.upper()
print(repr(out), repr(s))     # 'ABC' 'abc'
```

**Step 2: the RETURN VALUE, as a one-directional hint.**

```python
data = [3, 1, 2]
out = data.extend([7, 8])
print(out)                    # None
```

`None` back ⇒ the method did its work **in place**, because returning `None` has
no other purpose. **You can infer that about a method you have never seen.**

**The direction that does NOT hold:**

```python
nums = [3, 1, 2]
out = nums.pop()
print(out, nums)              # 2 [3, 1]
```

`pop` mutates **and** returns. So:

| Direction | Holds? |
|---|---|
| returns `None` ⇒ it mutated | **Yes** |
| mutates ⇒ returns `None` | **No** — `pop` is the counterexample |

### 1.4 `del` is a STATEMENT

`del` is a statement, like `return` or `if`. Not a function, not a method —
hence no parentheses. **It removes a binding, not an object.**

```python
d = {"a": 1, "b": 2}
del d["a"]
print(d)                      # {'b': 2}

n = 5
del n
print(n)                      # NameError: name 'n' is not defined
```

`del n` did not destroy `5`. It removed the **name** from the namespace — which
is why the failure is a `NameError`: the NAME is what broke.

**Why it cannot be assigned from:**

```python
x = del d["a"]
```
```
  File "d1.py", line 2
    x = del d["a"]
        ^^^
SyntaxError: invalid syntax
```

- **`d.pop("a")` is an EXPRESSION** — it evaluates to a value, so it can go
  anywhere a value can go.
- **`del d["a"]` is a STATEMENT** — it does not evaluate to anything at all.
  There is nothing for `=` to take.

**Your own line for this was the sharpest of the session:** *"del does not
return anything, and by nothing I don't mean None."* Exactly right — "nothing"
and `None` are different things.

`pop` gives you the value back; `del` does not. That is the whole choice.

### 1.5 The error-label discriminator (1.9's last bullet, now open)

Not a roster to memorise. One rule, three outcomes:

| Error | The rule | Example |
|---|---|---|
| **`TypeError`** | Wrong **type**. The operation is impossible for this kind of thing. | `d[["a","b"]] = 1` → `unhashable type: 'list'`; `n = 5; n[0]` → `'int' object is not subscriptable` |
| **`ValueError`** | **Right type, wrong value.** | `a, b = [1,2,3]` → `too many values to unpack (expected 2)`; `int("abc")` |
| **`IndexError`** | Type indexes fine; **this index** doesn't exist. | `[1,2][5]` → `list index out of range` |
| **`NameError`** | The **name** broke — nothing is bound to it. | `del n; print(n)` |
| **`SyntaxError`** | Compile time. **Nothing runs.** | missing `:` |

**Two traps you hit, both worth re-reading:**

- **`ValueError` is not "a value that can't be converted".** That is one
  instance. The definition is *right type, wrong value* — and the **number of
  items in a list is a property of the value, not the type**, which is exactly
  why unpacking mismatches raise `ValueError` and not `TypeError`.
- **Decode `subscriptable`.** A **subscript** is the `[...]` notation. *"Not
  subscriptable"* = you cannot put a subscript on this thing at all. That is a
  statement about the TYPE, so the error is a `TypeError`.

**Hashability:** dict keys must be hashable; mutable objects are not; so a
`list` can never be a key **whatever it contains** — a fact about the type,
hence `TypeError`. Swap to a tuple and it works: `d[("a","b")] = 1`.

### 1.6 Lazy objects: snapshot vs live

Three things in this session were **not** the list they looked like.

```python
print(reversed([1, 2, 3]))            # <list_reverseiterator object at 0x...>
print(list(reversed([1, 2, 3])))      # [3, 2, 1]
```

**`reversed()` returns an ITERATOR.** `list()` is what forces it into a real
list — a **snapshot**.

```python
names, frames = ["a","b","c"], [10, 20]
pairs = zip(names, frames)

for n, f in pairs: print("first :", n, f)   # a 10 / b 20
for n, f in pairs: print("second:", n, f)   # nothing at all
```

**`zip` fails silently twice:** (1) it truncates to the shorter input and never
complains — `"c"` is dropped; (2) it is an iterator, so once consumed it is
**exhausted** and a second pass yields nothing. Your words: *"forward only
state, once consumed need to be recreated."*

**And the one that got you:**

```python
d = {"a": 1, "b": 2}
k = d.keys()
d["c"] = 3
print(k)                 # dict_keys(['a', 'b', 'c'])   <- LIVE

l = list(d.keys())
d["e"] = 4
print(l)                 # ['a', 'b', 'c']              <- FROZEN
```

**`.keys()` returns a VIEW — a live window onto the dict, not a copy of its
keys.** It reads `d` at the moment you look at it. `list()` takes the
photograph.

**Same pattern, three times, one session.** You applied it correctly twice and
missed the third. The pattern is: *does this object hold the data, or does it
look at the data?* If it looks, wrap it in `list()` to freeze it.

### 1.7 Sorting with a rule you supply

```python
records = [{"id":3,"frames":120}, {"id":1,"frames":90}, {"id":2,"frames":300}]
list(reversed(sorted(records, key=lambda x: x["frames"])))
# [{'id': 2, 'frames': 300}, {'id': 3, 'frames': 120}, {'id': 1, 'frames': 90}]
# records itself: unchanged
```

`sorted` returns a **new list** and leaves the input alone; `.sort()` mutates
and returns `None`. `key=` takes a function called once per item to produce the
value actually compared. **Cheaper alternative for the same result:**
`sorted(records, key=..., reverse=True)`.

### 1.8 Dead code

Your own drill:

```python
count = 0
if gap != 0:            # <- can never change the outcome
    gap = abs(gap)
    while gap > 0:
        gap = gap // 2
        count += 1
return count
```

The guard tests what the loop header already tests. **Dead code** = present,
reachable-looking, and incapable of affecting the result. Your account of its
origin was exactly right: a guard written for an older spec and left behind when
the spec changed. The harmful version is still in your validator — three
`except TypeError:` blocks that a short-circuiting `or` guarantees can never run.

---

## 2. THE DRILL

`drills/s38_while.py`, **20/20 green on first submission, cold.**

```python
def backoff_steps(gap):
    count = 0
    if gap != 0:
        gap = abs(gap)
        while gap > 0:
            gap = gap // 2
            count += 1
    return count

def first_bad(rows):
    number_of_rows = len(rows)
    row_index = 0
    while row_index < number_of_rows:
        column_index = 0
        number_of_columns = len(rows[row_index])
        while column_index < number_of_columns:
            if rows[row_index][column_index] < 0:
                return row_index, column_index
            column_index = column_index + 1
        row_index = row_index + 1
```

**What it demonstrated:** a `while` with an unknown trip count; a nested `while`;
an early `return` as the exit (no found-flag needed, which is the better
structure); `len()` recomputed per row rather than assumed rectangular; and
`first_bad` falling off the end so the function returns `None` implicitly for
the no-negative case — correct, and the tests checked it with `is None`.

**Your done-line, written as file comments, contained a real failure case:**
*"lets say the user enters something else apart from int, then this will fail."*
True — `backoff_steps("8")` raises on `abs()`. That is the case-half the rule
asks for, not a scope report. Keep doing it that way.

---

## 3. THINKING GAPS THIS SESSION (with error-type classification)

| # | Gap | Type | Note |
|---|---|---|---|
| 1 | **`del` — no recall at all** | **Knowledge gap**, declared honestly | You said "I don't remember, let's revise that". Correct procedure — recall first, notes second, "gap" where empty. Re-taught; your teach-back was excellent. |
| 2 | **`TypeError` label on unhashable** | **Label gap on an intact mechanism** | You derived mutable ⇒ unhashable ⇒ not a key completely unaided, then could not name the error. The machinery was never the problem. |
| 3 | **`subscriptable` → said `IndexError`** | **Label gap + failure to reuse a discriminator you had just used** | Sixty seconds earlier you separated type-problems from value-problems correctly on the dict key. Same rule, not applied. |
| 4 | **Unpacking → talked yourself out of `ValueError`** | **Structural flaw: a too-narrow definition overrode a correct mechanism** | You had the count mismatch exactly right. The faulty definition of `ValueError` beat your own correct reasoning. Same shape as this morning's short-circuit: right mechanism, wrong model. |
| 5 | **`.keys()` as a view** | **Transfer failure — a missing INDEX, not a missing fact** | You applied lazy-vs-snapshot correctly twice in the same hour and did not recognise the third instance. This is the most important finding of the session. |
| 6 | **Confidence: seven consecutive 7s** | **Calibration flaw** | Then over-corrected: 6 and 5 on two correct answers. A rating that never moves aims nothing; a rating that under-reads sends the queue chasing things you have. |

**What did NOT go wrong, and should be read as evidence:** nine mechanisms were
produced cold and unaided on material 8 to 24 days old, including a complete
frames trace, both halves of the mutating tell, the compile/run split, and the
lazy-iterator model three separate times.

---

## 4. TEACHING MISTAKES THIS SESSION

1. **The drill spec was unclear and read as recursion — pushback 70, upheld in
   full.** "A control cycle that closes HALF the remaining gap" was jargon
   wrapped around a self-referential-sounding process. Rewritten to plain
   steps with two worked traces, plus an honest statement of what was being
   measured. You passed 20/20 immediately afterwards. **SPEC BEFORE PUZZLE
   breached and repaired inside one turn.**
2. **The `.keys()` snippet was run before your rating was taken.** The binding
   rule is that the rating comes after your answer and **before** the verdict —
   and executing the code in view is part of the verdict. Self-caught,
   disclosed, no rating logged.
3. **STATE.md carried a false alarm into the session.** The previous session's
   header said the working tree was red with three unclosed `try:` blocks and
   made fixing it the first action. It was wrong — `HEAD` was green and ran
   27/27 immediately. Your file had been repaired at 05:32, three minutes
   before the ruling that was recorded. **New standing check: verify a STATE
   warning against the repo before acting on it.**

---

## 5. REFERENCE CHECKLIST — name, what it does, the trap

| Item | What it does | The trap |
|---|---|---|
| **`SyntaxError`** | Raised at COMPILE time | **Nothing runs at all** — not even correct lines above it |
| **frame** | Created per CALL; holds that call's locals; dies on return | Its death kills the **binding**, not the object |
| **module namespace** | Holds top-level names, including every `def` | It is never empty — that is how nested calls find each other |
| **the tell** | Returns `None` ⇒ it mutated | **One-directional.** `pop` mutates and returns a value |
| **the type check** | Immutable ⇒ mutation impossible ⇒ new object returned | Run this **first**, before looking at the return value |
| **`del`** | STATEMENT. Removes a binding | Cannot sit right of `=` — it evaluates to nothing (≠ `None`) |
| **`TypeError`** | Wrong type for the operation | Covers `unhashable` and `not subscriptable` |
| **`ValueError`** | Right type, wrong value | **Includes unpacking count mismatches** — item count is a property of the value |
| **`IndexError`** | This index doesn't exist | Only on types that support indexing at all |
| **`NameError`** | Nothing is bound to that name | What `del n` then `print(n)` gives you |
| **`reversed()`** | Built-in returning an **iterator**; reverses, does not order | Print it and you get an object; `list()` it to see values |
| **`zip()`** | Pairs positionally, lazily | **Two silent failures**: truncates to the shortest, and exhausts after one pass |
| **`.keys()`** | Returns a **live view** of the dict | Not a snapshot. `list(d.keys())` is the snapshot |
| **`sorted` vs `.sort()`** | New list vs in-place | `.sort()` returns `None` |
| **`key=`** | A function called once per item to produce the compared value | Not a comparison function |
| **dead code** | Present, reachable-looking, cannot affect the result | Usually a guard left behind when the spec changed |

---

## 6. WHAT'S COMING NEXT

- **S39 is the August gauntlet if a real day has passed** — strict-legend audit
  of every `[x]`, and the re-baseline arithmetic against 30 Sep.
- **Due 2 Sep, all from today's misses:** `del`, `hashable`, `subscriptable`,
  unpacking, `.keys()` as a view — plus `short-circuit`, held over from S37.
- **`.keys()` closes the 1.8 `dict` bullet on one cold ask.** It is the cheapest
  tick on the board and has been for three sessions.
- **Then 1.10 — modules, packages and imports.** That is the first of the three
  units standing between you and reading LeRobot; the other two are 1.12 (OOP)
  and 1.13 (dunders and decorators). **A scheduling decision is owed from you at
  the open:** once 1.10 lands, should the weekly cold build block point at a
  real LeRobot file instead of a synthetic task?
