# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 24 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S23
#      (Wed 19 Aug 2026). Later day → cold work is promotable.
#   3. SECOND ACTION: the TERM-TAX. Run it — S23 swept most of the backlog,
#      so S24's volley is SHORT. Do not let it eat the session again.
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 23, Wednesday 19 Aug 2026. Next: Session 24.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S23 yield: the two-session term-tax backlog CLEARED, eight promotions, two
  drills passed, and LAMBDAS closed to [x]. 1.8 DID NOT OPEN.**
- ⚠ **1.8 has now slipped a session. It was the S23 plan and the recall backlog
  ate it.** That was the right call once — the backlog was two sessions deep —
  but it cannot happen twice. **1.8 OPENS IN S24, early, before any long
  recall block.**
- Position: 1.1–1.7 closed. **1.8–1.13 remain, ~5.5 weeks.**
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- Current Layer: 1. Current Topic: **1.8 Data Structures — opens S24.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **(empty — nothing adopted S23.)**
- **PARKED CANDIDATE, raised by the mentor, for the student to decide in S24:**
  **"A [RECALL] block has a budget. State it at the top and stop when it is
  spent."** S23 spent roughly two-thirds of the session on the recall queue and
  1.8 never opened; S22 had the same shape. The counter-argument is real — the
  backlog was genuine and the closure gap it exposed was worth the time — which
  is why this is parked and not adopted. **His call.**
- Settled operational decisions still standing:
  **(a) First weekly cold build block: THIS WEEKEND, Sat 22 or Sun 23 Aug**,
  his pick on the day. ≥90 min, timed, no AI, git+pytest, work-adjacent
  (LeRobot episode validator or joint-limit clamp). **Hold him to it — it was
  NOT re-confirmed at the S23 close; confirm the day first thing in S24.**
  **(b) Queue tooling = a SCRIPT in this repo** (not Anki). Candidate task for
  the weekend block itself.

## WHERE WE LEFT OFF

### SESSION 24 STARTS HERE — exact resume point

S23 ran Wednesday 19 Aug 2026, two days after S22. The overdue term-tax was
swept in two waves, **eight promotions**, two drills written and passed
(`drills/s23_sort_key.py` 6/6, `drills/s23_ordering.py` 6/6 **cold on the
first attempt**), one demotion, and **one root cause found that had been
mis-attributed to the student for two sessions** (see the closure entry below).

Run in this order:

1. **CONFIRM THE WEEKEND BUILD BLOCK — Sat 22 or Sun 23.** One line, first
   thing. It was missed at the S23 close.

2. **OPEN 1.8 — LISTS FIRST. Do this EARLY, before any long recall block.**
   Cash in the S17 discriminator by name — **this is where the mutating-methods
   ROSTER finally gets owned rather than derived.** Teach SLICING formally (he
   flagged it untaught himself, pushback 25; `word[:-1]` and `l[::-1]` are
   seen-but-not-taught). `zip` and list comprehensions are owed here too and
   are marked seen-but-not-taught. The iteration protocol (S15) is the
   machinery under comprehensions — say so when they open.
   ⚠ **Prerequisite honesty: the iteration protocol is [~] and got WORSE in
   S23 (see item 4). Comprehensions rest on it. Gate them out loud.**

3. **[RECALL] CLOSURE DEFINITION, COLD — FAILED TWICE NOW (S22 5/10, S23
   7/10), SAME TWO DEFECTS BOTH TIMES.** Target line: *a function object that
   binds a free variable from its enclosing scope into a cell, so the value
   survives after the enclosing frame has died.* The two things he drops:
   (a) the **survival clause** — missing both times; (b) the **layers** —
   he called `cell_contents` a tuple both times.
   **DO NOT LOG A THIRD FAILURE WITHOUT READING THIS FIRST: the root cause was
   found in S23 and it is a MENTOR defect.** The four layers had been taught
   as a stack of labels; what a cell *is* was never taught. He asked directly —
   *"I am still unsure what a cell is, is it a memory cell?"* — and it was
   then taught properly: **a cell is a TYPE (`<class 'cell'>`), a one-slot
   box, and `__closure__` is a TUPLE because there is one cell PER FREE
   VARIABLE.** Shown with `type()` output and a two-free-variable example.
   **If the definition holds now, the muddle was never his.**

4. **[RECALL] THE ITERATION PROTOCOL — DEMOTED IN S23, RE-TEACH IS DONE, TEST
   IT.** He passed the *causation* (exhausted iterator → second loop prints
   nothing, zero body runs) but **could not name `next()` and guessed
   "EndofIterator" / "EndofIteration" for `StopIteration`.** `StopIteration`
   **reverts [x] → [~]** — failed re-test. Re-taught in S23 with the three-call
   demo and a real traceback. Ask cold: **what does a `for` loop call to get
   each item, and what comes back to stop it?**

5. **[RECALL] DOCSTRING MECHANISM — placement is owned, mechanism is not.**
   He documents functions correctly and unaided, but predicted `__doc__` would
   still return the string when it sits on the SECOND line of the body. It is
   `None`. The line to get back: **triple quotes do not make a docstring,
   POSITION does — first statement of the body, attached at `def` time;
   anywhere else it is an expression evaluated and discarded.**

6. **THE FIVE CHECKS — he now has a mnemonic; test that it survived.**
   He could not name a single one cold (they were taught S20 and transferred
   on first use — gone in three days). He then asked for a memory hook, and
   one was built with him: **"Boundary pe khaali ek bahar mila"** →
   Boundary / Khaali (empty-zero-nothing) / Ek (one) / Bahar (outside your
   assumption) / Mila (two things that must agree). Fire it cold in S24.

7. **STILL OWED FROM THE S23 TERM-TAX (all failed or gapped, all overdue):**
   `pass` (gave a *use*, not the mechanism), **loop `else` (0/10, flat gap)**,
   **ternary (0/10, flat gap)**, `print()` `sep` (said `"_"`; it is a single
   SPACE) and what `print()` returns, **associativity** (he gave precedence
   only, both times), statement-half of expression-vs-statement.

**Standing turn rules: short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — traces
never optional, five checks on every drill, boundary values first. Tag every
block. Do not propose ending the session.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x]; the 1.6 spoken Feynman recall; the S22 short-gap
  promotions (iterator causation, `__defaults__`, cell causation); the eight
  S23 promotions.
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- Three-error set (`TypeError`/`NameError`/`UnboundLocalError`) still untested
  MIXED. **Spelling of `UnboundLocalError` is FIXED — typed correctly in S23.**
- **Keyword argument** (defined S21) still owed its first cold test.
- `None`/`is None` and `bool("False")` remain [~]. `str` immutability is an
  [x] candidate on one clean later-day pass.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 24 closes with a ~30-second spoken summary from memory.


## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
**S23 swept the backlog. The rows below marked S24 are the FAILURES only.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined between types; `"5"+3` | [x] S18 | ~10 Sep |
| **truncation** | **cut off TOWARD ZERO; `int(-5.98)` → `-5`** | **[x] S23 — 7/10, then 10/10 on the direction discriminator vs `//`** | ~10 Sep |
| **floor division** | **floors toward −∞; `-5.98 // 1` → `-6`** | **[x] S23, 9/10** | ~10 Sep |
| **alias** | **two names, one object** | **[x] S23, 10/10** | ~10 Sep |
| **rebind** | **`=` points a NAME at an object** | **[x] S23, 10/10** | ~10 Sep |
| **operand** | **value an operator acts on** | **[x] S23, 7/10** | ~10 Sep |
| expression vs statement | value vs action | [~] S23: expression half correct, **statement half he flagged himself as confused** | **S24** |
| precedence / associativity | rank; direction on ties, `**` right→left | [~] S23 8/10: **precedence correct, ASSOCIATIVITY not given at all** | **S24 — ask associativity ALONE** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| **modulo identity** | **`a == b*(a//b) + (a%b)`; sign follows divisor** | **[x] S23 — PRODUCED COLD AND UNPROMPTED to prove `-13 % 10 == 7` while bug-hunting his own lambda. Owed since S13.** | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] S14 pass | **OVERDUE — S24** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable | able-to-be-iterated; hands out iterators; REUSABLE | [x] S16 | ~9 Sep |
| **iterator** | **the nozzle; forward-only; CONSUMED** | **[x] S23, 7/10 — the S22 label slip did NOT recur** | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION raised by `next()`** | **⚠ DEMOTED [x] → [~] S23. Guessed "EndofIterator"/"EndofIteration". Failed re-test.** | **S24 — retaught, test it** |
| forward-only state (iterator causation) | position only moves forward | [x] S22; S23 causation held, naming failed | gauntlet, bug-first |
| **`next()` / `iter()`** | **`iter()` once at the top; `next()` once per pass** | **[~] S23 — could not name `next()` at all. Retaught with the three-call demo + real traceback.** | **S24** |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **traceback** | **crash report; each line = one live frame** | **[~] S23 — read one correctly in the wild (named the error and the line it points at) but this was cued, not cold** | **S24 cold, then gauntlet** |
| NameError | the NAME does not exist anywhere | [x] S18 | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [~] S23 8/10: **`end` correct, `sep` WRONG (said `"_"`, it is a SPACE), return value not given** | **S24** |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade answer S23, 7/10 | ~10 Sep |
| `break` / `continue` | exit loop / **end this ITERATION** | [~] S23: `break` correct; **`continue` phrased as "exits the current loop" → precision fix issued** | **S24** |
| `pass` | no-op filling a block that cannot be empty | [~] S23 7/10 — **gave a USE ("we don't know the body yet"), not the mechanism; said so himself** | **S24, 3-way vs continue/break** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **ran without `break`** | **[~] S23 — FLAT GAP, 0/10** | **S24 — re-teach** |
| **ternary** | **EXPRESSION: `x if cond else y`** | **[~] S23 — FLAT GAP, could not retrieve it** | **S24 — re-teach** |
| elif | chain, first true wins, rest never evaluated | [x] S17 | ~10 Sep |
| keyword argument | `name=value` in the CALL, matched by NAME | [~] defined S21, never tested | S24 |
| **UnboundLocalError** | **name IS local (compile-time), no value bound yet** | **SPELLING FIXED — typed correctly, unaided, S23** | mixed 3-error test |
| mutating vs non-mutating | in-place mutators return `None`; check TYPE first | discriminator [x]; ROSTER settles in 1.8 | **1.8 — S24** |
| **pre-order / post-order** | **work before the call / after the call** | **[x] S23, 6/10 — both labels correct cold, the S22 gap closed** | ~10 Sep |
| **lambda** | **EXPRESSION form of a function; one-expression body, auto-returned** | **[x] S23 — two written cold in a drill (6/6 first attempt) + auto-return recalled unaided** | ~10 Sep |
| **docstring / `__doc__`** | **FIRST statement of the body; POSITION makes it, not the quotes; absent = `None`** | **[~] S23 — placement owned, MECHANISM missed (predicted the string on a second-line literal)** | **S24** |
| `key=` | called once per element, ONE argument, sorts by RESULTS, returns ORIGINAL items | **[x]-grade in use S23 (both drills), signature looked up not recalled** | ~10 Sep |
| **cell** | **a TYPE — a one-slot box; `__closure__` is a TUPLE with one cell per free variable; `.cell_contents` is the value inside** | **⚠ NEWLY TAUGHT PROPERLY S23. Previously taught as labels only — that is why the layers collapsed twice.** | **S24, inside the closure recall** |
| **closure four layers** | **name → function object → `__closure__` TUPLE → CELL → `cell_contents`** | **[~] — muddled AGAIN S23 (same error as S22), then the substrate was finally given** | **S24** |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] S22; **reinforced S23 via `plain.__closure__` → `None` and absent `__doc__` → `None`** | S24 |
| **THE FIVE CHECKS (mnemonic)** | **"Boundary pe khaali ek bahar mila"** | **[~] — could not name ONE cold in S23 despite S20 transfer; mnemonic built with him afterwards** | **S24 — fire the mnemonic cold** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] due 29 Aug |
| `<module>` entry point; running vs paused; stack not queue | S14 pass cold | [~] due 29 Aug |
| Namespace vs frame | S14 not unaided | [~] due 29 Aug |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (rebinding vs mutation, `==` vs `is`, mutability+aliasing, copies, precedence, `+=`, negative `//` and `%`, `**`, if-block scope, `range()`, function scope) | all PROMOTED S16 | [x] — gauntlet + ~9 Sep |
| `str` immutability | S17 supporting evidence | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps (`bool("False")`, `10/2` float) | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S18: concept owned, roster assumed | [~] **roster settles in 1.8 — S24** |
| `__defaults__` | S22 produced cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day | [~] due ~5 Sep |
| Short-circuit | S14 pass | [~] one more pass promotes |
| **Iteration protocol (`iter()` once, `next()` per pass, `StopIteration` to stop)** | **S23 FAILED — causation held, both NAMES lost. Retaught with live traceback.** | **[~] PRIORITY — cold S24** |
| Iterator causation (forward-only state) | S22 pass; S23 causation held under a new bug shape | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong | [~] label re-test |
| Traceback: each line = one live frame | S22 partial; **S23 read one correctly in the wild, but cued** | [~] S24 cold, then ~16 Sep |
| `while` mechanics; `continue`-skips-update; nested loops; loop `else`; found-flag; `pass`; ternary | **S23: `while`/`for` distinction PASSED; loop `else` and ternary FLAT GAPS; `pass` mechanism missing** | [~] **S24 — this cluster is the weakest thing in the file** |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged, ~10 Sep |
| Mutable/immutable discriminator | S18 pass + corrected the rule | [x] ~10 Sep |
| Cell causation (five calls, five cells) | S22 pass 7/10 | [x] — ~31 Aug, then ~17 Sep |
| **Closure definition (one line)** | **S23 FAILED AGAIN, 7/10 — identical two defects as S22. ROOT CAUSE IS MENTOR-SIDE (see resume item 3).** | **[~] TOP PRIORITY — cold S24** |
| **Closure APPLICATION (write one under a forcing constraint)** | **S23: `drills/s23_sort_key.py` reached 6/6, but through THREE guided debug cycles — missing argument, call-vs-object, missing `abs()`. Not unaided.** | **[~] — needs one clean unaided build** |
| **Function object vs call (`f` vs `f()`)** | **S23: the drill's central bug. Two Socratic attempts failed; taught directly. `key=f()` runs it NOW.** | **[~] NEW — re-test S24** |
| Recursion: base/recursive case, frames stacked | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order (transfer) | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| **Five checks** | **S23: could not name one cold (GAP). Applied them well WITH the list in hand and found a real bug. Mnemonic now exists.** | **[~] — fire the mnemonic cold S24** |
| Argument count ⊥ return value | S20 category confusion | [~] ~16 Sep |
| Trace-tail truncation | S17 did not fire | [~] watch |
| `global` | S22 pass 10/10, `drills/s22_counter.py` | [x] — gauntlet, then ~17 Sep |
| `*args`/`**kwargs` | S22 pass 8/10, `drills/s22_report.py` | [x] — ~7 Sep |
| Compile-time locality TRAP inside a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| **Lambdas** | **S23 PASS — `drills/s23_ordering.py`, 6/6 cold first attempt, unaided. PROMOTED.** | **[x] — ~10 Sep** |
| **Docstrings / `__doc__`** | **S23 SPLIT: placement unaided and correct; mechanism (first-statement rule) MISSED.** | **[~] — S24** |
| **Spec-vs-implementation agreement (check 5, generalised)** | **S23 NEW: his docstring said "last digit", his code said `% 10`; they disagree for `-13`. He judged BOTH partly wrong and said the contract should be explicit — a mature answer.** | **[~] strong first showing** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** not observed S20–S23. Weakening; not closed.
- **Term/label retention — first-class watch area.** S23 evidence both ways:
  **eight promotions** (including labels that had slipped before —
  iterator, pre/post-order) against **two flat gaps** (loop `else`, ternary)
  and **one demotion** (`StopIteration` → guessed name). Decodable labels are
  holding; arbitrary ones still need brute-force spacing. **`UnboundLocalError`
  spelling is now FIXED.**
- ⚠ **CONFIDENCE CALIBRATION RAN HOT — NEW, S23, and it matters because his
  ratings had been a usable targeting signal for six sessions.** Three
  over-ratings in one session: 8 on precedence with associativity entirely
  missing; 8 on `sep`/`end` with `sep` wrong; **7 on a closure definition that
  repeated both of S22's defects.** Named to him in session. **Watch whether
  this was one bad day or a drift; if it drifts, the rating stops being usable
  for setting re-test intervals.**
- **Depth-before-answer:** ⚠ **fired hard in S23.** The five-checks report was
  asked FOUR times — once as item 1 at the top of a short message — and skipped
  each time; he answered the mechanism question instead and moved on. Named to
  him directly. **He also declared the first drill "works" without running it;
  it crashed on the next line.** RUNNING IT IS PART OF THE ANSWER.
- **Layer-muddle:** recurred S23 (`cell_contents` called a tuple, second
  session running) — **but the root cause is now known to be mentor-side.**
  Re-classify only after the S24 re-test.
- **Right answer / wrong or missing mechanism:** S23 showed the *inverse* and
  it is worth naming — **working code with the mechanism absent** (docstrings
  placed correctly with no idea why; lambdas written correctly before the
  auto-return rule was stated). Task-first recall makes this visible; it did
  not used to be.
- False attribution: **28 pushbacks, zero wrong.** S23 raised three: syntax
  lookup is legitimate (upheld); "we haven't studied unit testing" (partially
  upheld — pytest is a harness he only runs, testing is not taught); **"why
  didn't you tell me all this when you used `cell` the first time" (UPHELD,
  and it found a real two-session mis-attribution).**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; IEEE 754 (1.13, promised); 32/64-bit;
  `globals()`/`locals()` drill; senior traceback read (1.9); .pyc (1.10); GIL
  (1.13); concurrency (post-Layer 1); certifications (not scheduled); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff
- `reversed()` / `l[::-1]` — lands in 1.8 slicing, **next session**
- **NEW S23: unit testing / pytest as a SUBJECT.** He correctly observed it has
  never been taught — he only runs the command. Not scheduled in Layer 0;
  say so plainly if it comes up again, and keep using pytest as a harness.
- **NEW S23: `nonlocal`** — surfaced implicitly by the closure locality trap.
  Belongs to 1.13. Do not open early.

---
