# Session 49 — notes (Mon 14 Sep 2026, 20:47 → ~21:00)

**What this session was:** short. You opened ~23 hours after S48, ruled no
revision again, and stopped after about fifteen minutes because you were
tired. Three ideas in `teaching/s49_oop/`: the class-attribute file from
S48 re-issued and read (its [PREDICT] answered), `__repr__` taught, and
class methods opened but not confirmed — you will start from class methods
at S50. Everything here is [~]; same-session evidence cannot be [x]. No
drill. Zero pushbacks.

---

## SELF-TEST — do this first, notes closed

1. `class Joint: unit = "deg"` plus an `__init__` setting `name` and
   `angle`. After `a = Joint("elbow", 10)`, is `"unit"` a key in `vars(a)`?
   Where is it a key?
2. `a.unit` works anyway. State the lookup order in two words.
3. After `a.unit = "rad"`: what are `a.unit`, `b.unit` (a second object)
   and `vars(a)`? Which dict did the write go into?
4. What is the ONLY way to change the class's copy of `unit`?
5. `print(a)` shows `<__main__.Joint object at 0x...>`. Name the method
   that replaces it, and say what it must return.
6. Does `__repr__` print, or return? Who calls it?
7. What does "dunder" mean, and what is special about a dunder name?
   Name five you had met before `__repr__`.
8. `print([a, b])` where both have `__repr__`. What prints, and why does a
   printed list of strings show quotes for the same reason?
9. `print` tries one dunder before `__repr__`. Which, and what happens if
   it is missing?
10. `Joint.from_dict(d)` is called with no object in existence. What fills
    its first parameter, and what decided that?

Answers are in section 1. Check only after you have written yours.

---

## 1. FULL TEACHING — from scratch, with runnable code

Run every file from inside `teaching/s49_oop/`.

### 1.1 Class attributes, re-issued — `teaching/s48_oop/class_attr.py`

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
$ python3 class_attr.py
deg deg
{'name': 'elbow', 'angle': 10}
{'name': 'wrist', 'angle': 45}
True
True
```

Six points:

1. `unit = "deg"` sits in the class block, not in `__init__`. An assignment
   there goes into the **class's** dict, `vars(Joint)`.
2. `vars(a)` and `vars(b)` have no `unit`. Object dicts hold only what
   `__init__` (or a later dot-assignment) put there.
3. `a.unit` still works: the dot READ checks the object dict first, finds
   nothing, then checks the class dict and finds `"deg"`.
4. `"unit" in vars(Joint)` is True: that is where it lives.
5. `"__init__" in vars(Joint)` is also True. **Methods are class attributes
   too** — same dict, same lookup. That is why `a.move` was found in S48
   without `move` being in `vars(a)`.
6. The model: **two dicts, checked in order** — object, then class. One
   shared copy of `unit`; one copy of `name` per object.

### 1.2 The shadowing [PREDICT] — `shadow.py`

Your answer: `rad`, `deg`, then the class dict. The first two were right;
the third was the wrong dict. Your own first two lines already said the
write had gone into `a`'s dict (otherwise `b.unit` would have changed too).

```python
class Joint:
    unit = "deg"

    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

a.unit = "rad"
print(a.unit)
print(b.unit)
print(vars(a))
print(vars(Joint)["unit"])
```
```
$ python3 shadow.py
rad
deg
{'name': 'elbow', 'angle': 10, 'unit': 'rad'}
deg
```

The rule, in one line: **`obj.x = value` always writes into the object's
own dict, never the class's.** The class copy changes only if you write
`Joint.unit = ...`. Reads are two-dict; writes are one-dict.

### 1.3 `__repr__` — `no_repr.py` and `with_repr.py`

**Frame.** WHAT: a method you write in the class; Python calls it whenever
it needs a text form of the object (print, f-string, traceback, an element
inside a printed list). WHY: without it Python knows nothing about your
object but its type and address. WHAT IT BUYS: one method, and every
print, log and traceback for that class becomes readable. Convention:
return the call that would rebuild the object.

```python
# no_repr.py
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a)
print([a, b])
```
```
$ python3 no_repr.py
<__main__.Joint object at 0x770bac235670>
[<__main__.Joint object at 0x770bac235670>, <__main__.Joint object at 0x770bac2361b0>]
```

```python
# with_repr.py
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def __repr__(self):
        return f"Joint('{self.name}', {self.angle})"

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a)
print("__repr__" in vars(Joint))
print([a, b])
```
```
$ python3 with_repr.py
Joint('elbow', 10)
True
[Joint('elbow', 10), Joint('wrist', 45)]
```

Walk:

1. `__repr__` is a plain method: `self` is the object left of the dot. It
   **returns a string**. It does not print.
2. It sits in `vars(Joint)` like `__init__` and `move`. Storage is not
   special.
3. The only special thing is **who calls it**. You never write
   `a.__repr__()`. Python calls it, at a fixed moment, because of the name.
4. **Dunder** = **d**ouble **under**score. A name Python looks for at a
   fixed moment. Already met: `__init__` (at the type call), `__dict__`,
   `__file__`, `__name__`, `__main__`. `__repr__` is the sixth.
5. `__str__`: `print` and f-strings look for `__str__` first, then fall
   back to `__repr__`. Define `__repr__` only unless you need two forms.
6. The list [PREDICT] (you got it right): the list has no idea what a
   `Joint` is. It asks each element for its `__repr__` and joins them.
   Same reason `print(['a', 'b'])` shows quotes: the quotes come from
   `str`'s own `__repr__`.

### 1.4 Class methods — `from_dict.py` (delivered; re-issued at S50)

**Frame.** WHAT: a method whose first parameter receives the **class**,
not an object. Spelling: `@classmethod` on the line above the `def`; first
parameter `cls` by convention. WHY: `__init__` takes one fixed shape,
`Joint("elbow", 10)`. Real data arrives as a dict from JSON or a CSV row.
You want a second door in, and it has to run before any object exists, so
it cannot get `self`. WHAT IT BUYS, honestly: today only tidiness — a plain
function `make_joint(d)` would work. The real payoff comes at inheritance,
when `cls` is not always `Joint`.

```python
class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def __repr__(self):
        return f"Joint('{self.name}', {self.angle})"

    def move(self, delta):
        self.angle = self.angle + delta

    @classmethod
    def from_dict(cls, d):
        print("cls is", cls)
        return cls(d["name"], d["angle"])

d = {"name": "elbow", "angle": 10}
a = Joint.from_dict(d)
print(a)
print(vars(a))
print(a.move)
```
```
$ python3 from_dict.py
cls is <class '__main__.Joint'>
Joint('elbow', 10)
{'name': 'elbow', 'angle': 10}
<bound method Joint.move of Joint('elbow', 10)>
```

Walk:

1. The call is `Joint.from_dict(d)`. Left of the dot is the class. No
   object exists yet.
2. `cls` is `Joint`. What fills `cls` is the thing left of the dot,
   exactly as `self` was in S48 — only now that thing is the class.
3. `cls(d["name"], d["angle"])` is `Joint("elbow", 10)` under another
   name: the type call runs, `__init__` fills, the object comes back.
4. `@classmethod` is **spelling only** for now: a line starting with `@`
   above a `def` changes how that `def` is stored in the class dict. The
   mechanism is 1.13 (decorators/closures).
5. `a.move` is a bound method holding `a` (S48 `bound.py`).

**The open [PREDICT]:** what does `print(Joint.from_dict)` print? Reason
from point 5 and point 2. Answered at S50, then run.

**Owed one line:** `@staticmethod` — a plain function stored in the class
for tidiness; receives neither the object nor the class.

---

## 2. THINKING GAPS THIS SESSION — with classification

| # | Where | What happened | Type |
|---|---|---|---|
| 1 | `vars(a)` after `a.unit = "rad"` [PREDICT] | gave the class dict (`{"unit": deg, __init__}`) for the object dict | Which-dict slip, not a model gap — his own lines 1–2 required the object dict to hold the write; right after one pointer; not ledger |

Nothing ledger-eligible moved. No ratings taken (no [RECALL] fired).

## 3. TEACHING MISTAKES THIS SESSION

- None caught by you; zero pushbacks. Mentor-side: `from_dict.py` went out
  in a full turn (frame, file, five-point walk, [PREDICT]) at the moment you
  were tiring — you stopped without reading it. Same lesson as S48's
  `class_attr.py`: nothing delivered is taught until you reply to it.
  Re-issue in full at S50; do not assume the frame was read.
- Held: interval gate from the repo; parked rule asked once and dropped;
  paste-walk-ask with path, command, output; frame first with the honest
  "today only tidiness"; [PREDICT] from the screen only; one pointer on the
  miss, never the answer; proof by running; doubt gate before each idea;
  close in the turn you asked.

## 4. REFERENCE CHECKLIST — name, what it does, the trap

| Name | What it does | Trap |
|---|---|---|
| class attribute | a name bound in the class block; one shared copy in `vars(Joint)` | never in any object dict; visible through every object by fall-through |
| dot READ | object dict first, then class dict | a same-named object attribute hides the class one |
| dot WRITE (`obj.x = v`) | writes the object's own dict, always | it never touches the class copy; `Joint.x = v` is the only way |
| `__repr__(self)` | returns the text form; Python calls it for print, f-string, traceback, list element | it must RETURN a string; printing inside it is the S36 output-policy bug again |
| `__str__` | tried first by `print`/f-strings | falls back to `__repr__`; define `__repr__` only unless two forms are needed |
| dunder | double-underscore name Python looks for at a fixed moment | stored like any attribute; only the CALLER is special |
| `@classmethod` / `cls` | the class left of the dot fills `cls`; `cls(...)` is the type call | `@` is spelling only until 1.13; runs before any object exists, so no `self` |
| `@staticmethod` | a plain function kept in the class for tidiness | receives neither object nor class (owed, one line) |

## 5. NEXT

Re-issue `from_dict.py` in full and take its [PREDICT]; `@staticmethod` one
line; inheritance, overriding, `super()`, and paying `except ... as e`;
encapsulation, polymorphism, composition, dataclasses; then the LeRobot
block. Revision when you ask for it.
