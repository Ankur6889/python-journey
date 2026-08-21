# SESSION 4 NOTES — Finishing 1.1: The Call Stack & the REPL

**Topics: the stack data structure · the call stack and frames · tracebacks and
their print direction · REPL vs script · `x[0] = 99` — mutation, not rebinding**

This closes 1.1.

---

## SELF-TEST — answer these cold before reading on

1. Walk through everything between hitting Enter on `python3 hello.py` and `hi`
   appearing on screen.
2. `x = [1,2,3]; y = x; x[0] = 99`. Rebinding or mutation? What is on the left of
   the `=`, exactly?
3. What is a stack, in one rule? Why is it the right structure for function calls?
4. What exactly is in a frame?
5. `a()` calls `b()` calls `c()` which divides by zero. In what order does the
   traceback print the three functions, and why isn't the answer LIFO?
6. In a script, a bare line `x` produces what output?

---

## FULL TEACHING

### 1. Rebinding vs mutating — where the rule actually lives

```python
x = [1, 2, 3]
y = x
x[0] = 99
```

The trap: the presence of `=` fires the "rebinding" rule before the left-hand
side has been read. But look at the left side. It is not `x`. It is `x[0]`.
The name `x` is **never rebound**. Python parses this as
`__setitem__(x, 0, 99)` — reach into the object `x` is currently bound to and
change one slot. That is **mutation**: `x` and `y` still point at the same
object, and both see `[99, 2, 3]`.

> **The rule: classify the operation by what is on the left of the equals, not
> by the presence of the equals.**
>
> `x = ...` rebinds. `x[0] = ...` mutates.

Contrast with genuine rebinding:

```python
a = [10, 20]
b = a
b = [10, 20]      # creates ANOTHER object and binds it to b
a is b            # False — equal contents, separate objects
```

One correction to carry from 1.1: bytecode is **not** cached to `.pyc` on direct
script execution. `.pyc` caching happens on **import** only. (Full coverage in
1.10.)

### 2. The stack, as a data structure

A **stack** is an ordered collection with one rule: you may only add (**push**)
or remove (**pop**) at the top. **Last In, First Out.** Picture plates stacked on
a counter.

```python
stack = []
stack.append("A")   # push — ["A"]
stack.append("B")   # push — ["A", "B"]
stack.append("C")   # push — ["A", "B", "C"]
stack.pop()         # returns "C" — ["A", "B"]
stack.pop()         # returns "B" — ["A"]
```

### 3. The call stack — Python's use of that structure

Every function call **pushes a frame**; every return **pops** one. A **frame**
bundles:

- the function's local namespace (the same kind of namespace dictionary from
  Session 1, scoped to this call),
- the currently executing line,
- the return address.

**Why a stack and not something else?** Because of the shape of nested calls: the
most recently called function is always the one that must finish first. If `main`
calls `outer` calls `inner`, then `inner` must return before `outer` can resume,
which must return before `main` can resume. LIFO matches the problem exactly.

```python
def inner():
    print("inner running")

def outer():
    print("outer about to call inner")
    inner()
    print("outer back from inner")

def main():
    print("main about to call outer")
    outer()
    print("main back from outer")

main()
```

Stack state through the run:

```
[main] → [main, outer] → [main, outer, inner] → [main, outer] → [main] → []
```

Frames push and pop in mirror order.

### 4. Tracebacks — the call stack made visible

When Python dies on an uncaught exception it prints a **traceback**. The
traceback is literally a snapshot of the call stack at the moment of the crash,
dumped to screen. Not a metaphor — the actual stack.

```python
def c():
    return 1 / 0

def b():
    c()

def a():
    b()

a()
```

Python prints **`a` first, then `b`, then `c`** — *bottom of stack first*, walking
upward through the call chain.

**Why "LIFO, so `c` first" is wrong:** LIFO describes **execution flow** — the
order frames pop off at runtime. A traceback isn't popping frames.
It reads the stack as a frozen snapshot and prints it so a reader can see where
the program started and how it got to the crash. The print order is a **display
choice**: the entry point is the orienting context, the crash is the punchline.

> Tracebacks tell a story from entry point (top of printed output, bottom of the
> stack) to crash site (bottom of printed output, top of the stack). **LIFO
> governs execution behaviour, not print direction.**

**Senior-engineer technique: read tracebacks bottom-up.** The last printed line
names the exception and the line that crashed; the line above names the function.
The bottom two or three lines are usually all you need — walk upward only for
context.

### 5. REPL vs script

**REPL** — Read, Eval, Print, Loop. Interactive: type one line, the interpreter
evaluates it and prints the value automatically.

**Script** (`.py`) — batch execution: parse the whole file, run start to finish,
exit. Expressions evaluate **silently**.

```python
# In the REPL
>>> x = 10
>>> x
10

# In test.py, run as a script
x = 10
x
# (no output)
```

The auto-print *is* the **P** in REPL — every expression's value is echoed back.
Scripts need an explicit `print()` to show anything.

> **Common beginner trap:** code that "worked" in the REPL prints nothing as a
> script. The auto-print is REPL-only.

---

## KEY MENTAL MODELS

- Stack: push/pop at the top only, LIFO. Plates on a counter.
- Call stack: runtime bookkeeping for nested calls — frame pushed on call, popped
  on return. LIFO because the innermost call always finishes first.
- Frame: local namespace + current line + return address.
- Traceback: a frozen snapshot of the call stack, printed bottom-of-stack first
  so it reads as a story. Read it bottom-up.
- LIFO ≠ print direction.
- REPL is for exploration (auto-print); scripts are for automation (explicit
  `print`).
- Rebinding vs mutation, refined: classify by what's on the **left** of `=`.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| stack | Ordered collection, LIFO, push/pop at top | Nothing but the top is reachable |
| call stack | Holds one frame per active call | Depth is finite — deep recursion overflows it |
| frame | Locals + current line + return address | Locals die with the frame |
| traceback | Snapshot of the stack at the exception | Printed bottom-of-stack first, so read it bottom-up |
| `x[0] = v` | `__setitem__` — mutates in place | Looks like assignment; every alias sees the change |
| REPL auto-print | Echoes each expression's value | Doesn't happen in scripts |

---

## WHAT'S COMING NEXT — SESSION 5

- Recall on the call stack and traceback direction, phrased as a scenario: given a
  crash trace, describe the stack at the moment of the crash and name the entry
  function.
- Open **1.3 Data Types — the five primitives**, starting with `int` and `float`,
  including the `0.1 + 0.2 != 0.3` demo under predict-then-verify.
- Drill `type()` and `isinstance()` — runtime type inspection.
- **Not** the 1.4 mutation drill yet; it waits until list/dict familiarity is
  there, and will use `id()` before and after to make mutation visceral.
