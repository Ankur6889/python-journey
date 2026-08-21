# SESSION 1 NOTES — How Python Thinks: The Memory Model

**Topics: everything is an object · names vs boxes · the namespace dictionary ·
`id()` · multiple names on one object · rebinding vs mutation · reference
counting and garbage collection · `locals()`**

---

## SELF-TEST — answer these cold before reading on

1. What does `x = 42` actually do, in two steps?
2. Where does the type live — on the name or on the object? Why does that make
   Python "dynamically typed"?
3. `x = 42` then `y = 42`. Do `id(x)` and `id(y)` match? Why?
4. After `x = x + 1`, what happened to the old object?
5. When does an object get destroyed, and who decides?

---

## FULL TEACHING

### 1. The core mental model

The single most important shift from other languages: **variables are not boxes
that hold values. They are names bound to objects.**

What `x = 42` actually does:

- Python creates an integer object in memory with value `42`.
- Python adds the entry `'x' → address of that object` to the namespace
  dictionary.
- Every later use of `x` is a lookup: find the name, get the address, go to the
  object.

**Key rule: the type belongs to the OBJECT, not the name.** `x` carries no type
information; only the object does. That is what "dynamically typed" means.

### 2. The namespace

Python maintains a **namespace** — a dictionary mapping names (strings) to the
objects they are bound to. Every name you create is a key in that dictionary, and
you can look at it directly:

```python
x = 42
y = 42
print(locals())
# includes {'x': 42, 'y': 42, ...} plus Python's internals
```

The `__name__`, `__file__`, `__builtins__` entries are Python's own bookkeeping —
explained later, at modules and imports.

### 3. `id()` — inspecting the address

`id()` returns the memory address of the object a name is bound to. It is the
tool for answering "same object, or two objects?"

```python
x = 42
y = 42
print(id(x))     # e.g. 11757000
print(id(y))     # e.g. 11757000  — same object

x = x + 1
print(id(x))     # e.g. 11757032  — new object, x was rebound
print(id(y))     # e.g. 11757000  — y unchanged
```

Why do `x` and `y` share an address at the start? Python reuses an existing
object of that value rather than making a duplicate. Both names point at the one
and only `42`.

### 4. Rebinding vs mutation

`x = x + 1` does **not** modify the object `x` pointed to. It builds a brand new
object for the result and **rebinds** `x` to it. The old object is untouched, and
`y` still points at it.

- **Rebinding** — changing what a name points to.
- **Mutation** — changing the contents of an object in place.

Mutability, in Session 2, is where this gets its full treatment.

### 5. Reference counting and garbage collection

Every object tracks how many names point at it — its **reference count**. When
that count reaches zero, the garbage collector destroys the object and frees the
memory.

```python
x = 42      # object 42: refcount 1
y = x       # object 42: refcount 2
x = 100     # object 42: refcount 1 (y still points at it)
y = 0       # object 42: refcount 0 — garbage collected
```

You never manage memory by hand in Python. The interpreter does it. This is one
of the biggest departures from C/C++.

---

## WORKED EXAMPLE

```python
a = 10
b = a
b = b + 5
print(a)
print(b)
```

Line by line:

- `a = 10` → creates int object `10`, binds `'a'` to it.
- `b = a` → adds `'b'` to the namespace, pointing at the **same** object.
- `b = b + 5` → creates a new int object `15` and rebinds `'b'`; `'a'` untouched.
- Output: `10`, then `15`.
- The object `10` survives because `a` still points at it — not collected.

---

## KEY MENTAL MODELS

- Names are labels tied to objects; they are not containers.
- The type is a property of the object, never of the name.
- The namespace is a real dictionary you can print.
- `id()` is how you settle "same object or copy?" empirically.
- Assignment rebinds. It never edits the object on the right-hand side.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| `id(obj)` | Returns the object's memory address | Equal values may share an address — that is reuse, not a rule to rely on |
| `locals()` | Dumps the current namespace as a dict | Also shows Python's internal entries |
| rebinding | Points a name at a different object | Looks like mutation, isn't — other names are unaffected |
| refcount | Names currently pointing at an object | Hits zero → object destroyed, automatically |

---

## WHAT'S COMING NEXT — SESSION 2

- 1.1 How Python runs code — interpreter, bytecode (`.pyc`), the PVM, the call stack.
- 1.3 Data types — `int`, `float`, `bool`, `str`, `None` in depth.
- 1.4 Mutability vs immutability — why it changes everything.
