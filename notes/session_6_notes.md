# SESSION 6 NOTES — Frames, the Module Frame, and the Call Stack

**Topics: what a frame actually is · frames without functions · `locals()` ·
`<module>` as the file's frame · namespace vs frame · running vs paused frames ·
why a stack and not a queue · `traceback.print_stack()`**

This reopens 1.1: "frame" had been used since Session 4 but never defined. Built
from the ground up here, and 1.1 closes properly.

---

## SELF-TEST — answer these cold before reading on

1. A file contains only `a = 1` and `b = 2`. No functions anywhere. How many
   frames exist while it runs, and what is that frame called?
2. What are the three things a frame holds?
3. What is the difference between a namespace and a frame?
4. Do objects live inside a namespace? Yes or no, and explain.
5. A program has three frames on the stack. Which one is running, and what are
   the others doing?
6. A frame appears in a traceback. Can that frame be finished? Why or why not?
7. Why does Python use a stack for function calls rather than a queue? Answer
   from the structure of the problem.
8. Which comes into existence first when you run a `.py` file: the module frame,
   or the frame of the first function called? Why is the other order impossible?
9. `nums = [1,2,3]` then `backup = nums` then `nums = nums + [4]` — is line 3
   rebinding or mutation, and what rule did you use to decide?

Answers at the bottom.

---

## FULL TEACHING — FRAMES

### 1. Start from what was already locked

From Session 1: a namespace is a dictionary of names. `x = 10` writes an entry
into a dictionary — key `"x"`, value a reference to the object `10`.

The question never asked in Session 1: **where does that dictionary live?** It is
a real object in memory. Something must own it. That owner is the **frame**.

> **Definition.** A frame is the container Python creates in order to execute one
> chunk of code. It holds three things:
> 1. the **namespace** for that chunk (the dictionary of names created there),
> 2. the **line currently executing**,
> 3. the **return address** — where execution resumes when this chunk finishes.
>
> That is the entire definition. No functions are required, and never were.

**The distinction that must not blur:** code is what you wrote and it sits on
disk unchanged. A frame is what Python creates *while running* that code, and it
is destroyed when the run ends. A recipe card is not the same thing as cooking.
One recipe, three cooks, three separate workspaces — the recipe is the code, a
frame is one workspace for one act of cooking.

### 2. A file with no functions at all

```python
x = 10
y = 20
print(x + y)
```

No `def` anywhere. No function is ever called. Yet a frame exists, from the
moment the program starts:

| Point in execution | The frame's namespace holds |
|---|---|
| before line 1 | empty |
| after `x = 10` | `{'x': 10}` |
| after `y = 20` | `{'x': 10, 'y': 20}` |
| line 3 runs | looks up `x` and `y` in that dictionary, adds, prints `30` |
| program ends | frame destroyed, dictionary gone |

**One frame. Zero functions.**

### 3. See the namespace directly with `locals()`

```python
x = 10
print(locals())
y = 20
print(locals())
```

At file level Python pre-loads the namespace with internal entries (`__name__`,
`__builtins__`, `__file__` and others; the exact set varies by version). Ignore
all of it and read the **end** of each printed dictionary. The first ends with
`'x': 10`. The second ends with `'x': 10, 'y': 20`.

That dictionary **is** the frame's namespace. You are looking directly at the
thing.

Now watch a rebinding overwrite an entry rather than create one:

```python
x = 10
print(locals())
x = 99
print(locals())
```

Same key, new value. One dictionary, one frame, edited in place — the Session 1
name-binding model made visible.

### 4. Why the frame is called `<module>`

Python needs a name for this frame when reporting errors. The file you ran is a
**module**, so the frame belonging to the file is labelled `<module>`.

```python
# crash.py
x = 10
y = 0
print(x / y)
```

```
Traceback (most recent call last):
  File "crash.py", line 3, in <module>
    print(x / y)
ZeroDivisionError: division by zero
```

One frame in the entire traceback, named `<module>`, in a file containing no
functions. So `<module>` **cannot** be a function. It is the frame Python creates
for the file itself.

> **Consequence:** every Python program starts executing at module level.
> `main()` or `run()` is never where a program *starts* — it is the first thing
> the module frame chooses to call. The module frame is created before a single
> line runs and sits at the bottom of the stack for the life of the program.

The observation that makes it impossible to forget: put a bare `print("hello")`
at the top of a file, outside every function, and run it. It prints. Nothing
called it. So something was already executing in order to run that line — and
that something is the module frame.

### 5. Only now, add a function

```python
x = 10

def show():
    z = 5
    print(locals())

show()
print(locals())
```

The inner `print(locals())` shows `{'z': 5}` and nothing else — no `x`, no
internal entries. The outer one shows the file's namespace, with `x` in it and no
`z`.

Two different dictionaries, therefore **two frames**.

The function call did not invent the concept of a frame. The module frame was
already there holding `x`. Calling `show()` created a second frame on top of it
with its own separate namespace. When `show()` returned, that second frame was
destroyed and `z` went with it.

> **Why `z` disappears, as a full causal chain:** `z` was never a free-floating
> thing. `z` was an entry in `show`'s namespace. That namespace was owned by
> `show`'s frame. Frame destroyed → namespace destroyed → entry gone. `x`
> survives because it is an entry in a *different* namespace, owned by the module
> frame, which is still alive.
>
> Naming the container that died is the explanation. "The frame was destroyed"
> alone stops one step short of why `z` specifically vanished.

> **The one-sentence version.** Every chunk of code Python executes needs a
> namespace, and a frame is what holds one. A file is a chunk of code, so a file
> gets a frame. A function call is a chunk of code, so a function call gets a
> frame. Files come first, because a function can only be called by something
> already running.

### 6. Namespace versus frame, precisely

| | Namespace | Frame |
|---|---|---|
| What it is | a dictionary | a container |
| What it holds | names mapped to references | a namespace, the current line, the return address |
| Relationship | the frame **owns** the namespace; the namespace is one of the three things inside it |

**Wrong:** "a namespace is the dictionary of all the objects in memory."

**Correct:** a namespace maps **names to references**. It does not contain
objects, and it is not global. The objects live elsewhere in memory; the
namespace holds only the labels pointing at them.

Two consequences that prove the distinction is real:

- An object can exist with **no name** pointing at it. `[1,2] + [3]` builds a
  list that is never named. It exists, briefly, in no namespace at all.
- Two different namespaces can point at the **same object** at the same time. If
  the object lived *inside* the namespace, this would be impossible.

A namespace is a directory of labels, not a warehouse of things.

### 7. Running versus paused — what a stack of frames is actually doing

```python
def load():
    print("loading")

def run():
    load()
    print("running")

run()
```

At the exact instant `loading` appears on screen:

| Frame | State | Line it sits on | Waiting on |
|---|---|---|---|
| `load` (top) | running | line 2, the `print` | nothing |
| `run` | paused | line 5, `load()` | `load` to return |
| `<module>` (bottom) | paused | line 8, `run()` | `run` to return |

> **The rule.** The top frame is running. Every frame below it is paused, and
> each is paused on **its own line** — the line containing the call it is waiting
> on. There is no single shared line. Nothing on the stack is ever "completed",
> because completing means returning, and returning destroys the frame and
> removes it from the stack.

> **Corollary worth memorising:** a frame that appears on the stack, or in a
> traceback, is by definition **not finished**. If it were finished it would not
> be there.

Two sub-points that cause specific errors:

- **A paused frame is never paused on a `def` line.** A `def` executes fast: it
  builds a function object and binds a name, then it is done. It does not run the
  body. In the file above, the module frame is paused on line 8, not line 1.
- **A line finishing does not mean a frame finishing.** `load` had already
  executed its `print`, but it had not returned, so it was still running. **The
  frame ends at the return, not at its last visible action.**

### 8. Why a stack, and not a queue

This is not a design preference among options. It is **forced by the shape of the
problem**.

Read the "waiting on" column above. `<module>` is stuck until `run` returns;
`run` is stuck until `load` returns. So `load` must finish first, then `run` can
move, then `<module>` can move. The most recently started call is always the only
one not blocked, so it is always the first to finish. That is the definition of
last-in-first-out.

Now try the alternative, to see why it is *impossible* rather than merely
awkward. A queue (first-in-first-out) would mean the earliest call finishes
first, so `<module>` would have to complete before `run` does. But `<module>` is
frozen mid-line on `run()`. It has no next instruction until `run` hands back a
value. Finishing first is not slow for it — it is a **contradiction**.

> Python does not *select* a stack. Function call lifetimes are already LIFO; the
> stack is simply the data structure whose shape matches. Handed this problem
> cold, you would reinvent a stack.

### 9. Verify it yourself, every time

```python
import traceback

def load():
    print("loading")
    traceback.print_stack()

def run():
    load()
    print("running")

run()
```

`traceback.print_stack()` prints the **live** call stack at the instant it
executes, without crashing anything. Actual output (paths shortened):

```
loading
  File "trial.py", line 11, in <module>
    run()
  File "trial.py", line 8, in run
    load()
  File "trial.py", line 5, in load
    traceback.print_stack()
running
```

Three frames, each labelled with the exact line it is sitting on: 11, 8, 5. That
line number is the frame's "current line" field, made visible. This is the most
useful debugging tool covered so far, because it turns an abstract argument about
frames into something you can print.

### 10. Three corrections worth stating explicitly

**Rebinding vs mutation, correct form.** Look at what sits on the **left of the
`=`**. A bare name means rebinding; a name plus index or attribute access
(`nums[0]`, `config.speed`) means mutation. Anchoring on "there is an `=`, so it
rebinds" is the reflex that misclassifies `x[0] = 99`.

Related imprecision: `nums + [4]` is not "the modified list". Nothing was
modified — `nums + [4]` builds a **brand new** list object and leaves the
original untouched.

**`is` and the box model.** `is` compares **object identity**. CPython happens to
implement identity as the memory address, but that is a CPython detail, not a
language guarantee. And nothing is "stored in `a`" — `a` is a name bound to an
object.

**Strict vs permissive type checks.** `bool` is a subclass of `int`. Therefore
`isinstance(True, int)` is `True` and accepts the bool, while
`type(True) == int` is `False` and rejects it. To reject bools, use the strict
check.

---

## KEY MENTAL MODELS

- **Frame**: the container Python creates to run one chunk of code — namespace,
  current line, return address. Created at runtime, destroyed on return. Not the
  code.
- **Frames do not require functions.** A file with zero `def`s still gets exactly
  one frame.
- **Namespace vs frame**: a namespace is a dictionary mapping names to
  references; a frame owns a namespace. Objects live in memory, not inside
  namespaces.
- **`<module>` is the file's frame**, created before any line executes. Every
  program starts there.
- **Local names die with their frame** — they were entries in that frame's
  namespace.
- **Top frame runs, all others are paused**, each on its own calling line.
- **A frame on the stack is never finished.**
- **A line finishing is not a frame finishing.**
- **A paused frame is never paused on a `def` line.**
- **Stack is forced, not chosen.**
- **Rebinding vs mutation: classify by the left-hand side.**
- **`traceback.print_stack()`** prints the live stack without crashing. Use it.

---

## REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| frame | Runtime container: namespace + current line + return address | It is not the code, and it does not need a function |
| `<module>` | The frame for the file itself | Mistaken for `main`; it exists before `main` is called |
| namespace | Dict of names → references | Does not hold objects, and is not global |
| `locals()` | Prints the current frame's namespace | At file level it is padded with `__name__`, `__file__`, … |
| paused frame | A caller frozen on its calling line | Each sits on its *own* line; none of them are finished |
| `traceback.print_stack()` | Dumps the live stack, no exception needed | Prints bottom-of-stack first, like a traceback |

---

## SELF-TEST ANSWERS

1. One frame, called `<module>`. See §2.
2. The namespace for that chunk of code, the line currently executing, and the
   return address. See §1.
3. A namespace is a dictionary mapping names to references. A frame is the
   container that owns a namespace, plus the current line and return address.
   See §6.
4. No. Namespaces hold names mapped to references; objects live in memory. Proof:
   `[1,2] + [3]` creates an object with no name pointing at it, and two
   namespaces can point at one object simultaneously. See §6.
5. The top frame is running. Every frame below it is paused, each on its own
   line — the line containing the call it is waiting on. See §7.
6. No. A frame finishes by returning, and returning destroys it and removes it
   from the stack. If it is visible, it has not returned. See §7.
7. Because nested call lifetimes are already LIFO: each caller is frozen mid-line
   until its callee returns, so the most recent call is always the only unblocked
   one. A queue would require a frozen frame to finish first — a contradiction.
   See §8.
8. The module frame. A function frame is created by a call; a call is a line of
   code; a line of code can only run inside a frame that already exists. So a
   function frame is structurally incapable of being first. See §4.
9. Rebinding, because the left of the `=` is a bare name. `backup` still holds
   `[1,2,3]`, because `nums + [4]` built a new object rather than changing the
   old one. See §10.

---

## WHAT'S COMING NEXT — SESSION 7

- Re-test the entry point from a fresh traceback (third attempt).
- Re-test the running/paused rule on a three-frame program — which frame is
  running, which line each paused frame sits on.
- A cross-check drill: a multi-part question built so a wrong answer to one part
  contradicts another.
- Outstanding: apply the rebinding rule to `config.speed = 5`.
- Then close 1.3: `str` (immutability, common methods), `None` (singleton,
  `is None` not `== None`, `None` vs `False` vs `0`), type conversion (`int()`,
  `str()`, `float()`, `bool()`), implicit vs explicit.
- **Not** 1.4 yet — the mutation drill stays queued.
