# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 36 (for Claude):
#   1. Read RULES.md fully (**v5 — unchanged in S33, S34 and S35**), then this
#      file fully. No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE — **AND VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER OR HIS WORD.**
#      ⚠⚠ **S35 GOT THIS WRONG.** The gate was ruled "same sitting" off the
#      model's context header (29 Aug) plus his *"today is saturday"*; the drill
#      file's mtime says **Sun 30 Aug 17:10 BST**. If it was the 30th, S34's
#      material was ELIGIBLE and was wrongly deferred all night. **No promotion
#      is corrupted — everything promoted in S35 was S27 material, 7 days cold —
#      but a whole session of promotable evidence was thrown away.**
#      **ASK HIM AT THE OPEN WHICH DAY S35 RAN, then fix the dates here.**
#   3. ⚠⚠ **THE AUGUST GAUNTLET IS NOW TUESDAY 1 SEP — HIS CALL, TAKEN IN S35.**
#      He has Mon 31 Aug and Tue 1 Sep off work and wants volume. So S36 (Mon)
#      is a TEACHING session; the gauntlet is S37 (Tue), carrying the
#      strict-legend audit AND the 31-Aug re-baseline arithmetic.
#   4. ⚠ **ONE RULE CANDIDATE IS PARKED AND HE HAS ALREADY AGREED TO IT
#      OPERATIONALLY — take the formal ruling at the open.** See RULE-CHANGE
#      PARKING below. One line; do not debate it.
#   5. ⚠ **THE QUEUE IS NOW A SCRIPT. USE IT.** `python3 tools/retest.py`.
#      He ruled it in S35 and ordered that he never has to touch it. **Do not
#      schedule re-tests from memory or from a markdown table ever again.**
#      `--answers` shows the hooks; `--asked "<term>" --result pass --rating 7`
#      records the outcome and sets the next date.
#   6. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** Held clean in S35.
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held clean S35.
#   8. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 35, Sun 30 Aug 2026 (see item 2 — date disputed).
# Next: Session 36 — **finish 1.9.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally at the gauntlet — in ITEMS)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S35 yield: ONE PROMOTION, ONE CURRICULUM TICK (1.8 `set` — bullet CLOSED),
  1.9 OPENED AND FOUR OF ITS NINE BULLETS TAUGHT, and `drills/s35_faults.py`
  29/29 GREEN ON THE FIRST RUN** — on material he had never written a line of
  ninety minutes earlier. **Strongest first-sitting drill result in the file.**
- **Position: 1.1–1.7 closed. 1.8 — TWO bullets still [~]. 1.9 open, ~40%.**
- **1.8 — what remains. It shrank from three to two:**
  - ✅ `set` — **CLOSED S35.** `set()` vs `{}` written cold with the mechanism
    attached to both, unprompted, 7/10, seven days after S27.
  - `dict` — **`.keys()` AS A VIEW WAS FINALLY TAUGHT (S35), so it is no longer
    blocked — but it was taught TODAY and cannot be tested today.** ONE cold
    later-day ask closes this bullet. **It is the cheapest tick on the board.**
  - `list` — **HELD [~].** The returns-`None` tell broke live in S34.
  - `when to use which` — still never asked cold. Legitimate since S33.
- ✅ **BUILD BLOCK 01 CLOSED.** ⚠ **`LOG.md` STILL NOT WRITTEN. SIXTH SKIP.**
- ⚠⚠ **BUILD BLOCK 02 NEEDS A NEW TASK.** It was going to be the re-test queue
  script — but in S35 he ruled that the mentor builds and maintains it and *"I
  don't need to know about it"*. **The script is DONE and is a mentor tool.
  Propose a new block-02 task at the S36 open, one line.**
- Current Layer: 1. Current Topic: **1.9 error handling.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ⚠ **PARKED S35, PROPOSED BY THE STUDENT (pushback 60), ALREADY RUNNING
  OPERATIONALLY, RULING OWED AT THE S36 OPEN:** *"I will just say Done and you
  execute the test on the drill file, and if some error comes you can ask me to
  find the error, then I will implement the check."*
  **MENTOR RECOMMENDATION: ADOPT, WITH THE ONE-LINE ADDITION HE ALREADY
  ACCEPTED.** The form that ran in S35 and worked:
  > He says **"done"** + **one line naming the function he is least sure about
  > and the case that worries him.** THEN the mentor runs pytest. A red test
  > comes back as *"find it"*, never as an answer.
  **WHY IT IS RIGHT:** the mentor's tests already cover boundary/khaali/ek/
  bahar, so hand-running all five duplicated work — his S24 ruling (*scan five,
  report only the ones that bite*) had been silently escalated past by the
  mentor, and he was right to say so. **WHY THE ONE LINE MATTERS:** in an
  interview nobody hands him a test suite, and STATE has recorded twice that he
  *debugs well with a traceback and poorly without one*. The pre-run line is the
  only thing standing between the new flow and making that permanent.
  ⚠ **FIRST DATA POINT, S35, AND IT WAS GOOD:** he flagged `check_angle` for
  missing **bahar-by-TYPE** — the subtle half of check 4 — unprompted.
- ✅ **RULED S35 (pushback 57): SCRIPT, NOT A RULE.** Built: `tools/retest.py`
  + `tools/queue.json`, 121 rows. **RULES stays at v5.** He added: *"maintain it
  in such a way that I don't need to know about it, and you can audit it
  whenever you want."*
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.

## WHERE WE LEFT OFF

### SESSION 36 STARTS HERE — exact resume point

S35 opened on the interval gate + the S34 rule ruling, closed the 1.8 `set`
bullet in three minutes, retired the four-station hook, opened 1.9 and taught
`try`/`except`, specific-vs-bare `except`, `raise`, `except … as e`, and
`else`/`finally`. `drills/s35_faults.py` came back **29/29 first run.**

Run in this order:

1. **INTERVAL GATE — verified from `git log` and mtimes, not from memory
   (header item 2).** Then the **rule ruling** (parking lot above), one line.
   Then **the new build-block-02 task**, one line.

2. ⚠⚠ **THE S35 HEADLINE, AND IT IS THE ONE THING THAT MUST BE ASKED FIRST:
   HE WROTE A BARE `except:` FORTY MINUTES AFTER AGREEING IT WAS THE WORST
   POSSIBLE BEHAVIOUR.** In the `total_valid` prediction he was shown a bare
   `except:` turning a one-character typo into a silent `total: 0`, was asked
   which was more dangerous, and answered — correctly and unprompted —
   *"obviously total:0 is more dangerous, because you ended up believing that
   program is running fine."* **Then he wrote `except: pass` in his own
   `total_valid`.** Told at the close, he named it correctly immediately.
   **THIS IS NOT A KNOWLEDGE GAP. IT IS A TRANSFER GAP — understanding held in
   [PREDICT] and did not survive into PRODUCTION.** New watch area.
   **THE ASK: give him a function with a bare `except:` in it and ask what it
   costs. Then have him fix his own `total_valid`.**

3. ⚠ **THE `SyntaxError` ROW IS HALF-CLOSED AND THE OTHER HALF JUST BROKE.**
   Label named correctly cold — **first hit in three firings** after misses in
   S27 and S32, on a NEW shape (a missing colon, not a statement-inside-`print`).
   **But asked whether line 1 printed, he said YES. It does not.** The
   no-frames / nothing-ran half is written into the row itself. **Re-ask that
   half alone, cold, and note he rated the wrong half 7/10 — his first
   over-rating in a long while; his usual error is under-rating.**

4. ✅ **THE FOUR-STATION HOOK IS RETIRED. DO NOT RE-DRILL IT.** Asked to name
   the stations he said *"I still don't remember that hook, it has not been
   working for me."* **Second artefact failure on the same material** (the S26
   TABLE failed inside twenty minutes; the hook that replaced it has now failed
   too). Diagnosis: the hook was five arbitrary words on top of machinery he
   owns — the exact thing this file says he drops.
   **THE REPLACEMENT, TAUGHT S35 AND IT WORKED ON FIRST USE: "HOW FAR DID
   PYTHON GET?"** He walked the whole timeline unaided — syntax → does the name
   exist → the operation → the specific key — and produced it as a TIMELINE,
   not a list. Rated 6/10, and under-rated. **Keep asking in that form.**

5. ⚠⚠ **HE DERIVED THE COMPILE/RUN SPLIT HIMSELF, UNPROMPTED, OFF ONE
   TRACEBACK** — *"python compiler is compiling the file to bytecode, and all
   the syntax error is checked there itself… once the bytecode is there, then
   execution starts, and then we come towards the other errors."* Confirmed and
   sharpened with the one thing missing: **the compiler checks GRAMMAR, never
   MEANING — a typo'd NAME compiles perfectly.** `.pyc` parked to 1.10.
   **This is the third session running with an unprompted derivation. Re-ask it
   cold; it is a promotion waiting to happen.**

6. ⚠ **`TypeError` vs `ValueError` WOBBLED AND HE NAMED THE CAUSE HIMSELF.**
   Volunteering a revision he called `1 + "a"` a `ValueError`. **Recovered fully
   on a one-line narrowing**, with the right mechanism both ways and a good
   counter-example (`"1" + "a"` would concatenate). His own diagnosis: *"this is
   my problem, its old content, not being revised for long."* **That is the
   script's whole purpose — both rows are now on a 2-day interval in it.**
   Discriminator given: **change only the VALUE and it works ⇒ `ValueError`;
   change only the TYPE and it works ⇒ `TypeError`.**

7. ⚠ **HE TALKED HIMSELF OUT OF A CORRECT ANSWER BECAUSE OF THE MENTOR'S
   FRAMING.** On "does `finally` run when nothing catches the exception?" he
   said *"should[n't it be] like the other cases"* — right — then reversed:
   *"since you are specifically showing this case, I presume not."* Named to his
   face: **the framing of a question is not evidence.** Watch for it; it will
   cost him in an interview.

8. ⚠ **STILL OWED FROM S34, NOT FIRED IN S35:** the mutating tell's
   **return-value half alone** (he owns TYPE and MUTATES); `del` as a STATEMENT;
   `.clear()` → `None`; **`while` mechanics, now NINE sessions overdue**;
   hashability; `subscriptable`; unpacking count-mismatch ⇒ `ValueError`; `zip`
   fails silently twice; `constructors` as his FIRST word; `when to use which`.
   ⚠ **`constructors` NEARLY CLOSED AND THE MENTOR'S OWN TAG COST IT:** he said
   *"the constructor of the set **builds** the set object over the iterable"* —
   the exact first word the row has waited for since S33 — **inside a block the
   mentor had tagged [TEACH-BACK], which is never ledger-eligible.** Not banked.
   **Re-ask it cold and un-tagged; it is one question from [x].**

9. **THEN FINISH 1.9:** custom exceptions, `raise` re-raise, exception hierarchy,
   exceptions-for-control-flow (the iteration protocol IS this, and it is a good
   design point), defensive-programming mindset. **`traceback` reading is going
   well — build on the two-frame example from S35.**

**Standing turn rules: FRAME FIRST, and say out loud how much each fact is
worth (it worked in S35 — "finally is load-bearing, else is a scoping tool");
SPEC BEFORE PUZZLE — exact interfaces and exact expected values, in a file, with
boundary cases in the TESTS; short messages, one teaching idea per turn, asks
near the top; doubt gate before every new subsection; depth-before-answer;
NAME THE ERROR BEFORE THE MENTOR SHOWS IT; take the rating AFTER his answer and
GIVE THE VERDICT immediately after; tag every block and CHECK THE TAG IS RIGHT
— an accidental [TEACH-BACK] tag cost a promotion in S35. Do not propose ending
the session.**

**CARRY FORWARD:**
- **The gauntlet (Tue 1 Sep) carries:** the strict-legend audit of every [x] —
  the bundled S16 promotions; the 1.6 spoken Feynman recall; the S22 short-gap
  promotions; the eight S23; the eleven S25; the eight S27; the S29 `zip`; the
  eight S30; the four S31; the four S32; the seven S33; the two S34 (**plus the
  `.count()` echo caveat on the tuple tick**); **and the one S35.**
  **Plus the 31-Aug RE-BASELINE arithmetic, in ITEMS.**
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()`.
- ⚠ **STYLE, S35, both small:** he left a debug `print` in `measure` and a
  `print(e)` inside `safe_angles`. **A library function that prints has decided
  the caller's output policy** — which is the same division-of-labour point
  `raise` was taught with. One line, once.
- ⚠ **`{angle:4.1f}` on an int** renders `200` as `200.0`. Ask why a reading
  that is an `int` should be shown as a float.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- Every teaching block shows full runnable source alongside output.

## TERM RE-TEST QUEUE — ⚠ **MOVED OUT OF THIS FILE, S35.**
**It now lives in `tools/queue.json` and is driven by `tools/retest.py`.**
121 rows, 67 `[x]`, 54 `[~]`, 12 overdue, 12 never asked.
**Do not re-create the table here.** `python3 tools/retest.py` at the open.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **1.9 try/except/else/finally/raise** | **S35 taught + `drills/s35_faults.py` 29/29 FIRST RUN — but same-session, so echo** | **[~] — cold later-day ask due 1 Sep** |
| **NESTED STRUCTURES + SHALLOW COPY + DEEPCOPY** | S33 25/25 cold | **[x] — ~3 Sep** |
| **⚠ THE MUTATING TELL** | S34: TYPE and MUTATES intact, RETURN-VALUE half gone | **[~] — the return-value half ALONE** |
| **`reversed()`** | **S35 TAUGHT AS A PAIR IN ONE TABLE (the S33 remedy). He could not say what it hands back — honest gap — then took the table** | **[~] — cold ask due ~2 Sep** |
| **THE FIVE CHECKS** | **⚠ S35: the reporting FORM was demonstrated for the first time, on a worked example. He then challenged the cost and won (see parking lot)** | **[~] — now discharged via the pre-run line** |
| **`while` mechanics; nested loops; found-flag** | NOT tested S27–S35 | **[~] ⚠ NINE sessions overdue** |
| Frames / namespace / execution pipeline / REPL vs script | S14, never re-run | [~] **overdue badly** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| **Four-station hook** | **⚠⚠ RETIRED S35 — he could not recall it and reported it had never worked. Replaced by "HOW FAR DID PYTHON GET?", which worked first time** | **retired** |
| **CONTAINERS AS CODE** | S30 19/19; S32 17/17; S34 36/36 | **[x] — closed** |
| **DRY / one copy of a decision** | S31 applied fast; **S35: `safe_angles` correctly held no second copy of the rule, enforced by a test and passed first run** | **[~] — later-day ask** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S35 HEADLINE: UNDERSTANDING IN [PREDICT] DID NOT TRANSFER INTO
  PRODUCTION.** He predicted the bare-`except:` disaster correctly, called it
  more dangerous than a crash in his own words, and wrote one forty minutes
  later. **S33's lesson was "change where the ask sits". S34's was "an ask that
  can be satisfied without executing anything will be". S35's is the next one:
  a fact he can PREDICT is not yet a fact he will APPLY. The test for a taught
  idea is whether it shows up in his next file, not whether he can predict it.**
- ⚠⚠ **AN ARTEFACT THAT FAILS TWICE IS THE ARTEFACT'S PROBLEM.** The S26 error
  TABLE failed in twenty minutes; the four-station hook that replaced it failed
  outright. **Both were arbitrary labels stacked on machinery he owns — the
  precise failure mode this file has documented since S12.** What worked
  instead was a QUESTION he could ask the code ("how far did Python get?"),
  which is the same shape as the S17 discriminator ruling. **When an artefact
  fails, do not re-drill it; check whether it is a list or a question.**
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE** — unchanged, and
  it is now the argument for the pre-run line in the new drill flow.
- ⚠ **THE FRAMING OF A QUESTION IS NOT EVIDENCE** — new S35, item 7 above.
- ⚠ **CONFIDENCE CALIBRATION: three ratings taken (7, 6, 7), and the pattern
  INVERTED for the first time.** The 7 sat on the half he got WRONG; both 6s sat
  on answers that were correct and complete. **His usual signature is
  under-rating. Watch whether this repeats.**
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 60 raised, 59 upheld or
  part-upheld.** S35 raised THREE, all upheld in whole or part.
  **(58)** *"am I eligible to answer this because raise statement ValueError()
  and you are using it as a function — this is totally unknown to me"* —
  **UPHELD IN FULL. Define-before-use, substrate included, ELEVENTH
  occurrence**, and the first time he has invoked the eligibility rule himself
  rather than answering anyway.
  **(59)** the cost of reporting five checks per function — **PART-UPHELD**: the
  mentor had escalated past his own S24 ruling (*scan five, report the ones that
  bite*); the execution requirement stood, the reporting burden was cut, and the
  cost was fixed with a tool (`drills/s35_check.py`) rather than a lecture.
  **(60)** the drill flow — **UPHELD**, now parked as the S36 rule candidate.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read (1.9);
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35, off his own
  compile/run derivation)**; GIL (1.13); concurrency (post-Layer 1); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
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
- **`traceback` module, `sys.exc_info()`, exception chaining (`raise … from`)** —
  parked from 1.9; mention once when custom exceptions land.

---
