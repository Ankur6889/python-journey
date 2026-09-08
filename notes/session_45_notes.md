# Session 45 — notes (Mon 7 Sep 2026, 21:37 → ~22:10; paused; Tue 8 Sep ~08:50 → ~11:00; paused; ~21:05 → 22:24)

**What this session was:** you opened it 18 minutes after S44 closed, saying
you were uncomfortable with `sys.modules` since the `arm.limits` question.
The whole first two blocks went to that discomfort, one physical demo per
idea, until you could state the rule yourself: the `sys.modules` key is the
ROUTE Python walked from a `sys.path` folder to the file, and the name bound
in your file is decided by the word after `import`. You asked for a re-walk
of absolute vs relative imports and a quiz on it; the quiz found the same
two misses as S44 (the absolute form of `from . import limits`, and the
run-directly trap), and you asked to park the first one. Then circular
imports were taught and closed as taught material, with both fixes. The
standard library was opened and its first two ideas taught, including the
REAL front-door `__init__.py` in `json`, which pays a debt from S44.

Result: no cold asks fired, no ratings taken, no promotions. Three blocks
across two calendar days; all of it same-sitting relative to the material
being re-taught, so nothing is ledger evidence. Two curriculum bullets
[ ] → [~] (circular imports; the standard library). Four queue rows added.
Pushbacks 84 (part), 85, 86, 87 — all upheld or part-upheld.

---

## SELF-TEST — do this first, notes closed

Folder `arm/` holds `__init__.py` (prints a line), `limits.py` (prints a
line, `MAX_ANGLE = 180`), `safety_rel.py` (`from .limits import MAX_ANGLE`).

1. `python3 arm/safety_rel.py`, run from the folder above `arm/`. What is
   printed, or what breaks, on which line, and why in terms of the ROUTE?
2. Same file reached by `import arm.safety_rel` from an outside file. Full
   output, and what is `safety_rel`'s `__name__` now?
3. A file inside `arm/` says `import limits` (no dot) and is run directly.
   Which key lands in `sys.modules`, and does `__init__.py` run?
4. `import arm` alone. How many keys land in `sys.modules`, and what is in
   `vars(arm)` afterwards? Why did `import json` behave differently?
5. Two files: `a.py` does `from b import helper` on line 2 and `X = 1` on
   line 3; `b.py` does `from a import X` on line 2. `main.py` imports `a`.
   Which print lines appear, what is the error, and why is it NOT an
   infinite loop?
6. Name the two fixes for question 5, and say which one a reviewer wants.
7. What is `__file__`?

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

### 1.1 `sys.modules` is a plain dict (`teaching/s45_cache/`)

`see_modules.py`, next to a copy of the S39 `robot.py`:
```python
import sys

print(type(sys.modules))
print("robot" in sys.modules)

import robot

print("robot" in sys.modules)
print(sys.modules["robot"])
```
```
<class 'dict'>
False
robot.py is running
True
<module 'robot' from '.../teaching/s45_cache/robot.py'>
```
Key: the module's name as a string. Value: the module object built by
running the file. Before the import the key is absent; after, present.

### 1.2 A package import puts TWO keys in (`teaching/s43_packages/see_arm.py`)

```python
import sys

print([k for k in sys.modules if k.startswith("arm")])

import arm.limits

print([k for k in sys.modules if k.startswith("arm")])
print(sys.modules["arm"])
print(sys.modules["arm.limits"])
```
```
[]
arm/__init__.py is running
arm/limits.py is running
['arm', 'arm.limits']
<module 'arm' from '.../arm/__init__.py'>
<module 'arm.limits' from '.../arm/limits.py'>
```
Two files ran, two module objects, two keys. The key is the file's position
on disk with dots for slashes: `arm/__init__.py` → `"arm"`,
`arm/limits.py` → `"arm.limits"`.

### 1.3 The bound name is `arm`; `arm.limits` is two steps (`see_names.py`)

```python
import arm.limits

print("arm" in vars())
print("limits" in vars())
print("arm.limits" in vars())

print("limits" in vars(arm))
print(arm.limits.MAX_ANGLE)
```
```
arm/__init__.py is running
arm/limits.py is running
True
False
False
True
180
```
A name has no dots. `arm.limits.MAX_ANGLE` is: look up the name `arm`, ask
that module object for attribute `limits`, ask that for `MAX_ANGLE`. The
attribute `limits` was written onto `arm` when `limits.py` finished running.

Two tables, side by side:
```
sys.modules (LOADED, one per program)     your file's namespace (BOUND, one per file)
  "arm"        -> module                    arm -> module
  "arm.limits" -> module
```

### 1.4 `__init__.py` does NOT load the folder (`see_arm_ns.py`, `only_arm.py`)

```python
import sys
import arm

print([k for k in sys.modules if k.startswith("arm")])
print([k for k in vars(arm) if not k.startswith("__")])

import arm.limits

print([k for k in sys.modules if k.startswith("arm")])
print([k for k in vars(arm) if not k.startswith("__")])
```
```
arm/__init__.py is running
['arm']
[]
arm/limits.py is running
['arm', 'arm.limits']
['limits']
```
After `import arm` alone: one key, empty namespace. Python does not scan
the folder. A submodule enters `sys.modules`, and becomes an attribute of
its package, only when some import line names it: yours, or one inside
`__init__.py`. `only_arm.py` shows the cost: `arm.limits.MAX_ANGLE` →
`AttributeError: module 'arm' has no attribute 'limits'`.

### 1.5 The key is the ROUTE, not the file (`arm/direct.py`)

```python
import sys
print(sys.path[0])

import limits

print([k for k in sys.modules if "limits" in k or k == "arm"])
print(limits.MAX_ANGLE)
```
```
$ python3 arm/direct.py
/home/ankur/Desktop/python-journey/teaching/s43_packages/arm
arm/limits.py is running
['limits']
180
```
| Start folder (`sys.path[0]`) | Route to the file | Key | `__init__.py` runs? |
|---|---|---|---|
| `s43_packages/` | enter `arm/`, then `limits.py` | `arm.limits` | yes |
| `s43_packages/arm/` | `limits.py` directly | `limits` | no |

Same file on disk, two keys, depending on where the search started. If
both routes happen in one program, Python holds TWO module objects for one
file, each with its own `MAX_ANGLE`. Real bug class in research code.

### 1.6 Absolute vs relative, restated (`arm/p1.py`, `p2.py`, `p3.py`)

Each probe is inside `arm/`, run via a one-line outside runner
(`import arm.pN`), and prints the `sys.modules` keys and then
`"MAX_ANGLE" in vars(), "limits" in vars(), "arm" in vars()`.

| Line inside `arm/` | Rewritten to | `sys.modules` keys | Name bound |
|---|---|---|---|
| `from arm.limits import MAX_ANGLE` (p3) | already absolute | `arm`, `arm.p3`, `arm.limits` | `MAX_ANGLE` |
| `from .limits import MAX_ANGLE` (p1) | `from arm.limits import MAX_ANGLE` | `arm`, `arm.p1`, `arm.limits` | `MAX_ANGLE` |
| `from . import limits` (p2) | `from arm import limits` | `arm`, `arm.p2`, `arm.limits` | `limits` |

The dot is rewritten to `arm` BEFORE any loading, from the importing
module's own `__name__` (`arm.p1`, strip the last part). There is never a
key `"limits"` from a relative import. The bound name follows the word
after `import`:
```
import X.Y          binds the LEFTMOST word:      X
from X import Y     binds the word after import:  Y
```
Relative buys rename-safety only. LeRobot uses it because the package is
large and moves.

### 1.7 `__main__` is a placeholder name (`arm/whoami.py`)

```python
import sys
print("my __name__ is:", __name__)
print("__main__" in sys.modules, "arm.whoami" in sys.modules)
```
```
$ python3 arm/whoami.py
my __name__ is: __main__
True False

$ python3 run_whoami.py          # contains: import arm.whoami
arm/__init__.py is running
my __name__ is: arm.whoami
True True
```
Every module carries `__name__`, a string set before line 1 runs. Reached
by import: the route. Run directly: the fixed word `"__main__"`, because the
starting file has no route. There is exactly one `__main__` per program.

### 1.8 The run-directly trap, from the route (`arm/safety_rel.py`)

```
$ python3 arm/safety_rel.py
  File ".../arm/safety_rel.py", line 1, in <module>
    from .limits import MAX_ANGLE
ImportError: attempted relative import with no known parent package
```
Run directly: `sys.path[0]` is `arm/` itself, nothing entered `arm`, no
`__init__.py`, the file's name is `__main__`. Strip the last part off
`__main__` and nothing is left, so the dot cannot become `arm`.
```
$ python3 run_safety_rel.py      # import arm.safety_rel; print name; clamp(200)
arm/__init__.py is running
arm/limits.py is running
arm.safety_rel
180
```
Rule: a relative import needs the file to have a dotted name, and a file
only gets a dotted name by being reached through its folder.

### 1.9 Circular imports (`teaching/s45_circular/`)

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
`main.py`: `import a` then `print("main done")`.
```
$ python3 main.py
a.py starting
b.py starting
Traceback (most recent call last):
  File ".../main.py", line 1, in <module>
    import a
  File ".../a.py", line 2, in <module>
    from b import helper
  File ".../b.py", line 2, in <module>
    from a import X
ImportError: cannot import name 'X' from partially initialized module 'a' (most likely due to a circular import)
```
The key `"a"` enters `sys.modules` BEFORE `a.py` line 1 runs. Proof,
`self_check.py` (imported by `run_self_check.py`):
```python
import sys
print("self_check.py line 2, still running")
print("self_check" in sys.modules)
print(vars(sys.modules["self_check"]).get("X"))
X = 1
print("self_check.py done")
```
```
self_check.py line 2, still running
True
None
self_check.py done
```
So at `b.py` line 2 the cache HITS and hands back a half-built `a` with no
`X`. One lookup, one failure. NOT an infinite loop: the early key is what
prevents the loop; the price is a half-built module on a hit. The error is
`ImportError` because `from a import X` is an attribute lookup on the module
object done by the import machinery, not a name lookup in `b.py`.

**Fix 1 (the real one):** move `X` to a third module both import. No cycle.
**Fix 2 (the patch, `fix/b.py`):** move the import inside the function.
```python
print("b.py starting")
def helper():
    from a import X
    return X
print("b.py done")
```
```
$ python3 fix/main.py            # import a; print("main done"); print(a.helper())
a.py starting
b.py starting
b.py done
a.py done
main done
1
```
A `def` body does not run at import time, so the lookup happens after `a`
is complete. When you see an import inside a function in research code,
this is why.

### 1.10 The standard library on disk (`teaching/s45_stdlib/`)

New token: **`__file__`** is a string every module carries, the path on
disk it was built from.

`where_is.py`
```python
import sys
import json

print(json.__file__)
print(sys.path)
```
```
/usr/lib/python3.12/json/__init__.py
['/home/ankur/Desktop/python-journey/teaching/s45_stdlib',
 '/opt/ros/jazzy/lib/python3.12/site-packages',
 '/usr/lib/python312.zip',
 '/usr/lib/python3.12',
 '/usr/lib/python3.12/lib-dynload',
 '/usr/local/lib/python3.12/dist-packages',
 '/usr/lib/python3/dist-packages']
```
`json` was found from the fourth `sys.path` entry: enter `json/`, hit
`__init__.py`. A package, same rule as `arm`. That folder holds 202
readable entries.

`json/__init__.py` lines 106–108, unedited:
```python
from .decoder import JSONDecoder, JSONDecodeError
from .encoder import JSONEncoder
import codecs
```
`front_door.py`
```python
import sys
import json

print([k for k in sys.modules if k.startswith("json")])
print([k for k in vars(json) if not k.startswith("_")])
print(json.decoder.__file__)
```
```
['json.scanner', 'json.decoder', 'json.encoder', 'json']
['scanner', 'decoder', 'JSONDecoder', 'JSONDecodeError', 'encoder', 'JSONEncoder', 'codecs', 'dump', 'dumps', 'detect_encoding', 'load', 'loads']
/usr/lib/python3.12/json/decoder.py
```
One `import json` → four keys (`json.scanner` because `decoder.py` imports
it) and twelve names on `json`. That is the front door: `__init__.py` pulls
the submodules up so the user needs one name. Compare `arm`, whose
`__init__.py` only printed, so `import arm` loaded nothing else. This is
the LeRobot pattern (`from lerobot.policies import ACTPolicy`).

---

## 2. THINKING GAPS THIS SESSION — with classification

All same-sitting relative to the material, so none is ledger evidence.
Listed because the SHAPE matters.

1. **Absolute form of `from . import limits` → `import arm.limits`. THIRD
   time (S43, S44, S45).** Knowledge gap on the `import X.Y` vs `from X
   import Y` binding rule, not on packages. You asked to park it; it was
   parked WITH the answer (`from arm import limits`). Comes back cold.
2. **Run-directly trap answered as the import path, second time.** Asked
   what `python3 arm/safety_rel.py` prints, you gave the two `running`
   lines. Lazy-thinking class (depth-before-answer): the route was not
   checked before answering. Once the route rule was stated you reasoned
   it correctly and predicted `run_safety_rel.py` in full.
3. **"kind of an infinite loop"** on the circular import. Structural flaw
   in the model, corrected: the early key is what PREVENTS the loop.
4. **"the key goes in after `a` finishes"** — structural, corrected with
   `self_check.py`. This one is subtle and reasonable to have assumed.
5. **`NameError` for a failed `from a import X`** — label from the wrong
   table (name lookup vs attribute lookup by the import machinery). Not
   logged; you had not seen the error.
6. **Earlier: "does relative import put `limits` in `sys.modules`?"** —
   resolved by the probes; you then stated the route rule cleanly.

Correct and unprompted: `sys.modules` definition; two-keys reasoning;
**bound name `arm` for `import arm.limits` — right for the first time**;
the route rule; `run_safety_rel.py` full output; `def` body not run at
import; `json` package identification.

## 3. TEACHING MISTAKES THIS SESSION

1. **Referred to a file that did not exist** (`run_safety_rel.py`) as if it
   were on disk. Pushback 85, upheld. Files are announced by path WITH code
   after they are created, never before.
2. **A question that pointed back at earlier output** instead of carrying
   its full scenario. Pushback 86, upheld. S19 rule.
3. **A [PREDICT] that asked you to NAME an error you had never seen.**
   Pushback 87, upheld. Predicting print lines from a walk is fair;
   predicting an unseen label is guessing.
4. **The interval gate was stated once, at 21:37 Mon, and not re-stated
   when blocks 2 and 3 began on Tue.** No harm to the ledger (nothing was
   rated), but the gate is per-block as well as per-material.
5. **The loaded/bound split has now failed to land across three sessions.**
   The route rule (1.5) is the version that finally produced a clean
   restatement from you; the two-tables picture alone did not. Use the
   route first next time.
6. Sequencing pushback 84 (part): nothing was skipped, but jumping to
   circular before the re-walk was the wrong read of why you opened.

Held clean: every demo written as a file (no `-c`); `test -e` before
every write; every snippet run before its output was shown; no ratings on
same-day material; [TEACH-BACK]/[PREDICT] tagged; the parked item was
parked with its answer; direct questions answered directly.

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | The trap |
|---|---|---|
| `sys.modules` | dict, key = module name string, value = module object; one per program | the key enters BEFORE the file runs |
| the key | the ROUTE from a `sys.path` folder to the file, dots for slashes | same file can be `limits` or `arm.limits`; two objects |
| the bound name | `import X.Y` → `X`; `from X import Y` → `Y` | a name has no dots; `arm.limits` is a lookup |
| `__init__.py` | makes a folder a package; runs when the folder is ENTERED | does not load the folder's files; empty is normal |
| front door | imports inside `__init__.py` pull submodules onto the package | `json` does it; `arm` did not |
| relative import | the dot = "my own folder", filled from `__name__` | run directly → `__main__` → no parent → `ImportError` |
| `__name__` | string set before line 1; the route, or `"__main__"` | `__main__` is a placeholder, not a filename |
| `__file__` | path on disk the module was built from | — |
| circular import | second import hits a half-built module | `ImportError: cannot import name ... partially initialized` |
| the two fixes | third module (real); import inside the function (patch) | an in-function import means someone left a cycle |
| stdlib | `/usr/lib/python3.12/`, ordinary `.py` files, on `sys.path` | packages there follow the same route rule |

## 5. NEXT

- Doubt gate on stdlib idea 2; the held teach-back (why `arm` empty, `json`
  twelve names). Then pip / site-packages (~20 min), `enumerate()` defined.
- Cold asks, legal from 10 Sep: packages bound name; `from . import limits`
  absolute form (parked); run-directly trap; circular; `__main__` route.
- The overdue volley on older material. Fire a block of 8 first next time.
