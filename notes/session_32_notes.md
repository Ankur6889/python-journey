# SESSION 32 NOTES — Thursday 27 August 2026 (evening → 00:15 Friday 28)
**1.8 Data Structures — raise-vs-shrug closed; nested data structures opened**

---

## 0. SELF-TEST FIRST (close these notes and answer before reading on)

1. `d = {"a": 1}`. What does `d.pop("a")` hand back? What does `del d["a"]` hand back?
2. Why is `print(del d["a"])` a `SyntaxError` and not a `TypeError`?
3. `limits = (0, 145)` then `limits[0] = 10`. Which error, and why that one?
4. You are writing code and a key might be missing. What single question decides whether you use `d[k]` or `d.get(k, default)`?
5. `a = [[1,2],[3,4]]`, `b = a[:]`, `b[0][0] = 99`. What is `a` now? What is `a is b`? What is `a[0] is b[0]`?
6. `box = iter([1,2,3])`. What do the two `print(list(box))` lines show?
7. `len([])` vs `len([None])` — and why is that distinction the point?
8. `f"{name:10}{angle:8.1f}"` — which value hugs the left of its field, which hugs the right, and what does that buy you?

---

## 1. FULL TEACHING

### 1.1 `del` vs `.pop()` — the difference is WHAT YOU GET BACK

Both remove a key. They differ in what they hand you, and that difference decides where each one can legally appear in your code.

```python
d = {"shoulder": (-90, 90), "elbow": (0, 145)}
print(d.pop("elbow"))
print(d)
```
```
(0, 145)
{'shoulder': (-90, 90)}
```

**`.pop(k)` ALWAYS hands back the value. Always — with or without a default.**

The mistake made this session, and it was a *smart* one: believing the optional second argument is what *creates* the return value. It is not.

> **The default is a fallback used ONLY when the key is absent. It does not create the return; it replaces the crash.**

That belief came from over-applying a rule that is genuinely owned — *in-place mutators return `None`* (`.append`, `.sort`, `.clear`). **That tell runs ONE WAY ONLY** (S24): returns `None` ⇒ mutating is true; mutating ⇒ returns `None` is **false**, and `.pop` is the counterexample. It is the counterexample *because handing the item back is the entire point of popping*.

| form | hands back | key absent, no default |
|---|---|---|
| `d.pop(k)` | **the value** | raises `KeyError` |
| `d.pop(k, default)` | the value, or `default` | shrugs |
| `del d[k]` | **nothing at all** | raises `KeyError` |
| `d.clear()` | `None` | — leaves `{}`, same object |

### 1.2 Why `del` cannot go inside `print(...)` — Station 0

```python
d = {"shoulder": (-90, 90)}
print(del d["shoulder"])
```
```
  File "q.py", line 2
    print(del d["shoulder"])
          ^^^
SyntaxError: invalid syntax
```

**`SyntaxError` — not `TypeError`.** The distinction is the first station of the four-station hook:

> **STATION 0 — DID IT RUN AT ALL?**

A `TypeError` is a **runtime verdict**: Python read the line, understood it, built the objects, attempted the operation and refused. To reach that point the line must be **grammatical first**. Here nothing ran — Python could not finish *reading* the line.

**The tell in the traceback itself: there are no frames.** No `line 2, in <module>`, no call stack. Every other traceback in this course has had at least one frame, because a frame means something was executing. A `SyntaxError` traceback has none, because there was never a running program.

And the reason the grammar breaks is the `del`/`.pop` split seen from the other side:

> **`.pop` is an EXPRESSION — it produces a value. `del` is a STATEMENT — it performs an action.** `print(...)` needs a value in its brackets. `x = del d[k]` is impossible for the same reason.

This is the student's own S27 test — *can it go inside `print(...)`?* — used as a decision procedure rather than recited as a fact.

### 1.3 The raise-vs-shrug pairing — ONE design rule, seen three times

| shrugs (absence EXPECTED) | raises (absence is a BUG) |
|---|---|
| `d.get(k, default)` | `d[k]` |
| `d.pop(k, default)` | `d.pop(k)` |
| `s.discard(x)` | `s.remove(x)` |

The rule for choosing, in its non-circular form:

> **Is a missing key a legitimate state of the world, or does it mean my program's assumptions are already broken?**
>
> - Legitimate → **shrug**. An unconfigured joint, an absent optional setting, a key not written yet.
> - Assumptions broken → **raise, deliberately and as early as possible.**

Why "I want an error here" is not a reason: it renames the choice instead of grounding it. The grounding is about *where the failure surfaces*.

```python
low, high = limits.get(joint, (-180, 180))    # shrug
low, high = limits[joint]                     # raise
```

Misspell a joint name in a config. The **shrug** hands back a ±180° range for a joint that does not exist — so the safety clamp clamps *nothing*, nothing crashes, and you find out on the hardware. The **raise** stops you at the config-load line with the bad name in the traceback.

> **Absence you did not plan for is a bug wearing a disguise. Shrugging is what puts the disguise on.**

Note also (S26): `.get()` **with no default** is the worst of both — it moves the crash away from the cause.

### 1.4 Tuple immutability

```python
limits = (0, 145)
limits[0] = 10
```
→ **`TypeError`**

Python is not objecting to the `0` and not objecting to the `10` — both are perfectly good values. It is objecting that **this operation does not exist for this type**. Item assignment is simply not defined for a tuple.

> **Immutability has no error of its own. It always arrives as `TypeError`.**

Route to the label via the hook: *did it run at all?* (yes, the grammar is fine) → *is it a name problem?* (no) → *a dot problem?* (no) → **type**.

### 1.5 Nested data structures

**What it is:** a container whose items are themselves containers.

**Why it exists — the honest version: nothing was added to the language for this.** Containers hold objects. A list *is* an object. A dict *is* an object. Nesting is a **consequence** of a rule you already have, not a feature.

**What it buys you:** real data has shape, and flat containers lose it. Walking two parallel lists with `range(len(...))` means the relationship between them lives in your head rather than in the data. Nesting puts the shape *in* the structure.

```python
limits = {
    "shoulder": [-90, 90],
    "elbow":    [0, 145],
}
print(limits["elbow"])
print(limits["elbow"][1])
```
```
[0, 145]
145
```

Read `limits["elbow"][1]` **left to right, one step at a time**: the first `[]` hands back a list; you then index that list. **No new syntax — the same `[]`, applied twice, because the first one handed back something indexable.**

```python
episodes = [[1, 2, 3], [4, 5], [6]]
print(episodes[1][0])   # 4
print(len(episodes))    # 3  <- counts the OUTER items, not the numbers inside
```

**What is NOT claimed:** nesting is not better. Deep nesting is a smell — two levels is normal, four usually means you wanted a class.

### 1.6 SHALLOW COPY — the trap the unit exists for

```python
a = [[1, 2], [3, 4]]
b = a[:]          # a NEW list, not an alias
b[0][0] = 99
print(a)
print(b)
print(a is b)
print(a[0] is b[0])
```
```
[[99, 2], [3, 4]]
[[99, 2], [3, 4]]
False
True
```

`a is b` → **False**: the outer list really is new. `a[0] is b[0]` → **True**: the inner list was never copied. Both outer lists point at the same one.

> **SHALLOW COPY — "shallow" means it goes ONE level deep.** A new container, filled with *the same object references* the original held. **New box, same contents.**

Same story for dicts, and for the constructor form:

```python
config = {"limits": [-90, 90]}
backup = dict(config)
backup["limits"][0] = 0
print(config)                                   # {'limits': [0, 90]}
print(config["limits"] is backup["limits"])     # True
```

**Why it never bit you before:** for a flat list of numbers or strings a shallow copy is **indistinguishable** from a real copy — immutable items cannot be mutated, so sharing them is invisible. The moment the items are themselves mutable, the sharing becomes visible.

Three shallow forms, all equivalent: `a[:]`, `list(a)`, `a.copy()`. **Prefer `.copy()` — it says what it means.** Dicts are not sliceable, so there `dict(d)` or `d.copy()`.

**Still owed: `copy.deepcopy` — the copy that goes all the way down.**

### 1.7 Constructors are not type conversions

`dict(config)` is a **CONSTRUCTOR CALL**: *build me a new dict out of what I am handing you.* Given a dict it walks the key→value pairs and stores **those same value objects** in a brand-new dict.

> **That is exactly why it comes out shallow — it copied the pairs, not the things the pairs point at.**

Same for `list(...)`, `set(...)`, `tuple(...)`: build a new container from any iterable.

### 1.8 `list()` on a spent iterator — and `None` is not nothing

```python
box = iter([1, 2, 3])
print(list(box))
print(list(box))
print(len(list(box)), len([None]))
```
```
[1, 2, 3]
[]
0 1
```

An iterator is **forward-only**. Once exhausted there is nothing left, so `list()` asks for the next item, receives the `StopIteration` signal on the very first ask, **catches it**, and hands back a list it never put anything into.

> **`[]` has length 0. `[None]` has length 1 — it CONTAINS something, and that something is the object `None`.**

**THE DISTINCTION, and it is the headline of the session:**

> **`None` is an OBJECT. It occupies a slot. "Nothing" is the absence of a slot.**
>
> - `del d[k]` hands back **nothing**. A function with no `return` hands back **`None`**.
> - `d.pop(k, None)` hands back `None` on absence. `d.pop(k)` on a present key hands back the value.
> - `[]` contains nothing. `[None]` contains `None`.

### 1.9 Format-spec alignment — the WHY

```python
rows = [("elbow", 145.0), ("shoulder", 90.0), ("wrist", 7.25), ("base", 180.0)]
for name, angle in rows:
    print(f"{name:10}{angle:8.1f}")
```
```
elbow        145.0
shoulder      90.0
wrist          7.2
base         180.0
```

**Defaults: text hugs LEFT, numbers hug RIGHT.** Nobody asked for either.

The payoff is only visible in a column. Names all start at the same left edge, so the eye scans a straight margin. Numbers right-align, so **place value lines up — units under units, tens under tens, decimal points stacked** — and you can compare magnitudes without reading a single digit. Left-align them and `7.2` and `180.0` start in the same place and the shape tells you nothing.

> **The default matches what you scan the column FOR.** Text you scan by its start; numbers you compare by their size.

**Override operators (new this session):** `<` forces left, `>` forces right, `^` centres.

---

## 2. THE DRILL — `drills/s31_shrug.py`

Six functions, three pairs, **under a constraint banning `if`, `in`, `else` and `try`** below the docstring (enforced by a test). The constraint is the drill: it bans the hand-rolled guard and forces the tool.

His final code, 17/17:

```python
def limit_for(limits, joint):
    return limits.get(joint, (-180, 180))

def must_limit(limits, joint):
    return limits[joint]

def drop_limit(limits, joint):
    return limits.pop(joint, None)

def must_drop(limits, joint):
    return limits.pop(joint)

def retire(active, joint):
    active.discard(joint)
    return active

def must_retire(active, joint):
    active.remove(joint)
    return active
```

**All six tools chosen cold and correctly on the first attempt, with no guards.**
Three fixes were needed: two missing `return`s on the `.pop` pair, and `None`
instead of `(-180, 180)` as `limit_for`'s default.

---

## 3. THINKING GAPS THIS SESSION (with error-type classification)

| # | Gap | Type | Note |
|---|---|---|---|
| 1 | **`None` conflated with "nothing", TWICE** — `.pop`'s default believed to create the return; `[None]` for `list()` on a spent iterator | ⚠ **STRUCTURAL FLAW — a missing distinction, NOT a lost label** | **The most important entry. Every other retention finding in this file is *mechanism intact, label gone*. This is a mechanism he does not have. Teach it as new material, not as revision.** |
| 2 | `print(del d[k])` labelled `TypeError`; it is `SyntaxError` | **Knowledge gap → NAMED PATTERN** | **Identical to the S27 miss (`print(if n > 10: "high")`), five sessions apart. Station 0 is not what he reaches for when a snippet *looks* like a normal call.** |
| 3 | `.pop` believed not to return by default | Structural flaw | **A smart wrong answer**: the in-place-mutators-return-`None` tell run BACKWARDS. The S24 warning that the tell is one-directional exists for exactly this. |
| 4 | Two missing `return`s on `.pop` in the drill | **Lazy thinking** | Taught 20 minutes earlier. **The five checks would have caught it; they were not run.** |
| 5 | `limit_for` default left as `None` | Lazy thinking | The correct value was in his own docstring four lines above. |
| 6 | Shallow-copy prediction: mechanism perfect, final VALUE wrong (forgot to apply his own `99`) | Lazy thinking | The reasoning was flawless; the arithmetic step was skipped. |
| 7 | Raise-vs-shrug rule stated **circularly** on the second half | Structural flaw | Owns the behaviour, has never had to justify it. Fixed by asking what the choice BUYS. |
| 8 | `dict(config)` called "explicit type conversion" | Knowledge gap | It is a constructor call. Corrected. |
| 9 | *"`print` takes in a string"* | Knowledge gap — **Level 1** | Takes any object and calls `str()` on it. Joins the level-1 audit list. |
| 10 | `list()` second line given as `[None]` | See #1 | Mechanism (exhaustion, forward-only) was **cold and correct**. |

**NOT logged as gaps:** the `SyntaxError` guess on the unseen `<`/`>` snippet
(tagged [PREDICT], never ledger-eligible); the *"I belive we havent discussed
why"* on alignment (an honest gap, and he was right); and both unsaved-buffer
incidents (channel artefacts, caught by mtime).

---

## 4. TEACHING MISTAKES THIS SESSION

1. ⚠⚠ **DEFINE-BEFORE-USE, NINTH OCCURRENCE, AND THE INSTRUMENT LEAKED ITS OWN
   ANSWER.** A ledger-eligible [RECALL] on alignment was fired as
   `f"{name:<10}{angle:>8.1f}"` — **`<` and `>` had never been taught.** He
   caught it: *"I havent seen these before."* **Pushback 54, upheld in full.**
   The breach is bad; the leak is worse — `<` means left and `>` means right, so
   the snippet announced the answer to the question it was asking. Had he
   guessed what the arrows meant, a pass would have been recorded that he had
   not earned. **Same defect class as the S30 planted boundary.** The row was
   held at [~] and the instrument scrapped. **The missing check is cheap: grep
   the notes for every symbol in a recall snippet before firing it.**
2. **Verified rather than remembered, and it paid.** Before ruling on the
   pushback, the S31 notes and ARCHIVE were grepped for `<`/`>` — confirming
   that only the *default* alignment had been taught. The S15 stale-file rule
   applied to the course's own history: **look, do not remember.**
3. **The five checks have now been asked for as a postscript three sessions
   running and skipped three times.** That is a mentor-side design failure, not
   a compliance failure. **Change the ask: the five checks are the GATE on
   saying "done".**

---

## 5. REFERENCE CHECKLIST (name — what it does — the trap)

| Name | What it does | The trap |
|---|---|---|
| `d.pop(k)` | removes the key and **hands back its value** | the default does NOT create the return; it replaces the crash. `.pop` is the counterexample to "mutators return `None`" |
| `del d[k]` | removes the key, **hands back nothing** | a STATEMENT, not an expression — cannot go inside `print(...)` or on the right of `=` |
| `d.clear()` | empties the dict, returns `None` | leaves `{}` — empty, not gone, **same object** |
| raise-vs-shrug | one design rule, three pairs | the deciding question is not "do I want an error" — it is **"is absence legitimate, or are my assumptions broken?"** |
| `s.remove` / `s.discard` | same job; `remove` raises, `discard` shrugs | the label is `KeyError`, not a set-specific error — **a set item IS its own chaabi** |
| tuple immutability | item assignment not defined for the type | **immutability has no error of its own; it arrives as `TypeError`** |
| `SyntaxError` | **Station 0** — the grammar broke, nothing ran | **no frames in the traceback**, because there was never a running program. A `TypeError` is a RUNTIME verdict and needs a grammatical line first |
| nested structures | containers holding containers | **not a feature — a consequence.** `len()` counts the OUTER items only |
| chained subscripting | `d[k][i]`, read left to right | no new syntax; the first `[]` handed back something indexable |
| **shallow copy** | new container, **same references inside** | `a[:]`, `list(a)`, `a.copy()`, `dict(d)` are ALL shallow. Invisible for flat immutables — that is why it hides |
| constructors | `list()`/`dict()`/`set()`/`tuple()` build a NEW container from an iterable | **not a type conversion.** Copying the pairs, not what they point at, is *why* it is shallow |
| `list()` on an iterator | drains it; **catches `StopIteration`** | a spent iterator gives `[]`, **not `[None]`** |
| **`None` vs nothing** | `None` is an OBJECT filling a slot | `len([None])` is 1, `len([])` is 0. `del` gives nothing; a bare `return` gives `None` |
| alignment defaults | text LEFT, numbers RIGHT | it differs **by type**, which is why it is easy to state backwards. `<` `>` `^` override |

---

## 6. WHAT'S NEXT

- **`copy.deepcopy`** — the copy that goes all the way down. Announced as the next block, ~15 minutes.
- **`reversed()`**, then **common patterns and pitfalls** — and **1.8 CLOSES.**
- **Cold and owed S33:** format-spec alignment (no arrows anywhere), `list()`, `del`/`.pop`/`.clear`, `SyntaxError`, the four-station hook **by name**, and the `None`-is-not-nothing distinction as a direct test.
- ⚠ **If the next session is the last of August it is the GAUNTLET — pure mixed recall, no new material, carrying the strict-legend audit.**
