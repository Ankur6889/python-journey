# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 28 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. S27 ran Sat 22 Aug 2026 (morning).
#      ⚠ **HE SAID HE WOULD CONTINUE "IN THE EVENING" — SO S28 MAY BE
#      SAME-DAY. IF IT IS: NOTHING FROM S27 IS PROMOTABLE. Say so, skip the
#      S27 recall, and teach. The S26→S27 pattern already proves he uses
#      same-day sessions well when they are declared as content sessions.**
#   3. ⚠ **NO RULE DECISION IS OWED. The parking lot is EMPTY for the first
#      time since S22 — do not manufacture a candidate.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. ⚠ **EVERY [PREDICT] MUST DECLARE ITS KIND** — "derivable from what's
#      on screen" or "a genuine guess, wrong is fine". Held clean in S27.
#   6. ⚠ **NEW BINDING RULE, ADOPTED S27: every snippet that raises gets its
#      error NAMED by him before the traceback is shown.** Held clean all
#      session. Keep firing it.
#   7. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 27, Saturday 22 Aug 2026. Next: Session 28.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S27 yield: EIGHT PROMOTIONS + A DRILL FILE + DICT FINISHED + SET TAUGHT IN
  FULL + WHEN-TO-USE-WHICH TAUGHT.** The single best-yielding session since S25,
  and unlike S25 it produced code as well as recall.
- ⚠ **THE WEAKEST CLUSTER IN THE FILE SINCE S23 HAS CLEARED.** `break`,
  `continue`, `pass`, loop `else`, ternary — all cold, all unaided, all in one
  task-first drill. **The S25 hooks are what did it.** Read this as validation
  of the hook method, not of the explanations that preceded it.
- **`drills/s27_flow.py` — 20/20 pytest, five constraints met.** This is the
  drill file S26 owed and did not produce.
- Position: 1.1–1.7 closed. **1.8 open (~70% done). 1.9–1.13 remain, ~5.3 wk.**
- **COMPREHENSIONS: GATE DECLARED OPEN AT THE END OF S27 AND NOT WALKED
  THROUGH — he closed the session at exactly that point. S28 OPENS ON
  COMPREHENSIONS.**
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- ⚠ **COLD BUILD BLOCK: MOVED TO SUNDAY 23 AUG — SECOND DATE IT HAS CARRIED.**
  His call, and his reason was good ("I will have entire day for it then").
  ≥90 min, timed, no AI, git+pytest. **His own chosen task: the joint-limit
  clamp extended to MULTIPLE JOINTS with `*args`/`**kwargs`.** The design hole
  stays with him: `*args` delivers angles positionally and anonymously,
  `**kwargs` delivers limits by name, and nothing in that design pairs them.
  **S27 was deliberately kept off `*args`/`**kwargs` to protect the
  measurement. KEEP S28 OFF IT TOO IF THE BLOCK HAS NOT RUN. ASK AT THE OPEN.**
- Current Layer: 1. Current Topic: **1.8 — comprehensions next.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ✅ **ADOPTED S27 — "NAME THE ERROR BEFORE THE MENTOR SHOWS IT."** Written into
  RULES.md (now v3). **He proposed it AND ruled on it himself — a first.** It
  paid for itself on first use: his `SyntaxError`→`TypeError` miss is what
  exposed the missing **Station 0** in the four-station hook.
- **PARKING LOT NOW EMPTY.** Do not invent a candidate to fill it.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- Settled: queue tooling = a SCRIPT in this repo (not Anki). **STILL UNBUILT and
  now the top candidate for a build block after Sunday's.**

## WHERE WE LEFT OFF

### SESSION 28 STARTS HERE — exact resume point

S27 ran Saturday 22 Aug 2026 and closed **mid-sentence on comprehensions**: the
gate was declared open and he stopped the session there to save the material for
the evening.

Run in this order:

1. **INTERVAL GATE** (same-day risk is high — see header), then **one line: did
   Sunday's build block run, or is it still ahead?**

2. **THE COLD BLOCK — MUCH SMALLER THAN S27's, AND SHARPLY TARGETED:**
   - ⚠ **`KeyError` — THE ONE MISS OF S27.** He read `robot["speed"]` as
     `IndexError`. **The brackets are identical on a list and a dict; what goes
     INSIDE them decides.** Fire it cold, mixed with `IndexError` and
     `TypeError`, not alone.
   - **THE S26 BACKLOG THAT S27 NEVER REACHED — still entirely untested:
     TUPLE (whole unit), DICT (S26's two-thirds), SHALLOW COPY, UNPACKING,
     `list()`, `.get()`, `.items()`.** ⚠ **This is the second session running
     that this backlog has been declared and not run. Do it task-first, in one
     drill file, or it will rot.**
   - `while` mechanics (the bundle was deliberately NOT promoted in S27).
   - The mixed three-error set (`TypeError`/`NameError`/`UnboundLocalError`).

3. **OPEN COMPREHENSIONS.** The gate has been open since S25 (iteration protocol
   [x]) and was formally declared open at the S27 close. **Say the prerequisite
   out loud: the iteration protocol is the machinery underneath every
   comprehension.** List comprehensions → dict comprehensions.

4. **THEN THE 1.8 TAIL:** `zip`, f-strings (**he uses them correctly and cannot
   yet explain them**), nested structures, `reversed()`, `copy.deepcopy`.

**Standing turn rules: short messages, one teaching idea per turn, asks near the
top; doubt gate before every new subsection; depth-before-answer — traces never
optional, five checks on every drill, boundary values first. Tag every block, and
CHECK THE TAG IS RIGHT (S27 mis-tagged twice, both caught and corrected in
session — once too generous, once too modest). Do not propose ending the
session.**

⚠ **STANDING FROM S26, HELD CLEAN IN S27: teach a piece WITH CODE AND OUTPUT
first, then ask ONE question on it. Every [PREDICT] declares its kind.**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — target: every BUNDLED S16 promotion; the 1.6 spoken
  Feynman recall; the S22 short-gap promotions; the eight S23 promotions; the
  eleven S25 promotions; **the eight S27 promotions.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~]. **`str` immutability is still
  an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 28 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 70+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18. **S27 re-passed cold with mechanism, twice** | ~15 Sep |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran. Not one line of the file executes** | **[~] NEW S27 — he labelled it `TypeError` on first ask. Re-passed same-session (not promotable)** | **S28 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] — passed cold S27 on `dict.append`, self-rated 6/10. One more clean pass promotes** | **S28** |
| **`KeyError`** | **the KEY is not in the dict. ⚠ THE BRACKETS DON'T DECIDE THE ERROR — WHAT'S INSIDE THEM DOES** | **[~] ⚠ THE ONE MISS OF S27 — read as `IndexError`. Named correctly twice later, same-session, so NOT promotable** | **S28 cold, MIXED with `IndexError`** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value. ⚠ AN ORDER, NOT A MENU** | **[~] TESTED S27: 1 hit, 1 miss, 1 honest gap. Station 0 ADDED S27 after the `SyntaxError` miss** | **S28 cold** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27** | **S28 cold** |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | [x] — S26 full chain cold | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. THE TEST HE PRODUCED HIMSELF: can it go inside `print(...)`?** | **[x] ⚠ CLOSED S27 — the statement half was owed since S14. `d[k]=v` and `del d[k]` are STATEMENTS** | **~1 Sep** |
| **precedence** | **rank between DIFFERENT operators** | **[x] S27 — tested SEPARATELY for the first time, 7/10** | **~15 Sep** |
| **associativity** | **direction within the SAME rank. Sab left se, sirf `**` right se** | **[x] ⚠ RE-PROMOTED S27 after the S25 demotion. Asked ALONE, unbundled, 7/10** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | [x] S16, S23 | ~10 Sep |
| StopIteration | the stop signal; an EXCEPTION | [x] S25 | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator** | **[~] ⚠ queued S25, NOT ASKED IN S26 OR S27 — two sessions overdue** | **S28 cold** |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[~] S27 supporting evidence only: he rewrote `find_index` to `range(len(...))` correctly and unaided. Not directly asked** | **S28 cold** |
| **slicing / shallow copy** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]` copies the OUTER list, references SHARED** | **[~] taught S24/S26, NOT tested in S25, S26 or S27 — three sessions overdue** | **S28 cold** |
| **traceback** | **crash report; each line = one live frame** | **[x] ⚠ PROMOTED S27 after being [~] "cued only" since S23. Read `<module>` off a live `KeyError` unaided, 8/10. Later read a TWO-frame traceback correctly** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18. **S27: honest gap when asked on `rbot["joint"]`** | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade S23 | ~10 Sep |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] ⚠ ALL THREE PROMOTED S27, cold, in `drills/s27_flow.py`, 8/10. `break` and `pass` were the last [~]s of the set** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **runs only if the loop finished WITHOUT `break`. Read it as `nobreak`** | **[x] ⚠ PROMOTED S27 after a flat gap in S23. He also USED it unprompted where the task didn't require it** | **~15 Sep** |
| **ternary** | **EXPRESSION: `A if C else B` — evaluates to a VALUE. `ter-` = THREE** | **[x] ⚠ PROMOTED S27 after a flat gap in S23. Gave `print("high" if n>10 else "low")` as the concrete case** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument** | **`name=value` in the CALL, matched by NAME to a PARAMETER** | **[x] ⚠ PROMOTED S27 — [~] since S21, never tested until now. 7/10. ⚠ He called parameters "placeholders"; correction issued** | **~15 Sep** |
| **parameter vs argument** | **parameter = the name in the `def`; argument = what you pass** | **[~] ⚠ NEW WATCH — taught S18, and S27 shows the LABELS have not stuck even though the machine has** | **S28** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ `None`. **TYPE FIRST** | [x] S25. **S27: `pop` seen as the counterexample on a SECOND type (dict)** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates → `None`; `sorted()` builds a NEW list | [x] S25. **S27: `sorted(a_set)` returns a LIST — there is no sorted set** | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | [~] 3/6 cold S24 | **S28** |
| **tuple** | **immutable ordered sequence. THE COMMA MAKES IT. Immutability is SHALLOW** | **[~] taught S26. ⚠ NOT TESTED IN S27. S27 supporting evidence: he chose tuple correctly for a fixed-size sample record, unprompted** | **S28 cold** |
| tuple roster | `count` and `index` ONLY | [~] S26 | **S28 cold** |
| unpacking | `low, high = t`; count mismatch ⇒ `ValueError` | [~] S26, untested | **S28 cold** |
| single return value | `return a, b` builds ONE tuple | [~] S26, untested | **S28 cold** |
| `sum()` | totals an iterable; returns a new value | [~] S26, untested | **S28 cold** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] S26 two-thirds STILL UNTESTED. S27 taught the tail: `del`, `.pop()`, `.clear()`, `.update()`, insertion ordering** | **S28 cold** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order; overwriting a value does NOT move the key; delete-then-re-add DOES. ⚠ ORDERED ≠ SORTED** | **[~] NEW S27 — he predicted the delete-then-re-add case correctly from the rule** | **S28 cold** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE; `.clear()` → `None`, leaves `{}` — empty, not gone** | **[~] NEW S27** | **S28 cold** |
| **THE RAISE-VS-SHRUG PAIRING** | **ONE design rule seen three times: `d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when absence is EXPECTED** | **[~] NEW S27 — generalised from three separate facts. ⚠ HE ARGUED FOR THE RAISING FORM ON INSTINCT AND THE SPEC OVERRODE HIM; the lesson taught was that the SPEC decides, not temperament** | **S28** |
| hashable | hash must be STABLE ⇒ key must be immutable | [~] S26. **S27: re-used as the whole basis for `set`, and as tuple's stronger reason** | **S28 cold** |
| `.get()` vs `[]` | `[]` when missing is a BUG; `.get()` when absence is EXPECTED | [~] S26, untested | **S28 cold** |
| `.items()` / `.keys()` / `.values()` | looping a dict gives the KEYS; `.items()` gives TUPLES | [~] S26. **S27: `.keys()` is a VIEW and views support SET OPERATIONS directly** | **S28 cold** |
| **set** | **a dict with the values thrown away. Unique, unordered, hashable items. `{}` is an empty DICT — use `set()`** | **[~] NEW S27, taught in full, no drill file** | **S28 cold, TASK-FIRST** |
| **set order instability** | **no first element — the same file printed three different orders in three runs. Python won't offer an operation with no stable answer** | **[~] NEW S27 — he asked "why can't 0 mean first element" and was answered with the machine, not a rule** | **S28** |
| **`|` `&` `-` on sets** | **union / intersection / difference. All build a NEW set, so they are EXPRESSIONS. `-` is NOT symmetric** | **[~] NEW S27. `commanded - supported` = joints you can't drive, one operator, no loop** | **S28 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?" — not what you store** | **[~] NEW S27. ⚠ He gave four correct STORAGE answers and could not produce the single ASK question** | **S28** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell | a one-slot box; `__closure__` is a TUPLE | [x]-grade S25 | ~1 Sep |
| closure four layers | name → function object → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] **S27: `.clear()` leaving `{}` is the clean live example** | **S28** |
| THE FIVE CHECKS | "Boundary pe khaali ek bahar mila" — `bahar` = outside what you ASSUMED, sign AND type | [x] S25. **S27: the `find_index` latent bug WAS a `bahar`-by-type bug and he did not find it unaided** | ~1 Sep |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14 pass cold. **S27: identified `<module>` as the single live frame off a real traceback, unaided** | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 one-directional rule + `pop`, 8/10. **S27: `dict.pop` seen as the same counterexample on a second type** | [x] — gauntlet, then ~11 Sep |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day; S26 on a dict. **S27: `in` on a set as its defining question** | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD | [x] — **UNBLOCKS COMPREHENSIONS, WHICH S28 MUST OPEN** |
| Iterator causation | S22/S23 | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong. **S27: `first_big` handles the zero-iteration case correctly via loop `else`** | [~] label re-test |
| **Traceback: each line = one live frame** | **S27 PASSED COLD, 8/10** | **[x] — gauntlet, then ~15 Sep** |
| **`while` mechanics; nested loops; found-flag** | **S27 did NOT test these — the flow drill covered the keywords, not `while`** | **[~] S28** |
| **loop `else` / `pass` / ternary / `break` / `continue`** | **S27: ALL PASSED COLD in `drills/s27_flow.py`, 20/20 pytest** | **[x] — gauntlet, then ~15 Sep** |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged |
| Mutable/immutable discriminator | S18/S24/S26. **S27: used it unprompted to justify tuple-as-hashable** | [x] type half; tell half [~] **S28** |
| Cell causation | S22 pass 7/10 | [x] — ~31 Aug |
| Closure definition + application | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes; **S28** |
| Recursion | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| Five checks | S25 5/5 COLD. **⚠ S27: he did NOT catch the `find_index` `None`-as-both-sentinel-and-value bug on his own pass** | [x] — **gauntlet, and re-test with a TYPE boundary specifically** |
| Argument count ⊥ return value | S20 confusion; S26 the one-object half | [~] ~16 Sep |
| **`global` / `*args`/`**kwargs`** | **S22 pass 10/10 and 8/10. ⚠ DELIBERATELY UNTOUCHED IN S27 to protect the build block** | **[x] — leave alone until the block runs** |
| Compile-time locality TRAP in a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| Docstrings / `__doc__` | S25 cold, 6/10 | [x] — ~1 Sep |
| **Indexing / slicing** | **S24 taught; NOT re-tested in S25, S26 or S27 — three sessions overdue. S27 gave indirect evidence only** | **[~] — cold S28, with shallow copy** |
| **TUPLE (whole unit)** | **S26 taught in full. ⚠ STILL no drill file and no cold test — declared for S27 and not run** | **[~] — cold S28, TASK-FIRST, PRIORITY** |
| **DICT (whole unit)** | **S26 two-thirds + S27 tail. ⚠ The S26 two-thirds has still never been cold-tested** | **[~] — cold S28, TASK-FIRST, PRIORITY** |
| **SET (whole unit)** | **S27 taught in full, same-session throughout, no drill file** | **[~] — cold S28, TASK-FIRST** |
| **When-to-use-which** | **S27 taught; the deciding question was NOT produced by him** | **[~] — cold S28** |
| **Four-station hook + Station 0** | **S27: the experiment RAN. 1 hit, 1 miss, 1 honest gap** | **[~] — S28 re-fire, mixed** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** not observed S20–S27. **S27 gave the inverse twice: he
  asked whether to go learn hashing properly and ACCEPTED the Level 2 boundary
  when it was explained; and he chose to protect the build block by moving it to
  a full day rather than squeezing it.** Read both as calibration.
- ⚠ **NEW S27 — DESIGN-SWITCHING UNDER A HARD QUESTION. This is the sharpest new
  finding and it belongs beside depth-before-answer.** Asked three times what
  the outer container must DO when a new sample arrives mid-motion, he twice
  answered by **proposing a different design** (a dict keyed by timestamp)
  rather than answering the question. On the third, direct re-ask he got it
  instantly: *"tuple can't grow, list can grow."* **He had the answer the whole
  time. The escape route was redesign, not guessing.** ⚠ **COUNTERMEASURE: when
  he changes the design mid-question, name it and re-issue the ORIGINAL question
  unchanged. It worked immediately.** Related to but distinct from
  depth-before-answer: that one stops early, this one goes sideways.
- **Term/label retention — first-class watch area, and S27 SPLIT IT CLEANLY IN
  TWO for the first time.** Mechanisms: excellent, cold, unaided — `break`/
  `continue`/`pass` in one breath, loop `else`, ternary, associativity vs
  precedence, keyword-argument matching. Labels: still the failure point —
  `KeyError`→`IndexError`, `SyntaxError`→`TypeError`, "placeholders" for
  parameters, `{"a"=99}` for a dict literal. ⚠ **THE HOOKS FIXED THE MECHANISM
  RECALL AND HAVE NOT YET FIXED THE LABELS. That is exactly what the new S27
  rule is aimed at — keep firing it.**
- ⚠ **HE RAISED THE FORGETTING FEAR HIMSELF IN S27:** *"I still fear I am going
  to forget these methods, is that fair??"* Answered honestly: yes you will
  forget names, and no that is not what to protect — the model is three ideas
  (mutable type? returns `None`? raising or shrugging form?) and the roster is
  lookup-able. **Tenth instance of him auditing the learning system itself.**
- ⚠ **BUNDLED PROMOTIONS REMAIN A NAMED RISK — AND S27 IS THE FIRST SESSION THAT
  ACTIVELY REFUSED A BUNDLE.** `break` and `continue` both passed cold, but the
  `while` bullet that carries them was left [~] because `while` mechanics were
  not tested. **Do this every time.**
- **CONFIDENCE CALIBRATION — STRONG DATA THIS SESSION AND IT IS ACCURATE.** Eight
  ratings, 6–8/10, and the two 6/10s were the two shakiest answers (one right,
  one wrong). **Keep using self-rating as a TARGETING signal.**
- **Depth-before-answer:** fired **three times** in S27 (the precedence concept
  half, the ternary concrete case, the set-meaninglessness half) and **all three
  recovered on the re-ask.** ⚠ **Ten successful re-asks across S24–S27, zero
  failures. THE RE-ASK IS THE INTERVENTION. Do not re-teach.**
- **Honest-gap declaration remains reliable.** S27: *"actually I don't remember
  this"* on `NameError`, and *"I am not sure"* before offering the four container
  usages.
- **⚠⚠ SPEC-WRITING IS THE MENTOR WATCH AREA — FOURTH CONSECUTIVE SESSION, BUT
  THE VOLUME COLLAPSED: FOUR defective asks in S26, ONE in S27.** The one:
  *"you're checking whether a joint name is supported — would you use `remove` or
  `discard` to drop a joint?"* — a membership scenario welded to a removal
  question with no reason to remove anything. **He called it senseless and was
  right.** The fix that worked, and it should now be standard: **the re-issued
  version supplied the missing condition explicitly ("the handler may fire
  TWICE"), and that one clause made the question decidable.**
- ⚠ **TEACH:ASK RATIO — S26's finding, and S27 HELD IT.** Every teaching block
  carried code and output before its question; the pure-question stretch was
  DECLARED as a cold block up front (*"this stretch is meant to be all
  questions"*) and he did not push back once.
- ⚠ **INSTRUMENT TAGGING — TWO SELF-CAUGHT MIS-TAGS IN S27, BOTH CORRECTED IN
  SESSION, IN OPPOSITE DIRECTIONS.** (a) A [RECALL] fired thirty seconds after
  teaching the station-4 table — should have been [TEACH-BACK]; corrected before
  anything was ledgered. (b) A traceback read tagged [TEACH-BACK] when it was
  genuinely later-day cold material — corrected UP to [RECALL] and promoted.
  **Both matter: (a) protects the ledger from echo, (b) stops real evidence being
  thrown away. Check the tag in both directions.**
- False attribution: **39 raised, 38 upheld or part-upheld.** S27 raised one:
  (39) *"why would I be removing a joint after checking if its supported?
  question is itself senseless"* — **UPHELD IN FULL.**

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; IEEE 754 (1.13, promised); 32/64-bit;
  `globals()`/`locals()` drill; senior traceback read (1.9); .pyc (1.10); GIL
  (1.13); concurrency (post-Layer 1); certifications; GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff
- **`reversed()`** — still owed in 1.8.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **`copy.deepcopy` and the `copy` module** — still owed inside "nested data
  structures" in 1.8.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- ⚠ **HASHING as a mechanism — HE ASKED DIRECTLY IN S27 whether to go learn it
  now, and the Level 2/Level 3 boundary was drawn to his face: he has the Level 2
  model (a number from the contents, used to jump to a slot, must be stable) and
  that is the course target. HOW the number is computed, COLLISIONS and RESIZING
  are DSA — master Layer 8. He accepted it immediately.** Reuse this exchange as
  the template for future "how deep here?" questions.
- ⚠ **HASH RANDOMISATION** — he saw set order differ across three runs of the
  same file. The *why* (per-process seed, a security measure) was stated but not
  taught. Park to 1.13.
- **`zip`** — reached for unprompted in S26, untaught since S19. **Owed in 1.8.**
- **f-strings** — he uses them correctly and cannot yet explain them. **Owed in
  1.8. Teach, don't assume.**

---
