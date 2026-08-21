# SESSION 3 NOTES — How Python Runs Code (1.1)

**Topics: `is`/`==` and `id()` · rebinding vs mutating · the REPL ·
source → bytecode → PVM · compile time vs run time · CPython vs the alternatives
· why bytecode isn't AOT-compiled · JIT and type specialisation · the GIL, defined**

---

## SELF-TEST — answer these cold before reading on

1. Two lists with identical contents: what do `==` and `is` return, and what
   primitive do you reach for to prove it?
2. `id(y)` didn't change. Name the *precise* reason — and say why "the object
   wasn't modified" is the wrong reason.
3. What are the two stages between a `.py` file and the CPU?
4. A syntax error on line 2: does line 1 print? A `ZeroDivisionError` on line 3:
   does line 1 print? Explain the difference in one sentence.
5. Why doesn't compiling Python bytecode straight to machine code make it fast?
6. Why can't PyPy just be dropped in for a PyTorch project?

---

## FULL TEACHING

### 1. `is` vs `==`, and the primitive that proves it

```python
a = [1, 2]
b = [1, 2]
print(a == b)     # True  — equal contents
print(a is b)     # False — two separate objects
```

Run it and `id(a)` and `id(b)` come back as different integers. Same value,
different objects.

The precise phrasing matters: not "`is` checks if objects are the same" but
**"`is` compares object identity — same object in memory, same `id()`."**

The habit: **when you make a claim, reach for the primitive that verifies it.**
`id()` is that primitive for identity claims.

### 2. Rebinding vs mutating — the precise distinction

```python
x = [1, 2, 3]
y = x
x = x + [4]
```

- `x` is `[1,2,3,4]`, `y` is `[1,2,3]`.
- `id(x)` changed — `x` was rebound to a new object.
- `id(y)` did not change — **because `y` was never rebound.** That is the whole
  reason.

"`id(y)` didn't change because we aren't changing the object bound to `y`" is
the wrong reason — it conflates two separate operations:

- **Rebinding** — `y = something_else`. The name points at a different object.
  `id(y)` *does* change.
- **Mutating** — modifying the object in place. `id(y)` does *not* change, but
  the contents do.

Here nothing was mutated either, because `x + [4]` constructs a new list — but
that is a separate fact, not the reason.

Had line 3 been `x.append(4)` instead, `x` and `y` would still be the same
object, mutated, and `print(y)` would show `[1, 2, 3, 4]`.

### 3. What the REPL is

**REPL = Read-Eval-Print Loop.** Type `python3` in a terminal with no script and
you get `>>>`. Each line is Read, Evaluated, its result Printed, then it Loops.

Script vs REPL: a script runs top to bottom and the process ends — state is gone.
The REPL is a live process: state persists across lines and you can poke at
objects between steps. For predict-then-verify drills the REPL beats editing a
file every round.

### 4. Topic 1.1 — how Python runs code

#### 4.1 The core mental shift

CPUs don't speak Python; they speak machine code. Between your `.py` and the CPU
there is machinery, and that machinery is the topic.

Two stages:

- **Source → bytecode.** The whole `.py` file is parsed and compiled to
  bytecode — a Python-specific intermediate representation. Not machine code:
  instructions for a fictional machine. Cached as `.pyc` in `__pycache__/`.
- **Bytecode → executed by the PVM.** The Python Virtual Machine is a program
  (written in C, for CPython) that reads bytecode instructions one at a time and
  performs the corresponding action.

**Key reframe:** the PVM is not a translator handing work to the CPU. It is a
**virtual CPU implemented in software**; its instructions are bytecode
operations. The real CPU runs the PVM (a C program); the PVM runs the bytecode.
**Layers, not translations.** Python code, in a real sense, never runs directly
on the CPU — it runs inside another program.

#### 4.2 The folk distinction that needs replacing

"Python is interpreted, C++ is compiled" is folk understanding. Python *is*
compiled — to bytecode. The clean distinction:

- **C++:** source → machine code (ahead of time) → CPU executes it directly.
- **Python:** source → bytecode (at runtime, on first execution) → PVM executes
  the bytecode.

Python has more layers, and the bottom layer is itself a compiled C program.
That extra indirection is the cost. "No realtime conversion" was the right
intuition; **"no extra layer of indirection"** is the precise version.

#### 4.3 Compile time vs run time — verified empirically

**Test 1 — syntax error:**

```python
print("line 1")
print("line 2"
print("line 3")
```

Observed: **line 1 did not print.** The whole file failed to compile to bytecode,
so nothing executed. This kills the line-by-line model dead — under that model
line 1 would have printed.

**Test 2 — runtime error:**

```python
print("line 1")
print("line 2")
print(1 / 0)
print("line 4")
```

Observed: lines 1 and 2 printed, then `ZeroDivisionError`, then nothing. The file
compiled fine; the PVM executed until it hit the problem.

The lock-in:

- **Compile time** — whole file parsed, syntax checked, bytecode produced.
  Failure here means *nothing* runs.
- **Run time** — the PVM executes bytecode in order. Failure stops execution from
  that point on; everything before it already happened and isn't coming back.

### 5. CPython vs the alternatives

There is no "Python the program." There is a **language specification** and there
are **implementations** of it.

- **CPython** — the reference implementation, written in C. What `python.org` and
  `apt install python3` give you; `/usr/bin/python3` on the Ubuntu box is
  CPython. Used by nearly everyone.
- **PyPy** — written in a restricted subset of Python, with a JIT. 5–10× faster
  than CPython on long-running CPU-bound code. Trade-off: weak C-extension
  compatibility.
- **Jython** — compiles Python to Java bytecode for the JVM. Niche, largely
  abandoned, stuck on Python 2.
- **MicroPython** — from-scratch reimplementation for microcontrollers
  (kilobytes of RAM, no OS): ESP32, Pi Pico.

**The mental model: language = spec, implementation = a program honouring the
spec.** When people say "Python is slow" or "Python has the GIL", they mean
CPython. The language mandates neither.

### 6. `.pyc` portability

`python3 path/to/file.pyc` works — CPython skips the compile step and feeds the
bytecode straight to the PVM. The version constraint is strict: the bytecode
format changes between minor releases, so `trial.cpython-312.pyc` will not run on
3.11. The version is baked into the filename.

(Note for later: `.pyc` files are generated on **import**, not on direct script
execution — covered properly in 1.10.)

### 7. Why C extensions pin you to CPython

NumPy, PyTorch, OpenCV and SciPy are **C extensions** — written in C/C++/CUDA,
compiled to machine code, exposed to Python through the **CPython C API**. They
depend on CPython's specific internal data structures (a Python `int` is a
`PyLongObject` with a particular memory layout). PyPy doesn't share those
internals; its `cpyext` compatibility layer is slow and partial, which destroys
the speed advantage you bought PyPy for.

So: **simulation → PyPy is plausible; ML → it isn't**, and the reason is
mechanical, not vague "libraries don't work well". The whole scientific Python
ecosystem treats the CPython C API as a load-bearing wall.

### 8. "Why not just compile bytecode to machine code?"

The right question — and the one CPython core developers have wrestled with for
years.

#### 8.1 Why naive ahead-of-time compilation buys little

In C++, types are known at compile time: `a + b` with two ints compiles to a
single machine instruction.

In Python, `a + b` could be int+int, float+float, str+str, list+list, array+array,
or a custom class with `__add__`. The compiler cannot know until the call
happens. Any machine code emitted ahead of time would still have to look up the
type, look up `__add__`, dispatch, handle the result — exactly what the PVM
already does. You get a bigger binary doing the same dynamic lookups.

**The dynamism is the cost, not the bytecode layer.**

#### 8.2 JIT — the trick that works

Don't compile ahead of time. Compile **while the program runs**, after observing
which types actually flow through each function. That is **Just-In-Time**
compilation.

PyPy watches execution. If `add(a, b)` is called a thousand times in a loop
always with ints, it compiles a specialised version that assumes ints and emits
the fast instruction. If a float shows up later, it notices, falls back to the
generic version and recompiles if needed. **Type specialisation** — this is why
PyPy is 5–10× faster on tight numerical loops.

So the answer is: **PyPy already exists**, and it does this, with the JIT twist
that makes it viable for a dynamic language.

#### 8.3 Why CPython hasn't simply copied it

- **The C API constraint** — the scientific ecosystem is built against CPython's
  internals; a JIT rewrite would break every C extension on Earth.
- **Engineering cost** — PyPy has been in development since 2007. Production JITs
  need a small army of compiler engineers.
- **Workload reality** — most Python isn't compute-bound. If the bottleneck is a
  DB query, an HTTP call or a NumPy matmul, making the surrounding Python 5×
  faster does nothing.

#### 8.4 The plot twist

CPython is getting a JIT anyway. Python 3.13 (2024) shipped an experimental one;
3.14 is iterating, navigating the constraints above with backwards compatibility
intact.

### 9. GIL — scoped definition

**GIL = Global Interpreter Lock.** A CPython mechanism ensuring only one thread
executes Python bytecode at a time, even on a multi-core CPU. Practical
consequence: pure-Python code can't use multiple cores for parallel speedup the
way C++ threads can.

It is a property of **the CPython implementation**, not the language. PyPy has
one too; some implementations don't. The "no-GIL" work (PEP 703, experimental in
3.13+) is the ongoing effort to remove it.

Full mechanics — why it exists, what it costs, why reference counting forces it —
parked for 1.13.

---

## KEY MENTAL MODELS

- Source → bytecode → PVM. A two-stage pipeline, not a line-by-line translator.
- The PVM is a virtual CPU in software. Layers, not translations.
- Compile time vs run time is empirically testable: syntax errors stop everything
  before any line runs; runtime errors only stop what follows.
- Language vs implementation: "the GIL", "Python is slow" are CPython facts.
- Dynamism is the speed cost; bytecode is not the bottleneck.
- JIT + type specialisation is how you make a dynamic language fast.
- `is` = identity (`id()`), `==` = value. Verify identity claims with `id()`.
- Rebinding ≠ mutating. `id` changes only on rebinding.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| bytecode | Python-specific intermediate instructions | Not machine code; the CPU never sees it |
| `.pyc` / `__pycache__` | Cached bytecode | Tied to the exact minor version; written on import, not on direct run |
| PVM | Software CPU that executes bytecode | It doesn't "translate for the CPU" — it *is* the executor |
| CPython | The reference C implementation | Its properties get mistaken for the language's |
| PyPy | JIT implementation, 5–10× on hot loops | `cpyext` makes C extensions slow/partial — no good for the ML stack |
| REPL | Live read-eval-print process | State persists, unlike a script run |
| GIL | One thread runs bytecode at a time | A CPython property, not a language rule |

---

## WHAT'S COMING NEXT — SESSION 4

- Recall on source → bytecode → PVM, and on rebinding vs mutating.
- Then either finish 1.1 (the call stack, REPL vs script formally) or move into
  1.3 Data Types — the five primitives.
- Queued: the `.append()` mutation drill with `id()` before and after, for 1.4.
