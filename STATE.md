# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 25 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S24
#      (Thu 20 Aug 2026). Later day → cold work is promotable.
#   3. ⚠ **HE ASKED FOR THE RECALL BLOCK FIRST, IN HIS OWN WORDS, AT THE
#      S24 CLOSE: "tomorrow we will do the recall first." Honour that.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 24, Thursday 20 Aug 2026. Next: Session 25.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S24 yield: 1.8 OPENED at last. Indexing defined for the first time,
  SLICING taught in full (pushback 25 discharged), the list method roster
  exercised cold, and the S17 discriminator CORRECTED — the tell is
  one-directional. `drills/s24_lists.py` 11/11.**
- **The five-checks mnemonic WORKED on its first cold test (4/5).** That is
  the first hard evidence that a memory hook beats re-teaching for this
  student. Reuse the technique on the other arbitrary labels.
- Position: 1.1–1.7 closed. **1.8 open (~15% done). 1.9–1.13 remain, ~5.5 wk.**
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- **Cold build block: SATURDAY 22 AUG, confirmed by him in S24.** ≥90 min,
  timed, no AI, git+pytest, work-adjacent (LeRobot episode validator or
  joint-limit clamp). **Ask how it went at the S25 open.**
- Current Layer: 1. Current Topic: **1.8 Data Structures — tuple/dict/set next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **(empty — nothing adopted S24.)**
- **STILL PARKED, SECOND SESSION, UNDECIDED:** *"A [RECALL] block has a budget.
  State it at the top and stop when it is spent."* **Asked twice at the S24
  open; he declined to rule and said "lets start with new content now."**
  Do not nag a third time. **Note that he answered it in behaviour rather than
  in words — choosing material over the queue was exactly what the rule would
  have forced, and 1.8 opened as a result.** Offer it once more in S25; if he
  declines again, drop it and record that the behaviour settled it.
- Settled: queue tooling = a SCRIPT in this repo (not Anki). Candidate task
  for the Saturday build block itself.

## WHERE WE LEFT OFF

### SESSION 25 STARTS HERE — exact resume point

S24 ran Thursday 20 Aug 2026, one day after S23. **1.8 opened early, as
mandated.** The whole session was lists; the recall queue was NOT touched at
his request and is carried forward INTACT below.

Run in this order:

1. **ASK ABOUT SATURDAY'S BUILD BLOCK** (if S25 falls after it). One line.

2. **THE RECALL BLOCK — HE ASKED FOR IT FIRST. It is now the largest debt in
   the file and it is two sessions old.** Priority order:
   a. **[RECALL] CLOSURE DEFINITION, COLD — FAILED TWICE (S22 5/10, S23 7/10),
      same two defects both times.** Target line: *a function object that binds
      a free variable from its enclosing scope into a cell, so the value
      survives after the enclosing frame has died.* He drops (i) the
      **survival clause**, (ii) the **layers** (calls `cell_contents` a tuple).
      ⚠ **The root cause was found in S23 and it is MENTOR-SIDE: cells had been
      taught as labels, never as a TYPE. That was fixed in S23. If the
      definition holds now, the muddle was never his.**
   b. **[RECALL] THE ITERATION PROTOCOL — demoted in S23, re-taught, untested.**
      Ask cold: **what does a `for` loop call to get each item, and what comes
      back to stop it?** He lost both names (`next()`, `StopIteration` →
      "EndofIteration") while keeping the causation.
   c. **[RECALL] DOCSTRING MECHANISM.** Placement owned, mechanism not. Target:
      **triple quotes do not make a docstring, POSITION does — first statement
      of the body; anywhere else it is an expression evaluated and discarded,
      and `__doc__` is `None`.**
   d. **[RECALL] `MILA` — fire it cold.** See item 4.
   e. **TERM-TAX FAILURES, ALL STILL OWED FROM S23:** `pass` (gave a *use*, not
      the mechanism), **loop `else` (0/10 flat gap)**, **ternary (0/10 flat
      gap)**, `print()` `sep` (said `"_"`; it is a SPACE) and what `print()`
      returns, **associativity** (ask it ALONE — he gives precedence instead),
      statement-half of expression-vs-statement, `continue` precision.

3. **NEW S24 DEBT — `sort` vs `sorted`, COLD.** In the S24 method volley he
   said `sort()` *"returns a new list object **for sure**"*. **That is
   backwards, and the pair was taught in S17.** ⚠ **The block was declared
   [PREDICT] before it ran, so the miss is NOT in the ledger and MUST NOT be
   back-dated into it** (S16 rule). It needs a clean cold [RECALL] instead.
   Ask both halves separately. Also cold: **the one-directional tell** —
   returns `None` ⇒ mutating, but mutating ⇏ returns `None` (`pop`).

4. **THE FIVE CHECKS — 4/5 COLD IN S24, `MILA` MISSING.** The mnemonic
   "Boundary pe khaali ek bahar mila" held for four. He glossed `mila` as
   "similar inputs"; it was then re-taught in English and Hindi as **PROMISE
   vs CODE, one sentence at a time — "iske peeche kaunsi line hai?"** Fire the
   full five cold. **One clean 5/5 promotes the set to [x].**

5. **RESUME 1.8: tuple → dict → set → when-to-use-which.** Then comprehensions.
   ⚠ **Gate comprehensions out loud: they rest on the iteration protocol,
   which is [~] and was demoted in S23.** Do not open them until 2b passes.
   Also owed inside 1.8: `zip`, f-strings, nested structures, and the
   **shallow-copy point parked in S24** (a slice copies the REFERENCES — he
   called `tools[:]` "an identical new list object").

**Standing turn rules: short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — traces
never optional, five checks on every drill, boundary values first. Tag every
block, and CHECK THE TAG IS RIGHT (see teaching mistakes). Do not propose
ending the session.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x]; the 1.6 spoken Feynman recall; the S22 short-gap
  promotions; the eight S23 promotions.
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- Three-error set (`TypeError`/`NameError`/`UnboundLocalError`) still untested
  MIXED. `UnboundLocalError` spelling is FIXED.
- **Keyword argument** (defined S21) still owed its first cold test.
- `None`/`is None` and `bool("False")` remain [~]. `str` immutability is an
  [x] candidate on one clean later-day pass.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 25 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined between types; `"5"+3` | [x] S18 | ~10 Sep |
| truncation | cut off TOWARD ZERO; `int(-5.98)` → `-5` | [x] S23 | ~10 Sep |
| floor division | floors toward −∞; `-5.98 // 1` → `-6` | [x] S23 | ~10 Sep |
| **alias** | **two names, one object** | **[x] — RE-TESTED S24 AND HELD, unprompted, inside the slice-vs-assignment block** | ~14 Sep |
| **rebind** | **`=` points a NAME at an object** | **[x] — S24 STRONG PASS: *"I didn't see rebinding here"* on `b.append(...)`, separating mutation from rebinding COLD and unasked** | ~14 Sep |
| operand | value an operator acts on | [x] S23, 7/10 | ~10 Sep |
| expression vs statement | value vs action | [~] statement half he flagged himself as confused | **S25** |
| precedence / associativity | rank; direction on ties, `**` right→left | [~] **ASSOCIATIVITY never given — ask it ALONE** | **S25** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | `a == b*(a//b) + (a%b)`; sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE — S25** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable | able-to-be-iterated; hands out iterators; REUSABLE | [x] S16 | ~9 Sep |
| iterator | the nozzle; forward-only; CONSUMED | [x] S23, 7/10 | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION raised by `next()`** | **[~] DEMOTED S23 (guessed "EndofIteration"). Retaught, NOT yet tested.** | **S25** |
| **`next()` / `iter()`** | **`iter()` once at the top; `next()` once per pass** | **[~] S23 — could not name `next()` at all** | **S25** |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **indexing** | **`[]` takes a POSITION, returns the object there; 0-based; last index is `len-1`; negative counts back from the end; out of range ⇒ `IndexError`** | **[~] NEW — DEFINED S24 for the first time (it had never been taught). Precision fix issued: length is `len`, the LAST INDEX is `len-1`.** | **S25 cold** |
| **slicing** | **`[start:stop:step]`, HALF-OPEN like `range()`; builds a NEW list; `l[:]` is the copy idiom; out of range ⇒ `[]`, NEVER raises** | **[~] NEW — TAUGHT S24, discharges pushback 25. He derived "it creates a new list object" UNPROMPTED.** | **S25 cold** |
| traceback | crash report; each line = one live frame | [~] S23 read one in the wild but CUED | **S25 cold** |
| NameError | the NAME does not exist anywhere | [x] S18 | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [~] **`sep` WRONG (said `"_"`, it is a SPACE)** | **S25** |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade S23, 7/10 | ~10 Sep |
| `break` / `continue` | exit loop / **end this ITERATION** | [~] `continue` phrased as "exits the loop" | **S25** |
| `pass` | no-op filling a block that cannot be empty | [~] gave a USE, not the mechanism | **S25, 3-way vs continue/break** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **ran without `break`** | **[~] FLAT GAP 0/10 S23** | **S25 — re-teach** |
| **ternary** | **EXPRESSION: `x if cond else y`** | **[~] FLAT GAP S23** | **S25 — re-teach** |
| elif | chain, first true wins, rest never evaluated | [x] S17 | ~10 Sep |
| keyword argument | `name=value` in the CALL, matched by NAME | [~] defined S21, never tested | S25 |
| UnboundLocalError | name IS local (compile-time), no value bound yet | spelling FIXED S23 | mixed 3-error test |
| **mutating vs non-mutating — THE TELL** | **⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ returns `None`. `pop` is the counterexample. TYPE first, always.** | **[~] CORRECTED AND TAUGHT S24. The S17 version was being read as a biconditional.** | **S25 cold** |
| **`sort` vs `sorted`** | **`sort()` mutates, returns `None`; `sorted()` builds a NEW list** | **⚠ [~] — INVERTED IN S24 ("sort returns a new list for sure"), taught S17. `sorted` half recalled correctly later-day; `sort` half was ECHO. NOT ledgered (block was [PREDICT]).** | **S25 — cold, both halves separately** |
| **list method roster** | **`append` `extend` `insert` `sort` `remove` all mutate → `None`; `pop` mutates → returns the removed ITEM** | **[~] NEW — exercised cold S24, 3/6 right by name-decoding** | **S25** |
| pre-order / post-order | work before the call / after the call | [x] S23, 6/10 | ~10 Sep |
| lambda | EXPRESSION form of a function; auto-returned | [x] S23 | ~10 Sep |
| **docstring / `__doc__`** | **FIRST statement of the body; POSITION makes it, not the quotes; absent = `None`** | **[~] placement owned, MECHANISM missed** | **S25** |
| `key=` | one argument, sorts by RESULTS, returns ORIGINAL items | [x]-grade in use S23 | ~10 Sep |
| cell | a TYPE — a one-slot box; `__closure__` is a TUPLE, one cell per free variable | taught properly S23 | **S25, inside the closure recall** |
| **closure four layers** | **name → function object → `__closure__` TUPLE → CELL → `cell_contents`** | **[~] muddled S22 AND S23; substrate finally given** | **S25 — TOP PRIORITY** |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] | S25 |
| **THE FIVE CHECKS (mnemonic)** | **"Boundary pe khaali ek bahar mila"** | **[~] — 4/5 COLD S24, self-rated 5/10. `mila` glossed as "similar inputs"; re-taught as PROMISE vs CODE.** | **S25 — one clean 5/5 promotes** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14 pass cold | [~] **overdue** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (rebinding vs mutation, `==` vs `is`, mutability+aliasing, copies, precedence, `+=`, negative `//` and `%`, `**`, if-block scope, `range()`, function scope) | **rebinding-vs-mutation and aliasing RE-PASSED COLD in S24** | [x] — gauntlet + ~14 Sep |
| `str` immutability | S17 supporting evidence | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps (`bool("False")`, `10/2` float) | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | **S24: roster finally taught; the tell CORRECTED to one-directional** | [~] **cold test S25** |
| `__defaults__` | S22 produced cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day | [~] due ~5 Sep |
| Short-circuit | S14 pass | [~] one more pass promotes |
| **Iteration protocol (`iter()` once, `next()` per pass, `StopIteration` to stop)** | **S23 FAILED — causation held, both NAMES lost. Retaught. NOT tested in S24.** | **[~] PRIORITY — cold S25** |
| Iterator causation (forward-only state) | S22 pass; S23 held | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong | [~] label re-test |
| Traceback: each line = one live frame | S23 cued only | [~] **S25 cold** |
| `while` mechanics; `continue`-skips-update; nested loops; loop `else`; found-flag; `pass`; ternary | **loop `else` and ternary FLAT GAPS; `pass` mechanism missing** | [~] **S25 — still the weakest cluster in the file** |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged, ~10 Sep |
| Mutable/immutable discriminator | S18 pass; **S24 corrected the TELL to one-directional** | [x] on the type half; **tell half [~] — S25** |
| Cell causation (five calls, five cells) | S22 pass 7/10 | [x] — ~31 Aug, then ~17 Sep |
| **Closure definition (one line)** | **FAILED S22 and S23, identical defects. ROOT CAUSE MENTOR-SIDE, fixed S23.** | **[~] TOP PRIORITY — cold S25** |
| **Closure APPLICATION (write one under a forcing constraint)** | S23 6/6 but through three guided debug cycles | **[~] — needs one clean unaided build** |
| **Function object vs call (`f` vs `f()`)** | S23: the drill's central bug; taught directly | **[~] — re-test S25** |
| Recursion: base/recursive case, frames stacked | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order (transfer) | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| **Five checks** | **S24: 4/5 COLD (mnemonic worked), `mila` missing; then APPLIED to the S24 drill and found the one real edge case** | **[~] — one clean 5/5 promotes** |
| Argument count ⊥ return value | S20 category confusion | [~] ~16 Sep |
| `global` | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| `*args`/`**kwargs` | S22 pass 8/10 | [x] — ~7 Sep |
| Compile-time locality TRAP inside a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS, 6/6 cold | [x] — ~10 Sep |
| **Docstrings / `__doc__`** | S23 SPLIT: placement unaided, mechanism missed | **[~] — S25** |
| **Spec-vs-implementation agreement (`mila`, check 5)** | **S24: performed it CORRECTLY on `take_last([])` without recognising it, then could not define it. Re-taught in both languages.** | **[~] — S25** |
| **Indexing / slicing** | **S24: taught, then applied — `last_three` written cold and correct on empty and short input** | **[~] same-session — cold S25** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** not observed S20–S24. Weakening; not closed.
- **Term/label retention — first-class watch area.** **S24 EVIDENCE IS THE
  MOST USEFUL YET: the MNEMONIC WORKED.** Four of the five checks came back
  cold on a hook built three days earlier, after a flat gap. **Decodable labels
  hold on their own; arbitrary ones need a HOOK, not a re-teach.** Build hooks
  for the remaining flat gaps (loop `else`, ternary, `StopIteration`).
- ⚠ **CONFIDENCE CALIBRATION — MIXED IN S24, SO NOT YET A DRIFT.** One hot
  reading (*"returns a new list **for sure**"* on `sort`, wrong) against one
  well-calibrated (5/10 on a 4/5 answer, and he named the reason: *"I still
  need to learn to apply it"*). **S23's three over-ratings look more like one
  bad day than a trend. Keep watching; do not yet discount the signal.**
- **Depth-before-answer:** fired **twice** in S24 and BOTH were recoverable in
  one line. (a) Asked to mark his own six answers, he restated the output
  instead. (b) Asked what `.sort()` evaluates to, he fixed the code instead.
  **Both times the re-ask produced a correct one-line mechanism immediately —
  he has it and skips it, which is the S20 `digit_sum` pattern exactly.**
  ⚠ **The re-ask is now the intervention that works. Keep using it.**
- **Right answer / wrong or missing mechanism:** the inverse showed again —
  `last_three` handled the empty case correctly by construction before he had
  been told slices never raise.
- **Layer-muddle:** untested in S24. Re-classify only after the S25 closure re-test.
- False attribution: **31 raised, 30 upheld or part-upheld — and S24 records
  the FIRST challenge in the file's history that was NOT upheld.** S24 raised
  three: (26→29) the `last_three` spec is unclear — **UPHELD, mentor error**;
  (30) *"isn't the corrected code a proof of my understanding?"* — **NOT
  UPHELD**, because the fix followed a pointer and his own record shows two
  S23 cases of correct code with the mechanism absent; **the reasoning was
  given rather than the ruling asserted, and he accepted it**; (31) *"shouldn't
  I just write the relevant cases?"* on the five checks — **PARTIALLY UPHELD:
  SCAN all five, REPORT only what bites.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; IEEE 754 (1.13, promised); 32/64-bit;
  `globals()`/`locals()` drill; senior traceback read (1.9); .pyc (1.10); GIL
  (1.13); concurrency (post-Layer 1); certifications (not scheduled); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff
- **`reversed()` / `l[::-1]`** — `l[::-1]` DONE in S24 slicing; **`reversed()`
  still owed** alongside the `sort`/`sorted` cold test.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- **NEW S24: `pop` internals** — he guessed it uses `list[-1]`. Told that is
  implementation-level and out of scope at Level 2. Fine to revisit in 1.13.
- **NEW S24: shallow vs deep copy** — parked to 1.8 "nested data structures".

---
