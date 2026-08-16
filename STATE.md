# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 21 (for Claude):
#   1. Read RULES.md fully, then this file fully. Do not ask for
#      re-introductions. Do not load ARCHIVE.md unless this is a gauntlet /
#      re-baseline session or the student asks.
#   2. FIRST ACTION: the INTERVAL GATE. Ask how long since S20 (Sun 16 Aug
#      2026). If it is a later day, cold work today is promotable evidence.
#   3. Then follow "SESSION 21 STARTS HERE" below, exactly.
#   4. Before teaching anything, ask the student for a decision on the seven
#      PROPOSED CHANGES listed at the top of RULES.md. Adopt at most what he
#      agrees to; record the decision in the RULE-CHANGE PARKING area below.
#   5. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, return everything as downloads.
#
# STATE AS OF: end of Session 20, Sunday 16 Aug 2026. Next: Session 21.
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (carried from the v16 progress tracker; recompute 31 Aug)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** Cadence required: ~5 sessions/week.
  Hour budget ~900h against ~870h available: zero slack.
- **Last honest position (10 Aug, end of S18):** 1.6 closed, 1.7 ~two-thirds
  taught, six-and-a-bit subsections remaining (1.7 tail + 1.8–1.13) against
  ~7 weeks; required rate ~1 subsection/week, margin ZERO.
- Since then: S19 ≈ ? (closures, recursion deferred), S20 ≈ 0.4. **1.7 has
  FOUR items left; one good session closes it.** 1.8–1.13 untouched.
- **RE-BASELINE LADDER STAYS ARMED — formally due 31 Aug 2026.** Observed
  throughput → derived completion date, written into the master whether or
  not it is welcome. The student chose the date himself in S15.
- Review note (16 Aug): the "fraction of a subsection" unit treats all
  subsections as equal. 1.8 and 1.12 are several times 1.6. Do the 31 Aug
  arithmetic in ITEMS, not subsections. The student has stated NOTHING is to
  be cut from the curriculum; the re-baseline therefore moves the date, not
  the scope, and must say so plainly.
- Current Layer: 1. Current Topic: **1.7 Functions — `global`,
  `*args`/`**kwargs`, lambdas, docstrings remain.**

## RULE-CHANGE PARKING (proposal 3 — candidates wait here; adopt ≤1 per session, at close)
- (empty — the seven items at the top of RULES.md await a decision in S21)

## WHERE WE LEFT OFF

### SESSION 21 STARTS HERE — exact resume point

Session 20 ran on SUNDAY 16 AUGUST 2026. **The interval gate passed** — a
FOUR-day gap since S19, the longest of the arc — and was applied by the mentor
unprompted for the third session running.

**CHECK THE DATE FIRST, AS ALWAYS.** If S21 runs on a genuinely later day, the
S20 material is promotable and the [RECALL] block below is legitimate. If it
runs within hours of S20, skip the block, say why, and go straight to the 1.7
tail, which is new material and legitimate at any interval.

**READ THE RULES BEFORE TEACHING ANYTHING: the S16 five, the S17 three, the S18
two, the S19 one and THE S20 THREE.** Tag every question block [RECALL],
[PREDICT], [DRILL] or [TEACH-BACK]. State the prerequisite and its status before
opening any unit. Confidence after his own answer, before the verdict — none at
all on a [TEACH-BACK]. RECALL FIRST, NOTES SECOND. **Do not propose ending the
session.**

**THE THREE S20 RULES ARE THE OPERATIVE ONES THIS SESSION AND THEY CHANGE HOW A
TURN IS WRITTEN, NOT JUST WHAT IS IN IT:**
- **KEEP MESSAGES SHORT. One teaching idea per turn.** He does not read long
  messages to the end — he said so plainly — and that, not carelessness, is why
  asks have been going unanswered. **Put any question or instruction NEAR THE
  TOP of a turn, never in a tail after a table or a code block.**
- **RUN THE DOUBT GATE before opening any new subsection.** Ask for doubts,
  WAIT, and if any come, **restate the just-taught material IN FULL as one clean
  block** before answering them. Hold any stranded question and say you are
  holding it.
- **DEPTH BEFORE ANSWER.** A correct output does not discharge a request for a
  trace or a mechanism — re-ask. Every drill he writes gets THE FIVE CHECKS run
  on it by HIM before submission. Boundary values tested first.

Run in this order:

1. **[RECALL] THE POST-ORDER TRANSFER QUESTION — HIGHEST-VALUE ITEM AVAILABLE.**
   Give him a recursive function with the work AFTER the call and ask for the
   output and the reason. **He failed this in S20 by imagining one mutating `n`
   instead of four frames each holding their own — the identical isolation
   principle he had correctly explained for cells twenty minutes earlier.**
   ⚠ **ASK IT AS A TRANSFER QUESTION, NOT A RECURSION QUESTION.** The concept is
   not missing; its recognition in a new container is. If he stalls, the prompt
   is *"where have you already told me two things can't collide?"* — do not
   hand him the frames answer.

2. **[RECALL] THE CELL CAUSATION, AND TELL HIM WHY IT IS BEING ASKED AGAIN.**
   He got this CORRECT UNAIDED in S20 and rated it 5/10, which blocked the
   promotion. **This is the first under-rating in the file.** Re-fire it once,
   cold. If it comes back correct again, **say explicitly that his rating is the
   only thing standing between this item and an [x]** — his calibration is used
   as a targeting signal and it has to be accurate in both directions.
   ⚠ Watch for the two S20 corrections: the new object comes from **THE CALL**,
   not the loop; and it is a **CELL**, with `cell_contents` as an attribute on
   it, not a "content cell".

3. **[RECALL] THE CLOSURE DEFINITION, COLD.** Self-rated 4/10 in S20 and the
   cold attempt missed the CELL entirely. Target: **a function object that binds
   a free variable from where it was created into its own private cell, so the
   value survives after the enclosing frame has died.** Corrections to listen
   for: "free VARIABLE" not "free value"; `__closure__[0]` is the CELL and the
   value is `.cell_contents`; `__closure__` is `None`, not an empty tuple, when
   there are no free variables; **and the binding happens WHEN `def` RUNS** —
   he had that in his first attempt and lost it in his second.

4. **[RECALL] `traceback` — AND THIS IS ITS FIRST HONEST TEST.** ⚠ **Do not
   treat it as a carried failure. It was taught for the first time in S20**;
   S16, S18 and S19 fired it as a recall on material that had never been
   delivered, and those measurements are struck. Ask what ONE line of a
   traceback is. Required answer: **one live frame on the call stack.** Do not
   accept "where the error happened" — that is the location half he already had.

5. **THEN CLOSE 1.7 — FOUR ITEMS AND ONE SESSION SHOULD DO IT.** `global`
   (taught AGAINST `nonlocal`, which he owns: `nonlocal` targets the enclosing
   cell, `global` the module), `*args`/`**kwargs` (**he asked for these by name
   — say so**), lambdas, docstrings. **1.7 CANNOT BE MARKED CLOSED UNTIL ALL
   FOUR ARE TAUGHT.**

6. **THE SPOKEN FEYNMAN RECALL FOR THE WHOLE OF 1.6 — NOW SLIPPED THREE
   SESSIONS.** It has been scheduled and dropped in S18, S19 and S20. **Either
   run it in S21 or move it formally into the August gauntlet and stop
   pretending it is a live item.** Do not schedule it a fourth time and skip it.

**CARRY FORWARD:**
- **THE FOUR S19 CONFIDENCE RATINGS ARE STILL OWED.** Asked once in S20, per
  plan, and still not given. **Do not ask a third time — it is not worth the
  friction, and rule 2 explains why they were missed.** Mark them
  unrecoverable, note it, move on.
- **`__defaults__` (7/10) and the ITERATOR CAUSATION (4/10) were NOT fired in
  S20** — the traceback re-teach and the recursion block took the room. **Fire
  both in S21.** The iterator causation must be opened **BUG-FIRST** (the
  hoisted `it = iter(range(2))` image); it has now worked twice and the
  definition-first approach failed three times. `__defaults__` handle: **shelf
  par naam, dabbe ke andar attribute.**
- ⚠ **AUDIT THE CARRY-FORWARD LIST FOR THE TRACEBACK DEFECT.** One item on that
  list turned out to have been repeatedly TESTED and never TAUGHT. **Before the
  August gauntlet, check every remaining [~] against a simple question: was this
  ever actually delivered, or only ever asked?** Any others found get their
  clocks reset the same way.
- **SLICING IS NOW ON THE UNTAUGHT-BUT-USED LIST alongside `zip` and LIST
  COMPREHENSIONS.** All three belong to 1.8. He has caught all three himself.
  **Do not assume any of them.** He was given the bare minimum on `word[:-1]` in
  S20 and nothing more.
- **THE FIVE CHECKS (1.7.11) MUST BE REQUIRED ON EVERY DRILL** until he runs
  them without being asked. It transferred on first use, which is encouraging,
  but one transfer is not a habit.
- **THE IDENTITY-VALUE RULE** (`0` for `+`, `1` for `*`, `[]` for concat) should
  be re-tested **AS A RULE**, not as three worked examples.
- The three-error set (`TypeError` / `NameError` / `UnboundLocalError`) is still
  untested cold. **Re-test them MIXED, never singly** — discrimination has
  always been the failure mode, not definition.
- The modulo identity in SYMBOLIC FORM is still owed cold. TEXT MODE, low
  priority.
- The in-place-mutator ROSTER is still not owned; the DISCRIMINATOR is [x].
  **1.8 settles the roster — do not re-drill it before then.**
- `str` immutability is an **[x] CANDIDATE** — one clean later-day pass
  promotes it. `None` / `is None` and `bool("False")` remain [~].
- Governance/format requests mid-session → PARK, close material, write at end.
- **First monthly gauntlet: end of August 2026**, carrying the strict-legend
  audit of every remaining [x] in Layer 1. Sacred. **Flag the `if`/`elif`/`else`
  promotion and the S18 exception-triad promotions specifically.**
- **31 AUG: the RE-BASELINE arithmetic is formally due.** Compute observed
  throughput over the four preceding weeks, derive the honest completion date,
  and write it into the master file whatever it says.

Every teaching block shows full runnable source alongside any output.
Session 21 closes with a ~30-second spoken summary from memory.


## TERM RE-TEST QUEUE (live — the vocabulary spaced-retrieval track)
Fire these cold at session open. Student defines from memory; "gap" if empty.
**NOT RUN IN S17 — interval gate. Everything below carries its S16 due date.**

| Term | Decode hook / one-line mechanism | Seeded | Latest result | Next cold-tax due |
|---|---|---|---|---|
| coercion | coerce = force; Python silently forcing one type into another where safe (`1 + 2.0 → 3.0`) | S12 | **S16 PASS cold — "forcefully... ek tarah ki implicit conversion". Name-decode intact. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| ValueError | value wrong, type OK; `int("2.5")` | S12 | **S18 PASS COLD, LATER-DAY, IN MIXED ORDER — and this is the single most important result in the file. He gave `int("335")`/`int("2.5")` as the value-is-bad case with the label attached, and the `NameError` conflation that failed THREE TIMES in S16 did not recur. Self-rated 8/10 before the verdict. PROMOTED.** | **[x] — 1-month re-test ~10 Sep** |
| TypeError | operation doesn't exist between these types; `"5" + 3` | S12 | **S18 PASS COLD again inside the mixed triad — string plus integer, label correct. One precision fix repeated from S16: Python does not "guess", it REFUSES, because it cannot know whether you mean `8` or `"53"`. Holds.** | **[x] — 1-month re-test ~10 Sep** |
| truncation | truncate = cut off; `int()` drops decimal toward zero | S12 | S13 PASS | ~12 Aug |
| floor division | `//` floors toward −∞; `-7//2 → -4` | S12 | S13 PASS | ~12 Aug |
| alias | two names, one object; `b = a` never copies | S10/S12 | S13 PASS | ~12 Aug |
| rebind | `=` points a NAME at a (possibly new) object | S12 | S13 PASS | ~12 Aug |
| operand | the value an operator acts on | S12 | S13 PASS | ~12 Aug |
| expression vs statement | expression evaluates to a value; statement performs an action | S12 | **S17 RE-CONFIRMED IN USE (not a formal test): he applied the distinction correctly and unprompted to explain what ternary produces. The concept is load-bearing and holding.** | ~12 Aug |
| precedence | which operator runs first, by RANK not position | S12 | S13 PASS | ~12 Aug |
| associativity | direction when ranks tie; `**` is right→left | S12 | S13 PASS | ~12 Aug |
| short-circuit | `and`/`or` stop the moment the result is settled; return the OPERAND | S13 | **S16 PASS cold, textbook-clean — including the return-the-VALUE subtlety, unprompted. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| modulo identity | `a == b * (a // b) + (a % b)`; sign follows the DIVISOR | S13 | **S18 SPLIT AGAIN, and honestly so. Asked for the symbolic form cold he said plainly he had NOT memorised the formula and offered to demonstrate the mechanism instead — which he then did, in TEXT, on `a = 17, b = -5`, A NEGATIVE DIVISOR HE CHOSE HIMSELF because it was harder. `a // b = -4` correct with flooring toward −∞; `r = -3` correct; the identity closed. BUT the middle step ran BACKWARDS (he guessed `r` first, then reasoned to the quotient), and the word `quotient` was used loosely for the raw division. Self-rated 9/10. NOT PROMOTED — the mechanism is [x]-grade, the SYMBOLIC FORM has still never been produced cold.** | **[~] — re-test the FORMULA FORM alone, TEXT MODE. Lower priority than `traceback` and iterator causation.** |
| control flow | steering which line runs next | S14 | S14 PASS (name-decoded cold) | ~15 Aug |
| conditional | code gated on a condition | S14 | S14 PASS | ~15 Aug |
| truthy / falsy | empty/zero = falsy, everything else = truthy | S14 | S14 PASS (all three cases derived unaided) | ~15 Aug |
| block vs frame | a block creates NO scope; only a FUNCTION CALL creates a frame | S14 | S14 PASS (student self-caught the wrong-domain reflex) | ~15 Aug |
| **indentation** | **the spacing that DELIMITS a block after the colon opens it** | **S15** | **S16 PASS cold, clean. PROMOTED. ⚠ S17 NOTE: do NOT re-test this by asking him to TYPE indented code — he cannot enter tabs in this channel. Test it by asking him to state the nesting in words. See S17 rule 3.** | **[x] — 1-month re-test ~9 Sep** |
| **iterable** | **able-to-be-iterated; hands you an iterator when asked. list, str, dict, tuple, range. REUSABLE.** | **S15** | **S16 PASS cold with full mechanism and examples. ⚠ THE MENTOR LOGGED A FALSE SLIP HERE — see the TRANSCRIPTION-ARTIFACT rule. NO retention failure occurred. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| **iterator** | **the nozzle: gives the next item on demand, raises StopIteration when exhausted. Holds FORWARD-ONLY state. CONSUMED.** | **S15** | **S16 PASS on mechanism and on the reuse contrast. CAUSATION still [gap] — see next row.** | **[~] — causation only** |
| **StopIteration** | **the signal raised when an iterator is exhausted; `for` catches it internally and stops quietly. A SIGNAL, NEVER A VALUE — it is never bound to a name.** | **S15** | **S18 PASS COLD on the CATEGORY, which was the exact thing S16 got wrong ("ek state"). Asked what category of thing it is, he said: an exception. Self-rated 7/10 alongside exceptions-are-signals. PROMOTED. ⚠ TRANSCRIPTION NOTE: the channel rendered his spoken "StopIteration" as "stock attrition" — read through it, nothing was logged.** | **[x] — 1-month re-test ~10 Sep** |
| **forward-only state (iterator causation)** | **an iterator holds a position that only ever moves forward. THAT is why it cannot rewind and is consumed — NOT because it yields one item at a time.** | **S15** | **S19 PASSED ON FIRST ATTEMPT — THE FIRST TIME IN FOUR ATTEMPTS ACROSS FOUR SEPARATE DAYS. Fired bug-first per the standing instruction (hoisted `it = iter(range(2))` above a nested loop) and he gave the CORRECT causation unaided: "forward-only state, moves forward only, can't rewind." He did NOT reach for "one item at a time", which had beaten him in S15, S16 and S18. THE BUG-FIRST METHOD IS NOW VINDICATED TWICE — never open this item with the definition. Self-rated 4/10, and that rating is the reason it does not promote: a correct answer he does not trust is not yet owned. S18 FAILED ON FIRST ATTEMPT FOR A THIRD TIME — he went straight back to "ek baar mein ek item deta jaata hai", the exact wrong causation. Retaught against the S16 code-as-bug image (hoisted `it = iter(range(2))`) rather than the definition, and the teach-back then came back CORRECT: forward-only, consumed is a STATE, the pointer has moved on. One over-claim corrected — he added "saare elements khatam ho gaye", which is not required; partial consumption still counts. Self-rated 3/10.** | **[~] — STILL TOP PRIORITY. Failed on three separate days now. Do NOT open with the definition; open with the bug.** |
| **range** | **a stretch of numbers, start UP TO stop. HALF-OPEN (stop excluded) and LAZY (computed on demand). It is an ITERABLE, not an iterator.** | **S15** | **S16 PASS cold and COMPLETE — the strongest single answer of the term-tax. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| **traceback** | **the crash report the interpreter writes when an exception goes uncaught; last line names the exception. Goes to the error stream.** | **S15** | **S19 PASS COLD on a genuine later day, and the improvement is real: he gave the TRIGGER correctly unaided ("exception uncaught → traceback generated"), which is the exact part he missed in S18. The STREAM was a gap, honestly declared, and after teaching he restated it correctly — error stream / stderr, last line names the exception. Self-rated 6/10, DOUBLE his S18 rating of 3/10. NOT PROMOTED — 6/10 is below the bar and this label is arbitrary rather than decodable, so it stays in brute-force spaced repetition. S18 PARTIAL. He had runtime and "tells you which line" but MISSED THE TRIGGER — that a traceback is produced only when an exception goes UNCAUGHT. Retaught with an uncaught-error handle; on the re-ask the transcription garbled badly, the question was re-posed cleanly with an "un-" hint, and he then produced `uncaught` himself and stated it correctly. Self-rated 3/10 with the honest rider that he will need to hear it repeatedly.** | **[~] — PRIORITY, joint-first with iterator causation. His own 3/10 is the targeting signal.** |
| **NameError** | **named after the part that broke: the NAME does not exist. Raised when you use a name that was never created.** | **S15** | **S18 PASS COLD, UNCUED, IN MIXED ORDER — "name used but never defined". This is the item the file has called its single weakest label since S16, and it is now clean on genuine later-day evidence. Self-rated 8/10. PROMOTED.** | **[x] — 1-month re-test ~10 Sep. ⚠ Re-test it MIXED with `ValueError`, never alone; the failure mode was always discrimination, not definition.** |
| **function scope, not block scope** | **`for`/`if`/`while`/`try` create NO new scope. Only a `def` does. Names born inside a block survive after it.** | **S15** | **S16 PASS cold on a genuine later day — BOTH `print(last)` and `print(i)` → 2. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| **`print()` — `sep` and `end`** | **`print` is a function returning `None`. It calls `str()` on each argument. `sep` (default `" "`) goes BETWEEN items; `end` (default `"\\n"`) goes after. Both are changeable.** | **S16** | **Return-`None` derived cold. `sep` was a GAP. `end` right mechanism, wrong symbol (`/n` for `\\n`). Post-teaching check PASSED.** | **~12 Aug** |
| **`while`** | **repeats while a CONDITION stays true. `for` asks an iterator for the next item; `while` re-evaluates a condition.** | **S16** | **S17: [PREDICT] PASS on the infinite-loop case, with the full mechanism stated unprompted — `i` never increments, so `i < 5` is permanently true. Same-day, so not promotable.** | **~12 Aug** |
| **`break` / `continue`** | **`break` exits the innermost loop entirely. `continue` abandons THIS ITERATION only and jumps back to the condition check. Loop lives; iteration dies.** | **S16** | **S17 [RECALL] on `break`: PASS — "loop khatam, bahar nikal jayega", and he volunteered the INNERMOST-ONLY precision for nested loops unprompted. Same-day, so [~] stands. `continue` was re-stated but not tested.** | **~12 Aug — `continue` still owes a RECALL test** |
| **chained comparison** | **`5 > 3 > 1` expands to `5 > 3 and 3 > 1`, but the MIDDLE OPERAND IS EVALUATED ONCE. Not plain syntactic sugar.** | **S16** | **PASS both halves, including `f() > 3 > 1` calling `f()` exactly once. PROMOTED.** | **[x] — 1-month re-test ~9 Sep** |
| **loop `else`** | **runs if the loop finished WITHOUT hitting `break`. Nothing to do with `if`/`else` — do not read it as "otherwise".** | **S16** | **S17 EARNED BY CONTRAST, which was the owed repair for the S16 prerequisite breach. After writing the found-flag version himself he derived the purpose unprompted: the flag only ever answers "did the loop finish without breaking?", and Python already knows that. Rule re-stated and confirmed.** | **~12 Aug** |
| **`pass`** | **a no-op statement. Does nothing; exists only to satisfy the rule that a block opened by a colon cannot be empty. NOT `continue` (skip to next iteration) and NOT `break` (exit the loop).** | **S17** | **[PREDICT] PASS — he supplied the function-stub use case from prior exposure ("classes banate hain tab dekha hai") and stated the mechanism correctly: fills the block, tells Python to do nothing. Same-day, [~].** | **~12 Aug** |
| **ternary / conditional expression** | **`x if condition else y`. An EXPRESSION — it evaluates to a value, so it can go anywhere a value can go (a variable, a `print` argument, inside a list). Read from the middle outward.** | **S17** | **[PREDICT] PASS, and a good one — asked how it differs from `if`/`else`, he went straight to the right axis: the `if` block executes, whereas the ternary PRODUCES something which then gets bound to a name. Same-day, [~].** | **~12 Aug** |
| **`elif`** | **else-if, contracted. A CHAIN checked top to bottom; the FIRST true condition wins and the rest are not evaluated at all. `else` is optional and catches everything remaining.** | **S17** | **[RECALL] PASS COLD — see the re-test queue row. This one IS promotable: it was owed from S16 and answered unaided, including the part that mattered (with `x = 20` the `elif` is never evaluated). Self-rated 10/10.** | **[x] — 1-month re-test ~10 Sep** |
| **mutating vs non-mutating methods** | **A method that changes the object in place returns `None`; a method that returns a new object leaves the original untouched. `sort`/`sorted` and `reverse`/`reversed` are the deliberate name-pairs proving it.** | **S17** | **S18 [DRILL] targeted at `reverse` and `sort`: all three answers CORRECT (`x` → `None`, `y` → `None`, `l` → `[1,2,3]`) — but he said in writing that he still did not know whether `reverse` mutates and had ASSUMED it. Correct output, un-owned roster. He then challenged the generalisation itself and was RIGHT: mutable-type methods do NOT all return `None` (`pop`, `index`, `count` return values). Rule narrowed to IN-PLACE MUTATORS specifically. Self-rated 10/10 concept, roster still soft.** | **[~] on the ROSTER; the DISCRIMINATOR is now [x]-grade. Re-test by naming in-place mutators cold, not by classifying.** |

## RE-TEST QUEUE (live — update every session)

| Item | First taught | Latest re-test | 1-month re-test | Status |
|---|---|---|---|---|
| Frames: definition and three contents | S6 | S14: held WITH A HINT for the exact three | due 29 Aug 26 | [~] hint ≠ pass; re-test |
| `<module>` / script entry point | S5, retaught S6 | S14 PASS cold | due 29 Aug 26 | [~] strong |
| Running vs paused frames | S6 | S14 completed | due 29 Aug 26 | [~] |
| Why a stack not a queue | S4, retaught S6 | S14 PASS cold | due 29 Aug 26 | [~] strong |
| Namespace vs frame | S6 | S14: NOT unaided, retaught | due 29 Aug 26 | [~] |
| Rebinding vs mutation (left-of-`=` rule) | S4 | **S16 PASSED cold — immutable→rebind, mutable→mutate, stated unprompted with the object/name distinction intact** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| `==` vs `is` | S2/S3, FAILED S7 | **S16 PASSED cold at last — `==` compares value, `is` compares identity, given as `id(a) == id(b)`. Owed since S7.** | due ~9 Sep 26 | **[x] PROMOTED S16 — longest-outstanding item in the file, now closed** |
| Execution pipeline: source → bytecode → PVM | S3 | FAILED S7 | pending | [~] DUE re-test |
| REPL vs script | S4 | FAILED S7 | pending | [~] DUE re-test |
| `str` immutability + methods return new objects | S7 | **S17 SUPPORTING EVIDENCE (not a formal cold test): in the method drill he classified `s.upper()` as returning a new string at 10/10 and, when asked WHY strings cannot have a mutating method, gave immutability as the reason. Consistent with S9's four cold predictions.** | due 29 Aug 26 | **[x] CANDIDATE — one clean later-day pass promotes** |
| `None` / `is None` / None vs 0 vs False | S9 | S10 same-day only | due ~29 Aug 26 | **[~] needs unaided from-cold re-test** |
| Type conversion: int/str/float/bool + traps | S10 | S12 cold pass on the hinge | due ~1 Sep 26 | **[~]; `bool("False")` and `10/2`-float STILL OWED** |
| Implicit vs explicit conversion / `"5"+3` TypeError | S10 | **S16 PASSED cold; "no coercion happens here, that's why it errors" — correct** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Mutability, aliasing, mutable args in functions | S10 | **S16 PASSED cold — change visible through both names because the change happened in the OBJECT, not the name** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Mutable default argument trap + `None` sentinel fix | S10 | S12 cold: trap+fix correct | due ~1 Sep 26 | **[~]; trap strong, WHERE-it-lives weak** |
| Conversion returns a NEW object; original UNTOUCHED | S10 | **S16 PASSED cold for the general case — the immutable-optimisation follow-up (`tuple(t)` may return the SAME object) was new material. NOT PROMOTED — deliberately.** | due ~9 Sep 26 | **[~] the immutable-optimisation half is owed a cold test** |
| Mutating methods return `None` (`result=q.append(4)`) | S11 | **S18: the targeted `reverse`/`sort` [DRILL] ran and all three answers were correct, INCLUDING `l.append(5)` → `None`, `s.upper()` → new string and `l.pop()` → the removed element in the second half. But he stated in writing that `reverse` was an ASSUMPTION, not knowledge. The concept is owned; the roster is not. ⚠ `d.clear()` was also asked and he correctly refused it as never-taught — MENTOR ERROR, see Teaching Mistakes; nothing logged.** | due ~10 Sep 26 | **[~] CONCEPT [x]-grade, ROSTER not owned. 1.8 is where the roster gets settled.** |
| WHERE the default lives: `__defaults__` NOT the frame | S10 | **S19 NEAR-PASS — the first time it has ever come back. Asked in isolation he produced the name `__defaults__` correctly. ⚠ TRANSCRIPTION ARTEFACT, SECOND OF THE ARC: the channel rendered his spoken "dunder" ambiguously, the mentor briefly questioned a correct answer, then self-corrected and apologised. NOTHING LOGGED AGAINST HIM — the S16 rule worked. Self-rated 7/10. A SEPARATE SLIP DID occur later in the same block: asked where `__defaults__` LIVES, he said "module ki namespace mein". Wrong. Repaired across three passes and he closed it himself — *"wo dunder default us object ka attribute hai na?"* — which is the correct statement. REPAIR HANDLE THAT LANDED: **shelf par naam, dabbe ke andar attribute** — the NAME sits in the module namespace and points at the object; the ATTRIBUTE lives inside the function object. S18 COLD MISS — FOURTH OCCURRENCE. Tested in isolation at last, in its natural home (1.7 default arguments), after being untouched since S12. He answered with the FUNCTION'S LOCAL NAMESPACE — the call-time construct — rather than `__defaults__`, an attribute that lives on the function OBJECT from definition time onward. Retaught with the durable-vs-momentary contrast: `__defaults__` is built at `def` time and persists; the local namespace is built at call time and dies with the call.** | due ~10 Sep 26 | **[~] FOURTH SLIP. It is no longer merely the weakest item — it is the only item in the file that has never once been produced cold. Re-test it EVERY session until it lands.** |
| `//` with NEGATIVE numbers vs `int()` truncation | S12 | **S16 PASSED cold: `-7 // 2 → -4`, floors toward −∞ stated unprompted.** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Shallow vs deep copy (`id()` proof) | S11 | **S16 PASSED cold with a self-built nested example.** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Comparison / logical operators → boolean | S12 | **S16: `10 / 2 → 5.0` and `a == b` / `a is b` both PASSED cold.** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Operator precedence + associativity | S12 | **S16 DRILL PASSED cold in text: `2 ** 3 ** 2` → 512, right-associativity named explicitly** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Augmented assignment `+=` | S12 | **S16 PASSED cold — mutable mutates, immutable rebinds** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| Membership `in` / `not in` | S13 | same-day only | due ~5 Sep 26 | [~] |
| Short-circuit evaluation | S13 | S14 PASS cold | due ~3 Sep 26 | [~] one more pass promotes |
| `%` modulo — value AND sign on negatives | S13 | **S16 PASSED COLD TWICE on a later day. No longer weak.** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| `**` exponentiation + right-to-left | S13 | **S16 DRILL PASSED cold, no hedging** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| `if` block scope — a block creates no frame | S14 | **S16 PASSED cold on a genuine later day, both halves** | due ~9 Sep 26 | **[x] PROMOTED S16** |
| **ITERATION PROTOCOL: `iter()` once, `next()` per pass, StopIteration ends it** | **S15** | **same-day PASS only** | **due ~8 Sep 26** | **[~] SAME-DAY ONLY. Needs a genuine later-day cold pass.** |
| **Iterables are REUSABLE, iterators are CONSUMED (forward-only state)** | **S15** | **S18: the CAUSATION FAILED A THIRD TIME on first attempt ("one item at a time"), was repaired with the code-as-bug image, and the teach-back was then correct. Self-rated 3/10.** | **due ~10 Sep 26** | **[~] STILL THE MOST STUBBORN ITEM IN THE FILE. Three failures on three separate days.** |
| **`range()`: half-open and lazy; an ITERABLE not an iterator** | **S15** | **S16 PASSED cold on a later day, including the memory rationale for laziness** | **due ~9 Sep 26** | **[x] PROMOTED S16** |
| **Python has FUNCTION scope, not BLOCK scope — `i` survives the loop as 2** | **S15** | **S16 PASSED cold — BOTH prints → 2** | **due ~9 Sep 26** | **[x] PROMOTED S16** |
| **Exceptions are SIGNALS, never bound to a name** | **S15** | **S18 PASS COLD on a genuine later day — "signal hote hain jo Python ko batate hain ki yahan galti hui hai", explicitly not a value that sits somewhere. Full gap in S16, clean in S18. Self-rated 7/10 before the verdict.** | **due ~10 Sep 26** | **[x] PROMOTED S18 — the weakest cluster in the file has started to come good** |
| **A name created only inside a loop body does not exist if the body never ran (`range(0)` → NameError)** | **S15** | **S16 SPLIT — MECHANISM PERFECT, LABEL WRONG (said `ValueError`).** | **due ~9 Sep 26** | **[~] mechanism [x]-grade; the LABEL needs the re-test** |
| **`traceback` — each line is ONE LIVE FRAME; the whole thing is a printout of the STACK at the moment of the crash** | **S15 asked, S16 asked, S18 asked, S19 asked — ⚠ PROPERLY TAUGHT ONLY IN S20** | **S20 SELF-RATED 0/10, AND THE FINDING IS A MENTOR FINDING. It emerged that this item had been FIRED as a [RECALL] for three consecutive sessions and NEVER ACTUALLY TAUGHT — repeating a question is not teaching. THREE SESSIONS OF RECORDED "FAILURE" ON THIS ITEM WERE MEASURING A TEACHING GAP, NOT A RETENTION GAP. He could read the location half unaided ("the remaining part points to the fault happening in line 2") and correctly reported that `<stdin>` was meaningless to him. TAUGHT IN FULL: `<stdin>` is just the FILENAME SLOT (code from standard input, not from disk; `<string>` for `exec`, `<module>` for top level) — nothing deep. THE REAL CONTENT, which he did not have: EACH LINE IS ONE LIVE FRAME ON THE CALL STACK. That is why they repeat — line 2 did not fail 999 times, there were 999 frames all paused at line 2. A traceback is read bottom-up as "who called whom" in reverse; the bottom line is where the exception was raised, the lines above are the chain of callers. Demonstrated on a clean `a → b → c` chain. TIED TO HIS OWN WORK: when a traceback bottoms out in library code, the useful line is the LOWEST ONE NAMING HIS OWN FILE. [TEACH-BACK] on the ordering was CORRECT.** | **due ~16 Sep 26 — CLOCK RESET** | **[~] RE-ENTERS AS NEWLY-TAUGHT MATERIAL. Do not carry the S16/S18/S19 "failures" against him; they were not valid measurements. Next cold test is the FIRST honest one.** |
| **`print()` returns `None`; `sep` and `end` are parameters** | **S16** | **return-`None` reasoned out cold; `sep` GAP; `end` symbol wrong (`/n`); post-teach check PASSED** | **due ~9 Sep 26** | **[~]** |
| **`while` — condition re-checked before every pass** | **S16** | **S17: [PREDICT] PASS on the missing-increment infinite loop. He named the exact cause unprompted — no increment in the body, so `i` stays 0 and the condition never turns false. Same-day.** | **due ~9 Sep 26** | **[~] strong** |
| **`continue` in a `while` loop skips the state update — the classic infinite loop** | **S16** | **FOUND UNPROMPTED in S16 with the correct reason. Re-stated in S17 as a warning attached to the `pass`/`continue`/`break` contrast; NOT re-tested.** | **due ~9 Sep 26** | **[~] strong** |
| **Nested loops — inner runs to completion for every outer value; a FRESH iterator each pass** | **S16** | **PREDICT PASS on all three parts.** | **due ~9 Sep 26** | **[~]** |
| **Loop `else` — runs only if the loop finished WITHOUT `break`** | **S16** | **S17: THE OWED EARN-IT EXERCISE COMPLETED. He wrote the found-flag equivalent himself, then derived WHY loop `else` exists — the flag is only ever recording "did the loop finish without breaking", which the interpreter already knows. The S16 prerequisite breach is now repaired.** | **due ~9 Sep 26** | **[~] — now taught in the right order** |
| **THE FOUND-FLAG PATTERN — search a sequence, report found / not found** | **S17** | **WRITTEN BY HIM, unaided on structure: `flag = False` before the loop; `flag = True` + `print` + `break` on the hit; `if not flag` after the loop. Four iterations, all fixes were syntax/idiom (bare names for strings, missing colon, `== False`) or channel artefacts (indentation), NOT structure. Same-day.** | **due ~10 Sep 26** | **[~]** |
| **`pass` — the no-op that satisfies a non-empty block** | **S17** | **[PREDICT] PASS with a use case supplied from his own prior exposure. The `pass` vs `continue` vs `break` three-way contrast was taught alongside it and is the part most likely to blur — test THAT, not `pass` alone.** | **due ~10 Sep 26** | **[~]** |
| **Ternary / conditional EXPRESSION — `x if cond else y`** | **S17** | **[PREDICT] PASS. He identified the expression-vs-statement axis himself: the ternary produces a value that gets bound, the `if` block just executes. Caveat taught: use it only when both branches select a simple value.** | **due ~10 Sep 26** | **[~]** |
| **`if` / `elif` / `else` AS A CHAIN — first true condition wins, the rest are never evaluated** | **S14 (`if`), S17 (`elif`/`else`)** | **S17 [RECALL] PASS COLD, and this one IS later-day evidence: the question was posed at the end of S16 and went unanswered, so it was genuinely untested when he answered it. `x = 5` → "B", with the skip stated; and with `x = 20`, "A" prints and `elif x > 3` is NEVER EVALUATED. Self-rated 10/10 BEFORE the verdict, per rule 3. ⚠ HONEST CAVEAT: he asked to be re-taught `elif` before attempting, so the chain rule was explained minutes earlier. The PROMOTION IS AWARDED on the strength of the answer and his rating, but flag it for the August gauntlet.** | **due ~10 Sep 26** | **[x] PROMOTED S17 — the last owed item from S16** |
| **The MUTABLE/IMMUTABLE DISCRIMINATOR — how to tell mutating from non-mutating without a roster** | **S17** | **S18 PASS COLD, AND BETTER THAN A PASS. He applied it to unseen methods correctly (`append` → `None` because in-place, `s.upper()` → new string because `str` is immutable, `pop` → returns the removed element) AND HE FOUND THE HOLE IN THE MENTOR'S OWN FORMULATION: "mutable type ke saare methods mutate karenge, yeh main general rule nahi maanunga." Correct. The rule is not about MUTABLE TYPES, it is about IN-PLACE MUTATORS; `pop`, `index` and `count` are counter-examples. Rule narrowed in session. Self-rated 10/10 on concept.** | **due ~10 Sep 26** | **[x] PROMOTED S18 — and note HOW it was earned: by him correcting the model, not by him reciting it** |
| **CELL CAUSATION — WHY five calls give five non-colliding values** | **S19** | **S20 CORRECT UNAIDED FROM COLD — first time in five attempts across two days. "each loop iteration a new function object with a new cell... the five values are not overwriting each other because they are all associated with five different objects." TWO CORRECTIONS: (a) he attributed the new object to THE LOOP; it is THE CALL — five separate `make_counter(3)` calls on five lines give five cells with no loop anywhere. (b) LABEL SLIP: "content cell" — it is a CELL; `cell_contents` is an attribute ON the cell. Self-rated 5/10.** | **due ~16 Sep 26** | **[~] NOT PROMOTED on his 5/10 — but see the calibration note: this is the file's FIRST recorded UNDER-rating, ~85% correct and rated 5.** |
| **CLOSURE DEFINITION — stated as one line joining free variable, cell, function object** | **S19** | **S20 COLD ATTEMPT self-rated 4/10. Substance largely right — nesting, free variable, binding at function-object creation, persistence — but he did NOT name the CELL, and "retains itself during different sessions" is wrong wording for "survives after the enclosing frame has died". A SECOND, stronger interview-style version followed, but AFTER the cell and the frame-death were handed to him, so it is SCAFFOLDED and not evidence. Corrections owed on re-test: "free VARIABLE" not "free value"; `__closure__[0]` is a CELL, the value is `.cell_contents`; `__closure__` is `None` (not an empty tuple) when there are no free variables; and the BINDING HAPPENS WHEN `def` RUNS, not at call time — he had this in attempt one and lost it in attempt two.** | **due ~16 Sep 26** | **[~] re-test COLD. His 4/10 was well calibrated.** |
| **RECURSION — base case, recursive case, frames of the same function stacked** | **S20** | **taught S20; [PREDICT] on value-returning recursion PASSED both parts (`total(4)` → 10, deepest frame `n=0` returns 0). Same-day only.** | **due ~16 Sep 26** | **[~]** |
| **PRE-ORDER vs POST-ORDER — work before the call vs after it** | **S20** | **S20 [PREDICT] FAILED: answered `2 1 0` for the post-order countdown (actual `liftoff 1 2 3`). ROOT CAUSE: imagined ONE mutating `n` instead of four frames each holding its own. ⚠ THE SAME ISOLATION PRINCIPLE HE HAD CORRECTLY EXPLAINED FOR CELLS MINUTES EARLIER — owned in one container, dropped in another. Also printed `0`, which never prints.** | **due ~16 Sep 26** | **[~] PRIORITY — re-test as a TRANSFER question, not a recursion question** |
| **THE IDENTITY-VALUE RULE — a base case returns the identity for the operation (`0` for `+`, `1` for `*`, `[]` for concat)** | **S20** | **taught S20 across three instances; not tested as a RULE** | **due ~16 Sep 26** | **[~] test it as a RULE, not as three examples** |
| **TERMINATION — base case must EXIST and the step must LAND on it** | **S20** | **S20 BUG HUNT PASSED: found the `first_char("")` non-shrinking input via check 2 and connected it to the step never reaching the base, unaided.** | **due ~16 Sep 26** | **[~] strong** |
| **PRINTER vs CALCULATOR — does this function print, or return?** | **S20** | **S20: his `count_down_by` mixed the two (`return 0, step` — a tuple nobody uses). Base case and step-passing both correct unaided. Retaught with the testability argument.** | **due ~16 Sep 26** | **[~]** |
| **PURE FUNCTIONS vs SIDE EFFECTS + the disguised mutator** | **S10 pre-load, TAUGHT S20** | **S20 [PREDICT] on `scale` — ALL THREE LINES CORRECT and he named the mutation and aliasing before being asked. ⚠ But he then asked what "pure" meant — the definition had been in the block lost to the doubt-gate breach.** | **due ~16 Sep 26** | **[~] mechanism strong, LABEL owed** |
| **THE FIVE CHECKS — boundary, empty, one, assumed type/sign, step-meets-base** | **S20** | **S20: transferred on first use — found the planted bug via check 2 with the correct mechanism. Same-day.** | **due ~16 Sep 26** | **[~] REQUIRE IT ON EVERY DRILL until he runs it unprompted** |
| **ARGUMENT COUNT AND RETURN VALUE ARE UNRELATED** | **S20** | **NEW — arose from his own written reasoning ("a function call with two arguments so returning a none will not cause problem"). A category confusion, not a slip. `None` is only ever a problem AT THE POINT OF USE, in the CALLER.** | **due ~16 Sep 26** | **[~] re-test — this is the implicit-`None` trap from 1.7.3 in a new dress** |
| **TRACE-TAIL TRUNCATION — student-side pattern, named S16** | **S16** | **S17: DID NOT FIRE. Required to state the final cycle on the `while i < 5` trace, he traced all five cycles and named the terminating check correctly (`i` = 5, `5 < 5` false, body skipped, 5 never printed).** | **due ~9 Sep 26** | **[~] WATCH — keep requiring the FINAL cycle explicitly, but the countermeasure is working** |


## WATCH AREAS
- Knows bits and pieces — needs structured foundation, not patches
- Risk of over-relying on AI tools early — enforce the solo-first rule
- **EDGE CASES AND FAILURE MODES — PROMOTED FROM A ONE-LINE WATCH ITEM TO A
 TAUGHT SUBSECTION (1.7.11) IN S20, AT HIS OWN REQUEST.** This line had sat
 here since the file was created, describing a gap that was never actually
 addressed by anything. **He closed that hole himself**, naming the deficit
 precisely and asking for it to be taught rather than merely watched.
 **HIS OWN DIAGNOSIS, unprompted, and it is the sharpest self-assessment in
 the file:** *"I just did the things at surface level and always do that and
 that's why i was not able to catch the edge case."*
 **THIS IS THE SAME ROOT CAUSE AS RIGHT-ANSWER-WITHOUT-MECHANISM, VIEWED FROM
 THE OTHER END.** That pattern names the symptom that shows up in the ledger;
 this names the habit that produces it — the first plausible answer is treated
 as the finished answer and the probing pass never runs.
 **THE COUNTERMEASURE IS NOW MECHANICAL AND IS S20 RULE 3
 (DEPTH-BEFORE-ANSWER): he runs the five checks on his own code before
 submitting it, and a boundary value is always tested first.** The method
 transferred on first use in the same session, which is encouraging, but
 **one transfer is not a habit — require the five checks explicitly on every
 drill until he runs them without being asked.**
- Known tendency to jump ahead or switch resources — **OBSERVED S17 after
 eleven clean sessions. See LEARNING PATTERN TO ACTIVELY CORRECT for the
 instance and how it was handled. It fired at the moment a unit felt easy
 ("yeh sab to mujhe pehle se aata tha"), not at the moment it felt hard —
 worth noting, because the file has always framed this pattern as a
 friction response. IT IS ALSO A BOREDOM RESPONSE. Watch for it on easy
 material as well as hard.**
 **S18 RAN THE PATTERN IN REVERSE, AND IT DESERVES ITS OWN LINE.** Offered
 recursion three times — the single topic he has most wanted since S17 — he
 declined each time, first to finish arguing about why closures exist at all,
 and then to insist closures be RESTARTED FROM SCRATCH in text rather than
 tagged as taught. **He turned down the thing he wanted in order to protect
 the integrity of the thing he had just been given.** That is the exact
 opposite of the self-sabotage pattern this section exists to counter.
 **Read it as the pattern weakening rather than as a one-off, but do not
 declare it closed on one instance.**
- **TERM / LABEL RETENTION — FIRST-CLASS WATCH AREA (S12, named by the
 student himself). S15 CONFIRMS IT SHARPLY.** In the closing spoken summary
 he had every mechanism right and reached for the wrong LABEL three times:
 "margins/spacing" for **indentation**, "iterative" for **iterable**, and a
 garbled attempt at **StopIteration**. This is the exact profile the Term
 Retention System was built for — mechanism retained, label dropped. The
 countermeasure is unchanged (name-decoding, term-tax, no naked terms).
 **S18 IS THE FIRST REAL EVIDENCE THAT THE COUNTERMEASURE WORKS.** The
 exception LABELS — the exact failure this watch area was opened for, and the
 ones conflated three times in a single S16 session — came back cold, in
 mixed order, on a genuine later day, and were correct. `NameError`,
 `ValueError`, `TypeError`, and the `StopIteration` CATEGORY all held.
 **Six sessions of name-decoding and spaced term-tax produced this. Do not
 quietly drop the mechanism now that it is paying.** The residue is narrower
 than it was: `traceback` and `__defaults__` are the two labels still loose,
 and both are ARBITRARY rather than decodable, which is consistent with the
 S12 diagnosis — **what he drops is the label that cannot be re-derived from
 its own name. Those two belong in brute-force spaced repetition, not in
 name-decoding.**
- **REASONING HYGIENE / ABSENT CROSS-CHECK — recurring, structural.**
 Not a problem in S15, S16 or S17.
- **WRONG CAUSATION ATTACHED TO A RIGHT ANSWER — S15 INSTANCE.** He stated
 correctly that an iterator is consumed, but justified it with "because it
 gives one item at a time." That is not the cause — a spoon dispensing one
 item at a time could rewind. The cause is **forward-only state: the
 iterator holds a position that only ever moves forward**. Corrected in
 session. This is the right-answer-wrong-model family (now ~7 occurrences)
 and the standing instruction holds: never accept a correct conclusion
 without auditing the mechanism underneath it.
 **NOT OBSERVED IN S17.** **BUT IT FIRED AGAIN IN S18, ON THE SAME ITEM AS
 S15 AND S16 — the iterator. Asked what "consumed" means he went straight
 back to "ek baar mein ek item deta jaata hai".** That is now a THIRD failure
 of the same causation on a third separate day, and it is the clearest
 evidence in the file that **a repaired mechanism does not stay repaired if
 the repair was delivered as a DEFINITION.** The fix that worked both times
 was the same one: the S16 code-as-bug image (a hoisted iterator making a
 nested loop's inner body run once and then silently never again).
 **STANDING INSTRUCTION: for this item, never lead with the definition. Lead
 with the bug, make him diagnose it, and let the causation fall out.**
- **Rule application by surface syntax / wrong domain instead of semantic
 structure — THE MOST PERSISTENT STRUCTURAL FLAW** (S4, S5, S6, S7, S9,
 S12, S13, S15). **S17 INSTANCE, ONE, AND IT IS A CLEAN EXAMPLE OF THE
 FLAW'S SIGNATURE: `l.reverse()` classified as returning a new list.** The
 surface cue is the word "reverse", which sounds like it produces something;
 the semantic structure is that `reverse` is a plain-named method on a
 MUTABLE object, which by Python's own design convention mutates in place
 and returns `None`. **He rated it 5/10 himself** — the flaw fired exactly
 where he already suspected it would, which is the mitigating detail.
- **TRACE-TAIL TRUNCATION (named S16) — RESOLVED IN S17, PENDING A LATER-DAY
 RE-TEST.** In S16 he twice ended a loop trace one cycle early. In S17 he was
 explicitly required to state the final cycle, and did: he traced
 `while i < 5` cycle by cycle to the end and named the terminating check
 correctly — `i` becomes 5, the condition is re-evaluated, `5 < 5` is false,
 the body does not run, 5 is never printed. **Keep the countermeasure (require
 the FINAL cycle explicitly on every trace) until it survives a later-day
 test, but the pattern did not fire this session.**
- **STYLE HABITS NEED REPETITION, NOT EXPLANATION (NEW, S17).** `if flag ==
 False` → `if not flag` had to be issued three separate times, and the code
 came back with `== False` each time in between. He understood it the first
 time; understanding is not the mechanism here. **For idiom-level habits,
 stop re-explaining and instead require him to type the corrected line back
 once.**
- `==` vs `is` conflation — **CLOSED S16, promoted to [x].**
- Box model leak under pressure — S2, S6. Not observed S9–S17.
- "I got it" offered as evidence — refused cleanly whenever it appears.
- False attribution of a gap to the mentor — **S15, S16 and S17: every
 attribution was TRUE and upheld. He attributes accurately; when he says the
 mentor broke a rule, check the rule, because he is usually right.**


## CURIOSITY PARKING LOT
- venv and virtual environments (master Layer 1)
- VS Code extensions and best practices (master Layer 1)
- .ipynb notebooks vs .py files (master Layer 4)
- CPython's experimental JIT (Python 3.13+) — 1.13
- IEEE 754 float internals — PROMOTED to a definite 1.13 deep dive (S5)
- 32-bit vs 64-bit processors — 1.13
- `globals()` vs `locals()` at module level — still needs its formal drill
- Reading tracebacks like a senior engineer — **PARTIALLY DISCHARGED S15**
 (the term is now defined and the argument-evaluation subtlety taught);
 the full senior-level read stays parked for the exceptions work in 1.9
- When does Python actually generate .pyc files? — 1.10
- The GIL — working definition held; full mechanics in 1.13
- CONCURRENCY / THREADS — deferred to a concurrency block after Layer 1
- PYTHON CERTIFICATIONS — researched S11, NOT scheduled
- Garbage collection mechanics — parked for 1.13
- **S15 — `__iter__` / `__next__` as dunder methods, i.e. how an object
 DECLARES itself iterable, and generators as the lazy-iterator factory.**
 Level 3 material by the depth doctrine. Correctly out of scope now;
 lands in **1.13 (generators and iterators)** where it is already listed.
 Flag to the student when 1.13 opens that this is the promised payoff of
 the S15 protocol teaching.
- **NEW, S17 — RECURSION AND NESTED FUNCTIONS, requested by name.** He named
 these unprompted as the concepts he most wants to learn properly: *"function
 ke andar function, recursion type ke concepts mujhe acche seekhne hain."*
 **NOT parked indefinitely — both are already scheduled in 1.7, which is the
 very next unit.** Tell him so when 1.7 opens; the request is about to be
 met and that is worth saying out loud, because it converts his impatience
 into momentum. Nested functions land with closures; recursion has its own
 line item.
- **NEW, S17 — `reversed()` and `l[::-1]`.** Mentioned in passing as the
 non-mutating counterparts to `l.reverse()`. Slicing proper belongs to 1.8;
 do not open it early, but the name-pair (`sort`/`sorted`,
 `reverse`/`reversed`) is a legitimate hook to reuse there.

---

