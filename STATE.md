# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 27 (for Claude):
#   1. Read RULES.md fully, then this file fully. No re-introductions.
#      No ARCHIVE.md unless gauntlet / re-baseline / asked.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S26
#      (Fri 21 Aug 2026). S25 AND S26 both ran that same day, so a
#      later-day S27 makes a LARGE backlog of cold tests legitimate.
#   3. ⚠ **RULE DECISION OWED AT THE OPEN — see RULE-CHANGE PARKING.
#      He asked for it himself; get the ruling before teaching.**
#   4. [RECALL]s open TASK-FIRST: drills/ + pytest where sensible; the
#      name/definition question comes only after the code runs.
#   5. ⚠ **EVERY [PREDICT] MUST DECLARE ITS KIND — "derivable from what's
#      on screen" or "a genuine guess, wrong is fine". Committed to him
#      in S26 after pushback 38.**
#   6. At session end: rewrite this file, tick CURRICULUM.md if anything
#      moved, append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 26, Friday 21 Aug 2026. Next: Session 27.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S26 yield: TUPLE TAUGHT IN FULL, DICT ~⅔ TAUGHT. ZERO PROMOTIONS — and that
  is correct, not a shortfall: S26 ran the SAME DAY as S25, so nothing today was
  promotable.** Second session in a row on his explicit instruction (S25 = all
  recall by his request; S26 = all content by his request). The instruction was
  honoured both times.
- **⚠ NO DRILL FILE WAS WRITTEN IN S26.** The session ran on live code and
  prediction only. **Nothing from S26 can promote until it is drilled.** S27
  must produce `drills/s27_*.py`.
- Position: 1.1–1.7 closed. **1.8 open (~40% done). 1.9–1.13 remain, ~5.5 wk.**
- **COMPREHENSIONS STILL UNBLOCKED** (iteration protocol [x] S25) and STILL NOT
  OPENED. Declare the gate open out loud when they start.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date,
  written into the master whether or not it is welcome. Scope moves NEVER cut.
- **Cold build block: SATURDAY 22 AUG — still tomorrow.** ≥90 min, timed, no AI,
  git+pytest. **His own chosen task: the joint-limit clamp extended to MULTIPLE
  JOINTS with `*args`/`**kwargs`.** The design hole stays with him: `*args`
  delivers angles positionally and anonymously, `**kwargs` delivers limits by
  name, and nothing in that design pairs them. **ASK HOW IT WENT AT THE S27 OPEN.**
- Current Layer: 1. Current Topic: **1.8 — finish dict, then set.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ⚠ **ONE CANDIDATE, RAISED BY HIM, AWAITING HIS RULING AT THE S27 OPEN:**
  **"Every snippet that raises gets its error NAMED by the student before the
  mentor shows it."** His words: *"in order to stick it you need to ask me again
  and again, different error — when using regularly it will definitely stick."*
  **This is him asking for spaced retrieval on the error labels rather than more
  explanation, which is exactly the S25 hook finding.** Offered once, no ruling
  taken (he closed the session first). **Take the ruling, then adopt or drop.
  Do not offer it a third time — see the dropped-rule precedent below.**
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Three offers,
  no ruling; behaviour settled it. Do not raise it again.
- Settled: queue tooling = a SCRIPT in this repo (not Anki). Still unbuilt.

## WHERE WE LEFT OFF

### SESSION 27 STARTS HERE — exact resume point

S26 ran Friday 21 Aug 2026, **the same day as S25**, at his request: *"no
recall, actually studying 1.8 further."* Honoured — the session opened on
content and the four hook tests were correctly deferred as same-day echo.

Run in this order:

1. **INTERVAL GATE, then the rule ruling** (above), then **one line: how did
   Saturday's build block go?**

2. **⚠ THE COLD BLOCK IS NOW LARGE AND IT IS ALL LEGITIMATE.** Two full sessions
   of material sit untested. Task-first where possible. Priority order:
   - **The four S25 hooks** — `pass` (*jagah bharo / agla chakkar / bahar niklo*),
     loop `else` (read it as **`nobreak`**), ternary (**`ter-` = three**),
     **associativity ALONE, never bundled with precedence.**
   - **`list()`** — constructor call, builds a NEW list from any iterable,
     drains an iterator. Queued S25 after nine sessions of never being asked.
   - **The FOUR-STATION HOOK, new S26: NAAM → DOT → TYPE → CHEEZ**, and station
     4's three siblings (jagah = Index, chaabi = Key, cheez = Value).
   - `break` alone; indexing/slicing; `traceback`; keyword argument.

3. **FINISH DICT:** deletion (`del`, `.pop()`), insertion ordering, dict
   comprehensions. Then **set**, then **when-to-use-which**.

4. **THEN THE 1.8 TAIL:** comprehensions (**gate open — say so**), `zip`,
   f-strings (**he already uses them correctly and cannot yet explain them**),
   nested structures, `reversed()`.

5. **STILL OWED:** the statement half of expression-vs-statement; `while`
   mechanics; the mixed three-error set.

**Standing turn rules: short messages, one teaching idea per turn, asks near the
top; doubt gate before every new subsection; depth-before-answer — traces never
optional, five checks on every drill, boundary values first. Tag every block, and
CHECK THE TAG IS RIGHT. Do not propose ending the session.**

⚠ **NEW STANDING RULE FROM S26, COMMITTED TO HIM: teach a piece WITH CODE AND
OUTPUT first, then ask ONE question on it. And every [PREDICT] declares its kind
— "derivable from what's on screen" or "a genuine guess, wrong is fine".**

**CARRY FORWARD:**
- **August gauntlet (last session of August): SACRED.** Carries: strict-legend
  audit of every [x] — **target: every BUNDLED S16 promotion, because
  associativity proved bundling hides untested items**; the 1.6 spoken Feynman
  recall; the S22 short-gap promotions; the eight S23 promotions; the eleven S25
  promotions.
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- Three-error set (`TypeError`/`NameError`/`UnboundLocalError`) still untested
  MIXED. `UnboundLocalError` spelling is FIXED.
- `None`/`is None` and `bool("False")` remain [~]. `str` immutability is an
  [x] candidate on one clean later-day pass.
- Governance/format requests mid-session → PARK, close material, write at end.
- Drills: mentor never edits a file the student started; autocomplete OFF.

Every teaching block shows full runnable source alongside output.
Session 27 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: the two queues are 70+ rows against the
~30-row trigger in RULES proposal 6. The adopted remedy is a SCRIPT IN THIS
REPO. Still unbuilt; now the top candidate for a build block after Saturday's.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18 | ~10 Sep |
| **`AttributeError`** | **the name after the DOT is not on the object; Python never got as far as doing anything** | **[~] NEW — mentioned S13 and S25, DEFINED for the first time S26. Same bookkeeping hole as `list()`: seen twice, never queued.** | **S27 cold** |
| **`KeyError`** | **the KEY is not in the dict** | **[~] NEW — had NEVER appeared in the course before S26 (verified by grep). Pushback 36, upheld.** | **S27 cold** |
| **FOUR-STATION HOOK** | **NAAM → DOT → TYPE → CHEEZ. Station 4: jagah = Index, chaabi = Key, cheez = Value** | **[~] NEW S26 — built after he diagnosed that the error TABLE was not sticking. Untested.** | **S27 cold — hook test** |
| truncation | cut off TOWARD ZERO; `int(-5.98)` → `-5` | [x] S23 | ~10 Sep |
| floor division | floors toward −∞; `-5.98 // 1` → `-6` | [x] S23 | ~10 Sep |
| alias | two names, one object | [x] — held S24. **S26: the full chain (parameter/argument → alias → mutable → mutating method) produced cold and unprompted** | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 strong pass | ~14 Sep |
| operand | value an operator acts on | [x] S23, 7/10 | ~10 Sep |
| expression vs statement | value vs action | [~] statement half STILL owed | **S27** |
| **precedence / associativity** | **precedence = rank between DIFFERENT operators; associativity = direction on the SAME rank. Sab left se, sirf `**` right se.** | **[~] DEMOTED S25 — flat "gap" when asked ALONE. Re-taught S25. Precedence half untouched.** | **S27 cold, ALONE** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | `a == b*(a//b) + (a%b)`; sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | able-to-be-iterated (REUSABLE) / the nozzle (CONSUMED) | [x] S16, S23 | ~10 Sep |
| StopIteration | the stop signal; an EXCEPTION raised by `next()` | [x] S25, 7/10 | ~11 Sep |
| `next()` / `iter()` | `iter()` once at the top; `next()` once per pass | [x] S25, 8/10 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **`list()`** | **CONSTRUCTOR CALL — builds a NEW list from any iterable; drains an iterator** | **[~] queued S25 after nine sessions of never being asked. Retrieved from NOTES, not memory.** | **S27 cold** |
| **indexing** | **`[]` takes a POSITION; 0-based; last index is `len-1`; negative counts back; out of range ⇒ `IndexError`** | **[~] taught S24, not re-tested in S25 or S26** | **S27 cold** |
| **slicing** | **`[start:stop:step]`, HALF-OPEN; builds a NEW list; `l[:]` is the copy idiom; out of range ⇒ `[]`, NEVER raises** | **[~] taught S24. S26 EXTENDED IT: `l[:]` is a SHALLOW copy — outer list new, inner references SHARED. He predicted both output lines wrong.** | **S27 cold** |
| **shallow copy** | **uthla — one level deep. The container is copied; the REFERENCES inside are copied, so nested mutables are SHARED. Only bites when the container holds mutables.** | **[~] NEW S26 — discharges the S24 parked point (`tools[:]` called "an identical new list object")** | **S27 cold** |
| traceback | crash report; each line = one live frame | [~] S23 cued only | **S27 cold — overdue** |
| NameError | the NAME does not exist anywhere | [x] S18 | ~10 Sep, MIXED |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25, 8/10 | ~11 Sep |
| `while` vs `for` | condition re-checked vs walking an iterable | [x]-grade S23, 7/10 | ~10 Sep |
| `break` / `continue` | exit loop / end this ITERATION | `continue` [x] S25. **`break` still [~]** | **`break` S27** |
| **`pass`** | **no-op filling a block that cannot be empty. HOOK: *pass = jagah bharo, continue = agla chakkar, break = bahar niklo*** | **[~] flat "gap" S25, re-taught same session** | **S27 cold — hook test** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else`** | **runs only if the loop finished WITHOUT `break`. HOOK: read the keyword as `nobreak`.** | **[~] flat gap S23, re-taught S25** | **S27 cold — hook test** |
| **ternary** | **EXPRESSION: `A if C else B` — evaluates to a VALUE. HOOK: `ter-` = THREE; value, condition, value; the middle is the condition.** | **[~] flat gap S23, re-taught S25** | **S27 cold — hook test** |
| elif | chain, first true wins, rest never evaluated | [x] S17 | ~10 Sep |
| keyword argument | `name=value` in the CALL, matched by NAME | [~] defined S21, never tested | **S27** |
| UnboundLocalError | name IS local (compile-time), no value bound yet | spelling FIXED S23 | mixed 3-error test |
| mutating vs non-mutating — THE TELL | ⚠ ONE-DIRECTIONAL: returns `None` ⇒ mutating; mutating ⇏ returns `None`; `pop` is the counterexample. **TYPE FIRST.** | [x] S25, 8/10. **S26 strong supporting evidence: he derived the whole tuple roster from the type alone** | ~11 Sep |
| `sort` vs `sorted` | `sort()` mutates, returns `None`; `sorted()` builds a NEW list | [x] S25, 8/10 | ~11 Sep |
| list method roster | `append` `extend` `insert` `sort` `remove` all mutate → `None`; `pop` mutates → returns the removed ITEM | [~] 3/6 cold S24 | **S27** |
| **tuple** | **immutable ordered sequence. THE COMMA MAKES IT, not the parentheses — `(5)` is an `int`. Immutability is SHALLOW.** | **[~] NEW — TAUGHT IN FULL S26** | **S27 cold** |
| **tuple roster** | **`count` and `index` ONLY — an immutable type can only carry methods that REPORT** | **[~] NEW S26 — he DERIVED all six list methods as impossible, from the type, unaided** | **S27 cold** |
| **unpacking** | **`low, high = t` binds items to names left to right. Count mismatch ⇒ `ValueError` (type fine, count wrong)** | **[~] NEW S26** | **S27 cold** |
| **single return value** | **`return a, b` builds ONE tuple. A function never returns more than one object.** | **[~] NEW S26** | **S27 cold** |
| **`sum()`** | **built-in; totals an iterable of numbers; returns a new value; does not mutate** | **[~] NEW — NINTH substrate breach; used before being defined, defined in-session S26** | **S27 cold** |
| **dict** | **key → value; `[]` takes a KEY; no scan. Keys UNIQUE — existing key OVERWRITES, never duplicates.** | **[~] NEW S26** | **S27 cold** |
| **hashable** | **the key's hash must be STABLE, so the key must be immutable — else the value becomes unreachable. Error says `unhashable type`, not "immutable".** | **[~] NEW S26 — he REASONED IT OUT HIMSELF from collision/lost-value. ⚠ Correction issued: immutability ⇏ uniqueness; `(1,2)` and `(1,2)` are the SAME key.** | **S27 cold** |
| **`.get()` vs `[]`** | **`[]` when a missing key is a BUG; `.get()` when absence is EXPECTED and you have a real default. `.get()` with no default MOVES the crash away from the cause.** | **[~] NEW S26 — the design half answered cold on the re-ask: *"silent failures"*** | **S27 cold** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS. `.items()` gives `(key, value)` TUPLES — it is tuple unpacking in disguise.** | **[~] NEW S26** | **S27 cold** |
| pre-order / post-order | work before the call / after the call | [x] S23, 6/10 | ~10 Sep |
| lambda | EXPRESSION form of a function; auto-returned | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it; absent = `None` (the attribute EXISTS) | [x] S25, 6/10 | ~1 Sep |
| `key=` | one argument, sorts by RESULTS, returns ORIGINAL items | [x]-grade in use S23 | ~10 Sep |
| cell | a TYPE — a one-slot box; `__closure__` is a TUPLE, one cell per free variable | [x]-grade S25 | ~1 Sep |
| closure four layers | name → function object → `__closure__` TUPLE → CELL → `cell_contents` | [x] S25, 7/10 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | [~] **S26 adds a live example: `.get()` manufacturing a `None` that travels** | **S27** |
| THE FIVE CHECKS (mnemonic) | "Boundary pe khaali ek bahar mila" — `ek` = EXACTLY ONE; `bahar` = outside what you ASSUMED, sign AND type | [x] S25, 5/5 cold | ~1 Sep |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14 pass cold | [~] **overdue** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (rebinding vs mutation, `==` vs `is`, mutability+aliasing, copies, precedence, `+=`, negative `//` and `%`, `**`, if-block scope, `range()`, function scope) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half separately** + ~14 Sep |
| `str` immutability | S17 supporting evidence; **S26 supporting: `"abc"[0]="z"` → `TypeError` shown, and he correctly said a string can't be mutated** | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | [~] due 29 Aug |
| Type conversion traps (`bool("False")`, `10/2` float) | owed | [~] due ~1 Sep |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 one-directional rule + `pop`, 8/10 | [x] — gauntlet, then ~11 Sep |
| `__defaults__` | S22 produced cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13 same-day. **S26 taught `in` on a DICT (checks KEYS)** | [~] due ~5 Sep |
| Short-circuit | S14 pass | [~] one more pass promotes |
| Iteration protocol (`iter()` once, `next()` per pass, `StopIteration`) | S25 PASSED COLD, all three parts | [x] — **UNBLOCKS COMPREHENSIONS.** Gauntlet, then ~11 Sep |
| Iterator causation (forward-only state) | S22 pass; S23 held | [x] — gauntlet, bug-first always |
| Exceptions are signals | S18 pass | [x] ~10 Sep |
| Loop-body name after zero iterations | S16 label wrong | [~] label re-test |
| Traceback: each line = one live frame | S23 cued only; not reached S25 or S26 | [~] **still owed — S27** |
| `while` mechanics; nested loops; loop `else`; found-flag; `pass`; ternary | S25 re-taught with hooks, same-session | [~] **S27 is the hook experiment — still the weakest cluster** |
| `if`/`elif`/`else` chain | S17 pass cold | [x] gauntlet-flagged, ~10 Sep |
| Mutable/immutable discriminator | S18 pass; S24 corrected the TELL. **S26: applied it unaided to derive the entire tuple roster — strongest evidence yet** | [x] type half; tell half [~] **S27** |
| Cell causation (five calls, five cells) | S22 pass 7/10 | [x] — ~31 Aug, then ~17 Sep |
| Closure definition + application | S25 both PASSED COLD; `drills/s25_closure.py` 10/10 unaided | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting evidence | [~] — one direct cold test promotes; **S27** |
| Recursion: base/recursive case, frames stacked | S20 same-day | [~] ~16 Sep |
| Pre-order vs post-order (transfer) | S22 pass 10/10 | [x] — gauntlet, then ~17 Sep |
| Identity-value rule (as a RULE) | S20, untested as rule | [~] ~16 Sep |
| Termination: base exists + step lands | S20 bug-hunt pass | [~] strong |
| Printer vs calculator | S20 | [~] ~16 Sep |
| Pure functions + disguised mutator | S20; label "pure" owed | [~] ~16 Sep |
| Five checks | S25: 5/5 COLD, self-rated 4/5 | [x] — gauntlet, then ~1 Sep |
| Argument count ⊥ return value | S20 category confusion. **S26 adds the other half: a function returns exactly ONE object, always** | [~] ~16 Sep |
| `global` / `*args`/`**kwargs` | S22 pass 10/10 and 8/10 | [x] — ~7 to ~17 Sep |
| Compile-time locality TRAP inside a closure | S22 miss → unaided repair | [~] — the `nonlocal` motivation for 1.13 |
| Lambdas | S23 PASS, 6/6 cold | [x] — ~10 Sep |
| Docstrings / `__doc__` | S25 both values cold, 6/10 | [x] — ~1 Sep |
| Indexing / slicing | S24 taught; **NOT re-tested in S25 or S26 — two sessions overdue** | [~] — **cold S27, plus shallow copy** |
| **TUPLE (whole unit)** | **S26 taught in full. No drill file, no cold test — same-day session.** | **[~] — cold S27, TASK-FIRST** |
| **DICT (~⅔ taught)** | **S26: pairs, `[]`, uniqueness, hashability, `in`, `.get()`, iteration, `.items()`. Deletion/ordering/comprehensions untaught.** | **[~] — cold S27, TASK-FIRST** |
| **Four-station error hook** | **S26: built, never tested** | **[~] — S27 is the experiment** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- **Jump-ahead pattern:** not observed S20–S26. **S26 gave the inverse again:
  he stopped the session himself when the cognitive load got high** rather than
  pushing on badly. Read that as calibration, not avoidance.
- **Term/label retention — first-class watch area, and S26 REPRODUCED THE S25
  FINDING FROM THE OTHER SIDE.** A full error-reference TABLE was delivered on
  request; twenty minutes later he mislabelled `AttributeError` as `TypeError`
  and diagnosed it himself: *"maybe it's not sticking in my mind."* **Tables are
  explanations, and explanations have never worked for arbitrary labels in this
  file. It was rebuilt as the four-station HOOK.** S27 tests it cold.
- ⚠ **BUNDLED PROMOTIONS REMAIN A NAMED RISK.** Gauntlet action stands: audit
  every [x] sharing a bullet, re-ask each half SEPARATELY.
- **CONFIDENCE CALIBRATION — NO DATA THIS SESSION.** Correctly so: every block
  was [PREDICT] or [TEACH-BACK], neither of which carries a rating, and the
  session was same-day. Do not read the absence as regression.
- **Depth-before-answer:** fired **twice** in S26 (the `.get()` design half, the
  tuple-choice design half) and **both recovered on the re-ask** — the `.get()`
  one in a single line, *"silent failures"*. ⚠ **Seven successful re-asks across
  S24–S26 with zero failures. The re-ask IS the intervention. Do not re-teach.**
- **Honest-gap declaration remains reliable.** Three times in S26: *"I don't
  know"* on the unpacking-mismatch, *"I don't get the second question"* on what
  a tuple buys, and *"I am not sure... what am I saying, is that correct??"*
  self-flagging his own wrong uniqueness claim mid-sentence.
- **⚠⚠ SPEC-WRITING IS THE MENTOR WATCH AREA AND S26 WAS THE WORST SESSION YET
  — THIRD CONSECUTIVE.** **FOUR defective asks in one session:** (a) `KeyError`
  demanded having never appeared in the course; (b) dict-key uniqueness never
  stated before a PREDICT depended on it; (c) *"given you have `[]`"* read as
  *"you have a list"*; (d) the linear-cost question unanswerable as worded.
  **The S25 fix — lettered sub-requirements — was written for DRILL specs and
  was not applied to ORAL asks. Extend it: every ask states exactly what is
  being asked for, and names what the student is allowed to use.**
- **⚠ NEW S26 — TEACH:ASK RATIO IS A MENTOR WATCH AREA.** He raised it directly:
  *"all your questions look like you are asking things without teaching, it's
  daunting — is it my fault of thinking or your fault?"* **Audited and mostly
  upheld.** The session ran predict → predict → predict with almost no
  exposition between. **Committed fix, now standing: teach a piece WITH CODE AND
  OUTPUT, then ask ONE question on it — and every [PREDICT] declares whether it
  is derivable from what's on screen or a genuine guess.** The second half is
  the S18 rule-1 finding recurring: *if the student cannot tell one instrument
  from another, it is not being declared clearly enough.*
- False attribution: **38 raised, 37 upheld or part-upheld.** S26 raised four:
  (35) the linear-cost ask is unintelligible — **UPHELD**; (36) *"you didn't
  tell me if a dict can have two same keys, and you're straight asking
  questions"* — **UPHELD**, and auditing it found `KeyError` had never been
  taught **anywhere in the course**; (37) *"your question was not properly
  asked, I thought you said you have `[]` list"* — **UPHELD**; (38) *"are you
  asking without teaching — is it my fault or yours?"* — **PART-UPHELD**.
  ⚠ **NOTE THE SHAPE OF 38: it is not a complaint about difficulty. It is a
  request for a DIAGNOSIS, offered with his own fault as the first hypothesis.**
  Ninth instance of him auditing the teaching system itself.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; IEEE 754 (1.13, promised); 32/64-bit;
  `globals()`/`locals()` drill; senior traceback read (1.9); .pyc (1.10); GIL
  (1.13); concurrency (post-Layer 1); certifications (not scheduled); GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff
- **`reversed()`** — still owed in 1.8 (`l[::-1]` done S24).
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **DEEP copy (S24 park, half-discharged S26):** shallow copy is now TAUGHT.
  **`copy.deepcopy` and the `copy` module are still owed** — park to "nested
  data structures" inside 1.8.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **NEW S26: HASHING as a mechanism.** He was given the Level 2 model (a number
  computed from the key, used to jump to a slot; must be stable). **How the hash
  is computed, collisions, and resizing are DSA / Level 3 — master Layer 8.**
  He spotted the DSA boundary himself on the linear-scan question.
- **NEW S26: `zip`** — he reached for it unprompted and correctly. Untaught since
  S19. **Owed inside 1.8.**
- **NEW S26: f-strings** — he uses them correctly and cannot yet explain them.
  Already parked in 1.8 from S16; now has live evidence. **Teach, don't assume.**

---
