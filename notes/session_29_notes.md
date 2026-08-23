# SESSION 29 NOTES — Sunday 23 August 2026
## COLD BUILD BLOCK 01 — joint-limit clamp, multiple joints

---

## SELF-TEST (do this cold before reading anything below)

1. `zip(a, b)` — what does it pair, and what does each pass hand you?
2. `for k in d:` where `d` is a dict — what is `k`? What would `d.items()`
   have given you instead?
3. Why does `zip(angles, limits)` put the FIRST angle with the FIRST joint?
   Three facts hold that up. Name all three.
4. A function opens `result = {}`, never fills it, and returns it. What does
   the caller get, and why is that worse than returning `None`?
5. The same rule is written out in four functions. You change three. What does
   pytest say?
6. `f"{name:10s}"` and `f"{value:8.1f}"` — what is the number, and which way
   does each one hug?

---

## WHAT THIS SESSION WAS

Not a teaching session. A **measurement**. The build block is not a curriculum
item — it exists to find out what you can build with the scaffold removed.

**Result: 13/13 pytest, cold, no AI, no autocomplete. All three levels plus
the stretch.**

Two of the four conditions were not met, and that is on the mentor: the timer
was abandoned and `LOG.md` was never written, because the spec had to be
rewritten four times before it was usable. So the block yields a correctness
number and no process record.

---

## FULL TEACHING

### 1. The design hole this block was built around

```python
def clamp_joints(*angles, **limits):
    ...
```

`*angles` collects positional arguments into a **tuple**: `(120, -10, 90)`.
Anonymous — the numbers arrive with no names attached.

`**limits` collects keyword arguments into a **dict**:
`{"shoulder": (-90,90), "elbow": (0,145), "wrist": (-180,180)}`.
Named — but the names are on the *limits*, not on the angles.

**Nothing in that signature pairs an angle with a joint.** That is the whole
problem, and it is why S27 and S28 were deliberately steered away from
`*args`/`**kwargs`.

### 2. Your solution, and why it works

```python
for angle_value, limits_key in zip(angles, limits):
```

Three separate facts hold this line up. All three are load-bearing:

**(a) A dict iterated bare yields its KEYS.**

```python
d = {"shoulder": (-90, 90), "elbow": (0, 145)}
for k in d:
    print(k)
```
```
shoulder
elbow
```

Not the values. Not the pairs. `d.items()` is what gives you `(key, value)`
tuples; `d.values()` gives the values. Bare `for k in d` gives keys.

**(b) Dict keys hold INSERTION order.**

The order the caller wrote the keyword arguments in is the order `limits`
iterates in. `shoulder` was written first, so `shoulder` comes out first.
⚠ **ORDERED ≠ SORTED.** They are not alphabetised; they are in the order they
first went in. A set has no such guarantee and no first element — which is the
contrast you drew yourself.

**(c) `zip` pairs ITERABLES positionally, and yields a TUPLE per pass.**

```python
list(zip((120, -10, 90), {"shoulder": 1, "elbow": 2, "wrist": 3}))
```
```
[(120, 'shoulder'), (-10, 'elbow'), (90, 'wrist')]
```

**Language fix issued this session:** `zip` pairs **iterables**, not "lists".
Your own line passes it a **tuple** and a **dict** — neither is a list. Saying
"lists" would predict that your code shouldn't run.

Each pass yields a tuple, which is why `for a, b in zip(...)` can unpack into
two names.

### 3. `zip` truncates, silently (S28, and it did real work here)

```python
clamp_joints(120, -10, 90, 30, shoulder=(-90,90), elbow=(0,145), wrist=(-180,180))
```

Four angles, three joints. `zip` stops at the **shortest** — no error, no
warning. The `30` is dropped. Your code prints a warning first, which is a
deliberate third choice: not `raise`, not a silent shrug.

⚠ **You never wrote the one line in `LOG.md` saying why.** The deciding
question stands for S30: is an angle with no limits a **BUG in the caller** or
an **EXPECTED case**? For a safety clamp on real hardware, argue it out.

### 4. The dead return

```python
def report(*angles, **limits):
    clamped_joint_angles = {}      # created
    for ...:
        print(...)                 # only ever prints
    return clamped_joint_angles    # still empty
```

`safe = report(...)` gets `{}`.

**Why this is worse than returning `None`:** your own S25 tell — a function
returning `None` is a signal, and code downstream tends to blow up on it fast.
`{}` is not a signal. It is a **plausible-looking empty result**. It is falsy,
it iterates zero times, and nothing complains. The failure travels.

You diagnosed the cause yourself: the function was copied from `clamp_joints`
and never rewired.

### 5. The finding underneath — duplication, and why the green tests lied

The clamp rule — *below low → low, above high → high, otherwise unchanged* —
is written out in full **four times** in 46 lines: lines 2–5, 13–18, 26–31,
40–45.

Now change the spec: exactly-on-a-limit must count as clamped. You update
`clamp_one`, `clamp_all`, `clamp_joints`. You forget `report`.

```
clamp_joints(...)  says shoulder WAS clamped
report(...)        prints  shoulder : 90.0 -> 90.0  ok
```

**pytest says `13 passed`.** Green. Every test.

Because `report` was never tested. **Green tests do not mean the code is
correct — they mean the things you tested pass.** Duplication is the mechanism
by which the untested copy quietly stops matching the tested one. On a real
arm, `report` is the log someone reads during an incident review, and it now
disagrees with what the hardware was actually sent.

**Your fix, and it is right: one function owns the rule; everyone else calls
it.** Not done yet — it carries to S30.

### 6. Format specs, applied correctly and cold

```python
print(f"{limits_key:10s} : {float(angle_value):8.1f} -> {float(low):8.1f} CLAMPED")
```
```
shoulder   :    120.0 ->     90.0 CLAMPED
elbow      :    -10.0 ->      0.0 CLAMPED
wrist      :     90.0 ->     90.0 ok
```

The number is **TOTAL FIELD WIDTH**, not padding added on. `10s` = ten
characters wide in total. **Text hugs LEFT, numbers hug RIGHT** — which is
exactly why the decimal points line up in that middle column. You applied both
facts on the first run, the day after learning them.

⚠ **One thing you wrote without knowing it was version-gated:**

```python
f"...,{"angles" if len(angles)>len(limits) else "joint_limits"} will be discarded"
```

Double quotes **inside** a double-quoted f-string. That is a `SyntaxError` on
Python 3.11 and earlier. It is legal only from **3.12 (PEP 701)**, and you are
on 3.12.3. It runs on your machine and would break on an older interpreter.
Not a mistake — just a thing to know you did.

---

## THINKING GAPS THIS SESSION (with error-type classification)

1. **Skipped the failure-mode question, gave the fix instead.**
   *Type: Lazy thinking — depth-before-answer, his own named weakness.*
   Asked what happens when three of four copies get updated, he answered with
   the remedy. Recovered on the re-ask. **Fourteenth straight recovery.**

2. **Answered in five-checks vocabulary instead of the question asked.**
   *Type: Structural — DESIGN-SWITCHING, the S27 watch area, purest instance
   yet.* Asked what the **caller sees**, he answered *"failure mode will be
   Boundary... bahar"* — substituting a question answerable in owned vocabulary
   for the one asked. Recovered when the question was re-issued unchanged and
   narrowed. **Fifteenth straight.**

3. **Third mechanism fact only on the re-ask.** Dict-iteration-yields-keys was
   not offered until the question was re-put. *Type: Knowledge gap, mild — he
   had it, he did not reach for it.*

4. **Copy-paste left a dead return in shipped code.** *Type: Structural — new
   watch area.* The diagnosis was his own and immediate; the gap is that
   nothing in his process caught it before he called the work done.

5. **`LOG.md` never written.** *Type: Channel/instruction — the request was
   prose in the middle of a document, and prose instructions get skipped.
   Mentor's problem to fix, not his.*

**NOT logged as gaps:** the pytest uncertainty (correctly flagged as untaught),
and the stale markdown preview (channel artefact).

---

## TEACHING MISTAKES THIS SESSION

**The worst mentor session in this file. One failure, committed four times.**

1. **THE SPEC WAS WRITTEN FOUR TIMES BEFORE IT WAS USABLE.** v1: no exercise
   at all. v2: five levels in pure prose, not one number. v3: concrete numbers,
   still no signature. v4: exact signatures and exact expected values — and he
   started immediately.
   **Root cause: protecting a puzzle at the student's expense, and re-deriving
   the same wrong answer three times without checking the premise.** The
   premise — that giving the signature gives away the problem — was false. The
   design hole lived in the function **body**. He proved it within the hour.
   **Cost: half the session, the timer, the process log, and all teaching
   time.** Three pushbacks, escalating to *"lets call this off"*, all upheld.

2. **THE SPEC REQUIRED HIM TO WRITE PYTEST TESTS HE HAS NEVER BEEN TAUGHT TO
   WRITE.** Ninth define-before-building breach; same shape as S18's
   `d.clear()`. STATE.md:363 said pytest is not scheduled in Layer 0.
   **He caught it before writing a line.** Remedy: the mentor wrote the
   13-test suite, verified it against a throwaway stub, deleted the stub.
   **Standing from now on: the mentor writes every test file.**

3. **The dict-iteration confidence question bolted two facts into one clause.**
   He said he did not understand it — correctly. Re-phrased, then dropped.
   That rating is still owed and it is the only thing between dict insertion
   ordering and [x].

**Rule candidate parked for his ruling: SPEC BEFORE PUZZLE.** A spec states the
exact interface and the exact expected values; only the solution is withheld.
A block that does not run measures strictly less than a block that runs with
help. No rule adopted this session; RULES.md stays at v4.

---

## REFERENCE CHECKLIST

| Name | What it does | The trap |
|---|---|---|
| `*args` | collects extra positional arguments into a **tuple** | they arrive **anonymous** — no names attached |
| `**kwargs` | collects keyword arguments into a **dict** | the names are on the kwargs, not on the positional args |
| `*seq` at a call site | **unpacks** a sequence into separate arguments | the mirror of collecting; same symbol, opposite direction |
| `zip(a, b)` | pairs **iterables** positionally; yields a **tuple** per pass | truncates to the **shortest**, silently. Exhausted → `[]`, no error |
| `for k in d` | yields the dict's **KEYS** | not values, not pairs — `.items()` is what gives pairs |
| dict insertion order | keys stay in first-insertion order | **ORDERED ≠ SORTED.** Sets guarantee nothing |
| `{name:10s}` | field is **10 chars total** | it is total width, not padding added |
| `{v:8.1f}` | 8 wide, 1 decimal | **text hugs left, numbers hug right** — that is why points align |
| nested same-type quotes in an f-string | legal from **3.12** (PEP 701) | `SyntaxError` on 3.11 and earlier |
| returning an unfilled `{}` | hands back a plausible-looking empty result | worse than `None` — it does not look like a failure |
| duplicated logic | four copies of one rule | the **untested** copy drifts and the suite stays green |

---

## WHAT'S COMING NEXT (S30)

1. The parked rule decision — **SPEC BEFORE PUZZLE**. Your ruling.
2. **The comprehensions drill.** Deferred twice now, and both times the file's
   fault, not yours. First teaching thing that happens.
3. The refactor you proposed — one function owns the clamp rule.
4. The three-session backlog: tuple, dict, set, shallow copy, unpacking,
   `list()`, `.get()`, `.items()`, raise-vs-shrug, when-to-use-which.
5. Then the 1.8 tail — nested structures → shallow copy, `reversed()`,
   `copy.deepcopy` — and **1.8 closes.**
