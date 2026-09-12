# Session 47 — notes (Fri 11 Sep 2026, 18:26 → ~21:40; Sat 12 Sep ~07:40 → 07:55)

**What this session was:** you opened ~21 hours after S46 and asked for new
content first. The cost was stated (three sessions with zero cold asks);
you chose the volley. Four asks fired: three passes, one fail, and one
voided by a mentor error, after which you stopped it. Then **1.11 File
Handling was opened and taught to the end of its checklist in one
session**: fourteen ideas, each a file you could run, from `open()` to
`json.dump`. Every bullet is [~]; nothing taught today can be [x] until a
later-day cold pass. Pushbacks 95–99, all upheld, all on how the mentor
built a question or delivered a file.

---

## SELF-TEST — do this first, notes closed

1. `f = open("limits.txt")`; `a = f.read()`; `b = f.read()`. What is `b`,
   and what single word explains it?
2. `.readline()` on a two-line file, called three times. Write the three
   return values exactly, including any `\n`.
3. `open("out.txt", "w")` on a file that already holds two lines. What is
   in the file the instant `open()` returns, before any `.write()`?
4. `f.write("x\n")` has run. `cat` on the file shows nothing. Why, and what
   makes it appear?
5. Inside `try:` you write two lines, the second write raises. Without
   `finally`, does `f.close()` run? With `with open(...) as f:`, does the
   file get closed? What is on disk in each case?
6. `python3 teaching/s47_files/read_it.py` from the repo root raises
   `FileNotFoundError`; from inside the folder it works. Nothing in the
   file changed. What did? What does `import` do differently?
7. Write the one line that turns `__file__` into "the folder this script
   is in", using `pathlib`. Then the same with `os.path`.
8. A CSV row reads `wrist,45,"tight, recheck"`. What does `csv.reader`
   give for it, and what does `line.split(",")` give?
9. `json.dump({"limits": (10, 45), "safe": True}, f)`, then `json.load`.
   What type is `limits` afterwards, and what did `True` look like in
   the file?
10. `a = [1, 2]; b = a; a += [3]; print(b)`. Exact line, and is `a is b`
    still `True`?

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

All files live in `teaching/s47_files/`. Run them from inside that folder
unless the text says otherwise; the working-directory idea (1.9 below) is
the reason.

### 1.0 The frame

Everything built for 46 sessions lived in memory and died with the
process. A file is bytes on disk that outlive the process. `open()` gives
you an object that reads or writes those bytes. Without it a program
cannot load a config, read a dataset, or write a log; a LeRobot dataset is
files. What matters most: `open`, `read`, `write`, `with`. What is
vocabulary: the mode letters, `readline` vs `readlines`. What is a reading
skill: `os.path` and `pathlib`. CSV and JSON are two stdlib modules
putting structure on top of the same thing.

### 1.1 `open()` returns an object; `.read()` returns one string

`limits.txt` (made with the shell):
```
elbow 10
wrist 45
```

`read_it.py`:
```python
f = open("limits.txt")
print(type(f))
text = f.read()
print(type(text))
print(repr(text))
f.close()
```
```
$ python3 read_it.py
<class '_io.TextIOWrapper'>
<class 'str'>
'elbow 10\nwrist 45\n'
```
`open()` returns a file object (the class name is a stdlib detail).
`.read()` returns the whole file as ONE `str`, newlines included; `repr`
shows the `\n` as characters. `.close()` releases it.

A text file is not a list of lines. It is one long string of characters
in which `\n` is just another character. The line-cutting is something
the file object does for you on the way out.

### 1.2 The file object carries a POSITION

`read_twice.py`:
```python
f = open("limits.txt")
first = f.read()
second = f.read()
print(repr(first))
print(repr(second))
f.close()
```
```
$ python3 read_twice.py
'elbow 10\nwrist 45\n'
''
```
The file object is a cursor over the file, not the file. `.read()` returns
everything from the cursor to the end and leaves the cursor there. A
second `.read()` starts at the end, so `''`. Same shape as an exhausted
iterator: the list underneath is untouched; the position ran off the end.

### 1.3 `.readline()` moves the cursor one line

`read_lines.py`:
```python
f = open("limits.txt")
print(repr(f.readline()))
print(repr(f.readline()))
print(repr(f.readline()))
f.close()
```
```
$ python3 read_lines.py
'elbow 10\n'
'wrist 45\n'
''
```
Reads up to and including the next `\n`, then stops. The `\n` stays on
the line. Past the end: `''`, the same signal as 1.2.

### 1.4 The file object is iterable; this is the form you write

`loop_lines.py`:
```python
f = open("limits.txt")
for line in f:
    print(repr(line))
print(repr(f.read()))
f.close()
```
```
$ python3 loop_lines.py
'elbow 10\n'
'wrist 45\n'
''
```
`for line in f` hands you one line per pass, moving the same cursor, and
never loads the whole file into memory. The `.read()` after the loop finds
the cursor at the end. `.readlines()` (vocabulary) returns the same lines
as a `list`; it loads everything, so prefer the loop for anything big.

### 1.5 Writing, and the `"w"` trap

`open()` takes a second argument, the MODE. `"r"` is the default.

`write_it.py`:
```python
f = open("out.txt", "w")
f.write("shoulder 90\n")
f.write("base 180\n")
f.close()
```
```
$ ls out.txt        -> No such file or directory
$ python3 write_it.py
$ cat out.txt
shoulder 90
base 180
$ python3 write_it.py      (second run, unchanged)
$ wc -l out.txt
2 out.txt
```
`"w"` creates the file if missing. `.write()` adds no newline; both `\n`
came from the strings. Second run: still two lines, because **`"w"`
truncates the file to empty the moment `open()` runs**, before any write.
Truncate = cut off (S12). The old contents are gone at the `open` line.

### 1.6 `"a"` keeps the file

`append_it.py`:
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
`"a"` opens with the cursor at the END and never truncates. The roster:
`"r"` read, default, fails if missing; `"w"` write, truncates, creates;
`"a"` append, cursor at end, creates. The only trap in it is `"w"`.

### 1.7 Writes are buffered; `close` is what lands them

`no_close.py` (two file objects, one disk file):
```python
w = open("buf.txt", "w")
w.write("elbow 10\n")

r = open("buf.txt")
print("before close:", repr(r.read()))
r.close()

w.close()

r = open("buf.txt")
print("after close: ", repr(r.read()))
r.close()
```
```
$ python3 no_close.py
before close: ''
after close:  'elbow 10\n'
```
Line 1: `w` opens for writing (disk now empty). Line 2: the string goes
into `w`'s buffer in memory, not to disk. Lines 4–6: a separate reader
reads DISK, gets `''`. Line 8: `w.close()` flushes the buffer. Lines
10–12: the reader now sees the line.

### 1.8 Why `finally`, and why `with`

The close does not fail. It gets SKIPPED, because the line before it
raised. `skip_close.py` (`.write()` needs a `str`, so `f.write(42)` is a
`TypeError`):
```python
f = open("skip.txt", "w")
try:
    f.write("elbow 10\n")
    f.write(42)
    f.close()
except TypeError:
    print("write raised. did close run?", f.closed)

print("on disk:", repr(open("skip.txt").read()))
```
```
$ python3 skip_close.py
write raised. did close run? False
on disk: ''
```
Line 4 raised; execution jumped to `except`; line 5 never ran; the good
line from line 3 is stuck in a buffer nobody flushed. In a long-running
program that catches and continues (a 15 Hz loop), every skipped close is
a leaked handle and a lost buffer, until the OS says "Too many open
files" far from the cause.

The guaranteed shape, `safe_close.py`:
```python
f = open("buf.txt", "w")
try:
    f.write("elbow 10\n")
    f.write("wrist 45\n")
finally:
    f.close()

print(repr(open("buf.txt").read()))
```
```
$ python3 safe_close.py
'elbow 10\nwrist 45\n'
```
`open()` before the `try` (if opening fails there is nothing to close);
the work inside; `close()` in `finally`. Correct, and four lines of
ceremony around two lines of work.

`with` is that shape as one statement. `with_it.py`:
```python
with open("with.txt", "w") as f:
    f.write("elbow 10\n")
    print("inside block, closed?", f.closed)

print("after block,  closed?", f.closed)
print("on disk:", repr(open("with.txt").read()))
```
```
$ python3 with_it.py
inside block, closed? False
after block,  closed? True
on disk: 'elbow 10\n'
```
`as f` binds the name (the same `as` as `import x as y`). The dedent
closes the file. `f` still exists afterwards; only the file object is
closed. An object that works with `with` is a **context manager**: it
sets itself up on entry and tears itself down on exit. How (a pair of
dunder methods) is on credit until 1.12.

With an exception inside, `with_err.py`:
```python
try:
    with open("with_err.txt", "w") as f:
        f.write("elbow 10\n")
        f.write(42)
        print("this line never runs")
except TypeError:
    print("write raised. closed?", f.closed)

print("on disk:", repr(open("with_err.txt").read()))
```
```
$ python3 with_err.py
write raised. closed? True
on disk: 'elbow 10\n'
```
Same two writes as `skip_close.py`, opposite result. Leaving the block
closes the file, however you leave it.

### 1.9 `open()` follows the SHELL; `import` follows the SCRIPT

```
$ cd ~/Desktop/python-journey
$ python3 teaching/s47_files/read_it.py
    f = open("limits.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'limits.txt'
```
Nothing in the file changed; the shell's folder did. A relative path in
`open()` is resolved against the current working directory, the folder
the process was started from. Contrast 1.10: `sys.path[0]` is the
SCRIPT's folder, so imports do not care where you start. Files follow the
shell; imports follow the script.

### 1.10 Anchor paths to `__file__`

`read_anywhere.py`:
```python
from pathlib import Path

here = Path(__file__).parent
print(here)

with open(here / "limits.txt") as f:
    print(repr(f.read()))
```
```
$ python3 read_anywhere.py                       (from the script folder)
/home/ankur/Desktop/python-journey/teaching/s47_files
'elbow 10\nwrist 45\n'
$ python3 teaching/s47_files/read_anywhere.py    (from the repo root)
/home/ankur/Desktop/python-journey/teaching/s47_files
'elbow 10\nwrist 45\n'
```
`Path(...)` is a stdlib constructor (a class, on credit) that turns a
path string into a path object. `.parent` is its folder. `/` on a `Path`
means join, not divide: the object decides what the operator does, same
as `+` on a list vs an int. `here` is the same from both shells because
`__file__` does not care where the shell is.

The older spelling, `os_form.py`:
```python
import os

print("shell is in:", os.getcwd())

here = os.path.dirname(os.path.abspath(__file__))
print("script is in:", here)

path = os.path.join(here, "limits.txt")
print("opening:", path)

with open(path) as f:
    print(repr(f.read()))
```
```
$ python3 teaching/s47_files/os_form.py          (from the repo root)
shell is in: /home/ankur/Desktop/python-journey
script is in: /home/ankur/Desktop/python-journey/teaching/s47_files
opening: /home/ankur/Desktop/python-journey/teaching/s47_files/limits.txt
'elbow 10\nwrist 45\n'
```
`getcwd` = get current working directory, the shell's folder. `abspath`
+ `dirname` = `Path(__file__).parent` in two calls. `os.path.join` = the
`/`. The map: `os` (filesystem: `getcwd`, `listdir`, `makedirs`,
`remove`); `os.path` (path STRINGS: `join`, `dirname`, `abspath`,
`exists`, `expanduser`); `pathlib.Path` (the object form). New code uses
`pathlib`; the code you read uses both.

**How much to remember:** cold: `with open(p) as f`, `for line in f`,
the three modes and the `"w"` trap, files-follow-the-shell, and ONE join
form (`Path(__file__).parent / name`). The rest is a reference roster.

### 1.11 CSV

Comma-Separated Values: text, one record per line, one value per comma.
You could `.split(",")` each line (S7); it breaks when a value contains a
comma or a quote. The `csv` module knows the quoting rules and hands you
each row as a `list` of strings.

`joints.csv`:
```
name,limit,note
elbow,10,ok
wrist,45,"tight, recheck"
```
`read_csv.py`:
```python
import csv

with open("joints.csv") as f:
    for row in csv.reader(f):
        print(row)

print("---- naive split")
with open("joints.csv") as f:
    for line in f:
        print(line.strip().split(","))
```
```
$ python3 read_csv.py
['name', 'limit', 'note']
['elbow', '10', 'ok']
['wrist', '45', 'tight, recheck']
---- naive split
['name', 'limit', 'note']
['elbow', '10', 'ok']
['wrist', '45', '"tight', ' recheck"']
```
`csv.reader(f)` wraps the file object and is iterable. Row 3: three
fields with the quotes removed, versus four fields with quote characters
left in. Every value is a `str`, including `'10'`; `int()` is your job.
The header is just row one.

`write_csv.py`:
```python
import csv

rows = [["name", "limit"], ["elbow", 10], ["wrist", 45]]

with open("out.csv", "w", newline="") as f:
    w = csv.writer(f)
    for row in rows:
        w.writerow(row)

print(repr(open("out.csv").read()))
```
```
$ python3 write_csv.py
'name,limit\nelbow,10\nwrist,45\n'
```
`newline=""` is part of the spelling when opening a file for `csv`;
without it some platforms double the line endings. `writerow` takes one
list, writes one line, calling `str()` on each value.

### 1.12 JSON

A text format for NESTED data: dicts, lists, strings, numbers, booleans,
`null`. LeRobot's `meta/info.json` is this. CSV is a flat table; a config
with a list of joints each holding its own limits does not fit a table.
Two calls: `json.load(f)` reads a file into a dict or list; `json.dump(obj,
f)` writes one out.

`config.json`:
```
{"robot": "gen3", "hz": 15, "safe": true, "joints": [{"name": "elbow", "limit": 10}, {"name": "wrist", "limit": 45}], "note": null}
```
`read_json.py`:
```python
import json

with open("config.json") as f:
    cfg = json.load(f)

print(type(cfg))
print(cfg["hz"], type(cfg["hz"]))
print(cfg["safe"], cfg["note"])
print(cfg["joints"][1]["limit"])
```
```
$ python3 read_json.py
<class 'dict'>
15 <class 'int'>
True None
45
```
The outer `{}` became a `dict`; `15` came back as an `int` (unlike CSV);
`true` → `True`, `null` → `None`, `false` → `False`. Nested access is the
`[]` you own.

`write_json.py`:
```python
import json

cfg = {"robot": "gen3", "limits": (10, 45), "safe": True, "note": None}

with open("out.json", "w") as f:
    json.dump(cfg, f, indent=2)

print(open("out.json").read())

with open("out.json") as f:
    back = json.load(f)
print(back["limits"], type(back["limits"]))
```
```
$ python3 write_json.py
{
  "robot": "gen3",
  "limits": [
    10,
    45
  ],
  "safe": true,
  "note": null
}
[10, 45] <class 'list'>
```
`dump(obj, f)` in that order; `indent=2` is cosmetic. The trap: JSON has
no tuple and no set. The tuple went out as `[10, 45]` and came back a
`list`. The round trip is not exact for those two types.

### 1.13 The volley fact you were missing: `+=` on a list

`v4_id.py` (scratch):
```python
a = [1, 2]
b = a
print(id(a) == id(b))
a += [3]
print(id(a) == id(b))
a = a + [4]
print(id(a) == id(b))
```
```
True
True
False
```
On a list, `+=` does NOT rebind. It mutates the existing object in place,
like `.extend()`, so an alias sees it. Only `a = a + [4]` builds a new
list and rebinds. Discriminator: mutable type ⇒ `+=` mutates in place;
immutable type (int, str, tuple) ⇒ `+=` has no choice but to rebind. Look
at the type first, the same rule as for methods.

### 1.14 `LookupError` (one line, defined after pushback 97)

`KeyError` and `IndexError` share one parent, `LookupError`. You do not
memorise the tree; you own the rule (a catcher reaches DOWN, so an
ancestor placed first swallows every descendant) and look the tree up.

### Self-test answers
1. `''`; cursor. 2. `'elbow 10\n'`, `'wrist 45\n'`, `''`. 3. Nothing: it
was truncated at `open`. 4. Buffered in memory; `close()` (or a full
buffer) flushes it. 5. No / yes; `''` / `'elbow 10\n'`. 6. The shell's
folder; `import` uses `sys.path[0]`, the script's folder. 7.
`Path(__file__).parent`; `os.path.dirname(os.path.abspath(__file__))`.
8. `['wrist', '45', 'tight, recheck']`; `['wrist', '45', '"tight', '
recheck"']`. 9. `list`; `true`. 10. `[1, 2, 3]`; `True`.

---

## 2. THINKING GAPS THIS SESSION — with classification

1. **`+=` on a list modelled as a rebind — FAIL, rated 7.** Your logic
   was correct from that premise to the end; the premise was wrong.
   **Knowledge gap on ONE fact, honestly the mentor's to give once it
   failed** (pushback 96 upheld). Over-rating: a 7 on a model never
   corrected. New row due 13 Sep; ask for the identity next time.
2. **`[[0]*3]*3` "three copies" → "three references".** Line right,
   label loose, fixed on one narrowing question. **Language precision,
   not a mechanism gap.** Rated 6, honest.
3. **`UnboundLocalError`: "def creates the object and sees `count =`".**
   Mechanism right; sharpened to: the COMPILER marks the name local
   before anything runs. **Precision.** Deletion test clean. Label
   leaked by the mentor, so the label is unmeasured.
4. **`is None` clean**, with `.get()` → `None` as the reason unprompted.
5. **"A file is basically like a list of strings"** — a model slip,
   corrected: one string, the reader cuts at `\n`. Watch on the cold ask.
6. **`"w"` predicted as cursor-at-start (four lines).** A good forward
   reasoning from the cursor model; the truncation fact was not on
   screen. [PREDICT], not logged.
7. **Hierarchy direction: unanswered.** The ask was voided by an
   untaught name; the re-posed version was never answered because you
   stopped the volley. Row stays overdue.
8. **Volley: 4 of 8, then stopped.** Two mentor construction errors in
   five asks; your call to stop was reasonable.

## 3. TEACHING MISTAKES THIS SESSION

1. Pushback 95 — the error name in the question header before you
   answered (`UnboundLocalError`). Label half unmeasured.
2. Pushback 96 — after a failed recall, a second Socratic question
   instead of the missing fact. You were angry and right. **Parked as a
   rule candidate for your ruling at the S48 open.**
3. Pushback 97 — `LookupError` in a cold ask; never taught (grep found
   it only in STATE's own plan). Voided, nothing logged.
4. Pushback 98 — a [PREDICT] on a second `.read()` before the cursor
   had been shown. Foundation-before-prediction (S5).
5. Pushback 99 — `no_close.py` pasted with a one-line gloss and a
   question; no line-by-line walk. Fixed by walking it; every
   teach-back after that was clean.
6. A shell pipe (`2>&1 | tail -3`) shown in a command you had not been
   given. Explained when you asked; should not have appeared.

Held: interval gate from three sources; the cost of skipping the volley
stated and your choice taken; every demo a real file, pasted under its
path, run with its command shown; every snippet run before posing; tags
on every block; no ratings on same-day material; substrate checked
(`split`/`strip` against S7) before use; direct questions answered
(context, `os`, "must I remember this", the pipe); your right-sizing of
CSV accepted; the close written in the turn you asked for it.

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| name | what it does | trap |
|---|---|---|
| `open(path, mode)` | returns a file object: a CURSOR over the file | relative path is resolved against the SHELL's folder |
| `.read()` | everything from the cursor to the end, one `str` | second call returns `''` |
| `.readline()` | one line incl. `\n`, cursor moves one line | `''` past the end |
| `for line in f` | one line per pass, no full load | the loop consumes the cursor |
| `.readlines()` | all lines as a `list` | loads the whole file |
| `"w"` | write; CREATES if missing | TRUNCATES at `open`, before any write |
| `"a"` | append; cursor at the END | — |
| `.write(s)` | puts `s` into the BUFFER | no newline added; not on disk until close |
| `.close()` | flushes the buffer, releases the handle | skipped when a line before it raises |
| `with open(...) as f:` | `try`/`finally` close in one statement | `f` is still a name after the block, just closed |
| context manager | an object with set-up on entry, tear-down on exit | internals on credit (1.12) |
| `__file__` anchor | `Path(__file__).parent / name` | forget it and the script only works from one folder |
| `os.getcwd()` | the shell's folder | this is what `open("x")` uses |
| `os.path.join/dirname/abspath` | path STRING operations | never `a + "/" + b` |
| `FileNotFoundError` | the path did not resolve to a file | usually a cwd problem, not a typo |
| `csv.reader(f)` | one `list` of `str` per row, quotes handled | every value is text; header is row one |
| `csv.writer(f)` | `writerow(list)` → one line | open with `newline=""` |
| `json.load(f)` / `json.dump(obj, f)` | file ↔ nested dict/list, real types | tuple → list; `True`/`None` ↔ `true`/`null` |
| `+=` on a list | mutates IN PLACE, alias sees it | `a = a + [..]` rebinds; immutables always rebind |
| `LookupError` | parent of `KeyError` and `IndexError` | own the rule, look up the tree |

## 5. NEXT

- **His ruling on the parked rule** (fact-after-fail), one line, first.
- **The volley, built clean**: the two unlanded S47 asks (hierarchy with
  `Exception`/`KeyError`; `+=` with `id`), then the S41/S42 backlog.
- 1.10 cold asks, all legal now; 1.11 drill and cold asks legal 13 Sep.
- `pdb` inside 1.11 (owed); LeRobot block; then 1.12 OOP.
