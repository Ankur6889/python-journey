# Session 46 — notes (Thu 10 Sep 2026, 16:25 → ~21:45; close written Fri 11 Sep 18:17)

**What this session was:** you opened 42 hours after S45 and asked to
restart from the point where circular imports finished. The standard
library was re-walked from its frame with one physical demo per idea, then
finished: you opened a real stdlib file (`bisect.py`) and read `bisect_left`
line by line. `enumerate()` and the bare `*` in a signature were defined.
Then pip / site-packages was opened and taught with a live shadowing bug.
**1.10 is now taught-complete.** Seven bullets stay [~] until cold asks pass
on a later day. No ratings, no promotions. The overdue volley did not fire
(third session running). Pushbacks 88–94, all upheld or part-upheld, six
of them on delivery and one on the close itself, which was not performed
when you asked and was written the next day.

---

## SELF-TEST — do this first, notes closed

1. `sys.path` is `['/home/me/proj', '/opt/ros/jazzy/lib/python3.12/site-packages', '/usr/lib/python312.zip', '/usr/lib/python3.12', ...]`.
   Walk `import json` by hand: what does Python look for in each folder,
   where does it stop, and what runs when it stops?
2. Why does importing a FOLDER need a file to run at all? One sentence.
3. `json/__init__.py` says `from .decoder import JSONDecoder`. Which folder
   does the dot refer to, and how does Python actually resolve it?
4. After `import json`, `sys.modules` holds `json.scanner`. Nothing in
   `__init__.py` names `scanner`. Where did it come from?
5. `sys.modules` keys are inserted early, yet the printed order after
   `import json` is `['json.scanner', 'json.decoder', 'json.encoder', 'json']`.
   Reconcile the two facts.
6. `def clamp(value, low, high, *, verbose=False)`. Which of these raises,
   and why: `clamp(1, 0, 2, True)` / `clamp(1, 0, 2, verbose=True)`?
7. What does `enumerate(["a", "b"])` hand out on each pass, and what
   construct on the `for` line splits it into two names?
8. Your script folder holds `json.py` (one print). `main.py` next to it
   does `import json` then `json.loads('{}')`. Which line crashes, with
   what error, and why not the import line?
9. Where does `pip install numpy` put the files, and why does that make
   `import numpy` work with no change to your code?

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

### 1.1 FRAME — the standard library
What: the modules and packages that ship with the interpreter (`json`,
`sys`, `os`, `math`, `bisect`). Why: so nobody writes a JSON reader twice.
What it buys you today, only two things: (1) it is on disk as ordinary
`.py` files found by the same route rule as `arm`; (2) its packages use
`__init__.py` as a front door, which is the LeRobot / openpi pattern.

### 1.2 The route, done by hand (idea 1)
`teaching/s45_stdlib/where_is.py` printed `json.__file__` →
`/usr/lib/python3.12/json/__init__.py` and `sys.path` (seven folders,
entry 0 = the script's folder). Python asks ONE question in each folder,
in order: is there a `json.py` or a `json/` here? In the shell:
```
$ ls -d <entry0>/json <entry0>/json.py      # No such file (both)
$ ls -d <entry1>/json <entry1>/json.py      # No such file (both)
$ ls -d <entry2>/json <entry2>/json.py      # No such file (both)
$ ls -d /usr/lib/python3.12/json /usr/lib/python3.12/json.py
/usr/lib/python3.12/json                    # a folder. STOP.
$ ls /usr/lib/python3.12/json/
decoder.py  encoder.py  __init__.py  __pycache__  scanner.py  tool.py
```
First hit wins; entries 4–6 are never looked at. **A folder is not code.**
`import json` must build a module OBJECT, and a module object is built by
running a file line by line into a namespace. So one file stands for the
folder: `__init__.py`. Nothing else in the folder runs unless asked for.
Proof re-run: `teaching/s43_packages/see_arm.py` — `import arm.limits`
prints `arm/__init__.py is running` then `arm/limits.py is running`, and
`sys.modules["arm"]` is `<module 'arm' from '.../arm/__init__.py'>`.

Running code without a file: the REPL (`python3`, `>>>`, `Ctrl-D`), where
`sys.path[0]` is `''` = the folder you stand in; or `python3 -c "..."`.

### 1.3 The front door (idea 2)
`/usr/lib/python3.12/json/__init__.py` lines 106–108, READ from disk, not
run by us:
```python
from .decoder import JSONDecoder, JSONDecodeError
from .encoder import JSONEncoder
import codecs
```
The dot means "the package this file belongs to", resolved by NAME: the
module being built is called `json`, so `.decoder` is spelled out as
`json.decoder`, that string becomes the `sys.modules` key, and
`json/decoder.py` is opened under it. The caller's folder plays no part.
Where `json.scanner` comes from — `json/decoder.py` line 5:
```python
from json import scanner
```
Imports chain: `__init__.py` → `decoder.py` → `scanner.py`. One user line,
four keys, twelve names on `json`. `arm/__init__.py` only printed, so
`import arm` loaded nothing else. That is the whole front-door idea.

### 1.4 Key order: early in, moved to the end on finish (your question)
`teaching/s46_stdlib/key_order/`
```python
# p/__init__.py
print("p/__init__.py starting")
from . import inner
print("p/__init__.py done")

# p/inner.py
import sys
print("p/inner.py running, keys now:", [k for k in sys.modules if k.startswith("p")])

# main.py
import sys
import p
print("main after import, keys now:", [k for k in sys.modules if k.startswith("p")])
```
```
$ cd teaching/s46_stdlib/key_order && python3 main.py
p/__init__.py starting
p/inner.py running, keys now: ['posix', 'posixpath', 'p', 'p.inner']
p/__init__.py done
main after import, keys now: ['posix', 'posixpath', 'p.inner', 'p']
```
(`posix`, `posixpath` are filter noise.) Mid-run: `p` then `p.inner` —
insertion order, as circular imports taught. After: `p.inner` then `p` —
when a module's run finishes, its key is moved to the END. Both facts are
true. A package that imports its own files finishes last.

### 1.5 Read a stdlib file: `bisect_left` (idea 3)
`/usr/lib/python3.12/bisect.py`, 118 lines, four functions, pure Python.
Frame: given a SORTED list `a` and a value `x`, return the index where `x`
would go to keep it sorted. Why: scanning is N comparisons; halving is
about log N. What it buys you: `lo`, `hi`, `mid` — every binary search.
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
`lo`/`hi` fence off the part still in play. Each pass: `mid` = middle of
the fence; if `a[mid] < x`, `x` belongs to the right → `lo = mid + 1`;
else `x` belongs at `mid` or left → `hi = mid`. Stop when `lo == hi`.

| `bisect_left([10, 20, 30, 40], 35)` | lo | hi | mid | a[mid] | < 35? | move |
|---|---|---|---|---|---|---|
| pass 1 | 0 | 4 | 2 | 30 | yes | lo = 3 |
| pass 2 | 3 | 4 | 3 | 40 | no | hi = 3 |
| stop | 3 | 3 | | | | return 3 |

### 1.6 The bare `*` — a keyword-only fence
`teaching/s46_stdlib/star.py`
```python
def clamp(value, low, high, *, verbose=False):
    if verbose:
        print("clamping", value, "into", low, high)
    return max(low, min(value, high))

print(clamp(150, 0, 100))
print(clamp(150, 0, 100, verbose=True))
print(clamp(150, 0, 100, True))
```
```
100
clamping 150 into 0 100
100
Traceback (most recent call last):
  File ".../star.py", line 8, in <module>
    print(clamp(150, 0, 100, True))
TypeError: clamp() takes 3 positional arguments but 4 were given
```
Positional filling STOPS at the star; everything to its right must be
passed by keyword. The message says 3, not 4, because of the star. Why it
exists: `bisect_left(a, x, 0, 4, len)` is unreadable; the fence forces
`key=`. Substrate: `min(a, b)` = the smaller argument, `max(a, b)` = the
larger; `max(low, min(value, high))` = no lower than `low`, no higher
than `high`.

### 1.7 `enumerate()`
`teaching/s46_stdlib/enum.py`
```python
joints = ["shoulder", "elbow", "wrist"]

for pair in enumerate(joints):
    print(pair)

for i, name in enumerate(joints):
    print(i, name)
```
```
(0, 'shoulder')
(1, 'elbow')
(2, 'wrist')
0 shoulder
1 elbow
2 wrist
```
Enumerate = number off. Hands out one tuple per element, `(count,
element)`, count from 0. `for i, name in ...` is two-name UNPACKING on the
`for` line (S23: `a, b = pair`). Replaces `for i in range(len(x))`.

### 1.8 pip / site-packages (`teaching/s46_pip/`)
Frame: `pip` downloads a package and COPIES its folder into a folder that
is already on `sys.path`, called `site-packages` (`dist-packages` on
Ubuntu). No third tier; the route rule does not change.
`where_third.py`
```python
import sys
import json
import numpy
import rclpy

print(json.__file__)
print(numpy.__file__)
print(rclpy.__file__)
print()
for i, folder in enumerate(sys.path):
    print(i, folder)
```
```
$ cd teaching/s46_pip && python3 where_third.py
/usr/lib/python3.12/json/__init__.py
/usr/lib/python3/dist-packages/numpy/__init__.py
/opt/ros/jazzy/lib/python3.12/site-packages/rclpy/__init__.py

0 /home/ankur/Desktop/python-journey/teaching/s46_pip
1 /opt/ros/jazzy/lib/python3.12/site-packages
2 /usr/lib/python312.zip
3 /usr/lib/python3.12
4 /usr/lib/python3.12/lib-dynload
5 /usr/local/lib/python3.12/dist-packages
6 /usr/lib/python3/dist-packages
```
Three packages, three `__init__.py`, three folders on the list. Entry 1 is
what `source /opt/ros/jazzy/setup.bash` adds. A `json/` copied into entry
1 would win over the real one at entry 3: first hit wins.

### 1.9 Shadowing — the bug that bites at entry 0
`teaching/s46_pip/shadow/json.py`: `print("MY json.py is running")`
`teaching/s46_pip/shadow/main.py`:
```python
import json

print(json.__file__)
print(json.loads('{"a": 1}'))
```
```
$ cd teaching/s46_pip/shadow && python3 main.py
MY json.py is running
/home/ankur/Desktop/python-journey/teaching/s46_pip/shadow/json.py
Traceback (most recent call last):
  File ".../shadow/main.py", line 4, in <module>
    print(json.loads('{"a": 1}'))
AttributeError: module 'json' has no attribute 'loads'
```
Entry 0 is `shadow/`; `shadow/json.py` exists; walk stops; the stdlib
`json` is never opened. Line 1 succeeds (it imported SOMETHING called
`json`); line 4 asks a one-line module for `loads`. The crash lands three
lines after the cause. **Never name your own file after a package you
import** (`random.py`, `numpy.py`, `test.py`, `json.py`). The script's
folder is not "checked before `sys.path`"; it IS `sys.path[0]`.
`sys.path.append("/some/folder")` at the top of a script is the same
mechanism by hand and a smell in a real repo; the clean fix is
`pip install -e .` (named, not shown).

---

## 2. THINKING GAPS THIS SESSION — with classification

1. **Route rule at 42h — gap named.** [RECALL] "walk `import json`": you
   had `__init__.py` runs first and "the path of arm, excluding arm"
   (right), then said you forgot and asked to be reminded. **Knowledge
   gap (retention), honestly declared.** Re-walked by hand; row re-dated
   12 Sep, still [~]. The abstract five-point restatement did not land;
   the shell walk did — same finding as S45.
2. **`__init__.py` — right label, "guess work".** Reasoning ("a folder is
   not code") was not retained; after one sentence + `see_arm.py` your
   teach-back was clean. **Label retained, mechanism not** — the reverse
   of your usual pattern; watch whether it recurs on the cold ask.
3. **`json.scanner` — gap named.** Not a ledger item; it was only ever
   seen in output on Tuesday.
4. **Key-order challenge — INSIGHT, not a gap.** You applied the
   circular-import fact correctly and found the mentor's half-answer.
   Produced a new demo and a new queue row.
5. **"Run a file" for "import a file"** — language precision. The two
   verbs are the `__main__` difference.
6. **Bare `*` teach-back: answer without the why** ("the first one
   raises"). Re-asked per S20-3a; mechanism then right. **Surface-answer
   pattern, mild.** Phrase "with the argument" → "by keyword".
7. **"Same folder first, then `sys.path`"** — structural slip, corrected:
   one list, entry 0 is the folder. Watch on the cold ask.
8. **Relative vs absolute "still hurting"** — parked by you, correctly,
   with the answer attached from S45. Cold task, not teaching.
9. **Volley: 0 of 8, third session.** Not a thinking gap; a scheduling
   one, and the mentor's to fix at the next open.

## 3. TEACHING MISTAKES THIS SESSION

1. Pushback 88 (part) — "last 20 minutes" resolved without asking.
2. Pushback 89 — five-point list instead of a shell walk. Physical first.
3. Pushback 90 — `bisect_left` shown before its frame (S28 FRAME FIRST).
4. Pushback 91 — quoted file lines without saying they were read, not run.
5. Pushback 92 — half a mechanism on key order; your objection was right.
6. Pushback 93 — output without its command.
7. Pushback 94 — the close was not written when you asked; two checks ran
   and the turn ended. Caught by you the next day. Written 20h late.
8. `max()`/`min()` undefined inside `star.py` — substrate rule, defined
   in the same turn, queued.
9. `startswith("p")` let `posix`/`posixpath` into a demo's output.

Held: interval gate from three sources; every demo a file run from a
stated folder; nine files announced by path with code after creation;
every snippet run before posing; tags on every block; no ratings on
same-day material; direct questions answered directly; your park honoured.

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| name | what it does | trap |
|---|---|---|
| the route walk | one question per `sys.path` folder in order: `X.py` or `X/`? first hit wins | later entries never looked at |
| `__init__.py` | the file that stands for a folder, because a folder is not code | only it runs on `import pkg`; submodules need an import line |
| the dot in `from .x import` | "my own package", resolved by NAME into `pkg.x` | run the file directly and there is no package name |
| front door | `__init__.py` imports the folder's files; imports chain | `json.scanner` came from `decoder.py`, not `__init__.py` |
| key order | early in (stops loops); moved to END on finish | printed order is finish order |
| `bisect_left` | index where `x` goes in a sorted list; `lo`/`hi`/`mid` halving | list must already be sorted |
| bare `*` | positional filling stops here; right side by keyword only | a 4th positional → `TypeError ... 3 positional arguments` |
| `enumerate()` | `(count, element)` tuples, count from 0 | needs unpacking on the `for` line |
| `max()` / `min()` | larger / smaller argument | — |
| pip / site-packages | copies a folder into a folder already on `sys.path` | no third tier; same route |
| shadowing | your `json.py` at entry 0 hides the real one | crash lands later, as `AttributeError` |
| `sys.path.append` | the route by hand | a smell; `pip install -e .` |

## 5. NEXT

- **VOLLEY FIRST**, before anything: 8 cold asks from the August/1.9
  backlog. Three sessions with zero fired.
- 1.10 cold asks, legal from 12 Sep: route rule (gapped today), packages
  bound name, `from . import limits` absolute form (parked), run-directly
  trap, circular, `__main__`, shadowing, pip, bare `*`, `enumerate()`.
- The LeRobot build block (S42 decision) now that 1.10 is taught-complete.
- Then 1.11 File Handling.
