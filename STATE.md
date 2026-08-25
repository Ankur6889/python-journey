# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 32 (for Claude):
#   1. Read RULES.md fully (**v5 — unchanged in S31**), then this file fully.
#      No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S31 ran Tue 25 Aug 2026 (evening).
#      He said he would return **Thu 27 Aug** — "I have some work to do
#      tomorrow". A Thu session is a clean two-day gap: everything below is
#      ledger-eligible.
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY and that is
#      deliberate — do not invent a candidate to fill it.**
#   4. ⚠⚠ **THE S31 HEADLINE IS A MENTOR FAILURE AND IT IS THE FIRST THING TO
#      FIX: SPEC BEFORE PUZZLE was adopted at the S30 open and BREACHED THE
#      NEXT DAY.** Not by withholding an interface — by issuing the refactor
#      spec **in chat only**, then writing a first brief file that was abstract
#      ("the clamp decision appears exactly once") with no concrete finish
#      line. He raised it TWICE. **THE SPEC GOES IN A FILE IN THE REPO, AND
#      EVERY ACCEPTANCE CONDITION GETS A MECHANICAL WAY TO CHECK IT.**
#   5. ⚠ **DO NOT SPEND HIS TURNS ON NON-LEDGER QUESTIONS.** He objected, and
#      part-upheld: a [TEACH-BACK] fired on code he had *already fixed* can
#      record nothing either way. Application is still not an ask — but ask the
#      things that can actually promote.
#   6. ⚠ **GIVE THE VERDICT. He rated, and the mentor moved on without ruling.**
#      Sequence is fixed: his answer → his rating → THE VERDICT → next thing.
#   7. ⚠ **DO NOT DUMP TOOL OUTPUT AT HIM.** Writing and verifying his next
#      drill should be silent. He asked "what is happening".
#   8. ⚠ **S27 RULE: every snippet that raises gets its error NAMED by him
#      before the traceback is shown.** Fired once in S31 — see item 4 of the
#      resume plan; the mechanism was cold, the LABEL was aided.
#   9. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES EVERY TEST FILE. Never ask him to.** Held clean in S31.
#  10. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held clean in
#      S31 — zero unsaved-buffer firings, down from four in S30.
#  11. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 31, Tuesday 25 Aug 2026 (evening, ~1h).
# Next: Session 32, expected Thu 27 Aug 2026.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S31 yield: ONE CURRICULUM TICK (1.8 f-strings/format spec → [x]) and FOUR
  LEDGER PROMOTIONS, all cold, all later-day. Build block 01 CLOSED for real —
  the refactor is done and 19/19 green.** Short session (~1h, his call).
- **Position: 1.1–1.7 closed. 1.8 open (~93%). 1.9–1.13 remain, ~5 wk.**
- **1.8 REMAINING: nested data structures, common patterns/pitfalls,
  `reversed()`, `copy.deepcopy`.** Nested structures is next and it is the one
  that makes SHALLOW COPY finally land — say that when it opens.
- **AUGUST GAUNTLET: last session of August. SACRED.** With a Thu 27 restart
  that is realistically **Sat 30 or Sun 31 Aug**. Plan it now, do not discover it.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date.
  Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 FULLY CLOSED.** `builds/block_01_joint_clamp/` — 19/19.
  ⚠ **`LOG.md` STILL NOT WRITTEN. FOURTH SKIP.** It was a numbered step in
  `BRIEF_REFACTOR.md` this time and was still skipped. **Stop asking for it as
  homework. For block 02, make it the FIRST step, before any code.**
- **NEXT BUILD BLOCK: the re-test queue SCRIPT** — settled since S21, still
  unbuilt, this file is 75+ rows past its own trigger. That is block 02.
- Current Layer: 1. Current Topic: **1.8 — nested data structures next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING PARKED. Do not manufacture a candidate.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- ⚠ Considered and **NOT** parked in S31: a rule requiring every spec to live in
  a repo file. **It is not a new rule — it is SPEC BEFORE PUZZLE, and adding a
  second rule to enforce the first is governance scope-creep.** Fix the
  behaviour, not the rulebook.

## WHERE WE LEFT OFF

### SESSION 32 STARTS HERE — exact resume point

S31 ran Tue 25 Aug 2026 evening and closed at his call — *"lets close this
session actually, I will do it day after tomorrow, I have some work to do
tomorrow so will pick it up from here."*

Run in this order:

1. **INTERVAL GATE.** No rule decision owed.

2. ⚠ **THE DRILL IS ALREADY WRITTEN, ISSUED AND UNTOUCHED — IT IS THE FIRST
   THING THAT HAPPENS.** `drills/s31_shrug.py` + `tests/test_s31_shrug.py`
   (mentor-written, verified green against a throwaway reference which was then
   deleted). Currently **13 failed, 4 passed**. Six functions, three pairs:
   `limit_for`/`must_limit`, `drop_limit`/`must_drop`, `retire`/`must_retire`.
   **The constraint is the drill:** no `if`, `in`, `else` or `try` below the
   docstring — a test enforces it — which bans the hand-roll he used in S30 and
   forces `.get(k, default)`, `.pop(k, default)`, `discard`/`remove`.
   **This is THE priority item: raise-vs-shrug is the one row where he owns the
   CONCEPT and has lost the TOOL.** Ask the choosing rule AFTER the tests pass.

3. ⚠ **TUPLE IMMUTABILITY — RE-ASK. Held [~] in S31 on purpose.** Given
   `limits = (-90, 90); limits[0] = -45` he gave the mechanism completely and
   correctly and then said *"I can't come up with the error type"* — honest gap,
   not a guess. He then derived `TypeError` from the four-station hook on one
   prompt. **Mechanism cold, LABEL aided ⇒ no promotion.** Re-ask cold.

4. ⚠ **FORMAT-SPEC ALIGNMENT — RE-ASK, SHORT GAP.** Promoted, but the
   alignment half was stated **inverted** first (*"string ... on the right side,
   numbers on the left"*) and **he self-repaired it unprompted before any
   evidence was shown.** Text hugs LEFT, numbers hug RIGHT. One clean pass and
   it stops coming back.

5. ⚠ **STILL UNTESTED — the container-CONCEPTS backlog, now smaller.** Never
   asked cold: **the `count`/`index` roster; HASHABILITY; set order
   instability; `{}` is an empty dict; `del` vs `.pop()` vs `.clear()`;
   when-to-use-which (THE ASK QUESTION — he could not produce it in S27);
   `list()` as a constructor; `.keys()`/`.values()`; unpacking count-mismatch
   ⇒ `ValueError`.**

6. **THE SMALL COLD SET, fired mixed:**
   - `SyntaxError` + Station 0 ("did it run at all?"), and Stations 1–3.
   - `AttributeError`, `subscriptable`.
   - **`while` mechanics — NOT touched since S23. FIVE sessions overdue.**
   - ⚠ Build a raising snippet in deliberately. S30 and S31 both did.

7. **THEN THE 1.8 TAIL:** nested structures (→ shallow copy), `reversed()`,
   `copy.deepcopy`, common patterns and pitfalls. **Then 1.8 CLOSES.**

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
  `zip`; **the eight S30 promotions (clean later-day but all from ONE sitting —
  spread them); and the four S31 promotions.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~]. **`str` immutability is still
  an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`abs()` still owed a proper definition** — used unprompted in S30, never
  taught. Level-1 audit list: `len()`, `range()` as an object, `print()`'s
  return value, `.append()` vs `+`, `import`, `abs()`.

Every teaching block shows full runnable source alongside output.
Session 32 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt — it
is the designated build block 02.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| **f-string — THE THREE STEPS** | **evaluate the expression → call `str()` on it → splice it in** | **[x] PROMOTED S31, 8/10. ⚠ The `str()` step needed ONE narrowing re-ask; the braces-hold-an-EXPRESSION half came unprompted** | **gauntlet, then ~9 Sep** |
| **format spec — width + precision** | **`{v:8.1f}`. ⚠ THE NUMBER IS TOTAL FIELD WIDTH, not extra spaces** | **[x] PROMOTED S31, 10/10 challenged to 10 on this half — he named *total width* unprompted, which is the trap** | **gauntlet, then ~10 Sep** |
| **format spec — ALIGNMENT** | **⚠ TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points line up** | **[~] ⚠ S31: stated INVERTED, then SELF-REPAIRED unprompted before any evidence. Rated 10; mentor challenged that half to 7** | **S32 cold, SHORT GAP** |
| **single return value** | **`return a, b` builds ONE tuple; a function never hands back more than one object** | **[x] PROMOTED S31, cold, no re-ask, 8/10 — off his own S30 `span`** | **gauntlet, then ~9 Sep** |
| **THE COMMA MAKES THE TUPLE** | **not the parentheses. `(1)` is an `int`; `1, 2` is a tuple** | **[x] PROMOTED S31, cold, all three cases right first time, 8/10** | **gauntlet, then ~9 Sep** |
| **tuple immutability** | **item assignment on a tuple ⇒ `TypeError`. Immutability has NO error of its own; it arrives as `TypeError`** | **[~] ⚠ S31: MECHANISM COLD AND COMPLETE, LABEL AIDED — honest gap declared, then derived from the hook on one prompt. FIFTH session untested-cold** | **S32 cold, PRIORITY** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[~] ⚠ S30: both tools aided, rule stated INVERTED. S31: DRILL WRITTEN AND ISSUED, NOT ATTEMPTED** | **S32 — `drills/s31_shrug.py`, PRIORITY** |
| **`.get()` vs `[]`** | **`[]` when missing is a BUG; `.get()` when absence is EXPECTED** | **[~] S30 aided. In the S31 drill** | **S32 via the drill** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE; `.clear()` → `None`, leaves `{}`** | **[~] S27, untested. In the S31 drill** | **S32 via the drill** |
| **`remove` vs `discard` (sets)** | **same job; `remove` raises `KeyError` when absent, `discard` shrugs. An item IS its own chaabi** | **[~] taught S27, reinforced S30, NEVER TESTED. In the S31 drill** | **S32 via the drill** |
| **DRY / one copy of a decision** | **if a rule is written in four places you will change three of them and miss one** | **[~] S31 — APPLIED CORRECTLY AND FAST in the block-01 refactor, and he spotted the redundant repeat-calls himself when asked. NOT ledger-eligible: taught same session** | **S32+ — later-day ask** |
| **slicing / shallow copy** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]` copies the OUTER list, references SHARED** | **[~] S30 SUPPORTING: `angles[:]` written cold. Never asked. SIX sessions overdue** | **S32 cold — nested structures is the vehicle** |
| **`set()` / `\|` `&` `-`** | **`set()` is the ONLY empty set. Union / intersection / difference all build a NEW set ⇒ EXPRESSIONS. `-` is NOT symmetric** | **[~] S30 SUPPORTING: `set(a) & set(b)` written cold. Never asked** | **S32 cold** |
| **`sum()`** | **totals an iterable; returns a new value; `sum([])` is `0`** | **[~] S30 SUPPORTING, written cold** | **S32** |
| **`abs()`** | **distance from zero, sign discarded** | **[~] ⚠ USED UNPROMPTED IN S30 AND STILL NEVER TAUGHT** | **S32 — define it properly** |
| tuple roster | `count` and `index` ONLY | [~] S26 | **S32 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds. S30 discharged the ORDERING and `.items()` thirds** | **S32 cold** |
| **set (unit)** | **a dict with the values thrown away. Unique, unordered, hashable** | **[~] S27. ORDER INSTABILITY and `{}`-is-a-dict never asked** | **S32 cold** |
| **hashable** | **hash must be STABLE ⇒ key must be immutable** | **[~] S26/S27, untested** | **S32 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?"** | **[~] S27. ⚠ He could not produce the ASK question** | **S32** |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration`** | **[~] ⚠ queued since S25, NOT ASKED IN S26–S31. SIX sessions overdue** | **S32 cold** |
| **unpacking** | **two names on the left take apart the tuple on the right** | **[x] core PROMOTED S30. ⚠ COUNT-MISMATCH ⇒ `ValueError` half NEVER asked** | **the ValueError half, S32** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[x] `.items()` S30. ⚠ `.keys()`/`.values()` NOT asked** | **`.keys()` view + set ops still owed** |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran** | **[~] S27 miss, re-passed same-day; S28 cold. Not fired S29–S31** | **S32 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] passed cold S27, 6/10. One clean pass promotes** | **S32** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S32 cold** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] ⚠ S31: STATION 3 (TYPE) fired and WORKED — it is what let him derive `TypeError` he could not recall. Stations 0–2 not fired** | **S32 cold, full hook** |
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`** | **[x] S30, 16/16 cold, 8/10** | **gauntlet, then ~8 Sep** |
| **comprehension execution order** | **iterable → variable → gate → expression. WRITTEN ORDER ≠ EXECUTION ORDER** | **[x] S30, 8/10** | **gauntlet, then ~8 Sep** |
| **the filter as a GATE** | **`if` runs BEFORE the expression** | **[x] S30 — mechanism unprompted** | **~8 Sep** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. The BRACES and the COLON** | **[x] S30, written cold** | **gauntlet, then ~8 Sep** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting does NOT move a key. ⚠ ORDERED ≠ SORTED** | **[x] S30, all three parts cold** | **gauntlet, then ~8 Sep** |
| **`KeyError` vs `IndexError`** | **⚠ THE BRACKETS DON'T DECIDE THE ERROR — THE CONTAINER DOES** | **[x] S30, 7/10** | **gauntlet, then ~8 Sep** |
| **`zip`** | **pairs parallel ITERABLES; each pass yields a TUPLE** | **[x] S29, 8/10. ⚠ SHORT-GAP** | **gauntlet, then ~7 Sep** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST; exhausted ⇒ `[]`, no error** | **[~] S28, untested S29–S31** | **S32 cold** |
| **comprehension scope** | **its variable does not exist afterwards ⇒ `NameError`. ⚠ A FOOTNOTE** | **[~] S28** | **low priority** |
| **when NOT to use a comprehension** | **it BUILDS A CONTAINER. If the expression DOES rather than PRODUCES, you wanted a loop** | **[~] S28, untested** | **S32** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[x] PROMOTED S31 with the f-string ask — he gave it unprompted as his first move** | **~9 Sep** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] S28** | **with 1.9** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18, re-passed S27/S28. **⚠ S31: NOT recalled on tuple item assignment — derived, not retrieved** | **re-test ~1 Sep** |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | [x] S26 | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. HIS OWN TEST: can it go inside `print(...)`?** | **[x] S27 — the highest-earning row in the file** | **~1 Sep** |
| **precedence / associativity** | **rank between operators / direction within a rank** | **[x] S27** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | [x] S16, S23 | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION. `list()` is what CATCHES it** | **[x] S25, reinforced S28** | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[x] S30** | **~8 Sep** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18, S28 | ~10 Sep |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| **`while` vs `for`** | **condition re-checked vs walking an iterable** | **[x]-grade S23. ⚠ NOT touched S27–S31** | **~10 Sep** |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] S27, `drills/s27_flow.py`, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else` / ternary** | **runs only without `break` / `A if C else B` is an EXPRESSION** | **[x] S27. S31: he reached for a ternary unprompted again inside `report`** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument / parameter vs argument** | **`name=value` in the CALL / name in the `def` vs what you pass** | **[x] kwarg S27, 7/10. ⚠ parameter-vs-argument labels still [~]** | **S32** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating. **TYPE FIRST** | **[x] S25** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | [x] S25 | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | [~] 3/6 cold S24 | **S32** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell / closure four layers | one-slot box; name → function → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | **[~] the S31 drill's `drop_limit` returns `None` for absent — a live example** | **S32** |
| THE FIVE CHECKS | "Boundary pe khaali ek bahar mila" — `bahar` = outside what you ASSUMED, sign AND type | [x] S25 | ~1 Sep |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[~] ⚠ S30 evidence was contaminated by the docstring giving the boundary away. S31: the boundary test lived in `test_report.py` and PASSED — but he did not write the condition, he reused `clamp_one`** | **S32 — boundary in the TESTS ONLY** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14/S27/S28 | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 + S27 + S28 | [x] — gauntlet, then ~11 Sep |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13/S26/S27; S30 first-draft guards | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD; S28 carried comprehensions | **[x]** |
| Exceptions are signals | S18 pass; S28 `StopIteration` caught | [x] ~10 Sep |
| Traceback: each line = one live frame | S27 cold 8/10; S28 three reads | [x] — gauntlet, then ~15 Sep |
| **`while` mechanics; nested loops; found-flag** | **NOT tested S27–S31** | **[~] S32 — FIVE sessions overdue** |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, 20/20 | [x] — gauntlet, then ~15 Sep |
| Mutable/immutable discriminator | S18/S24/S26/S27 | [x] type half; tell half [~] **S32** |
| Closure definition + application; cell causation | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes; **S32** |
| Recursion | S20 same-day | [~] ~16 Sep |
| Five checks | S25 5/5 COLD; S27/S28 each missed one. **S30 and S31: asked to run them, did not report them either time** | [x] — **gauntlet, re-test with TYPE and BOUNDARY specifically** |
| **`global` / `*args`/`**kwargs`** | **S22 10/10 and 8/10; S29 build block used all four forms cold** | **[x] CONFIRMED — use freely** |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| **COMPREHENSIONS (list + dict)** | **S30 — 16/16 cold, mechanism cold, 8/10** | **[x] — gauntlet, then ~8 Sep** |
| **CONTAINERS AS CODE** | **S30 — `drills/s30_containers.py`, 19/19 cold; ⚠ `.get`/`.pop` defaults AIDED** | **[~] — the ASKS are owed, S32** |
| **DICT: ordering + `.items()`** | **S30 BOTH PROMOTED COLD** | **[x] — ~8 Sep** |
| **f-strings + format spec** | **S31: three steps cold (one re-ask on `str()`); width = TOTAL WIDTH unprompted; alignment INVERTED then self-repaired** | **[x] CURRICULUM TICKED — alignment half back S32** |
| **TUPLE: the comma / immutability** | **S31: comma-makes-it COLD and clean; immutability mechanism cold, `TypeError` label AIDED** | **[x] comma / [~] immutability — S32** |
| **RAISE-VS-SHRUG (all three pairs)** | **drill written and issued S31, NOT ATTEMPTED** | **[~] — S32, PRIORITY** |
| **Four-station hook + Station 0** | **S30 Station 4; S31 Station 3 fired and worked** | **[~] — S32, full hook** |
| **DRY / one copy of a decision** | **S31 applied fast and correctly in the block-01 refactor; taught same session** | **[~] — later-day ask, S32+** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S31 HEADLINE IS A MENTOR FAILURE AND IT REPEATS S29 EXACTLY, ONE DAY
  AFTER THE RULE THAT WAS WRITTEN TO PREVENT IT.** The refactor spec was issued
  **in chat only**; when he asked where the instructions were, the first brief
  file written was abstract — *"the clamp decision appears exactly once"* — with
  no concrete finish line. He rejected it: *"its still confusing... I can't
  understand what i need to do, make it clear, for all the instructions that i
  need to do."* The second version worked: the job split into Part A and Part B,
  every acceptance condition given a **mechanical check** ("count the function
  bodies that compare an angle to a low/high — that count must be 1"), exact
  expected values quoted, and an explicit MAY / MAY NOT list. **He finished both
  parts inside fifteen minutes.** ⚠ **THE LESSON, NARROWER THAN THE RULE: SPEC
  BEFORE PUZZLE IS NOT DISCHARGED BY SAYING THE SPEC OUT LOUD. It has to be a
  file, and every condition needs a way for HIM to check it without asking.**
- ⚠ **NEW — DO NOT SPEND HIS TURNS ON QUESTIONS THAT CANNOT BE RECORDED.** He
  objected to a [TEACH-BACK] on the redundant `clamp_one` calls: *"its stupid
  that you are still asking me the question, its easily understandable that I
  have made the changes in the code so I do understand it."* **Part-upheld.**
  Application is still not an ask — that principle is why four rows sat at [~]
  for three sessions and it is not being dropped. **But the question fired was
  tagged [TEACH-BACK], carried no rating and could promote nothing, and it was
  fired on code he had already corrected.** Fire the asks that can promote.
- ⚠ **NEW — GIVE THE VERDICT.** He rated the comma/tuple answer 8 and the mentor
  went straight to building the next drill without ruling, dumping tool output
  on the way: *"wait what you asked me my confidence after this... and then you
  have given some random output what is happening."* **Upheld in full.** The
  sequence is fixed and it is cheap: his answer → his rating → **the verdict** →
  the next thing. Silent tool work; no narration of file writing.
- ⚠ **THE MOST INTERESTING STUDENT MOMENT OF S31 — AN UNPROMPTED SELF-REPAIR.**
  On format-spec alignment he first said text right / numbers left, which is
  inverted. The mentor had a `cat -A` of his own output ready and **never needed
  it**: he came back with *"actually I said it wrong... string starts from first
  cell, that is left, whereas... the full number will be on the right side."*
  **He corrected a label with no evidence shown and no re-ask.** That is new,
  and it is the exact failure mode this file has tracked for fifteen sessions.
- ⚠ **HE PROPOSED THE REFACTOR'S SECOND FIX HIMSELF, AND CHECKED BEFORE
  ANSWERING.** Asked how many times a joint got clamped per loop pass, he
  replied by proposing corrected code and asking *"before I answer is this ok"* —
  then answered the question afterwards. Both moves are right. Count `3` was
  exact; the *"how many were necessary"* half was skipped and recovered on
  re-ask. **Depth-before-answer fired twice in S31, both recovered — NINETEEN
  AND TWENTY STRAIGHT.**
- **Honest-gap declaration remains reliable.** *"I can't come up with the error
  type"* on tuple item assignment — flagged, not guessed, with the whole
  mechanism stated correctly around the hole. **This is the Term Retention
  diagnosis in its purest form yet: the machinery is intact, the label is gone.**
- ⚠ **CONFIDENCE CALIBRATION — one challenged rating, one clean.** He rated the
  format spec 10; the width/precision half earned it, the alignment half did not
  (stated inverted first), and the mentor split the interval rather than the
  promotion. Everything else at 8, well calibrated.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** Audit list unchanged and
  still owed: `len()`, `range()` as an object, `print()`'s return value,
  `.append()` vs `+`, `import`, **`abs()`**.
- ⚠⚠ **CHANNEL — ZERO unsaved-buffer firings in S31, down from four.** mtime was
  checked before every read anyway. Keep checking; do not stop because it held.
- ⚠ **`LOG.md` — FOURTH SKIP.** It was written into `BRIEF_REFACTOR.md` as
  numbered step 4 and was still not produced. **Prose did not work, and a
  numbered step did not work either. For block 02 it goes FIRST, before code.**
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 53 raised, 52 upheld or
  part-upheld.** S31 raised FOUR — (50) where are the instructions; (51) the
  brief is not clear; (52) the [TEACH-BACK] was not worth a turn (part-upheld);
  (53) you took my rating and never gave a verdict. **Three upheld in full.**

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
- **`copy.deepcopy` and the `copy` module** — still owed inside "nested data
  structures" in 1.8.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 is the course target; collisions and
  resizing are DSA, master Layer 8.
- **HASH RANDOMISATION** — per-process seed. Park to 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0. One
  line if he asks, then park.
- ⚠ **NEW S31: DRY as a named principle, and "extract a function".** Applied
  correctly tonight without the vocabulary. The NAME is worth one line later;
  it is not worth a unit.

---
