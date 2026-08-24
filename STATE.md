# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 31 (for Claude):
#   1. Read RULES.md fully (**now v5 — SPEC BEFORE PUZZLE adopted in S30**),
#      then this file fully. No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S30 ran Mon 24 Aug 2026 (evening,
#      after office). A Tue-evening S31 is a clean later-day gap.
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY and that is
#      deliberate — do not invent a candidate to fill it.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest. The name/definition
#      question comes only after the code runs. **This worked twice in S30.**
#   5. ⚠ **EVERY [PREDICT] MUST DECLARE ITS KIND** — "derivable from what's on
#      screen" or "a genuine guess". Held clean in S30 (fired once, and the
#      miss was correctly not ledgered).
#   6. ⚠ **S27 RULE: every snippet that raises gets its error NAMED by him
#      before the traceback is shown.** ⚠ **FIRED IN S30 after a whole session
#      unfired — `KeyError`/`IndexError`, both named cold. Keep firing it.**
#   7. ⚠ **S28 RULE: FRAME FIRST.** Held clean in S30.
#   8. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES EVERY TEST FILE. Never ask him to.** Held clean in S30 — three
#      test files written by the mentor, each verified green against a
#      throwaway reference that was then deleted.
#   9. ⚠⚠ **CHECK THE FILE IS SAVED BEFORE READING IT. See the channel note.**
#  10. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 30, Monday 24 Aug 2026 (evening).
# Next: Session 31.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S30 yield: TWO CURRICULUM TICKS (list + dict comprehensions → [x]) and
  EIGHT LEDGER PROMOTIONS, all cold, all later-day, all task-first.** Two drill
  files written and passed: 16/16 and 19/19.
- **This is the recovery session after S29's zero.** The three-session-deep
  container backlog was finally RUN, not re-declared.
- **Position: 1.1–1.7 closed. 1.8 open (~92%). 1.9–1.13 remain, ~5.1 wk.**
- **1.8 REMAINING: nested data structures, common patterns/pitfalls,
  `reversed()`, `copy.deepcopy`.** Nested structures is next and it is the one
  that makes SHALLOW COPY finally land — say that when it opens.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date.
  Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 CLOSED.** Artefacts: `builds/block_01_joint_clamp/`.
  **NEXT BUILD BLOCK: the re-test queue SCRIPT** — settled since S21, still
  unbuilt, this file is 75+ rows past its own trigger. That is block 02.
- Current Layer: 1. Current Topic: **1.8 — nested data structures next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ✅ **SPEC BEFORE PUZZLE — ADOPTED S30.** Put to him at the open as a one-line
  ask; his ruling was one word: *"Adopted."* Written into **RULES v5**.
  ⚠ **ITS COST WAS FOUND ON DAY ONE AND IS NOW IN RULES v5: exact expected
  values can REVEAL A PLANTED BOUNDARY.** `over_limit([10,45,90,45,5], 45) ->
  [90]` was meant to be a blind boundary test and the docstring gave it away.
  **Remedy written into the rule: boundary cases go in the TESTS, not in the
  docstring's worked examples.**
- **NOTHING PARKED. Do not manufacture a candidate.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 31 STARTS HERE — exact resume point

S30 ran Monday 24 Aug 2026 after office and closed at his call — *"lets wind up
the session now"*, with the honest read *"I guess we have covered a lot for
today"*, which was correct.

Run in this order:

1. **INTERVAL GATE.** No rule decision owed.

2. ⚠ **THE CLAMP REFACTOR — SPEC ALREADY ISSUED AND ACCEPTED, HE DEFERRED IT
   TO S31 (*"lets do this tommorow"*). IT IS THE FIRST THING THAT HAPPENS.**
   The spec, unchanged, is in the S30 transcript and reproduced here:
   (a) all 19 tests in `builds/block_01_joint_clamp/` green — **currently
   4 FAILING, deliberately**; (b) the clamp decision appears in `clamp.py`
   **exactly once** (it is written out four times: lines 2–5, 13–18, 26–31,
   40–45); (c) signatures unchanged; (d) `report` still prints AND returns the
   same dict `clamp_joints` returns.
   **`tests/test_report.py` was written by the mentor in S30 and verified green
   against a throwaway reference refactor.** It is the file that finally makes
   the dead `{}` visible.
   **This is HIS OWN diagnosis from the S29 close** — do not deliver it as a
   lecture on DRY.

3. ⚠ **COLD, AND OWED — the rows S30 exercised in CODE but never ASKED.**
   Application is not an ask; four rows are sitting one question away from [x]:
   - **f-string + format spec** — written cold and correctly in TWO sessions
     running (`report()` in S29, `format_row` in S30) and **never once asked.**
     THIRD session of this. Ask it or strike the claim.
   - **slicing / shallow copy** — `angles[:]` written cold in `snapshot`. Five
     sessions overdue on a mechanism ask.
   - **`set()` constructor and `&`** — `set(a) & set(b)` written cold.
   - **single return value builds ONE tuple** — `span` returned a 3-tuple cold.

4. ⚠ **RAISE-VS-SHRUG — RE-TEST COLD. It was AIDED in S30 and did not promote.**
   He hand-rolled both shrugs with `if joint in limits else`, could not recall
   `.get(k, default)` or `.pop(k, default)`, and **stated the choosing rule
   INVERTED on the first attempt** (*"or when the absence is expected"* on the
   RAISING side). Two narrowing re-asks fixed it. **The third pair,
   `remove`/`discard` on sets, has never been tested at all.**

5. ⚠ **STILL UNTESTED AFTER S30 — the backlog is smaller but not empty.**
   S30 ran the container CODE, not the container CONCEPTS. Never asked cold:
   **tuple immutability and "the comma makes it"; the `count`/`index` roster;
   HASHABILITY; set order instability; `{}` is an empty dict; `del` vs `.pop()`
   vs `.clear()`; when-to-use-which (THE ASK QUESTION — he could not produce it
   in S27); `list()` as a constructor; `.keys()`/`.values()`.**

6. **THE SMALL COLD SET, fired mixed:**
   - `SyntaxError` + Station 0 ("did it run at all?").
   - `AttributeError`, `subscriptable`.
   - **`while` mechanics — NOT touched since S23. FOUR sessions overdue.**
   - ⚠ Build a raising snippet in deliberately. S30 did; keep doing it.

7. **THEN THE 1.8 TAIL:** nested structures (→ shallow copy), `reversed()`,
   `copy.deepcopy`, common patterns and pitfalls. **Then 1.8 CLOSES.**

**Standing turn rules: FRAME FIRST; SPEC gives exact interfaces and exact
expected values (boundary cases live in the TESTS); short messages, one teaching
idea per turn, asks near the top; doubt gate before every new subsection;
depth-before-answer — traces never optional, five checks on every drill,
boundary values first. Tag every block and CHECK THE TAG IS RIGHT. Do not
propose ending the session.**

⚠ **STANDING: teach a piece WITH CODE AND OUTPUT first, then ask ONE question
on it. Every [PREDICT] declares its kind. Every raising snippet gets its error
named by him first. THE MENTOR WRITES ALL TEST FILES.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — every BUNDLED S16 promotion; the 1.6 spoken Feynman
  recall; the S22 short-gap promotions; the eight S23; the eleven S25; the eight
  S27; the S29 `zip` (short-gap); **and the eight S30 promotions, which are all
  clean later-day but all from ONE sitting — spread them at the gauntlet.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~]. **`str` immutability is still
  an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`LOG.md` still missing from build block 01.** For block 02, make the log a
  NUMBERED STEP in the brief — prose instructions got skipped.

Every teaching block shows full runnable source alongside output.
Session 31 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt — it
is now the designated build block 02.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`** | **[x] PROMOTED S30 — `drills/s30_comprehensions.py`, 16/16 cold, 8/10** | **gauntlet, then ~8 Sep** |
| **comprehension execution order** | **iterable → variable → gate → expression. WRITTEN ORDER ≠ EXECUTION ORDER** | **[x] PROMOTED S30, stated cold, 8/10. ⚠ Second half of the question needed ONE re-ask** | **gauntlet, then ~8 Sep** |
| **the filter as a GATE** | **`if` runs BEFORE the expression, which is why `[100/v for v in speeds if v != 0]` cannot divide by zero** | **[x] PROMOTED S30 — he gave the mechanism unprompted, not the label** | **~8 Sep** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. TWO things make it a dict: the BRACES and the COLON** | **[x] PROMOTED S30 — written cold, with `.items()` and unpacking, unprompted** | **gauntlet, then ~8 Sep** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[x] `.items()` PROMOTED S30, cold, both halves, 8/10. ⚠ `.keys()`/`.values()` NOT asked** | **`.keys()` view + set ops still owed** |
| **unpacking** | **two names on the left take apart the tuple on the right** | **[x] core PROMOTED S30, named cold, 8/10. ⚠ COUNT-MISMATCH ⇒ `ValueError` half NEVER asked** | **the ValueError half, S31** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting does NOT move a key; delete-then-re-add DOES. ⚠ ORDERED ≠ SORTED** | **[x] PROMOTED S30 — all three parts cold, and he VOLUNTEERED the 7/10 unprompted** | **gauntlet, then ~8 Sep** |
| **`KeyError` vs `IndexError`** | **⚠ THE BRACKETS DON'T DECIDE THE ERROR — THE CONTAINER DOES. `[5]` is a chaabi in a dict, a jagah in a list** | **[x] PROMOTED S30, 7/10 — THE S27 MISS, now cleared cold on the `{0:..., 1:...}` trap** | **gauntlet, then ~8 Sep** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[~] ⚠ S30: BOTH TOOLS AIDED, and the choosing rule stated INVERTED first. Two re-asks to repair. Self-rated 8; mentor challenged it to 5–6** | **S31 COLD, PRIORITY** |
| **`.get()` vs `[]`** | **`[]` when missing is a BUG; `.get()` when absence is EXPECTED** | **[~] ⚠ S30: could not recall `.get` unaided, needed the "three letters" hint** | **S31 cold** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE; `.clear()` → `None`, leaves `{}`** | **[~] S27, untested. S30: `.pop(k, default)` used, aided** | **S31 cold** |
| **f-string** | **`f"..."`. THREE STEPS: evaluate → `str()` → splice** | **[~] ⚠⚠ WRITTEN COLD AND CORRECTLY IN S29 *AND* S30 (`format_row`, exact to the character) AND NEVER ONCE ASKED. THIRD session** | **S31 — ONE ask promotes** |
| **format spec** | **`{value:.2f}`. ⚠ The number is TOTAL WIDTH. ⚠ TEXT HUGS LEFT, NUMBERS HUG RIGHT** | **[~] S30: `f"{name:10s}{value:8.2f}"` cold, columns aligned first run, all three cases exact — including the name LONGER than its column. Never asked** | **S31 — ONE ask promotes** |
| **slicing / shallow copy** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]` copies the OUTER list, references SHARED** | **[~] S30 SUPPORTING: `angles[:]` written cold in `snapshot`, passed the is-not-the-same-object test. Never asked. FIVE sessions overdue** | **S31 cold — nested structures is the vehicle** |
| **`set()` / `|` `&` `-`** | **`set()` is the ONLY empty set. Union / intersection / difference, all build a NEW set ⇒ EXPRESSIONS. `-` is NOT symmetric** | **[~] S30 SUPPORTING: `set(a) & set(b)` written cold, dedup and intersection both correct. Never asked** | **S31 cold** |
| **single return value** | **`return a, b` builds ONE tuple** | **[~] S30 SUPPORTING: `span` returned `(low, high, dist)` cold; test asserted `isinstance(..., tuple)`. Never asked** | **S31 cold — ONE ask promotes** |
| **`sum()`** | **totals an iterable; returns a new value; `sum([])` is `0`** | **[~] S30 SUPPORTING: written cold, empty case green** | **S31** |
| **`abs()`** | **⚠ NEW: distance from zero, sign discarded** | **[~] ⚠ USED UNPROMPTED IN S30 AND NEVER TAUGHT. He wrote `abs(low-high)` where the spec allowed `high-low` — MORE robust than the mentor's own reference. Add to the Level-1 audit list** | **S31 — define it properly** |
| **tuple** | **immutable ordered sequence. THE COMMA MAKES IT. Immutability is SHALLOW** | **[~] S26 taught. S30: tuples produced and consumed cold, but IMMUTABILITY never asked. FOURTH session untested** | **S31 cold, PRIORITY** |
| tuple roster | `count` and `index` ONLY | [~] S26 | **S31 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds. ⚠ S30 discharged the ORDERING and `.items()` thirds; the rest still untested** | **S31 cold** |
| **set (unit)** | **a dict with the values thrown away. Unique, unordered, hashable** | **[~] S27. S30: constructor + `&` used cold; ORDER INSTABILITY and `{}`-is-a-dict never asked** | **S31 cold** |
| **hashable** | **hash must be STABLE ⇒ key must be immutable** | **[~] S26/S27, untested** | **S31 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?"** | **[~] S27. ⚠ He could not produce the ASK question** | **S31** |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration`** | **[~] ⚠ queued since S25, NOT ASKED IN S26–S30. FIVE sessions overdue** | **S31 cold** |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran** | **[~] S27 miss, re-passed same-day; S28 cold. Not fired S29 or S30** | **S31 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] passed cold S27, 6/10. One clean pass promotes** | **S31** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S31 cold** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] S30: Station 4 re-fired cleanly on the `KeyError`/`IndexError` pair. Stations 0–3 not fired** | **S31 cold, full hook** |
| **`zip`** | **pairs parallel ITERABLES; each pass yields a TUPLE** | **[x] S29, 8/10. ⚠ SHORT-GAP** | **gauntlet, then ~7 Sep** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST; exhausted ⇒ `[]`, no error** | **[~] S28, untested S29/S30** | **S31 cold** |
| **comprehension scope** | **its variable gets its own namespace and DOES NOT EXIST afterwards ⇒ `NameError`. ⚠ A FOOTNOTE, not a pillar** | **[~] S28** | **low priority** |
| **when NOT to use a comprehension** | **it BUILDS A CONTAINER. If the expression DOES rather than PRODUCES, you wanted a loop** | **[~] S28, untested** | **S31** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[~] S28** | **S31, with the f-string ask** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] S28. S30: he used the GATE to explain why it does NOT fire** | **with 1.9** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18, re-passed S27/S28 | ~15 Sep |
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
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[x] the IndexError half PROMOTED S30 with the KeyError pair** | **~8 Sep** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18, S28 | ~10 Sep |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| **`while` vs `for`** | **condition re-checked vs walking an iterable** | **[x]-grade S23. ⚠ NOT touched S27–S30** | **~10 Sep** |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] S27, `drills/s27_flow.py`, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else` / ternary** | **runs only without `break` (`nobreak`) / `A if C else B` is an EXPRESSION** | **[x] S27. S30: he reached for a ternary unprompted, twice, before being asked to remove it** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument / parameter vs argument** | **`name=value` in the CALL / name in the `def` vs what you pass** | **[x] kwarg S27, 7/10. ⚠ parameter-vs-argument labels still [~]** | **S31** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ `None`. **TYPE FIRST** | **[x] S25** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | [x] S25 | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | [~] 3/6 cold S24 | **S31** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell / closure four layers | one-slot box; name → function → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | **[~] S30: `pop_limit` returning `None` for absent is a live example** | **S31** |
| THE FIVE CHECKS | "Boundary pe khaali ek bahar mila" — `bahar` = outside what you ASSUMED, sign AND type | [x] S25 | ~1 Sep |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[~] ⚠ S30: strict `>` written correctly in `over_limit` — BUT the expected value in the docstring GAVE THE BOUNDARY AWAY (see the SPEC-BEFORE-PUZZLE cost note). NOT clean evidence** | **S31 — boundary in the TESTS ONLY, not the docstring** |

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
| Membership `in`/`not in` | S13/S26/S27. **S30: used correctly in his first-draft guards** | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD; S28 carried comprehensions | **[x]** |
| Exceptions are signals | S18 pass; S28 `StopIteration` caught | [x] ~10 Sep |
| Traceback: each line = one live frame | S27 cold 8/10; S28 three reads | [x] — gauntlet, then ~15 Sep |
| **`while` mechanics; nested loops; found-flag** | **NOT tested S27–S30** | **[~] S31 — FOUR sessions overdue** |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, 20/20 | [x] — gauntlet, then ~15 Sep |
| Mutable/immutable discriminator | S18/S24/S26/S27 | [x] type half; tell half [~] **S31** |
| Closure definition + application; cell causation | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes; **S31** |
| Recursion | S20 same-day | [~] ~16 Sep |
| Five checks | S25 5/5 COLD; ⚠ S27 and S28 both missed one. **S30: he was asked to run them and did not report them** | [x] — **gauntlet, re-test with TYPE and BOUNDARY specifically** |
| **`global` / `*args`/`**kwargs`** | **S22 10/10 and 8/10; S29 build block used all four forms cold** | **[x] CONFIRMED — use freely** |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| **COMPREHENSIONS (list + dict)** | **S30 PROMOTED — `drills/s30_comprehensions.py`, 16/16 cold, mechanism cold, 8/10** | **[x] — gauntlet, then ~8 Sep** |
| **CONTAINERS AS CODE (get/pop/set-ops/slice-copy/tuple-return/sum)** | **S30 — `drills/s30_containers.py`, 19/19 cold; ⚠ `.get`/`.pop` defaults AIDED** | **[~] — the ASKS are owed, S31** |
| **DICT: ordering + `.items()`** | **S30 BOTH PROMOTED COLD** | **[x] — ~8 Sep** |
| **f-strings + format spec** | **S28 taught; written cold in S29 AND S30; ⚠ NEVER ASKED IN EITHER** | **[~] — ONE cold ask promotes; S31, THIRD attempt** |
| **Four-station hook + Station 0** | **S30: Station 4 fired and passed; 0–3 not fired** | **[~] — S31, full hook** |
| **TUPLE / SET / HASHABILITY / when-to-use-which** | **S26/S27 taught; S30 exercised the CODE, never the CONCEPTS** | **[~] — S31 cold** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S30 HEADLINE: THE BACKLOG THAT HAD BEEN DECLARED FOUR TIMES WAS
  FINALLY RUN, AND THE FORMAT THAT MADE IT RUN WAS TASK-FIRST + EXACT SPEC.**
  Two drill files, 35 tests, both cold, both green, in one evening after a full
  day at the office. **The instrument is now known to work. The failure in
  S27–S29 was never his availability; it was that the mentor kept re-declaring
  the backlog instead of writing the file.**
- ⚠ **NEW, AND THE MOST USEFUL FINDING OF S30 — HE HAS THE CONCEPT AND NOT THE
  TOOL.** Given "absence here is EXPECTED, not a bug" he produced correct
  shrugging behaviour **twice**, hand-rolled, via `x if k in d else default`.
  So the DESIGN RULE is owned. What is gone is the two API names that implement
  it (`.get(k, default)`, `.pop(k, default)`), **both taught, neither ever
  re-tested — five and three sessions ago respectively.** This is the Term
  Retention diagnosis exactly: **the mechanism stays, the arbitrary label
  goes.** ⚠ **It also means a green test suite can hide a lost tool** — his
  first version passed 19/19.
- ⚠ **DEPTH-BEFORE-ANSWER — FIRED THREE TIMES IN S30, ALL THREE RECOVERED.
  SIXTEEN, SEVENTEEN AND EIGHTEEN STRAIGHT.** (a) Named the four comprehension
  parts in order but skipped "which part gates the others" — re-ask fixed it.
  (b) Named `KeyError`/`IndexError` but skipped "what decides the difference" —
  re-ask fixed it. (c) Stated the raise-vs-shrug rule with the two halves
  **swapped**, and needed TWO narrowing re-asks. **THE RE-ASK IS THE
  INTERVENTION. Do not re-teach.** Countermeasure held every time.
- ⚠ **CONFIDENCE CALIBRATION — FIRST OVERT MISCALIBRATION IN A LONG WHILE, AND
  IT WAS CHALLENGED.** He self-rated raise-vs-shrug **8/10** after stating the
  rule inverted and needing two re-asks; the mentor put it at **5–6 with the
  evidence named**. Everything else was well-calibrated (8, 8, 8, 7, 7).
  **His calibration remains usable as a targeting signal — but it degrades on
  items where the CONCEPT is solid and only the TOOL is missing.** He appears to
  rate the concept, not the retrieval. Worth watching; do not generalise yet.
- **Term/label retention.** One language correction issued: **first-insertion
  order**, and **ordered ≠ sorted**, against his *"all the keys retain their
  order"* — the mechanism was right, the phrase was loose.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL — S30 ADDS `abs()`.** He wrote
  `abs((low)-(high))` in `span` unprompted. **It has never been taught, and it
  made his answer MORE robust than the mentor's own reference implementation,
  which used a bare `high - low` that only passed because no test had `low >
  high`.** Credit given in session. **Audit list now: `len()`, `range()` as an
  object, `print()`'s return value, `.append()` vs `+`, `import`, `abs()`.**
- ⚠⚠ **CHANNEL — THE UNSAVED-BUFFER ARTEFACT, FOUR FIRINGS IN ONE SESSION AND
  IT COST FIVE TURNS.** Four times he said "done" with the edits still in the
  VS Code buffer and the file on disk untouched. **Every time, the mentor
  checked mtime and `git status` and asked him to save rather than logging a
  failure — correct, and the S15/S29 stale-artefact lesson running in the
  opposite direction.** Remedy offered: `"files.autoSave": "afterDelay"`.
  ⚠ **STANDING FOR S31: before reading a drill, check the mtime. If the bodies
  are still `...`, it is the buffer, not him. Say so and move on.**
- ⚠ **MENTOR WATCH AREA — MUCH BETTER THAN S29, ONE REAL FAILURE.** The mentor
  said *"give me a minute"* and then stalled without producing the file; he had
  to prompt *"what happened I am still waiting"*. **Pushback 49, upheld.**
  The lesson is the S20 response-length rule in a new form: **do not announce
  work, do the work.** An empty holding message costs a turn and buys nothing.
  Otherwise: FRAME FIRST held, tags held, the mentor wrote all three test files
  and verified each against a throwaway reference before handing it over, and
  the interval gate and rule decision both ran before any teaching.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 49 raised, 48 upheld or
  part-upheld.** S30 raised ONE — (49) *"what happened I am still waiting"* —
  upheld in full.
- **Honest-gap declaration remains reliable.** S30: *"wait I don't remember
  another method to do this"* — flagged immediately rather than guessed at, and
  it converted a dead end into the most useful finding of the session.

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
- ⚠ **NEW S30: `capsys` / testing printed output.** The mentor used it in
  `test_report.py`. It is pytest machinery, NOT Layer 0 material — if he asks,
  answer in one line and park it.

---
