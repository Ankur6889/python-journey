# Unit 1.2 — Variables, Name Binding, and the Object Model

Everything is an object; a variable is a name bound to one. The namespace
dictionary, `id()`, aliasing, rebinding vs mutation, reference counting,
`del`, integer caching, interning, and `is` vs `==`.

---

## 1. Everything is an object; the type belongs to the object

Every value in Python — `42`, `"hi"`, a list, a function, a module — is an
object with its own identity. **The type is a property of the object, never of
the name.** A name carries no type information; only the object it points at
does. That is what "dynamically typed" means.

```python
x = 42
print(type(x))      # <class 'int'>
x = "forty-two"
print(type(x))      # <class 'str'>   — same name, different object, different type
```

---

## 2. Variables are names, not boxes

What `x = 42` actually does, in two steps:

1. Python creates an integer object with value `42` in memory.
2. Python adds the entry `'x' → (reference to that object)` to the namespace
   dictionary.

Every later use of `x` is a lookup: find the name, follow the reference, reach
the object.

The phrasing that matters: **"bind the object to a name"**, never "bind the
name with the object". The object is the thing that exists; the name is one of
possibly several labels pointing at it. **Objects come first; names are tags
attached afterwards.**

---

## 3. The namespace is a real dictionary

Python maintains a **namespace**: a dictionary mapping names (strings) to the
objects they are bound to. You can print it.

```python
x = 42
y = 42
print(locals())
# {..., 'x': 42, 'y': 42}     (the front is Python's own bookkeeping)
```

- `locals()` — the current frame's namespace dict. At file level it is padded
  with `__name__`, `__file__`, `__builtins__` and friends (explained in 1.10).
- `globals()` — the module-level namespace dict. `sorted(globals().keys())`
  after two `def`s lists `'inner'` and `'outer'` among the entries: **`def`
  binds a name**, so the module namespace is never empty once a function has
  been defined — that is how a nested call finds the function at all.
- `vars(obj)` — an object's own namespace dict (`__dict__`); `vars()` with no
  argument is the namespace of the file you are standing in (1.10).

A namespace maps **names to references**. It does not hold the objects. Objects
live on the **heap**; several namespaces (several frames) can each hold a name
referencing the same heap object. Frames and their namespaces are ephemeral —
created on call, destroyed on return — while objects survive as long as
something still refers to them.

---

## 4. `id()` — the object's identity

`id(obj)` returns the object's identity (in CPython, its memory address). It
is the primitive for settling **"same object, or two objects?"**

```python
x = 42
y = 42
print(id(x), id(y))     # same number — one object, two names
x = x + 1
print(id(x))            # different — x was rebound to a new object
print(id(y))            # unchanged — y was never rebound
```

Addresses are assigned fresh every run and mean nothing in absolute terms.
Only *sameness or difference within one run* carries information. **When you
make an identity claim, reach for `id()` to verify it.**

`id` is unique among live objects and constant for an object's lifetime; the
number can be reused after the object dies.

---

## 5. Aliasing — multiple names on one object

**Aliasing** is when two or more names refer to the same object. **Assignment
never copies.** `b = a` does not duplicate anything; it binds a second name to
the one object.

```python
a = [1, 2, 3]
b = a
print(a is b)       # True
b.append(4)
print(a)            # [1, 2, 3, 4]  — one object, seen through both names
```

Demonstrating aliasing with an integer proves the definition and teaches
nothing (`x = 5; y = x; x is y` → `True`, and now what?). Aliasing only
*matters* when the shared object can be changed through one name and seen
through the other — which needs a mutable object (1.4).

---

## 6. Rebinding vs mutation

Two operations look similar and are not:

- **Rebinding** — pointing a name at a different object. `id(name)` changes.
  The old object is untouched; any other name still bound to it is
  unaffected.
- **Mutation** — changing the contents of an object in place. `id()` stays
  the same. Every other name bound to that object sees the change.

**The rule that decides which one you are looking at: the LEFT side of the
`=`, not the presence of `=`.**

- a **bare name** on the left (`x = ...`) → **rebinding**;
- a name **plus an accessor** on the left (`x[0] = ...`, `config.speed = ...`)
  → **mutation** of the object the name is bound to.

The right-hand side only tells you what the new or updated value is. It never
tells you whether you rebound or mutated.

```python
x = [1, 2, 3]
y = x
x = x + [4]         # bare name on the left -> REBIND. x + [4] built a NEW list.
print(x, y)         # [1, 2, 3, 4] [1, 2, 3]
print(x is y)       # False
```

```python
x = [1, 2, 3]
y = x
x[0] = 99           # x[0] on the left -> MUTATION. Python runs __setitem__(x, 0, 99).
print(x, y)         # [99, 2, 3] [99, 2, 3]
print(x is y)       # True
```

`nums + [4]` is not "the modified list". Nothing was modified — it builds a
brand-new list and leaves the original untouched.

### 6.1 Objects own namespaces too

A frame owns a namespace. So does an object. `config.speed = 5` does not touch
the name `config`; it writes `speed -> 5` into **that object's own namespace**.

```python
class Config:
    pass

config = Config()
config.speed = 1
before = id(config)
config.speed = 5
print(id(config) == before, config.__dict__)
# True {'speed': 5}       -> mutation: same object, changed contents
```

Contrast with `str`, which has no such door: `s[0] = "X"` raises
`TypeError: 'str' object does not support item assignment`. Two constructs
that look alike on the page, opposite outcomes, and the difference is a
property of the object's **type**, not of the syntax.

### 6.2 The rebinding rule, stated

> Assignment rebinds the name on the left. It does nothing to any other name —
> even one currently bound to the same object. Aliases do not propagate
> updates, because there is no update: only a new binding on one key in the
> namespace dictionary.

```python
x = 42       # namespace: {'x': <obj 42>}
y = x        # namespace: {'x': <obj 42>, 'y': <obj 42>}    same object
x = x + 1    # namespace: {'x': <obj 43>, 'y': <obj 42>}    x rebound, y untouched
```

---

## 7. Reference counting and garbage collection

Every object tracks how many references point at it — its **reference
count**. When the count reaches zero, the object is destroyed and its memory
freed. You never manage memory by hand.

```python
x = 42      # object 42: refcount 1
y = x       # refcount 2
x = 100     # refcount 1 (y still points at it)
y = 0       # refcount 0 -> collected
```

After `x = 42; y = x; x = x + 1`, two integer objects exist (`42` and `43`);
`42` survives because `y` still holds a reference. (Garbage collector
mechanics beyond refcounting are 1.13.)

---

## 8. `del` — a statement that removes a binding

`del` is a **statement**, like `return` or `if`. Not a function, not a method,
no parentheses. **It removes a binding, not an object.**

```python
n = 5
del n
print(n)
```
```
NameError: name 'n' is not defined
```
`del n` did not destroy `5`. It removed the **name** from the namespace —
which is why the failure is a `NameError`: the name is what broke.

On a container it removes an entry:

```python
d = {"a": 1, "b": 2}
del d["a"]
print(d)            # {'b': 2}
del d["zzz"]        # KeyError: 'zzz'
```

Because it is a statement, it evaluates to nothing and cannot sit on the right
of `=` or inside `print(...)`:

```python
x = del d["b"]
```
```
  File "d1.py", line 2
    x = del d["b"]
        ^^^
SyntaxError: invalid syntax
```
Compare `d.pop("b")`, an **expression** that removes the key and hands back
its value (1.8). **`del` hands back nothing — and "nothing" is not `None`.**
`None` is an object that fills a slot; "nothing" is the absence of a slot.

---

## 9. Integer caching: −5 to 256

```python
p = 100
q = 100
print(p is q)       # True  — both bound to the same cached object

p = 1000
q = 1000
print(p is q)       # False — equal value, DIFFERENT objects
print(p == q)       # True
```

CPython pre-creates integer objects for **−5 through 256** at startup and
reuses them, because loop counters, indices and small arithmetic use those
values constantly. Outside that range Python just makes a new object — there
is no global "does an int of this value exist?" lookup. Caching is an
implementation optimisation, not a language rule. **Never write code that
depends on it; `is` on values is a bug waiting for a number above 256.**

---

## 10. String interning (working definition)

CPython sometimes reuses one object for identical string literals rather than
creating two, which is why `a = "hi"; b = "hi"; a is b` can come back `True`
while the list version comes back `False`. The rules are an implementation
detail that shifts between versions. **Never use `is` to compare strings for
equality.** Mechanism not taught further.

---

## 11. Identity vs equality: `is` vs `==`

| Operator | Question it asks | Implementation |
|---|---|---|
| `==` | Do these two objects have equal **values**? | calls `__eq__` |
| `is` | Are these two names bound to the **exact same object**? | compares `id()` |

```python
a = [1, 2]
b = [1, 2]
print(a == b)       # True  — equal contents
print(a is b)       # False — two separate objects
```

```python
p = True
q = 1
print(p == q)       # True   — bool subclasses int; True's numeric value is 1
print(p is q)       # False  — different objects, different types
print(type(p), type(q))     # <class 'bool'> <class 'int'>
```

Two different objects can be `==` without being `is`. Equal values say
nothing about how many objects exist — identity cannot be inferred from
equality. And identity can differ because of **type**, not just contents.

**Use `is` only when you genuinely mean "same object"** — in practice,
`x is None`. Two reasons `is None` beats `== None`:

1. `None` is a **singleton** — one object for the whole program — so identity
   is the exact question.
2. `==` calls `__eq__`, which any class can override and make lie, including
   about `None`. `is` compares identity and cannot be faked.

`is` compares object identity. CPython implements identity as the memory
address, but that is a CPython detail, not a language guarantee.

---

## 12. Binding happens only on a successful return

A name is bound when the right-hand side **produces a value**. If the call
**raises** instead of returning, nothing is produced and nothing is bound.

```python
for i in range(3):
    last = i
print(last)     # 2
print(i)        # 2  — not StopIteration
```
The final `next()` call raised `StopIteration` rather than returning, so no
new binding happened and `i` kept its last successful value. An exception is
a **signal that travels**; it is never bound to a name. This generalises to
every assignment.

---

## 13. Functions and modules are objects too

`def greet(): ...` builds a **function object** and binds the name `greet` to
it — the same names-and-objects rule as everything else (1.7). `import robot`
binds the name `robot` to a **module object** whose namespace is a real dict
(1.10). Every object in Python obeys this one model.

---

## Quick reference

| Name | What it does | The trap |
|---|---|---|
| `x = 42` | builds the object, then binds the name | the name has no type; the object does |
| namespace | dict of names → references | holds no objects; objects are on the heap |
| `locals()` / `globals()` / `vars(o)` | the current / module / object's namespace dict | file-level `locals()` is padded with dunders |
| `id(obj)` | the object's identity | same within a run = same object; absolute value meaningless |
| aliasing | `b = a` — two names, one object | assignment **never** copies |
| rebinding | `x = ...` — bare name on the left | `id` changes; other aliases untouched |
| mutation | `x[0] = ...`, `x.attr = ...` — accessor on the left | `id` unchanged; every alias sees it |
| refcount | references currently pointing at an object | hits zero → object destroyed automatically |
| `del name` / `del d[k]` | statement; removes a **binding** | evaluates to nothing (not `None`); `x = del ...` is a `SyntaxError` |
| int cache −5…256 | CPython reuses these objects | `is` "works" inside the range and fails outside it |
| string interning | identical literals may share an object | never compare strings with `is` |
| `==` | value equality via `__eq__` | can be overridden |
| `is` | identity via `id()` | use for `None` and singletons only |
| `is None` | identity test against the single `None` | `== None` can be made to lie |
| binding on return | a raise binds nothing | `for i in range(3)` leaves `i == 2` |
