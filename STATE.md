# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 44 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S43**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S43. The gate is PER-MATERIAL (RULES S17-1).
#      ⚠ S43 ran across TWO calendar days (opened Sat 17:03, paused after the
#      term-tax, resumed Sunday, closed Sun ~23:00). Check `last_asked` per row.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED. NO DECISION IS OWED.**
#   5. ⚠ **THE QUEUE IS A SCRIPT.** `python3 tools/retest.py --overdue --all`
#      at the open. **137 rows, 99 [x], 38 [~], 36 overdue, 2 never asked.**
#      ⚠ `--asked` substring-matches: the bare `print()` row and the two `zip`
#      rows cannot be hit by name; edit `tools/queue.json` directly for those.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S43.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN — AND ONE IDEA PER DEMO.**
#   9. ⚠⚠ **S43 LESSON — WHEN HE ASKS A DIRECT QUESTION, ANSWER IT. DO NOT
#      REPLY WITH A [PREDICT].** Pushback 79, upheld. FOUNDATION BEFORE
#      PREDICTION: an untaught rule gets taught, then asked.
#  10. ⚠⚠ **S43 LESSON — WHEN YOU CREATE FILES, SAY SO, LIST THE PATHS, AND
#      PASTE EACH FILE'S CODE UNDER ITS PATH.** A tree diagram is not an
#      explanation. Pushback 80, upheld.
#  11. ⚠⚠ **NEVER OVERWRITE A FILE WITHOUT LOOKING AT IT FIRST.** S43: the
#      untracked S42 demo `teaching/s39_imports/where.py` was clobbered by a
#      `printf >`. Content lost. Mentor failure, see ARCHIVE S43 §5.
#  12. ⚠ **`except ... as e` NEEDS class → object, ON CREDIT UNTIL 1.12.**
#      Do not test "what is `e`" cold before 1.12.
#
# STATE AS OF: end of Session 43, **Sun 6 Sep 2026, ~23:00** (verified).
# Next: Session 44 — **packages [TEACH-BACK] first (re-frame), then the rest
# of 1.10; overdue volley between units.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S43 yield:** term-tax 4 terms (2 promoted, 2 stayed [~]); positional vs
  keyword ORDER + double-fill taught (new); import cache RE-TAUGHT at his
  request as the five-step story; `sys.path` taught to the ground (three
  restatements) and its [PREDICT] answered; REPL finally defined; **packages
  OPENED** (`teaching/s43_packages/`), stopped one teach-back short.
  ~0.4 unit-equivalent. Slow session: two pushbacks on delivery, both upheld.
- **Position: 1.1–1.8 closed. 1.9 — every bullet taught; three [x] of ten,
  seven [~] with cold asks due 7 Sep. 1.10 — six [x], `sys.path` + `.pyc` +
  `packages` [~], three [ ] (relative vs absolute, circular, stdlib/pip).**
- ✅ **DECIDED S42:** once 1.10 lands, the weekly cold build block moves to a
  **REAL LeRobot file**. Act on it when 1.10 closes.
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.10 second half — packages open.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S43, NOTHING PARKED.** RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 44 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S43 closed Sun 6 Sep ~23:00.
   The S42 rows (due 7 Sep) were taught Sat 5 Sep 00:00–03:00 and are legal
   from 7 Sep. The S43-taught rows (`positional vs keyword ORDER`, due 8 Sep)
   and `packages` are legal from 8 Sep.

2. ⚠ **RE-FRAME PACKAGES, THEN THE HELD [TEACH-BACK]** — a break inside an
   open idea (carry-forward rule). The demo is real and on disk:
   `teaching/s43_packages/use_arm.py`, `arm/__init__.py`, `arm/limits.py`.
   Tell him to OPEN the three files by path; paste each file's code under
   its path. Established so far: folder + `__init__.py` = package;
   `import arm.limits` runs `__init__.py` then `limits.py`, binds ONE name
   `arm`, and `arm` IS the `__init__.py` module object (`print(arm)` shows
   it); `limits` is an attribute on `arm`. **He predicted the bound name as
   `arm.limits` — a [PREDICT] miss, not logged.** The held question: *why
   does `__init__.py` run first, and what does it become?*

3. **THEN FINISH PACKAGES, one idea per turn:** `from arm import limits`
   (binds `limits`), `from arm.limits import MAX_ANGLE`; an EMPTY
   `__init__.py` is the normal case; the `sys.modules` keys `"arm"` and
   `"arm.limits"`. Then **relative vs absolute imports** → **circular
   imports** (`teaching/s39_imports/` is reusable) → **the standard library
   as a reading skill** → **pip and third-party** (his
   `/opt/ros/jazzy/.../site-packages` entry is the live example, and it is
   why `sys.path.append` in a real codebase is a smell — promised S43).
   FRAME FIRST on each.

4. ⚠⚠ **OVERDUE VOLLEY — 36 rows.** `python3 tools/retest.py --overdue
   --all`, oldest first, task-first. Still due from S41/S42: `UnboundLocal
   Error` deletion test; `[[0]*3]*3`; `None`-as-absence (*why not `0`*);
   `subscriptable`; `augmented assignment` with an alias; **hierarchy
   direction** both ways; **refuse vs convert**; `mutable default + sentinel`
   (`add_reading(10)` then `add_reading(20)`, no `__defaults__`); `except
   ... as e` (printed lines only); `cell / closure` (after he reads S19/S23).
   ⚠ `< > ^ in a format spec` FAILED S43 — `^` and "overrides the type
   default" both missing; due 6 Sep, ask cold.
   ⚠ `keyword argument / parameter vs argument` FAILED S43 on the keyword
   half (called it a *default argument*; could not name it). The
   parameter/argument half PASSED at 6. Ask the keyword label cold, due 7 Sep.

5. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — `notes/session_21_notes.md`
   + `drills/s22_report.py`. Row `global / *args / **kwargs`. Cold ask after.

6. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement. **The REPL half of
   frames/REPL-vs-script was TAUGHT S43 (Read-Eval-Print-Loop, `''` in slot
   0); cold ask now legal.**

7. ⚠ **`enumerate()` — he used it correctly in the S43 term-tax, still never
   taught.** Define it at the next natural place (a `for` over a package
   listing, or the stdlib turn). One line, then a queue row.

**Standing turn rules: FRAME FIRST; ANSWER A DIRECT QUESTION DIRECTLY
(pushback 79); FILES YOU CREATE ARE ANNOUNCED BY PATH WITH THEIR CODE
(pushback 80); CONSOLIDATED QUESTIONS CARRY THEIR OWN RUNNABLE CODE; SPEC
BEFORE PUZZLE; ONE TEACHING IDEA PER TURN AND PER DEMO; asks near the top;
doubt gate before every new subsection; depth-before-answer; NAME THE ERROR
BEFORE THE MENTOR SHOWS IT, with NO warning that it raises; rating AFTER his
answer and BEFORE the verdict; tag every block. Do not propose ending the
session. NEVER EDIT HIS DRILL FILE. NEVER OVERWRITE A FILE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **A LONG BREAK INSIDE AN OPEN IDEA NEEDS A RE-GATE AND A RE-FRAME.**
  Applies to packages at the S44 open. Held S43 for `sys.path`.
- ⚠⚠ **PLAIN LANGUAGE FOR FRAMES.** `sys.path` needed THREE restatements:
  "entry 0", "slot", and a tree diagram all failed; *"the list of folders
  Python searches; slot 0 is the folder your script lives in"* landed. When
  he says *"keep the language simpler"*, restate from "what is it,
  physically" (a module, a variable, a list) before "what it is for".
- ⚠ **HE ASKED TO RESTART FROM THE CACHE** — an [x] item (`the import cache
  / sys.modules`, due 8 Sep). Logged as a WATCH, not a miss: no cold ask was
  posed. His full-flow teach-back was complete and correct. If the 8 Sep
  cold ask fails, that is the demotion, not this.
- ⚠ **DECLARED GAP → FRAME → DEFINITION → [TEACH-BACK].** Held S43 three
  times (keyword label, the ordering rule, REPL).
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S43.
- ⚠ **Language fixes issued S43, all on intact mechanisms:** unpacking takes
  apart a TUPLE into NAMES, not "placeholders"; the IMPORT MACHINERY
  searches, not "the compiler"; `sys.modules` is a DICT, not a file; the
  double-fill check happens AT THE CALL, not "inside" the body; a `SyntaxError`
  on `f(a=1, 2)` needs no `def` to be detected.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()` vs
  `+`, and now `enumerate()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — three instances; full treatment still parked.
- Governance/format requests mid-session → PARK, close material, write at end.
- **Mentor demos, re-runnable:** `teaching/s43_packages/` (package import
  order, bound name); `teaching/s39_imports/twice.py` (cache); `teaching/
  s39_imports/where.py` (**REWRITTEN S43** — prints `sys.path[0]`; the S42
  version is lost); `teaching/s41_gauntlet/fin_loop.py`.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**137 rows, 99 [x], 38 [~], 36 overdue, 2 never asked.** Do not re-create the
table here. `python3 tools/retest.py --overdue --all` at the open.
**S43: 4 rows fired (term-tax) — 2 pass/promote (`ZeroDivisionError` 6,
`unpacking` 5 incl. the count-mismatch `ValueError` half at 7), 2 fail (`< > ^
in a format spec`; `keyword argument / parameter vs argument` on the keyword
half). 1 row added: `positional vs keyword ORDER + double-fill` [~] due 8 Sep.**

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls | **[x] — re-test at the next build block (REAL LeRobot file)** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S42 re-taught, teach-back clean | **[~] — cold snippet ask, both directions, due 7 Sep** |
| **1.9 `raise ... from` / bare `except` / ordering** | S42 taught | **[~] — due 7 Sep** |
| **`except ... as e` — what `e` IS** | S42 FAIL, substrate on credit | **[~] — printed-lines half due; object half waits for 1.12** |
| **MUTABLE DEFAULT + SENTINEL** | S42 FAIL 6, re-taught | **[~] — first cold pass or not, OVERDUE** |
| **CLOSURES — four layers** | S42 declared gap | **[~] at queue level — after he reads S19/S23** |
| **`.pyc` / compiled-then-interpreted** | S42 taught | **[~] — due 7 Sep** |
| **`sys.path`** | **S43 taught to the ground, [PREDICT] answered (append ✓, files-together declined, `import ~/path` → SyntaxError)** | **[~] — cold ask due 7 Sep: "why does the import fail, two fixes"** |
| **PACKAGES** | **S43 opened; bound-name [PREDICT] missed; teach-back HELD** | **[~] — finish at the S44 open; cold ask due 8 Sep** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | **S43 taught after pushback 79; teach-back clean** | **[~] — due 8 Sep: `f(10, 20, arg1=99)` vs `f(arg1=1, 10, 20)`, name both errors** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — 8 Sep; the cache row is a WATCH after his S43 restart request** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x] — 8 Sep** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — OVERDUE** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S38 full trace | **[x] — OVERDUE; UBL deletion test due** |
| **THE MUTATING TELL** | S38 both halves | **[x] — OVERDUE** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | S42: PASS 8 / 8 / 7 | **[x] — 10–17 Sep; `[[0]*3]*3` still due** |
| **`constructors`** | S38 7/10 | **[x] — OVERDUE** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 `finally` guarantee** | S41: PASS 7 | **[x] — 8 Sep** |
| **`short-circuit`** | S41: PASS 7 | **[x] — 8 Sep** |
| **1.9 try/except** | S41 drill clean | **[x] — OVERDUE** |
| **RAISE-VS-SHRUG / `None` returns / expression-vs-statement** | S42: PASS 8 / 8 / 8 | **[x] — 17 Sep** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK still owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S41 DEMOTED | **[~] — OVERDUE** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; **S43 REPL defined** | [~] **cold ask on both halves now legal** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **DELIVERY, NOT RETENTION, WAS THE S43 PROBLEM.** Two upheld pushbacks
  on how material was presented (79: question answered with a question; 80:
  files created silently, tree diagram unexplained), and three restatements
  of `sys.path`. His reading was fine once the language was plain. The watch
  is on the MENTOR: physical-first frames, files by path with code.
- ⚠⚠ **RIGHT OUTPUT, WRONG MODEL — no new instance S43.** Keep asking WHY.
- ⚠ **HE ASKS THE GOOD QUESTION HIMSELF:** *"has unpacking even been taught?"*
  (it had — S21, verified from the queue before answering); *"I thought there
  is just one cache, `__pycache__`"* (two caches, distinguished); *"does
  `sys.path` hold everywhere we have run Python?"* (no — built fresh per
  process). Answer at real size.
- ⚠ **CONFIDENCE CALIBRATION — SECOND 7/8-ON-A-MISS:** rated 7 on the keyword
  half while calling it a default argument. S42 had 8 on `except ... as e`.
  Two data points now. Use ≤5 as the targeting signal; treat a 7+ on a label
  as unreliable until three clean.
- ⚠ **REFUSES TO GUESS, fourth session running:** *"I don't remember what we
  call name=value"*, *"I don't know how ... without touching the list"*. Teach,
  then re-ask. Held.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()`,
  `.append()` vs `+`, `enumerate()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 80 raised, 78 upheld or
  part-upheld.** S43: 79 and 80, both upheld in full.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`.pyc` / bytecode — PAID S42.** ✅ **REPL — DEFINED S43.**
- ✅ **`sys.path.append` — SHOWN S43**, with the "smell in a real codebase"
  promise owed at the pip/site-packages turn.
- ✅ **BREAKPOINT DEBUGGING / `pdb` — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 opens with the exception classes.
- ⚠ **`enumerate()`** — used by him S43, never taught. Define before a drill.
- ⚠ **Python does not expand `~`** — one line, said S43; `os.path.expanduser`
  belongs to 1.11.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — with
  `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances)**; **`__dict__`** (1.12–1.13); **PEP 709**
  (1.13); `nonlocal` (1.13); `pop` internals (1.13); `copy.copy()` one line;
  deepcopy on self-reference (1.13); bytecode constants + `dis` (1.13);
  **HASH RANDOMISATION** (1.13); **`%` and `.format()`** as a reading skill;
  `!r` in an f-string; `capsys` — not Layer 0.

---
