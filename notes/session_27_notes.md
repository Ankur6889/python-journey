# SESSION 27 NOTES — Saturday 22 August 2026
### 1.8 Data Structures — dict finished, `set` taught, when-to-use-which
### Layer 0 / Python Core · later-day session after S26

---

## 0. SELF-TEST — DO THIS FIRST, NOTES CLOSED

Answer all of these from memory before reading a single line below.

1. When does a `for` loop's `else` block run? What single word should you read
   the keyword as?
2. Give the one-line difference between `break`, `continue` and `pass`.
3. What can `"high" if n > 10 else "low"` do that a four-line `if`/`else`
   cannot? Give a concrete line of code.
4. What is the difference between **precedence** and **associativity**?
5. Name the error: `x = "5" + 3` · `x = 5 +` · `robot["speed"]` on a dict with
   no `"speed"` key · `rbot["joint"]` when `rbot` was never defined ·
   `seen[0]` on a set.
6. Three ways to remove a pair from a dict. What does each hand back?
7. Why is `{}` an empty dict and not an empty set? How do you write an empty set?
8. Why does `seen[0]` fail on a set even in principle?
9. `commanded - supported` where both are sets — what does that line MEAN?
10. What is the ONE question that decides between list, tuple, dict and set?
11. You log joint angles for a 30-second motion and replay it exactly. Which
    container, outer and inner, and why?
12. Why is a keyword argument allowed to appear out of order?

---

## 1. FULL TEACHING

### 1.1 The five flow-control keywords — recovered cold

All five had failed before. All five came back. The drill is
`drills/s27_flow.py` and the tests are `tests/test_s27_flow.py` — 20/20.

**`break` — bahar niklo.** Leaves the loop entirely, immediately.

```python
def first_big(values, limit):
    for i in values:
        if i > limit:
            break
    else:
        i = None
    return i

print(first_big([1, 7, 9, 2], 5))   # 7
print(first_big([5, 5, 5], 5))      # None
print(first_big([], 0))             # None
```
```
7
None
None
```

**Note the empty-list case.** `for` never runs, so `i` is never bound — and the
loop `else` is what saves it, by assigning `i = None`. That was not required by
the task; it was used unprompted and it is why the boundary case works.

**`continue` — agla chakkar.** Abandons *this* iteration only.

```python
def total_positive(values):
    total = 0
    for i in values:
        if i <= 0:
            continue
        total = total + i
    return total

print(total_positive([3, -4, 10, -1]))   # 13
print(total_positive([0, 0, 4]))         # 4  — zero is excluded
print(total_positive([]))                # 0
```
```
13
4
0
```

**`pass` — jagah bharo.** A no-op. It exists because **a block opened by a colon
cannot be empty** — and a comment is not a body.

```python
def todo(x):
    pass

print(todo(123))      # None
```
```
None
```

**Loop `else` — read the keyword as `nobreak`.** It runs only if the loop
reached its natural end without hitting `break`. It has nothing to do with the
`else` of an `if` and must never be read as "otherwise".

```python
def find_index(values, target):
    l = len(values)
    for i in range(l):
        if values[i] == target:
            break
    else:
        i = None
        print("missing")
    return i

print(find_index([10, 20, 30], 20))    # 1
print(find_index([1, 2, 3], 99))       # missing / None
```
```
1
missing
None
```

**Ternary — `ter-` = three: value, condition, value.** The middle is the
condition.

```python
def label(n):
    return "high" if n > 10 else "low"
```

### 1.2 The `find_index` rewrite — and the bug it killed

The first version looped over **items**, then recovered the position afterwards:

```python
    return values.index(i) if i != None else None
```

It passed all 20 tests. It was also wrong, and the bug only shows on a type
boundary:

```python
data = [None, 5, 9]
print("old:", old(data, None))   # loops over items
print("new:", new(data, None))   # loops over positions
```
```
old: None
new: 0
```

`None` is in the list at position 0. The old version found it and then **threw
the answer away**, because `None` was doing two jobs at once — *"the thing I
found"* and *"I found nothing"*. Walking positions makes the bug impossible:
**a position is never `None` unless the loop ran to the end.**

> **THE LESSON: a sentinel value must be something the data can never contain.
> This is the five checks' `bahar` — outside what you assumed — by TYPE.**

### 1.3 Precedence vs associativity — two different questions

```python
print(2 ** 3 ** 2)        # 512   -> 2 ** (3 ** 2)
print(2 + 3 * 4 ** 2)     # 50    -> 2 + (3 * (4 ** 2))
```
```
512
50
```

- **Precedence** = rank between **different** operators. Who goes first?
- **Associativity** = direction within the **same** rank.
  **Sab left se, sirf `**` right se.**

The first line is an associativity question — one operator, repeated. The second
is a precedence question — three different operators competing.

### 1.4 EXPRESSION vs STATEMENT — closed at last (owed since S14)

- An **EXPRESSION evaluates to a VALUE**: `n > 10`, `"high"`, `n + 1`, `len(x)`,
  a ternary, `a | b` on sets.
- A **STATEMENT DOES something and evaluates to nothing**: `x = 5`,
  `if n > 10:`, `for i in values:`, `return i`, `break`, `del d[k]`, `d[k] = v`.

> **THE TEST: can it go inside `print(...)`?** Values can. Actions cannot.

```python
n = 12
print(if n > 10: "high")
print("this line exists")
```
```
  File "synt.py", line 2
    print(if n > 10: "high")
          ^^
SyntaxError: invalid syntax
```

**Look at what did NOT happen: `n = 12` never ran and `"this line exists"` never
printed. Not one line of the file executed.** That is the whole `SyntaxError`
tell.

### 1.5 The error stations — now FIVE, not four

> **STATION 0 — DID IT RUN AT ALL?** Grammar broken ⇒ nothing executes ⇒
> `SyntaxError`. Only a *running* program can reach the rest.
> **STATION 1 — NAAM.** The name itself is not bound anywhere ⇒ `NameError`.
> **STATION 2 — DOT.** The name after the dot is not on the object ⇒
> `AttributeError`.
> **STATION 3 — TYPE.** The operation is not defined for these types ⇒
> `TypeError`.
> **STATION 4 — CHEEZ.** Everything was fine and the thing asked for is absent:
> **jagah** (position) ⇒ `IndexError` · **chaabi** (key) ⇒ `KeyError` ·
> **cheez** (value of right type, wrong content) ⇒ `ValueError`.

**The stations are an ORDER, not a menu.**

```python
robot = {"joint": 3}
robot.append(5)        # AttributeError: 'dict' object has no attribute 'append'
robot["speed"]         # KeyError: 'speed'
rbot["joint"]          # NameError: name 'rbot' is not defined
```

`rbot["joint"]` has a bad name **and** brackets — and Python never reached the
brackets. It failed at station 1 and stopped.

**THE TRAP THAT CAUGHT YOU, AND IT IS WORTH A LINE ON ITS OWN:**

```python
a = [10, 20, 30]
a[5]              # IndexError
b = {"x": 1}
b[0]              # KeyError: 0
seen = {"x"}
seen[0]           # TypeError: 'set' object is not subscriptable
```

> **The brackets are identical in all three. THE BRACKETS DO NOT DECIDE THE
> ERROR — WHAT YOU PUT INSIDE THEM DOES, and what the container IS decides
> whether the attempt is even possible.**
>
> **Station 3 vs station 4, the test: COULD PYTHON EVEN ATTEMPT IT?**
> Attempt made, thing absent → station 4. Attempt impossible → station 3.

New word: **subscriptable** = can be indexed with `[ ]`. `list`, `tuple`, `str`,
`dict` are. `set` is not.

### 1.6 Dict — the tail that was owed

**DELETION — three ways, and the difference is what you get back.**

```python
limits = {"shoulder": 90, "elbow": 120, "wrist": 45}
del limits["wrist"]                 # statement — hands back NOTHING
value = limits.pop("elbow")         # hands back the VALUE
result = limits.clear()             # returns None, leaves {}
print(value, result, limits)
```
```
120 None {}
```

- `del d[k]` is a **statement**. `x = del d[k]` is impossible.
- `d.pop(k)` hands back the **value** — **the returns-`None` counterexample, now
  seen on a second type.**
- `d.clear()` returns `None` and leaves `{}` — **empty, not gone. Same object.**
- `d.update(other)` merges `other` in, overwriting clashes, returns `None`.

**THE RAISING FORM AND THE SHRUGGING FORM — one rule, three appearances:**

| raises when absent | shrugs when absent |
|---|---|
| `d[k]` | `d.get(k)` / `d.get(k, default)` |
| `del d[k]` | `d.pop(k, default)` |
| `set.remove(x)` | `set.discard(x)` |

> **Raise when a missing thing is a BUG. Shrug when absence is EXPECTED and you
> have a real default. THE SPEC DECIDES THIS, NOT YOUR TEMPERAMENT.**

```python
limits = {"shoulder": 90}
print(limits.pop("gripper", "not fitted"))   # not fitted
del limits["gripper"]                        # KeyError: 'gripper'
```

**INSERTION ORDERING.**

```python
d = {}
d["shoulder"] = 90
d["elbow"] = 120
d["shoulder"] = 999          # overwrite an EXISTING key
print(d)
```
```
{'shoulder': 999, 'elbow': 120}
```

- A dict keeps its keys in the order they were **first inserted** (3.7+).
- **Overwriting a value does NOT move the key.** Position is set when the key
  first appears.
- Delete then re-add and the key goes to the **back** — it is a first appearance
  again.
- ⚠ **ORDERED IS NOT SORTED.** Insertion order, not alphabetical.

### 1.7 `set` — a dict with the values thrown away

Same braces, same hashing machinery, same uniqueness rule — **so set items must
be hashable for exactly the reason dict keys must be.**

```python
seen = {"elbow", "wrist", "elbow", "shoulder", "wrist"}
print(seen, len(seen))
print(type({}), type(set()))
```
```
{'elbow', 'wrist', 'shoulder'} 3
<class 'dict'> <class 'set'>
```

Five in, three out — **duplicates are absorbed SILENTLY, not rejected.**
⚠ **`{}` is an empty DICT. The only way to write an empty set is `set()`.**

```python
seen.add("shoulder")        # returns None -> mutating
seen.discard("gripper")     # absent -> shrugs
seen.remove("gripper")      # absent -> KeyError: 'gripper'
```

The label is `KeyError`, not some set-specific error — **a set item IS its own
chaabi.**

**WHY A SET HAS NO `[0]` — the same file, three runs:**

```python
a = {"elbow", "wrist", "shoulder"}
b = {"shoulder", "wrist", "elbow"}
print(a); print(a == b)
```
```
run 1: {'elbow', 'wrist', 'shoulder'}      True
run 2: {'shoulder', 'elbow', 'wrist'}      True
run 3: {'shoulder', 'wrist', 'elbow'}      True
```

**There is no first element to return.** Print order comes from which hash slot
each item landed in, and Python randomises string hashing per process. `seen[0]`
would give a different answer every run.

> **Python does not offer operations it cannot make mean anything.**

Also: **`a == b` is `True`** across different insertion orders — a set compares
purely by **contents**. And `sorted(seen)` returns a **list**; there is no such
thing as a sorted set.

**SET OPERATIONS — the reason sets exist.**

```python
supported = {"shoulder", "elbow", "wrist"}
commanded = {"elbow", "wrist", "gripper"}

supported | commanded     # union         -> in either
supported & commanded     # intersection  -> in both
commanded - supported     # difference    -> {'gripper'}
```

- **All three build a NEW set** — originals untouched — so they are
  **EXPRESSIONS** and go straight inside `print()`.
- **`-` is not symmetric.** Flip the operands, get a different question.
- `commanded - supported` in English: **the joints someone asked for that you
  cannot drive.** One operator, no loop, no `if`.

```python
command = {"elbow": 30, "gripper": 10}
bad = command.keys() - supported
if bad:
    print("unsupported joints:", bad)
```
```
unsupported joints: {'gripper'}
```

**`.keys()` is a VIEW, and views support set operations directly** — no
conversion needed. An empty set is **falsy**, so `if bad:` reads as *"if there
were any"*; no `len(bad) > 0`.

### 1.8 When to use which

> **THE DECIDING QUESTION: WHAT AM I GOING TO ASK THIS CONTAINER?**
> Not what you store — what you will ask it, repeatedly, in code not yet written.

| the question you will ask it | container |
|---|---|
| *"give me the one at position N"* / *"in order"* | **list** |
| same, but fixed size, position has meaning, must not change | **tuple** |
| *"give me the value for this key"* | **dict** |
| *"is this in you?"* / *"what's in both?"* | **set** |

**TWO CORRECTIONS WORTH KEEPING:**

1. **Pairing is not the reason for a dict — LOOKUP is.**
   `[("shoulder", 30), ("elbow", 45)]` stores pairs perfectly well, but
   answering *"what's the elbow at?"* means **walking and comparing**. The dict
   hashes the key and jumps.
2. **"Must not change" is the WEAKER of tuple's two reasons.** The stronger one:
   **a tuple is HASHABLE, so it can be a dict key or a set item. A list cannot.**
   ```python
   reachable = {(0, 0), (0, 1), (1, 1)}
   print((0, 1) in reachable)     # True
   ```

**THE APPLIED CASE — logging joint angles across a 30-second motion:**

```python
log = []
log.append((0.00, 30.0, 45.0, 10.0))     # (t, j1, j2, j3)
log.append((0.02, 30.4, 45.1, 10.0))
```

- **Inner = tuple.** Fixed-size record; each position means a specific joint.
- **Outer = list.** It must **grow** during the motion, and it is replayed **in
  order**. ⚠ **Order is NOT the list/tuple discriminator — both are ordered.
  GROWTH is.**
- The **timestamp is not a key**, it is another field of the sample. A dict
  keyed by timestamp never uses its one superpower, because you never hold the
  exact float to look up.
- **Where a dict WOULD win:** replay by discrete frame number — `frames[1500]` —
  real random access.

### 1.9 Keyword arguments

```python
def clamp(value, low, high): ...
clamp(50, high=90, low=10)      # legal
```

A **keyword argument** is matched to a **parameter** by **NAME**, so position
stops mattering. **PARAMETER** = the name in the `def` line. **ARGUMENT** = what
you pass at the call.

⚠ **`=` vs `:`** — inside a dict it is `{"a": 99}`, a **colon**. The `=` form is
a keyword argument and lives in a function **call**. Same shape, different
machine.

### 1.10 How deep does hashing go? (asked directly, answered honestly)

**You have enough. What you have is the Level 2 model:** a hash is a number
computed from the item's contents; Python uses it to jump straight to a slot and
never scans; the number must not change while the item is in the container, and
**that is the entire reason keys and set items must be immutable.**

**Deliberately NOT taught:** how the number is computed, collisions, table
resizing. **That is DSA — master Layer 8.** Parked, not refused.

---

## 2. THINKING GAPS THIS SESSION — with error-type classification

| # | Gap | Classification |
|---|---|---|
| 1 | `robot["speed"]` labelled **`IndexError`**; it is `KeyError`. **The one miss of the session.** Root cause: read the `[ ]` and reached for Index. | **Knowledge gap — LABEL, not mechanism.** The exact watch area. |
| 2 | `print(if n > 10: "high")` labelled **`TypeError`**; it is `SyntaxError`. The *sentence* he gave ("doesn't support this") was close; the label was wrong. | **Knowledge gap — LABEL.** Produced the fix: Station 0. |
| 3 | `seen[0]` on a set predicted as `KeyError`; it is `TypeError`. Reasoning was the right shape aimed **one station too late**. | **Structural — station 3 vs station 4 not yet separated.** Now taught with an explicit test. |
| 4 | **DESIGN-SWITCHING.** Asked three times what the outer container must DO when a sample arrives mid-motion, he **twice proposed a different design** instead of answering, then got it instantly on the direct re-ask. | ⚠ **NEW PATTERN — Lazy thinking, sideways variant.** Adjacent to depth-before-answer: that one stops early, this one goes sideways. He had the answer the whole time. |
| 5 | *"because I want order, its a tuple"* — order is not the list/tuple discriminator; **growth is**. | **Structural flaw** — a real discriminator confusion, now corrected. |
| 6 | Asked for **ONE deciding question** across the four containers, gave four correct STORAGE statements instead. | **Depth — surface answer accepted as finished.** The upstream half is the item. |
| 7 | Did not find the `find_index` sentinel bug on his own five-checks pass (`None` as both "found" and "not found"). | **Depth — the `bahar` check was not run against TYPE.** |
| 8 | *"python can definitely add a string to a integer"* — `+` is simply **not defined** for those types. | **Language precision** — reasoning right, verb too generous. |
| 9 | *"placeholders inside the function objects"* for **parameters**; `{"a"=99}` for `{"a": 99}`. | **Label slips on owned machinery.** Same signature as 1 and 2. |
| 10 | *"I am lazy to calculate so will say 512"* — he **had** done the work, so nothing logged, but the instinct was named. | **Habit watch, not an error.** The exact habit he asked to have policed. |

**THE STRUCTURAL FINDING, AND IT IS THE MOST IMPORTANT LINE IN THESE NOTES:**
**the term-retention watch area has split cleanly in two. MECHANISMS ARE NOW
STRONG — five recovered cold in one drill. LABELS ARE STILL THE FAILURE POINT —
four slips in one session, every one on machinery he demonstrably owns. The
hooks fixed the mechanisms and have not yet fixed the labels.** That is exactly
what the rule adopted this morning targets.

**WHAT WENT RIGHT, and it should be read as hard as the gaps:**
- **Eight promotions, all cold, all later-day, all rated** — the biggest haul
  since S25, and the first in three sessions to come with a drill file.
- **He used loop `else` unprompted** where the task did not require it, and that
  is what made his empty-list case work.
- **He derived the tuple-as-hashable argument himself** and applied it correctly
  to a set of coordinates.
- **Honest gap declared twice** rather than guessed.
- **Confidence calibration accurate across eight ratings** — the two 6/10s were
  the two shakiest answers.
- **Pushback 39 raised and upheld in full.**
- **He asked for the progress audit before deciding how to spend the last block**
  and chose the measurement instrument over more teaching.

---

## 3. TEACHING MISTAKES THIS SESSION

1. ⚠ **ONE DEFECTIVE ASK — PUSHBACK 39, UPHELD IN FULL.** *"You're checking
   whether a joint name is one you support. Would you reach for `remove` or
   `discard` to drop a joint from that set?"* A **membership** scenario welded
   to a **removal** question, with no reason given to remove anything. His words:
   *"question is itself senseless??"* Correct. **Fourth consecutive session with
   a spec-writing failure — but the volume collapsed from four in S26 to one.**
   **THE FIX THAT WORKED AND SHOULD NOW BE STANDARD: the re-issued version
   supplied the missing condition explicitly ("the handler may fire TWICE"), and
   that single clause made the question decidable.**
2. **MIS-TAG, TOO GENEROUS.** A [RECALL] was fired **thirty seconds after**
   teaching the station-4 table. It should have been [TEACH-BACK]. Caught and
   corrected before anything reached the ledger. **A same-minute correct answer
   measures echo, and echo in the ledger is worse than no entry.**
3. **MIS-TAG, TOO MODEST.** The traceback read was tagged [TEACH-BACK] when it
   was genuinely later-day cold material. Corrected **up** to [RECALL] and
   promoted. **Both directions matter: one protects the ledger from echo, the
   other stops real evidence being thrown away.**
4. **A FULL METHOD ROSTER WAS DELIVERED ON REQUEST, against the S17 no-roster
   doctrine.** Mitigated rather than avoided: it was prefaced with the S26
   finding that a delivered table failed within twenty minutes, framed as a
   reference sheet, and **paired with the discriminator rather than offered
   instead of it.** ⚠ **Watch whether it sticks. If it does not, that is the
   second data point and the doctrine wins outright.**
5. **The `todo` and `label` constraints said "the body is exactly one line"**
   without excluding a docstring — and he had copied the instructions into each
   function as a docstring for readability. **A channel workaround, not a code
   error.** Nothing logged; the constraint was read as "body excluding
   docstring". **Write constraints so a reasonable workaround cannot violate
   them.**

---

## 4. REFERENCE CHECKLIST — name · what it does · the trap

| Name | What it does | THE TRAP |
|---|---|---|
| `break` | leaves the loop entirely | there is no `break 2`; it exits the **innermost** loop only |
| `continue` | ends this iteration only | in a `while`, a `continue` above the state update makes it infinite |
| `pass` | fills a block that cannot be empty | **a comment is not a body** — `# todo` alone still raises |
| loop `else` | runs only if the loop finished **without** `break` | it is **not** "otherwise" — read it as `nobreak` |
| ternary | `A if C else B`, evaluates to a **value** | only for choosing one simple value; work in a branch makes it unreadable |
| precedence | rank between **different** operators | it is a different question from associativity — never bundle them |
| associativity | direction within the **same** rank | **`**` is the only right-to-left one** |
| expression | evaluates to a **value** | test it: can it go inside `print(...)`? |
| statement | **does** something, yields nothing | `d[k] = v` and `del d[k]` are statements — you cannot catch them in a variable |
| `SyntaxError` | grammar broken; **nothing ran** | line 1 never executes either — that is the tell |
| `NameError` | the name is bound nowhere | Python stops at the name; it never reaches the brackets |
| `AttributeError` | the name after the **dot** is not on the object | |
| `TypeError` | the operation is **not defined** for these types | it needs a **running** program; `SyntaxError` never gets that far |
| `IndexError`/`KeyError`/`ValueError` | jagah / chaabi / cheez absent | **the brackets are identical on a list and a dict — what's INSIDE decides** |
| subscriptable | can be indexed with `[ ]` | `set` is **not**; `list`/`tuple`/`str`/`dict` are |
| `del d[k]` | removes the pair | a **statement** — hands back nothing; raises `KeyError` if absent |
| `d.pop(k)` | removes and **returns the value** | the counterexample to the returns-`None` tell, on a second type |
| `d.clear()` | empties the dict, returns `None` | leaves `{}` — **empty, not gone; same object** |
| dict ordering | keys stay in **first-insertion** order | **ordered ≠ sorted**; overwriting a value does **not** move the key |
| `set` | unique, unordered, hashable items | **`{}` is an empty DICT — use `set()`** |
| `set.add` | adds, returns `None` | adding something present is a **silent** no-op |
| `remove` / `discard` | raise / shrug when absent | pick by whether absence is a **bug** — the spec decides, not temperament |
| `\|` `&` `-` | union / intersection / difference | all build a **NEW** set; **`-` is not symmetric** |
| set order | there is **no first element** | the same file printed three different orders in three runs |
| `.keys()` | a **view** of the keys | not a list — but it **does** support set operations directly |
| keyword argument | matched to a **parameter** by name | `=` in a call, **`:` in a dict** |
| parameter vs argument | the name in the `def` vs what you pass | they are not interchangeable words |
| when-to-use-which | **"what am I going to ASK this container?"** | not "what am I storing?" — that is the downstream half |
| list vs tuple | **growth**, not order | both are ordered; only one can grow |
| hashable | stable hash ⇒ immutable item | that is why a tuple can be a key and a list cannot |
| sentinel values | mark "nothing here" | **must be something the data can never contain** — `None` in a list of `None`s is a bug |

---

## 5. WHAT'S COMING NEXT

1. **Cold, task-first:** `KeyError` mixed with `IndexError` and `TypeError`;
   then the S26 backlog that has now been declared twice and never run — tuple,
   dict, shallow copy, unpacking, `list()`, `.get()`, `.items()`.
2. **COMPREHENSIONS.** The gate is open (iteration protocol [x] since S25) and
   was declared open at this session's close. List → dict.
3. **The 1.8 tail:** `zip`, f-strings, nested structures, `reversed()`,
   `copy.deepcopy`.
4. ⚠ **SUNDAY 23 AUG: THE COLD BUILD BLOCK.** ≥90 min, timed, no AI, git +
   pytest. Joint-limit clamp extended to multiple joints with `*args`/`**kwargs`.
   **The design hole is yours: `*args` gives angles positionally and
   anonymously, `**kwargs` gives limits by name, and nothing in that design
   pairs them.**
