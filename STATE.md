# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 42 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S41**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S41. The gate is PER-MATERIAL (RULES S17-1).
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠ **NO RULE CANDIDATE IS PARKED.** Nothing to rule on at the open.
#      **ONE NON-RULE DECISION IS OWED BY HIM FOR THE THIRD SESSION — item 2.**
#   5. ⚠ **THE QUEUE IS A SCRIPT.** `python3 tools/retest.py` at the open.
#      **128 rows, 96 [x], 32 [~], 40 overdue, 2 never asked.**
#      ⚠ The bare `print()` row cannot be hit by `--asked "print()"` (it
#      substring-matches two rows); edit `tools/queue.json` directly for it.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S41.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN. RED COMES BACK AS ONE GROUP, IN WORDS
#      — NEVER AS A DUMP OF ASSERTION LINES.** S41 defect: eight reds in one
#      message; *"I am unable to understand the errors."* One group at a time
#      then worked every time.
#   9. ⚠ **IN A DRILL DOCSTRING THE EXCEPTION TYPE NAME IS INTERFACE — WRITE
#      `TypeError`, `ValueError`. The CONSTRUCT (`raise`/`except`/subclass) is
#      mechanism — withhold it.** Pushback 76, part-upheld.
#
# STATE AS OF: end of Session 41, **Fri 4 Sep 2026, ~23:10** (verified).
# Next: Session 42 — **1.9 tail cold, then 1.10's untaught half.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE RUN AT THE S41
  GAUNTLET: observed ~0.8 subsection-equivalents/week since 16 Aug; ~5.2 units
  remain (1.9 ×0.7, 1.10 ×0.5, 1.11, 1.12 weighted ×2, 1.13); DERIVED CLOSE ≈
  22 OCT 2026. The 30 Sep gate is missed at the observed rate. LADDER RUNG 1
  INVOKED: weekend blocks first; recompute at the September gauntlet. Nothing
  de-scoped.** Tell him the number if he asks; do not soften it.
- **S41 yield: the gauntlet, at last.** 32 cold asks, 27 passes, 17 queue
  promotions, 1.8 CLOSED, 1.10 taught-half [x], two 1.9 bullets [x], one
  1.5 revert, strict audit 11/12, cold drill skipped at 32/34-then-24/34.
- **Position: 1.1–1.8 closed. 1.9 — three [x] of ten, seven [~]. 1.10 — six
  [x], six [ ] (packages, `sys.path`, circular imports, standard library, pip,
  relative vs absolute, **the `.pyc`/bytecode answer owed since S35**).**
- **RULED S40: `pdb` / VS Code debugger → 1.11.**
- Current Layer: 1. Current Topic: **1.9 tail + 1.10 second half.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **NOTHING ADOPTED IN S41, NOTHING PARKED.** RULES stays at **v6**.
- Two rules of thumb recorded in ARCHIVE S41 §6/§7 (red-as-one-group; type
  name is interface). Neither is proposed as a binding rule. Do not re-raise
  unless he does.

## WHERE WE LEFT OFF

### SESSION 42 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S41 closed Fri 4 Sep ~23:10.

2. ⚠⚠ **DECISION OWED BY HIM, THIRD SESSION RUNNING — asked S41 open, not
   answered:** once 1.10 lands, the weekly cold build block moves to a REAL
   LeRobot file. Not a rule. **One line at the open; if unanswered again, log
   it as declined-by-silence and stop carrying it.**

3. ⚠⚠ **THE SKIPPED DRILL — `drills/s41_commands.py`, committed at 24/34.**
   He skipped it at 22:08 on 4 Sep after a 20-hour break inside it. **Do not
   reopen the file with him unless he asks.** What it owes the ledger is TWO
   facts, and both can be asked cold as snippets, no file:
   - **HIERARCHY DIRECTION** — he wrote `except BadCommand:` around
     `int(text)` after `class BadCommand(ValueError)`. Ask: *`int("n/a")`
     raises a plain `ValueError`. Does `except BadCommand:` catch it? Does
     `except ValueError:` catch a `BadCommand`?* Both directions, one line
     each. This is the 1.9 hierarchy/ordering bullet's real test.
   - **REFUSE vs CONVERT** — `0 <= 45.0 <= 90` is `True`; `int(45.0)` is
     `45`. Ask: *how does a function REFUSE a float when the comparison will
     not?* (`type(angle) != int` — he used it in S37.)

4. ⚠⚠ **DUE 5 SEP (rated low or failed S41):** `UnboundLocalError` — ask the
   DELETION TEST cold (*remove the assignment; what prints and why?*); he gave
   a clean teach-back after being taught, so this is the first cold pass or
   not. `* on a sequence` — fire `[[0]*3]*3` again. `None-as-absence` — ask
   *why `None` and not `0` for "not found"; why not `-1`?* `subscriptable` (5).
   `augmented assignment` — `x += [2]` vs `x = x + [2]` with an alias, cold.

5. ⚠ **DUE 3–4 SEP, NOT REACHED IN S41:** `slicing / SHALLOW COPY`, `zip`,
   `zip FAILS SILENTLY`, `KeyError vs IndexError`, `hashable`, `{} is a DICT`.
   Run `python3 tools/retest.py --overdue` and take the oldest first.

6. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED FROM ITEM 8 OF S40:** `DRY`, `mutate-while-iterating` (now has
   a live instance: `list(z)` after `d["c"] = 3` → `RuntimeError`), `list
   method roster`, `HOW FAR DID PYTHON GET?`.

7. **THEN NEW MATERIAL, 1.9 TAIL FIRST:** `raise ... from`, `except Exception`
   vs bare `except` footnote, the hierarchy taught AGAIN with the DIRECTION
   drawn (parent catcher catches child; child catcher does not catch parent)
   — he has now failed the direction once under fatigue. Then 1.10's second
   half, opening with the owed `.pyc` answer.

**Standing turn rules: FRAME FIRST; CONSOLIDATED QUESTIONS CARRY THEIR OWN
RUNNABLE CODE; SPEC BEFORE PUZZLE with boundaries in the TESTS and TYPE NAMES
in the docstring; ONE TEACHING IDEA PER TURN; RED AS ONE GROUP IN WORDS; asks
near the top; doubt gate before every new subsection; depth-before-answer;
NAME THE ERROR BEFORE THE MENTOR SHOWS IT; rating AFTER his answer and BEFORE
the verdict — held S41 throughout; tag every block. Do not propose ending the
session. DO NOT MISQUOTE HIS OWN CODE. NEVER EDIT HIS DRILL FILE — he asked
in S41 and was refused; that refusal stands.**

**CARRY FORWARD:**
- ⚠⚠ **A LONG BREAK INSIDE A DRILL NEEDS A RE-GATE AND A RE-FRAME.** S41: 20
  hours between sittings, none given, and the direction error followed.
- ⚠⚠ **DECLARED GAP → FRAME → DEFINITION → [TEACH-BACK].** Held S41 on
  `UnboundLocalError` and `None`-as-absence; both teach-backs clean.
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S41 for all
  20 snippets; it caught the `zip`/`RuntimeError` footnote in advance.
- ⚠ **Language: "the ITERATOR is exhausted"** (three issues). Not tested S41.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()` vs
  `+`. (`print()` cleared S41, `abs()` S40.)
- ⚠ **`[i for i in config]` is just `list(config)`** — he wrote it AGAIN in
  `check`'s message. Still not said. Say it next time it appears.
- ⚠ **DEAD CODE** — full treatment parked.
- Governance/format requests mid-session → PARK, close material, write at end.
- **`teaching/s41_gauntlet/fin_loop.py`** — mentor demo, the two `finally`
  shapes. Not his work. Re-runnable.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**128 rows, 96 [x], 32 [~], 40 overdue, 2 never asked.** Do not re-create the
table here. `python3 tools/retest.py` at the open.
**S41: 17 promotions, 3 fails** (`UnboundLocalError` mechanism, `* on a
sequence` at 3, `None-as-absence` gap). Details in ARCHIVE S41 §9.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls, reason spoken | **[x] — CLOSED on two cold files (S37, S41). Re-test at the next build block.** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S41: applied BACKWARDS under fatigue | **[~] — snippet ask, item 3. Then re-teach with the direction drawn.** |
| **`.keys()` AS A VIEW** | S41: PASS, 6 | **[x] — 8 Sep. `dict` bullet closed.** |
| **1.10 — taught half** | S41: 7/7 at 7, ~51h cold | **[x] — 8 Sep** |
| **THE COMPILE/RUN SPLIT** | S38 PASS 7; S41 pipeline 7 | **[x] — 6 Sep** |
| **`while` mechanics; nested loops; found-flag** | S38: 20/20 COLD | **[x] — 6 Sep** |
| **Frames / namespaces / execution pipeline** | S38 full trace; S41 UBL mechanism GAP then taught | **[x] — 6 Sep; UBL deletion test 5 Sep** |
| **THE MUTATING TELL** | S38 both halves; S41 given unprompted under the wrong question | **[x] — 6 Sep** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38: cold, 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S38 cold | **[x] — OVERDUE 3 Sep, not reached** |
| **`constructors`** | S38: 7/10 | **[x] — 6 Sep** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 custom exceptions / hierarchy / re-raise** | S41 drill: `raise` clean, hierarchy direction failed | **[~] — item 3, then re-teach** |
| **1.9 `finally` guarantee** | S41: PASS 7 + used correctly in the drill | **[x] — 8 Sep** |
| **`short-circuit`** | S41: PASS 7 | **[x] — 8 Sep** |
| **1.9 try/except** | S36 promoted; S41 drill clean | **[x] — 5 Sep** |
| **`StopIteration`** | S40 PASS 7 | **[x] — 7 Sep** |
| **DRY / one copy of a decision** | S37 held structurally; S41 `run` asks `check`, holds | **[~] — later-day ASK still owed** |
| **NESTED STRUCTURES + SHALLOW/DEEPCOPY** | S41: slice-copy + deepcopy 7; **`[[0]*3]*3` MISSED at 3** | **[x] — the `*` aliasing case 5 Sep** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | **S41: DEMOTED, right output wrong model, 5** | **[~] — 6 Sep** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 survive | **DONE — next audit at the September gauntlet** |
| Frames / REPL vs script | S38 frames only | [~] **the REPL half still overdue** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **NEW IN S41: HE ASKED THE MENTOR TO EDIT HIS DRILL AND SHOW THE FIX, THEN
  SKIPPED THE DRILL.** *"You know what please edit the code and show me my
  error"* → refused → *"I want to strictly skip this exercise."* First on
  record for both. Context: 22:00 on the second evening of a drill that had
  stalled at 01:30 the night before, two lines from green. **Read it as
  fatigue plus a stalled fix, not as a pattern — unless it recurs.** The
  remedy is item 3: ask the two facts as snippets, no file.
- ⚠⚠ **THE HIERARCHY DIRECTION INVERTED UNDER FATIGUE.** Told "a parent's
  catcher catches the child", he changed the parent catcher to the child. This
  is a rule he can STATE and could not APPLY at 22:00. Re-teach with the
  direction drawn, then test cold.
- ⚠⚠ **RIGHT OUTPUT, WRONG MODEL — TWICE MORE.** `x = x + [2]` "mutates"
  (S41); the grid `[[0]*3]*3` (S41, rated 3 — calibrated). Same signature as
  `short-circuit` S37. **His code would work; his explanation of why would
  not survive an interview.** Keep asking the WHY after every right output.
- ⚠⚠ **PUSHBACK 75 WAS THE SECOND NOT UPHELD ON ITS FACT, AND IT WAS A
  SURFACE READ OF THE SPEC** — the quotes in the worked example were not seen.
  He named this habit himself in S20 (depth-before-answer). **Running total:
  76 raised, 74 upheld or part-upheld.** Say the arithmetic; he prefers it.
- ⚠ **CONFIDENCE CALIBRATION — GOOD AGAIN.** 3 on the grid (miss), 5 on
  `+=` (half-miss), 5 on `subscriptable` (pass, but third asking), 7s and 8s on
  clean passes. Use ≤5 as the targeting signal.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE — CONFIRMED IN
  BOTH DIRECTIONS.** Every red delivered as ONE group in words was found off a
  single pointer; eight reds in a dump were unreadable to him.
- ⚠ **HE UNDER-RATES HIS RETENTION** — reversed on `_` (S40 withdrawn, S41
  passed at 6).
- ⚠ **HE PRODUCED THE MODULO IDENTITY UNPROMPTED** (owed since S18). Not a
  watch item; recorded so nobody asks for it again.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()` as an
  object, `.append()` vs `+`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 76 raised, 74 upheld or
  part-upheld.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read;
  **`.pyc` and what the bytecode actually IS (1.10 — promised S35, STILL
  OWED, opens 1.10's second half)**; GIL (1.13); concurrency (post-Layer 1);
  GC (1.13)
- ✅ **BREAKPOINT DEBUGGING / `pdb` / VS Code debugger — RULED S40: 1.11.**
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 owes him the real unit. S41 showed
  the cost: `class X(Y)` is written by pattern, and the direction of what
  `(Y)` buys was inverted.
- ⚠ **`except Exception:` vs bare `except:`** — 1.9 footnote, owed.
- ⚠ **`raise ... from` / chaining, `sys.exc_info()`, `traceback` module** — 1.9.
- ⚠ **`enumerate()`** — used by the mentor in the `None`-as-absence demo
  (S41), never taught. Define it before it appears in a drill.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — shown as a
  footnote S41; belongs with `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE**; **EXPRESSION vs STATEMENT** (reinforced S38);
  **`__dict__`** (1.12–1.13); **PEP 709** (1.13); `nonlocal` (1.13); `pop`
  internals (1.13); `copy.copy()` one line; deepcopy on self-reference (1.13);
  bytecode constants (1.13); **HASH RANDOMISATION** (1.13); **`%` and
  `.format()`** as a reading skill; `capsys` — not Layer 0.

---
