# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 39 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule was adopted in S38**),
#      then this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** ✅ Held clean S36, S37, S38. In S38 it decided the whole
#      shape of the session in the first minute.
#   3. ⚠⚠ **S39 IS THE AUGUST GAUNTLET, NOW DEFERRED TWICE (S37 and S38),
#      BOTH TIMES CORRECTLY BY THE INTERVAL GATE — RUN IT IF THE GAP IS A
#      REAL DAY.** Load ARCHIVE.md AND master/robotics_career_curriculum.md at
#      the open (gauntlet exception). Pure mixed recall, NO NEW MATERIAL.
#      Strict-legend audit + re-baseline. **S38 already did a large slice of
#      the overdue-cold-ask half of it — see the yield below — so the gauntlet
#      is now mostly (a) the STRICT-LEGEND AUDIT and (b) the RE-BASELINE.**
#   4. ⚠⚠ **DO NOT REPEAT THE S38 OPENING ERROR: STATE.md CARRIED A FALSE
#      ALARM.** The S37 header said the working tree was RED (three `try:`
#      with no `except`, zero tests collecting) and instructed the mentor to
#      get it fixed before teaching. **It was false. `HEAD` had all three
#      `except TypeError:` blocks, `git status` was clean, and the block ran
#      27/27 on the first try.** Cost: nothing, because it was checked. **RULE
#      OF THUMB EARNED: verify a STATE warning against the REPO before acting
#      on it. This file can be wrong; the repo cannot.**
#   5. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule at the open.
#      **ONE SCHEDULING DECISION IS OWED BY HIM (not a rule): see item 3 of
#      the resume point.**
#   6. ⚠ **THE QUEUE IS A SCRIPT. USE IT.** `python3 tools/retest.py`.
#   7. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held S35–S38.
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37, S38.
#
# STATE AS OF: end of Session 38, **Tue 1 Sep 2026, ~21:20** (verified).
# Next: Session 39 — **THE AUGUST GAUNTLET, if a real day has passed.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S38 yield: A PURE REVISION SESSION, REQUESTED BY HIM — "no new content,
  clear the oldest material first and work forward". IT WAS THE HIGHEST-YIELD
  SESSION THE QUEUE HAS EVER HAD.** 20 rows fired, **15 passes / 5 fails**.
  Queue moved **66 [x] → 77 [x]**, **38 overdue → 25**, **12 never-asked → 8**.
  **TWO CURRICULUM BULLETS MOVED — the first curriculum movement since S36:
  1.8 `list` → [x], and 1.9 `Common built-in exceptions` [ ] → [~]** (the last
  untouched bullet in 1.9; now opened).
- **THE OLDEST DEBT IN THE FILE IS PAID.** `while` mechanics / nested loops /
  early exit — eleven sessions overdue, untested since 10 Aug — **20/20 cold
  on first submission** (`drills/s38_while.py`, two `while` loops, a nested
  `while` with an early `return`, and an implicit `None` on fall-through).
- **ALSO PAID: the compile/run split**, third time of asking, cold and
  standalone at the top of the session, with a complete mechanism —
  *"the code execution starts once the code has been converted to bytecode,
  but since SyntaxError it will never enter the execution state."*
- **Position: 1.1–1.7 closed. 1.8 — TWO bullets still [~] (`dict`,
  `when to use which`). 1.9 — one [x], seven [~], ZERO [ ].**
- **AFTER THE GAUNTLET: 1.10 modules and imports.**
- Current Layer: 1. Current Topic: **1.9 closing / 1.10 next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING WAS ADOPTED IN S38 AND NOTHING IS PARKED FOR S39.** Do not invent
  a candidate. RULES stays at **v6**.
- **RULES v6 (THE DONE LINE) — FOURTH DATA POINT, AND IT WAS A CLEAN ONE.**
  He submitted the drill with his five checks written as comments IN THE FILE,
  and among them was a real failure case, correctly the case-half rather than
  the function-half: *"lets say the user enters something else apart from int,
  then this will fail"* — true, `backoff_steps("8")` raises on `abs()`.
  **Accept the file-comment form; it is the same instrument.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 39 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** Then the **term-tax** (valid at a
   real gap). Then, if the gap is real, **THE GAUNTLET**.

2. ⚠⚠ **WHAT THE GAUNTLET STILL HAS TO SETTLE, now that S38 has cleared 13
   overdue rows:**
   **(a) THE STRICT-LEGEND AUDIT of every [x]** — the bundled S16 promotions;
   the 1.6 spoken Feynman recall; the S22 short-gap promotions; the eight S23;
   the eleven S25; the eight S27; the S29 `zip`; the eight S30; the four S31;
   the four S32; the seven S33; the two S34 (**plus the `.count()` echo caveat
   on the tuple tick**); the one S35; the one S36; **the eleven S38 — which are
   the cleanest in the file (all cold, all on material 8–24 days old) and
   should be the AUDIT'S CONTROL GROUP rather than a target.**
   **(b) THE RE-BASELINE ARITHMETIC, IN ITEMS**, against 30 Sep.
   ⚠ **(c) THE AUDIT'S STARTING LEAD IS UNCHANGED: `queue.json` and
   `CURRICULUM.md` drifted apart on `short-circuit` without anyone noticing.
   Diff the queue against CURRICULUM row by row.**

3. ⚠⚠ **HE ASKED THE BIG SCOPE QUESTION AT THE S38 CLOSE AND IT NEEDS A RULING
   FROM HIM, NOT AN ANSWER FROM THE MENTOR.** His question: *"the agreement was
   to make me capable of reading and understanding complex code bases, is that
   still part of plan and if yes when will we reach that stage?"* **He was
   given the honest arithmetic:** it is one of the four things RULES.md says
   Layer 0 must deliver; it is NOT a unit; it is blocked on 1.10 (the map),
   1.12 (LeRobot/openpi/PyTorch ARE class hierarchies) and 1.13 (dunders and
   decorators); realistically the third week of September; and **1.12 is the
   largest unopened unit while `class` is already on credit — four exception
   classes written without the construct ever being taught.**
   **THE OPTION PUT TO HIM, EXPLICITLY NOT AS A RULE:** once 1.10 lands, point
   the weekly cold build block at a REAL LeRobot file instead of a synthetic
   task — same instrument, real substrate. **Take his ruling at the S39 open.**

4. ⚠⚠ **THE ONE MECHANISM MISS OF THE DAY, AND IT IS THE MOST INTERESTING
   RESULT IN THE SESSION: `.keys()` IS A VIEW — STILL NOT HELD, AND HE OWNS
   EVERY PIECE OF IT.** Given `k = d.keys()` then `d["c"] = 3`, he said `k`
   prints `dict_keys(['a','b'])` because *"the line comes after, so it will not
   impact k"*. It prints `dict_keys(['a','b','c'])`.
   ⚠ **WHY THIS MATTERS FAR MORE THAN A MISSED FACT: IN THE SAME SESSION,
   TWICE, HE USED `list()` CORRECTLY TO FREEZE A LAZY OBJECT** — he wrote
   `list(reversed(...))` unprompted, and he explained `zip` exhaustion as
   *"forward only state, once consumed need to be recreated"*. **He owns the
   lazy-vs-snapshot pattern and did not recognise `.keys()` as an instance of
   it.** That is the transfer gap in its purest recorded form: not a missing
   fact, a missing INDEX from the pattern to the case.
   **Ask it again 2 Sep, and ask it as an instance:** *"which of these three
   are live and which are frozen — `d.keys()`, `list(d.keys())`, `zip(a,b)`?"*
   **This is still the cheapest tick on the board: ONE cold ask closes the 1.8
   `dict` bullet.**

5. ⚠ **`short-circuit` — DUE 2 SEP, NOT ASKED IN S38** (correctly: it was
   demoted in S37 the same day). Given `x = "90"`, he said
   `type(x) != int or x < 0` raises `TypeError`. It prints `True`. **Right code,
   wrong model.** Re-ask cold.

6. ⚠ **THE TRANSFER GAP — NO NEW FILE EVIDENCE IN S38 AND NONE WAS POSSIBLE.**
   The S37 result (zero catch-alls in 81 lines of cold fresh code) **still
   needs its re-run at a real gap. Highest-value ask on the board.**

7. ⚠ **`StopIteration` — STILL DUE, NOT FIRED IN S37 OR S38. Re-ask the LABEL
   ALONE.** Mechanism intact after three weeks; the label came back as
   "EndofIteration".

8. ⚠ **STILL OWED, NOT FIRED IN S38:** `UnboundLocalError`; `print()`;
   **`abs()` — and it is now urgent-ish, because he USED `abs()` in his S38
   drill and has still never been given a definition of it**; `when to use
   which` (1.8, never asked, 14+ days); `comprehension scope`; `* on a
   sequence`; `None`-as-absence vs empty container; DRY.
   ⚠ **`mutate-while-iterating` and `list method roster` are also overdue.**

**Standing turn rules: FRAME FIRST; CONSOLIDATED QUESTIONS CARRY THEIR OWN
RUNNABLE CODE; SPEC BEFORE PUZZLE with boundaries in the TESTS — **BREACHED IN
S38, see pushback 70**; short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — **HELD
IN S38 AND IT PAID IMMEDIATELY, see the compile/run result**; NAME THE ERROR
BEFORE THE MENTOR SHOWS IT; **take the rating AFTER his answer and BEFORE the
verdict — BREACHED IN S38, see teaching mistakes**; tag every block and CHECK
THE TAG. Do not propose ending the session. DO NOT MISQUOTE HIS OWN CODE.**

**CARRY FORWARD:**
- ⚠ **`abs()` still owed a proper definition — he used it in S38.** Level-1
  audit list: `len()`, `range()` as an object, `.append()` vs `+`, `abs()`,
  `print()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Still not asked.
- ⚠ **DEAD CODE — SECOND INSTANCE, AND THIS ONE WAS BENIGN AND HIS OWN.** His
  `if gap != 0:` guard could never change the outcome, because the loop header
  tested the same condition. **He explained its origin correctly and unaided:
  a guard written for an older spec and left behind when the spec changed.**
  The harmful instance (three unreachable `except TypeError:` blocks) is still
  in `builds/block_02_episode_validator/validator.py` and he now knows why.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
121 rows, **77 [x], 44 [~]**, 25 overdue, 8 never asked.
**Do not re-create the table here.** `python3 tools/retest.py` at the open.
S38 recorded 15 passes and 5 fails. **Fails, all due 2 Sep:** `del vs .pop()
vs .clear()`, `hashable`, `subscriptable`, `unpacking`,
`.items()/.keys()/.values()`.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S37: ZERO catch-alls in 81 lines of cold fresh code | **[~] — RE-RUN AT A REAL GAP. Highest-value ask on the board.** |
| **⚠⚠ `.keys()` AS A VIEW** | **S38: MISS — and he owns the lazy/snapshot pattern he failed to apply** | **[~] — ask as an INSTANCE, 2 Sep. Cheapest tick on the board.** |
| **THE COMPILE/RUN SPLIT** | **S38: PASS cold, full mechanism, 7/10 — third asking** | **[x] — re-test 6 Sep** |
| **`while` mechanics; nested loops; found-flag** | **S38: 20/20 COLD, `drills/s38_while.py`, 7/10** | **[x] — re-test 6 Sep. ELEVEN-SESSION DEBT CLEARED** |
| **Frames / namespaces / execution pipeline** | **S38: full unaided trace, 7/10. One correction: he said the module namespace holds nothing — `def` binds a name, which is how `inner` is found at all** | **[x] — re-test 6 Sep** |
| **⚠ THE MUTATING TELL** | **S38: BOTH halves. Stated the one-directional rule himself and applied it to an UNSEEN method (`extend`)** | **[x] — re-test 6 Sep** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | **S38: one correct line cold, 13 days on, `records` unmutated, `list()` around `reversed`, 8/10** | **[x] — 13 Sep** |
| **`zip` — both silent failures** | **S38: truncation AND exhaustion, cold, with the lazy model in his own words** | **[x] — 3 Sep** |
| **`constructors`** | **S38: "constructor" as his FIRST word, un-tagged ask, 7/10** | **[x] — 6 Sep** |
| **`del` as a STATEMENT** | **S38: GAP declared, then taught. Teach-back was sharp — "del does not return anything, and by nothing I don't mean None"** | **[~] — cold ask 2 Sep** |
| **1.9 custom exceptions / hierarchy / re-raise** | S37: written cold in a build block, SAME SITTING | **[~] — cold later-day ask, S39** |
| **`short-circuit` in `and`/`or`** | S37: cold MISS at 6/10, conceded | **[~] — due 2 Sep** |
| **1.9 try/except** | S36: promoted on two cold later-day recalls | **[x] — re-test ~5 Sep** |
| **`StopIteration`** | S36: mechanism intact 3 weeks, label = "EndofIteration" | **[~] — label alone, OVERDUE** |
| **DRY / one copy of a decision** | S37: held structurally, unprompted | **[~] — later-day ask, OVERDUE** |
| **NESTED STRUCTURES + SHALLOW/DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| Frames / REPL vs script | **S38 covered frames; REPL-vs-script NOT re-run** | [~] **the REPL half is still overdue** |
| **CONTAINERS AS CODE** | S30 19/19; S32 17/17; S34 36/36; S37 27/27; **S38 20/20** | **[x] — closed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **EVERY MISS IN S38 EXCEPT ONE WAS A LABEL SITTING ON AN INTACT
  MECHANISM. THAT IS NOW THE MOST REPLICATED FINDING IN THE FILE.**
  `hashable`: he derived mutable ⇒ unhashable ⇒ not a key, unaided, and then
  *"can't come up with the error myself"*. `subscriptable`: said `IndexError`,
  and had used the exact right discriminator sixty seconds earlier on the dict
  key. `unpacking`: named the count mismatch precisely and then **reasoned
  himself out of the right answer on a too-narrow definition of `ValueError`**
  (*"when we give a value which is not directly convertible"* — that is one
  instance, not the definition). **The machinery is not the problem. The
  vocabulary layer on top of it is, exactly as the Term Retention System says.**
- ⚠⚠ **THE TRANSFER GAP HAS A SHARPER NAME NOW: A MISSING INDEX, NOT A MISSING
  FACT.** S33: *change where the ask sits.* S34: *an ask that can be satisfied
  without executing anything will be.* S35: *a fact he can PREDICT is not a
  fact he will APPLY.* S36: *he takes the last lesson and drops the one
  before.* S37: *the idea showed up in the file.* **S38: he applied the
  lazy-vs-snapshot pattern twice, correctly and unprompted, and then failed the
  third instance of the same pattern because it was labelled `.keys()`.**
- ⚠⚠ **RIGHT CODE, WRONG MODEL / GREEN TESTS ARE NOT EVIDENCE OF A MODEL.**
  Unchanged from S37 and still the reason to ask *why does this work* on code
  that already passes.
- ⚠ **CONFIDENCE CALIBRATION MOVED, THEN DRIFTED THE OTHER WAY.** He opened
  with **seven consecutive 7s on seven correct answers** — told to his face
  that a flat 7 aims nothing and that his S17 per-item spread was the useful
  version. **He then spread it: 8, 8, 6, 6, 5.** The 6 on `subscriptable`
  correctly flagged the one he got wrong. **But the bottom of the scale now
  UNDER-reads: 6 → correct, 5 → correct.** ⚠ **UNRESOLVED: he answered "7"
  after the `.keys()` miss and it was never established whether that was the
  rating or an answer to a different question. Not logged. Ask him.**
- ⚠ **HE ASKS THE RIGHT GOVERNANCE QUESTION AT THE RIGHT TIME — TWICE IN S38.**
  Mid-session, unprompted: *"what is happening to the items I have reproduced
  cold, are you 'x'ing them?"* — which is him auditing the ledger he depends
  on. At the close: the codebase-reading question. **Both got tables with
  arithmetic, not reassurance. Keep answering him that way.**
- ⚠ **HE UNDER-RATES HIS READING AND HIS SPEED (S37) — and S38 adds the
  counterweight: he is now four build blocks and five drills deep at
  35/35, 29/29, 25/25, 27/27 and 20/20.** Answer self-doubt with his own
  record, never with reassurance.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **HE ASKS FOR THE TOOL BEFORE IT IS TAUGHT, BY SHAPE — FOURTH SESSION
  RUNNING.** S38: he asked when codebase reading arrives, which is the shape of
  1.10 + 1.12. **Give him the tool when he names its shape.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()` (**used again in S38**), `print()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 70 raised, 69 upheld or
  part-upheld.** **S38 raised ONE (70) and it was UPHELD IN FULL: the drill
  spec was unclear and read as recursion** — *"the description is not very
  helpful, seems like you want to see recursion, can you be more clear"*. The
  spec said "each control cycle closes HALF the remaining gap", which is
  jargon around a self-referential-sounding process. **Rewritten before he
  started — plain steps, two worked traces — and he then passed 20/20 first
  submission.** SPEC BEFORE PUZZLE, breached and repaired inside one turn.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35)**;
  GIL (1.13); concurrency (post-Layer 1); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **`class` — STILL ON CREDIT, AND HE HAS NOW ASKED WHEN IT ARRIVES.** Four
  one-line exception classes written; 1.12 owes him the real unit; and the
  codebase-reading answer named 1.12 as the biggest remaining risk to the
  30 Sep deadline. **This is the most load-bearing park in the file.**
- ⚠ **`except Exception:` vs bare `except:`** — still a parked footnote.
- ⚠ **`raise ... from` / chaining, `sys.exc_info()`, `traceback` module** — 1.9 park.
- ⚠ **DEAD CODE as a concept — TAUGHT IN PASSING S38** off his own guard.
  Full treatment still parked.
- ⚠ **EXPRESSION vs STATEMENT — reinforced S38** on `del` vs `.pop()`, and he
  produced the distinction himself. Ternary (S17) was the first instance.
- ⚠ **PEP 709 / how comprehension scope is implemented** — Level 3, 1.13.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — 1.13. `pop` internals (S24) — Level 3, 1.13.
- **`copy.copy()` and the `copy` module's surface** — one line still owed.
- **Why `deepcopy` does not loop forever on a self-referencing structure** — 1.13.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 target; collisions/resizing are master L8.
- **HASH RANDOMISATION** — per-process seed. 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0.

---
