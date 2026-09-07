# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 45 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S44**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S44. The gate is PER-MATERIAL (RULES S17-1).
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED. NO DECISION IS OWED.**
#   5. ⚠ **THE QUEUE IS A SCRIPT.** `python3 tools/retest.py --overdue --all`
#      at the open. **139 rows, 99 [x], 40 [~], 49 OVERDUE. NOTHING WAS FIRED IN S44 —
#      the overdue pile only grew.** `--asked` substring-matches: the bare
#      `print()` row and the two `zip` rows need `tools/queue.json` edited
#      directly.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S44.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN — AND ONE IDEA PER DEMO.**
#   9. ⚠⚠ **WHEN HE ASKS A DIRECT QUESTION, ANSWER IT. DO NOT REPLY WITH A
#      QUESTION.** Pushback 79 (S43) AND pushback 82 (S44). Twice now. This
#      includes the S27 name-the-error ask: if he is mid-doubt, EXPLAIN the
#      run; save name-the-error for snippets posed as questions.
#  10. ⚠⚠ **FILES YOU CREATE: SAY SO, LIST THE PATHS, PASTE EACH FILE'S CODE
#      UNDER ITS PATH.** Held S44 for eight files.
#  11. ⚠⚠ **NEVER OVERWRITE A FILE WITHOUT LOOKING AT IT FIRST.** Held S44
#      (`test -e` before every `printf >`).
#  12. ⚠⚠ **S44 LESSON — NO `python3 -c` IN A DEMO. WRITE THE FILE.** He
#      could not follow `-c` and said so; it had never been defined. Also:
#      **bare `vars()` (no argument) was used untaught** — now defined
#      (namespace dict of the file you are in). Two define-before-use
#      breaches in one session. Check every token of a demo, not just the
#      headline construct.
#  13. ⚠ **`except ... as e` NEEDS class → object, ON CREDIT UNTIL 1.12.**
#
# STATE AS OF: end of Session 44, **Mon 7 Sep 2026, 21:18** (verified from the commit; TWO blocks — see yield).
# **He closed to do a VOICE re-teach of packages on the web, from
# `notes/voice_teach_packages_relative_imports.md`.** That pass is NOT
# ledger evidence. Next: Session 45 — cold asks on packages + relative
# imports (legal 8 Sep), then circular imports, then the overdue volley.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S44 yield (~2h30 in TWO blocks: 07:27 → ~09:00 packages; paused ~11h; ~20:20 → 21:18 relative imports + voice file):** packages re-framed and CLOSED for
  the day (held teach-back answered via his own question; `import arm`
  alone, `__init__.py`'s two uses, `from arm import limits`, `sys.modules`
  keys fixed by disk position); **relative vs absolute imports OPENED and
  taught through the run-directly trap**; two teach-backs; a voice re-teach
  file written at his request. **No cold ask fired. Zero promotions,
  correctly (same-day).** ~0.3 unit-equivalent. Three pushbacks, all upheld
  or part-upheld.
- **Position: 1.1–1.8 closed. 1.9 — three [x] of ten, seven [~] with cold
  asks due 7 Sep (NOT fired S44 — fire S45). 1.10 — six [x]; `sys.path`,
  `.pyc`, `packages`, `relative vs absolute` [~]; two [ ] (circular,
  stdlib/pip).**
- ✅ **DECIDED S42:** once 1.10 lands, the weekly cold build block moves to a
  **REAL LeRobot file**. Act on it when 1.10 closes.
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.10 — circular imports next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S44, NOTHING PARKED.** RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 45 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S44 closed Mon 7 Sep 21:18 (relative imports taught 20:20–21:05 — same evening).
   S44 material (packages close, relative imports, `-c`, bare `vars()`) is
   legal from 8 Sep. Ask him whether the web voice pass happened; it changes
   nothing on the ledger either way, but note it in the session block.

2. ⚠⚠ **COLD ASKS ON PACKAGES + RELATIVE IMPORTS (rows added S44, due 8
   Sep).** Task-first, text. Target the two misses that recurred:
   - **`import arm.limits` binds which NAME?** He said `arm.limits` in S43
     ([PREDICT]) and again in S44 ([TEACH-BACK]). A name has no dots. If he
     says it a third time cold, that is a real gap, and the fix is
     `print("arm" in vars(), "limits" in vars())` run by HIM.
   - **`from . import limits` → absolute form.** He converted it to
     `import arm.limits` (wrong form, wrong binding). Answer: `from arm
     import limits`.
   - **The trap:** `python3 arm/motion.py` → `ImportError: attempted
     relative import with no known parent package`, because a script run
     directly is loaded as `__main__` and has no dotted name to fill the
     dot from. He answered "syntax is valid" instead of the run — surface
     answer. Ask it as "what is printed / what breaks" on a real file.
   Demo files on disk, all runnable from `teaching/s43_packages/`: `use_arm.py`,
   `only_arm.py`, `from_arm.py`, `quiz1.py`, `run_motion.py`, `arm/__init__.py`,
   `arm/limits.py`, `arm/safety.py`, `arm/safety_rel.py`, `arm/motion.py`.

3. **THEN CIRCULAR IMPORTS** (`teaching/s39_imports/` reusable, or a new
   `a.py`/`b.py` pair under `teaching/s45_circular/`). FRAME FIRST, physical:
   two files that each `import` the other; the cache makes the second import
   find a HALF-BUILT module in `sys.modules`; `from a import x` then fails
   with `ImportError: cannot import name` because `x` is not defined yet.
   Prerequisite is the cache ([x], due 8 Sep — fire that cold ask FIRST as
   the gate). Then **stdlib as a reading skill** → **pip / site-packages**
   (his `/opt/ros/jazzy/.../site-packages` entry; `sys.path.append` as a
   smell — promised S43).

4. ⚠⚠ **OVERDUE VOLLEY — NOT RUN IN S44.** `python3 tools/retest.py
   --overdue --all`, oldest first, task-first. Still due from S41/S42:
   `UnboundLocalError` deletion test; `[[0]*3]*3`; `None`-as-absence (*why
   not `0`*); `subscriptable`; `augmented assignment` with an alias;
   **hierarchy direction** both ways; **refuse vs convert**; `mutable default
   + sentinel`; `except ... as e` (printed lines only); `cell / closure`
   (after he reads S19/S23); `< > ^ in a format spec` (FAILED S43);
   `keyword argument` label (FAILED S43 keyword half). Fire a block of 8
   between units; do not let 1.10 eat the whole session again.

5. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — `notes/session_21_notes.md`
   + `drills/s22_report.py`. Cold ask after.

6. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half of
   frames/REPL-vs-script (legal).

7. ⚠ **`enumerate()` — used correctly S43, never taught.** Define at the
   stdlib turn. One line, then a queue row.

**Standing turn rules: FRAME FIRST, physical-first; ANSWER A DIRECT QUESTION
DIRECTLY (79, 82); FILES BY PATH WITH CODE (80); NO `-c`, WRITE THE FILE;
CONSOLIDATED QUESTIONS CARRY THEIR OWN RUNNABLE CODE; SPEC BEFORE PUZZLE;
ONE TEACHING IDEA PER TURN AND PER DEMO; asks near the top; doubt gate
before every new subsection; depth-before-answer; NAME THE ERROR BEFORE THE
MENTOR SHOWS IT, on snippets posed as questions only; rating AFTER his
answer and BEFORE the verdict; tag every block. Do not propose ending the
session. NEVER EDIT HIS DRILL FILE. NEVER OVERWRITE A FILE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **WHEN HE SAYS "AMBIGUOUS" OR "SIMPLER", RESTATE SIDE-BY-SIDE FROM
  "WHAT IS IT PHYSICALLY".** S44 (83): absolute vs relative landed on the
  restatement that opened with the folder tree and called the dot "a word
  meaning my own folder". S43: `sys.path` same shape. Two data points; this
  is now the default frame style, not a fallback.
- ⚠⚠ **LOADED vs BOUND ARE TWO TABLES. SAY WHICH ONE YOU ARE ASKING ABOUT.**
  Pushback 81 (part-upheld): "what did `import arm.limits` import?" and
  "what NAME got bound?" are different questions. `sys.modules` keys are
  fixed by disk position (`"arm"`, `"arm.limits"`) for every import form;
  the name in the file depends on the form. This split is what he needs to
  hear until it sticks.
- ⚠ **He wanted `import arm` to make `arm.limits` valid.** Reasonable
  expectation, corrected by `only_arm.py` (`AttributeError`). The bridge is
  `__init__.py` containing `from . import limits` — the LeRobot front-door
  pattern. Not yet demonstrated live; do it at the circular-imports turn or
  when `__init__.py` comes up again.
- ⚠ **`print(arm)` with `arm` not a name → he said `ModuleNotFoundError`.**
  `NameError` is [x] (due 10 Sep). Label reached from the wrong table
  (module exists in `sys.modules`; name does not exist in the file). WATCH
  on the `NameError` row; not a miss — teach-back.
- ⚠ **HE ASKED TO RESTART FROM THE CACHE (S43)** — `the import cache /
  sys.modules` [x], due 8 Sep. WATCH. Fire it as the gate before circular.
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** One slip S44:
  the `from arm import limits` → `sys.modules` claim was stated, then run;
  it was right. Run first anyway.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()` vs
  `+`, `enumerate()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — three instances; full treatment still parked.
- Governance/format requests mid-session → PARK, close material, write at end.
  (S44: the voice-file request was a teaching artefact, not governance; it
  was written on the spot, correctly.)
- **Mentor demos, re-runnable:** `teaching/s43_packages/` (ten files, see
  item 2); `teaching/s39_imports/twice.py` (cache); `teaching/s39_imports/
  where.py` (S43 version, prints `sys.path[0]`); `teaching/s41_gauntlet/
  fin_loop.py`.
- **Voice re-teach file:** `notes/voice_teach_packages_relative_imports.md`
  — eight ideas, every file's code and output, mentor instructions at the
  top. Reusable as the template if he asks for one on another topic.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**139 rows, 99 [x], 40 [~].** Do not re-create the table here.
`python3 tools/retest.py --overdue --all` at the open.
**S44: 0 rows fired. 2 rows added, both [~] due 8 Sep: `package /
__init__.py / bound name`; `relative import / the dot / run-directly trap`.**

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
| **`sys.path`** | S43 taught to the ground | **[~] — OVERDUE (7 Sep): "why does the import fail, two fixes"** |
| **PACKAGES** | **S44 CLOSED for the day: `import arm` stops at `__init__.py`; two uses of `__init__.py`; `from arm import limits`; keys fixed by disk. Bound-name miss REPEATED in teach-back** | **[~] — cold ask due 8 Sep, target the bound name** |
| **RELATIVE vs ABSOLUTE IMPORTS** | **S44 OPENED and taught: the dot = "my own folder", filled from the module's dotted name; run-directly → `ImportError`. Teach-back: two flaws (wrong absolute form; answered syntax instead of the run)** | **[~] — cold ask due 8 Sep** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | S43 taught | **[~] — due 8 Sep** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — 8 Sep; the cache row is a WATCH; fire it as the circular-imports gate** |
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
| Frames / REPL vs script | S38 frames; S43 REPL defined | [~] **cold ask on both halves now legal** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **DELIVERY, NOT RETENTION, WAS THE PROBLEM AGAIN (S43, S44).** S44:
  three pushbacks on how material was presented (81: two questions run
  together; 82: question instead of explanation + untaught `vars()`; 83:
  ambiguous absolute/relative prose), plus `-c` used undefined. Once the
  language was physical and side-by-side, he restated everything correctly.
  **The watch is on the MENTOR.** Two sessions running.
- ⚠⚠ **HE NOW ASKS TO BE QUIZZED** (*"quiz me to see if the concept has
  landed"*, *"quiz me to find flaws in my logic"*) — twice in S44. That is
  the retrieval habit the course exists to build. Give the quiz when asked;
  tag it [TEACH-BACK] same-day, and say so.
- ⚠ **BOUND-NAME MISS, TWICE (`import X.Y` → he says the name is `X.Y`).**
  S43 [PREDICT], S44 [TEACH-BACK]. Not on the ledger yet. The 8 Sep cold
  ask decides. Root cause candidate: he reads `arm.limits` as one token
  because that is how he TYPES it; the split into name + attribute lookup
  has been said but not exercised by him. If it fails cold, make HIM run
  `vars()` on it.
- ⚠ **SURFACE ANSWER on the run-directly trap** — answered "the syntax is
  valid" to "run this file directly". Depth-before-answer, S20-3. Same
  shape as the S20 `digit_sum` no-trace. Lazy-thinking class.
- ⚠ **HE ASKS THE GOOD QUESTION HIMSELF (S44):** *"shouldn't `import arm`
  be the starting point, and then `arm.limits.MAX_ANGLE` valid?"* (wrong
  but exactly the right question — it IS the `__init__.py` front-door
  design); *"does `from arm import limits` put `arm` and `limits` or `arm`
  and `arm.limits` in `sys.modules`?"* (the loaded/bound split, asked
  precisely). Answer at real size.
- ⚠ **CONFIDENCE CALIBRATION:** no ratings taken S44 (all same-day). The
  S42/S43 finding stands: use ≤5 as the targeting signal; a 7+ on a LABEL
  is unreliable until three clean.
- ⚠ **REFUSES TO GUESS** — no instance S44; he answered everything asked.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()`,
  `.append()` vs `+`, `enumerate()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 83 raised, 81 upheld or
  part-upheld.** S44: 81 part-upheld, 82 upheld, 83 upheld.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`.pyc` — PAID S42.** ✅ **REPL — DEFINED S43.** ✅ **`python3 -c` —
  DEFINED S44** (run the quoted text as code instead of a file; then
  retired from demos). ✅ **bare `vars()` — DEFINED S44.**
- ✅ **`sys.path.append` — SHOWN S43**, "smell in a real codebase" owed at
  the pip/site-packages turn.
- ⚠ **`__init__.py` as a FRONT DOOR (`from . import limits` inside it, so
  `import arm` alone exposes `arm.limits`)** — explained S44, NOT
  demonstrated live. He said *"I believe we will be exploring this further
  in detail"* — yes, at the LeRobot reading turn. Owed.
- ⚠ **`..` (two dots, parent package)** — one line said S44, never shown.
- ✅ **BREAKPOINT DEBUGGING / `pdb` — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 opens with the exception classes.
- ⚠ **`enumerate()`** — used by him S43, never taught. Define before a drill.
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
