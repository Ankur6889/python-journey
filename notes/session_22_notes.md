# SESSION 22 NOTES — Mon 17 Aug 2026
**Topics: the deferred recall queue paid (six promotions) · first repo drills · lambdas · docstrings · 1.7 CLOSED**

---

## SELF-TEST FIRST (do this cold, before reading on)

1. `climb(3)` where the body is `if n == 0: return` / `climb(n-1)` / `print(n)` — output, and WHY, frame by frame?
2. Two calls `a = make_counter(10)` and `b = make_counter(10)` — is `a is b` True? Do they share a cell?
3. State the closure definition in one interview line. (You failed this today — the exact line is below.)
4. What is ONE line of a traceback?
5. Delete `global count` from a function that does `count = count + 1` — what error, and what decides it, WHEN?
6. In a signature, `*args` does what? In a call, `*nums` does what? What do the collectors hold when nothing is left over?
7. Which attribute holds default parameter values, built when, living where, of what type?
8. Why can't a `for` loop restart a hoisted iterator on its second pass?
9. What is a lambda, in one line? What is its body allowed to contain?
10. Where must a docstring sit, which attribute stores it, and what is `f.__doc__` when there is no docstring?

---

## FULL TEACHING

### 1. Post-order recursion — the transfer question (PROMOTED 10/10)

```python
def climb(n):
    if n == 0:
        return
    climb(n - 1)
    print(n)

climb(3)
```
Output:
```
1
2
3
```
Four frames — `climb(3)`, `climb(2)`, `climb(1)`, `climb(0)` — each holding
ITS OWN `n`. The deepest returns first; each caller resumes AFTER its call
line, so the prints run on the unwind: 1, 2, 3. **There is no single mutating
`n`.** (S20's failure; today's clean trace.)

**Labels (decoded today, were a gap): PRE-order = work before the call
(`3 2 1`), POST-order = work after the call (`1 2 3`).**

### 2. Cells — causation, the same-argument case, and the locality trap

```python
def make_counter(start):
    def bump():
        return start + 1
    return bump

a = make_counter(10)
b = make_counter(10)    # same argument value!
print(a is b)                                  # False
print(a.__closure__[0] is b.__closure__[0])    # False
```
**Sharing comes from the same CALL, never from equal values.** Every call to
the factory mints a fresh function object with a fresh cell.

**The trap you remembered — and missed again, then repaired unaided:**
```python
def make_counter(start):
    def bump():
        start = start + 1     # assignment!
        return start
    return bump

c = make_counter(10)
print(c())    # UnboundLocalError
```
Assignment anywhere in the body → `start` classified LOCAL at `def`-compile
time → NOT a free variable → **no cell, the closure never forms** → the read
hits an unbound local. **The error is `UnboundLocalError`** — capital L; the
name IS local, no value bound yet.

### 3. The closure definition — FAILED today (5/10); the line to own

> **A closure is a function object that binds a free variable from its
> enclosing scope into a cell, so the value survives after the enclosing
> function's frame has died.**

The four layers, outside-in (*shelf par naam, dabbe ke andar attribute*):

| Layer | What it is |
|---|---|
| `add5` | NAME on the shelf (module namespace) → points at the function object |
| `add5.__closure__` | attribute INSIDE the function object — a **tuple** |
| `add5.__closure__[0]` | the first **cell** (one per free variable) |
| `.cell_contents` | the **value** inside the cell |

```python
print(add5.__closure__)                     # (<cell at 0x...: int object at 0x...>,)
print(add5.__closure__[0])                  # <cell at 0x...: int object at 0x...>
print(add5.__closure__[0].cell_contents)    # 5
```
Missing today: the SURVIVAL clause (the whole point) — and the layers were
muddled twice. `__closure__` is `None` (not `()`) when there are no free
variables. Binding happens WHEN `def` RUNS.

### 4. Traceback — one line = one live frame

**Each line of a traceback is one live frame on the call stack, frozen at the
line it was executing when the crash happened.** Bottom frame: the raise
point. Every frame above: frozen at its CALL to the next function down —
"who called whom", nothing "problematic" about those lines. In an
`a() → b() → c()` chain, `a`'s line is its call to `b`.

### 5. `global` — earned through drills/s22_counter.py (3/3 pytest, PROMOTED 10/10)

```python
count = 0

def tick():
    global count
    count = count + 1
    return count

def reset():
    global count
    count = 0
```
Without `global`: assignment → compile-time LOCAL classification → LEGB never
runs for that name → `UnboundLocalError`. **Read: free. Mutate: free.
Rebind: needs `global`.**

### 6. `*args` / `**kwargs` — earned through drills/s22_report.py (4/4, PROMOTED 8/10)

```python
def report(*args, **kwargs):
    return args, kwargs

report(1, 2, x=3)   # ((1, 2), {'x': 3})
report()            # ((), {})  ← empty containers, NEVER None
```
**The mirror: signature side COLLECTS many into one; call side UNPACKS one
into many** — `report(*nums)` spreads a list into separate positional
ARGUMENTS (not "variables").

### 7. `__defaults__` — produced cold at last (PROMOTED 7/10)

```python
def greet(name="world"):
    return "hello " + name

print(greet.__defaults__)    # ('world',)  ← a TUPLE
```
Built when `def` runs; lives as an attribute on the function OBJECT,
permanently. (The local namespace is call-time and momentary.)

### 8. Iterator causation — first later-day pass (PROMOTED 5/10, short gap)

```python
it = iter(range(2))
for round_num in range(3):
    for x in it:
        print(round_num, x)
# 0 0 / 0 1 — rounds 1 and 2 print nothing
```
`it` is an ITERATOR (the iterable was `range(2)`). It holds **forward-only
state** — a position that only ever moves forward — and all three rounds ask
the SAME iterator. By round 1 the position is past the end, permanently.
NOT "because it gives one item at a time." It holds a position, not a list.

### 9. LAMBDAS — new material

**A lambda is the EXPRESSION form of a function**: it evaluates to a function
object where it stands, no name, no statement.

```python
double = lambda x: x * 2
print(double(4))     # 8
print(double)        # <function <lambda> at 0x...>

mul = lambda x, y: x * y      # parameter list works like a def's
print(mul(3, 4))     # 12
```
Hard limits: body = ONE expression (no `=`, no blocks); its value is
auto-returned (no `return` allowed). Label: Greek λ — brute-force, does not
decode.

**Where it earns its keep — a function demanded as an argument:**
```python
robots = ["ur12e", "Panda", "kinova"]
print(sorted(robots))                          # ['Panda', 'kinova', 'ur12e']
print(sorted(robots, key=lambda s: s.lower())) # ['kinova', 'Panda', 'ur12e']
```
`key=` (re-taught from S19): `sorted` calls it once per element with ONE
argument, sorts by the RESULTS, returns the ORIGINAL items.

```python
nums = [-3, 7, -1, 4]
print(sorted(nums, key=lambda n: n * n))   # [-1, -3, 4, 7]
```

**Lambdas close over variables exactly like `def`:**
```python
def make_adder(k):
    return lambda n: n + k

add5 = make_adder(5)
print(add5(10))                              # 15
print(add5.__closure__[0].cell_contents)     # 5
```

### 10. DOCSTRINGS — new material

A string literal as the **first statement** of a body → stored on the
function object as **`__doc__`** at `def` time. Third member of the def-time
attribute family: `__defaults__`, `__closure__`, `__doc__`.

```python
def clamp(n, limit):
    """Return n capped to the range -limit ... +limit."""
    if n > limit:
        return limit
    if n < -limit:
        return -limit
    return n

print(clamp.__doc__)   # Return n capped to the range -limit ... +limit.
```
A `#` comment is discarded before the code runs; a docstring is **data on the
object** — `help()`, editor tooltips, doc tools all read it. Convention:
triple quotes, imperative ("Return...", not "This function returns...").

**The absence discriminator (from today's miss):**
```python
def f():
    pass
print(f.__doc__)   # None  — not ""
```
Collectors give back **empty containers** (`()`, `{}`) — the thing exists,
empty. Optional attributes give back **`None`** — never created. `""` would
mean "documented as blank", a different claim.

---

## THINKING GAPS THIS SESSION

1. **Layer-muddle on closure storage (Knowledge gap — NEW, fired twice).**
   `cell_contents` called a tuple in the definition attempt; `__closure__`
   predicted to print `5` in the lambda block. Repaired via the four-layer
   shelf/dabba walk; watch in the S23 cold re-test.
2. **Label losses against won mechanisms (Term retention — the S12 profile).**
   Pre/post-order declared "gap"; "UnboundError" ×2 (then lowercase l);
   "inner iterable" for iterator; `cell_content`. His own diagnosis, said in
   session: "if not used for long I tend to forget terminology."
3. **Output-without-trace on the first recall (Depth-before-answer — S20
   rule 3).** Gave `1 2 3` with no reason; the complete frame trace arrived
   on one re-ask. He had it and skipped it — the exact pattern the rule
   names.
4. **The locality trap missed at first sight (Knowledge gap, narrow).**
   Predicted `11` for the incrementing closure; produced the full
   compile-time story unaided when pointed at the single line. The rule is
   owned; RECOGNIZING its trigger in unfamiliar code is what needs reps.
5. **`""` for absent `__doc__` (honest [PREDICT] miss, productive).** Bought
   the None-vs-empty-container discriminator.
6. **Five checks not visibly run on either drill.** The drills were small,
   but the habit is the point — require an explicit report next drill.

## TEACHING MISTAKES THIS SESSION

1. **TERM-TAX SKIPPED on a valid later day.** The interval gate was applied
   (correctly, fifth session running) but the volley it guards was then
   forgotten in the rush to the recall queue. Many rows were already overdue.
   Owed FIRST in S23. The gate is not the ritual; the ritual is the point.
2. **Lambda teaching turn ran long without declaring itself** — against the
   S20 response-length rule's "if a turn must be long, say so at the top."
3. **The `UnboundLocalError` type-back took three asks** — the first two were
   buried mid-message despite the S20 finding that buried asks don't get
   done. The third, isolated as its own numbered line, worked immediately.

## REFERENCE CHECKLIST (name — what it does — the trap)

| Name | What it does | The trap |
|---|---|---|
| pre-/post-order | work before / after the recursive call | there is no single mutating `n` — one per frame |
| cell / `cell_contents` | per-object storage for a free variable | `__closure__` is the TUPLE; sharing needs the same CALL |
| closure | function object + cell keeping a value alive past its frame | the SURVIVAL clause is the definition's point |
| compile-time locality | assignment anywhere → local everywhere in the body | kills the cell inside a closure → `UnboundLocalError` |
| `global` | permits REBINDING a module name | read and mutate never needed it |
| `*args` / `**kwargs` | collect leftovers → tuple / dict | empty = `()` / `{}`, never `None`; call-side is UNPACK |
| `__defaults__` | tuple of defaults, on the function object, def-time | not the local namespace; not module namespace |
| traceback line | one live frame frozen at its executing line | callers' lines are calls, not "problems" |
| forward-only state | iterator position, no rewind | not "one at a time"; iterable ≠ iterator |
| lambda | expression that evaluates to a function object | one-expression body; auto-return; λ doesn't decode |
| `key=` | per-element function; sort by results | returns ORIGINAL items, keys are discarded |
| docstring / `__doc__` | first-statement string stored on the object | absent → `None`, not `""`; comments are not data |

## WHAT'S COMING NEXT (S23)
Term-tax sweep (overdue) → iterator causation re-fire (bug-first) → closure
definition cold → lambda/docstring task-first drills → traceback cold ask →
**OPEN 1.8: lists, slicing at last, the roster settled.** Weekend: first cold
build block. 31 Aug: gauntlet + re-baseline.
