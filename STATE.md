# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 49 (for Claude):
#   1. Read RULES.md fully (**v6, unchanged — no rule adopted in S48**), then
#      this file fully. No re-introductions.
#   2. FIRST ACTION: the INTERVAL GATE — **VERIFY THE DATE FROM `date`,
#      `git log -1` AND FILE MTIMES, NOT FROM THE CONTEXT HEADER AND NOT BY
#      ASKING HIM.** Held S36–S48 at the open.
#   3. ⚠⚠ **VERIFY ANY WARNING IN THIS FILE AGAINST THE REPO BEFORE ACTING ON
#      IT.** This file can be wrong; the repo cannot.
#   4. ⚠⚠ **REVISION IS HIS CALL (ruled S48 open).** He has an oral revision
#      agent working from `notes/units/`. **NO VOLLEY, NO COLD ASKS, NO
#      `retest.py` AT THE OPEN unless he asks.** Sessions go forward on
#      content. Do not push back on this; he asked for none. Consequence,
#      stated once and not repeated: [~] → [x] cannot move until he asks
#      for a volley, so [x] stays at 101.
#   5. ⚠⚠ **ONE RULE CANDIDATE IS STILL PARKED (see RULE-CHANGE PARKING).
#      Asked at the S48 open; his reply "everything is clear" answered the
#      doubt gate, not the ruling. Ask ONCE more, one line, then drop it if
#      unanswered.**
#   6. ⚠⚠⚠ **THE FIRST TEACHING MOVE OF S49 IS A RE-ISSUE: paste
#      `teaching/s48_oop/class_attr.py` in full, walk it line by line, THEN
#      the held [PREDICT] (`a.unit = "rad"` → `a.unit`, `b.unit`, `vars(a)`).**
#      He stopped S48 saying *"I have not read any of what you have given
#      above after my answer"*. The file exists; it is NOT taught. The
#      curriculum bullet is still [ ].
#   7. ⚠ **PYTEST IS NOT TAUGHT. THE MENTOR WRITES AND RUNS EVERY TEST FILE.**
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held S48.
#   9. ⚠⚠ **ONE IDEA PER TURN, PASTE THEN WALK THEN ASK.** Held S48 for all
#      eleven files; zero pushbacks. Keep the shape exactly.
#  10. ⚠⚠⚠ **A FACT HE DOES NOT HAVE CANNOT BE ASKED OUT OF HIM.** Held S48
#      three times ("I am not sure", a wrong [PREDICT], "I don't know how
#      python decides that") — each time the fact was run, not re-asked.
#  11. ⚠⚠ **[PREDICT] ONLY FROM WHAT IS ON SCREEN. NO ERROR NAME IN A
#      HEADER. NO UNSEEN NAME IN AN ASK.** Held S48.
#  12. ⚠⚠ **FILES YOU CREATE: SAY SO, LIST THE PATHS, PASTE EACH FILE'S CODE
#      UNDER ITS PATH, SHOW THE COMMAND, SHOW THE OUTPUT.** Held S48.
#  13. ⚠⚠ **S27 RULE: HE NAMES THE ERROR BEFORE THE TRACEBACK IS SHOWN.**
#      Held S48 (`AttributeError` on `b.angle`, named with mechanism).
#  14. ⚠⚠ **WHEN HE ASKS A DIRECT QUESTION, ANSWER IT, THEN PROVE IT WITH A
#      FILE.** Held S48 (`a = list(); a.name = ...` → `no_dict.py`; "what
#      does `Joint(...)` return" → `by_hand.py`).
#  15. ⚠⚠⚠ **WHEN HE SAYS STOP, THE CLOSE IS WRITTEN IN THAT TURN.** Held S48.
#  16. ⚠ **ON CREDIT:** `except ... as e` (object half) → pay it in 1.12
#      when inheritance/exception classes come; `Path` is a class (now
#      sayable); `with` = `__enter__`/`__exit__` (dunders, later in 1.12).
#
# STATE AS OF: end of Session 48, **Sun 13 Sep 2026, ~21:50** (`date` at his
# close request 21:48). One block: **Sun 13 Sep 17:43 → 21:48** (demo
# files `teaching/s48_oop/` written in sequence; drill saved 21:28 and
# 21:35). He asked: *"can you save the session now and again give me full
# explanation when we start next."*
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ⚠⚠ **RE-BASELINE (S41 gauntlet):
  observed ~0.8 subsection-equivalents/week; DERIVED CLOSE ≈ 22 OCT 2026.
  The 30 Sep gate is missed at the observed rate. Nothing de-scoped.** Tell
  him the number if he asks; do not soften it.
- **S48 yield (~4h):** **1.12 OOP OPENED** with the frame and taught
  through `class` / instances / attributes / `__dict__` / `__init__` /
  methods / bound methods; eleven files in `teaching/s48_oop/`; **first
  student drill since S41 (`drills/s48_joint.py`, 10/10 after one red)**.
  ~0.4 unit-equivalent. Zero pushbacks. Zero cold asks (by his ruling).
- **Position: 1.1–1.8 closed. 1.9, 1.10, 1.11 all taught-complete, cold
  asks waiting on HIS call. 1.12 — four bullets [~] (three full, one half),
  nine [ ].**
- ✅ **DECIDED S42:** the weekly cold build block moves to a **REAL LeRobot
  file**. Still not placed. Now 1.12 gives it a better shape (a `Episode`
  or `JointLimits` class reading `meta/info.json`). Place it when 1.12 has
  `__repr__` and inheritance.
- **RULED S40: `pdb` → 1.11.** Still owed. Not blocking.
- Current Layer: 1. Current Topic: **1.12 OOP, continuing.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- **PARKED S47 (mentor-proposed, from pushback 96): "AFTER A FAILED
  [RECALL], THE MISSING FACT IS GIVEN, NOT ASKED FOR."** Asked at the S48
  open; no ruling given (his reply addressed the doubt gate). **S48 note:
  the mentor applied it anyway three times and it worked.** Ask once more
  at the S49 open, one line; if no ruling, leave it parked and stop asking.
  RULES stays at **v6**.

## WHERE WE LEFT OFF

### SESSION 49 STARTS HERE — exact resume point

1. **INTERVAL GATE from `date` + `git log -1` + mtimes.** S48 closed Sun
   13 Sep ~21:50. 1.12 material taught in S48 is legal from **14 Sep
   evening or later** (say the hours). Everything older is legal now. State
   it; do not run a volley.

2. **THE PARKED RULE — one line, once.**

3. ⚠⚠⚠ **RE-ISSUE `teaching/s48_oop/class_attr.py` IN FULL.** He did not
   read it. Paste the code under its path, the command, the output, and
   the six-point walk (assignment in the class block → class dict; object
   dicts have no `unit`; `"unit" in vars(Joint)`; `"__init__" in
   vars(Joint)` — methods ARE class attributes; the two-dict order). Then
   the held **[PREDICT]**: add `a.unit = "rad"`, print `a.unit`, `b.unit`,
   `vars(a)` → expected `rad`, `deg`, `{'name': 'elbow', 'angle': 10,
   'unit': 'rad'}` (run-verified in scratch before posing; it shadows on
   the object, the class copy is untouched). That closes **Instance vs
   class attributes** to [~].

4. **THEN, in this order, one file per idea, frame each:**
   - **`__repr__`** — pays the S48 promise (*"the line that replaces
     `<__main__.Joint object at 0x...>` with something readable"*). Show
     `print(a)` before and after. `__str__` one line after. This is the
     first DUNDER; define "dunder" here (double-underscore, a name Python
     looks for), tying back to `__init__`, `__file__`, `__name__`,
     `__dict__`, `__main__` — all already seen.
   - **Class methods / static methods** — the other half of the Methods
     bullet. Right-size: instance methods are load-bearing; `@classmethod`
     for alternate constructors (`Joint.from_dict(d)`, which the LeRobot
     block will want); `@staticmethod` one line. ⚠ **`@` decorator syntax
     is UNTAUGHT** — give it as spelling only ("this line above a def
     changes how the def is stored"), full decorators are 1.13/closures.
   - **Inheritance + overriding + `super()`** — open from what he owns:
     `class OverLimit(Exception): pass` (S36) and the 1.9 tree. `class
     Servo(Joint)`; lookup order becomes object dict → `Servo` dict →
     `Joint` dict (extend the two-dict model to a chain — do not name MRO
     beyond one line). **PAY `except ... as e`: `e` is an instance of the
     exception class, `vars(e)`/`e.args`.**
   - Encapsulation (`_name` convention, one line; properties maybe),
     polymorphism (one file: two classes, one loop calling `.describe()`),
     composition vs inheritance (`Arm` HAS joints, a list of `Joint`),
     dataclasses intro.

5. **THEN the LeRobot block** (S42 decision, five sessions unplaced).

6. **REVISION / VOLLEY — ONLY WHEN HE ASKS.** When he does: `python3
   tools/retest.py --overdue --all`, oldest first, task-first, grep every
   label, run every snippet, no name in the header. The two S47 asks that
   never landed (hierarchy direction with `Exception`/`KeyError`; `+=` with
   an alias, ask for the identity) go first.

7. ⚠ **HE ASKED TO REVISE `*args`/`**kwargs`** (S44) — his call now; do not
   raise it unless he does.

**Standing turn rules: RULING ONCE; NO VOLLEY UNASKED; FRAME FIRST; physical-
first; PASTE THEN WALK THEN ASK; AFTER A FAIL OR A NAMED GAP GIVE THE FACT
BY RUNNING IT; [PREDICT] ONLY FROM THE SCREEN; NO ERROR NAME IN A HEADER; NO
UNSEEN NAME IN AN ASK; HE NAMES THE ERROR BEFORE THE TRACEBACK; ANSWER A
DIRECT QUESTION DIRECTLY THEN PROVE IT; FILES BY PATH WITH CODE, COMMAND
AND OUTPUT; NO `-c`; NO SHELL PIPES HE HAS NOT BEEN GIVEN; SPEC BEFORE
PUZZLE; ONE IDEA PER TURN; DONE LINE BEFORE PYTEST; RED COMES BACK AS "FIND
IT"; doubt gate before every new idea; tag every block. Do not propose
ending the session. WHEN HE SAYS STOP, WRITE THE CLOSE IN THAT TURN. NEVER
EDIT HIS DRILL FILE. NEVER OVERWRITE UNSEEN.**

**CARRY FORWARD:**
- ⚠⚠ **THE DONE LINE MISSED THE BUG (third data point).** He named
  `is_safe` (*"its language was not clear to me"*); `is_safe` was 4/4
  including the boundary. The red was `describe`: **`print` where the spec
  said `return`.** Same S36 principle (a function that prints decides its
  caller's output policy) — this is a REPEAT of a known shape, not a
  knowledge gap. Classified: spec-reading slip. Watch: does he read the
  word "return" in a constraint.
- ⚠ **Style, given once:** `if cond: return True / else: return False` →
  `return cond`. Same family as `if flag == False` (S17). Do not re-teach;
  check it in the next drill.
- ⚠ **`abs()` used unprompted** in `is_safe` (`-abs(self.limit)`). Seen in
  S23/S28/S31 notes; legal. Not needed — the spec had no negative limits.
- ⚠ **Two [PREDICT] misses, not logged:** `print(Joint())` ("not sure");
  `Joint("elbow")` with a missing arg → he said `AttributeError`, it is
  `TypeError`. Discriminator given: **wrong CALL = `TypeError` at the
  parentheses; wrong DOT READ = `AttributeError` at the dot.** Queue row
  added. Cold ask when he opens a volley.
- ⚠ **Named gap, given by running:** *"I don't know how python decides
  that"* (what fills `self`) → `bound.py`: the object left of the dot;
  `a.move` is a bound method holding `a`; `Joint.move` is a plain
  function. His teach-back after: *"the method stays with the class, and
  applies to whatever object it is called for."* Sharpened to
  `vars(self)`.
- ⚠ **His good question of the session:** *"can we do `a = list();
  a.name = 'ankur'`? if not why?"* → `no_dict.py`: built-ins carry no
  `__dict__` (`AttributeError` on attach, `TypeError` from `vars()`);
  functions and modules do. Reason given at Level 2: fixed C layout,
  memory and speed. `__slots__` parked as one line for 1.13.
- ⚠ **His second good question:** *"what is `Joint('elbow', 10)`
  returning ... `Joint(a, 'elbow', 10)` should also work?"* → `by_hand.py`:
  the TYPE call makes, fills via `__init__`, returns the object;
  `__init__` returns `None` (thrown away); `Joint.__init__(a, ...)` is the
  legal by-hand form; `Joint(a, "elbow", 10)` → `TypeError` 4 vs 3.
- ⚠ **Language precision, given:** "constructor" in this course = the type
  call (`list()`, `Joint()`); `__init__` is the INITIALISER, it fills an
  object that already exists. He said "constructor" for `__init__`
  unprompted; corrected once.
- ⚠ **Teach-backs clean:** frame (*"tight organisation and a separate
  datatype ... built on usual things we already use"* — right, the usual
  thing is a dict); `a.angle` vs `vars(a)`; `self` in `move`.
- ⚠ **Same address printed twice** when `print(Joint()); print(Joint())`
  ran unbound (refcount freed the first). Mentor rewrote with names
  before showing; the artefact was never on his screen. Do not pose it.
- ⚠ **`pdb` NOT taught.** Owed inside 1.11. `os.path.expanduser` named,
  not shown. `newline=""` reason owed. `json.loads` one line owed.
- ⚠ **STILL NEVER ASKED:** `sum()`, `when NOT to use a comprehension`.
  **STILL OWED:** `DRY`, `mutate-while-iterating`, `list method roster`,
  `HOW FAR DID PYTHON GET?`, `del` as a statement, REPL half. All wait on
  his volley call.
- ⚠ **Level-1 audit list:** `len()`, `range()` as an object, `.append()`
  vs `+`.
- **Mentor demos, re-runnable:** `teaching/s48_oop/` (11 files, run from
  inside the folder): `make_one.py`, `print_one.py`, `attach.py` (raises
  on line 14), `look_inside.py`, `no_dict.py`, `init.py`, `init_short.py`
  (raises), `by_hand.py` (raises on line 13), `method.py`, `bound.py`,
  `class_attr.py` (UNREAD). Earlier: `teaching/s47_files/`, `s46_*`,
  `s45_*`, `s43_packages/`.

## TERM RE-TEST QUEUE — lives in `tools/queue.json`, driven by `tools/retest.py`.
**167 rows, 101 [x], 66 [~], overdue count not run (his ruling).** Do not
re-create the table here. **S48: 0 rows fired.** Six 1.12 rows added, all
[~] due 15 Sep: `class statement makes a TYPE / calling it makes an
object`; `attribute = a key in the object's __dict__ (vars)`; `built-ins
have no __dict__`; `__init__ vs the type call`; `self = the object left of
the dot / bound method`; `TypeError (wrong call) vs AttributeError (wrong
dot read)`.

## RE-TEST QUEUE — SUBSECTION LEVEL (kept here; too coarse for the script)

| Item | Latest result | Status / next due |
|---|---|---|
| **⚠⚠ THE CATCH-ALL / TRANSFER GAP** | S41: ZERO catch-alls; **S48 drill: 10/10, boundary right, no catch-alls needed** | **[x] — re-test at the LeRobot block** |
| **⚠⚠ 1.9 HIERARCHY DIRECTION** | S47 ask voided, re-posed, unanswered | **[~] — cold ask, TAUGHT pair, when he calls a volley** |
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
| **1.12 OOP — class / instance / `__init__` / instance methods** | **S48 taught + drill 10/10 same-session** | **[~] — cold ask legal 14 Sep evening; drill evidence `drills/s48_joint.py`** |
| **1.12 instance vs class attributes** | **S48 file delivered, UNREAD** | **[ ] — re-issue first thing S49** |
| **1.10 — taught half** | S41: 7/7 at 7 | **[x]** |
| **`.keys()` AS A VIEW** | S41: PASS 6 | **[x]** |
| **THE COMPILE/RUN SPLIT** | S41 7; S42 answered | **[x] — overdue** |
| **`while` mechanics; nested loops; found-flag** | S38 20/20; S42 8 | **[x] — 17 Sep** |
| **Frames / namespaces / execution pipeline** | S47 UBL PASS 7 (label leaked) | **[x] — label re-check 16 Sep** |
| **THE MUTATING TELL** | S38 both halves | **[x] — overdue** |
| **`sorted` / `key=` / `lambda` / `reversed()`** | S38 cold 8/10 | **[x] — 13 Sep** |
| **`zip` — both silent failures** | S42: PASS 8 / 8 | **[x] — 17 Sep** |
| **SHALLOW COPY / deepcopy / tuple slots** | S47 PASS 6 | **[x] — 16 Sep** |
| **`constructors`** | S38 7/10; **S48: "constructor" vs `__init__` precision given** | **[x] — overdue** |
| **`del` as a STATEMENT** | S38 taught | **[~] — cold ask, overdue** |
| **1.9 `finally` guarantee** | S41 PASS 7 | **[x]** |
| **`short-circuit`** | S41: PASS 7 | **[x]** |
| **1.9 try/except** | S41 drill clean | **[x] — overdue** |
| **RAISE-VS-SHRUG / `None` returns / print-vs-return** | S42 PASS 8/8/8; S47 `is None` PASS 7; **S48 drill: `print` where `return` was specified — a REPEAT** | **[x] at queue level — watch the next drill** |
| **DRY / one copy of a decision** | S41 holds structurally | **[~] — later-day ASK owed** |
| **AUGMENTED ASSIGNMENT `+=` vs `=`** | S47 FAIL 7 | **[~] — ask for the identity, his call** |
| **1.1–1.5 STRICT-LEGEND AUDIT** | S41: 11/12 | **DONE — next at the September gauntlet** |
| Frames / REPL vs script | S38 frames; S43 REPL defined | [~] cold ask, both halves |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ✅ **DELIVERY HELD FOR A WHOLE SESSION (S48).** Zero pushbacks in ~4h,
  eleven files, one drill. What worked: every idea as a file with path,
  code, command, output, and a numbered walk; every gap or miss answered
  by RUNNING the fact; direct questions answered in the first line. **Keep
  this shape. The S43–S47 run was a delivery problem and this is the fix.**
- ⚠⚠ **HE STOPS READING WHEN HE DECIDES TO STOP.** S48 close: *"I have
  not read any of what you have given above after my answer."* The
  class-attribute file went out after his teach-back and before he had
  said "clear" on the next idea. **Nothing delivered after a teach-back
  reply is taught until he has replied to it.** Re-issue, do not assume.
- ⚠⚠ **REVISION IS HIS CALL (S48 ruling).** Do not open with the volley,
  do not count overdue rows at him, do not raise the cost. He knows it.
- ⚠⚠ **HE ASKS THE GOOD QUESTION HIMSELF (S48, twice):** `list().name`,
  and "what does `Joint(...)` return / can I pass `a` myself". Both
  produced the two best files of the session. Answer, then prove.
- ⚠ **HE NAMES A GAP INSTEAD OF GUESSING** — *"I am not sure about this"*,
  *"I don't know how python decides that"*. Twice in S48. Honour it: the
  fact, physically, no second question.
- ⚠ **THE DONE LINE IS NOT YET PREDICTIVE (0 for 3 on naming the failing
  function).** Keep holding the gate for it; it is his rule.
- ⚠ **HE DEBUGS WELL WITH A TRACEBACK.** S48: given `None` + captured
  stdout, he fixed `describe` in one edit without a hint.
- ⚠ **CONFIDENCE CALIBRATION:** no ratings taken in S48 (no [RECALL]
  fired). Nothing new.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 99 raised, 97 upheld or
  part-upheld.** S48: none raised.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read; GIL (1.13);
  concurrency (post-Layer 1); GC (1.13)
- ⚠ **`pdb` / breakpoint debugging — RULED S40 → 1.11. NOT YET TAUGHT.**
- ⚠ **`__slots__`** — one line said S48 ("a class can opt out of the
  `__dict__` to be lean like a list"), parked → 1.13.
- ⚠ **Refcount / why two unbound `Joint()` print the same address** —
  never shown to him; GC, 1.13.
- ⚠ **`__repr__` / `__str__`** — PROMISED S48 ("the line that replaces the
  address form"). Next session, first new idea after the re-issue.
- ⚠ **`@` decorator spelling** — needed for `@classmethod`; spelling only
  in 1.12, mechanism with closures/1.13.
- ⚠ **`with` internals (`__enter__`/`__exit__`)** — dunders, later in 1.12.
- ⚠ **`Path` is a class** — now sayable; one line when `pathlib` recurs.
- ⚠ **`isinstance`** — untaught; do not use in a demo until defined
  (inheritance is the natural place).
- ⚠ **`os.path.expanduser`**, **`newline=""` reason**, **binary mode /
  encoding**, **`csv.DictReader`**, **`json.loads`/`dumps`**, **two module
  objects for one file**, **`..` parent package**, **`python3 -m`**,
  **`import *`**, **`pip install -e .`** — all still owed, unchanged.
- `__iter__`/`__next__` + generators — 1.13. Generator EXPRESSIONS unshown.
- ⚠ **A dict iterator refuses a resized dict (`RuntimeError`)** — with
  `mutate-while-iterating`.
- ⚠ **HASH COLLISIONS** — master L8. **`_` in the REPL** — one line, owed.
- ⚠ **DEAD CODE (three instances)**; **`__dict__`** — ✅ now SHOWN S48 via
  `vars()` and the `TypeError` message naming it; the name itself used
  once, direct `a.__dict__` not yet written; **PEP 709** (1.13);
  `nonlocal` (1.13); `pop` internals (1.13); `copy.copy()` one line;
  deepcopy on self-reference (1.13); bytecode constants + `dis` (1.13);
  **HASH RANDOMISATION** (1.13); **`%` and `.format()`** as a reading
  skill; `!r` in an f-string; `capsys` — not Layer 0.

---
