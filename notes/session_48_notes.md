# Session 48 — notes (Sun 13 Sep 2026, 17:43 → 21:48)

**What this session was:** you opened ~34 hours after S47 and ruled that
revision is yours to run (oral agent on `notes/units/`; you will ask for a
volley when you want one). No volley fired. **1.12 OOP opened** with its
frame and ran through eleven files in `teaching/s48_oop/` and one drill,
`drills/s48_joint.py`, 10/10. Everything is [~]: same-session evidence
cannot be [x]. Zero pushbacks. You stopped before reading the last file
(`class_attr.py`); it is re-issued in full at the start of S49, so this
notes file covers it too, at the end of section 1.

---

## SELF-TEST — do this first, notes closed

1. `class Joint: pass` then `a = Joint(); b = Joint()`. What is `a is b`,
   and what does `type(a)` print when the file is run directly?
2. `a.name = "elbow"` works on a `Joint`. `x = list(); x.name = "elbow"`
   does not. Name the error and give the one-word reason.
3. What does `vars(a)` return, and how is it related to `a.angle`?
4. `Joint("elbow", 10)` with `def __init__(self, name, angle)`. List the
   three things the call does, in order, and say what it returns.
5. What does `__init__` itself return? Where does that value go?
6. `Joint("elbow")` against that same `__init__`. Error name, and why it is
   not `AttributeError`.
7. `a.move(5)` with `def move(self, delta)`. What fills `self`, and what
   decided that?
8. `Joint.move` and `a.move` print differently. What are the two kinds of
   thing, and what extra does the second one carry?
9. `vars(a)` has no key `move`. Where does `a.move` find it, and in what
   order does the dot lookup search?
10. Write `is_safe(self)` in ONE line, given `self.angle` and `self.limit`,
    inclusive at both ends.

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

All files live in `teaching/s48_oop/`. Run each from inside that folder:
`cd teaching/s48_oop` then `python3 <file>`.

### 1.0 The frame

A `class` statement adds a new TYPE to the ones you already use (`int`,
`str`, `list`, `dict`, `Path`). Calling the type makes an object of that
type, the way `list()` makes a list. Functions written inside the class
become the things you call with a dot on the object, like `f.close()`.

Why it exists: a joint as a dict plus loose functions leaves two things
loose. Nothing says which functions fit the dict. Nothing says the dict IS
a joint; `type()` says `dict`. A class ties the shape and the functions
under one name, and `type(j)` says `Joint`.

What it buys: the functions travel with the data (`j.move(5)`); a real
type of your own (`isinstance`, the exception tree, error messages that
name your thing); and readability — every `nn.Module`, `Path`, file
object and exception you have used is an instance of a class.

What it does NOT buy: anything a dict plus functions cannot do. It is
organisation plus a name. For twenty lines, a dict is fine.

Cheap: the words class, instance, attribute, method, `self`. Load-bearing:
**the class is a factory for objects, and `self` is the object handed in
as the first argument.**

### 1.1 A class statement makes a type; calling it makes an object — `make_one.py`

```python
class Joint:
    pass

a = Joint()
b = Joint()

print(type(a))
print(a is b)
```
```
<class '__main__.Joint'>
False
```

`class Joint:` runs like `def`: it creates a type object and binds `Joint`
in the module namespace. `pass` because a block cannot be empty. `Joint()`
calls the type and returns a fresh object each time, so `a is b` is
`False`. The dotted name `__main__.Joint` is 1.10: the class lives in the
module the file became. Imported, it would say `make_one.Joint`.

### 1.2 What an empty object shows — `print_one.py`

```python
class Joint:
    pass

a = Joint()
b = Joint()
print(a)
print(b)
```
```
<__main__.Joint object at 0x7d2564a35160>
<__main__.Joint object at 0x7d2564a350d0>
```

Type plus address (the `id()` number). Nothing about contents, because an
empty class makes empty objects. `[]` prints `[]` because a list knows how
to display itself; `Joint` does not yet. The line that fixes that is
`__repr__`, next session.

### 1.3 Attaching data by dot — `attach.py`

```python
class Joint:
    pass

a = Joint()
b = Joint()

a.name = "elbow"
a.angle = 10

b.name = "wrist"

print(a.name, a.angle)
print(b.name)
print(b.angle)
```
```
elbow 10
wrist
Traceback (most recent call last):
  File ".../attach.py", line 14, in <module>
    print(b.angle)
          ^^^^^^^
AttributeError: 'Joint' object has no attribute 'angle'
```

A dot on the LEFT of `=` attaches a value to the object under that name:
an **attribute**. Each object has its own set. `b` was never given
`angle`, so reading it is `AttributeError` — the ATTRIBUTE is what broke,
and the message names the type and the missing name. Same mechanism as
`arm.limits` after `import arm` alone.

### 1.4 The dict underneath — `look_inside.py`

```python
class Joint:
    pass

a = Joint()
b = Joint()

a.name = "elbow"
a.angle = 10
b.name = "wrist"

print(vars(a))
print(vars(b))
print(vars(a)["angle"])
```
```
{'name': 'elbow', 'angle': 10}
{'name': 'wrist'}
10
```

`vars(a)` is a plain dict: every attribute is a key. Same function you
used on a module. `a.angle` and `vars(a)["angle"]` read the same `10`. An
object is a dict of attributes with a type stamped on it; the dot is a
dict lookup, and a missing key through the dot is `AttributeError` rather
than `KeyError`. Your line: "built on usual things we already use" — this
is the usual thing.

### 1.5 Your question: can a list take an attribute? — `no_dict.py`

```python
a = list()

try:
    a.name = "ankur"
except AttributeError as e:
    print("attach:", e)

try:
    print(vars(a))
except TypeError as e:
    print("vars:  ", e)

def f():
    pass

f.name = "ankur"
print(vars(f))
```
```
attach: 'list' object has no attribute 'name'
vars:   vars() argument must have __dict__ attribute
{'name': 'ankur'}
```

No. A list, tuple, dict, int or str carries no attribute dict, so there is
nowhere for a new name to land. The `TypeError` message gives the real
name of that dict: `__dict__`. Functions, modules, and objects of classes
you write all have one. Why the built-ins refuse: they are built in C with
a fixed layout (a list is a length plus item slots); no per-object dict
means less memory and a faster object, and there are millions alive.
Rule: **attaching a name by dot needs a `__dict__` on the object.** One
line ahead, parked for 1.13: your own class can opt out of the `__dict__`
to be lean like a list.

### 1.6 `__init__` — `init.py`

```python
class Joint:
    def __init__(self, name, angle):
        print("init running, self is", self)
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a)
print(vars(a))
print(vars(b))
```
```
init running, self is <__main__.Joint object at 0x7f68c988b6b0>
init running, self is <__main__.Joint object at 0x7f68c988b6e0>
<__main__.Joint object at 0x7f68c988b6b0>
{'name': 'elbow', 'angle': 10}
{'name': 'wrist', 'angle': 45}
```

`__init__` is an ordinary `def` inside the class block; the double
underscores mark a name Python looks for itself, at the moment the class is
called. `Joint("elbow", 10)` does: make an empty object; call `__init__`
with that object as the first argument (`self`) and your arguments after
it; return the object. The address printed for `self` equals the address
of `a` — two names, one object. `self.name = name` is the dot assignment
from 1.3, now done by the class every time, so every `Joint` has the same
shape. `__init__` has no `return` and you never call it yourself.

Precision: in this course "constructor" is the TYPE CALL (`list()`,
`Joint()`), the thing that makes the object. `__init__` is the
INITIALISER: it fills an object that already exists.

### 1.7 A wrong call is `TypeError` — `init_short.py`

```python
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow")
```
```
TypeError: Joint.__init__() missing 1 required positional argument: 'angle'
```

`__init__` has three parameters; the call supplied two (the new object and
`"elbow"`). Same failure as `add(1)` against `def add(x, y)`. It happens
before any attribute exists, so there is no object to raise
`AttributeError` from. Discriminator: **a wrong CALL is `TypeError`, at the
parentheses; a wrong DOT READ is `AttributeError`, at the dot.**

### 1.8 Your question: what does `Joint(...)` return, and can I pass `self`? — `by_hand.py`

```python
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
print(vars(a))

result = Joint.__init__(a, "shoulder", 90)
print(result)
print(vars(a))

b = Joint(a, "elbow", 10)
```
```
{'name': 'elbow', 'angle': 10}
None
{'name': 'shoulder', 'angle': 90}
Traceback (most recent call last):
  File ".../by_hand.py", line 13, in <module>
    b = Joint(a, "elbow", 10)
        ^^^^^^^^^^^^^^^^^^^^^
TypeError: Joint.__init__() takes 3 positional arguments but 4 were given
```

The type call returns the new object. `__init__` returns `None` like any
function without `return`, and the type call throws that `None` away.
`Joint.__init__(a, ...)` reaches the plain function through the class and
fills `self` by hand: legal, overwrites `a`'s dict, makes no new object.
`Joint(a, "elbow", 10)` is the type call, so Python puts a fresh object in
`self` itself and your three land on two parameters: 4 given, 3 taken.
You will never write the by-hand form in real code; it only shows `self`
is nothing special.

### 1.9 Methods — `method.py`

```python
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def move(self, delta):
        self.angle = self.angle + delta

a = Joint("elbow", 10)
b = Joint("wrist", 45)

a.move(5)
b.move(-40)
print(vars(a))
print(vars(b))

Joint.move(a, 100)
print(vars(a))
```
```
{'name': 'elbow', 'angle': 15}
{'name': 'wrist', 'angle': 5}
{'name': 'elbow', 'angle': 115}
```

Any `def` in the class block works like `__init__` did: called through an
object with a dot, the object fills the first parameter. `a.move(5)` reads
and writes `a`'s dict; `b.move(-40)` the same function on `b`'s dict.
`Joint.move(a, 100)` is the by-hand form. A function defined in the class
and called through an object is a **method**.

### 1.10 How Python decides what `self` is — `bound.py`

```python
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def move(self, delta):
        self.angle = self.angle + delta

a = Joint("elbow", 10)

print(vars(a))
print(Joint.move)
print(a.move)

m = a.move
m(5)
print(vars(a))
```
```
{'name': 'elbow', 'angle': 10}
<function Joint.move at 0x7010fe4acfe0>
<bound method Joint.move of <__main__.Joint object at 0x7010fe48f800>>
{'name': 'elbow', 'angle': 15}
```

**The thing on the left of the dot fills `self`.** `vars(a)` has no
`move`; the function is not in the object. `Joint.move` through the class
is a plain `function`. `a.move` through the object is a **bound method**:
the dot lookup looked in `vars(a)`, found nothing, looked in the type,
found the function, and because it arrived via an object it wrapped the
function and that object together. `m = a.move; m(5)` calls it with no
`a` in sight, and the wrapper supplies its stored object as `self`.

Two-line model: **attributes live in the object dict, found first;
methods live on the type, found second, and arrive already holding the
object that asked.**

### 1.11 Class attributes — `class_attr.py` (UNREAD in S48; re-issued at the S49 open)

```python
class Joint:
    unit = "deg"

    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a.unit, b.unit)
print(vars(a))
print(vars(b))
print("unit" in vars(Joint))
print("__init__" in vars(Joint))
```
```
deg deg
{'name': 'elbow', 'angle': 10}
{'name': 'wrist', 'angle': 45}
True
True
```

`unit = "deg"` is an assignment in the class block, outside any `def`. It
runs once when the `class` statement runs and binds `unit` in the CLASS's
dict: a **class attribute**. `a.unit` and `b.unit` both read `"deg"`, yet
neither object dict has `unit`. The dot went object dict first (nothing),
then the type's dict (found). `__init__` is in `vars(Joint)` too: methods
are class attributes, functions stored in the class dict. Two dicts, one
order: **object first, class second.** Data attached through `self` is
per-object; names bound in the class block are shared, one copy.

Held [PREDICT] for S49, not yet posed: `a.unit = "rad"` then `a.unit`,
`b.unit`, `vars(a)`.

### 1.12 The drill — `drills/s48_joint.py`

Spec: `Joint(name, angle, limit)` with exactly three attributes; `move`
changes `angle` in place, returns `None`; `is_safe` inclusive between
`-limit` and `limit` (boundary side in the tests only); `describe` returns
`"<name> at <angle> deg"`. Ten mentor tests in `tests/test_s48_joint.py`.

Your first run: 9/10. `describe` printed the string; the test received
`None` and pytest captured the text on stdout. You fixed it in one edit.
Your `is_safe` was 4/4 including both boundaries.

---

## 2. THINKING GAPS THIS SESSION — with classification

| # | Where | What happened | Type |
|---|---|---|---|
| 1 | `print(Joint())` [PREDICT] | "not sure" — no model of what an empty object shows | Knowledge gap, fair (untaught); fact run |
| 2 | `Joint("elbow")` [PREDICT] | said `AttributeError`; it is `TypeError` (a wrong call fails at the parentheses) | Knowledge gap, not ledger; discriminator given |
| 3 | `a.move(5)` [TEACH-BACK] | "I don't know how python decides that" | Named gap, honest; `bound.py` |
| 4 | Drill `describe` | `print` where the spec said `return`; test got `None` | REPEAT of the S36 output-policy point → spec-reading slip (lazy read of the word "return") |
| 5 | Done line | named `is_safe` (4/4); the bug was in `describe` | Calibration — the done line is 0 for 3 |
| 6 | `is_safe` shape | `if cond: return True else: return False` | Style habit, same family as `if flag == False`; given once |

Nothing ledger-eligible moved. No ratings were taken (no [RECALL] fired).

## 3. TEACHING MISTAKES THIS SESSION

- **`class_attr.py` went out before you had replied to the previous
  idea.** You had just given the `move` teach-back; the sharpening and the
  next file were in one turn and you did not read it. Rule for the mentor:
  nothing sent after a teach-back reply is taught until you reply to it.
  Re-issue at S49.
- **`print(Joint()); print(Joint())` printed the same address twice** in
  the first draft (the first object is freed before the second is made).
  Caught before showing; rewritten with bound names. Never on your screen.
- Held: interval gate, prerequisite gate, doubt gate before each idea, one
  idea per turn, paste-walk-ask, every fact by running, no error name in a
  header, name-the-error before the traceback, direct questions answered
  then proved, done line, "find it" on red, close in the turn you asked.

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | Trap |
|---|---|---|
| `class X:` | statement; creates a type object, binds `X` | runs like `def` — the body executes once at definition |
| `X()` | the type call: makes an object, runs `__init__`, returns the object | this is the "constructor"; `__init__` is not |
| `__init__(self, ...)` | fills the new object; called by the type call | returns `None`; never call it yourself; missing args → `TypeError` |
| `self` | the object left of the dot, passed as the first argument | never passed by you in the dot form; `X(a, ...)` puts a fresh object in `self` and shifts your args |
| attribute (`a.x = v`) | a key in the object's `__dict__` | reading a missing one is `AttributeError`, not `KeyError` |
| `vars(obj)` | the `__dict__` as a plain dict | `TypeError` on built-ins (list, tuple, int, str, dict): they have no `__dict__` |
| method | a function in the class dict, called through an object | not in `vars(a)`; found in `vars(Joint)` |
| bound method | `a.move`: the function plus the object that asked | `Joint.move` is the bare function; `m = a.move` keeps `a` inside |
| lookup order | object dict, then class dict | (S49) an object attribute of the same name shadows the class one |
| class attribute | a name bound in the class block, shared by every object | lives in `vars(Joint)`, not in any object dict |
| `TypeError` vs `AttributeError` | wrong CALL vs wrong DOT READ | the call fails before any attribute exists |

## 5. NEXT

Re-issue of `class_attr.py` plus its [PREDICT]; `__repr__`/`__str__` (the
readable print); class and static methods (with `@` as spelling only);
inheritance, overriding, `super()`, and paying `except ... as e`; then
encapsulation, polymorphism, composition, dataclasses; then the LeRobot
block. Revision when you ask for it.
