# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 23 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S22
#      (Mon 17 Aug 2026). Later day → cold work is promotable.
#   3. SECOND ACTION: run the TERM-TAX. It was NOT run in S22 despite a
#      valid later-day gap — mentor miss, logged. Many rows are overdue.
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 22, Monday 17 Aug 2026. Next: Session 23.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S22 yield: 1.7 FULLY TAUGHT AND CLOSED** (lambdas + docstrings, the last
  two items) **plus SIX ledger promotions to [x]** — the biggest promotion day
  since S16, and the first under the new promotion-on-correctness rule.
- Position: 1.1–1.7 closed. **1.8–1.13 remain, ~6 weeks. 1.8 opens S23** and
  is several times the size of 1.6 — count the 31 Aug arithmetic in items.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- Current Layer: 1. Current Topic: **1.8 Data Structures — opens S23.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- (empty — nothing proposed in S22, nothing adopted)
- Two S21 operational decisions were SETTLED in S22 (not rules, recorded here):
  **(a) First weekly cold build block: THIS WEEKEND, Sat 22 or Sun 23 Aug**,
  his pick on the day. ≥90 min, timed, no AI, git+pytest, work-adjacent
  (LeRobot episode validator or joint-limit clamp). **Hold him to it.**
  **(b) Queue tooling = a SCRIPT in this repo** (not Anki): stores items +
  due dates, prints today's queue. Build incrementally; candidate task for
  the weekend block itself.

## WHERE WE LEFT OFF

### SESSION 23 STARTS HERE — exact resume point

S22 ran Monday 17 Aug 2026, the day after S21 — first genuine later-day
session since S19, and the queue finally got paid. **Six promotions: post-order
transfer (10/10, clean frame trace), cell causation (7/10), `global` (10/10,
via drill), `*args`/`**kwargs` (8/10, via drill), `__defaults__` (7/10 —
PRODUCED COLD FOR THE FIRST TIME IN FIVE ATTEMPTS), iterator causation (5/10,
bug-first, promoted with a SHORT gap under the new rule).** The repo's first
two drills were written and passed pytest (`drills/s22_counter.py` 3/3,
`drills/s22_report.py` 4/4). Lambdas and docstrings taught → **1.7 CLOSED.**
Zero pushbacks raised (denominator: 0/0). One mentor miss: **term-tax skipped
on a valid later day** — run it first thing in S23.

Run in this order:

1. **TERM-TAX — OWED AND OVERDUE.** Sweep the overdue rows (~12–15 Aug dues)
   plus the new S22 terms: lambda, docstring/`__doc__`, pre-/post-order,
   `UnboundLocalError` (HE MUST TYPE IT — spelled it wrong twice in S22),
   iterator-vs-iterable label, the closure four layers.

2. **[RECALL] ITERATOR CAUSATION — his 5/10 bought a short gap, so it fires
   again NOW.** Bug-first ALWAYS (hoisted `it = iter(range(2))`); never the
   definition. S22 was the first later-day pass (forward-only state, no
   "one-at-a-time" relapse). A second clean pass here makes it solid before
   the gauntlet.

3. **[RECALL] CLOSURE DEFINITION, COLD — FAILED S22 at 5/10.** He had nesting
   + free variable but MUDDLED THE LAYERS (called `cell_contents` a tuple)
   and MISSED THE SURVIVAL CLAUSE. Target line: *a function object that binds
   a free variable from its enclosing scope into a cell, so the value
   survives after the enclosing frame has died.* Also listen for: binding
   when `def` RUNS; `__closure__` is `None` with no free variables. The
   four-layer walk (name → function object → `__closure__` tuple →
   cell → `cell_contents`) was retaught via the shelf/dabba handle and his
   teach-back was clean — test it cold now.

4. **[RECALL] LAMBDAS + DOCSTRINGS — first cold pass, TASK-FIRST in drills/.**
   Good constraints: sort a list of strings case-insensitively / by computed
   value WITHOUT defining a named helper (forces lambda as `key=`); a module
   whose functions must carry runtime-readable documentation checked via
   `__doc__` (forces docstring placement). Then the mechanism questions:
   lambda = EXPRESSION form of a function, one-expression body, auto-return;
   docstring = first statement, stored on `__doc__` at `def` time,
   comment-vs-docstring (comment discarded, docstring is data);
   `f.__doc__` is `None` when absent, NOT `""`.

5. **[RECALL] TRACEBACK — repaired S22, one honest line-item still open.**
   S22: he tied each line to A FRAME (the S20 content held) but called it
   "the problematic line" — corrected to *one live frame frozen at the line
   it was executing; for callers that line is the call itself*. His a→b→c
   teach-back was correct. Ask cold: "what is one line of a traceback?"

6. **THEN OPEN 1.8 — LISTS FIRST.** Cash in the S17 discriminator by name
   (this is where the mutating-methods ROSTER gets owned). Teach SLICING
   formally — he has flagged it untaught himself (pushback 25); `word[:-1]`
   and `l[::-1]` are seen-but-not-taught. `zip` and list comprehensions
   likewise owed here. The iteration protocol (S15) is the machinery under
   comprehensions — say so when they open.

7. **WEEKEND: the first cold build block (Sat 22 / Sun 23).** If S23 runs
   before the weekend, confirm the day with him at close.

**Standing turn rules: short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — traces
never optional, five checks on every drill (HE DID NOT REPORT RUNNING THEM on
the two S22 drills — require it explicitly next drill), boundary values
first. Tag every block. Do not propose ending the session.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x]; the `if`/`elif`/`else` and S18 exception-triad
  promotions; the 1.6 spoken Feynman recall; the S22 promotions flagged
  short-gap (iterator causation, `__defaults__`, cell causation).
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- ⚠ Audit the [~] list for the traceback defect (asked-but-never-taught)
  before the gauntlet.
- Three-error set (`TypeError`/`NameError`/`UnboundLocalError`) still untested
  cold — MIXED, never singly. Include the SPELLING of UnboundLocalError.
- Modulo identity SYMBOLIC FORM still owed cold. TEXT, low priority.
- `str` immutability is an [x] candidate — one clean later-day pass.
  `None`/`is None` and `bool("False")` remain [~].
- **Keyword argument** (defined S21) still owed its first cold test.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 23 closes with a ~30-second spoken summary from memory.


## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
**⚠ NOT RUN IN S22 (mentor miss) — many rows overdue. Sweep in S23.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined between types; `"5"+3` | [x] S18 | ~10 Sep |
| truncation | cut off; `int()` drops decimals toward zero | [~] S13 pass | **OVERDUE — S23** |
| floor division | `//` floors toward −∞; `-7//2 → -4` | [~] S13 pass | **OVERDUE — S23** |
| alias | two names, one object | [~] S13 pass | **OVERDUE — S23** |
| rebind | `=` points a NAME at an object | [~] S13 pass | **OVERDUE — S23** |
| operand | value an operator acts on | [~] S13 pass | **OVERDUE — S23** |
| expression vs statement | value vs action | [~] held in use S17 | **OVERDUE — S23** |
| precedence / associativity | rank; direction on ties, `**` right→left | [~] S13 pass | **OVERDUE — S23** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | `a == b*(a//b) + (a%b)`; sign follows divisor | [~] formula form never cold | low priority, TEXT |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] S14 pass | **OVERDUE — S23** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep (in words, never typed) |
| iterable | able-to-be-iterated; hands out iterators; REUSABLE | [x] S16 | ~9 Sep |
| iterator | the nozzle; forward-only; CONSUMED | label slipped again S22 ("inner iterable exhausted") | fold into S23 term-tax |
| StopIteration | the stop signal; an EXCEPTION | [x] S18 | ~10 Sep |
| forward-only state (iterator causation) | position only moves forward — THAT is why consumed | **[x] PROMOTED S22 — first later-day pass, bug-first, no relapse. 5/10 = short gap.** | **S23 + gauntlet. Bug-first ALWAYS.** |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| traceback | crash report on uncaught exception; each line = one live frame | [~] repaired S22 (frame link held, "problematic line" skew fixed) | S23, then gauntlet |
| NameError | the NAME does not exist anywhere | [x] S18 | ~10 Sep, MIXED with ValueError |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [~] | **OVERDUE — S23** |
| `while` / `break` / `continue` | condition re-checked; exit loop; kill iteration | [~]; `continue` owes a RECALL | **OVERDUE — S23** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| loop `else` | ran without `break` | [~] earned S17 | **OVERDUE — S23** |
| `pass` | no-op filling a block that cannot be empty | [~]; test the pass/continue/break 3-way | **OVERDUE — S23** |
| ternary | EXPRESSION: `x if cond else y`, evaluates to a value | [~] | **OVERDUE — S23** |
| elif | chain, first true wins, rest never evaluated | [x] S17 | ~10 Sep |
| keyword argument | `name=value` in the CALL, matched by NAME | [~] defined S21, never tested | S23 |
| UnboundLocalError | name IS local (compile-time), no value bound yet | [~] mechanism [x]-grade; **SPELLED WRONG TWICE S22 ("UnboundError", lowercase l)** | S23 — he TYPES it; then mixed 3-error test |
| mutating vs non-mutating | in-place mutators return `None`; check TYPE first | discriminator [x]; ROSTER settles in 1.8 | 1.8 |
| **pre-order / post-order** | **work before the call / after the call** | **NEW S22 — mechanism [x] (10/10 trace), LABEL was a gap; decoded in session** | **S23 term-tax** |
| **lambda** | **EXPRESSION form of a function; one-expression body, auto-return. Brute-force label (Greek λ)** | **NEW S22, [~]** | **S23 task-first** |
| **docstring / `__doc__`** | **doc-string decodes; first statement of body, stored on `__doc__` at `def` time; absent = `None` not `""`** | **NEW S22, [~]** | **S23 task-first** |
| **`key=`** | **sorted calls it once per element, ONE argument, sorts by RESULTS, returns ORIGINAL items** | **NEW S22 (re-taught from S19), [~]** | **S23** |
| **closure four layers** | **name → function object → `__closure__` TUPLE → CELL → `cell_contents`** | **NEW S22 — muddled twice in session, teach-back clean after shelf/dabba handle** | **S23, inside the closure-definition recall** |
| **None-as-absence vs empty container** | **collectors give `()`/`{}` (empty thing exists); optional attributes give `None` (never created)** | **NEW S22, [~] — his `""` guess for absent `__doc__`** | **S23** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] due 29 Aug |
| `<module>` entry point; running vs paused; stack not queue | S14 pass cold | [~] due 29 Aug |
| Namespace vs frame | S14 not unaided | [~] due 29 Aug |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **DUE — overdue badly** |
| Rebinding vs mutation; `==` vs `is`; implicit/explicit conversion; mutability+aliasing; shallow/deep copy; comparison ops; precedence; `+=`; negative `//`; `%` negatives; `**`; if-block scope; range(); function scope | all PROMOTED S16 | [x] — gauntlet + ~9 Sep |
| `str` immutability | S17 supporting evidence | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps (`bool("False")`, `10/2` float) | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S18: concept owned, roster assumed | [~] roster settles in 1.8 |
| **`__defaults__` — attribute on the function object, built at `def` time, a TUPLE** | **S22 PRODUCED COLD, FIRST TIME IN FIVE ATTEMPTS, 7/10. PROMOTED.** | **[x] — re-test ~31 Aug (gauntlet) then ~17 Sep** |
| Membership `in`/`not in` | S13 same-day | [~] due ~5 Sep |
| Short-circuit | S14 pass | [~] one more pass promotes |
| Iteration protocol (`iter()` once, `next()` per pass) | S15 same-day only | [~] due ~8 Sep |
| **Iterator causation (forward-only state)** | **S22 PASS later-day, bug-first, unaided. PROMOTED at 5/10.** | **[x] — SHORT GAP: re-fire S23, then gauntlet. Bug-first always.** |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong (`ValueError`) | [~] label re-test |
| **Traceback: each line = one live frame** | **S22 first honest test: PARTIAL — frame link held, "problematic line" skew corrected, a→b→c teach-back correct** | [~] S23 cold ask, then ~16 Sep |
| `print()` returns `None`; `sep`/`end` | S16 | [~] ~9 Sep |
| `while` mechanics; `continue`-skips-update trap; nested loops; loop `else`; found-flag; `pass`; ternary | S16/S17 | [~] ~9–10 Sep |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged, ~10 Sep |
| Mutable/immutable discriminator | S18 pass + corrected the rule | [x] ~10 Sep |
| **Cell causation (five calls, five cells, no collision)** | **S22 PASS 7/10 + tricky follow-up (same-arg calls → separate cells: the CALL creates the object). PROMOTED. `cell_contents` spelling fixed.** | **[x] — ~31 Aug, then ~17 Sep** |
| **Closure definition (one line)** | **S22 FAILED at 5/10 — layers muddled, survival clause missing. Clean line handed after; four-layer walk retaught (shelf/dabba), teach-back clean.** | **[~] PRIORITY — cold S23** |
| Recursion: base/recursive case, frames stacked | S20 same-day | [~] ~16 Sep |
| **Pre-order vs post-order (transfer)** | **S22 PASS 10/10 — full four-frame trace, the S20 one-mutating-n error did NOT recur. PROMOTED. Labels were a gap → term queue.** | **[x] — gauntlet, then ~17 Sep** |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| Five checks | S20 transfer on first use; **not visibly run on S22 drills** | [~] REQUIRE explicitly next drill |
| Argument count ⊥ return value | S20 category confusion | [~] ~16 Sep |
| Trace-tail truncation | S17 did not fire | [~] watch, require final cycle |
| **`global` (compile-time locality; read/mutate/rebind)** | **S22 PASS via task-first drill (3/3 pytest) + full mechanism unaided, 10/10. PROMOTED. Evidence: `drills/s22_counter.py`.** | **[x] — gauntlet, then ~17 Sep** |
| **`*args`/`**kwargs` (collect/unpack mirror, empty cases)** | **S22 PASS via drill (4/4 pytest) + mirror stated both ways, 8/10. PROMOTED. Evidence: `drills/s22_report.py`.** | **[x] — ~7 Sep** |
| **Compile-time locality TRAP inside a closure (`start = start + 1` kills the cell)** | **S22: predicted 11 (MISS), repaired unaided when pointed at the line** | **[~] NEW — re-test; it is the `nonlocal` motivation for 1.13** |
| **Lambdas** | **taught S22; [PREDICT]s passed (closure transfer 15, squares sort); two-param question his own** | **[~] first cold test S23, task-first** |
| **Docstrings / `__doc__`** | **taught S22; [PREDICT] miss on absent case (`""` for `None`) → discriminator taught** | **[~] first cold test S23, task-first** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** fires on BOREDOM as well as friction (S17). Ran in
  reverse in S18 (protected ledger integrity over wanted topic). Weakening;
  not closed. **Not observed S20–S22.**
- **Term/label retention — first-class watch area.** S22 evidence BOTH ways:
  mechanisms promoted six times, while labels slipped four times (pre/post-order
  gap, "UnboundError" twice, "inner iterable" for iterator, `cell_content`).
  The countermeasure works on decodable labels (S18 exception triad holds);
  arbitrary labels (traceback, lambda, `__defaults__` history) need
  brute-force spaced repetition. **His own self-diagnosis in S22: "if not used
  for long I tend to forget terminology" — accurate.**
- **Right answer / wrong or missing mechanism:** standing audit; S22 was
  CLEAN — every promoted answer carried its mechanism.
- **Wrong-domain / surface-syntax flaw** (most persistent, ~S4–S15): not
  observed S22.
- **Depth-before-answer:** S22 first answer to the post-order recall was
  output-only; the trace came complete on ONE re-ask. Keep re-asking.
- **Layer-muddle (NEW, S22): tuple/cell/cell_contents confused twice in one
  session** — watch it in the closure re-test; shelf/dabba handle repaired it.
- Five checks not yet self-initiated on drills — require verbally until he
  runs them unprompted.
- False attribution: his record stands 26 pushbacks, zero wrong. When he says
  a rule broke, check the rule.

## CURIOSITY PARKING LOT (unchanged S22 except as noted)
- venv; VS Code practices; notebooks; JIT; IEEE 754 (1.13, promised); 32/64-bit;
  `globals()`/`locals()` drill; senior traceback read (1.9); .pyc (1.10); GIL
  (1.13); concurrency (post-Layer 1); certifications (not scheduled); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff
- Recursion + nested functions — DELIVERED (S18–S20). Line retired.
- `reversed()` / `l[::-1]` — lands in 1.8 slicing, next session
- **NEW S22: lambdas with `*args` (parameter list works like `def`'s) — noted
  in passing when he asked about two-parameter lambdas; nothing owed, the
  question was answered in session.**

---
