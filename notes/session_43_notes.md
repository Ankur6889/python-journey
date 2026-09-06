# Session 43 — notes (Sat 5 Sep 2026 17:03 → paused → Sun 6 Sep ~23:00)

**What this session was:** term-tax, one new rule of the language (positional
vs keyword ORDER), the whole import story re-told from the cache at your
request, `sys.path` finished, and packages opened. You stopped one teach-back
short of closing packages.

Result: term-tax 2/4 promoted (`unpacking`, `ZeroDivisionError`); 2 stayed
[~] (`< > ^`, the *keyword argument* label). One row added. Pushbacks 79 and
80, both upheld.

---

## SELF-TEST — do this first, notes closed

1. `def f(arg1, arg2, arg3)`. Two calls: `f(10, 20, arg1=99)` and
   `f(arg1=1, 10, 20)`. Which one fails when, and with which error? Why?
2. What is `name=value` on a CALL line called? On a `def` line?
3. `import robot` twice in one file. How many times does `robot.py` run, and
   what is the name of the dict that makes that true?
4. Two caches are involved in an import. Which one lives where, and which
   step does each one save?
5. `sys.path`: what is it physically, what is in slot 0 when you run a script,
   and what is in slot 0 in a REPL?
6. `~/tools/helper.py`, imported from a script in `~/Desktop/codes/`. Fails.
   Two fixes.
7. `import arm.limits`. Which files run, in what order? Which ONE name is bound
   in your file? What is `arm`?

---

## 1. FULL TEACHING — from scratch, with runnable code

### 1.1 Positional vs keyword arguments — the matching rule

**What.** When you call a function, Python has to put each value you pass into
a parameter. Two ways to say which: by **position** (a bare value fills the next
empty slot, left to right) or by **name** (`arg1=99` goes into `arg1`).

**Vocabulary, the pair you dropped.** `name=value` on the **call** line is a
**keyword argument**. `name=value` on the **`def`** line is a **default**. Same
shape, different side, different meaning.

**The rule.** Bare values first, left to right; then each named one into the
parameter of that name; every parameter filled exactly once.

**Two ways to break it, both run:**

```python
def another_function(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

another_function(arg1=1, 10, 20)
```
```
SyntaxError: positional argument follows keyword argument
```
Once a named one appears, slot counting has stopped; a bare value after it has
no slot. Refused at **compile time**, before any call, and without looking at
the `def` at all.

```python
another_function(10, 20, arg1=99)
```
```
TypeError: another_function() got multiple values for argument 'arg1'
```
`10` filled `arg1`, `20` filled `arg2`, then `arg1=99` arrives and `arg1` is
already full. Caught **at the call**, before the body runs.

**The working shape:**
```python
another_function(10, 20, arg3=99)
another_function(10, arg3=99, arg2=20)
```
```
10 20 99
10 20 99
```
Named ones can be in any order among themselves. That is the position freedom
you described, and it was right.

Ranked: the double-fill rule is the one that bites in real code. Left-to-right
is a one-liner.

### 1.2 The import story, all five steps (re-told at your request)

`import robot` must produce a module object and bind the name `robot`. To build
the object Python must **find** `robot.py`, **compile** it, and **run** it.

**First time in this process:**
1. Look in `sys.modules`, a **dict in memory**. Key `"robot"` absent. Miss.
2. Find the file: walk the folders in `sys.path`, first one holding `robot.py`
   wins.
3. Compile: if `__pycache__/robot.cpython-312.pyc` exists and is newer than
   `robot.py`, load it and skip compiling; otherwise compile and write it.
4. Run the bytecode top to bottom. This is when `print(...)` at module level
   fires and names like `MAX_ANGLE` are created.
5. **Store** the module object in `sys.modules["robot"]`. Bind `robot` in your
   file.

**Second time in the same process:**
1. Look in `sys.modules`. Key present. Hit.
2. Bind the name. Done. Nothing runs, nothing prints.

**Two caches, not one.** `.pyc` is on disk and saves step 3 **across runs**.
`sys.modules` is in memory and saves steps 2–4 **within one run**; it dies with
the process.

```python
# teaching/s39_imports/robot.py
print("robot.py is running")
MAX_ANGLE = 180
```
```python
# teaching/s39_imports/twice.py
import robot
print("first import done")
import robot
print("second import done")
print(robot.MAX_ANGLE)
```
```
robot.py is running
first import done
second import done
180
```

Your language fixes: the **import machinery** searches, not "the compiler";
`sys.modules` is a dict, not a file; step 5, the store, is what makes the
second import a hit.

### 1.3 `sys.path` — what it is, physically

`sys` is a module that ships with Python. Inside it is a variable `path`. It
holds a **list of folder-name strings**. That is all `sys.path` is.

```
>>> import sys
>>> type(sys.path)
<class 'list'>
>>> len(sys.path)
7
```

**What it is for.** Python will not search your whole disk for `robot.py`. It
searches **only** the folders in this list, in order, stopping at the first hit.

**Where the list comes from.** Built fresh every time a process starts. Not a
history of where you have run Python; not a guess.
- **Slot 0:** the folder the **script you ran lives in**. Not where the terminal
  is. In a REPL or `python3 -c` there is no script, so slot 0 is `''`, meaning
  "the folder the terminal is in".
- **Slots 1–6:** the installation's folders (stdlib, `site-packages`, and on
  your machine the ROS Jazzy `site-packages`). Same every run.

```
$ cd ~/Desktop/python-journey
$ python3 -c "import sys; print(sys.path)"
['', '/opt/ros/jazzy/lib/python3.12/site-packages', '/usr/lib/python312.zip',
 '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload',
 '/usr/local/lib/python3.12/dist-packages', '/usr/lib/python3/dist-packages']
$ python3 -c "import s22_counter"
ModuleNotFoundError: No module named 's22_counter'
```
The file is in `drills/`, and `drills/` is not one of the seven. File exists,
import fails. Only the list is searched.

**The two fixes** (your hypothetical: `~/tools/helper.py` imported from
`~/Desktop/codes/python_codes/ankur.py`):
1. Put the files side by side, so slot 0 covers both. What real projects do.
2. Add the folder to the list, **before** the import line, because `import`
   reads the list at the moment it runs:
```python
import sys
sys.path.append("/home/ankur/tools")   # a string; Python does NOT expand ~
import helper
```
Run on the repo case:
```python
import sys
sys.path.append("/home/ankur/Desktop/python-journey/drills")
import s22_counter
print(s22_counter.__file__)
```
```
/home/ankur/Desktop/python-journey/drills/s22_counter.py
```
Your third idea, `import ~/tools/helper.py`, is a `SyntaxError`: `import` takes
a **name**, never a path.

### 1.4 REPL

**R**ead, **E**val, **P**rint, **L**oop. Type `python3` with no file name and
you get `>>>`. It reads one line, evaluates it, prints the result, loops. No
script file exists, which is why slot 0 of `sys.path` is `''` there.

```
$ cd ~/Desktop/python-journey/drills
$ python3
>>> import sys
>>> sys.path[0]
''
>>> import s22_counter
>>> s22_counter
<module 's22_counter' from '/home/ankur/Desktop/python-journey/drills/s22_counter.py'>
```

### 1.5 Packages (opened, one teach-back short)

**What.** A folder Python treats as importable. **Why.** One flat folder of
`.py` files stops scaling at about twenty: names collide, nothing is grouped.
**What it buys you.** `import lerobot.datasets.utils` reads as a path through
folders, and that is exactly what it is.

**Definition.** A folder is a package when it contains a file named
`__init__.py`. That file may be empty. Each `.py` inside is a module, reached
with a dot.

The demo, real files in `teaching/s43_packages/`:

```python
# teaching/s43_packages/use_arm.py
import arm.limits
print("import done")
print(arm.limits.MAX_ANGLE)
```
```python
# teaching/s43_packages/arm/__init__.py
print("arm/__init__.py is running")
```
```python
# teaching/s43_packages/arm/limits.py
print("arm/limits.py is running")
MAX_ANGLE = 180
```
```
$ cd teaching/s43_packages && python3 use_arm.py
arm/__init__.py is running
arm/limits.py is running
import done
180
```

**Which name is bound.** One: `arm`. You predicted `arm.limits`; that is not a
name, it is **attribute access** on the object `arm`, same shape as
`robot.MAX_ANGLE`. Proof:
```python
import arm.limits
print(arm)
print(arm.limits)
print(limits)
```
```
<module 'arm' from '.../s43_packages/arm/__init__.py'>
<module 'arm.limits' from '.../s43_packages/arm/limits.py'>
NameError: name 'limits' is not defined
```
Read the first line: **the object `arm` IS `__init__.py`.** That is why it runs
first: the package's module object has to exist before `limits` can be hung
off it as an attribute. Both go into `sys.modules`, under `"arm"` and
`"arm.limits"`. `arm.limits.MAX_ANGLE` is one name and two attribute lookups.

**Held for S44:** your one-sentence teach-back on the two lines above.

---

## 2. THE TERM-TAX — 4 rows

| Term | Your answer | Verdict |
|---|---|---|
| `unpacking` | count of names = count of items, via `zip`/`enumerate`/dict; count-mismatch snippet named `ValueError` at 7 | **[x]**, rated 5, due 7 Sep |
| `ZeroDivisionError` | `any_number / 0`, rated 6 | **[x]** |
| `< > ^` in a format spec | `<` left, `>` right, `^` gone; "overrides the type default" gone | [~], due 6 Sep |
| parameter vs argument / **keyword argument** | first half exact at 6; second half: *"default argument"* at 7, then no label | [~], due 7 Sep |

---

## 3. THINKING GAPS THIS SESSION — with classification

1. **Keyword vs default label swap** — *Knowledge gap (label).* The mechanism
   (position freedom by naming) was intact; the word was missing and a
   neighbouring word was used. Fixed by placing the two words on their two
   sides. **Rated 7 on the miss — second 7/8-on-a-label-miss in two sessions.**
2. **`ankur(city="jaipur", tiwari)` looked like a normal call** — *Knowledge
   gap (untaught rule).* Not a retention failure; the ordering rule had never
   been taught. Taught, teach-back clean.
3. **`^` and the override fact in format specs** — *Knowledge gap.* You asked
   for the one line yourself. Cold ask due.
4. **Bound name predicted as `arm.limits`** — *Structural (name vs attribute).*
   A [PREDICT], not logged. The same distinction as `robot.MAX_ANGLE`; worth
   watching because it recurs in `from x import y` next session.
5. **"Compiler" for the import search; "file" for `sys.modules`** — *Label
   slips on an intact mechanism.* Corrected, nothing logged.
6. **Declined to guess twice** (keyword label; files-together fix). Correct
   behaviour, fourth session running.

---

## 4. TEACHING MISTAKES THIS SESSION

1. **Pushback 79 (upheld):** you asked a direct question about an untaught
   rule and got a [PREDICT] back. FOUNDATION BEFORE PREDICTION breached.
2. **Pushback 80 (upheld):** the package demo files were created on disk
   without saying so, and a tree diagram was shown without saying what
   indentation in it means. Fixed by listing each path with its code beneath.
3. **`teaching/s39_imports/where.py` (untracked, S42) was overwritten** by a
   one-line `printf` without being read first. The S42 content is lost.
4. **Three restatements of `sys.path`.** The S42 frame was re-used verbatim
   with jargon ("entry 0", "slot") you had not been given. What landed was
   physical-first: a module, a variable, a list of strings.
5. The two-caches table was correct and did not teach; the linear five-step
   story did.

Held clean: interval gate from the repo; every snippet run before it was
posed; error named by you before each traceback; ratings after your answer;
"understood" not accepted as evidence; your restart request on an [x] item
logged as a watch, not a miss.

---

## 5. REFERENCE CHECKLIST — name, what it does, the trap

- **keyword argument** — `name=value` on the CALL line — TRAP: same shape as a
  default, which is on the `def` line.
- **positional argument** — a bare value, filled by slot left to right — TRAP:
  a bare value AFTER a named one is a `SyntaxError` at compile time.
- **double fill** — a slot filled by position and again by name — TRAP:
  `TypeError: got multiple values`, at the call, not inside the body.
- **`sys.modules`** — dict in memory, name → module object — TRAP: it is why
  a module runs once per process; it dies with the process.
- **`.pyc` / `__pycache__`** — compiled bytecode on disk — TRAP: saves the
  compile only, never the run.
- **`sys.path`** — list of folder strings, searched in order — TRAP: slot 0 is
  the SCRIPT's folder, `''` in a REPL; not a history, built fresh per process.
- **`sys.path.append(...)`** — `.append()` on a list — TRAP: must come BEFORE
  the import; Python does not expand `~`; a smell in a real codebase.
- **REPL** — Read-Eval-Print-Loop, `>>>` — TRAP: no script, so slot 0 is `''`.
- **package** — a folder containing `__init__.py` — TRAP: the package object
  IS `__init__.py`; `import a.b` binds only `a`; `a.b` is attribute access.

## 6. NEXT
Packages [TEACH-BACK] (re-framed), then `from arm import limits`, relative vs
absolute, circular imports, stdlib, pip. 36 overdue rows to fire between
units, oldest first. Read `notes/session_21_notes.md` for `*args`/`**kwargs`
and S19/S23 for closures before their cold asks.
