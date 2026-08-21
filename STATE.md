# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 26 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S25
#      (Fri 21 Aug 2026). Later day → cold work is promotable.
#   3. ⚠ **HE GAVE AN EXPLICIT INSTRUCTION AT THE S25 CLOSE:
#      "next session should start without recall actually studying 1.8
#      further." HONOUR IT. Open on 1.8 CONTENT — tuple → dict → set.
#      The four cold tests owed (item 2) are fired LATER in the session,
#      not at the open. Do not lead with a recall block.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 25, Friday 21 Aug 2026. Next: Session 26.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S25 yield: THE RECALL BLOCK IS CLEARED. ELEVEN PROMOTIONS on cold later-day
  evidence — the largest single-session promotion count in the file's history.**
  Closures (definition AND a 10/10 unaided build), the whole iteration protocol,
  `StopIteration`, docstrings, the five checks, `sort`/`sorted`, the
  one-directional tell, `continue`, `print()` sep/end/returns.
- **ONE DEMOTION, and it matters more than the eleven: ASSOCIATIVITY [x] → [~].**
  Promoted S16 bundled with precedence, never once tested alone; asked alone and
  cold in S25 it came back **"gap"**. **Audit the other bundled S16 promotions at
  the August gauntlet — this is exactly what the gauntlet is for.**
- **THE HOOK TECHNIQUE IS NOW CONFIRMED, NOT PROVISIONAL.** The five checks came
  back 5/5 after being 4/5, and `mila` — a flat gap in S24 — was recovered. Four
  new hooks were built in S25 for the remaining flat gaps. **Re-teaching failed
  these items repeatedly; hooks did not. This is the S25 finding.**
- Position: 1.1–1.7 closed. **1.8 open (~15% done). 1.9–1.13 remain, ~5.5 wk.**
- **COMPREHENSIONS ARE UNBLOCKED.** They were gated on the iteration protocol,
  which is now [x]. The gate can be declared open in S26.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- **Cold build block: SATURDAY 22 AUG — i.e. TOMORROW as of the S25 close.**
  ≥90 min, timed, no AI, git+pytest. **He chose the task himself in S25: the
  joint-limit clamp extended to MULTIPLE JOINTS with `*args`/`**kwargs`.** One
  design hole was named and deliberately left unanswered: `*args` delivers
  angles positionally and anonymously, `**kwargs` delivers limits by name, and
  nothing in that design pairs them. **ASK HOW IT WENT AT THE S26 OPEN.**
- Current Layer: 1. Current Topic: **1.8 Data Structures — tuple/dict/set next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **(empty — nothing adopted S25.)**
- **DROPPED, AND THE RECORD IS CLOSED:** *"A [RECALL] block has a budget."*
  Offered a third and final time at the S25 open as STATE mandated; he did not
  rule on it, and went straight to the material. **Three offers, no ruling —
  the behaviour settled it. Do not raise it again.** Note that S25 then ran a
  recall block with NO budget and cleared eleven items, which is evidence the
  rule was never needed.
- Settled: queue tooling = a SCRIPT in this repo (not Anki). Still unbuilt.

## WHERE WE LEFT OFF

### SESSION 26 STARTS HERE — exact resume point

S25 ran Friday 21 Aug 2026, one day after S24. It was **entirely a recall
session by his own request** — he asked for the recall block first at the S24
close and it was honoured — and it cleared the whole backlog.

⚠ **HIS CLOSING INSTRUCTION, VERBATIM: "next session should start without
recall actually studying 1.8 further." OPEN ON CONTENT.**

Run in this order:

1. **ONE LINE: how did Saturday's build block go?** Then drop it unless he
   wants to talk about it.

2. **OPEN 1.8 CONTENT IMMEDIATELY: tuple → dict → set → when-to-use-which.**
   Doubt gate before each. Then comprehensions — **and declare the gate OPEN
   out loud, because it was declared SHUT in S24 and S25 opened it.**
   Also owed inside 1.8: `zip`, f-strings, nested structures, `reversed()`,
   and the **shallow-copy point parked in S24** (a slice copies the
   REFERENCES — he called `tools[:]` "an identical new list object").

3. **LATER IN THE SESSION, NOT AT THE OPEN — the four hooked items, cold.**
   All four were taught or re-taught in S25, so S26 is their first legitimate
   later-day test. **This is the experiment that tests the hook technique:**
   - **`pass`** — hook: *jagah bharo / agla chakkar / bahar niklo*. Ask the
     MECHANISM, not a use. It was a flat "gap" in S25.
   - **loop `else`** — hook: read it as **`nobreak`**. Flat gap S23.
   - **ternary** — hook: **`ter-` = three**; value, condition, value. Flat gap S23.
   - **associativity** — hook: *rank barabar? ab direction dekho; sab left se,
     sirf `**` right se*. **Ask it ALONE. Never bundled with precedence —
     bundling is what produced the false S16 [x].**

4. **ALSO COLD, FIRST TIME EVER QUEUED: `list()`.** Constructor call; builds a
   NEW list from any iterable; drains an iterator. **Defined S15 as a patch to
   a breach and then never queued or re-tested for nine sessions** — found when
   he needed it in S25 and had to open his S15 notes. Pushback 34, part-upheld.

5. **STILL OWED:** the statement half of expression-vs-statement; `while`
   mechanics and `break` cold (only `continue` promoted in S25); keyword
   argument's first cold test; the mixed three-error set.

**Standing turn rules: short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — traces
never optional, five checks on every drill, boundary values first. Tag every
block, and CHECK THE TAG IS RIGHT. Do not propose ending the session.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — **now with a named target: every BUNDLED S16 promotion,
  because associativity proved bundling hides untested items**; the 1.6 spoken
  Feynman recall; the S22 short-gap promotions; the eight S23 promotions; the
  eleven S25 promotions.
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- Three-error set (`TypeError`/`NameError`/`UnboundLocalError`) still untested
  MIXED. `UnboundLocalError` spelling is FIXED.
- `None`/`is None` and `bool("False")` remain [~]. `str` immutability is an
  [x] candidate on one clean later-day pass.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 26 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: this file is ~4,100 words against a
2,000-word target, and the two queues are 60+ rows against the ~30-row trigger
in RULES proposal 6. The adopted remedy is a SCRIPT IN THIS REPO. It is still
unbuilt and is now the top candidate for a build block.**

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
| expression vs statement | value vs action | [~] statement half STILL owed; the S25 ternary teaching approached it but did not test it | **S26** |
| **precedence / associativity** | **precedence = rank between DIFFERENT operators; associativity = direction on the SAME rank. Sab left se, sirf `**` right se.** | **⚠ ASSOCIATIVITY DEMOTED [x]→[~] S25 — flat "gap" when asked ALONE. Taught properly S25 with `10-3-2` vs `2**3**2`. Precedence half untouched.** | **S26 cold, ALONE** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | `a == b*(a//b) + (a%b)`; sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE — S25** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable | able-to-be-iterated; hands out iterators; REUSABLE | [x] S16 | ~9 Sep |
| iterator | the nozzle; forward-only; CONSUMED | [x] S23, 7/10 | ~10 Sep |
| StopIteration | the stop signal; an EXCEPTION raised by `next()` | **[x] S25 — named exactly, cold, 7/10. S23 demotion reversed.** | ~11 Sep |
| `next()` / `iter()` | `iter()` once at the top; `next()` once per pass | **[x] S25 — both names produced cold and used correctly, 8/10 (`drills/s25_iteration.py`)** | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **`list()`** | **CONSTRUCTOR CALL — builds a NEW list from any iterable; drains an iterator to exhaustion** | **[~] NEVER QUEUED. Defined S15 as a breach patch, then never re-tested in nine sessions. S25: needed in a drill, retrieved from NOTES not memory — mentor bookkeeping failure, pushback 34 part-upheld.** | **S26 cold** |
| **indexing** | **`[]` takes a POSITION, returns the object there; 0-based; last index is `len-1`; negative counts back from the end; out of range ⇒ `IndexError`** | **[~] NEW — DEFINED S24 for the first time (it had never been taught). Precision fix issued: length is `len`, the LAST INDEX is `len-1`.** | **S25 cold** |
| **slicing** | **`[start:stop:step]`, HALF-OPEN like `range()`; builds a NEW list; `l[:]` is the copy idiom; out of range ⇒ `[]`, NEVER raises** | **[~] NEW — TAUGHT S24, discharges pushback 25. He derived "it creates a new list object" UNPROMPTED.** | **S25 cold** |
| traceback | crash report; each line = one live frame | [~] S23 read one in the wild but CUED | **S25 cold** |
| NameError | the NAME does not exist anywhere | [x] S18 | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | **[x] S25 — `sep` corrected to SPACE, `end` = `\n`, `None` given on the re-ask. 8/10** | ~11 Sep |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade S23, 7/10 | ~10 Sep |
| `break` / `continue` | exit loop / **end this ITERATION** | **`continue` [x] S25 (8/10, phrasing fixed). `break` still [~] — never cold-tested alone.** | **`break` S26** |
| **`pass`** | **no-op filling a block that cannot be empty. HOOK: *pass = jagah bharo, continue = agla chakkar, break = bahar niklo*** | **[~] FLAT "gap" S25. Re-taught same session with the IndentationError gate and the 3-way contrast.** | **S26 cold — hook test** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **runs only if the loop finished WITHOUT `break`. HOOK: read the keyword as `nobreak`.** | **[~] FLAT GAP S23. Re-taught S25; he then derived the empty-list case correctly from the hook on first use.** | **S26 cold — hook test** |
| **ternary** | **EXPRESSION: `A if C else B` — evaluates to a VALUE, so it goes where a value goes. HOOK: `ter-` = THREE; value, condition, value; the middle is the condition.** | **[~] FLAT GAP S23. Re-taught S25 with the placement motivation (you cannot put an if-block inside a `+`).** | **S26 cold — hook test** |
| elif | chain, first true wins, rest never evaluated | [x] S17 | ~10 Sep |
| keyword argument | `name=value` in the CALL, matched by NAME | [~] defined S21, never tested | S25 |
| UnboundLocalError | name IS local (compile-time), no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ returns `None`; `pop` is the counterexample. **TYPE FIRST, always — the return value is the SECOND filter.** | **[x] S25 — rule and counterexample both cold, 8/10. He omitted the type-first half; it was re-stated.** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates, returns `None`; `sorted()` builds a NEW list | **[x] S25 — all FOUR printed values correct cold, 8/10. The S24 inversion is gone.** | ~11 Sep |
| **list method roster** | **`append` `extend` `insert` `sort` `remove` all mutate → `None`; `pop` mutates → returns the removed ITEM** | **[~] NEW — exercised cold S24, 3/6 right by name-decoding** | **S25** |
| pre-order / post-order | work before the call / after the call | [x] S23, 6/10 | ~10 Sep |
| lambda | EXPRESSION form of a function; auto-returned | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it, not the quotes; absent = `None` **(the attribute EXISTS and holds `None` — it is not missing)** | **[x] S25 — both values right WITH the mechanism, 6/10.** | ~1 Sep |
| `key=` | one argument, sorts by RESULTS, returns ORIGINAL items | [x]-grade in use S23 | ~10 Sep |
| cell | a TYPE — a one-slot box; `__closure__` is a TUPLE, one cell per free variable | taught properly S23 | **S25, inside the closure recall** |
| closure four layers | name → function object → `__closure__` TUPLE → CELL → `cell_contents` | **[x] S25, 7/10 — survival clause AND layers both present. THE S23 DIAGNOSIS WAS RIGHT: the muddle was mentor-side. Correction issued: nesting is necessary but NOT sufficient — the FREE VARIABLE capture is what makes it.** | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] | S25 |
| THE FIVE CHECKS (mnemonic) | "Boundary pe khaali ek bahar mila" — **`ek` = EXACTLY ONE (not "small"); `bahar` = outside what you ASSUMED, sign AND type** | **[x] S25 — 5/5 COLD, `mila` recovered as PROMISE vs CODE, self-rated 4/5. Two precisions issued.** | ~1 Sep |

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
| In-place mutators return `None` | **S25: the one-directional rule AND `pop` as counterexample, both cold, 8/10** | **[x] — gauntlet, then ~11 Sep** |
| `__defaults__` | S22 produced cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day | [~] due ~5 Sep |
| Short-circuit | S14 pass | [~] one more pass promotes |
| **Iteration protocol (`iter()` once, `next()` per pass, `StopIteration` to stop)** | **S25 PASSED COLD, all three parts. `drills/s25_iteration.py` 7/7 with `for`/`while`/indexing/slicing BANNED and the ban enforced by a test.** | **[x] — UNBLOCKS COMPREHENSIONS. Gauntlet, then ~11 Sep** |
| Iterator causation (forward-only state) | S22 pass; S23 held | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong | [~] label re-test |
| Traceback: each line = one live frame | S23 cued only; not reached in S25 | [~] **still owed — S26** |
| `while` mechanics; nested loops; loop `else`; found-flag; `pass`; ternary | **S25: `continue` PROMOTED. `pass`, loop `else` and ternary all RE-TAUGHT WITH HOOKS after flat gaps — same-session, so none promotable.** | [~] **S26 is the hook experiment — still the weakest cluster** |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged, ~10 Sep |
| Mutable/immutable discriminator | S18 pass; **S24 corrected the TELL to one-directional** | [x] on the type half; **tell half [~] — S25** |
| Cell causation (five calls, five cells) | S22 pass 7/10 | [x] — ~31 Aug, then ~17 Sep |
| **Closure definition (one line)** | **S25 PASSED COLD, 7/10 — survival clause AND layers both present after failing twice. Confirms the S23 root-cause diagnosis: the muddle was mentor-side.** | **[x] — gauntlet, then ~1 Sep** |
| **Closure APPLICATION (write one under a forcing constraint)** | **S25: `drills/s25_closure.py` 10/10, UNAIDED, zero debug cycles. Boundary handled correctly unprompted (`>` not `>=`).** | **[x] — gauntlet, then ~1 Sep** |
| **Function object vs call (`f` vs `f()`)** | **S25 supporting evidence: `make_clamp` returned the function OBJECT correctly and `clamp_all` called it correctly, unaided** | **[~] — one direct cold test promotes; S26** |
| Recursion: base/recursive case, frames stacked | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order (transfer) | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| **Five checks** | **S25: 5/5 COLD, self-rated 4/5. `mila` recovered and stated correctly as PROMISE vs CODE.** | **[x] — gauntlet, then ~1 Sep** |
| Argument count ⊥ return value | S20 category confusion | [~] ~16 Sep |
| `global` | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| `*args`/`**kwargs` | S22 pass 8/10 | [x] — ~7 Sep |
| Compile-time locality TRAP inside a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS, 6/6 cold | [x] — ~10 Sep |
| **Docstrings / `__doc__`** | **S25: both values cold WITH the position mechanism, 6/10. Precision fix: the attribute EXISTS holding `None`, it is not absent.** | **[x] — ~1 Sep** |
| **Spec-vs-implementation agreement (`mila`, check 5)** | **S25: defined cold and correctly — *"is the program doing the same as it says"*.** | **[x] — with the five checks** |
| **Indexing / slicing** | **S24 taught; NOT re-tested in S25 (the session ran on the recall queue instead)** | **[~] — cold S26, plus the shallow-copy point** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** not observed S20–S25. **S25 gave the cleanest
  counter-evidence yet: mid-session he proposed extending the clamp drill with
  `*args`/`**kwargs` — but that is TAUGHT material ([x] S22), not new territory,
  so it is APPLICATION APPETITE, not scope creep.** It was redirected into
  Saturday's cold build block rather than refused. **Read it as fuel and spend
  it somewhere legitimate; that worked.**
- **Term/label retention — first-class watch area. S25 SETTLES THE METHOD.**
  Four items that had failed as flat gaps under repeated re-teaching were given
  HOOKS instead; the five-checks mnemonic, the only hook with a track record,
  went 4/5 → **5/5**. **Decodable labels hold on their own; arbitrary ones need
  a HOOK, not another explanation.** S26 tests four new hooks cold.
- ⚠ **BUNDLED PROMOTIONS ARE NOW A NAMED RISK — NEW S25.** Associativity sat at
  [x] since S16 purely because it was ticked on the same line as precedence and
  never asked alone. **A bundled tick can hide a completely empty item for nine
  sessions.** Gauntlet action: audit every [x] that shares a bullet with another
  item, and re-ask each half SEPARATELY.
- **CONFIDENCE CALIBRATION — IMPROVING, AND S24's HOT READING LOOKS LIKE NOISE.**
  S25 ratings: 7, 8, 6, 4/5, 8, 8, 8 — every one attached to a correct answer,
  none inflated, and the 6/10 on docstrings correctly flagged the weakest of them.
  **Compare S24's *"for sure"* on a wrong answer. Keep using the rating as a
  targeting signal.**
- **Depth-before-answer:** fired **three times** in S25 and all three recovered
  in ONE line — the `beta` string called "a comment", the missing `pop`
  counterexample, the unanswered `print()` return value. ⚠ **The re-ask is the
  intervention. It has now worked six times across S24–S25 without a single
  failure. Do not re-teach; re-ask.**
- **Honest-gap declaration is now reliable behaviour.** He said "gap" twice in
  S25 rather than guessing, and volunteered that `list()` came from his notes
  when silence would have bought him a clean 7/7. **Third time he has protected
  the ledger at his own expense.**
- **Layer-muddle: CLOSED.** The S22/S23 closure muddle was re-tested in S25 and
  the structure held. **It was mentor-side, exactly as S23 predicted.**
- **⚠ SPEC-WRITING IS A MENTOR WATCH AREA — SECOND CONSECUTIVE SESSION.** S24's
  `last_three` and S25's `clamp_all` were both found ambiguous by him, both
  upheld. **S25's defects, named: "oldest order preserved" (meaningless here —
  copied from a time-ordered drill), "a NEW list of the same angles, each pulled
  inside the limit" (self-contradictory), and four requirements welded into one
  sentence.** Fix: numbered sub-requirements, one per line, worked immediately.
  **Write drill specs as (a)/(b)/(c), never as prose.**
- False attribution: **34 raised, 33 upheld or part-upheld.** S25 raised three:
  (32) the `clamp_all` spec is unintelligible — **UPHELD, mentor error**;
  (33) refusing a teach-back on the closure line as echo rather than knowledge —
  **UPHELD, and it is him enforcing the file's own confidence rule on me**;
  (34) *"you expect me to remember `list()` from long back — wrong expectation?"*
  — **PART-UPHELD: "it was long ago" is no defence in this course, but `list()`
  was NEVER ENTERED IN THE QUEUE after S15, so the system had never once asked
  him for it. That half is mentor bookkeeping failure.**

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
- **NEW S25: bytecode / what CPython does with a bare constant expression.** He
  asked whether `5` alone on a line costs memory in the bytecode. **Told plainly
  that this is LEVEL 3 and out of scope**, that CPython's compiler does drop bare
  constants, and that the answer is implementation-specific. **The Level 2 model
  — expression statement, evaluated, result discarded — is the one that must be
  cold-solid.** Revisit in 1.13.
- **NEW S25: multi-joint clamp with `*args`/`**kwargs`** — HIS OWN design, moved
  to the Saturday 22 Aug cold build block. The unanswered pairing question is
  deliberately left with him.

---
