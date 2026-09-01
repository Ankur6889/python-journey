# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 38 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule was adopted in S37**),
#      then this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** ✅ Held clean S36 and S37. In S37 it did real work: it
#      moved the gauntlet off the session in the first sixty seconds.
#   3. ⚠⚠ **S38 IS THE AUGUST GAUNTLET, DEFERRED FROM S37 BY THE INTERVAL
#      GATE — RUN IT ONLY IF THE GAP IS A REAL DAY.** Load ARCHIVE.md AND
#      master/robotics_career_curriculum.md at the open (gauntlet exception).
#      Pure mixed recall, NO NEW MATERIAL. Strict-legend audit + re-baseline.
#   4. ⚠⚠ **BEFORE ANYTHING ELSE: THE WORKING TREE IS RED. FIX IT FIRST.**
#      `builds/block_02_episode_validator/validator.py` has three `try:` with
#      no `except` (lines 16, 22, 32). ZERO tests collect. He broke it in a
#      cleanup at 05:29 and **ruled at 05:35 to close with it broken** —
#      "close it, let those remain there". His call, recorded, not a lapse.
#      **The block's real result is 27/27 and it was verified in session at
#      ~05:22 — but that green state was never committed and cannot be
#      re-created from git.** Ask him to close the three blocks (either put
#      the `except TypeError:` back or delete the `try:` and de-indent), then
#      re-run and commit the green.
#   5. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule at the open.
#   6. ⚠ **THE QUEUE IS A SCRIPT. USE IT.** `python3 tools/retest.py`.
#   7. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held clean S35–S37.
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held clean S37
#      and it paid: at 05:31 the tree was red, mtime said 05:29, so it was a
#      SAVED broken file and not an unsaved buffer. Report the right thing.
#
# STATE AS OF: end of Session 37, **Tue 1 Sep 2026, ~05:35** (verified).
# Next: Session 38 — **THE AUGUST GAUNTLET.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S37 yield: COLD BUILD BLOCK 02 RUN AND PASSED — 27/27, ONE bug, in the
  function he predicted. FIRST DURATION EVER RECORDED (2h 55m). FIRST `LOG.md`
  EVER WRITTEN (3 of 5 items). ZERO curriculum movement, correctly — the whole
  session was same-sitting. ONE LEDGER DEMOTION (`short-circuit`).**
- **Position: unchanged. 1.1–1.7 closed. 1.8 — TWO bullets still [~].
  1.9 — one bullet [x], six [~], one [ ]. Nothing moved in S37.**
- **1.8 — what remains, unchanged since S35:**
  - `dict` — **`.keys()` as a VIEW taught S35, still never asked cold.** ONE
    cold ask closes this bullet. **STILL the cheapest tick on the board.**
  - `list` — HELD [~]. The returns-`None` tell broke live in S34.
  - `when to use which` — still never asked cold.
- **1.9 — what remains:** `[x]` try/except. `[~]` specific-vs-bare, else/finally,
  raise, custom exceptions, hierarchy+ordering, control-flow, defensive
  programming. `[ ]` **Common built-in exceptions** — still the only untouched
  bullet, with heavy pre-loaded S26/S27 material to TEST rather than teach.
- ✅ **BUILD BLOCK 01 CLOSED. BUILD BLOCK 02 RUN AND PASSED (S37).**
- **AFTER THE GAUNTLET: 1.10 modules and imports.** The hook is still live —
  `import` appeared in an S36 test file, he flagged correctly that it had never
  been taught (pushback 63), and got the one-line minimum only.
- Current Layer: 1. Current Topic: **1.9 closing / 1.10 next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING WAS ADOPTED IN S37 AND NOTHING IS PARKED FOR S38.** Do not invent
  a candidate. RULES stays at **v6**.
- **RULES v6 (THE DONE LINE) — THIRD DATA POINT, AND IT WAS THE GOOD ONE.**
  He said *"function with least clarity is L4, because I didn't have a clear
  picture in mind"*. **Both failures were in L4.** It is still the
  function-half rather than the case-half — he named WHICH function, not WHICH
  CASE — but the reason he gave (no clear model) was accurate and predictive.
  **Keep asking for the case. Do not treat this as fully discharged.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 38 STARTS HERE — exact resume point

**S38 IS THE GAUNTLET, if and only if a real day has passed.** Load ARCHIVE.md
and the master. Run in this order:

1. **INTERVAL GATE from `git log` + mtimes.** Then **FIX THE RED TREE** (header
   item 4) — it is five minutes and the block cannot be filed until it is green.
   Then the **term-tax** (valid at a real gap; it was correctly skipped in S37).

2. ⚠⚠ **THE THREE THINGS THE GAUNTLET MUST SETTLE, IN THIS ORDER:**
   **(a) THE STRICT-LEGEND AUDIT of every [x]** — the bundled S16 promotions;
   the 1.6 spoken Feynman recall; the S22 short-gap promotions; the eight S23;
   the eleven S25; the eight S27; the S29 `zip`; the eight S30; the four S31;
   the four S32; the seven S33; the two S34 (**plus the `.count()` echo caveat
   on the tuple tick**); the one S35; the one S36 (`try`/`except`).
   **(b) THE 1-SEP RE-BASELINE ARITHMETIC, IN ITEMS**, against 30 Sep.
   **(c) THE OVERDUE COLD ASKS BELOW.** The queue reports **38 overdue**.
   ⚠ **(d) THE AUDIT HAS A CONCRETE STARTING LEAD: `queue.json` AND
   `CURRICULUM.md` DISAGREED ON `short-circuit`** — the queue carried it `[x]`
   due 9 Sep while CURRICULUM.md line 152 has said `[~]` since S13. The S37
   miss settled it downward and both now read `[~]`, but **the two files
   drifting apart unnoticed is exactly what the strict-legend audit is for.
   Diff the queue against CURRICULUM row by row.**

3. ⚠⚠ **THE COMPILE/RUN SPLIT — ASKED TWICE IN S37, NOT ANSWERED EITHER TIME.
   THIRD TIME OF ASKING AND IT IS NOW THE OLDEST UNPAID ASK IN THE FILE AFTER
   `while`.** It was fired cold and clean off his own broken file ("no tests
   ran — how far did Python get?"). **He answered the CAUSE instead** — *"I
   deleted the except block without deleting try"* — which is correct and is
   NOT the question. Re-asked in one line; he moved to the gauntlet question
   and it lapsed. **This is depth-before-answer, part (a): a correct diagnosis
   does not discharge a traced mechanism. Fire it cold, standalone, at the top
   of the gauntlet, with nothing about syntax in the preceding three turns.**
   Shape that works: *"a 40-line file, lines 1–39 perfect, line 40 missing a
   colon — how much executes?"*

4. ⚠⚠ **THE TRANSFER GAP — FIRST POSITIVE RESULT IN FOUR SESSIONS, AND IT WAS
   MEASURED THE ONLY WAY THAT COUNTS: IN A FILE.** S36 recorded that he passed
   the catch-all recalls and then shipped a catch-all in fresh code the same
   evening. **S37 reran that exact experiment at the same interval** — material
   taught 31 Aug ~23:50, `validator.py` written 02:17–05:12 on 1 Sep, cold,
   unsupervised, three hours. **Result: `except TypeError:` ×3 and
   `except UnidentifiedEpisode:` ×1. Bare `except:` / `except Exception:` — ZERO,
   in 81 lines.** ⚠ **DO NOT PROMOTE ANYTHING ON THIS. Same sitting.** What it
   earns is a re-run at a real gap, and that is the single most valuable thing
   the gauntlet can do.

5. ⚠ **`short-circuit` DEMOTED [x] → [~], DUE 2 SEP. Cold miss, S13 material,
   24-day gap, and he conceded it himself: *"yes I have forgotten short
   circuiting"*.** Given `x = "90"`, he said `type(x) != int or x < 0` **raises
   `TypeError`**. It prints `True`. **His code was CORRECT and his model of why
   was wrong** — the `or` guard is textbook-safe, and S13's own note says
   *"short-circuiting is what makes a guard expression safe"*. He built one by
   accident and then defended it against an impossible failure.
   **CONSEQUENCE STILL LIVE IN HIS FILE: three `except TypeError:` blocks that
   can never run.** He spotted the same thing unaided on the `fps` branch —
   *"I believe no need of checking exception for this"* — and was right there.
   **Same structure, opposite conclusion, in one function.** Re-ask 2 Sep.

6. ⚠ **`StopIteration` — STILL DUE, NOT FIRED IN S37. Re-ask the LABEL ALONE.**
   Mechanism intact after three weeks; the label came back as "EndofIteration".

7. ⚠ **`SyntaxError` — filed as a DETECTION MISS UNDER A BAD FRAME, not a
   knowledge gap.** Ask it as *"what happens when you run this?"*, never as a
   yes/no about one line. ⚠ **S37 gave a live instance and it went unharvested**
   (see item 3) — his own file, a real `SyntaxError`, and he named the cause
   correctly and instantly. That is evidence the DETECTION works; the
   compile/run half is what is still unmeasured.

8. ⚠ **STILL OWED, NOT FIRED IN S37 — this list has not shortened in two
   sessions:** the mutating tell's **return-value half alone**; `del` as a
   STATEMENT; `.clear()` → `None`; **`while` mechanics, now ELEVEN sessions
   overdue and the oldest debt in the file**; hashability; `subscriptable`;
   unpacking count-mismatch ⇒ `ValueError`; `zip` fails silently twice;
   **`constructors` as his FIRST word (one question from [x], re-ask cold and
   UN-TAGGED)**; `when to use which`; **`.keys()` as a view**;
   `UnboundLocalError`, `print()`, `abs()` (never asked).

**Standing turn rules: FRAME FIRST — and S37 breached it on L4, see pushback 69;
CONSOLIDATED QUESTIONS CARRY THEIR OWN RUNNABLE CODE; SPEC BEFORE PUZZLE with
boundaries in the TESTS; short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection; depth-before-answer — BREACHED
BY OMISSION IN S37, see item 3; NAME THE ERROR BEFORE THE MENTOR SHOWS IT; take
the rating AFTER his answer and GIVE THE VERDICT immediately after; tag every
block and CHECK THE TAG. Do not propose ending the session. DO NOT MISQUOTE HIS
OWN CODE BACK AT HIM.**

**CARRY FORWARD:**
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said. One line,
  when comprehensions next come up. **He used a comprehension well in S37**
  (`[f for f in record_struct if f not in record.keys()]`), so the hook is warm.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Still not asked.
- ✅ **THE S35 STYLE NOTE HELD WITHOUT BEING REPEATED:** nothing in his 81-line
  `validator.py` prints. Do not deliver the note again.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
121 rows, **66 [x], 55 [~]**, 38 overdue, 12 never asked.
**Do not re-create the table here.** `python3 tools/retest.py` at the open.
S37 recorded: `short-circuit` **fail → DEMOTED [~], due 2 Sep** (rated 6 before
the verdict). One rating taken all session; the block itself is not queue work.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | **S37: ZERO catch-alls in 81 lines of cold fresh code, same interval as the S36 failure** | **[~] — RE-RUN AT A REAL GAP. Highest-value ask on the board.** |
| **THE COMPILE/RUN SPLIT** | **S37: asked twice, answered neither time — he gave the CAUSE instead** | **[~] — COLD, STANDALONE, S38. Third asking.** |
| **`short-circuit` in `and`/`or`** | **S37: cold MISS at 6/10, conceded** | **[~] DEMOTED — due 2 Sep** |
| **1.9 try/except** | S36: promoted on two cold later-day recalls | **[x] — re-test ~5 Sep** |
| **1.9 custom exceptions / hierarchy / re-raise** | **S37: `UnidentifiedEpisode` + a correct bare `raise` written cold in a build block, but SAME SITTING** | **[~] — cold later-day ask, S38** |
| **DRY / one copy of a decision** | **S37: `fps_defaults` defined once; `validate_all` asks `faults` rather than re-checking the id. Held structurally, unprompted** | **[~] — later-day ask** |
| **`sorted` / `key=`** | **S37: `sort(key=record_struct.index)` reused unprompted, 14 sessions after S23** | **[x] CANDIDATE — confirm cold** |
| **`StopIteration`** | S36: mechanism intact 3 weeks, label = "EndofIteration" | **[~] — label alone, OVERDUE** |
| **NESTED STRUCTURES + SHALLOW/DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| **⚠ THE MUTATING TELL** | S34: TYPE and MUTATES intact, RETURN-VALUE half gone | **[~] — the return-value half ALONE** |
| **`reversed()`** | S35 taught as a pair in one table | **[~] — cold ask OVERDUE** |
| **`while` mechanics; nested loops; found-flag** | NOT tested S27–S37 | **[~] ⚠ ELEVEN sessions overdue — OLDEST DEBT** |
| Frames / namespace / execution pipeline / REPL vs script | S14, never re-run | [~] **overdue badly** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| **CONTAINERS AS CODE** | S30 19/19; S32 17/17; S34 36/36; **S37 build block 27/27** | **[x] — closed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE TRANSFER GAP — FIRST GREEN LIGHT, AND IT MUST NOT BE OVER-READ.**
  S33: *change where the ask sits.* S34: *an ask that can be satisfied without
  executing anything will be.* S35: *a fact he can PREDICT is not yet a fact he
  will APPLY.* S36: *he takes the last lesson and drops the one before it.*
  **S37: at the identical interval that produced the S36 failure, the idea
  showed up in the file.** One data point, same-sitting, not a promotion.
  **The test for a taught idea is still his next FILE, never his next answer.**
- ⚠⚠ **RIGHT CODE, WRONG MODEL — THE PATTERN GOT ITS CLEANEST INSTANCE YET.**
  The short-circuit guard is correct and his account of why is wrong. This is
  the same shape as right-answer-without-mechanism, and it is now the reason to
  keep asking *why does this work* on code that already passes. **Green tests
  are not evidence of a model.**
- ⚠⚠ **AN ARTEFACT THAT FAILS TWICE IS THE ARTEFACT'S PROBLEM — TWO MORE WINS.**
  **`LOG.md` was written for the first time in seven askings** once cut to five
  fill-in lines, and **the timer became two git commits** and immediately
  produced a duration after block 01's stopwatch was abandoned. **Keep
  converting asks into artefacts with no discipline cost.**
- ⚠⚠ **HE CANNOT START FROM A SPEC HE HAS NOT INTERROGATED, AND THIS IS A
  STRENGTH BEING MIS-READ AS A WEAKNESS.** He asked **seven** spec questions
  across ~2 hours before writing a line, and twice asked whether the problem was
  him (*"is that my problem or the language"*, *"am I bad at reading??"*).
  **Three of the seven were holes in the mentor's brief and one found a case
  the TESTS did not cover.** He also said mid-block *"I feel like I am slow in
  building logic"* — against 35/35, 29/29, 25/25 and 27/27. ⚠ **He under-rates
  both his reading and his speed. Answer that with evidence from his own
  record, never with reassurance** — it worked twice in S37.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE — CONFIRMED TWICE
  IN S37.** Given the raw assertion and "find it", he fixed the L4 tuple bug
  unaided. Given a red collection with no output shown, he named the cause
  instantly from memory of what he had just edited.
- ⚠ **CONFIDENCE CALIBRATION: one rating in S37 (6, on a miss).** Honest doubt
  on a wrong answer. **The standing over-rating exception — "did anything run
  before the error" — did NOT repeat.**
- ⚠ **HE ASKS FOR THE TOOL BEFORE IT IS TAUGHT, BY SHAPE — THIRD SESSION
  RUNNING.** S37: he derived the need for an outside caller off the spec alone —
  *"is there an outside function that will call validate all and handle those
  exceptions?"* — which is the exact frame for **catching is not handling**.
  **Give him the tool when he names its shape.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 69 raised, 68 upheld or
  part-upheld.** S37 raised FIVE (65–69), **all upheld in whole or part, and
  all five about the mentor's SPEC rather than his teaching** — L3 written
  argument-first (65); classes not taught (66); "message" never defined (67);
  **the mixed missing/wrong case covered by neither the brief nor the tests
  (68 — a test was added, 26 → 27, and disclosed to him)**; and FRAME FIRST
  breached on L4 (69, part-upheld — his implied counter, that the caller could
  write the try/except itself, is correct at this size). **Full write-ups in
  ARCHIVE.md, S37 block.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35)**;
  GIL (1.13); concurrency (post-Layer 1); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **`class` — STILL ON CREDIT, AND THE DEBT GREW.** He has now written FOUR
  one-line exception classes (`OverLimit`, `UnknownJointError`,
  `UnidentifiedEpisode`) and asked directly in S37 whether it is "just a class
  definition". **1.11 owes him the real unit and he has four concrete hooks.**
- ⚠ **`except Exception:` vs bare `except:`** — the real difference is still a
  parked footnote. One line, in 1.11 or 1.13.
- ⚠ **`raise ... from` / exception chaining, `sys.exc_info()`, the `traceback`
  module** — parked from 1.9.
- ⚠ **DEAD CODE as a concept** — new S37 hook. He has three unreachable
  `except` blocks in his own file and now knows why. One line when it comes up.
- ⚠ **PEP 709 / how comprehension scope is actually implemented** — Level 3, 1.13.
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
