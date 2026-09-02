# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 40 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule was adopted in S39**),
#      then this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** ✅ Held clean S36, S37, S38, S39. In S39 it ran in the
#      first minute and killed the gauntlet before a word was taught.
#   3. ⚠⚠ **S40 IS THE AUGUST GAUNTLET, NOW DEFERRED THREE TIMES (S37, S38,
#      S39).** The first two were the gate's call; **the third was HIS** — he
#      opened S39 with *"the next block instead of gauntlet, we will do the
#      gauntlet tomorrow"*, and the gate independently agreed (3-minute gap).
#      **If the gap to S40 is a real day, RUN IT.** Load ARCHIVE.md AND
#      master/robotics_career_curriculum.md at the open (gauntlet exception).
#      Pure mixed recall, NO NEW MATERIAL. Strict-legend audit + re-baseline.
#   4. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** Earned in S38 (this file carried a false RED-tree alarm; HEAD was
#      green). **This file can be wrong; the repo cannot.** Applied in S39 —
#      `git status` was checked clean at the open before anything else.
#   5. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule at the open.
#      **TWO NON-RULE DECISIONS ARE OWED BY HIM — see items 2 and 3 below.**
#   6. ⚠ **THE QUEUE IS A SCRIPT. USE IT.** `python3 tools/retest.py`.
#      **128 rows now — seven 1.10 rows were added at the S39 close and are
#      due 3 Sep. They are the cheapest evidence on the board tomorrow.**
#   7. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held S35–S39.
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S39.
#
# STATE AS OF: end of Session 39, **Wed 2 Sep 2026, ~18:55** (verified).
# Next: Session 40 — **THE AUGUST GAUNTLET, if a real day has passed.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S39 yield: 1.10 OPENED — the first new curriculum unit since S36.** Five
  master bullets moved `[ ] → [~]` (what a module is; `import`; `from x import
  y`; `import as`; `__name__ == "__main__"`), plus one bullet ADDED at his
  request (the module namespace as a real dict). **All five are `[~]` and
  cannot be more — the session opened 3 minutes after S38 closed.**
- ⚠⚠ **THE COST OF THE SESSION, STATED PLAINLY: OVERDUE WENT 25 → 40.** S39
  fired ZERO ledger-eligible asks, correctly (a 3-minute gap makes recall
  meaningless), but the queue does not care about the reason. **A pure-teaching
  session costs ~15 overdue rows per day. Two in a row would undo S38.**
- **Position: 1.1–1.7 closed. 1.8 — TWO bullets still [~] (`dict`, `when to
  use which`). 1.9 — one [x], seven [~], ZERO [ ]. 1.10 — OPEN, ~40%.**
- **REMAINING IN 1.10:** packages (the `lerobot.common.datasets...` shape),
  `sys.path`, circular imports, the standard library, pip, relative vs
  absolute imports, and **the `.pyc`/bytecode answer owed since S35.**
- Current Layer: 1. Current Topic: **1.10, open and half-done.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING WAS ADOPTED IN S39 AND NOTHING IS PARKED FOR S40.** Do not invent
  a candidate. RULES stays at **v6**.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 40 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** Then the **term-tax** (valid at a
   real gap — it has not run since S36). Then **THE GAUNTLET**.

2. ⚠⚠ **DECISION OWED BY HIM #1 — PROMISED TO HIM AT THE S39 CLOSE, SO ASK IT.**
   He asked mid-session where **debugging with breakpoints** is covered. He was
   given the arithmetic, not reassurance: it is one of the four things RULES.md
   says Layer 0 must deliver; **there is NO bullet for it anywhere in 1.1–1.13
   (grepped, not remembered)**; the traceback half has been drilled hard (S15
   definition, the S27 name-the-error rule); **the half he is missing is the
   no-traceback case, which is his oldest recorded weakness** (*he debugs well
   with a traceback and poorly without one*). `pdb` is a MODULE and VS Code's
   debugger is a front end on it, so **it is gated on 1.10, the unit he was
   sitting in when he asked — fifth session running of him naming a tool by
   its shape one unit before it arrives.** Cost quoted to him: 45–60 min, most
   of it cheap Level-1, with one load-bearing piece (**VS Code's Call Stack
   panel is the frame stack he traced unaided in S38**).
   **THE OPTION PUT TO HIM: bolt a debugger block onto the tail of 1.10, or
   leave it to 1.11 where file handling gives it more to chew on. TAKE HIS
   RULING AT THE S40 OPEN.**

3. ⚠⚠ **DECISION OWED BY HIM #2 — CARRIED UNRESOLVED FROM S38, NOT ASKED IN
   S39.** Once 1.10 lands, point the weekly cold build block at a REAL LeRobot
   file instead of a synthetic task — same instrument, real substrate. **This
   is now nearly due: 1.10 is the unit in progress, and S39 gave him the honest
   frame for it** (*the import block at the top of a file is its dependency
   list; read the imports and you know what the file is about before you read
   a line of logic*). Explicitly NOT a rule. Take his ruling.

4. ⚠⚠ **THE SEVEN NEW 1.10 QUEUE ROWS ARE DUE 3 SEP AND ARE THE CHEAPEST
   EVIDENCE ON THE BOARD.** All taught same-sitting, none testable until a real
   gap. **Ask them cold and as INSTANCES, not as definitions** — this student's
   failure mode is the label, never the machinery. **The one to ask first:
   `import RUNS the file`. He dropped the module-level `print` line from his
   predicted output TWICE, confirmed it was forgetting rather than a channel
   artefact, and can state the mechanism correctly on demand.**

5. ⚠⚠ **`.keys()` IS A VIEW — STILL NOT HELD, STILL NOT ASKED. Owed since S38
   and now a day older.** Ask it as an INSTANCE: *"which of these three are
   live and which are frozen — `d.keys()`, `list(d.keys())`, `zip(a,b)`?"*
   **Still the cheapest tick on the board: ONE cold ask closes the 1.8 `dict`
   bullet.** He owns the lazy-vs-snapshot pattern and fails to index into it.

6. ⚠ **`short-circuit` — WAS DUE 2 SEP, NOT ASKED IN S38 OR S39.** Given
   `x = "90"`, he said `type(x) != int or x < 0` raises `TypeError`. It prints
   `True`. **Right code, wrong model.** Re-ask cold.

7. ⚠ **THE TRANSFER GAP — NO NEW FILE EVIDENCE IN S38 OR S39 AND NONE WAS
   POSSIBLE.** The S37 result (zero catch-alls in 81 lines of cold fresh code)
   **still needs its re-run at a real gap. Highest-value ask on the board.**

8. ⚠ **STILL OWED, NOT FIRED IN S38 OR S39:** `StopIteration` (**label alone** —
   mechanism intact three weeks, label came back as "EndofIteration");
   `UnboundLocalError`; `print()`; **`abs()` — used in his S38 drill and still
   never defined**; `when to use which` (1.8, never asked, 15+ days);
   `comprehension scope`; `* on a sequence`; `None`-as-absence; DRY;
   `mutate-while-iterating`; `list method roster`; `AttributeError`;
   `HOW FAR DID PYTHON GET?`; `_ as a name`.

**Standing turn rules: FRAME FIRST — **HELD IN S39 and he said so** (*"the
frame lands, and is good"*); CONSOLIDATED QUESTIONS CARRY THEIR OWN RUNNABLE
CODE — **BREACHED TWICE IN S39, pushbacks 71 and 73**; SPEC BEFORE PUZZLE with
boundaries in the TESTS; short messages, one teaching idea per turn, asks near
the top; doubt gate before every new subsection — **HELD, four times**;
depth-before-answer; NAME THE ERROR BEFORE THE MENTOR SHOWS IT — **HELD, and
he named `NameError` cold with the right mechanism**; take the rating AFTER his
answer and BEFORE the verdict; tag every block and CHECK THE TAG. Do not
propose ending the session. DO NOT MISQUOTE HIS OWN CODE.**

**CARRY FORWARD:**
- ⚠⚠ **NEW, AND IT IS THE MENTOR DEFECT OF S39: DO NOT CREATE NUMBERED FILE
  VARIANTS MID-BLOCK.** `sensors.py`/`app.py` were duplicated as
  `sensors2.py`/`app2.py` to make a second point, and the follow-up question
  then named the UN-numbered file. He got frustrated and was right to.
  **RULE OF THUMB: two files, fixed names, both shown in full, every time. If
  a demo needs different content, CHANGE the file — do not fork it.**
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Still not asked.
- ⚠ **DEAD CODE** — full treatment still parked. The harmful instance (three
  unreachable `except TypeError:` blocks) is still in
  `builds/block_02_episode_validator/validator.py` by his explicit ruling.
- Governance/format requests mid-session → PARK, close material, write at end.
  **S39 note: he raised the debugging question mid-material and it was answered
  in-line rather than parked. That was the right call — it was two lines of
  arithmetic and it fed straight into the unit — but the RULING was parked.**
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.
- **`teaching/s39_imports/` holds every demo file from S39.** Mentor-written,
  not his work, not evidence. Re-runnable if he wants the outputs again.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**128 rows, 77 [x], 51 [~], 40 overdue, 8 never asked.**
**Do not re-create the table here.** `python3 tools/retest.py` at the open.
S39 recorded ZERO passes and ZERO fails — nothing was ledger-eligible.
**Seven new rows added at the S39 close, all `[~]`, all due 3 Sep:**
`import RUNS the file`; `import binds ONE name`; `the import cache /
sys.modules`; `a module IS an object, its namespace IS a dict`; `vars()`;
`subscription vs attribute access`; `__name__ and __main__`.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S37: ZERO catch-alls in 81 lines of cold fresh code | **[~] — RE-RUN AT A REAL GAP. Highest-value ask on the board.** |
| **⚠⚠ `.keys()` AS A VIEW** | S38: MISS — he owns the lazy/snapshot pattern he failed to apply | **[~] — ask as an INSTANCE, S40. Cheapest tick on the board.** |
| **⚠ 1.10 — THE WHOLE UNIT** | **S39: taught, same sitting, seven queue rows opened** | **[~] — ALL of it cold on 3 Sep. Nothing here is evidence yet.** |
| **THE COMPILE/RUN SPLIT** | S38: PASS cold, full mechanism, 7/10 — third asking | **[x] — re-test 6 Sep** |
| **`while` mechanics; nested loops; found-flag** | S38: 20/20 COLD, `drills/s38_while.py`, 7/10 | **[x] — re-test 6 Sep** |
| **Frames / namespaces / execution pipeline** | S38: full unaided trace, 7/10 | **[x] — re-test 6 Sep. ⚠ S39 leaned on this hard and it held: the module namespace was taught BY CONTRAST with the frame (same idea, different lifetime) and he followed it without a re-explanation.** |
| **⚠ THE MUTATING TELL** | S38: BOTH halves, applied to an UNSEEN method (`extend`) | **[x] — re-test 6 Sep** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38: one correct line cold, 13 days on, 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S38: truncation AND exhaustion, cold, lazy model in his own words | **[x] — 3 Sep** |
| **`constructors`** | S38: "constructor" as his FIRST word, un-tagged ask, 7/10 | **[x] — 6 Sep** |
| **`del` as a STATEMENT** | S38: GAP declared, then taught; sharp teach-back | **[~] — cold ask, OVERDUE** |
| **1.9 custom exceptions / hierarchy / re-raise** | S37: written cold in a build block, SAME SITTING | **[~] — cold later-day ask, S40** |
| **`short-circuit` in `and`/`or`** | S37: cold MISS at 6/10, conceded | **[~] — OVERDUE** |
| **1.9 try/except** | S36: promoted on two cold later-day recalls | **[x] — re-test ~5 Sep** |
| **`StopIteration`** | S36: mechanism intact 3 weeks, label = "EndofIteration" | **[~] — label alone, OVERDUE** |
| **DRY / one copy of a decision** | S37: held structurally, unprompted | **[~] — later-day ask, OVERDUE** |
| **NESTED STRUCTURES + SHALLOW/DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| Frames / REPL vs script | S38 covered frames; REPL-vs-script NOT re-run | [~] **the REPL half is still overdue** |
| **CONTAINERS AS CODE** | S30 19/19; S32 17/17; S34 36/36; S37 27/27; S38 20/20 | **[x] — closed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **NEW IN S39, AND IT IS THE SESSION'S REAL FINDING: HE REFUSED TO GUESS
  TWICE, BOTH TIMES NAMING THE EXACT UNDETERMINED FORK.** On `from robot import
  clamp`: *"will it run the entire file, or will it just import the function,
  so I am not answering."* On the aliasing snippet: he located the gap in the
  CACHE rule — *"this file has already been run, so what will happen now I am
  not sure."* **Both refusals were correct: nothing he had been shown decided
  either question, and the second one found a real hole in the mentor's own
  compression of the cache rule.** This is the exact inverse of the
  depth-before-answer failure the file has logged for twenty sessions.
  **DO NOT PUSH THROUGH A REFUSAL LIKE THIS. Teach the missing half, then
  re-ask — which is what was done, and he then answered correctly.**
- ⚠⚠ **AN ANSWER HE MEANT BUT DID NOT WRITE IS, TO ANY EXAMINER, AN ANSWER HE
  DID NOT HAVE.** He omitted the module-level `print` line from his predicted
  terminal output TWICE. The channel was checked first (the second ask's
  wording was genuinely ambiguous) and he answered honestly: *"actually I
  forgot to write that line, I am clear conceptually."* **Nothing logged in the
  ledger — [PREDICT] never is — but note WHICH line he drops: the side effect
  of an import, which is exactly the invisible thing that bites in real
  codebases because nobody wrote a call for it.**
- ⚠⚠ **HE TESTED A MENTOR CLAIM IN JUPYTER AND DISPROVED IT.** Told *"the dot is
  sugar over a dict access"*, he went and tried `d.key`, found it failed, and
  came back with it. **Pushback 72, upheld — the claim is true for a MODULE and
  false in general.** This is the behaviour the entire course exists to
  produce. It is also the second technical (not process) pushback on his record.
- ⚠⚠ **THE TRANSFER GAP: A MISSING INDEX, NOT A MISSING FACT.** S33: *change
  where the ask sits.* S34: *an ask satisfiable without executing anything will
  be.* S35: *a fact he can PREDICT is not a fact he will APPLY.* S36: *he takes
  the last lesson and drops the one before.* S37: *the idea showed up in the
  file.* S38: *he applied lazy-vs-snapshot twice and failed the third instance
  because it was labelled `.keys()`.* **S39: he produced `if __name__ ==
  "__main__":` unprompted and then put the guard in the WRONG FILE** — he had
  the construct and not the direction (it protects the file being IMPORTED).
- ⚠⚠ **EVERY MISS IN S38 EXCEPT ONE WAS A LABEL SITTING ON AN INTACT
  MECHANISM.** Still the most replicated finding in the file.
- ⚠⚠ **RIGHT CODE, WRONG MODEL / GREEN TESTS ARE NOT EVIDENCE OF A MODEL.**
  Unchanged. Keep asking *why does this work* on code that already passes.
- ⚠ **CONFIDENCE CALIBRATION.** No ratings taken in S39 — correctly, nothing
  was ledger-eligible. ⚠ **STILL UNRESOLVED from S38:** he answered "7" after
  the `.keys()` miss and it was never established whether that was a rating.
  Ask him.
- ⚠ **HE ASKS THE RIGHT GOVERNANCE QUESTION AT THE RIGHT TIME — THIRD SESSION
  RUNNING.** S38: the ledger audit, then the codebase-reading question. **S39:
  the debugging question, raised at the exact moment `pdb` became reachable.**
  All three got tables with arithmetic, not reassurance. Keep answering that way.
- ⚠ **HE ASKS FOR THE TOOL BEFORE IT IS TAUGHT, BY SHAPE — FIFTH SESSION
  RUNNING.** S39 twice: the module namespace (*"when are we going to discuss
  the namespace of a file and what is in it? because I believe this question
  opens the door for that"* — it did, exactly) and the debugger.
  **Give him the tool when he names its shape.**
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged, and
  now with a candidate remedy on the table (item 2 above).
- ⚠ **HE UNDER-RATES HIS RETENTION, HONESTLY AND USEFULLY.** S39: *"I read
  everything mostly clear, but I won't say I remember everything now."*
  **That is the correct report and the system assumes it.** Answer self-doubt
  with his own record and with the design, never with reassurance.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 73 raised, 72 upheld or
  part-upheld.** **S39 raised THREE and all three were UPHELD IN FULL:**
  **(71)** *"please write whatever files are needed together, it is difficult
  to scroll up and down"* — the S19 consolidated-code rule, breached;
  **(72)** the dot-on-a-dict claim, disproved by his own experiment;
  **(73)** *"I am getting frustrated because you have already made multiple
  versions of the file and what you want is not clear"* — **the same defect as
  71, from the same mentor, inside one session.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35, STILL
  OWED, and 1.10 is now open so it is due inside this unit)**;
  GIL (1.13); concurrency (post-Layer 1); GC (1.13)
- ⚠ **BREAKPOINT DEBUGGING / `pdb` / the VS Code debugger — RAISED BY HIM S39.
  No bullet exists for it anywhere in 1.1–1.13. Ruling owed (item 2).**
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **`class` — STILL ON CREDIT.** Four one-line exception classes written;
  1.12 owes him the real unit; **the most load-bearing park in the file.**
- ⚠ **`except Exception:` vs bare `except:`** — still a parked footnote.
- ⚠ **`raise ... from` / chaining, `sys.exc_info()`, `traceback` module** — 1.9.
- ⚠ **DEAD CODE as a concept** — taught in passing S38; full treatment parked.
- ⚠ **EXPRESSION vs STATEMENT** — reinforced S38 on `del` vs `.pop()`.
- ⚠ **`__dict__` as a general object feature, and why a `dict` has none** —
  touched in S39 via `vars({})` raising `TypeError`. Level 3 / 1.12–1.13.
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
