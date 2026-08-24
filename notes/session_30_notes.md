# Session 30 — Monday 24 August 2026 (evening, after office)

**Topics:** comprehensions drill (list + dict), the container backlog
(`.get`/`.pop` defaults, set operations, slice-copy, tuple return, `sum`),
`KeyError` vs `IndexError`, raise-vs-shrug.
**Rule adopted:** SPEC BEFORE PUZZLE → **RULES v5**.
**Yield:** 2 curriculum ticks, 8 ledger promotions, 35 tests passed cold.

---

## 0. SELF-TEST FIRST — close these notes and answer these

Do this before reading anything below. Say "gap" where empty.

1. In `[key for key, value in d.items() if value > 10]`, what runs first, and
   what runs last?
2. Which part decides whether the expression runs at all?
3. `d = {0: "a", 1: "b"}; d[5]` — which error? `l = ["a", "b"]; l[5]` — which
   error? What decides?
4. Write the shrugging form of `d[k]`. Write the shrugging form of `d.pop(k)`.
5. When do you deliberately want the form that RAISES?
6. `.items()` hands you what, exactly? What arrives if you loop `d` directly?
7. `a = [1,2,3]; b = a[:]` — what is `b`, and is it the same object as `a`?
8. `return low, high, high - low` — how many objects come back?

---

## 1. FULL TEACHING

### 1.1 Comprehension execution order — the load-bearing fact

The written order is not the execution order.

```python
speeds = [3, 0, 7, 0, 12]
print([100 / v for v in speeds if v != 0])
```
```
[33.333333333333336, 14.285714285714286, 8.333333333333334]
```

Written: `EXPRESSION for VAR in ITERABLE if CONDITION`.
Executed: **ITERABLE → VAR → CONDITION → EXPRESSION.**

**The condition is a GATE.** It runs *before* the expression, which is the only
reason the line above does not raise `ZeroDivisionError`. The zeros never reach
the division — they are stopped one step earlier. Remove the gate and it dies:

```python
print([100 / v for v in speeds])
```
```
ZeroDivisionError: division by zero
```

That is not a rule to memorise. It is a fact you can *prove* in two lines, and
proving it is how you keep it.

### 1.2 Dict comprehensions and `.items()`

```python
limits = {"shoulder": 90, "elbow": 45}
print({key: value * 2 for key, value in limits.items()})
print([key for key, value in limits.items() if value > 45])
print([key for key in limits])
```
```
{'shoulder': 180, 'elbow': 90}
['shoulder']
['shoulder', 'elbow']
```

Two things make it a dict rather than a list: **the braces and the colon.**

`.items()` hands you **one tuple per pass**. `for key, value in ...` is **tuple
unpacking** — two names on the left taking apart the tuple on the right. Loop
the dict directly and you get **keys only**.

**Dict order:** keys stay in **first-insertion** order. Overwriting a value does
**not** move a key; deleting and re-adding **does** move it to the back.
⚠ **Ordered is not sorted.**

```python
limits = {"z": 1, "a": 2, "m": 3}
limits["z"] = 99          # overwrite — z stays first
print(list(limits))
del limits["a"]; limits["a"] = 2   # delete then re-add — a goes last
print(list(limits))
```
```
['z', 'a', 'm']
['z', 'm', 'a']
```

### 1.3 f-strings and the format spec

```python
print(f"{'shoulder':10s}{12.5:8.2f}")
print(f"{'elbow':10s}{4.0:8.2f}")
print(f"{'wrist_rotation':10s}{100.456:8.2f}")
```
```
shoulder     12.50
elbow         4.00
wrist_rotation  100.46
```

- The number is **TOTAL field width**, not extra spaces.
- **Text hugs LEFT, numbers hug RIGHT** — which is why the decimal points line
  up in the first two rows.
- A name **longer** than its column is **not truncated** — the column simply
  gives way, and the alignment breaks. Row three shows it.

### 1.4 `KeyError` vs `IndexError` — the container decides

```python
data = {0: "shoulder", 1: "elbow"}
print(data[5])
```
```
KeyError: 5
```
```python
names = ["shoulder", "elbow"]
print(names[5])
```
```
IndexError: list index out of range
```

Both lines are `[5]`. **The brackets do not decide the error.** In the dict `5`
is a *chaabi* that is not there; in the list `5` is a *jagah* that is not there.
Station 4 of the four-station hook: **jagah = Index, chaabi = Key, cheez =
Value.**

### 1.5 Raise vs shrug — ONE design rule, seen three times

| Raises when missing | Shrugs when missing |
|---|---|
| `d[k]` | `d.get(k, default)` |
| `del d[k]` | `d.pop(k, default)` |
| `s.remove(x)` | `s.discard(x)` |

```python
d = {"shoulder": 90}
print(d.get("wrist", "SHRUG"))
print(d.pop("wrist", "SHRUG"))
print(d)
```
```
SHRUG
SHRUG
{'shoulder': 90}
```

**The rule:** use the **raising** form when a missing thing is a **BUG** — you
want the crash, at the cause, loudly. Use the **shrugging** form when absence is
**EXPECTED** and the default is a real answer.

⚠ A shrug in the wrong place is worse than a crash: it moves the failure away
from its cause and you debug the wrong line.

### 1.6 The container one-liners

```python
print(set(["a", "a", "b"]) & set(["b", "c"]))   # intersection, dedup for free
print([10, 20, 30][:])                          # a NEW list, same contents
def span(low, high): return low, high, abs(low - high)
print(span(-90, 90))                            # ONE tuple comes back
print(sum([]))                                  # 0, not an error
```
```
{'b'}
[10, 20, 30]
(-90, 90, 180)
0
```

`|` union, `&` intersection, `-` difference — all build a **new** set, so all
three are **expressions** and go straight inside `print()`. `-` is **not**
symmetric.

---

## 2. CODE YOU WROTE THIS SESSION

`drills/s30_comprehensions.py` — **16/16 cold**

```python
def over_limit(angles, ceiling):
    return [x for x in angles if x > ceiling]

def scaled(limits, factor):
    return {key:value*factor for key,value in limits.items() }

def names_over(limits, ceiling):
    return [key for key,value in limits.items() if value>ceiling]

def format_row(name, value):
    return f"{name:10s}{value:8.2f}"
```

`drills/s30_containers.py` — **19/19 cold** (final form, after the rewrite)

```python
def limits_for(limits, joint):
    return limits.get(joint,(0,0))

def shared_joints(a, b):
    return set(a)&set(b)

def pop_limit(limits, joint):
    return limits.pop(joint,None)

def snapshot(angles):
    return angles[:]

def span(low, high):
    return (low,high,abs((low)-(high)))

def total(angles):
    return sum(angles)
```

---

## 3. THINKING GAPS THIS SESSION (with error-type classification)

**GAP 1 — the raise-vs-shrug rule stated INVERTED. Type: KNOWLEDGE GAP (label),
not structural.**
Asked when to choose the raising form, you answered *"when we don't want silent
errors, **or when the absence is expected**"* — the second half is the condition
for the *other* form. Two narrowing re-asks fixed it. The mechanism was never in
doubt; the two halves were welded to the wrong sides.

**GAP 2 — `.get(k, default)` and `.pop(k, default)` could not be recalled.
Type: KNOWLEDGE GAP (arbitrary label on owned machinery) — the file's own
diagnosed pattern.**
You produced the correct *behaviour* twice by hand
(`limits[joint] if joint in limits else (0,0)`). The design rule is yours. The
two API names were gone — taught S26 and S27, **never re-tested until tonight.**
⚠ **That is the file's failure, not yours.**
⚠ **Second-order lesson: your hand-rolled version passed 19/19. A green suite
can hide a lost tool.**

**GAP 3 — depth-before-answer, three firings, all recovered. Type: LAZY
THINKING (the named habit), not comprehension.**
(a) You listed the four comprehension parts in order but skipped *"which part
decides whether the others run"*. (b) You named both errors but skipped *"what
decides the difference"*. (c) The inverted rule above. **Each time the fix was a
re-ask, never a re-teach — you had the answer and stopped at the first
plausible one.** Sixteen, seventeen and eighteen straight recoveries.

**GAP 4 — confidence miscalibration. Type: SELF-ASSESSMENT.**
You rated raise-vs-shrug **8/10** immediately after stating it inverted and
needing two re-asks. Challenged to **5–6** with the evidence named. Every other
rating tonight (8, 8, 8, 7, 7) was well calibrated. **The pattern to watch: on
items where you own the CONCEPT but have lost the TOOL, you appear to rate the
concept.**

**NOT A GAP — logged so it is not mistaken for one:**
- The `.pop()` second-argument guess (`ValueError`) was a **[PREDICT]** on
  never-before-seen behaviour. **Not ledger-eligible in either direction.**
- The four "done"s where the file had not been saved were a **CHANNEL
  ARTEFACT**, not a lapse. Nothing logged.

---

## 4. TEACHING MISTAKES THIS SESSION

1. **"Give me a minute" and then nothing.** The mentor announced it was writing
   the container drill and produced no file, and you had to prompt: *"what
   happened I am still waiting."* **Pushback 49, upheld in full.** The rule it
   restates: **do not announce work, do the work.** A holding message costs a
   turn and buys nothing.
2. **The new rule leaked a measurement on its first day.** SPEC BEFORE PUZZLE
   requires exact expected values; `over_limit([10,45,90,45,5], 45) -> [90]` was
   meant to be a **blind** boundary test and the docstring handed you the
   boundary. Your strict `>` was correct, but **it is not clean evidence.**
   Fix now written into RULES v5: **boundary cases go in the TESTS, never in the
   worked examples.**
3. **The reference implementation was weaker than yours.** The mentor's `span`
   used `high - low`; yours used `abs(low - high)`. No test had `low > high`, so
   the mentor's version would have passed while being wrong. **You covered a
   case the tests did not.**

---

## 5. REFERENCE CHECKLIST — name / what it does / the trap

| Name | What it does | The trap |
|---|---|---|
| list comprehension | an **expression** that builds a **new list** | written order ≠ execution order |
| execution order | iterable → var → condition → expression | the expression is **last**, not first |
| the filter | a **gate** before the expression | it is what stops `ZeroDivisionError` |
| dict comprehension | `{K: V for ... }` | the **braces and the colon** make it a dict |
| `.items()` | one **tuple** per pass | looping the dict directly gives **keys only** |
| unpacking | two names take apart one tuple | count mismatch ⇒ `ValueError` |
| dict order | **first-insertion** order | ordered ≠ **sorted**; re-adding moves a key |
| f-string | evaluate → `str()` → splice | no `f` and `{x}` is literal characters |
| format spec | `{v:8.2f}` | the number is **total width**; long names are not truncated |
| `KeyError` / `IndexError` | chaabi missing / jagah missing | **the container decides, not the brackets** |
| `.get(k, default)` | shrugging lookup | shrugging at a **bug** hides the cause |
| `.pop(k, default)` | shrugging removal | `.pop(k)` alone **raises** |
| `remove` / `discard` | raising / shrugging on a set | the error is `KeyError` — an item **is** its own chaabi |
| `&` `\|` `-` | intersection / union / difference | all build **new** sets; `-` is **not** symmetric |
| `l[:]` | new **outer** list | it is a **shallow** copy — nested objects are shared |
| `return a, b` | builds **one** tuple | a function never returns more than one object |
| `sum([])` | `0` | it does not raise on empty |
| `abs()` | distance from zero | ⚠ **you used it before it was taught** — see S31 |

---

## 6. WHAT'S COMING NEXT (Session 31)

1. **The clamp refactor** — spec already issued and accepted; 4 tests currently
   failing on purpose in `builds/block_01_joint_clamp/`.
2. **The asks you earned but were never given:** f-string + format spec (third
   session running), slice-copy, `set()`/`&`, single-return-tuple.
3. **Raise-vs-shrug, cold** — it did not promote tonight.
4. **Tuple / set / hashability / when-to-use-which** — the concepts behind the
   code you already wrote.
5. **`while` mechanics** — four sessions overdue.
6. **Then the 1.8 tail:** nested structures → shallow copy lands, `reversed()`,
   `copy.deepcopy`. **Then 1.8 closes.**
