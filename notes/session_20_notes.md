# SESSION 20 NOTES — Sunday 16 August 2026

**Topics: recursion — base case, recursive case, pre-order vs post-order, the
identity-value rule, termination · printer vs calculator · pure functions and side
effects · the disguised mutator · edge-case analysis, the five checks · traceback,
taught properly**

1.7 Functions — recursion, pure functions, edge-case analysis.

---

## SELF-TEST — answer these cold before reading on

1. What are the two required parts of a recursive function?
2. What are the **two** termination conditions?
3. Why does work placed *after* the recursive call run in reverse order?
4. What must a base case return, and why?
5. Is `RecursionError` a law of recursion?
6. Printer or calculator — how do you tell, and what changes?
7. What are the two conditions for a pure function?
8. How can a function that takes input and returns output still be impure?
9. What is ONE line of a traceback?
10. Why do traceback lines repeat in a recursion crash?
11. What is `<stdin>`?
12. Name the five checks for finding edge cases.
13. Which check finds a bug like `n <= 10` vs `n < 10`?
14. Does argument count affect whether returning `None` is safe?

Answers in the reference checklist at the back.

---

## FULL TEACHING

### 1. Recursion

**Definition:** a function that calls itself, where each call gets a **strictly
smaller** version of the same problem, and at least one input is small enough to
answer with no further call.

- **Base case** — answered outright, no recursive call.
- **Recursive case** — calls itself on a smaller input and builds its answer from
  what comes back.

**The framing that carries the whole subsection: nothing new is happening in the
machinery.** Every call gets its own frame with its own locals — exactly as in
1.1. Recursion just means **several frames of the same function are alive at
once**.

#### Pre-order vs post-order

Work **before** the recursive call happens on the way **down**; work **after** it
happens on the way **back up**. Same function, same base case — the only
difference is which side of the call your statement sits on.

```python
def countdown(n):              def countdown(n):
    if n == 0:                     if n == 0:
        print("liftoff")               print("liftoff")
        return                         return
    print(n)                       countdown(n - 1)
    countdown(n - 1)               print(n)

# 3, 2, 1, liftoff              # liftoff, 1, 2, 3
```

Why the second one reverses: **each frame parks mid-body waiting for the call
below it.** When that returns, the frame resumes on the next line — and the
deepest frame resumes first.

#### The identity-value rule for base cases

**The base case must return the identity for the operation:** `0` for `+`, `1` for
`*`, `[]` for list concatenation. Return the wrong one and every answer is off.

#### Value-returning recursion — the answer assembled on the unwind

```python
def total(n):
    if n == 0:
        return 0
    return n + total(n - 1)

total(4) -> 4 + total(3)          <- parked, waiting for a number
  total(3) -> 3 + total(2)        <- parked
    total(2) -> 2 + total(1)      <- parked
      total(1) -> 1 + total(0)    <- parked
        total(0) -> returns 0     <- base case answers outright

# unwinding: 1 -> 3 -> 6 -> 10
```

#### Termination needs two conditions, both required

1. A **base case exists** that returns without recursing.
2. **Every call moves the input strictly closer to it.**

**A base case that exists but is stepped over is not a base case.**

`RecursionError` fires at CPython's default depth of **1000**. That is a guard
against runaway memory, **not a law of recursion**.

#### Printer vs calculator

Does the function **print**, or does it **return**?

- A **printer** uses a bare `return` and makes its recursive call **without**
  `return` in front of it.
- A **calculator** returns on every branch.

Mixing them produces stray values nobody uses.

```python
# printer                              # calculator — the stronger design
def count_down_by(n, step):            def count_down_by(n, step):
    if n <= 0:                             if n <= 0:
        return                                 return []
    print(n)                               return [n] + count_down_by(n - step, step)
    count_down_by(n - step, step)
```

The calculator is **testable**:

```python
assert count_down_by(10, 3) == [10, 7, 4, 1]
assert count_down_by(5, 5) == [5]
assert count_down_by(0, 3) == []
```

#### `digit_sum` — where the base case boundary bites

```python
def digit_sum(n):
    if n < 10:                 # n <= 10 would make digit_sum(10) return 10
        return n
    return n % 10 + digit_sum(n // 10)

digit_sum(472) -> 2 + digit_sum(47)
  digit_sum(47) -> 7 + digit_sum(4)
    digit_sum(4) -> base case, returns 4
# unwinding: 4 -> 11 -> 13
```

One character in the comparison is the whole bug.

### 2. Pure functions and side effects

- **Pure** = output depends **only** on the arguments **AND** nothing outside the
  function changes.
- **Side effect** = anything beyond returning a value: printing, writing a file,
  mutating what you were handed, changing a global.

**Neither is better.** Side effects are the point of a program — a program that
touches nothing is a heater. The rule is: **don't hide them, don't mix them.**

**The disguised mutator.** A function that takes input and returns output can
still be impure if it **mutates in place and hands back the same object**:

```python
def add_item(basket, item):
    basket.append(item)     # mutates the caller's list
    return basket           # hands back the SAME object

def add_item(basket, item):
    return basket + [item]  # pure: new list
```

The `is` check exposes it: `True` means you got your own object back.

### 3. Edge-case analysis — the five checks

**The premise correction first: this is not a knack.** It is a checklist run
against the structure of the code.

**Where bugs actually live:**

1. **The exact boundary** of every condition.
2. **Empty / zero / nothing.**
3. **One** — the smallest non-empty case.
4. **The value outside what you silently assumed** (negative, float).
5. **Where two things must agree** — base case and the step that approaches it.

**Five checks, ninety seconds, run before you consider a function done.**

Applied to a bug hunt:

```python
def first_char(word):
    if len(word) <= 1:       # <= 1 catches "" as well as a single char
        return word          # == 1 loops forever on ""
    return first_char(word[:-1])
```

### 4. Traceback — properly

- **`<stdin>` is just the filename slot.** Code typed into the interpreter came
  from standard input, not from a file on disk. You will also see `<string>` for
  `exec()` and `<module>` for top-level code. Nothing deeper than that.
- **The part that matters: each line is ONE LIVE FRAME on the call stack.** That
  is why lines repeat in a recursion crash — line 2 did not fail 999 times; there
  were 999 frames, all paused at line 2.
- **A traceback is a printout of the stack at the moment of the crash, top frame
  last.** Read bottom-up and you are reading "who called whom" in reverse. The
  bottom line is where the exception was raised; the lines above are the chain of
  callers.
- **For your own work:** when a traceback bottoms out in library code you have
  never opened, the useful line is **the lowest one that names your own file** —
  the last thing you wrote before control passed into someone else's code.

### 5. Two precision points worth keeping

- **Argument count and return value are unrelated.** A five-argument function can
  return `None`; a zero-argument function can return a dict. Whether `None` is a
  problem depends only on **what the caller does with it** — the implicit-`None`
  trap, where the function is happy and the caller explodes.
- **Label precision:** it is a **cell**, and `cell_contents` is an attribute on
  the cell (not a "content cell"). And the **variable** is free — unbound in the
  inner function's own scope — while the **value** lives in the cell. Interviewers
  notice this one.

---

## KEY MENTAL MODELS

- Recursion is not new machinery: it is several frames of the same function alive
  at once, each with its own locals.
- Before the call → on the way down. After the call → on the way back up.
- The base case returns the **identity** for the operation.
- Termination needs a base case *and* strict progress toward it.
- Printer or calculator — pick one; the calculator is the testable one.
- Pure means: output from arguments only, and nothing outside changes.
- Returning the object you mutated does not make a function pure.
- Edge cases are a checklist, not an instinct.
- One traceback line = one live frame.

---

## REFERENCE CHECKLIST — cover the right column and answer cold

| Question | Answer |
|---|---|
| What are the two required parts of a recursive function? | A base case that returns without recursing, and a recursive case that calls itself on a strictly smaller input |
| What are the TWO termination conditions? | (1) A base case exists. (2) Every call moves the input strictly closer to it. A base case that gets stepped over is not one |
| Why does work placed AFTER the recursive call run in reverse order? | Each frame parks mid-body waiting for the call below it; when that returns, the frame resumes — deepest first |
| What must a base case return, and why? | The identity for the operation: `0` for `+`, `1` for `*`, `[]` for list concatenation. The wrong one skews every answer |
| Is `RecursionError` a law of recursion? | No. It is CPython's default depth guard at 1000 frames, to stop runaway memory use |
| Printer or calculator — how do you tell, and what changes? | Does it print or return? A printer uses a bare `return` and calls itself WITHOUT `return` in front. A calculator returns on every branch |
| What are the two conditions for a pure function? | Output depends only on its arguments, and nothing outside the function changes |
| How can a function that takes input and returns output still be impure? | If it mutates the object it was handed and returns that same object. The `is` check exposes it |
| What is ONE line of a traceback? | One live frame on the call stack — not "where the error happened", which is only the location half |
| Why do traceback lines repeat in a recursion crash? | Because there were that many frames, all paused at the same line. The line did not fail repeatedly |
| What is `<stdin>`? | The filename slot, for code that came from standard input rather than a file on disk. Nothing deeper |
| Name the five checks for finding edge cases. | Boundary of every condition; empty/zero; one; the type or sign you silently assumed; whether the base case and the step agree |
| Which check finds a bug like `n <= 10` vs `n < 10`? | Check 1. Read the operator, test the exact value sitting on the boundary — not a value near it |
| Does argument count affect whether returning `None` is safe? | No. They are unrelated. `None` is only ever a problem at the point of use, in the caller |
| Define a closure in one line. | A function object that binds a free variable from where it was created into its own private cell, so the value survives the dead frame |
| Five calls to a factory — how many cells, and why don't the values collide? | Five. Each CALL (not the loop) makes a new frame, re-runs `def`, mints a new function object and a new cell |
| What exactly is `__closure__[0]`? | A cell object. The value is `__closure__[0].cell_contents`. And `__closure__` is `None`, not an empty tuple, when there are no free variables |

---

## WHAT'S COMING NEXT — SESSION 21

- The post-order transfer question, the cell-causation re-fire, the closure
  definition cold, and the first honest traceback test.
- Then **`global`**, **`*args`/`**kwargs`**, **lambdas** and **docstrings** —
  which closes 1.7.
- Still owed from earlier: full slicing (1.8), `zip`, and list comprehensions —
  all used before being taught.
