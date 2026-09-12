# Unit 1.8 — Data Structures

Lists, tuples, dicts, sets; when to use which; comprehensions; `zip`;
nested structures and copying; f-strings and the format spec.

---

## 1. Lists

An ordered, mutable, growable sequence of references to objects.

### 1.1 Indexing

`[]` after a list is the **index operator**: it takes a **position** and hands
back **the object at that position**.

```python
tools = ['drill', 'saw', 'clamp', 'vice']
print(tools[0])     # drill        positions start at 0
print(tools[3])     # vice         the last valid index is len - 1
print(tools[-1])    # vice         negative indices count back from the end
print(len(tools))   # 4            the LENGTH is 4; the last INDEX is 3
print(tools[4])     # IndexError: list index out of range
```

Length counts items; indices label positions. Say "the last index is
`len - 1`, so 4 is one past the end."

**Subscriptable** = can take `[...]`. `list`, `tuple`, `str`, `dict` are;
`set` and `int` are not (`5[0]` → `TypeError: 'int' object is not
subscriptable` — a statement about the **type**, so `TypeError`, not
`IndexError`).

### 1.2 Slicing

`[start:stop:step]` is a **slice**. It is **half-open** — starts *at* `start`,
stops *before* `stop` — the same rule as `range()`. Omitted `start` means
"from the beginning", omitted `stop` "to the end"; `step` defaults to 1 and a
negative step walks backward.

```python
tools = ['drill', 'saw', 'clamp', 'vice']
print(tools[1:3])       # ['saw', 'clamp']
print(tools[1])         # saw          indexing hands back ONE object
print(tools[1:2])       # ['saw']      slicing BUILDS A NEW LIST
print(tools[::2])       # ['drill', 'clamp']
print(tools[::-1])      # ['vice', 'clamp', 'saw', 'drill']   a reversed COPY
print(tools[-3:])       # ['saw', 'clamp', 'vice']
print(tools[10:20])     # []           out of range -> empty, NEVER raises
print(tools[10])        # IndexError
```

Indexing must return one specific object, so it raises when it is not there.
Slicing builds a list, and a list is entitled to be empty. **Slicing never
raises `IndexError`** — convenient, and also how out-of-range bugs go silent.

The same operator works on strings: `"clamp"[:-1]` → `'clam'`,
`"clamp"[::-1]` → `'pmalc'`, `"clamp"[1:3]` → `'la'`.

### 1.3 `l[:]` — copy vs alias

```python
tools = ['drill', 'saw']
b = tools           # assignment -> alias
c = tools[:]        # full slice -> NEW list
b.append('file')
print(tools, c)     # ['drill', 'saw', 'file'] ['drill', 'saw']
print(tools is b, tools is c)   # True False
```

The new list holds **the same item references**, not copies of the items —
a **shallow** copy (§8). Three equivalent shallow forms: `a[:]`, `list(a)`,
`a.copy()`; prefer `.copy()` for intent.

### 1.4 The method roster

Each line on a fresh `tools = ['drill', 'saw', 'clamp']`:

```
append('vice')    -> returned None      ['drill', 'saw', 'clamp', 'vice']
extend(['v','f']) -> returned None      ['drill', 'saw', 'clamp', 'v', 'f']
insert(1, 'vice') -> returned None      ['drill', 'vice', 'saw', 'clamp']
sort()            -> returned None      ['clamp', 'drill', 'saw']
reverse()         -> returned None      ['clamp', 'saw', 'drill']
remove('saw')     -> returned None      ['drill', 'clamp']       (first occurrence, by VALUE)
clear()           -> returned None      []                       (empty, not gone; same object)
pop()             -> returned 'clamp'   ['drill', 'saw']         (removes AND returns the last item)
pop(0)            -> returned 'drill'   ['saw', 'clamp']
count('saw')      -> returned 1         unchanged
index('saw')      -> returned 1         unchanged  (ValueError if absent)
copy()            -> returned a new list unchanged
```

`append` adds ONE item; `extend` adds MANY (from an iterable). All the
mutators return `None` except `pop`, which returns the removed item because
"which item did I just take out?" is useful. The discriminator for any method
you have never met is in 1.4 §5: type first, then the one-directional tell.

### 1.5 `sort` / `sorted` and `reverse` / `reversed` — one distinction, two names

| | kind | mutates? | hands back |
|---|---|---|---|
| `values.sort()` | method on a list | **yes** | `None` |
| `sorted(values)` | built-in, any iterable | no | a **new list** |
| `values.reverse()` | method on a list | **yes** | `None` |
| `reversed(values)` | built-in | no | an **iterator** |

```python
nums = [3, 1, 2]
print(nums.sort(), nums)        # None [1, 2, 3]
more = [3, 1, 2]
print(sorted(more), more)       # [1, 2, 3] [3, 1, 2]

path = ["home", "pick", "lift", "place"]
print(reversed(path))           # <list_reverseiterator object at 0x...>
print(list(reversed(path)))     # ['place', 'lift', 'pick', 'home']
print(path)                     # ['home', 'pick', 'lift', 'place']   untouched
```

- `sorted()` takes any iterable — set, tuple, dict — and always returns a
  **list**. `.sort()` exists only on lists. Both accept `key=` and
  `reverse=True` (1.7 §11).
- `reversed()` walks a sequence back to front with **no copy** (`path[::-1]`
  builds a whole second list). It hands back an iterator, so `print` shows an
  object; wrap in `list()` to see values; it exhausts after one pass.
- **`reversed()` does not ORDER, it REVERSES** the order that is already
  there. `reversed(["c", "a", "b"])` → `b, a, c`.
- `l = l.sort()` and `l = l.reverse()` destroy the list (bind `None`).
- `list(reversed(sorted(records, key=lambda x: x["frames"])))` — or, cheaper,
  `sorted(records, key=..., reverse=True)`.

### 1.6 `*` repetition and the shared-row trap

```python
print([0] * 5)              # [0, 0, 0, 0, 0]
grid = [[0] * 3] * 3
grid[0][0] = 99
print(grid)                 # [[99, 0, 0], [99, 0, 0], [99, 0, 0]]
print(grid[0] is grid[1])   # True — three slots, ONE inner list

good = [[0] * 3 for _ in range(3)]
good[0][0] = 99
print(good)                 # [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

`*` repeats the **reference**, not the contents. Safe when the element is
immutable (a shared `0` cannot be mutated), a trap when it is mutable. The
comprehension fixes it because the expression re-runs once per pass.

### 1.7 Never mutate a container while iterating over it

```python
angles = [10, 200, 250, 30]
for a in angles:
    if a > 180:
        angles.remove(a)
print(angles)               # [10, 250, 30]   <- 250 SURVIVED
```

| counter | list at that moment | `a` | action |
|---|---|---|---|
| 0 | `[10, 200, 250, 30]` | 10 | keep |
| 1 | `[10, 200, 250, 30]` | 200 | remove → `[10, 250, 30]` |
| 2 | `[10, 250, 30]` | 30 | keep |
| 3 | length is 3 → loop stops | | |

`for` keeps an internal position counter and does not know the list is
changing. When `200` left, `250` slid into index 1 — a slot already passed.
**And it hides:** on `[10, 200, 30, 250, 50]` the same code returns
`[10, 30, 50]`, the right answer, having skipped two elements that happened
to be keepers. The bug is always present; the data hides it.

**Don't remove, SELECT:** `angles = [a for a in angles if a <= 180]` — build
a new list and rebind the name. Nothing mutates while it is being read. (A
dict iterator goes further and refuses: resizing a dict during iteration
raises `RuntimeError: dictionary changed size during iteration`.)

### 1.8 Nested indexing

```python
rows = [[1, 2, 3], [4, 5], [6]]
print(rows[1][0])           # 4
print(len(rows))            # 3 — counts the OUTER items only
print(len(rows[1]))         # 2
```

Chained subscripting reads **left to right**: the first `[]` hands back
something indexable; the second `[]` is the same operator applied to it. No
new syntax. `len()` on a nested structure counts the outer container only.

---

## 2. Tuples

An ordered, indexable, iterable sequence that is **immutable**: once built, no
element can be replaced, added, or removed.

```python
joint_limits = (-170.0, 170.0)
print(type(joint_limits), joint_limits[0], len(joint_limits))
# <class 'tuple'> -170.0 2
```

### 2.1 The comma makes the tuple, not the parentheses

```python
a = (5)
b = (5,)
c = 1, 2, 3
d = ()
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'tuple'> <class 'tuple'> <class 'tuple'>
```

`(5)` is the grouping parenthesis from arithmetic; wrapping one value gives
the value back. The lonely trailing comma in `(5,)` does all the work.
Parentheses are required only where a bare comma would be ambiguous —
`f((1, 2))` passes one tuple, `f(1, 2)` passes two arguments.

### 2.2 Immutability arrives as `TypeError`; a missing method as `AttributeError`

```python
joint_limits[0] = -90.0
# TypeError: 'tuple' object does not support item assignment
joint_limits.append(180.0)
# AttributeError: 'tuple' object has no attribute 'append'
```

| Line | Error | Why |
|---|---|---|
| `t[0] = x` | `TypeError` | the operation exists; this **type** refuses it |
| `t.append(x)` | `AttributeError` | the name after the **dot** is not there at all |

**Immutability has no error of its own. It shows up as `TypeError`.**

### 2.3 Non-mutating operations build new tuples

```python
new_limits = joint_limits + (200.0,)
print(joint_limits, new_limits)     # (-170.0, 170.0) (-170.0, 170.0, 200.0)
```

### 2.4 The roster is derivable

A list's `append`, `extend`, `insert`, `sort`, `remove`, `pop` all mutate;
none can exist on a tuple. **An immutable type can only carry methods that
REPORT.** There are exactly two:

```python
t = (3, 1, 2, 1)
print(t.count(1))   # 2  — how many times
print(t.index(2))   # 2  — position of the first; ValueError if absent
```

(Why no new-object `append`? Because that already exists and is spelled `+`.)

### 2.5 Unpacking and multiple return

```python
low, high = (-170.0, 170.0)         # left to right, one statement
x, y, z = 1, 2, 3

def limits():
    return -170.0, 170.0            # builds ONE tuple

low, high = limits()

low, high = (1, 2, 3)
# ValueError: too many values to unpack (expected 2)
```

Count mismatch is **`ValueError`**, not `TypeError`: a tuple *is* unpackable
(type fine); the **number of values** is wrong, and item count is a property
of the value. `for name, angle in pairs:` is unpacking on the `for` line.

### 2.6 Immutability is SHALLOW

```python
config = ("arm", [10.0, 20.0])
config[1].append(30.0)          # legal
print(config)                   # ('arm', [10.0, 20.0, 30.0])
config[1] = [99.0]              # TypeError: 'tuple' object does not support item assignment
```

**A tuple stores REFERENCES. Immutable means the references cannot be
re-pointed. It says nothing about the objects they point at.** You cannot
make slot 1 point at a different list; you can do anything to the list it
already points at.

### 2.7 When to choose a tuple — what it buys

```python
def clamp(angle, limits):
    if angle > limits[1]:
        limits[1] = angle        # a "temporary fix"
    return angle

joint_limits = [-170.0, 170.0]
clamp(200.0, joint_limits)
print(joint_limits)             # [-170.0, 200.0]  — the safety limit silently moved
```

With a tuple that line raises `TypeError` at the exact offending line. Four
gains:

1. **You can stop reading** — the value never changed, without auditing every
   function it was passed to.
2. **The failure moved** from a silent wrong value at runtime to a loud error
   at the cause.
3. **It states intent**: tuple = fixed record; list = growing collection.
4. **A tuple is HASHABLE**, so it can be a dict key or a set item; a list
   cannot (§3.3). This is the stronger reason.

Streaming joint angles → list (changes every tick). Joint limits read once →
tuple (fixed).

---

## 3. Dicts

### 3.1 The problem: parallel lists

```python
joint_names  = ["shoulder", "elbow", "wrist"]
joint_angles = [10.0, 20.0, 30.0]
i = joint_names.index("elbow")
print(joint_angles[i])          # 20.0
```

Two defects: the pairing is not enforced (append to one list and they drift);
and `.index()` walks the list one item at a time — **linear** cost. A missing
name raises `ValueError: 'gripper' is not in list` (`index` exists and ran;
the value is not there).

### 3.2 What a dict is

```python
joints = {"shoulder": 10.0, "elbow": 20.0}
print(joints["elbow"], len(joints), type(joints))    # 20.0 2 <class 'dict'>

joints["wrist"] = 30.0      # new key    -> INSERTS
joints["elbow"] = 25.0      # exists     -> OVERWRITES
print(joints)               # {'shoulder': 10.0, 'elbow': 25.0, 'wrist': 30.0}

print(joints["gripper"])    # KeyError: 'gripper'
```

- **Key → value** pairs; `[]` takes a **key** instead of a position. The
  pairing lives inside one object and cannot drift. Lookup does not scan —
  roughly the same cost at 3 entries or 10 million.
- **Keys are unique**, and it is derivable: `[]` must return one value.
  Assigning to an existing key overwrites; never duplicates.
- `KeyError` — the **key** is what broke.

### 3.3 Why keys must be hashable

A dict finds a value without scanning by computing a number from the key — the
**hash** — and jumping straight to a slot. The key's contents must never change
after it is stored, or the number computed later would not match the slot it
was filed under and the value would be unreachable. **Immutable ⇒ contents
cannot change ⇒ hash is stable ⇒ safe as a key.** Python enforces it up front:

```python
limits = {["shoulder", "min"]: -170.0}
# TypeError: unhashable type: 'list'
d = {("shoulder", "min"): -170.0}   # a tuple works
```

- The error says **unhashable**, not "immutable", and it is a `TypeError`
  because it is a fact about the type, whatever the list contains.
- A hash is a fixed-size number computed from a value. It is **not unique**
  (two different values can share one — a collision); what matters is that
  **equal values hash equal** (`hash(1) == hash(1.0)` is `True`) and the value
  does not change while stored.
- **Immutability does not mean uniqueness**: `d[(1, 2)] = "a"` then
  `d[(1, 2)] = "b"` — two equal tuples are the **same key**.
- How the number is computed, collisions and table resizing are DSA
  material, not this unit.

### 3.4 Avoiding `KeyError`: `in` and `.get()`

```python
print("elbow" in joints, "gripper" in joints)   # True False — `in` tests KEYS
print(joints.get("elbow"))                      # 20.0
print(joints.get("gripper"))                    # None
print(joints.get("gripper", 0.0))               # 0.0
```

`.get(key)` never raises; `.get(key, default)` returns your fallback. The
design trap:

```python
angle = joints.get("gripper")
angle * 2
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

`.get()` did not prevent the crash; it **moved** it — to an innocent line,
away from the missing key. **The rule: `[]` when a missing key is a BUG (you
want the crash at the cause, by name); `.get()` when absence is EXPECTED and
you have a real default. `.get()` with no default is the dangerous middle —
it manufactures a `None` that travels.**

### 3.5 Iterating a dict

```python
for j in joints:                    # bare loop -> KEYS
    print(j)

for name, angle in joints.items():  # (key, value) tuples, unpacked
    print(name, angle)

print(joints.keys())    # dict_keys(['shoulder', 'elbow', 'wrist'])
print(joints.values())  # dict_values([10.0, 25.0, 30.0])
print(joints.items())   # dict_items([('shoulder', 10.0), ('elbow', 25.0), ('wrist', 30.0)])
```

`.items()` is tuple unpacking in disguise. `for k in d: d[k]` does the lookup
twice; `.items()` is the idiom.

### 3.6 `.keys()` is a live VIEW; `list()` is a snapshot

```python
d = {"a": 1, "b": 2}
k = d.keys()
l = list(d.keys())
d["c"] = 3
print(k)        # dict_keys(['a', 'b', 'c'])   <- LIVE window onto the dict
print(l)        # ['a', 'b']                   <- FROZEN copy taken at that moment
print(type(k))  # <class 'dict_keys'>
```

`.keys()` builds nothing — a window onto the dict's own keys; `set(a)` copies
every key. **Views support set operations directly**, because dict keys are
unique and hashable:

```python
a = {"shoulder": 90, "elbow": 45}
b = {"elbow": 60, "base": 180}
print(a.keys() & b.keys())      # {'elbow'}
print(a.keys() - b.keys())      # {'shoulder'}
```

The general pattern: *does this object hold the data, or look at the data?*
Views, `zip`, `reversed`, `enumerate` look; `list()` takes the photograph.

### 3.7 Deletion — three ways, and the difference is what you get back

```python
limits = {"shoulder": 90, "elbow": 120, "wrist": 45}
del limits["wrist"]             # statement — hands back NOTHING
value = limits.pop("elbow")     # hands back the VALUE, always
result = limits.clear()         # returns None, leaves {} — empty, not gone, same object
print(value, result, limits)    # 120 None {}
```

- `x = del d[k]` is a `SyntaxError`; `del` is a statement (1.2 §8).
- `d.pop(k)` raises `KeyError` if absent; `d.pop(k, default)` shrugs. The
  default does not create the return value — it replaces the crash.
- `d.update(other)` merges `other` in, overwriting clashes, returns `None`.
- `del d[k]` on a missing key raises `KeyError`.

### 3.8 Insertion ordering

```python
d = {}
d["shoulder"] = 90
d["elbow"] = 120
d["shoulder"] = 999         # overwrite — does NOT move the key
print(list(d))              # ['shoulder', 'elbow']
del d["shoulder"]; d["shoulder"] = 1
print(list(d))              # ['elbow', 'shoulder']   — delete then re-add moves it to the back
```

A dict keeps keys in the order they were **first inserted** (guaranteed since
3.7). **Ordered is not sorted.**

### 3.9 Copying a dict

Dicts are not sliceable; `dict(d)` and `d.copy()` are the shallow forms
(§8).

---

## 4. Sets

**A dict with the values thrown away.** Same braces, same hashing machinery,
same uniqueness rule — so set items must be hashable for exactly the reason
dict keys must be.

```python
seen = {"elbow", "wrist", "elbow", "shoulder", "wrist"}
print(seen, len(seen))          # {'elbow', 'wrist', 'shoulder'} 3  — duplicates absorbed SILENTLY
print(type({}), type(set()))    # <class 'dict'> <class 'set'>
```

- **`{}` is an empty DICT. The only way to write an empty set is `set()`.**
- `seen.add("x")` returns `None` (mutating); adding a present item is a silent
  no-op.
- `seen.remove("gripper")` on an absent item raises **`KeyError`** (a set item
  is its own key); `seen.discard("gripper")` shrugs.

### 4.1 A set is UNORDERED — no positions at all

```python
seen[0]
# TypeError: 'set' object is not subscriptable
```

Not `IndexError`: there is no "first element" to return, so the operation is
not defined for the type. The same file printed three different orders in
three runs (string hashing is randomised per process). **Python does not offer
operations it cannot make mean anything.** Consequences:

- `sorted(s)` returns a **list** — there is no such thing as a sorted set.
- `set()` **destroys any order that reached it**: `list(set(sorted(x)))` is
  arbitrary again. Ordering must be the **last** step: `sorted(set(names))`.
- `a == b` is `True` for different insertion orders — a set compares purely
  by **contents**.

### 4.2 Set operations — the reason sets exist

```python
supported = {"shoulder", "elbow", "wrist"}
commanded = {"elbow", "wrist", "gripper"}
print(supported | commanded)    # union         — in either
print(supported & commanded)    # intersection  — in both
print(commanded - supported)    # difference    — {'gripper'}: asked for but cannot drive
```

- All three build a **new** set — originals untouched — so they are
  **expressions** and go straight inside `print()`.
- **`-` is not symmetric.**
- `&` is not "for sets only": it works on any type that defines it (dict key
  views do).
- An empty set is **falsy**: `if bad:` reads as "if there were any".

```python
command = {"elbow": 30, "gripper": 10}
bad = command.keys() - supported
if bad:
    print("unsupported joints:", bad)     # unsupported joints: {'gripper'}
```

---

## 5. When to use which — the deciding question

The four containers hold the same objects and differ in what they make
**cheap**. The question is not *what am I storing* but:

> **"WHAT AM I GOING TO ASK THIS CONTAINER?"**

| The question you will ask it | Container |
|---|---|
| *"give me the one at position N" / "in order"* | **list** |
| same, but fixed size, position has meaning, must not change | **tuple** |
| *"give me the value for this key"* | **dict** |
| *"is this in you?" / "what's in both?"* | **set** |

- **Pairing is not the reason for a dict — LOOKUP is.** `[("shoulder", 30),
  ("elbow", 45)]` stores pairs fine but must be walked to answer "what's the
  elbow at?"; a dict hashes and jumps.
- **Order is not the list/tuple discriminator — both are ordered. GROWTH
  is.** A list can grow; a tuple cannot.
- The tell for a set: storing keys with nothing on the other side.

Applied — log every joint angle across a 30-second motion:

```python
log = []
log.append((0.00, 30.0, 45.0, 10.0))     # (t, j1, j2, j3)
log.append((0.02, 30.4, 45.1, 10.0))
```

Inner = **tuple** (fixed-size record, position means a joint). Outer = **list**
(must grow, replayed in order). The timestamp is a field, not a key — you never
hold the exact float to look up. A dict would win for replay by discrete frame
number, `frames[1500]`, real random access.

---

## 6. The raise-vs-shrug design rule

One rule, three appearances:

| raises when absent | shrugs when absent |
|---|---|
| `d[k]` | `d.get(k, default)` |
| `del d[k]` / `d.pop(k)` | `d.pop(k, default)` |
| `s.remove(x)` | `s.discard(x)` |

> Is a missing key a **legitimate state of the world**, or does it mean my
> program's assumptions are **already broken**? Legitimate → shrug.
> Assumptions broken → raise, deliberately, as early as possible.

Misspell a joint name in a config: the shrug hands back a default range for a
joint that does not exist, the clamp clamps nothing, and you find out on the
hardware. The raise stops you at the config-load line with the bad name in the
traceback. **Absence you did not plan for is a bug wearing a disguise;
shrugging puts the disguise on.** The spec decides, not temperament.

---

## 7. Comprehensions, `zip`, `enumerate`

### 7.1 List comprehensions

An **expression** that builds a **new list** by running the iteration protocol
over an iterable. New spelling for machinery you own, not new machinery.

```python
joints = [0.5, 1.2, -0.3, 2.0]

doubled_loop = []
for j in joints:
    doubled_loop.append(j * 2)

doubled_comp = [j * 2 for j in joints]
print(doubled_comp)                 # [1.0, 2.4, -0.6, 4.0]
```

**Why it exists:** a `for` loop is a **statement**; a comprehension is an
**expression** — it can go inside a function call, a `return`, an argument,
an f-string, another comprehension:

```python
readings = [0.5, -1.2, 2.4]
print(sum([abs(r) for r in readings]))      # 4.1  — no for loop can sit there
```

Also: LeRobot, openpi and every PyTorch stack are written in this idiom; it
is a reading skill.

**The filter** is a **gate**: an item that fails is never handed to the
expression.

```python
readings = [0.5, -1.2, 0.0, 2.4]
print([r * 2 for r in readings if r > 0])   # [1.0, 4.8]   (0.0 is excluded: > is strict)
```

**The anatomy — written order ≠ execution order:**

```
[  EXPRESSION   for  VAR  in  ITERABLE   if  CONDITION  ]
      (4)            (2)         (1)            (3)
```

Executed 1 → 2 → 3 → 4: `iter()` on the iterable once; `next()` binds the
variable each pass; the condition is tested; only then the expression runs
and its result is appended. **The piece you write first runs last.** Proof:

```python
speeds = [10, 0, 5]
[100 / v for v in speeds]               # ZeroDivisionError: division by zero
[100 / v for v in speeds if v != 0]     # [10.0, 20.0]  — the gate runs BEFORE the expression
```

**The comprehension's variable does not exist afterwards** — it gets its own
namespace, discarded at the end (on 3.12, PEP 709 inlines the comprehension
but keeps this isolation):

```python
doubled = [x * 2 for x in [1, 2, 3]]
print(x)        # NameError: name 'x' is not defined
```

**When NOT to use one:** a comprehension BUILDS A CONTAINER. If you are not
building one, use a loop. `[print(j) for j in joints]` prints, and also
builds and discards `[None, None, None]`. More than one line of logic, or
cannot read it in one breath → write the loop. `[i for i in x]` is just
`list(x)`.

A ternary can sit in the expression slot:
`["pos" if n > 0 else "neg" for n in nums]`.

### 7.2 Dict comprehensions

Same machinery; **the braces and the colon** make it a dict.

```python
joints = ["base", "shoulder", "elbow"]
home = {name: 0.0 for name in joints}
print(home)             # {'base': 0.0, 'shoulder': 0.0, 'elbow': 0.0}

angles = {"base": 90, "shoulder": 200, "elbow": 180, "wrist": 190}
over = {name: a for name, a in angles.items() if a > 180}
print(over)             # {'shoulder': 200, 'wrist': 190}   (elbow at exactly 180 is out)

scaled = {k: v * 2 for k, v in angles.items()}
names_over = [k for k, v in angles.items() if v > 180]
```

Walking an existing dict: `.items()` yields `(key, value)` tuples; two names
unpack them; the gate can test the value. Two parallel lists into one dict:
`{name: angle for name, angle in zip(names, angles)}`.

### 7.3 `zip`

Pairs two or more iterables positionally — first with first, second with
second. **Each pass yields a TUPLE**, which is why `for a, b in zip(...)`
unpacks. It removes the index bookkeeping of `for i in range(len(names))`.

```python
names  = ["base", "shoulder", "elbow"]
angles = [90, 45, 180]
for name, angle in zip(names, angles):
    print(name, angle)
print(list(zip(names, angles)))     # [('base', 90), ('shoulder', 45), ('elbow', 180)]
```

`zip` pairs **iterables**, not "lists": a tuple and a dict work too, and a
dict iterated bare yields its keys in insertion order.

**`zip` fails silently — twice:**

```python
names  = ["base", "shoulder", "elbow", "wrist"]
angles = [90, 45, 180]
print(list(zip(names, angles)))     # 3 pairs — "wrist" is GONE, no error
# zip stops when the SHORTEST runs out

z = zip(names, angles)
print(list(z))                      # 3 pairs
print(list(z))                      # []  — an iterator, exhausted; list() caught StopIteration
```

If you are wrong about your data, `zip` hands you a plausible result and lets
you carry on — a sensor returning 6 readings for 7 joints. Check lengths
yourself.

### 7.4 `enumerate`

`(count, element)` tuples counting from 0; replaces `range(len(x))` when you
need the index and the item (1.6 §13).

---

## 8. Nested data structures and copying

**Nesting is not a feature, it is a consequence:** containers hold objects,
and lists and dicts *are* objects. Flat containers lose the shape of the data
and force you to keep relationships in your head; nesting puts the shape in
the structure.

```python
limits = {"shoulder": [-90, 90], "elbow": [0, 145]}
print(limits["elbow"][1])       # 145 — the first [] hands back a list; the second indexes it
```

Two levels is normal; four usually means you wanted a class.

### 8.1 Shallow copy — the trap the unit exists for

```python
a = [[1, 2], [3, 4]]
b = a[:]                    # a NEW outer list
b[0][0] = 99
print(a)                    # [[99, 2], [3, 4]]
print(a is b)               # False — new outer
print(a[0] is b[0])         # True  — the inner list was never copied
```

```python
config = {"limits": [-90, 90]}
backup = dict(config)
backup["limits"][0] = 0
print(config)                                   # {'limits': [0, 90]}
print(config["limits"] is backup["limits"])     # True
```

**Shallow = one level deep.** New box, same contents. `a[:]`, `list(a)`,
`a.copy()`, `dict(d)`, `d.copy()`, `copy.copy(x)` are all shallow. Invisible
for a flat container of immutables (sharing a `90` cannot bite); visible the
moment the items are mutable.

`dict(config)` is a **constructor call**, not a type conversion: it walks the
pairs and stores the same value objects — which is *why* it comes out
shallow. Same for `list()`, `set()`, `tuple()`.

### 8.2 `copy.deepcopy` — the copy with no floor

```python
import copy

defaults = {"elbow": [0, 150], "wrist": [-90, 90]}
shallow = dict(defaults)
deep = copy.deepcopy(defaults)

shallow["elbow"][1] = 90
deep["wrist"][0] = -45
print(defaults)     # {'elbow': [0, 90], 'wrist': [-90, 90]}  — the shallow edit leaked; the deep one did not
print(defaults["elbow"] is shallow["elbow"], defaults["wrist"] is deep["wrist"])   # True False
```

New outer container **and** new contents, recursively. A **snapshot** you can
hand away or mutate freely. Not "the better copy": slower, copies things you
may have wanted shared, buys nothing on flat immutables; most of the time
build the data fresh instead. Full discussion in 1.4 §7.

---

## 9. f-strings and the format spec

The `f` prefix turns a string literal into an instruction. Without it,
`{angle}` is seven literal characters.

```python
angle = 90.5
print(f"the angle is {angle}")      # the angle is 90.5
print("the angle is {angle}")       # the angle is {angle}
```

**The three steps** for each `{ }`:

1. **Evaluate** what is inside as an **expression**;
2. call **`str()`** on the result;
3. **splice** the text into the string.

Step 2 is why `f"{[1, 2, 3]}"` is a `str` and why `"the angle is " + angle`
raises `TypeError: can only concatenate str (not "float") to str`.

**What sits in the braces is an EXPRESSION, not a name:**

```python
names = ["base", "shoulder", "elbow"]
home  = {"base": 90, "shoulder": 45}
print(f"there are {len(names)} joints")          # there are 3 joints
print(f"base sits at {home['base']} degrees")    # base sits at 90 degrees
print(f"twice that is {home['base'] * 2}")       # twice that is 180
print(f"over 100? {home['base'] > 100}")         # over 100? False
print(f"doubled: {[a * 2 for a in [90, 45]]}")   # doubled: [180, 90]
```

A comprehension fits; a `for` loop never will (expression vs statement).
Inside a `"`-quoted f-string use `'` for inner strings; on Python 3.12+ (PEP
701) the same quote may be nested, which is a `SyntaxError` on 3.11.

### 9.1 The format spec — everything after the colon

```python
reading, count = 3.14159, 7
print(f"{reading:.2f}")     # 3.14      precision: 2 digits after the point
print(f"{reading:8.2f}")    #     3.14  width 8 TOTAL, 2 decimals
print(f"{count:03d}")       # 007       zero-padded, width 3
print(f"{'elbow':10s}|")    # elbow     |   width 10 total, text
```

- **The number before the dot is the TOTAL field width**, not extra spaces.
  `10s` = ten characters wide in total.
- A value wider than its field is **not truncated** — the field loses:
  `f"{'shoulder_yaw':10s}|"` → `shoulder_yaw|`.
- `.1f` etc. is precision.

### 9.2 Alignment defaults

**Text hugs the LEFT of its field. Numbers hug the RIGHT.**

```python
rows = [("elbow", 145.0), ("shoulder", 90.0), ("wrist", 7.25)]
for name, angle in rows:
    print(f"[{name:10s}] [{angle:8.1f}]")
```
```
[elbow     ] [   145.0]
[shoulder  ] [    90.0]
[wrist     ] [     7.2]
```

Names start at the same left edge; numbers end at the same right edge, so
decimal points stack and magnitudes compare without reading digits. The
default matches what you scan a column *for*. Override with `<` (left), `>`
(right), `^` (centre): `f"{name:<10}{angle:>8.1f}"`.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| `l[i]` | returns the object at position `i`; 0-based; negatives from the end | last index is `len - 1`; `IndexError` past it |
| `l[a:b:c]` | builds a **new** list, half-open like `range` | never raises; out of range → `[]` |
| `l[:]` / `list(l)` / `l.copy()` | shallow copy | references copied, not items |
| `append` / `extend` / `insert` / `remove` / `sort` / `reverse` / `clear` | mutate in place | return `None` |
| `pop()` | removes **and returns** an item | the counterexample to "mutating ⇒ `None`" |
| `count` / `index` | read only | `index` raises `ValueError` if absent |
| `sorted(x)` / `x.sort()` | new list / in place | `.sort()` returns `None` |
| `reversed(x)` / `x.reverse()` | iterator / in place | `reversed` does not sort; wrap in `list()` |
| `seq * n` | repeats the reference | `[[0]*3]*3` shares one row |
| mutate-while-iterating | `for` keeps a position counter | silently skips; select into a new list instead |
| tuple | immutable ordered sequence | the **comma** makes it; `(5)` is an `int` |
| `t[0] = x` / `t.append` | `TypeError` / `AttributeError` | immutability arrives as `TypeError` |
| tuple methods | `count`, `index` only | an immutable type can only report |
| unpacking | `a, b = t` | count mismatch is `ValueError` |
| `return a, b` | one tuple | never more than one object |
| shallow immutability | references fixed, objects inside not | a list inside a tuple can still be mutated |
| hashable | stable hash ⇒ immutable | tuple can be a key; list cannot (`TypeError: unhashable`) |
| dict | key → value; `[]` takes a key | keys unique; existing key overwrites |
| `KeyError` | the key is not there | brackets do not decide the error; what's inside does |
| `in` on a dict | tests **keys** | not values |
| `.get(k, default)` | shrugging lookup | with no default it manufactures a travelling `None` |
| `for k in d` | keys | `.items()` for pairs; `.values()` for values |
| `.keys()` / `.values()` / `.items()` | live **views** | `list(...)` is the snapshot; views support `& \| -` |
| `del d[k]` / `d.pop(k)` / `d.clear()` | nothing / the value / `None` | `del` is a statement; `clear` leaves `{}`, same object |
| dict order | first-insertion order | ordered ≠ sorted; overwrite does not move a key |
| set | unique, unordered, hashable items | `{}` is a dict; `set()` for empty |
| `s[0]` | `TypeError: not subscriptable` | no positions at all; `sorted(s)` is a list |
| `add` / `remove` / `discard` | `None` / `KeyError` if absent / shrugs | a set item is its own key |
| `\|` `&` `-` | union / intersection / difference, new sets | `-` is not symmetric |
| when to use which | "what will I ASK this container?" | growth, not order, separates list from tuple |
| raise vs shrug | `d[k]`/`.get`, `del`/`.pop(k, d)`, `remove`/`discard` | the spec decides, not temperament |
| list comprehension | expression that builds a list | executed iterable → var → gate → expression |
| the filter | gate before the expression | it protects the expression only because it runs first |
| comprehension scope | own namespace | the variable does not exist afterwards |
| dict comprehension | `{K: V for ...}` | braces **and** colon |
| `zip` | pairs iterables, yields tuples, lazy | truncates to the shortest, silently; exhausts |
| `enumerate` | `(i, item)` tuples | unpack on the `for` line |
| nested structures | a consequence of containers holding objects | `len()` counts the outer only |
| `copy.deepcopy` | new all the way down | not the default choice |
| f-string | evaluate → `str()` → splice | no `f` ⇒ literal braces; braces hold an expression |
| format spec | `{v:8.2f}`, `{n:03d}`, `{s:10s}` | the number is **total** width; never truncates |
| alignment | text left, numbers right | `<` `>` `^` override |
