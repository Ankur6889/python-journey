# Unit 1.11 — File Handling

`open()` and the file object, reading, writing, modes, buffering and
`close()`, `with` and context managers, the working directory vs the script
folder, `pathlib` and `os.path`, CSV, and JSON.

---

## 1. The frame

Everything in the earlier units lived in memory and died with the process. A
file is bytes on disk that **outlive the process**. `open()` gives you an
object that reads or writes those bytes. Without it a program cannot load a
config, read a dataset, or write a log; a LeRobot dataset is files.

What matters most: `open`, `read`, `write`, `with`. What is vocabulary: the
mode letters, `readline` vs `readlines`. What is a reading skill: `os.path`
and `pathlib`. CSV and JSON are two stdlib modules putting structure on top of
the same thing.

All examples below use this file, `limits.txt`:
```
elbow 10
wrist 45
```

---

## 2. `open()` returns an object; `.read()` returns ONE string

```python
f = open("limits.txt")
print(type(f))          # <class '_io.TextIOWrapper'>   (the class name is a stdlib detail)
text = f.read()
print(type(text))       # <class 'str'>
print(repr(text))       # 'elbow 10\nwrist 45\n'
f.close()
```

- `open(path)` returns a **file object**. `.read()` returns the **whole file
  as one `str`**, newlines included — `repr` shows each `\n` as characters.
  `.close()` releases it.
- **A text file is not a list of lines.** It is one long string of
  characters in which `\n` is just another character. The line-cutting is
  something the file object does for you on the way out.

---

## 3. The file object carries a POSITION (a cursor)

```python
f = open("limits.txt")
first = f.read()
second = f.read()
print(repr(first))      # 'elbow 10\nwrist 45\n'
print(repr(second))     # ''
f.close()
```

The file object is a **cursor over the file, not the file**. `.read()`
returns everything from the cursor to the end and leaves the cursor there; a
second `.read()` starts at the end, so `''`. Same shape as an exhausted
iterator: the thing underneath is untouched; the position ran off the end.

---

## 4. `.readline()`, `for line in f`, `.readlines()`

```python
f = open("limits.txt")
print(repr(f.readline()))   # 'elbow 10\n'   up to and including the next \n
print(repr(f.readline()))   # 'wrist 45\n'   the \n stays on the line
print(repr(f.readline()))   # ''             past the end: the same signal as .read()
f.close()
```

**The file object is iterable — this is the form you write:**

```python
f = open("limits.txt")
for line in f:
    print(repr(line))       # 'elbow 10\n' / 'wrist 45\n'
print(repr(f.read()))       # ''  — the loop moved the same cursor to the end
f.close()
```

`for line in f` hands you one line per pass, moving the same cursor, and
**never loads the whole file into memory**. `.readlines()` (vocabulary)
returns the same lines as a `list`; it loads everything, so prefer the loop
for anything big. Strip the newline with `line.strip()` and split fields with
`.split()` (1.3 §4) when you need to.

---

## 5. Modes: `"r"`, `"w"`, `"a"` — and the `"w"` trap

`open()` takes a second argument, the **mode**. `"r"` (read) is the default.

```python
f = open("out.txt", "w")
f.write("shoulder 90\n")
f.write("base 180\n")
f.close()
```
```
$ ls out.txt                -> No such file or directory   (before the run)
$ python3 write_it.py
$ cat out.txt
shoulder 90
base 180
$ python3 write_it.py       (second run, unchanged)
$ wc -l out.txt
2 out.txt
```

- `"w"` **creates** the file if missing.
- `.write(s)` adds **no newline**; both `\n` came from the strings. It takes a
  `str` — `f.write(42)` is a `TypeError`.
- Second run: still two lines, because **`"w"` truncates the file to empty
  the moment `open()` runs, before any write.** The old contents are gone at
  the `open` line. (Truncate = cut off.)

```python
f = open("out.txt", "a")
f.write("gripper 0\n")
f.close()
```
```
$ python3 append_it.py
$ python3 append_it.py
$ cat out.txt
shoulder 90
base 180
gripper 0
gripper 0
```

`"a"` (append) opens with the cursor at the **end** and never truncates.

| mode | meaning | if the file is missing | cursor |
|---|---|---|---|
| `"r"` | read (default) | `FileNotFoundError` | start |
| `"w"` | write | creates it | start — after **truncating** the file at `open` |
| `"a"` | append | creates it | end |

The only trap in the roster is `"w"`.

---

## 6. Writes are buffered; `close()` is what lands them

Two file objects, one disk file:

```python
w = open("buf.txt", "w")
w.write("elbow 10\n")

r = open("buf.txt")
print("before close:", repr(r.read()))      # before close: ''
r.close()

w.close()

r = open("buf.txt")
print("after close: ", repr(r.read()))      # after close:  'elbow 10\n'
r.close()
```

Line 1: `w` opens for writing (disk now empty). Line 2: the string goes into
`w`'s **buffer in memory**, not to disk. A separate reader reads **disk** and
gets `''`. `w.close()` **flushes** the buffer; only then does the reader see
the line.

---

## 7. Why `finally`, and why `with`

The close does not *fail*; it gets **skipped**, because a line before it
raised:

```python
f = open("skip.txt", "w")
try:
    f.write("elbow 10\n")
    f.write(42)             # TypeError: write() argument must be str, not int
    f.close()
except TypeError:
    print("write raised. did close run?", f.closed)   # False

print("on disk:", repr(open("skip.txt").read()))     # ''
```

Execution jumped to `except`; the `close` line never ran; the good line is
stuck in a buffer nobody flushed. In a long-running program that catches and
continues, every skipped close is a leaked handle and a lost buffer, until
the OS says "Too many open files" far from the cause.

The guaranteed shape (1.9 §8):

```python
f = open("buf.txt", "w")        # before the try: if opening fails there is nothing to close
try:
    f.write("elbow 10\n")
    f.write("wrist 45\n")
finally:
    f.close()
```

Correct, and four lines of ceremony around two lines of work. **`with` is
that shape as one statement:**

```python
with open("with.txt", "w") as f:
    f.write("elbow 10\n")
    print("inside block, closed?", f.closed)    # False

print("after block,  closed?", f.closed)        # True
print(repr(open("with.txt").read()))            # 'elbow 10\n'
```

- `as f` binds the name (the same `as` as `import x as y`).
- **The dedent closes the file.** `f` still exists afterwards as a name; only
  the file object is closed.
- An object that works with `with` is a **context manager**: it sets itself
  up on entry and tears itself down on exit. How (a pair of dunder methods)
  is 1.12.

With an exception inside the block:

```python
try:
    with open("with_err.txt", "w") as f:
        f.write("elbow 10\n")
        f.write(42)
        print("this line never runs")
except TypeError:
    print("write raised. closed?", f.closed)    # True

print("on disk:", repr(open("with_err.txt").read()))    # 'elbow 10\n'
```

Same two writes as the skipped-close case, opposite result. **Leaving the
block closes the file, however you leave it.** The idiom to write, always:

```python
with open(path) as f:
    for line in f:
        ...
```

---

## 8. `open()` follows the SHELL; `import` follows the SCRIPT

```
$ cd ~/Desktop/python-journey
$ python3 teaching/s47_files/read_it.py
    f = open("limits.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'limits.txt'
```

Nothing in the file changed; the shell's folder did. A relative path in
`open()` is resolved against the **current working directory** — the folder
the process was started from. Contrast imports: `sys.path[0]` is the
**script's** folder, so imports do not care where you start (1.10 §4).

> **Files follow the shell; imports follow the script.**

`FileNotFoundError` is usually a working-directory problem, not a typo.

---

## 9. Anchor paths to `__file__`

`__file__` is the path on disk the module was built from (1.10). Turn it into
"the folder this script is in" and join from there:

```python
from pathlib import Path

here = Path(__file__).parent
print(here)                     # /home/ankur/Desktop/python-journey/teaching/s47_files

with open(here / "limits.txt") as f:
    print(repr(f.read()))       # 'elbow 10\nwrist 45\n'
```

Run from the script's folder or from the repo root, `here` is the same,
because `__file__` does not care where the shell is.

- `Path(...)` is a stdlib constructor (a class — 1.12) that turns a path
  string into a path object. `.parent` is its folder.
- **`/` on a `Path` means join, not divide.** The object decides what the
  operator does — the same rule as `+` on a list vs an int.

The older spelling, `os` / `os.path`:

```python
import os

print(os.getcwd())                              # the SHELL's folder — what open("x") uses
here = os.path.dirname(os.path.abspath(__file__))   # the SCRIPT's folder
path = os.path.join(here, "limits.txt")
with open(path) as f:
    print(repr(f.read()))
```

| module | works on | functions seen |
|---|---|---|
| `os` | the filesystem | `getcwd`, `listdir`, `makedirs`, `remove` |
| `os.path` | path **strings** | `join`, `dirname`, `abspath`, `exists`, `expanduser` |
| `pathlib.Path` | the **object** form | `Path(...)`, `.parent`, `/` |

`getcwd` = get current working directory. `abspath` + `dirname` =
`Path(__file__).parent` in two calls. `os.path.join` = the `/`. Never build a
path with `a + "/" + b`. `os.path.expanduser` turns `~` into the home folder
(Python does not expand `~` on its own). New code uses `pathlib`; the code
you read uses both.

**How much to remember cold:** `with open(p) as f`, `for line in f`, the
three modes and the `"w"` trap, files-follow-the-shell, and ONE join form —
`Path(__file__).parent / name`. The rest is a reference roster.

---

## 10. CSV

Comma-Separated Values: text, one record per line, one value per comma. You
could `.split(",")` each line; it breaks when a value contains a comma or a
quote. The `csv` module knows the quoting rules and hands you each row as a
**`list` of strings**.

`joints.csv`
```
name,limit,note
elbow,10,ok
wrist,45,"tight, recheck"
```

```python
import csv

with open("joints.csv") as f:
    for row in csv.reader(f):
        print(row)
# ['name', 'limit', 'note']
# ['elbow', '10', 'ok']
# ['wrist', '45', 'tight, recheck']

with open("joints.csv") as f:
    for line in f:
        print(line.strip().split(","))
# ['name', 'limit', 'note']
# ['elbow', '10', 'ok']
# ['wrist', '45', '"tight', ' recheck"']      <- four fields, quotes left in
```

- `csv.reader(f)` wraps the file object and is iterable.
- **Every value is a `str`**, including `'10'`; `int()` is your job.
- The header is just row one.

```python
import csv

rows = [["name", "limit"], ["elbow", 10], ["wrist", 45]]
with open("out.csv", "w", newline="") as f:
    w = csv.writer(f)
    for row in rows:
        w.writerow(row)

print(repr(open("out.csv").read()))     # 'name,limit\nelbow,10\nwrist,45\n'
```

`newline=""` is part of the spelling when opening a file for `csv`; without
it some platforms double the line endings. `writerow` takes one list, writes
one line, calling `str()` on each value. CSV gives flat rows of `str`.

---

## 11. JSON

A text format for **nested** data: dicts, lists, strings, numbers, booleans,
`null`. LeRobot's `meta/info.json` is this. CSV is a flat table; a config with
a list of joints each holding its own limits does not fit a table. Two calls:
`json.load(f)` reads a file into a dict or list; `json.dump(obj, f)` writes
one out.

`config.json`
```
{"robot": "gen3", "hz": 15, "safe": true, "joints": [{"name": "elbow", "limit": 10}, {"name": "wrist", "limit": 45}], "note": null}
```

```python
import json

with open("config.json") as f:
    cfg = json.load(f)

print(type(cfg))                    # <class 'dict'>
print(cfg["hz"], type(cfg["hz"]))   # 15 <class 'int'>   — real types, unlike CSV
print(cfg["safe"], cfg["note"])     # True None          — true/null -> True/None
print(cfg["joints"][1]["limit"])    # 45                 — nested access is the [] you own
```

```python
import json

cfg = {"robot": "gen3", "limits": (10, 45), "safe": True, "note": None}
with open("out.json", "w") as f:
    json.dump(cfg, f, indent=2)

print(open("out.json").read())
with open("out.json") as f:
    back = json.load(f)
print(back["limits"], type(back["limits"]))     # [10, 45] <class 'list'>
```
```
{
  "robot": "gen3",
  "limits": [
    10,
    45
  ],
  "safe": true,
  "note": null
}
```

- `dump(obj, f)` in that order; `indent=2` is cosmetic.
- Mapping: `{}` ↔ `dict`, `[]` ↔ `list`, `true`/`false`/`null` ↔
  `True`/`False`/`None`, numbers come back as `int`/`float`.
- **JSON has no tuple and no set.** The tuple went out as `[10, 45]` and came
  back a `list`; the round trip is not exact for those two types.
- `json.loads(text)` / `json.dumps(obj)` are the same two operations on a
  **string** instead of a file (`loads` = load from string).

Teach-back in one line: CSV gives flat rows of `str`; JSON gives one nested
structure with real types.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| `open(path, mode)` | returns a file object: a **cursor** over the file | a relative path resolves against the **shell's** folder |
| `.read()` | everything from the cursor to the end, one `str` | second call returns `''` |
| `.readline()` | one line including its `\n`; cursor moves one line | `''` past the end |
| `for line in f` | one line per pass, no full load — the form to write | the loop consumes the cursor |
| `.readlines()` | all lines as a `list` | loads the whole file |
| `"r"` | read (default) | `FileNotFoundError` if missing |
| `"w"` | write; creates if missing | **truncates at `open`**, before any write |
| `"a"` | append; cursor at the end | — |
| `.write(s)` | puts `s` into the buffer; no newline added | needs a `str`; not on disk until close/flush |
| `.close()` | flushes the buffer, releases the handle | skipped when a line before it raises |
| `with open(...) as f:` | `try`/`finally` close as one statement | `f` is still a name after the block, just closed |
| context manager | set-up on entry, tear-down on exit | internals in 1.12 |
| `f.closed` | `True` after close | — |
| cwd vs script folder | `open()` uses the shell's folder; `import` uses the script's | `FileNotFoundError` is usually a cwd problem |
| `Path(__file__).parent / name` | the one join form to know cold | `/` on a `Path` means join |
| `os.getcwd()` | the shell's folder | this is what `open("x")` uses |
| `os.path.join/dirname/abspath/exists/expanduser` | path-string operations | never `a + "/" + b`; `~` is not expanded for you |
| `csv.reader(f)` | one `list` of `str` per row, quotes handled | every value is text; header is row one |
| `csv.writer(f)` | `.writerow(list)` writes one line | open with `newline=""` |
| `json.load(f)` / `json.dump(obj, f)` | file ↔ nested dict/list with real types | tuple → list; no sets; `true`/`null` ↔ `True`/`None` |
| `json.loads` / `json.dumps` | the same, on strings | — |
