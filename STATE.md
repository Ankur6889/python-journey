# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 48 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S47**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S47 at the open. Re-state it per block.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠⚠ **ONE RULE CANDIDATE IS PARKED (see RULE-CHANGE PARKING). ASK FOR
#      HIS RULING BEFORE TEACHING. He may reject it.**
#   5. ⚠⚠⚠ **THE VOLLEY FIRED IN S47 — FOUR ASKS, NOT EIGHT, AND HE STOPPED
#      IT AFTER TWO MENTOR ERRORS.** `python3 tools/retest.py --overdue
#      --all` at the open. **161 rows, 101 [x], 60 [~], 115 overdue.**
#      BUILD EVERY ASK CLEAN: no error name in the header, no name he has
#      never seen, the snippet on screen. Two of five asks were voided by
#      construction errors (pushbacks 95, 97). Run it first; ask him to
#      confirm the order if he wants teaching first, and say what it costs.
#   6. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   7. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S37–S47.
#   8. ⚠⚠ **ONE TEACHING IDEA PER TURN, ONE IDEA PER DEMO, AND WALK THE FILE
#      LINE BY LINE.** Pushback 99 (S47): `no_close.py` pasted with a
#      one-line gloss → *"you gave the file but didn't explain it at all."*
#      Paste, then walk, then ask. Fifth session where prose-only failed.
#   9. ⚠⚠⚠ **A FACT HE DOES NOT HAVE CANNOT BE ASKED OUT OF HIM.** Pushback
#      96 (S47): after a FAILED recall on `+=`, the mentor asked a second
#      Socratic question instead of giving the missing fact; he was
#      furious and right. After a fail: give the fact, physically, then
#      move on. (Parked as a rule candidate.)
#  10. ⚠⚠ **[PREDICT] ONLY FROM WHAT IS ON SCREEN.** Pushback 98 (S47): a
#      second `.read()` was posed before the cursor had been shown.
#  11. ⚠⚠ **NEVER PUT THE ERROR NAME IN THE QUESTION HEADER.** Pushback 95.
#  12. ⚠⚠ **NEVER USE A NAME HE HAS NEVER SEEN IN A COLD ASK.** Pushback 97:
#      `LookupError` was in the S46 plan and had never been taught. Grep
#      notes/ + teaching/ + drills/ before posing any label.
#  13. ⚠⚠ **FILES YOU CREATE: SAY SO, LIST THE PATHS, PASTE EACH FILE'S CODE
#      UNDER ITS PATH, AND SHOW THE COMMAND THAT RAN IT.** Held S47 (27
#      files). Do not show shell pipes (`2>&1 | tail`) he has not been
#      given — he asked what it was.
#  14. ⚠⚠ **NEVER OVERWRITE A FILE WITHOUT LOOKING AT IT FIRST.** Held S47.
#  15. ⚠⚠ **NO `python3 -c` IN A DEMO. WRITE THE FILE.** Held S47.
#  16. ⚠⚠ **WHEN HE ASKS A DIRECT QUESTION, ANSWER IT.** Held S47 (context,
#      `os` module, "do I need to remember this syntax", `2>&1`).
#  17. ⚠⚠⚠ **WHEN HE SAYS STOP, THE CLOSE IS WRITTEN IN THAT TURN.** Held S47.
#  18. ⚠ **`except ... as e` NEEDS class → object, ON CREDIT UNTIL 1.12.**
#      **`Path` is a class, `with` is a dunder pair — both ON CREDIT.**
#
# STATE AS OF: end of Session 47, **Sat 12 Sep 2026, 07:55** (`date` at his
# close request). Two blocks: **Fri 11 Sep 18:26 → ~21:40** (volley + 1.11
# through CSV; demo mtimes 19:04 → 21:35) and **Sat 12 Sep ~07:40 → 07:55**
# (JSON; mtimes 07:43 → 07:53). He asked *"close the session."*
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S47 yield (~3h15 + 15 min):** volley 4 asks (3 pass, 1 fail, 1 voided);
  **1.11 FILE HANDLING OPENED AND TAUGHT-COMPLETE in one session**, every
  bullet [ ] → [~], 14 ideas, 27 files in `teaching/s47_files/`. ~1.0
  unit-equivalent. Five pushbacks (95–99), all upheld. Two promotions
  from the volley ([~] → [x]: `UnboundLocalError`, `None / is None`).
- **Position: 1.1–1.8 closed. 1.9 — cold asks still OVERDUE (7 Sep). 1.10
  — six [x], seven [~], cold asks legal now. 1.11 — nine [~], zero [x].**
- ✅ **DECIDED S42:** the weekly cold build block moves to a **REAL LeRobot
  file**. Still not placed. 1.11 gives it its material (a `meta/info.json`
  or an episode CSV reader). Place it.
- **RULED S40: `pdb` / VS Code debugger → 1.11.** Not yet taught; 1.11 is
  taught-complete without it. Owed inside 1.11 before it closes.
- Current Layer: 1. Current Topic: **volley → 1.10 + 1.11 cold asks →
  1.11 drill → LeRobot block → 1.12 OOP.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **PARKED S47 (mentor-proposed, from pushback 96): "AFTER A FAILED
  [RECALL], THE MISSING FACT IS GIVEN, NOT ASKED FOR."** Once a cold ask
  has failed and the rating is taken, the mentor gives the fact
  physically (a run) and moves on. No second Socratic question on a gap
  he has just demonstrated. His words: *"if I would have known what
  a+=[3] is doing my remaining logic is correct so you need to tell me
  that instead of asking."* Ask for his ruling at the S48 open; he may
  reject it. RULES stays at **v6** until then.

## WHERE WE LEFT OFF

### SESSION 48 STARTS HERE — exact resume point

1. **INTERVAL GATE from `git log` + mtimes.** S47 closed Sat 12 Sep 07:55.
   1.11 material is legal from **13 Sep**. S46 material (stdlib, `bisect`,
   `*`, `enumerate`, pip, shadowing) is legal now. Everything older is
   legal now.

2. **THE PARKED RULE — one-line ask, his ruling, before anything else.**

3. ⚠⚠⚠ **THE VOLLEY, built clean.** `python3 tools/retest.py --overdue
   --all`, oldest first, task-first, text, one at a time, rating after
   his answer. Before each ask: grep the label, run the snippet, keep the
   name out of the header. Re-pose the two S47 asks that did not land:
   - **Hierarchy direction** with a TAUGHT pair (run-verified,
     `scratchpad`): `except Exception` before `except KeyError` on a
     missing dict key → `"general"`, and "what does that make the second
     block" (dead code). He never answered it; he stopped the volley.
   - **`+=` on a list** (FAILED S47, new row due 13 Sep): alias `b = a`,
     `a += [3]`, `print(b)`. Ask for the line AND the identity.
   Then from the S41/S42 list still unasked: `subscriptable`; **refuse vs
   convert**; `mutable default + sentinel`; `< > ^ in a format spec`
   (FAILED S43); `keyword argument` label (FAILED S43).

4. **THEN the 1.10 cold asks, task-first, each with its full scenario:**
   route rule (a `sys.path` list printed in the question); packages bound
   name; `from . import limits` absolute form (parked twice — cold task
   only, no re-teach); run-directly trap; circular (error SEEN, so fair);
   `__main__` placeholder; shadowing; pip.

5. **THEN the 1.11 drill (legal 13 Sep, and the first cold evidence for
   the unit).** Spec-before-puzzle: `drills/s48_files.py`, mentor tests.
   Candidate shape: `load_limits(path) -> dict[str, int]` from a CSV with
   a header (`with`, `csv.reader`, `int()`), `save_limits(path, d)` as
   JSON, round trip in the tests, one row with a quoted comma. Put the
   `"w"`-truncation case and the missing-file case in the tests.

6. **THEN the LeRobot block** (S42 decision, four sessions unplaced).

7. **THEN 1.12 OOP.** Prerequisite gate: 1.11 nine [~], 1.10 seven [~].
   `class` has been on credit since S36; 1.12 opens with the exception
   classes. `pdb` is still owed inside 1.11 first.

8. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** — `notes/session_21_notes.md`
   + `drills/s22_report.py`. Cold ask after. Not touched S44–S47.

9. ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
   **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
   `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half.

**Standing turn rules: RULING FIRST; VOLLEY SECOND; FRAME FIRST; physical-
first; PASTE THEN WALK THEN ASK; AFTER A FAIL GIVE THE FACT; [PREDICT]
ONLY FROM THE SCREEN; NO ERROR NAME IN A HEADER; NO UNSEEN NAME IN AN ASK;
ANSWER A DIRECT QUESTION DIRECTLY; FILES BY PATH WITH CODE AND THE
COMMAND; NO `-c`; NO SHELL PIPES HE HAS NOT BEEN GIVEN; SPEC BEFORE
PUZZLE; ONE IDEA PER TURN; asks near the top; doubt gate before every new
subsection; rating AFTER his answer and BEFORE the verdict; tag every
block. Do not propose ending the session. WHEN HE SAYS STOP, WRITE THE
CLOSE IN THAT TURN. NEVER EDIT HIS DRILL FILE. NEVER OVERWRITE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **`+=` ON A LIST — FAILED COLD, RATED 7 (over-rated).** He modelled
  `a += [3]` as a rebind. Fact given with `v4_id.py` (`id` equal through
  `+=`, different after `a = a + [4]`); discriminator: mutable type ⇒ in
  place, immutable ⇒ must rebind. Row `augmented assignment += on a
  MUTABLE type` [~] due 13 Sep. **Ask for the identity, not just the line.**
- ⚠ **`UnboundLocalError` promoted with the LABEL LEAKED** (pushback 95).
  Mechanism and the deletion test were his and clean; sharpening given:
  the COMPILER marks the name local, not the `def` line. **Re-check the
  label naked at the next due date (16 Sep).**
- ⚠ **`[[0]*3]*3`: line right, "three copies" → "three references" after
  one narrowing question.** Rated 6, honest. Language precision: a copy
  is a second object.
- ⚠ **`is None` clean at 7.** `.get()` → `None` as the reason, unprompted.
- ⚠ **1.11 model slips, corrected once, watch on the cold ask:** *"a file
  is like a list of strings"* → one string, the reader cuts at `\n`;
  `"w"` predicted as cursor-at-start → truncates at `open`.
- ⚠ **He asked "do I need to remember this syntax?"** Answer given and to
  be kept: cold = `with open(p) as f`, `for line in f`, three modes and
  the `"w"` trap, files-follow-the-shell / imports-follow-the-script,
  ONE join form (`Path(__file__).parent / name`). Everything else in `os`
  / `os.path` / `csv` / `json` is a reference roster.
- ⚠ **He right-sized CSV himself** (*"just a convention and good to
  know"*). Agree; do not drill the roster.
- ⚠ **Substrate held:** `.split()` / `.strip()` checked against S7 notes
  before use; `__file__` (S45), `finally` (1.9), `try`/`except`, `for`,
  `int()` all prior. On credit: `Path` (class), `with` internals (dunder
  pair), `newline=""` (spelling only).
- ⚠ **New error shown and named by the mentor (never seen before):
  `FileNotFoundError`.** Now fair to ask.
- ⚠ **`LookupError` defined in one line** (parent of `KeyError` and
  `IndexError`) after pushback 97. Row [~] due 14 Sep.
- ⚠ **`pdb` NOT taught — 1.11 is taught-complete without it.** Owed.
- ⚠ **`os.path.expanduser` named, not shown.** `~` not expanded (S43).
- ⚠ **VERIFY EVERY SNIPPET BY RUNNING IT BEFORE POSING IT.** Held S47.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()`
  vs `+`.
- ⚠ **`[i for i in config]` is just `list(config)`** — still not said.
- ⚠ **DEAD CODE** — three instances; full treatment still parked.
- Governance/format requests mid-session → PARK, close material, write at
  end.
- **Mentor demos, re-runnable:** `teaching/s47_files/` (27 files: `limits.txt`,
  `read_it.py`, `read_twice.py`, `read_lines.py`, `loop_lines.py`,
  `write_it.py`, `append_it.py`, `no_close.py`, `safe_close.py`,
  `skip_close.py`, `with_it.py`, `with_err.py`, `read_anywhere.py`,
  `os_form.py`, `joints.csv`, `read_csv.py`, `write_csv.py`, `config.json`,
  `read_json.py`, `write_json.py`, plus the `.txt`/`.csv`/`.json` outputs
  they wrote). ⚠ `read_it.py` must be run FROM `teaching/s47_files/`;
  `read_anywhere.py` and `os_form.py` run from anywhere — that contrast
  is the demo. Earlier: `teaching/s46_*`, `s45_*`, `s43_packages/`.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**161 rows, 101 [x], 60 [~], 115 overdue.** Do not re-create the table here.
`python3 tools/retest.py --overdue --all` at the open.
**S47: 4 rows fired.** `slicing / SHALLOW COPY` PASS 6 (stays [x], due
16 Sep); `UnboundLocalError` PASS 7 ([~] → [x], due 16 Sep, label leaked);
`None / is None / vs 0 / False` PASS 7 ([~] → [x], due 16 Sep); `augmented
assignment += on a MUTABLE type` NEW ROW, FAIL 7, [~] due 13 Sep. Eleven
1.11 rows added, all [~] due 14 Sep: `open() returns a FILE OBJECT with a
CURSOR`; `read() vs readline() vs for line in f`; `modes r / w / a`;
`write buffer / close flushes`; `with open(...) as f / context manager`;
`cwd vs script folder: open() vs import`; `pathlib.Path / os.path`;
`FileNotFoundError`; `csv.reader / csv.writer`; `json.load / json.dump`;
`LookupError`.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls | **[x] — re-test at the next build block (REAL LeRobot file)** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S42 re-taught; **S47 ask VOIDED (untaught `LookupError`), re-posed with `Exception`, unanswered — he stopped the volley** | **[~] — cold snippet ask, TAUGHT pair, OVERDUE (7 Sep)** |
| **1.9 `raise ... from` / bare `except` / ordering** | S42 taught | **[~] — OVERDUE (7 Sep)** |
| **`except ... as e` — what `e` IS** | S42 FAIL, substrate on credit | **[~] — printed-lines half due; object half waits for 1.12** |
| **MUTABLE DEFAULT + SENTINEL** | S42 FAIL 6, re-taught | **[~] — OVERDUE** |
| **CLOSURES — four layers** | S42 declared gap | **[~] at queue level — after he reads S19/S23** |
| **`.pyc` / compiled-then-interpreted** | S42 taught | **[~] — OVERDUE (7 Sep)** |
| **`sys.path`** | S43 taught; S46 walked BY HAND | **[~] — OVERDUE: "why does the import fail, two fixes"** |
| **PACKAGES** | S46 teach-back clean | **[~] — cold ask legal, task-first** |
| **RELATIVE vs ABSOLUTE IMPORTS** | S46 parked by him a second time | **[~] — cold ask, both halves; NO re-teaching** |
| **CIRCULAR IMPORTS** | S46 doubt gate "clear" | **[~] — cold ask legal** |
| **STDLIB / FRONT DOOR** | S46 finished | **[~] — cold ask legal from 12 Sep** |
| **PIP / SITE-PACKAGES / SHADOWING** | S46 taught | **[~] — cold ask legal from 12 Sep** |
| **BARE `*` / `enumerate()`** | S46 defined | **[~] — cold ask legal from 12 Sep** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | S43 taught | **[~] — legal** |
| **1.11 FILE HANDLING — all nine bullets** | **S47 taught-complete, 14 ideas, teach-backs clean; two model slips corrected (file-as-list, `"w"` as cursor-at-start)** | **[~] — drill + cold asks legal from 13 Sep; `pdb` still owed** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x] — legal** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x] — legal** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — OVERDUE** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | **S47: UBL deletion test PASS 7 (label leaked)** | **[x] — label re-check 16 Sep** |
| **THE MUTATING TELL** | S38 both halves | **[x] — OVERDUE** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | **S47: `[[0]*3]*3` PASS 6 after one narrowing question ("copies" → "references")** | **[x] — 16 Sep** |
| **`constructors`** | S38 7/10 | **[x] — OVERDUE** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, OVERDUE** |
| **1.9 `finally` guarantee** | S41: PASS 7; **S47 reused as the `close` argument, no ask** | **[x] — legal** |
| **`short-circuit`** | S41: PASS 7 | **[x] — legal** |
| **1.9 try/except** | S41 drill clean | **[x] — OVERDUE** |
| **RAISE-VS-SHRUG / `None` returns / expression-vs-statement** | S42: PASS 8 / 8 / 8; **S47 `is None` PASS 7** | **[x] — 16 Sep** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK still owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | **S47 FAIL 7 — modelled as a rebind; fact given with `id()`** | **[~] — 13 Sep, ask for the identity** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; S43 REPL defined | [~] **cold ask on both halves legal** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **DELIVERY, NOT RETENTION, WAS THE PROBLEM AGAIN (S43–S47).** S47:
  pushbacks 95 (label in header), 96 (asked instead of told after a
  fail), 97 (untaught name), 98 (PREDICT off-screen), 99 (file without
  walk). He was openly angry twice (96, 99) and right both times. Once
  each file was pasted AND walked line by line, every teach-back was
  clean. **Five sessions running. The watch is on the MENTOR.**
- ⚠⚠ **THE VOLLEY FIRED, THEN DIED ON MENTOR ERRORS.** Four asks landed;
  two were voided by construction faults; he stopped it. Build each ask
  clean before posing (grep the label, run the snippet, no name in the
  header) or the volley will die again.
- ⚠⚠ **HE NAMES HIS OWN LIMIT AND PARKS** — relative/absolute (S46);
  *"how am I supposed to remember so many Exceptions"* (S47, answered:
  the rule, not the roster). Honour it.
- ⚠⚠ **HE ASKS THE GOOD QUESTION HIMSELF (S47):** *"why would f.close ever
  fail?"* — produced `skip_close.py`, the best demo of the session;
  *"are we not going to learn os?"*; *"do I need to remember this
  syntax?"*. Each one produced a demo or a right-sizing.
- ⚠ **HE NAMES A GAP INSTEAD OF GUESSING** — *"I don't know what to say
  here"* on `LookupError`. Never log a named gap as anything but a gap.
- ⚠ **CONFIDENCE CALIBRATION, S47:** 6 on shallow copy (honest, matched
  the wobble); 7 on UBL and `is None` (right); **7 on `+=` (WRONG —
  over-rated a rebind model he was sure of).** A 7 on a mechanism he has
  never had corrected is not reliable. ≤5 is still the targeting signal.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE.** Unchanged;
  `skip_close.py` + `f.closed` was the traceback-shaped proof he needed.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL:** `len()`, `range()`,
  `.append()` vs `+`.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 99 raised, 97 upheld or
  part-upheld.** S47: 95, 96, 97, 98, 99 all upheld.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ✅ **`os.path` — SHOWN S47** (`getcwd`, `abspath`, `dirname`, `join`).
  ✅ **`pathlib.Path` — SHOWN S47** (`.parent`, `/`). ✅ **`with` — S47.**
  ✅ **`__file__` as a path anchor — S47.**
- ⚠ **`pdb` / breakpoint debugging — RULED S40 → 1.11. NOT YET TAUGHT.**
- ⚠ **`os.path.expanduser`** — named S47, not shown. `~` not expanded.
- ⚠ **`with` internals (`__enter__`/`__exit__`)** — on credit → 1.12.
- ⚠ **`Path` is a class** — on credit → 1.12.
- ⚠ **`newline=""`** — given as spelling; the line-ending reason (text
  mode translation) not taught. One line owed.
- ⚠ **binary mode `"rb"`/`"wb"`, encoding** — not mentioned. Bytes vs
  str is 1.13-adjacent; say one line when a `.parquet` or image comes up.
- ⚠ **`csv.DictReader`** — not shown; the LeRobot block may want it.
- ⚠ **`json.loads`/`dumps` (string form)** — `loads` seen in the S46
  shadowing demo, never defined. One line owed.
- ⚠ **Two module objects for one file** — stated S45, not demonstrated.
- ⚠ **`..` (two dots, parent package)** — one line said S44, never shown.
- ⚠ **`python3 -m`** — never shown. Do not use in a demo until defined.
- ⚠ **`import *`** — untaught (`bisect.py` lines 111–114).
- ⚠ **`pip install -e .` / editable installs** — owed at the LeRobot block.
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **`class` — STILL ON CREDIT.** 1.12 opens with the exception classes.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — with
  `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances)**; **`__dict__`** (1.12–1.13); **PEP 709**
  (1.13); `nonlocal` (1.13); `pop` internals (1.13); `copy.copy()` one line;
  deepcopy on self-reference (1.13); bytecode constants + `dis` (1.13);
  **HASH RANDOMISATION** (1.13); **`%` and `.format()`** as a reading skill;
  `!r` in an f-string; `capsys` — not Layer 0.

---
