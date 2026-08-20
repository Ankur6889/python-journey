# CURRICULUM.md — PYTHON LEARNING JOURNEY (Layer 0 / Python Core)
# ═══════════════════════════════════════════════════
# One of FOUR files (see RULES.md header for the loading protocol).
# THIS FILE: the full checklist, 1.1–1.13, with the strict [ ]/[~]/[x] marks
# and the per-item notes that justify each mark. Load it when a subsection
# opens or closes, or before changing any tick. Do NOT narrate sessions here;
# that goes to ARCHIVE.md. Live queues and the resume point are in STATE.md.
# LEGEND is in RULES.md and is strict: [x] = unaided, no notes, later day.
#
# STATUS AT SPLIT (16 Aug 2026, end of S20): 1.1–1.6 closed. 1.7 Functions
# active, four items remaining (`global`, `*args`/`**kwargs`, lambdas,
# docstrings). 1.8–1.13 not started. Bullet counts at split: 22 lines [x]
# (a few lines carry two [x] marks), 74 lines [~], 47 lines [ ].
# NOTE the size warning from the 16 Aug review: 1.8 and 1.12 are several
# times larger than 1.6; "0.4 of a subsection" is not a constant unit.
#
# VERSION: CURRICULUM 2026-08-16. Derived from python_learning_journey v16.
# ═══════════════════════════════════════════════════

## OVERALL CURRICULUM (reconciled with master, Session 6)
- Layer 1: Python Core Fundamentals ← ACTIVE. = master "Layer 0". Governs now.
- Layer 2: Software Engineering Habits → SUPERSEDED by master Layer 1
- Layer 3: Web & Data Fundamentals → CUT. Only HTTP/JSON awareness survives.
- Layer 4: Domain Libraries → SUPERSEDED by master Layers 4 and 5
- Layer 5: DSA + CS Fundamentals → SUPERSEDED by master Layer 8


## GRANULAR CURRICULUM

### LAYER 1 — Python Core Fundamentals

> **OUTSTANDING: strict-legend audit.** Every [x] awarded before the Session 6
> reconciliation was under the old looser definition. Do not trust them.
> **First task of the first monthly gauntlet: audit every remaining [x] in
> Layer 1 by cold re-test, and revert failures to [~].**

#### 1.1 How Python Runs Code
- [x] What happens when you run a .py file (Session 3)
- [x] The Python interpreter — what it is, CPython vs others (Session 3)
- [~] Compilation to bytecode (.pyc files) (DOWNGRADED S7)
- [~] The Python Virtual Machine (PVM) (DOWNGRADED S7)
- [~] The call stack (DOWNGRADED S6; rebuilt S6)
- [~] FRAMES — what a frame actually is (S14: held with a hint, not [x])
- [~] The module frame `<module>` (S14 PASS cold)
- [~] Running vs paused frames (S14 completed)
- [~] Why a stack and not a queue (S14 PASS cold)
- [~] `traceback.print_stack()` as a live verification tool
- [~] **TRACEBACK — what it actually is. DEFINED S15**, fifteen sessions
 after it was first shown on screen. The crash report the interpreter
 writes when an exception is not caught; it goes to the error stream and
 its last line names the exception. **The subtlety taught with it: in
 `print(next(box))` on an exhausted iterator, `print` never runs at all —
 Python evaluates the argument first and `next()` raises before `print` is
 called. This is what proves an exception is a travelling signal, not a
 value that lands.**
- [~] What the REPL is and how it differs from running a script (DOWNGRADED S7)
- [~] How import works at a high level (S3 — depth in 1.10)

#### 1.2 Variables, Name Binding, and the Object Model
- [x] Everything in Python is an object
- [x] Variables are names, not boxes — name binding
- [x] The namespace as a dictionary
- [x] id() to inspect memory addresses
- [x] Multiple names binding to the same object (ALIASING)
- [~] Rebinding a name creates a new object, doesn't mutate the old one
- [x] locals() to inspect the current namespace
- [ ] globals() and the difference from locals()
- [~] Reference counting (introduced, not drilled)
- [~] Garbage collection — basic concept introduced
- [ ] The del keyword
- [~] Integer caching (-5 to 256)
- [ ] String interning
- [x] Identity vs equality (`is` vs `==`) — **PROMOTED S16 after being owed
 since S7**
- [~] **BINDING HAPPENS ONLY ON A SUCCESSFUL RETURN — TAUGHT S15.** A name is
 bound when the right-hand side produces a value. If the call RAISES
 instead of returning, nothing is produced and nothing is bound. This is
 the mechanism behind `for i in range(3): ...` leaving `i == 2`: the final
 `next()` raised rather than returned, so `i` kept its last successful
 value. Interview-grade point; it generalises to every assignment.

#### 1.3 Data Types — The Five Primitives
- [x] int (Session 5)
- [~] float — precision issues; binary mechanism PARKED for 1.13
- [x] bool — subclass of int, truthiness
- [~] str — immutability, methods return new objects — **[x] CANDIDATE**
- [~] None — None vs False vs 0; `is None` over `== None`
- [x] type() / [x] isinstance()
- [~] Type conversion — int(), str(), float(), bool()
- [~] Implicit vs explicit conversion
- [x] What "type belongs to the object, not the name" means

> **1.3 STATUS: CLOSED — Session 10.** `bool("False")` and the `10/2`-float
> miss remain owed a cold re-test.

#### 1.4 Mutability vs Immutability
- [~] What mutability means
- [~] Immutable types: int, float, bool, str, tuple
- [~] Mutable types: list, dict, set
- [~] Why this matters when passing objects to functions
- [~] id() before and after mutation vs rebinding
- [x] Shallow vs deep copy — **PROMOTED S16**
- [~] Common bugs from mutability — THE MUTABLE DEFAULT ARGUMENT
- [x] ALIASING — the term
- [~] **THE MUTABLE/IMMUTABLE DISCRIMINATOR AS A PREDICTIVE TOOL — TAUGHT
 S17, and this is 1.4's most useful downstream payoff.** Asked how he could
 possibly know which methods mutate, he was given a model rather than a
 list: **check the TYPE first.** An immutable type cannot have a mutating
 method at all, so every `str` method necessarily returns a new object —
 which is why `s.upper()` needed no memorising. For mutable types, the
 **return value is the tell: a method that returns `None` mutated in place,
 because returning `None` serves no other purpose.** Hence the classic bug
 `l = l.sort()`, which silently replaces the list with `None`. Python's
 deliberate name-pairs make the design visible: `sort` mutates / `sorted`
 returns new; `reverse` mutates / `reversed` returns new.

> **1.4 STATUS: FULLY CLOSED — Session 11.** Several items promoted to [x] in
> the Session 16 promotion pass. The discriminator above was added S17.

#### 1.5 Operators and Expressions — COVERED END-TO-END (S13)
- [~] Arithmetic operators (+, -, *, /, //, %, **)
- [~] Comparison operators (==, !=, >, <, >=, <=)
- [~] Logical operators (and, or, not)
- [x] Identity operators (is, is not) — **CONFIRMED S16**
- [~] Membership operators (in, not in) — S13
- [~] Bitwise operators — S13, AWARENESS ONLY by design
- [x] Operator precedence / [x] Associativity — **PROMOTED S16**
- [x] Augmented assignment (+=, -=, etc.) — **PROMOTED S16**
- [~] Short-circuit evaluation in and/or — S13

> **1.5 STATUS: COVERED END-TO-END — Session 13.** Most items promoted in the
> S16 pass; the remainder stay [~] pending later-day unaided re-tests.

#### 1.6 Control Flow — **CLOSED, SESSION 17.** Opened S14, advanced S15/S16
- [x] **if / elif / else — OPENED S14, CLOSED AND CONFIRMED S17.** `if` =
 keyword, condition, colon, indented block. The condition is coerced to a
 `bool`; truthy/falsy cover non-bool values. **The colon OPENS a block;
 INDENTATION delimits it; a block creates NO new frame/namespace.**
 **THE CHAIN RULE, taught properly in S17 after he asked for it directly:
 `if`/`elif`/`elif`/`else` is ONE connected ladder, not several independent
 `if`s. Python checks top to bottom, and the FIRST condition that is true
 wins — its block runs and the interpreter leaves the entire chain without
 evaluating anything below it.** With `x = 5` against `if x > 10` /
 `elif x > 3` / `elif x > 1` / `else`, only "B" prints even though `x > 1`
 is also true. `else` is optional, evaluates nothing, and catches every
 remaining case. **CONFIRMED COLD: he gave "B" for `x = 5`, and for `x = 20`
 correctly stated that "A" prints and `elif x > 3` IS NEVER EVALUATED AT
 ALL. Self-rated 10/10. PROMOTED — this was the last item owed from S16.**
- [~] **Truthiness — TAUGHT S14.** Emptiness falsy, zero falsy, everything
 else truthy.
- [~] **THE ITERATION PROTOCOL — TAUGHT S15.** What `for x in <iterable>`
 actually does: **Stage A**, call `iter()` ONCE to get an iterator;
 **Stage B**, call `next()` on each pass — the returned item is bound to
 `x` and the block runs. When the iterator is exhausted `next()` raises
 `StopIteration`, which `for` catches internally and stops quietly. Hand-
 unrolled against a live 4-item list; the N+1 call-count trap identified
 correctly (`iter()` 1×, `next()` 5× for 4 items — the fifth raises).
- [~] **ITERABLE vs ITERATOR — TAUGHT S15. The load-bearing distinction.**
 An **iterable** is able-to-be-iterated: ask it and it hands you a fresh
 iterator (list, str, dict, tuple, range). An **iterator** is the nozzle:
 it gives the next item on demand and raises `StopIteration` when spent.
 **RULE: iterables are REUSABLE, iterators are CONSUMED.** Proved in code
 — draining an iterator with `list()` once leaves the second `list()` call
 returning `[]`, while the underlying list is untouched. **THE CAUSATION,
 corrected in session: an iterator is consumed because it holds
 FORWARD-ONLY STATE — a position that only ever moves forward, with no
 rewind. Not because "it gives one item at a time."** Confidence 4/5.
- [~] **`list()` AS A CONSUMER OF THE PROTOCOL — DEFINED S15** (forced by a
 correct student pushback). `list(x)` runs `next()` repeatedly until
 `StopIteration` and collects everything into a NEW list. It is not part
 of the protocol; it is a customer of it.
- [x] **`range()` — DEFINED S15, PROMOTED S16.** Name-decode: a stretch of
 numbers, start UP TO stop. **TWO LOCKS: HALF-OPEN** (`range(3)` → 0, 1, 2)
 and **LAZY** (computes on demand). **`range` is an ITERABLE, not an
 iterator.** `range(0)` is legal: zero items, body runs zero times.
- [x] **BLOCKS DO NOT CREATE SCOPE — PROMOTED S16.** **Python has FUNCTION
 scope, not BLOCK scope. `for`, `if`, `while` and `try` create no new
 scope. Names born inside them survive in the enclosing scope. Only a `def`
 makes a new scope.**
- [~] **`StopIteration` IS A SIGNAL, NOT A VALUE — TAUGHT S15.** An
 exception travels; it is never bound to a name. `i` keeps `2` because the
 final `next()` RAISED instead of RETURNING, so no binding occurred.
- [~] **`NameError` — DEFINED S15** via the `range(0)` case. Named after the
 part that broke: the NAME does not exist. **The distinction taught:
 "scoped away" (Python does not have this) vs "never created" (the only
 failure mode Python has).**
- [~] **`while` loops — break, continue — TAUGHT S16.** `for` asks an iterator
 for the next item; **`while` re-evaluates a CONDITION before every pass.**
 `break` exits the innermost loop entirely (there is no `break 2` in
 Python); `continue` abandons only the current iteration and jumps back to
 the condition check. **THE TRAP, found unprompted by the student: in a
 `while` loop a `continue` placed above the state update skips that update
 and produces an infinite loop.** RULE: in a `while` loop, put the state
 update where `continue` cannot skip it.
- [~] **Nested loops — TAUGHT S16.** The inner loop runs to COMPLETION for
 every single value of the outer. The inner `range(2)` restarts at zero each
 pass because `for` calls `iter()` on the ITERABLE again and gets a FRESH
 iterator. The counter-case was shown in code (`it = iter(range(2))` hoisted
 above the outer loop → the inner body runs only on the first pass, then
 silently never again). **Reuse that image — it is the best handle on the
 causation gap he keeps failing.**
- [~] **Loop `else` clause — TAUGHT S16, EARNED S17.** Runs if the loop
 completed WITHOUT hitting `break`; skipped if it broke out. **It has
 nothing to do with the `else` of `if` — it must not be read as
 "otherwise".** **THE S16 PREREQUISITE BREACH IS NOW REPAIRED: the owed
 exercise ran in S17 and it worked exactly as intended.** He first wrote the
 search WITHOUT loop `else`, using only `for`, `if`, `break` and a flag —
 and having felt the cost (a variable created before the loop, set inside
 the loop, and checked after it: three separate places for one question) he
 derived the justification himself. **The flag exists only to record "did
 this loop finish without breaking?" — and the interpreter already knows
 that.** Told rather than earned, loop `else` is a curiosity; earned, it is
 obvious.
- [~] **THE FOUND-FLAG PATTERN — TAUGHT AND WRITTEN BY THE STUDENT, S17.**
 The canonical search-a-sequence idiom, and the reason it matters here is
 that it is the loop `else` contrast case:
 ```python
 lis = [1, 35, 23, 64, 10, 243]
 flag = False
 for i in lis:
 if i == 10:
 flag = True
 print("found")
 break
 if not flag:
 print("not found")
 ```
 Output: `found`
 And the same job with loop `else`, which is what the pattern earns:
 ```python
 for i in lis:
 if i == 10:
 print("found")
 break
 else:
 print("not found")
 ```
 Output: `found`
 **He produced the flag version's STRUCTURE correctly and unaided.** Four
 iterations were needed, and the classification of what needed fixing is
 the useful part: iteration 1 used loop `else` (defeating the exercise) plus
 a name mismatch and shadowing of the builtin `list`; iteration 2 had the
 structure right with `print(found)` writing bare names instead of strings
 and a missing colon; iterations 3 and 4 were **whitespace only, which is a
 CHANNEL ARTEFACT and not a student error — see Session 17 rule 3.**
- [~] **`pass` statement — TAUGHT S17.** A no-op: a statement that does
 nothing at all. **It exists because of a hard syntactic rule — once a colon
 opens a block, that block cannot be empty; leaving it empty raises
 `IndentationError: expected an indented block`.** So when the syntax
 demands a body and there is nothing yet to put in it, `pass` fills the
 hole:
 ```python
 def calculate_torque():
 pass
 ```
 **THE DISTINCTION THAT WILL BLUR, and it is the thing to test rather than
 `pass` itself: `pass` means "do nothing, carry on"; `continue` means "skip
 the rest of THIS iteration and go to the next"; `break` means "leave the
 loop entirely". Three different jobs.** Second trap taught: **a comment is
 not a body.** A block containing only `# todo` still raises
 `IndentationError`, because comments are not code. He supplied the
 class-stub use case himself from prior exposure.
- [~] **Ternary / conditional EXPRESSION — TAUGHT S17.** `x if condition
 else y`. Where an `if`/`else` block spends four lines doing nothing but
 choosing between two values, the ternary does it in one:
 ```python
 sign = "positive" if x > 0 else "negative"
 ```
 Read it from the middle outward: *this value, if the condition holds,
 otherwise that one.* **THE POINT IS THE WORD EXPRESSION.** An `if`/`else`
 is a STATEMENT — it performs an action and produces nothing. A ternary is
 an EXPRESSION — **it evaluates to a value, so it can be used anywhere a
 value can be used**: bound to a name, passed straight into a call
 (`print("positive" if x > 0 else "negative")`), or dropped inside a list.
 An `if` block cannot be nested inside another expression that way.
 **He reached this himself** when asked how the two differ, framing it as
 the ternary producing something that then gets bound. **THE CAVEAT TAUGHT
 WITH IT: use a ternary only when both branches select one simple value. If
 either branch needs to do several things, write the full block — cramming
 work into a ternary is how it becomes unreadable.**
- [~] **Common loop patterns and pitfalls — TAUGHT S17.** Two pieces, both
 carried from S16 findings.
 **(1) THE INFINITE LOOP, and its single most common cause: the variable in
 the condition is never updated in the body.**
 ```python
 i = 0
 while i < 5:
 print(i)
 ```
 This prints `0` forever. He diagnosed it cold and completely — `i` is never
 incremented, so `i < 5` can never become false. The fix is `i += 1` inside
 the body.
 **(2) THE FULL TRACE, INCLUDING THE FINAL CYCLE** — the direct
 countermeasure to TRACE-TAIL TRUNCATION:
 ```python
 i = 0
 while i < 5:
 print(i)
 i += 1
 ```
 Output: `0 1 2 3 4` (one per line)
 **He traced all five cycles aloud and, critically, stated the terminating
 check explicitly: after `4` is printed `i` becomes 5, control returns to
 the top, `5 < 5` evaluates false, the body is skipped and the loop ends —
 so 5 is never printed.** That final re-check is the step the pattern used
 to drop, and it did not drop this time.
- [~] **`print()` — FORMALLY DEFINED S16**, after being deferred twice. It is
 a function that writes its arguments to standard output and **returns
 `None`** — same family as `append` and `sort`. **It calls `str()` on each
 argument**, which is why `print(5)` works while `"5" + 3` raises: `print`
 converts, `+` refuses. `print("a", "b", sep=" ", end="\\n")` are the
 defaults written out — **`sep` goes BETWEEN the items** and **`end` goes
 after everything**. Symbol correction issued: the newline is `\\n`,
 backslash-n, not `/n`. f-strings were raised by him and correctly PARKED
 for 1.8.
- [x] **MUTATING VS NON-MUTATING METHOD IDENTIFICATION — THE OWED DRILL RAN,
 S17.** This was the specific gap he named when he asked for his own S16
 demotion, and delivering it discharges that debt. Result **4/5**, with his
 own per-item confidence attached before any verdict:
 `l.append(4)` mutates + returns `None` (correct, unprompted);
 `l.copy()` new object (correct, 8/10);
 `l.extend([5,6])` mutates + returns `None` (correct, 5/10);
 `s.upper()` new string (correct, 10/10);
 `l.insert(0, 99)` mutates (correct, 8/10);
 **`l.reverse()` WRONG — called a new-object method (rated 5/10).**
 **The miss is the wrong-domain flaw firing on a surface cue, and his own
 rating predicted it.** The repair was not a roster but the discriminator
 now recorded in 1.4. Note the item stays [~] in the re-test queue —
 the DRILL is discharged, the ROSTER is not yet owned.

> **1.6 STATUS: CLOSED — SESSION 17.** Every listed item has now been taught.
> **Nothing here is [x] on S17's own evidence except the `if`/`elif`/`else`
> chain, because S17 ran within hours of S16 — see the INTERVAL GATE.**
> **S18 UPDATE: the first genuine later-day cold pass over the 1.6 tail has
> now happened and it was PARTIAL.** The exception cluster largely promoted
> (`NameError`, `ValueError`, `TypeError`, exceptions-are-signals, the
> `StopIteration` category) and the mutable/immutable discriminator promoted.
> **Two items did not: `traceback` and the iterator CAUSATION, both self-rated
> 3/10.** The spoken Feynman recall for the whole of 1.6 is STILL OWED.

#### 1.7 Functions ← **ACTIVE. OPENED SESSION 18.**

> **PREREQUISITE GATE, stated aloud at the open: 1.6 Control Flow, CLOSED in
> S17. Gate clear.** The unit was opened by cashing in "function scope, not
> block scope" ([x], promoted S16) and by telling him explicitly that NESTED
> FUNCTIONS AND RECURSION LIVE IN THIS UNIT — the two things he had named
> unprompted in S17 as what he most wanted. Both moves landed; he engaged
> harder in this unit than in any since S13.

- [~] **Defining functions with `def` — TAUGHT S18.** **THE DISTINCTION THAT
 IS THE WHOLE POINT: `def` time versus CALL time.** When the `def` line
 executes, Python builds a FUNCTION OBJECT and binds a name to it. That is
 all. **The body does not run and NO local namespace exists yet.** The local
 namespace is created when the function is CALLED, fresh on every call, and
 destroyed when the call ends.
 ```python
 def greet():
 print("hi")

 print(greet) # <function greet at 0x...> — object exists, body has not run
 greet() # hi — now the local namespace exists
 ```
 Output:
 ```
 <function greet at 0x...>
 hi
 ```
 **HIS FIRST ANSWER CONFLATED THE TWO** — he said the `def` line creates
 "greet ka local namespace". Corrected, and the teach-back was then clean:
 object at `def`, local namespace at call. One precision fix issued on top:
 **the object comes first and the name is a label attached to it**, which is
 the same names-and-objects rule from 1.2 applied to functions.

- [~] **Parameters vs arguments — TAUGHT S18.** In `def add(x, y):`, `x` and
 `y` are PARAMETERS — named empty slots declared at definition. In
 `add(3, 5)`, `3` and `5` are ARGUMENTS — the actual values supplied at the
 call, which fill those slots. **One is a NAME, the other is a VALUE.**
 Teach-back correct, and he volunteered the `def`-creates-an-object point
 alongside it unprompted.

- [~] **Return values — explicit and implicit `None` — TAUGHT S18, and it
 links straight back to the mutating-methods work.** `return x + y` sends a
 value back to the caller. **THREE CASES ALL PRODUCE `None`: no `return` at
 all; a bare `return`; an explicit `return None`.** No function returns
 nothing — every function returns at least `None`.
 ```python
 def f():
 pass

 def g():
 return

 def h():
 return None

 print(f(), g(), h())
 ```
 Output:
 ```
 None None None
 ```
 **The name for the first case is IMPLICIT `None`** — the value Python
 supplies without being asked; the third is EXPLICIT. **This is exactly why
 `l.sort()` and `l.reverse()` evaluate to `None`: they mutate and never
 return a value.** He stated all three cases correctly in the teach-back.
 ⚠ **TRANSCRIPTION INCIDENT LOGGED HERE: he said `None` and the channel
 rendered it "done"; the mentor corrected a mistake he had not made and he
 had to say so. See Teaching Mistakes and the S16 TRANSCRIPTION-ARTIFACT
 rule — SECOND occurrence of that exact class.**

- [~] **Scope and THE LEGB RULE — TAUGHT S18.** Name lookup walks four
 namespaces, innermost outward, and **STOPS AT THE FIRST HIT**:
 **L**ocal (this call's own namespace) → **E**nclosing (the namespace of a
 function this one is written INSIDE) → **G**lobal (module top level) →
 **B**uilt-in (`print`, `len`, `range`).
 **He produced all four, in the right order, with correct examples.** Two
 precision fixes were required and both matter downstream:
 **(a) ENCLOSING IS LEXICAL, NOT DYNAMIC.** He said the enclosing scope is
 the function "jiske through call hua hai". Wrong axis. **Enclosing is
 decided by where the function is WRITTEN in the source, not by where it is
 called from.** This is the point closures will stand on.
 **(b) GLOBAL IS NOT "MODULE-LEVEL LOCAL".** He called it "module level ki
 local namespace"; drop the word local — local means inside a function.
 **Also stated: his existing [x] "function scope, not block scope" is the L
 of LEGB and was never wrong, only incomplete.**

- [x] **`global` — TAUGHT S21; PROMOTED S22 on a later-day task-first drill:
 `drills/s22_counter.py` (3/3 pytest, written unaided) plus the full
 compile-time-locality mechanism stated cold when asked what deleting
 `global count` would do. Self-rated 10/10. Taught against `nonlocal`
 exactly as planned.**
 (`nonlocal` itself was taught S19 — see its entry below.) The pair:
 `nonlocal` says "don't create a local — target the ENCLOSING function's
 cell"; **`global` says the same one level higher — target the MODULE
 namespace.**
 ```python
 count = 0
 def tick():
     global count
     count = count + 1
 tick(); tick()
 print(count)      # 2
 ```
 **THE MECHANISM UNDERNEATH, and he re-derived the hard part himself by
 asking the right question ("why UnboundLocalError — shouldn't LEGB find
 the global?"): locality is decided at FUNCTION-CREATION time, not line by
 line.** The compiler scans the whole body; an assignment to a name
 ANYWHERE in the body classifies it local EVERYWHERE in the body, and a
 name classified local never gets the LEGB walk — reads go only to the
 local slot. Local-and-unbound = `UnboundLocalError`, which is the
 S19 three-error separation confirmed from a second direction.
 **THE WORKING RULE, completed on the mutation case (`scores.append(4)`
 works fine with no `global`): `global` is about REBINDING A NAME, not
 about touching an object. Read: free. Mutate: free. Rebind: needs
 `global`.** He predicted both the read-only case (`0`, no `global`
 needed) and the mutation case correctly, with the classification story
 stated unaided. One label fix: he reached for "associativity" for
 RHS-before-assignment — that is the EVALUATION ORDER of an assignment
 statement; associativity is the tie-break direction for equal-rank
 operators.

- [~] **Default arguments — TAUGHT S18.** `def power(base, exp=2):` makes
 `exp` optional; `power(5)` uses `2`, `power(5, 3)` uses `3`.
 ```python
 def power(base, exp=2):
 return base ** exp

 print(power(5), power(5, 3))
 ```
 Output:
 ```
 25 125
 ```
 He got `exp = 2` immediately and connected it to `__defaults__` unprompted.
 One label fix: `__defaults__` is an ATTRIBUTE (a tuple), **not a namespace**.

- [x] **`__defaults__` — PRODUCED COLD AT LAST, S22, FIRST TIME IN FIVE
 ATTEMPTS: "when the def is run... the object greet.__defaults__ is created
 which stores the default value." Self-rated 7/10; promoted; gauntlet-
 flagged. One sharpening owed on re-test: it is a TUPLE, `("world",)`.
 (History: RE-TESTED IN ISOLATION S18 AND MISSED COLD FOR THE FOURTH
 TIME.)** Asked which attribute on a function object holds its
 default values, he described the **local namespace** instead. **The repair
 to reuse: `__defaults__` is built at `def` time and lives on the function
 OBJECT permanently; the local namespace is built at CALL time and dies with
 the call. One is durable, one is momentary.**
 ```python
 def power(base, exp=2):
 return base ** exp

 print(power.__defaults__)
 ```
 Output:
 ```
 (2,)
 ```
 **This is now the only item in the file that has never once been produced
 cold. Fire it every session until it lands.**

- [x] **`*args` and `**kwargs` — TAUGHT S21; PROMOTED S22 on a later-day
 task-first drill: `drills/s22_report.py` (4/4 pytest including the empty
 case, signature written unaided) plus the collect/unpack mirror stated
 both ways cold. Self-rated 8/10. The item he asked for by name in
 S17. Motivated by a constraint he could not beat: `print()` accepts any
 number of arguments, and NO fixed parameter list can do that.**
 **KEYWORD ARGUMENTS had to be defined first — he stopped the block to say
 the term had never been taught, and he was right (see Teaching Mistakes
 S21).** Positional argument = matched by POSITION; keyword argument =
 passed as `name=value` in the CALL and matched by NAME, so
 `intro(role="robotics", name="Ankur")` lands correctly in any order.
 **THE COLLECTORS:** in a signature, `*args` collects all LEFTOVER
 POSITIONAL arguments into a TUPLE; `**kwargs` collects all LEFTOVER
 KEYWORD arguments into a DICT (keys = the names as strings). Signature
 order is fixed: normal parameters, then `*args`, then `**kwargs`.
 ```python
 def report(title, *args, **kwargs):
     print(title); print(args); print(kwargs)
 report("joints", 1.2, 0.8, unit="rad", safe=True)
 # joints / (1.2, 0.8) / {'unit': 'rad', 'safe': True}
 ```
 **THE EMPTY CASES, and the design point:** nothing left over → `()` and
 `{}`, never `None` — **one type in all cases, so the body can loop
 without a special case.** (His first guess was `None`; he self-corrected
 from output already on screen.)
 **THE MIRROR RULE, which completes the model: the same symbols in a CALL
 unpack instead of collecting.** `intro(*pair)` spreads a tuple into
 separate positional arguments; `intro(**info)` spreads a dict into
 keyword arguments. **Signature side = collect many into one; call side =
 spread one into many.** Teach-back correct with one fix: unpacking feeds
 the call with ARGUMENTS — nothing called a "variable" is created.

- [~] **Functions as first-class objects — TAUGHT/RE-CONFIRMED S18.** A
 function is an ordinary object: bindable to a name, passable as an argument,
 returnable from another function. **`f = greet` (no brackets) makes a second
 NAME for the same object — an alias; `f()` (brackets) CALLS it.**
 ```python
 def greet():
 print("hi")

 f = greet # alias — nothing runs
 print(f is greet) # True
 f() # hi
 ```
 Output:
 ```
 True
 hi
 ```
 **He answered this correctly and unprompted, and recognised it as something
 he had met before** — brackets are the call, the bare name is the object.

- [~] **Nested functions — TAUGHT S18, DEFINITION ONLY.** A function written
 inside another function; outer is the OUTER, inner is the INNER, and the
 outer is the inner's ENCLOSING scope (the E of LEGB). He defined it back
 correctly and immediately.

- [~] **CLOSURES — TAUGHT FROM SCRATCH IN TEXT, S19.** He required this in S18
  and nothing from S18 counted as coverage. Built bottom-up from LEGB.
  **THE SETUP THAT CREATES THE PROBLEM — return the inner function WITHOUT
  brackets, so it outlives its birthplace:**
  ```python
  def outer():
      n = 10
      def inner():
          return n * 2
      return inner          # no brackets — the function OBJECT itself

  double = outer()          # outer has finished and returned
  print(double())
  ```
  Output:
  ```
  20
  ```
  **THE CONTRADICTION THAT MOTIVATES THE WHOLE TOPIC, and it is the right way
  in:** `outer` is dead by the time `double()` runs. Its local frame — and
  `n = 10` with it — should have died on return, by the same rule that makes a
  local namespace momentary. Yet `20` comes back. **He predicted `20`
  correctly, but his stated mechanism ("apne enclosing namespace check karega")
  BREAKS HERE — there is no live enclosing frame left to check.** That gap is
  the lesson.
  **THE MECHANISM:** the only thing that escaped alive is the `inner` object,
  sitting in `double`. So Python binds `n` **to that object**. The bond is a
  **CLOSURE**; the captured name (`n`) is a **FREE VARIABLE** — free because it
  is not `inner`'s own local, yet `inner` holds it; and it is stored in a
  **CELL** on the attribute **`__closure__`**.
  ```python
  print(double.__closure__)                     # (<cell at 0x...: int object>,)
  print(double.__closure__[0].cell_contents)    # 10
  ```
  **HE REACHED THE ANSWER HIMSELF ACROSS THREE GUESSES, and the wrong two are
  worth keeping because the reasons they fail are teaching:**
  (1) `outer.__defaults__` — wrong, but a good instinct (Python really does use
  a dunder attribute). It fails on ROLE and on TIMING: `__defaults__` exists
  only for PARAMETERS' default values and is fixed at `def` time, whereas `n`
  is an ordinary local created during the call.
  (2) `<module>` — wrong, and he had already supplied the refutation himself
  earlier in the file: **the module namespace is ONE, SHARED**, so two closures
  from the same factory would overwrite each other.
  (3) **the `inner` function object — CORRECT.**
  **PER-OBJECT CELLS, which is the property that makes closures useful:**
  ```python
  def make_multiplier(x):
      def multiply(num):
          return num * x
      return multiply

  double = make_multiplier(2)
  triple = make_multiplier(3)
  print(double(5), triple(5), double.__closure__[0].cell_contents)
  ```
  Output:
  ```
  10 15 2
  ```
  Every call to the factory re-runs `def multiply`, producing **a new function
  object with a new cell**. Cells are per-object and never shared. He predicted
  all three values correctly and gave the causation ("alag alag objects hain").

- [~] **WHY CLOSURES EXIST AT ALL — THE HONEST ANSWER, S19. Do not soften this
  and do not re-motivate it from scratch; he has now demolished five weak
  motivations across two sessions and he will notice.**
  **A closure gives NO new power.** Anything it does can be done with a dict
  plus passing both values every time. What it gives is a **SHAPE**: a function
  that needs only ONE argument from outside, with the extra value sealed
  inside. **Wherever the student is the one calling, the two-parameter version
  is better and he should be told so.**
  **The shape becomes a NECESSITY in exactly one situation: when you are not
  the one calling the function — some other code is, and it will only ever
  pass one argument.**
  ```python
  def apply(price, pct):
      return price - price * pct / 100

  prices = [200, 50, 120]
  sorted(prices, key=apply)      # BREAKS — sorted only ever passes one argument
  ```
  `sorted` calls `apply(200)`, `apply(50)`, `apply(120)`. It does not know
  `pct` exists and there is nowhere to inject it. **The two-parameter version
  genuinely cannot be used here** — and this is the first and only example that
  he accepted: *"ye pehla example hai jo sense bana raha hai, yahan pe samajh
  aaya closure lagega."*
  ```python
  def make_discounter(pct):        # pct sealed in a cell
      def apply(price):            # one argument — the shape sorted wants
          return price - price * pct / 100
      return apply

  sorted(prices, key=make_discounter(10))     # fits
  ```
  **HIS SHARPER SECOND CHALLENGE, and the answer to keep:** *"ek baar ban gaya
  to wo to fixed hai, dynamism kahan hai?"* Half right, and the half matters.
  A SINGLE closure IS fixed. **The dynamism is not inside one closure — it is
  that the factory can mint any number of them at runtime, each sealing a value
  unknown at write time**, in a count also unknown at write time.

- [~] **`sorted` AND `key=` — TAUGHT FROM ZERO, S19, MID-FLOW.** These had
  never been covered and were deployed as a closure example anyway; he flagged
  it twice and was right both times. See Teaching Mistakes.
  `sorted(list)` returns a **NEW list** in ascending order; the original is
  untouched. `key=` is an optional keyword argument taking **a function name**,
  and it means: *do not order elements by their own value — first pass each
  element through this function and order by whatever it returns.*
  **THE LOAD-BEARING PART, and the thing that makes closures necessary: YOU do
  not call that function. `sorted` calls it, internally, once per element,
  passing EXACTLY ONE argument.**
  ```python
  def negate(num):
      return -num

  print(sorted([10, 4, 8, 2], key=negate))
  ```
  Output:
  ```
  [10, 8, 4, 2]
  ```
  **CORRECTION ISSUED: the returned list holds the ORIGINAL elements in a new
  order — NOT the key values.** Keys are readings used to decide order, then
  discarded. He had assumed the output would contain the negated values.
  **HE THEN REVERSE-ENGINEERED `sorted` UNPROMPTED and his skeleton was
  correct** — run the function on each element, pair each key with its element,
  compare on keys, lay out the real elements. **One correction: he proposed a
  DICTIONARY, which breaks on duplicate keys** (two elements with the same key
  value would overwrite, losing an element) and inverts the relationship. The
  right structure is a list of `(key, element)` pairs:
  ```python
  def my_sorted(items, key):
      pairs = [(key(x), x) for x in items]   # key() called once per element
      pairs.sort()                            # sorts on the first slot
      return [x for (k, x) in pairs]          # real elements, new order
  ```

- [~] **`nonlocal` — TAUGHT S19. Reading a cell versus WRITING to one.**
  Until this point the cell had only ever been read. Writing is a different
  problem, and the broken counter is the way in:
  ```python
  def make_counter():
      count = 0
      def increment():
          count = count + 1
          return count
      return increment

  c = make_counter()
  print(c())
  ```
  Output:
  ```
  UnboundLocalError: cannot access local variable 'count' where it is not
  associated with a value
  ```
  **He predicted `1` then `2` — MISS, and a productive one.**
  **THE RULE: if a name is ASSIGNED anywhere in a function body, that name is
  that function's LOCAL for the entire body, from the first line. The decision
  is made at `def` time, while reading the code, before anything runs.** So
  `count` inside `increment` is local, the enclosing cell is invisible, LEGB's
  E step never runs — and then the right-hand side reads a local that has no
  value bound yet. **Name reserved, value absent: `UnboundLocalError`.**
  **THE THREE-ERROR SEPARATION, now explicit and worth re-testing as a set:**
  `TypeError` = a required argument was never supplied, raised at CALL time
  before the body runs. `NameError` = the name does not exist anywhere in LEGB.
  `UnboundLocalError` = the name IS local, but no value is bound yet.
  **The fix:**
  ```python
  def make_counter():
      count = 0
      def increment():
          nonlocal count
          count = count + 1
          return count
      return increment

  c = make_counter()
  print(c())
  print(c())
  print(c.__closure__[0].cell_contents)
  ```
  Output:
  ```
  1
  2
  2
  ```
  All three predicted correctly. `nonlocal` says *do not make this name local —
  use the enclosing cell, and write into it.* **The third print showing `2` and
  not `0` is the proof the cell was WRITTEN to; and `count` surviving between
  calls is the real payoff: STATE THAT OUTLIVES THE CALL.**
  Note for the tail of 1.7: **`nonlocal` targets the ENCLOSING cell only, never
  module-level global. `global` is the separate keyword and is still untaught.**

- [~] **ALIAS vs NEW OBJECT vs RETURN VALUE — the def-vs-call loop closed, S19.**
  This began as his own doubt: if the inner function is always written as
  `inner`, are two closures the same function under two names? **No — separate
  objects.** The name appears once in the source, but every CALL re-runs the
  `def` line and mints a fresh object with a fresh cell. Mould and castings.
  ```python
  a = outer()
  b = outer()
  print(a is b)    # False
  ```
  **HIS OWN INSIGHT, UNPROMPTED AND STRUCTURALLY SOUND:** *"ye to class jaisa
  hai, har baar ek instance create kar rahe hain."* The pattern he spotted is
  real — **behaviour carrying private data with it**; class puts data in
  attributes and behaviour in methods, a closure puts data in a cell and
  behaviour in the body. Label precision issued (a closure is a function
  object, not a class) alongside the saying that *a closure is a poor man's
  object and an object is a poor man's closure.*
  **The three cases, which he ended up distinguishing correctly:**
  ```python
  b = a                  # ALIAS — same object, same cell → 1, 2, 3 (shared count)
  b = make_counter()     # NEW object, new cell     → 1, 2, 1 (separate counts)
  b = a()                # the RETURN VALUE (an int) → b() raises TypeError
  ```
  **He MISSED the middle one** — predicted `1, 2, 3` for two independent
  counters, which requires a shared cell — **despite having established `a is
  b` → `False` minutes earlier.** See Thinking Gaps: the fact was retrievable
  but not load-bearing. He then got the alias case right WITH the correct
  causation, and asked about `b = a()` himself, which completed the set.
  Handle: **brackets give you the `return` value, not the function.**

#### 1.7.9 Recursion — **TAUGHT S20, after four deferrals. [~]**

- [~] **DEFINITION, given before any code.** A function that calls itself, where
  each call gets a *strictly smaller* version of the same problem, and where at
  least one input is small enough to answer with no further call.
  **BASE CASE** = answered outright, no recursive call. **RECURSIVE CASE** =
  calls itself on a smaller input and builds its answer from what comes back.
  **The framing that did the work: there is NOTHING NEW IN THE MACHINERY.**
  Every call gets its own frame with its own locals, exactly as taught in 1.1.
  Recursion only means several frames OF THE SAME FUNCTION are alive at once.
  **Cash in the 1.1 frames work — it is the whole explanation.**

- [x] **PRE-ORDER vs POST-ORDER — PROMOTED S22: fresh post-order code
  (`climb(3)`) traced frame-by-frame, unaided, later-day, 10/10 — the S20
  one-mutating-`n` error did not recur; the `0`-never-prints point held.
  ⚠ The LABELS (pre-/post-order) were a gap; decoded in session, now in the
  term queue. Taught as a matched pair, and THE PAIR IS THE
  LESSON.** Identical function, identical base case; the only change is whether
  `print(n)` sits above or below the recursive call.
  ```python
  def countdown(n):          # work on the way DOWN
      if n == 0:
          print("liftoff"); return
      print(n)
      countdown(n - 1)
  ```
  → `3 2 1 liftoff`
  ```python
  def countdown(n):          # work on the way BACK UP
      if n == 0:
          print("liftoff"); return
      countdown(n - 1)
      print(n)
  ```
  → `liftoff 1 2 3`
  **[PREDICT] FAILED — he answered `2 1 0 liftoff`, and the failure is
  diagnostic.** Three separate errors, ONE root cause: he imagined a SINGLE `n`
  that keeps changing and prints as it descends. **There is no single `n`. There
  are four frames, each holding its own, and `print(n)` prints the `n` belonging
  to the frame that statement is in.**
  ⚠ **THIS IS THE IDENTICAL ISOLATION PRINCIPLE HE HAD CORRECTLY EXPLAINED FOR
  CELLS TWENTY MINUTES EARLIER IN THE SAME SESSION** — five objects, five cells,
  no collision. **He owns it for cells and dropped it for frames.** Same idea,
  different container. Log this as the transfer failure it is; the concept is
  not the problem, the RECOGNITION of the concept in a new container is.
  His third error was separate and simpler: he printed `0`, which never prints —
  that frame hits the base case and `return`s before reaching `print(n)`.

- [~] **VALUE-RETURNING RECURSION — the answer assembled on the unwind.**
  ```python
  def total(n):
      if n == 0:
          return 0
      return n + total(n - 1)
  ```
  **[PREDICT] BOTH PARTS CORRECT: `10`, and the deepest frame is `n=0` which
  RETURNS 0.** The second half is the one that matters and he got it clean —
  most people fumble that the base case returns a VALUE rather than nothing.
  Taught alongside: `n + total(n - 1)` cannot finish evaluating until the inner
  call returns, so **every frame sits half-evaluated, holding its own `n`,
  waiting.** Four frames stacked, then four additions on the way back.

- [~] **THE IDENTITY-VALUE RULE FOR BASE CASES.** `factorial` returns `1` at the
  base, not `0`. **The base case must return the IDENTITY for the operation
  being used** — `0` for `+`, `1` for `*`, `[]` for list concatenation. Return
  `0` in factorial and the entire product collapses to zero.
  **This rule recurred three times in the session and is the single most
  transferable thing in 1.7.9. Re-test it as a RULE, not as three examples.**

- [~] **TERMINATION — TWO CONDITIONS, BOTH REQUIRED.**
  (1) A base case exists that returns without recursing.
  (2) Every recursive call moves the input **strictly closer** to it.
  Missing (1) → `RecursionError`. **Missing (2) ALSO → `RecursionError`, and
  this is the non-obvious half**: `broken(5)` with `n == 0` as the base and a
  step of `n - 2` runs 5, 3, 1, −1, −3… and steps straight past zero forever.
  **A base case that exists but is never landed on is not a base case.**
  `RecursionError` fires at CPython's default depth of 1000 — taught explicitly
  as a **guard against runaway memory, not a law of recursion**.

- [~] **PRINTER vs CALCULATOR — the design distinction, and it came out of his
  own code.** The question to ask of any function: **does it print, or does it
  return?**
  **PRINTER** — values reach the user via `print`; nothing to return; base case
  is a bare `return`; the recursive call is made WITHOUT `return` in front of
  it; the function yields `None` implicitly, which is the honest answer to
  "what did this compute?" — nothing. It *did* something.
  **CALCULATOR** — returns on every branch, prints nothing.
  **Mixing the two is what produces stray return values nobody uses.**
  ⚠ Taught as legibility, not law: `return` in front of a printer's recursive
  call is HARMLESS (the `None` propagates up and nothing breaks) but MISLEADING,
  because `return <something>` is a claim that the caller wants the value.

- [~] **[DRILL] `count_down_by(n, step)` — PASSED on both checked points.**
  ```python
  def count_down_by(n, step):
      if n <= 0:
          return 0, step          # ← the flaw
      print(n)
      return count_down_by(n - step, step)
  ```
  **Base case `n <= 0` was the RIGHT choice and he chose it unaided** — `n == 0`
  would have failed, since from 10 by 3 the values run 10, 7, 4, 1, −2 and never
  touch zero exactly. **He caught the whole tail.** `step` correctly passed
  through. **THE FLAW: `return 0, step` builds a tuple that is handed up through
  every frame and out the top, unused.** His instinct to return something was
  right; the mistake was **returning debris instead of the identity value.**
  The calculator rewrite was then shown and is the better design:
  ```python
  def count_down_by(n, step):
      if n <= 0:
          return []
      return [n] + count_down_by(n - step, step)
  ```
  **Why it is better, and this is the part worth re-testing: a printer can only
  put text on a terminal; a calculator can be printed, summed, sliced, fed
  onward — and TESTED.** `assert count_down_by(10, 3) == [10, 7, 4, 1]` cannot
  be written against the printer version without capturing stdout.
  **Tied to his own work explicitly: a function that RETURNS a trajectory is
  testable in CI; one that PRINTS it is not.**
  ⚠ **A FOLLOW-UP VARIANT OF HIS DROPPED THE `print` ENTIRELY**, leaving a
  function that burns four frames and tells nobody anything — neither printer
  nor calculator. Flagged. **And one reasoning error inside it needs re-testing
  because it is a category confusion, not a slip:** he wrote *"this is a
  function call with two arguments so returning a none will not cause problem."*
  **ARGUMENT COUNT AND RETURN VALUE ARE UNRELATED.** A five-argument function
  can return `None`; a zero-argument function can return a dict. Whether `None`
  is a problem depends ONLY on what the CALLER does with it — which is the
  implicit-`None` trap from 1.7.3 wearing a new coat: the function is happy, the
  CALLER explodes, and the traceback points at the caller's line.

- [~] **[DRILL] `digit_sum(n)` — recursive case CORRECT UNAIDED, base case
  BOUNDARY BUG.**
  ```python
  def digit_sum(n):
      if n <= 10:                     # ← bug
          return n
      return n % 10 + digit_sum(n // 10)
  ```
  **The recursive case is right on all four checked points** — peels the last
  digit, shrinks the input, returns on that branch, combines rather than
  discarding. **`n <= 10` lets `10` itself through and returns it whole:
  `digit_sum(10)` → 10, `digit_sum(100)` → 10.** His own test values (472, 9999)
  both bottom out at a single digit and never land on 10, so they passed.
  Fix is one character: `n < 10` ("single digit — nothing left to peel"), or
  `n == 0` returning `0`, which matches the identity pattern from `total`.
  **HIS TRACE, PRODUCED CORRECTLY ON THE SECOND ASK:** two frames parked, base
  at 4, unwind 4 → 11 → 13. ⚠ **On the FIRST ask he gave only "13". See rule 3
  and Thinking Gaps — he had the trace and skipped it.**

#### 1.7.10 Pure functions vs side effects — **TAUGHT S20 (pre-loaded S10). [~]**

- [~] **PURE = two conditions.** Output depends only on the arguments, AND it
  changes nothing outside itself. Same input, same output, forever.
  **SIDE EFFECT** = anything a function does beyond returning a value: printing,
  writing a file, mutating something it was handed, changing a global.
  **Taught explicitly as NOT a hierarchy: side effects are the point of a
  program; a pure program that touches nothing is a heater. The rule is DON'T
  HIDE THEM and DON'T MIX THEM** — a function that both computes and mutates is
  hard to test, because you cannot check its answer without triggering its
  damage.
  ⚠ **THIS BLOCK WAS THE DOUBT-GATE CASUALTY.** It was delivered immediately
  after a drill with no doubt check, he invoked the gate, and when the `scale`
  prediction came back he had to ask *"what do you mean when you say scale is
  pure??"* — **the definition had been in the lost block. Restated. This is the
  clearest possible evidence for rule 1 and it happened in the same session the
  rule was written.**

- [~] **THE DISGUISED-MUTATION TRAP — the S19 alias trio in new clothes.**
  ```python
  def add_item(basket, item):
      basket.append(item)
      return basket        # LOOKS pure: takes input, returns output. Is not.
  ```
  `append` mutates the caller's list in place and `return` hands back the SAME
  object. Pure version: `return basket + [item]` — builds a new list, original
  untouched.
  **[PREDICT] `scale` — ALL THREE LINES CORRECT** (`[10, 20, 30]`,
  `[10, 20, 30]`, `True`) **and he identified the mutation and the aliasing
  unprompted before the prediction was even posed.**
  **The `is` check is the load-bearing one: `True` proves no new list was ever
  made.** Assigning to `scaled` LOOKS like a fresh result; it is a second name.

#### 1.7.11 EDGE-CASE ANALYSIS — **TAUGHT S20 AS AN EXPLICIT SKILL. [~]**
**ADDED TO THE CURRICULUM AT THE STUDENT'S DIRECT REQUEST.** It was previously
implicit — a line in WATCH AREAS and an expectation in drills, but never taught.
He named the gap precisely: *"I am unable to think about the failure cases and
dissect the problem the way you do... that's why I am doing this curriculum,
because I have never done this, and don't know how to find the edge cases, are
we going to work on that and i believe you need to teach me that as well??"*
**He was right that it was missing. It does not wait for Layer 6 testing — he
needs it on every drill from here.**

**THE PREMISE THAT HAD TO BE CORRECTED FIRST:** he was treating edge-case
hunting as a knack the mentor has and he lacks. **It is not. It is a checklist
run against the STRUCTURE of the code.** Saying so was as important as the
content, because "I can't think like that" is a self-limiting frame and it is
false.

- [~] **THE FIVE CHECKS — where bugs actually live.** Not spread evenly across
  the input range; they cluster in five places.
  1. **THE BOUNDARY OF EVERY CONDITION.** Any `if` with `<`, `<=`, `>`, `>=`
     has an exact value where the branches meet. **Test THAT value, not values
     near it.** (His `n <= 10` → test `digit_sum(10)`. Bug found. Not intuition
     — read the operator, test the number sitting on it.)
  2. **EMPTY / ZERO / NOTHING.** Zero, empty string, empty list, `None`.
  3. **ONE.** The smallest NON-empty case. Loops that run once and recursions
     that recurse once behave differently from the general case.
  4. **THE VALUE OUTSIDE WHAT YOU ASSUMED.** Negative when you assumed
     non-negative; float when you assumed int. (`digit_sum(-5)` returns `-5`,
     silently wrong. Out of scope as specified — **noticing it is the skill.**)
  5. **WHERE TWO THINGS MUST AGREE.** A base case and the step that approaches
     it. This is what killed `broken(n)`.
  **Stated as a procedure: list every condition and test its boundary; test
  zero/empty; test one; ask what type or sign you silently assumed; if
  recursive, check the step always LANDS on the base. Five checks, ninety
  seconds.**
  **S24 COLD RE-TEST — 4/5 UNAIDED, later day, self-rated 5/10 (well
  calibrated). The mnemonic "Boundary pe khaali ek bahar mila", built with him
  in S23, WORKED: three days earlier he could not name one.** Boundary,
  khaali, ek and bahar all came back with correct content. **`Mila` did not —
  he glossed it "similar inputs".** Check 5 has now been generalised past
  recursion and restated for him in both languages: **`mila` compares the
  PROMISE (docstring/spec) against the CODE, one sentence at a time — "iske
  peeche kaunsi line hai?"** He then performed it correctly on
  `take_last([])` without recognising that he was doing it — ruling the
  `IndexError` NOT a bug because the spec says the list may be assumed
  non-empty. **Naming the move he had already made is what landed it.**
  He then applied all five to `drills/s24_lists.py` and found the one real
  edge case in it. **Stays [~] on the missing fifth; one clean 5/5 promotes.**
  ⚠ **He also challenged the cost — "shouldn't I just write the relevant
  cases?" PARTIALLY UPHELD and the resolution is worth keeping: SCAN all five,
  REPORT only the ones that bite. Pre-filtering by "relevant" uses the same
  assumption that produced the bug — which is exactly how the S20 `n <= 10`
  boundary looked irrelevant until it was the bug.**

- [~] **[DRILL] THE BUG HUNT — and THE METHOD TRANSFERRED ON FIRST USE.**
  ```python
  def first_char(word):
      if len(word) == 1:
          return word
      return first_char(word[:-1])
  ```
  **He found the empty-string failure via CHECK 2, with the correct mechanism
  stated unaided:** `len("") == 1` is False → takes the recursive branch →
  `""[:-1]` is `""` → **the input cannot get smaller, so the base case is never
  reached** → `RecursionError`. **That is termination condition 2 failing, and
  he connected it without being pointed at it.** Fix: `len(word) <= 1`.
  ⚠ **PUSHBACK 25, UPHELD: he refused the drill on the grounds that SLICING HAS
  NEVER BEEN TAUGHT** — *"So I am not currently eligible to answer this reason
  you have not taught index slicing."* **Correct, and it is the TENTH
  define-before-building breach** — the same class of error as `zip` and list
  comprehensions in S19. The minimum was then given (`word[:-1]` = everything
  except the last character, the string analogue of `n // 10`). **FULL SLICING
  REMAINS OWED IN 1.8 and must not be treated as taught.**
  **NOTE THE SHAPE OF THE TWO BUGS FOUND IN THIS SESSION: his own `n <= 10` and
  the planted `len(word) == 1` are the SAME BUG — a base case too narrow, caught
  only by testing the exact edge. Same bug, twice, in ten minutes.**

- [x] **Lambda functions — TAUGHT S22, EARNED S23** (`drills/s23_ordering.py`,
 6/6 pytest COLD ON FIRST ATTEMPT, unaided, two lambdas written under a
 constraint forbidding a third `def`; auto-return then recalled unaided —
 *"lambda automatically returns the computed"* — corrected to EXPRESSION,
 not statement). The EXPRESSION form of a function:
 evaluates to a function object where it stands, no name. Body is ONE
 expression, its value auto-returned — no statements, no `return`. The
 parameter list works exactly like a `def`'s (he asked about two-parameter
 lambdas himself; confirmed). **Motivated honestly via the S18/S19 answer —
 a function demanded as an argument:** `sorted(robots, key=lambda s:
 s.lower())` beats a named one-use helper. `key=` re-taught from S19:
 called once per element, ONE argument, sorts by RESULTS, returns ORIGINAL
 items — he held that last part unprompted in the squares [PREDICT]
 (`[-1, -3, 4, 7]`, correct). Closure transfer [PREDICT] also passed
 (lambda closes over `k` like any `def`). **Label is brute-force (Greek λ)
 — spaced queue, not decoding.**
- [~] **Docstrings — TAUGHT S22.** A string literal as the FIRST statement of
 a body, stored on the function object as **`__doc__`** at `def` time —
 same attribute family as `__defaults__`/`__closure__` (shelf/dabba handle
 reused). Comment vs docstring: comments are discarded before run; a
 docstring is DATA on the object (`help()`, hover-tooltips read it).
 Convention: triple quotes, imperative one-liner. **[PREDICT] miss worth
 keeping: absent docstring → he guessed `""`; it is `None` — taught the
 absence discriminator: collectors give empty containers (`()`/`{}`),
 optional attributes give `None`.**
 **S23 — STAYS [~], AND THE SPLIT IS THE POINT. PLACEMENT held cold and
 unaided (`drills/s23_ordering.py`, both functions documented, tests
 green). MECHANISM missed: asked what `__doc__` returns when the same
 string sits on the SECOND line of the body, he predicted the string.
 It is `None`. Taught then: TRIPLE QUOTES DO NOT MAKE A DOCSTRING,
 POSITION DOES — elsewhere the literal is an expression evaluated and
 discarded. He can place one correctly without knowing why it works,
 which is exactly what [~] is for.**

> **1.7 STATUS: CLOSED — SESSION 22.** Every item is now taught. S20 added
> RECURSION (1.7.9), PURE FUNCTIONS vs SIDE EFFECTS (1.7.10) and EDGE-CASE
> ANALYSIS (1.7.11); S21 added `global` and `*args`/`**kwargs`; S22 added
> lambdas and docstrings and closed the unit.
> **SIX items in 1.7 are [x] as of S23** (`global`, `*args`/`**kwargs`,
> `__defaults__`, pre/post-order, the S18 discriminator, plus LAMBDAS earned
> S23) — all earned on later-day evidence, under the new promotion rule. The
> rest of the S18–S22 material is owed its later-day cold passes.
> ⚠ **THE CLOSURE DEFINITION FAILED A SECOND TIME IN S23 (7/10), with the
> SAME two defects as S22 — `cell_contents` called a tuple, and the survival
> clause missing. Root cause found and it is a MENTOR one: the four layers
> had been taught as a stack of LABELS. What a cell IS was never given —
> that it is a TYPE, a one-slot box, and that `__closure__` is a tuple
> because there is one cell PER FREE VARIABLE. Taught in S23 with `type()`
> output. Re-test the definition cold; if the structure now holds, the
> muddle was never his.**
> ⚠ **TWO CONSTRUCTS WERE USED IN S19 EXAMPLES WITHOUT EVER BEING TAUGHT and
> must not be quietly assumed later: `zip` (in `zip(customers, percents)` — he
> flagged it himself) and LIST COMPREHENSIONS (in `[(key(x), x) for x in
> items]`). Both are listed in 1.8. Mark them seen-but-not-taught.**

#### 1.8 Data Structures
- [~] list — methods, indexing, slicing — **TAUGHT S24** (`drills/s24_lists.py`,
 11/11 pytest, one guided fix). Covered: INDEXING formally (0-based, last
 index is `len-1`, negative indices, `IndexError`) — **it had never been
 defined, despite `__closure__[0]` being used for two sessions; caught by
 checking rather than assuming**. SLICING in full (`[start:stop:step]`,
 half-open like `range()`, omitted ends, negative step, `l[:]` as the copy
 idiom, slices build a NEW list, out-of-range slices return `[]` and NEVER
 raise, same operator on `str` — which retro-explains the `word[:-1]` given
 as a minimum in S20 and DISCHARGES pushback 25). METHOD ROSTER exercised
 cold: `append`, `extend`, `insert`, `sort`, `remove`, `pop` — all six
 mutating, five returning `None`, `pop` returning the removed item.
 ⚠ **THE REAL YIELD IS THE CORRECTED DISCRIMINATOR: the S17 tell runs ONE
 WAY ONLY. returns `None` ⇒ mutating (true); mutating ⇒ returns `None`
 (FALSE — `pop` is the counterexample). TYPE first, return value as a
 one-directional hint, never as a biconditional.**
 NOT YET [x]: everything here is same-session. He inverted `sort`/`sorted`
 in the volley (`sort` "returns a new list for sure") — the block was
 tagged [PREDICT], so **that miss is NOT ledgered**; it needs a clean cold
 [RECALL] pass. Shallow-vs-deep copy PARKED to "nested data structures".
- [ ] **Copy semantics: a slice copies the REFERENCES, not the items** —
 parked S24 when he described `tools[:]` as "an identical new list object".
 Only bites on nested structures; belongs with the bullet below.
- [ ] tuple — immutable; when to use over list
- [ ] dict / [ ] set
- [ ] When to use which — decision framework
- [ ] List comprehensions (**pre-loaded S15: the iteration protocol is the
 machinery underneath every comprehension — say so when this opens**)
- [ ] Dict comprehensions
- [ ] Nested data structures
- [ ] Common patterns and pitfalls
- [ ] **String formatting / f-strings — PARKED HERE FROM S16** at the
 student's own raising.

#### 1.9 Error Handling and Exceptions
- [ ] What exceptions are — the exception hierarchy (**pre-loaded S15:
 `StopIteration` as a signal, `NameError`, and the traceback definition.
 He has now met three exceptions as MECHANISM rather than as noise.
 ⚠ NOTE UPDATED S18: the deferred re-test finally RAN and this cluster is no
 longer the weakest in the file. `NameError`, `ValueError`, `TypeError`,
 exceptions-are-signals and the `StopIteration` CATEGORY all promoted to [x]
 on genuine later-day cold evidence. **`traceback` is the one that did NOT
 (self-rated 3/10) — when 1.9 opens, build from the UNCAUGHT-exception
 trigger rather than from the label.**)
- [ ] try / except blocks
- [ ] Catching specific exceptions vs bare except (**pre-loaded S15: `for`
 catching `StopIteration` internally is the first real example of an
 exception being caught and handled quietly — reuse it here**)
- [ ] else and finally clauses
- [ ] Raising exceptions with raise
- [ ] Creating custom exceptions
- [ ] Common built-in exceptions
- [ ] Using exceptions for control flow vs error handling (**pre-loaded S15
 — the iteration protocol IS exception-driven control flow, and that is a
 genuinely interesting design point to raise here**)
- [ ] Defensive programming mindset

#### 1.10 Modules, Packages, and Imports
- [ ] What a module is / [ ] import statement / [ ] from x import y
- [ ] import as aliasing / [ ] `__name__ == "__main__"`
- [ ] The standard library / [ ] pip and third-party packages
- [ ] What a package is / [ ] Relative vs absolute imports
- [ ] Circular imports / [ ] sys.path

#### 1.11 File Handling
- [ ] open() / [ ] Read modes / [ ] read(), readline(), readlines()
- [ ] Writing files / [ ] The with statement — context managers
- [ ] Why context managers matter / [ ] os.path and pathlib
- [ ] CSV basics / [ ] JSON basics

#### 1.12 OOP
- [ ] Why OOP exists / [ ] Classes and instances / [ ] `__init__`
- [ ] Instance vs class attributes / [ ] Methods — instance, class, static
- [ ] Inheritance / [ ] Method overriding / [ ] super()
- [ ] Dunder methods / [ ] Encapsulation / [ ] Polymorphism
- [ ] Composition vs inheritance / [ ] Dataclasses (intro)

#### 1.13 Python Internals (Deep Dive) — TRIMMED per master
- [ ] Memory model revisited
- [ ] Garbage collector mechanics
- [ ] The GIL
- [ ] IEEE 754 float internals — PROMISED S5. Non-negotiable.
- [ ] **Generators and iterators — NOW CARRYING A PROMISE FROM S15.** The
 protocol is taught at Level 2; this is where `__iter__`/`__next__` and
 generators cash it out at Level 3. Tell him this when 1.13 opens.
- [ ] Decorators / [ ] Closures
- [ ] Python's data model — dunder methods ↔ operators
- [~] PARKED per master: descriptor protocol, context-manager internals
- [ ] 32-bit vs 64-bit, word size

---

