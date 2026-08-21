# SESSION 7 NOTES — Tracebacks, Object Namespaces, and `str`

**Topics: reading a four-frame traceback · line finishing vs frame finishing ·
objects own namespaces too (`config.speed = 5`) · `==` vs `is` ·
compile time vs run time · what the REPL really does differently · `str`
immutability and the method roster**

---

## SELF-TEST — answer these cold before reading on

Do not read past this section until you have written answers. Confidence /5 on each.
After writing each answer, reread it against the rule you cited *in that same answer*
and confirm the answer obeys the rule. That check is the point.

Given this program, `pipeline.py`:

```python
 1  def scale(vec, factor):
 2      out = []
 3      for v in vec:
 4          out.append(v / factor)
 5      return out
 6
 7  def normalise(vec):
 8      total = 0.0
 9      for v in vec:
10          total = total + v * v
11      return scale(vec, total)
12
13  def run_pipeline():
14      raw = [0, 0]
15      result = normalise(raw)
16      return result
17
18  print(run_pipeline())
```

which raises `ZeroDivisionError` inside `scale`:

**S1.** Which function did the program start executing in?
**S2.** At the instant the exception was raised, how many frames were on the stack? Name them.
**S3.** Give the line number each of those frames was sitting on.
**S4.** Which frame was running? What was true of all the others?
**S5.** Had the `<module>` frame finished executing? Justify in one sentence.
**S6.** Had line 15 finished executing? Why?
**S7.** `config` is an object with a `speed` attribute. `config.speed = 5` runs. Rebinding or mutation? Does `id(config)` change? What rule did you apply?
**S8.** `p = True`, `q = 1`. What are `p == q` and `p is q`, and what is the mechanical difference between the operators?
**S9.** Between a `.py` source file and a `ZeroDivisionError`, what did CPython produce and what executed it? At which of those two moments does a frame get created?
**S10.** In the REPL you type `run_pipeline()` with no `print()`. Something appears on screen. In a script the same line shows nothing. Why?
**S11.** After `t = s.strip()`, is `s` changed? Is `id(s)` the same? What about `s[0] = "X"`?
**S12.** Name the four things that make `str` behave differently from `config` when you try to change them.

Answers at the bottom.

---

## FULL TEACHING

### 2.1 Reading a traceback as a stack snapshot

A **frame** is the container Python creates to execute one chunk of code. It holds
the namespace (the mapping from names to references), the current line, and the
return address. A **traceback** is a photograph of the frame stack at the instant
something went wrong.

For `pipeline.py` above, the traceback is:

```
Traceback (most recent call last):
  File "pipeline.py", line 18, in <module>
    print(run_pipeline())
  File "pipeline.py", line 15, in run_pipeline
    result = normalise(raw)
  File "pipeline.py", line 11, in normalise
    return scale(vec, total)
  File "pipeline.py", line 4, in scale
    out.append(v / factor)
ZeroDivisionError: float division by zero
```

Four frames. `<module>` on line 18, `run_pipeline` on 15, `normalise` on 11, `scale`
on 4. Read it bottom-up: the last block is where the error actually happened, and
everything above is the chain of callers still waiting.

Three things this shows that are easy to get wrong:

**Every program starts in `<module>`, not in a function you wrote.** `<module>` is
the frame Python creates for the file itself, before a single line runs. `main()`,
`run_pipeline()` or whatever you call your entry function is merely the *first thing
that frame calls*.

**Paused frames each sit on their own line.** Not one shared line. `<module>` is
stuck on 18, `run_pipeline` on 15, `normalise` on 11. Each is frozen exactly where
it made its call.

**A frame on the stack has not finished.** Finishing means returning, and returning
removes the frame. So the presence of `<module>` in that traceback is proof that
`<module>` is unfinished, no matter how much of line 18 looks like it already ran.

### 2.2 A line finishing is not a frame finishing

These are different questions and separating them is the whole skill.

Line 15 is `result = normalise(raw)`. An assignment needs a value on the right. The
value is `normalise`'s return. `normalise` never returned. So line 15 **started and
did not finish**. It is mid-flight, and it will stay mid-flight until the callee
returns.

The frame `run_pipeline` is paused, and it is paused *because there is a frame above
it*, not because line 15 decided to pause. The pause is a consequence of the stack,
not an action taken by a line.

### 2.3 Objects own namespaces too

You already knew a frame owns a namespace. So does an object.

When you write `config.speed = 5`, Python does not touch the name `config` at all.
It looks up what `config` refers to, then writes the entry `speed -> 5` into **that
object's own namespace**. Same dictionary idea, different owner.

```python
class Config:
    pass

config = Config()
config.speed = 1
before = id(config)
print("before:", before, config.__dict__)

config.speed = 5
after = id(config)
print("after :", after, config.__dict__)
print("id unchanged:", before == after)
```

```
before: 140382276940384 {'speed': 1}
after : 140382276940384 {'speed': 5}
id unchanged: True
```

So `config.speed = 5` is **mutation**. Same object, changed contents, `id` held.

**The rule.** Look at what sits on the LEFT of the `=`, not at the presence of
the `=`.

- A **bare name** on the left → rebinding. The name is pointed at a different object.
- A name **plus an accessor** on the left (`x[0]`, `config.speed`) → mutation. You
  are reaching through the name into the object it refers to and changing that.

`config.speed` is not a bare name. Neither is `x[0]`. Both are mutation — the same
shape as `x[0] = 99`.

### 2.4 `==` and `is`, third time

```python
p = True
q = 1
print('p == q :', p == q)
print('p is q :', p is q)
print('id(p)  :', id(p))
print('id(q)  :', id(q))
print('type(p):', type(p), ' type(q):', type(q))
```

```
p == q : True
p is q : False
id(p)  : 10654560
id(q)  : 11755688
type(p): <class 'bool'>   type(q): <class 'int'>
```

`True` and `1` are **two different objects**. `True` is the single `bool` instance;
`1` is a cached `int`. `p == q` is True because `bool` subclasses `int` and True's
numeric value is 1, so the comparison is numeric. `p is q` is False because they sit
at different addresses.

`==` asks *do these have the same value*. `is` asks *are these the same object*.
"Has the same value as" is not "is". The trap is that in English those sound identical.

### 2.5 Compile time and run time are different moments

Running `python pipeline.py` does two separate things.

1. **Compile.** CPython turns your source into **bytecode**, a static instruction
   sequence stored in a code object. Syntax errors surface here. Nothing has run yet.
2. **Execute.** The **PVM** (Python Virtual Machine) walks that bytecode. When it
   reaches a call, it creates a frame *at that moment* and pushes it.

So: bytecode is built at compile time; **frames are built at run time**. Collapsing
those two is a real error, because it makes frames sound like something the compiler
can see, and it cannot. The compiler does not know how many frames your program will
create; that depends on data, branches and recursion depth it has never seen.

### 2.6 What the REPL actually does differently

REPL is Read-Eval-**Print**-Loop. The P is the whole answer. The REPL automatically
displays the value of any expression you type. A script does not: an expression
statement is evaluated and the value is thrown away, so nothing appears unless you
call `print()`.

That is the *only* difference in what you see. It is not a difference in the
execution model. The REPL still creates a `<module>` frame per input:

```
$ printf 'import traceback\ntraceback.print_stack()\n' | python3 -
  File "<stdin>", line 2, in <module>
```

Note `<stdin>` where a filename would normally be. Same `<module>` frame.

### 2.7 `str` — immutability

**Intuition.** A string is a fixed run of characters, and Python will never edit one
in place. Every operation that looks like editing builds a brand new string and hands
it back. The original is untouched.

**Mechanism.** `config` had a namespace and you could write into it, so the object
changed and `id` held. A string has no such door. Nothing reaches inside an existing
`str` and alters it, so the only way to get different text is a different object,
which means a different `id`.

```python
# strdemo.py

s = "  Kinova Gen3  "
print("1  s       :", repr(s), id(s))

t = s.strip()
print("2  t       :", repr(t), id(t))
print("3  s again :", repr(s), id(s))

u = s.upper()
print("4  u       :", repr(u), id(u))

parts = "3,4,5".split(",")
print("5  split   :", parts)

print("6  join    :", "-".join(parts))

print("7  replace :", repr(s.replace("Gen3", "Gen7")))
print("8  s again :", repr(s), id(s))

try:
    s[0] = "X"
except TypeError as e:
    print("9  TypeError:", e)
```

```
1  s       : '  Kinova Gen3  ' 140565061446896
2  t       : 'Kinova Gen3' 140565061451440
3  s again : '  Kinova Gen3  ' 140565061446896
4  u       : '  KINOVA GEN3  ' 140565061451376
5  split   : ['3', '4', '5']
6  join    : 3-4-5
7  replace : '  Kinova Gen7  '
8  s again : '  Kinova Gen3  ' 140565061446896
9  TypeError: 'str' object does not support item assignment
```

Your `id` numbers will differ from these. Addresses are assigned fresh every run and
mean nothing in absolute terms. Only *sameness or difference within one run* carries
information.

Reading it:

- Lines 1 and 3 share an address, so `strip()` did not touch `s`. Line 2 is a new
  address: `strip` built a new object and returned it.
- `repr()` is used throughout because it shows the quotes, which is the only way to
  see the whitespace at the ends.
- Line 4 is a third address. `upper()` also built new, and it uppercased the padding,
  since the spaces were never removed from `s`.
- Lines 5 and 6 are `split` and `join`, inverses of each other. Note `join`'s odd
  shape: the separator is the string you call the method on, the list is the argument.
- Lines 7 and 8 are the important pair. `replace` returned a modified string, and `s`
  on the very next line is still original, same address as line 1. The return value
  was printed and discarded. **This is the most common string bug there is.**
- Line 9 is the hard proof. `s[0] = "X"` does not silently fail, it *raises*. `str`
  has no item assignment at all. Compare with `config.speed = 5`, which succeeded and
  held its `id`. Two constructs that look alike on the page, opposite outcomes, and
  the difference is a property of the object's type, not of the syntax.

**Methods to have now**, all returning new strings and changing nothing:
`.strip()`, `.upper()`, `.lower()`, `.replace(old, new)`, `.split(sep)`,
`sep.join(list)`, `.startswith(prefix)`, `.find(sub)`.

**Parked definition: string interning.** CPython sometimes reuses one object for
identical strings rather than creating two, which is why `a = "hi"; b = "hi"; a is b`
can come back `True` while the list version comes back `False`. Working definition
only; the mechanism is a 1.2 item. Build nothing on it. And never use `is` to compare
strings for equality in real code — the interning rules are an implementation detail
that will shift under you.

---

## EXTRA PRACTICE

Do these cold, notes closed, no REPL, confidence /5.

**P1.**
```python
class Config:
    pass

a = Config()
b = a
a.speed = 5
print(b.speed)
```
What prints, or does it raise? Why?

**P2.**
```python
a = "reading"
b = a
a = a.upper()
print(b)
```
What prints? Did any object change?

**P3.**
```python
name = "  culham  "
name.strip()
print(repr(name))
```
What prints? Why.

**P4.**
```python
x = "abc"
before = id(x)
x = x + "d"
after = id(x)
```
Is `before == after`? Rebinding or mutation, and which side of the `=` told you?

---

## SELF-TEST ANSWERS

**S1.** `<module>`. Not `run_pipeline`. Every program starts at module level; your
entry function is only the first thing the module frame calls.

**S2.** Four: `<module>`, `run_pipeline`, `normalise`, `scale`.

**S3.** `<module>` 18, `run_pipeline` 15, `normalise` 11, `scale` 4. Each paused frame
on its own line, not a shared one.

**S4.** `scale` was running. Every other frame was paused, frozen on the line where it
made its call.

**S5.** No. A frame on the stack has by definition not finished, because finishing
means returning and returning removes the frame.

**S6.** No. Line 15 is an assignment; an assignment needs the value on the right;
that value is `normalise`'s return; `normalise` never returned. The line started and
is still mid-flight.

**S7.** Mutation. `id(config)` is unchanged. Rule: look at the LEFT of the `=`.
`config.speed` is a name plus an accessor, not a bare name, so you are reaching
through `config` into the object and changing its namespace. A bare name on the left
would have been rebinding.

**S8.** `p == q` is True, `p is q` is False. `==` compares value; `is` compares
identity, i.e. whether both names refer to the same object. `True` and `1` are
distinct objects at distinct addresses, of distinct types (`bool` and `int`), but
compare equal because `bool` subclasses `int` and True's numeric value is 1.

**S9.** CPython produced **bytecode**; the **PVM** executed it. Frames are created at
**run time**, by the PVM, at the moment a call is reached. Never at compile time.

**S10.** The REPL is a Read-Eval-**Print**-Loop and automatically displays the value
of any expression you type. A script evaluates an expression statement and discards
the value, so nothing shows without an explicit `print()`. Execution model is
otherwise identical, including the `<module>` frame.

**S11.** `s` is unchanged and `id(s)` is the same; `strip()` returned a new object.
`s[0] = "X"` raises `TypeError: 'str' object does not support item assignment`.

**S12.** `str` has no namespace you can write into; no item assignment (it raises
rather than failing quietly); every method returns a new object rather than editing;
and any "change" therefore produces a new `id`, whereas mutating `config` held its
`id`.
