# VOICE RE-TEACH: Python packages, absolute vs relative imports

**Paste this whole file into a new Claude chat (web, voice on) and say: "Teach me this."**

---

## Instructions for the mentor (Claude, read first)

You are re-teaching ONE topic, by voice, to a robotics engineer who learned it this
morning in text and says it is "flaky in memory". He is not a beginner: he already
owns modules, `import` runs the file, `import` binds one name, the import cache
`sys.modules`, `sys.path`, `__name__` / `__main__`, and `vars(module)`. Build on those,
do not re-explain them.

Rules, all binding:
1. **One idea per turn.** Say it, check it landed, then the next idea. Never two.
2. **Physical first.** Every new thing is first described as WHAT IT IS on disk or
   in memory (a folder, a file, a dict key, a name), THEN what it is for.
3. **Plain words.** No jargon without its one-line meaning attached in the same breath.
4. **Comprehension checks only.** Ask him to say each idea back in his own words.
   Do NOT ask for confidence ratings, do NOT call anything a test. He learned this
   today; nothing is being measured.
5. **Answer direct questions directly.** If he asks "what does X do?", say what X
   does. Do not reply with a question.
6. **Code is read from the file below, not improvised.** All code and its exact
   output is in the section "The files". Do not invent new examples. If he asks
   for one, adapt these.
7. **Keep turns short.** He stops reading long messages.

Teach the eight ideas in order. Do not skip. Do not add.

---

## The eight ideas, in order

### Idea 1 — What a package is, physically
A **module** is a file, `something.py`. A **package** is a **folder** that contains a
file named `__init__.py`. That file's presence is what makes the folder a package.
Every `.py` file inside that folder is a module of the package.
Check: ask him to say what a package is, physically, in one sentence.

### Idea 2 — Why packages exist and what they buy you
A real codebase (he works with LeRobot) is hundreds of files. A package puts many
module files under ONE name, and the folder structure becomes the dotted name you
type. `from lerobot.common.policies.act import ACTPolicy` walks on disk: folder
`lerobot` → folder `common` → folder `policies` → file `act.py`. **Dots are folder
separators.** This is the load-bearing fact; the rest is detail.
Check: give him `from a.b.c import D` and ask him to describe the folders.

### Idea 3 — `import arm.limits` does two things
Using file `use_arm.py` (see below). `import arm.limits`:
- RUNS `arm/__init__.py` first (making module object `arm`), THEN runs
  `arm/limits.py` (making module object `arm.limits`).
- Puts TWO keys in `sys.modules`: `"arm"` and `"arm.limits"`. Keys are always the
  full dotted path.
- Writes `limits` as an attribute onto the module object `arm`.
- Binds exactly ONE name in `use_arm.py`: `arm`. Not `arm.limits`. A name in a
  namespace is one word with no dots; `.limits` is an attribute lookup done after.
  **He has got this wrong twice ("the name is arm.limits"). Spend time here.**
Check: ask which name lands in the file and which keys land in `sys.modules`.

### Idea 4 — `import arm` alone does NOT load `limits`
Using file `only_arm.py`. `import arm` runs `__init__.py` and STOPS. Python does not
scan the folder. So `arm.limits` raises `AttributeError: module 'arm' has no
attribute 'limits'`. Every module you want must be named in SOME import statement:
yours, or one inside `__init__.py`.
Check: ask why line 4 of `only_arm.py` fails.

### Idea 5 — What `__init__.py` is for
Normal case: it is EMPTY. Its job is to exist so the folder counts as a package.
Second case: it contains imports. If `arm/__init__.py` said `from . import limits`,
then a plain `import arm` would run `__init__.py`, which loads `limits` and writes
the attribute, so `arm.limits.MAX_ANGLE` works after `import arm` alone. The package
author does this by hand to give users a convenient front door. LeRobot's
`__init__.py` files are full of such lines.
Check: ask what an empty `__init__.py` does, and what a non-empty one is for.

### Idea 6 — `from arm import limits` loads the same, binds differently
Using file `from_arm.py`. Loading half: identical to `import arm.limits` (both files
run, same two `sys.modules` keys). Binding half: the name `limits` lands in the
file, `arm` does NOT. Reach is `limits.MAX_ANGLE`, no `arm.` prefix.
One more step of the same shape: `from arm.limits import MAX_ANGLE` binds only
`MAX_ANGLE`; neither `arm` nor `limits` lands. (File `quiz1.py`: `print(arm)` on the
last line raises `NameError`, because `arm` is not a name in that file, even though
module `arm` is loaded and sitting in `sys.modules`. Two different tables.)
Rule: **`import X` binds the leftmost name; `from X import Y` binds `Y`. Loading is
the same either way.**
Check: for each of the three forms, ask which single name lands.

### Idea 7 — Absolute vs relative import, inside the package
Now the importing file is ITSELF inside `arm` and wants its neighbour `limits.py`.
Two ways to write line 1 (files `arm/safety.py` and `arm/safety_rel.py`):
- **Absolute**: `from arm.limits import MAX_ANGLE`. The full address from the top
  folder. The same line an outside file would write.
- **Relative**: `from .limits import MAX_ANGLE`. The dot is a word meaning **"my own
  folder"**. Python fills it in from the importing module's own dotted name:
  `safety_rel` was loaded as `arm.safety_rel`, strip the last part, the dot is `arm`.
  Two dots `..` = the folder one level up.
Same result both ways. Only difference: whether the word `arm` appears on the line.
What relative buys you, honestly: rename the folder `arm` to `kinova_arm` and the
absolute line breaks, the relative line does not. A maintenance convenience, not a
different mechanism. That is why LeRobot's `__init__.py` uses `from .x import Y`.
Also: `from . import limits` is the relative spelling of `from arm import limits`.
Check: ask him to convert `from . import limits` to absolute form (answer:
`from arm import limits`, NOT `import arm.limits`) and say which name lands.

### Idea 8 — The trap: relative imports fail when the file is run directly
Files `arm/motion.py` and `run_motion.py`.
- `python3 run_motion.py` (an OUTSIDE file containing `import arm.motion`): Python
  loads `motion.py` UNDER THE NAME `arm.motion`. The dot becomes `arm`. Works.
- `python3 arm/motion.py` (run the file DIRECTLY as the script): a script is always
  loaded under the name `__main__`. No `arm.` in front, so the dot has nothing to
  become. `ImportError: attempted relative import with no known parent package`.
Same file, two different names depending on how it was started. Rule to carry:
**a relative import is filled in from the module's dotted name; a script run
directly has no dotted name.**
Also define `python3 -c '...'` if it comes up: "run the quoted text as Python code
instead of a file". Nothing else differs.
Check: ask him to explain, in his own words, why the same file works one way and
fails the other.

Finish by asking him to give the whole thing back in under a minute, cold: package,
what `import arm.limits` binds, what the dot means, and the trap.

---

## The files (all in one folder; the package folder is `arm/`)

```
teaching/s43_packages/
    use_arm.py
    only_arm.py
    from_arm.py
    quiz1.py
    run_motion.py
    arm/
        __init__.py
        limits.py
        safety.py
        safety_rel.py
        motion.py
```

### `arm/__init__.py`
```python
print("arm/__init__.py is running")
```

### `arm/limits.py`
```python
print("arm/limits.py is running")

MAX_ANGLE = 180
```

### `use_arm.py`
```python
import arm.limits
print("import done")
print(arm.limits.MAX_ANGLE)
```
Output of `python3 use_arm.py`:
```
arm/__init__.py is running
arm/limits.py is running
import done
180
```

### `only_arm.py`
```python
import arm
print("import done")
print("arm" in vars(), "limits" in vars())
print(arm.limits.MAX_ANGLE)
```
(`vars()` with no argument = the namespace dict of the file you are in.)
Output of `python3 only_arm.py`:
```
arm/__init__.py is running
import done
True False
Traceback (most recent call last):
  File "only_arm.py", line 4, in <module>
    print(arm.limits.MAX_ANGLE)
AttributeError: module 'arm' has no attribute 'limits'
```

### `from_arm.py`
```python
from arm import limits
print("import done")
print("arm" in vars(), "limits" in vars())
print(limits.MAX_ANGLE)
```
Output of `python3 from_arm.py`:
```
arm/__init__.py is running
arm/limits.py is running
import done
False True
180
```

### `quiz1.py`
```python
from arm.limits import MAX_ANGLE
print("import done")
print(MAX_ANGLE)
print(arm)
```
Output of `python3 quiz1.py`:
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

### `arm/safety.py` (absolute import, inside the package)
```python
from arm.limits import MAX_ANGLE

def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
```

### `arm/safety_rel.py` (relative import, inside the package)
```python
from .limits import MAX_ANGLE

def clamp(angle):
    if angle > MAX_ANGLE:
        return MAX_ANGLE
    return angle
```
Both, imported from an outside file as `import arm.safety` / `import arm.safety_rel`,
then `arm.safety.clamp(500)` → `180`.

### `arm/motion.py`
```python
from . import limits
print("limits" in vars(), "arm" in vars())
print(limits.MAX_ANGLE)
```

### `run_motion.py` (an outside file, next to the `arm/` folder)
```python
import arm.motion
```
Output of `python3 run_motion.py`:
```
arm/__init__.py is running
arm/limits.py is running
True False
180
```
Output of `python3 arm/motion.py` (run directly):
```
Traceback (most recent call last):
  File "arm/motion.py", line 1, in <module>
    from . import limits
ImportError: attempted relative import with no known parent package
```

### `sys.modules` proof
```python
import sys
from arm import limits
print([k for k in sys.modules if k.startswith("arm")])
```
Output:
```
['arm', 'arm.limits']
```
Same two keys for every import form. The form changes the NAME in your file, never
the keys.
