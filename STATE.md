# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 47 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S46**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S46 at the open. Re-state it per block.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED. NO DECISION IS OWED.**
#   5. ⚠⚠⚠ **THE VOLLEY FIRES FIRST. THREE SESSIONS (S44, S45, S46) HAVE
#      FIRED ZERO COLD ASKS.** `python3 tools/retest.py --overdue --all` at
#      the open. **149 rows, 99 [x], 50 [~].** Say at the open, in one line,
#      that the volley of 8 runs BEFORE any teaching and why. If he asks to
#      start elsewhere, say what that costs and do it only if he insists.
#      `--asked` substring-matches: the bare `print()` row and the two `zip`
#      rows need `tools/queue.json` edited directly.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S46.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN — AND ONE IDEA PER DEMO. PHYSICAL,
#      NEVER A NUMBERED LIST OF RULES.** Pushback 89 (S46): a five-point
#      restatement of the route rule → *"sorry not understood"*; the same
#      walk done with `ls` in the shell landed at once. Fourth session
#      where prose failed and a run succeeded.
#   9. ⚠⚠ **WHEN HE ASKS A DIRECT QUESTION, ANSWER IT.** Held S46 (five).
#  10. ⚠⚠ **FILES YOU CREATE: SAY SO, LIST THE PATHS, PASTE EACH FILE'S CODE
#      UNDER ITS PATH, AND SHOW THE COMMAND THAT RAN IT.** Pushback 93
#      (S46): output shown without `$ cd ...; $ python3 main.py`. Pushback
#      91 (S46): lines quoted from a file on disk must be LABELLED read-
#      not-run.
#  11. ⚠⚠ **NEVER OVERWRITE A FILE WITHOUT LOOKING AT IT FIRST.** Held S46.
#  12. ⚠⚠ **NO `python3 -c` IN A DEMO. WRITE THE FILE.** Held S46.
#  13. ⚠⚠ **A QUESTION CARRIES ITS FULL SCENARIO.** Held S46.
#  14. ⚠⚠ **NEVER ASK HIM TO NAME AN ERROR HE HAS NEVER SEEN.** Held S46.
#  15. ⚠⚠ **FRAME FIRST, EVEN FOR A FUNCTION YOU ARE ONLY READING.**
#      Pushback 90 (S46): `bisect_left` on screen with no what/why.
#  16. ⚠⚠⚠ **WHEN HE SAYS STOP, THE CLOSE IS WRITTEN IN THAT TURN, ALL SIX
#      STEPS, BEFORE ANYTHING ELSE.** Pushback 94 (S46): two read-only
#      checks ran and the turn ended with nothing written; he found the
#      uncommitted folders the next day. Never end a turn between "stop"
#      and `git push`.
#  17. ⚠ **`except ... as e` NEEDS class → object, ON CREDIT UNTIL 1.12.**
#
# STATE AS OF: end of Session 46, **Thu 10 Sep 2026, ~21:45** (`date` 21:44
# at his close request; demo mtimes 19:27 → 21:32; open 16:25). **Close
# files written Fri 11 Sep 18:17**, see item 16. He asked *"what is the next
# unit?"* then *"close the session for today."*
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S46 yield (~5h, one block with pauses):** stdlib RE-WALKED from its
  frame and FINISHED (idea 3: `bisect.py` read); `enumerate()`, bare `*`,
  `max()`/`min()` defined; **PIP / SITE-PACKAGES opened and taught with a
  live shadowing bug. 1.10 IS TAUGHT-COMPLETE.** No cold ask fired, no
  rating, zero promotions. ~0.5 unit-equivalent. Seven pushbacks.
- **Position: 1.1–1.8 closed. 1.9 — three [x] of ten, seven [~], cold asks
  OVERDUE since 7 Sep. 1.10 — six [x], seven [~], zero [ ].**
- ✅ **DECIDED S42:** once 1.10 lands, the weekly cold build block moves to a
  **REAL LeRobot file**. 1.10 is taught-complete; place the block now.
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.10 cold asks → LeRobot block → 1.11.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S46, NOTHING PARKED.** RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 47 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S46 closed Thu 10 Sep ~21:45
   (files Fri 11 Sep 18:17). S46 material (stdlib re-walk, `bisect`, `*`,
   `enumerate`, pip, shadowing, key order) is legal from 12 Sep. All
   older 1.10 rows are legal now. Everything from August is legal now.

2. ⚠⚠⚠ **THE VOLLEY. FIRST. STATE IT AT THE OPEN.** `python3 tools/
   retest.py --overdue --all`, oldest first, task-first, text, one at a
   time, rating after his answer. A block of 8 BEFORE anything else.
   Volley 1 was posed in S46 and not answered; re-pose it:
   `grid = [[0] * 3] * 3; grid[0][0] = 7; print(grid)` → exact line +
   what the outer `* 3` makes three of (run-verified: three references
   to ONE inner list). Then from the S41/S42 list: `UnboundLocalError`
   deletion test; `None`-as-absence; `subscriptable`; `augmented
   assignment` with an alias; **hierarchy direction** both ways
   (run-verified snippet: `except LookupError` before `except KeyError`
   on a missing dict key → `"lookup"`); **refuse vs convert**; `mutable
   default + sentinel`; `< > ^ in a format spec` (FAILED S43); `keyword
   argument` label (FAILED S43).

3. **THEN the 1.10 cold asks, task-first, each with its full scenario:**
   - **Route rule** (GAPPED at 42h in S46): a `sys.path` list printed in
     the question, "walk `import X` and say where it stops and what runs."
   - **Packages bound name**: which one name is in `vars()` after
     `import arm.limits`.
   - ⚠⚠ **`from . import limits` absolute form** (PARKED S45 at his
     request, answer given: `from arm import limits`; rule `import X.Y`
     binds `X`, `from X import Y` binds `Y`). Cold task: a file inside
     `arm/`, "which one name is in `vars()` after this line". Do not
     re-teach; he said in S46 it is *"still hurting"* and parked it again.
   - **Run-directly trap** (missed twice): `python3 arm/safety_rel.py`.
   - **Circular**: the two-file scenario, error name (SEEN, so fair), why
     not a loop, the two fixes.
   - **`__main__` placeholder**; **shadowing** (from 12 Sep); **pip**.

4. **THEN act on the S42 decision:** the weekly cold build block on a REAL
   LeRobot file. Pick the file with him; he builds the `arm` front door
   (`arm/__init__.py` with `from .limits import MAX_ANGLE`) as the warm-up
   — still not built by him.

5. **THEN 1.11 File Handling.** Prerequisite gate: 1.10 seven [~]. Frame
   first. `pdb` and `os.path.expanduser` are parked into it.

6. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — `notes/session_21_notes.md`
   + `drills/s22_report.py`. Cold ask after. Not touched S44–S46.

7. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half of
   frames/REPL-vs-script (legal).

**Standing turn rules: VOLLEY FIRST; FRAME FIRST; physical-first, ROUTE
FIRST for anything import-shaped; ANSWER A DIRECT QUESTION DIRECTLY;
FILES BY PATH WITH CODE AND THE COMMAND, AFTER THEY EXIST; quoted lines
labelled read-not-run; NO `-c`; EVERY QUESTION CARRIES ITS FULL
SCENARIO; NEVER ASK FOR AN UNSEEN ERROR NAME; SPEC BEFORE PUZZLE; ONE
TEACHING IDEA PER TURN AND PER DEMO; asks near the top; doubt gate before
every new subsection; depth-before-answer (re-ask a skipped WHY); rating
AFTER his answer and BEFORE the verdict; tag every block. Do not propose
ending the session. WHEN HE SAYS STOP, WRITE THE CLOSE IN THAT TURN.
NEVER EDIT HIS DRILL FILE. NEVER OVERWRITE A FILE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **THE ROUTE RULE WAS GAPPED AT 42 HOURS.** He had `__init__.py`
  first and "the parent of `arm/`", then *"please remind me the whole
  thing."* Honest gap. What re-landed it: `ls -d <entry>/json
  <entry>/json.py` down the list, then `ls` inside the hit. **For the cold
  ask, put a real `sys.path` list in the question.**
- ⚠⚠ **"A FOLDER IS NOT CODE" is the sentence that made `__init__.py` make
  sense to him.** He had the label as "guess work" and not the reason.
  Lead with the sentence, then `see_arm.py`.
- ⚠ **HE FOUND THE KEY-ORDER CONTRADICTION HIMSELF** (insertion vs finish
  order). Answered with `teaching/s46_stdlib/key_order/`. New row. He
  applies the circular-import fact correctly; the mentor had given half.
- ⚠ **"Same folder first, then `sys.path`"** — corrected: the folder IS
  `sys.path[0]`. Watch on the shadowing / route cold asks.
- ⚠ **Bare `*`: right answer, WHY skipped, re-asked, then right.** Mild
  surface-answer instance. "By keyword" is the phrase.
- ⚠ **"Run a file" vs "import a file"** — corrected once.
- ⚠ **RELATIVE vs ABSOLUTE parked by him a SECOND time** (*"still
  hurting, lets not waste time on it yet"*). Honour it. Cold task only.
- ⚠ **`max()`/`min()` used undefined (mentor) — now defined and queued.**
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S46.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()`
  vs `+`. (`enumerate()` now defined.)
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — three instances; full treatment still parked.
- Governance/format requests mid-session → PARK, close material, write at
  end.
- **Mentor demos, re-runnable:** `teaching/s46_stdlib/` (`key_order/`,
  `star.py`, `enum.py`); `teaching/s46_pip/` (`where_third.py`,
  `shadow/json.py` + `shadow/main.py` — ⚠ `shadow/` deliberately holds a
  file named `json.py`; never run anything else from inside it);
  `teaching/s45_stdlib/`, `s45_circular/`, `s45_cache/`, `s43_packages/`.
- **Voice re-teach file:** `notes/voice_teach_packages_relative_imports.md`.
  Never confirmed used; not chased.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**149 rows, 99 [x], 50 [~].** Do not re-create the table here.
`python3 tools/retest.py --overdue --all` at the open.
**S46: 0 rows fired (third session running). 6 rows added, all [~] due
12 Sep: `enumerate()`; `keyword-only fence: bare *`; `shadowing / first
hit wins`; `pip / site-packages`; `sys.modules key moved to END on
finish`; `max() / min()`. Route row: asked 10 Sep, GAP, re-dated 12 Sep.
Stdlib row re-dated 12 Sep.**

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
| **`sys.path`** | S43 taught; S46 walked BY HAND with `ls` | **[~] — OVERDUE (7 Sep): "why does the import fail, two fixes"** |
| **PACKAGES** | S45 restated same-sitting; **S46: `__init__.py` label right as "guess", reason re-taught ("a folder is not code"), teach-back clean** | **[~] — cold ask now legal, task-first** |
| **RELATIVE vs ABSOLUTE IMPORTS** | S45 re-walked; **S46: parked by him a second time; the dot-resolves-by-NAME point taken from his own question** | **[~] — cold ask, both halves, legal now; NO re-teaching** |
| **CIRCULAR IMPORTS** | S45 taught; **S46 doubt gate: "clear"** | **[~] — cold ask legal now** |
| **STDLIB / FRONT DOOR** | **S46: RE-WALKED and FINISHED — route by hand, "a folder is not code", chain `decoder.py` → `scanner`, key order, `bisect_left` read** | **[~] — cold ask 12 Sep** |
| **PIP / SITE-PACKAGES / SHADOWING** | **S46 taught; teach-backs clean after one correction** | **[~] — cold ask 12 Sep** |
| **BARE `*` / `enumerate()`** | **S46 defined; teach-backs right after a re-ask** | **[~] — cold ask 12 Sep** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | S43 taught | **[~] — legal** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — cache row 10 Sep, legal** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x] — legal** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — OVERDUE** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S38 full trace | **[x] — OVERDUE; UBL deletion test due** |
| **THE MUTATING TELL** | S38 both halves | **[x] — OVERDUE** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | S42: PASS 8 / 8 / 7 | **[x] — `[[0]*3]*3` posed S46, unanswered; re-pose first** |
| **`constructors`** | S38 7/10 | **[x] — OVERDUE** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 `finally` guarantee** | S41: PASS 7 | **[x] — legal** |
| **`short-circuit`** | S41: PASS 7 | **[x] — legal** |
| **1.9 try/except** | S41 drill clean | **[x] — OVERDUE** |
| **RAISE-VS-SHRUG / `None` returns / expression-vs-statement** | S42: PASS 8 / 8 / 8 | **[x] — 17 Sep** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK still owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S41 DEMOTED | **[~] — OVERDUE** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; S43 REPL defined; S46 REPL re-shown | [~] **cold ask on both halves legal** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **DELIVERY, NOT RETENTION, WAS THE PROBLEM AGAIN (S43–S46).** S46:
  pushbacks 89 (abstract list), 90 (no frame), 91 (read-not-run), 93 (no
  command), 94 (close not written). Once a demo was a file run from a
  stated folder with its command shown, he restated everything. **Four
  sessions running. The watch is on the MENTOR.**
- ⚠⚠ **ZERO COLD ASKS FOR THREE SESSIONS.** The ledger has had no new
  evidence since S43. Every "[x] overdue" row is now two weeks stale. The
  volley is not optional at the S47 open.
- ⚠⚠ **HE NAMES HIS OWN LIMIT AND PARKS** — relative/absolute parked a
  second time (S46). *"I won't say clear... lets finish this unit
  today."* Honour it, cold task only.
- ⚠⚠ **HE ASKS THE GOOD QUESTION HIMSELF (S46):** the key-order
  contradiction; the dot-is-whose-folder question; *"what file did we
  run?"* Each one produced a demo or a correction of the mentor.
- ⚠ **HE NAMES A GAP INSTEAD OF GUESSING** (route rule, `json.scanner`)
  and TAGS a guess as a guess (`__init__.py`). Keep rewarding it; never
  log a named gap as anything but a gap.
- ⚠ **FORM-CONVERSION MISS (`from . import limits`)** — untouched S46 by
  his request. Cold task next.
- ⚠ **SURFACE ANSWER, mild (bare `*` why skipped).** Re-ask works.
- ⚠ **CONFIDENCE CALIBRATION:** no ratings taken S44–S46. Use ≤5 as the
  targeting signal; a 7+ on a LABEL is unreliable until three clean.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()`,
  `.append()` vs `+`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 94 raised, 92 upheld or
  part-upheld.** S46: 88 part, 89, 90, 91, 92, 93, 94 upheld.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`.pyc` — PAID S42.** ✅ **REPL — DEFINED S43, re-shown S46.**
  ✅ **`python3 -c` — DEFINED S44.** ✅ **bare `vars()` — S44.**
  ✅ **`__file__` — S45.** ✅ **`__init__.py` as a FRONT DOOR — S45 live,
  chain read S46; the `arm` version still not built by him (LeRobot
  warm-up).** ✅ **`sys.path.append` smell — SAID S46;** `pip install -e .`
  named, not shown. ✅ **`enumerate()` — DEFINED S46.** ✅ **bare `*` —
  DEFINED S46.** ✅ **shadowing — SHOWN S46.**
- ⚠ **Two module objects for one file** (`limits` AND `arm.limits` in one
  program) — stated S45 as a real bug class, not demonstrated.
- ⚠ **`..` (two dots, parent package)** — one line said S44, never shown.
- ⚠ **`python3 -m`** — never shown to him. Do not use in a demo until
  defined.
- ⚠ **`bisect.py` lines 111–114** (`try: from _bisect import *` — the C
  override) — not shown; `import *` untaught.
- ⚠ **`pip install -e .` / editable installs** — named S46, owed at the
  LeRobot block.
- ✅ **BREAKPOINT DEBUGGING / `pdb` — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 opens with the exception classes.
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
