# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 34 (for Claude):
#   1. Read RULES.md fully (**v5 — unchanged in S33**), then this file fully.
#      No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S33 ran Fri 28 Aug 16:00 → Sat 29 Aug
#      ~12:00, with a sleep break in the middle. Ask the gap.
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY and that is
#      deliberate — do not invent a candidate to fill it.** Two mentor failures
#      in S33 (define-before-use tenth occurrence; FRAME FIRST breached) are
#      BEHAVIOUR failures on rules that already exist. Fix the behaviour.
#   4. ⚠⚠ **THE AUGUST GAUNTLET IS THE LAST SESSION OF AUGUST AND IT IS
#      SACRED. Only Sun 30 and Mon 31 remain.** He said at the S33 open that he
#      would sit again before 1 Sep, and at the S33 close that he wanted 1.9 as
#      a fresh session. **BOTH CANNOT BE THE LAST SESSION. Ask at the S34 open
#      which this is — gauntlet, or 1.9 — and SAY WHICH BEFORE TEACHING.** If
#      gauntlet: load ARCHIVE.md and master/ at START, pure mixed recall, no new
#      material, carrying the strict-legend audit under CARRY FORWARD.
#   5. ⚠ **MENTOR FAILURE, DEFINE-BEFORE-USE, TENTH OCCURRENCE, SECOND NIGHT
#      RUNNING.** `*` on a sequence (`[[0] * 3] * 3`) was fired inside a
#      [PREDICT] having never been taught. He caught it. **The check is cheap
#      and it was skipped again: GREP THE NOTES FOR EVERY SYMBOL AND EVERY
#      OPERATOR IN A SNIPPET BEFORE FIRING IT.** When it was finally run, the
#      grep took one command and settled it in seconds.
#   6. ⚠ **MENTOR FAILURE, FRAME FIRST (S28 rule), BREACHED.** The
#      when-to-use-which block was fired as three scenarios with no frame; he
#      said TWICE he did not understand the question. The fix that worked was
#      to stop, own it, and state the unit in one sentence
#      (**"what am I going to ASK this container?"**) before any scenario.
#      **Two "I don't understand" replies in a row is not a comprehension
#      signal — it is a frame signal. Stop and frame.**
#   7. ⚠ **THE FIVE CHECKS WERE REPORTED, FIRST TIME SINCE S25.** The change
#      that did it: they were declared THE GATE ON THE WORD "DONE", not a
#      postscript. **Keep issuing them that way in every drill brief.** He gave
#      boundary + `mila` unprompted and needed one push for the other three.
#   8. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES EVERY TEST FILE. Never ask him to.** Held clean in S33.
#   9. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Fired ONCE in
#      S33 and **he caught it himself** before the mentor read anything.
#  10. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 33, Fri 28 Aug 2026 16:00 → Sat 29 Aug ~12:00.
# Next: Session 34 — **1.9, or the AUGUST GAUNTLET. ASK.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S33 yield: SEVEN LEDGER PROMOTIONS, ONE DEMOTION, THREE CURRICULUM TICKS.**
  `drills/s33_copies.py` 25/25 cold, and the five checks reported as the gate.
- **Position: 1.1–1.7 closed. 1.8 at ~98% — FIVE bullets still [~]. 1.9–1.13
  remain, ~4½ wk.**
- ⚠ **1.8 DID NOT CLOSE, AND THE MENTOR SAID IN SESSION THAT IT HAD.** Corrected
  before the close, but the over-claim is logged. **What remains, exactly:**
  - `list` — method roster 3/6 cold since S24; ⚠ **honest gap on `.count()` in
    S33** ("I don't remember this method").
  - `tuple` — taught in full S26, never given a task-first cold pass, no drill.
  - `dict` — `.keys()`/`.values()` as VIEWS supporting set operations NEVER asked.
  - `set` — ORDER INSTABILITY and `{}`-is-a-dict never asked.
  - `when to use which` — properly taught for the FIRST time in S33 (see below);
    cannot promote before S34.
  **All five are cold-ask shaped, not teaching shaped. One focused block closes
  1.8 — put it at the front of the next non-gauntlet session.**
- **AUGUST GAUNTLET: last session of August. SACRED.** See header item 4.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date.
  Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 FULLY CLOSED.** ⚠ **`LOG.md` STILL NOT WRITTEN. FOURTH
  SKIP. For block 02 it is step ONE, before any code.**
- **NEXT BUILD BLOCK: the re-test queue SCRIPT** — settled since S21, still
  unbuilt, this file is 75+ rows past its own trigger. That is block 02.
- Current Layer: 1. Current Topic: **1.8 tail (five cold asks), then 1.9.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING PARKED. Do not manufacture a candidate.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- ⚠ Considered and **NOT** parked in S33: a rule requiring an operator-level
  grep before any snippet. **It is not a new rule — it is DEFINE BEFORE USE,
  substrate included, tenth occurrence. Fix the behaviour, not the rulebook.**

## WHERE WE LEFT OFF

### SESSION 34 STARTS HERE — exact resume point

S33 ran Fri 28 Aug 16:00 into the early hours, broke for sleep, and finished
Sat 29 Aug at midday when he closed it himself. He asked for 1.9 to be a
**fresh session**.

Run in this order:

1. **INTERVAL GATE, then DECLARE THE SESSION KIND** (gauntlet or 1.9 — header
   item 4). No rule decision owed.

2. ⚠⚠ **THE DEMOTION IS THE FIRST THING TO RE-TEST: THE MUTATING TELL.**
   `[x]` → `[~]` in S33. Asked to state the rule he produced *"a method on a
   mutable object mutates the object"* — false — and then **could not produce
   the tell at all** ("I cannot come up with the statement as well").
   **THIRD BREAK OF THIS ROW IN TWO SESSIONS, each in a different direction:**
   S32 had `.pop(k)` returning nothing because it mutates; S33 had `.count()`
   mutating because the object is mutable; S33 then had no statement at all.
   **The re-taught model, in three parts — ask for ALL THREE:**
   (1) **TYPE FIRST** — on an immutable object mutation is not on the table.
   (2) **THE TELL** — returns `None` ⇒ it mutated (nothing else is worth
       returning `None` for).
   (3) **THE DIRECTION IT DOES NOT RUN** — a value coming back tells you
       **NOTHING**; `.pop()` returns the item AND mutates.

3. ⚠ **`reversed()` — RE-ASK, AND IT IS THE SESSION'S SHARPEST FINDING.**
   Taught S33 with full output. Nine hours later, in the drill, he did NOT
   reach for it: he wrote `[steps[-(i+1)] for i in range(len(steps))]` and
   explained *"couldn't use reverse because it mutates the list itself"*.
   **He merged `steps.reverse()` (method, mutates, returns `None`) with
   `reversed(steps)` (built-in, mutates nothing, returns an ITERATOR).** A pure
   name collision over intact machinery. **Ask for the table, both rows.**
   ⚠ And name the habit under it: **`range(len(...))` index bookkeeping,
   already caught in S29 where `zip` removed it.** When he computes indices to
   get at items, there is usually a built-in that hands him the items.

4. ⚠ **`SyntaxError` — NOT FIRED IN S33. STILL OWED, STILL PRIORITY.** It was
   on the S33 plan and the session never reached it. **Named repeat pattern:
   missed in S27 and again in S32, five sessions apart, same shape (a statement
   put where a value belongs). Fire it cold, in a shape he has not seen.**

5. ⚠ **THE FOUR-STATION HOOK BY NAME — NOT FIRED IN S33. STILL OWED.**
   S32 showed USE without RECALL. Ask him to name the stations, in order,
   including Station 0.

6. ⚠ **`del` and `.clear()` — HALF-DISCHARGED ONLY.** S33 got `.pop(k)` right
   unaided (*"returns the removed value, KeyError if the key is missing"*).
   **`del` as a STATEMENT handing back nothing, and `.clear()` → `None`
   leaving `{}`, were never asked.** They pair naturally with `SyntaxError`
   (`print(del d[k])`) — but use a DIFFERENT shape from S32's snippet.

7. ⚠ **CONSTRUCTORS — cold ask owed.** In S33 his first word was still
   *"converts it to a dictionary"*; *"builds a new object from the iterable"*
   only arrived after the mentor pointed at the word. **Row held [~]
   deliberately. It promotes when the right word is his FIRST word.**

8. ⚠ **`when to use which` — TAUGHT PROPERLY FOR THE FIRST TIME IN S33, so a
   cold ask is now legitimate and it has never had one.** THE ASK QUESTION:
   *"WHAT AM I GOING TO ASK THIS CONTAINER?"* → in here? `set`. Value for a
   name? `dict`. Order/position? `list`. Must never change? `tuple`.

9. **THE SMALL COLD SET, fired mixed, NOT as a block:**
   - **`while` mechanics — NOT touched since S23. SEVEN sessions overdue.**
   - HASHABILITY; set order instability; `{}` is an empty dict.
   - `.keys()`/`.values()` as VIEWS supporting set operations.
   - unpacking count-mismatch ⇒ `ValueError`; the `count`/`index` roster
     (⚠ he had an honest gap on `.count()` in S33).
   - `AttributeError`, `subscriptable`.
   - `zip` fails silently — twice.
   - ⚠ Build a raising snippet in. S30–S33 all did.

10. **THEN 1.9 — ERROR HANDLING.** ⚠ **The overdue error-label set IS 1.9's
    substrate** — `SyntaxError`, `AttributeError`, `KeyError`/`IndexError`, the
    four-station hook. **Run the revision INSIDE the new subsection rather than
    ahead of it; this was the S33 plan and it is still the right one.**
    Build `traceback` from the UNCAUGHT-exception trigger (self-rated 3/10 when
    1.9 was scoped).

**Standing turn rules: FRAME FIRST — and if he says "I don't understand the
question" TWICE, that is a frame failure, not a comprehension failure; SPEC
gives exact interfaces and exact expected values, IN A FILE IN THE REPO, with a
mechanical check per acceptance condition (boundary cases live in the TESTS);
short messages, one teaching idea per turn, asks near the top; doubt gate before
every new subsection; depth-before-answer — traces never optional, THE FIVE
CHECKS ARE THE GATE ON THE WORD "DONE", boundary values first. Tag every block
and CHECK THE TAG IS RIGHT. Give the verdict after the rating. Do not propose
ending the session.**

**CARRY FORWARD:**
- **August gauntlet: SACRED.** Carries: strict-legend audit of every [x] —
  every BUNDLED S16 promotion; the 1.6 spoken Feynman recall; the S22
  short-gap promotions; the eight S23; the eleven S25; the eight S27; the S29
  `zip`; the eight S30; the four S31; the four S32; **and the seven S33.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~] — **though the `None`-is-not-
  nothing row that made them urgent CLOSED in S33.**
- **`str` immutability is still an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()` (**he said it
  "takes in a string"; it takes ANY object and calls `str()` on it**).
  ✅ **`import` DISCHARGED S33** — given a one-line Level-2 model (it binds the
  NAME to a module object; the `.` is the one he already owns).
- ⚠ **STYLE, S33, both minor and both worth repeating once:** `import` belongs
  at the TOP of the file, not inside the function; and `i` conventionally means
  an INDEX — `[i for i in angles ...]` should be `[a for a in angles ...]`.

Every teaching block shows full runnable source alongside output.
Session 34 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt — it
is the designated build block 02.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| ⚠⚠ **mutating vs non-mutating — THE TELL** | **(1) TYPE FIRST (2) returns `None` ⇒ it mutated (3) a VALUE back tells you NOTHING — `.pop()` returns the item AND mutates** | **[x] → [~] DEMOTED S33. Could not state the rule at all; before that stated it INVERTED (*"a method on a mutable object mutates the object"*). THIRD break in two sessions, three different directions** | **S34 cold, PRIORITY — ask all three parts** |
| ⚠ **`reversed()` vs `.reverse()`** | **`reversed(x)` is a BUILT-IN returning an ITERATOR, mutates nothing. `x.reverse()` is a METHOD, mutates, returns `None`** | **[~] TAUGHT S33. ⚠ Nine hours later he did not reach for it and gave the method's behaviour as the reason. NAME COLLISION over intact machinery** | **S34 cold, PRIORITY** |
| **`copy.deepcopy`** | **new outer container AND new contents recursively, all the way down. Not "the better copy" — slower, and buys nothing on a flat container of immutables** | **[x] PROMOTED S33 — written cold in `drills/s33_copies.py` from a docstring that never named it; all six independence tests green first run. Rated 7** | **short gap — ~2 Sep** |
| **slicing / SHALLOW COPY** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]`, `list(l)`, `l.copy()` copy the OUTER container, references SHARED. Shallow = ONE level deep** | **[x] PROMOTED S33 — cold on `dict(defaults)` with a nested list: correct value AND both halves (why the inner edit leaks, why the new key does not). Derived unprompted S32** | **~3 Sep** |
| **`*` ON A SEQUENCE** | **repeats the REFERENCE, not the contents. SAFE when the element is immutable, a TRAP when mutable — `[[0]*3]*3` shares one row** | **[~] NEW S33, taught after the breach (pushback 55). He resolved the trap himself off shallow copy and asked the right question — *"but 0 is not mutable"*** | **S34** |
| **MUTATE-WHILE-ITERATING** | **`for` keeps an internal POSITION COUNTER; removing an item slides the next into a slot already passed. DON'T REMOVE — SELECT: `[a for a in angles if a <= 180]`** | **[~] NEW S33 — [PREDICT], so not eligible. ⚠ He predicted the SAFE-LOOKING list correctly and the failing one wrong** | **S34 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?" in here → `set`; value for a name → `dict`; order/position → `list`; never changes → `tuple`** | **[~] ⚠ FRAMED PROPERLY FOR THE FIRST TIME S33 after he twice said he did not understand the question — mentor's FRAME FIRST breach. He had `dict` and `list` right and folded the `set` in** | **S34 cold — first legitimate ask** |
| **set difference `-`** | **`set(a) - set(b)` builds a NEW set ⇒ an EXPRESSION. `-` is NOT symmetric** | **[x] PROMOTED S33 — `missing_joints` written in one line cold. Taught S30, never once tested until now** | **~5 Sep** |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[x] PROMOTED S33 — he read `<=` off the PROMISE before writing, and reported it unprompted as check 1** | **~5 Sep** |
| **THE FIVE CHECKS** | **"Boundary pe khaali ek bahar mila". ⚠ `ek` = smallest NON-EMPTY case, not the number 1. ⚠ `bahar` = TYPE as well as sign** | **[x] — ⚠ REPORTED S33, FIRST TIME SINCE S25, because they were made the GATE on "done". Two halves loose: `ek` given as "the number 1"; `bahar` given as sign only** | **~5 Sep — re-ask `ek` and `bahar` specifically** |
| **format spec — ALIGNMENT** | **TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points stack and you compare magnitudes without reading digits** | **[x] PROMOTED S33, 8/10, cold, NO ARROWS — fourth session live, closed. The *why* was volunteered too but was taught S32** | **~8 Sep** |
| **⚠ `None` IS NOT NOTHING** | **`None` is an OBJECT and fills a slot: `len([None]) == 1`. Nothing is the absence of a slot: `len([]) == 0`** | **[x] PROMOTED S33, 7/10 — `[150, None]` given cold with the mechanism, then `0 1` stated directly. ⚠ A KNOWLEDGE-STRUCTURE gap closed in ONE NIGHT** | **short gap — ~2 Sep** |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration` ⇒ `[]`, not `[None]`** | **[x] PROMOTED S33, 7/10 — value corrected unaided, and he re-derived the reason himself** | **~2 Sep** |
| **constructors** | **`dict()`/`list()`/`set()`/`tuple()` BUILD A NEW CONTAINER from an iterable — not a type conversion. Copying the PAIRS, not the things they point at, is *why* it comes out shallow** | **[~] HELD S33 DELIBERATELY — his first word was still "converts"; "builds a new object" came only after the mentor pointed at the word** | **S34 — promotes when it is his FIRST word** |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran. ⚠ NO FRAMES IN THE TRACEBACK, because there was never a running program** | **[~] ⚠⚠ NOT FIRED IN S33 — session never reached it. NAMED PATTERN: missed S27 and S32, same shape** | **S34 cold, PRIORITY, NEW SHAPE** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] ⚠ NOT FIRED IN S33. S32 showed USE without RECALL** | **S34 cold, full hook by name** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE — ALWAYS; `.clear()` → `None`, leaves `{}`** | **[~] HALF-DISCHARGED S33 — `.pop(k)` stated correctly unaided, including `KeyError` on a missing key. `del` and `.clear()` never asked** | **S34 cold — the other two halves** |
| **`while` vs `for`** | **condition re-checked vs walking an iterable** | **[x]-grade S23. ⚠ NOT touched S27–S33** | **⚠ SEVEN sessions overdue** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[x] `.items()` S30. ⚠ `.keys()`/`.values()` NOT asked — blocks the 1.8 dict bullet** | **S34** |
| **set (unit)** | **a dict with the values thrown away. Unique, unordered, hashable** | **[~] ORDER INSTABILITY and `{}`-is-a-dict never asked — blocks the 1.8 set bullet** | **S34 cold** |
| tuple roster | `count` and `index` ONLY | **[~] ⚠ S33 HONEST GAP on `.count()` — "I don't remember this method"** | **S34 cold** |
| **tuple (unit)** | **immutable ordered sequence; the COMMA makes it; `TypeError` on item assignment** | **[~] taught in full S26, never given a task-first cold pass — blocks the 1.8 tuple bullet** | **S34** |
| **list method roster** | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | **[~] 3/6 cold S24 — blocks the 1.8 list bullet** | **S34** |
| **hashable** | **hash must be STABLE ⇒ key must be immutable** | **[~] S26/S27, untested** | **S34 cold** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST; exhausted ⇒ `[]`, no error** | **[~] S28, untested S29–S33** | **S34 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] passed cold S27, 6/10. One clean pass promotes** | **S34** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S34 cold** |
| **unpacking** | **two names on the left take apart the tuple on the right** | **[x] core PROMOTED S30. ⚠ COUNT-MISMATCH ⇒ `ValueError` half NEVER asked** | **the ValueError half, S34** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[x] S32, 7/10** | **~2 Sep** |
| **`.get()` vs `[]`** | **`[]` when missing is a BUG; `.get()` when absence is EXPECTED. ⚠ `.get()` with no default MOVES THE CRASH AWAY FROM THE CAUSE** | **[x] S32 — and used correctly again in S33's `len(results)` question** | **~5 Sep** |
| **`remove` vs `discard` (sets)** | **same job; `remove` raises `KeyError` when absent, `discard` shrugs** | **[x] S32** | **~5 Sep** |
| **tuple immutability** | **item assignment on a tuple ⇒ `TypeError`. Immutability has NO error of its own; it arrives as `TypeError`** | **[x] S32, 5/10, COLD** | **~1 Sep** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] ordering, `.items()` and raise/shrug thirds all discharged; VIEWS outstanding** | **S34** |
| **single return value** | **`return a, b` builds ONE tuple** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **THE COMMA MAKES THE TUPLE** | **not the parentheses. `(1)` is an `int`; `1, 2` is a tuple** | **[x] S31, cold, 8/10** | **gauntlet, then ~9 Sep** |
| **f-string — THE THREE STEPS** | **evaluate the expression → call `str()` on it → splice it in** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **format spec — width + precision** | **`{v:8.1f}`. ⚠ THE NUMBER IS TOTAL FIELD WIDTH** | **[x] S31, 10/10 — restated correctly again unprompted in S33** | **~10 Sep** |
| **`<` `>` `^` in a format spec** | **force left / right / centre — they OVERRIDE the type default** | **[~] NEW S32, taught after the breach** | **S34** |
| **DRY / one copy of a decision** | **if a rule is written in four places you will change three and miss one** | **[~] S31 — applied correctly and fast, but taught same session** | **S34 — later-day ask** |
| **`set()` / `\|` `&` `-`** | **`set()` is the ONLY empty set. Union / intersection / difference build a NEW set ⇒ EXPRESSIONS** | **[x] the `-` half PROMOTED S33. `\|` and `&` still untested** | **`\|`/`&` S34** |
| **`sum()`** | **totals an iterable; returns a new value; `sum([])` is `0`** | **[~] S30 SUPPORTING, written cold** | **S34** |
| **`abs()`** | **distance from zero, sign discarded** | **[~] ⚠ USED UNPROMPTED IN S30 AND STILL NEVER TAUGHT** | **S34 — define it properly** |
| **`print()`** | **⚠ takes ANY object and calls `str()` on it — NOT "a string"** | **[~] NEW S32. Level-1 audit item** | **S34** |
| **`import`** | **binds the NAME to a MODULE OBJECT; `copy.deepcopy` is the same `.` he already owns. HOW it finds the module is 1.10** | **✅ DISCHARGED S33 — Level-2 model given, and he used `import copy` correctly in the drill** | **1.10** |
| **`_` as a name** | **an ordinary name, used by convention for "I am not going to use this value"** | **[~] NEW S33, one line** | **low priority** |
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`** | **[x] S30, 16/16 cold — used cold twice more in S33** | **~8 Sep** |
| **comprehension execution order** | **iterable → variable → gate → expression. WRITTEN ORDER ≠ EXECUTION ORDER** | **[x] S30, 8/10** | **~8 Sep** |
| **the filter as a GATE** | **`if` runs BEFORE the expression** | **[x] S30** | **~8 Sep** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. The BRACES and the COLON** | **[x] S30** | **~8 Sep** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order. ⚠ ORDERED ≠ SORTED** | **[x] S30** | **~8 Sep** |
| **`KeyError` vs `IndexError`** | **⚠ THE BRACKETS DON'T DECIDE THE ERROR — THE CONTAINER DOES** | **[x] S30, 7/10** | **~8 Sep** |
| **`zip`** | **pairs parallel ITERABLES; each pass yields a TUPLE** | **[x] S29, 8/10** | **gauntlet, then ~7 Sep** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[x] S31** | **~9 Sep** |
| **comprehension scope** | **its variable does not exist afterwards ⇒ `NameError`. ⚠ A FOOTNOTE** | **[~] S28** | **low priority** |
| **when NOT to use a comprehension** | **it BUILDS A CONTAINER. If the expression DOES rather than PRODUCES, you wanted a loop** | **[~] S28, untested** | **S34** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] S28** | **with 1.9** |
| **negative index** | **counts backward from the end; `-1` is last** | **[x] S24 — ⚠ S33 used cold and correctly in `replay_order`** | **~10 Sep** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18, re-passed S27/S28/S32 | ~5 Sep |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | **[x] S26 — the root of the whole S32/S33 copy chain** | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. HIS OWN TEST: can it go inside `print(...)`?** | **[x] S27 — the highest-earning row in the file** | **~1 Sep** |
| **precedence / associativity** | **rank between operators / direction within a rank** | **[x] S27** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | **[x] — ⚠ S33: said "the iterable was empty", SELF-REPAIRED unprompted and named it a saying error not a concept error** | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION. `list()` is what CATCHES it** | **[x] S25, reinforced S28/S32/S33** | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[x] S30** | **~8 Sep** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18, S28 | ~10 Sep |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] S27, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else` / ternary** | **runs only without `break` / `A if C else B` is an EXPRESSION** | **[x] S27** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument / parameter vs argument** | **`name=value` in the CALL / name in the `def` vs what you pass** | **[x] kwarg S27. ⚠ parameter-vs-argument labels still [~]** | **S34** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | **[x] S25 — ⚠ re-test alongside the demoted TELL** | **S34** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell / closure four layers | one-slot box; name → function → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | **[~] — ⚠ the `None`-is-not-nothing row it depended on CLOSED S33** | **S34** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| **NESTED STRUCTURES + SHALLOW COPY + DEEPCOPY** | **S33 `drills/s33_copies.py` 25/25 cold, later-day; independence proven at both levels** | **[x] — CURRICULUM TICKED. ~3 Sep** |
| **COMMON PATTERNS AND PITFALLS (1.8)** | **S33 taught: mutate-while-iterating, `[[0]*3]*3`, container choice** | **[x] TICKED as taught+closed; the three rows themselves are [~] and re-ask S34** |
| **⚠ THE MUTATING TELL** | **S33: stated INVERTED, then could not state it at all** | **[x] → [~] DEMOTED — S34 PRIORITY, all three parts** |
| **`reversed()`** | **S33 taught; nine hours later not reached for, merged with `.reverse()`** | **[~] — S34 PRIORITY** |
| **THE FIVE CHECKS** | **S33 REPORTED as the gate — first time since S25. `ek` and `bahar` both loose** | **[x] — re-ask `ek` and `bahar` specifically, ~5 Sep** |
| **`while` mechanics; nested loops; found-flag** | **NOT tested S27–S33** | **[~] ⚠ SEVEN sessions overdue** |
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14/S27/S28 | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | **[~] — the structural half closed S33** |
| Type conversion traps | owed | **[~] due ~1 Sep — and "converts" is still his first word for a constructor** |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 + S27 + S28 | **[~] — travels with the demoted TELL** |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13/S26/S27 | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD; S32 exhaustion cold; **S33 exhaustion applied to `reversed()` unprompted** | **[x]** |
| Exceptions are signals | S18 pass; S28 `StopIteration` caught | [x] ~10 Sep |
| Traceback: each line = one live frame | S27 cold 8/10 | [x] — gauntlet, then ~15 Sep |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, 20/20 | [x] — gauntlet, then ~15 Sep |
| Mutable/immutable discriminator | S18/S24/S26/S27; **S33 applied correctly to `[0]*3` vs `[[0]*3]*3`** | [x] type half; **tell half DEMOTED — S34** |
| Closure definition + application; cell causation | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes |
| Recursion | S20 same-day | [~] ~16 Sep |
| **`global` / `*args`/`**kwargs`** | **S22 10/10 and 8/10; S29 build block used all four forms cold** | **[x] CONFIRMED — use freely** |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| **COMPREHENSIONS (list + dict)** | **S30 16/16 cold; S33 used cold twice more** | **[x] — ~8 Sep** |
| **CONTAINERS AS CODE** | **S30 19/19; S32 17/17 all six tools cold** | **[x] — the tool half CLOSED** |
| **f-strings + format spec** | **S31 promoted; ALIGNMENT half PROMOTED S33, 8/10** | **[x] BOTH HALVES — ~8 Sep** |
| **TUPLE: the comma / immutability** | **S31 comma; S32 immutability COLD** | **[x] BOTH — ~1 Sep** |
| **RAISE-VS-SHRUG (all three pairs)** | **S32 17/17 cold + the choosing rule** | **[x] — ~2 Sep** |
| **Four-station hook + Station 0** | **S32 RUN correctly twice unprompted; ⚠ NOT ASKED IN S33** | **[~] — S34, ask the hook BY NAME** |
| **DRY / one copy of a decision** | **S31 applied fast; taught same session** | **[~] — later-day ask, S34** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S33 HEADLINE, AND IT IS ABOUT HOW HE LEARNS: A KNOWLEDGE-STRUCTURE
  GAP CLOSED OVERNIGHT.** S32 found that he had no line between an object that
  fills a slot and the absence of a slot. It was named, not drilled. Sixteen
  hours later he produced `[150, None]`, `len` of `0` and `1`, and the
  correction to his own `.pop` model — unaided. **When the gap is STRUCTURAL,
  naming it precisely appears to be enough; he builds the piece himself. That
  is the opposite of the LABEL gaps, which need repetition.** Two different
  failure modes needing two different treatments — file this and use it.
- ⚠⚠ **NAME COLLISIONS ARE A DISTINCT AND NEWLY-EVIDENCED FAILURE MODE.**
  `reversed()` vs `.reverse()` in S33 is the cleanest instance yet: taught nine
  hours earlier with full output, and it lost to a near-identical name over
  machinery he demonstrably owns. **Where two constructs have near-identical
  names, TEACH THEM AS A PAIR IN ONE TABLE or he will merge them.** Related
  prior instances: `sort`/`sorted`, `remove`/`discard`, `iterable`/`iterator`.
- ⚠ **THE MUTATING TELL IS NOW THE MOST BROKEN ROW IN THE FILE** — three
  failures in two sessions, each in a different direction. It is not a label
  problem: he has repeatedly rebuilt it as a TWO-WAY rule. **Teach the
  one-directionality as the headline, not as a caveat.**
- ⚠ **THE FIVE CHECKS FINALLY LANDED, AND THE FIX WAS STRUCTURAL, NOT SOCIAL.**
  Three sessions of asking produced nothing; declaring them the GATE ON THE WORD
  "DONE" produced a report in the very next drill. **When an ask fails
  repeatedly, change WHERE it sits in the workflow, not how loudly it is made.**
- ⚠ **"I DON'T UNDERSTAND THE QUESTION" IS A FRAME SIGNAL.** He said it twice on
  when-to-use-which. The mentor rephrased once (wrong fix) before stopping and
  admitting there had been no frame at all. **Second occurrence of the S19/S20
  shape: the first fix solves the wrong half.**
- ⚠ **HE ASKS THE RIGHT QUESTION MID-DERIVATION.** On `[[0]*3]*3` he stopped
  himself with *"but 0 is not mutable"* — which is precisely the discriminator
  that decides when `* n` is safe. Same shape as the S32 shallow-copy
  derivation. **When he interrupts his own answer with an objection, that
  objection is usually the load-bearing part; let it run.**
- ⚠ **MENTOR: DEFINE-BEFORE-USE, TENTH OCCURRENCE, SECOND NIGHT RUNNING.**
  `*` on a sequence, fired in a [PREDICT], never taught. **The grep that settles
  it takes one command.** Also logged: a [PREDICT] example whose data hid the
  very bug it was meant to expose — recovered by making that the lesson, but it
  was luck, not design. **Choose failing data deliberately.**
- ⚠ **MENTOR: AN OVER-CLAIM ABOUT HIS OWN PROGRESS.** "That closes 1.8" was said
  in session and was false — five bullets remain [~]. Caught at close and
  corrected to his face. **This is the exact class the END-OF-SESSION section
  warns about: an artefact that looks authoritative while being wrong.**
- ⚠ **CONFIDENCE CALIBRATION — steady all session.** 8 on alignment (right), 7
  on `len(results)` (right), 7 on the shallow-copy trace (right), 8 on the five
  checks (right, two halves loose), 7 on the drill (25/25). **No rating below 7
  all session, and nothing below 7 was wrong. The two genuine misses — the tell
  and `reversed()` — he never rated, because he could not produce an answer to
  rate. Watch for that: silence is the new low rating.**
- ⚠ **CHANNEL — the unsaved-buffer artefact fired ONCE and HE caught it**
  (*"sorry I forgot to save"*) before anything was read. Down from four in S30
  and two in S32. Keep checking mtime anyway.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`. ✅ `import` discharged S33.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 55 raised, 54 upheld or
  part-upheld.** S33 raised ONE — (55) *"normally for brackets we use () but
  here we are using [] , this hasn't been taught"* on `[[0] * 3] * 3`.
  **Upheld in full after a grep of every note file.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read (1.9);
  .pyc (1.10); GIL (1.13); concurrency (post-Layer 1); certifications; GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **PEP 709 / how comprehension scope is actually implemented** — Level 3, 1.13.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **`copy.copy()` as the generic shallow form, and the `copy` module's own
  surface** — mentioned only in passing in S33; one line is owed.
- **Why `deepcopy` does not loop forever on a structure containing itself** —
  Level 3, park to 1.13.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 is the course target; collisions and
  resizing are DSA, master Layer 8.
- **HASH RANDOMISATION** — per-process seed. Park to 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0.
- **DRY as a named principle, and "extract a function"** — one line, later.

---
