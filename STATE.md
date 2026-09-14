# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 50 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S49**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S49.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING.**
#   4. ⚠⚠ **REVISION IS HIS CALL (ruled S48, restated S49 open).** He has an
#      oral revision agent on `notes/units/`. **NO VOLLEY, NO COLD ASKS, NO
#      `retest.py` AT THE OPEN unless he asks.** Do not push back; do not
#      count overdue rows at him. [x] stays at 101 until he calls a volley.
#   5. ⚠ **THE PARKED RULE IS CLOSED FOR ASKING.** Asked S48 and S49, no
#      ruling either time. It stays parked. **DO NOT ASK AGAIN.** Apply it
#      as practice; adopt only if HE raises it.
#   6. ⚠⚠⚠ **THE FIRST TEACHING MOVE OF S50 IS A RE-ISSUE: paste
#      `teaching/s49_oop/from_dict.py` in full, frame, walk, THEN the held
#      [PREDICT] (`print(Joint.from_dict)`).** He stopped tired the moment
#      it went out. His words: *"I will start from class method again
#      tomorrow."* Not confirmed read.
#   7. ⚠⚠ **NOTHING DELIVERED AFTER HIS LAST REPLY IS TAUGHT UNTIL HE
#      REPLIES TO IT.** Twice now (S48 `class_attr.py`, S49 `from_dict.py`).
#   8. ⚠⚠ **ONE IDEA PER TURN, PASTE THEN WALK THEN ASK. FILES BY PATH WITH
#      CODE, COMMAND, OUTPUT.** Held S48–S49, zero pushbacks in both.
#   9. ⚠⚠ **A FACT HE DOES NOT HAVE CANNOT BE ASKED OUT OF HIM.** On a miss
#      he can reason to, ONE pointer (S49 `vars(a)` worked); on a named gap,
#      run the fact.
#  10. ⚠ **[PREDICT] ONLY FROM THE SCREEN. NO ERROR NAME IN A HEADER. NO
#      UNSEEN NAME IN AN ASK. HE NAMES THE ERROR BEFORE THE TRACEBACK.**
#  11. ⚠ **PYTEST IS NOT TAUGHT; the mentor writes and runs every test.
#      CHECK mtime BEFORE READING HIS FILE.**
#  12. ⚠⚠⚠ **WHEN HE SAYS STOP, THE CLOSE IS WRITTEN IN THAT TURN.** Held.
#  13. ⚠ **ON CREDIT:** `except ... as e` (object half) → pay at
#      inheritance; `with` = `__enter__`/`__exit__` (dunders, now sayable);
#      `@` decorator = spelling only until 1.13.
#
# STATE AS OF: end of Session 49, **Mon 14 Sep 2026, ~21:00** (`date` at
# open 20:47). One short block, ~15 min, ended by him: *"I am feeling too
# much tired today lets close this session today here itself."*
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.**
  Tell him the number if he asks; do not soften it.
- **S49 yield (~15 min):** class attributes re-issued and read (→ [~]);
  `__repr__` + "dunder" taught (→ [~]); class methods delivered, not
  confirmed. ~0.15 unit-equivalent. Zero pushbacks. Zero cold asks.
- **Position: 1.1–1.8 closed. 1.9, 1.10, 1.11 taught-complete, cold asks
  on HIS call. 1.12 — six bullets [~] (Why, Classes/instances, `__init__`,
  Methods [instance full, class half unconfirmed], Instance vs class
  attributes, Dunder [repr only]); seven [ ] (static half, Inheritance,
  Overriding, `super()`, Encapsulation, Polymorphism, Composition,
  Dataclasses).**
- ✅ **DECIDED S42:** weekly cold build block → a REAL LeRobot file
  (`Episode`/`JointLimits` class reading `meta/info.json`). Place it when
  1.12 has `__repr__` (done) and inheritance.
- **RULED S40: `pdb` → 1.11.** Still owed. Not blocking.
- Current Layer: 1. Current Topic: **1.12 OOP, continuing.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **PARKED S47 (mentor-proposed): "AFTER A FAILED [RECALL], THE MISSING
  FACT IS GIVEN, NOT ASKED FOR."** Asked S48 and S49, unruled both times.
  **CLOSED FOR ASKING.** Applied as practice. RULES stays **v6**.

## WHERE WE LEFT OFF

### SESSION 50 STARTS HERE — exact resume point

1. **INTERVAL GATE from `date` + `git log -1` + mtimes.** S49 closed Mon
   14 Sep ~21:00. S49 material (shadowing, `__repr__`) legal from **Tue 15
   Sep evening**. S48 and older legal now. State it; no volley.

2. ⚠⚠⚠ **RE-ISSUE `teaching/s49_oop/from_dict.py` IN FULL.** Frame (a
   second door in; runs before any object exists so it gets the class, not
   `self`; honest: today only tidiness, payoff at inheritance). Paste code,
   command, output. Five-point walk: the call is on the CLASS; `cls` = the
   thing left of the dot, as `self` was; `cls(...)` is the type call under
   another name; `@classmethod` = spelling only ("a line starting with `@`
   above a `def` changes how the `def` is stored"); `a.move` is the S48
   bound method. Then the held **[PREDICT]**: `print(Joint.from_dict)` →
   `<bound method Joint.from_dict of <class '__main__.Joint'>>` — a bound
   method holding the CLASS. Run-verify before posing. Accept the mechanism
   ("bound to Joint") over the exact format.

3. **`@staticmethod` — one line plus a tiny file** (`static.py`:
   `deg_to_rad(deg)` with no `self`/`cls`, called as `Joint.deg_to_rad(90)`
   and as `a.deg_to_rad(90)`, both work). That completes the Methods
   bullet at [~].

4. **THEN, one file per idea, frame each, doubt gate between:**
   - **Inheritance + overriding + `super()`** — open from what he owns:
     `class OverLimit(Exception): pass` (S36) and the 1.9 tree. `class
     Servo(Joint)`; lookup becomes object dict → `Servo` dict → `Joint`
     dict (extend the two-dict model to a chain; name MRO in one line
     only). Override `describe`; `super().__init__(...)`. **This is where
     `from_dict` pays off: `Servo.from_dict(d)` builds a `Servo` because
     `cls` is `Servo`.** Show it. **PAY `except ... as e`:** `e` is an
     instance of the exception class; `vars(e)`, `e.args`. `isinstance`
     may be defined here (untaught until then — do not use it earlier).
   - Encapsulation (`_name` convention, one line; property maybe),
     polymorphism (two classes, one loop calling `.describe()`),
     composition (`Arm` HAS a list of `Joint`), dataclasses intro.
   - **A drill after inheritance** (spec before puzzle; boundary in the
     tests; done line; red = "find it"). Check the S48 style note
     (`return cond`) and the word "return" in the spec.

5. **THEN the LeRobot block** (S42 decision, six sessions unplaced).

6. **REVISION / VOLLEY — ONLY WHEN HE ASKS.** Then: `python3
   tools/retest.py --overdue --all`, oldest first, task-first, grep every
   label, run every snippet, no name in the header. First: the two S47
   asks that never landed (hierarchy direction with `Exception`/`KeyError`;
   `+=` with an alias, ask for the identity), then the S48 [PREDICT]
   misses as cold asks (`print(Joint())`; missing `__init__` arg →
   `TypeError`).

7. ⚠ **`*args`/`**kwargs` revision (S44 ask)** — his call; do not raise.

**Standing turn rules: RULING ONCE; NO VOLLEY UNASKED; FRAME FIRST (honest,
say what is cheap); physical-first; PASTE THEN WALK THEN ASK; AFTER A FAIL
OR A NAMED GAP GIVE THE FACT BY RUNNING IT (one pointer first if he has the
pieces); [PREDICT] ONLY FROM THE SCREEN; NO ERROR NAME IN A HEADER; NO
UNSEEN NAME IN AN ASK; HE NAMES THE ERROR BEFORE THE TRACEBACK; ANSWER A
DIRECT QUESTION DIRECTLY THEN PROVE IT; FILES BY PATH WITH CODE, COMMAND
AND OUTPUT; NO `-c`; NO SHELL PIPES HE HAS NOT BEEN GIVEN; SPEC BEFORE
PUZZLE; ONE IDEA PER TURN; DONE LINE BEFORE PYTEST; RED COMES BACK AS "FIND
IT"; doubt gate before every new idea; tag every block. Do not propose
ending the session. WHEN HE SAYS STOP, WRITE THE CLOSE IN THAT TURN. NEVER
EDIT HIS DRILL FILE. NEVER OVERWRITE UNSEEN.**

**CARRY FORWARD:**
- ⚠ **S49 [PREDICT] slip:** `vars(a)` after `a.unit = "rad"` answered as
  the class dict. His lines 1–2 (`rad`, `deg`) already required the object
  dict to hold the write; one pointer fixed it. Classified: which-dict
  slip, not a model gap. Not logged. Cold ask (his call): "after
  `a.unit = 'rad'`, what changed in `vars(Joint)`?" — expected: nothing.
- ⚠ **`__repr__` must RETURN.** Same family as the S36/S48 print-where-
  return bug. Watch for `print` inside `__repr__` in the next drill.
- ⚠⚠ **THE DONE LINE MISSED THE BUG (0 for 3).** Hold the gate for it; ask
  WHICH CASE breaks it, not which function felt biggest.
- ⚠ **Style, given once S48:** `if cond: return True else: return False`
  → `return cond`. Check in the next drill, do not re-teach.
- ⚠ **Two S48 [PREDICT] misses, not logged:** `print(Joint())`;
  `Joint("elbow")` missing arg → `TypeError` (wrong CALL at the
  parentheses vs wrong DOT READ at the dot). Cold asks on his volley.
- ⚠ **Language precision given S48:** "constructor" = the type call;
  `__init__` = initialiser.
- ⚠ **`pdb` NOT taught** (owed, 1.11). `os.path.expanduser`, `newline=""`
  reason, `json.loads` one line — owed.
- ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
  **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
  `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half. All wait on
  his volley call.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()`
  vs `+`.
- **Mentor demos, re-runnable (run from inside the folder):**
  `teaching/s49_oop/`: `shadow.py`, `no_repr.py`, `with_repr.py`,
  `from_dict.py` (UNCONFIRMED). `teaching/s48_oop/` (11 files; `attach.py`,
  `init_short.py`, `by_hand.py` raise on purpose). Earlier: `s47_files/`,
  `s46_*`, `s45_*`, `s43_packages/`.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**169 rows, 101 [x], 68 [~].** Do not re-create the table here. **S49: 0
rows fired.** Two rows added, [~] due 16 Sep: `class attribute vs instance
attribute (two dicts)`; `__repr__ / what a dunder is`. The six S48 rows are
due 15 Sep. Class-method row NOT added until the re-issue is confirmed.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41 zero catch-alls; S48 drill 10/10 | **[x] — re-test at the LeRobot block** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S47 ask voided, re-posed, unanswered | **[~] — cold ask, TAUGHT pair, his call** |
| **1.9 `raise ... from` / bare `except` / ordering** | S42 taught | **[~] — overdue, his call** |
| **`except ... as e` — what `e` IS** | S42 FAIL | **[~] — PAY IN 1.12 at inheritance** |
| **MUTABLE DEFAULT + SENTINEL** | S42 FAIL 6, re-taught | **[~] — overdue, his call** |
| **CLOSURES — four layers** | S42 declared gap | **[~] — after he reads S19/S23** |
| **`.pyc` / compiled-then-interpreted** | S42 taught | **[~] — overdue** |
| **`sys.path`** | S46 walked by hand | **[~] — cold ask, his call** |
| **PACKAGES / RELATIVE vs ABSOLUTE / CIRCULAR / STDLIB / PIP** | S43–S46 taught | **[~] — cold asks legal, his call** |
| **BARE `*` / `enumerate()`** | S46 defined | **[~] — legal** |
| **POSITIONAL vs KEYWORD ORDER + DOUBLE-FILL** | S43 taught | **[~] — legal** |
| **1.11 FILE HANDLING — all nine bullets** | S47 taught-complete | **[~] — drill + cold asks legal; `pdb` owed** |
| **1.12 class / instance / `__init__` / instance methods** | S48 taught + drill 10/10 | **[~] — cold ask legal now; evidence `drills/s48_joint.py`** |
| **1.12 instance vs class attributes** | **S49 re-issued, [PREDICT] 2/3 then right** | **[~] — cold ask legal 15 Sep evening** |
| **1.12 `__repr__` / dunder** | **S49 taught, list [PREDICT] right** | **[~] — cold ask legal 15 Sep evening** |
| **1.12 class methods** | **S49 delivered, UNCONFIRMED** | **[ ] — re-issue first thing S50** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x]** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x]** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — overdue** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S47 UBL PASS 7 (label leaked) | **[x] — label re-check 16 Sep** |
| **THE MUTATING TELL** | S38 both halves | **[x] — overdue** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — overdue** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | S47 PASS 6 | **[x] — 16 Sep** |
| **`constructors`** | S38 7/10; S48 precision given | **[x] — overdue** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, overdue** |
| **1.9 `finally` guarantee** | S41 PASS 7 | **[x]** |
| **`short-circuit`** | S41: PASS 7 | **[x]** |
| **1.9 try/except** | S41 drill clean | **[x] — overdue** |
| **RAISE-VS-SHRUG / `None` returns / print-vs-return** | S42 PASS 8/8/8; S47 PASS 7; S48 drill REPEAT (print for return) | **[x] at queue level — watch the next drill and `__repr__`** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S47 FAIL 7 | **[~] — ask for the identity, his call** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; S43 REPL defined | [~] cold ask, both halves |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ✅ **DELIVERY HELD TWO SESSIONS (S48, S49): zero pushbacks.** Every idea
  as a file with path, code, command, output, numbered walk; every gap by
  running the fact; direct questions answered first. **Keep this shape.**
- ⚠⚠ **HE STOPS WHEN HE DECIDES TO STOP — and the last thing sent is
  unread.** S48 `class_attr.py`, S49 `from_dict.py`. Re-issue, do not
  assume. Nothing delivered is taught until he replies to it.
- ⚠ **SHORT SESSIONS HAPPEN.** S49 was ~15 min on a tired evening. Do not
  comment on length; the close is the same size regardless.
- ⚠⚠ **REVISION IS HIS CALL.** Do not open with the volley, do not count
  overdue rows at him, do not raise the cost. He knows it.
- ⚠ **HE REASONS FROM THE MODEL WHEN GIVEN ONE.** S49: shadowing predicted
  right from the two-dict model; the list-`__repr__` predicted right from
  "Python calls it whenever it needs the text". One pointer on a slip is
  enough when the pieces are on his screen.
- ⚠ **THE DONE LINE IS NOT YET PREDICTIVE (0 for 3).** Keep holding the
  gate; it is his rule.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK** (S48: fixed `describe` from `None`
  + captured stdout, no hint).
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 99 raised, 97 upheld or
  part-upheld.** S49: none raised.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ⚠ **`pdb` / breakpoint debugging — RULED S40 → 1.11. NOT YET TAUGHT.**
- ⚠ **`__slots__`** — one line S48, parked → 1.13.
- ⚠ **Refcount / two unbound `Joint()` at the same address** — never shown;
  GC, 1.13.
- ✅ **`__repr__` / `__str__`** — PAID S49. `!r` in an f-string still
  unshown (the repr used explicit quotes instead).
- ⚠ **`@` decorator mechanism** — spelling given S49; mechanism 1.13.
- ⚠ **`@staticmethod`** — owed, one line, S50.
- ⚠ **`with` internals (`__enter__`/`__exit__`)** — dunders now defined;
  one line when `with` recurs.
- ⚠ **`Path` is a class** — one line when `pathlib` recurs.
- ⚠ **`isinstance`** — untaught; define at inheritance, not before.
- ⚠ **`os.path.expanduser`**, **`newline=""` reason**, **binary mode /
  encoding**, **`csv.DictReader`**, **`json.loads`/`dumps`**, **two module
  objects for one file**, **`..` parent package**, **`python3 -m`**,
  **`import *`**, **`pip install -e .`** — all still owed, unchanged.
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — with
  `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances)**; **`__dict__`** shown via `vars()`,
  direct `a.__dict__` not yet written; **PEP 709** (1.13); `nonlocal`
  (1.13); `pop` internals (1.13); `copy.copy()` one line; deepcopy on
  self-reference (1.13); bytecode constants + `dis` (1.13); **HASH
  RANDOMISATION** (1.13); **`%` and `.format()`** as a reading skill;
  `capsys` — not Layer 0.

---
