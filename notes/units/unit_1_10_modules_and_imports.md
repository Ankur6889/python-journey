# Unit 1.10 — Modules, Packages, and Imports

What `import` does, the cache, `sys.path`, `__name__`, packages,
absolute vs relative imports, circular imports, the standard library on disk,
and pip / site-packages / shadowing.

---

## 1. What a module is

**A module is a `.py` file.** That is the whole definition.

Why they exist: separate files get separate **namespaces**, so names stop
colliding; and it is how you use code you did not write (the standard
library, pip packages). Not "it organises your code" — splitting a 200-line
script into six files makes it worse. What it buys you: the import block at
the top of any file is that file's **dependency list**.

---

## 2. THE SENTENCE

> **`import` is executable code. It runs a file, top to bottom, ONCE per
> process — and then binds a name.**

Everything strange about imports falls out of that.

### 2.1 Import is a RUN, not a fetch

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

Nothing in `main.py` calls that `print`. `import robot` **executed `robot.py`
like a program**, and the print sits at its top level.

### 2.2 ONCE per process — the cache

`twice.py`
```python
import robot
print("first import done")
import robot
print("second import done")
print(robot.MAX_ANGLE)
```
```
robot.py is running          <-- once, not twice
first import done
second import done
180
```

**Cache** (from French *cacher*, to hide): a stash of results already worked
out, kept so the work is not done twice. Python keeps a **dict in memory**,
`sys.modules`, mapping module name → module object.

**Every import statement runs two independent steps:**

| Step | What happens |
|---|---|
| **1 — get the module object** | Check `sys.modules`. **Miss:** find the file, run it top to bottom, store the result. **Hit:** take the stored object, **no re-run**. |
| **2 — bind name(s) in YOUR namespace** | Just an assignment. **Always runs**, hit or miss. The *form* of the statement decides which names. |

A cache hit does not mean the import did nothing; it means step 1 was free.
The practical bite: editing a `.py` file and re-running `import` in a live
notebook **does not pick up the edit** — the cache hits and the new code
never runs.

```python
import sys
print(type(sys.modules))            # <class 'dict'>
print("robot" in sys.modules)       # False
import robot                        # robot.py is running
print("robot" in sys.modules)       # True
print(sys.modules["robot"])         # <module 'robot' from '.../robot.py'>
```

### 2.3 An import binds ONE name — not "all the names"

```python
import robot
print(MAX_ANGLE)
# NameError: name 'MAX_ANGLE' is not defined
```

`import robot` binds exactly one name, `robot`. `MAX_ANGLE` is fully alive
*inside* `robot`'s namespace; **the dot is the only route in.** That is the
collision protection: two modules can both define `clamp` and never clash.

### 2.4 The four forms — one machine, four labels

| You write | Runs `robot.py`? | Name(s) bound in YOUR namespace |
|---|---|---|
| `import robot` | yes | `robot` |
| `import robot as r` | yes | `r` |
| `from robot import clamp` | yes — **the whole file** | `clamp` |
| `from robot import clamp as c` | yes | `c` |

`from robot import clamp` runs the entire file: `clamp` does not exist until
the `def` line executes. **There is no way to get one name out of a module
without running the module.** Only step 2 differs.

```python
from robot import clamp
print(clamp(200))           # 180
print(robot.MAX_ANGLE)      # NameError: name 'robot' is not defined
```

**Aliasing REPLACES the name; it does not add a nickname beside it:**

```python
import robot as r
print(r.clamp(200))         # 180
print(robot.MAX_ANGLE)      # NameError: name 'robot' is not defined
```

Rule: `import X.Y` binds the **leftmost** word (`X`); `from X import Y` binds
the word **after `import`** (`Y`). `as` renames whichever it is.

### 2.5 A module IS an object; its namespace IS a dict

```python
import robot
print(type(robot))              # <class 'module'>
print(vars(robot).keys())
# dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__',
#            '__file__', '__cached__', '__builtins__', 'MAX_ANGLE', 'clamp'])
print(vars(robot)["MAX_ANGLE"]) # 180
```

- `vars(obj)` hands you the object's namespace dict (`__dict__`) — the actual
  dict, not a copy. `vars()` with no argument is the namespace of the file
  you are standing in.
- Your names are at the end, in the order `robot.py` created them; the
  dunders were put there by Python.
- A function call's namespace dies on return; a module's namespace
  **persists** for the whole process, held alive by the cache.
- `__file__` is a string every module carries: the path on disk it was built
  from. `__name__` is the module's name (§3).

**Subscription vs attribute access.** `d["k"]` looks in an object's
**contents**; `obj.k` looks in its **namespace** (`__dict__`). They coincide
for a **module only**, because a module's contents *are* its namespace. A
plain dict has no `__dict__`:

```python
d = {"MAX_ANGLE": 180}
print(d["MAX_ANGLE"])   # 180
print(d.MAX_ANGLE)      # AttributeError: 'dict' object has no attribute 'MAX_ANGLE'
print(vars(d))          # TypeError: vars() argument must have __dict__ attribute
```

`robot.MAX_ANGLE` is a lookup in the module's namespace dict — not because
dots do dict lookups, but because a module's namespace *is* that dict.

---

## 3. `__name__` and `__main__`

The problem: a file with a self-test at the bottom.

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

Import runs the file; you cannot opt out. Swap that `print` for
`run_calibration()` and importing a file to reuse one function launches the
robot.

**The mechanism.** Every module carries a string `__name__`, set before line
1 runs. The same file reports a different value depending on how it was
reached:

| How the file was reached | `__name__` |
|---|---|
| **imported** | the module's own name (its route), e.g. `"sensors"`, `"arm.limits"` |
| **handed to `python3`** | the fixed word `"__main__"` |

`__main__` is a **placeholder name**, not a filename: it belongs to whichever
file you launched. There is exactly one `__main__` per program.

**The fix:**

`sensors.py`
```python
def read_angle():
    return 200

if __name__ == "__main__":
    print("SELF-TEST:", read_angle())
```
```
$ python3 sensors.py
SELF-TEST: 200
$ python3 app.py
app is doing real work
```

**The guard goes in the file that gets IMPORTED**, to protect it from its own
top-level code running when someone imports it. The file you actually run
needs no guard. That block at the bottom of nearly every serious Python file
is this and nothing more: an `if` on a string.

---

## 4. `sys.path` — where Python looks for the file

`sys` is a module that ships with Python; inside it is a variable `path`
holding a **list of folder-name strings**. That is all `sys.path` is.

```
>>> import sys
>>> type(sys.path)
<class 'list'>
```

Python will not search your whole disk for `robot.py`. It searches **only**
the folders in this list, **in order, stopping at the first hit**. On this
machine, from the repo root:

```
$ python3 -c "import sys; print(sys.path)"
['', '/opt/ros/jazzy/lib/python3.12/site-packages', '/usr/lib/python312.zip',
 '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload',
 '/usr/local/lib/python3.12/dist-packages', '/usr/lib/python3/dist-packages']
```

- **Built fresh every time a process starts.** Not a history of where you
  have run Python.
- **Slot 0 is the folder the SCRIPT you ran lives in** — not where the
  terminal is. In a REPL or `python3 -c` there is no script, so slot 0 is
  `''`, meaning "the folder the terminal is in".
- Slots 1–6 are the installation's folders: the stdlib, `site-packages`, and
  here the ROS Jazzy `site-packages` (added by `source setup.bash`).

```python
import s22_counter     # from the repo root; the file is in drills/
# ModuleNotFoundError: No module named 's22_counter'
```

The file exists; `drills/` is not on the list; the import fails. **Every
`ModuleNotFoundError` means: not in any folder on `sys.path`.**

**Two fixes:**

1. Put the files side by side, so slot 0 covers both. What real projects do.
2. Add the folder to the list, **before** the import line (`import` reads
   the list at the moment it runs):

```python
import sys
sys.path.append("/home/ankur/Desktop/python-journey/drills")   # a string; ~ is NOT expanded
import s22_counter
print(s22_counter.__file__)
# /home/ankur/Desktop/python-journey/drills/s22_counter.py
```

`sys.path.append(...)` is `.append()` on a list. It is the route rule by hand
and a **smell** in a real repo; the clean fix is `pip install -e .` (an
editable install — named, not yet shown). `import ~/tools/helper.py` is a
`SyntaxError`: `import` takes a **name**, never a path.

---

## 5. The whole import story — five steps

`import robot`, first time in this process:

1. Look in **`sys.modules`** (dict in memory). Key `"robot"` absent. Miss.
2. **Find** the file: walk the folders in `sys.path`; the first holding
   `robot.py` (or a folder `robot/`) wins.
3. **Compile**: if `__pycache__/robot.cpython-312.pyc` exists and its stamp
   matches `robot.py`, load it and skip compiling; otherwise compile and write
   it.
4. **Run** the bytecode top to bottom into a fresh namespace. Module-level
   prints fire; names like `MAX_ANGLE` are created.
5. **Store** the module object in `sys.modules["robot"]`. Bind `robot` in
   your file.

Second time in the same process: step 1 hits; bind the name; done.

**Two caches, not one.** `.pyc` is on disk and saves step 3 **across runs**.
`sys.modules` is in memory and saves steps 2–4 **within one run**; it dies
with the process. The `.pyc` details (stamped with the source's mtime and
size, never stale, safe to delete, buys import speed only) are in 1.1 §3.

---

## 6. Packages

A **package** is a **folder** that contains a file named `__init__.py`. That
file's presence is the whole definition; it may be empty. Every `.py` inside
is a module of the package, reached with a dot. **Dots are folder
separators**: `from lerobot.common.policies.act import ACTPolicy` walks folder
`lerobot` → folder `common` → folder `policies` → file `act.py`.

```
teaching/s43_packages/
    use_arm.py   only_arm.py   from_arm.py
    arm/
        __init__.py     # print("arm/__init__.py is running")
        limits.py       # print("arm/limits.py is running"); MAX_ANGLE = 180
```

### 6.1 `import arm.limits` — two tables

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

`__init__.py` runs first and becomes the module object `arm`. Then
`limits.py` runs and becomes `arm.limits`. Then `limits` is written as an
**attribute** onto `arm`.

| Table | What lands | Same for every import form? |
|---|---|---|
| `sys.modules` (what got **LOADED**, one per program) | keys `"arm"` and `"arm.limits"` | **yes** — fixed by position on disk |
| your file's namespace (what got **BOUND**, one per file) | the ONE name `arm` | **no** — decided by how you wrote the line |

```python
import sys, arm.limits
print([k for k in sys.modules if k.startswith("arm")])   # ['arm', 'arm.limits']
print("arm" in vars(), "limits" in vars(), "arm.limits" in vars())   # True False False
print(vars(arm)["limits"] is sys.modules["arm.limits"])  # True — same object
print(arm)          # <module 'arm' from '.../arm/__init__.py'>
print(arm.limits)   # <module 'arm.limits' from '.../arm/limits.py'>
```

**A name in a namespace has no dots.** `arm.limits.MAX_ANGLE` is one name
lookup (`arm`) followed by two attribute lookups. **The object `arm` IS
`__init__.py`** — which is why it runs first: the package's module object
must exist before `limits` can be hung off it.

**A folder is not code.** `import arm` must build a module *object*, and an
object is built by running a file into a namespace; so one file stands for
the folder: `__init__.py`.

### 6.2 `import arm` alone does NOT load the modules inside

`only_arm.py`
```python
import arm
print("arm" in vars(), "limits" in vars())
print(arm.limits.MAX_ANGLE)
```
```
arm/__init__.py is running
True False
Traceback (most recent call last):
  File "only_arm.py", line 3, in <module>
    print(arm.limits.MAX_ANGLE)
AttributeError: module 'arm' has no attribute 'limits'
```

`import arm` runs `__init__.py` and **stops**. Python does not scan the
folder. A submodule enters `sys.modules`, and becomes an attribute of its
package, only when **some import line names it** — yours, or one inside
`__init__.py`.

### 6.3 What `__init__.py` is for — the front door

Normal case: **empty**; it exists so the folder counts as a package. Second
case: it holds imports that pull the folder's files up onto the package, so
the user needs one name. The real `json` package does this:

`/usr/lib/python3.12/json/__init__.py`, lines 106–108:
```python
from .decoder import JSONDecoder, JSONDecodeError
from .encoder import JSONEncoder
import codecs
```
```python
import sys, json
print([k for k in sys.modules if k.startswith("json")])
# ['json.scanner', 'json.decoder', 'json.encoder', 'json']
print([k for k in vars(json) if not k.startswith("_")])
# ['scanner', 'decoder', 'JSONDecoder', 'JSONDecodeError', 'encoder', 'JSONEncoder',
#  'codecs', 'dump', 'dumps', 'detect_encoding', 'load', 'loads']
```

One `import json` → four keys and twelve names. Imports **chain**:
`__init__.py` → `decoder.py` → (`from json import scanner` on its line 5) →
`scanner.py`. Compare `arm`, whose `__init__.py` only printed. This is the
LeRobot pattern (`from lerobot.policies import ACTPolicy`).

### 6.4 `from arm import limits` — same loading, different binding

```python
from arm import limits
print("arm" in vars(), "limits" in vars())    # False True
print(limits.MAX_ANGLE)                       # 180
```

Both files ran, same two `sys.modules` keys; the name `limits` landed, `arm`
did not. One level further, `from arm.limits import MAX_ANGLE` binds only
`MAX_ANGLE` — and then `print(arm)` is a **`NameError`**, not
`ModuleNotFoundError`: the module is loaded and sitting in `sys.modules`; the
*name* is not in this file. `ModuleNotFoundError` comes only from the import
machinery when an `import` statement finds nothing on `sys.path`.

### 6.5 Key order in `sys.modules`

A module's key enters `sys.modules` **early**, before its line 1 runs (this is
what stops circular imports looping, §8). When the module's run **finishes**,
its key is moved to the **end**. So a package that imports its own files
finishes last: mid-run the order is `p`, `p.inner`; afterwards `p.inner`, `p`.

---

## 7. Absolute vs relative imports, and the route rule

Now the importing file is itself inside `arm/` and wants its neighbour.

`arm/safety.py` — **absolute**: the full address from the top folder, the
same line an outside file would write.
```python
from arm.limits import MAX_ANGLE
```
`arm/safety_rel.py` — **relative**: the address from where you are. **The dot
means "my own package."**
```python
from .limits import MAX_ANGLE
```

Python fills the dot in **by name**, from the importing module's own dotted
`__name__`: `safety_rel` was loaded as `arm.safety_rel`; strip the last part;
the dot is `arm`. The rewrite happens **before** any loading. Two dots `..`
mean one package up.

| Line inside `arm/` | Rewritten to | Name bound |
|---|---|---|
| `from .limits import MAX_ANGLE` | `from arm.limits import MAX_ANGLE` | `MAX_ANGLE` |
| `from . import limits` | `from arm import limits` | `limits` |

`from . import limits` is the relative spelling of `from arm import limits`
— **not** of `import arm.limits`, which binds a different name.

| | absolute | relative |
|---|---|---|
| names its own package? | yes, `arm` on the line | no |
| rename the folder → | the line breaks | still works |
| cost | none | must be imported **as part of** the package |

### 7.1 The trap: run directly, the dot has nothing to become

`arm/motion.py`
```python
from . import limits
print(limits.MAX_ANGLE)
```
```
$ python3 run_motion.py          # contains: import arm.motion
arm/__init__.py is running
arm/limits.py is running
180

$ python3 arm/motion.py
Traceback (most recent call last):
  File "arm/motion.py", line 1, in <module>
    from . import limits
ImportError: attempted relative import with no known parent package
```

Reached by import, `motion.py` is loaded **under the name `arm.motion`**; the
dot becomes `arm`. Run directly, the file is the script: `sys.path[0]` is
`arm/` itself, nothing entered `arm`, `__init__.py` did not run, and the
file's name is `__main__`. Strip the last part off `__main__` and nothing is
left. **A relative import needs the file to have a dotted name, and a file
only gets a dotted name by being reached through its folder.**

```python
# arm/whoami.py
print("my __name__ is:", __name__)
# $ python3 arm/whoami.py      -> my __name__ is: __main__
# $ python3 run_whoami.py      -> arm/__init__.py is running / my __name__ is: arm.whoami
```

### 7.2 The `sys.modules` key is the ROUTE, not the file

`arm/direct.py`
```python
import sys
print(sys.path[0])
import limits                   # no dot, no arm
print([k for k in sys.modules if "limits" in k or k == "arm"])
```
```
$ python3 arm/direct.py
/home/ankur/Desktop/python-journey/teaching/s43_packages/arm
arm/limits.py is running
['limits']
```

| Start folder (`sys.path[0]`) | Route to the file | Key | `__init__.py` runs? |
|---|---|---|---|
| `s43_packages/` | enter `arm/`, then `limits.py` | `arm.limits` | yes |
| `s43_packages/arm/` | `limits.py` directly | `limits` | no |

Same file on disk, two keys, depending on where the search started. If both
routes happen in one program, Python holds **two module objects for one
file**, each with its own `MAX_ANGLE`. A real bug class in research code.

---

## 8. Circular imports

`a.py`
```python
print("a.py starting")
from b import helper
X = 1
print("a.py done")
```
`b.py`
```python
print("b.py starting")
from a import X
def helper():
    return X
print("b.py done")
```
`main.py`: `import a`
```
a.py starting
b.py starting
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    import a
  File "a.py", line 2, in <module>
    from b import helper
  File "b.py", line 2, in <module>
    from a import X
ImportError: cannot import name 'X' from partially initialized module 'a' (most likely due to a circular import)
```

Falls out of import-runs-the-file plus the cache. The key `"a"` enters
`sys.modules` **before** `a.py` line 1 runs (a module can see itself in
`sys.modules` from its own line 2, with none of its names yet). So at `b.py`
line 2 the cache **hits** and hands back a half-built `a` with no `X`. One
lookup, one failure. **Not an infinite loop** — the early key is what
*prevents* the loop; the price is a half-built module on a hit. It is
`ImportError` because `from a import X` is an attribute lookup on the module
object done by the import machinery, not a name lookup in `b.py`.

**Fix 1 (the real one):** move `X` to a third module both import. No cycle.
**Fix 2 (the patch):** move the import inside the function.

```python
# b.py
print("b.py starting")
def helper():
    from a import X         # a def body does not run at import time
    return X
print("b.py done")
```
```
a.py starting / b.py starting / b.py done / a.py done / main done / 1
```

When you see an import inside a function in research code, this is why:
someone left a cycle.

---

## 9. The standard library on disk

The modules and packages that ship with the interpreter (`json`, `sys`, `os`,
`math`, `bisect`, `csv`, `copy`, `traceback`, `pathlib`). Two facts that
matter:

1. It is on disk as ordinary `.py` files, found by the **same route rule** as
   `arm`. `json.__file__` is `/usr/lib/python3.12/json/__init__.py` — the
   fourth `sys.path` entry, a folder, so a package.
2. Its packages use `__init__.py` as a front door (§6.3).

The route, done by hand — one question per `sys.path` folder, in order: *is
there a `json.py` or a `json/` here?*

```
$ ls -d <entry0>/json <entry0>/json.py      # No such file (both)
$ ls -d <entry1>/json <entry1>/json.py      # No such file (both)
$ ls -d <entry2>/json <entry2>/json.py      # No such file (both)
$ ls -d /usr/lib/python3.12/json            # a folder. STOP.
$ ls /usr/lib/python3.12/json/
decoder.py  encoder.py  __init__.py  __pycache__  scanner.py  tool.py
```

First hit wins; later entries are never looked at. You can open and read any
of it. `/usr/lib/python3.12/bisect.py` is 118 lines of pure Python:

```python
def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
        ...  # same loop with key(a[mid])
    return lo
```

Given a **sorted** list `a` and a value `x`, it returns the index where `x`
would go to keep it sorted, by halving the fence `lo`/`hi` each pass — every
binary search. `bisect_left([10, 20, 30, 40], 35)` → pass 1: mid 2, 30 < 35,
lo = 3; pass 2: mid 3, 40 ≥ 35, hi = 3; stop, return 3. The bare `*` in the
signature is the keyword-only fence (1.7 §2.2).

---

## 10. pip, site-packages, and shadowing

`pip install numpy` downloads the package and **copies its folder into a
folder that is already on `sys.path`**, called `site-packages`
(`dist-packages` on Ubuntu). No third tier; the route rule does not change,
which is why `import numpy` then works with no change to your code.

```python
import sys, json, numpy, rclpy
print(json.__file__)    # /usr/lib/python3.12/json/__init__.py
print(numpy.__file__)   # /usr/lib/python3/dist-packages/numpy/__init__.py
print(rclpy.__file__)   # /opt/ros/jazzy/lib/python3.12/site-packages/rclpy/__init__.py
for i, folder in enumerate(sys.path):
    print(i, folder)
```

Three packages, three `__init__.py`, three folders on the list (entries 3, 6,
1). A `json/` copied into entry 1 would win over the real one at entry 3.

### 10.1 Shadowing — the bug that bites at entry 0

`shadow/json.py`: `print("MY json.py is running")`
`shadow/main.py`:
```python
import json
print(json.__file__)
print(json.loads('{"a": 1}'))
```
```
$ cd shadow && python3 main.py
MY json.py is running
/home/ankur/Desktop/python-journey/teaching/s46_pip/shadow/json.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(json.loads('{"a": 1}'))
AttributeError: module 'json' has no attribute 'loads'
```

Entry 0 is the script's folder; `shadow/json.py` exists; the walk stops; the
stdlib `json` is never opened. Line 1 succeeds (it imported *something* called
`json`); line 3 asks a one-line module for `loads`. The crash lands lines
after the cause. **Never name your own file after a package you import**
(`random.py`, `numpy.py`, `test.py`, `json.py`). The script's folder is not
"checked before `sys.path`" — it **is** `sys.path[0]`.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| module | a `.py` file; its executed namespace wrapped in an object | `type(m)` is `module` |
| `import x` | runs `x.py` once, binds **`x`** | it RUNS the file; top-level code fires |
| `from x import y` | runs `x.py` **in full**, binds **`y`** only | `x` itself is not bound |
| `import x as a` | binds `a` only | aliasing replaces, never adds |
| bound name rule | `import X.Y` → `X`; `from X import Y` → `Y` | a name has no dots; `X.Y` is attribute access |
| `sys.modules` | dict: name → module object; one per program | key enters **before** the file runs; hit skips the run, never the bind |
| the five steps | `sys.modules` → `sys.path` → `.pyc` → run → store | two caches: `.pyc` across runs, `sys.modules` within one |
| `vars(obj)` / `vars()` | the namespace dict of an object / of this file | a plain dict has no `__dict__` |
| `obj.k` vs `d["k"]` | namespace lookup vs contents lookup | they coincide for a module only |
| `__name__` | the route, or `"__main__"` for the launched file | `__main__` is a placeholder, not a filename |
| `if __name__ == "__main__":` | lets a file be script and module | goes in the file being **imported** |
| `__file__` | the path the module was built from | — |
| `sys.path` | list of folders searched in order, first hit wins | slot 0 is the **script's** folder; `''` in a REPL; built fresh per process |
| `ModuleNotFoundError` | nothing on `sys.path` | a missing name is `NameError` |
| `sys.path.append` | the route by hand, before the import | `~` not expanded; a smell |
| package | a folder with `__init__.py` | `import pkg` does NOT load the modules inside |
| `__init__.py` | stands for the folder; runs when it is entered | usually empty; non-empty = the front door |
| `import a.b` | runs `a/__init__.py` then `a/b.py`; binds `a` | keys `"a"`, `"a.b"`; `a.b` is an attribute |
| front door | imports inside `__init__.py` chain submodules onto the package | `json.scanner` came from `decoder.py` |
| absolute import | names the top package | breaks if the folder is renamed |
| relative import | `.` = my own package, filled from `__name__` | run directly → `ImportError: no known parent package` |
| the route rule | the key is the path walked from a `sys.path` folder | same file can be two keys → two objects |
| key order | early in; moved to the end on finish | printed order is finish order |
| circular import | second import hits a half-built module | `ImportError: cannot import name ... partially initialized`; not a loop |
| the two fixes | third module (real); import inside the function (patch) | an in-function import means someone left a cycle |
| stdlib | ordinary `.py` files under `/usr/lib/python3.12/`, on `sys.path` | same route rule; readable |
| pip / site-packages | copies a folder into a folder already on `sys.path` | no third tier |
| shadowing | your `json.py` at entry 0 hides the real one | crash lands later as `AttributeError` |
| `python3 -c "..."` | run the quoted text instead of a file | slot 0 is `''` |
