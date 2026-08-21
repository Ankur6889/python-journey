# SESSION 17 NOTES — Sunday 9 / Monday 10 August 2026

**Topics: the found-flag pattern and why loop `else` exists · `pass` and
`IndentationError` · the ternary (conditional expression) · `if`/`elif`/`else` as
a chain · infinite loops and tracing to the final check · mutating vs
non-mutating methods — the discriminator, not the roster**

This closes 1.6 Control Flow.

---

## SELF-TEST — answer these cold before reading on

Where you have nothing, say "gap" rather than guessing. Rate confidence before
checking.

1. Write the found-flag search from memory: given a list, print "found" if 10 is
   in it and "not found" otherwise, using only `for`, `if`, `break` and a flag
   variable.
2. Now write the same thing using loop `else`. In one sentence: what exact
   question does the flag variable answer, and why does that make loop `else`
   possible?
3. When does a loop `else` block run, and when is it skipped?
4. Why does `pass` exist at all? What error appears if you leave a block empty?
5. Is a comment enough to fill an empty block? Why or why not?
6. State the difference between `pass`, `continue` and `break` in one line each.
7. Rewrite as a ternary: `if x > 0: sign = "positive" else: sign = "negative"`.
8. Why can a ternary be passed straight into `print()` when an `if`/`else` block
   cannot? Use the words *expression* and *statement*.
9. With `x = 5` and the chain `if x > 10` / `elif x > 3` / `elif x > 1` / `else` —
   what prints, and why is only one thing printed when two conditions are true?
10. If `x` were 20 instead, is `elif x > 3` evaluated at all?
11. Why does `i = 0` then `while i < 5: print(i)` never stop?
12. Trace `i = 0; while i < 5: print(i); i += 1` to the end. What is the last
    number printed, and what is the final check that ends the loop?
13. Classify each and give the return value: `l.append(4)`, `l.sort()`,
    `l.reverse()`, `l.copy()`, `s.upper()`.
14. Without memorising a list — how do you work out whether an unfamiliar method
    mutates? Give the two-step test.
15. Why is `l = l.sort()` a bug?

---

## FULL TEACHING

### 1. The found-flag pattern — and why loop `else` exists

The task: search a list for the value 10; print "found" if it is there, "not
found" if it is not — using only `for`, `if`, `break` and a variable.

```python
lis = [1, 35, 23, 64, 10, 243]
flag = False

for i in lis:
    if i == 10:
        flag = True
        print("found")
        break

if not flag:
    print("not found")

# found
```

Notice what it costs: **one variable, touched in three separate places** — created
before the loop, set inside the loop, checked after the loop. That is a lot of
machinery for one question.

And the question worth asking: **what does `flag` actually record?** Only this —
*did the loop finish without hitting a `break`?* Nothing else. But the interpreter
already knows that. It ran the loop; it knows how the loop ended. The flag is you
re-recording, by hand, information Python already has.

That is exactly the gap loop `else` fills:

```python
lis = [1, 35, 23, 64, 10, 243]

for i in lis:
    if i == 10:
        print("found")
        break
else:
    print("not found")

# found
```

> **THE RULE:** a loop `else` block runs **if and only if the loop finished
> without executing a `break`**. If the loop broke out, the `else` is skipped
> entirely.

> **THE TRAP:** this `else` has nothing whatsoever to do with the `else` of an
> `if`. Do not read it as "otherwise". Read it as **"if the loop ran to
> completion"**. Many experienced Python programmers avoid it for exactly this
> reason — the keyword is badly chosen. Know it anyway: it appears in real code
> and in interviews.

### 2. `pass` — the statement that does nothing

Python has a hard syntactic rule: **once a colon opens a block, that block cannot
be empty.** There must be at least one indented statement after it.

```python
if x > 5:
print("done")

# IndentationError: expected an indented block
```

Sometimes the syntax demands a block you have nothing to put in yet — a function
or class whose body comes later. `pass` is the filler: a statement that performs
no operation at all (a **no-op**) and exists purely to satisfy the rule.

```python
def calculate_torque():
    pass

# Runs fine. The function exists and does nothing.
```

> **TRAP 1 — three keywords, three different jobs:**
> - `pass` → do nothing, carry on to the next line.
> - `continue` → abandon the rest of this iteration, jump to the next one.
> - `break` → leave the loop entirely.

> **TRAP 2 — a comment is not a body.** A block containing only `# todo later`
> still raises `IndentationError`, because comments are not code. `pass` is a
> real statement; that is why it works.

### 3. The ternary — a conditional expression

Look at this four-line block. Both branches do the same kind of thing: choose a
value and bind it to `sign`.

```python
if x > 0:
    sign = "positive"
else:
    sign = "negative"
```

When that is all that is happening, Python lets you write it on one line:

```python
sign = "positive" if x > 0 else "negative"
```

Read it from the middle outward: *this value, if the condition holds, otherwise
that one.*

The word that matters is **EXPRESSION**. An expression evaluates **to a value**; a
statement **performs an action**. An `if`/`else` block is a statement — it
executes a branch and produces nothing. A ternary is an expression — it evaluates
to a value, and a value can be used anywhere a value is allowed:

```python
sign = "positive" if x > 0 else "negative"           # bound to a name
print("positive" if x > 0 else "negative")           # passed into a call
labels = ["pos" if n > 0 else "neg" for n in nums]   # inside a list
```

You cannot nest an `if`/`else` block inside a function call like that. **That is
the whole practical difference.**

> **THE TRAP:** reach for a ternary only when both branches select one simple
> value. If either branch needs to do several things, write the full block.

### 4. `if` / `elif` / `else` as a CHAIN

`elif` is "else if" contracted. Its job is to build a chain of conditions checked
in order.

The load-bearing point: **this is ONE connected ladder, not several independent
`if` statements.** Python checks top to bottom, and the **first condition that is
true wins** — its block runs and the interpreter then leaves the entire chain,
without evaluating anything below it.

```python
x = 5

if x > 10:
    print("A")
elif x > 3:
    print("B")
elif x > 1:
    print("C")
else:
    print("D")

# B
```

Step by step: `x > 10`? False, skip A. `x > 3`? True — print B, and stop. `x > 1`
is also true, but it is never even looked at, because the chain has already been
won.

Contrast with three separate `if` statements: those are independent, so both B and
C would print. That is the difference the chain makes.

`else` is optional, evaluates no condition of its own, and catches every remaining
case.

> **THE TRAP:** with `x = 20`, "A" prints and `elif x > 3` is **never evaluated at
> all** — not evaluated-and-ignored, genuinely never run. This matters as soon as
> a condition has a side effect (a function call, a counter increment): **in a
> chain, conditions below the winner do not execute.**

### 5. Loop pitfalls — the infinite loop, and tracing to the end

**Pitfall one — the infinite loop.** A `while` loop re-evaluates its condition
before every pass. If nothing in the body ever changes the variable in that
condition, the condition can never become false:

```python
i = 0
while i < 5:
    print(i)

# 0
# 0
# 0
# ... forever
```

`i` stays 0, so `i < 5` is permanently true. The fix is an update inside the body:

```python
i = 0
while i < 5:
    print(i)
    i += 1

# 0
# 1
# 2
# 3
# 4
```

**Pitfall two — stopping the trace one cycle early.** When you trace a loop you
must state the final cycle explicitly, because **the loop always goes round one
more time than it prints**:

```
... prints 4, then i becomes 5
    control returns to the top
    condition re-evaluated: 5 < 5   ->  False
    body is SKIPPED, loop ends
    5 is never printed
```

> **THE RULE TO CARRY:** the condition **guards entry to the body**, not the value
> that gets printed. The loop terminates on a check that produces no output at
> all — and that silent final check is the step people leave out.

> **RELATED TRAP:** in a `while` loop, a `continue` placed **above** the state
> update skips that update and produces an infinite loop. Put the update where
> `continue` cannot jump over it. In a `for` loop the same shape is harmless,
> because the iterator advances regardless.

### 6. Mutating vs non-mutating methods — the discriminator, not the roster

Memorising a list is the wrong fix. Here is the model instead.

**Python's design principle:** a method that changes an object **in place**
returns `None`. A method that changes nothing returns **a new object** — because
if it did not return one, it would be pointless.

**Step 1 — look at the TYPE, not the method name.** Is the object mutable (`list`,
`dict`, `set`) or immutable (`str`, `int`, `float`, `bool`, `tuple`)? **An
immutable object cannot have a mutating method at all** — impossible by
definition. So every `str` method necessarily returns a new string. That is why
`s.upper()` needs no memorising.

**Step 2 — for mutable objects, use the return value as the tell.** If a method
returns `None`, it mutated, because returning `None` serves no other purpose.

The evidence Python designed this in deliberately: **it gives you name-pairs.**
`l.sort()` is a method and mutates; `sorted(l)` is a function and returns new.
`l.reverse()` mutates; `reversed(l)` and `l[::-1]` return new. **Two names because
there are two behaviours.**

| Call | Behaviour | Returns |
|---|---|---|
| `l.append(4)` | mutates in place | `None` |
| `l.extend([5, 6])` | mutates in place | `None` |
| `l.insert(0, 99)` | mutates in place | `None` |
| `l.sort()` | mutates in place | `None` |
| `l.reverse()` | mutates in place | `None` |
| `l.copy()` | leaves original alone | new list |
| `sorted(l)` | leaves original alone | new list |
| `s.upper()` / `s.strip()` / `s.split()` | cannot mutate (`str` immutable) | new object |

> **THE BUG THIS PREVENTS:** `l = l.sort()` and `l = l.reverse()` are classic
> errors. The method mutates the list and returns `None`, so you rebind `l` to
> `None` and lose your list. Call it as a bare statement: `l.sort()`.

A note on names: `reverse` *sounds* productive, as if it makes something. The
surface cue is wrong; the semantic structure decides. It is a plain-named method
called on a mutable object, which by Python's own convention means it mutates in
place and returns `None`.

---

## KEY MENTAL MODELS

- A flag variable in a search only ever records "did the loop finish without
  breaking?" — which Python already knows. That is what loop `else` is.
- Loop `else` means "if the loop ran to completion", never "otherwise".
- A colon-opened block cannot be empty, and a comment is not a body.
- Expression evaluates to a value; statement performs an action. That is why a
  ternary fits inside `print()` and an `if`/`else` block does not.
- An `elif` chain is one ladder: the first true condition wins and everything
  below it is never evaluated.
- The `while` condition guards entry to the body, not the printed value — always
  trace the silent final check.
- Classify methods by **type first, return value second**. Never by the name.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| found-flag pattern | Search idiom: flag `False` before the loop, `True` on the hit, checked after | Three touch-points for one question — which is exactly why loop `else` exists |
| loop `else` | Runs only if the loop finished WITHOUT hitting `break` | Nothing to do with `if`/`else`. Never read it as "otherwise" |
| `pass` | A no-op. Fills a block the syntax requires but you have nothing to put in | Not `continue` (skip iteration), not `break` (exit loop). And a comment is not a body |
| `IndentationError` | Raised when a colon opens a block and no indented statement follows | Comments do not count as a body. Only real statements do |
| ternary / conditional expression | `x if condition else y`. Evaluates TO a value | Use only when both branches select one simple value; otherwise write the block |
| expression vs statement | Expression evaluates to a value; statement performs an action | This is why a ternary fits inside `print()` and an `if`/`else` block does not |
| `elif` chain | One ladder checked top to bottom; first true condition wins, rest are skipped | Conditions below the winner are NEVER EVALUATED. Matters when they have side effects |
| `else` (in a chain) | Optional catch-all. Evaluates no condition of its own | Absence of `else` means nothing runs when all conditions are false. That is legal |
| infinite loop | `while` whose condition variable is never updated in the body | A `continue` placed above the update recreates it even when the update exists |
| the final loop check | The loop re-tests the condition one more time than it prints, then exits silently | Trace-tail truncation: stating the last printed value is not stating the last cycle |
| mutating method | Changes the object in place: `append`, `extend`, `insert`, `sort`, `reverse` | Returns `None`. `l = l.sort()` destroys your list |
| non-mutating method | Returns a new object: `copy`, `sorted`, `upper`, `strip`, `split` | Original is untouched — the return value is the only result, so you must bind it |
| the discriminator | Step 1 check the type; step 2 check the return value | Immutable types cannot mutate at all. Don't classify from the method's name |

---

## WHAT'S COMING NEXT — SESSION 18

- **[RECALL] The exception family** — `NameError` vs `ValueError` vs `TypeError`
  (name gone → `NameError`; value bad → `ValueError`; type wrong → `TypeError`);
  exceptions-are-signals; `StopIteration` is an exception, not a state; traceback.
- **[RECALL] The iterator causation** — why is an iterator consumed? Required
  answer: forward-only state, a position that only ever moves forward.
- **[RECALL] The modulo identity in symbolic form** — `a == b * (a // b) + (a % b)`.
- **[DRILL] `l.reverse()` and `l.sort()`** derived from the discriminator rather
  than recalled — then unseen methods to classify, which is the real test of the
  model.
- **Then 1.7 — Functions.** It opens by cashing in **function scope** (not block
  scope), which is half the LEGB story. Nested functions and recursion are both in
  this unit. Also due: **`__defaults__`** — where a default argument actually
  lives.
- Also standing: a spoken Feynman recall for the whole of 1.6, a few days out.
