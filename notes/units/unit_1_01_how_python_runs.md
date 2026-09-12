# Unit 1.1 — How Python Runs Code

What happens between `python3 file.py` and output on the screen: the
interpreter, bytecode, the PVM, compile time vs run time, the call stack,
frames, tracebacks, and the REPL.

---

## 1. Source → bytecode → PVM

CPUs do not speak Python. Between a `.py` file and the CPU there are two
stages:

1. **Compile.** The whole file is parsed and turned into **bytecode** —
   instructions for a fictional machine, not for the CPU. Grammar is checked
   here. Nothing has run yet.
2. **Execute.** The **PVM** (Python Virtual Machine) reads bytecode
   instructions one at a time and performs them.

```
SOURCE (.py)  ──compile──▶  BYTECODE  ──execute (PVM)──▶  OUTPUT
```

The PVM is not a translator that hands work to the CPU. It is a **virtual CPU
implemented in software** (a C program, in CPython). The real CPU runs the
PVM; the PVM runs your bytecode. Layers, not translations.

Two corrections that matter:

- The PVM executes bytecode **instructions**, not "lines". One source line is
  several instructions.
- "Python is interpreted, C++ is compiled" is folk understanding. Python **is**
  compiled — to bytecode. The clean distinction: C++ compiles to machine code
  ahead of time and the CPU runs it directly; Python compiles to bytecode at
  run time and ships its own interpreter to run that. Interview sentence:
  **"compiled to bytecode, then the bytecode is interpreted."**

CPython is therefore two parts in sequence: a **compiler** (source → bytecode;
`SyntaxError` lives here) and an **interpreter loop, the PVM** (runs the
bytecode; `NameError`, `TypeError` and everything else live here).

---

## 2. Compile time vs run time — proved

**A syntax error stops everything.** The file never compiles, so no bytecode
exists, so **not one line runs** — including perfect lines above the bad one.

```python
print("line 1")
print("line 2"
print("line 3")
```
```
  File "t.py", line 2
    print("line 2"
         ^
SyntaxError: '(' was never closed
```
`line 1` never printed.

**A runtime error stops only what follows.** The file compiled; the PVM ran
until it hit the problem.

```python
print("line 1")
print("line 2")
print(1 / 0)
print("line 4")
```
```
line 1
line 2
Traceback (most recent call last):
  File "t.py", line 3, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero
```

The compiler checks **grammar only, never meaning**. A typo'd name compiles
perfectly and fails at run time:

```python
print("checking limits")
print(rbot["joint"])        # rbot was never defined
```
```
checking limits
Traceback (most recent call last):
  File "names.py", line 2, in <module>
    print(rbot["joint"])
NameError: name 'rbot' is not defined
```

| stage | what is checked | errors raised here |
|---|---|---|
| compile | grammar | `SyntaxError`, `IndentationError` |
| run | everything else | `NameError`, `TypeError`, `KeyError`, … |

**The tell:** a `SyntaxError` traceback has **no frames** — no
`Traceback (most recent call last)` header, no `<module>` line — because there
was never a running program. If you see frames, something ran.

The diagnostic question to carry: **how far did Python get?** If the answer
is "nowhere", it is a syntax problem. If output appeared first, it is a
runtime problem, and the last line printed tells you where to look.

Bytecode is built at compile time; **frames are built at run time**. The
compiler cannot know how many frames a program will create — that depends on
data, branches and recursion depth it has never seen.

---

## 3. Bytecode files: `.pyc` and `__pycache__`

When a module is **imported**, its compiled bytecode is saved to disk in a
`__pycache__/` folder next to the source:

```
drills/__pycache__/s22_counter.cpython-312.pyc
```

- `cpython-312` names the interpreter that built it. The bytecode format
  changes between minor versions; a 3.12 `.pyc` will not run on 3.11.
- It buys a **faster import** the second time — the compile step is skipped.
  Nothing else: the code runs at the same speed either way.
- It is written on **import only**, not when you run a script directly.
- **Never stale.** The source file's modification time and size are stamped in
  the `.pyc` header. Every import compares the stamp with the file on disk;
  a mismatch triggers a recompile and overwrite. Deleting `__pycache__` is
  always safe.
- `python3 path/to/file.pyc` works: the compile step is skipped and the
  bytecode goes straight to the PVM.

Bytecode instructions look like `LOAD_NAME`, `CALL`, `RETURN_VALUE`. They are
for Python's own virtual machine, not the CPU.

---

## 4. The interpreter: language vs implementation

There is no "Python the program". There is a **language specification** and
there are **implementations** of it:

| Implementation | What it is | Note |
|---|---|---|
| **CPython** | The reference implementation, written in C. What `apt install python3` and python.org give you. | What nearly everyone runs |
| **PyPy** | Written in a restricted subset of Python, with a JIT. 5–10× faster on long-running CPU-bound pure Python. | Weak C-extension compatibility |
| **Jython** | Compiles Python to JVM bytecode. | Niche, stuck on Python 2 |
| **MicroPython** | From-scratch reimplementation for microcontrollers (ESP32, Pi Pico). | Kilobytes of RAM, no OS |

When people say "Python is slow" or "Python has the GIL", they mean
**CPython**. The language mandates neither.

**Why C extensions pin you to CPython.** NumPy, PyTorch, OpenCV and SciPy are
C extensions: written in C/C++/CUDA, compiled to machine code, exposed through
the **CPython C API**. They depend on CPython's internal data structures (a
Python `int` is a `PyLongObject` with a specific layout). PyPy's compatibility
layer for that API is slow and partial, which destroys the speed you bought
PyPy for. Simulation → PyPy is plausible; ML → it is not.

**Why not compile bytecode straight to machine code?** In C++, `a + b` with
two ints is one machine instruction because the types are known at compile
time. In Python `a + b` could be int+int, str+str, list+list, or a class with
`__add__`. Any machine code emitted ahead of time would still have to look up
the types and dispatch — exactly what the PVM already does. **The dynamism is
the cost, not the bytecode layer.**

**JIT — the trick that works.** Compile *while the program runs*, after
observing which types actually flow through each function. If `add(a, b)` is
called a thousand times with ints, compile a specialised int version; if a
float shows up, fall back and recompile. **Type specialisation** is why PyPy
is fast on tight numeric loops. CPython 3.13 shipped an experimental JIT.

**The GIL** (Global Interpreter Lock): in CPython only one thread executes
Python bytecode at a time, even on a multi-core CPU. Practical fork:
CPU-bound work gains nothing from threads (use `multiprocessing`); I/O-bound
work (waiting on a sensor, a camera frame, a network read) is exactly where
threads pay. A CPython property, not a language rule. Full mechanics are 1.13.

---

## 5. The stack, as a data structure

A **stack** is an ordered collection with one rule: add (**push**) and remove
(**pop**) only at the top. **Last In, First Out.**

```python
stack = []
stack.append("A")   # push  -> ['A']
stack.append("B")   # push  -> ['A', 'B']
stack.append("C")   # push  -> ['A', 'B', 'C']
print(stack.pop())  # 'C'   -> ['A', 'B']
print(stack.pop())  # 'B'   -> ['A']
```

---

## 6. Frames

A **frame** is the container Python creates in order to execute one chunk of
code. It holds three things:

1. the **namespace** for that chunk — the dictionary of names created there
   (see 1.2);
2. the **line currently executing**;
3. the **return address** — where execution resumes when this chunk finishes.

No function is required. **Code is what you wrote and sits on disk; a frame is
what Python creates while running it**, and it is destroyed when the run ends.
One recipe, three cooks, three separate workspaces.

### 6.1 A file with no functions has exactly one frame

```python
x = 10
print(locals())
y = 20
print(locals())
```
Read the **end** of each printed dictionary (the front is Python's own
bookkeeping: `__name__`, `__builtins__`, `__file__`, …):
```
{..., 'x': 10}
{..., 'x': 10, 'y': 20}
```
That dictionary **is** the frame's namespace. A rebinding overwrites an entry
rather than creating one:

```python
x = 10
x = 99
print(locals())     # {..., 'x': 99}
```

### 6.2 Why the frame is called `<module>`

The file you ran is a **module**, so the frame belonging to the file is
labelled `<module>` in every traceback:

```python
# crash.py
x = 10
y = 0
print(x / y)
```
```
Traceback (most recent call last):
  File "crash.py", line 3, in <module>
    print(x / y)
ZeroDivisionError: division by zero
```

Consequence: **every program starts executing at module level.** `main()` is
never where a program *starts* — it is the first thing the module frame calls.
The module frame exists before a single line runs and sits at the bottom of
the stack for the life of the program. Proof: a bare `print("hello")` at the
top of a file, outside every function, prints. Nothing called it; something
was already executing.

### 6.3 Adding a function adds a second frame

```python
x = 10

def show():
    z = 5
    print(locals())

show()
print(locals())
```
```
{'z': 5}
{..., 'x': 10, 'show': <function show at 0x...>}
```
Two different dictionaries, therefore two frames. When `show()` returned, its
frame was destroyed and `z` went with it: `z` was an entry in `show`'s
namespace; that namespace was owned by `show`'s frame; frame destroyed →
namespace destroyed → entry gone. `x` survives because it lives in a different
namespace, owned by the module frame, which is still alive.

A frame's death destroys the **binding**, not the object. The object is
destroyed only if nothing else refers to it.

### 6.4 Namespace vs frame

| | Namespace | Frame |
|---|---|---|
| What it is | a dictionary | a container |
| What it holds | names mapped to references | a namespace, the current line, the return address |
| Relationship | the frame **owns** the namespace | |

A namespace maps **names to references**. It does not contain objects, and it
is not global. Objects live elsewhere in memory (the **heap**); the namespace
holds only labels pointing at them. Two proofs:

- An object can exist with **no name**: `[1, 2] + [3]` builds a list that is
  never named.
- Two different namespaces can point at the **same object** at once. If the
  object lived inside the namespace, that would be impossible.

### 6.5 The call stack

Every function call **pushes a frame**; every return **pops** one.

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
Stack through the run (module frame omitted):
```
[main] → [main, outer] → [main, outer, inner] → [main, outer] → [main] → []
```

### 6.6 Running vs paused

```python
def load():
    print("loading")

def run():
    load()
    print("running")

run()
```
At the instant `loading` appears on screen:

| Frame | State | Line it sits on | Waiting on |
|---|---|---|---|
| `load` (top) | running | line 2, the `print` | nothing |
| `run` | paused | line 5, `load()` | `load` to return |
| `<module>` (bottom) | paused | line 8, `run()` | `run` to return |

- **The top frame is running. Every frame below it is paused, each on its own
  line** — the line containing the call it is waiting on.
- **A frame on the stack, or in a traceback, is never finished.** Finishing
  means returning, and returning removes the frame.
- **A paused frame is never paused on a `def` line.** A `def` executes fast:
  it builds a function object, binds a name, and is done. It does not run the
  body.
- **A line finishing is not a frame finishing.** `load` had already executed
  its `print` but had not returned, so it was still running. The frame ends at
  the return, not at its last visible action.
- **"Line reached" is not "line completed".** `result = normalise(raw)` has
  started and cannot finish until `normalise` returns; it is mid-flight.
- `print` is itself a call and gets its own top frame; the caller sits one
  below, paused mid-line, and resumes when `print` returns `None`.

### 6.7 Why a stack and not a queue

Forced by the shape of the problem, not chosen. `<module>` is stuck until
`run` returns; `run` is stuck until `load` returns. The most recently started
call is always the only one not blocked, so it is always the first to finish.
That is LIFO. A queue (first in, first out) would require `<module>` to finish
first — but `<module>` is frozen mid-line on `run()` with no next instruction
until `run` hands back a value. Not slow: a **contradiction**.

### 6.8 See the live stack: `traceback.print_stack()`

```python
import traceback

def load():
    print("loading")
    traceback.print_stack()

def run():
    load()
    print("running")

run()
```
```
loading
  File "trial.py", line 11, in <module>
    run()
  File "trial.py", line 8, in run
    load()
  File "trial.py", line 5, in load
    traceback.print_stack()
running
```
Three frames, each labelled with the exact line it is sitting on. That line
number is the frame's "current line" field, made visible. It prints without
crashing anything.

---

## 7. Tracebacks

A **traceback** is the crash report the interpreter writes when an exception
goes **uncaught**. Three facts:

1. **Trigger:** an exception went uncaught. Not "an error happened" — errors
   get caught all the time and produce no traceback.
2. **Destination:** the error stream (stderr), not standard output.
3. **Shape:** the whole path of calls from where execution started to where
   it broke; **the last line names the exception**, and the text after the
   colon is the message.

```python
def c():
    return 1 / 0

def b():
    c()

def a():
    b()

a()
```
```
Traceback (most recent call last):
  File "t.py", line 10, in <module>
    a()
  File "t.py", line 8, in a
    b()
  File "t.py", line 5, in b
    c()
  File "t.py", line 2, in c
    return 1 / 0
ZeroDivisionError: division by zero
```

- **It is a snapshot of the call stack at the moment of the crash.** Not a
  metaphor — the actual stack.
- **Each line is one live frame**, frozen at the line it was executing. The
  bottom frame is the raise point; every frame above is frozen at its *call*
  to the next function down. Those callers' lines are not "problematic" —
  they are "who called whom".
- **Print direction is a display choice.** Entry point first (bottom of the
  stack), crash last (top of the stack). LIFO governs execution order, not
  print direction.
- **Read it bottom-up.** The last line names the exception and the line that
  crashed; the line above names the function. When it bottoms out in library
  code you have never opened, the useful line is **the lowest one that names
  your own file**.
- **Lines repeat in a recursion crash** because there were that many frames,
  all paused at the same line. The line did not fail 999 times.
- `<stdin>` in the filename slot means the code came from the interactive
  interpreter; `<string>` means `exec()` of a string. Nothing deeper.

**The subtlety that proves an exception is a signal, not a value:**
```python
box = iter([1])
next(box)
print(next(box))
```
```
Traceback (most recent call last):
  File "t.py", line 3, in <module>
    print(next(box))
StopIteration
```
`print` never ran. Python evaluates the argument first; `next()` raised, and
the raise aborted the line before `print` was called. What you saw was the
interpreter's crash report, not program output.

An uncaught exception **terminates** the program with exit code 1. Nothing is
"paused" waiting to resume.

---

## 8. The REPL vs a script

**REPL = Read-Eval-Print Loop.** Type `python3` with no file and you get
`>>>`. It reads one line, evaluates it, **prints the result**, loops.
`Ctrl-D` leaves.

```
$ python3
>>> x = 10
>>> x
10
```
```python
# test.py, run as a script
x = 10
x
# (no output)
```

- **The auto-print is the P in REPL.** A script evaluates an expression
  statement and throws the value away; nothing shows without `print()`. That
  is the *only* difference in what you see. Execution is otherwise identical,
  including the `<module>` frame (`File "<stdin>", line 1, in <module>`).
- A script runs top to bottom and the process ends — state is gone. The REPL
  is a live process; state persists across lines.
- In the REPL the last result is stored in the name `_`. Not relevant to
  files.
- In the REPL there is no script file, so `sys.path[0]` is `''`, meaning "the
  folder the terminal is in" (see 1.10).
- `python3 -c "..."` runs the quoted text as Python code instead of a file.
  Nothing else differs.

The trap: code that "worked" in the REPL prints nothing as a script.

---

## 9. Import, at a high level

`import copy` binds the name `copy` in your namespace to a **module object**.
`copy.deepcopy` is then an ordinary attribute lookup on that object. An import
**runs** the file, once per process, then binds a name. How Python *finds*
the file, packages, and the cache are all in 1.10.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| bytecode | Python-specific instructions for the PVM | not machine code; the CPU never sees it |
| PVM | software CPU that executes bytecode | it *is* the executor, not a translator |
| compile time | whole file parsed, grammar checked, bytecode produced | failure here ⇒ nothing runs at all |
| run time | PVM executes bytecode in order | failure stops only what follows |
| `SyntaxError` | grammar broke | the only error with **no frames** in its traceback |
| `.pyc` / `__pycache__` | cached bytecode, written on import | speeds *import* only; version-tagged; never stale |
| CPython | reference implementation: compiler + PVM, in C | its properties get mistaken for the language's |
| PyPy | JIT implementation | C extensions slow/partial — no good for the ML stack |
| GIL | one thread runs bytecode at a time | CPython property; threads still help I/O-bound work |
| stack | push/pop at the top only, LIFO | nothing but the top is reachable |
| frame | namespace + current line + return address | needs no function; dies on return; not the code |
| `<module>` | the frame for the file itself | not `main` — `main` is just its first call |
| namespace | dict of names → references | holds no objects; objects live on the heap |
| paused frame | a caller frozen on its calling line | never on a `def` line; never "finished" |
| traceback | crash report for an **uncaught** exception, to stderr | one line = one live frame; read bottom-up |
| `traceback.print_stack()` | prints the live stack, no crash | prints bottom-of-stack first, like a traceback |
| REPL | read-eval-print loop, `>>>` | auto-print happens **only** there; `sys.path[0]` is `''` |
