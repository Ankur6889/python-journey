# Unit 1.9 — Error Handling and Exceptions

What an exception is, the built-in error types and how to tell them apart,
`try`/`except`/`else`/`finally`, `raise`, custom exceptions, the hierarchy,
re-raising, exceptions as control flow, and the raise-vs-return decision.

---

## 1. What an exception is

An exception is **a signal that travels**: raised at the point of failure,
propagating outward looking for something to catch it. It is **never bound to
a name** — it is not a value that lands somewhere and sits.

```python
box = iter([1])
next(box)
print(next(box))        # print NEVER runs: next() raised before print was called
```

- If nothing catches it, the interpreter prints a **traceback** to stderr and
  the program **terminates** with exit code 1 (1.1 §7). Nothing is "paused".
- Whether an exception is an "error" is a judgement the **caller** makes, not
  a property of the mechanism. `for` catches `StopIteration` on every normal
  run.
- **Every error name is a CLASS** — `ValueError`, `KeyError`, `TypeError` —
  like `list` or `dict`. What travels through `raise` is an **object** built
  from one of them (§7).

---

## 2. Compile time vs run time — where errors come from

Python parses the **entire file** before executing a single line (1.1 §2).

| stage | what is checked | errors |
|---|---|---|
| **compile** | grammar only | `SyntaxError`, `IndentationError` |
| **run** | everything else | `NameError`, `TypeError`, `KeyError`, `ValueError`, … |

```python
print("checking limits")
for name in angles          # missing colon
    print(name)
```
```
  File "syn.py", line 2
    for name in angles
                      ^
SyntaxError: expected ':'
```

`checking limits` never printed; there is **no traceback header and no
frames**, because there was never a running program. A `try:` with no
`except` or `finally` is also a `SyntaxError`, and it kills the whole file,
including perfect functions sixty lines below it.

The compiler checks **grammar, never meaning**: a typo'd name compiles and
fails at run time with frames.

---

## 3. "How far did Python get?" — the error timeline

Not a list to memorise. A timeline to walk; every error name is an answer to
*how far Python got before it stopped*:

| how far it got | what broke | error |
|---|---|---|
| did not even parse | grammar | `SyntaxError`, `IndentationError` |
| parsed; looked up a name; no such name | the NAME | `NameError` |
| found the object; looked after the dot; nothing there | the ATTRIBUTE | `AttributeError` |
| tried the operation; not defined for that type | the TYPE | `TypeError` |
| operation fine; this particular value / key / index is not | the VALUE | `ValueError`, `KeyError`, `IndexError` |

```python
robot = {"joint": 3}
robot.append(5)        # AttributeError: 'dict' object has no attribute 'append'
robot["speed"]         # KeyError: 'speed'
rbot["joint"]          # NameError: name 'rbot' is not defined  — never reached the brackets
```

The stations are an **order**, not a menu: `rbot["joint"]` has a bad name
*and* brackets, and Python stopped at the name.

**The brackets do not decide the error — what you put inside them, and what
the container IS, do:**

```python
a = [10, 20, 30];   a[5]        # IndexError   — position absent
b = {"x": 1};       b[0]        # KeyError: 0  — key absent
seen = {"x"};       seen[0]     # TypeError: 'set' object is not subscriptable
```

The test between the last two rows: **could Python even attempt it?**
Attempt made, thing absent → `KeyError`/`IndexError`. Attempt impossible for
the type → `TypeError`.

---

## 4. The built-in exceptions — mechanisms, not a roster

**The error is named after the part that broke.** Families:

**A — code never ran (compile time)**

| Error | Mechanism |
|---|---|
| `SyntaxError` | grammar broken; not one line executes; no frames |
| `IndentationError` | a colon opened a block and no indented statement followed. A comment is not a body; `pass` is the filler |

**B — a name could not be found (run time)**

| Error | Mechanism |
|---|---|
| `NameError` | the name is bound nowhere on the LEGB path |
| `UnboundLocalError` | the name **is** local (assigned somewhere in the body, so classified local at compile time) but read before a value is bound (1.7 §6) |
| `AttributeError` | the object exists; the name after the **dot** is not on it. `[1, 2].push(3)`; `"a".append("z")` |
| `ModuleNotFoundError` | an `import` statement found nothing on `sys.path` (1.10). A missing *name* is `NameError`, not this |
| `ImportError` | the import machinery could not complete: a relative import with no parent package, or a name missing from a partially initialised module (1.10) |

**C — the operation could not be done (run time)**

| Error | Mechanism |
|---|---|
| `TypeError` | wrong **type** — the operation is impossible for this kind of thing. `"5" + 3`; `t[0] = x` on a tuple; `5[0]` (not subscriptable); `{[1]: 2}` (unhashable); calling an `int`; a required argument missing; a float where `.write()` wants a `str`; `'>' not supported between 'int' and 'NoneType'` |
| `ValueError` | **right type, wrong value.** `int("2.5")`; `a, b = [1, 2, 3]` (item count is a property of the value); `["a"].index("z")`; `bisect_left(a, x, lo=-1)` |
| `IndexError` | the type indexes fine; **this index** does not exist. Only indexing raises it — slicing never does |
| `KeyError` | the key is not in the dict / the item is not in the set (`remove`) |
| `LookupError` | the shared parent of `KeyError` and `IndexError` |
| `ZeroDivisionError` | division by zero is not defined |
| `FileNotFoundError` | a path did not resolve to a file — usually a working-directory problem (1.11) |
| `RuntimeError` | e.g. `dictionary changed size during iteration` |

**D — not an error at all**

| Error | Mechanism |
|---|---|
| `StopIteration` | the iterator is spent; `next()` raises it; `for` catches it quietly. Spell it exactly |
| `RecursionError` | CPython's depth guard (~1000 frames); an implementation rule, not a law of recursion |

**The `ValueError` / `TypeError` discriminator:** change only the value and it
works ⇒ `ValueError`; change only the type and it works ⇒ `TypeError`.
`ValueError` is not "a value that cannot be converted" — that is one instance.

**`subscriptable`** = supports `x[...]`. `int` does not, so `n[0]` is a
`TypeError`; a list does, so `l[99]` is an `IndexError`.

**`hashable`** = a stable hash; mutable ⇒ unhashable ⇒ `TypeError` as a dict
key or set item, whatever it contains.

---

## 5. `try` / `except`

**What:** run this; if it raises, run that instead of dying.

```python
readings = ["45", "90", "n/a", "30"]
total = 0
for r in readings:
    try:
        total += int(r)
    except ValueError:
        print("skipping bad reading:", r)
print("total:", total)      # skipping bad reading: n/a / total: 165
```

Without it, `int("n/a")` kills the loop and the `45` and `90` already counted
are lost with it.

**When NOT to use it.** Where you *can* check cheaply in advance, do:
`.get()` beats `try` on a dict lookup. `try` earns its place in two
situations:

1. **You cannot ask in advance.** There is no `"n/a".can_be_int()`; checking a
   file exists and *then* opening it is a lie — it can vanish between the
   lines.
2. **The failure is deep.** The thing that breaks is five calls below you and
   you cannot write an `if` around a possibility you cannot see from here.

`try` is not "safer code": a `try` around a bug hides the bug.

---

## 6. Catch the exception you are EXPECTING — never everything

Same file, one typo'd variable (`rdg` for `r`), two ways of "handling" it:

```python
    try:
        total += int(rdg)
    except ValueError:              # SPECIFIC
```
```
Traceback (most recent call last):
  File "t3.py", line 6, in <module>
    total += int(rdg)
NameError: name 'rdg' is not defined
```
Dies on the first reading. Good — the bug is screaming.

```python
    except:                         # BARE
```
```
skipping bad reading: 45
skipping bad reading: 90
skipping bad reading: n/a
skipping bad reading: 30
total: 0
```
**No crash. Exit code 0.** Two good readings reported as junk and `total: 0`
handed back as if it were an answer. The error **is** caught — that is the
crime; say "no error is **reported**".

> **The rule: catch the exception you are EXPECTING.** `except ValueError:`
> says "I know `int()` can fail on junk text and I have a plan." Bare
> `except:` says "whatever goes wrong, pretend it didn't" — including bugs you
> have not found yet. This is raise-vs-shrug one level up: shrug at what you
> expect, let the unexpected raise.

**Worse than a bare `except`:** a catch-all filing into a **named** bucket.

```python
        except Exception:
            state_dict["broken"].append(r)      # "broken" means: this sensor sent garbage
```

A `NameError` in your own code now sends an engineer to swap a cable on a
healthy sensor. A bare `except:` **hides** a fault; a catch-all into a named
bucket **lies** about it.

**`except Exception:` vs bare `except:`.** Bare `except:` catches all of
`BaseException`, including `KeyboardInterrupt` (Ctrl-C) and `SystemExit` —
siblings of `Exception`, not children:

```python
try:
    raise KeyboardInterrupt
except Exception:
    print("swallowed")      # NOT printed — KeyboardInterrupt is not an Exception

try:
    raise KeyboardInterrupt
except:
    print("swallowed")      # printed; Ctrl-C is eaten
```

Never write bare `except:`. `except Exception:` only when you truly need a
wide net; name the class when you can.

---

## 7. `raise`, and exception classes are TYPES

Python raises `ValueError` for `int("2.6")` because Python knows what an
integer looks like. **Python has no idea 200° is illegal for your shoulder
joint.** You tell it:

```python
def check_angle(angle, limit):
    if angle > limit:
        raise ValueError(f"angle {angle} exceeds limit {limit}")
    return angle
```

- **`ValueError("...")` is a CONSTRUCTOR CALL** — an expression that
  **builds** an exception object carrying the message.
- **`raise <object>`** is a statement that **throws** it.
- The text after the colon in every traceback you have ever read **is that
  constructor's argument**:

```
ValueError: invalid literal for int() with base 10: 'n/a'
^^^^^^^^^^  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
the CLASS   the string handed to the constructor
```

**`except ValueError as e`** binds the **exception object itself** to `e` —
the same object the constructor built. `e` is neither the class nor a string:

```python
try:
    int("n/a")
except ValueError as e:
    print(type(e))      # <class 'ValueError'>  — the class that built it
    print(e)            # invalid literal for int() with base 10: 'n/a'
```

(The full class → object model arrives in 1.12; this is the sentence to keep
until then.)

**Why it exists — the division of labour:** the function **DETECTS**, the
caller **DECIDES** (skip, clamp, abort).

```python
for a in readings:
    try:
        safe.append(check_angle(a, limit))
    except ValueError as e:
        print("rejected:", e)       # rejected: angle 200 exceeds limit 180
```

`check_angle` knows 200 is illegal; it does not know the right response.
`raise` reports a problem upward without deciding the response. Returning
`-1` or `None` instead is worse: the caller has to *remember* to check, and
if they forget, `None` goes straight into the data and poisons everything
downstream, silently.

**Refuse vs convert:** a float sails through `0 <= 45.0 <= 90` with no
error, so no `except` will ever see it. If the spec says a float must be
refused, test the type yourself and raise `TypeError`; `int(angle)`
*converts* `45.0` to `45`, the opposite of refusing.

---

## 8. `else` and `finally`

| clause | when it runs |
|---|---|
| `try` | always attempted |
| `except X` | only if a **matching** exception was raised |
| `else` | only if **no** exception was raised |
| `finally` | **always** |

**`finally` is load-bearing; `else` is a scoping tool worth about one line.**

"Always" is stronger than it looks. No `except` at all, a `return` in the
way:

```python
def read(text):
    try:
        return int(text)
    finally:
        print("finally ran for", repr(text))

print(read("45"))
print(read("n/a"))
```
```
finally ran for '45'
45
finally ran for 'n/a'
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'n/a'
```

Four ways out of a `try`, all covered:

1. the `try` finishes normally;
2. it raises and an `except` catches it;
3. it raises and **nothing** catches it — `finally` runs on the way out, then
   the program dies;
4. it hits a `return` — `finally` runs **before** the value leaves.

Why cleanup cannot just go after the block: an exception leaves the function
*before* reaching those lines. Close the file, release the brake, disconnect
the arm — in `finally`. (This is the seed of `with`, 1.11.)

`finally` runs **last** inside its own `try` statement, once per time that
statement is entered:

```python
def inside(items):                  def around(items):
    for x in items:                     try:
        try:                                for x in items:
            print("work", x)                    print("work", x)
        finally:                        finally:
            print("done")                   print("done")
# work 1 / done / work 2 / done     # work 1 / work 2 / done
```

Per-item handling **and** a once-only exit action need two `try` statements,
one inside the other.

**`else`** keeps the `try` down to the one line you meant to guard, so a
`ValueError` from an unrelated later line is not swallowed and blamed on your
input. `except X` narrows by **type**; `else` narrows by **scope**.

```python
try:
    angle = to_angle(text)
except BadCommand:
    log.append(("bad", joint, text))
else:
    log.append(("ok", joint, angle))
    ok = ok + 1
```

---

## 9. Custom exceptions and the hierarchy

### 9.1 Why custom types exist — a collision you can see

`int("n/a")` raises `ValueError`. Your own `raise ValueError(...)` in
`check_angle` raises `ValueError`. **One `except ValueError` cannot tell them
apart**, and they mean completely different things: `"200"` = the sensor
works and the arm may be about to hit something; `"n/a"` = you have gone
blind on that joint. Both vanish into one bucket.

```python
class OverLimit(Exception):
    pass
```

- `class OverLimit(...)` creates a new **type** with that name. (The real
  `class` unit is 1.12; this one line is all exceptions need.)
- **`(Exception)` is load-bearing**: it adds a leaf to the tree, which is
  what lets `raise` accept it and keeps `except Exception` catching it.
- `pass` — the body needs nothing; it inherits everything, including
  message-carrying.
- Ending the name in `Error` is convention only. **Identifiers are not
  paraphrasable**: if the spec says `OverLimit`, `OverLimitError` is a
  different name.

Raise your own type in library code rather than letting a `KeyError` fly: it
hides that `config` happens to be a dict.

### 9.2 The hierarchy is a family tree with a DIRECTION

```
BaseException
├── KeyboardInterrupt      (Ctrl-C)
├── SystemExit             (the program asked to quit)
└── Exception
    ├── LookupError
    │   ├── KeyError
    │   └── IndexError
    ├── ValueError
    │   └── BadCommand     (yours: class BadCommand(ValueError))
    ├── TypeError
    ├── NameError
    │   └── UnboundLocalError
    ├── AttributeError
    ├── ZeroDivisionError
    ├── ImportError
    │   └── ModuleNotFoundError
    ├── OSError
    │   └── FileNotFoundError
    ├── StopIteration
    └── RuntimeError
        └── RecursionError
```

> **A catcher covers its own node and everything BELOW it. Never above.**
> Naming an ancestor catches every descendant; a catcher for the child does
> not catch the parent.

```python
class BadCommand(ValueError):
    pass

try:
    raise BadCommand("bad")
except ValueError:
    print("parent catcher caught the child")     # printed

try:
    int("n/a")                  # a PLAIN ValueError
except BadCommand:              # node BELOW ValueError — out of reach
    print("never printed")
# -> ValueError escapes
```

Choosing the parent when you write `class BadCommand(ValueError)` is
choosing who *else* catches it: callers already catching `ValueError` will.
`except BadCommand:` takes only the error you raised on purpose; a forgotten
`ValueError` from `int()` crashes loudly, which is what you want for a
forgotten case. Own the rule; look up the tree.

### 9.3 `except` ORDERING — specific first, general last

One `try` can carry several `except` blocks. **Python checks them top to
bottom and takes the first whose node covers the error. Then it stops.** They
are alternatives, like `elif`: one runs, or none, never two.

```python
def safe_angles(readings, limit):
    kept = []
    for r in readings:
        try:
            kept.append(check_angle(int(r), limit))
        except JointLimitError as e:
            print("SAFETY:", e)
        except ValueError as e:
            print("SENSOR:", e)
    return kept

print(safe_angles(["45", "90", "200", "n/a"], 180))
# SAFETY: angle 200 exceeds limit 180
# SENSOR: invalid literal for int() with base 10: 'n/a'
# [45, 90]
```

Move `except Exception` (or `except ValueError`) to the top and the
`except JointLimitError` block below it becomes **dead code — Python issues
no warning of any kind.** The wide catcher caught it before it reached the
narrow one; the ancestor eats its own children. **Child above parent,
always.**

---

## 10. Re-raising: bare `raise`, and `raise ... from`

`except` normally means "I am handling this; the caller never finds out".
The middle position — *do something about it (log it, close the gripper) but
do not decide what happens next* — is a **bare `raise`** inside the `except`
block:

```python
try:
    raise ValueError("boom")
except ValueError:
    print("first block ran")
    raise
except Exception as e:
    print("second block ran:", e)
print("after the try")
```
```
first block ran
Traceback (most recent call last):
  File "reraise.py", line 2, in <module>
    raise ValueError("boom")
ValueError: boom
```

1. **`except Exception` did not run.** Once Python enters an `except` block,
   that `try` is finished. Anything raised inside it goes **outward** to an
   enclosing `try`; it is never re-offered to sibling blocks.
2. **The traceback says line 2, not line 5.** A bare `raise` re-throws the
   *original* exception with its *original* traceback, so it still points at
   the real fault. `raise UnidentifiedEpisode(str(e))` builds a **new**
   exception with the same text and a different origin — the bottom frame of
   the traceback moves to your line, and the person debugging is pointed at
   the logger instead of the bad record.

**Catching is not handling.** A function that catches, logs and re-raises is
a **witness**, not a handler; a function that catches and decides has taken a
decision belonging to its caller.

```python
def validate_logged(records, log):
    try:
        output = validate_all(records)
    except UnidentifiedEpisode:
        log.append("UNIDENTIFIED")
        raise                        # put it straight back
    return output
```

**`raise X from e`** — catch a low-level error and raise a clearer one,
recording the first as the **cause**:

```python
def parse(text):
    try:
        return int(text)
    except ValueError as e:
        raise ValueError("bad command: " + text) from e
```
```
ValueError: invalid literal for int() with base 10: 'n/a'

The above exception was the direct cause of the following exception:

ValueError: bad command: n/a
```

Drop `from e` and the middle line reads *"During handling of the above
exception, another exception occurred:"* — as if by accident. That line is
the whole feature. This `from` is unrelated to `from math import sqrt`.

---

## 11. Exceptions as control flow — what a `for` loop really is

```python
it = iter(box)
while True:
    try:
        x = next(it)
    except StopIteration:
        break
    # ...your loop body...
```

**Every `for` loop ever written catches an exception, on every successful
run, as its normal way of finishing.** So "exceptions are for errors" is
wrong: an exception is a signal that travels; whether it counts as an error is
the caller's judgement.

---

## 12. Raise vs return — the takeaway of the unit

Three ways for a function to report a problem:

| | can the caller ignore it? |
|---|---|
| **return a value** (`None`, `-1`, `[]`, `{}`) | **yes — silently** |
| **print** | yes — *and* you have stolen their output policy |
| **raise** | **no** |

```python
config = {"shoulder": 180, "elbow": 150}

def get_joint(config, name):
    if name not in config:
        return None
    return config[name]

angle = 200
limit = get_joint(config, "elbw")       # line 11: the typo
if angle > limit:                       # line 14
    print("OVER LIMIT")
```
```
Traceback (most recent call last):
  File "sentinel.py", line 14, in <module>
    if angle > limit:
TypeError: '>' not supported between instances of 'int' and 'NoneType'
```

**It crashed on line 14. The mistake is on line 11.** `get_joint` understood
the problem and reported it as `None` — a value the caller can carry around
and only trip over later in innocent code. Had it let `config["elbw"]` raise,
you would have `KeyError: 'elbw'` pointing at line 11, naming the typo.

> **A sentinel return moves the failure away from its cause. `raise` keeps
> them together.**

- An unfilled `{}` returned by mistake is worse than `None`: it is falsy,
  iterates zero times, looks like a plausible empty result, and nothing
  complains.
- A **library function that prints** has decided its caller's output policy
  for them (log file? silence? a robot with no terminal?). Raise, or return,
  and let them choose.
- **Report vs raise:** a problem gets *reported* (in the return value) when
  the report can express it; it gets *raised* when it cannot. A validator
  that returns `{"clean": [...], "faulty": {id: [codes]}}` cannot file a
  record with no usable id, so it raises; a placeholder key would silently
  collide and undercount, and undercounting is worse than crashing.
- **Fault codes describe the caller's data, not your implementation.** The
  exception is *how you found out*; the string is *what you report*.
  `"frames"`, not `"TypeError"`.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| exception | a signal that travels; an object built from a class | never bound to a name; not "an error" by nature |
| traceback | record of how far Python got | `SyntaxError` has no frames; read bottom-up |
| "how far did Python get?" | parse → name → dot → type → value | the brackets never decide the error; the container does |
| `SyntaxError` / `IndentationError` | compile time; nothing runs | a `try:` with no `except` is one |
| `NameError` / `UnboundLocalError` | no such name / local but unbound | compile-time locality decides which |
| `AttributeError` | the dot failed | the name before the dot was fine |
| `TypeError` | operation impossible for the type | covers unhashable, not subscriptable, not callable, wrong arg count |
| `ValueError` | right type, wrong value | includes unpacking count mismatches |
| `IndexError` / `KeyError` / `LookupError` | position / key absent; their parent | slicing never raises `IndexError` |
| `StopIteration` / `RecursionError` | not errors: iterator spent / depth guard | spell `StopIteration` exactly |
| `try` / `except X` | run this; on a matching raise, run that | a `try` around a bug hides the bug |
| bare `except:` | catches all of `BaseException` | turns a typo into a silent wrong answer, exit code 0; eats Ctrl-C |
| `except Exception:` | widest sane net | still catches your own typos; name the class when you can |
| catch-all into a named bucket | files unknown faults as a known kind | worse than bare — it lies |
| `except X as e` | binds the thrown **object** | `type(e)` is the class; `print(e)` the message |
| `else` | runs only if the `try` did not raise | narrows by scope |
| `finally` | runs on every way out, last, once per entry of its `try` | including through `return` and an uncaught raise |
| `raise Cls("msg")` | constructor call builds the object; `raise` throws it | the text after the colon is that argument |
| the division of labour | the function detects, the caller decides | a sentinel makes the caller remember |
| `class X(Exception): pass` | a new error type | the `(Exception)` is the load-bearing part |
| hierarchy direction | a catcher covers its node and below | a child catcher does not catch its parent |
| `except` ordering | first match top-down wins | parent above child makes the child dead code, silently |
| bare `raise` | re-throws the same object, original traceback | not re-offered to sibling blocks |
| `raise X from e` | records `e` as the cause | different keyword from `from x import y` |
| catching vs handling | witness vs decider | a logger should be a witness |
| `for` loop | `while True` / `next` / `except StopIteration: break` | exceptions are control flow every day |
| raise vs return | a raise cannot be ignored | a sentinel moves the crash away from the cause |
| `print` in a library | decides the caller's output policy | raise or return instead |
| refuse vs convert | `type(x) != int` refuses; `int(x)` converts | a float passes a comparison silently |
