# SESSION 42 NOTES — Fri 4 Sep 2026 23:15 → Sat 5 Sep 02:56

**Same sitting as S41 (three minutes after its commit). Revision on the 40
overdue rows, oldest first, then the 1.9 tail as new material, then the start
of 1.10's second half.** You stopped mid-`sys.path`.

Result: 16 rows fired, 13 pass, 3 fail (`mutable default`, `closure`,
`except ... as e`). One promotion. 1.9 tail taught in full. `.pyc` paid.
`sys.path` opened. Pushbacks 77 and 78, both upheld.

---

## SELF-TEST — do this first, notes closed

1. `def add(v, log=[]): log.append(v); return log`. Two calls, `add(10)` then
   `add(20)`. What prints, and WHEN was the `[]` built?
2. Write the fix for question 1 using `None`.
3. `class BadCommand(ValueError)`. Does `except BadCommand:` catch a plain
   `ValueError`? Does `except ValueError:` catch a `BadCommand`? One sentence
   about the tree for each.
4. Two `except` clauses under one `try`: `except ValueError:` then
   `except BadCommand:`. A `BadCommand` is raised. Which prints, and why is the
   second one unreachable?
5. What does `raise X from e` change in the traceback? Quote the line.
6. Why is a bare `except:` worse than `except Exception:`? Name the two
   siblings of `Exception`.
7. Is Python compiled or interpreted? Give the one-sentence answer.
8. Where does a `.pyc` live, what does it buy you, and how does Python know
   whether it is stale?
9. `import s22_counter` from the repo root fails with `ModuleNotFoundError`.
   What list decides that, and what is entry 0 of it?
10. `except ValueError as e:` — what IS `e`? (This one is on credit until 1.12;
    it is fine to say "an object built by the class".)

---

## 1. FULL TEACHING — from scratch, with runnable code

### 1.1 The mutable default trap and the sentinel

A default argument is a value Python uses when the caller omits that
parameter. **The default expression is evaluated ONCE, when `def` runs, and the
result is stored on the function object in `__defaults__`.** Every call that
omits the parameter binds the name to that same stored object.

```python
def add_reading(value, log=[]):
    log.append(value)
    return log

print(add_reading.__defaults__)   # ([],)
print(add_reading(10))            # [10]
print(add_reading(20))            # [10, 20]   <- the SAME list
print(add_reading.__defaults__)   # ([10, 20],)
```

The fix: a sentinel. `None` is immutable, so sharing it is harmless; the
fresh list is built in the BODY, which runs on every call.

```python
def add_reading(value, log=None):
    if log is None:
        log = []
    log.append(value)
    return log

print(add_reading(10))            # [10]
print(add_reading(20))            # [20]
print(add_reading(30, [1, 2]))    # [1, 2, 30]
```

`__defaults__` is a dunder ATTRIBUTE (a tuple), not a method.

### 1.2 The exception hierarchy — DIRECTION

```
BaseException
├── KeyboardInterrupt      (Ctrl-C)
├── SystemExit             (the program asked to quit)
└── Exception
    └── ValueError
        └── BadCommand     (yours: class BadCommand(ValueError))
```

**A catcher covers its own node and everything BELOW it. Never above.**

```python
class BadCommand(ValueError):
    pass

try:
    int("n/a")               # raises a plain ValueError
except BadCommand:           # node BELOW ValueError -> out of reach
    print("caught")
# -> ValueError escapes, traceback printed
```

```python
try:
    raise BadCommand("stop")
except ValueError:           # node ABOVE BadCommand -> covers it
    print("caught")          # -> caught
```

**When to catch narrow, when wide.** `except BadCommand:` takes only the error
you raised on purpose; a forgotten `ValueError` from `int()` crashes loudly,
which is what you want for a forgotten case. `except ValueError:` takes both.
Choosing the parent class when you write `class BadCommand(ValueError)` is
choosing who ELSE catches it: callers already catching `ValueError` will.

### 1.3 `except` ORDERING

Python checks the clauses top to bottom and takes the FIRST whose node covers
the error. It does not look for the best match.

```python
try:
    raise BadCommand("stop")
except ValueError:
    print("wide catcher")        # <- prints
except BadCommand:
    print("narrow catcher")      # <- unreachable
```

**Child above parent, always.**

### 1.4 `except ... as e` — what `e` is (ON CREDIT until 1.12)

`ValueError("msg")` is a CONSTRUCTOR CALL, exactly like `list()`. It builds a
ValueError OBJECT carrying the message. `raise` throws that object. `except
ValueError as e:` binds `e` to it.

```python
try:
    int("n/a")
except ValueError as e:
    print(type(e))    # <class 'ValueError'>   the class that built it
    print(e)          # invalid literal for int() with base 10: 'n/a'
```

The tree in 1.2 is a tree of CLASSES; what travels through `raise` is always
an OBJECT built from one of them. The full class → object model arrives in
1.12; until then, this is the sentence to keep.

### 1.5 `raise ... from` — one fact

You catch a low-level error and raise a clearer one. Without `from`, Python
prints both and says the second happened *during handling* of the first, as
if by accident. With `from e`, Python says the first CAUSED the second.

```python
def parse(text):
    try:
        return int(text)
    except ValueError as e:
        raise ValueError("bad command: " + text) from e

parse("n/a")
```

```
ValueError: invalid literal for int() with base 10: 'n/a'

The above exception was the direct cause of the following exception:

ValueError: bad command: n/a
```

Drop `from e` and the middle line reads *"During handling of the above
exception, another exception occurred:"*. That line is the whole feature.
This `from` is unrelated to `from math import sqrt`.

### 1.6 `except Exception:` vs bare `except:`

```python
try:
    raise KeyboardInterrupt
except Exception:
    print("swallowed")
# -> NOT caught: KeyboardInterrupt is a SIBLING of Exception, not a child
```

```python
try:
    raise KeyboardInterrupt
except:                      # bare: catches all of BaseException
    print("swallowed")       # -> prints; Ctrl-C is eaten
print("still running")       # -> prints
```

**Never write bare `except:`.** `except Exception:` when you truly need a wide
net; name the class when you can.

### 1.7 `.pyc` and what bytecode is

Importing a module compiles its source to bytecode. A `.pyc` is that bytecode
SAVED to disk, in `__pycache__/` next to the source, e.g.
`drills/__pycache__/s22_counter.cpython-312.pyc` (`cpython-312` = the
interpreter that built it). It buys a faster IMPORT the second time and
nothing else: the code runs at the same speed either way.

**Bytecode** = instructions for Python's own virtual machine (`LOAD_NAME`,
`CALL`, `RETURN_VALUE`, …), not for the CPU. The interpreter loop reads them
one at a time. The C loop itself is 1.13.

**Staleness:** the source file's modification time and size are stamped in the
`.pyc` header. Every import compares the stamp with the file on disk.
Mismatch → recompile and overwrite. Demonstrated: `LIMIT = 90` → import →
edit to `180` → import → `180`, `.pyc` rewritten. Deleting `__pycache__` is
always safe.

### 1.8 Compiled AND interpreted (your question)

CPython is two parts in sequence:

1. **A compiler:** source → bytecode. `SyntaxError` lives here.
2. **An interpreter loop, the PVM:** runs the bytecode. `NameError`,
   `TypeError`, everything else lives here.

C compiles to MACHINE CODE, so no interpreter is needed at run time. Python
compiles to BYTECODE, which no CPU understands, so it ships its own
interpreter. Interview sentence: **"compiled to bytecode, then the bytecode is
interpreted."**

### 1.9 `sys.path` (opened, not finished)

A plain LIST of folder paths. `import x` walks it IN ORDER and takes the first
`x.py` found. Entry 0 is the folder of the script you ran (`''` = the current
folder in a REPL or `python3 -c`). On this machine, from the repo root:

```
                                             <- '' : current folder
/opt/ros/jazzy/lib/python3.12/site-packages
/usr/lib/python312.zip
/usr/lib/python3.12
/usr/lib/python3.12/lib-dynload
/usr/local/lib/python3.12/dist-packages
/usr/lib/python3/dist-packages
```

```python
import s22_counter     # from the repo root
# ModuleNotFoundError: No module named 's22_counter'   (it is in drills/)
```

Every `ModuleNotFoundError` means: not in any folder on this list. **Open
question for next session:** two different ways to make that import succeed.

---

## 2. THE REVISION VOLLEY — 16 rows

| Row | Result | Note |
|---|---|---|
| function object vs call | PASS 7 → [x] | `b(5)` → `TypeError`; say "CALL it", not "pass an argument to it" |
| mutable default + sentinel | FAIL 6, stays [~] | "a fresh list each call" — the trap itself; re-taught (§1.1) |
| while vs for | PASS 8 | `halvings(n)` cold; "runs WHILE true", not "till" |
| zip / zip fails silently | PASS 8 / 8 | truncation + exhausted `[]`; "`zip()` RETURNS an iterator" |
| slicing / shallow copy | PASS 8 | copies REFERENCES, not objects |
| `{}` is a dict | PASS 7 | `.add` → `AttributeError`; `set()`; BRACES |
| None is not nothing | PASS 8 | no return REACHED on that path |
| tuple immutability | PASS 7 | reasoned live; immutability is of the SLOTS |
| copy.deepcopy | PASS 8 | |
| expression vs statement | PASS 8 | 6/6, "boils down to a value" |
| ValueError | PASS 7 | + print never reached |
| raise-vs-shrug | PASS 8 | |
| docstring / `__doc__` | PASS 7 | position rule |
| cell / closure | GAP → [~] | read S19, S23 notes + `drills/s25_closure.py` |
| except ... as e | FAIL 8, stays [~] | over-rated; see §1.4, on credit |

Also requested for revision: `*args`/`**kwargs` → `notes/session_21_notes.md`,
`drills/s22_report.py`.

---

## 3. THINKING GAPS THIS SESSION — with classification

1. **Mutable default — KNOWLEDGE GAP (model inverted).** "Each call assigns a
   new empty list" is the exact wrong model, stated confidently at 6. The
   `__defaults__` check fixed it in one step. Later-day cold ask decides it.
2. **Closure four layers — DECLARED GAP, honest.** No guess, a request for the
   session pointer. Correct behaviour; the row drops to [~] and comes back.
3. **`except ... as e` — OVER-RATED at 8 on a miss.** The only calibration
   miss of the night. The underlying gap (class → object) is structural and
   belongs to 1.12; not a lazy-thinking entry.
4. **Direction vs ordering conflated on the first hierarchy teach-back** —
   PARTLY CHANNEL: the demo carried two ideas. Cleared when the demo was cut to
   one block.
5. **Shape slip:** `10` for a function that returns a list. Surface read of the
   `return` line — the depth-before-answer habit, small instance.

## 4. TEACHING MISTAKES THIS SESSION

1. "This one raises" said before the `{}` snippet — S27 rule breach.
2. Two `try` blocks in one demo — two ideas in one turn, produced a wrong-topic
   teach-back.
3. `except ... as e` teach-back built on class → object, which is on credit
   (define-before-use).
4. "The function from earlier" + unstated task shape on the classification ask
   (pushback 77).
5. `raise ... from` framed abstractly first; the before/after pair should have
   led.

## 5. REFERENCE CHECKLIST — name, what it does, the trap

- **default argument** — value used when the caller omits it — TRAP: built
  ONCE at `def`, shared by every call; use `None` + build in the body.
- **`__defaults__`** — tuple of default values on the function object — TRAP:
  attribute, not method.
- **hierarchy direction** — a catcher covers its node and below — TRAP: a
  child catcher does not catch its parent.
- **`except` ordering** — first match top-down wins — TRAP: parent above child
  makes the child unreachable.
- **`except ... as e`** — binds the thrown OBJECT — TRAP: `e` is neither the
  class nor text; `type(e)` is the class, `print(e)` the message.
- **`raise X from e`** — records `e` as the cause — TRAP: same keyword as
  `from x import y`, unrelated job.
- **bare `except:`** — catches all of `BaseException` — TRAP: eats Ctrl-C and
  `SystemExit`; write `except Exception:` at widest.
- **`.pyc`** — cached bytecode in `__pycache__` — TRAP: speeds IMPORT only;
  never stale (mtime + size stamp); safe to delete.
- **compiled vs interpreted** — CPython = compiler + PVM — TRAP: "compiled or
  interpreted" is a false choice; answer "compiled to bytecode, then
  interpreted".
- **`sys.path`** — list of folders searched in order — TRAP: entry 0 is the
  SCRIPT's folder, not the project root.

## 6. NEXT
`sys.path` [PREDICT] (two fixes), then packages / relative vs absolute /
circular imports / stdlib + pip. Cold asks due 7 Sep on tonight's eight new
rows. Read the closure and `*args`/`**kwargs` notes before then.
