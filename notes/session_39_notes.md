# SESSION 39 NOTES — Tue 1 September 2026, 21:28 → Wed 2 September 2026, 18:55

**1.10 Modules, Packages and Imports — OPENED.**
The August gauntlet was deferred a third time (your call, and the interval gate
agreed: S38 had closed **three minutes** earlier).

Everything below is `[~]`. Nothing taught in a single sitting can be `[x]`.
All of it comes back cold on **3 September**.

---

## SELF-TEST — do this first, notes closed

Write your answers down before reading anything else.

1. `import robot` — name the **two** things it does, in order.
2. A file `robot.py` has `print("hi")` at the top level. Another file does
   `import robot`. Does `hi` appear? Why?
3. A file does `import robot` twice. How many times does `robot.py` run? Why?
4. After `import robot`, why does bare `MAX_ANGLE` raise `NameError` even
   though `robot.py` defines it?
5. After `from robot import clamp`, what does `robot.MAX_ANGLE` do? Why?
6. After `import robot as r`, what does `robot.MAX_ANGLE` do? Why?
7. What is `vars(m)` for a module `m`? Name three things you'd find in it.
8. `d = {"a": 1}`. What does `d.a` do, and what does `d["a"]` do? Why are they
   different — and why does the same distinction *not* bite you on a module?
9. What are the two possible values of `__name__` in a file, and what decides
   which one you get?
10. `sensors.py` has a self-test at the bottom. `app.py` imports it. **Which
    file does the `if __name__ == "__main__":` guard go in, and why that one?**

---

## 1. FULL TEACHING

### 1.1 What a module is

**A module is a `.py` file.** That is the whole definition.

Why they exist — the honest list:

- separate files get separate **namespaces**, so names stop colliding;
- it is how you use code you did not write (standard library, pip).

**What is NOT claimed:** *"it organises your code."* Splitting a 200-line
script into six files makes it worse. Organisation is a consequence of getting
this right, never the reason to do it.

**What it buys you, and this is the load-bearing one:** the import block at the
top of any file is that file's **dependency list**. Read the imports and you
know what a LeRobot file is about before you read a line of its logic. That is
a reading skill, and it is mostly this unit.

### 1.2 THE SENTENCE — the whole unit compresses to this

> **`import` is executable code. It runs a file, top to bottom, ONCE per
> process — and then binds a name.**

Everything strange about imports falls out of that. Do not memorise the rest;
derive it.

### 1.3 Import is a RUN, not a fetch

`robot.py`
```python
print("robot.py is running")

MAX_ANGLE = 180


def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
```

`main.py`
```python
print("main.py starting")

import robot

print("import finished")
print(robot.MAX_ANGLE)
print(robot.clamp(200))
```

```
$ python3 main.py
main.py starting
robot.py is running          <-- nobody called this
import finished
180
180
```

**Line 2 is the lesson.** Nothing in `main.py` calls that `print`. It fired
because `import robot` **executed `robot.py` like a program**, and the print
sits at its top level. Under a "fetch the names" model that line has no reason
to exist.

### 1.4 ONCE per process — the cache

`twice.py`
```python
import robot
print("first import done")

import robot
print("second import done")

print(robot.MAX_ANGLE)
```

```
$ python3 twice.py
robot.py is running          <-- once, not twice
first import done
second import done
180
```

**`cache`** — from French *cacher*, to hide: a stash of results you already
worked out, kept so you don't do the work twice.

Python keeps a dictionary mapping **module name → module object**, called
`sys.modules`.

**Every import statement runs TWO INDEPENDENT STEPS:**

| | |
|---|---|
| **Step 1 — get the module object** | Check the cache. **Miss:** find the file, run it top to bottom, store the result. **Hit:** take the stored object, **no re-run**. Either way you end up holding the same one module object. |
| **Step 2 — bind name(s) in YOUR namespace** | Just an assignment. **This ALWAYS runs**, cache hit or miss. The *form* of the statement decides which names and what they point at. |

**A cache hit does not mean the import did nothing. It means step 1 was free.**

⚠ **The practical bite:** this is why editing a `.py` file and re-running
`import` in a live notebook **does not pick up your edit**. The cache hits,
your new code never runs, and you debug a file you already fixed.

### 1.5 An import binds ONE name — not "all the names"

`bare.py`
```python
import robot

print(MAX_ANGLE)
```
```
robot.py is running
NameError: name 'MAX_ANGLE' is not defined
```

`import robot` does exactly two things: runs `robot.py`, then binds **one**
name — `robot`. `MAX_ANGLE` never entered your namespace. It is fully alive
*inside* `robot`'s. **The dot is the only route in.**

**That is the collision protection working.** Two modules can both define
`clamp` and never clash, because neither one's names are in yours.

### 1.6 The four forms — one machine, four labels

`partial.py`
```python
from robot import clamp

print(clamp(200))
print(robot.MAX_ANGLE)
```
```
robot.py is running          <-- the WHOLE file still ran
180
NameError: name 'robot' is not defined
```

**`from robot import clamp` ran the entire file.** It has to — `clamp` does not
exist until the `def` line executes. **There is no way to get one name out of a
module without running the module.** The only difference is step 2.

| You write | Runs `robot.py`? | Name(s) bound in YOUR namespace |
|---|---|---|
| `import robot` | yes | `robot` |
| `import robot as r` | yes | `r` |
| `from robot import clamp` | yes | `clamp` |
| `from robot import clamp as c` | yes | `c` |

⚠ **Aliasing REPLACES the name; it does not add a nickname beside it.**

`alias.py`
```python
import robot as r
from robot import MAX_ANGLE as LIMIT

print(r.clamp(200))
print(LIMIT)
print(robot.MAX_ANGLE)
```
```
robot.py is running
180
180
NameError: name 'robot' is not defined
```

### 1.7 A module IS an object; its namespace IS a dict

`peek.py`
```python
import robot

print(type(robot))
print(vars(robot).keys())
print(vars(robot)["MAX_ANGLE"])
```
```
robot.py is running
<class 'module'>
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__',
           '__file__', '__cached__', '__builtins__', 'MAX_ANGLE', 'clamp'])
180
```

- **`type(robot)` is `module`** — an ordinary object, like a list or a dict.
- **`vars(obj)`** hands you an object's **namespace dictionary** (`__dict__`).
  Not a copy, not a listing — the actual dict.
- Your names are at the end, **in the order `robot.py` created them**.
- The eight dunders were put there **by Python**, not by your file.

**Connect it to S38:** a function call gets a fresh namespace that dies on
return. A module gets a namespace that **persists** — held alive by the cache —
for the whole process. Same idea, different lifetime.

### 1.8 Subscription vs attribute access — the correction

The mentor said *"the dot is sugar over a dict access."* **That was wrong as
stated, and you disproved it by testing it.** The precise version:

- **`d["k"]` — SUBSCRIPTION.** Looks in the object's **contents**.
- **`obj.k` — ATTRIBUTE ACCESS.** Looks in the object's **namespace**
  (`__dict__`).

**They coincide for a MODULE only, because a module's contents ARE its
namespace.** A plain dict's items are data it holds, not names bound on it:

```python
d = {"MAX_ANGLE": 180}
print(d["MAX_ANGLE"])
print(d.MAX_ANGLE)
```
```
180
AttributeError: 'dict' object has no attribute 'MAX_ANGLE'
```

And the sharper proof:
```python
print(vars({"MAX_ANGLE": 180}))
```
```
TypeError: vars() argument must have __dict__ attribute
```

**A dict does not have dot-access *disabled*. There is no namespace there for
the dot to search at all.**

**Keep this sentence:**
> `robot.MAX_ANGLE` is a lookup in the module's namespace dict — not because
> dots do dict lookups, but because a module's namespace *is* that dict.

### 1.9 `__name__` and `__main__`

**The problem first.**

`sensors.py`
```python
def read_angle():
    return 200


print("SELF-TEST:", read_angle())
```
`app.py`
```python
from sensors import read_angle

print("app is doing real work")
```
```
$ python3 app.py
SELF-TEST: 200               <-- app wanted a function, got a self-test
app is doing real work
```

Swap that `print` for `run_calibration()` and **importing a file to reuse one
function launches the robot.** Import runs the file; you cannot opt out.

**The mechanism.** `__name__` is a string in every module's namespace (you saw
it first in that dunder list). The *same file* reports a different value
depending on how it was reached:

| How the file was reached | `__name__` |
|---|---|
| **imported** | the module's own name, e.g. `"sensors"` |
| **handed to `python3`** | `"__main__"` — whichever file that is |

So a file can ask, at runtime: **was I run, or was I imported?**

**The fix.**

`sensors.py`
```python
def read_angle():
    return 200


if __name__ == "__main__":
    print("SELF-TEST:", read_angle())
```
`app.py`
```python
from sensors import read_angle

print("app is doing real work, angle =", read_angle())
```
```
$ python3 sensors.py
SELF-TEST: 200

$ python3 app.py
app is doing real work, angle = 200
```

⚠⚠ **THE PART YOU GOT WRONG, AND IT IS THE PART THAT MATTERS: THE GUARD GOES
IN THE FILE THAT GETS IMPORTED.** You said it wraps `app.py`'s content. It is
the other way round. The guard exists to protect a file **from its own
top-level code running when someone imports it**, so it lives in `sensors.py`.
`app.py` — the file you actually run — needs no guard at all.

**That block at the bottom of nearly every serious Python file you will read,
LeRobot included, is this and nothing more: an `if` on a string.**

---

## 2. THINKING GAPS THIS SESSION (with error-type classification)

1. **Dropped the module-level `print` from predicted output — TWICE.**
   *Type: LAZY THINKING (not a knowledge gap).* You could state the mechanism
   correctly on demand and confirmed it yourself: *"I forgot to write that
   line, I am clear conceptually."* The channel was checked first — the second
   ask's wording was genuinely ambiguous — and nothing was logged.
   **Why it still costs you: an answer you meant but did not write is, to any
   examiner, an answer you did not have.** And note *which* line you drop: the
   side effect of an import, which is exactly the invisible thing that bites in
   real codebases because nobody wrote a call for it.

2. **`if __name__ == "__main__":` produced unprompted, then placed in the wrong
   file.** *Type: STRUCTURAL FLAW — a missing INDEX, not a missing fact.*
   Identical signature to the S38 `.keys()` miss and the S36 pattern: **you had
   the construct and not the direction.** This is the file's most replicated
   finding about you.

3. **The "fetch" model of import.** *Type: KNOWLEDGE GAP, now closed.* Your
   opening reading — *"getting all the functions and variables in that file in
   our current file"* — was wrong twice over: it does not fetch (it runs), and
   it does not bring all the names (it binds one).

4. ⚠ **NOT A GAP, AND IT IS THE BEST THING IN THE SESSION: you refused to guess
   twice, and both refusals were correct.** On `from robot import clamp` you
   named the exact undetermined fork — *"will it run the entire file, or will
   just import the function"*. On the aliasing snippet you found a real hole in
   the mentor's own compression of the cache rule. **Neither question was
   decidable from what you had been shown.** That is the inverse of the
   depth-before-answer habit this file has logged against you for twenty
   sessions. Keep doing it.

5. ⚠ **You tested a mentor claim in Jupyter and disproved it** (the dot on a
   dict). Second *technical* pushback on your record. This is the behaviour the
   whole course exists to produce.

---

## 3. TEACHING MISTAKES THIS SESSION

1. ⚠⚠ **The same failure twice in one session: CONSOLIDATED QUESTIONS CARRY
   THEIR OWN CODE (S19 rule).** First, four snippets posed with `robot.py`
   shown once and then called "unchanged" — **pushback 71**, upheld. Fixed,
   acknowledged, and then **breached again in a worse form**: the `__name__`
   block forked `sensors.py`/`app.py` into numbered variants
   `sensors2.py`/`app2.py`, and the follow-up question then named the
   un-numbered file — **pushback 73**, upheld, and you were right to be
   frustrated. **Rule of thumb now in STATE.md: two files, fixed names, both
   shown in full, every time. If a demo needs different content, CHANGE the
   file — never fork it.**
2. ⚠ **`cache` used as a naked term** — the mechanism was given but the word
   never defined, until you asked *"what's cache"*. Repaired with the
   name-decoding the Term Retention System requires.
3. ⚠ **An over-broad claim: "the dot is sugar over a dict access."** True for a
   module, false in general. Corrected in §1.8 above.

**Held clean:** FRAME FIRST (you said so), the doubt gate (four times), the
interval gate, NAME-THE-ERROR-BEFORE-THE-MENTOR-SHOWS-IT (you named `NameError`
cold with the right mechanism), and every question tagged before it was posed.

**Pushback running total: 73 raised, 72 upheld or part-upheld.**

---

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | The trap |
|---|---|---|
| **module** | a `.py` file; its executed namespace wrapped in an object | it is an ordinary object — `type(m)` is `module` |
| **`import x`** | runs `x.py` once, binds **`x`** | **it RUNS the file.** Top-level code fires, prints and all |
| **`from x import y`** | runs `x.py` **in full**, binds **`y` only** | `x` itself is NOT bound → `NameError` on `x.anything` |
| **`import x as a`** | runs `x.py`, binds **`a` only** | aliasing **replaces**; `x` is not also available |
| **the import cache (`sys.modules`)** | dict of module name → module object, checked first | a hit skips the *run*, never the *bind*; and it is why a notebook re-import ignores your edit |
| **`vars(obj)`** | hands back the object's namespace dict (`__dict__`) | a plain `dict` has **no** `__dict__` — `vars({})` raises `TypeError` |
| **subscription `d["k"]`** | looks in the object's **contents** | not the same operation as the dot |
| **attribute access `o.k`** | looks in the object's **namespace** | coincides with subscription for a **module only** |
| **`__name__`** | a string: the module's own name, **or** `"__main__"` | `"__main__"` belongs to whichever file you handed to `python3` — it is not a fixed file |
| **`if __name__ == "__main__":`** | lets one file be both a script and an importable module | ⚠ **it goes in the file being IMPORTED, not the file you run** |

---

## 5. WHAT'S COMING NEXT

**Session 40 is the August gauntlet** (deferred three times, twice by the gate
and once by you) — pure mixed recall, no new material, plus the strict-legend
audit of every `[x]` and the re-baseline against 30 September.

**The seven 1.10 rows above come back cold on 3 September.** Nothing in these
notes is evidence yet.

**Still open in 1.10:** packages (the `lerobot.common.datasets...` shape),
`sys.path` (how Python finds the file at all), circular imports, the standard
library, pip, relative vs absolute imports — **and the `.pyc`/bytecode answer
owed to you since S35.**

**Two decisions owed by you at the S40 open:**
1. **Breakpoint debugging** — bolt a block onto the tail of 1.10, or leave it
   to 1.11? (`pdb` is a module; VS Code's debugger is a front end on it; VS
   Code's Call Stack panel is the frame stack you traced unaided in S38.)
2. **Point the weekly cold build block at a real LeRobot file** instead of a
   synthetic task, once 1.10 lands? Same instrument, real substrate. Carried
   from the S38 close.
