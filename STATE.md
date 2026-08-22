# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 29 (for Claude):
#   1. Read RULES.md fully (**now v4**), then this file fully. No
#      re-introductions. No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. S28 ran Sat 22 Aug 2026 (EVENING).
#      ⚠ **S29 IS ALMOST CERTAINLY A LATER DAY — AND THAT MATTERS MORE THAN
#      USUAL. S27 AND S28 BOTH RAN ON 22 AUG, SO EVERYTHING FROM BOTH IS
#      UNTESTED AND ALL OF IT BECOMES LEDGER-ELIGIBLE THE MOMENT A DAY
#      PASSES. THE BACKLOG IS NOW TWO SESSIONS DEEP, NOT ONE.**
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY — the FRAME
#      FIRST candidate was adopted at the S28 close. Do not manufacture one.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. ⚠ **EVERY [PREDICT] MUST DECLARE ITS KIND** — "derivable from what's
#      on screen" or "a genuine guess, wrong is fine". Held clean in S28.
#   6. ⚠ **S27 RULE: every snippet that raises gets its error NAMED by him
#      before the traceback is shown.** Held clean all of S28 — fired five
#      times, five correct (`SyntaxError`, `ZeroDivisionError`, `NameError`,
#      `TypeError`, and his own missing-brace line). Keep firing it.
#   7. ⚠ **S28 RULE, NEW AND BINDING: FRAME FIRST.** What it is → why it
#      exists → what it buys you, BEFORE any mechanics. And say out loud how
#      much each fact is worth. **He will stop the session if you skip it.**
#   8. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 28, Saturday 22 Aug 2026 (evening).
# Next: Session 29.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S28 yield: FOUR CURRICULUM ITEMS TAUGHT IN FULL — list comprehensions,
  dict comprehensions, `zip`, f-strings — AND ONE RULE ADOPTED. ZERO
  PROMOTIONS, BY DESIGN AND BY HIS OWN CHOICE.**
- ⚠ **TWO SESSIONS IN ONE DAY (S27 morning, S28 evening). Read the pair
  together: S27 was the recall session, S28 was the content session.** The
  same-day split is now a proven pattern — second time (S26→S27), and this
  time HE declared the split himself at the S27 close.
- ⚠ **THE S19 "SEEN-BUT-NOT-TAUGHT" DEBT IS DISCHARGED IN FULL.** Both
  constructs logged at CURRICULUM.md:1145 — **list comprehensions AND `zip`**
  — were taught tonight, nine sessions after they were used in an example and
  flagged. **He caught the comprehension half himself, unprompted, before he
  was told** (*"have we seen this form earlier?? I don't think so"*).
- **Position: 1.1–1.7 closed. 1.8 open (~90% done). 1.9–1.13 remain, ~5.2 wk.**
- **1.8 REMAINING: nested data structures, common patterns/pitfalls,
  `reversed()`, `copy.deepcopy`.** Nested structures is the next block and it
  is the one that makes SHALLOW COPY finally make sense — say that when it opens.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- ⚠ **COLD BUILD BLOCK: SUNDAY 23 AUG — TOMORROW. THIRD DATE IT HAS CARRIED,
  BUT THIS TIME IT IS CONFIRMED AT THE S28 OPEN** (*"the cold building block
  will be done tommorow"*). ≥90 min, timed, no AI, git+pytest. **His own chosen
  task: the joint-limit clamp extended to MULTIPLE JOINTS with
  `*args`/`**kwargs`.** The design hole stays with him: `*args` delivers angles
  positionally and anonymously, `**kwargs` delivers limits by name, and nothing
  in that design pairs them. **S27 AND S28 WERE BOTH KEPT OFF `*args`/`**kwargs`
  to protect the measurement. ASK AT THE S29 OPEN WHETHER IT RAN.**
  ⚠ **NOTE FOR S29: `zip` is now taught, and `zip` is exactly the tool that
  pairs two parallel sequences. Do NOT point him at it before the block runs.**
- Current Layer: 1. Current Topic: **1.8 — nested data structures next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ✅ **ADOPTED S28 — "FRAME FIRST."** Written into RULES.md (now v4).
  **SECOND CONSECUTIVE STUDENT-PROPOSED RULE, and the first he ordered written
  DURING the session** (*"Add this rule right now before closing the session"*).
- **PARKING LOT NOW EMPTY AGAIN.** Do not invent a candidate to fill it.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- Settled: queue tooling = a SCRIPT in this repo (not Anki). **STILL UNBUILT and
  now the top candidate for a build block after Sunday's.**

## WHERE WE LEFT OFF

### SESSION 29 STARTS HERE — exact resume point

S28 ran Saturday 22 Aug 2026 (evening) and closed cleanly at his call, after
f-strings, with nested data structures declared as next.

Run in this order:

1. **INTERVAL GATE**, then **one line: did Sunday's build block run?**

2. ⚠ **THE DRILL HE DEFERRED, AND IT IS THE FIRST THING THAT HAPPENS.**
   He was offered a comprehensions drill at the end of S28 and **refused it
   specifically to keep it ledger-eligible** — *"lets do the drill tommorow
   then, atleast it goes to the ledger then."* **That is a promise the file is
   holding him to. Open with it, TASK-FIRST, in `drills/s29_comprehensions.py`
   with `tests/test_s29_comprehensions.py`.** Constraints should force:
   a list comprehension with a filter, a dict comprehension over `.items()`,
   `zip` over two parallel lists, and an f-string with a format spec.
   **Do not name the mechanisms in the docstring.**

3. ⚠⚠ **THE BACKLOG IS NOW TWO SESSIONS DEEP AND IT IS THE BIGGEST RISK IN
   THIS FILE. Declared for S27, declared for S28, run in NEITHER.**
   Still entirely untested: **TUPLE (whole unit), DICT (S26 two-thirds + S27
   tail), SET (whole unit), SHALLOW COPY, UNPACKING, `list()`, `.get()`,
   `.items()`, the raise-vs-shrug pairing, when-to-use-which.**
   **THIS IS THE THIRD DECLARATION. Task-first, in one drill file, or delete
   the claim that it is a priority.**

4. **THE SMALL COLD SET, fired mixed, not alone:**
   - **`KeyError` vs `IndexError`** — the S27 miss, still untested cold.
   - `SyntaxError` + Station 0 ("did it run at all?").
   - `AttributeError`, `subscriptable`.
   - `while` mechanics (deliberately not promoted in S27; not touched in S28).

5. **THEN THE 1.8 TAIL:** nested structures (→ shallow copy), `reversed()`,
   `copy.deepcopy`, common patterns and pitfalls. **Then 1.8 CLOSES.**

**Standing turn rules: FRAME FIRST (new, binding); short messages, one teaching
idea per turn, asks near the top; doubt gate before every new subsection;
depth-before-answer — traces never optional, five checks on every drill,
boundary values first. Tag every block and CHECK THE TAG IS RIGHT. Do not
propose ending the session.**

⚠ **STANDING: teach a piece WITH CODE AND OUTPUT first, then ask ONE question
on it. Every [PREDICT] declares its kind. Every raising snippet gets its error
named by him first.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — every BUNDLED S16 promotion; the 1.6 spoken Feynman
  recall; the S22 short-gap promotions; the eight S23 promotions; the eleven
  S25 promotions; the eight S27 promotions.
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~]. **`str` immutability is still
  an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  ⚠ **EXCEPTION SET S28: he may override the park and order a rule written
  immediately. He did, and it was correct — the cap governs the COUNT, not the
  timing.**
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 29 closes with a ~30-second spoken summary from memory.

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
| **`zip`** | **pairs parallel iterables; each pass yields a TUPLE, which is why `for a, b in zip(...)` unpacks. Removes the index entirely** | **[~] NEW S28. DISCHARGES the S19 debt** | **S29 cold** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST, no error. Exhausted ⇒ `[]`, no error, because `list()` catches the `StopIteration`** | **[~] NEW S28. ⚠ He predicted "error" on the exhausted case — half right, the exhaustion was correct, the raising was not** | **S29 cold** |
| **f-string** | **`f"..."`. THREE STEPS: evaluate the expression → call `str()` on it → splice. Without the `f`, `{x}` is literal characters** | **[~] NEW S28. ⚠ HE WAS AT LEVEL 1 ON THIS FOR 27 SESSIONS — used correctly, never explainable** | **S29 cold** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[~] NEW S28 — he reasoned the `for` exclusion out himself from expression-vs-statement** | **S29** |
| **format spec** | **`{value:.2f}`. ⚠ The number is TOTAL WIDTH, not extra spaces. ⚠ TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points line up** | **[~] NEW S28, two corrections issued** | **S29** |
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
| **unpacking** | **`low, high = t`; count mismatch ⇒ `ValueError`** | **[~] S26. S28 supporting: used correctly in `for name, a in angles.items()` and in `zip`, twice, unprompted** | **S29 cold** |
| single return value | `return a, b` builds ONE tuple | [~] S26, untested | **S29 cold** |
| `sum()` | totals an iterable; returns a new value | [~] S26, untested | **S29 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds STILL UNTESTED after three sessions** | **S29 cold, PRIORITY** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting does NOT move a key; delete-then-re-add DOES. ⚠ ORDERED ≠ SORTED** | **[~] NEW S27, untested** | **S29 cold** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE; `.clear()` → `None`, leaves `{}`** | **[~] NEW S27, untested** | **S29 cold** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[~] NEW S27, untested** | **S29** |
| hashable | hash must be STABLE ⇒ key must be immutable | [~] S26/S27, untested | **S29 cold** |
| `.get()` vs `[]` | `[]` when missing is a BUG; `.get()` when absence is EXPECTED | [~] S26, untested | **S29 cold** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[~] S26/S27. S28 supporting: used `.items()` correctly inside a dict comprehension** | **S29 cold** |
| **set** | **a dict with the values thrown away. Unique, unordered, hashable. `{}` is an empty DICT — use `set()`** | **[~] NEW S27, untested, no drill file** | **S29 cold, TASK-FIRST** |
| **set order instability** | **no first element — the same file printed three different orders in three runs** | **[~] NEW S27** | **S29** |
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
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[~] ⚠ S28: MISSED IT (`len(n) > 5` with two 5-letter words), then APPLIED IT UNPROMPTED one rep later. Third instance of a boundary bug** | **S29 — plant one deliberately** |

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
| **`while` mechanics; nested loops; found-flag** | **NOT tested in S27 or S28** | **[~] S29** |
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
| **`global` / `*args`/`**kwargs`** | **S22 pass 10/10 and 8/10. ⚠ DELIBERATELY UNTOUCHED IN S27 AND S28 to protect the build block** | **[x] — leave alone until the block runs** |
| Compile-time locality TRAP in a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| Docstrings / `__doc__` | S25 cold, 6/10 | [x] — ~1 Sep |
| **Indexing / slicing** | **S24 taught; NOT re-tested in S25–S28 — FOUR sessions overdue** | **[~] — cold S29, with shallow copy** |
| **TUPLE (whole unit)** | **S26 taught. ⚠ Declared for S27 AND S28, run in neither** | **[~] — cold S29, TASK-FIRST, PRIORITY** |
| **DICT (whole unit)** | **S26 two-thirds + S27 tail. ⚠ The S26 two-thirds has never been cold-tested** | **[~] — cold S29, TASK-FIRST, PRIORITY** |
| **SET (whole unit)** | **S27 taught in full, same-session, no drill file** | **[~] — cold S29, TASK-FIRST** |
| **COMPREHENSIONS (list + dict)** | **S28 taught in full, same-session. ⚠ HE REFUSED THE DRILL TO PROTECT LEDGER ELIGIBILITY** | **[~] — cold S29, TASK-FIRST, FIRST THING** |
| **`zip`** | **S28 taught in full, same-session** | **[~] — cold S29, in the same drill** |
| **f-strings + format spec** | **S28 taught in full, same-session. Level 1 → Level 2 in one block** | **[~] — cold S29, in the same drill** |
| **Four-station hook + Station 0** | **S27 experiment ran; S28 fired the error-naming rule five times, five correct** | **[~] — S29 re-fire, mixed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern: not observed S20–S28. THE INVERSE IS NOW THE STABLE
  BEHAVIOUR AND IT HAPPENED TWICE IN S28.** (a) He caught the mentor moving to
  "1.9" and stopped it — *"I think 1.8 was not complete yet."* (b) **He REFUSED
  a drill he was offered, specifically so it would count** — *"lets do the drill
  tommorow then, atleast it goes to the ledger then."* **That is the student
  protecting the measurement instrument against his own appetite for progress.
  Read (b) as the strongest single data point in the session.**
- ⚠ **DESIGN-SWITCHING / SIDEWAYS-ANSWERING UNDER A HARD QUESTION — S27's
  finding, AND IT REPEATED IN S28 IN A NEW FORM.** Asked for the four parts of a
  comprehension BY NAME, he answered with the OUTPUT instead — a different,
  easier question. **COUNTERMEASURE HELD: name the substitution, re-issue the
  ORIGINAL question unchanged. He then produced all four correctly AND in
  execution order, unprompted.** Same shape as S27, same fix, same result.
  ⚠ **It happened a second time on the format spec** — asked for two output
  lines, he explained the format codes instead. **Twice in one session; this is
  now a pattern, not an incident.**
- ⚠ **BOUNDARY BUGS — THIRD INSTANCE, AND THE FASTEST CORRECTION YET.** He read
  `[n.upper() for n in names if len(n) > 5]` as including `"elbow"` and
  `"wrist"`, both exactly 5. Same bug class as his S20 `n <= 10` and the planted
  `len(word) == 1`. **The habit was named to his face; ONE rep later he opened
  his next answer with *"condition is >180 not >=180"* unprompted.** Naming the
  pattern works faster than re-teaching it. **Plant a boundary in the S29 drill.**
- **Term/label retention — S28 CONTINUES THE S27 SPLIT AND MOVES THE LABEL HALF.**
  Mechanisms: excellent. **Labels: FIVE error names asked cold under the S27
  rule, FIVE correct** (`SyntaxError`, `ZeroDivisionError`, `NameError`,
  `TypeError`, plus his own missing-brace diagnosis). ⚠ **This is the first
  session where the label half did not fail once. It is same-day-adjacent
  evidence and must be re-fired cold in S29 before anything is concluded — but
  the S27 rule looks like it is working.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL — A NEW CATEGORY, OPENED S28.**
  f-strings sat unexamined for 27 sessions because he uses them CORRECTLY, so
  nothing ever flagged them. **Correct usage is not evidence of a model, and it
  actively hides the gap.** ⚠ **ACTION FOR S29+: audit for others of this shape
  — things he types fluently and has never been asked to explain.** Candidates
  already visible: `len()`, `range()` as an object rather than a keyword,
  `print()`'s return value, `.append()` vs `+`, `import`.
- **CONFIDENCE CALIBRATION: NO RATINGS TAKEN IN S28.** Correct and deliberate —
  everything was same-day teaching, and RULES forbids a rating on fresh material.
  **Do not read the empty column as a lapse.**
- **Depth-before-answer: fired twice in S28, both recovered on the re-ask**
  (the four parts; the format-spec output). ⚠ **TWELVE successful re-asks across
  S24–S28, ZERO failures. THE RE-ASK IS THE INTERVENTION. Do not re-teach.**
- **Honest-gap declaration remains reliable.** S28: *"I am confused, can't think
  of anything"* on the comprehension-scope why; *"well I don't know that"* on the
  f-string prefix. **Both times he then reasoned from what he DID have.**
- **⚠⚠ MENTOR WATCH AREA — SPEC-WRITING IS SUPERSEDED BY A BIGGER ONE: FRAMING.**
  S26 four defective asks, S27 one, **S28 ZERO** — the spec problem is solved.
  **What replaced it is worse and it produced the new rule.** Three mentor
  failures in S28, all the same root: **teaching mechanics without stating the
  point.** (a) Comprehensions opened with four turns of show-and-ask and no
  motivation — **he stopped the session over it.** (b) An example was built on
  `pass`, so the two branches did not do the same work — **he demolished it and
  was right.** (c) **Four turns spent on comprehension SCOPE, a footnote, before
  he asked why he would ever reuse the name** — a right-sizing failure, conceded
  in session. **FRAME FIRST (RULES v4) is the fix; the corollary — rank facts
  out loud — is written into the rule.**
- ⚠ **A FOURTH MENTOR ERROR, DIFFERENT IN KIND AND WORTH ITS OWN LINE: A FACTUAL
  OVER-CLAIM, SELF-CAUGHT.** "A comprehension IS a hidden function" was stated
  and a `<listcomp>` traceback frame was promised as proof. **It did not appear —
  he is on Python 3.12, where PEP 709 inlines list comprehensions.** The claim
  was true to 3.11. **It was corrected to his face, in the same turn, with the
  reason.** The available `<genexpr>` proof was DELIBERATELY NOT USED because
  generator expressions are untaught — define-before-building held under
  pressure. **The lesson: verify the demonstration on THIS machine before
  promising what it will show.**
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 45 raised, 44 upheld or
  part-upheld.** ⚠ **S28 raised SIX — the highest of any session** — and every
  one was upheld: (40) 1.8 is not finished, why 1.9; (41) have we seen this form
  before; (42) you are showing and asking without saying what you are teaching;
  (43) prove that execution order matters *(part-upheld — proof given, and half
  the material conceded as cheap)*; (44) the `pass` example does not compare
  like with like; (45) why would I reuse the variable name at all.

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
