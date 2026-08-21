# Session 26 — Friday 21 Aug 2026
## 1.8 Data Structures — tuple taught in full, dict opened
### Same-day session (S25 closed hours earlier). NOTHING PROMOTED. No [x] awarded.

---

## 0. SELF-TEST — do this cold, before reading anything below

No notes open. Write the answers, then check.

1. What actually makes a tuple — the parentheses or the comma? What is `type((5))`?
2. `t = (1, 2)` then `t[0] = 9`. Which error, and why *that* one?
3. `t = (1, 2)` then `t.append(3)`. Which error, and why is it a **different** one from Q2?
4. A tuple can only ever have methods of one kind. Which kind, and why? Name the two it actually has.
5. `config = ("arm", [10.0, 20.0])` — is `config[1].append(30.0)` legal? Why?
6. `original = [["a"], ["b"]]`, `copy = original[:]`, then `copy[0].append("z")`. What is `original` now, and what is the term for what `[:]` did?
7. A function does `return -170.0, 170.0`. How many objects does it return?
8. `low, high = (1, 2, 3)` — which error?
9. Say the four-station hook in order, and the three station-4 siblings.
10. Why can a tuple be a dict key but a list cannot? Give the *mechanism*, not the rule.
11. `d["gripper"]` on a missing key vs `d.get("gripper")` — what does each do, and when is `.get()` the **wrong** choice?
12. Looping a dict directly gives you what? What does `.items()` give you, and what Python feature is `for name, angle in d.items()` secretly using?

---

## 1. FULL TEACHING

### 1.1 The problem tuples solve

Everything in this course about mutation converges here.

```python
def calibrate(readings):
    readings.append(0.0)
    return sum(readings)

joint_angles = [10.0, 20.0, 30.0]
total = calibrate(joint_angles)

print(total)
print(joint_angles)
```
```
60.0
[10.0, 20.0, 30.0, 0.0]
```

Passing an argument **binds the parameter name to the same object**. `readings`
and `joint_angles` are two names for one list. A mutating method called through
either name is visible through both.

> **`sum(iterable)`** — built-in, defined this session for the first time
> (ninth substrate breach; see Teaching Mistakes). Walks an iterable of numbers,
> returns their total as a new value. Does not mutate.

### 1.2 What a tuple is

A **tuple** is a sequence — ordered, indexable, iterable — that is **immutable**.
Once built, no element can be replaced, added, or removed.

```python
joint_limits = (-170.0, 170.0)

print(joint_limits)
print(type(joint_limits))
print(joint_limits[0])
print(len(joint_limits))
```
```
(-170.0, 170.0)
<class 'tuple'>
-170.0
2
```

### 1.3 Immutability arrives as `TypeError` — and its neighbour is `AttributeError`

```python
joint_limits = (-170.0, 170.0)
joint_limits[0] = -90.0
```
```
TypeError: 'tuple' object does not support item assignment
```

```python
joint_limits.append(180.0)
```
```
AttributeError: 'tuple' object has no attribute 'append'
```

**The distinction, and it is the useful one:**

| Line | Error | Why |
|---|---|---|
| `t[0] = x` | `TypeError` | The operation (item assignment) **exists**; this type refuses it |
| `t.append(x)` | `AttributeError` | The name after the dot **is not there at all** — Python never got as far as doing anything |

**Immutability has no special error of its own. It shows up as `TypeError`.**

### 1.4 Non-mutating operations build new objects

```python
joint_limits = (-170.0, 170.0)
new_limits = joint_limits + (200.0,)
print(joint_limits)
print(new_limits)
```
```
(-170.0, 170.0)
(-170.0, 170.0, 200.0)
```

`+` did not mutate. It built a **new** tuple. Same shape as `sorted()` vs
`sort()`. On an immutable type it is the **only** option available.

### 1.5 THE COMMA MAKES THE TUPLE, NOT THE PARENTHESES

The single commonest tuple trap.

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```
```
<class 'int'>
<class 'tuple'>
```

`(5)` is the ordinary **grouping** parenthesis from arithmetic — `(2 + 3) * 4`.
Wrapping one value in it gives the value straight back.

```python
c = 1, 2, 3
d = (1, 2, 3)
print(type(c), c)
print(type(d), d)
```
```
<class 'tuple'> (1, 2, 3)
<class 'tuple'> (1, 2, 3)
```

Parentheses are written for readability, and are *required* only where a bare
comma would be ambiguous (inside a call, for instance).

### 1.6 A function never returns more than one value

```python
def limits():
    return -170.0, 170.0

result = limits()
print(type(result))
print(result)
```
```
<class 'tuple'>
(-170.0, 170.0)
```

**"Returning multiple values" is tuples wearing a costume.** `return a, b`
builds one tuple and returns that one object.

### 1.7 Unpacking

```python
low, high = limits()
print(low)
print(high)
```
```
-170.0
170.0
```

**Unpacking** — the name decodes: the tuple is taken apart and its items bound
to names, left to right, in one statement. Works on any tuple:

```python
x, y, z = 1, 2, 3
```

Count mismatch — boundary-first:

```python
low, high = (-170.0, 170.0, 200.0)
```
```
ValueError: too many values to unpack (expected 2)
```

**`ValueError`, not `TypeError`.** The type is fine — a tuple *is* unpackable.
The **number of values** is wrong. Two names, three items, and Python refuses to
guess which to drop.

### 1.8 The tuple method roster is derivable, not memorable

Applying the type-first discriminator: a list has `append`, `extend`, `insert`,
`sort`, `remove`, `pop`. **All six mutate. None can exist on a tuple.**

Why is there no new-object `append`? **Because that already exists and is spelled
`+`.** Naming it `append` would be a lie — `append` promises in-place.

```python
t = (3, 1, 2, 1)
print(t.count(1))
print(t.index(2))
```
```
2
2
```

**Two methods, and both only report.** `count(x)` → how many times `x` appears.
`index(x)` → position of the first `x`.

> **THE DERIVABLE RULE: an immutable type can only carry methods that REPORT.
> Anything that would change it cannot exist.** This is the Level 2 answer to
> every "how do I know which methods exist?" question — a predictive model, not
> a lookup table.

### 1.9 Immutability is SHALLOW — the trap that catches experienced people

```python
config = ("arm", [10.0, 20.0])
config[1].append(30.0)
print(config)
```
```
('arm', [10.0, 20.0, 30.0])
```

Legal. And the other end:

```python
config[1] = [99.0]
```
```
TypeError: 'tuple' object does not support item assignment
```

> **THE MODEL: a tuple stores REFERENCES, not objects. Immutable means the
> references cannot be re-pointed. It says nothing about the objects they point
> at.** You cannot make slot 1 point at a *different* list. You can do anything
> you like to the list it already points at.

### 1.10 The same sentence, one level down: shallow copy

Discharges the point parked in S24, where `tools[:]` was called *"an identical
new list object"* — true of the outer list, and it hides this:

```python
original = [["a"], ["b"]]
copy = original[:]

copy.append(["c"])
copy[0].append("z")

print(original)
print(copy)
```
```
[['a', 'z'], ['b']]
[['a', 'z'], ['b'], ['c']]
```

```
original ──▶ [ •  ,  •  ]
               │     │
               ▼     ▼
             ["a"] ["b"]        ← the SAME two inner lists
               ▲     ▲
               │     │
copy ──────▶ [ •  ,  •  ]
```

Two mutations, two different levels:

- `copy.append(["c"])` mutates the **outer** list. Outer lists are separate →
  only `copy` changes.
- `copy[0].append("z")` never touches the outer list. It follows a reference to
  the **shared inner list** and mutates that. Both names see it.

**`original[:]` makes a SHALLOW COPY — *uthla*, one level deep.** Level one is
copied; everything below is shared.

**The trap can only fire when a container holds MUTABLE objects.** With flat
strings there is nothing shared-and-mutable to reach:

```python
copy = ["a", "b"]
copy[0].append("z")
```
```
AttributeError: 'str' object has no attribute 'append'
```
versus
```python
"abc"[0] = "z"
```
```
TypeError: 'str' object does not support item assignment
```

### 1.11 When to choose a tuple — what it buys beyond style

```python
def clamp(angle, limits):
    if angle > limits[1]:
        limits[1] = angle        # a "temporary fix" added under deadline
    return angle

joint_limits = [-170.0, 170.0]
clamp(200.0, joint_limits)
print(joint_limits)
```
```
[-170.0, 200.0]
```

The arm's safety limit silently moved to 200°. With a tuple:
`TypeError: 'tuple' object does not support item assignment`.

Three concrete gains:

1. **You can stop reading.** With a tuple you know the value never changed,
   without auditing every function it was passed to.
2. **The failure moved** — from a silent wrong value at runtime (worst) to a
   loud error on the exact offending line (best).
3. **It states intent.** `tuple` = fixed record. `list` = growing collection.

Fourth gain, delivered in §2.3: **a tuple can be a dict key; a list cannot.**

**Applied:** streaming joint angles → **list** (changing every tick). Joint
limits read once from the URDF → **tuple** (fixed).

---

## 2. dict

### 2.1 The problem it solves — parallel lists

```python
joint_names  = ["shoulder", "elbow", "wrist"]
joint_angles = [10.0, 20.0, 30.0]

i = joint_names.index("elbow")
print(joint_angles[i])
```
```
20.0
```

**Two defects, both found by the student unaided:**

1. **The pairing isn't enforced.** `joint_angles.append(40.0)` without touching
   `joint_names` leaves an angle with no name. Nothing in the language stops the
   lists drifting apart — the pairing lives only in your head.
2. **Lookup by name costs a scan.** `.index()` walks the list one item at a time
   until it matches. Cost grows **linearly** with length — 10,000 names, worst
   case 10,000 comparisons. (Formalised in DSA, master Layer 8. Level 2 answer:
   *`.index()` walks the list.*)

And a missing name:
```python
joint_names.index("gripper")
```
```
ValueError: 'gripper' is not in list
```
`index` exists and ran fine, so it is **not** `AttributeError`. The type is fine
(a string is a valid thing to search for). The **value** isn't there.

### 2.2 What a dict is

```python
joints = {"shoulder": 10.0, "elbow": 20.0, "wrist": 30.0}

print(joints["elbow"])
print(len(joints))
print(type(joints))
```
```
20.0
3
<class 'dict'>
```

A dict stores **key → value pairs**. `[]` now takes a **key** instead of a
position. The pairing is inside one object, so it cannot drift. Lookup does
**not** scan — roughly the same cost at 3 entries or 10 million.

**Keys are unique, and it is derivable:** if two identical keys could exist,
`joints["elbow"]` would have no single answer. `[]` must return one value.

```python
joints = {"shoulder": 10.0, "elbow": 20.0}
joints["wrist"] = 30.0     # new key    → INSERTS
joints["elbow"] = 25.0     # exists     → OVERWRITES
print(joints)
```
```
{'shoulder': 10.0, 'elbow': 25.0, 'wrist': 30.0}
```

**Same `[]=` syntax, two behaviours, decided by whether the key already exists.
Never duplicates.**

```python
print(joints["gripper"])
```
```
KeyError: 'gripper'
```

**`KeyError` — the KEY is what broke.** Decodes like every other error name.
**NEVER TAUGHT BEFORE THIS SESSION** — see Teaching Mistakes.

### 2.3 Why keys must be immutable — the hash

```python
limits_b = {["shoulder", "min"]: -170.0}
```
```
TypeError: unhashable type: 'list'
```

A dict finds a value **without scanning** by computing a number from the key and
using it to jump straight to a slot. That number is the **hash**.

> **The key's contents must never change after it is stored.** Otherwise the
> number computed later would not match the slot it was filed under, and the
> value would be unreachable — still sitting in the dict, never retrievable.

**Immutable ⇒ contents can't change ⇒ hash is stable ⇒ safe as a key.** Python
enforces it up front rather than letting you create an unfindable entry. The
error message names the real property: **unhashable**, not "immutable".

**Immutability does NOT mean uniqueness** — a student claim, corrected:

```python
d = {(1, 2): "a"}
d[(1, 2)] = "b"
print(d)
```
```
{(1, 2): 'b'}
```
Two equal tuples are the **same key**.

### 2.4 Avoiding `KeyError`: `in` and `.get()`

```python
joints = {"shoulder": 10.0, "elbow": 20.0}
print("elbow" in joints)
print("gripper" in joints)
```
```
True
False
```

**`in` on a dict checks the KEYS**, not the values — same near-instant lookup.

```python
print(joints.get("elbow"))
print(joints.get("gripper"))
print(joints.get("gripper", 0.0))
```
```
20.0
None
0.0
```

`.get(key)` never raises — returns `None` if absent. `.get(key, default)`
returns your fallback.

**The design trap:**

```python
angle = joints.get("gripper")
angle * 2
```
```
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

**`.get()` did not prevent the crash. It MOVED it.** The traceback now points at
`angle * 2`, which is innocent; `joints["gripper"]` would have pointed at the
actual missing key, by name.

> **THE RULE:** `[]` when a missing key is a **bug**. `.get()` when absence is
> **expected and you have a real default**. `.get()` with no default is the
> dangerous middle — it manufactures a `None` that travels.

Same principle as §1.11: **loud failure at the cause beats a silent wrong value
far away.**

### 2.5 Iterating a dict

```python
for j in joints:
    print(j)
```
```
shoulder
elbow
```

**Looping a dict directly gives the KEYS.** Student's own working version:

```python
for i in joints:
    print(f"{i} {joints[i]}")
```
```
shoulder 10.0
elbow 20.0
```

Correct, but it does the lookup twice — once to hand you the key, once for
`joints[i]`. The idiomatic form:

```python
for name, angle in joints.items():
    print(name, angle)
```
```
shoulder 10.0
elbow 20.0
```

And `.items()` is quietly using tuple unpacking from §1.7:

```python
for pair in joints.items():
    print(pair, type(pair))
```
```
('shoulder', 10.0) <class 'tuple'>
('elbow', 20.0) <class 'tuple'>
```

The family:

```python
print(joints.keys())
print(joints.values())
print(joints.items())
```
```
dict_keys(['shoulder', 'elbow'])
dict_values([10.0, 20.0])
dict_items([('shoulder', 10.0), ('elbow', 20.0)])
```

---

## 3. THE FOUR-STATION HOOK — the session's retention artefact

Built at the student's own diagnosis: *"I can't comprehend how to apply the
chain... maybe it's not sticking in my mind."* **He was right, and the cause was
that a TABLE had been handed over. Tables do not stick in this file's history;
HOOKS do (the S25 finding).**

> **NAAM → DOT → TYPE → CHEEZ**

Python ek line chalate waqt **chaar station** se guzarti hai. Gaadi jahan ruk
gayi, wahi error.

| Station | Sawaal | Ruk gayi ⇒ |
|---|---|---|
| **1. NAAM** | Ye naam hai bhi kahin? | `NameError` |
| **2. DOT** | Dot ke baad wala naam is object pe hai? | `AttributeError` |
| **3. TYPE** | Is type pe ye kaam hota hi hai? | `TypeError` |
| **4. CHEEZ** | Kaam ho sakta hai — par cheez andar hai? | `ValueError` / `IndexError` / `KeyError` |

**Station 4 ke teen bhai — poochho "dhoondh kaise rahe the?":**

- **Position se** dhoondha, nahi mila → **`IndexError`**
- **Chaabi se** dhoondha, nahi mila → **`KeyError`**
- **Value se** dhoondha (ya value bekaar thi) → **`ValueError`**

**Ek line me:** *Naam, Dot, Type, Cheez — aur cheez wale me: jagah = Index,
chaabi = Key, cheez khud = Value.*

Worked on the two he got wrong:
- `joint_names.index("gripper")` → naam ✅, dot ✅ (`index` exists), type ✅ →
  station 4, dhoondha **value** se → **`ValueError`**
- `joints["gripper"]` → station 4, dhoondha **chaabi** se → **`KeyError`**

**UNTESTED. Built same-day. First legitimate cold test is S27.**

---

## 4. THE FULL ERROR REFERENCE (built on request, mid-session)

Delivered in Hindi at his request, with real generated output (Python 3.12.3).
Master hook: **"Error ka naam batata hai KYA toota."**

| Family | Error | Mechanism |
|---|---|---|
| **A — code chala hi nahi** | `SyntaxError` | Grammar toota; Python vaakya padh hi nahi sakta. Ek bhi line nahi chalti |
| | `IndentationError` | Colon ne block khola, andar indented statement nahi mila. Block khaali nahi ho sakta — yahi `pass` ka gate hai |
| **B — naam nahi mila** | `NameError` | Poore LEGB me ye naam bandha hi nahi hai |
| | `UnboundLocalError` | Naam **hai**, local hai, par abhi value bandhi nahi. Function me assignment likhte hi naam compile-time par local ban gaya |
| | `AttributeError` | Object mila; uspe wo attribute/method hai hi nahi. Call tak pahuncha hi nahi |
| **C — kaam nahi ho saka** | `TypeError` | Operation exist karta hai, is type ke liye defined nahi |
| | `ValueError` | Type sahi, andar ki cheez galat |
| | `IndexError` | Us position pe kuch hai hi nahi. Last valid index = `len - 1` |
| | `KeyError` | Wo chaabi dict me hai hi nahi |
| | `ZeroDivisionError` | Zero se divide define hi nahi hai |
| **D — galti hai hi nahi** | `StopIteration` | Iterator khatam. `next()` raise karta hai; `for` ise andar chupchaap pakad leta hai |
| | `RecursionError` | CPython ka depth guard (~1000 frames). Recursion ka law nahi — implementation ka rule |

⚠ **`IndexError` vs slicing:** slicing **never** raises. `l[5:9]` returns `[]`.
Only **indexing** raises.

---

## 5. THINKING GAPS THIS SESSION — with error-type classification

**All [PREDICT]. Nothing is ledger-eligible, and the session was same-day
anyway, so none of this is a retention finding.**

| # | Gap | Error type | Note |
|---|---|---|---|
| 1 | `t[0] = x` guessed as *"AssignmentError"* | **Knowledge gap (label)** | Mechanism *"trying to mutate an immutable object"* was exactly right. No such error exists; it is `TypeError` |
| 2 | `type((5))` predicted as `tuple` | **Knowledge gap** | The comma-not-parentheses trap. Standard, and the point of the drill |
| 3 | Shallow-copy prediction wrong on **both** printed lines | **Structural flaw** | Treated `[:]` as a deep copy. Missed that `copy[0].append("z")` reaches a **shared inner list**, and dropped the outer `append` from his written answer entirely |
| 4 | `"a".append("z")` called `TypeError` | **Knowledge gap (label)** | It is `AttributeError`. Mechanism (*"a string is immutable"*) right. Twenty minutes after the reference table was delivered — **direct evidence the table wasn't sticking, and the trigger for the hook** |
| 5 | *"immutable object will always be unique"* | **Structural flaw** | **Self-flagged**: *"what am I saying, is that correct??"* Corrected: `(1,2)` and `(1,2)` are equal and are the **same** dict key. Immutability ⇏ uniqueness |
| 6 | `joint_names.index("gripper")` guessed as `AttributeError` | **Knowledge gap (label)** | `index` exists and ran; failure is one station further down. `ValueError` |
| 7 | `joints["gripper"]` guessed as `ValueError` | **NOT A GAP — mentor breach** | `KeyError` had never appeared once in the entire course. Nothing logged |
| 8 | Reached for `zip` + two parallel lists for the dict loop | **Structural flaw** | Fell back to the design the dict had just replaced; `joint`/`angle` no longer existed. `zip` is also untaught. **Recovered correctly on the restated ask** |
| 9 | Design half of *"when is `.get()` wrong"* skipped on first pass | **Depth-before-answer** | **Re-ask recovered it in one line** — *"silent failures"*. Seventh consecutive successful re-ask across S24–S26 |
| 10 | Design half of *"what does the tuple buy you"* skipped | **Depth-before-answer** | Re-asked; he answered the mapping correctly and declared an honest gap on the second half. Answered by the mentor |

**WHAT HE GOT RIGHT, COLD, AND IT IS THE BIGGER LIST:**

- The opening aliasing chain — parameter/argument, alias, mutable object,
  mutating method — **complete and unprompted**.
- **Derived the entire tuple method roster from the type**, including the
  genuinely sophisticated observation that a new-object `append` *could* exist —
  which is correct, and the reason it doesn't is a design answer (`+` already
  does it).
- **Shallow immutability, stated before being asked**: *"tuple is itself
  immutable, but the object inside if it's mutable it should be mutated."*
- **Reasoned out hashability from scratch** — collision, lost value, "someone
  changes the key" — and reached "keys must be immutable" **by himself**.
- Named `.index()`'s cost as **linear** unaided, and correctly identified it as
  DSA territory.
- Both parallel-list defects, both unaided.
- `list` vs `tuple` applied correctly to streaming angles vs URDF limits.
- The `None * 2` `TypeError`, cold.
- The `.get()` design answer: **"silent failures"**.

---

## 6. TEACHING MISTAKES THIS SESSION

**Four defective asks in one session — the worst spec-writing session in the
file's history, and the third consecutive session where spec-writing is the
named mentor failure.**

1. **`sum()` was used in the opening example having never been defined.**
   **NINTH substrate define-before-building breach.** Found by the mentor
   checking `grep` rather than assuming — which is the rule working — but it
   should not have reached the example. Defined in-session.

2. **`KeyError` was demanded by name having never appeared once in the entire
   course** (verified by grep across all four files and every note). **Pushback
   36's upheld half. A straight define-before-use breach**, and the fourth time
   an error label has been asked for before being given.

3. **Dict-key uniqueness was never stated before a `[PREDICT]` depended on it.**
   Part-upheld: it *is* derivable (`[]` must return one value), but the
   derivation should have been flagged, not slid past.

4. **"Given you have `[]`"** — meaning the bracket operator — was read as *"you
   have a list"*, and sent him to the wrong answer. **Ambiguous notation in a
   drill ask.**

5. **The cost question was unanswerable as worded**: *"what does it have to do
   with 10,000 entries, and roughly how much work is that?"* He said plainly
   *"I don't understand both the questions actually what you are trying to get
   out of me."* Restated as *"does it jump straight there or check one at a
   time, and how many comparisons if the match is last?"* — **answered
   correctly and immediately.** The question was the defect, not the student.

6. **⚠ THE STRUCTURAL ONE, AND IT IS THE SESSION'S REAL FINDING.** He asked:
   *"all your questions look to me like you are asking things without teaching,
   it's daunting — is it my fault of thinking or your fault?"*
   **Audited honestly and mostly UPHELD:**
   - **Density.** Almost every turn was a question. The correct ratio is *teach
     a piece with code and output → one question on it.* The session ran
     predict → predict → predict.
   - **Four defective asks** (items 1–5 above) meant a real share of the
     difficulty was unanswerable questions, not hard material.
   - **The tag was declared but its MEANING was not.** Some `[PREDICT]`s are
     derivable from what is on screen; some are genuine guesses where being
     wrong is the point. **From the student's side those are indistinguishable,
     and they must not be.** This is the S18 rule-1 finding — *"if the student
     cannot distinguish a comprehension check from a test, the instrument is not
     being declared clearly enough"* — recurring one level up.
   - **NOT upheld:** `[PREDICT]` asking before teaching is the instrument
     working as designed and is never ledgered.
   **THE COMMITTED FIX: every `[PREDICT]` states up front whether it is
   "derivable from what's on screen" or "a genuine guess — wrong is fine".**

7. **A table was handed over where a hook was needed.** The error chain was
   delivered as a decision table; twenty minutes later he mislabelled
   `AttributeError` as `TypeError`, and then diagnosed the cause himself:
   *"maybe it's not sticking in my mind."* **The file has known since S25 that
   arbitrary labels need HOOKS, not explanations, and a table is an
   explanation.** Rebuilt as the four-station hook (§3).

---

## 7. PUSHBACKS — 38 raised, 37 upheld or part-upheld

| # | Challenge | Verdict |
|---|---|---|
| 35 | *"I don't understand both the questions, what are you trying to get out of me"* (the linear-cost ask) | **UPHELD** — mentor wording. Restated, answered immediately |
| 36 | *"you didn't tell me if one dictionary can have two same keys, and you are straight asking the questions, that's not fair"* | **UPHELD.** Two defects on audit: uniqueness never stated (part — it is derivable), and `KeyError` never taught **anywhere in the course** (full breach, found by the mentor while auditing his challenge) |
| 37 | *"your question was not properly asked, I thought you said you have `[]` list"* | **UPHELD** — ambiguous notation |
| 38 | *"you are asking things without teaching, it's daunting — is it my fault or yours?"* | **PART-UPHELD** — density, four defective asks and undeclared PREDICT-kind are mentor-side; PREDICT-before-teaching itself is the instrument working |

**⚠ NOTE THE SHAPE OF 38. It is not a complaint about difficulty — it is a
request for a diagnosis, offered with his own fault as the first hypothesis.**
That is the ninth instance of him auditing the teaching system itself, and the
first time he has asked for the attribution to be *decided* rather than asserting
it. **The honest split was given: mostly mine.**

---

## 8. WHAT WAS NOT DONE

- **No drill file written.** No `drills/s26_*.py` exists. The session ran
  entirely on live code and prediction. **Nothing from today can promote without
  one.**
- **The four hook tests (`pass`, loop `else`, ternary, associativity) were
  correctly DEFERRED** — same-day, so they would have measured echo.
- **`set`, `when-to-use-which`, comprehensions, `zip`, f-strings, nested
  structures, `reversed()` — all still owed inside 1.8.**
- **Dict is only ~⅔ taught:** deletion (`del`, `.pop()`), insertion ordering,
  and dict comprehensions are untouched.

---

## 9. REFERENCE CHECKLIST — name · what it does · the trap

| Name | What it does | THE TRAP |
|---|---|---|
| `tuple` | Immutable ordered sequence; indexable, iterable | Immutability is **shallow** — a mutable object inside can still be mutated |
| the comma | **Makes** the tuple | `(5)` is an `int`. `(5,)` is a tuple. Parens are grouping, not construction |
| `t.count` / `t.index` | The **only** two tuple methods; both report | Anything that would change it cannot exist. Derive from the type |
| unpacking | `low, high = t` binds items to names left-to-right | Count mismatch ⇒ **`ValueError`**, not `TypeError` — type is fine, count is wrong |
| multiple return | `return a, b` builds **one tuple** | A function never returns more than one object |
| `sum(iterable)` | Totals an iterable of numbers; returns a new value | Does not mutate. **Defined S26 — ninth substrate breach** |
| shallow copy | `l[:]` copies the **outer** container and its **references** | Nested mutables are **shared**. Only bites when the container holds mutables |
| `dict` | key → value; `[]` takes a **key**; no scan | Keys are unique — assigning an existing key **overwrites**, never duplicates |
| hashable | Key's hash must be stable, so key must be immutable | Error says **`unhashable type`**, not "immutable". Immutability ⇏ uniqueness |
| `d[k]` | Lookup; raises on missing | **`KeyError`** — the key is what broke |
| `d.get(k)` | Lookup, never raises; `None` if absent | **Moves the crash away from the cause.** Use `[]` when a missing key is a bug |
| `d.get(k, default)` | Fallback instead of `None` | Only safe when absence is genuinely expected |
| `in` on a dict | Tests **keys**, not values | Not values. Not pairs |
| `for k in d` | Walks the **keys** | Then `d[k]` does the lookup a **second** time — use `.items()` |
| `.keys()`/`.values()`/`.items()` | Keys / values / `(key, value)` **tuples** | `.items()` is tuple unpacking in disguise |
| `AttributeError` | Name after the dot is not on the object | vs `TypeError`: the operation exists but the type refuses it |
| `KeyError` | The key is not in the dict | vs `IndexError` (position) vs `ValueError` (value) — station 4's three siblings |
| **NAAM→DOT→TYPE→CHEEZ** | The four-station error hook | Station 4 splits three ways: **jagah = Index, chaabi = Key, cheez = Value** |

---

## 10. WHAT'S NEXT — Session 27

1. **Cold, later-day, all deferred from S26:** the four hooks (`pass`, loop
   `else`, ternary, **associativity ALONE**), plus `list()`, `break`,
   indexing/slicing, `traceback`.
2. **NEW to the queue, first cold test:** the **four-station hook**,
   `AttributeError`, `KeyError`, tuple mechanics, shallow copy, hashability.
3. **Finish dict:** deletion, ordering, then **set**, then when-to-use-which.
4. **A DRILL FILE — non-negotiable.** S26 produced no evidence artefact.
5. Still owed in 1.8: comprehensions (**gate is open**), `zip`, f-strings,
   nested structures, `reversed()`.
6. **How did the Saturday 22 Aug cold build block go?**
