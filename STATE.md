# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 46 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S45**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S45 at the open. ⚠ **S45 LESSON: RE-STATE THE
#      GATE WHEN A NEW BLOCK STARTS AFTER A PAUSE.** S45 ran three blocks
#      over two calendar days and the gate was stated once. The gate is
#      PER-MATERIAL (RULES S17-1) and per-block.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED. NO DECISION IS OWED.**
#   5. ⚠ **THE QUEUE IS A SCRIPT.** `python3 tools/retest.py --overdue --all`
#      at the open. **143 rows, 99 [x], 44 [~]. NOTHING FIRED IN S44 OR S45 —
#      two sessions of 1.10 with zero volley.** `--asked` substring-matches:
#      the bare `print()` row and the two `zip` rows need `tools/queue.json`
#      edited directly.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S45.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN — AND ONE IDEA PER DEMO.** Held S45.
#   9. ⚠⚠ **WHEN HE ASKS A DIRECT QUESTION, ANSWER IT. DO NOT REPLY WITH A
#      QUESTION.** Pushbacks 79, 82. Held S45 (six direct questions, six
#      direct answers, each followed by a run).
#  10. ⚠⚠ **FILES YOU CREATE: SAY SO, LIST THE PATHS, PASTE EACH FILE'S CODE
#      UNDER ITS PATH — AND ONLY AFTER THEY EXIST.** Pushback 85 (S45): a
#      file was described as if on disk before it was written.
#  11. ⚠⚠ **NEVER OVERWRITE A FILE WITHOUT LOOKING AT IT FIRST.** Held S45.
#  12. ⚠⚠ **NO `python3 -c` IN A DEMO. WRITE THE FILE.** Held S45.
#  13. ⚠⚠ **A QUESTION CARRIES ITS FULL SCENARIO. NEVER "look at the output
#      from earlier".** Pushback 86 (S45). S19 rule, breached again.
#  14. ⚠⚠ **NEVER ASK HIM TO NAME AN ERROR HE HAS NEVER SEEN.** Pushback 87
#      (S45): *"how will I predict something I haven't seen, please stop
#      doing this behaviour."* [PREDICT] covers print lines and mechanism
#      reasoned from a walk; an unseen LABEL is a guess. S27 name-the-error
#      applies to error types already taught.
#  15. ⚠ **`except ... as e` NEEDS class → object, ON CREDIT UNTIL 1.12.**
#
# STATE AS OF: end of Session 45, **Tue 8 Sep 2026, 22:24** (verified from
# `date`; THREE blocks — Mon 21:37 → ~22:10; Tue ~08:50 → ~11:00; Tue ~21:05
# → 22:24, from demo mtimes). Stopped mid-stdlib: *"lets continue from the
# same point tomorrow."*
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S45 yield (~3h across three blocks):** `sys.modules` discomfort worked
  to the ground (dict → two keys → bound name → route rule → `__main__`);
  absolute vs relative RE-WALKED at his request with three probe files;
  **CIRCULAR IMPORTS taught and closed as taught material**, both fixes;
  **STDLIB OPENED**, two ideas, the real `json` front door shown. **No cold
  ask fired. Zero promotions, correctly.** ~0.5 unit-equivalent. Four
  pushbacks, all upheld or part-upheld.
- **Position: 1.1–1.8 closed. 1.9 — three [x] of ten, seven [~], cold asks
  OVERDUE since 7 Sep. 1.10 — six [x]; `sys.path`, `.pyc`, `packages`,
  `relative vs absolute`, `circular imports`, `standard library` [~]; one
  [ ] (pip / third-party).**
- ✅ **DECIDED S42:** once 1.10 lands, the weekly cold build block moves to a
  **REAL LeRobot file**. 1.10 is one bullet from landing.
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.10 — stdlib idea 3 / pip next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S45, NOTHING PARKED.** RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 46 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S45 closed Tue 8 Sep 22:24.
   S45 material (circular, stdlib, route rule, `__main__` placeholder) is
   legal from 9 Sep evening at the earliest; the queue rows say 10 Sep.
   Packages / relative imports were RE-WALKED on 7–8 Sep, so their 8 Sep
   due dates were pushed to 10 Sep. Older material (1.9, and everything
   overdue since August) is legal now.

2. ⚠⚠ **OPEN WITH THE OVERDUE VOLLEY THIS TIME.** `python3 tools/retest.py
   --overdue --all`, oldest first, task-first, text. A block of 8 BEFORE
   any 1.10 work. Two sessions running have fired nothing. Still due from
   S41/S42: `UnboundLocalError` deletion test; `[[0]*3]*3`; `None`-as-
   absence; `subscriptable`; `augmented assignment` with an alias;
   **hierarchy direction** both ways; **refuse vs convert**; `mutable
   default + sentinel`; `except ... as e` (printed lines only); `< > ^ in a
   format spec` (FAILED S43); `keyword argument` label (FAILED S43).

3. **THEN 1.10, from the held teach-back:** *why did `import arm` give an
   empty namespace and `import json` twelve names?* (answer: `json`'s
   `__init__.py` holds `from .decoder import ...`; `arm`'s only prints).
   Doubt gate. Then stdlib idea 3 — open one stdlib file and READ it
   (`bisect.py` is short and pure Python; or `json/decoder.py` since he
   has its `__file__`). **Define `enumerate()` here** (one line + queue
   row). Then **pip / site-packages** (~20 min): where `pip install` puts
   files; why that folder is on `sys.path`; his `/opt/ros/jazzy/lib/
   python3.12/site-packages` entry (second on the list, printed S45 in
   `teaching/s45_stdlib/where_is.py`); `sys.path.append` as a smell.
   That closes 1.10 as taught. Then act on the S42 decision (LeRobot
   build block).

4. ⚠⚠ **PARKED AT HIS REQUEST, WITH THE ANSWER GIVEN:** the absolute form
   of `from . import limits`. He converted it to `import arm.limits` for
   the THIRD time (S43, S44, S45) and said *"can we skip this for now, its
   been bugging me since last 3 days."* Answer given plainly: `from arm
   import limits`; rule `import X.Y` binds `X`, `from X import Y` binds
   `Y`. **Do not re-open it as teaching. It comes back as a cold task on
   10 Sep or later, task-first: a file inside `arm/` and "which one name
   is in `vars()` after this line".**

5. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — `notes/session_21_notes.md`
   + `drills/s22_report.py`. Cold ask after. Not touched S44 or S45.

6. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half of
   frames/REPL-vs-script (legal).

**Standing turn rules: FRAME FIRST, physical-first, ROUTE FIRST for
anything import-shaped; ANSWER A DIRECT QUESTION DIRECTLY; FILES BY PATH
WITH CODE, AFTER THEY EXIST; NO `-c`; EVERY QUESTION CARRIES ITS FULL
SCENARIO; NEVER ASK FOR AN UNSEEN ERROR NAME; SPEC BEFORE PUZZLE; ONE
TEACHING IDEA PER TURN AND PER DEMO; asks near the top; doubt gate before
every new subsection; depth-before-answer; rating AFTER his answer and
BEFORE the verdict; tag every block. Do not propose ending the session.
NEVER EDIT HIS DRILL FILE. NEVER OVERWRITE A FILE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **THE ROUTE RULE IS WHAT LANDED. LEAD WITH IT.** Three sessions of
  "two tables" did not stick; one demo of the same file loaded as `limits`
  (run from inside `arm/`) and as `arm.limits` (run from outside) did. His
  words: *"what decides whether we will have `limits` or `arm.limits` is
  `sys.path[0]` or the base folder from where we start."* For any future
  import question, start from `sys.path[0]` and the route.
- ⚠⚠ **THE BOUND-NAME MISS FLIPPED, THE FORM-CONVERSION MISS DID NOT.** He
  said `arm` for `import arm.limits` unprompted (first time right, S45
  block 1). He still converts `from . import limits` to `import arm.limits`
  (third time). These are now two separate rows; see item 4.
- ⚠ **RUN-DIRECTLY TRAP MISSED A SECOND TIME** (`python3 arm/safety_rel.py`
  → he gave the two `running` lines). After the route rule and the
  `__main__` demo he predicted `run_safety_rel.py` in full. Depth-before-
  answer: he answers the happy path without checking how the file was
  reached. Cold ask on 10 Sep decides.
- ⚠ **`__main__` was "less intuitive" to him** — answered with
  `arm/whoami.py` (same file, `__name__` printed both ways). He accepted
  it as a placeholder for "the file that was started". New queue row.
- ⚠ **Circular: "kind of an infinite loop"** — corrected; the early key
  PREVENTS the loop. His final teach-back on the fix was clean: *"the
  function object gets built but is not executed till it is called."*
- ⚠ **`print(arm)` with `arm` not a name → `ModuleNotFoundError` (S44).**
  `NameError` is [x] (due 10 Sep). WATCH.
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S45.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()` vs
  `+`, `enumerate()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — three instances; full treatment still parked.
- Governance/format requests mid-session → PARK, close material, write at end.
- **Mentor demos, re-runnable:** `teaching/s45_cache/` (`see_modules.py`);
  `teaching/s43_packages/` now also holds `see_arm.py`, `see_names.py`,
  `see_arm_ns.py`, `run_p1..3.py` + `arm/p1..3.py`, `arm/direct.py`,
  `arm/whoami.py` + `run_whoami.py`, `run_safety_rel.py`;
  `teaching/s45_circular/` (`a.py`, `b.py`, `main.py`, `self_check.py`,
  `run_self_check.py`, `fix/`); `teaching/s45_stdlib/` (`where_is.py`,
  `front_door.py`).
- **Voice re-teach file:** `notes/voice_teach_packages_relative_imports.md`.
  He did not say whether the web voice pass happened; asked once, not
  answered, not chased.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**143 rows, 99 [x], 44 [~].** Do not re-create the table here.
`python3 tools/retest.py --overdue --all` at the open.
**S45: 0 rows fired. 4 rows added, all [~] due 10 Sep: `circular import /
partially initialized`; `the route decides the key / __main__ placeholder`;
`sys.modules key enters BEFORE the run`; `stdlib on disk / __file__ / front
door`. Three rows re-dated 8 → 10 Sep after same-sitting re-teaching:
`the import cache / sys.modules` [x], `package / __init__.py / bound name`,
`relative import / the dot / run-directly trap`.**

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls | **[x] — re-test at the next build block (REAL LeRobot file)** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S42 re-taught, teach-back clean | **[~] — cold snippet ask, both directions, OVERDUE (7 Sep)** |
| **1.9 `raise ... from` / bare `except` / ordering** | S42 taught | **[~] — OVERDUE (7 Sep)** |
| **`except ... as e` — what `e` IS** | S42 FAIL, substrate on credit | **[~] — printed-lines half due; object half waits for 1.12** |
| **MUTABLE DEFAULT + SENTINEL** | S42 FAIL 6, re-taught | **[~] — OVERDUE** |
| **CLOSURES — four layers** | S42 declared gap | **[~] at queue level — after he reads S19/S23** |
| **`.pyc` / compiled-then-interpreted** | S42 taught | **[~] — OVERDUE (7 Sep)** |
| **`sys.path`** | S43 taught; S45 used as the start of the route rule | **[~] — OVERDUE (7 Sep): "why does the import fail, two fixes"** |
| **PACKAGES** | **S45: `sys.modules` keys, bound name `arm` (RIGHT, first time), `__init__.py` does not load the folder, route rule — all restated by him same-sitting** | **[~] — cold ask 10 Sep, task-first** |
| **RELATIVE vs ABSOLUTE IMPORTS** | **S45 re-walked with probes p1–p3; `from . import limits` → `import arm.limits` THIRD time, PARKED with answer; run-directly trap missed then reasoned; `run_safety_rel.py` predicted in full** | **[~] — cold ask 10 Sep, both halves** |
| **CIRCULAR IMPORTS** | **S45 taught: early key, half-built hit, `ImportError: cannot import name`, two fixes; teach-backs clean after "infinite loop" corrected** | **[~] — cold ask 10 Sep** |
| **STDLIB / FRONT DOOR** | **S45 opened: `__file__`, fourth `sys.path` entry, `json/__init__.py` lines 106–108, four keys / twelve names; teach-back HELD** | **[~] — finish S46, cold ask later** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | S43 taught | **[~] — due 8 Sep, now legal** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — cache row re-dated 10 Sep (re-told S45)** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x] — 8 Sep, legal** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — OVERDUE** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S38 full trace | **[x] — OVERDUE; UBL deletion test due** |
| **THE MUTATING TELL** | S38 both halves | **[x] — OVERDUE** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | S42: PASS 8 / 8 / 7 | **[x] — 10–17 Sep; `[[0]*3]*3` still due** |
| **`constructors`** | S38 7/10 | **[x] — OVERDUE** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 `finally` guarantee** | S41: PASS 7 | **[x] — 8 Sep, legal** |
| **`short-circuit`** | S41: PASS 7 | **[x] — 8 Sep, legal** |
| **1.9 try/except** | S41 drill clean | **[x] — OVERDUE** |
| **RAISE-VS-SHRUG / `None` returns / expression-vs-statement** | S42: PASS 8 / 8 / 8 | **[x] — 17 Sep** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK still owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S41 DEMOTED | **[~] — OVERDUE** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; S43 REPL defined | [~] **cold ask on both halves now legal** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **DELIVERY, NOT RETENTION, WAS THE PROBLEM AGAIN (S43, S44, S45).**
  S45: four pushbacks on presentation (84 sequencing, 85 phantom file, 86
  half scenario, 87 unseen error label). Once the demo was a real file run
  from a stated folder, he restated everything correctly. **Three sessions
  running. The watch is on the MENTOR.**
- ⚠⚠ **HE NAMES HIS OWN LIMIT AND PARKS** — *"can we skip this for now,
  its been bugging me since last 3 days"* (S45) and *"I am not eligible to
  answer this"* (S45). Both correct calls. Honour them, park with the
  answer attached, bring the item back cold.
- ⚠⚠ **HE ASKS TO BE QUIZZED** (S44 twice; S45: *"ask me all the questions
  you can to check my understanding"*). Give the quiz; tag it [TEACH-BACK]
  same-day; every question carries its full scenario.
- ⚠ **FORM-CONVERSION MISS, THREE TIMES (`from . import limits` →
  `import arm.limits`).** Now a real gap, parked at his request. Cold task
  10 Sep. Root cause candidate: he reaches for the form he TYPES most.
- ⚠ **SURFACE ANSWER on the run-directly trap, second time.** Same class as
  S20 `digit_sum`. He recovers fully once asked "how was the file reached?"
- ⚠ **HE ASKS THE GOOD QUESTION HIMSELF (S45):** *"can `limits.py` be loaded
  independently, or is everything always `arm.something`?"* — exactly the
  route question, and answering it (`arm/direct.py`) is what made the
  whole unit land. *"isn't the key built after `a` has fully executed?"* —
  the circular-import crux, answered with `self_check.py`.
- ⚠ **CONFIDENCE CALIBRATION:** no ratings taken S44 or S45 (all same-day).
  Use ≤5 as the targeting signal; a 7+ on a LABEL is unreliable until
  three clean.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()`,
  `.append()` vs `+`, `enumerate()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 87 raised, 85 upheld or
  part-upheld.** S45: 84 part-upheld, 85, 86, 87 upheld.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`.pyc` — PAID S42.** ✅ **REPL — DEFINED S43.** ✅ **`python3 -c` —
  DEFINED S44, retired.** ✅ **bare `vars()` — DEFINED S44.** ✅ **`__file__`
  — DEFINED S45.** ✅ **`__init__.py` as a FRONT DOOR — SHOWN LIVE S45 in
  `json/__init__.py`; the `arm` version still not built by him (do it at
  the LeRobot reading turn).**
- ✅ **`sys.path.append` — SHOWN S43**, "smell in a real codebase" owed at
  the pip/site-packages turn (S46).
- ⚠ **Two module objects for one file** (loaded as `limits` AND as
  `arm.limits` in one program) — stated S45 as a real bug class, not
  demonstrated. One demo owed if it comes up.
- ⚠ **`..` (two dots, parent package)** — one line said S44, never shown.
- ⚠ **`python3 -m`** — used in a mentor-side check S45, never shown to him.
  Do not use in a demo until defined.
- ✅ **BREAKPOINT DEBUGGING / `pdb` — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 opens with the exception classes.
- ⚠ **`enumerate()`** — used by him S43, never taught. Define at stdlib idea 3.
- ⚠ **Python does not expand `~`** — said S43; `os.path.expanduser` → 1.11.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — with
  `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances)**; **`__dict__`** (1.12–1.13); **PEP 709**
  (1.13); `nonlocal` (1.13); `pop` internals (1.13); `copy.copy()` one line;
  deepcopy on self-reference (1.13); bytecode constants + `dis` (1.13);
  **HASH RANDOMISATION** (1.13); **`%` and `.format()`** as a reading skill;
  `!r` in an f-string; `capsys` — not Layer 0.

---
