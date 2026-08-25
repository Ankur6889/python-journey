# Session 31 — Notes
**Tuesday 25 August 2026, evening (~1 hour). Layer 0 / Python Core.**
Topics: the block-01 refactor (one copy of a decision); f-strings and the
format spec; `return` builds one tuple; the comma makes the tuple; tuple
immutability and the `TypeError` it arrives as.

---

## 0. SELF-TEST — do this BEFORE reading anything below

No notes, no editor, no running it. Write your answers down first.

1. `f"{safe}"` — what are the three things Python does, in order?
2. In `f"{value:8.2f}"`, what does the `8` mean? What does `.2` mean?
3. In `f"{name:10s} {value:8.2f}"`, which edge of its field does `name` sit
   against? Which edge does `value` sit against?
4. How many values can a `return` statement hand back?
5. Which of these are tuples: `(1, 2)` · `1, 2` · `(1)` · `()` · `(1,)`
6. `limits = (-90, 90)` then `limits[0] = -45`. Name the error. Then say which
   station of the four-station hook you used to get there.
7. You have `d = {"shoulder": (-90, 90)}` and you want the limits for
   `"gripper"`, where a missing joint is **expected and fine**. Write the line.
   Now write the line for the case where a missing joint is a **bug**.
8. Same dict. Remove `"gripper"` and get its value back, where absence is
   expected. Then the version where absence is a bug.
9. `active = {"shoulder", "elbow"}`. Remove `"gripper"` without crashing. Then
   the version that crashes.
10. If a rule is written out in four places in a file, what goes wrong the day
    the rule changes?

Answers: §1 (Q1–3), §2 (Q4–6), §3 (Q7–9), §4 (Q10).

---

## 1. FULL TEACHING — f-strings and the format spec

### 1.1 What an f-string actually does

The `f` prefix turns a string literal into an instruction. Without it, `{safe}`
is six literal characters. With it, Python does **three things, in this order**:

1. **Evaluate** whatever is inside the braces. It is an *expression*, not just a
   name — a call, a lookup, arithmetic, a comparison all work.
2. **Convert the result to a string** by calling `str()` on it.
3. **Splice** that string into the surrounding text.

Step 2 is the one people skip, and it is the reason the whole thing is useful.
An f-string always produces a `str`, whatever you put in the braces:

```python
print(f"{[1, 2, 3]}")
print(type(f"{145}"))
```
```
[1, 2, 3]
<class 'str'>
```

The list went in; a string came out. That conversion is what saves you from the
`TypeError` you would get from `"limit: " + 145`.

### 1.2 The format spec — everything after the colon

```python
print(f"{'elbow':10s}|")
print(f"{145.0:8.1f}|")
```
```
elbow     |
   145.0|
```

Two numbers, two different jobs:

* **The number before the dot is the TOTAL FIELD WIDTH.** `10s` means the whole
  field is ten characters wide — not ten characters *added*. `elbow` is five
  characters, so five spaces pad it out to ten.
* **The number after the dot is the precision** — `.1f` is one digit after the
  decimal point.

If the value is wider than the field, the field loses. Nothing is truncated:

```python
print(f"{'shoulder_yaw':10s}|")
```
```
shoulder_yaw|
```

### 1.3 ⚠ ALIGNMENT — the fact that goes wrong

**Text hugs the LEFT of its field. Numbers hug the RIGHT.**

```python
print(f"{'elbow':10s}:{145.0:8.1f}")
print(f"{'wrist':10s}:{-5.25:8.1f}")
```
```
elbow     :   145.0
wrist     :    -5.2
```

The joint names all start at the same column; the numbers all *end* at the same
column, which is why the decimal points line up. That is not a coincidence and
it is not something the f-string is guessing — it is the default for each type,
and it is the default *because* it is what you almost always want: labels read
left-to-right, numbers compare digit-by-digit from the right.

You can override it with `<`, `>`, `^` — but the point of learning the default
is that you rarely need to.

---

## 2. FULL TEACHING — tuples: the comma, and immutability

### 2.1 A function hands back exactly one object

```python
def span(low, high):
    return (low, high, abs(low - high))

result = span(0, 145)
print(result)
print(type(result))
print(len(result))
```
```
(0, 145, 145)
<class 'tuple'>
3
```

`return` gives back **one value, always**. `return a, b, c` does not return
three things — it **builds a tuple** and returns that one tuple. Everything you
have ever seen that "returns two values" is doing this.

### 2.2 ⚠ THE COMMA MAKES THE TUPLE, NOT THE PARENTHESES

```python
a = (1, 2)
b = 1, 2
c = (1)
d = (1,)
print(type(a), type(b), type(c), type(d))
```
```
<class 'tuple'> <class 'tuple'> <class 'int'> <class 'tuple'>
```

`a` and `b` are the same thing. `c` is just the integer `1` with brackets round
it — those parentheses are *grouping*, exactly as in `(2 + 3) * 4`. `d` is a
one-element tuple, and the lonely trailing comma is doing all the work.

The one place parentheses are genuinely required is where a bare comma would be
ambiguous — inside a function call, `f((1, 2))` passes one tuple, `f(1, 2)`
passes two arguments.

### 2.3 Immutability, and the error it arrives as

```python
limits = (-90, 90)
limits[0] = -45
```
```
Traceback (most recent call last):
  File "t.py", line 2, in <module>
    limits[0] = -45
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
```

⚠ **Immutability has no error of its own. It arrives as `TypeError`** — and
that is derivable rather than memorisable. Run the four-station hook:

| Station | Question | This crash |
|---|---|---|
| 0 | Did it run at all? | Yes — the grammar is fine |
| 1 | NAAM — is a name missing? | No, `limits` exists |
| 2 | DOT — is the thing after a `.` missing? | No dot involved |
| 3 | **TYPE — is this operation defined for this type?** | **← stops here** |
| 4 | CHEEZ — jagah / chaabi / cheez | not reached |

Item assignment is simply not an operation tuples have. The *type* is what
broke, so the label is `TypeError`. **You do not have to remember this one. You
have to remember the hook.**

---

## 3. THE DRILL ISSUED FOR NEXT SESSION — raise vs shrug

`drills/s31_shrug.py`, six functions in three pairs. Each pair does one job
twice: once for a caller who **expects** the thing to be missing, once for a
caller for whom missing is a **bug**.

| Job | Absence is EXPECTED → shrug | Absence is a BUG → raise |
|---|---|---|
| read a dict value | `d.get(k, default)` | `d[k]` |
| remove a dict entry | `d.pop(k, default)` | `d.pop(k)` / `del d[k]` |
| remove a set item | `s.discard(x)` | `s.remove(x)` |

**THE DESIGN RULE, and it is the only part worth memorising:** you are not
choosing by temperament, you are choosing by **what the caller has promised**.
If the key must be there and it isn't, something upstream is already broken and
you want the crash **at the cause**, loudly. If the key genuinely might not be
there, a crash is noise and you want a default.

⚠ **Why the drill bans `if`, `in`, `else` and `try`:** in S30 you produced
completely correct shrugging behaviour by hand, `x if k in d else default`, and
passed 19/19. The *concept* was never in doubt. What was gone were the two API
names that implement it. A green test suite could not tell the difference, so
the constraint has to.

---

## 4. FULL TEACHING — one copy of a decision

`clamp.py` began the session with the clamp rule — *below low → low, above high
→ high, otherwise unchanged* — written out in **four** separate places.

Everything worked. 13/13 green. So what is the problem?

**The problem is the next change.** Suppose the rule gains a case: an angle
exactly on a limit must now be logged. You now have to find four blocks and edit
four blocks. Not "might miss one" — **will** miss one, and the one you miss will
be the one with no test covering it. That is not a hypothetical: `report()` had
been silently returning an empty dict for two sessions precisely because nothing
tested it.

The fix is the least glamorous move in programming: **one place decides, and
everything else asks that place.**

```python
def clamp_one(angle, low, high):
    if angle < low:
        angle = low
    elif angle > high:
        angle = high
    return angle


def clamp_all(low, high, *angles):
    out = []
    for a in angles:
        out.append(clamp_one(a, low, high))
    return tuple(out)
```

⚠ **THE SECOND-ORDER VERSION OF THE SAME MISTAKE, which you found yourself.**
Having removed the duplicated *rule*, the first draft of `report` called
`clamp_one` **three times per joint per pass** — once for the dict, once for the
printed value, once inside the `CLAMPED`/`ok` decision. Same value, computed
three times. One is necessary.

```python
for angle_value, joint in zip(angles, limits):
    safe = clamp_one(angle_value, limits[joint][0], limits[joint][1])
    clamped[joint] = safe
    print(f"{joint:10s} : {angle_value:8.1f} -> {safe:8.1f} "
          f"{'CLAMPED' if safe != angle_value else 'ok'}")
```

Compute once, name it, use the name. The name also documents what the value *is*.

---

## 5. THINKING GAPS THIS SESSION (with error-type classification)

| # | Gap | Error type | Detail and resolution |
|---|---|---|---|
| 1 | Could not produce the label `TypeError` for tuple item assignment | **Knowledge gap — LABEL ONLY** | The entire mechanism was stated correctly and the gap was **declared, not guessed**. Derived correctly from the four-station hook on one prompt. Mechanism cold, label aided ⇒ **no promotion**, re-test S32. This is the Term Retention diagnosis in its purest recorded form: the machinery is intact, the arbitrary name is gone. |
| 2 | Format-spec alignment stated **inverted** — "string on the right, numbers on the left" | **Lazy thinking → SELF-CORRECTED** | ⚠ **He repaired it unprompted, before any evidence was shown and with no re-ask** — a first for this file. The row still promoted (correctness promotes); the alignment half was given a **short** re-test gap instead. Interval adjusted, not the promotion. |
| 3 | Answered "how many times is it clamped" (3, exact) but skipped "how many were necessary" | **Depth-before-answer** | The nineteenth and twentieth firings of this pattern this term; both recovered on a re-ask with nothing re-taught. **The re-ask is the intervention.** |
| 4 | The `str()` step of the f-string omitted on first attempt | **Depth-before-answer** | Gave "computes the expression and puts the value there" — steps 1 and 3. One narrowing question ("the f-string always produces one type — what forces the value to change?") produced it immediately. |
| 5 | The five checks were asked for and not reported — again | **Structural, and it is now a pattern** | Second consecutive session. It is in the brief as a numbered step and still does not happen. Ask for them **as a message**, not as a line in a brief. |
| 6 | `LOG.md` not written — fourth skip | **Structural — MENTOR-SIDE** | Prose failed in S29; a numbered step failed in S31. The instruction is not the problem; its position is. Block 02 puts it first, before any code. |

**STRENGTHS, recorded with the same rigour:**
- **The unprompted self-repair (gap 2).** Fifteen sessions of tracking this
  failure mode; first time it was caught in flight by him.
- **Honest-gap declaration (gap 1)** — *"I can't come up with the error type"*
  rather than a guess, with correct machinery stated around the hole.
- **He proposed the redundant-call fix himself and asked for a check before
  answering the question about it** — *"before I answer is this ok"*. Correct
  order, and it is the depth-before-answer countermeasure being self-administered.
- **Four cold promotions in a one-hour session after a full day at the office.**

---

## 6. TEACHING MISTAKES THIS SESSION (mentor-side)

1. ⚠⚠ **SPEC BEFORE PUZZLE BREACHED — one day after it was adopted, and in the
   same shape as the S29 failure it was written to prevent.** The refactor spec
   was issued **in chat only**; when he asked where the instructions were, the
   brief file written was **abstract** ("the clamp decision appears exactly
   once") with no concrete finish line. Two pushbacks, both upheld.
   **THE FIX, and it is now standing: the spec is a FILE, and every acceptance
   condition gets a mechanical check the student can run himself.** The version
   that worked split the job in two, quoted the four repeated blocks side by
   side, gave exact expected values, listed what he MAY and MAY NOT do, and
   stated the finish line as a count he could perform. He finished in fifteen
   minutes. **Nothing about his capability changed between the two briefs.**
2. **A rating was taken and no verdict returned.** He answered, he rated 8/10,
   and the mentor moved on to building the next drill. Upheld in full. The
   sequence is not optional: **answer → rating → VERDICT → next thing.**
3. **Tool output dumped into the channel.** Writing and verifying his next drill
   is machinery, not teaching. *"you have given some random output what is
   happening"* — a fair question, and the answer is that he should never have
   had to ask it. **Tool work is silent.**
4. **A turn spent on a question that could record nothing.** The
   redundant-calls re-ask was tagged [TEACH-BACK] — no rating, not
   ledger-eligible — and was fired on code he had already fixed. Part-upheld.
   The correct correction is **not** "ask less"; three of tonight's four
   promotions came from finally asking about code he wrote days ago.
   It is **ask the things that can promote**.

**PUSHBACKS THIS SESSION: 4 raised, 3 upheld in full, 1 part-upheld.
Running total: 53 raised, 52 upheld or part-upheld.**

---

## 7. REFERENCE CHECKLIST — name · what it does · the trap

| Name | What it does | ⚠ The trap |
|---|---|---|
| **f-string** | `f"..."` — evaluate the expression, `str()` it, splice it in | Without the `f` the braces are literal characters. **The `str()` step is the one everyone forgets** — it is why `f"{[1,2]}"` gives you a string |
| **braces hold an EXPRESSION** | calls, lookups, arithmetic, comparisons, even a comprehension | **Never a `for` loop** — a loop is a statement, and only expressions have values to splice |
| **format spec** | everything after the `:` — `{v:8.2f}`, `{n:10s}`, `{i:03d}` | **The number before the dot is TOTAL FIELD WIDTH, not extra spaces.** Too-wide values are never truncated — the field just loses |
| **alignment default** | text hugs **LEFT**, numbers hug **RIGHT** | This is why decimal points line up in a column. It differs **by type**, which is exactly why it is easy to state backwards |
| **`return`** | hands back **exactly one object**, always | `return a, b` is not "two values" — **it builds a tuple**, and that tuple is the one object |
| **the comma makes the tuple** | `1, 2` is a tuple; `(1)` is an `int`; `(1,)` is a one-tuple | The parentheses are **grouping**, not construction. The trailing comma in `(1,)` is doing all the work |
| **tuple immutability** | you cannot rebind an element | **Immutability has no error of its own — it arrives as `TypeError`.** Derive it from Station 3 rather than memorising it |
| **four-station hook** | DID IT RUN? → NAAM → DOT → TYPE → CHEEZ | Station 4: jagah = `IndexError`, chaabi = `KeyError`, cheez = the value. **The brackets never decide the error; the container does** |
| **`.get(k, default)`** | dict read that shrugs when the key is absent | Use `d[k]` when a missing key is a **bug** — you want the crash at the cause, not three functions later |
| **`.pop(k, default)`** | removes and returns; shrugs when absent | `d.pop(k)` raises. `del d[k]` also raises but is a **statement** — it hands back nothing |
| **`.discard(x)` / `.remove(x)`** | set removal: shrug / raise | Same pairing as the two above. **An item in a set is its own key**, so the raising one gives `KeyError` |
| **one copy of a decision** | a rule lives in one place; everything else calls it | Four copies do not fail today — they fail **the day the rule changes**, in the copy with no test on it |
| **compute once, name it** | `safe = clamp_one(...)` then use `safe` | Calling the same function three times with the same arguments is the same duplication one level down, and the name documents the value |

---

## 8. WHAT IS COMING NEXT (Session 32)

1. `drills/s31_shrug.py` — **written, issued, untouched. It is first.**
   `13 failed, 4 passed` right now.
2. Cold re-asks: tuple immutability (the label); format-spec alignment.
3. The container concepts never asked cold: `count`/`index`, hashability, set
   order instability, `{}` is an empty dict, `del`/`.pop()`/`.clear()`,
   when-to-use-which, `list()` as a constructor, `.keys()`/`.values()`.
4. `while` mechanics — **five sessions overdue.**
5. Then the 1.8 tail: **nested data structures** (which is what finally makes
   shallow copy land), `reversed()`, `copy.deepcopy`, patterns and pitfalls —
   **and 1.8 closes.**
6. ⚠ **August gauntlet — Sat 30 / Sun 31 Aug. Sacred. Plus the 31 Aug
   re-baseline arithmetic.**
