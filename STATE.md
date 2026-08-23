# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 30 (for Claude):
#   1. Read RULES.md fully (**v4, unchanged — no rule adopted in S29**), then
#      this file fully. No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S29 ran Sun 23 Aug 2026 (evening).
#      **He has office on Mon 24 Aug.** If S30 is Mon evening, that is a clean
#      later-day gap and the ENTIRE backlog is ledger-eligible.
#   3. ⚠ **A RULE DECISION IS OWED. ONE candidate is parked (SPEC BEFORE
#      PUZZLE). Put it to him BEFORE teaching. Do not invent a second.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. ⚠ **EVERY [PREDICT] MUST DECLARE ITS KIND** — "derivable from what's
#      on screen" or "a genuine guess". Held clean in S29 (fired once).
#   6. ⚠ **S27 RULE: every snippet that raises gets its error NAMED by him
#      before the traceback is shown.** ⚠ **NOT FIRED ONCE IN S29** — nothing
#      raised all session. Re-fire it in S30.
#   7. ⚠ **S28 RULE: FRAME FIRST.** What it is → why it exists → what it buys
#      you, BEFORE any mechanics, and say how much each fact is worth.
#      **Held clean in S29 on the teaching; BREACHED IN SPIRIT on the SPEC —
#      see the mentor watch area, it is the whole story of this session.**
#   8. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0.** He caught
#      this in S29. **The mentor writes every test file. Never ask him to.**
#   9. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 29, Sunday 23 Aug 2026 (evening).
# Next: Session 30.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S29 yield: THE COLD BUILD BLOCK RAN AT LAST — 13/13 pytest, cold, unaided —
  AND ONE PROMOTION (`zip` → [x]). ZERO CURRICULUM ITEMS TAUGHT.** 1.8 stands
  exactly where S28 left it, at ~90%.
- ⚠ **THAT ZERO IS A MENTOR COST, NOT A STUDENT ONE. Roughly the first half of
  the session was spent rewriting the build-block spec FOUR TIMES because the
  first three were unusable. He never got a teaching block. See the mentor
  watch area — this is the single most expensive mentor failure in the file.**
- **Position: 1.1–1.7 closed. 1.8 open (~90%). 1.9–1.13 remain, ~5.1 wk.**
- **1.8 REMAINING: nested data structures, common patterns/pitfalls,
  `reversed()`, `copy.deepcopy`.** Nested structures is next and it is the one
  that makes SHALLOW COPY finally land — say that when it opens.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master. Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 IS DONE AND CLOSED.** Carried three dates, ran on the
  fourth. Artefacts: `builds/block_01_joint_clamp/`.
  **NEXT BUILD BLOCK: the re-test queue SCRIPT** — settled as the tooling
  answer since S21, still unbuilt, and this file is now 75+ rows past its own
  trigger. That is the natural block 02.
- Current Layer: 1. Current Topic: **1.8 — nested data structures next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ⚠ **ONE CANDIDATE PARKED, MENTOR-PROPOSED, HIS RULING OWED AT THE S30 OPEN:**
  **"SPEC BEFORE PUZZLE."** *A task spec states the exact interface and the
  exact expected values. The only thing ever withheld is the SOLUTION. If a
  spec leaves the student unable to start, it has measured nothing — and a
  block that does not run measures strictly less than a block that runs with
  help.*
  **THE BREACH THAT PRODUCED IT (S29, and it cost half a session):** the build
  block spec was written three times in prose that preserved a design puzzle —
  no signature, no concrete numbers, no exact returns. He pushed back three
  times, escalating, and was right every time. The mentor's reasoning was that
  giving the signature would give away the problem. **It would not have: the
  design hole lived in the FUNCTION BODY, not the parameter list.** Once exact
  signatures and exact expected values were handed over, he solved the body
  cold — including the part that was being "protected".
  ⚠ **PUT IT TO HIM AS A ONE-LINE ASK AND TAKE HIS RULING. He is entitled to
  reject it; the last two adopted rules were his and this one is not.**
- ⚠ **A SECOND OBSERVATION, DELIBERATELY NOT PARKED AS A RULE** (the cap
  governs the count, and one is enough): the S15 stale-file failure recurred
  in a new channel — he read a VS Code MARKDOWN PREVIEW that had cached an
  older render and spent two turns furious at a spec that had already been
  fixed on disk. **Channel before blame, again.** No rule needed; the existing
  one covers it. Just check the artefact he is actually looking at.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 30 STARTS HERE — exact resume point

S29 ran Sunday 23 Aug 2026 and closed at his call — *"I need to go and sleep
for the office tomorrow."* The build block ran and passed; no teaching happened.

Run in this order:

1. **INTERVAL GATE**, then **the parked rule decision (SPEC BEFORE PUZZLE).**

2. ⚠ **THE COMPREHENSIONS DRILL. DEFERRED TWICE NOW — S28 → S29 → S30.**
   He refused it at the S28 close *specifically* to keep it ledger-eligible
   (*"lets do the drill tommorow then, atleast it goes to the ledger then"*).
   It did not run in S29 because the mentor burned the session on the spec.
   **That is a promise this file made and then broke. It is the FIRST teaching
   thing that happens in S30, task-first, in `drills/s30_comprehensions.py`
   with `tests/test_s30_comprehensions.py` WRITTEN BY THE MENTOR.**
   Constraints should force: a list comprehension with a filter, a dict
   comprehension over `.items()`, and an f-string with a format spec.
   **`zip` is now [x] — it may appear as substrate. Do not name the mechanisms
   in the docstring.**

3. ⚠ **THE REFACTOR HE PROPOSED AND DID NOT DO.** His own words at the S29
   close: *"I should make one function that does all that calculation."*
   The clamp rule is written out FOUR times in `clamp.py` (lines 2–5, 13–18,
   26–31, 40–45), and `report()` returns a dead `{}` it never fills.
   **Small, concrete, his own diagnosis, and it produces committable evidence.
   Offer it as the warm-up — 10 minutes — not as a lecture on DRY.**

4. ⚠⚠ **THE BACKLOG IS NOW THREE SESSIONS DEEP. Declared for S27, S28 AND
   S29; run in none of them.** Still entirely untested:
   **TUPLE (whole unit), DICT (S26 two-thirds + S27 tail), SET (whole unit),
   SHALLOW COPY, UNPACKING, `list()`, `.get()`, `.items()`, the raise-vs-shrug
   pairing, when-to-use-which.**
   **FOURTH DECLARATION. Task-first, in one drill file, or strike the claim
   that it is a priority — a priority that loses three times running is not
   one, and pretending otherwise is exactly the kind of comfortable fiction
   this file exists to prevent.**

5. **THE SMALL COLD SET, fired mixed, not alone:**
   - **`KeyError` vs `IndexError`** — the S27 miss, still untested cold.
   - `SyntaxError` + Station 0 ("did it run at all?").
   - `AttributeError`, `subscriptable`.
   - `while` mechanics (not touched since S23).
   - ⚠ **Nothing raised in S29, so the S27 error-naming rule went unfired for
     a whole session. Build a raising snippet in deliberately.**

6. **THEN THE 1.8 TAIL:** nested structures (→ shallow copy), `reversed()`,
   `copy.deepcopy`, common patterns and pitfalls. **Then 1.8 CLOSES.**

**Standing turn rules: FRAME FIRST; SPEC gives exact interfaces and exact
expected values; short messages, one teaching idea per turn, asks near the top;
doubt gate before every new subsection; depth-before-answer — traces never
optional, five checks on every drill, boundary values first. Tag every block
and CHECK THE TAG IS RIGHT. Do not propose ending the session.**

⚠ **STANDING: teach a piece WITH CODE AND OUTPUT first, then ask ONE question
on it. Every [PREDICT] declares its kind. Every raising snippet gets its error
named by him first. THE MENTOR WRITES ALL TEST FILES.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — every BUNDLED S16 promotion; the 1.6 spoken Feynman
  recall; the S22 short-gap promotions; the eight S23 promotions; the eleven
  S25 promotions; the eight S27 promotions; **and the S29 `zip` promotion,
  which is short-gap (~10h + sleep) and flagged as such.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~]. **`str` immutability is still
  an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`LOG.md` WAS NOT WRITTEN IN THE BUILD BLOCK.** Process evidence for
  block 01 is the code only. **For block 02, make the log a numbered step in
  the brief rather than a paragraph of prose — prose instructions got skipped.**

Every teaching block shows full runnable source alongside output.
Session 30 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`. ⚠ WRITTEN ORDER ≠ EXECUTION ORDER: iterable → var → gate → expression** | **[~] NEW S28, taught in full, NO DRILL — deferred by him to S29** | **S29 cold, TASK-FIRST** |
| **why a comprehension exists** | **it is an EXPRESSION, so it fits where a `for` STATEMENT cannot — inside a call, a `return`, an argument, another comprehension** | **[~] NEW S28. ⚠ HE DERIVED THIS HIMSELF from his own `print(...)` test before it was stated** | **S29** |
| **the filter as a GATE** | **`if` runs BEFORE the expression, which is why `[100/v for v in speeds if v != 0]` does not divide by zero** | **[~] NEW S28 — the order was PROVED with a live `ZeroDivisionError`, not asserted** | **S29 cold** |
| **comprehension scope** | **its variable gets its own namespace and DOES NOT EXIST afterwards ⇒ `NameError`. ⚠ Right-sized out loud as a FOOTNOTE, not a pillar** | **[~] NEW S28** | **low priority** |
| **when NOT to use one** | **a comprehension BUILDS A CONTAINER. `[print(j) for j in joints]` builds `[None, None, None]` — if the expression DOES rather than PRODUCES, you wanted a loop** | **[~] NEW S28 — connects to his own S25 returns-`None` rule** | **S29** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. TWO things make it a dict: the BRACES and the COLON** | **[~] NEW S28 — he produced both himself** | **S29 cold** |
| **`zip`** | **pairs parallel ITERABLES (not "lists" — his S29 phrasing, corrected); each pass yields a TUPLE, which is why `for a, b in zip(...)` unpacks** | **[x] PROMOTED S29 — REACHED FOR UNPROMPTED to solve an unseen design problem, `builds/block_01_joint_clamp/clamp.py`, 13/13. 8/10. ⚠ SHORT-GAP** | **gauntlet, then ~7 Sep** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST, no error. Exhausted ⇒ `[]`, no error, because `list()` catches the `StopIteration`** | **[~] NEW S28. ⚠ He predicted "error" on the exhausted case — half right, the exhaustion was correct, the raising was not** | **S29 cold** |
| **f-string** | **`f"..."`. THREE STEPS: evaluate the expression → call `str()` on it → splice. Without the `f`, `{x}` is literal characters** | **[~] S28. ⚠ S29 STRONG SUPPORTING: written cold in `report()`, incl. NESTED SAME-TYPE QUOTES inside the braces — legal only on 3.12+ (PEP 701), and he is on 3.12.3. Not asked, not rated** | **S30 cold — ONE ask promotes** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[~] NEW S28 — he reasoned the `for` exclusion out himself from expression-vs-statement** | **S29** |
| **format spec** | **`{value:.2f}`. ⚠ The number is TOTAL WIDTH, not extra spaces. ⚠ TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points line up** | **[~] S28. ⚠ S29: wrote `{k:10s}` and `{v:8.1f}` cold and the columns ALIGNED FIRST RUN — applied, not recited. Not rated** | **S30 cold — ONE ask promotes** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] NEW S28 — decoded correctly cold on first exposure** | **with 1.9** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18. **S27 re-passed cold twice. S28: named cold on `"..." + float`** | ~15 Sep |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran. Not one line executes** | **[~] S27 miss, re-passed same-day. S28: named cold and correctly, and the "line 3 never printed" proof was shown** | **S29 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] — passed cold S27, 6/10. One more clean pass promotes** | **S29** |
| **`KeyError`** | **the KEY is not in the dict. ⚠ THE BRACKETS DON'T DECIDE THE ERROR — WHAT'S INSIDE THEM DOES** | **[~] ⚠ THE S27 MISS. NOT touched in S28** | **S29 cold, MIXED with `IndexError`** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] S27: 1 hit, 1 miss, 1 gap. S28 supporting: 5/5 error labels named cold** | **S29 cold** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S29 cold** |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | [x] — S26 full chain cold | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. HIS OWN TEST: can it go inside `print(...)`?** | **[x] S27. ⚠ S28: THIS ROW DID MORE WORK THAN ANY OTHER — it carried comprehensions, the f-string braces, and the `for`-loop exclusion. Paid for itself three times in one session** | **~1 Sep** |
| **precedence** | **rank between DIFFERENT operators** | **[x] S27, 7/10** | **~15 Sep** |
| **associativity** | **direction within the SAME rank. Sab left se, sirf `**` right se** | **[x] S27, re-promoted after the S25 demotion** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | [x] S16, S23 | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION. ⚠ S28: `list()` is what CATCHES it — the signal never reaches you** | **[x] S25, reinforced S28** | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration`** | **[~] ⚠ queued S25, NOT ASKED IN S26, S27 OR S28 — three sessions overdue. S28 used it heavily (`list(zip(...))`) as supporting evidence only** | **S29 cold** |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[~] S27 supporting only. S28: `zip` taught explicitly as the way to STOP indexing manually** | **S29 cold** |
| **slicing / shallow copy** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]` copies the OUTER list, references SHARED** | **[~] taught S24/S26, NOT tested in S25–S28 — FOUR sessions overdue** | **S29 cold, and nested structures is the natural vehicle** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10. S28: read three live tracebacks including the caret markers pointing at the EXPRESSION slot** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | **[x] S18. S28: named cold on the comprehension-scope case** | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | **[x] S16. ⚠ S28 EXCEPTION TAUGHT: a comprehension has its OWN namespace. Level 3 mechanics parked** | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade S23 | ~10 Sep |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] ALL THREE S27, cold, `drills/s27_flow.py`, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **runs only if the loop finished WITHOUT `break`. Read it as `nobreak`** | **[x] S27** | **~15 Sep** |
| **ternary** | **EXPRESSION: `A if C else B` — evaluates to a VALUE. `ter-` = THREE** | **[x] S27** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument** | **`name=value` in the CALL, matched by NAME to a PARAMETER** | **[x] S27, 7/10** | **~15 Sep** |
| **parameter vs argument** | **parameter = the name in the `def`; argument = what you pass** | **[~] WATCH — taught S18, labels still not stuck** | **S29** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ `None`. **TYPE FIRST** | **[x] S25. ⚠ S28: `[print(j) for j in joints]` → `[None, None, None]` is the third distinct payoff of this rule** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | [x] S25 | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | [~] 3/6 cold S24 | **S29** |
| **tuple** | **immutable ordered sequence. THE COMMA MAKES IT. Immutability is SHALLOW** | **[~] taught S26. ⚠ NOT TESTED IN S27 OR S28. S28 supporting: he identified `zip`'s output as tuples cold** | **S29 cold, PRIORITY** |
| tuple roster | `count` and `index` ONLY | [~] S26 | **S29 cold** |
| **unpacking** | **`low, high = t`; count mismatch ⇒ `ValueError`** | **[~] S26. S29 supporting: `for angle_value, limits_key in zip(...)` written cold, and `clamp_one(a, *limits[n])` — ⚠ he used the SPLAT to unpack a tuple into arguments, which is the `*args` mirror. Never asked directly** | **S30 cold** |
| single return value | `return a, b` builds ONE tuple | [~] S26, untested | **S29 cold** |
| `sum()` | totals an iterable; returns a new value | [~] S26, untested | **S29 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds STILL UNTESTED after three sessions** | **S29 cold, PRIORITY** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting does NOT move a key; delete-then-re-add DOES. ⚠ ORDERED ≠ SORTED** | **[~] S27. ⚠ S29: VOLUNTEERED COLD AND UNPROMPTED as the reason his `zip` line works, with the set contrast attached. NO RATING TAKEN — that is the only thing between it and [x]** | **S30 — take the number FIRST** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE; `.clear()` → `None`, leaves `{}`** | **[~] NEW S27, untested** | **S29 cold** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[~] NEW S27, untested** | **S29** |
| hashable | hash must be STABLE ⇒ key must be immutable | [~] S26/S27, untested | **S29 cold** |
| `.get()` vs `[]` | `[]` when missing is a BUG; `.get()` when absence is EXPECTED | [~] S26, untested | **S29 cold** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[~] S26/S27. ⚠ S29: stated correctly BUT ONLY ON THE RE-ASK — he gave two of the three facts and skipped this one until it was re-issued unchanged. No rating** | **S30 cold** |
| **set** | **a dict with the values thrown away. Unique, unordered, hashable. `{}` is an empty DICT — use `set()`** | **[~] NEW S27, untested, no drill file** | **S29 cold, TASK-FIRST** |
| **set order instability** | **no first element — the same file printed three different orders in three runs** | **[~] S27. S29: volunteered as the CONTRAST to dict ordering, unprompted (*"unlike sets"*)** | **S30** |
| **`|` `&` `-` on sets** | **union / intersection / difference. All build a NEW set ⇒ EXPRESSIONS. `-` is NOT symmetric** | **[~] NEW S27, untested** | **S29 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?"** | **[~] NEW S27. ⚠ He could not produce the ASK question** | **S29** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell | a one-slot box; `__closure__` is a TUPLE | [x]-grade S25 | ~1 Sep |
| closure four layers | name → function object → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] **S28: an exhausted `zip` giving `[]` is another clean live example** | **S29** |
| THE FIVE CHECKS | "Boundary pe khaali ek bahar mila" — `bahar` = outside what you ASSUMED, sign AND type | [x] S25 | ~1 Sep |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[~] ⚠⚠ **S29: THE FIRST CLEAN ONE IN FOUR.** A boundary was planted and DECLARED, and he wrote strict `<` / `>` correctly in all four copies of the rule. ⚠ CAVEAT: he did not write the tests, so this is correct CODE, not the testing HABIT** | **S30 — plant one UNDECLARED** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14 cold; S27 unaided off a real traceback; **S28 read `<module>` again on three live tracebacks** | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided. **⚠ S28 gave it fresh relevance: the comprehension's own namespace** | [~] **overdue — and now has a live example** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps | owed. **S28 touched the edge: `str()` is called FOR you inside an f-string** | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 + S27 (`dict.pop`) + **S28 (`[print(j) ...]` → `[None, None, None]`)** | [x] — gauntlet, then ~11 Sep |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day; S26 dict; S27 set | [~] due ~5 Sep |
| **Iteration protocol** | **S25 PASSED COLD. ⚠ S28: it was the named prerequisite for comprehensions, and it carried the whole unit — including WHY an exhausted `zip` returns `[]`** | **[x] — the gate it unblocked has now been used** |
| Iterator causation | S22/S23 | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass. **S28: `StopIteration` shown being CAUGHT rather than surfacing** | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong; S27 loop `else` handled it | [~] label re-test |
| Traceback: each line = one live frame | S27 PASSED COLD 8/10; **S28 three more reads** | [x] — gauntlet, then ~15 Sep |
| **`while` mechanics; nested loops; found-flag** | **NOT tested in S27, S28 or S29** | **[~] S30 — three sessions overdue** |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, `drills/s27_flow.py`, 20/20 | [x] — gauntlet, then ~15 Sep |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged |
| Mutable/immutable discriminator | S18/S24/S26/S27 | [x] type half; tell half [~] **S29** |
| Cell causation | S22 pass 7/10 | [x] — ~31 Aug |
| Closure definition + application | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes; **S29** |
| Recursion | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| Five checks | S25 5/5 COLD; **⚠ S27 missed a `None`-as-both-sentinel bug; S28 missed a boundary** | [x] — **gauntlet, re-test with TYPE and BOUNDARY specifically** |
| Argument count ⊥ return value | S20 confusion; S26 one-object half | [~] ~16 Sep |
| **`global` / `*args`/`**kwargs`** | **S22 pass 10/10 and 8/10. ⚠ S29 BUILD BLOCK: `*args`, `**kwargs`, `*args` AFTER a positional, and `*tuple` UNPACKING at a call site — all four written cold and correct** | **[x] CONFIRMED — the protection is discharged, use freely now** |
| Compile-time locality TRAP in a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| Docstrings / `__doc__` | S25 cold, 6/10 | [x] — ~1 Sep |
| **Indexing / slicing** | **S24 taught; NOT re-tested in S25–S28 — FOUR sessions overdue** | **[~] — cold S29, with shallow copy** |
| **TUPLE (whole unit)** | **S26 taught. ⚠ Declared for S27 AND S28, run in neither** | **[~] — cold S29, TASK-FIRST, PRIORITY** |
| **DICT (whole unit)** | **S26 two-thirds + S27 tail. ⚠ The S26 two-thirds has never been cold-tested** | **[~] — cold S29, TASK-FIRST, PRIORITY** |
| **SET (whole unit)** | **S27 taught in full, same-session, no drill file** | **[~] — cold S29, TASK-FIRST** |
| **COMPREHENSIONS (list + dict)** | **S28 taught. ⚠⚠ DRILL NOW DEFERRED TWICE (S28→S29→S30). NOT his doing either time — S29 was consumed by the mentor's spec churn** | **[~] — cold S30, TASK-FIRST, FIRST TEACHING THING** |
| **`zip`** | **S29 PROMOTED — used unprompted, cold, to solve an unseen design problem; 13/13** | **[x] — gauntlet (short-gap), then ~7 Sep** |
| **f-strings + format spec** | **S28 taught. S29: WRITTEN COLD and correctly in `report()`, columns aligned first run — applied, never asked** | **[~] — ONE cold ask promotes; S30** |
| **Four-station hook + Station 0** | **S27 ran; S28 five-for-five. ⚠ S29: NOT FIRED ONCE — nothing raised all session** | **[~] — S30, build a raising snippet in deliberately** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S29 HEADLINE, AND IT IS A STUDENT ONE: HE FOUND `zip` HIMSELF.**
  The build block was designed around a hole — `*args` delivers angles
  anonymously, `**kwargs` delivers limits by name, and nothing pairs them.
  **S27 and S28 were both deliberately steered away from `*args`/`**kwargs`
  to protect that measurement, and the mentor was under standing instruction
  not to mention `zip`.** He wrote `for angle_value, limits_key in zip(angles,
  limits)` cold, the day after learning `zip`, and it is correct for three
  stacked reasons he then produced on the mechanism question. **This is the
  first time in the file that a construct taught the previous session was
  DEPLOYED against a novel problem rather than recited. That is the whole
  point of the course, observed once, cleanly.**
- ⚠ **NEW WATCH AREA, OPENED S29: COPY-PASTE AS A DESIGN METHOD.** The clamp
  rule is written out FOUR times in 46 lines. `report()` is `clamp_joints()`
  with prints swapped in — **and it still carries the dead `clamped_joint_angles
  = {}` that it never fills and returns**, so `safe = report(...)` silently
  hands back `{}`. He diagnosed the cause himself and without prompting
  (*"i picked up the code from previous block and didn't modify it properly"*)
  and proposed the right fix (*"one function that does all that calculation"*).
  **The gap is not the diagnosis; it is that nothing in his process caught it
  before he called the work done.** ⚠ Note the pytest angle, which is the real
  lesson and was delivered: **the suite stayed 13/13 GREEN** because `report`
  was never tested. Duplication is how the untested copy quietly stops matching
  the tested one.
- ⚠ **DEPTH-BEFORE-ANSWER — FIRED TWICE IN S29, BOTH RECOVERED. FOURTEEN AND
  FIFTEEN STRAIGHT, ZERO FAILURES.** (a) Asked for the failure mode of a
  four-way duplication, he answered with the FIX instead. (b) Re-asked, he
  answered in five-checks vocabulary (*"failure mode will be Boundary... bahar"*)
  — **the DESIGN-SWITCHING pattern in its purest form yet: substituting a
  question he can answer in owned vocabulary for the one asked.** Countermeasure
  held both times: name the substitution, re-issue the ORIGINAL question
  unchanged, narrow it until it is derivable. **THE RE-ASK IS THE INTERVENTION.
  Do not re-teach.**
- **Term/label retention.** ⚠ **S29 collected almost no label data — nothing
  raised, so the S27 error-naming rule never fired.** One language correction
  issued: he defined `zip` as pairing "lists", corrected to **ITERABLES**, with
  the reason that mattered (his own line passes a tuple and a dict, neither of
  which is a list). Mechanism excellent, as always.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL (opened S28) — S29 ADDS A
  CANDIDATE.** He wrote nested same-type quotes inside an f-string
  (`f"...{"angles" if ... else "limits"}..."`) which is a **SyntaxError on
  ≤3.11 and legal only from 3.12 (PEP 701)**. It ran because he is on 3.12.3.
  He almost certainly does not know he wrote something version-gated.
  **Audit list stands: `len()`, `range()` as an object, `print()`'s return
  value, `.append()` vs `+`, `import`.**
- **CONFIDENCE CALIBRATION: ONE rating taken in S29 (`zip`, 8/10).** The
  dict-iteration rating was asked twice and never given — **the second ask was
  mis-phrased by the mentor (two facts bolted into one question), he said so,
  and the re-phrased ask was then dropped when he moved on.** Do not read it as
  refusal; it was fatigue at the end of a badly-run session. **Take it in S30 —
  it is the only thing standing between dict ordering and [x].**
- **Honest-gap declaration remains reliable.** S29: *"I am not sure about the
  pytest, you haven't taught that yet"* — flagged mid-answer, correctly, and
  he was right.
- **⚠⚠ MENTOR WATCH AREA — THE WORST SESSION IN THE FILE, AND IT NEEDS TO BE
  READ AS SUCH.** S28 produced three framing failures. **S29 produced ONE
  failure repeated four times, and it burned roughly half the session before
  the student could write a line of code.** The build-block spec was issued in
  four versions: (v1) no exercise at all, just "the design is yours"; (v2) five
  levels in pure prose, not one concrete number; (v3) concrete numbers, still
  no signature; (v4) exact signatures, exact expected values — **and he started
  immediately.** Three pushbacks, escalating from a question to *"lets call
  this off"* to open anger, **all three upheld.**
  **THE ROOT CAUSE, stated plainly: the mentor was protecting a puzzle at the
  student's expense, and re-derived the same wrong answer three times because
  it never checked the premise.** The premise was that giving the signature
  would give away the problem. **It was false — the design hole lived in the
  function BODY.** He proved it by solving that body cold within an hour of
  being handed the signature.
  ⚠ **THE COST WAS NOT ONLY TIME. The timer was abandoned, so block 01 has no
  duration measurement; `LOG.md` was never written, so it has no process
  record; and no teaching happened at all.** A measurement instrument that
  takes four attempts to describe is not an instrument.
  ⚠ **SECOND MENTOR ERROR, CAUGHT BY HIM AND SERIOUS: THE SPEC REQUIRED HIM TO
  WRITE PYTEST TESTS. Pytest has never been taught and STATE.md:363 said so in
  as many words.** That is the NINTH define-before-building breach and the
  exact shape of the S18 `d.clear()` breach. **He caught it before writing a
  line. Had he not, the entire block would have been unmeasurable.** Remedy
  applied in session: the mentor wrote `test_clamp.py` (13 tests), verified it
  ran against a throwaway stub, and deleted the stub. **STANDING: the mentor
  writes every test file in this course.**
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 48 raised, 47 upheld or
  part-upheld.** S29 raised THREE and all three were upheld: (46) the spec is
  abstract, give a concrete problem; (47) I still cannot see the exact problem,
  and *"you are not helping at all"*; (48) **you are expecting me to write
  tests — we haven't learnt that.** ⚠ **(48) is the most valuable pushback on
  his record: it is not a process catch, it is him auditing the instrument
  against the file's own rules and finding a hole that would have invalidated
  the measurement.**
- ⚠ **A CHANNEL ARTEFACT WORTH REMEMBERING: he read a stale VS Code MARKDOWN
  PREVIEW (Ctrl+Shift+V) that had cached an older render, and spent two turns
  frustrated at a spec already fixed on disk.** Disk was verified (2,907 bytes,
  17:37) and the preview was the liar. **Same lesson as the S15 stale master:
  an artefact that looks authoritative while being wrong is worse than one that
  is missing.** He asked what the discrepancy was rather than assuming — which
  is the correct instinct and should be said back to him.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised — ⚠ S28
  gave it a live face: `0.1 + 0.2` → `0.30000000000000004`, shown and
  explicitly parked)**; 32/64-bit; `globals()`/`locals()` drill; senior
  traceback read (1.9); .pyc (1.10); GIL (1.13); concurrency (post-Layer 1);
  certifications; GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **S28 NOTE: generator EXPRESSIONS `(x for x in y)` were deliberately NOT
  shown even though they would have proved a point, because they are untaught.
  They belong here.**
- ⚠ **PEP 709 / how comprehension scope is actually implemented (hidden
  function pre-3.12, inlined from 3.12) — NEW S28, Level 3, parked to 1.13.**
- **`reversed()`** — still owed in 1.8.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **`copy.deepcopy` and the `copy` module** — still owed inside "nested data
  structures" in 1.8.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 model is the course target; HOW the
  number is computed, COLLISIONS and RESIZING are DSA, master Layer 8. **Reuse
  the S27 exchange as the template for future "how deep here?" questions.**
- **HASH RANDOMISATION** — per-process seed, a security measure. Park to 1.13.
- ⚠ **`%` and `.format()` string formatting** — NEW S28. f-strings were taught
  as the modern form; the two older forms exist in every codebase he will read
  and were not shown. **Owed as a READING skill, not a writing one.**

---
