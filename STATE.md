# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 33 (for Claude):
#   1. Read RULES.md fully (**v5 — unchanged in S32**), then this file fully.
#      No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S32 ran Thu 27 Aug 2026, evening, and
#      finished ~00:15 on Fri 28. Ask the gap. He did NOT name a return date.
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY and that is
#      deliberate — do not invent a candidate to fill it.**
#   4. ⚠⚠ **IF THIS IS THE LAST SESSION OF AUGUST, IT IS THE GAUNTLET AND THE
#      GAUNTLET IS SACRED.** Realistically Sat 30 or Sun 31 Aug. Load ARCHIVE.md
#      and master/ at START if so. Pure mixed recall, no new material, carrying
#      the strict-legend audit listed under CARRY FORWARD. **Say at the S33 open
#      which kind of session it is — do not discover it halfway through.**
#   5. ⚠ **THE S32 MENTOR FAILURE: DEFINE-BEFORE-USE, NINTH OCCURRENCE.** A
#      [RECALL] on format-spec alignment was written as `f"{name:<10}{angle:>8.1f}"`
#      — and `<` / `>` had NEVER been taught. He caught it (*"I havent seen these
#      before"*). Worse than the breach: **the arrows ANNOUNCE THE ANSWER**, so a
#      pass would have been recorded that he had not earned. **Same defect class as
#      the S30 planted boundary. CHECK EVERY SYMBOL IN A RECALL SNIPPET AGAINST
#      WHAT WAS ACTUALLY TAUGHT — grep the notes, do not trust memory.**
#   6. ⚠ **THE STUDENT OPENED S32 SAYING HE FEELS HE IS FORGETTING THINGS, and
#      that revision must not eat the session.** The answer given, and it held up
#      all night: **mechanisms hold, LABELS drop** — so retrieval is the cheap
#      operation (60 seconds) and re-teaching is the expensive one. **Keep the
#      cold asks SHORT and MIXED INTO the material rather than run as a block.
#      Do not let S33 become a revision session; he will disengage.**
#   7. ⚠ **S27 RULE held clean in S32 — both raising snippets got their error
#      named by him first.** Keep building raising snippets in.
#   8. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES EVERY TEST FILE. Never ask him to.** Held clean in S32.
#   9. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Fired TWICE in
#      S32 — one "done" with no write at all, one save with a byte-identical
#      file. Both caught by mtime + size, nothing logged against him.
#  10. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 32, Thursday 27 Aug 2026 (evening → 00:15 Fri 28).
# Next: Session 33 — **probably the AUGUST GAUNTLET.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S32 yield: FOUR LEDGER PROMOTIONS (all cold, all later-day) and ONE
  CURRICULUM STATUS MOVE (1.8 nested data structures [ ] → [~]).**
  `drills/s31_shrug.py` finished 17/17.
- **Position: 1.1–1.7 closed. 1.8 open (~95%). 1.9–1.13 remain, ~4½ wk.**
- **1.8 REMAINING: `copy.deepcopy` (next, ~15 min — it was announced to him as
  the next block), `reversed()`, common patterns/pitfalls. Then 1.8 CLOSES.**
- **AUGUST GAUNTLET: last session of August. SACRED.** See header item 4.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date.
  Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 FULLY CLOSED.** `builds/block_01_joint_clamp/` — 19/19.
  ⚠ **`LOG.md` STILL NOT WRITTEN. FOURTH SKIP. For block 02 it is step ONE,
  before any code.**
- **NEXT BUILD BLOCK: the re-test queue SCRIPT** — settled since S21, still
  unbuilt, this file is 75+ rows past its own trigger. That is block 02.
- Current Layer: 1. Current Topic: **1.8 — `copy.deepcopy` next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING PARKED. Do not manufacture a candidate.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- ⚠ Considered and **NOT** parked in S32: a rule requiring every RECALL snippet
  to be symbol-audited against the notes before firing. **It is not a new rule —
  it is DEFINE BEFORE USE, ninth occurrence. Fix the behaviour, not the rulebook.**

## WHERE WE LEFT OFF

### SESSION 33 STARTS HERE — exact resume point

S32 ran Thu 27 Aug evening into Fri 28 and closed at his call — *"lets close
here"* — offered as a stopping point, not proposed.

Run in this order:

1. **INTERVAL GATE, then DECLARE THE SESSION KIND** (gauntlet or normal —
   header item 4). No rule decision owed.

2. ⚠ **FORMAT-SPEC ALIGNMENT — CLEAN COLD RE-ASK, NO ARROWS ANYWHERE.**
   Held [~] in S32 because the instrument was defective (see header item 5).
   Ask it on the DEFAULT form only: `f"{name:10}{angle:8.1f}"`. **TEXT HUGS
   LEFT, NUMBERS HUG RIGHT.** The *why* — right-aligning makes place value and
   decimal points stack so you compare magnitudes down a column without reading
   digits — **was TAUGHT in S32 and is therefore not ledger-eligible until S34.**
   Fourth session this row has been live. Close it.

3. ⚠ **`list()` — RE-ASK, SHORT GAP.** S32: `list(box)` twice on an exhausted
   iterator. First line `[1,2,3]` right; second he said **`[None]`**, it is `[]`.
   **Mechanism cold and correct** (exhausted, forward-only); the VALUE wrong.
   Rated 7. Seven sessions overdue before S32; do not let it slide again.

4. ⚠⚠ **NEW WATCH AREA AND IT IS THE MOST INTERESTING FINDING OF S32:
   `None` IS NOT THE SAME AS NOTHING, and he conflated them TWICE in one
   session on unrelated mechanisms** — (a) *"`.pop` by default doesn't hand back
   anything... by default it should be returning `None`"*; (b) *"so `None` in the
   second list"* for `list()` on a spent iterator. **`None` is an OBJECT and
   occupies a slot (`len([None]) == 1`); nothing is the absence of a slot
   (`len([]) == 0`).** Test it directly and cold: `del` hands back nothing vs a
   bare `return` hands back `None`; `[]` vs `[None]`; `d.pop(k, None)` vs
   `d.pop(k)`. **This is a knowledge-STRUCTURE gap, not a label gap — different
   from everything else in this file.**

5. ⚠ **`del` vs `.pop()` vs `.clear()` — RE-ASK COLD, TAUGHT S32.** He asked for
   it himself mid-drill. His model was wrong in a *smart* way: he had `.pop(k)`
   returning nothing and the DEFAULT ARGUMENT creating the return value —
   over-generalising the in-place-mutators-return-`None` tell he owns.
   **The fix taught: `.pop(k)` ALWAYS hands back the value; the default is a
   fallback for ABSENCE only. `del` is a STATEMENT and hands back nothing.**
   NOT promotable — taught this session. Cold ask S33.

6. ⚠ **`SyntaxError` + STATION 0 — MISSED AGAIN, AND IT IS NOW A NAMED PATTERN.**
   `print(del d["shoulder"])` → he said **`TypeError`**, rated 6. **Identical to
   his S27 miss on `print(if n > 10: "high")` — same shape, same wrong label,
   five sessions apart.** Taught: a `TypeError` is a RUNTIME verdict, so the line
   must be grammatical first; the traceback carries NO frames because there was
   never a running program. ⚠ **BUT SEE THE STRENGTHS ENTRY — Station 0 then
   fired UNPROMPTED TWICE within the hour.** Fire `SyntaxError` cold in S33.

7. **THE SMALL COLD SET, fired mixed, NOT as a block** (header item 6):
   - **`while` mechanics — NOT touched since S23. SIX sessions overdue.**
   - HASHABILITY; set order instability; `{}` is an empty dict.
   - `.keys()`/`.values()` as VIEWS supporting set operations.
   - unpacking count-mismatch ⇒ `ValueError`; the `count`/`index` roster.
   - when-to-use-which (**THE ASK QUESTION** — he could not produce it in S27).
   - `AttributeError`, `subscriptable`, the FULL four-station hook by name.
   - ⚠ Build a raising snippet in. S30, S31 and S32 all did.

8. **THEN THE 1.8 TAIL:** `copy.deepcopy` (announced to him as next),
   `reversed()`, common patterns and pitfalls. **Then 1.8 CLOSES.**

**Standing turn rules: FRAME FIRST; SPEC gives exact interfaces and exact
expected values, IN A FILE IN THE REPO, with a mechanical check per acceptance
condition (boundary cases live in the TESTS); short messages, one teaching idea
per turn, asks near the top; doubt gate before every new subsection;
depth-before-answer — traces never optional, five checks on every drill,
boundary values first. Tag every block and CHECK THE TAG IS RIGHT. Give the
verdict after the rating. Do not propose ending the session.**

**CARRY FORWARD:**
- **August gauntlet: SACRED.** Carries: strict-legend audit of every [x] —
  every BUNDLED S16 promotion; the 1.6 spoken Feynman recall; the S22
  short-gap promotions; the eight S23; the eleven S25; the eight S27; the S29
  `zip`; the eight S30 (clean later-day but all from ONE sitting — spread them);
  the four S31; **and the four S32 promotions.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~] — **and item 4 above is now
  the reason they matter more than their row suggests.**
- **`str` immutability is still an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `import`, `abs()`, and
  **NEW S32: `print()` — he said it "takes in a string"; it takes ANY object
  and calls `str()` on it.**
- ⚠ **THE FIVE CHECKS WERE NOT REPORTED AGAIN — THIRD SESSION RUNNING** (S30,
  S31, S32). They would have caught the missing `return` in `drop_limit` before
  pytest did. **Stop asking for them at the end of a drill; ask for them as the
  gate on saying "done".**

Every teaching block shows full runnable source alongside output.
Session 33 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt — it
is the designated build block 02.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[x] PROMOTED S32, 7/10 — direction CORRECT and cold after being stated INVERTED in S30. ⚠ His second half was CIRCULAR ("if the user wants an error he picks that column"); sharpened to *is absence a legitimate state of the world, or are my assumptions already broken?*** | **short gap — ~2 Sep** |
| **`.get()` vs `[]`** | **`[]` when missing is a BUG; `.get()` when absence is EXPECTED. ⚠ `.get()` with no default MOVES THE CRASH AWAY FROM THE CAUSE** | **[x] PROMOTED S32 — both tools written cold first try in `drills/s31_shrug.py`, no guards, plus the rule stated correctly** | **gauntlet, then ~5 Sep** |
| **`remove` vs `discard` (sets)** | **same job; `remove` raises `KeyError` when absent, `discard` shrugs. An item IS its own chaabi** | **[x] PROMOTED S32 — written cold, both correct first attempt. Taught S27, NEVER tested until now** | **gauntlet, then ~5 Sep** |
| **tuple immutability** | **item assignment on a tuple ⇒ `TypeError`. Immutability has NO error of its own; it arrives as `TypeError`** | **[x] PROMOTED S32, 5/10, COLD — S31 had the mechanism cold and the LABEL aided; S32 he produced the label unaided by walking Station 0 → Station 3 out loud** | **⚠ rated 5 ⇒ SHORT GAP, ~1 Sep** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE — ALWAYS, default or not; `.clear()` → `None`, leaves `{}`** | **[~] ⚠ S32: he asked for it himself and had it WRONG — default argument believed to create the return value. TAUGHT S32, not promotable** | **S33 cold** |
| **⚠ `None` IS NOT NOTHING** | **`None` is an OBJECT and fills a slot: `len([None]) == 1`. Nothing is the absence of a slot: `len([]) == 0`** | **[~] ⚠⚠ NEW S32 — conflated TWICE in one session on unrelated mechanisms. KNOWLEDGE-STRUCTURE gap, not a label gap** | **S33 cold, PRIORITY** |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration` ⇒ `[]`, not `[None]`** | **[~] ⚠ S32 asked at last after seven sessions: mechanism COLD and correct, VALUE wrong (`[None]`). Rated 7** | **S33, SHORT GAP** |
| **constructors** | **`dict()`/`list()`/`set()`/`tuple()` BUILD A NEW CONTAINER from an iterable — not a type conversion. Copying the PAIRS, not the things they point at, is *why* it comes out shallow** | **[~] NEW S32 — he called `dict(config)` "explicit type conversion"** | **S33** |
| **slicing / SHALLOW COPY** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]`, `list(l)`, `l.copy()` all copy the OUTER container, references SHARED. Shallow = ONE level deep** | **[~] ⚠ S32: he DERIVED the entire mechanism UNPROMPTED off S24 aliasing, before it was taught, then TRANSFERRED it to `dict()` — but a value slip (forgot to apply his own `99`) and it was same-session. NOT promotable** | **S33 cold — deepcopy is the vehicle** |
| **format spec — ALIGNMENT** | **⚠ TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points stack and you can compare magnitudes without reading digits** | **[~] ⚠ S32 HELD, INSTRUMENT DEFECTIVE — the snippet used untaught `<`/`>` which announce the answer. Pushback 54, upheld, mentor's fault. The *why* was taught S32** | **S33 cold, NO ARROWS** |
| **`<` `>` `^` in a format spec** | **force left / right / centre — they OVERRIDE the type default** | **[~] NEW S32, taught after the breach** | **S34** |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran. ⚠ NO FRAMES IN THE TRACEBACK, because there was never a running program** | **[~] ⚠⚠ S32 MISS — `print(del d[k])` labelled `TypeError`, rated 6. IDENTICAL to the S27 miss five sessions earlier. NAMED PATTERN** | **S33 cold, PRIORITY** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] ⚠ S32: he said *"I forgot the hook"* and then RAN IT CORRECTLY, TWICE, unprompted — including on unseen syntax. USE is not RECALL: hold [~] and ask the hook BY NAME** | **S33 cold, full hook by name** |
| **`while` vs `for`** | **condition re-checked vs walking an iterable** | **[x]-grade S23. ⚠ NOT touched S27–S32** | **~10 Sep** |
| **single return value** | **`return a, b` builds ONE tuple; a function never hands back more than one object** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **THE COMMA MAKES THE TUPLE** | **not the parentheses. `(1)` is an `int`; `1, 2` is a tuple** | **[x] S31, cold, 8/10** | **gauntlet, then ~9 Sep** |
| **f-string — THE THREE STEPS** | **evaluate the expression → call `str()` on it → splice it in** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **format spec — width + precision** | **`{v:8.1f}`. ⚠ THE NUMBER IS TOTAL FIELD WIDTH** | **[x] S31, 10/10 — and he restated *total width* correctly again unprompted in S32** | **gauntlet, then ~10 Sep** |
| **DRY / one copy of a decision** | **if a rule is written in four places you will change three of them and miss one** | **[~] S31 — applied correctly and fast, but taught same session** | **S33 — later-day ask** |
| **`set()` / `\|` `&` `-`** | **`set()` is the ONLY empty set. Union / intersection / difference all build a NEW set ⇒ EXPRESSIONS. `-` is NOT symmetric** | **[~] S30 SUPPORTING: `set(a) & set(b)` written cold. Never asked** | **S33 cold** |
| **`sum()`** | **totals an iterable; returns a new value; `sum([])` is `0`** | **[~] S30 SUPPORTING, written cold** | **S33** |
| **`abs()`** | **distance from zero, sign discarded** | **[~] ⚠ USED UNPROMPTED IN S30 AND STILL NEVER TAUGHT** | **S33 — define it properly** |
| **`print()`** | **⚠ takes ANY object and calls `str()` on it — NOT "a string"** | **[~] NEW S32 — he said it takes a string. Level-1 audit item** | **S33** |
| tuple roster | `count` and `index` ONLY | [~] S26 | **S33 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds. S30 discharged the ORDERING and `.items()` thirds; S32 discharged the raise/shrug thirds** | **S33 cold** |
| **set (unit)** | **a dict with the values thrown away. Unique, unordered, hashable** | **[~] S27. ORDER INSTABILITY and `{}`-is-a-dict never asked; `discard`/`remove` discharged S32** | **S33 cold** |
| **hashable** | **hash must be STABLE ⇒ key must be immutable** | **[~] S26/S27, untested** | **S33 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?"** | **[~] S27. ⚠ He could not produce the ASK question** | **S33** |
| **unpacking** | **two names on the left take apart the tuple on the right** | **[x] core PROMOTED S30. ⚠ COUNT-MISMATCH ⇒ `ValueError` half NEVER asked** | **the ValueError half, S33** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[x] `.items()` S30. ⚠ `.keys()`/`.values()` NOT asked** | **`.keys()` view + set ops still owed** |
| `AttributeError` | the name after the DOT is not on the object | **[~] passed cold S27, 6/10. One clean pass promotes** | **S33** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S33 cold** |
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`** | **[x] S30, 16/16 cold, 8/10** | **gauntlet, then ~8 Sep** |
| **comprehension execution order** | **iterable → variable → gate → expression. WRITTEN ORDER ≠ EXECUTION ORDER** | **[x] S30, 8/10** | **gauntlet, then ~8 Sep** |
| **the filter as a GATE** | **`if` runs BEFORE the expression** | **[x] S30 — mechanism unprompted** | **~8 Sep** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. The BRACES and the COLON** | **[x] S30, written cold** | **gauntlet, then ~8 Sep** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting does NOT move a key. ⚠ ORDERED ≠ SORTED** | **[x] S30, all three parts cold** | **gauntlet, then ~8 Sep** |
| **`KeyError` vs `IndexError`** | **⚠ THE BRACKETS DON'T DECIDE THE ERROR — THE CONTAINER DOES** | **[x] S30, 7/10** | **gauntlet, then ~8 Sep** |
| **`zip`** | **pairs parallel ITERABLES; each pass yields a TUPLE** | **[x] S29, 8/10. ⚠ SHORT-GAP** | **gauntlet, then ~7 Sep** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST; exhausted ⇒ `[]`, no error** | **[~] S28, untested S29–S32** | **S33 cold** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[x] S31** | **~9 Sep** |
| **comprehension scope** | **its variable does not exist afterwards ⇒ `NameError`. ⚠ A FOOTNOTE** | **[~] S28** | **low priority** |
| **when NOT to use a comprehension** | **it BUILDS A CONTAINER. If the expression DOES rather than PRODUCES, you wanted a loop** | **[~] S28, untested** | **S33** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] S28** | **with 1.9** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | **[x] S18, re-passed S27/S28/S32** | **~5 Sep** |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | **[x] S26 — ⚠ S32: he used it unprompted to derive shallow copy. Strongest evidence yet** | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. HIS OWN TEST: can it go inside `print(...)`?** | **[x] S27 — ⚠ S32 the test was reused to prove `del` is a statement. The highest-earning row in the file** | **~1 Sep** |
| **precedence / associativity** | **rank between operators / direction within a rank** | **[x] S27** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | **[x] S16, S23 — ⚠ S32: "forward only state" stated cold** | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION. `list()` is what CATCHES it** | **[x] S25, reinforced S28/S32** | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`. ⚠ S32: chained subscripting `d[k][i]` read left-to-right** | **[x] S30** | **~8 Sep** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18, S28 | ~10 Sep |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] S27, `drills/s27_flow.py`, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else` / ternary** | **runs only without `break` / `A if C else B` is an EXPRESSION** | **[x] S27** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument / parameter vs argument** | **`name=value` in the CALL / name in the `def` vs what you pass** | **[x] kwarg S27, 7/10. ⚠ parameter-vs-argument labels still [~]** | **S33** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating. **TYPE FIRST. ⚠ S32: he ran it BACKWARDS on `.pop` — the exact failure the one-directionality warns about** | **[x] S25 — ⚠ re-test the DIRECTION** | **S33** |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | [x] S25 | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | [~] 3/6 cold S24 | **S33** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell / closure four layers | one-slot box; name → function → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | **[~] ⚠ S32 — his `drop_limit` returns `None` for absent and he wrote it correctly, but see the `None`-is-not-nothing row** | **S33** |
| THE FIVE CHECKS | "Boundary pe khaali ek bahar mila" — `bahar` = outside what you ASSUMED, sign AND type | **[x] S25 — ⚠ NOT REPORTED S30, S31, S32** | ~1 Sep |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[~] ⚠ not exercised in S32 — the drill had no boundary in it** | **S33 — boundary in the TESTS ONLY** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14/S27/S28 | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24; **aliasing used unprompted S32** | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | **[~] ⚠ PRIORITY S33 — see the `None`-is-not-nothing finding** |
| Type conversion traps | owed | **[~] due ~1 Sep — and he called a constructor a "type conversion" in S32** |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 + S27 + S28 | **[x] — ⚠ S32 ran the tell BACKWARDS on `.pop`; re-test the direction** |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13/S26/S27; S30 first-draft guards | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD; S28 comprehensions; **S32 exhaustion stated cold** | **[x]** |
| Exceptions are signals | S18 pass; S28 `StopIteration` caught | [x] ~10 Sep |
| Traceback: each line = one live frame | S27 cold 8/10; **S32 the no-frames case on `SyntaxError`** | [x] — gauntlet, then ~15 Sep |
| **`while` mechanics; nested loops; found-flag** | **NOT tested S27–S32** | **[~] S33 — SIX sessions overdue** |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, 20/20 | [x] — gauntlet, then ~15 Sep |
| Mutable/immutable discriminator | S18/S24/S26/S27 | [x] type half; tell half [~] **S33** |
| Closure definition + application; cell causation | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes; **S33** |
| Recursion | S20 same-day | [~] ~16 Sep |
| Five checks | S25 5/5 COLD. **NOT REPORTED S30, S31, S32** | [x] — **gauntlet, re-test with TYPE and BOUNDARY specifically** |
| **`global` / `*args`/`**kwargs`** | **S22 10/10 and 8/10; S29 build block used all four forms cold** | **[x] CONFIRMED — use freely** |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| **COMPREHENSIONS (list + dict)** | **S30 — 16/16 cold, mechanism cold, 8/10** | **[x] — gauntlet, then ~8 Sep** |
| **CONTAINERS AS CODE** | **S30 19/19 cold; ⚠ `.get`/`.pop` defaults AIDED then. S32: `drills/s31_shrug.py` 17/17, ALL SIX TOOLS COLD, no guards** | **[x] — the tool half CLOSED** |
| **DICT: ordering + `.items()`** | **S30 BOTH PROMOTED COLD** | **[x] — ~8 Sep** |
| **f-strings + format spec** | **S31 promoted; ⚠ ALIGNMENT half still owed a clean ask** | **[x] ticked — alignment half S33, NO ARROWS** |
| **TUPLE: the comma / immutability** | **S31 comma; S32 immutability COLD, label unaided** | **[x] BOTH — immutability re-tests ~1 Sep** |
| **RAISE-VS-SHRUG (all three pairs)** | **S32: `drills/s31_shrug.py` 17/17 cold + the choosing rule stated correctly, 7/10** | **[x] PROMOTED — ~2 Sep** |
| **Four-station hook + Station 0** | **S32: RUN correctly twice unprompted, but he said he had forgotten it and `SyntaxError` was still missed** | **[~] — S33, ask the hook BY NAME** |
| **NESTED STRUCTURES + SHALLOW COPY** | **S32 taught; mechanism DERIVED UNPROMPTED, transferred to `dict()`; same-session** | **[~] — S33 cold, deepcopy is the vehicle** |
| **DRY / one copy of a decision** | **S31 applied fast and correctly; taught same session** | **[~] — later-day ask, S33** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **NEW AND IT IS THE SESSION'S BEST FINDING — `None` IS NOT NOTHING.**
  Two conflations in one night on unrelated mechanisms (`.pop`'s default; `[]`
  vs `[None]`). **This is NOT the Term Retention pattern.** Everything else in
  this file is *mechanism intact, label lost*; this is a mechanism he does not
  have — a missing distinction between an object that occupies a slot and the
  absence of a slot. **Treat it as new material, not as revision.**
- ⚠ **HE OPENED THE SESSION WITH A SELF-DIAGNOSIS: *"I feel like I have started
  forgetting things, but we can't just waste time revising, we need to learn new
  content as well."*** Both halves are correct and the file agrees with both.
  The answer that worked: **the forgetting is real but it is LABELS, not
  machinery — S31's tuple immutability had the whole mechanism and no name.
  Retrieval costs 60 seconds; re-teaching costs a session.** He accepted it and
  the night ran ~50/50 old/new without complaint. **Reuse this framing.**
- ⚠ **STATION 0 FIRED UNPROMPTED, TWICE, WITHIN AN HOUR OF BEING MISSED.** On
  tuple item assignment: *"is the syntax correct, yes, ok then can we do the `.`
  for this datatype, now so type error"* — and again on the unseen `<`/`>`
  snippet, where checking the grammar first was the correct instinct even though
  the conclusion was wrong. **He prefaced both with "I forgot the hook".** The
  hook has stopped being recited and started being used, which is the goal —
  but USE IS NOT RECALL, so the row stays [~] until he can name the stations.
- ⚠ **THE MENTOR FAILURE: DEFINE-BEFORE-USE, NINTH OCCURRENCE, and this one had
  teeth.** `<` and `>` appeared in a ledger-eligible [RECALL] having never been
  taught — **and they announce the answer to the very question being asked.**
  He caught it (pushback 54). The instrument was scrapped and the row held.
  **The check that was skipped is cheap: grep the notes for every symbol in a
  recall snippet before firing it.**
- ⚠ **HE DERIVED SHALLOW COPY BEFORE IT WAS TAUGHT, OFF S24 ALIASING, AND THEN
  TRANSFERRED IT TO A CONTAINER IT HAD NOT BEEN SHOWN IN** (`dict(config)`).
  Same shape as the S29 `zip` moment. **Transfer to an unseen case is the
  strongest evidence this course produces; both times it came from a [PREDICT],
  which cannot promote. Consider whether the gauntlet should ask these cold.**
- ⚠ **A NAMED REPEAT: `SyntaxError` labelled `TypeError`, exactly as in S27.**
  Five sessions apart, same shape (a statement placed where a value belongs).
  Not lazy thinking — Station 0 simply is not the first thing he reaches for
  when the snippet *looks* like a normal call.
- ⚠ **CONFIDENCE CALIBRATION — good, and honestly low where it should be.**
  5 on `.pop` (wrong), 6 on `SyntaxError` (wrong), 5 on tuple immutability
  (right), 7 on the raise/shrug rule (right but circular), 7 on `list()` (half
  right). **Every ≤6 rating sat on something genuinely shaky. Use them.**
- ⚠ **CIRCULAR ANSWERS AS A NEW SHAPE.** *"If the user wants it to raise, he
  chooses the raise column"* restates the choice instead of grounding it. He
  does this when he owns the behaviour but has never had to justify it. **The
  fix that worked: ask what the choice BUYS, in his own domain** — the shrug
  handing back a ±180° range for a misspelled joint so the clamp clamps nothing
  and the arm moves.
- ⚠ **CHANNEL — the unsaved-buffer artefact fired TWICE** (one "done" with no
  write, one save of a byte-identical file). mtime and size caught both; nothing
  logged against him. **Keep checking before every read.**
- ⚠ **THE FIVE CHECKS: THIRD SESSION UNREPORTED.** The missing `return` in
  `drop_limit` and `must_drop` is exactly what check 2 exists to catch.
  **Change the ask: the five checks are the GATE on saying "done", not a
  postscript to it.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** Audit list grows: `len()`,
  `range()` as an object, `.append()` vs `+`, `import`, `abs()`, **`print()`**.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 54 raised, 53 upheld or
  part-upheld.** S32 raised ONE — (54) *"I havent seen these before"* on `<`/`>`
  in a recall snippet. **Upheld in full.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read (1.9);
  .pyc (1.10); GIL (1.13); concurrency (post-Layer 1); certifications; GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **PEP 709 / how comprehension scope is actually implemented** — Level 3, 1.13.
- **`reversed()`** — still owed in 1.8.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **`copy.deepcopy` and the `copy` module** — ⚠ **ANNOUNCED TO HIM AS THE NEXT
  BLOCK at the S32 close. It is owed, ~15 minutes, and it is the natural opener
  if S33 is not the gauntlet.**
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 is the course target; collisions and
  resizing are DSA, master Layer 8.
- **HASH RANDOMISATION** — per-process seed. Park to 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0.
- **DRY as a named principle, and "extract a function"** — one line, later.

---
