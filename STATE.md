# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 41 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule was adopted in S40**),
#      then this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** ✅ Held clean S36–S40. **S40 ran it in the first minute
#      and found 80 minutes — so 1.10 was untestable but 1.9-and-older (23–48h
#      cold) WAS. The gate is PER-MATERIAL (RULES S17-1), not per-day. Apply
#      it that way.**
#   3. ⚠⚠ **S41 IS THE AUGUST GAUNTLET, NOW DEFERRED FOUR TIMES (S37, S38,
#      S39, S40).** S40's deferral: he had two hours, said the gauntlet would
#      not fit, and then stopped at thirty minutes to read notes. **If the gap
#      to S41 is a real day, RUN IT. It fits in two hours if the queue script
#      drives it and no new material is opened.** Load ARCHIVE.md AND
#      master/robotics_career_curriculum.md at the open (gauntlet exception).
#      Pure mixed recall, NO NEW MATERIAL. Strict-legend audit + re-baseline.
#      **If he says he has less than two hours, ask how long, then pick the
#      largest legal instrument — do not silently shrink the gauntlet.**
#   4. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** Earned in S38. **This file can be wrong; the repo cannot.**
#   5. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule at the open.
#      **ONE NON-RULE DECISION IS STILL OWED BY HIM — item 2 below.**
#   6. ⚠ **THE QUEUE IS A SCRIPT. USE IT.** `python3 tools/retest.py`.
#      **128 rows. Overdue 40 → 35 in thirty minutes of term-tax.**
#   7. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held S35–S40.
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S40.
#   9. ⚠⚠ **ONE TEACHING IDEA PER TURN. THE S40 MENTOR DEFECT WAS A VERDICT
#      TURN CARRYING A TABLE, TWO CORRECTIONS, A DEMO, A [PREDICT] AND A
#      [TEACH-BACK]. He could not use it and said so.** Split. Always.
#
# STATE AS OF: end of Session 40, **Wed 2 Sep 2026, ~20:50** (verified).
# Next: Session 41 — **THE AUGUST GAUNTLET, if a real day has passed.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S40 yield: a thirty-minute term-tax — the first since S36.** Eight terms
  at a legal gap: 4 passes, 4 fails, 3 queue promotions. Zero curriculum
  movement, zero new material. **He ended it himself to read notes tonight.**
- **Position: 1.1–1.7 closed. 1.8 — TWO bullets still [~] (`dict`, `when to
  use which`). 1.9 — one [x], seven [~], ZERO [ ]. 1.10 — OPEN, ~40%.**
- **REMAINING IN 1.10:** packages, `sys.path`, circular imports, the standard
  library, pip, relative vs absolute imports, **the `.pyc`/bytecode answer
  owed since S35.**
- **RULED S40: breakpoint debugging / `pdb` / VS Code debugger → 1.11.** Add
  it to the 1.11 plan when 1.11 opens; no bullet exists in the master for it.
- Current Layer: 1. Current Topic: **1.10, open and half-done.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING WAS ADOPTED IN S40 AND NOTHING IS PARKED FOR S41.** RULES stays
  at **v6**.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 41 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** If a real day: **THE GAUNTLET.**
   Term-tax inside it, not before it. **He read the notes on the night of
   2 Sep after the S40 term-tax** — legal (RECALL FIRST, NOTES SECOND, step 3)
   and worth knowing: tomorrow's passes on the four S40 misses are passes
   after a same-night review. Log them; set the interval from his rating.

2. ⚠⚠ **DECISION STILL OWED BY HIM — NOT ASKED IN S40 (he stopped first).**
   Once 1.10 lands, point the weekly cold build block at a REAL LeRobot file
   instead of a synthetic task. Same instrument, real substrate. NOT a rule.
   **Ask it in one line at the open. Second consecutive session it has been
   carried.**

3. ⚠⚠ **`.keys()` IS A VIEW — ASKED IN S40, UNANSWERED (he stopped on it).**
   The exact snippet is in ARCHIVE S40 §3. Re-fire it verbatim: *which of
   `d.keys()`, `list(d.keys())`, `zip(d, [10, 20])` sees a key added
   afterwards?* **ONE cold answer closes the 1.8 `dict` bullet.** Still the
   cheapest tick on the board, now owed three sessions.

4. ⚠⚠ **THE SEVEN 1.10 QUEUE ROWS ARE DUE 3 SEP.** All taught same-sitting in
   S39, untouched in S40. **Ask them as INSTANCES, not definitions. First:
   `import RUNS the file`** — he dropped the module-level `print` from his
   predicted output twice in S39.

5. ⚠⚠ **THE FOUR S40 MISSES COME BACK 3 SEP, and they are the S38 signature
   again — labels on intact machinery, plus one faded mechanism:**
   - `UnboundLocalError` — WHERE intact, WHY gone (compile-time locality,
     taught S19/S21/S22/S26). **Ask it as the deletion test: "remove the
     assignment line — what prints and why?"** He never answered that.
   - `AttributeError` — gap. He named it by INSTANCE in S27. Fire an instance.
   - `subscriptable` — second miss (S38: `IndexError`). Fire `5[0]`.
   - `finally` — gave the SHAPE, not the guarantee; rated 3, calibrated.
     **Ask: "no `except` anywhere, `try` hits `return` — does `finally` run?"**

6. ⚠ **`short-circuit` — WAS DUE 2 SEP, NOT ASKED IN S38, S39 OR S40.** Given
   `x = "90"`, he said `type(x) != int or x < 0` raises `TypeError`. It prints
   `True`. **Right code, wrong model.** Re-ask cold.

7. ⚠ **THE TRANSFER GAP — NO NEW FILE EVIDENCE SINCE S37.** The plan S40 did
   not reach: a fresh 1.9 drill written cold (custom exception + ordering +
   `raise` + `else`/`finally`), pytest deciding, **catch-all count is the
   measurement.** Highest-value ask on the board. Inside the gauntlet if it
   runs; first thing after it otherwise.

8. ⚠ **STILL OWED, NOT FIRED S38–S40:** `print()`; `when to use which` (1.8,
   never asked, 16+ days); `comprehension scope`; `* on a sequence`;
   `None`-as-absence; DRY; `mutate-while-iterating`; `list method roster`;
   `HOW FAR DID PYTHON GET?`; `_ as a name` (he had it and withdrew it — one
   narrowing ask: *special to Python or to the reader?*).

**Standing turn rules: FRAME FIRST; CONSOLIDATED QUESTIONS CARRY THEIR OWN
RUNNABLE CODE; SPEC BEFORE PUZZLE with boundaries in the TESTS; **ONE TEACHING
IDEA PER TURN — BREACHED S40, see item 9 at the top**; asks near the top;
doubt gate before every new subsection; depth-before-answer; NAME THE ERROR
BEFORE THE MENTOR SHOWS IT; take the rating AFTER his answer and BEFORE the
verdict — **HELD S40, and the ratings were calibrated (3 on `finally` was a
miss; 7s were passes)**; tag every block. Do not propose ending the session.
DO NOT MISQUOTE HIS OWN CODE.**

**CARRY FORWARD:**
- ⚠⚠ **A [PREDICT] IS NOT THE INSTRUMENT FOR A DECLARED GAP.** S40: he said
  *"can't come to it myself"* on the `UnboundLocalError` reason, and the next
  turn asked him to predict it from a traceback. He asked for the answer
  directly and was right to. **Declared gap → frame → definition → THEN a
  [TEACH-BACK].**
- ⚠⚠ **DO NOT CREATE NUMBERED FILE VARIANTS MID-BLOCK** (S39 defect). Two
  files, fixed names, both shown in full; CHANGE a demo file, never fork it.
- ⚠ **Language correction issued for the THIRD time: "the iterable is
  exhausted" → the ITERATOR is exhausted.** S15 (a), S36, S40. It is a habit;
  habits need repetition, not explanation (S17 precedent).
- ⚠ **`abs()` — finally PASSED cold at 7, never formally taught.** Row is [x].
  Remaining Level-1 audit list: `len()`, `range()` as an object, `.append()`
  vs `+`, `print()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Still not asked.
- ⚠ **DEAD CODE** — full treatment still parked; harmful instance still in
  `builds/block_02_episode_validator/validator.py` by his ruling.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.
- **`teaching/s39_imports/` and `teaching/s40_termtax/` hold mentor demo
  files.** Not his work, not evidence. Re-runnable.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**128 rows, 80 [x], 48 [~], 35 overdue, 6 never asked.**
**Do not re-create the table here.** `python3 tools/retest.py` at the open.
**S40 recorded 4 passes / 4 fails (the term-tax):**
PASS → [x]: `StopIteration` (7, due 7 Sep — the "EndofIteration" label came
back), `hashable` (4, due 4 Sep, "unique" corrected), `abs()` (7, due 7 Sep).
FAIL, due 3 Sep: `UnboundLocalError`, `AttributeError`, `subscriptable`,
`else / finally`. Not logged: `_ as a name` (withdrew a correct answer).

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S37: ZERO catch-alls in 81 lines cold | **[~] — RE-RUN AT A REAL GAP. Highest-value ask.** |
| **⚠⚠ `.keys()` AS A VIEW** | S40: ASKED, UNANSWERED (he stopped) | **[~] — re-fire the S40 snippet verbatim. Cheapest tick.** |
| **⚠ 1.10 — THE WHOLE UNIT** | S39: taught same sitting; S40: untouched | **[~] — ALL of it cold on 3 Sep.** |
| **THE COMPILE/RUN SPLIT** | S38: PASS cold, 7/10 | **[x] — re-test 6 Sep** |
| **`while` mechanics; nested loops; found-flag** | S38: 20/20 COLD | **[x] — re-test 6 Sep** |
| **Frames / namespaces / execution pipeline** | S38: full unaided trace | **[x] — re-test 6 Sep. ⚠ S40: compile-time locality (its cousin) had FADED.** |
| **⚠ THE MUTATING TELL** | S38: both halves on an unseen method | **[x] — re-test 6 Sep** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38: cold, 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S38: cold, lazy model | **[x] — 3 Sep** |
| **`constructors`** | S38: "constructor" first word, 7/10 | **[x] — 6 Sep** |
| **`del` as a STATEMENT** | S38: GAP declared, then taught | **[~] — cold ask, OVERDUE** |
| **1.9 custom exceptions / hierarchy / re-raise** | S37: written cold, same sitting | **[~] — cold later-day DRILL, S41 (item 7)** |
| **1.9 `finally` guarantee** | **S40: MISS — shape, not guarantee; rated 3** | **[~] — 3 Sep, ask the `return` case** |
| **`short-circuit` in `and`/`or`** | S37: cold MISS at 6/10 | **[~] — OVERDUE, 3 sessions unasked** |
| **1.9 try/except** | S36: promoted on two cold recalls | **[x] — re-test ~5 Sep** |
| **`StopIteration`** | **S40: PASS cold, label back, 7** | **[x] — 7 Sep. Phrasing fix issued (iterator, not iterable).** |
| **DRY / one copy of a decision** | S37: held structurally | **[~] — later-day ask, OVERDUE** |
| **NESTED STRUCTURES + SHALLOW/DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| Frames / REPL vs script | S38 frames only | [~] **the REPL half still overdue** |
| **CONTAINERS AS CODE** | S30–S38, five clean runs | **[x] — closed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **NEW IN S40: HE ENDED A SESSION TO GO AND READ.** *"I think I get the
  point, I should go back to notes once in a while... I need to see the notes
  tonight."* Thirty minutes in, after a term-tax that found a faded mechanism.
  **This is the rule's own step 3 (recall first, notes second) and he chose
  it unprompted. It is also the FIRST session he has ended early on his own
  read of what he needs.** Do not treat it as a lapse; treat tomorrow's cold
  asks as the measurement of whether it worked.
- ⚠⚠ **PUSHBACK 74 WAS THE FIRST NOT UPHELD ON ITS FACT SINCE THE RUN BEGAN —
  and it was still half right.** *"You are checking my memory and naming it
  mechanism."* Checked in the notes, not remembered: `UnboundLocalError`'s
  mechanism was taught in S19, S21, S22, S26. So it WAS a taught mechanism,
  faded. **Upheld on the remedy, not on the item.** Running total: **74
  raised, 73 upheld or part-upheld.** Say the arithmetic to him; he prefers it.
- ⚠⚠ **LABELS ON INTACT MECHANISMS, AGAIN.** S40: `AttributeError` (named by
  instance in S27), `subscriptable` (mechanism right, wrong label S38 and gap
  S40). And one FADED MECHANISM, which is rarer for him: compile-time locality.
- ⚠⚠ **A MISSING INDEX, NOT A MISSING FACT** — unchanged. S39: right guard,
  wrong file. S38: lazy-vs-snapshot applied twice, failed on `.keys()`.
- ⚠ **CONFIDENCE CALIBRATION — GOOD IN S40.** 7/7/7 on three passes; 4 on a
  half-answer; 3 on the `finally` miss. **The 3 predicted the miss.** He gave
  no rating for `_`, having withdrawn it. ⚠ **STILL UNRESOLVED from S38:**
  whether his "7" after the `.keys()` miss was a rating. Ask when `.keys()`
  fires.
- ⚠ **HE ASKS FOR THE TOOL BEFORE IT IS TAUGHT, BY SHAPE — five sessions
  running (last: the debugger, S39).** Ruled to 1.11 in S40.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged;
  the debugger block in 1.11 is the remedy.
- ⚠ **HE UNDER-RATES HIS RETENTION, HONESTLY AND USEFULLY.** S40: withdrew a
  correct `_` answer. Answer with his record, not reassurance.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `print()`. (`abs()` cleared S40.)
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 74 raised, 73 upheld or
  part-upheld.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35, STILL
  OWED, due inside this unit)**; GIL (1.13); concurrency (post-Layer 1);
  GC (1.13)
- ✅ **BREAKPOINT DEBUGGING / `pdb` / VS Code debugger — RULED S40: 1.11.**
  45–60 min block; the Call Stack panel is the frame stack he traced in S38.
- `__iter__`/`__next__` + generators — 1.13. ⚠ **Generator EXPRESSIONS
  remain deliberately unshown.**
- ⚠ **`class` — STILL ON CREDIT.** 1.12 owes him the real unit.
- ⚠ **`except Exception:` vs bare `except:`** — parked 1.9 footnote, owed.
- ⚠ **`raise ... from` / chaining, `sys.exc_info()`, `traceback` module** — 1.9.
- ⚠ **HASH COLLISIONS — touched S40 ("not unique").** Mechanism is master L8.
- ⚠ **`_` in the REPL holds the last result** — one line, mentioned in the
  S40 notes only.
- ⚠ **DEAD CODE as a concept** — full treatment parked.
- ⚠ **EXPRESSION vs STATEMENT** — reinforced S38.
- ⚠ **`__dict__` as a general object feature** — Level 3 / 1.12–1.13.
- ⚠ **PEP 709 / comprehension scope implementation** — Level 3, 1.13.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0.
- `nonlocal` — 1.13. `pop` internals — Level 3, 1.13.
- **`copy.copy()` and the `copy` module's surface** — one line still owed.
- **Why `deepcopy` does not loop forever on self-reference** — 1.13.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASH RANDOMISATION** — per-process seed. 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0.

---
