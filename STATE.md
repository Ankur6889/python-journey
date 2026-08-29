# STATE.md — PYTHON LEARNING JOURNEY — LIVE SESSION STATE
# ═══════════════════════════════════════════════════
# One of FOUR files. THIS is the file that changes every session.
# HOW TO START SESSION 35 (for Claude):
#   1. Read RULES.md fully (**v5 — unchanged in S33 and S34**), then this file
#      fully. No re-introductions. No ARCHIVE.md unless gauntlet.
#   2. FIRST ACTION: the INTERVAL GATE. S34 ran Sat 29 Aug ~16:00–18:30, a few
#      hours after S33 closed. Ask the gap.
#   3. ⚠⚠ **ONE RULING IS OWED AT THE OPEN, AND HE RAISED IT (pushback 57).**
#      He asked that revision be RANDOM and spread across days, not
#      "taught yesterday, tested today". **THE MENTOR'S RECOMMENDATION IS: NOT
#      A NEW RULE.** Random spaced recall is already binding doctrine (RETENTION
#      SYSTEM 2, 3 and 5), and the adopted remedy for the queue being unrunnable
#      by hand is RULES proposal 6 — **move it into a SCRIPT, which is already
#      designated build block 02 and still unbuilt.** Put that to him in one
#      line; he is entitled to overrule it and have a rule written.
#   4. ⚠⚠ **THE AUGUST GAUNTLET IS THE LAST SESSION OF AUGUST AND IT IS
#      SACRED. Only Sun 30 and Mon 31 remain.** He closed S34 saying he wanted
#      to start a fresh session for 1.9 immediately. **ASK AT THE OPEN which
#      this is — 1.9, or the gauntlet — and SAY WHICH BEFORE TEACHING.** If
#      gauntlet: load ARCHIVE.md and master/ at START, pure mixed recall, no new
#      material, carrying the strict-legend audit under CARRY FORWARD.
#   5. ⚠⚠ **MENTOR FAILURE, S34, AND IT IS THE HEADLINE: THE MENTOR ASKED HIM
#      TO RUN PYTEST.** Item 8 below has said for two sessions that he never
#      runs it. Worse, it was asked while ENFORCING the five-checks gate — so
#      the gate was made impossible to discharge and he was held to it twice.
#      **He caught it: *"I am not able to run the test myself... don't delay the
#      session for unnecessary things."* Pushback 56, upheld in full.**
#      **THE FIVE CHECKS ARE DISCHARGED BY CALLING HIS OWN FUNCTION AND LOOKING
#      AT WHAT COMES BACK. Never by pytest. Say so when issuing the drill.**
#   6. ⚠ **THE FIVE CHECKS: NEW FAILURE MODE. REPORTED BUT NOT RUN.** S33's win
#      was getting them reported at all. S34 got a full report — "khaali taken
#      care of, ek taken care of, bahar taken care of" — on two functions that
#      both FAILED, one of them on the worked example printed in its own
#      docstring. **He wrote the report by READING HIS CODE, not by executing a
#      case.** The gate now has to name the form: **the case, the value that
#      came back, matched or not.** An `if` existing in the body is not a check.
#   7. ⚠ **PYTEST IS NOT TAUGHT AND IS NOT SCHEDULED IN LAYER 0. THE MENTOR
#      WRITES AND RUNS EVERY TEST FILE. Never ask him to.** ⚠ **BREACHED S34.**
#   8. ⚠ **CHECK THE FILE IS SAVED (mtime) BEFORE READING IT.** Held clean in
#      S34 — the first "Done" came on an untouched file and mtime caught it
#      before a word was said about his code. Keep doing exactly that.
#   9. At session end: rewrite this file, tick CURRICULUM.md if anything moved,
#      append one block to ARCHIVE.md, commit and push.
#
# STATE AS OF: end of Session 34, Sat 29 Aug 2026 ~16:00–18:30.
# Next: Session 35 — **1.9 ERROR HANDLING, or the AUGUST GAUNTLET. ASK.**
# ═══════════════════════════════════════════════════

## SCHEDULE POSITION (recompute formally 31 Aug — in ITEMS, not subsections)
- **DEADLINE: Layer 0 closes 30 Sep 2026.** ~5 sessions/week needed; zero slack.
- **S34 yield: TWO LEDGER PROMOTIONS, ONE CURRICULUM TICK (tuple).**
  `drills/s34_tail.py` 36/36 green, but only after three wrong fixes on one
  function. **A short session (~2½ h) and a same-sitting one, declared as such.**
- **Position: 1.1–1.7 closed. 1.8 — THREE bullets still [~]. 1.9–1.13 remain,
  ~4½ wk.**
- **1.8 — what remains, exactly. It shrank from five to three:**
  - ✅ `tuple` — **CLOSED S34**, `drills/s34_tail.py::reading_stats`, task-first
    and cold. ⚠ Caveat written next to the tick: `.count()` was an honest gap in
    S33 hours earlier, so that one method carries an ECHO RISK — re-ask at the
    gauntlet.
  - `set` — **[x] CANDIDATE, ONE ONE-LINE ASK AWAY.** Order instability asked
    and PASSED cold (7/10). Only **`{}` builds a dict, `set()` is the only empty
    set** is un-asked. Fire it first thing.
  - `dict` — **`.keys()`/`.values()` as VIEWS supporting set operations STILL
    never asked.** He solved `shared_keys` with `set(a) & set(b)` — correct, and
    it proves he owns "looping a dict gives the KEYS", but it converts instead of
    using the view. ⚠ **The mentor said it would ask this after the drill and
    then never did.** ONE line: *what is `a.keys()`, and why does `&` work on it?*
  - `list` — **HELD [~] DELIBERATELY.** Roster, slicing and `sorted`/`.sort()`
    were all clean cold, but the bullet's own named core — the returns-`None`
    tell — **broke live in his code**. Will not tick a bullet whose load-bearing
    half failed in front of the mentor the same hour.
  - `when to use which` — untouched; taught S33, still ineligible until a
    later-day ask.
- **AUGUST GAUNTLET: last session of August. SACRED.** See header item 4.
- **RE-BASELINE formally due 31 Aug.** Observed throughput → derived date.
  Scope moves NEVER cut.
- ✅ **BUILD BLOCK 01 FULLY CLOSED.** ⚠ **`LOG.md` STILL NOT WRITTEN. FIFTH
  SKIP. For block 02 it is step ONE, before any code.**
- ⚠⚠ **NEXT BUILD BLOCK IS NOW URGENT AND HE HAS INDEPENDENTLY ASKED FOR IT:
  the re-test queue SCRIPT.** Settled since S21, 75+ rows against a ~30-row
  trigger, and S34 produced the evidence that hand-scheduling has failed —
  `while` mechanics SEVEN sessions overdue, `.keys()`/`.values()` never asked
  since S26, `SyntaxError` missed in S27 and again in S32. **That is block 02.**
- Current Layer: 1. Current Topic: **1.9 error handling; 1.8's three-bullet tail
  rides the queue.**

## RULE-CHANGE PARKING (adopt ≤1 per session, at close)
- ⚠⚠ **PARKED S34, RAISED BY THE STUDENT (pushback 57), RULING OWED AT THE S35
  OPEN:** *"revision should be random and not like this-this-yesterday-should-be-
  tested-today, I need random recall even after days."*
  **MENTOR RECOMMENDATION: DO NOT WRITE A RULE.** It is already doctrine —
  RETENTION SYSTEM 2 (spaced re-tests at ~1 wk / ~1 mo), 3 (monthly gauntlet =
  pure MIXED recall) and 5 (question bank as a pool). What has failed is not the
  policy but its EXECUTION by hand, and the remedy for that is also already
  adopted: **RULES proposal 6 — put the queue in a SCRIPT. That is build block
  02.** Same shape as the S33 ruling: fix the behaviour, build the tool, do not
  grow the rulebook. **He is entitled to overrule this and have a rule written —
  put it to him in one line and take his word for it.**
  ⚠ One correction owed with it, on the facts: **S34 did not test S33 material.**
  Everything asked was S24–S27, two to five days cold, and everything from S33
  was DEFERRED at the open for exactly his reason. His policy point stands; his
  factual premise about this session did not.
- **DROPPED, RECORD CLOSED:** *"A [RECALL] block has a budget."* Do not re-raise.
- ⚠ Considered and **NOT** parked in S33: a rule requiring an operator-level
  grep before any snippet. **It is not a new rule — it is DEFINE BEFORE USE,
  substrate included, tenth occurrence. Fix the behaviour, not the rulebook.**

## WHERE WE LEFT OFF

### SESSION 35 STARTS HERE — exact resume point

S34 ran Sat 29 Aug ~16:00–18:30, a few hours after S33 closed — declared a SAME
SITTING at the open, so all S33 material was deferred and only S24–S27 material
was tested. He closed it himself and said he wanted **1.9 as a fresh session,
starting immediately**.

Run in this order:

1. **INTERVAL GATE, then DECLARE THE SESSION KIND** (1.9 or gauntlet — header
   item 4). **Then take the RULE RULING he is owed** — header item 3, one line.

2. ⚠ **TWO ONE-LINE ASKS THAT CLOSE TWO 1.8 BULLETS. FIRE THEM FIRST; THEY COST
   THREE MINUTES.** Both were queued at the end of S34 and dropped when he
   called stop, and one of them the mentor had already promised once and forgot.
   - **`{}` builds a DICT; `set()` is the only empty set.** → closes `set`.
   - **What is `a.keys()`, and why does `&` work on it directly?** → closes
     `dict`. He wrote `set(a) & set(b)` in S34: correct, but a conversion where
     a view would do.

3. ⚠⚠ **THE MUTATING TELL — AND S34 SPLIT IT PRECISELY. READ THIS BEFORE
   RE-TEACHING IT.** The row is not broken as a whole. In `ranked` he wrote
   `sorted(values)` and commented, unaided, *"could have also used values.sort()
   but that will mutate the passed list so not using that"* — **he owns TYPE and
   he owns MUTATES.** Ninety seconds later he wrote `list(set(names.sort()))`.
   **What is gone is only the RETURN-VALUE half: that a mutating method hands
   back `None`.** Teach and test THAT half alone; the other two are intact.
   (Still `[~]`, demoted S33. Not promotable on S34 evidence — it failed.)

4. ⚠⚠ **`reversed()` IS NOW BROKEN IN BOTH DIRECTIONS AND THIS IS THE FILE'S
   CLEANEST NAME-COLLISION EVIDENCE.** S33: he avoided `reversed()` believing it
   mutates. S34: he reached for `reversed()` believing it ORDERS — offering
   `return reversed(list(set(names)))` for a docstring asking ascending
   alphabetical. **Same collision, opposite error, one day apart.**
   ⚠ **HE STILL OWES THE ANSWER TO "what does `reversed(x)` hand back?" — asked
   in S34 and never answered; he jumped straight to a corrected line.** That is
   depth-before-answer and it was not re-asked. **Re-ask it, and teach the two
   as a PAIR IN ONE TABLE (the S33 watch-area remedy for collisions).**

5. ⚠ **`SyntaxError` — NOT FIRED IN S33 OR S34. STILL OWED, STILL PRIORITY.**
   **Named repeat pattern: missed in S27 and again in S32, five sessions apart,
   same shape (a statement put where a value belongs). Fire it cold, in a shape
   he has not seen.** It is 1.9 substrate — fire it inside the subsection.

6. ⚠ **THE FOUR-STATION HOOK BY NAME — NOT FIRED IN S33 OR S34. STILL OWED.**
   S32 showed USE without RECALL. Ask him to name the stations, in order,
   including Station 0. ⚠ **S34 gave a live datapoint: shown
   `list(set(names.sort()))` he could not name the error at all** (*"I can't see
   the fault... I believe its correct"*) — an honest gap, declared. The label
   `TypeError: 'NoneType' object is not iterable` is Station 3.

7. ⚠ **`del` and `.clear()` — HALF-DISCHARGED ONLY.** `del` as a STATEMENT
   handing back nothing, and `.clear()` → `None` leaving `{}`, were never asked.
   They pair naturally with `SyntaxError` (`print(del d[k])`) — but use a
   DIFFERENT shape from S32's snippet.

8. ⚠ **CONSTRUCTORS — cold ask owed.** His first word is still *"converts"*.
   **Row held [~] deliberately. It promotes when the right word is his FIRST
   word.**

9. ⚠ **`when to use which` — TAUGHT PROPERLY FOR THE FIRST TIME IN S33, and
   S34 was a same sitting so it was correctly deferred. IT IS NOW LEGITIMATE.**
   THE ASK QUESTION: *"WHAT AM I GOING TO ASK THIS CONTAINER?"* → in here?
   `set`. Value for a name? `dict`. Order/position? `list`. Must never change?
   `tuple`.

10. **THE SMALL COLD SET, fired mixed, NOT as a block:**
    - **`while` mechanics — NOT touched since S23. EIGHT sessions overdue.**
    - HASHABILITY; `subscriptable`; `AttributeError`.
    - unpacking count-mismatch ⇒ `ValueError`.
    - `zip` fails silently — twice.
    - ⚠ Build a raising snippet in. S30–S33 all did; S34's arrived by accident
      out of his own bug, which worked well — **but that was luck, not design.**

11. **THEN 1.9 — ERROR HANDLING.** ⚠ **The overdue error-label set IS 1.9's
    substrate** — `SyntaxError`, `AttributeError`, `KeyError`/`IndexError`, the
    four-station hook. **Run the revision INSIDE the new subsection rather than
    ahead of it; this was the S33 and S34 plan and it is still the right one.**
    Build `traceback` from the UNCAUGHT-exception trigger (self-rated 3/10 when
    1.9 was scoped).

**Standing turn rules: FRAME FIRST — and if he says "I don't understand the
question" TWICE, that is a frame failure, not a comprehension failure; SPEC
gives exact interfaces and exact expected values, IN A FILE IN THE REPO, with a
mechanical check per acceptance condition (boundary cases live in the TESTS);
short messages, one teaching idea per turn, asks near the top; doubt gate before
every new subsection; depth-before-answer — traces never optional AND A CORRECTED
LINE DOES NOT DISCHARGE AN UNANSWERED MECHANISM QUESTION (S34: `reversed`);
THE FIVE CHECKS ARE THE GATE ON THE WORD "DONE" AND THEY ARE RUN BY CALLING HIS
FUNCTION, NEVER BY PYTEST — ask for the case, the value back, and matched-or-not;
boundary values first. Tag every block and CHECK THE TAG IS RIGHT. Give the
verdict after the rating. Do not propose ending the session.**

**CARRY FORWARD:**
- **August gauntlet: SACRED.** Carries: strict-legend audit of every [x] —
  every BUNDLED S16 promotion; the 1.6 spoken Feynman recall; the S22
  short-gap promotions; the eight S23; the eleven S25; the eight S27; the S29
  `zip`; the eight S30; the four S31; the four S32; the seven S33; **and the two
  S34 — plus the `.count()` echo caveat attached to the tuple tick.**
- ⚠ **NEITHER S34 PROMOTION CARRIES A CONFIDENCE RATING EXCEPT `set` UNORDERED
  (7/10).** `sorted` vs `.sort()` was promoted off code and an unaided written
  comment, with no rating taken — the mentor did not ask. Under RULES proposal 2
  the rating sets the INTERVAL, not the promotion, so **the interval defaults to
  SHORT: re-ask it early.**
- **31 AUG: RE-BASELINE arithmetic due, in ITEMS.**
- `None`/`is None` and `bool("False")` remain [~] — **though the `None`-is-not-
  nothing row that made them urgent CLOSED in S33.**
- **`str` immutability is still an [x] candidate on one clean later-day pass.**
- Governance/format requests mid-session → PARK, close material, write at end.
  Exception (S28): he may override the park and order a rule written at once.
- Drills: mentor never edits a file the student started; autocomplete OFF.
- ⚠ **`abs()` still owed a proper definition.** Level-1 audit list: `len()`,
  `range()` as an object, `.append()` vs `+`, `abs()`, `print()` (**he said it
  "takes in a string"; it takes ANY object and calls `str()` on it**).
  ✅ **`import` DISCHARGED S33** — given a one-line Level-2 model (it binds the
  NAME to a module object; the `.` is the one he already owns).
- ⚠ **STYLE, S33, both minor and both worth repeating once:** `import` belongs
  at the TOP of the file, not inside the function; and `i` conventionally means
  an INDEX — `[i for i in angles ...]` should be `[a for a in angles ...]`.

Every teaching block shows full runnable source alongside output.
Session 34 closes with a ~30-second spoken summary from memory.

## TERM RE-TEST QUEUE (live — fire cold at session open; "gap" if empty)
Histories live in ARCHIVE.md; this table carries only current status.
⚠ **SIZE BREACH, DECLARED NOT HIDDEN: 75+ rows against the ~30-row trigger in
RULES proposal 6. Adopted remedy is a SCRIPT IN THIS REPO. Still unbuilt — it
is the designated build block 02.**

| Term | Decode hook / mechanism | Status | Next due |
|---|---|---|---|
| ⚠⚠ **mutating vs non-mutating — THE TELL** | **(1) TYPE FIRST (2) returns `None` ⇒ it mutated (3) a VALUE back tells you NOTHING — `.pop()` returns the item AND mutates** | **[~] DEMOTED S33. ⚠⚠ S34 SPLIT IT PRECISELY: he owns TYPE and owns MUTATES — wrote *"could have used values.sort() but that will mutate the passed list"* unaided — then 90 s later wrote `set(names.sort())`. **ONLY THE RETURN-VALUE HALF IS GONE.** Teach and test that half alone** | **S35 PRIORITY — the return-value half** |
| ⚠⚠ **`reversed()` vs `.reverse()`** | **`reversed(x)` is a BUILT-IN returning an ITERATOR, mutates nothing, and REVERSES — it does not ORDER. `x.reverse()` is a METHOD, mutates, returns `None`** | **[~] ⚠⚠ NOW BROKEN IN BOTH DIRECTIONS. S33: avoided it believing it mutates. S34: reached for it believing it sorts — `reversed(list(set(names)))` for an ascending-alphabetical spec. ⚠ "What does it hand back?" ASKED S34 AND NEVER ANSWERED** | **S35 PRIORITY — teach as a PAIR IN ONE TABLE** |
| **`copy.deepcopy`** | **new outer container AND new contents recursively, all the way down. Not "the better copy" — slower, and buys nothing on a flat container of immutables** | **[x] PROMOTED S33 — written cold in `drills/s33_copies.py` from a docstring that never named it; all six independence tests green first run. Rated 7** | **short gap — ~2 Sep** |
| **slicing / SHALLOW COPY** | **`[start:stop:step]` half-open, builds a NEW list; `l[:]`, `list(l)`, `l.copy()` copy the OUTER container, references SHARED. Shallow = ONE level deep** | **[x] PROMOTED S33 — cold on `dict(defaults)` with a nested list: correct value AND both halves (why the inner edit leaks, why the new key does not). Derived unprompted S32** | **~3 Sep** |
| **`*` ON A SEQUENCE** | **repeats the REFERENCE, not the contents. SAFE when the element is immutable, a TRAP when mutable — `[[0]*3]*3` shares one row** | **[~] NEW S33, taught after the breach (pushback 55). He resolved the trap himself off shallow copy and asked the right question — *"but 0 is not mutable"*** | **S34** |
| **MUTATE-WHILE-ITERATING** | **`for` keeps an internal POSITION COUNTER; removing an item slides the next into a slot already passed. DON'T REMOVE — SELECT: `[a for a in angles if a <= 180]`** | **[~] NEW S33 — [PREDICT], so not eligible. ⚠ He predicted the SAFE-LOOKING list correctly and the failing one wrong** | **S34 cold** |
| **when-to-use-which** | **⚠ THE DECIDING QUESTION IS "WHAT AM I GOING TO ASK THIS CONTAINER?" in here → `set`; value for a name → `dict`; order/position → `list`; never changes → `tuple`** | **[~] ⚠ FRAMED PROPERLY FOR THE FIRST TIME S33 after he twice said he did not understand the question — mentor's FRAME FIRST breach. He had `dict` and `list` right and folded the `set` in** | **S34 cold — first legitimate ask** |
| **set difference `-`** | **`set(a) - set(b)` builds a NEW set ⇒ an EXPRESSION. `-` is NOT symmetric** | **[x] PROMOTED S33 — `missing_joints` written in one line cold. Taught S30, never once tested until now** | **~5 Sep** |
| **BOUNDARY-FIRST (his own S20 rule)** | **when a condition uses `<` `<=` `>` `>=`, test the value ON the boundary FIRST** | **[x] PROMOTED S33 — he read `<=` off the PROMISE before writing, and reported it unprompted as check 1** | **~5 Sep** |
| **THE FIVE CHECKS** | **"Boundary pe khaali ek bahar mila". ⚠ `ek` = smallest NON-EMPTY case. ⚠ `bahar` = TYPE as well as sign. ⚠⚠ A CHECK IS A CASE YOU RAN AND LOOKED AT — not an `if` in the body** | **⚠⚠ NEW FAILURE MODE S34: REPORTED BUT NOT RUN. Full report given — "khaali taken care of, ek taken care of, bahar taken care of" — on two functions that both FAILED, one on the worked example in its own docstring. Written by READING the code** | **S35 — demand case / value back / matched** |
| **format spec — ALIGNMENT** | **TEXT HUGS LEFT, NUMBERS HUG RIGHT — which is why decimal points stack and you compare magnitudes without reading digits** | **[x] PROMOTED S33, 8/10, cold, NO ARROWS — fourth session live, closed. The *why* was volunteered too but was taught S32** | **~8 Sep** |
| **⚠ `None` IS NOT NOTHING** | **`None` is an OBJECT and fills a slot: `len([None]) == 1`. Nothing is the absence of a slot: `len([]) == 0`** | **[x] PROMOTED S33, 7/10 — `[150, None]` given cold with the mechanism, then `0 1` stated directly. ⚠ A KNOWLEDGE-STRUCTURE gap closed in ONE NIGHT** | **short gap — ~2 Sep** |
| **`list()`** | **CONSTRUCTOR CALL — new list from any iterable; drains an iterator; CATCHES `StopIteration` ⇒ `[]`, not `[None]`** | **[x] PROMOTED S33, 7/10 — value corrected unaided, and he re-derived the reason himself** | **~2 Sep** |
| **constructors** | **`dict()`/`list()`/`set()`/`tuple()` BUILD A NEW CONTAINER from an iterable — not a type conversion. Copying the PAIRS, not the things they point at, is *why* it comes out shallow** | **[~] HELD S33 DELIBERATELY — his first word was still "converts"; "builds a new object" came only after the mentor pointed at the word** | **S34 — promotes when it is his FIRST word** |
| **`SyntaxError`** | **STATION 0 — grammar broke, so NOTHING ran. ⚠ NO FRAMES IN THE TRACEBACK, because there was never a running program** | **[~] ⚠⚠ NOT FIRED IN S33 — session never reached it. NAMED PATTERN: missed S27 and S32, same shape** | **S34 cold, PRIORITY, NEW SHAPE** |
| **FOUR-STATION HOOK + STATION 0** | **DID IT RUN? → NAAM → DOT → TYPE → CHEEZ. Station 4: jagah=Index, chaabi=Key, cheez=Value** | **[~] ⚠ NOT FIRED IN S33. S32 showed USE without RECALL** | **S34 cold, full hook by name** |
| **`del` vs `.pop()` vs `.clear()`** | **`del` is a STATEMENT, hands back nothing; `.pop(k)` hands back the VALUE — ALWAYS; `.clear()` → `None`, leaves `{}`** | **[~] HALF-DISCHARGED S33 — `.pop(k)` stated correctly unaided, including `KeyError` on a missing key. `del` and `.clear()` never asked** | **S34 cold — the other two halves** |
| **`while` vs `for`** | **condition re-checked vs walking an iterable** | **[x]-grade S23. ⚠ NOT touched S27–S33** | **⚠ SEVEN sessions overdue** |
| **`.items()` / `.keys()` / `.values()`** | **looping a dict gives the KEYS; `.items()` gives TUPLES; `.keys()` is a VIEW supporting SET operations** | **[x] `.items()` S30. ⚠⚠ `.keys()`/`.values()` AS VIEWS **STILL** NOT ASKED — blocks the 1.8 dict bullet. S34: he wrote `set(a) & set(b)`, which proves looping-a-dict-gives-KEYS but converts instead of using the view. **The mentor promised this ask in S34 and never fired it*** | **S35, first thing** |
| **set — UNORDERED** | **a set has NO positions at all — not "no fixed order". Which is why it is not subscriptable, and why `set()` destroys any order you built before it** | **[x] PROMOTED S34, 7/10, cold — named unprompted off his own failing output `['b','c','a']`. Sharpened from "doesn't have a fixed order" to UNORDERED** | **~5 Sep** |
| **`{}` is a DICT** | **`{}` builds an empty dict; `set()` is the ONLY way to write an empty set** | **[~] STILL NEVER ASKED — the last thing blocking the 1.8 set bullet** | **S35, first thing** |
| tuple roster | `count` and `index` ONLY | **[x] PROMOTED S34 — both reached for unaided in `reading_stats` from a docstring naming neither. ⚠ ECHO CAVEAT: `.count()` was an honest gap in S33 a few hours earlier, so this one method is not fully cold** | **gauntlet — re-ask `.count()` specifically** |
| **tuple (unit)** | **immutable ordered sequence; the COMMA makes it; `TypeError` on item assignment** | **[x] CURRICULUM BULLET TICKED S34 — the task-first cold pass owed since S26 was run: `reading_stats` over a tuple, `.count()`/`.index()`, and a returned tuple `(0, -1)`** | **~5 Sep** |
| **list method roster** | `append` `extend` `insert` `sort` `remove` mutate → `None`; `pop` returns the ITEM | **[~] S34: `insert`, `remove`, `sort` used cold and correctly, `append`/`extend` named unprompted in his own comments. ⚠ HELD — the roster is fine, the returns-`None` half is what broke** | **S35** |
| **hashable** | **hash must be STABLE ⇒ key must be immutable** | **[~] S26/S27, untested** | **S34 cold** |
| **`zip` FAILS SILENTLY — TWICE** | **unequal lengths ⇒ truncates to the SHORTEST; exhausted ⇒ `[]`, no error** | **[~] S28, untested S29–S33** | **S34 cold** |
| `AttributeError` | the name after the DOT is not on the object | **[~] passed cold S27, 6/10. One clean pass promotes** | **S34** |
| **subscriptable** | **can be indexed with `[ ]`. `list`/`tuple`/`str`/`dict` are; `set` is NOT** | **[~] NEW S27, untested** | **S34 cold** |
| **unpacking** | **two names on the left take apart the tuple on the right** | **[x] core PROMOTED S30. ⚠ COUNT-MISMATCH ⇒ `ValueError` half NEVER asked** | **the ValueError half, S34** |
| **THE RAISE-VS-SHRUG PAIRING** | **`d[k]`/`.get()`, `del d[k]`/`.pop(k,default)`, `remove`/`discard`. Raise when absence is a BUG; shrug when expected** | **[x] S32, 7/10** | **~2 Sep** |
| **`.get()` vs `[]`** | **`[]` when missing is a BUG; `.get()` when absence is EXPECTED. ⚠ `.get()` with no default MOVES THE CRASH AWAY FROM THE CAUSE** | **[x] S32 — and used correctly again in S33's `len(results)` question** | **~5 Sep** |
| **`remove` vs `discard` (sets)** | **same job; `remove` raises `KeyError` when absent, `discard` shrugs** | **[x] S32** | **~5 Sep** |
| **tuple immutability** | **item assignment on a tuple ⇒ `TypeError`. Immutability has NO error of its own; it arrives as `TypeError`** | **[x] S32, 5/10, COLD** | **~1 Sep** |
| **dict** | **key → value; `[]` takes a KEY. Keys UNIQUE — existing key OVERWRITES** | **[~] ordering, `.items()` and raise/shrug thirds all discharged; VIEWS outstanding** | **S34** |
| **single return value** | **`return a, b` builds ONE tuple** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **THE COMMA MAKES THE TUPLE** | **not the parentheses. `(1)` is an `int`; `1, 2` is a tuple** | **[x] S31, cold, 8/10** | **gauntlet, then ~9 Sep** |
| **f-string — THE THREE STEPS** | **evaluate the expression → call `str()` on it → splice it in** | **[x] S31, 8/10** | **gauntlet, then ~9 Sep** |
| **format spec — width + precision** | **`{v:8.1f}`. ⚠ THE NUMBER IS TOTAL FIELD WIDTH** | **[x] S31, 10/10 — restated correctly again unprompted in S33** | **~10 Sep** |
| **`<` `>` `^` in a format spec** | **force left / right / centre — they OVERRIDE the type default** | **[~] NEW S32, taught after the breach** | **S34** |
| **DRY / one copy of a decision** | **if a rule is written in four places you will change three and miss one** | **[~] S31 — applied correctly and fast, but taught same session** | **S34 — later-day ask** |
| **`set()` / `\|` `&` `-`** | **`set()` is the ONLY empty set. Union / intersection / difference build a NEW set ⇒ EXPRESSIONS** | **[x] the `-` half S33; **the `&` half PROMOTED S34** — `shared_keys` written in one expression cold. `\|` still untested** | **`\|` S35** |
| **`sum()`** | **totals an iterable; returns a new value; `sum([])` is `0`** | **[~] S30 SUPPORTING, written cold** | **S34** |
| **`abs()`** | **distance from zero, sign discarded** | **[~] ⚠ USED UNPROMPTED IN S30 AND STILL NEVER TAUGHT** | **S34 — define it properly** |
| **`print()`** | **⚠ takes ANY object and calls `str()` on it — NOT "a string"** | **[~] NEW S32. Level-1 audit item** | **S34** |
| **`import`** | **binds the NAME to a MODULE OBJECT; `copy.deepcopy` is the same `.` he already owns. HOW it finds the module is 1.10** | **✅ DISCHARGED S33 — Level-2 model given, and he used `import copy` correctly in the drill** | **1.10** |
| **`_` as a name** | **an ordinary name, used by convention for "I am not going to use this value"** | **[~] NEW S33, one line** | **low priority** |
| **list comprehension** | **an EXPRESSION that builds a NEW list. `[EXPR for VAR in ITERABLE if COND]`** | **[x] S30, 16/16 cold — used cold twice more in S33** | **~8 Sep** |
| **comprehension execution order** | **iterable → variable → gate → expression. WRITTEN ORDER ≠ EXECUTION ORDER** | **[x] S30, 8/10** | **~8 Sep** |
| **the filter as a GATE** | **`if` runs BEFORE the expression** | **[x] S30** | **~8 Sep** |
| **dict comprehension** | **`{KEY: VALUE for VAR in ITERABLE}`. The BRACES and the COLON** | **[x] S30** | **~8 Sep** |
| **dict insertion ordering** | **keys stay in FIRST-INSERTION order. ⚠ ORDERED ≠ SORTED** | **[x] S30** | **~8 Sep** |
| **`KeyError` vs `IndexError`** | **⚠ THE BRACKETS DON'T DECIDE THE ERROR — THE CONTAINER DOES** | **[x] S30, 7/10** | **~8 Sep** |
| **`zip`** | **pairs parallel ITERABLES; each pass yields a TUPLE** | **[x] S29, 8/10** | **gauntlet, then ~7 Sep** |
| **braces hold an EXPRESSION** | **calls, lookups, arithmetic, comparisons, even a COMPREHENSION — but never a `for` loop** | **[x] S31** | **~9 Sep** |
| **comprehension scope** | **its variable does not exist afterwards ⇒ `NameError`. ⚠ A FOOTNOTE** | **[~] S28** | **low priority** |
| **when NOT to use a comprehension** | **it BUILDS A CONTAINER. If the expression DOES rather than PRODUCES, you wanted a loop** | **[~] S28, untested** | **S34** |
| **`ZeroDivisionError`** | **decodes cleanly; formally belongs to 1.9** | **[~] S28** | **with 1.9** |
| **negative index** | **counts backward from the end; `-1` is last** | **[x] S24 — ⚠ S33 used cold and correctly in `replay_order`** | **~10 Sep** |
| coercion | coerce = force; implicit safe conversion | [x] S16 | ~9 Sep |
| ValueError | value wrong, type OK; `int("2.5")` | [x] S18 | ~10 Sep |
| TypeError | operation not defined for the type; `"5"+3` | [x] S18, re-passed S27/S28/S32 | ~5 Sep |
| truncation | cut off TOWARD ZERO | [x] S23 | ~10 Sep |
| floor division | floors toward −∞ | [x] S23 | ~10 Sep |
| alias | two names, one object | **[x] S26 — the root of the whole S32/S33 copy chain** | ~14 Sep |
| rebind | `=` points a NAME at an object | [x] S24 | ~14 Sep |
| operand | value an operator acts on | [x] S23 | ~10 Sep |
| **expression vs statement** | **value vs action. HIS OWN TEST: can it go inside `print(...)`?** | **[x] S27 — the highest-earning row in the file** | **~1 Sep** |
| **precedence / associativity** | **rank between operators / direction within a rank** | **[x] S27** | **~15 Sep** |
| short-circuit | and/or stop early, return the OPERAND | [x] S16 | ~9 Sep |
| modulo identity | sign follows divisor | [x] S23 | ~10 Sep |
| control flow / conditional / truthy-falsy / block-vs-frame | S14 set | [~] | **OVERDUE** |
| indentation | spacing that DELIMITS a block | [x] S16 | ~9 Sep |
| iterable / iterator | reusable / consumed | **[x] — ⚠ S33: said "the iterable was empty", SELF-REPAIRED unprompted and named it a saying error not a concept error** | ~10 Sep |
| **StopIteration** | **the stop signal; an EXCEPTION. `list()` is what CATCHES it** | **[x] S25, reinforced S28/S32/S33** | ~11 Sep |
| `next()` / `iter()` | `iter()` once, `next()` per pass | [x] S25 | ~11 Sep |
| range | half-open, lazy, an ITERABLE | [x] S16 | ~9 Sep |
| **indexing** | **`[]` takes a POSITION; 0-based; out of range ⇒ `IndexError`** | **[x] S30** | **~8 Sep** |
| **traceback** | **crash report; each line = one live frame** | **[x] S27, 8/10** | **~15 Sep** |
| NameError | the NAME does not exist anywhere | [x] S18, S28 | ~10 Sep |
| function scope, not block scope | only `def` makes scope | [x] S16 | ~9 Sep |
| `print()` `sep`/`end` | between items; after everything; returns `None` | [x] S25 | ~11 Sep |
| **`break` / `continue` / `pass`** | **bahar niklo / agla chakkar / jagah bharo** | **[x] S27, 8/10** | **~15 Sep** |
| chained comparison | middle operand evaluated ONCE | [x] S16 | ~9 Sep |
| **loop `else` / ternary** | **runs only without `break` / `A if C else B` is an EXPRESSION** | **[x] S27** | **~15 Sep** |
| elif | chain, first true wins | [x] S17 | ~10 Sep |
| **keyword argument / parameter vs argument** | **`name=value` in the CALL / name in the `def` vs what you pass** | **[x] kwarg S27. ⚠ parameter-vs-argument labels still [~]** | **S34** |
| UnboundLocalError | name IS local, no value bound yet | spelling FIXED S23 | mixed 3-error test |
| **`sort` vs `sorted`** | **`sort()` mutates → `None`; `sorted()` builds a NEW list** | **[x] RE-PROMOTED S34 — the clean cold pass CURRICULUM said was owed since the S24 inversion. Wrote `sorted(values)` and `values.sort()` correctly in adjacent functions and explained the choice unaided. ⚠ NO RATING TAKEN — interval defaults SHORT** | **~1 Sep** |
| pre-order / post-order | before the call / after the call | [x] S23 | ~10 Sep |
| lambda | EXPRESSION form of a function | [x] S23 | ~10 Sep |
| docstring / `__doc__` | FIRST statement of the body; POSITION makes it | [x] S25 | ~1 Sep |
| `key=` | sorts by RESULTS, returns ORIGINAL items | [x]-grade S23 | ~10 Sep |
| cell / closure four layers | one-slot box; name → function → `__closure__` → CELL → `cell_contents` | [x] S25 | ~1 Sep |
| None-as-absence vs empty container | collectors give `()`/`{}`; optional attributes give `None` | **[~] — ⚠ the `None`-is-not-nothing row it depended on CLOSED S33** | **S34** |

## RE-TEST QUEUE (live — update every session)

| Item | Latest result | Status / next due |
|---|---|---|
| **NESTED STRUCTURES + SHALLOW COPY + DEEPCOPY** | **S33 `drills/s33_copies.py` 25/25 cold, later-day; independence proven at both levels** | **[x] — CURRICULUM TICKED. ~3 Sep** |
| **COMMON PATTERNS AND PITFALLS (1.8)** | **S33 taught: mutate-while-iterating, `[[0]*3]*3`, container choice** | **[x] TICKED as taught+closed; the three rows themselves are [~] and re-ask S34** |
| **⚠ THE MUTATING TELL** | **S34 SPLIT IT: TYPE and MUTATES intact (his own unaided comment on `.sort()`); the RETURN-VALUE half gone (`set(names.sort())`)** | **[~] — S35 PRIORITY, the return-value half ALONE** |
| **`reversed()`** | **S34: reached for it believing it SORTS. Broken in BOTH directions now, one day apart. "What does it hand back?" asked and never answered** | **[~] — S35 PRIORITY, teach as a PAIR in one table** |
| **THE FIVE CHECKS** | **⚠⚠ S34: REPORTED BUT NOT RUN — a clean report on two functions that both failed. Written from reading the code** | **[x] concept / ⚠ PRACTICE BROKEN — demand case, value back, matched** |
| **`while` mechanics; nested loops; found-flag** | **NOT tested S27–S34** | **[~] ⚠ EIGHT sessions overdue** |
| Frames: definition, three contents | S14 held WITH HINT | [~] **overdue** |
| `<module>` entry point; running vs paused; stack not queue | S14/S27/S28 | **[x] candidate — one direct ask promotes** |
| Namespace vs frame | S14 not unaided | [~] **overdue** |
| Execution pipeline; REPL vs script | FAILED S7, never re-run | [~] **overdue badly** |
| The S16 promotion block (bundled) | rebinding-vs-mutation and aliasing RE-PASSED COLD S24 | [x] — **gauntlet: unbundle and re-ask each half** |
| `str` immutability | S17 + S26 supporting | **[x] CANDIDATE — one clean later-day pass** |
| `None`/`is None`/vs 0/False | S10 same-day only | **[~] — the structural half closed S33** |
| Type conversion traps | owed | **[~] due ~1 Sep — and "converts" is still his first word for a constructor** |
| Mutable default trap + sentinel | S12 pass | [~] due ~1 Sep |
| In-place mutators return `None` | S25 + S27 + S28 | **[~] — travels with the demoted TELL** |
| `__defaults__` | S22 cold, 7/10 | [x] — gauntlet, then ~17 Sep |
| Membership `in`/`not in` | S13/S26/S27 | [~] due ~5 Sep |
| Iteration protocol | S25 PASSED COLD; S32 exhaustion cold; **S33 exhaustion applied to `reversed()` unprompted** | **[x]** |
| Exceptions are signals | S18 pass; S28 `StopIteration` caught | [x] ~10 Sep |
| Traceback: each line = one live frame | S27 cold 8/10 | [x] — gauntlet, then ~15 Sep |
| loop `else` / `pass` / ternary / `break` / `continue` | S27 ALL PASSED COLD, 20/20 | [x] — gauntlet, then ~15 Sep |
| Mutable/immutable discriminator | S18/S24/S26/S27; **S33 applied correctly to `[0]*3` vs `[[0]*3]*3`** | [x] type half; **tell half DEMOTED — S34** |
| Closure definition + application; cell causation | S25 both PASSED COLD | [x] — gauntlet, then ~1 Sep |
| Function object vs call (`f` vs `f()`) | S25 supporting | [~] — one direct cold test promotes |
| Recursion | S20 same-day | [~] ~16 Sep |
| **`global` / `*args`/`**kwargs`** | **S22 10/10 and 8/10; S29 build block used all four forms cold** | **[x] CONFIRMED — use freely** |
| Lambdas | S23 PASS 6/6 cold | [x] — ~10 Sep |
| **COMPREHENSIONS (list + dict)** | **S30 16/16 cold; S33 used cold twice more** | **[x] — ~8 Sep** |
| **CONTAINERS AS CODE** | **S30 19/19; S32 17/17; **S34 36/36** across list, tuple, dict and set in one file** | **[x] — the tool half CLOSED** |
| **f-strings + format spec** | **S31 promoted; ALIGNMENT half PROMOTED S33, 8/10** | **[x] BOTH HALVES — ~8 Sep** |
| **TUPLE: the comma / immutability / roster** | **S31 comma; S32 immutability; **S34 the task-first cold pass owed since S26 — CURRICULUM BULLET TICKED** | **[x] — ~1 Sep** |
| **RAISE-VS-SHRUG (all three pairs)** | **S32 17/17 cold + the choosing rule** | **[x] — ~2 Sep** |
| **Four-station hook + Station 0** | **S32 RUN correctly twice unprompted; ⚠ NOT ASKED IN S33 OR S34. ⚠ S34 live datapoint: could not label `TypeError: 'NoneType' object is not iterable` at all — honest gap declared** | **[~] — S35, ask the hook BY NAME** |
| **DRY / one copy of a decision** | **S31 applied fast; taught same session** | **[~] — later-day ask, S35** |

## WATCH AREAS (full histories in ARCHIVE.md)
- Structured foundation over patches; solo-first; AI-reliance guarded.
- ⚠⚠ **THE S34 HEADLINE: A CHECK REPORTED IS NOT A CHECK RUN.** S33's win was
  getting the five checks reported at all, by making them the gate on "done".
  S34 got a fluent report — *"khaali taken care of, ek taken care of, bahar also
  taken care of"* — **on two functions that both failed, one of them on the
  worked example printed in its own docstring.** He wrote it by reading his code
  and seeing an `if`. **The S33 lesson was "change WHERE the ask sits". The S34
  lesson is the next one: an ask that can be satisfied without executing anything
  will be. Demand the ARTEFACT — the case, the value that came back, matched or
  not — not the assertion.**
- ⚠⚠ **THE MUTATING TELL IS NOT BROKEN AS A WHOLE, AND S34 PROVED WHICH THIRD IS
  GONE.** In `ranked` he wrote, unaided, *"could have also used values.sort() but
  that will mutate the passed list so not using that"* — TYPE owned, MUTATES
  owned. Ninety seconds later: `list(set(names.sort()))`. **Only the
  returns-`None` half is missing.** Four sessions of re-teaching all three parts
  have been treating a two-thirds-intact model as a ruin. **Teach the third.**
- ⚠⚠ **NAME COLLISION, AND `reversed()` IS NOW THE FILE'S CLEANEST CASE.** S33:
  avoided it believing it mutates. S34: reached for it believing it ORDERS. **Same
  pair, opposite errors, one day apart** — which is what a collision looks like
  when the machinery is intact and only the label is floating. **Teach collided
  names as a PAIR IN ONE TABLE.** Related: `sort`/`sorted`, `remove`/`discard`,
  `iterable`/`iterator`.
- ⚠ **HE DEBUGS WELL ONCE HE HAS THE TRACEBACK, AND POORLY WITHOUT IT.** Shown
  the failing line he said *"I can't see the fault, I believe its correct"* and
  could not name the error. Shown the traceback he found it in one line —
  *"ah fuck .sort returns None"* — unaided. **The gap is not reasoning; it is
  that he does not run the thing.** Same root as the five-checks failure above,
  and it is the strongest argument yet for the checks being executed.
- ⚠ **THREE WRONG FIXES BEFORE THE RIGHT ONE, AND THE SECOND WAS THE GOOD NEWS.**
  `sorted` → `set` → `reversed` → `sorted(list(set(...)))`. The middle step was
  him correctly applying the set-unordered fact he had just been promoted on, to
  demolish his own proposed fix. **He self-corrects when asked to trace; he does
  not self-correct when asked to write.**
- ⚠ **SELF-REPORTED FATIGUE, AND HE NAMED IT HIMSELF** — *"I am actually doing
  this for long, and lost my concentration."* It arrived immediately before the
  correct answer. Session length is his call; the mentor did not propose an end,
  stated what remained, and he chose.
- ⚠⚠ **MENTOR, AND IT IS THE WORST KIND: A GATE MADE IMPOSSIBLE TO DISCHARGE.**
  The five-checks gate was enforced twice on the word "done" — correct — but the
  form demanded was `python3 -m pytest`, **which STATE has said for two sessions
  he never runs.** He was held to a standard the channel could not deliver.
  **Check that an instruction is EXECUTABLE BY HIM before enforcing it.**
- ⚠ **MENTOR: A PROMISED ASK, NEVER FIRED.** The `.keys()`-as-a-view question was
  announced as coming "after the drill" and then lost to the `unique_sensors` fix.
  It blocks a 1.8 bullet. **Write promised asks into the resume point the moment
  they are made.**
- ⚠ **CONFIDENCE CALIBRATION — one rating all session (7 on set-unordered,
  correct). Everything else went unrated because the mentor did not ask.** ⚠ The
  S33 finding holds and got a second instance: **the real misses carried no
  rating because he could not produce an answer to rate. Silence is the low
  rating.**
- ⚠ **CHANNEL — mtime caught an untouched file on the first "Done".** Nothing was
  said about his code until he confirmed it was saved. Keep doing exactly that.
- ⚠ **LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL.** `len()`, `range()` as an
  object, `.append()` vs `+`, `abs()`, `print()`. ✅ `import` discharged S33.
- **FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 57 raised, 56 upheld or
  part-upheld.** S34 raised TWO. **(56)** *"I am not able to run the test myself
  — don't delay the session for unnecessary things"* — **upheld in full**, a
  direct breach of a standing STATE item. **(57)** *"revision should be random
  and not this-yesterday-tested-today, I need random recall even after days"* —
  **part-upheld**: the policy is right and is already doctrine, and the evidence
  that hand-scheduling has failed is overwhelming; **but his premise about this
  session was factually wrong** — S34 tested S24–S27 material only, and S33's was
  deferred at the open for his exact reason. Both halves were said to his face.

## CURIOSITY PARKING LOT
- venv; VS Code practices; notebooks; JIT; **IEEE 754 (1.13, promised)**;
  32/64-bit; `globals()`/`locals()` drill; senior traceback read (1.9);
  .pyc (1.10); GIL (1.13); concurrency (post-Layer 1); certifications; GC (1.13)
- `__iter__`/`__next__` + generators — 1.13, the promised S15 payoff.
  ⚠ **Generator EXPRESSIONS `(x for x in y)` remain deliberately unshown.**
- ⚠ **PEP 709 / how comprehension scope is actually implemented** — Level 3, 1.13.
- unit testing / pytest as a SUBJECT — not scheduled in Layer 0; say so plainly.
- `nonlocal` — belongs to 1.13. Do not open early.
- `pop` internals (S24) — Level 3, revisit in 1.13.
- **`copy.copy()` as the generic shallow form, and the `copy` module's own
  surface** — mentioned only in passing in S33; one line is owed.
- **Why `deepcopy` does not loop forever on a structure containing itself** —
  Level 3, park to 1.13.
- Bytecode / bare constant expressions (S25) — Level 3, 1.13.
- **HASHING as a mechanism** — Level 2 is the course target; collisions and
  resizing are DSA, master Layer 8.
- **HASH RANDOMISATION** — per-process seed. Park to 1.13.
- ⚠ **`%` and `.format()` string formatting** — owed as a READING skill.
- **`capsys` / testing printed output** — pytest machinery, NOT Layer 0.
- **DRY as a named principle, and "extract a function"** — one line, later.

---
