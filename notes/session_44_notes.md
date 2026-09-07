# Session 44 — notes (Mon 7 Sep 2026, 07:27 → ~08:40)

**What this session was:** packages closed for the day, starting from your
own question rather than my held teach-back; relative vs absolute imports
opened and taught through the run-directly trap; two quizzes at your
request, both with real flaws; a voice re-teach file written because you
said the topic was flaky. You closed early to run that file on the web.

Result: no cold asks fired, no promotions (all same-day, correctly). Two
queue rows added, due 8 Sep. Pushbacks 81 (part), 82, 83 — all upheld.

---

## SELF-TEST — do this first, notes closed

Folder `arm/` holds `__init__.py`, `limits.py` (has `MAX_ANGLE = 180`), and
`motion.py`. An outside file sits next to the folder.

1. The outside file says `import arm.limits`. Which files run, in what
   order? Which keys land in `sys.modules`? Which ONE name lands in the
   outside file?
2. The outside file says `import arm` only, then `arm.limits.MAX_ANGLE`.
   What happens, and why?
3. The outside file says `from arm import limits`. Same three questions as
   Q1. What is different from Q1, and what is the same?
4. `motion.py` line 1 is `from . import limits`. Write it as an absolute
   import. Which name lands in `motion.py`?
5. `python3 arm/motion.py`, run directly. Works or fails? Name the error
   and say what Python could not work out.
6. What is `__init__.py` for when it is empty? When it is not?

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

All files live in `teaching/s43_packages/`. Run everything from inside that
folder.

### 1.1 What a package is, physically

A **module** is a file, `x.py`. A **package** is a **folder** that contains a
file named `__init__.py`. That file's presence is the whole definition.
Every `.py` inside the folder is a module of the package.

Why: a real codebase is hundreds of files. A package puts them under one
name, and the folder structure becomes the dotted name. `from
lerobot.common.policies.act import ACTPolicy` walks on disk: folder
`lerobot` → folder `common` → folder `policies` → file `act.py`. **Dots are
folder separators.** That is the fact worth having; the rest is detail.

```
teaching/s43_packages/
    use_arm.py   only_arm.py   from_arm.py   quiz1.py   run_motion.py
    arm/
        __init__.py   limits.py   safety.py   safety_rel.py   motion.py
```

`arm/__init__.py`
```python
print("arm/__init__.py is running")
```
`arm/limits.py`
```python
print("arm/limits.py is running")

MAX_ANGLE = 180
```

### 1.2 `import arm.limits` — two tables

`use_arm.py`
```python
import arm.limits
print("import done")
print(arm.limits.MAX_ANGLE)
```
```
arm/__init__.py is running
arm/limits.py is running
import done
180
```

What happens, in order: `__init__.py` runs first and becomes the module
object `arm`. Then `limits.py` runs and becomes the module object
`arm.limits`. Then `limits` is written as an **attribute** onto `arm`.

Two tables, and this is the split you asked for:

| Table | What lands | Same for every import form? |
|---|---|---|
| `sys.modules` (what got LOADED) | keys `"arm"` and `"arm.limits"` | **yes** — keys are fixed by position on disk |
| your file's namespace (what got BOUND) | the ONE name `arm` | **no** — depends on how you wrote the line |

A name in a namespace is one word with no dots. `arm.limits.MAX_ANGLE` is
one NAME lookup (`arm`) followed by two ATTRIBUTE lookups. Proof:

```python
import sys, arm.limits
print([k for k in sys.modules if k.startswith("arm")])   # ['arm', 'arm.limits']
print("limits" in vars(arm))                             # True
print(vars(arm)["limits"] is sys.modules["arm.limits"])  # True — same object
```

### 1.3 `import arm` alone does NOT load `limits`

`only_arm.py`
```python
import arm
print("import done")
print("arm" in vars(), "limits" in vars())
print(arm.limits.MAX_ANGLE)
```
```
arm/__init__.py is running
import done
True False
Traceback (most recent call last):
  File "only_arm.py", line 4, in <module>
    print(arm.limits.MAX_ANGLE)
AttributeError: module 'arm' has no attribute 'limits'
```

New construct, defined here: **`vars()` with no argument** is the namespace
dict of the file you are standing in, the way `vars(arm)` is the namespace
dict of module `arm`.

`import arm` runs `__init__.py` and **stops**. Python does not scan the
folder. `__init__.py` contains one `print`, so `vars(arm)` has no `limits`,
so `arm.limits` is an `AttributeError`. Every module you want must be named
in *some* import statement — yours, or one inside `__init__.py`.

### 1.4 What `__init__.py` is for

Normal case: **empty**. It exists so the folder counts as a package.

Second case: it contains imports. If `arm/__init__.py` held
`from . import limits`, then `import arm` alone would run `__init__.py`,
which would load `limits` and write the attribute, and `arm.limits.MAX_ANGLE`
would work after `import arm`. That is the behaviour you expected. Python
does not do it for free; the package author does it by hand as a front
door. LeRobot's `__init__.py` files are full of such lines. (Explained, not
yet demonstrated live — owed.)

### 1.5 `from arm import limits` — same loading, different binding

`from_arm.py`
```python
from arm import limits
print("import done")
print("arm" in vars(), "limits" in vars())
print(limits.MAX_ANGLE)
```
```
arm/__init__.py is running
arm/limits.py is running
import done
False True
180
```

Both files ran, same two `sys.modules` keys. The name `limits` landed;
`arm` did not. One level further, `from arm.limits import MAX_ANGLE` binds
only `MAX_ANGLE`.

**Rule:** `import X` binds the leftmost name; `from X import Y` binds `Y`.
Loading is identical either way.

`quiz1.py` shows the two tables again:
```python
from arm.limits import MAX_ANGLE
print("import done")
print(MAX_ANGLE)
print(arm)
```
```
arm/__init__.py is running
arm/limits.py is running
import done
180
Traceback (most recent call last):
  File "quiz1.py", line 4, in <module>
    print(arm)
NameError: name 'arm' is not defined
```
Module `arm` is loaded and sitting in `sys.modules`. The NAME `arm` is not
in this file. `NameError`, not `ModuleNotFoundError` — that one comes from
the import machinery only, when an `import` statement finds nothing on
`sys.path`. Line 4 is not an import statement.

### 1.6 Absolute vs relative, inside the package

Now the importing file is itself inside `arm` and wants its neighbour.

`arm/safety.py` — **absolute**: the full address from the top folder, the
same line an outside file would write.
```python
from arm.limits import MAX_ANGLE

def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
```

`arm/safety_rel.py` — **relative**: the address from where you are. The
dot is a word meaning **"my own folder."**
```python
from .limits import MAX_ANGLE

def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
```

Python fills the dot in from the importing module's own dotted name:
`safety_rel` was loaded as `arm.safety_rel`; strip the last part; the dot
is `arm`. Two dots `..` = one folder up (said, not shown).

Both, imported from an outside file (`import arm.safety` / `import
arm.safety_rel`), give `clamp(500)` → `180`. `limits.py` runs once, not
twice — the cache.

| | absolute | relative |
|---|---|---|
| names its own package? | yes, `arm` on the line | no |
| rename the folder → | line breaks | line still works |
| cost | none | must be imported AS PART OF the package |

`from . import limits` is the relative spelling of `from arm import limits`.
Not of `import arm.limits` — that binds a different name.

### 1.7 The trap: run directly, the dot has nothing to become

`arm/motion.py`
```python
from . import limits
print("limits" in vars(), "arm" in vars())
print(limits.MAX_ANGLE)
```
`run_motion.py` (an outside file, next to the folder)
```python
import arm.motion
```
```
$ python3 run_motion.py
arm/__init__.py is running
arm/limits.py is running
True False
180

$ python3 arm/motion.py
Traceback (most recent call last):
  File "arm/motion.py", line 1, in <module>
    from . import limits
ImportError: attempted relative import with no known parent package
```

Run A loads `motion.py` **under the name `arm.motion`**; the dot becomes
`arm`. Run B opens `motion.py` directly as the script; a script is always
loaded as **`__main__`**, which you own; no `arm.` in front, so the dot has
nothing to become. Same file, two names, depending on how it was started.

**Rule to carry:** a relative import is filled in from the module's dotted
name. A script run directly has no dotted name.

`python3 -c '...'`, defined because it confused you: run the quoted text as
Python code instead of a file. Nothing else differs. Retired from demos.

---

## 2. THINKING GAPS THIS SESSION — with classification

All from [TEACH-BACK]s, same-day. Nothing on the ledger. Listed because two
of them repeat.

1. **`import arm.limits` binds the name `arm.limits`** — said in S43
   ([PREDICT]) and again today. **Knowledge gap, repeated.** A name has no
   dots. Likely cause: you read `arm.limits` as one token because that is
   how you type it. The 8 Sep cold ask targets this; if it fails, you run
   `print("arm" in vars(), "limits" in vars())` yourself.
2. **`from . import limits` → `import arm.limits`** — wrong absolute form.
   **Knowledge gap**, same root as 1: the two forms bind different names and
   you treated them as interchangeable.
3. **`print(arm)` with no such name → "ModuleNotFound"** — label reached
   from the wrong table. `NameError` is [x] on your ledger; this is a WATCH.
   **Structural flaw** (which table am I in?), not a missing label.
4. **"the syntax is valid" for "run `python3 arm/motion.py`"** — answered a
   different, easier question. **Lazy thinking / surface answer**, the S20
   `digit_sum` shape. The restriction had been stated twice.
5. **`sys.modules` half of quiz 1 skipped, then "arm and limits"** — the key
   is the full dotted path. Minor precision.

Correct and worth saying: the package definition; folder.module; the two
`sys.modules` keys once the loaded/bound split was named; the namespace
after `from arm.limits import MAX_ANGLE`; the output order every time.

## 3. TEACHING MISTAKES THIS SESSION

1. **Pushback 81, part-upheld.** The S43 question "what did `import
   arm.limits` import?" and "what name got bound?" were run together. Two
   tables, two questions; say which.
2. **Pushback 82, upheld.** Bare `vars()` used untaught (define-before-use,
   substrate included), and a name-the-error ask fired while you were
   mid-doubt. Fix: define, then explain the run line by line, no question.
3. **`python3 -c` used undefined for four turns.** Second substrate breach
   in an hour. Fix: defined, then replaced with a real file
   (`run_motion.py`). The checklist has to cover every token on a demo line.
4. **Pushback 83, upheld.** Absolute/relative first explained as "addresses"
   in prose. What landed: the folder tree, then one sentence per form, then
   a one-line difference. Physical-first, side by side, is the default now.
5. One claim stated before it was run (`sys.modules` under `from arm import
   limits`). Right, but run first anyway.

Held: gate from the repo; every file announced by path with its code; no
file overwritten unseen; no ratings on same-day material; every block
tagged; quizzes given when you asked and tagged [TEACH-BACK].

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | The trap |
|---|---|---|
| package | a folder with `__init__.py`; its `.py` files are modules | `import pkg` does NOT load the modules inside |
| `__init__.py` | runs first; becomes the module object for the package | usually empty; non-empty = the front door |
| `import a.b` | runs `a/__init__.py` then `a/b.py`; binds the name `a` | the bound name is `a`, never `a.b` |
| `from a import b` | same loading; binds `b` | `a` is NOT in your file afterwards |
| `sys.modules` keys | full dotted path, `"a"`, `"a.b"` | fixed by disk position, not by how you wrote the import |
| `vars()` (no arg) | namespace dict of the file you are in | — |
| absolute import | `from a.b import X`; names the top folder | breaks if the folder is renamed |
| relative import | `from .b import X`; dot = "my own folder" | only works when imported AS PART OF the package |
| run-directly trap | `python3 a/b.py` loads the file as `__main__` | `ImportError: attempted relative import with no known parent package` |
| `ModuleNotFoundError` | import machinery found nothing on `sys.path` | a missing NAME is `NameError`, not this |
| `python3 -c '...'` | run the quoted text as code instead of a file | retired from demos |

## 5. NEXT
Cold asks on packages and relative imports (8 Sep), targeting the bound
name. Cache cold ask as the gate, then circular imports, then stdlib and
pip. The overdue volley (49 rows) between units — it was not run
today. `notes/voice_teach_packages_relative_imports.md` is your web file;
that pass does not count on the ledger.
