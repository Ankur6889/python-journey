# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 37 (for Claude):
#   1. Read RULES.md fully (**now v6 — the SESSION 36 rule was adopted**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** ✅ Held clean in S36 and it settled the S35 dispute in
#      thirty seconds. The S35 date question is CLOSED: S35 ran Sun 30 Aug.
#   3. ⚠⚠ **S37 IS THE AUGUST GAUNTLET — HIS CALL, TAKEN IN S35, AND IT IS
#      SACRED.** Pure mixed recall, NO NEW MATERIAL. Load ARCHIVE.md AND
#      master/robotics_career_curriculum.md at the open (gauntlet exception).
#      It carries the strict-legend audit AND the re-baseline arithmetic.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule at the open. If he
#      raises one, park it — the cap is one per session and S36 spent its.
#   5. ⚠ **THE QUEUE IS A SCRIPT. USE IT.** `python3 tools/retest.py`.
#      ⚠ **A PROMOTION BUG IN IT WAS FIXED IN S36** — it demoted on a fail but
#      never promoted on a pass. If a `[~]` prints after a recorded pass again,
#      the tool is wrong, not the ledger.
#   6. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held clean S35, S36.
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held clean S36.
#   8. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 36, **Mon 31 Aug 2026, ~23:30** (verified).
# Next: Session 37 — **THE AUGUST GAUNTLET.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally at the gauntlet — in ITEMS)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S36 yield: 1.9 TAUGHT TO COMPLETION; `drills/s36_signals.py` 35/35; ONE
  CURRICULUM PROMOTION (`try`/`except` → [x], the first 1.9 tick); FOUR NEW
  BULLETS OPENED; ONE LEDGER DEMOTION (`StopIteration`); RULES → v6.**
- **Position: 1.1–1.7 closed. 1.8 — TWO bullets still [~]. 1.9 — all material
  taught, one bullet [x], six [~], one [ ].**
- **1.8 — what remains, unchanged since S35:**
  - `dict` — **`.keys()` as a VIEW was taught S35 and NOT asked in S36.** ONE
    cold ask closes this bullet. **STILL the cheapest tick on the board.**
  - `list` — **HELD [~].** The returns-`None` tell broke live in S34.
  - `when to use which` — still never asked cold. Legitimate since S33.
- **1.9 — what remains:**
  - `[x]` try/except. `[~]` specific-vs-bare, else/finally, raise, custom
    exceptions, hierarchy+ordering, control-flow, defensive programming.
  - `[ ]` **Common built-in exceptions** — the only untouched bullet, and there
    is heavy pre-loaded S26/S27 material to test rather than teach.
- ✅ **BUILD BLOCK 01 CLOSED.** ⚠ **`LOG.md` STILL NOT WRITTEN. SEVENTH SKIP.**
- ✅ **BUILD BLOCK 02 AGREED S36, ONE LINE, HIS YES:** an **episode validator** —
  a list of episode records as plain dicts (NO file I/O, not taught), checked
  against a stated spec, returning a report of every fault, plus a custom
  exception for the case that cannot be reported. ≥90 min, timed, no AI, mentor
  writes the tests. **`LOG.md` IS IN THE DEFINITION OF DONE.** He ruled it runs
  after 1.9 — so it is **due after the gauntlet**, not during it.
- Current Layer: 1. Current Topic: **1.9 closing / 1.10 next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ✅ **ADOPTED S36 — RULES v6, THE SESSION 36 RULE: THE DONE LINE.** His
  proposal, his ruling in four words: *"Adopt with the extra line."*
  > He says **"done"** + **ONE LINE naming the function he trusts least and the
  > case that worries him.** Then the mentor runs pytest. Red comes back as
  > *"find it"*, never as an answer.
  ⚠ **ITS SECOND DATA POINT WAS BAD AND THE NEXT SESSION MUST HOLD THE LINE.**
  He said only *"Done"*; the gate was held; what came back was **a scope report**
  (*"I have done more than what was asked"*), **not a failure prediction.**
  **THE LINE ASKS WHICH CASE BREAKS IT, NOT WHICH FUNCTION FELT BIGGEST.**
- **NOTHING IS PARKED FOR S37.** Do not invent a candidate.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 37 STARTS HERE — exact resume point

**S37 IS THE GAUNTLET. NO NEW MATERIAL.** Load ARCHIVE.md and the master.

Run in this order:

1. **INTERVAL GATE from `git log` + mtimes.** Then say plainly that this is the
   gauntlet and no new material will be taught. Then the **term-tax**.

2. ⚠⚠ **THE THREE THINGS THE GAUNTLET MUST SETTLE, IN THIS ORDER:**
   **(a) THE STRICT-LEGEND AUDIT of every [x]** — the bundled S16 promotions; the
   1.6 spoken Feynman recall; the S22 short-gap promotions; the eight S23; the
   eleven S25; the eight S27; the S29 `zip`; the eight S30; the four S31; the
   four S32; the seven S33; the two S34 (**plus the `.count()` echo caveat on the
   tuple tick**); the one S35; **and the one S36 (`try`/`except`).**
   **(b) THE 31-AUG RE-BASELINE ARITHMETIC, IN ITEMS**, against 30 Sep.
   **(c) THE FOUR OVERDUE COLD ASKS BELOW.**

3. ⚠⚠ **THE ONE ASK THE MENTOR OWES HIM AND MUST FIRE FIRST, CLEAN AND COLD:
   THE COMPILE/RUN SPLIT.** He derived it himself in S35, unprompted, off one
   traceback. In S36 he answered it correctly **but the mentor had quoted his own
   derivation back at him two turns earlier — echo, not recall — and REFUSED the
   promotion out loud.** **Fire it with NOTHING about compilation, bytecode or
   syntax in the preceding three turns. It is a promotion waiting to happen and
   it has now waited twice.** Shape that works: *"a 40-line file, lines 1–39
   perfect, line 40 missing a colon — how much executes?"*

4. ⚠⚠ **THE TRANSFER GAP IS THE WATCH ITEM OF THE WHOLE FILE RIGHT NOW, AND S36
   MEASURED IT TWICE MORE.** He passed both cold bare-`except:` recalls at 7/10,
   fixed his own `total_valid` — **and then shipped a catch-all in fresh code the
   same evening, ORDERED CORRECTLY LAST.** He took the ordering lesson and not the
   catch-all one. **THE GAUNTLET TEST FOR THIS IS NOT A QUESTION, IT IS A FILE:
   give him something small to write and check whether the ideas show up in it.**
   The line to reuse, which he derived himself once asked: **a bare `except:`
   HIDES a fault; a catch-all filing into a NAMED bucket actively LIES about it.**

5. ⚠ **NEW S36, CHEAP TO FIX, EXPENSIVE TO LEAVE: IDENTIFIERS ARE NOT
   PARAPHRASABLE.** The drill spec said `OverLimit`; he wrote `JointLimitError`,
   then `OverLimitError`. **Two collection failures, zero tests run.** Note the
   shape: **the thing on screen five minutes ago beat the spec in front of him**
   — the same mechanism as the catch-all. Watch for it; do not lecture it again.

6. ⚠ **`StopIteration` IS DEMOTED [x] → [~] AND IS DUE 1 SEP.** Mechanism intact
   after three weeks; the label came back as **"EndofIteration"**. His exact
   signature. **Re-ask the LABEL alone.**

7. ⚠ **`SyntaxError` no-frames half — MISSED TWICE NOW, THEN RECLASSIFIED.** He
   pushed back that the framing was unfair (64, **part-upheld** — "does line 1
   print" aims him away from line 3; *"syntax errors are easy to miss"* does
   not stand). **He then passed a clean no-code version.** ⇒ **filed as a
   DETECTION MISS UNDER A BAD FRAME, not a knowledge gap.** Ask it as
   *"what happens when you run this?"*, never as a yes/no about one line.

8. ⚠ **STILL OWED, NOT FIRED IN S36 — this list has not shortened:**
   the mutating tell's **return-value half alone**; `del` as a STATEMENT;
   `.clear()` → `None`; **`while` mechanics, now TEN sessions overdue and the
   oldest debt in the file**; hashability; `subscriptable`; unpacking
   count-mismatch ⇒ `ValueError`; `zip` fails silently twice; **`constructors`
   as his FIRST word (one question from [x], lost in S35 to the mentor's own bad
   tag — re-ask cold and UN-TAGGED)**; `when to use which`; **`.keys()` as a
   view**; `UnboundLocalError`, `print()`, `abs()` (never asked).

9. **AFTER THE GAUNTLET: build block 02** (spec above), then **1.10 modules and
   imports** — for which there is now a natural hook: `import` was used in S36's
   test file, he flagged correctly that it had never been taught (pushback 63),
   and was given the one-line minimum only.

**Standing turn rules: FRAME FIRST — and S36 breached it, so say what an
exercise BUYS before asking for it; CONSOLIDATED QUESTIONS CARRY THEIR OWN
RUNNABLE CODE (breached S36, pushback 62 — no fragments, no `cfg` that is not
defined on screen); SPEC BEFORE PUZZLE with boundaries in the TESTS; short
messages, one teaching idea per turn, asks near the top; doubt gate before every
new subsection; depth-before-answer; NAME THE ERROR BEFORE THE MENTOR SHOWS IT;
take the rating AFTER his answer and GIVE THE VERDICT immediately after — and
TAKE ONE PER DRILL FUNCTION, which S36 forgot and which cost the `raise` bullet
its promotion; tag every block and CHECK THE TAG. Do not propose ending the
session. DO NOT MISQUOTE HIS OWN CODE BACK AT HIM — S36 did, and he did not
catch it.**

**CARRY FORWARD:**
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()`.
- ✅ **THE S35 STYLE NOTE WAS DELIVERED (once, as required):** a library function
  that prints has decided its caller's output policy. Do not repeat it.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Still not asked.
- ⚠ **`[i for i in config]` is just `list(config)`** — seen in his S36
  `read_limit` message. One line, when comprehensions next come up.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
121 rows, **67 [x], 54 [~]**, 12 overdue, 12 never asked.
**Do not re-create the table here.** `python3 tools/retest.py` at the open.
S36 recorded: `try / except` pass 7 → **[x]**; `TypeError` pass 7 → [x];
`specific vs bare except` pass 7 but **HELD [~] deliberately** (curriculum sets
the stricter condition and his fresh code failed it); `StopIteration` **fail →
demoted [~]**; `SyntaxError` **fail → [~]**.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **1.9 try/except** | **S36: PROMOTED on two cold later-day recalls, 7/10 each** | **[x] — re-test ~5 Sep** |
| **1.9 custom exceptions / hierarchy / ordering / re-raise** | **S36 taught + `drills/s36_signals.py` 35/35 — same-session, so echo** | **[~] — cold later-day ask due 1 Sep** |
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | **S36: recalls PASSED, fresh code STILL shipped one** | **[~] — test with a FILE, not a question** |
| **THE COMPILE/RUN SPLIT** | **S36 correct but ECHO-CONTAMINATED; promotion refused by the mentor** | **[~] — CLEAN COLD ASK, S37, no scaffolding** |
| **`StopIteration`** | **S36: mechanism intact 3 weeks, label = "EndofIteration"** | **[~] DEMOTED — label alone, 1 Sep** |
| **NESTED STRUCTURES + SHALLOW COPY + DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| **⚠ THE MUTATING TELL** | S34: TYPE and MUTATES intact, RETURN-VALUE half gone | **[~] — the return-value half ALONE** |
| **`reversed()`** | S35 taught as a pair in one table | **[~] — cold ask OVERDUE** |
| **THE FIVE CHECKS** | **Discharged into the DONE LINE (RULES v6)** | **retired as a report** |
| **`while` mechanics; nested loops; found-flag** | NOT tested S27–S36 | **[~] ⚠ TEN sessions overdue — OLDEST DEBT** |
| Frames / namespace / execution pipeline / REPL vs script | S14, never re-run | [~] **overdue badly** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| **CONTAINERS AS CODE** | S30 19/19; S32 17/17; S34 36/36 | **[x] — closed** |
| **DRY / one copy of a decision** | **S36: `sort_faults` called `check_limit` rather than copying the rule, enforced by a test, first try** | **[~] — later-day ask** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE TRANSFER GAP, NOW THREE SESSIONS DEEP AND THE FILE'S HEADLINE.**
  S33: *change where the ask sits.* S34: *an ask that can be satisfied without
  executing anything will be.* S35: *a fact he can PREDICT is not yet a fact he
  will APPLY.* **S36 adds the sharpest version: he can pass the recall, fix the
  old code, and still ship the same class of bug in the new code an hour later —
  and he took the ORDERING lesson from 90 minutes earlier while dropping the
  CATCH-ALL lesson from four hours earlier. He does not lose the last thing
  taught; he loses the one before it.** The test for a taught idea is his next
  FILE, never his next answer.
- ⚠⚠ **AN ARTEFACT THAT FAILS TWICE IS THE ARTEFACT'S PROBLEM.** S26 table
  failed; the four-station hook failed. **"HOW FAR DID PYTHON GET?" has now
  worked twice** — S35 cold, and S36 on the import failure. **Keep using the
  QUESTION, never a roster.**
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE** — unchanged, and
  it is the entire argument for the done-line in RULES v6.
- ⚠ **THE FRAMING OF A QUESTION IS NOT EVIDENCE** (S35). **S36 shows the mentor
  side of the same coin: a bad frame produced a miss that was NOT a knowledge
  gap.** Check the frame before logging the gap.
- ⚠ **CONFIDENCE CALIBRATION: five ratings in S36 (7, 7, 6, 7, 7).** Four were
  correct-and-under-rated; the 7 on the `SyntaxError` half was wrong. **The S35
  inversion did NOT repeat — he is back to systematic under-rating, with one
  standing exception: he over-rates "did anything run before the error".**
- ⚠ **HE ASKS FOR THE TOOL BEFORE IT IS TAUGHT, BY SHAPE.** S35: he invoked the
  eligibility rule himself. S36: *"I want something more general like
  `except error as e`"* — he described `except Exception` before it existed for
  him. **Second session running. This is the behaviour the course exists to
  produce; give him the tool when he names its shape.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 64 raised, 63 upheld or
  part-upheld.** S36 raised FOUR, all upheld in whole or part.
  **(61)** *"what is it you actually want from this exercise?"* — **UPHELD.**
  FRAME FIRST breached: he was told to edit a line without being told what it
  bought. **(62)** *"the whole code should be in front of eyes"* — **UPHELD IN
  FULL**, S19's own rule, breached with a fragment that was not even runnable.
  **(63)** *"I haven't been taught about any imports"* — **UPHELD IN PART**;
  correct, and the import was in the mentor's test file, so the one-line minimum
  was given and no more. **(64)** *"this one is unfair"* on the `SyntaxError`
  framing — **PART-UPHELD**; the framing half stands, *"syntax errors are easy to
  miss"* does not, and his claim to know the rule was **tested immediately and
  verified**.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35)**;
  GIL (1.13); concurrency (post-Layer 1); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ✅ **THE S15 IOU ON EXCEPTION-DRIVEN CONTROL FLOW WAS PAID IN S36** — `for`
  written out as `while True` + `try` + `except StopIteration: break`.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **`class` — OPENED ON CREDIT IN S36.** He was given exactly
  `class X(Exception): pass` and nothing else. **1.11 owes him the real unit,
  and he now has a concrete hook for it: he has already written two.**
- ⚠ **`except Exception:` vs bare `except:`** — the real difference was named a
  footnote and parked. One line, in 1.11 or 1.13.
- ⚠ **`raise ... from` / exception chaining, `sys.exc_info()`, the `traceback`
  module** — parked from 1.9; mentioned once when custom exceptions landed.
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
