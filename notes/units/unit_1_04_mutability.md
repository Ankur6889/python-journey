# Unit 1.4 — Mutability vs Immutability

Whether an object can change in place, and everything that follows from it:
aliasing that matters, arguments to functions, the mutable default trap,
shallow vs deep copy, and how to tell whether a method mutates.

---

## 1. What mutability means

- **Mutable** — the object can be changed in place: same object, same `id()`,
  different contents. `list`, `dict`, `set`.
- **Immutable** — the object cannot be changed. Any "change" builds a **new**
  object and rebinds the name; the original is untouched. `int`, `float`,
  `bool`, `str`, `tuple`.

```python
lst = [1, 2, 3]
print(lst, id(lst))         # [1, 2, 3] 140234891234567
lst.append(4)
print(lst, id(lst))         # [1, 2, 3, 4] 140234891234567   same id — mutated

s = "hello"
print(s, id(s))             # hello 140234889112345
s = s + " world"
print(s, id(s))             # hello world 140234887654321  new id — rebound
```

> **Immutable → the name moves. Mutable → the object changes and the name
> stays.**

`id()` is the ground truth: unchanged → the object was mutated in place;
changed → the name was rebound to a new object.

The whole unit rests on one question: **does an operation change the original
object, or return a new one?**

---

## 2. Aliasing, demonstrated properly

`b = a` never copies; it binds a second name to the same object (1.2 §5).
With an immutable object nothing can be done to it through either name, so
the alias is harmless. With a mutable object, a change through one name is
visible through the other:

```python
a = [1, 2, 3]
b = a
print(id(a) == id(b), a is b)   # True True
b.append(99)
print(a)                        # [1, 2, 3, 99]
```

Contrast an immutable:

```python
x = "hello"
y = x                   # alias
y = y + " world"        # REBINDS y to a brand-new string
print(x, y)             # hello hello world
print(x is y)           # False
```

If strings were mutable, `x` would have changed too. **The immutability of
`str` is what makes the second line safe.**

---

## 3. Why this matters when passing objects to functions

**Passing an argument to a function is an assignment.** It binds a new local
name inside the function's frame to the **same object** the caller passed.
That single fact produces the whole behaviour.

```python
def mutate(lst):
    lst.append(99)      # acts on the OBJECT

def rebind(lst):
    lst = [99]          # rebinds the LOCAL NAME only

data = [1, 2, 3]
mutate(data)
print(data)             # [1, 2, 3, 99]   caller sees it

data2 = [1, 2, 3]
rebind(data2)
print(data2)            # [1, 2, 3]       caller sees nothing
```

> **MUTATE and the caller sees it. REBIND and the caller does not.**

`lst = lst + [value]` inside a function builds a new object bound to a local
name, discarded on return — the caller is unaffected. This is a **semantic**
reading, not "is there an `=`": classify by what the statement does to the
**object** versus the **name** (1.2 §6).

Frames are separate; the object is shared. Namespaces hold names, not
objects, so two frames can each hold a name for one heap object.

The same rule explains why a function can silently corrupt a caller's data:

```python
def calibrate(readings):
    readings.append(0.0)
    return sum(readings)

joint_angles = [10.0, 20.0, 30.0]
print(calibrate(joint_angles))  # 60.0
print(joint_angles)             # [10.0, 20.0, 30.0, 0.0]   — changed under the caller
```

---

## 4. Mutating methods return `None`

A method call does two independent things: a **side effect** (it may change an
object in place) and a **return value**. For the in-place mutators on `list`
(`append`, `extend`, `insert`, `remove`, `sort`, `reverse`, `clear`) the
return value is always `None`.

```python
q = [1, 2, 3]
result = q.append(4)
print(q)            # [1, 2, 3, 4]   the list WAS mutated
print(result)       # None           append returned None, not the list
```

The classic broken line:

```python
q = [].append(4)
print(q)            # None  — the [4] list is unreachable and collected
l = [3, 1, 2]
l = l.sort()        # silently replaces the list with None
```

`lst.append(x)`, `lst.sort()` and friends are **statements in disguise** —
never the right-hand side of an assignment. Call them bare: `l.sort()`.

The durable test for any call: **does it MUTATE or BUILD?** Mutate → returns
`None`, don't assign. Build → returns a new object, do assign. (Not "methods
return `None`, functions return values" — `str.upper()` is a method that
builds.)

---

## 5. The discriminator: how to tell whether an unfamiliar method mutates

Not a roster to memorise. Two steps, run in this order:

**Step 1 — the TYPE.** Is the object mutable or immutable? **An immutable
object cannot have a mutating method at all.** So every `str`, `int`, `tuple`
method necessarily returns a new object. Nothing to memorise.

**Step 2 — for mutable types, the return value as a ONE-DIRECTIONAL hint.**

| Direction | Holds? |
|---|---|
| returns `None` ⇒ it mutated | **Yes** — returning `None` serves no other purpose |
| mutates ⇒ returns `None` | **No** — `pop` mutates *and* returns the removed item |

```python
path = ["home", "pick", "lift", "place"]
print(path.reverse())       # None       -> mutated
print(path.count("home"))   # 1          -> a value back tells you NOTHING; count reads
print(path.pop())           # home       -> a value back, AND it mutated
print(path)                 # ['place', 'lift', 'pick']

data = [3, 1, 2]
out = data.extend([7, 8])   # never seen extend before?
print(out)                  # None       -> you can infer: data was mutated in place
```

Python's deliberate **name-pairs** make the design visible: `sort` mutates /
`sorted` returns new; `reverse` mutates / `reversed` returns new. Two names
because there are two behaviours.

| Call | Behaviour | Returns |
|---|---|---|
| `l.append(4)`, `l.extend([5, 6])`, `l.insert(0, 99)`, `l.remove(x)`, `l.sort()`, `l.reverse()`, `l.clear()` | mutate in place | `None` |
| `l.pop()` | mutates **and** returns the removed item | the item |
| `l.count(x)`, `l.index(x)` | read only | an `int` |
| `l.copy()`, `sorted(l)`, `reversed(l)` | leave the original alone | new list / new list / iterator |
| `s.upper()`, `s.strip()`, `s.split()` | cannot mutate (`str` is immutable) | new object |

---

## 6. The mutable default argument

**The broken version:**

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item(1))      # [1]
print(add_item(2))      # [1, 2]
print(add_item(3))      # [1, 2, 3]
```

**Why:** the default expression `[]` is evaluated **once — when the `def`
statement executes**, not on each call. That single list lives on the
**function object**, in its `__defaults__` attribute (a tuple), and is reused
by every call that omits the argument.

```python
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

print(add_item.__defaults__)    # ([],)
add_item(1)
print(add_item.__defaults__)    # ([1],)   — the default itself was mutated
```

Where the default lives, and why it accumulates: **not** in the function's
namespace — that is created fresh per call and destroyed on return, and if the
list lived there it would vanish each time and there would be no trap. It lives
on the **durable** function object, which outlives every call.

**The fix — a sentinel:**

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket

print(add_item(1))          # [1]
print(add_item(2))          # [2]
print(add_item(3, [7]))     # [7, 3]
```

`None` is immutable, so sharing it is harmless; the fresh list is built in the
**body**, which runs on every call. Sentinel check first, then the work
**outside** the branch. Two bugs commonly appear in the "fix":
`lst = [].append(value)` (binds `None`) and putting the append inside the
`if` (a caller-supplied list is never appended to).

Use `is None`, not `== None` (1.2 §11).

- **Safe defaults:** `0`, `""`, `None`, tuples — immutable, nothing to
  accumulate into.
- **Unsafe defaults:** `[]`, `{}`, `set()`, any mutable object.
- Supplying your own argument binds the parameter to *your* object, so
  `add_item(5, [])` works even in the broken version. **The bug only bites
  when the default applies.**

---

## 7. Shallow vs deep copy

A direct consequence of aliasing.

- **`b = a`** is not a copy at all. One object, two names.
- **Shallow copy** — `a.copy()`, `a[:]`, `list(a)`, `dict(d)`, `d.copy()`,
  `copy.copy(a)` — builds a new **outer** container and fills it with **the
  same inner references**. New box, same contents. **Shallow = one level
  deep.**
- **Deep copy** — `copy.deepcopy(a)` — new outer container **and** new
  copies of everything inside, recursively. Nothing shared.

```python
import copy

a = [[1, 2], [3, 4]]
shallow = a.copy()
deep = copy.deepcopy(a)

print(a is shallow, a[0] is shallow[0])     # False True   — new outer, SHARED inner
print(a[0] is deep[0])                      # False        — new all the way down

shallow[0].append(99)
print(a)        # [[1, 2, 99], [3, 4]]   — the append followed the shared reference
print(deep)     # [[1, 2], [3, 4]]       — untouched
```

The inner list was **not copied**; it was **aliased** — a second name attached
to the existing object. That is the entire concept.

- The trap only fires when the container holds **mutable** objects. For a flat
  list of numbers or strings a shallow copy is indistinguishable from a real
  copy, because the shared items cannot be mutated anyway.
- `copy.deepcopy` is **not "the better copy"**: it is slower (it walks the
  whole structure) and copies things you may have wanted shared. On a flat
  container of immutables it buys nothing over `[:]`. Most of the time the
  right answer is to build the data fresh; you copy when you did not build it
  and cannot trust who else holds it.
- `import copy` binds the name `copy` to a module object; `copy.deepcopy` is
  an ordinary attribute lookup (1.10).
- Constructors are not type conversions: `dict(config)` **builds a new dict**
  by walking the pairs and storing the same value objects — which is *why* it
  comes out shallow. Same for `list()`, `set()`, `tuple()`.

More shallow-copy shapes (`[[0] * 3] * 3`, tuples holding lists) are in 1.8.

---

## 8. `+=` depends on mutability

Same operator, opposite behaviour, decided by the object's type:

```python
x = [1, 2, 3]
y = x
x += [4]                # MUTABLE: mutates in place, like .extend()
print(x, y, x is y)     # [1, 2, 3, 4] [1, 2, 3, 4] True

a = 5
b = a
a += 1                  # IMMUTABLE: must rebind to a new object
print(a, b, a is b)     # 6 5 False
```

`x = x + [4]` always rebinds (it builds a new list). Full treatment in 1.5 §9.

---

## 9. The disguised mutator

A function that takes input and returns output can still be impure if it
mutates what it was handed and returns the same object:

```python
def add_item(basket, item):
    basket.append(item)     # mutates the caller's list
    return basket           # hands back the SAME object

def add_item_pure(basket, item):
    return basket + [item]  # new list; original untouched

b = [1]
r = add_item(b, 2)
print(r is b)               # True  — you got your own object back
```

The `is` check exposes it. Pure functions are in 1.7 §15.

---

## Quick reference

| Item | What it does | The trap |
|---|---|---|
| mutable types | `list`, `dict`, `set` — change in place | same `id()` after mutation; every alias sees it |
| immutable types | `int`, `float`, `bool`, `str`, `tuple` — cannot change | "changing" one builds a new object and rebinds the name |
| aliasing | `b = a` binds a second name to the SAME object | never a copy; only *matters* for mutables |
| passing an argument | is an assignment: local name → same object | the function can mutate the caller's object |
| `lst.append(v)` in a function | mutates the shared object | caller **sees** it |
| `lst = [v]` in a function | rebinds the local name only | caller sees **nothing** |
| in-place mutators | `append`, `extend`, `insert`, `remove`, `sort`, `reverse`, `clear` return `None` | `l = l.sort()` destroys the list |
| the tell | returns `None` ⇒ mutated | **one-directional**: `pop` mutates and returns a value |
| the discriminator | TYPE first, then the return value | immutable type ⇒ mutation impossible |
| mutate vs build | mutate → `None`, don't assign; build → new object, assign | not method-vs-function |
| default argument | evaluated **once**, at `def` time, stored in `__defaults__` | a mutable default accumulates across calls |
| the fix | `x=None` + `if x is None: x = []`, work outside the `if` | `[].append(v)` binds `None` |
| shallow copy | new outer container, same inner references | invisible on flat immutables; bites on nested mutables |
| `copy.deepcopy` | new objects all the way down | slower; copies things you may want shared |
| constructors | `list()`, `dict()`, `set()`, `tuple()` build a new container | copies the references, not the items — hence shallow |
| `+=` | in place on mutables; rebinds on immutables | `x = x + y` always builds new |
