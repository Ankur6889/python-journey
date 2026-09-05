# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 43 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S42**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S42. The gate is PER-MATERIAL (RULES S17-1).
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED. NO DECISION IS OWED.** The build-block
#      decision was answered at the S42 open (see SCHEDULE). Nothing to rule on.
#   5. ⚠ **THE QUEUE IS A SCRIPT.** `python3 tools/retest.py` at the open.
#      **136 rows, 97 [x], 39 [~], 28 overdue, 2 never asked.**
#      ⚠ `--asked` substring-matches: the bare `print()` row and the two `zip`
#      rows cannot be hit by name; edit `tools/queue.json` directly for those.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S42.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN — AND ONE IDEA PER DEMO.** S42: a demo
#      with two `try` blocks produced a teach-back about the wrong idea. One
#      block, one catcher, one question fixed it.
#   9. ⚠ **IN A DRILL DOCSTRING THE EXCEPTION TYPE NAME IS INTERFACE — WRITE
#      `TypeError`, `ValueError`. The CONSTRUCT is mechanism — withhold it.**
#  10. ⚠⚠ **S27 RULE: NEVER SAY "THIS ONE RAISES" BEFORE HE NAMES IT.**
#      Breached once in S42 on the `{}` snippet. Do not repeat.
#  11. ⚠⚠ **`except ... as e` NEEDS class → object, WHICH IS ON CREDIT UNTIL
#      1.12.** Do not test "what is `e`" cold before 1.12; the S42 teach-back
#      failed twice for that reason and it was the mentor's fault.
#
# STATE AS OF: end of Session 42, **Sat 5 Sep 2026, ~03:00** (verified).
# Next: Session 43 — **`sys.path` [PREDICT] first, then the rest of 1.10.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. LADDER RUNG 1 INVOKED:
  weekend blocks first; recompute at the September gauntlet. Nothing
  de-scoped.** Tell him the number if he asks; do not soften it.
- **S42 yield:** 16 overdue rows fired (13/3), one promotion, one demotion;
  **1.9 TAUGHT IN FULL** (direction drawn, ordering, `raise ... from`, bare
  `except`); **`.pyc` debt paid**; `sys.path` [ ] → [~]. ~0.5 unit-equivalent.
- **Position: 1.1–1.8 closed. 1.9 — every bullet taught; three [x] of ten,
  seven [~] awaiting later-day cold asks (due 7 Sep). 1.10 — six [x],
  `sys.path` + `.pyc` [~], four [ ] (packages, relative vs absolute,
  circular imports, stdlib/pip).**
- ✅ **DECIDED S42 (non-rule, asked three sessions running):** once 1.10
  lands, the weekly cold build block moves to a **REAL LeRobot file**. His
  words: *"yes lets move it to real LeRobot file."* Stop carrying it; act on
  it when 1.10 closes.
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.10 second half.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S42, NOTHING PARKED.** RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 43 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S42 closed Sat 5 Sep ~03:00.
   ⚠ If S43 opens the same day, the eight S42 rows (due 7 Sep) and the S41
   rows (due 5–6 Sep) are STILL not later-day evidence relative to when they
   were last taught. Check `last_asked` per row, not the session date.

2. ⚠ **RE-GATE AND RE-FRAME `sys.path` BEFORE THE [PREDICT]** — a break inside
   an open idea needs both (carry-forward from S41). Then fire it: *from the
   repo root `import s22_counter` fails. Two different ways to make it
   succeed, using only the printed list.* (Run from `drills/`, or
   `sys.path.append("drills")` — either; he has not seen `append` on
   `sys.path` so accept "add the folder to the list" in words.)

3. **THEN THE REST OF 1.10, in this order:** what a package is (a folder,
   `__init__.py`, dotted import) → relative vs absolute imports → circular
   imports (the S39 `main.py`/`robot.py` demo folder is reusable:
   `teaching/s39_imports/`) → the standard library as a reading skill → pip
   and third-party (his `/opt/ros/jazzy/.../site-packages` entry is the live
   example). FRAME FIRST on each; one idea per turn.

4. ⚠⚠ **DUE 5–6 SEP (S41 rated-low / failed, deferred out of S42 as same-
   sitting):** `UnboundLocalError` deletion test; `[[0]*3]*3`; `None`-as-
   absence (*why not `0`, why not `-1`*); `subscriptable`; `augmented
   assignment` with an alias. Plus the two S41 snippet facts: **hierarchy
   direction** (`except BadCommand:` vs a plain `ValueError`, both ways) and
   **refuse vs convert** (`type(angle) != int`). Run `python3 tools/retest.py
   --overdue` and take oldest first.

5. ⚠ **DUE 6 SEP, RE-TAUGHT S42, FIRST COLD PASS OR NOT:** `mutable default
   trap + sentinel` (ask `add_reading(10)` then `add_reading(20)` WITHOUT
   showing `__defaults__`; then the fix), `except ... as e` (**only the two
   printed lines — not "what is `e`", which is on credit**), `cell / closure`
   (he was told to read S19/S23 notes + `drills/s25_closure.py` first — that
   is legal, notes-then-recall on a later day).

6. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — pointed at
   `notes/session_21_notes.md` + `drills/s22_report.py`. The queue row is
   `global / *args / **kwargs`. Cold ask after he has read.

7. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement, the REPL half of
   frames/REPL-vs-script.

**Standing turn rules: FRAME FIRST; CONSOLIDATED QUESTIONS CARRY THEIR OWN
RUNNABLE CODE — AND SAY WHAT THE TASK IS (classify / predict / write), pushback
77; SPEC BEFORE PUZZLE; ONE TEACHING IDEA PER TURN AND PER DEMO; RED AS ONE
GROUP IN WORDS; asks near the top; doubt gate before every new subsection;
depth-before-answer (the fix alone does not discharge the why — held S42 on
ordering); NAME THE ERROR BEFORE THE MENTOR SHOWS IT, with NO warning that it
raises; rating AFTER his answer and BEFORE the verdict — held S42 throughout;
tag every block. Do not propose ending the session. NEVER EDIT HIS DRILL FILE.**

**CARRY FORWARD:**
- ⚠⚠ **A LONG BREAK INSIDE AN OPEN IDEA NEEDS A RE-GATE AND A RE-FRAME.**
  Applies to `sys.path` at the S43 open.
- ⚠⚠ **DECLARED GAP → FRAME → DEFINITION → [TEACH-BACK].** Held S42 on the
  mutable default (teach-back clean in two halves). On `except ... as e` the
  teach-back failed twice because the definition needed 1.12 — when a
  teach-back fails twice, check whether the SUBSTRATE is taught before
  re-asking a third time.
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S42 for
  all 20; it caught an untaught `{text!r}` before it was posed.
- ⚠ **Language fixes issued S42, all on intact mechanisms:** "CALL it" not
  "pass an argument to it"; "`zip()` RETURNS an iterator; the ITERATOR is
  exhausted" (fourth issue of that phrasing); "copies the REFERENCES";
  "braces" not "parentheses"; "no return REACHED"; "`__defaults__` is an
  attribute, not a method"; "runs WHILE true", not "till".
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()` vs
  `+`. Unchanged.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — a third instance S42 (debug `print(n)` left inside
  `halvings`). Full treatment still parked; the count is now three.
- Governance/format requests mid-session → PARK, close material, write at end.
- **Mentor demos, re-runnable:** `teaching/s41_gauntlet/fin_loop.py` (two
  `finally` shapes); `teaching/s39_imports/` (import semantics). S42 demos
  were scratch-only; their code and output are in `notes/session_42_notes.md`.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**136 rows, 97 [x], 39 [~], 28 overdue, 2 never asked.** Do not re-create the
table here. `python3 tools/retest.py` at the open.
**S42: 13 pass / 3 fail; 1 promotion (`function object vs call`), 1 demotion
(`cell / closure`), 8 rows added due 7 Sep** (`raise ... from`; `except
Exception vs bare except`; `hierarchy DIRECTION`; `except ORDERING`;
`exception INSTANCE` — on credit; `.pyc / bytecode cache`; `compiled AND
interpreted (PVM)`; `sys.path`). Details in ARCHIVE S42 §1 and §6.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls, reason spoken | **[x] — re-test at the next build block (a REAL LeRobot file, decided S42)** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S41 inverted under fatigue; **S42 re-taught with the tree drawn, teach-back + flip [PREDICT] clean** | **[~] — cold snippet ask, both directions, due 7 Sep** |
| **1.9 `raise ... from` / bare `except` / ordering** | S42 taught, teach-backs clean | **[~] — due 7 Sep** |
| **`except ... as e` — what `e` IS** | S42 FAIL, then taught, teach-back failed ×2 — SUBSTRATE ON CREDIT | **[~] — printed-lines half due 6 Sep; the object half waits for 1.12** |
| **MUTABLE DEFAULT + SENTINEL** | S42 FAIL 6 (model inverted), re-taught | **[~] — 6 Sep, first cold pass or not** |
| **CLOSURES — four layers** | S42 declared gap | **[~] at queue level (1.7 tick untouched) — after he reads S19/S23** |
| **`.pyc` / compiled-then-interpreted** | S42 taught; he named PVM himself | **[~] — due 7 Sep** |
| **`sys.path`** | S42 opened, [PREDICT] unanswered | **[~] — re-frame then fire at the S43 open** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — 8 Sep** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x] — 8 Sep** |
| **THE COMPILE/RUN SPLIT** | S41 pipeline 7; S42 the compiler-vs-interpreter question answered | **[x] — 6 Sep** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 `halvings` cold 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S38 full trace; S41 UBL taught | **[x] — 6 Sep; UBL deletion test due** |
| **THE MUTATING TELL** | S38 both halves | **[x] — 6 Sep** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | **S42: PASS 8 / 8, both** | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | **S42: PASS 8 / 8 / 7** | **[x] — 10–17 Sep; the `[[0]*3]*3` case still due** |
| **`constructors`** | S38 7/10; S42 `set()` given unprompted | **[x] — 6 Sep** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 `finally` guarantee** | S41: PASS 7 | **[x] — 8 Sep** |
| **`short-circuit`** | S41: PASS 7 | **[x] — 8 Sep** |
| **1.9 try/except** | S36 promoted; S41 drill clean | **[x] — 5 Sep** |
| **RAISE-VS-SHRUG / `None` returns / expression-vs-statement** | **S42: PASS 8 / 8 / 8** | **[x] — 17 Sep** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK still owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S41 DEMOTED | **[~] — 6 Sep** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames only | [~] **the REPL half still overdue** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **S41's "edit my drill / skip it" DID NOT RECUR IN S42.** Two declared
  gaps, both honest, both followed by a request for the notes pointer rather
  than for an answer. Read S41 as fatigue, as STATE said. Watch stays.
- ⚠⚠ **RIGHT OUTPUT, WRONG MODEL — one more instance:** the mutable default
  (*"a new empty list each call"*). Same signature as `+=`, `[[0]*3]*3`,
  `short-circuit`. Keep asking the WHY after every right output.
- ⚠⚠ **HE ASKS THE INTERVIEW QUESTION HIMSELF:** *"then when would I ever
  catch by BadCommand?"* and *"why call it an interpreter if Python is
  compiled?"* Both were the right questions. Answer them honestly and at
  their real size; a frame that oversells gets demolished (S18/S19/S28).
- ⚠ **CONFIDENCE CALIBRATION — ONE OVER-RATING:** 8 on the `except ... as e`
  miss. Everything else calibrated (6 on the mutable-default miss; 7–8 on
  clean passes; no rating offered on the declared closure gap). Use ≤5 as
  the targeting signal; note that 8-on-a-miss now has one data point.
- ⚠ **REFUSES TO GUESS, CONSISTENTLY — third session running:** *"have we
  studied this `from`?"*, *"I am not sure about this question"*, *"no idea"*.
  Do not push through; teach, then re-ask.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()` as an
  object, `.append()` vs `+`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 78 raised, 76 upheld or
  part-upheld.** S42: 77 (complete code + task shape, S19) and 78 (*"your
  language is not clear"*), both upheld in full.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`.pyc` / bytecode — PAID S42.** The C eval loop itself → 1.13.
- ✅ **BREAKPOINT DEBUGGING / `pdb` — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT, and the cost grew in S42:** `except ... as e`
  cannot be fully taught without class → object. 1.12 owes him the real
  unit; open it with the exception classes as the first worked example.
- ⚠ **`sys.path.append` / editing the list** — one line, when the [PREDICT]
  fires.
- ⚠ **`enumerate()`** — used by the mentor S41, never taught. Define before a
  drill uses it.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — belongs
  with `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances now)**; **EXPRESSION vs STATEMENT** (passed
  S42); **`__dict__`** (1.12–1.13); **PEP 709** (1.13); `nonlocal` (1.13);
  `pop` internals (1.13); `copy.copy()` one line; deepcopy on self-reference
  (1.13); bytecode constants + `dis` (1.13); **HASH RANDOMISATION** (1.13);
  **`%` and `.format()`** as a reading skill; `!r` in an f-string (unshown,
  removed from an S42 demo); `capsys` — not Layer 0.

---
