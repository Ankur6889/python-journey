# ARCHIVE.md — PYTHON LEARNING JOURNEY — SESSION HISTORY (append-only)
# ═══════════════════════════════════════════════════
# One of FOUR files. NOT loaded at normal session start. Load only for the
# MONTHLY GAUNTLET, a RE-BASELINE / SCOPE DECISION, or when the student asks
# ("what happened in Session N?", "when was X taught?").
# CONTENTS, in order:
#   A. The original v16 single-file header (superseded, kept for the record)
#   B. Version notes v16 → v1 (the per-session summary lines)
#   C. Student's observed strengths (evidence log)
#   D. Progress tracker (session-by-session yield and schedule notes)
#   E. Assignments log (table)
#   F. "What Session N established" — full narratives, S20 → S14
# NEW MATERIAL IS APPENDED at the end of section F as ONE block per session,
# plus one row in E and one bullet in D. Nothing here is edited afterwards;
# if a recorded measurement is struck (as `traceback` S16–S19 was in S20),
# the strike is recorded in the later block, the earlier text stays.
# ═══════════════════════════════════════════════════

## A. ORIGINAL v16 HEADER (superseded by the four-file split, 16 Aug 2026)

# PYTHON LEARNING JOURNEY - SESSION REFERENCE FILE
# ═══════════════════════════════════════════════════
# HOW TO USE THIS FILE (for Claude):
# This is a complete context document for an ongoing Python learning journey.
# When the student shares this file:
# 1. Read it fully before responding
# 2. Continue exactly from "Where We Left Off"
# 3. Follow ALL teaching style agreements listed below — they are non-negotiable
# 4. Do NOT ask for re-introductions — you already know the student
# 5. At end of each session, update this file and RETURN IT TO THE STUDENT FOR
# HIM TO UPLOAD MANUALLY, saved under the naming convention in OUR
# AGREEMENTS: python_learning_journey_<YYYY-MM-DD>_v<N>.md (date first,
# version number LAST).
# **DO NOT attempt to upload to Google Drive directly — Drive upload has
# failed at session end in Sessions 10, 11 and 12. Hand every file back as
# a download; the student uploads it himself. This is the standing
# procedure, not a fallback. Applies to this file, the master file, and the
# session_<N>.pdf notes.**
# 6. The student does not need to give any additional prompt —
# this file contains everything you need to begin immediately
# 7. At the end of EVERY session, create a separate session notes file named:
# session_XX_notes.md — concepts covered, mental models explained,
# code written, key insights, and common mistakes to avoid.
# Do this automatically — student should never need to ask.
#
# CHECKLIST LEGEND (STRICT — imported verbatim from the master curriculum,
# Session 6 reconciliation):
# [ ] = not started
# [~] = introduced / partially covered — taught but NOT yet demonstrated
# unaided. Also the status an item REVERTS TO if a spaced re-test fails.
# [x] = fully covered, drilled, and demonstrated WITHOUT AI assistance and
# WITHOUT notes. Being taught it well is not [x]. Getting it right
# during the session it was taught is not [x]. Only an unaided,
# from-cold demonstration on a later day earns [x].
#
# GOVERNANCE (Session 6 reconciliation, 29 Jul 2026; SINGLE-FILE SESSION
# PROTOCOL adopted post-Session 14, 8 Aug 2026, at the student's request to
# cut per-session context load):
# This file is one of TWO. The other is robotics_career_curriculum.md, the
# master file. Until Layer 0 (this file's Layer 1, Python Core) is closed,
# THIS file governs sessions. After Layer 0 closes, the master governs.
# LOADING PROTOCOL (binding):
# - At SESSION START, load THIS file ONLY. It is self-sufficient for running
# a session: every session-relevant binding rule, watch-area and queue
# lives here (the master's session-relevant content is mirrored here,
# including the NORTH STAR below).
# - The master is loaded at SESSION END, when the teaching is done, so both
# files can be updated together and returned as downloads.
# - EXCEPTIONS — load the master at SESSION START instead when: (a) it is a
# MONTHLY CHECKPOINT / GAUNTLET session; (b) a SCOPE DECISION or
# re-baseline is on the agenda; (c) the student explicitly asks.
# **SESSION 15 PRECEDENT: the student asked mid-session for a schedule
# review ("aaj hamko kitna complete karna chahiye tha aur hum kahan hain?").
# That is exception (c) and it legitimately triggered loading the master
# mid-session. Answering a plan question from memory would have been a
# guess. Load the file, then answer.**
# - Both files are still UPDATED every session; only the load timing changed.
#

## B. VERSION NOTES v16 → v1 (as they stood in v16)

# VERSION: v16, 16 Aug 2026 (Session 20). Supersedes v15 of 12 Aug 2026.
# NOTE: Session 20 ran on SUNDAY 16 AUG 2026. **THE INTERVAL GATE WAS APPLIED AS
# THE FIRST ACTION AND IT PASSED** — a FOUR-DAY gap since S19, the longest of
# the arc, so S20's cold work is strong later-day evidence. Third consecutive
# session where the mentor applied the gate unprompted.
# WHAT THE SESSION DID: **RECURSION WAS FINALLY DELIVERED after four deferrals,
# and it was the largest single teaching block since 1.6 closed.** Base case,
# recursive case, the pre-order/post-order distinction, value-returning
# recursion, factorial and the identity-value rule for base cases,
# `RecursionError`, the two termination conditions, and the PRINTER vs
# CALCULATOR distinction. **1.7.10 pure functions vs side effects was taught on
# top of it, which leaves only four items before 1.7 can close.**
# **THE CELL CAUSATION — ASKED FOUR TIMES IN S19 AND NEVER PRODUCED — CAME BACK
# CORRECT UNAIDED, FROM COLD, ON A GENUINELY LATER DAY.** It did not promote,
# because he rated it 5/10. **That rating is the session's most important
# finding and it points the OTHER way from every previous one: the answer was
# ~85% right and he UNDER-rated it. First recorded under-rating in the file.**
# **THE TRACEBACK FINDING IS A MENTOR FINDING AND IT IS SERIOUS.** Fired as a
# [RECALL] for the THIRD consecutive session, he rated it 0/10 — and it then
# emerged that `traceback` had never been TAUGHT properly, only repeatedly
# ASKED. Repeating a question is not teaching. **Three sessions of recorded
# "failure" on this item were measuring a teaching gap, not a retention gap.**
# It has been retaught in full (each line is ONE LIVE FRAME; a traceback is a
# printout of the stack at the moment of the crash) and RE-ENTERS THE QUEUE AS
# NEWLY-TAUGHT MATERIAL with the clock reset.
# **EDGE-CASE ANALYSIS IS NOW A TAUGHT SKILL WITH ITS OWN PROCEDURE (the five
# checks), at his direct request** — he named the gap himself: *"I am unable to
# think about the failure cases and dissect the problem the way you do... I have
# never done this, and don't know how to find the edge cases."* It transferred
# on first use, in the same session.
# **THREE NEW BINDING RULES, ALL THREE HIS: the DOUBT GATE, the RESPONSE LENGTH
# CAP, and DEPTH-BEFORE-ANSWER.** See **THE THREE SESSION 20 RULES**.
# **Running total of correct student pushbacks: TWENTY-FIVE, still zero wrong.**
# VERSION: v15, 12 Aug 2026 (Session 19). Supersedes v14 of 10 Aug 2026.
# NOTE: Session 19 ran on TUESDAY 12 AUG 2026. **THE INTERVAL GATE WAS APPLIED
# AS THE FIRST ACTION AND IT PASSED** — a two-day gap since S18, so S19's cold
# work is REAL later-day evidence and IS promotable. Second consecutive session
# where the mentor applied the gate unprompted.
# WHAT THE SESSION DID: **the three items that did not promote in S18 were
# re-fired cold, and all three improved.** `traceback` PASSED (trigger correct;
# stream a gap then correct after teach) at 6/10, up from 3/10. **The iterator
# causation PASSED ON FIRST ATTEMPT for the first time ever** — "forward-only
# state, can't rewind" — after failing on three separate prior days; delivered
# bug-first, per the standing instruction, which is now vindicated twice over.
# `__defaults__` came back NEAR-PASS at 7/10. **None promoted: every one is
# still carry-forward on his own low confidence.** A second transcription
# artefact fired on "dunder" and the rule worked — questioned, self-corrected,
# apologised, nothing logged against him.
# **CLOSURES WERE THEN TAUGHT FROM SCRATCH IN TEXT, AS HE REQUIRED IN S18** —
# free variables, cells, `__closure__`, per-object cell isolation, `nonlocal`,
# and the alias / new-object / return-value trio. `sorted` and `key=` had to be
# taught from zero mid-flow because they had never been covered.
# **THE SESSION'S DOMINANT EVENT WAS A REPEAT OF S18'S, AND HE WON IT AGAIN:
# he rejected FOUR successive motivating examples for closures, correctly every
# time**, because each one could be done with two parameters, a hardcoded value,
# or a loop and a dict. The detour cost roughly half the session and it was the
# MENTOR'S fault, not his: the genuine necessity — a callback that will only
# ever be handed ONE argument — should have been the first motivation, not the
# fifth. He reached it himself: *"ye pehla example hai jo sense bana raha hai."*
# ONE new rule. See **THE SESSION 19 RULE**.
# VERSION: v14, 10 Aug 2026 (Session 18). Supersedes v13 of the same day.
# NOTE: Session 18 ran on MONDAY 10 AUG 2026, in the evening. **THE INTERVAL
# GATE WAS APPLIED AS THE FIRST ACTION OF THE SESSION AND IT PASSED.** The
# mentor asked, before posing a single question, how long it had been since
# S17; the answer was that S17 finished LAST NIGHT and the file was saved this
# morning. That is a genuine LATER DAY, so **S18's cold work is REAL later-day
# evidence and IS promotable.** This is the first session where the S17 rule
# was applied by the mentor rather than enforced by the student, and it is the
# reason this session could finally clear the deferred block.
# WHAT THE SESSION DID: **the exception-family block — the weakest cluster in
# this file, deferred out of S17 — was finally run, and it largely PASSED.**
# The `NameError`/`ValueError`/`TypeError` triad, which had been conflated
# three separate times in S16 and was the single weakest label in the file,
# came back CLEAN AND COLD in mixed order. Exceptions-are-signals and the
# `StopIteration` CATEGORY both passed. `traceback` did not — self-rated 3/10
# and held at [~]. **The iterator-causation item FAILED FOR A THIRD TIME on
# first attempt** (he reached again for "one item at a time"), was retaught
# against the code-as-bug image, and is held at [~] on his own 3/10.
# **1.7 FUNCTIONS WAS THEN OPENED** and taken from `def`-vs-call through
# parameters/arguments, return values and implicit `None`, scope and LEGB,
# `__defaults__` (cold MISS, fourth occurrence), default arguments, and
# first-class objects. **Nested functions was taught; CLOSURES AND RECURSION
# WERE NOT TAGGED AT ALL, at the student's explicit instruction.**
# **THE SESSION'S DOMINANT INTELLECTUAL EVENT WAS A DESIGN CHALLENGE HE
# PRESSED THREE TIMES: "why does closure need to exist at all?"** He would not
# accept the factory example, then would not accept the runtime-value defence,
# then proposed a two-parameter function as a straight substitute — which is
# correct, and forced the honest answer (closures win when you must hand
# someone a ONE-ARGUMENT function with a setting already packed inside).
# **He then stopped the topic himself and asked to restart closures from
# scratch in TEXT with worked examples.** That is the scope-creep pattern
# running in REVERSE and it should be recorded as such.
# FOUR MENTOR FAILURES were logged. See **THE TWO SESSION 18 RULES**.
# VERSION: v13, 10 Aug 2026 (Session 17). Supersedes v12 of 9 Aug 2026.
# NOTE: Session 17 began LATE ON SUNDAY 9 AUG and ran into MONDAY 10 AUG 2026,
# starting only a short time after Session 16 ended. **ITS EVIDENCE IS
# THEREFORE EFFECTIVELY SAME-DAY AND NOTHING TAUGHT IN IT MAY BE PROMOTED ON
# ITS OWN EVIDENCE.** The one exception is documented in its place: the
# `if`/`elif`/`else` confirmation, which was owed from S16 and answered cold.
# **THE STUDENT ESTABLISHED THE SAME-DAY POINT HIMSELF, IN THE OPENING MINUTE.**
# The mentor began the planned exception-family [RECALL] exactly as the resume
# plan instructed, and he stopped it: S16 had only just finished, so a "cold"
# test measures short-term echo and nothing else. The mentor checked the prior
# session, confirmed he was right, apologised, and DEFERRED the entire
# exception-family block to a genuinely later day. **That is the eleventh
# correct process pushback on his record and the most sophisticated one yet —
# he did not challenge a fact or a rule, he challenged THE VALIDITY OF A
# MEASUREMENT BEFORE IT WAS TAKEN.** Note the escalation across sessions: S15
# he refused a confidence rating; S16 he surrendered a mark already awarded;
# S17 he refused an entire test on the grounds that the interval was too short.
# WHAT THE SESSION DID INSTEAD: **1.6 CONTROL FLOW IS NOW CLOSED.** The owed
# found-flag exercise was completed over four iterations, loop `else` was then
# EARNED BY CONTRAST rather than told, `pass` and ternary expressions were
# taught, the infinite-loop and full-trace work ran with the trace tail stated
# explicitly, the owed `if`/`elif`/`else` confirmation was ANSWERED AND PASSED
# (and promoted), and the mutating-vs-non-mutating IDENTIFICATION drill — the
# exact gap he named when requesting his own S16 demotion — ran at 4/5.
# THREE MENTOR FAILURES were logged. See **THE THREE SESSION 17 RULES**.
# VERSION: v12, 9 Aug 2026 (Session 16, end-of-session amendment). Supersedes
# v11 of the same day. ONE addition, no teaching content changed: the
# END-OF-SESSION PROCEDURE + DRIVE MAP section below, added at the student's
# request after the master file was again not updated until he asked for it.
# The root cause was found and it was not forgetfulness: THE TWO FILES LIVE IN
# DIFFERENT DRIVE FOLDERS, and a search scoped to the Python folder returns
# NOTHING for the master. The map is now written down so no session has to
# rediscover it. Read that section at SESSION END, every time, unprompted.
# VERSION: v11, 9 Aug 2026 (Session 16). Supersedes v10 of 8 Aug 2026.
# NOTE: Session 16 ran on SUNDAY 9 Aug 2026 — a genuine LATER DAY after the
# S14+S15 Saturday double. Its cold work is therefore REAL later-day evidence
# and this session ran the long-overdue PROMOTION PASS. NINE items moved
# [~] → [x]. The session ran the S15 term-tax cold, re-tested the S15 core,
# cleared the promotion backlog, and CLOSED most of the remaining 1.6 tail:
# `print()` formally defined (sep/end), `while` + `break`/`continue`, nested
# loops, and loop `else`. `pass`, ternary and common-loop-patterns REMAIN.
# **THE SESSION'S DOMINANT FINDING IS A MENTOR FINDING, NOT A STUDENT ONE.**
# The student raised an unprompted meta-challenge — *"you have been very
# irresponsible in teaching, how can we fix that?"* — and he was right. FIVE
# process failures were logged, THREE of which he caught in real time within
# a twenty-minute window. See **THE SESSION 16 RULES** below: they exist
# because pace was being optimised over protocol fidelity while working
# through a four-phase resume backlog. The five fixes are mechanical and
# binding, and the most important is INSTRUMENT TAGGING — every question
# must now declare whether it is RECALL, PREDICT or DRILL, because
# mislabelling new material as recall corrupts the retention ledger itself.
# ALSO LOGGED: a VOICE-MODE TRANSCRIPTION ARTIFACT was wrongly recorded as a
# label slip. The student said "iterable"; the transcription rendered it as
# "travel"; the mentor logged a retention failure and had to be corrected
# twice. That near-miss produced the TRANSCRIPTION-ARTIFACT rule.
# VERSION: v10, 8 Aug 2026 (Session 15). Supersedes v9 of the same day.
# NOTE: Session 15 ran on SATURDAY 8 Aug 2026, the SAME DAY as Session 14 —
# the student's weekend block, two sessions in one day. Its cold work is
# therefore SAME-DAY and earns [~] only; nothing from S15 may be promoted to
# [x] on S15's evidence. This session taught the ITERATION PROTOCOL
# (`iter()` once, `next()` per pass, `StopIteration` caught internally by
# `for`), the iterable-vs-iterator distinction (**iterables are reusable,
# iterators are consumed**), `range()` (half-open + lazy, and itself an
# ITERABLE not an iterator), and ran the FAIR function-scope re-test owed
# from S14 — now legitimate because `for`/`range` had been defined first.
# Two new terms were forced into definition by student pushbacks: `traceback`
# and `NameError`. FOUR mentor failures were logged, all caught by the
# student — the fourth and most serious was READING THE STALE UNVERSIONED
# MASTER FILE instead of the current v8, and then writing a replacement
# master on top of it that would have destroyed v2–v8 had it been uploaded.
# See the FILE NAMING entry for the READ-THE-LATEST-VERSION rule this
# produced. The first three: (dragging in an
# undefined `list()`; showing a traceback without defining it) plus a third
# logged unprompted (asking for a confidence rating immediately after giving
# the answer). `while` and the formal `print()` definition remain OWED and
# open Session 16.
# NOTE: Session 14 ran on SATURDAY 8 Aug 2026 — a THREE-DAY gap from Session 13
# (Wednesday 5 Aug), so its cold re-tests are strong later-day evidence. It
# CLEARED the whole S11–S13 owed backlog and OPENED 1.6 (Control Flow). It
# added the SUBSTRATE DEFINE-BEFORE-BUILDING rule.
# NOTE: Session 13 ran on WEDNESDAY 5 Aug 2026 and CLOSED subsection 1.5.

## C. STUDENT'S OBSERVED STRENGTHS (evidence log; add to it, do not rewrite)

- Strong systems thinking — naturally breaks problems into components
- Already thinks in distributed architecture from ROS2 experience
- Correctly predicted memory behavior before running code (Session 1)
- Wrote clean, well-commented code on first attempt
- Self-aware about his own learning flaws — rare and valuable trait
- Pushes back when coverage feels incomplete (S3 GIL; S10 undefined
 "aliasing"; S12 undefined "tuple" + symbols-in-voice; S14 the
 `for`/`range` substrate breach. **S15 — THREE MORE, all upheld: (a) the
 `list()`/`next()` relation was never drawn, and `list()` itself was never
 defined; (b) "how do I know you are actually completing things and not
 quietly dropping them?" — a governance challenge, answered with the live
 open-ledger of the session's to-do list; (c) "you showed StopIteration
 printed on the screen, so it IS a value" — a genuine contradiction the
 mentor had created by showing a traceback without defining it; and (d)
 after the files were delivered, "you didn't follow the rule for robotics
 curriculum naming" — and then, when the mentor's explanation didn't fit,
 he sent a SCREENSHOT OF THE FOLDER rather than accepting it. That
 screenshot exposed the real failure: the mentor had read a stale 31 Jul
 master instead of the current v8 and written a replacement on top of it,
 which would have destroyed v2–v8 had he uploaded it. NINE correct
 process pushbacks then on record, none of them wrong — and this one was
 the most valuable, because he did not stop at the mentor's first
 explanation. Note the shape for future sessions: he escalated from an
 assertion to EVIDENCE. That instinct is worth more than the catch.**
 **S17 — THREE MORE, ALL UPHELD, TAKING THE RUNNING TOTAL TO THIRTEEN WITH
 ZERO FALSE POSITIVES: (a) the same-day recall refusal, before a single
 question had been answered; (b) "I asked you to make the notes for closing
 the session not starting a new topic"; (c) the whitespace-channel
 explanation, which ended three turns of misdirected correction.**)
- Self-corrects in real time when an error is precisely named
- Names knowledge gaps precisely under pressure rather than freezing
- Predict-then-verify discipline locked in (Session 3, 4-for-4)
- **TRANSFERS A LEARNED RULE TO A NEW CONSTRUCT UNPROMPTED (NEW, S15).**
 Having just learned that a 4-item list costs FIVE `next()` calls (N+1, the
 last one raising), he applied N+1 to `range(4)` without being prompted and
 without being told the rule generalises. This is the OPPOSITE of the
 wrong-domain flaw: correct transfer across a real domain boundary,
 self-initiated. Log it as evidence the flaw is directional, not universal
 — he over-transfers under uncertainty and transfers correctly under
 understanding. Feed him more transfer opportunities.
- **REFUSES A MEASUREMENT HE KNOWS IS INVALID (NEW, S15).** See the Session
 15 rule above. He declined to give a confidence score on material he had
 not yet retrieved himself, on the grounds that it would echo the mentor
 rather than measure him. Calibration behaviour of exactly the kind the
 file has been trying to build since S6.
- **REFUSES AN ENTIRE TEST WHOSE INTERVAL IS INVALID (NEW, S17) — THE
 STRONGEST INSTANCE OF THIS BEHAVIOUR SO FAR.** S15 he refused a rating;
 S16 he handed back a mark already awarded; **S17 he refused the test
 itself, before it ran, on the grounds that the gap since the material was
 taught was too short for the result to mean anything.** He had to argue it
 — the mentor was following the written resume plan — and he was right. It
 produced the INTERVAL GATE. **This is no longer calibration; it is
 experimental design. He is now reasoning about what his own results would
 be evidence OF.**
- **CALIBRATION IS NOW ACCURATE ENOUGH TO USE AS A TARGETING SIGNAL (NEW,
 S17).** On the five-item method drill he attached a confidence to each
 answer unprompted. The single item he rated 5/10 was the single item he got
 wrong; the 8/10s and the 10/10 were all correct. **Use his self-ratings to
 choose what to re-test, not merely to decide whether a promotion is legal.**
- **Owns the learning system itself** (S5 Teaching Mistakes; S6 notes format;
 S8 two-mode operation; S9 language precision; S10 short-form cross-check;
 S12 the Term Retention System; S15 the confidence-after-recall rule;
 **S17 the interval gate and the whitespace-channel rule**)
- **STAYS ON THE FRICTION POINT** (S6 frames; S9; S10; S12; S15 — three
 separate doubts on the same block and he pushed each to a real resolution
 rather than nodding through)
- **ASKS THE HARD META-QUESTION RATHER THAN ACCEPTING A ROSTER (NEW, S17).**
 Given the list of mutating methods he did not accept it: *"mujhe jab pata
 hi nahi hai to main kaise pehchanoonga ki kaun sa mutate karne wala method
 hai? Mujhe yeh kaise pata chalega?"* That is the right question and it
 forced the right answer — the type-first discriminator rather than
 memorisation. **He reliably refuses to accept a lookup table where a model
 is possible. Teach to that.**
- **REFUSES A MARK ON MATERIAL HE DOES NOT YET OWN, AND SETS THE RE-ENTRY
 TERMS HIMSELF (NEW, S18) — the fourth and most deliberate instance of this
 behaviour.** S15 he refused a rating; S16 he handed back a mark; S17 he
 refused a test on interval grounds; **S18 he refused a TAG — "isko taught
 tag mat karo, isko hum wapas se start karenge" — and specified the
 conditions under which the topic should reopen (text mode, worked
 examples).** He is no longer only rejecting bad measurements; he is
 specifying what a good one would require.
- **FINDS THE HOLE IN A MODEL HE HAS JUST BEEN HANDED (NEW, S18, and this is
 the highest-value behaviour in the session).** Given the discriminator
 "methods on mutable types mutate and return `None`", he did not take it:
 *"yeh ek general rule to nahi maanunga."* **He was right.** `pop`, `index`
 and `count` all sit on a mutable type and all return values; the rule is
 about IN-PLACE MUTATORS, not about mutable types. The mentor's formulation
 was too broad and he narrowed it. **He accepted a model in S17 and audited
 it in S18 — that is the difference between being taught and understanding,
 and it is exactly what the course is for.**
- **PRESSES A DESIGN QUESTION TO THE THIRD LEVEL (NEW, S18).** On closures he
 asked "why does this exist?", rejected the factory answer, rejected the
 runtime-value answer, and then produced the correct rival design himself —
 a two-parameter function. **Each objection was better than the last.** The
 honest answer he forced out (closures earn their keep when a one-argument
 callable is required, or when a setting is fixed once and reused often) is
 now recorded in 1.7 and must not be softened when the topic reopens.
 **Feed him "why does this exist rather than the obvious alternative?" as a
 standing question; it is where he does his best work.**
- Diagnoses mentor delivery failures precisely, not vaguely
- Self-rating calibration now tracks reality
- **ASKS FOR THE HONEST SCHEDULE POSITION RATHER THAN AVOIDING IT (NEW,
 S15).** He stopped the session to ask where he stands against the original
 plan and how far behind he is. He then accepted the un-cushioned answer
 (danger line, zero margin) and made a correct process call himself: don't
 judge on one day's data, recompute at the month end, because session yield
 is genuinely uneven. That is the RE-BASELINE LADDER working as designed —
 and it was the student who invoked its logic, not the mentor.


## D. PROGRESS TRACKER
- Sessions Completed: **35**
- **SESSION 35 (Sun 30 Aug 2026 — ⚠ DATE DISPUTED, see below; ~4h) — 1.9 OPENED
 AND HALF-TAUGHT; ONE LEDGER PROMOTION; ONE CURRICULUM TICK (1.8 `set` CLOSED);
 `drills/s35_faults.py` 29/29 GREEN ON THE FIRST RUN.** The strongest
 first-sitting drill result in the file, on material he had never written a line
 of ninety minutes earlier. ⚠⚠ **THE HEADLINE STUDENT FINDING IS A TRANSFER GAP,
 NOT A KNOWLEDGE GAP: he predicted the bare-`except:` disaster correctly, called
 the silent `total: 0` more dangerous than the crash in his own words, and then
 wrote `except: pass` in his own `total_valid` forty minutes later.**
 ⚠⚠ **THE FOUR-STATION HOOK WAS RETIRED** — the second artefact failure on the
 same material — and replaced by a QUESTION rather than a list: **"HOW FAR DID
 PYTHON GET?"**, which worked on first use. ⚠⚠ **HE DERIVED THE COMPILE/RUN
 SPLIT UNPROMPTED off a single traceback.** ⚠ **THE RE-TEST QUEUE BECAME A
 SCRIPT** — his ruling, and the first structural fix to the retention system
 since the four-file split: `tools/retest.py` + `tools/queue.json`, 121 rows.
 **THREE pushbacks, all upheld in whole or part, 60/59** — including the first
 time he has invoked the eligibility rule himself and REFUSED to answer a
 question built on undefined substrate. ⚠⚠ **THE HEADLINE MENTOR FAILURE:
 THE INTERVAL GATE MAY HAVE BEEN RULED ON THE WRONG DATE** — "same sitting" was
 declared from the model's context header and his *"today is saturday"*, while
 every file mtime says Sunday 30 Aug. **No promotion is corrupted (everything
 promoted was S27 material, seven days cold) but an entire session of S34
 material was deferred for nothing. VERIFY THE DATE FROM `git log` AND MTIMES.**
- **SESSION 34 (Sat 29 Aug 2026, ~16:00–18:30, ~2½h) — A SHORT SAME-SITTING
 SESSION, DECLARED AS SUCH AT THE OPEN. ONE CURRICULUM TICK (1.8 tuple) AND TWO
 LEDGER PROMOTIONS.** `drills/s34_tail.py` 36/36 green across list, tuple, dict
 and set in one file. ⚠ **THE INTERVAL GATE DID REAL WORK FOR THE SECOND TIME
 IN THE FILE'S HISTORY: everything S33 taught was deferred unprompted, and only
 S24–S27 material was tested** — which is why 1.8 could not close and was said
 so at the OPEN rather than discovered at the close (the direct correction of
 the S33 over-claim). ⚠ **THE HEADLINE FINDING IS A GATE DEGRADING: the five
 checks were REPORTED BUT NOT RUN** — a fluent report on two functions that both
 failed, one on the worked example in its own docstring. ⚠ **THE HEADLINE MENTOR
 FAILURE IS THE WORST SHAPE IN THE FILE: a gate made impossible to discharge** —
 the checks were demanded via pytest, which STATE has said for two sessions he
 never runs. **Two pushbacks, both his, 57/56.** ⚠ **`reversed()` broke in the
 OPPOSITE direction to S33, one day later** — the file's cleanest name-collision
 evidence. ⚠ **The mutating tell was SPLIT: TYPE and MUTATES intact, only the
 returns-`None` half gone.**
- **SESSION 33 (Fri 28 Aug 2026 16:00 → Sat 29 Aug ~12:00, with a sleep break) —
 SEVEN LEDGER PROMOTIONS, ONE DEMOTION, THREE CURRICULUM TICKS.** The longest
 session in the file, requested by him as such (*"one of the longer ones where
 we need to focus on covering more content, approximately 6-8 hour window,
 so mix learning with revision"*). `drills/s33_copies.py` finished 25/25 cold
 the following morning, **and the five checks were reported BEFORE the word
 "done" for the first time since S25** — the fix was structural, not social:
 they were declared the GATE rather than asked for as a postscript.
 ⚠ **THE HEADLINE IS A FINDING ABOUT HOW HE LEARNS: THE `None`-IS-NOT-NOTHING
 GAP, OPENED IN S32 AS A KNOWLEDGE-STRUCTURE HOLE, CLOSED OVERNIGHT WITHOUT
 BEING DRILLED.** Named precisely at the end of S32; sixteen hours later he
 produced `[150, None]`, `len([]) == 0` / `len([None]) == 1`, and an unaided
 correction of his own `.pop` model. **Structural gaps appear to close on
 naming; LABEL gaps need repetition. Two failure modes, two treatments.**
 ⚠ **THE SHARPEST MISS IS A NAME COLLISION: `reversed()` vs `.reverse()`.**
 Taught with full output at midnight; nine hours later he did not reach for it
 in the drill, writing `[steps[-(i+1)] for i in range(len(steps))]` and
 explaining *"couldn't use reverse because it mutates the list itself"*.
 ⚠ **AND THE FILE'S MOST BROKEN ROW IS NOW THE MUTATING TELL, DEMOTED [x] →
 [~]** after three failures in two sessions, each in a different direction.
 ⚠ **MENTOR: define-before-use TENTH occurrence** (`*` on a sequence, fired in
 a [PREDICT], never taught — pushback 55, upheld in full after a grep);
 **FRAME FIRST breached** on when-to-use-which, which he stopped twice with
 *"I don't understand the question"*; and **an over-claim — "that closes 1.8"
 — said in session and false**, caught at close and corrected to his face.
 **1.8 is at ~98%: nested structures, copy semantics and patterns-and-pitfalls
 ticked; `list`, `tuple`, `dict`, `set` and when-to-use-which still [~], all
 five cold-ask shaped rather than teaching shaped.**
- **SESSION 32 (Thu 27 Aug 2026, evening → 00:15 Fri 28) — FOUR LEDGER
 PROMOTIONS, all cold and later-day, and 1.8 NESTED DATA STRUCTURES OPENED.**
 `drills/s31_shrug.py` finished 17/17 with all six tools chosen cold and not one
 `if`/`in`/`else`/`try` — the raise-vs-shrug row, which has been the file's
 longest-standing concept-owned/tool-missing split, closed on both halves.
 ⚠ **THE SESSION OPENED WITH HIS OWN SELF-DIAGNOSIS — *"I feel like I have
 started forgetting things, but we can't just waste time revising"* — and the
 answer that worked is worth reusing: THE FORGETTING IS REAL BUT IT IS LABELS,
 NOT MACHINERY.** ⚠ **THE FINDING OF THE SESSION IS NEW AND IT IS NOT A LABEL
 GAP: `None` IS NOT NOTHING**, conflated twice in one night on unrelated
 mechanisms. ⚠ **THE MENTOR FAILURE: DEFINE-BEFORE-USE, NINTH OCCURRENCE** —
 `<`/`>` fired inside a ledger-eligible [RECALL] having never been taught, in a
 snippet that announced its own answer; he caught it, and the row was held
 rather than promoted.
- **SESSION 31 (Tue 25 Aug 2026, evening, ~1h) — BUILD BLOCK 01 CLOSED FOR
 REAL. ONE CURRICULUM TICK (1.8 f-strings/format spec) AND FOUR LEDGER
 PROMOTIONS, all cold, all later-day.** The refactor he deferred at the S30
 close was done in about fifteen minutes once the spec was written properly:
 four copies of the clamp rule collapsed to one, `report` made to return what
 it had always only printed, 4 failing tests to **19/19**. ⚠ **THE SESSION'S
 LESSON IS AGAINST THE MENTOR, AND IT REPEATS S29 ONE DAY AFTER THE RULE
 WRITTEN TO PREVENT IT: SPEC BEFORE PUZZLE IS NOT DISCHARGED BY SAYING THE
 SPEC OUT LOUD.** It was issued in chat, then in an abstract brief file, and
 he rejected both — *"I can't understand what i need to do, make it clear."*
 The version that worked gave every acceptance condition a mechanical check
 he could run himself. ⚠ **THE BEST STUDENT MOMENT IN SEVERAL SESSIONS: an
 unprompted label self-repair on format-spec alignment, with no evidence
 shown and no re-ask** — the exact failure mode this file has tracked for
 fifteen sessions, corrected by him in flight. `drills/s31_shrug.py` (the
 raise-vs-shrug drill, `if`/`in`/`else`/`try` banned by a test) is written,
 issued and untouched — it is the first thing in S32.
- **SESSION 30 (Mon 24 Aug 2026, after office) — THE RECOVERY SESSION. TWO
 CURRICULUM TICKS (list + dict comprehensions → [x]) AND EIGHT LEDGER
 PROMOTIONS, all cold, all later-day, all task-first.** Two mentor-written
 drill files run and passed cold: `drills/s30_comprehensions.py` 16/16 and
 `drills/s30_containers.py` 19/19. **SPEC BEFORE PUZZLE adopted at the open in
 one word — RULES v5.** ⚠ **The three-session-deep container backlog was
 finally RUN rather than re-declared, and the thing that made it run was the
 newly adopted rule: exact signatures and exact expected values.** ⚠ **The
 session's most useful finding is a gap, not a win: given "absence is EXPECTED"
 he produced correct shrugging behaviour TWICE by hand-rolling
 `x if k in d else default`, and could recall neither `.get(k, default)` nor
 `.pop(k, default)` — the design rule owned, the two API names gone.**
- **SESSION 29 (Sun 23 Aug 2026) — THE COLD BUILD BLOCK FINALLY RAN, AND HE
 PASSED IT: 13/13 pytest, cold, unaided, all three levels plus the stretch.
 ONE PROMOTION (`zip` → [x]). ZERO CURRICULUM ITEMS TAUGHT.** ⚠ **The zero is
 a MENTOR cost: the build-block spec was written FOUR times before it was
 usable, consuming roughly half the session and three escalating pushbacks
 (all upheld) before he could write a line.** **THE RESULT THAT MATTERS: he
 reached for `zip` HIMSELF to close the design hole the block was built
 around — the day after learning it, with the mentor under standing
 instruction not to mention it. First time in this file that a
 previous-session construct was DEPLOYED against a novel problem rather than
 recited.** He also caught that the spec demanded pytest tests he has never
 been taught to write — the ninth define-before-building breach, caught
 before it cost anything. Boundary handled correctly for the first time in
 four attempts. 1.8 unmoved at ~90%. **Running pushback total 48/47.**
- **SESSION 28 (Sat 22 Aug 2026, EVENING) — FOUR CURRICULUM ITEMS TAUGHT AND
 THE S19 DEBT DISCHARGED; ZERO PROMOTIONS, BY HIS OWN CHOICE.** Same-day as S27
 and declared as such at the open, so the whole session ran as CONTENT with the
 recall block correctly skipped. Comprehensions (list and dict), `zip` and
 f-strings all taught in full — **the second and last construct flagged
 "seen-but-not-taught" back in S19 is now discharged, and HE caught the first
 one himself before being told.** 1.8 moved ~70% → ~90%. **He was offered a
 drill and REFUSED IT so it would count tomorrow** — the single strongest data
 point in the session. **SIX pushbacks, the most in any session, all upheld or
 part-upheld (running total 45/44)** — and all six landed on the same mentor
 defect: teaching mechanics without stating the point. That produced **RULES
 v4: FRAME FIRST**, the second consecutive student-proposed rule and the first
 he ordered written mid-session. **A factual over-claim was made and
 self-corrected in the same turn** (comprehensions as hidden functions — true
 to 3.11, not to his 3.12). **The S27 error-naming rule fired five times and
 hit five times — the first session in which the LABEL half did not fail once.**

- **SESSION 27 (Sat 22 Aug 2026) — THE WEAKEST CLUSTER IN THE FILE CLEARED, AND
 1.8 ADVANCED FROM ~40% TO ~70%. EIGHT PROMOTIONS PLUS A DRILL FILE.** Later-day
 gap after S26, so the whole cold block was legitimate and it paid: `break`,
 `continue`, `pass`, loop `else`, ternary, associativity (**re-promoted after the
 S25 demotion, asked ALONE**), precedence (**tested separately for the first
 time**), `traceback` and keyword argument all promoted on cold unaided evidence.
 **`drills/s27_flow.py` — five constrained functions, 20/20 pytest — is the drill
 file S26 owed.** Content: dict FINISHED (`del`/`.pop()`/`.clear()`/`.update()`,
 insertion ordering), `set` taught in full, when-to-use-which taught.
 **EXPRESSION vs STATEMENT was finally closed — owed since S14 — off the back of
 his own ternary answer.** One rule adopted, and it is the first he both proposed
 and ruled on. ONE MISS: `KeyError` read as `IndexError`.
- **SESSION 26 (Fri 21 Aug 2026) — 1.8 MOVED AT LAST: TUPLE TAUGHT IN FULL,
 DICT TWO-THIRDS TAUGHT. ZERO PROMOTIONS, AND THAT IS CORRECT.** SAME-DAY as
 S25, so nothing was promotable and the four hook tests were deferred rather
 than run — the interval gate applied unprompted for the ninth session running.
 **He asked at the S25 close for content and no recall; honoured exactly.**
 The yield is real curriculum movement after two sessions where the recall queue
 consumed the teaching slot: the comma-not-parentheses trap, unpacking, the
 one-object return, shallow immutability, shallow copy (discharging the S24
 park), dict motivation from parallel-lists, hashability, `.get()` vs `[]`, and
 `.items()`. **He DERIVED the tuple method roster from the type unaided and
 REASONED OUT hashability from first principles**, both without being told.
 ⚠ **NO DRILL FILE WAS WRITTEN — the session ran on live code and prediction
 only, so none of it can promote until drilled.** **THE SESSION'S REAL FINDING
 IS A MENTOR ONE, and it is the third consecutive spec-writing failure: FOUR
 defective asks in one session, including `KeyError` demanded by name having
 never appeared once in the entire course.** He then raised the structural
 version — *"you are asking things without teaching, is it my fault or yours?"*
 — which was audited and mostly upheld. **Two standing fixes adopted: teach with
 code and output BEFORE asking, and every [PREDICT] declares whether it is
 derivable or a genuine guess.** Second finding: a delivered error TABLE failed
 within twenty minutes and was rebuilt as the FOUR-STATION HOOK — the S25 hook
 result reproduced from the other side.
- **SESSION 25 (Fri 21 Aug 2026) — THE RECALL BLOCK CLEARED; ELEVEN PROMOTIONS,
 ONE DEMOTION, AND THE HOOK TECHNIQUE CONFIRMED.** One-day gap; interval gate
 applied, eighth session running. **He had asked at the S24 close for recall
 first, and the whole session was spent on it — the largest promotion count in
 the file's history.** Closures fell at last: the definition came back cold with
 BOTH previously-missing parts, and `drills/s25_closure.py` was built 10/10
 unaided with zero debug cycles. The entire iteration protocol returned
 (`iter()`, `next()`, `StopIteration`), unblocking comprehensions. **The one
 demotion matters more than the eleven promotions: ASSOCIATIVITY, [x] since S16,
 came back a flat "gap" when finally asked ALONE — it had been ticked bundled
 with precedence and never tested separately.** Four flat-gap items were given
 HOOKS rather than another explanation, on the strength of the five-checks
 mnemonic going 4/5 → 5/5. **Three pushbacks raised, all upheld or part-upheld,
 taking the record to 34/33.**
- **SESSION 24 (Thu 20 Aug 2026) — 1.8 OPENED; INDEXING AND SLICING DEFINED AT
 LAST; THE S17 DISCRIMINATOR CORRECTED; AND THE MNEMONIC WORKED.** One-day gap;
 interval gate applied, seventh session running. He chose material over the
 recall queue at the open, so the queue is carried forward INTACT and he asked
 for it first next time. **Indexing had NEVER been formally taught** — found by
 checking the curriculum rather than assuming, after two sessions of using
 `__closure__[0]`. **Slicing taught in full, discharging pushback 25 from S20.**
 The list method roster was exercised cold and produced the session's real
 yield: **the S17 tell is ONE-DIRECTIONAL** — returns `None` ⇒ mutating, but
 mutating ⇏ returns `None`, with `pop` as the counterexample. He had been
 reading it as a biconditional. `drills/s24_lists.py` reached **11/11** with a
 single guided fix. **THE FIVE-CHECKS MNEMONIC BUILT IN S23 SURVIVED THREE DAYS
 AND RETURNED 4/5 COLD**, after a flat gap the session before — the first hard
 evidence in this file that a hook beats a re-teach for arbitrary labels.
 **Count S24 as ~0.15 of a subsection** — low, but 1.8 is open and the two
 prerequisites it had been blocked on are now taught.
- **SESSION 23 (Wed 19 Aug 2026) — THE TERM BACKLOG CLEARED, EIGHT PROMOTIONS,
 AND A TWO-SESSION MIS-ATTRIBUTION CORRECTED.** Two-day gap; interval gate
 applied, sixth session running. The term-tax, skipped in S22 and two sessions
 overdue, was finally swept in two waves. **Promoted to [x]: truncation (with
 the toward-zero vs toward-−∞ discriminator, 10/10), floor division, alias,
 rebind, operand, iterator (the S22 label slip gone), pre-order/post-order
 (labels closed), and the MODULO IDENTITY — produced cold and UNPROMPTED to
 prove `-13 % 10 == 7` while hunting a bug in his own code, owed since S13.**
 Two task-first drills: `drills/s23_sort_key.py` (a closure forced by the
 one-argument `key=` constraint — 6/6, but through three guided debug cycles)
 and `drills/s23_ordering.py` (**lambdas + docstrings — 6/6 COLD ON THE FIRST
 ATTEMPT, unaided**), which closed **LAMBDAS to [x]**. **One demotion:
 `StopIteration` [x] → [~]** — he could not name `next()` and guessed
 "EndofIterator". **⚠ 1.8 DID NOT OPEN — the second session running where the
 recall queue consumed the teaching slot.** **Count S23 as ~0 subsections of
 new curriculum**, which is the honest number and the reason a recall-budget
 rule is now parked. **THE MAJOR FINDING IS A MENTOR FINDING, the second of
 this kind after the S20 traceback discovery: the closure definition failed
 for the second session running with the identical two defects, and the cause
 is that the four layers were taught as a STACK OF LABELS — what a cell IS
 (a type, a one-slot box, one per free variable, hence a tuple) had never
 been taught. He asked for it directly. Pushback 28, upheld.**
- **SESSION 22 (Mon 17 Aug 2026) — THE QUEUE GETS PAID: SIX PROMOTIONS, THE
 REPO'S FIRST DRILLS, AND 1.7 CLOSED.** First genuine later-day session since
 S19, and the first run of the new S21 promotion rule — it worked exactly as
 designed. **Promoted to [x] on later-day evidence: post-order transfer
 (10/10, clean four-frame trace — the S20 failure did not recur), cell
 causation (7/10, plus the same-argument tricky case), `global` (10/10, via
 task-first drill `drills/s22_counter.py`, 3/3 pytest), `*args`/`**kwargs`
 (8/10, `drills/s22_report.py`, 4/4 pytest), `__defaults__` (7/10 — PRODUCED
 COLD FOR THE FIRST TIME IN FIVE ATTEMPTS), and iterator causation (5/10,
 bug-first, first later-day pass with no one-at-a-time relapse — the short
 gap his rating buys re-fires it in S23).** The closure DEFINITION failed at
 5/10 (layers muddled, survival clause missing) and stays the priority [~].
 Taught: **lambdas and docstrings — 1.7 CLOSED.** Decisions settled: first
 weekly cold build block Sat 22/Sun 23 Aug; queue tooling = a script in the
 repo. Zero pushbacks (0 raised / 0). **Mentor miss: term-tax skipped on a
 valid later day — owed first thing in S23.** Count S22 as ~0.25 subsection
 taught, but the real yield was the ledger: biggest promotion day since S16.
- **SESSION 21 (Sun 16 Aug 2026, evening — SAME DAY AS S20) — GOVERNANCE
 SETTLED, ENVIRONMENT MOVED, AND THE 1.7 TAIL HALF-CLOSED.** Interval gate
 applied at the open: ~2 hours since S20, so **no promotable evidence, term-tax
 skipped, and the four queued [RECALL]s (post-order transfer, cell causation,
 closure definition, traceback) deferred to a genuinely later day** — the gate
 has now run unprompted four sessions running. **All SEVEN proposals from the
 16 Aug review were ACCEPTED and adopted as a package** (task-based recall;
 promotion-on-correctness with confidence setting the interval; the
 rule-change cap; the seven-principle index; the weekly cold build block;
 queue tooling; the pushback denominator). **First session run in VS Code +
 Claude Code on the new four-file git repo** — drills now happen in real
 files with pytest, which retires the chat-channel whitespace problem by
 construction. Taught: **`global`** (compile-time locality classification,
 `UnboundLocalError` mechanism, read/mutate/rebind rule) and
 **`*args`/`**kwargs`** (keyword arguments defined first after his catch;
 collect-to-tuple/dict; empty cases; the signature/call mirror). **Count S21
 as ~0.15 of a subsection** — a short evening session ended at his call.
 ZERO promotions, correctly (same-day). **One pushback, upheld: "keyword
 argument" used naked before definition — running total TWENTY-SIX, zero
 wrong. Under the new denominator rule: 1 challenge raised, 1 upheld.**
 1.7 has TWO items left: lambdas, docstrings.
- **SESSION 20 (Sun 16 Aug 2026) — RECURSION DELIVERED AT LAST, AND THE FILE'S
 OLDEST "STUDENT WEAKNESS" TURNED OUT TO BE A MENTOR GAP.** Interval gate
 passed (FOUR-day gap, the longest of the arc), applied unprompted for the
 third session running. **The cell causation — asked four times in S19 and
 never produced — came back CORRECT UNAIDED FROM COLD.** Recursion taught in
 full: base/recursive case, pre-order vs post-order, value-returning
 recursion, the identity-value rule, `RecursionError`, the two termination
 conditions, printer-vs-calculator. **1.7.10 (pure functions vs side effects)
 taught on top, and 1.7.11 (EDGE-CASE ANALYSIS) ADDED TO THE CURRICULUM at
 his request.** **Count S20 as ~0.4 of a subsection.** Yield held back by the
 traceback re-teach and by the doubt-gate stoppage, both of which were the
 right calls.
- **THE SESSION'S DOMINANT FINDING IS A MENTOR FINDING, AND IT IS THE MOST
 CONSEQUENTIAL ONE IN THE FILE SO FAR.** `traceback` has been fired as a
 [RECALL] in S16, S18 and S19 and logged as a repeated failure. **In S20 he
 rated it 0/10 and said plainly that he did not know what `<stdin>` meant —
 at which point it became clear the item had never been TAUGHT, only
 repeatedly ASKED.** Three sessions of "he keeps failing this" were measuring
 a hole in the teaching. **The clock is reset and the prior failures are
 struck from the record as invalid measurements.** ⚠ **Audit the rest of the
 carry-forward list for the same defect before the August gauntlet.**
- **ZERO PROMOTIONS AGAIN — THIRD SESSION RUNNING — AND THE REASON HAS
 CHANGED.** S19's zero was low confidence on correct answers. **S20's is a
 5/10 on an answer that was ~85% right: the file's FIRST RECORDED
 UNDER-RATING.** His calibration has been the file's most reliable instrument
 since S17 and it is used as a targeting signal; **under-rating wastes
 sessions re-teaching what he already owns, and it is as much a measurement
 error as over-rating.** Watch whether this repeats. One instance is not a
 trend, but it inverts a two-month pattern.
- **THREE NEW BINDING RULES, ALL THREE HIS, ALL THREE ABOUT BANDWIDTH.** The
 DOUBT GATE, the RESPONSE LENGTH CAP and DEPTH-BEFORE-ANSWER. **The second
 one carries information the file did not have: he does not read long
 messages to the end.** That single admission retro-explains the four missing
 S19 ratings, the skipped `digit_sum` trace and the unanswered S19
 cell-causation re-fire. **Those were not compliance failures — they were
 asks buried where he never got to them. Message length is the mentor's
 problem to fix and it is now a rule.**
- **THE HONEST COUNTERWEIGHT: the [PREDICT] on post-order recursion FAILED, and
 it failed on a principle he had explained correctly twenty minutes earlier.**
 Four frames each holding their own `n` is the same isolation he had just
 described for five objects each holding their own cell. **He owns the concept
 in one container and does not recognise it in another. That is a transfer
 failure and it should be tested as one.** Also owed and NOT done: the four
 S19 confidence ratings (asked once, lightly, per plan — still not given), the
 spoken Feynman recall for 1.6 (**now slipped THREE sessions**), and the
 `__defaults__` / iterator-causation fires.
- **SESSION 19 (Tue 12 Aug 2026) — CLOSURES TAUGHT PROPERLY, AND THE MOST
 STUBBORN ITEM IN THE FILE FINALLY CAME BACK CORRECT.** Interval gate passed
 (2-day gap), applied by the mentor unprompted for the second session running.
 **The iterator causation PASSED ON FIRST ATTEMPT after failing on three
 separate prior days** — bug-first delivery, exactly as the S18 note
 instructed. `traceback` improved 3/10 → 6/10 and `__defaults__` came back at
 7/10 having never once been produced before. **ZERO PROMOTIONS, and that is
 correct: all three self-rated below the bar and stay carry-forward.** Closures
 were then built from scratch in text — free variables, cells, `__closure__`,
 per-object isolation, `nonlocal`, the three-way alias/new-object/return-value
 distinction — plus `sorted` and `key=` taught from zero. **Count S19 as ~0.35
 of a subsection.** The yield is lower than S18's because roughly half the
 session went to a motivation detour that was the mentor's fault.
- **THE HONEST COUNTERWEIGHT, and it is a mentor counterweight this time.**
 Four successive motivating examples for closures were offered and all four
 were correctly rejected by the student. **The answer that finally worked —
 the one-argument callback constraint — WAS ALREADY WRITTEN IN THIS FILE from
 S18 and was not used until the fifth attempt.** `sorted(key=)` was also
 deployed before it had ever been taught, and he had to flag it twice.
 **Recursion was deferred a FOURTH time as a direct consequence.**
- **SESSION 18 (Mon 10 Aug 2026, evening) — THE DEFERRED BLOCK CLEARED AND
 1.7 FUNCTIONS OPENED.** The interval gate passed (S17 ended the previous
 night), so **this session produced the first genuine later-day evidence
 since S16 — and it was used.** SEVEN items promoted to [x]: the
 `NameError`/`ValueError`/`TypeError` triad, exceptions-are-signals, the
 `StopIteration` category, and the mutable/immutable discriminator. **1.7 was
 then opened and taken about two-thirds of the way through.** **Count S18 as
 ~0.5 of a subsection** — roughly 0.15 for clearing the deferred re-tests and
 0.35 for the Functions material.
- **THE HONEST COUNTERWEIGHT: three items did NOT promote, and they are the
 same three the file has been carrying for weeks.** `traceback` (3/10),
 iterator causation (3/10, third failure on a third separate day) and
 `__defaults__` (fourth cold miss, and still the only item in the file never
 once produced cold). **Closures and recursion were not covered at all** —
 closures deliberately untagged at his instruction, recursion deferred three
 times by him in favour of the closure argument.
- **THE STRUCTURAL POINT WORTH KEEPING: the weakest cluster in this file
 stopped being the weakest because the INTERVAL GATE forced it to be tested
 properly rather than early.** S17 would have promoted it on echo. S18
 promoted it on evidence. The gate cost one session and bought a true ledger.
- **SESSION 17 (late Sun 9 Aug → Mon 10 Aug 2026) — 1.6 CONTROL FLOW CLOSED.**
 The last five items of the subsection were taught (the owed found-flag
 exercise and the loop-`else` contrast, `pass`, ternary, loop patterns, and
 the owed method-identification drill), and the owed `if`/`elif`/`else`
 confirmation from S16 was answered cold and PROMOTED. **Count S17 as ~0.3
 of a subsection.** Layer 1 is now 1.1–1.6 taught, with 1.7 opening next.
- **THE STRUCTURAL CAVEAT, and it is the whole reason this session's yield
 reads lower than its content: S17 ran within hours of S16, so ITS EVIDENCE
 IS SAME-DAY.** Everything taught is [~] and stays [~]. The exception-family
 re-test, the iterator-causation re-test and the modulo-identity re-test were
 all DEFERRED OUT of this session by the student's own correct objection.
 **Two sessions in one sitting buys coverage, not consolidation — the same
 lesson the S14+S15 double taught, learned again.** The next session must be
 on a genuinely later day and must open with the deferred block.
- **SESSION 16 (Sun 9 Aug 2026) — THE PROMOTION SESSION.** NINE items moved
 [~] → [x] on genuine later-day cold evidence, including `==` vs `is` (owed
 since S7) and the negative-`%` case. Six terms also promoted. **Count S16 as
 ~0.5 of a subsection.** **THE COUNTERWEIGHT: five mentor process failures in
 one session, three caught by the student.** Yield and fidelity traded against
 each other and that trade must not be repeated.
- **DEADLINE: Layer 0 closes 30 Sep 2026.** Cadence required: ~5 sessions/week.
 Hour budget ~900h against ~870h available: zero slack.
- **THE HONEST SCHEDULE POSITION AS OF 10 AUG (end of S18):** 1.6 is closed
 and 1.7 is ~two-thirds taught, so **six and a bit subsections remain
 (the 1.7 tail plus 1.8–1.13) against ~7 weeks.** Required rate is still
 ~1 subsection/week and the margin is still ZERO. **But S18 is the best
 single-session yield in a fortnight (~0.5) and it was achieved on a WEEKDAY
 EVENING, not a weekend block** — which is the first real evidence that the
 3h weekday commitment can carry the required rate on its own.
 **The binding constraint remains per-session YIELD rather than session
 frequency, and the re-baseline arithmetic is still formally due 31 Aug.**
- **CADENCE — SESSION 15: ~0.4.** Iteration protocol, iterable/iterator,
 `range`, function-scope. Did not close 1.6.
- **SESSION 14: ~0.3.** Backlog clearance + 1.6 opened.
- **SESSION 13: ~0.4.** Closed the 1.5 tail.
- **RE-BASELINE LADDER STAYS ARMED.** The true arithmetic (observed
 throughput → derived completion date) is **formally due 31 Aug 2026** and
 gets written into the master file whether or not it is welcome. The student
 asked for this himself in S15 and chose the date; honour it on time.
- **WEEKEND BLOCKS:** Sat 1 Aug used (S10+S11). Sun 2 Aug NOT used.
 **Sat 8 Aug USED — TWO SESSIONS (S14 + S15). Sun 9 Aug USED — TWO SESSIONS
 (S16 + S17, the second running past midnight into Mon 10 Aug).** That is two
 consecutive weekend blocks fully used, which is the committed compensation
 mechanism actually showing up in the log. **But note the pattern cost: both
 doubles produced same-day evidence that cannot be promoted.** Log actual
 hours at the 31 Aug checkpoint.
- Current Layer: 1
- Current Topic: **1.7 (Functions). Recursion, pure functions and edge-case
 analysis all taught in S20. FOUR ITEMS REMAIN: `global`, `*args`/`**kwargs`,
 lambdas, docstrings. One good session closes 1.7.**
- **Last Session: Session 17 (late 9 Aug → 10 Aug 2026)** — deferred the
 exception-family recall on the student's correct objection; completed the
 owed found-flag exercise across four iterations; earned loop `else` by
 contrast; taught `pass` (with the three-way `pass`/`continue`/`break`
 distinction and the comment-is-not-a-body trap); taught the ternary as an
 EXPRESSION; took the owed `if`/`elif`/`else` confirmation cold and PROMOTED
 it; taught `elif` chain semantics properly at his request; ran the
 infinite-loop and full-trace work with the final cycle stated explicitly;
 ran the owed mutating-vs-non-mutating drill (4/5) and replaced the roster
 with the type-first discriminator; **and produced three new binding rules —
 the INTERVAL GATE, AMBIGUOUS ASSENT, and WHITESPACE-IS-NOT-TESTABLE.**
- Session Before: **Session 16 (9 Aug 2026, Sunday)** — the promotion pass;
 nine items to [x]; most of the 1.6 tail; five mentor process failures.
- Session Before That: **Session 15 (8 Aug 2026, Saturday)** — the iteration
 protocol; same-day as S14.


## E. ASSIGNMENTS LOG
| Session | Topic | Assignment | Status | Notes |
|---------|-------|------------|--------|-------|
| 0 | Onboarding | ATM logic exercise (verbal) | Complete | Strong systems thinking |
| 1 | Name binding | Predict a=10,b=a,b=b+5 | Complete | Correct, clean comments |
| 2 | Recall + rebinding | Drills 1–3 | Complete | Gaps named honestly; C++ leak self-corrected |
| 3 | Recall + 1.1 | Drills + empirical tests | Complete | Clean; PVM phrasing sharpened |
| 4 | Recall + 1.1 final | Call-stack + traceback + REPL | Complete | Mutation/rebinding misclassified |
| 5 | Recall + open 1.3 | Four demo functions | Complete | Entry-point wrong — corrected |
| 6 | Diagnostic + rebuild 1.1 | Cold recall + frames rebuilt | Complete | Root cause: "frame" never defined |
| 7 | Cold re-test + open `str` | Traceback drill + 3 re-tests | INCOMPLETE (carried) | 3 [x]→[~] |
| 8 | Governance — voice model | Nine binding rules adopted | Complete (governance) | ZERO subsections |
| 9 | Discharge predictions + `None` | P1–P4 cold + `==`/`is` | Partial | Four str predictions correct cold |
| 10 | Close 1.3 + open/close 1.4 | Conversion + drills | Complete — TWO closed | Four mechanism doubts pushed to resolution |
| 11 | Feynman backlog + finish 1.4 | Two Feynman pages + depth doctrine | Complete — 1.4 CLOSED | `int(x)` self-repair |
| 12 | Cold re-tests + OPEN 1.5 | 6-item cold block + 1.5 core + Term Retention System | Complete — 1.5 OPENED (~60%) | Student caught FIVE mentor process errors |
| 13 | Term-tax + CLOSE 1.5 tail | membership, short-circuit, bitwise, `%`/`**` drills | Complete — 1.5 covered end-to-end | Wrong-domain flaw on negative `%`, repaired |
| 14 | Clear owed backlog + OPEN 1.6 | term-tax + 5 Aug re-test batch + `id()` demo + Feynman 1.3/1.4 + `if`/truthiness | Complete — backlog cleared, 1.6 OPENED | Student self-caught the wrong-domain reflex — a first. SUBSTRATE rule added. |
| 15 | **Iteration protocol + fair function-scope re-test + schedule review** | **`iter()`/`next()`/StopIteration hand-unrolled (text) + iterable-vs-iterator with `list()` drain proof + `range()` half-open/lazy + `for i in range(3)` scope re-test + `range(0)` NameError case + mid-session plan review** | **Complete — 1.6 substantially advanced, NOT closed** | **Three correct student pushbacks, all upheld. Two new terms defined. Student REFUSED a premature confidence rating → new binding rule. Same-day as S14, so all evidence [~].** |
| 16 | **Term-tax + S15 cold re-test + THE PROMOTION PASS + most of 1.6** | **S15 label volley cold; iterables/iterators + `range(0)` + scope re-tests; nine-item promotion pass; S13 operator drills in text (6/6); `print()` formally defined; `while` + `break`/`continue`; nested loops; loop `else`** | **Complete — 1.6 nearly closed** | **NINE promotions to [x] including `==`/`is` (owed since S7). FIVE mentor process failures, three caught by the student → the five Session 16 rules. Student requested and was granted a DEMOTION. `NameError`/`ValueError` conflated three times.** |
| 17 | **CLOSE 1.6 — the owed tail** | **Found-flag search written by the student (4 iterations) → loop `else` earned by contrast; `pass` + the `pass`/`continue`/`break` three-way; ternary as an EXPRESSION; `if`/`elif`/`else` chain taught on request then CONFIRMED COLD; infinite-loop diagnosis + full `while` trace with the final cycle stated; mutating-vs-non-mutating identification drill (4/5) + the type-first discriminator** | **Complete — 1.6 CLOSED** | **THREE correct student pushbacks, all upheld, taking the running total to 13 with zero false positives — and the first one, refusing a same-day recall test before it ran, produced the INTERVAL GATE. `if`/`elif`/`else` PROMOTED to [x], the last item owed from S16. The owed method drill was delivered, discharging the debt from his own S16 demotion request. His per-item confidence PREDICTED his single wrong answer. Mentor also misread "continue" and opened 1.7 against his explicit request; that material was discarded at his instruction and is not recorded.** |
| 18 | **Clear the deferred recall block + OPEN 1.7 Functions** | **[RECALL] exception family cold in mixed order (`NameError`/`ValueError`/`TypeError`, exceptions-are-signals, `StopIteration` category, `traceback`); [RECALL] iterator causation; [RECALL] modulo identity in TEXT on a self-chosen negative divisor; [DRILL] `reverse`/`sort` + classification of unseen methods; then 1.7 — `def` vs call, parameters vs arguments, return values and implicit `None`, scope and LEGB, `__defaults__` cold re-test, default arguments, first-class objects, nested functions** | **Complete — deferred block cleared, 1.7 OPENED (~two-thirds)** | **SEVEN promotions to [x] on genuine later-day evidence, including the `NameError`/`ValueError` conflation that had been the single weakest label in the file since S16. The INTERVAL GATE was applied by the MENTOR unprompted for the first time. `traceback` (3/10), iterator causation (3/10, third failure) and `__defaults__` (fourth cold miss) all held at [~]. FIVE correct student pushbacks — running total EIGHTEEN, zero wrong — including a TECHNICAL correction to the mentor's own discriminator rule and a refusal to let closures be tagged as taught. Closures and recursion NOT covered; closures reopen from scratch in TEXT.** || 19 | **Recall the three S18 non-promotions + CLOSURES FROM SCRATCH IN TEXT** | **[RECALL] `traceback`, iterator causation (bug-first), `__defaults__`; [RECALL] def-vs-call / first-class / alias and LEGB; then closures ground-up — free variable, cell, `__closure__`, per-object cells, the one-argument-callback necessity, `sorted` and `key=` from zero, student-built `my_sorted`, `nonlocal` and the three-error separation, alias vs new object vs return value** | **Complete — 1.7 advanced to ~five-sixths; recursion deferred a fourth time** | **THE ITERATOR CAUSATION PASSED ON FIRST ATTEMPT for the first time in four attempts across four days — bug-first delivery vindicated. ZERO promotions and that is correct: 6/10, 4/10 and 7/10 all sit below the bar. Second transcription artefact of the arc fired on "dunder" and the S16 rule handled it — nothing logged against him. FOUR correct student rejections of weak closure motivations, running total TWENTY-TWO with zero wrong. Mentor failures: `sorted(key=)` used before ever being taught (flagged twice by him), four motivations that did not require a closure (~half the session), `zip` and list comprehensions used untaught, and questions consolidated without their code → THE SESSION 19 RULE. Closure DEFINITION declared a gap; cell causation asked a fourth time and still not produced unaided.** |
| 20 | **Close the owed closure recalls + RECURSION AT LAST + pure functions + edge-case analysis** | **[RECALL] closure definition cold (4/10); [RECALL] cell causation cold — CORRECT UNAIDED at last (5/10); [RECALL] `traceback` → 0/10 and retaught from scratch; then 1.7.9 RECURSION in full (base/recursive case, pre-order vs post-order, value-returning recursion, identity-value base rule, `RecursionError`, the two termination conditions, printer-vs-calculator); [PREDICT] post-order countdown (FAILED), [PREDICT] `total(4)` (PASSED both parts); [DRILL] `count_down_by` (passed, tuple flaw); [DRILL] `digit_sum` (recursive case unaided, base-case boundary bug); 1.7.11 EDGE-CASE ANALYSIS — the five checks, taught as a procedure; [DRILL] `first_char` bug hunt (PASSED via check 2); 1.7.10 pure functions vs side effects + [PREDICT] `scale` (3/3)** | **Complete — 1.7 advanced to four remaining items** | **THE CELL CAUSATION CAME BACK CORRECT UNAIDED after five attempts across two days. ZERO PROMOTIONS — but for a NEW reason: the file's FIRST UNDER-RATING (5/10 on an ~85%-correct answer). ⚠ THE MAJOR FINDING IS A MENTOR FINDING: `traceback` had been FIRED for three sessions and NEVER TAUGHT; the prior "failures" were invalid measurements and are struck. TENTH define-before-building breach (slicing used untaught) → PUSHBACK 25, upheld. Running total TWENTY-FIVE, zero wrong. THREE NEW RULES, all his — DOUBT GATE, RESPONSE LENGTH CAP, DEPTH-BEFORE-ANSWER — and the disclosure behind rule 2 (he does not read long messages to the end) retro-explains several logged student lapses. EDGE-CASE ANALYSIS added to the curriculum as 1.7.11 at his request; it transferred on first use.** |
| 22 | **Pay the deferred recall queue + close 1.7** | **[RECALL] post-order transfer (fresh `climb(3)`, frame trace demanded and delivered); [RECALL] cell causation + same-argument tricky case + the `start = start + 1` locality trap (miss → unaided repair); [RECALL] closure definition cold (FAILED 5/10, four-layer walk retaught); [RECALL] traceback line-=-frame (partial, repaired, teach-back correct); TASK-FIRST DRILLS: `s22_counter.py` (forced `global`, 3/3) and `s22_report.py` (forced collectors, 4/4); [RECALL] `__defaults__` (COLD AT LAST); [RECALL] iterator causation bug-first (later-day pass); then LAMBDAS (key=, closure transfer, two [PREDICT]s passed) and DOCSTRINGS (`__doc__`, None-absence discriminator) — 1.7 CLOSED** | **Complete — SIX promotions, 1.7 closed, first two repo drills** | **First run of the new promotion rule: correctness promotes, rating sets the gap — iterator causation promoted at 5/10 with a deliberately short re-test. Label slips ran opposite to mechanism wins all session (pre/post-order gap, "UnboundError" ×2, `cell_content`, "inner iterable") — consistent with the S12 diagnosis. Zero pushbacks raised. Mentor misses: term-tax skipped on a valid later day; lambda teaching turn ran long undeclared. Decisions: cold build block this weekend; queue tooling = script.** |
| 23 | **Clear the overdue term-tax + task-first recalls; 1.8 planned but not reached** | **TERM-TAX in two waves (~24 rows swept cold); [RECALL] iterator causation bug-first via a two-loop exhaustion program (causation held, BOTH protocol names lost); [RECALL] closure definition cold (FAILED again, 7/10, same two defects as S22) → cells finally taught as a TYPE with `type()` output and a two-free-variable example; TASK-FIRST DRILLS: `s23_sort_key.py` (closure forced by the one-argument `key=` constraint, 6/6 after three guided debug cycles — missing argument, call-vs-object, missing `abs()`) and `s23_ordering.py` (lambdas + docstrings under a no-third-`def` constraint, **6/6 cold first attempt**); the FIVE CHECKS re-taught after a flat gap and a mnemonic built with him; [RECALL] docstring placement mechanism (MISS — second-line literal predicted to survive)** | **Complete — EIGHT promotions, one demotion, lambdas closed; ⚠ 1.8 NOT OPENED** | **THE TERM BACKLOG IS CLEARED. Eight promotions including the modulo identity, produced cold and unprompted to find a real negative-modulo bug in his own lambda — the strongest single moment of the session and an item owed since S13. `UnboundLocalError` typed correctly, spelling fixed. THREE pushbacks, all sound (syntax-lookup legitimacy; "unit testing was never taught" — partially upheld; **"why didn't you tell me all this when you used `cell` the first time" — UPHELD and it corrected a two-session mis-attribution**), running total TWENTY-EIGHT, zero wrong. TWO NEW WATCH AREAS: **confidence calibration ran HOT for the first time** (three over-ratings, including 7/10 on a repeat failure), and **depth-before-answer fired hard** — the five-checks report was asked four times and skipped each time, and he declared a drill "works" without running it. Mentor misses: cells taught as labels in S22; the call-vs-object question ground through two failed Socratic attempts before going direct.** |
| 24 | **OPEN 1.8 — lists, and the two prerequisites it was blocked on** | **Governance: weekend cold build block CONFIRMED for Sat 22 Aug; the parked [RECALL]-budget rule offered twice and declined twice in favour of material. INDEXING defined for the first time (0-based, `len-1` as the last index, negative indices, `IndexError`) after a check showed it had never been taught. SLICING in full — `[start:stop:step]`, half-open like `range()`, omitted ends, negative step, `l[:]` as the copy idiom, slices build a NEW list, out-of-range slices return `[]` and never raise, the same operator on `str` — discharging pushback 25 from S20. [TEACH-BACK] slice-vs-alias (correct, and he separated mutation from rebinding unprompted). [PREDICT] the six-method roster volley (`append` `extend` `insert` `sort` `remove` `pop`) — 3/6, then the ONE-DIRECTIONAL correction to the S17 tell. [RECALL] the five checks cold via the S23 mnemonic — 4/5, `mila` missing, re-taught in English and Hindi. TASK-FIRST DRILL `drills/s24_lists.py` — four functions under observable-behaviour-only contracts, 11/11 pytest after one guided fix** | **Complete — 1.8 OPENED, ~15%** | **NO PROMOTIONS, correctly — everything taught was same-session; the two later-day items that DID hold (aliasing, rebinding-vs-mutation) were already [x] and simply re-passed. THE SESSION'S FINDING IS THE MNEMONIC: 4/5 cold after a flat gap three days earlier. THREE pushbacks (running total 31): the `last_three` spec is ambiguous — UPHELD, mentor error, I had written "oldest" and imported a time ordering that was never in the spec; "isn't the corrected code a proof of my understanding?" — **NOT UPHELD, the first non-upheld challenge in the file's history**, answered with reasoning rather than authority and accepted; "shouldn't I just write the relevant cases?" on the five checks — PARTIALLY UPHELD, resolved as SCAN all five / REPORT what bites. Mentor misses: the roster volley was tagged [PREDICT] but `sort` had been taught in S17, so a genuine recall miss went unledgered — declared to him in session rather than back-dated; and the `last_three` docstring was ambiguous. Depth-before-answer fired twice and BOTH re-asks produced the correct mechanism in one line.** |
| 21 | **Adopt the seven review proposals + move to VS Code/Claude Code + open the 1.7 tail** | **Governance: all seven 16-Aug proposals ACCEPTED (RULES v2). Tooling: repo/drills/pytest workflow established. Taught `global` (compile-time locality, `UnboundLocalError`, read/mutate/rebind rule) with [PREDICT]s on the read-only and mutation cases (both correct); taught `*args`/`**kwargs` (keyword args defined after his catch, collectors, empty cases, signature order, the collect/unpack mirror) with [PREDICT]s and [TEACH-BACK]s throughout** | **Complete — 1.7 down to TWO items (lambdas, docstrings)** | **Same-day session (~2h after S20): interval gate applied unprompted, term-tax skipped, the four queued [RECALL]s deferred — zero promotions, correctly. ONE pushback, upheld ("keyword argument" used before definition — 11th define-before-use breach; running total 26, zero wrong; denominator: 1 raised / 1 upheld). Session ended at his call before lambdas/docstrings.** |
| 25 | Recall block — closures, iteration, docstrings, five checks | `drills/s25_closure.py` (10/10) + `drills/s25_iteration.py` (7/7) | Complete | ELEVEN promotions, one demotion (associativity); 3 pushbacks, all upheld |
| 26 | 1.8 — tuple in full, dict two-thirds | **NONE — no drill file written** | ⚠ **MISSING** | Same-day as S25, so zero promotions and the four hook tests correctly deferred. Ran on live code + [PREDICT] only. **4 pushbacks, all upheld/part-upheld (running total 38/37) — third consecutive spec-writing failure, incl. `KeyError` demanded having never appeared in the course.** Error TABLE failed in 20 min → rebuilt as the FOUR-STATION HOOK. Two standing fixes adopted: teach-before-ask, and every [PREDICT] declares its kind. **S27 must produce `drills/s27_*.py`.** |
| 27 | **Clear the S25 hook backlog task-first + FINISH DICT + SET + when-to-use-which** | **TASK-FIRST [RECALL]: `drills/s27_flow.py` — five functions under lettered CONSTRAINTS forcing `break` (one-return-last-line), `continue` (if-has-no-else), loop `else` (print only on natural end, no `if` after the loop), ternary (single-line return), `pass` (one-line body, not a return/string/assignment); 20/20 pytest, then a guided rewrite of `find_index` from items to positions; naming half of each mechanism taken after the code ran; [DRILL] `2 ** 3 ** 2` then `2 + 3 * 4 ** 2` for associativity and precedence SEPARATELY; [RECALL] traceback frames off a live `KeyError`; [RECALL] keyword argument; four-station error hook fired cold on three dict snippets; EXPRESSION vs STATEMENT closed; then dict deletion + ordering, `set` in full (uniqueness, `set()` vs `{}`, add/discard/remove, not-subscriptable, order instability across three runs, `|`/`&`/`-`), and when-to-use-which with the 30-second joint-log exercise** | **Complete — EIGHT promotions, 1.8 to ~70%; comprehensions declared open and NOT walked through** | **THE `while`/loop-`else`/`pass`/ternary CLUSTER — WEAKEST IN THE FILE SINCE S23 — CLEARED IN ONE DRILL, AND THE S25 HOOKS ARE WHY. Associativity RE-PROMOTED after its S25 demotion, asked alone; precedence tested separately; the `while` bullet DELIBERATELY LEFT [~] because `while` mechanics were untested — the first time this file has refused a bundle. His `find_index` rewrite killed a latent bug he never saw (`None` serving as both sentinel and value) — a five-checks `bahar`-by-TYPE miss. RULE ADOPTED (his own, proposed and ruled on by him): name the error before the mentor shows it; it paid for itself on first use by exposing STATION 0 of the four-station hook (`SyntaxError` = did it run at all?). Hook result mixed and therefore useful: `AttributeError` hit, `KeyError`→`IndexError` MISS, `NameError` honest gap. Confidence calibration accurate across eight ratings. Depth-before-answer fired three times, all three recovered on re-ask (ten straight). NEW WATCH AREA: DESIGN-SWITCHING — asked three times what the outer container must DO, he twice proposed a different design instead of answering, then got it instantly on the direct re-ask. Mentor: ONE defective ask (down from four), upheld; two self-caught mis-tags corrected in opposite directions. Build block moved to Sun 23 Aug — second date it has carried.** |
| 28 | **OPEN AND TEACH COMPREHENSIONS + the 1.8 tail: `zip` and f-strings** | **NONE — drill DEFERRED TO S29 AT THE STUDENT'S OWN REQUEST so it would be ledger-eligible.** Taught: LIST COMPREHENSIONS (the form; expression-vs-statement as the reason the construct exists — **derived by him from his own `print(...)` test**; the `if` filter as a GATE; the formal anatomy with written-order ≠ execution-order 4→2→3→1, **PROVED with a live `ZeroDivisionError` rather than asserted**; the comprehension's own namespace via `NameError`, explicitly right-sized as a footnote; and WHEN NOT TO USE ONE via `[print(j) for j in joints]` → `[None, None, None]`). DICT COMPREHENSIONS (braces + colon; `.items()` + two-name unpacking; filtering on the value). `zip` (pairing; yields TUPLES; **the motivation taken from his own S27 `range(len(...))` code**; **and the headline — it FAILS SILENTLY TWICE, truncating to the shortest and returning `[]` when exhausted because `list()` catches the `StopIteration`**). F-STRINGS (the three steps evaluate→`str()`→splice; braces hold an EXPRESSION not a name — **he reasoned out the `for`-loop exclusion himself**; the format spec `.2f`/`8.2f`/`03d`/`10s`, total width, and text-left/numbers-right alignment). [DRILL] `{name: angle for name, angle in zip(names, angles)}` written cold, one guided fix (missing braces). | **Complete — 1.8 to ~90%; ⚠ NO DRILL FILE, deliberately** | **ZERO PROMOTIONS and that is correct — same-day throughout. ⚠ THE HEADLINE IS HIS: offered a drill, he refused it to protect ledger eligibility (*"atleast it goes to the ledger then"*) — the jump-ahead pattern running backwards for the second time in one session, after he also stopped the mentor mislabelling comprehensions as "1.9". SIX pushbacks, ALL upheld/part-upheld (running total 45/44), the most in any session and all on ONE mentor defect → **RULES v4: FRAME FIRST**, ordered written mid-session. MENTOR ERRORS: four — no frame before mechanics (he stopped the session); a scope example built on `pass` so the branches did not do equal work (demolished, correctly); four turns spent on a footnote before he asked why it mattered; and a FACTUAL OVER-CLAIM (comprehension = hidden function; true ≤3.11, wrong on his 3.12/PEP 709) self-caught and corrected in the same turn, with the `<genexpr>` proof deliberately withheld because generator expressions are untaught. STUDENT: five-for-five on cold error labels under the S27 rule — the label half's first clean session; sideways-answering repeated TWICE (output instead of the four parts; format codes instead of the two output lines), both fixed by re-issuing the question unchanged — twelve straight re-ask recoveries; THIRD boundary bug (`len(n) > 5` with two 5-letter words), then boundary-first applied UNPROMPTED one rep later. NEW WATCH AREA: LEVEL-1 CONSTRUCTS HE USES WITHOUT A MODEL — f-strings hid for 27 sessions precisely because he types them correctly.** |
| 29 | **COLD BUILD BLOCK 01 — the measurement instrument, not a curriculum item** | **`builds/block_01_joint_clamp/clamp.py` — written cold, no AI, no autocomplete, against a mentor-written 13-test acceptance suite. L1 `clamp_one(angle, low, high)`; L2 `clamp_all(low, high, *angles)` → tuple; L3 `clamp_joints(*angles, **limits)` → dict, THE DESIGN HOLE (anonymous positional angles vs named limits); L4 the extra-angle case; L5 `report()` with an aligned f-string table. Then a code read: the dead `{}` return in `report()`, and the clamp rule duplicated four times** | **Complete — 13/13, ONE promotion (`zip`)** | ⚠ **HALF THE SESSION WENT ON MENTOR SPEC CHURN — four versions, three upheld pushbacks (46 abstract spec, 47 *"lets call this off"*, 48 **pytest was never taught**), running total 48/47. The timer was abandoned in frustration and `LOG.md` never written, so block 01 has NO duration and NO process record — code only. THE STUDENT RESULT IS EXCELLENT AND SEPARATE FROM THAT: `zip` found unprompted to pair `*args` with `**kwargs`, plus dict insertion order VOLUNTEERED with the set contrast; `*args`, `**kwargs`, `*args`-after-positional and `*tuple` call-site unpacking all cold and correct; f-string format specs `{k:10s}`/`{v:8.1f}` aligning first run; and the planted boundary handled right — the first clean boundary in four. Third mechanism fact (`for k in d` yields KEYS) only on the re-ask. Depth-before-answer fired twice, both recovered — fourteen and fifteen straight. NO teaching, NO drill, NO rule adopted; SPEC BEFORE PUZZLE parked for his ruling. Comprehensions drill now deferred TWICE and it is the file's fault, not his.** |
| 30 | **Comprehensions drill (deferred twice) + the container backlog (declared four times)** | **`drills/s30_comprehensions.py` — `over_limit` (list comp + filter), `scaled` (dict comp), `names_over` (dict comp over `.items()`), `format_row` (f-string + format spec); one `return` per body, 16 mentor-written tests. Then `drills/s30_containers.py` — `limits_for`, `shared_joints`, `pop_limit`, `snapshot`, `span`, `total`; 19 mentor-written tests. Then `builds/block_01_joint_clamp/test_report.py` written by the mentor to expose the dead `{}`, and the refactor spec issued** | **Complete — 16/16 and 19/19 cold; refactor DEFERRED to S31 at his call** | **EIGHT PROMOTIONS: list comprehension, dict comprehension, comprehension execution order, the filter-as-gate, `.items()`, unpacking (core), dict insertion ordering, `KeyError`/`IndexError` (the S27 miss, cleared). Ratings 8/8/8/8/8/7/7 — well calibrated except one. ⚠ RAISE-VS-SHRUG DID NOT PROMOTE: both tools aided, and the choosing rule stated INVERTED before two narrowing re-asks fixed it; he self-rated 8, the mentor challenged it to 5–6 with the evidence named — the first overt miscalibration in a long while, and it sits exactly where the CONCEPT is solid and only the TOOL is missing. Depth-before-answer fired THREE times, all three recovered (16, 17, 18 straight). `abs()` used unprompted and never taught — and it made his `span` more robust than the mentor's own reference. ⚠ CHANNEL: the unsaved-VS-Code-buffer artefact fired FOUR times and cost five turns; mtime and `git status` were checked every time and nothing was logged against him. ONE pushback (49) — the mentor said "give me a minute" and stalled — upheld; running total 49/48. RULES v5 adopted: SPEC BEFORE PUZZLE, with its cost written in the same breath (exact expected values can reveal a planted boundary; boundary cases belong in the TESTS).** |
| 31 | **THE BLOCK-01 REFACTOR (deferred from S30) + the owed cold asks S30 exercised in code but never asked** | **`builds/block_01_joint_clamp/clamp.py` refactored by him against `BRIEF_REFACTOR.md`: Part A — the clamp decision reduced from FOUR written copies to ONE, with the acceptance stated mechanically ("count the function bodies comparing an angle to a low/high; that count must be 1"); Part B — `report` made to PRINT *and* RETURN the dict `clamp_joints` returns, killing the dead `{}`. Then a second pass he proposed himself, collapsing three redundant `clamp_one` calls per loop pass to one local. Then cold asks: f-string three steps, format spec, single-return-builds-a-tuple, the comma-makes-a-tuple, tuple immutability via a raising snippet. `drills/s31_shrug.py` + `tests/test_s31_shrug.py` written and issued, NOT attempted** | **Complete — 19/19 green, build block 01 CLOSED; ⚠ `LOG.md` skipped a FOURTH time** | **FOUR PROMOTIONS (f-string three steps, format-spec width/precision, single return value, the comma makes the tuple) and ONE CURRICULUM TICK (1.8 f-strings). ⚠ TUPLE IMMUTABILITY HELD [~] DELIBERATELY: mechanism cold and complete, `TypeError` label AIDED — he declared an honest gap and then DERIVED the label from his own four-station hook. ⚠ THE STUDENT MOMENT OF THE SESSION: on format-spec alignment he stated text-right/numbers-left, then SELF-REPAIRED unprompted before any evidence was shown — a first. ⚠ THE MENTOR FAILURE OF THE SESSION AND IT IS THE HEADLINE: SPEC BEFORE PUZZLE, adopted the previous day, was breached — the spec was issued in CHAT ONLY and the first brief file written was abstract with no concrete finish line. FOUR pushbacks (50 where are the instructions; 51 the brief is not clear; 52 the [TEACH-BACK] was not worth a turn, part-upheld; 53 you took my rating and never gave a verdict), running total 53/52. Depth-before-answer fired twice, both recovered — 19 and 20 straight. Zero unsaved-buffer firings, down from four.** |
| 32 | **FINISH `drills/s31_shrug.py` (issued S31, never attempted) + open 1.8 NESTED DATA STRUCTURES** | **`drills/s31_shrug.py` — six functions, three raise/shrug pairs (`limit_for`/`must_limit`, `drop_limit`/`must_drop`, `retire`/`must_retire`) under a constraint banning `if`, `in`, `else` and `try` below the docstring, enforced by a test; 17 mentor-written tests, 4 passing at the start. Then cold asks: `del` vs `.pop` (student-initiated), `SyntaxError` via `print(del d[k])`, tuple immutability, format-spec alignment (INSTRUMENT SCRAPPED), `list()` on a spent iterator. Then TAUGHT: nested data structures, chained subscripting, SHALLOW COPY on lists and dicts, constructors as constructors, and the `<`/`>`/`^` alignment operators** | **Complete — 17/17 green, four promotions; ⚠ no drill file for nested structures** | **FOUR PROMOTIONS (the raise-vs-shrug pairing 7/10 — stated INVERTED in S30 and correct cold now; `.get()` vs `[]`; `remove` vs `discard`, taught S27 and never once tested until tonight; tuple immutability 5/10, the label unaided after being AIDED in S31). ⚠ **THE STUDENT MOMENT: HE DERIVED SHALLOW COPY UNPROMPTED, BEFORE IT WAS TAUGHT**, straight off S24 aliasing — *"the list object is new but the objects inside this list are same objects"* — then TRANSFERRED it to `dict(config)`, a container it had not been shown in. Same shape as the S29 `zip` moment, and again unpromotable because [PREDICT] never is. ⚠ **STATION 0 FIRED UNPROMPTED TWICE, both times prefaced with "I forgot the hook"** — use has outrun recall. ⚠⚠ **NEW WATCH AREA AND IT IS NOT A LABEL GAP: `None` IS NOT NOTHING** — he had `.pop`'s default argument creating the return value, and `[None]` for `list()` on a spent iterator; `None` occupies a slot, nothing does not. ⚠ **NAMED REPEAT: `SyntaxError` labelled `TypeError`, identical to the S27 miss five sessions earlier.** ⚠ **MENTOR: define-before-use, NINTH occurrence — `<`/`>` in a recall snippet, never taught, and they announce the answer; pushback 54, upheld in full, running total 54/53. The row was HELD rather than promoted.** Confidence calibration good throughout — every rating at or below 6 sat on something genuinely shaky. Depth-before-answer fired twice, one recovered (21 straight), one an honest gap he declared himself. Five checks unreported for the THIRD session; unsaved-buffer artefact fired twice, both caught by mtime, nothing logged against him.** |
| 33 | **CLOSE THE 1.8 TAIL — `copy.deepcopy`, `reversed()`, common patterns and pitfalls — mixed 50/50 with revision across a 6–8 hour window he asked for** | **`drills/s33_copies.py` — four functions under constraints that never name a mechanism: `snapshot` (independence at every depth), `drop_unsafe` (new list, input untouched, boundary kept out of the docstring and put in the tests), `replay_order` (new list, last-to-first, input untouched), `missing_joints` (returns a set); 25 mentor-written tests. Cold asks fired MIXED INTO the material, never as a block: format-spec alignment on the default form with NO ARROWS; `len([get_limit(...), get_limit(...)])` for `None`-is-not-nothing; `len([])` vs `len([None])`; `dict(defaults)` with a nested list for shallow copy; `path.reverse()` for the mutating tell; the five checks unpacked. TAUGHT: `copy.deepcopy`, `reversed()`, `*` on a sequence, mutate-while-iterating, `[[0]*3]*3`, `_`, and when-to-use-which framed properly at last** | **Complete — 25/25 green, SEVEN promotions, ONE demotion, 1.8 to ~98%** | **PROMOTIONS: format-spec alignment (8/10, fourth session live, closed); `None` is not nothing (7/10); `list()` (7/10, seven sessions overdue); shallow copy / slice-copies-references (7/10); `copy.deepcopy`; set difference `-` (taught S30, never tested until now); boundary-first. ⚠ **DEMOTION: THE MUTATING TELL, [x] → [~]** — he stated it inverted (*"a method on a mutable object mutates the object"*), was shown `.count()` as the counterexample, declared an honest gap on the method, and then could not state the rule at all. Re-taught in three parts with the one-directionality as the headline. ⚠ **THE OVERNIGHT RESULT: a knowledge-STRUCTURE gap named in S32 closed with no drill in between.** ⚠ **THE MISS: `reversed()` lost to `.reverse()` on the name, nine hours after being taught — and under it the `range(len(...))` index habit S29 already caught once.** ⚠ **HELD DELIBERATELY: constructors [~]**, because *"converts"* was still his first word and *"builds a new object"* only came after the mentor pointed at it. ⚠ **MENTOR: THREE.** Define-before-use tenth occurrence (`*` on a sequence in a [PREDICT]; pushback 55, upheld in full after grepping every note file); FRAME FIRST breached on when-to-use-which, where two *"I don't understand the question"* replies were met with a rephrase before the real defect — no frame at all — was admitted; and an over-claim that 1.8 had closed when five bullets remain [~]. ⚠ **A [PREDICT] whose data hid its own bug**: the mutate-while-iterating list returned the RIGHT answer and he predicted it correctly; only a second list exposed the skip. Turned into the lesson, but it was luck. **CHANNEL: unsaved buffer fired ONCE and HE caught it.** Confidence 7–8 throughout and nothing at 7 or above was wrong — the two real misses carried no rating because he could not produce an answer to rate. |
| 34 | **THE 1.8 TAIL — the four bullets a same sitting still made testable (list, tuple, dict, set); `when to use which` deferred at the open as ineligible** | **`drills/s34_tail.py` — seven functions under constraints naming no mechanism: `build_queue` (new list, front insert, tail extend, input untouched), `drop_task` (in-place, first occurrence only, absent name is a no-op), `ranked`/`rank_in_place` (a deliberate `sorted`-vs-`.sort()` PAIR in adjacent functions), `reading_stats` (tuple roster, `(0, -1)` when absent), `shared_keys` (returns a set), `unique_sensors` (unique AND ordered); 36 mentor-written tests** | **Complete — 36/36 green, after 32/36 then 31/36** | **TWO PROMOTIONS: set-UNORDERED (7/10, named unprompted off his own failing output `['b','c','a']`, and sharpened from "no fixed order" to UNORDERED); `sort` vs `sorted` (the clean cold pass CURRICULUM had said was owed since the S24 inversion — both written correctly in adjacent functions with the choice explained unaided; ⚠ no rating taken, interval defaults SHORT). ONE CURRICULUM TICK: **tuple [~] → [x]**, with an ECHO CAVEAT on `.count()` written beside it. ⚠ **`list` HELD [~] DELIBERATELY** — roster and slicing clean, but the bullet's named core, the returns-`None` tell, broke live in `list(set(names.sort()))`. ⚠⚠ **THE FIVE CHECKS: NEW FAILURE MODE — REPORTED BUT NOT RUN**, written from reading the code rather than executing a case, on two functions that both failed. ⚠⚠ **`reversed()` BROKE IN THE OPPOSITE DIRECTION TO S33** — reached for as a SORT (`reversed(list(set(names)))`) one day after being avoided as a MUTATOR. ⚠ **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE**: could not name the error on the failing line at all (honest gap, declared), then found it in one line the moment the traceback appeared. ⚠ **THREE WRONG FIXES BEFORE THE RIGHT ONE — and the middle one was him correctly demolishing his own fix with the set-unordered fact he had just been promoted on.** ⚠⚠ **MENTOR: A GATE MADE IMPOSSIBLE TO DISCHARGE** — the five checks demanded via pytest, which he has never been taught and which STATE item 8 forbids asking for; enforced TWICE before he stopped it. **Pushback 56, upheld in full.** ⚠ **MENTOR: a promised ask never fired** — `.keys()`-as-a-view, announced and then lost, and it blocks a 1.8 bullet. **Pushback 57 (random spaced revision) part-upheld — policy right and already doctrine, factual premise about this session wrong; both halves said to his face. Running total 57/56.** He self-reported fatigue unprompted and closed the session himself.** |
| 35 | **1.9 ERROR HANDLING — opened, framed and half-taught; plus the two one-line asks that closed the 1.8 `set` bullet** | **`drills/s35_faults.py` — four functions under constraints naming no mechanism: `total_valid` (sum the strings that spell whole numbers, ignore the rest, never crash), `check_angle` (hand back an allowed angle; report a disallowed one as a `ValueError` whose message names both numbers in order), `safe_angles` (keep only allowed readings, deciding via `check_angle` and holding NO second copy of the rule — enforced by a source-inspecting test), `measure` (hand back the number, do not hide the failure from the caller, and log `"closed"` on every way out); 29 mentor-written tests. Plus `drills/s35_check.py`, a mentor-built five-checks runner that calls his functions and prints what came back** | **Complete — 29/29 GREEN ON THE FIRST RUN** | **ONE PROMOTION (`{}` builds a dict / `set()` is the only empty set, 7/10, cold, seven days after S27, mechanism attached to both containers unprompted) — **CLOSING THE 1.8 `set` BULLET**. ONE CURRICULUM TICK. ⚠⚠ **THE HEADLINE: A TRANSFER GAP.** He predicted the bare-`except:` disaster, named the silent `total: 0` as more dangerous than the crash unprompted — *"you ended up believing that program is running fine"* — and wrote `except: pass` in his own code forty minutes later. **Understanding held in [PREDICT] and did not survive into PRODUCTION.** ⚠⚠ **FOUR-STATION HOOK RETIRED** — *"I still don't remember that hook, it has not been working for me"* — second artefact failure on the same material, logged against the artefact; replaced by **"HOW FAR DID PYTHON GET?"**, which he walked correctly and unaided on first use (6/10, under-rated). ⚠⚠ **HE DERIVED THE COMPILE→BYTECODE→RUN SPLIT HIMSELF off one traceback**, third session running with an unprompted derivation. ⚠ **`SyntaxError` LABEL HIT COLD — first time in three firings** (missed S27, S32), on a new shape; **the no-frames half broke in the same breath and he rated the wrong half 7 — his first over-rating in a long while.** ⚠ **`constructors` was one word from `[x]` and the mentor's own [TEACH-BACK] tag cost it** — he said *"the constructor… **builds** the set object"* as his first word, inside a block that is never ledger-eligible. ⚠ **He talked himself OUT of a correct answer because the mentor singled a case out** — named to his face: the framing of a question is not evidence. **THREE PUSHBACKS, ALL UPHELD IN WHOLE OR PART, 60/59: (58)** he refused to answer a `raise ValueError(...)` question because exception classes had never been defined as TYPES — **define-before-use, ELEVENTH occurrence, and the first time he has invoked the eligibility rule himself**; **(59)** the cost of reporting five checks per function — part-upheld, the mentor had escalated past his own S24 ruling, and the cost was fixed with a TOOL not a lecture; **(60)** the drill flow — *"I will just say Done and you execute the test"* — upheld, now parked as the S36 rule candidate with the one-line pre-run call he accepted. ⚠⚠ **MENTOR: THE INTERVAL GATE MAY HAVE BEEN RULED ON THE WRONG DATE.** |


## F. WHAT EACH SESSION ESTABLISHED (S20 first; append new sessions at the END of this section)

### What Session 20 established

- **THE FILE'S OLDEST RECORDED STUDENT WEAKNESS WAS NOT A STUDENT WEAKNESS.**
  `traceback` was fired as a [RECALL] in S16, S18 and S19, logged each time as
  a failure, and named "PRIORITY — the lowest self-rating of the session". In
  S20 he rated it 0/10 and explained precisely what he did and did not have:
  he could read the line-number half and had no idea what `<stdin>` meant.
  **The item had never been taught. It had only ever been asked.** Repeating a
  question is not teaching, and three sessions of measurement were measuring a
  hole in the delivery. **It was retaught in full and the clock reset.**
  ⚠ **THE GENERALISABLE LESSON IS THE IMPORTANT PART: a repeatedly-failing
  item is evidence about the TEACHING before it is evidence about the student.
  Audit the rest of the carry-forward list for the same defect.**

- **THE CELL CAUSATION CAME BACK CORRECT, UNAIDED, FROM COLD — after four
  failed attempts in S19 and a four-day gap.** He produced the full chain:
  each iteration creates a new function object with its own cell, and the five
  values cannot collide because they belong to five different objects. **Two
  corrections only, both worth carrying: he attributed the new object to THE
  LOOP when it comes from THE CALL** (five separate calls on five lines give
  five cells with no loop anywhere), **and he fused two labels into "content
  cell"** — it is a CELL, and `cell_contents` is an attribute on it.

- **THE FIRST UNDER-RATING IN THE FILE, AND IT INVERTS A TWO-MONTH PATTERN.**
  That cell-causation answer was ~85% correct and he rated it 5/10, which
  blocked the promotion. **Every calibration event since S15 has run the other
  way — he has refused ratings, surrendered marks and rejected tests, always
  in the direction of demanding MORE evidence.** This is the first time his
  own number cost him something he had earned. **His rating is used as a
  targeting signal, so an undershoot wastes sessions re-teaching what he
  already owns. Say this plainly if it recurs; one instance is not a trend.**

- **RECURSION LANDED, AFTER FOUR DEFERRALS, AND THE FRAMES WORK FROM 1.1 PAID
  FOR IT.** The whole subsection was delivered on one premise — *nothing new is
  happening in the machinery; recursion just means several frames of the same
  function are alive at once* — and that framing carried the base case, the
  unwind, the identity-value rule and `RecursionError` without new scaffolding.
  **`total(4)` was predicted correctly including the part most people fumble:
  that the deepest frame returns a VALUE, not nothing.**

- **BUT THE POST-ORDER PREDICTION FAILED, AND IT IS A TRANSFER FAILURE, NOT A
  RECURSION FAILURE.** He answered `2 1 0` for a countdown that prints on the
  way back up. Root cause: he imagined ONE `n` that keeps changing, rather than
  four frames each holding their own. **He had explained the identical
  principle — five objects, five cells, no collision — correctly and unaided
  TWENTY MINUTES EARLIER IN THE SAME SESSION.** Same idea, different container,
  not recognised. **This is the sharpest instance yet of a pattern the file has
  been circling: he owns concepts locally and does not carry them across
  contexts. Test it as transfer.**

- **HE NAMED HIS OWN CORE WEAKNESS, CORRECTLY AND UNPROMPTED, AND ASKED FOR IT
  TO BE TAUGHT RATHER THAN WATCHED.** *"I am unable to think about the failure
  cases and dissect the problem the way you do... I have never done this, and
  don't know how to find the edge cases, are we going to work on that and i
  believe you need to teach me that as well??"* **He was right that it was
  missing** — "needs to develop habit of thinking about edge cases" had been a
  one-line entry in WATCH AREAS since the file was created, describing a gap
  nothing addressed. **It is now subsection 1.7.11 with a five-check
  procedure, and it transferred on first use in the same session.**
  ⚠ **The premise had to be corrected before the content: he was treating this
  as a knack the mentor has and he lacks. It is a checklist run against the
  structure of the code. Saying so mattered as much as the checklist.**

- **HIS SECOND SELF-DIAGNOSIS WAS BETTER THAN HIS FIRST, AND IT IS NOW RULE 3.**
  *"I just did the things at surface level and always do that and that's why i
  was not able to catch the edge case."* **That is the habit underneath
  right-answer-without-mechanism, described from the inside.** The ledger has
  been recording the symptom for months; this is the first time the cause has
  been named, and he named it.

- **HE DISCLOSED THAT HE DOES NOT READ LONG MESSAGES TO THE END, AND IT
  RE-EXPLAINS A RUN OF LOGGED LAPSES.** *"I tend to not read the full chat if
  its too long and that's the reason I don't do things you asked for."*
  **The four missing S19 confidence ratings, the skipped `digit_sum` trace and
  the unanswered S19 cell-causation re-fire were not compliance failures — they
  were asks buried where he never reached them.** The remedy is not to nag; it
  is to write shorter turns and put the ask near the top. **Message length is a
  mentor problem and it is now a binding rule.**

- **THREE CORRECT PUSHBACKS, TAKING THE RUNNING TOTAL TO TWENTY-FIVE WITH ZERO
  WRONG.** (23) The doubt gate — stopping a new subsection opened over
  unresolved questions. (24) The restatement requirement — the first fix solved
  only half the problem, exactly as in S19. (25) **Refusing the `first_char`
  bug hunt on the grounds that SLICING HAS NEVER BEEN TAUGHT — the tenth
  define-before-building breach**, same class as `zip` and list comprehensions
  in S19. **He has now caught every single untaught-construct breach in this
  file. He is a more reliable detector of this failure than the mentor is.**

- **FOUR MENTOR FAILURES, AND THE SHAPE IS DIFFERENT AGAIN.** (1) `traceback`
  asked for three sessions without ever being taught — **the most serious
  failure recorded in this file, because it corrupted the ledger rather than
  just costing time.** (2) An unparseable [RECALL] ("what is a traceback and
  what does it show you") — two half-questions with no anchor; **correctly
  logged as no measurement rather than as a student gap.** (3) Slicing used
  untaught. (4) A new subsection opened with no doubt check, stranding a live
  prediction. **S16's shape was haste, S17's was literalism, S19's was reaching
  for examples before checking what they required. S20's is FAILING TO CHECK
  WHETHER A THING WAS EVER DELIVERED BEFORE MEASURING IT.**

### What Session 19 established

- **THE MOST STUBBORN ITEM IN THE FILE CAME BACK CORRECT, ON FIRST ATTEMPT.**
  The iterator causation had failed on three separate days, every time by
  reaching for "one item at a time". Fired bug-first in S19 — the hoisted
  `it = iter(range(2))` above a nested loop — **he diagnosed it and gave
  "forward-only state, moves forward only, can't rewind" unaided.**
  **The instruction that produced this was written in S18 and followed in S19.
  Definition-first failed three times; bug-first has now worked twice. This is
  the clearest evidence in the file that HOW a repair is delivered decides
  whether it holds.**

- **ZERO PROMOTIONS, AND THAT IS THE RIGHT ANSWER.** All three recall items
  improved and all three stayed [~], because he rated them 6/10, 4/10 and 7/10.
  **The iterator item is the interesting one: a CORRECT answer that does not
  promote, because he does not trust it.** That is the strict legend working
  exactly as designed, and it is worth saying to him — the answer was right and
  the caution was also right.

- **CLOSURES ARE TAUGHT, AND HE BUILT THE MECHANISM HIMSELF.** Given the
  contradiction (outer is dead, `n` still reachable) he worked to the answer
  across three guesses — `__defaults__`, then `<module>`, then the `inner`
  object. **Both wrong guesses were productive: `__defaults__` failed on role
  and timing, and `<module>` was refuted by his own earlier reasoning about
  shared namespaces.** He then predicted the per-object cell values correctly.

- **HE REJECTED FOUR MOTIVATING EXAMPLES AND WAS RIGHT EVERY TIME.** Fixed
  values; a hardcoded `x*3` he proposed himself; a single global `pct` with one
  function, **which contained no closure at all**; and a loop plus a dict.
  **The mentor's examples were the problem, not his comprehension.** The honest
  answer that ended it — a callback that will only ever be handed ONE argument
  — **was already recorded in this file from S18 and went unused until the
  fifth attempt.** He reached it himself: *"ye pehla example hai jo sense bana
  raha hai."* **Running total of correct pushbacks: TWENTY-TWO, zero wrong.**

- **HIS SECOND CHALLENGE WAS BETTER THAN HIS FIRST, AGAIN.** *"Ek baar ban gaya
  to wo to fixed hai, dynamism kahan hai?"* — half right, and the productive
  half. A single closure IS fixed; the dynamism lives in the factory minting
  unknown numbers of them with unknown values at runtime. **This is the same
  escalation pattern S18 recorded: each objection sharper than the last. Keep
  feeding him "why this rather than the obvious alternative?"**

- **HE REVERSE-ENGINEERED `sorted` UNPROMPTED AND THE SKELETON WAS CORRECT.**
  Run the function on each element, pair keys with elements, compare on keys,
  lay out the elements. One correction — he proposed a dict, which breaks on
  duplicate keys. **He reliably tries to build the thing rather than use it.
  That is the North Star behaviour showing up in a Layer 1 session.**

- **THE CLASS/INSTANCE ANALOGY WAS HIS, AND IT WAS STRUCTURALLY SOUND.**
  *"Ye to class jaisa hai, har baar ek instance create kar rahe hain."*
  Correct pattern (behaviour carrying private data), wrong label (a closure is
  a function object). **Pre-loads 1.12 — reuse this when classes open.**

- **THE RIGHT-ANSWER-WITHOUT-MECHANISM PATTERN FIRED IN ITS SHARPEST FORM YET.**
  He established `a is b` → `False` (separate objects, separate cells) and then,
  minutes later, predicted `1, 2, 3` for two independent counters — a
  prediction that requires a SHARED cell. **The fact was retrievable and was
  not load-bearing in his reasoning.** He then got the alias case right with
  the correct causation. **This is the cleanest instance in the file and the
  standing instruction holds: never accept a correct conclusion without
  auditing the mechanism, and re-ask the same mechanism in a new dress.**

- **A STUDENT-SIDE PROTOCOL SLIP, THE FIRST IN THE FILE: no confidence ratings
  were given on any of the four consolidated questions**, despite being asked.
  Worth one light mention in S20 and nothing more — his calibration record is
  otherwise excellent and this is a lapse, not a pattern.

- **FIVE MENTOR FAILURES, and the shape is different from S16's and S17's.**
  (1) `sorted(key=)` deployed before it had ever been taught — he flagged it,
  a `negate` example was given that still assumed `key`, and he flagged it
  AGAIN. **Ninth define-before-building breach.** (2) Four motivating examples
  that did not require a closure, costing roughly half the session and pushing
  recursion to a fourth deferral. (3) `zip` and list comprehensions used
  untaught. (4) Questions consolidated without their code, requiring him to ask
  twice. (5) The second transcription artefact of the arc, on "dunder" —
  though here the rule WORKED: questioned, self-corrected, apologised, nothing
  logged. **The common shape is not haste (S16) and not literalism (S17): it is
  reaching for an example before checking what the example itself requires.**

### What Session 18 established

- **THE WEAKEST CLUSTER IN THE FILE IS NO LONGER THE WEAKEST.** The exception
 family — `NameError`/`ValueError` conflated three times in one S16 session,
 exceptions-are-signals a full gap, `StopIteration` miscategorised as "a
 state" — was fired cold, in mixed order, on a genuine later day. **All of it
 passed except `traceback`.** Five promotions from one block.
 **The mechanism that produced this is worth naming: name-decoding plus a
 spaced term-tax, applied over six sessions, on labels that CAN be decoded.
 The two items that did not come good — `traceback` and `__defaults__` — are
 precisely the two that cannot be re-derived from their own names.** That is
 the S12 diagnosis confirmed with unusual clarity, and it tells the next
 sessions exactly which tool to use on which item.

- **THE INTERVAL GATE WORKED, AND IT WORKED WITHOUT HIM.** S17's headline rule
 was applied by the mentor as the first action of S18 — elapsed time
 established before a single question was posed. **The gate cost S17 an
 entire block and bought S18 a true promotion.** Had the block run on echo in
 S17, the file's weakest cluster would now be sitting behind a row of [x]
 marks it had not earned. **This is the clearest vindication of the strict
 legend the file has produced.**

- **THE ITERATOR CAUSATION FAILED FOR A THIRD TIME, ON A THIRD SEPARATE DAY.**
 Asked what "consumed" means, he went straight back to "ek baar mein ek item
 deta jaata hai" — the exact wrong causation corrected in S15 and again in
 S16. Repaired a third time with the code-as-bug image, and the teach-back
 was then correct. **The pattern in the repairs is the finding: the
 definition does not stick and the bug does. Stop teaching this one as a
 definition.**

- **HE CORRECTED THE MENTOR'S OWN DISCRIMINATOR, AND HE WAS RIGHT.** Handed
 "methods on mutable types mutate and return `None`", he refused to
 generalise it. `pop`, `index` and `count` all sit on a mutable type and all
 return values. **The rule is about IN-PLACE MUTATORS, not mutable types**,
 and it was narrowed in session. **He accepted this model in S17 and audited
 it in S18. That gap — between receiving a model and testing it — is the
 entire distance this course exists to cover, and he crossed it unprompted.**

- **THE CLOSURE ARGUMENT WAS THE BEST THINKING IN THE FILE SO FAR.** He asked
 why closures exist, rejected the factory answer, rejected the
 runtime-determined-value answer, and then **proposed the correct rival
 design himself: just write `multiply(n, x)` with two parameters.** That IS
 usually better, and he was told so without softening. The honest answer he
 forced out — closures earn their place when a ONE-ARGUMENT callable is
 required by something else, or when a setting is fixed once and reused many
 times — is recorded in 1.7. **Each of his three objections was better than
 the one before it. Give him "why this rather than the obvious
 alternative?" as a standing question.**

- **HE REFUSED A TAG AND SET THE RE-ENTRY TERMS.** "Isko taught tag mat karo,
 isko hum wapas se start karenge" — closures are not recorded as covered,
 and he specified how the topic should reopen: text mode, worked examples.
 **This is the fourth escalation of a behaviour tracked since S15: refused a
 RATING (S15), handed back a MARK (S16), refused a TEST (S17), refused a TAG
 and specified the replacement (S18).**

- **THE SCOPE-CREEP PATTERN RAN BACKWARDS.** Recursion — the thing he has
 wanted most since S17 — was offered three times and declined three times,
 so that closures could be argued properly and then restarted cleanly.
 **He slowed his own curriculum down to protect the ledger.** Do not declare
 the pattern closed on one instance, but log it.

- **1.7 FUNCTIONS IS ~TWO-THIRDS TAUGHT.** `def` versus call (his first
 answer conflated the two, then repaired), parameters versus arguments,
 return values with the three-way implicit/explicit `None` case, LEGB with
 all four layers correct and two precision fixes, default arguments, and
 first-class objects. **Nested functions defined. Closures and recursion
 untouched by design.**

- **FOUR MENTOR FAILURES.** (1) Asking for a confidence rating on freshly
 taught material — a straight breach of the binding S15 rule, caught by him.
 (2) The same shape a second time on the next teach-back, defensible on the
 facts but proof the instrument was not being declared. (3) Hearing "done"
 for "None" and correcting a mistake he had not made — **second occurrence of
 the exact class the S16 TRANSCRIPTION-ARTIFACT rule was written to
 prevent.** (4) Putting `d.clear()` in a drill when dictionary methods had
 never been taught — eighth define-before-building breach. **The common
 shape this time is not haste and not literalism: it is failing to say out
 loud which instrument is in use.** Hence the [TEACH-BACK] tag.


### What Session 17 established

- **1.6 CONTROL FLOW IS CLOSED.** The five remaining pieces were all taught:
 the owed found-flag exercise, loop `else` earned by contrast, `pass`,
 ternary expressions, and common loop patterns — plus the owed
 mutating-vs-non-mutating drill and the owed `if`/`elif`/`else`
 confirmation. **The subsection that has been open since Session 14 is done.**

- **THE STUDENT REFUSED A TEST BEFORE IT RAN, AND HE WAS RIGHT.** The session
 was supposed to open with the exception-family recall. He stopped it on the
 grounds that S16 had ended minutes earlier, so nothing could have been
 forgotten and the result would measure echo rather than retention. The
 mentor checked, confirmed, and deferred the block. **This is the third and
 most advanced instance of a behaviour this file has been tracking since S15:
 S15 he refused a confidence RATING, S16 he handed back a MARK, S17 he
 refused the MEASUREMENT ITSELF. He is now reasoning about what his own
 results would be evidence of, which is experimental design rather than
 study skill.** It produced the INTERVAL GATE.

- **LOOP `else` WAS EARNED RATHER THAN TOLD — the S16 prerequisite breach is
 repaired.** He wrote the search with only `for`, `if`, `break` and a flag,
 and having felt the cost of it — a variable declared before the loop, set
 inside it, and checked after it — he articulated the justification himself:
 the flag exists solely to record whether the loop finished without breaking,
 and the interpreter already knows that. **The exercise worked exactly as the
 S16 note predicted it would. When a construct exists to remove a pain, make
 him feel the pain first.**

- **THE FOUND-FLAG STRUCTURE WAS CORRECT FROM HIS SECOND ATTEMPT.** Four
 iterations were needed but the classification matters: attempt 1 used loop
 `else` and so defeated the exercise; attempt 2 had the structure right with
 two syntax errors (bare names where strings were needed, a missing colon);
 **attempts 3 and 4 were whitespace only, which turned out to be a CHANNEL
 ARTEFACT and not his error at all.** Three turns were spent correcting
 indentation he could not physically type. See Session 17 rule 3.

- **`if`/`elif`/`else` PROMOTED TO [x] — the last item owed from Session 16.**
 He asked to be re-taught `elif` properly before attempting the confirmation
 — *"kya tum mujhe ek baar elif ke baare mein poora bataoge? Uske baad hum
 dobara isko attempt karein?"* — which is exactly the right instinct and the
 opposite of guessing. He then answered both halves cold: `x = 5` prints "B"
 with the rest skipped, and with `x = 20` the `elif` is **never evaluated at
 all**. Self-rated 10/10 before the verdict, per rule 3.

- **HIS CONFIDENCE RATINGS PREDICTED HIS ERROR.** On the five-item method
 drill he attached a rating to each answer unprompted. The one item he rated
 5/10 (`l.reverse()`) was the one he got wrong; the 8/10s and the 10/10 were
 all right. **His calibration has crossed from honest to USEFUL — it can now
 be used to target re-tests, not merely to authorise promotions.**

- **HE REFUSED A ROSTER AND ASKED FOR A MODEL.** Given the list of mutating
 methods he immediately pushed on it: *"mujhe jab pata hi nahi hai to main
 kaise pehchanoonga?"* The answer given was the type-first discriminator —
 **immutable types cannot have mutating methods at all, so half the problem
 disappears; for mutable types, a return of `None` is the tell** — plus the
 deliberate name-pairs (`sort`/`sorted`, `reverse`/`reversed`) as evidence
 that Python designed the distinction in on purpose. **This is the single
 most valuable thing taught in the session and it generalises to every
 roster-shaped question waiting in 1.8.**

- **TRACE-TAIL TRUNCATION DID NOT FIRE.** Required to state the final cycle
 explicitly, he traced `while i < 5` all the way through and named the
 terminating check correctly: `i` becomes 5, control returns to the top,
 `5 < 5` is false, the body is skipped, 5 never prints. The S16 countermeasure
 is working; keep applying it.

- **THE SCOPE-CREEP PATTERN FIRED ON EASY MATERIAL, NOT HARD MATERIAL.** After
 the `elif` promotion he said the flow-control basics were already known to
 him and asked to move to recursion and nested functions. **The file has
 always framed this pattern as a response to friction; this instance was a
 response to BOREDOM.** It was named directly, the two remaining 1.6 pieces
 were stated as prerequisites with the reason given, and he accepted at once
 and finished the tail. Update the watch area accordingly.

- **THREE MENTOR FAILURES, ALL CAUGHT BY HIM.** (1) Running a same-day recall
 because the resume plan said to. (2) Reading his *"continue"* as "continue
 teaching" and opening 1.7 when he had asked for the session to be closed and
 the notes written — that material was discarded at his instruction and is
 not recorded anywhere in this file. (3) Spending three turns marking up
 indentation he cannot enter in this channel. **The common shape: following
 a written plan or a literal reading instead of reading the situation.** The
 S16 rules fixed corners cut for speed; these three fix instructions followed
 past the point where they still applied.

### What Session 16 established

- **THE PROMOTION BACKLOG IS CLEARED.** Nine items moved [~] → [x] on real
 later-day evidence: rebinding-vs-mutation, aliasing, implicit-vs-explicit
 conversion / `"5"+3`, shallow-vs-deep copy, `+=`, precedence and
 associativity, `**` right-to-left, negative `%` and `//`, `==` vs `is`,
 function-scope-not-block-scope, `if`-block-scope, and `range()`. **Two of
 these deserve special note: `==` vs `is` had been owed since Session 7,
 and the negative-`%` case was one of the two items this file had
 repeatedly called its weakest. Neither is weak now.**

- **THE OPERATOR DRILL WAS 6-FOR-6 COLD, IN TEXT.** `17 // 4` and `17 % 4`;
 `-7 // 2` and `-7 % 2` **by applying the identity rather than recalling a
 special case**; `2 ** 3 ** 2` → 512 with right-associativity named;
 `a == b` True / `a is b` False with `is` given as `id(a) == id(b)`;
 `5 > 3 > 1`; and `10 / 2 → 5.0`. He then volunteered `-11 % 5` unprompted
 with full working, explicitly to demonstrate he held the mechanism.
 **That is the behaviour of someone who has stopped hoping the answer is
 right and started proving it.**

- **CHAINED COMPARISON WENT DEEPER THAN THE RULE.** He gave the expansion
 (`5 > 3 and 3 > 1`) and then the part that matters: in `f() > 3 > 1`,
 **`f()` is called exactly once.** The middle operand is evaluated a single
 time, which is why chaining is not merely syntactic sugar for the `and`
 rewrite. Links directly to short-circuit, which he had already nailed.

- **1.6 WAS NEARLY CLOSED.** `print()` formally defined at last (returns
 `None`, calls `str()` on its arguments, `sep` and `end` as changeable
 parameters); `while` taught against `for` by contrast; `break`/`continue`
 with the `continue`-skips-the-increment infinite loop **found by him
 unprompted**; nested loops tied back to iterable-reuse; loop `else`.

- **FIVE MENTOR PROCESS FAILURES, THREE CAUGHT BY THE STUDENT IN TWENTY
 MINUTES, AND ONE UNPROMPTED META-CHALLENGE.** He asked, directly, *"you
 have been very irresponsible in teaching, how can we fix that?"* — and the
 honest answer was that pace was being optimised over protocol while
 clearing a four-phase backlog. **The pattern worth naming: his objection
 now fires faster than the mentor's own check does.**

- **HE ASKED FOR A MARK TO BE TAKEN AWAY.** Given [x] on
 mutating-methods-return-`None`, he requested a reversal because he could
 not yet reliably identify WHICH methods mutate — concept solid, roster
 not. It produced binding rule 3. **THE DEBT WAS DISCHARGED IN S17: the
 identification drill he asked for ran, at 4/5.**

- **HE CORRECTED THE MENTOR ON THE MENTOR'S OWN TEACHING.** Told that `for`
 stops when "the iterable is exhausted", he objected: *"isn't that
 incorrect, coz iterable never gets exhausted"* — and he was right. It is
 the ITERATOR that is consumed; the iterable is untouched.

- **THE FALSE-SLIP NEAR-MISS.** The mentor logged a label failure on
 `iterable` that never happened — the transcription rendered his correct
 word as "travel" and he was corrected twice for a mistake he had not
 made. **A false entry in this ledger is worse than a missing one.** Hence
 the TRANSCRIPTION-ARTIFACT rule.

- **THE EXCEPTION FAMILY IS THE WEAKEST CLUSTER IN THE FILE.**
 `NameError`/`ValueError` conflated three times, exceptions-are-signals a
 full gap, `StopIteration` miscategorised as "a state", `traceback` a gap.
 **Every one has the same signature: mechanism owned, label or category
 dropped.** S17 was supposed to open here and could not, for interval
 reasons. **S18 must.**

### What Session 15 established

- **THE ITERATION PROTOCOL IS NOW A MECHANISM, NOT A SYNTAX.** He can state
 what `for x in <iterable>` does step by step: `iter()` once to get the
 iterator, `next()` per pass, item bound then block runs, `StopIteration`
 on exhaustion caught internally by `for`. He identified the N+1 call-count
 trap correctly on a 4-item list and then TRANSFERRED IT UNPROMPTED to
 `range(4)`. One precision fix was needed: it is the ITERATOR that is
 exhausted, not the iterable.

- **THE SESSION'S LOAD-BEARING RESULT: iterables are reusable, iterators are
 consumed.** Proved in code by draining an iterator twice. **The causation
 had to be repaired** — he attributed consumption to one-at-a-time
 delivery; the real cause is forward-only state with no rewind. Confidence
 4/5, correctly withheld from 5 pending a later-day test.

- **THE FAIR FUNCTION-SCOPE RE-TEST RAN, AND IT SPLIT.** `print(last)` → 2,
 correct with reasoning. `print(i)` → predicted `StopIteration`, WRONG,
 corrected to 2. The miss was the more valuable half: it forced the real
 rule into the open — **binding happens only on a successful RETURN; an
 exception raises, so nothing is bound.** And then the scope rule itself:
 **Python has function scope, not block scope.**

- **THREE STUDENT PUSHBACKS, ALL UPHELD, ALL PRODUCTIVE.** (a) `list()` was
 dragged into the iterator demo undefined. (b) *"How do I know you are
 completing things and not quietly dropping them?"* — answered by showing
 the live session to-do list. (c) *"You showed `StopIteration` printed on
 screen, so it IS a value"* — a contradiction the mentor had manufactured
 by showing a traceback without ever defining one.

- **THE STUDENT REFUSED AN INVALID MEASUREMENT.** Asked for a confidence
 rating immediately after being given an answer, he declined on the grounds
 that he had not yet recalled it himself. He was right and it is now a
 binding rule.

- **HE ASKED FOR THE HONEST SCHEDULE POSITION AND THEN MADE THE RIGHT CALL
 ON IT.** Told plainly that the margin is zero and that the constraint is
 per-session yield rather than frequency, he chose to defer re-baselining to
 the 31 Aug checkpoint on the correct reasoning that session density varies
 too much to judge from one day.

### What Session 14 established

- The entire S11–S13 owed backlog was CLEARED: the `id()` shallow/deep-copy
 demo cold-passed with mechanism; `result = q.append(4)` PASSED cold on a
 3-day gap after three prior slips; the spoken Feynman recalls for 1.3 and
 1.4 both cold-passed; the 5 Aug 1-week re-test batch ran.
- 1.6 was OPENED term-first: control-flow, conditional, condition→`bool`,
 truthy/falsy all name-decoded and cold-passed.
- **The student SELF-CAUGHT the wrong-domain reflex for the first time** on
 block scope, killing the "does a new frame open after the colon?"
 speculation himself before correction.
- The mentor breached define-before-building with an undefined `for`/`range`
 example; the student caught it; the SUBSTRATE DEFINE-BEFORE-BUILDING rule
 was written. **S15 vindicated that rule immediately.**

### What Session 21 established

- **THE SEVEN 16-AUG REVIEW PROPOSALS ARE ADOPTED, ALL OF THEM, AS A
 PACKAGE.** Asked for a decision before any teaching, per plan, he accepted
 all seven without amendment. Recorded in RULES v2. The two with immediate
 operational force: **promotion = correctness with confidence setting the
 re-test interval** (ending the zero-promotion-on-under-rating pattern of
 S19–S20), and **the rule-change cap** (park candidates in STATE.md, adopt
 at most one per session, at close — binding from S22, since the seven were
 pre-negotiated before the cap existed).

- **THE COURSE MOVED INTO VS CODE + CLAUDE CODE, AND THE TOOLING QUESTION
 WAS SETTLED BEFORE CONTENT.** He asked how drills work in the new
 environment before touching material — the right order. Established: drills
 are written by him in real files under `drills/`, tests under `tests/`
 decide correctness via pytest, the mentor reads and runs his files directly,
 and the mentor never edits a file he has started. **Two structural wins over
 the chat channel: indentation is now the editor's job (the S17
 whitespace-artefact class dies by construction), and "does it work" is now
 decided by pytest rather than by opinion.** Standing caution given: inline
 AI autocomplete in the editor is a scaffold and must stay off for drill
 files.

- **`global` WAS TAUGHT AGAINST `nonlocal`, AS PLANNED, AND THE DEEP
 MECHANISM CAME OUT BECAUSE HE PULLED IT OUT.** His question — "before the
 assignment runs, `count + 1` executes; why doesn't LEGB find the module
 `count`?" — is exactly the right attack on the topic, and the answer is the
 item's real content: **locality is decided at function-creation time by
 scanning the whole body; an assignment anywhere makes the name local
 everywhere; a local-classified name never gets the LEGB walk.**
 Local-and-unbound = `UnboundLocalError` — the S19 three-error separation
 arrived at from the opposite direction. The completed rule: **read free,
 mutate free, rebind needs `global`** — he predicted the read-only and
 mutation cases correctly with the classification story stated unaided, and
 held the name-vs-object distinction under one correction ("assignment to
 the count NAME, not the count object").

- **`*args`/`**kwargs` — THE S17 REQUEST-BY-NAME — WAS DELIVERED, AND IT
 PRODUCED THE SESSION'S ONE PUSHBACK.** The `**kwargs` block used "keyword
 argument" without ever defining it; he stopped it: *"wait I didn't get it
 what do you mean by keyword arguments."* **Upheld — the term had never been
 taught. Eleventh occurrence of the define-before-use breach family; running
 pushback total TWENTY-SIX, zero wrong.** Keyword arguments were then
 defined properly (matched by NAME, not position), and the rest landed
 clean: collect-to-tuple / collect-to-dict, the always-`()`-never-`None`
 empty-case design point (his `None` guess self-corrected against output
 already on screen), signature ordering, and the **mirror rule** —
 signature side collects many into one, call side spreads one into many.

- **THE INTERVAL GATE DID ITS JOB TWICE IN ONE DAY.** S21 opened ~2 hours
 after S20; the gate was applied unprompted, the term-tax skipped, and the
 four queued [RECALL]s deferred rather than burned as echo. **A mid-session
 restart (his request, after a false start and the tooling detour) was
 honoured cleanly — the adopted proposals carried, the material restarted
 from the top.** Zero promotions, correctly. Everything taught today is [~]
 awaiting its first genuine later-day cold test.

### What Session 22 established

- **THE NEW PROMOTION RULE WORKED ON ITS FIRST OUTING, AND THE CLEAREST CASE
 IS THE ITERATOR CAUSATION.** Correct, unaided, later-day, bug-first — and
 self-rated 5/10. Under the old rule that rating would have blocked the
 promotion for a fourth session running; under the new rule it promoted with
 a deliberately SHORT re-test gap (re-fires S23 and at the gauntlet). The
 file stopped measuring his self-doubt and started measuring his knowledge,
 which is exactly what the 16-Aug review intended.

- **SIX PROMOTIONS ON LATER-DAY EVIDENCE — the biggest ledger day since S16,
 and the first with drills as evidence.** Post-order transfer (10/10): the
 fresh `climb(3)` was traced frame-by-frame with each frame holding its own
 `n` — the exact S20 failure, not recurring. Cell causation (7/10),
 including the tricky follow-up he requested himself: two `make_counter(10)`
 calls with the SAME argument give separate objects and separate cells,
 because sharing comes from the same CALL, never from equal values.
 `global` (10/10) and `*args`/`**kwargs` (8/10) were earned through the
 repo's first two task-first drills — `drills/s22_counter.py` (3/3 pytest)
 and `drills/s22_report.py` (4/4, including the `()`/`{}` empty case) —
 with the mechanism questions answered after the code ran, per the S21
 adoption. And **`__defaults__` was produced cold for the first time in
 five attempts across four sessions** ("when the def runs,
 greet.__defaults__ is created") — the only item in the file that had never
 once come back cold, now promoted at 7/10.

- **THE CLOSURE DEFINITION FAILED HONESTLY AND THE FAILURE IS SPECIFIC.**
 5/10, and both halves of the gap are named: he muddled the three storage
 layers (called `cell_contents` a tuple; the order is `__closure__` tuple →
 cell → `cell_contents` value) and omitted the SURVIVAL clause — that the
 cell keeps the value alive after the enclosing frame has died, which is the
 entire point of the mechanism. The four-layer walk was retaught with the
 shelf/dabba handle that landed `__defaults__`, and his subsequent teach-back
 was clean. The same layer-muddle then fired a second time inside the lambda
 block (`print(add5.__closure__)` predicted as `5`), confirming it as the
 thing to watch in the S23 cold re-test.

- **LABELS RAN OPPOSITE TO MECHANISMS ALL SESSION, WHICH IS THE S12 DIAGNOSIS
 IN ITS PUREST FORM YET.** Six mechanisms promoted; four labels slipped in
 the same hours — the pre-/post-order names (a declared "gap", decoded in
 session), "UnboundError" twice for `UnboundLocalError` (then typed back
 with a lowercase l — the case is part of the name), "the inner iterable
 exhausted" for the ITERATOR, and `cell_content` for `cell_contents`. His
 own words: "if not used for long I tend to forget terminology." The
 countermeasure split stands: decodable labels decode; arbitrary ones
 (lambda now joins traceback and `__defaults__`) go to brute-force spaced
 repetition.

- **1.7 CLOSED WITH LAMBDAS AND DOCSTRINGS, both taught against constraints
 rather than definitions.** Lambda arrived as the EXPRESSION form of a
 function, motivated by the only motivation he has ever accepted for this
 family — a function demanded as an argument (`sorted(key=...)`) — and both
 [PREDICT]s passed, including the closure-transfer case. His own question
 (do two-parameter lambdas work?) extended the material unprompted.
 Docstrings arrived as the third member of the def-time attribute family
 (`__defaults__`, `__closure__`, `__doc__`), and his one [PREDICT] miss
 (guessing `""` for an absent docstring) bought the absence discriminator:
 collectors hand back empty containers, optional attributes hand back
 `None`.

- **GOVERNANCE: two S21 decisions were settled before any teaching** (first
 cold build block this weekend, Sat 22/Sun 23 Aug; queue tooling as a repo
 script, his call, made after asking what Anki was and choosing the build).
 **Zero pushbacks were raised — the first zero since the denominator rule
 began — and the reading is benign: the protocol held without needing him.**
 Two mentor misses for the record: the TERM-TAX was skipped despite a valid
 later-day gap (owed first in S23), and the lambda teaching turn ran long
 without declaring itself. Interval gate: applied, fifth session running.

### What Session 23 established

**THE HEADLINE IS A MENTOR FINDING, AND IT IS THE SECOND OF ITS KIND.** The
closure definition failed cold for the second session running — 5/10 in S22,
7/10 here — with the *identical* two defects both times: `cell_contents`
called a tuple, and the survival clause missing. Two failures on the same item
with the same shape is a pattern, and the file was about to record it as a
student retention problem. **It is not one.** He asked, unprompted and
honestly, *"I am still unsure what a cell is, is it a memory cell?"* — and he
was right to ask, because it had never been taught. S22 gave him the
four-layer table, the runnable code and the survival clause, but never gave
him **what a cell IS**: that it is a type in its own right (`<class 'cell'>`),
that it is a one-slot box, and that `__closure__` is a *tuple* because there
is **one cell per free variable**. Four labels in a stack with no structure
underneath them is memorisation, and memorisation collapses. **This is the
same discovery as the S20 traceback finding — an item fired repeatedly as a
[RECALL] and logged as a failure when the substrate had never been delivered
— and it is the second time in four sessions.** Pushback 28, upheld. The
correct read of the two prior "failures" is deferred to the S24 re-test: if
the definition holds now, the muddle was never his.

**THE TERM BACKLOG, TWO SESSIONS OVERDUE, WAS CLEARED — AND IT COST THE
SESSION.** Roughly twenty-four rows were fired cold in two waves. Eight
promotions came out of it: truncation (7/10, then 10/10 on the direction
discriminator — `int(-5.98)` → `-5` toward zero, `-5.98 // 1` → `-6` toward
−∞), floor division, alias, rebind, operand, **iterator** (the S22 label slip
did not recur), **pre-order/post-order** (the S22 label gap closed), and the
**modulo identity**. Set against that: two flat gaps (**loop `else`** and
**ternary**, both retrieved as nothing at all), a wrong `sep` default, an
associativity miss, and `pass` given as a *use* rather than a mechanism.
**⚠ The cost is that 1.8 did not open, for the second session running.** That
was defensible once — the backlog was real and the closure gap it exposed was
worth the time — but the arithmetic to 30 September does not survive a third
instance. A recall-budget rule is parked for his decision.

**THE BEST MOMENT OF THE SESSION WAS UNPROMPTED, AND IT WAS A BUG HUNT.**
Having been handed the five checks and a mnemonic, he applied check 4 ("the
value outside what you assumed") to his own lambda `lambda x: x % 10` and
reasoned, cold and in text: *"lets see a case -13%10 lets apply the rule
-2*10 + r = -13 which gives r as 7 this will definitely cause problem."*
Correct — `-13 % 10` is `7`, his sort puts `-13` last as though its final
digit were 7, and **the modulo identity had been sitting in the queue since
S13 as "symbolic form never produced cold."** He produced it without being
asked for it, in service of something else. That is the difference between a
memorised formula and an owned tool, and it is the single strongest piece of
evidence in the session.

**TASK-FIRST RECALL EXPOSED A NEW SHAPE OF GAP: WORKING CODE WITH THE
MECHANISM ABSENT.** This is the inverse of the file's long-standing
"right answer, missing mechanism" watch area, and the drills made it visible
for the first time. He placed docstrings correctly in both functions of
`s23_ordering.py`, unaided, tests green — and then predicted that a string
literal on the *second* line of a body would still show up in `__doc__`. It
returns `None`. **Triple quotes do not make a docstring; POSITION does.**
Same split on lambdas, except that one resolved: he wrote two correct lambdas
before being able to state the auto-return rule, and then produced the rule
when asked. **Lambdas promoted to [x]** on `drills/s23_ordering.py` — 6/6
pytest, cold, first attempt, under a constraint forbidding a third `def`.
Docstrings stay [~], and the split is the reason [~] exists.

**ONE DEMOTION, AND IT WAS THE RIGHT CALL.** The iterator-causation recall ran
bug-first as specified: a two-loop program over a hoisted `iter(range(2))`.
He got the causation — the second loop prints nothing, its body runs zero
times — but could not name `next()`, and guessed **"EndofIterator"** and then
**"EndofIteration"** for `StopIteration`, which had been [x] since S18.
**A failed re-test reverts the item, so `StopIteration` goes back to [~]**
and the iteration protocol is the priority for S24. Consistent with the S12
diagnosis, unchanged: the mechanism survives, the arbitrary label does not.

**TWO NEW WATCH AREAS, BOTH ABOUT HOW HE WORKS RATHER THAN WHAT HE KNOWS.**
(a) **Confidence calibration ran hot** — 8/10 on precedence with associativity
entirely missing, 8/10 on `sep`/`end` with `sep` wrong, and **7/10 on a
closure definition that repeated both of S22's defects.** His ratings have
been accurate enough to use as a *targeting* signal since S17; three
over-ratings in one session is a first, and if it drifts, the rating stops
being usable for setting re-test intervals. Named to him in session.
(b) **Depth-before-answer fired hard.** The five-checks report was requested
**four times**, including once as item 1 at the top of a short message, and
skipped every time in favour of answering the adjacent mechanism question.
He also declared the first drill "works" — *"I have written the code and it
works"* — when it crashed on the very next line. **Running it is part of the
answer, not a formality after it.** Both named directly.

**THE STUDENT'S THREE CHALLENGES, ALL SOUND (running total 28, zero wrong).**
(1) That looking up the `sorted` signature is legitimate and distinct from
being handed the answer — upheld; the signature was given, the worked example
withheld, and the boundary stated out loud. (2) That **unit testing has never
been taught** — partially upheld, and worth recording: `pytest` has been used
as a *harness* since S21 and he only ever runs a command; testing as a subject
is not in Layer 0. He was right to refuse an instruction he had no basis for.
(3) The cell challenge above. **Note the shape of all three: each one was him
refusing to proceed on an unstated foundation, which is the exact behaviour
the define-before-use rule exists to produce and which he now performs
without being invited to.**

**MNEMONIC ADOPTED, AT HIS REQUEST.** He could not name a single one of the
five checks cold — they were taught in S20 and transferred on first use, and
were gone in three days — and rather than accept a re-teach he asked for a
memory hook in the style of the Hindi trigonometry mnemonics. Built with him:
**"Boundary pe khaali ek bahar mila"** → Boundary / Khaali (empty, zero,
nothing) / Ek (one) / Bahar (outside your assumption) / Mila (two things that
must agree). Delivered with the warning that a mnemonic recovers the *list*
and never the *thinking*, and that check 4 in particular cannot be
mechanised. **Check 5 was also generalised beyond recursion for the first
time: "where two things must agree" covers a docstring and its
implementation** — his docstring claimed "last digit" while his code computed
`% 10`, and the two disagree for negatives. Asked which was wrong, he said
both, and that the contract should be stated explicitly. That is an
engineering answer, not a Python one.

### What Session 24 established

**THE SESSION OPENED WITH A GOVERNANCE REFUSAL, AND IT WAS THE RIGHT ONE.**
The interval gate ran first: one day since S23, so cold work was promotable.
The parked rule candidate — *"a [RECALL] block has a budget; state it at the
top and stop when it is spent"* — was put to him twice, and twice he moved past
it: *"lets start with new content now we will do recall later."* **Note what
that is: the rule was proposed because two consecutive sessions let the recall
queue eat the teaching slot, and he settled it by DOING the thing the rule
would have forced rather than by writing the rule.** 1.8 opened as a result,
one session after it slipped. The candidate stays parked; if he declines a
third time, the behaviour has answered it and it should be dropped.
The Saturday 22 Aug cold build block was confirmed in one line, as owed.

**THE MAJOR FINDING IS A MENTOR FINDING, AND IT WAS CAUGHT BY LOOKING RATHER
THAN BY BEING CAUGHT.** Before teaching slicing, the curriculum was searched
for `indexing` — and it returned nothing but `__closure__[0]` in code blocks.
**Indexing had never been formally taught in twenty-three sessions, while
being used since S22.** This is the same class as `traceback` (S20), `list()`
(S15), and slicing itself (S20, pushback 25) — but for the first time it was
found by a pre-emptive check instead of by the student's objection. The
declaration was made out loud before the material opened. **That is the
define-before-building rule finally being self-enforcing rather than
student-enforced, which is what the S18 note asked for.**

**INDEXING, THEN SLICING — AND SLICING IS THE DEBT FROM S20 DISCHARGED.**
Indexing: `[]` takes a position and returns the object there; 0-based; the last
valid index is `len - 1`; negatives count back from the end; out of range
raises `IndexError`. **A precision fix was issued and it matters for
interviews:** he said *"the length is `len(list) - 1`"*. The length is the
count; `len - 1` is the last INDEX. Slicing then followed: `[start:stop:step]`,
**half-open exactly like `range()`**, which he already owns — omitted ends,
negative step, `l[:]` as the copy idiom, and the same operator on `str`, which
retro-explains the `word[:-1]` he was given as a bare minimum in S20.

**THE BEST MOMENT OF THE SESSION WAS UNPROMPTED DEPTH.** Asked whether
`tools[1:3]` returns an item or a list, he answered *"it returns a new list —
oh that means it creates a new list object"* and went a level past the
question on his own. **That is the probing pass the depth-before-answer rule
exists to force, running without the rule.** It was cashed in immediately:
`b = tools` versus `c = tools[:]`, `append` on `b`, and the observation that
`tools is b` is `True` while `tools is c` is `False`. His explanation used
`alias`, `object` and `mutate` correctly and closed with **"I didn't see
rebinding here"** — separating mutation from rebinding cold, unasked, on a
later day. Both `alias` and `rebind` re-passed on that alone.

**THE ROSTER VOLLEY, AND THE CORRECTION IT PRODUCED.** Six list methods —
`append`, `extend`, `insert`, `sort`, `remove`, `pop` — were fired for
name-decoding: does it change the list, and what does the call evaluate to?
He got three. He believed `extend` builds a new list ("append already adds
elements, so extend must do something different") and that `sort` *"returns a
new list object for sure"*. All six mutate; five return `None`; **`pop`
returns the removed item.** Asked what that does to the tell he was using, he
answered *"mutating methods usually return None, which is correct to an
extent"* — and the sharpening is the session's real yield:

> **The S17 tell runs ONE WAY ONLY. Returns `None` ⇒ mutating (returning
> `None` has no other purpose). Mutating ⇒ returns `None` is FALSE, and `pop`
> is the counterexample. TYPE first, return value as a one-directional hint,
> never as a biconditional.**

**He had been reading a one-directional heuristic as an equivalence, and that
is precisely the shape of error the depth doctrine's "give the discriminator,
not the roster" policy is exposed to.** The roster was then owned by running
it, not by being handed a table.

**A MENTOR TAGGING ERROR, DECLARED IN SESSION AND NOT BACK-DATED.** The volley
was tagged [PREDICT] on the grounds that the methods were unseen — but `sort`
was taught in **S17** as half of the `sort`/`sorted` pair, so that line was
[RECALL] and his inversion of it was a genuine retention miss. **Because
[PREDICT] had been declared before the questions, the miss was NOT entered in
the ledger** — booking a PREDICT miss as a RECALL miss is exactly what S16
rule 1 forbids, and the prohibition does not bend just because the miss is
real. It went to the re-test list for a clean cold pass instead. **The S18
principle — an unseen method on a taught type tests the discriminator — is
sound, but it does not license sweeping a TAUGHT method into the same block.**

**THE FIVE CHECKS: THE MNEMONIC WORKED, AND THIS IS THE FINDING TO CARRY.**
In S23 he could not name one of the five checks cold, three days after they had
been taught and successfully transferred; a hook was built with him,
**"Boundary pe khaali ek bahar mila."** Fired cold in S24 he returned
**four of five with correct content** — boundary conditions, empty/zero/None,
the smallest non-empty case, and the value outside the assumption — and
self-rated **5/10, which was well calibrated** (*"I still need to learn to
apply it"*). **`Mila` was the miss**, glossed as "similar inputs". It was
re-taught, generalised past recursion, and given in both languages: **`mila`
holds the PROMISE (docstring/spec) against the CODE, one sentence at a time —
"iske peeche kaunsi line hai?"** ⚠ **The decisive detail: he had already
PERFORMED `mila` correctly minutes earlier without recognising it**, ruling the
`IndexError` on `take_last([])` NOT a bug because the spec says the list may be
assumed non-empty. **Naming the move he had already made is what landed it,
and that is a better teaching instrument than another definition.**

**THE DRILL — `drills/s24_lists.py`, 11/11.** Four functions specified purely
by what the CALLER must be able to observe, with no mechanism named, so that
choosing between mutating and non-mutating WAS the exercise: return a sorted
copy leaving the caller's list intact; sort the caller's own list and evaluate
to nothing usable; remove the last item and hand it back; and return the last
three values without raising for any length including zero. **Three of four
were right first time**, and `last_three` handled the empty and short cases
correctly **by construction, before he had been told that slices never raise**
— the "right answer, mechanism absent" pattern in its benign direction.
The failure was `return readings[:].sort()`: the slice copy was the correct
instinct and the bug sat downstream of it. Pointed at the one line, he fixed it
by separating the mutation from the return.

**THE FIRST NON-UPHELD PUSHBACK IN THE FILE'S HISTORY.** Re-asked what
`.sort()` evaluates to, he challenged the question itself: *"isn't the
corrected code a proof of my understanding?"* **It is a reasonable claim and it
was answered with reasoning rather than authority:** the fix followed a
pointer, so it is guided rather than unaided, and his own S23 record contains
two cases of correct code with the mechanism absent — docstrings placed
perfectly with no idea why, lambdas written before the auto-return rule was
known. **For this student, on this evidence, "it works" has already been shown
not to imply "I know why."** He accepted it and then answered the question
correctly in one line. Running total: **31 raised, 30 upheld or part-upheld,
one not upheld.** The other two: **the `last_three` docstring was ambiguous —
UPHELD, a mentor error** (it said "oldest of the three", importing a time
ordering that was nowhere in the spec; corrected in chat rather than in the
file, since the drill file was his); and **"shouldn't I just write the relevant
cases?"** on the five-checks report — **PARTIALLY UPHELD**, resolved as
**SCAN all five, REPORT only the ones that bite**, with the reason stated:
pre-filtering by "relevant" applies the same assumption that produced the bug,
which is exactly how his S20 `n <= 10` boundary looked irrelevant until it was
the bug.

**DEPTH-BEFORE-ANSWER FIRED TWICE, AND BOTH RECOVERIES TOOK ONE LINE.** Asked
to mark his own six roster answers, he restated the output instead; asked what
`.sort()` evaluates to, he fixed the code instead. **Both times the re-ask
produced a correct, complete mechanism immediately.** That is the S20
`digit_sum` shape exactly — he has it and skips it — and it confirms the
intervention: **re-ask, do not re-teach.**

**CONFIDENCE CALIBRATION: MIXED, SO S23's THREE OVER-RATINGS ARE NOT YET A
DRIFT.** One hot reading (*"for sure"* attached to a wrong answer about `sort`)
against one well-calibrated (5/10 on a 4/5 answer, with an accurate reason for
the number). Keep watching; do not yet discount the rating as a targeting
signal.

**ZERO PROMOTIONS, AND THAT IS THE CORRECT OUTCOME.** Everything taught in S24
was same-session. The two items that held on later-day evidence — aliasing and
rebinding-vs-mutation — were already [x] and simply re-passed. **1.8's list
bullet moves [ ] → [~]; nothing moves to [x].** The recall queue was untouched
at his request and carries forward intact, and he asked for it first next
session in his own words.

### What Session 25 established

**Friday 21 Aug 2026. One day after S24. Interval gate applied at the open for
the eighth session running, and it opened clean: a real overnight gap, so
everything produced cold today was promotable. He confirmed the gap himself.**

**THE SHAPE OF THE SESSION.** He had asked at the S24 close, in his own words —
*"tomorrow we will do the recall first"* — and the whole session honoured that.
No new curriculum subsection was opened. **The recall backlog had been carried
untouched for two sessions and was the largest single debt in the file; S25
cleared it entirely.** ELEVEN items promoted on cold later-day evidence, which
is the highest count any session in this file has produced.

**CLOSURES FELL, AND THE S23 DIAGNOSIS IS VINDICATED.** The definition had
failed twice — S22 at 5/10 and S23 at 7/10, with the *identical* two defects
both times: the survival clause dropped and `cell_contents` miscalled a tuple.
S23 located the root cause and placed it MENTOR-SIDE: cells had been taught as
a stack of labels, never as a TYPE. **S25 tested the prediction and it held.**
Cold, unprompted, he produced free variables, cells, the tuple, the attribute on
the function object, *and* the survival clause — *"can be accessed even after
the enclosing function frame has come to an end."* **The muddle was never his,
and that is now evidence rather than a hypothesis.**
⚠ **ONE IMPRECISION CORRECTED, and it is the standard one:** he opened with
*"when we define a function inside another function."* A [PREDICT] on
`inner.__closure__` being `None` for a non-capturing nested function broke it in
one step. **The corrected line: nesting is necessary but NOT sufficient — the
capture of a free variable is what makes the closure.**

**THE APPLICATION HALF, WHICH HAD BEEN OWED SINCE S23, WAS DISCHARGED IN ONE
PASS.** `drills/s25_closure.py` — a symmetric joint-limit clamp under four
forcing constraints (one-argument tool, no `global`, maker must have returned,
two clamps alive simultaneously) — **10/10 pytest, unaided, ZERO guided debug
cycles.** S23's closure build had needed three. Two details worth keeping: he
collapsed both directions into `abs(given_value) > limit` rather than writing a
symmetric if/else, and he used `>` not `>=`, so the boundary test at exactly
`90` passed. **Boundary-first, applied without being told — the S20 rule 3(c)
habit is taking.**

**THE ITERATION PROTOCOL RETURNED IN FULL, AND IT UNBLOCKS COMPREHENSIONS.**
S23 had demoted it: he kept the causation but lost both names, producing
"EndofIteration". `drills/s25_iteration.py` banned `for`, `while`, indexing,
slicing, `.pop()`, `.remove()`, `.index()` and `enumerate`, with the ban
enforced by a test that greps the source — leaving exactly one way to get an
item out of a list. **He named `iter()` and `next()` cold and unprompted, 8/10.
`StopIteration` came back with its exact spelling, 7/10.** 7/7 on the drill.
⚠ **The gate this opens should be declared out loud in S26: comprehensions were
blocked on this item being [~], and it is now [x].**

**⚠ THE DEMOTION IS THE MOST IMPORTANT FINDING IN THE SESSION.** Asked for
`associativity` **alone** — as STATE.md explicitly instructed, because every
previous attempt had drifted into precedence — he answered **"gap"**. A flat
empty. **It had been sitting at [x] since S16.** The reason it survived nine
sessions undetected: the S16 tick reads *"[x] Operator precedence / [x]
Associativity — PROMOTED S16"*, one bullet, two items, promoted together and
never asked separately. **A bundled tick can conceal a completely empty item
indefinitely.** Demoted to [~], re-taught with `10 - 3 - 2` against
`2 ** 3 ** 2`, and a new gauntlet action recorded: **audit every [x] that shares
a bullet with another item and re-ask each half separately.** This is precisely
what the strict legend exists for, and it is the first time the file has caught
a false [x] by instrument rather than by accident.

**THE HOOK TECHNIQUE IS NOW CONFIRMED RATHER THAN PROMISING.** S24 recorded the
first evidence: the mnemonic *"Boundary pe khaali ek bahar mila"*, built in S23,
returned 4/5 cold after the same material had been a flat gap. **S25 took it to
5/5 — and the recovered item was `mila`, the one he had glossed wrongly as
"similar inputs" in S24.** Two precisions were issued on the way through
(`ek` = exactly ONE, not "small inputs"; `bahar` = outside what you assumed,
covering TYPE as well as sign). **THE FIVE CHECKS → [x].**
**On that evidence, the three remaining flat gaps were given hooks instead of
another explanation:**
- **`pass` = jagah bharo / `continue` = agla chakkar / `break` = bahar niklo.**
  Gated first on the `IndentationError` that proves a block cannot be empty,
  then taught as one loop written three times with one word changed.
  **The reason this one needs a hook: the name decodes to the WRONG keyword —
  "pass" sounds like "skip it", which is `continue`'s job.**
- **loop `else` = read the keyword as `nobreak`.** He then predicted the
  empty-iterable case correctly on the hook's first use, with the right reason.
- **ternary = `ter-` is THREE** — value, condition, value, middle is the
  condition. Taught with the placement motivation (an `if` block cannot go
  inside a `+`) rather than brevity. **S26 is the experiment that tests all
  four cold.**
⚠ **A MENTOR CATCH WORTH RECORDING: the first draft of the ternary demo used a
LIST COMPREHENSION and a bool-as-index trick, neither of which has been taught.
Caught before it was shown.** Substrate define-before-building, self-enforced.

**DEPTH-BEFORE-ANSWER FIRED THREE TIMES; ALL THREE RECOVERED IN ONE LINE.**
(a) Asked what Python does with a non-first string literal, he said "considers
it as a comment" — wrong, and repaired completely on a single probe (`is 5 a
comment?`) into *"an object will be created for it, occupying memory, but will
not be used anywhere"*. (b) He gave the one-directional tell without the
counterexample; re-asked, `pop` came instantly. (c) He answered `sep` and `end`
but skipped what `print()` evaluates to; re-asked, `None`. **Across S24–S25 the
re-ask has now worked six times out of six. The knowledge is not the bottleneck;
the first-answer habit is. RE-ASK, DO NOT RE-TEACH.**

**THREE PUSHBACKS, ALL UPHELD OR PART-UPHELD — RECORD NOW 34 RAISED / 33.**
- **(32) THE DRILL SPEC WAS UNINTELLIGIBLE — UPHELD, MENTOR ERROR, AND IT IS THE
  SECOND CONSECUTIVE SESSION.** He stopped before writing a line: *"I am unable
  to understand this instruction, again, this has been happening to me a lot
  lately, is this my problem?"* **It was not.** The sentence contained "oldest
  order preserved" (meaningless — copied from a time-ordered drill), "a NEW list
  of the same angles, each pulled inside the limit" (self-contradictory), and
  four requirements welded into one sentence, inside a file written to test him.
  **S24's `last_three` spec failed the same way.** Rewriting item 5 as lettered
  sub-requirements, one per line, fixed it immediately and he built the drill
  10/10. **STANDING FIX: drill specs are written as (a)/(b)/(c), never prose.**
  ⚠ **His question deserves its answer recorded: his record is 34 challenges
  raised and 33 upheld. Spotting an ambiguous spec IS the engineering skill;
  the failure mode would be building the wrong thing silently.**
- **(33) HE REFUSED A TEACH-BACK AS ECHO — UPHELD.** Offered the corrected
  closure line and asked to say it back, he declined: *"saying the line will be
  just copying, so not worth saying, will definitely give the whole thing in
  cold recall."* **That is the Session 15 confidence rule and the Term Retention
  System's own same-day caveat, applied to the mentor by the student. Eighth
  instance of him owning the learning system itself.**
- **(34) `list()` — PART-UPHELD, AND THE UPHELD HALF IS A BOOKKEEPING FAILURE.**
  Needing `list()` to drain a partially-consumed iterator, he opened his S15
  notes, **said so unprompted**, and asked whether expecting recall after that
  gap was fair. **NOT upheld:** "it was long ago" is no defence in a course built
  to survive exactly that gap. **UPHELD:** `list()` was defined in S15 *as a
  patch to a breach he himself caught*, and was then **never entered in the
  re-test queue, never drilled, and never re-tested across nine sessions**. The
  system had not once asked him for it. Added to the queue in-session.
  ⚠ **He could have stayed silent and taken a clean 7/7. Third time he has
  protected the accuracy of his own ledger at his own expense.**

**JUMP-AHEAD: COUNTER-EVIDENCE, NOT AN INSTANCE.** Mid-session he proposed
extending the clamp with `*args`/`**kwargs` for multiple named joints. **That is
[x] material from S22, so it is application appetite rather than scope creep** —
and it was redirected, not refused, into the Saturday 22 Aug cold build block,
which RULES already names "joint-limit clamp with tests". **One design hole was
named and deliberately left unanswered: `*args` delivers angles positionally and
anonymously while `**kwargs` delivers limits by name, and nothing pairs them.**
S17's instruction — read his enthusiasm as fuel and spend it — worked exactly as
written.

**CONFIDENCE CALIBRATION IS IMPROVING AND S24's HOT READING NOW LOOKS LIKE
NOISE.** Every S25 rating (7, 8, 6, 4/5, 8, 8, 8) sat on a correct answer, none
inflated, and the lowest — 6/10 on docstrings — correctly identified the weakest
of the set. **Contrast S24's *"returns a new list object for sure"* attached to
a wrong answer about `sort`. The rating stays usable as a targeting signal.**
The `sort`/`sorted` inversion itself was cleared: all four printed values right,
cold, 8/10.

**HONEST GAPS: TWO, BOTH DECLARED RATHER THAN GUESSED** — `pass` and
associativity. **In a session that promoted eleven items, the two refusals to
guess are worth as much as the promotions**, because they are what makes the
other numbers trustworthy.

**TEACHING MISTAKES THIS SESSION.**
1. **The `clamp_all` spec — pushback 32 above. Second consecutive session of
   ambiguous drill prose. Now a standing format rule: lettered sub-requirements.**
2. **`list()` was never queued after S15 — pushback 34. A term defined as a
   breach patch was left out of the very system built to carry it.** Any term
   defined mid-session must be entered into the queue in the same session.
3. **A list comprehension and a bool-as-index trick reached the first draft of
   the ternary demo, neither taught.** Caught before delivery — but the draft
   should not have contained them.
4. **The parked "[RECALL] budget" rule was offered a third time** despite
   STATE.md saying "do not nag a third time" alongside "offer it once more".
   The instruction was self-contradictory; it has now been DROPPED and the
   record closed, settled by behaviour rather than by ruling.

**WHAT HE ASKED FOR AT THE CLOSE, VERBATIM:** *"close this session here but next
session should start without recall actually studying 1.8 further."* **S26 opens
on 1.8 content — tuple, dict, set — and the four hooked items are fired later in
the session, not at the open.**

---

### What Session 26 established

**Friday 21 Aug 2026. THE SAME DAY AS S25, and that fact governs everything
below: ZERO PROMOTIONS, and zero is the correct number.** The interval gate was
applied unprompted as the first action — ninth consecutive session — and it did
real work this time rather than merely passing: **the four hook tests built in
S25 (`pass`, loop `else`, ternary, associativity) were DEFERRED rather than
fired.** Running them hours after the hooks were taught would have measured echo
and written it into the ledger as retention. **That is precisely the failure
mode that produced the false associativity [x] in S16, discovered nine sessions
later.** The hooks stay untested until a later day. **S27 is their first
legitimate test.**

**HIS S25 CLOSING INSTRUCTION WAS HONOURED EXACTLY:** *"next session should
start without recall, actually studying 1.8 further."* The session opened on
content, and no recall block was run at any point. **Second consecutive session
shaped by his own instruction — S25 all recall at his request, S26 all content
at his request — and both times the instruction was followed rather than
negotiated.**

**THE CURRICULUM MOVED, WHICH IT HAD NOT DONE MEANINGFULLY SINCE S24.** 1.8 went
from ~15% to ~40%: **tuple taught in full, dict taught to roughly two-thirds.**

**TUPLE, IN FULL.** Opened not from the definition but from the failure it
prevents — the S24-era aliasing bug, a function "helpfully" appending to a list
its caller owns. **He produced the entire causal chain cold and unprompted:
parameter/argument → alias → mutable object → mutating method.** From there:
immutability as a guarantee; **`TypeError` on item assignment versus
`AttributeError` on `.append`, and the point that immutability has no error of
its own — it arrives as `TypeError`**; `+` building a new tuple; **THE COMMA
MAKES THE TUPLE, NOT THE PARENTHESES** (`(5)` is an `int`); unpacking, and count
mismatch raising **`ValueError`** because the type is fine and the count is not;
and **a function never returning more than one object — `return a, b` builds one
tuple, so "multiple return values" is tuples wearing a costume.**

⚠ **THE BEST MOMENT OF THE SESSION IS THE METHOD ROSTER, AND IT VALIDATES THE
S17 DEPTH-DOCTRINE DECISION NOT TO GIVE HIM A ROSTER TO MEMORISE.** Asked which
of the six list methods a tuple could possibly have, he reasoned entirely from
the type and got all six right — **and went further than the question, observing
that a new-object `append` COULD exist in principle.** That is correct, and the
reason it does not exist is a design answer rather than a memory one: **that
version already exists and is spelled `+`; naming it `append` would be a lie,
because `append` promises in-place.** He was then given the derivable rule — **an
immutable type can only carry methods that REPORT** — and the actual two-method
roster (`count`, `index`) as a consequence rather than a fact. **This is the
S17 discriminator paying off four months later: he did not recall the answer, he
computed it.**

**SHALLOW IMMUTABILITY, STATED BEFORE IT WAS ASKED FOR.** Given
`config = ("arm", [10.0, 20.0])` and `config[1].append(30.0)`, he answered:
*"tuple is itself immutable, but the object inside if it's a mutable it should
be mutated."* Correct, unprompted, and it carried the model with it. The mentor
formalised it: **a tuple stores REFERENCES; immutable means the references
cannot be re-pointed, and says nothing about the objects they point at.**

**THAT SENTENCE, ONE LEVEL DOWN, DISCHARGES THE S24 PARK.** He had described
`tools[:]` as *"an identical new list object"* — true of the outer list, and it
hides the trap. Given nested lists and two mutations at different levels he
**predicted both output lines wrong**, treating the slice as a deep copy. Tagged
[PREDICT], so nothing ledgered, and it is the single most valuable wrong answer
of the session. **SHALLOW COPY was then defined with a reference diagram: the
container is new, the references inside are copied, so nested mutables are
SHARED — and the trap can only fire when the container holds mutables.**
`copy.deepcopy` remains owed, parked to nested data structures.

**DICT, MOTIVATED FROM ITS ALTERNATIVE — which is the S18 finding about him
applied deliberately.** He presses *"why does this exist rather than the obvious
thing?"*, so dict was opened on parallel lists doing the same job. **He found
both defects unaided:** that nothing in the language enforces the pairing, so
the lists can drift apart; and that `.index()` must walk the list, **naming the
cost as LINEAR himself** and correctly identifying it as DSA territory (master
Layer 8). Then: key→value; `[]` taking a key; **keys unique, and derivable —
`[]` must return one value**; existing key overwrites and new key inserts;
`KeyError`; `in` testing keys; `.get()`; iteration giving keys; and **`.items()`
revealed as tuple unpacking in disguise**, which closed the loop back to the
first half of the session.

⚠ **HE REASONED OUT HASHABILITY FROM FIRST PRINCIPLES, WHICH WAS NOT EXPECTED.**
Asked why a list cannot be a dict key, he worked through it aloud — *"if its
mutable someone change the key, the value for that pair lost... but what if
someone make it same to other keys, then value collision"* — and arrived at
**"it needs to be immutable"** by himself. The mechanism was then supplied: the
dict computes a number from the key to jump straight to a slot, that number must
stay stable, so the key's contents must never change. **One claim of his was
corrected, and he had flagged the doubt himself mid-sentence (*"what am I
saying, is that correct??"*): immutability does NOT imply uniqueness — `(1,2)`
and `(1,2)` are equal and are the SAME key.** This also delivered the fourth
tuple-over-list reason, which had been promised and deferred earlier in the
session.

**`.get()` WAS TAUGHT AS A DESIGN TRAP RATHER THAN A CONVENIENCE**, and the
design half came back correct on the re-ask: **"silent failures."** The rule
recorded: `[]` when a missing key is a BUG, `.get()` when absence is EXPECTED
and there is a real default; **`.get()` with no default is the dangerous middle,
because it does not prevent the crash — it MOVES it away from the cause.** Same
principle as the tuple safety-limit example: **loud failure at the cause beats a
silent wrong value far away.** That principle now appears in two independent
places in one session and should be treated as a spine of 1.8.

---

**TEACHING MISTAKES THIS SESSION — AND THIS IS THE SESSION'S REAL FINDING.**
**FOUR DEFECTIVE ASKS IN ONE SESSION. Spec-writing is now the mentor watch area
for the THIRD CONSECUTIVE SESSION and S26 was the worst instance yet.**

1. **`sum()` was used in the opening example having never been defined. NINTH
   substrate define-before-building breach.** Found by the mentor grepping the
   repo rather than assuming — the rule working — but it should never have
   reached the example. Defined in-session.
2. **`KeyError` was demanded by name having NEVER appeared once in the entire
   course**, verified by grep across all four files and every note. **A straight
   define-before-use breach, and the fourth time an error label has been asked
   for before being given.** His `ValueError` guess was reasonable from what he
   had been taught; nothing logged.
3. **Dict-key uniqueness was never stated before a [PREDICT] depended on it.**
   Part-upheld — it *is* derivable, but the derivation should have been flagged
   rather than slid past.
4. **"Given you have `[]`"**, meaning the bracket operator, was read as *"you
   have a list"* and sent him to a wrong answer built on two parallel lists —
   **the very design the dict had just replaced.** Ambiguous notation in an ask.
5. **The linear-cost question was unanswerable as worded.** He said so plainly:
   *"I don't understand both the questions actually what you are trying to get
   out of me."* Restated as *"does it jump straight there or check one at a
   time, and how many comparisons if the match is last?"* — **answered correctly
   and immediately.** The question was the defect, not the student.

⚠ **AND THEN THE STRUCTURAL ONE, WHICH HE RAISED HIMSELF AND WHICH MATTERS MORE
THAN THE FOUR ABOVE.** *"I think all your questions are looking to me like you
are asking things without teaching, it's daunting — is it my fault of thinking
or your fault, lets clarify this first."* **Audited honestly and MOSTLY UPHELD:**

- **DENSITY.** Almost every turn was a question. The correct ratio is *teach a
  piece with code and output → ask ONE question on it.* The session ran
  predict → predict → predict with almost no exposition between.
- **The four defective asks meant a real share of the difficulty was
  unanswerable questions rather than hard material.**
- **THE TAG WAS DECLARED BUT ITS MEANING WAS NOT.** Some [PREDICT]s are
  derivable from what is on screen; others are genuine guesses where being wrong
  is the point. **From the student's side those are indistinguishable, and they
  must not be. This is the S18 rule-1 finding recurring one level up: if the
  student cannot tell one instrument from another, the instrument is not being
  declared clearly enough.**
- **NOT upheld:** [PREDICT] asking before teaching is the instrument working as
  designed, and is never ledgered in either direction.

**TWO STANDING FIXES COMMITTED TO HIM AND WRITTEN INTO STATE.md: (a) teach the
piece WITH CODE AND OUTPUT first, then ask ONE question on it; (b) every
[PREDICT] declares up front whether it is "derivable from what's on screen" or
"a genuine guess — wrong is fine and expected."**

**THE SECOND FINDING REPRODUCES S25's HOOK RESULT FROM THE OTHER SIDE.** He
asked mid-session for a consolidated explanation of every error met so far, in
Hindi, *"with the hook so I can recall everything fresh"* — **note that he asked
for a hook by name; the technique has been internalised.** It was delivered as
twelve errors in four families with real generated output, and a **decision
TABLE** at the end. **Twenty minutes later he mislabelled `AttributeError` as
`TypeError`, and diagnosed the cause himself: *"maybe its not sticking in my
mind."* He was right, and the cause was the table.** RULES has known since S25
that arbitrary labels need HOOKS rather than explanations, **and a table is an
explanation.** It was rebuilt as:

> **NAAM → DOT → TYPE → CHEEZ** — four stations; wherever the train stops, that
> is the error. **Station 4 splits three ways: jagah = `IndexError`, chaabi =
> `KeyError`, cheez khud = `ValueError`.**

**He then specified his own retention protocol for it**, unprompted: *"in order
to stick it you need to ask me again and again, different error — when using
regularly it will definitely stick."* **That is spaced retrieval, requested by
name, and it is parked as the single rule candidate for S27's ruling.**

---

**PUSHBACKS: FOUR RAISED, ALL UPHELD OR PART-UPHELD. RUNNING TOTAL 38 RAISED,
37 UPHELD.**

- **(35) The linear-cost ask was unintelligible — UPHELD**, mentor wording.
  Restated, answered immediately and correctly.
- **(36) *"you didn't tell me if one dictionary can have two same keys; and you
  are straight asking the questions, that's not fair"* — UPHELD.** Auditing his
  challenge turned up a second, larger defect he had not named: **`KeyError` had
  never appeared anywhere in the course.** ⚠ **He challenged the fairness of one
  question and the audit found a nine-session-scale bookkeeping hole — the same
  shape as pushback 34's `list()` finding in S25.**
- **(37) *"your question was not properly asked, I thought you said you have
  `[]` list"* — UPHELD**, ambiguous notation.
- **(38) *"is it my fault of thinking or your fault, lets clarify this first"* —
  PART-UPHELD.** ⚠ **NOTE THE SHAPE OF THIS ONE. It is not a complaint about
  difficulty. It is a request for a DIAGNOSIS, offered with his own fault as the
  first hypothesis, and with the explicit instruction to settle the attribution
  before continuing. That is the ninth instance of him auditing the teaching
  system itself, and the first time he has asked for an attribution to be
  DECIDED rather than asserting it.** The honest split was given: mostly mine.

**HONEST GAPS: THREE, ALL DECLARED RATHER THAN GUESSED** — *"I don't know"* on
the unpacking mismatch, *"I don't get the second question"* on what a tuple
buys, and the self-flagged *"what am I saying, is that correct??"* on his own
uniqueness claim. **The third is the most valuable: he interrupted his own
correct-sounding sentence to mark the part he was unsure of.**

**DEPTH-BEFORE-ANSWER fired twice and BOTH re-asks recovered.** The `.get()`
design half came back in one line. **Seven successful re-asks across S24–S26
with zero failures. The re-ask IS the intervention — do not re-teach, re-ask.**

**CONFIDENCE CALIBRATION: NO DATA, CORRECTLY.** Every block was [PREDICT] or
[TEACH-BACK], neither of which carries a rating, and the session was same-day.
**Do not read the absence as regression.**

⚠ **WHAT WAS NOT DONE, AND IT IS THE SESSION'S DEBT: NO DRILL FILE WAS WRITTEN.**
S26 ran entirely on live code and prediction. **Nothing taught today can promote
until it is drilled task-first.** Also still owed inside 1.8: dict deletion and
ordering, `set`, when-to-use-which, comprehensions (**gate open since S25 and
still not opened**), `zip`, f-strings (**he uses them correctly and cannot yet
explain them**), nested structures, `reversed()`.

**HE ENDED THE SESSION HIMSELF:** *"I guess lets close the teaching for today, I
have done more than enough for the day"* — **called immediately after the
attribution question was settled, which reads as calibration rather than
avoidance. Session length is his call (S18 rule 2); it was honoured without
argument and the closing procedure ran unasked.**

---

### What Session 27 established
**Saturday 22 August 2026. A LATER-DAY session after S26 — the first legitimate
cold block in three sittings, and the largest promotion haul since S25.**

**THE HEADLINE: THE WEAKEST CLUSTER IN THIS FILE SINCE S23 HAS CLEARED, AND IT
CLEARED IN A SINGLE DRILL FILE.** `break`, `continue`, `pass`, loop `else` and
the ternary — five items that between them had produced three flat "gap"
answers across S23 and S25 — were all produced cold, unaided, one day after the
hooks were built. **`drills/s27_flow.py`, five functions under lettered
constraints, 20/20 pytest.** This is also the drill file S26 owed and did not
write, so it retroactively unblocks nothing from S26 and everything from S25.

**READ THE CAUSE CORRECTLY: it was the HOOKS, not the explanations.** All five
had been explained repeatedly before S25 and all five failed. They were
re-taught in S25 with mnemonics (*jagah bharo / agla chakkar / bahar niklo*;
loop `else` read as `nobreak`; `ter-` = three) and one day later he produced the
MECHANISMS, not the mnemonics — which is what a working hook looks like.

**THE DRILL DESIGN IS WORTH REUSING.** Each function carried lettered
sub-requirements that made the target mechanism NECESSARY rather than merely
possible: one-`return`-as-the-last-line forced `break`; an `if` with no `else`
plus the adding line outside it forced `continue`; "the printing line runs only
when the loop reaches its natural end" plus "no `if` after the loop" forced loop
`else`; a single-line `return` forced the ternary; a one-line body that is not a
return, a string or an assignment forced `pass`. **pytest decided behaviour; the
constraints were checked by reading his code.** He met four of five cleanly.

**THE `find_index` REWRITE IS THE BEST TEACHING MOMENT OF THE SESSION.** His
first version looped over ITEMS, broke on a match, then recovered the position
with `values.index(i)` and guarded it with a ternary — passing all 20 tests. He
was pointed at ONE line and asked what the loop's first line would become if it
walked positions; he answered "range", rewrote it himself, and the ternary
became unnecessary. **The rewrite silently killed a bug neither of us had
tested: `find_index([None, 5], None)` returned `None` instead of `0`, because
`None` was serving as both "the thing I found" and "I found nothing". That is a
five-checks `bahar` miss BY TYPE, and he did not catch it on his own pass.**

**PROMOTIONS — EIGHT, ALL COLD, ALL LATER-DAY, ALL RATED:**
`break`, `continue`, `pass` (8/10) · loop `else` (8/10) · ternary (8/10) ·
**associativity, RE-PROMOTED after its S25 demotion and asked ALONE (7/10)** ·
**precedence, tested separately for the first time (7/10)** · **`traceback`,
[~] as "cued only" since S23 (8/10)** · **keyword argument, defined S21 and
NEVER tested until now (7/10)**.

⚠ **THE FIRST REFUSED BUNDLE IN THE HISTORY OF THIS FILE.** `break` and
`continue` both passed, but the CURRICULUM bullet that carries them is
*"`while` loops — break, continue"* and `while` mechanics were not tested. **The
items were promoted; the bullet was left [~].** This is exactly the audit the
August gauntlet exists to perform, executed in advance rather than in arrears.

**EXPRESSION vs STATEMENT — CLOSED, OWED SINCE S14.** The expression half had
been carried alone for thirteen sessions. It closed off the back of his own
ternary answer: asked what a ternary can do that a four-line `if`/`else` cannot,
he said *"can return a value"*, and on the depth re-ask produced
`print("high" if n>10 else "low")` with *"we can't put an if else block inside a
print"*. **He had produced the TEST before it was named.** The statement half was
then delivered against `print(if n > 10: "high")` ⇒ `SyntaxError`, proved by the
output rather than asserted — **`n = 12` on line 1 never ran and line 3 never
printed.** Applied immediately: `d[k] = v` and `del d[k]` are STATEMENTS.

**THE RULE ADOPTED — AND IT IS A FIRST.** *"Every snippet that raises gets its
error NAMED by the student before the mentor shows it."* **He proposed it in S26
and ruled on it himself at the S27 open** — the first rule in this file both
raised and decided by the student. RULES.md is now v3. **It paid for itself on
first use, through a MISS:** he labelled the `SyntaxError` snippet as
`TypeError`, and that miss exposed a hole in the four-station hook that no
amount of re-explaining the error table would have found.

⚠ **THE FOUR-STATION HOOK GAINED A STATION 0: "DID IT RUN AT ALL?"** If Python
could not read the sentence, nothing executes ⇒ `SyntaxError`. Only a RUNNING
program can reach NAAM → DOT → TYPE → CHEEZ. Re-tested immediately on `"5" + 3`
versus `5 +` — both correct with full mechanism.

**THE HOOK EXPERIMENT ITSELF: RUN, AND MIXED, WHICH IS THE USEFUL RESULT.**
Fired cold on three dict snippets: `robot.append(5)` → `AttributeError`, HIT;
`robot["speed"]` → he said `IndexError`, it is `KeyError`, **THE ONE MISS OF THE
SESSION**; `rbot["joint"]` → *"actually I don't remember this"*, honest gap, it
is `NameError`. **The diagnosis: he read the `[ ]` and reached for Index. The
correction taught — the brackets are IDENTICAL on a list and a dict; what goes
INSIDE them decides.** And `rbot["joint"]` is why the stations are an ORDER and
not a menu: bad name AND brackets, and Python never reached the brackets.

**THE SHARPEST DISCRIMINATION OF THE SESSION CAME LATER, ON SETS.** `b[0]` on a
dict is `KeyError` — Python PERFORMED the lookup and the chaabi was absent
(station 4). `seen[0]` on a set is `TypeError: 'set' object is not
subscriptable` — the operation does not exist for the type and no attempt was
possible (station 3). **The test given: could Python even ATTEMPT it?**

**DICT FINISHED.** Deletion three ways, and the difference is what you get back:
`del d[k]` is a statement and hands back nothing; `d.pop(k)` hands back the
VALUE — **the returns-`None` counterexample now seen on a SECOND type**;
`d.clear()` returns `None` and leaves `{}`, **empty but not gone, same object**.
`del` on a missing key ⇒ `KeyError`, **which he named cold and correctly forty
minutes after mislabelling it**. Insertion ordering: keys hold their
FIRST-insertion position; **overwriting a value does not move the key**;
delete-then-re-add does, **which he predicted correctly from the rule**. Taught
with the warning that **ordered is not sorted**.

⚠ **A FULL DICT METHOD TABLE WAS DELIVERED AT HIS REQUEST, AGAINST THE S17
NO-ROSTER DOCTRINE — AND THE WAY IT WAS DELIVERED IS THE PRECEDENT.** It was
prefaced with the S26 finding (a delivered table failed inside twenty minutes),
framed as a reference sheet rather than a memorisation task, and **paired with
the discriminator rather than offered instead of it.** He then raised the fear
himself — *"I still fear I am going to forget these methods, is that fair??"* —
and was answered plainly: **yes you will forget the names, and no, that is not
what to protect. The model is three ideas (is the type mutable / does it return
`None` / raising form or shrugging form) and the roster is lookup-able.** Tenth
instance of him auditing the learning system itself.

**SET TAUGHT IN FULL**, motivated as **"a dict with the values thrown away"** —
same braces, same hashing, same uniqueness rule, **therefore set items must be
hashable for exactly the reason dict keys must be.** Five items in, three out:
**duplicates are absorbed SILENTLY**. `{}` is an empty DICT; **the only way to
write an empty set is `set()`**. `add` returns `None`; **`remove` raises,
`discard` shrugs**, and the label is `KeyError` because **a set item IS its own
chaabi**. `sorted(s)` returns a LIST — there is no sorted set. Set operations
`|`, `&`, `-`: **all build a NEW set, so they are EXPRESSIONS**, and **`-` is
not symmetric**. Read as English they are real robot checks —
`commanded - supported` is the joints someone asked for that you cannot drive,
one operator, no loop, no `if`. **`.keys()` is a VIEW and views support set
operations directly**, so `command.keys() - supported` needs no conversion.

⚠ **THE RAISE-VS-SHRUG PAIRING WAS GENERALISED, AND THAT IS THE REAL YIELD OF
THE SET BLOCK.** `d[k]`/`.get()`, `del d[k]`/`.pop(k, default)`,
`remove`/`discard` — **three facts collapsed into ONE design rule: raise when a
missing thing is a BUG, shrug when absence is EXPECTED.** Tested on a fault
handler that may fire twice; **he argued for the raising form on instinct
("silently discarding can cause catastrophic result") and the SPEC overrode
him.** The lesson taught was not that `discard` is safer — it was that **the
choice is a reading of the spec, not a temperament**, and that changing the spec
to "fires exactly once" makes his first answer correct.

**HE ASKED THE BEST QUESTION OF THE SESSION UNPROMPTED:** *"why can't 0 mean
first element in the set"* — and it was answered with the machine rather than a
rule. **The same file run three times printed the set in three different
orders** (string hashing is randomised per process). There is no stable first
element to return. **Python does not offer operations it cannot make mean
anything.** Also banked from that output: `a == b` is `True` across different
insertion orders — **a set compares purely by CONTENTS**.

**HE ALSO ASKED WHETHER TO GO AND LEARN HASHING PROPERLY**, and the Level 2 /
Level 3 boundary was drawn to his face: he already has the Level 2 model (a
number computed from the contents, used to jump to a slot, must be stable), and
**how the number is computed, collisions and resizing are DSA — master Layer 8.**
He accepted immediately. **Reuse this exchange as the template for future "how
deep here?" questions.**

**WHEN-TO-USE-WHICH — TAUGHT, AND THE DIAGNOSTIC IS THE INTERESTING PART.**
Asked for **ONE deciding question**, he gave four correct usage statements
instead — all four right, and all four about what you STORE. **The upstream half
is the item: "WHAT AM I GOING TO ASK THIS CONTAINER?"** Two corrections issued:
**pairing is not the reason for a dict, LOOKUP is** (a list of 2-tuples stores
pairs perfectly well but must be walked); and **"must not change" is the WEAKER
of tuple's two reasons — the stronger one he derived himself in S26: a tuple is
HASHABLE, so it can be a dict key or a set item.**

⚠⚠ **THE NEW WATCH AREA — DESIGN-SWITCHING UNDER A HARD QUESTION.** The applied
exercise (log every joint angle across a 30-second motion) produced the sharpest
finding of the session. **He got the INNER container right, unprompted and for
the right reason: each sample is a TUPLE, a fixed-size record where position
means a specific joint.** He got the outer one wrong via a precise slip —
*"because I want order, its a tuple"* — and **order is not the list/tuple
discriminator; both are ordered. GROWTH is.** Asked what the container must DO
when a new sample arrives at 15 s, **he twice answered by proposing a different
design (a dict keyed by timestamp) rather than answering the question.** On the
third, direct re-ask he had it instantly: *"tuple can't grow, list can grow,
dictionary can grow."* **He had the answer the whole time; the escape route was
redesign, not guessing.** COUNTERMEASURE, and it worked on first use: **name the
switch and re-issue the ORIGINAL question unchanged.** This is adjacent to
depth-before-answer but distinct — that pattern stops early, this one goes
sideways. The resolution taught: **list of tuples**; the timestamp is not a key,
it is another field of the sample, and the dict's one superpower is never used
because you never hold the exact float to look up. **His dict design was
credited where it WOULD win — replay by discrete frame number, real random
access.**

**PUSHBACK 39, UPHELD IN FULL.** *"why would I be removing or discard a joint
name after checking if its the one I support?? question is itself senseless??"*
— correct. A membership scenario was welded to a removal question with no reason
to remove anything. **Running total: 39 raised, 38 upheld or part-upheld.**
⚠ **SPEC-WRITING REMAINS THE MENTOR WATCH AREA FOR A FOURTH CONSECUTIVE SESSION,
BUT THE VOLUME COLLAPSED — FOUR defective asks in S26, ONE in S27.** The fix that
worked should now be standard: **the re-issued version supplied the missing
condition explicitly ("the handler may fire TWICE"), and that single clause made
the question decidable.**

⚠ **TWO SELF-CAUGHT MIS-TAGS, CORRECTED IN SESSION, IN OPPOSITE DIRECTIONS —
AND BOTH DIRECTIONS MATTER.** (a) A [RECALL] was fired thirty seconds after
teaching the station-4 table; it should have been [TEACH-BACK] and was corrected
before anything reached the ledger — **that protects the ledger from echo.**
(b) A traceback read was tagged [TEACH-BACK] when it was genuinely later-day
cold material; it was corrected UP to [RECALL] and promoted — **that stops real
evidence being thrown away.** The standing instruction is to check the tag in
BOTH directions, not only the generous one.

**CONFIDENCE CALIBRATION: STRONG DATA AND ACCURATE.** Eight ratings between 6
and 8. **The two 6/10s were the two shakiest answers — one right, one wrong.**
Keep using the self-rating as a targeting signal, not merely as a gate.

**DEPTH-BEFORE-ANSWER fired three times and ALL THREE recovered on the re-ask**
(the precedence concept half, the ternary concrete case, the
set-meaninglessness half). **Ten successful re-asks across S24–S27 with zero
failures. THE RE-ASK IS THE INTERVENTION — do not re-teach.** One related
instance was logged and not punished: *"I am lazy to calculate so will say 512"*
— he had in fact done the work, so nothing was recorded, but the instinct was
named to his face as the exact habit he asked to have policed.

**TEACH:ASK RATIO — THE S26 FINDING HELD.** Every teaching block carried code
and output before its question, and the pure-question stretch was **DECLARED as
a cold block up front**. He did not push back on it once.

**LANGUAGE PRECISION — THREE CORRECTIONS ISSUED, ALL LABEL-LEVEL, ALL ON
MACHINERY HE OWNS.** (a) *"python can definitely add a string to a integer"* →
**`+` is not DEFINED for `str` and `int`; Python refuses rather than guessing.**
(b) *"placeholders inside the function objects"* → **PARAMETERS are the names in
the `def`; ARGUMENTS are what you pass.** (c) `{"a"=99}` → **inside a dict it is
`"a": 99`, a COLON; the `=` form is a keyword argument and lives in a CALL** —
and that slip is what produced the keyword-argument recall that promoted.

⚠ **THE TERM-RETENTION WATCH AREA SPLIT CLEANLY IN TWO FOR THE FIRST TIME, AND
THIS IS THE MOST IMPORTANT STRUCTURAL FINDING OF THE SESSION. MECHANISMS ARE NOW
STRONG** — the three-way keyword separation in one breath, loop `else`, the
ternary, associativity versus precedence, keyword matching. **LABELS ARE STILL
THE FAILURE POINT** — `KeyError`→`IndexError`, `SyntaxError`→`TypeError`,
"placeholders" for parameters, `=` for `:`. **The hooks fixed the mechanism
recall and have NOT yet fixed the labels. That is precisely what the rule he
adopted this morning is aimed at.**

**WHAT WAS NOT DONE, DECLARED RATHER THAN GLOSSED:** the S26 backlog — tuple,
dict's first two-thirds, shallow copy, unpacking, `list()`, `.get()`,
`.items()` — was listed in the plan and **never run, for the second session in a
row.** It is now the priority for S28 and must go in a drill file or it will
rot. **Comprehensions were declared open at the very end and not walked
through** — he closed the session at exactly that point, to protect the cold
build block, which he moved to **Sunday 23 August: the second date it has
carried.** He asked for the progress audit himself before deciding
(*"how much have we covered till now?? is it enough for a 3 hours session??"*)
and chose to trade the last block of teaching for a full day on the measurement
instrument. **That is scheduling judgement, not avoidance.**

---

## What Session 28 established (Saturday 22 August 2026, evening)

**THE SECOND SESSION OF THE SAME DAY, DECLARED AS SUCH AT THE OPEN AND RUN
CORRECTLY BECAUSE OF IT.** The interval gate was applied unprompted as the first
action: S27's commit was stamped 15:56 the same afternoon, so nothing taught in
S27 was promotable and the entire recall block was skipped. He confirmed and
chose content: *"today lets skip the recall for now lets go for new material."*
**Zero promotions, by design. The S26→S27 pattern is now the S27→S28 pattern —
morning session for recall, evening session for content — and it works.**

### THE MATERIAL — FOUR ITEMS, AND A NINE-SESSION DEBT CLOSED

**1.8 moved from ~70% to ~90%.** List comprehensions, dict comprehensions,
`zip` and f-strings were taught in full, all with runnable code and real output.

⚠ **THE S19 "SEEN-BUT-NOT-TAUGHT" DEBT IS DISCHARGED IN FULL.** Two constructs
were logged in S19 as having been used in examples without ever being taught —
`zip` and list comprehensions. **Both were taught tonight, nine sessions later.
And he caught the comprehension half HIMSELF, unprompted, three turns in:**
*"j * 2 for j in joints] have we seen this form earlier?? I understand what this
line is doing but have we studied it earlier, i don't think so."* **The file
agreed with him — CURRICULUM.md:1145 had written it down precisely so nobody
could later pretend otherwise.** That is define-before-building being enforced by
the student against a record he was not reading at the time.

**THE PREREQUISITE GATE WAS OPENED CLEAN AND ON CREDIT FROM NOBODY.** The
iteration protocol went [x] in S25 specifically to unblock this, and the S15
pre-load instruction — *say out loud that the iteration protocol is the machinery
underneath every comprehension* — was honoured. **It then carried the entire
unit**, including the explanation of why an exhausted `zip` returns `[]`.

**THE SINGLE MOST PRODUCTIVE FACT OF THE SESSION WAS ONE HE ALREADY OWNED.**
Expression-vs-statement, closed in S27 with his own test (*can it go inside
`print(...)`?*), paid out **three separate times in ninety minutes**: it told him
a comprehension is an expression and a `for` loop is not; it explained why
`sum([abs(r) for r in readings])` is legal and a loop in that position is not;
and it let him reason out, unaided, that a comprehension can live inside an
f-string's braces while a `for` loop cannot. **This is what a properly closed
item looks like in use, and it is the best argument in the file for the strict
legend.**

**THE ORDER-OF-EXECUTION BLOCK WAS PROVED, NOT ASSERTED — BECAUSE HE DEMANDED
IT.** Asked *"how important is to know the order of execution, if important
prove me"*, the answer was a live pair: `[100 / v for v in speeds]` raises
`ZeroDivisionError` on a list containing `0`, while
`[100 / v for v in speeds if v != 0]` returns `[10.0, 20.0, 50.0]`. **The filter
can only protect the expression because the gate runs first.** The honest framing
that came with it — *"the four part-names are vocabulary, forget them; the ORDER
is load-bearing"* — is the move that made the proof land.

**`zip` FAILS SILENTLY, TWICE OVER, AND THAT IS THE HEADLINE OF THAT BLOCK.**
Unequal lengths truncate to the shortest with no error; an exhausted `zip`
returns `[]` rather than raising. **He predicted the exhaustion correctly and the
consequence wrongly** — he expected an error. The repair connected to material he
owns: `StopIteration` **is** raised, and `list()` is the thing that catches it,
which is `list()`'s entire job. **Two silent failures in one construct, in five
minutes, on a tool he will use to pair joint names with sensor readings.**

**F-STRINGS MOVED HIM FROM LEVEL 1 TO LEVEL 2 ON A CONSTRUCT HE HAS USED
CORRECTLY FOR 27 SESSIONS.** The file had flagged it — *he uses them correctly
and cannot yet explain them* — and the block was opened by saying exactly that.
Taught: the `f` prefix (without it `{angle}` is eight literal characters); the
three steps **evaluate → `str()` → splice**, with step 2 motivated by the
`TypeError` from `"the angle is " + angle` which he named cold; **what sits in
the braces is an EXPRESSION, not a name**; and the format spec. **Two corrections
issued on the spec: the width number is TOTAL field width, not extra spaces; and
the default alignment differs by type — text hugs the LEFT, numbers hug the
RIGHT, which is why a column of readings lines up on the decimal point.**

### THE STUDENT — TWO MOMENTS THAT MATTER MORE THAN THE MATERIAL

⚠ **HE REFUSED A DRILL HE WAS OFFERED, TO PROTECT THE MEASUREMENT.** At the end
of the teaching he was offered a comprehensions drill file. He declined:
*"wait lets do the drill tommorow then, atleast it goes to the ledger then, lets
continue with further content."* **He traded immediate practice for valid
evidence, unprompted, having correctly worked out that same-day work cannot
promote.** This is the strongest single data point in the session and it belongs
next to the S18 (e) precedent where he refused the "taught" tag on closures.

⚠ **HE STOPPED THE MENTOR MISNUMBERING THE CURRICULUM.** A teaching block was
headed "1.9 — LIST COMPREHENSIONS". He challenged it: *"I think 1.8 was not
complete yet why are you moving to 1.9??"* **Checked and upheld — comprehensions
are inside 1.8; 1.9 is Error Handling and is not open.** He was tracking the plan
he holds against the claim in front of him.

**Both are the jump-ahead pattern running BACKWARDS, in one session.**

### THE MENTOR — FOUR ERRORS, AND THE RULE THEY PRODUCED

⚠⚠ **THE SPEC-WRITING WATCH AREA IS RETIRED (four defective asks in S26, one in
S27, ZERO in S28) AND REPLACED BY A LARGER ONE: FRAMING.** Three of tonight's
four errors have one root — **mechanics taught without the point being stated.**

**(a) THE BREACH THAT PRODUCED THE RULE.** Comprehensions opened with a code
contrast, a three-point anatomy and a [TEACH-BACK] — four turns of show-and-ask
with **not one sentence saying what a comprehension is FOR.** He stopped the
session: *"I am not getting the point in this session what are you trying to
teach me, I am getting confused, you are focussing too much in showing and asking
but not being specific what you are teaching."* **The frame was then given in
full — what it is, why it exists (the expression capability), the honest second
reason (LeRobot/openpi are written in this idiom and reading them is a stated
Layer 0 deliverable), and explicitly what was NOT being claimed (comprehensions
are not better than loops).** His verdict: *"this explanation seems more logical,
you need to start explaining like this, not just come up with something new
randomly."*

**(b) A DEMOLISHED EXAMPLE — THE FIFTH ON HIS RECORD.** The scope contrast was
built with `for angle in [1,2,3]: pass`, so the loop appeared to do nothing and
the two branches were not comparable. *"you used pass after the for loop, so I am
not sure if the variable was even used, or anything happened can you give a
better example."* **Upheld.** Rebuilt so both forms built `[2, 4, 6]`, leaving
the form as the only difference. **This is the S18/S19 motivation-rejection
pattern and it is completely reliable: a weak example will not survive him.**

**(c) A RIGHT-SIZING FAILURE, CONCEDED IN SESSION.** Four turns were spent on
comprehension scope before he asked *"why would I even in first place use the
same variable as I have used to name an object"* — and he was right. The honest
version is one line (**the comprehension's variable does not exist afterwards,
which is the bug people actually hit**), and it was relabelled a footnote out
loud, with the four wasted turns named as a mentor cost. **This became the
COROLLARY inside the new rule: rank facts against each other, in his hearing.**

**(d) A FACTUAL OVER-CLAIM, SELF-CAUGHT AND CORRECTED IN THE SAME TURN — a
different class of error and it needs its own line.** "A comprehension IS a
hidden function" was stated, with a `<listcomp>` traceback frame promised as
proof. **The frame did not appear: he is on Python 3.12, where PEP 709 inlines
list comprehensions while deliberately keeping the scope isolation.** The claim
was true through 3.11. It was corrected to his face with the reason, the Level 2
statement restated (**it gets its own namespace, discarded at the end**), and the
mechanics parked to 1.13. ⚠ **A working `<genexpr>` proof existed and was
DELIBERATELY NOT USED, because generator expressions are untaught — define-
before-building held under pressure to rescue a claim.** **The lesson: verify the
demonstration on THIS machine before promising what it will show.**

### THE RULE ADOPTED — RULES v4, FRAME FIRST

**FRAME FIRST (binding): before any mechanics, a new unit opens with WHAT the
thing is, WHY it exists, and WHAT IT BUYS YOU. No show-and-ask until the frame is
stated. And say out loud how much each fact is worth.**

**Second consecutive rule proposed by the student, in two sessions on the same
day — and the first he ordered written DURING the session rather than parked:**
*"Add this rule right now before closing the session."* The cap was honoured (one
rule), and the timing exception is now recorded: **the cap governs the COUNT, not
the moment.**

**Why it is a rule and not a preference:** it promotes an existing observation
about him — *he presses "why does this exist rather than the obvious
alternative?"*, written down in S18 — into an obligation on the mentor. **S19
recorded that the honest motivation for closures was already in this file and
went unused until the fifth attempt.** This rule makes the frame the first move
instead of the fifth.

### MEASUREMENT AND WATCH AREAS

**FIVE ERROR LABELS ASKED COLD UNDER THE S27 RULE. FIVE CORRECT** —
`SyntaxError` (with the Station 0 proof that line 3 never printed),
`ZeroDivisionError` (decoded on first-ever exposure), `NameError`, `TypeError`,
and his own missing-brace diagnosis on code he had just written. ⚠ **This is the
first session in which the LABEL half of the term-retention split did not fail
once.** It is same-day-adjacent and must be re-fired cold in S29 before anything
is concluded — **but the rule he proposed one session ago is doing exactly what
he said it would.**

⚠ **SIDEWAYS-ANSWERING REPEATED TWICE AND IS NOW A PATTERN, NOT AN INCIDENT.**
S27 recorded design-switching under a hard question. S28 shows the same shape in
a new form: asked for the four parts of a comprehension **by name**, he gave the
**output** instead; asked for two printed lines from a format-spec snippet, he
explained the **format codes** instead. **The countermeasure held both times —
name the substitution, re-issue the ORIGINAL question unchanged.** On the first,
he then produced all four parts correctly **and in execution order, unprompted.**
**Twelve successful re-asks across S24–S28 with zero failures. THE RE-ASK IS THE
INTERVENTION — do not re-teach.**

⚠ **THIRD BOUNDARY BUG, AND THE FASTEST CORRECTION YET.** He read
`[n.upper() for n in names if len(n) > 5]` as keeping `"elbow"` and `"wrist"`,
both exactly five letters. Same class as his S20 `n <= 10` and the planted
`len(word) == 1`. **The habit was named to his face — "your bugs live on the
boundary" — and ONE rep later he opened his next answer with *"condition is >180
not >=180"* without being prompted.** Naming the pattern outperformed re-teaching
it. **Plant a boundary in the S29 drill.**

⚠ **A NEW WATCH AREA, AND IT IS A CATEGORY RATHER THAN AN ITEM: LEVEL-1
CONSTRUCTS HE USES WITHOUT A MODEL.** f-strings sat unexamined for 27 sessions
**because he uses them correctly**, so nothing ever raised a flag. **Correct
usage is not evidence of a model, and it actively hides the gap.** Audit for
others of the same shape — things he types fluently and has never been asked to
explain. Visible candidates: `len()`, `range()` as an object rather than a
keyword, `print()`'s return value, `.append()` vs `+`, `import`.

**NO CONFIDENCE RATINGS WERE TAKEN, correctly** — everything was same-day
teaching and RULES forbids a rating on fresh material. **Do not read the empty
column as a lapse.**

**HONEST-GAP DECLARATION REMAINS RELIABLE.** *"I am confused, can't think of
anything"* on the comprehension-scope mechanism; *"well I don't know that"* on
the f-string prefix. **Both times he then reasoned forward from what he did
have** — the second produced a correct Level 1 answer unaided.

**LANGUAGE PRECISION — THREE CORRECTIONS, ALL LABEL-LEVEL.** (a) *"the list
function goes on the iterator"* → **`list()` calls `next()` on the iterator
repeatedly until `StopIteration`.** (b) `i`/`j` as names when unpacking a name
and an angle → **`i` and `j` read as INDEX names to any Python developer; call
them `name, angle`.** (c) *"left indentation"* for a string field → **strings pad
on the RIGHT; it is the numbers that pad on the left.**

**FALSE ATTRIBUTION / PUSHBACK DENOMINATOR: 45 raised, 44 upheld or
part-upheld.** ⚠ **S28 raised SIX — the highest of any session in the file — and
every one was sound:** (40) *"I think 1.8 was not complete yet why are you moving
to 1.9"*; (41) *"have we seen this form earlier?? i don't think so"*; (42) *"you
are focussing too much in showing and asking but not being specific what you are
teaching"*; (43) *"how important is to know the order of execution, if important
prove me"* — **part-upheld: the proof was given and half the block was conceded
as cheap**; (44) *"you used pass after the for loop... can you give a better
example"*; (45) *"why would I even in first place use the same variable"*.
**Six challenges and four mentor errors in one session is the highest defect rate
recorded here — and every one was caught by him, not by the mentor.**

### WHAT WAS NOT DONE, DECLARED RATHER THAN GLOSSED

**NO DRILL FILE — at his request, and for a good reason (see above). It is owed
as the FIRST item of S29.**

⚠⚠ **THE S26 BACKLOG WAS DECLARED FOR S27, DECLARED AGAIN FOR S28, AND HAS NOW
RUN IN NEITHER.** Tuple, the dict two-thirds, set, shallow copy, unpacking,
`list()`, `.get()`, `.items()`, the raise-vs-shrug pairing, when-to-use-which —
all still untested, some of it four sessions overdue. **This is the third
declaration. S29 either runs it task-first in one drill file or the file should
stop calling it a priority.** The `KeyError`/`IndexError` miss from S27 is
untouched. `while` mechanics remain untested for a second session.

**`*args`/`**kwargs` WAS DELIBERATELY AVOIDED FOR THE SECOND SESSION RUNNING**,
to protect tomorrow's cold build block. ⚠ **`zip` is now taught and `zip` is
exactly the tool that pairs two parallel sequences — do not point him at it
before the block runs.**

**1.8 remaining: nested data structures, common patterns and pitfalls,
`reversed()`, `copy.deepcopy`.** Nested structures is next and it is the block
that finally makes shallow copy make sense.

## What Session 29 established (Sunday 23 August 2026)

**The first cold build block in the course's history ran, four dates after it
was first scheduled. He passed it. The mentor nearly prevented it from
happening at all.** Both halves are true and neither should soften the other.

### THE INSTRUMENT — WHAT WAS MEASURED, AND WHAT WAS LOST

Conditions asked for: 90 minutes timed, no AI, no autocomplete, git commits as
the clock, pytest as the arbiter. **Conditions actually achieved: no AI, no
autocomplete, pytest as the arbiter.** The timer was abandoned — he dropped it
in frustration after the fourth spec rewrite (*"we don't have any timers"*) —
and `LOG.md`, the process record, was never written. **So block 01 yields a
correctness measurement and nothing else. There is no duration and no stall
log.** Recorded as a loss, not glossed: two of the four conditions in the
file's own definition of the instrument were not met, and the reason was
mentor-side.

The acceptance suite was written by the mentor — 13 tests across L1/L2/L3 —
after he pointed out that the spec had demanded he write tests himself.
**He wrote one file, `clamp.py`, and it went 13/13 on the run.**

### THE RESULT — AND THE ONE MOMENT THAT MATTERS

The block was designed around a single hole, described in STATE.md since S26:
`*args` delivers joint angles **positionally and anonymously**, `**kwargs`
delivers limits **by name**, and nothing in that design pairs them. **S27 and
S28 were both deliberately steered off `*args`/`**kwargs` to protect the
measurement, and STATE.md carried an explicit standing order: `zip` is now
taught, `zip` is exactly the tool that pairs two parallel sequences, DO NOT
POINT HIM AT IT.**

He wrote, cold, the day after learning `zip`:

```python
for angle_value, limits_key in zip(angles, limits):
```

**That line is correct for three stacked reasons, and on the mechanism question
he produced all three:** dict keys hold insertion order (**volunteered
unprompted, with the contrast to sets attached — *"unlike sets"***); `zip`
pairs positionally, first with first; and iterating a bare dict yields its
**KEYS**, not its values and not its items (**this one only on the re-ask**).
Self-rating 8/10 on `zip`; the dict-iteration rating was asked twice, mis-phrased
once by the mentor, and never given.

**THIS IS THE FIRST TIME IN TWENTY-NINE SESSIONS THAT A CONSTRUCT TAUGHT IN THE
PREVIOUS SESSION WAS DEPLOYED AGAINST A NOVEL PROBLEM RATHER THAN RECITED.**
The whole course exists to produce exactly that and it has now been observed
once, cleanly, under cold conditions. `zip` promoted to [x] — flagged
SHORT-GAP (~10h plus sleep) for the August gauntlet.

Also correct and cold, none of it directly asked: `*args`; `**kwargs`; `*args`
placed after a positional parameter; `*limits[n]` unpacking a tuple into a call
(the `*args` mirror); f-string format specs `{limits_key:10s}` and
`{value:8.1f}`, **with the columns aligning on the first run** — the S28
text-hugs-left/numbers-hug-right fact applied rather than repeated.

**AND THE BOUNDARY WAS HANDLED CORRECTLY — THE FIRST CLEAN ONE IN FOUR.**
A boundary was planted in the spec and declared as planted. He wrote strict
`<` and `>` in all four copies of the rule; the exact-on-limit tests passed.
⚠ Caveat kept honest: he did not write the tests, so this is correct CODE, not
yet the boundary-first testing HABIT.

### THE CODE READ — TWO FINDINGS, ONE OF THEM HIS OWN

`report()` opens `clamped_joint_angles = {}`, never fills it, and returns it.
It prints correctly and hands back an empty dict. **He diagnosed the cause
himself and unprompted: *"i picked up the code from previous block and didn't
modify it properly."*** The danger was named — it does not crash, and `{}`
looks like data, so it slips past his own S25 returns-`None` tell.

Underneath it: **the clamp rule is written out four times in 46 lines** —
`clamp_one`, `clamp_all`, `clamp_joints`, `report`. He proposed the right fix
immediately (*"I should make one function that does all that calculation"*)
but skipped the failure-mode question twice. **The delivered lesson, and it is
the one worth keeping: change the rule, update three of the four, and pytest
still says 13 PASSED — because `report` was never tested. Duplication is how
the untested copy quietly stops matching the tested one, and on a real arm that
is the log you read during an incident review.** The refactor was not done; it
carries to S30.

### THE STUDENT — THREE PUSHBACKS, ALL UPHELD, ONE OF THEM THE BEST ON RECORD

(46) the spec is abstract, give me a concrete problem. (47) I still cannot see
the exact problem — *"lets call this off"*. **(48) you are expecting me to
write tests, we haven't learnt that.** Running total **48 raised, 47 upheld or
part-upheld.**

**(48) IS THE MOST VALUABLE PUSHBACK IN THIS FILE.** It is not a process catch
and not a technical catch — **it is him auditing a measurement instrument
against the course's own define-before-building rule and finding a hole that
would have invalidated the entire block.** STATE.md:363 said in as many words
that pytest as a subject is not scheduled in Layer 0; every `N/N pytest` in
CURRICULUM.md is a mentor-written file he passed. He has never authored a test.
**Ninth define-before-building breach, same shape as the S18 `d.clear()` one,
caught before it cost a minute of block time.**

He also read a **stale VS Code markdown preview** and spent two turns furious
at a spec already fixed on disk — and **asked what the discrepancy was rather
than concluding the mentor was useless.** Channel before blame, from his side.
The anger in this session was real, sustained and directed at the mentor, and
**it was earned; it is recorded here as a cost of the mentor's failure, not as
a fact about him.**

Depth-before-answer fired twice and recovered twice — **fourteen and fifteen
straight, still zero failures.** The second instance is the purest example yet
of **DESIGN-SWITCHING**: asked what a caller would SEE when three of four
copies get updated, he answered in five-checks vocabulary (*"failure mode will
be Boundary... bahar"*) — substituting a question he can answer in owned
vocabulary for the one that was asked. Fixed, as always, by naming the
substitution and re-issuing the question unchanged and narrower.

### THE MENTOR — ONE FAILURE, COMMITTED FOUR TIMES

**The worst mentor session in the file, and it should be read that way.** S28
produced three framing failures in a session that still taught four items. S29
produced one failure repeated four times and taught nothing.

The spec was issued in four versions: **(v1)** no exercise at all — "the design
is yours"; **(v2)** five levels in pure prose, not one concrete number;
**(v3)** concrete arm, concrete angles, acceptance table — **still no
signature**; **(v4)** exact signatures, exact expected return values. He
started immediately on v4.

**ROOT CAUSE, stated plainly: the mentor protected a puzzle at the student's
expense and re-derived the same wrong answer three times without ever checking
its premise.** The premise was that handing over the signature would give away
the problem. **It was false. The design hole lived in the function BODY, not
the parameter list** — proved within the hour, by him, on v4. **A measurement
instrument that takes four attempts to describe is not an instrument.**

Second failure, above: the spec required untaught pytest authoring.
Third, minor and self-corrected: the dict-iteration confidence question bolted
two facts into one clause, he said he did not understand it, and the re-phrased
version was then dropped when he moved on.

**RULE CANDIDATE PARKED, MENTOR-PROPOSED, HIS RULING OWED AT THE S30 OPEN —
"SPEC BEFORE PUZZLE":** a task spec states the exact interface and the exact
expected values; the only thing ever withheld is the solution. A spec that
leaves the student unable to start has measured nothing, and **a block that
does not run measures strictly less than a block that runs with help.**
No rule was adopted in S29; RULES.md stays at v4.

### WHAT WAS NOT DONE, DECLARED RATHER THAN GLOSSED

- **No teaching. No curriculum movement.** 1.8 stands at ~90%, exactly where
  S28 left it.
- **The comprehensions drill did not run — deferred a SECOND time (S28 → S29 →
  S30).** He refused it at the S28 close specifically to keep it
  ledger-eligible. **That is a promise this file made to him and then broke,
  and the reason is entirely mentor-side.** First teaching item in S30.
- **The three-session backlog was not touched** — tuple, dict, set, shallow
  copy, unpacking, `list()`, `.get()`, `.items()`, raise-vs-shrug,
  when-to-use-which. Fourth consecutive declaration.
- **The S27 error-naming rule never fired**: nothing raised all session.
- **The refactor he proposed was not done.**
- **`LOG.md` was never written; the timer was abandoned.**


## What Session 30 established (Monday 24 August 2026, evening, after office)

**THE RECOVERY SESSION, AND THE THING THAT RECOVERED IT WAS A RULE.** S29 ended
with zero curriculum items and a mentor-proposed rule parked for a ruling. S30
opened with the interval gate, then that ruling, then teaching — in that order,
for the first time in three sessions.

**1. SPEC BEFORE PUZZLE — ADOPTED, RULES v5.** Put to him as a one-line ask
before any teaching, with the explicit statement that he was entitled to reject
it and that the last two adopted rules were his and this one was not. His
ruling: *"Adopted."* ⚠ **Its cost was found on its first day and written into
the rule in the same breath: exact expected values can REVEAL A PLANTED
BOUNDARY.** `over_limit([10, 45, 90, 45, 5], 45) -> [90]` was meant to test
boundary-first blind; the docstring gave it away. **Remedy now binding:
boundary cases go in the TESTS, not in the worked examples.**

**2. THE COMPREHENSIONS DRILL RAN — THE PROMISE THIS FILE BROKE TWICE.**
Deferred S28 → S29 → S30, and the second deferral was the mentor's fault.
`drills/s30_comprehensions.py`, four functions, one `return` per body, against
16 mentor-written tests. **16/16 cold, unaided, later-day.** He wrote a filtered
list comprehension, a dict comprehension, a dict comprehension over `.items()`
with two-name unpacking, and `f"{name:10s}{value:8.2f}"` exact to the character
including the case where the name is LONGER than its column.
**The mechanism half was taken separately and it is what earned the ticks:** he
stated the execution order cold (iterable → variable → condition → expression),
named the condition as the gate, and explained unprompted why
`[100/v for v in speeds if v != 0]` cannot raise. **List and dict comprehensions
both go to [x] in CURRICULUM.md.**

**3. THE CONTAINER BACKLOG — DECLARED FOR S27, S28, S29, AND RUN IN S30.**
`drills/s30_containers.py`, six functions, 19 mentor-written tests, **19/19
cold.** Written correctly and unprompted: `set(a) & set(b)`, `angles[:]` as the
copy, `return low, high, dist` as ONE tuple, `sum`, and `abs` — the last of
which **has never been taught and made his answer more robust than the mentor's
own reference implementation**, which used a bare `high - low` that only passed
because no test had `low > high`. Credited in session.

**4. THE MOST USEFUL FINDING IS A GAP, AND IT IS THE TERM-RETENTION DIAGNOSIS
IN ITS PUREST FORM.** Two of the six functions said *"absence here is EXPECTED,
not a bug."* He produced correct shrugging behaviour both times — by hand, as
`limits[joint] if joint in limits else (0,0)` and
`limits.pop(joint) if joint in limits else None`. **The design rule is owned.
What is gone is the two API names that implement it** — `.get(k, default)`
taught S26, `.pop(k, default)` taught S27, neither ever re-tested. Asked to
rewrite with no `if` and no `in`, he said plainly *"wait I don't remember
another method to do this"* — an honest gap declaration, correctly flagged
rather than guessed at. **He was given one pointer, not a solution:** a
[PREDICT], declared as a genuine guess, on what a second argument to `.pop()`
does. He guessed `ValueError`; it shrugs. **Not ledgered — a PREDICT miss on
never-before-seen behaviour is not a retention failure.**
⚠ **THE SECOND-ORDER LESSON, AND IT IS THE S29 LESSON AGAIN: HIS FIRST VERSION
PASSED 19/19. A GREEN SUITE CAN HIDE A LOST TOOL.**

**5. RAISE-VS-SHRUG DID NOT PROMOTE, AND THE REASON IS RECORDED HONESTLY.**
The tools were aided. Worse, asked for the rule rather than an example, he put
*"when the absence is expected"* on the **raising** side — the pairing
inverted. Two narrowing re-asks repaired it (*"when we don't want the absence
to go unnoticed"*). **He then self-rated 8/10, and the mentor challenged it to
5–6 with the evidence named.** First overt miscalibration in a long while, and
it sits precisely where the concept is solid and only the tool is missing —
**he appears to have rated the concept, not the retrieval.** Watch it; do not
generalise yet.

**6. THE S27 ERROR-NAMING RULE FIRED AGAIN AFTER A SESSION UNFIRED.** Two
snippets, both `[5]`, one on `{0: "shoulder", 1: "elbow"}` and one on a list.
He named `KeyError` and `IndexError` cold and correctly — **clearing the S27
miss** — then, on the re-ask, gave the discriminator in his own words: the dict
was handed a key that does not exist, the list an index that is not there.
**The brackets do not decide the error; the container does.** Station 4 of his
own hook, re-fired clean.

**7. THE DEAD `{}` WAS MADE VISIBLE.** `report()` in block 01 returns an empty
dict it never fills, and the S29 suite stayed 13/13 green because nothing ever
tested `report`. The mentor wrote `builds/block_01_joint_clamp/test_report.py`
(6 tests), verified it green against a throwaway reference refactor which was
then discarded, and ran it: **4 failed, 15 passed.** The refactor spec — one
copy of the clamp rule, unchanged signatures, `report` printing AND returning —
was issued and accepted. **He deferred it to S31 at his own call.**

**8. DEPTH-BEFORE-ANSWER FIRED THREE TIMES, ALL THREE RECOVERED — 16, 17, 18
STRAIGHT WITH ZERO FAILURES.** Each time the countermeasure was the same and it
is worth repeating: **name nothing, re-issue the original question unchanged,
narrow it until it is derivable. THE RE-ASK IS THE INTERVENTION. Do not
re-teach.**

**9. CHANNEL — THE UNSAVED-BUFFER ARTEFACT, FOUR FIRINGS, FIVE TURNS.** Four
times he said "done" with his edits still in the VS Code buffer and the file on
disk untouched. **Every time the mentor checked mtime and `git status` first
and asked him to save rather than logging a failure.** This is the S15 stale-
master and S29 stale-preview lesson running in the opposite direction: **before
logging a failure, ask whether the channel could have produced it.** Remedy
offered: `"files.autoSave": "afterDelay"`.

**10. MENTOR FAILURES — ONE, AND MUCH SMALLER THAN S29's.** The mentor said
*"give me a minute"* and then produced nothing, and he had to prompt: *"what
happened I am still waiting."* **Pushback 49, upheld in full. Running total:
49 raised, 48 upheld or part-upheld.** The lesson is the S20 response-length
rule in a new form — **do not announce work, do the work.** Otherwise the
protocol held: FRAME FIRST clean, every block tagged, the [PREDICT] declared its
kind, the interval gate and the rule decision both ran before any teaching, and
**all three test files were written by the mentor and verified green against
throwaway references that were then deleted** — the S29 standing rule, honoured
without being asked.

**WHAT IS STILL NOT TESTED, STATED PLAINLY SO IT IS NOT PRETENDED AWAY:** S30
ran the container CODE, not the container CONCEPTS. Tuple immutability, the
`count`/`index` roster, hashability, set order instability, `{}`-is-a-dict,
`del`/`.pop()`/`.clear()`, when-to-use-which, `list()` as a constructor, and
`.keys()`/`.values()` remain cold-untested. **f-strings and format specs have
now been written cold and correctly in TWO consecutive sessions and asked in
NEITHER — third attempt owed in S31.** `while` mechanics are four sessions
overdue.

### What Session 31 established (Tuesday 25 August 2026, evening, ~1 hour)

**1. BUILD BLOCK 01 IS CLOSED, AND THE THING THAT CLOSED IT WAS A REWRITTEN
SPEC — NOT MORE TEACHING.** The refactor he deferred at the S30 close took him
about fifteen minutes once the brief was right: the clamp decision went from
FOUR written copies (`clamp_one`, `clamp_all`, `clamp_joints`, `report`) to one,
with the other three calling it; `report` was made to PRINT **and** RETURN the
dict it had always only printed. `4 failed, 15 passed` → **`19 passed`**.
He then proposed a second improvement himself, unprompted, and asked for a check
before answering the question about it: `report` had been calling `clamp_one`
**three times per joint per pass** — once for the dict, once for the printed
value, once inside the `CLAMPED`/`ok` ternary — and he collapsed it to a single
local. **The count question he answered exactly (`3`); the *"how many were
necessary"* half he skipped and recovered on the re-ask.**

**2. ⚠⚠ THE HEADLINE IS A MENTOR FAILURE, IT REPEATS S29 EXACTLY, AND IT
HAPPENED ONE DAY AFTER THE RULE WRITTEN TO PREVENT IT WAS ADOPTED.**
SPEC BEFORE PUZZLE was ruled on at the S30 open. In S31 it was breached twice
over, and not in the way the rule anticipated:
* The refactor spec was issued **in chat only**. He asked *"where are the
  instructions for this file what I need to do??"* — **pushback 50, upheld.**
  The spec existed nowhere he could go back and read.
* The brief file then written was **abstract**: "the clamp decision appears
  exactly once", with no concrete finish line. He rejected it — *"wait its
  still confusing, the brief factor file is not clear, I can't understand what
  i need to do, make it clear, for all the instructions that i need to do."*
  **Pushback 51, upheld in full.**
The version that worked did four things and all four are reusable: **the job
was split into Part A and Part B with separate finish lines; every acceptance
condition got a MECHANICAL check he could run himself** ("read `clamp.py`, count
the function bodies that compare an angle to a `low` or `high` — that count must
be 1"); **the four repeated blocks were quoted side by side** so the repetition
was visible rather than described; and an explicit **MAY / MAY NOT** list was
given, because "signatures unchanged" had left him unsure whether he was even
allowed to add a function.
⚠ **THE LESSON, NARROWER THAN THE RULE ITSELF: SPEC BEFORE PUZZLE IS NOT
DISCHARGED BY SAYING THE SPEC OUT LOUD. It has to be a file in the repo, and
every acceptance condition needs a way for HIM to check it without asking.**
⚠ **AND THE DIAGNOSTIC VALUE IS REAL: the moment the spec was concrete, the work
took fifteen minutes. Nothing about his capability changed between the two
briefs.** This is the S29 finding confirmed a second time, and it should now be
treated as settled fact about this course rather than as a hypothesis.

**3. FOUR PROMOTIONS, ALL COLD, ALL LATER-DAY — AND THREE OF THEM WERE ITEMS HE
HAD WRITTEN CORRECTLY FOR SESSIONS WITHOUT EVER BEING ASKED.**
* **f-string, the three steps** — evaluate, convert to string, splice. Asked off
  his own live code. He opened with braces-hold-an-EXPRESSION **unprompted**,
  and needed **one narrowing re-ask** to produce the `str()` step. 8/10.
* **format spec, width and precision** — he named the number as **TOTAL FIELD
  WIDTH** without being led, which is the trap in that fact.
* **single return value builds ONE tuple** — cold, no re-ask, off his own S30
  `span`. 8/10.
* **THE COMMA MAKES THE TUPLE** — `(1)` is an int, `1, 2` is a tuple, the
  parentheses are only grouping. All three cases right first time. 8/10.
**THIRD SESSION OF ASKING for the f-string row.** It had been written cold and
correctly in S29 and S30 and asked in neither. **That was a mentor failure, not
a student one, and it is now discharged — 1.8 String formatting is [x].**

**4. ⚠ THE BEST STUDENT MOMENT IN SEVERAL SESSIONS: AN UNPROMPTED LABEL
SELF-REPAIR.** On format-spec alignment he first said *"string is filled ... on
the right side, whereas numbers on the left side"* — inverted. The mentor had a
`cat -A` of his own printed output ready to show him and **never needed it.**
Before any evidence appeared he came back: *"actually I said it wrong, 10 means
10 grid spaces allocated for the string, and string starts from first cell, that
is left, whereas ... the full number will be on the right side."*
**He corrected an arbitrary label, unaided, with nothing shown to him and no
re-ask.** The label-slip-on-owned-machinery pattern has been the single most
persistent finding in this file since S15. **This is the first recorded instance
of him catching one in flight.** The row was promoted with the alignment half
split out for a short-gap re-test — **the interval was adjusted, not the
promotion**, which is exactly what the confidence rule is for.

**5. TUPLE IMMUTABILITY HELD AT [~] DELIBERATELY, AND THE REASON IS THE MOST
PRECISE ILLUSTRATION OF THE TERM RETENTION DIAGNOSIS THIS FILE HAS.**
Given `limits = (-90, 90)` then `limits[0] = -45` under the S27 error-naming
rule, he produced the entire mechanism and then stopped at the label: *"a tuple
is immutable, and we are trying to assign a value to the 0th index object of an
immutable, this operation is not possible so its a — I can't come up with the
error type."* **Honest gap declared rather than guessed, with the machinery
stated correctly all around the hole.** He was not given the label. He was
pointed at his own four-station hook and derived it: **Station 3, TYPE ⇒
`TypeError`.**
**MECHANISM COLD, LABEL AIDED ⇒ NO PROMOTION.** Recorded that way on purpose.
But note what the hook did: it converted an unrecallable arbitrary label into a
derivable one, which is precisely the job it was built for in S25/S27.

**6. A PUSHBACK THAT WAS PART-UPHELD, AND THE HALF THAT WAS REFUSED MATTERS AS
MUCH AS THE HALF THAT WAS GRANTED.** Re-asked the skipped half of the
redundant-calls question, he objected: *"its stupid that you are still asking me
the question, its easily understandable that I have made the changes in the code
so I do understand it."* **Pushback 52, part-upheld.**
* **Granted:** that question was tagged **[TEACH-BACK]** — no rating, not
  ledger-eligible — and it was fired on code he had **already corrected**. It
  could record nothing in either direction. Spending his turn on it was wrong.
* **Refused, and stated to his face:** writing correct code is **not** the same
  as being asked. Four rows sat at `[~]` for three sessions for exactly that
  reason, and three of tonight's four promotions came from finally asking about
  code he wrote in S29 and S30. **Application is not evidence.**
The operational rule that comes out of it is not "ask less" — it is **ask the
things that can promote.**

**7. THE VERDICT WAS OWED AND NOT GIVEN.** After he rated the comma/tuple answer
8/10, the mentor went straight to building the next drill and let tool output
land in the channel. He stopped it: *"wait what you asked me my confidence after
this ... and then you have given some random output what is happening."*
**Pushback 53, upheld in full.** Two separate defects in one turn: a rating taken
with no ruling returned, and unnarrated machinery shown to the student.
**The sequence is fixed and it is cheap: his answer → his rating → THE VERDICT →
the next thing. Tool work is silent.**

**8. THE RAISE-VS-SHRUG DRILL WAS WRITTEN AND ISSUED BUT NOT ATTEMPTED.**
`drills/s31_shrug.py` — six functions, three pairs (`limit_for`/`must_limit`,
`drop_limit`/`must_drop`, `retire`/`must_retire`), each pair doing one job twice:
once where a missing thing is **expected**, once where it is a **bug**.
⚠ **THE DESIGN POINT IS THE CONSTRAINT, AND IT COMES STRAIGHT FROM THE S30
FINDING THAT A GREEN SUITE CAN HIDE A LOST TOOL:** `if`, `in`, `else` and `try`
are **banned below the docstring, enforced by a test that reads the source
file**. That bans the hand-roll (`x if k in d else default`) he used to pass
19/19 in S30 while having lost `.get(k, default)` and `.pop(k, default)`
entirely. `tests/test_s31_shrug.py` (17 tests) was written by the mentor and
verified green against a throwaway reference which was then deleted; the stub
stands at `13 failed, 4 passed`. **It is the first thing in S32.**

**9. PROTOCOL SCORECARD.** Held: the interval gate ran first; no rule was
invented to fill an empty parking lot; every block was tagged and the
non-ledger one was declared as such; the S27 error-naming rule fired; the mentor
wrote both test files and verified them before handing them over; **mtime was
checked before every read and the unsaved-buffer artefact fired ZERO times, down
from four in S30**; session length was left entirely to him and he ended it.
Failed: SPEC BEFORE PUZZLE (twice), the missing verdict, the tool-output dump,
and a turn spent on a non-ledger question. **Depth-before-answer fired twice and
recovered both times — NINETEEN AND TWENTY STRAIGHT.**
**PUSHBACK DENOMINATOR: 53 raised, 52 upheld or part-upheld. S31 raised FOUR,
three upheld in full — the second-highest count in any session, and all four
about the same thing: give him something concrete he can act on without asking.**

**10. `LOG.md` WAS SKIPPED A FOURTH TIME.** It was prose in the S29 brief and a
**numbered step** in `BRIEF_REFACTOR.md`, and neither worked. Block 01 therefore
closes with code and tests but **no process record and no duration**, which is
the one thing a measurement instrument was supposed to produce.
**For block 02 it goes FIRST, before any code is written.**


## What Session 32 established (Thursday 27 August 2026, evening → 00:15 Friday 28)

**Ran with a two-day gap from S31. Everything asked was ledger-eligible.
Four promotions, all cold, all later-day. 1.8 moved from ~93% to ~95% with
nested data structures opened. No rule adopted; the parking lot stayed empty
deliberately.**

---

**1. THE SESSION OPENED WITH A SELF-DIAGNOSIS, AND IT IS THE MOST IMPORTANT
THING IN IT.** Before any teaching he said: *"I feel like I have started
forgetting things, but also we can't just waste time just revising we need to
learn new content as well."*

**Both halves are true and the file already agreed with both.** The answer
given, which held up across the whole night and should be reused verbatim:

> The forgetting is real, but it is **LABELS, not machinery.** In S31 he
> produced the entire mechanism of tuple immutability and then said *"I can't
> come up with the error type."* Understanding intact; name gone.
> **Therefore retrieval is the CHEAP operation — sixty seconds — and
> re-teaching is the expensive one.** Revision is not the remedy; testing is.

The session was then run ~50/50 old/new, with the cold asks **mixed into** the
material rather than fired as an opening block, and he did not push back once.
**That split is the operational answer to his complaint and it should be the
default shape from here.**

---

**2. THE DRILL: `drills/s31_shrug.py`, 17/17, AND THE ROW IT CLOSED.**

Written and issued in S31, untouched for two days, finished tonight. Six
functions, three pairs, under a constraint banning `if`, `in`, `else` and `try`
below the docstring — a constraint enforced by one of the tests, and aimed
squarely at the hand-rolled guards he wrote in S30.

**Every one of the six tools was chosen cold and correctly on the first
attempt:** `.get(k, default)`, `d[k]`, `.pop(k, default)`, `.pop(k)`,
`discard`, `remove`. Not one guard was written. **In S30 both tools in this
family were AIDED and the choosing rule was stated INVERTED; tonight the tool
half was clean.**

Three fixes were needed and they are worth separating by kind:
- **`drop_limit` and `must_drop` were missing their `return`** — he called
  `.pop(...)` and threw the value away. **Twenty minutes after being taught
  that `.pop` hands the value back.** This is the five-checks gap, not a
  comprehension gap.
- **`limit_for`'s default was `None` instead of `(-180, 180)`** — a spec-read
  slip; the value was written in his own docstring four lines up.

**THE CHOOSING RULE THEN PROMOTED, 7/10, ASKED AFTER THE TESTS WERE GREEN.**
He gave the direction correctly — *"the user expects the input to be missing
then we chose the shrug"* — which is the exact statement he got **backwards**
in S30. **But the second half was CIRCULAR:** *"if the user want the missing
values to raise an error he choses the second column."* That renames the choice
instead of grounding it.

The sharpening that landed, and it is the reusable version:

> **Is a missing key a legitimate state of the world, or does it mean my
> program's assumptions are already broken?** Legitimate ⇒ shrug. Broken ⇒
> raise, deliberately and early, so the failure appears where the CAUSE is
> instead of travelling.

Grounded in his own domain: `limits.get(joint, (-180, 180))` on a misspelled
joint name hands back a ±180° range, so the safety clamp clamps **nothing** and
the arm moves; `limits[joint]` stops at the config-load line with the bad name
in the traceback. **Absence you did not plan for is a bug wearing a disguise,
and shrugging is what puts the disguise on.**

---

**3. ⚠⚠ THE FINDING OF THE SESSION, AND IT IS A NEW KIND: `None` IS NOT
NOTHING.**

Twice in one night, on two unrelated mechanisms, hours apart:

- On `.pop`, unprompted and self-initiated: *"`.pop` by default doesent hand
  back anything, but we can add a default parameter for it to return, by
  default it should be returning `None`."*
- On `list()` over a spent iterator: *"so `None` in the second list"* — for a
  result that is `[]`.

**`None` is an OBJECT. It occupies a slot: `len([None])` is 1. "Nothing" is the
absence of a slot: `len([])` is 0.** `del` hands back nothing at all; a
function with no `return` hands back `None`; an empty list contains neither.

**WHY THIS MATTERS MORE THAN ANY OTHER ENTRY TONIGHT.** Every retention finding
in this file for twenty sessions has had the same shape — *mechanism intact,
label lost*. **This one is the opposite: a distinction he does not have.** It is
a knowledge-structure gap, and it must be taught as new material rather than
re-tested as revision. It also retro-explains the `.pop` error, which was
otherwise a *smart* wrong answer: he was reaching for the
in-place-mutators-return-`None` tell he genuinely owns, and running it
**backwards** — the exact failure the S24 one-directionality warning exists to
prevent.

---

**4. STATION 0 FIRED UNPROMPTED, TWICE, WITHIN AN HOUR OF BEING MISSED.**

The miss came first. `print(del d["shoulder"])` — he labelled it `TypeError`,
rated 6. It is `SyntaxError`, **and it is the identical miss to his first-ever
error-naming ask in S27** (`print(if n > 10: "high")`, also called `TypeError`).
Five sessions apart, same shape: a statement placed where a value belongs.
**Logged as a named pattern, not a one-off.** Taught: a `TypeError` is a
RUNTIME verdict, so the line must be grammatical before it can be reached — and
the traceback carries **no frames at all**, because there was never a running
program to have frames.

**Then, within the hour, twice, without being asked:**

- On tuple item assignment: *"is the syntax correct, yes, ok then can we do the
  `.` for this datatype, now so type error"* — Station 0, then Station 3.
- On the (untaught) `<`/`>` snippet: he checked the grammar first and concluded
  `SyntaxError`. **Wrong conclusion, right instinct** — and tagged [PREDICT],
  so nothing was logged.

**He prefaced both with "I forgot the hook".** The hook has stopped being a
thing he recites and become a thing he uses. **USE IS NOT RECALL, so the row
stays [~] and S33 must ask the stations BY NAME** — but this is the mechanism
working exactly as designed.

---

**5. TUPLE IMMUTABILITY PROMOTED — THE S31 GAP CLOSED IN ONE ASK.** S31 held it
at [~] deliberately: mechanism cold and complete, `TypeError` **aided**. Tonight,
cold, two days later, he produced the label unaided in one move by walking the
hook. Rated 5, so it comes back on a short gap. Sharpened afterwards:
**Python is not objecting to the `0` or to the `10` — it is objecting that the
operation does not exist for the type. Immutability has no error of its own; it
always arrives as `TypeError`.**

---

**6. ⚠ THE MENTOR FAILURE: DEFINE-BEFORE-USE, NINTH OCCURRENCE — AND THIS ONE
HAD TEETH.**

A ledger-eligible [RECALL] on format-spec alignment was fired as
`f"{name:<10}{angle:>8.1f}"`. **`<` and `>` had never been taught.** He stopped
it: *"wait you worte a `<` and `>` sign after the `:` for both of them, I havent
seen these before."* **Pushback 54, upheld in full.** S31 taught the *default*
alignment only — verified by grepping the S31 notes rather than reasoning from
memory, which is itself the S15 rule being applied.

**The breach is not the serious half. The serious half is that `<` means left
and `>` means right — so the snippet ANNOUNCED THE ANSWER to the question it
was asking.** Had he guessed what the arrows meant, a pass would have been
recorded that he had not earned. **This is the same defect class as the S30
planted boundary, and it is the second time an instrument has leaked its own
answer.** The row was **HELD at [~]** and scrapped for the night, because with
the arrows on screen no answer could be clean.

The check that was skipped costs nothing: **grep the notes for every symbol in a
recall snippet before firing it.** Not parked as a rule — it *is* define
before use, and adding a second rule to enforce the first is governance
scope-creep (the same ruling as S31).

The *why* behind alignment was then taught as new material: **right-aligning
numbers makes place value and decimal points stack, so magnitudes can be
compared down a column without reading a digit; left-aligning text gives the eye
a straight margin to scan.** The default matches what you scan the column FOR.

---

**7. NESTED DATA STRUCTURES OPENED — AND HE DERIVED THE PAYOFF BEFORE IT WAS
TAUGHT.**

Framed honestly, per FRAME FIRST: **nesting is not a feature, it is a
consequence.** Containers hold objects; lists and dicts *are* objects; nothing
was added to the language for this. Motivated from his own S29 `range(len(...))`
habit — flat containers lose the shape of the data and force the relationship to
live in your head. Non-claim stated out loud: deep nesting is a smell.

Then the trap. Given `a = [[1,2],[3,4]]; b = a[:]; b[0][0] = 99`, tagged
[PREDICT], **he produced the entire mechanism cold, off S24 aliasing, before any
teaching:**

> *"`:` will create a new copy, but what we studied earlier the object in this
> copy are the same object, so the list object is new but the objects inside
> this list are same objects in the old list... and thus `b[0][0]` mutates the 1
> in this so `a` and `b` both..."*

Only the final **value** slipped — he wrote `[[1,2],[3,4]]`, forgetting to apply
his own `99`. Proved with `a is b` → `False` and `a[0] is b[0]` → `True`.

**Then he TRANSFERRED it, unprompted, to a container it had not been shown in:**
given `dict(config)` he flagged honest uncertainty about the constructor, then
reasoned the shallow-copy consequence through correctly and got
`{'limits': [0, 90]}`.

**THIS IS THE SAME SHAPE AS THE S29 `zip` MOMENT — transfer to an unseen case,
which is the strongest evidence this course produces. And for the second time it
arrived inside a [PREDICT], which can never promote.** Worth a decision at the
gauntlet: these should be re-asked cold so they can count.

Also banked: **for a flat list of immutables a shallow copy is
indistinguishable from a real copy**, which retro-explains why `angles[:]` never
bit him in S30; the three shallow forms `a[:]`, `list(a)`, `a.copy()`, with
`.copy()` preferred for intent; and **constructors corrected — `dict(config)` is
not a type conversion, it is a CONSTRUCTOR CALL that walks the pairs and stores
the same value objects, which is exactly why it comes out shallow.**

---

**8. `list()` ASKED AT LAST — SEVEN SESSIONS OVERDUE — AND HALF PASSED.**
`list(box)` twice on an exhausted iterator: first line `[1,2,3]` right, second
`[None]` where it is `[]`. Rated 7. **The mechanism was cold and correct** —
*"iterator after going through the iterable goes empty, it has forward only
state"* — and only the value was wrong, which is the `None`-is-not-nothing
finding again rather than a fact about `list()`. Not promoted; short gap.

---

**9. CONFIDENCE CALIBRATION WAS GOOD AND HONESTLY LOW WHERE IT SHOULD BE.**
5 on `.pop` (wrong), 6 on `SyntaxError` (wrong), 5 on tuple immutability
(right), 7 on the raise/shrug rule (right but circular), 7 on `list()` (half
right). **Every rating at or below 6 sat on something genuinely shaky.** Per the
S17 finding these are a targeting signal, and S33 should re-fire exactly those.

---

**10. PROCESS.** Depth-before-answer fired twice: once recovered on re-ask (the
*why* behind `TypeError` — **21 straight**), once answered with an honest gap he
declared himself rather than guessing (*"I know this heappnes, I belive we
havent discussed why"* — and he was right, so nothing was logged).
**The five checks went unreported for the THIRD consecutive session**, and they
are precisely what would have caught the two missing `return`s before pytest
did — **so the ask changes: the five checks are the GATE on saying "done", not a
postscript.** The unsaved-buffer artefact fired **twice** (one "done" with no
write at all, one save producing a byte-identical file); mtime and size caught
both and nothing was logged against him. **`print()` joins the level-1 audit
list** — he described it as taking a string; it takes any object and calls
`str()` on it.

## What Session 33 established (Friday 28 August 2026, 16:00 → Saturday 29 August, ~12:00)

**The longest session in the file, and he specified its shape at the open:**
*"one of the longer ones where we need to focus on covering more content,
approximately 6-8 hour window today so mix learning with revision."* Both halves
were honoured — seven promotions came out of cold asks fired **mixed into** the
material, never as a revision block, and the 1.8 tail was taught end to end.

### The interval gate, and a ruling worth reusing

S32's commit landed at 00:43 on 28 Aug; the session opened at 16:02 the same
calendar day. **The ruling given out loud rather than assumed: a sleep cycle and
~15 hours is later-day evidence and it promotes**, because the S17 gate asks
whether forgetting was *possible*, not whether the date changed. Anything
promoted on it was given a short gap rather than a long one. The session then
ran past midnight, broke for sleep, and finished the next morning — which had
the useful side effect of making the drill, issued at ~00:30, later-day evidence
for everything taught the previous evening including `deepcopy` and `reversed()`.

### The overnight result, and it is the finding of the session

S32 ended having identified something the file had never seen before: not a lost
label but a **missing distinction** — `None` conflated with nothing, twice in one
night, on unrelated mechanisms. It was named precisely and **not drilled**.

Sixteen hours later, cold:

- `len([get_limit(limits, "elbow"), get_limit(limits, "wrist")])` → **2**, with
  the mechanism volunteered: *"the previous line makes a list `[150, None]`"*.
- `len([])` and `len([None])` → **0 and 1**, and he connected it back to his own
  `list()` error himself: *"I confused it with the None"*.
- His `.pop` model repaired unaided: *"`.pop` returns the removed value, and if
  the given key is not there then `KeyError`"* — the exact thing he had had
  backwards.

**The lesson to carry: structural gaps and label gaps need different treatments.**
A label gap needs repetition; this one closed on being named accurately, because
he built the missing piece himself between sessions. **Diagnose which kind it is
before deciding how much drilling it needs.**

### What was taught

**`copy.deepcopy`** — framed first, as the rule requires: what it is (new outer
container and new contents recursively, no floor), why it exists (one level of
copying is not a copy, it is a trap that looks like one), and what it buys (a
snapshot). **And what was explicitly NOT claimed**: it is not the better copy —
slower, and it copies things you may have wanted shared; it buys nothing over
`[:]` on a flat container of immutables; and most of the time the right answer is
to build the data fresh rather than copy it. `import` was given a one-line Level-2
model in passing — it binds the NAME to a module object, and the `.` is the one he
already owns — **discharging an item from the level-1 audit list.**

**`reversed()`** — an iterator that walks a sequence back to front with no copy,
motivated against `path[::-1]` building an entire second list. `print(reversed(path))`
showing the iterator object rather than its contents. He then predicted the
exhaustion case correctly from the `list()` machinery he had repaired two hours
earlier — **transfer onto a construct he had met five minutes before.**

**`*` on a sequence** — taught only because he stopped the session to demand it
(see the mentor section). Repetition builds a new sequence; on `str` too.

**Mutate-while-iterating** — `for` keeps an internal position counter and does not
know the list is changing underneath it. **The replacement pattern is one he
already owns: don't remove, SELECT.**

**`[[0] * 3] * 3`** — `*` repeats the reference, not the contents. He resolved it
himself off the previous night's shallow-copy work, and **interrupted his own
answer with the load-bearing objection** — *"but `[0][0]` is 0 which is not a
mutable"* — which is exactly the discriminator: `* n` is safe when the element is
immutable and a trap when it is mutable.

**When-to-use-which** — the ASK question, framed properly for the first time in
the course. See the mentor section for why that took two attempts.

### The drill

`drills/s33_copies.py` — four bodies against 25 mentor-written tests, issued at
~00:30 and written the following morning. **25/25 green, cold, unaided.**

```python
def snapshot(config):      return copy.deepcopy(config)
def drop_unsafe(a, c):     return [i for i in a if i <= c]
def replay_order(steps):   return [steps[-(i+1)] for i in range(len(steps))]
def missing_joints(r, p):  return set(r) - set(p)
```

**The boundary was kept out of the docstring and put in the tests**, per the S30
cost-of-SPEC-BEFORE-PUZZLE note — and he found it anyway, off the promise:
*"boundary is one thing I needed to take care of, `<=` or `<`, otherwise `mila`
would have come into action."* **That is checks 1 and 5 working as a pair, and it
is the first time in four sessions they have been reported at all.**

`missing_joints` is the quiet win: **set difference was taught in S30 as a
supporting move and had sat untested for three sessions.** One line, cold, and the
container chosen for a job whose only question is *"is this in here?"* — the rule
from ninety minutes earlier, applied rather than recited.

### The demotion

**THE MUTATING TELL, `[x]` → `[~]`.** Asked what rule let him work out
`path.reverse()`, he gave *"a method on a mutable object mutates the object"* —
false. Shown `path.count("home")` as the counterexample he declared an honest gap
on the method itself (*"I don't remember this method"*), and then, asked to
restate the tell, produced *"I cannot come up with the statement as well."*

**Third break of this row in two sessions, in three different directions:** S32
had `.pop(k)` returning nothing because it mutates; S33 had `.count()` mutating
because the object is mutable; then no statement at all. **He keeps rebuilding it
as a two-way rule.** Re-taught with the one-directionality as the headline rather
than a caveat: TYPE FIRST; returns `None` ⇒ it mutated; **a value coming back
tells you nothing**, because `.pop()` returns the item AND mutates.

### The miss that matters most — a name collision

Nine hours after `reversed()` was taught with full runnable output, he did not
reach for it. He wrote `[steps[-(i+1)] for i in range(len(steps))]` and explained:
*"couldn't use reverse because it mutates the list itself."*

**`steps.reverse()` and `reversed(steps)` had merged into one thing on the
strength of their names.** The machinery was intact — his code is correct and
passes — and the tool was invisible. **New watch area: where two constructs have
near-identical names, teach them as a PAIR IN ONE TABLE or he will merge them.**
Prior instances now readable as the same pattern: `sort`/`sorted`,
`remove`/`discard`, `iterable`/`iterator`.

Underneath it, an older habit: **`range(len(...))` index bookkeeping, already
caught in S29** where `zip` removed it. When he computes indices to get at items,
there is usually a built-in that hands him the items.

### Held deliberately

**Constructors stayed `[~]`.** His first word for `dict(defaults)` was still
*"converts it to a dictionary"*; *"the constructor is actually making a new object
from the iterable"* arrived only after the mentor pointed at the word. **A
correction that has to be pulled out is not evidence**, and he was told so in
those terms. It promotes when the right word is his first word.

### Mentor failures — three

1. **DEFINE-BEFORE-USE, SUBSTRATE INCLUDED — TENTH OCCURRENCE, SECOND NIGHT
   RUNNING.** `[[0] * 3] * 3` was fired inside a [PREDICT] and **`*` on a sequence
   had never been taught anywhere in the course.** He stopped it: *"normally for
   brackets we use () but here we are using [], this hasn't been taught."* Every
   note file and the curriculum were grepped rather than argued with; he was
   right; the snippet was withdrawn, repetition taught properly with output, and
   the trap re-issued afterwards. **Pushback 55, upheld in full; running total
   55/54.** The check that was skipped costs one command.

2. **FRAME FIRST (RULES v4) BREACHED.** When-to-use-which was fired as three
   scenarios with no frame. He replied *"I don't understand the question itself"*;
   the mentor rephrased — **the wrong fix, and the same first-fix-solves-the-wrong-
   half shape as S19 and S20** — and only after a second *"I still don't
   understand the question that well"* did it stop and state the unit in one
   sentence. **Two "I don't understand" replies in a row is a frame signal, not a
   comprehension signal.** Two thirds of his answer had been right all along.

3. **AN OVER-CLAIM ABOUT HIS OWN PROGRESS.** *"That closes 1.8"* was said in
   session and was false — five bullets remain `[~]`. Caught during the closing
   procedure by counting them, and corrected to his face before the files were
   written. **This is precisely the class the end-of-session section names: an
   artefact that looks authoritative while being wrong. Missing gets noticed;
   wrong gets believed.**

A fourth, smaller: **the mutate-while-iterating [PREDICT] used data that hid its
own bug.** He predicted it correctly because the code genuinely returns the right
answer on that list. Recovered by making the hiding itself the lesson — and the
recovery was the better teaching — but it was luck, not design. **Choose failing
data deliberately.**

### Student record

- **Seven promotions**, all cold and later-day: format-spec alignment (8/10,
  fourth session live, finally closed on a clean instrument with no arrows);
  `None` is not nothing (7/10); `list()` (7/10, seven sessions overdue); shallow
  copy (7/10); `copy.deepcopy`; set difference; boundary-first.
- **Confidence 7–8 all session and nothing at 7 or above was wrong.** ⚠ **The two
  genuine misses carried no rating at all, because he could not produce an answer
  to rate. Silence is the new low rating — watch for it.**
- **Self-repair, unprompted, twice.** On *"the iterable was empty"* he corrected
  himself to the iterator's forward-only state and classified his own error
  precisely: *"not an error in my concept, was an error in saying."*
- **He stopped an untaught construct on sight** — the fourth consecutive session
  in which the biggest catch of the night was his.
- **Channel: the unsaved-buffer artefact fired once and he caught it himself**
  before anything was read. Down from four in S30 and two in S32.
- Two style corrections issued: `import` belongs at the top of the file, and `i`
  conventionally means an index — `[i for i in angles ...]` should be `[a for a
  in angles ...]`.

### Where 1.8 actually stands

**Ticked this session:** nested data structures `[~]` → `[x]`; copy semantics
`[~]` → `[x]`; common patterns and pitfalls `[ ]` → `[x]`.

**Still `[~]`, and all five are cold-ask shaped rather than teaching shaped:**
`list` (method roster 3/6, plus the fresh `.count()` gap), `tuple` (taught in full
S26, never given a task-first pass), `dict` (`.keys()`/`.values()` as views never
asked), `set` (order instability and `{}`-is-a-dict never asked), and
when-to-use-which (taught properly only today, so ineligible until S34).
**One focused block closes the subsection.**

**No rule was adopted. The parking lot is deliberately empty** — both process
failures this session were breaches of rules that already exist, and the file's
own S32 precedent says to fix the behaviour rather than grow the rulebook.

### What Session 34 established

**A short, same-sitting session — ~2½ hours, a few hours after S33 closed — and
it was declared as such before a single question was asked.** One curriculum
tick, two ledger promotions, and three findings that are worth more than the
tick.

- **THE INTERVAL GATE DID REAL WORK, UNPROMPTED, AND IT SHAPED THE WHOLE
  SESSION.** Told the gap was a few hours, the mentor split the plan out loud:
  everything S33 *taught* — the mutating tell, `reversed()`, `*` on a sequence,
  mutate-while-iterating, when-to-use-which, constructors — was **deferred as
  echo**, and only S24–S27 material was put on the table. **The direct
  consequence was stated at the OPEN rather than discovered at the close: 1.8
  could not close today, because `when to use which` was un-askable.** That is
  the exact correction of the S33 over-claim, made one session later and made
  *in advance*.

- **THE HEADLINE FINDING IS A GATE DEGRADING, AND IT IS THE NEXT LESSON AFTER
  S33's.** S33 got the five checks reported for the first time since S25 by
  making them the gate on the word "done". S34 got a fluent, confident report —
  *"khaali actually taken care of by if condition, ek also taken care of, bahar
  also taken care of"* — **on two functions that both failed, one of them on the
  worked example printed in its own docstring.** He had written the report by
  reading his own code and seeing an `if`.
  **S33's lesson was: change WHERE an ask sits in the workflow. S34's is the one
  after it: an ask that can be satisfied without executing anything will be.
  Demand the ARTEFACT — the case, the value that came back, matched or not.**

- **THE MUTATING TELL IS NOT A RUIN. S34 PROVED WHICH THIRD IS GONE, AND FOUR
  SESSIONS OF RE-TEACHING HAVE BEEN AIMED AT THE WRONG TARGET.** In `ranked` he
  wrote, unaided and unprompted: *"could have also used values.sort() but that
  will mutate the passed list so not using that."* **TYPE owned. MUTATES owned.**
  Ninety seconds later, in the next function but one, he wrote
  `list(set(names.sort()))`. **The only missing piece is that a mutating method
  hands back `None`.** Teach that third alone.

- **`reversed()` BROKE IN THE OPPOSITE DIRECTION TO S33, ONE DAY LATER — and
  that makes it the cleanest name-collision evidence in this file.** S33: he
  avoided `reversed()` because *"it mutates the list itself"*. S34: he reached
  for `reversed(list(set(names)))` to satisfy a docstring asking for **ascending
  alphabetical** order. Avoided as a mutator, then deployed as a sorter. **Two
  opposite errors on one pair in twenty-four hours is what a floating label over
  intact machinery looks like.** The S33 remedy stands and is now overdue:
  **teach collided names as a PAIR IN ONE TABLE.**

- **HE DEBUGS WELL WITH A TRACEBACK AND POORLY WITHOUT ONE, AND THIS IS THE SAME
  ROOT AS THE FIVE-CHECKS FAILURE.** Shown the failing line under the S27
  error-naming rule, he could not label it at all and said so honestly: *"I can't
  see the fault, that's the thing, I believe its correct"* — then described a
  perfectly sound three-step intent. Shown the traceback, he found it in one
  line, unaided: *"ah fuck .sort returns None."* **The reasoning is not the gap.
  Not running the thing is the gap.** That is the strongest argument yet for the
  five checks being executed rather than asserted, and the two findings should be
  read together.

- **THREE WRONG FIXES BEFORE THE RIGHT ONE — AND THE MIDDLE ONE WAS THE BEST
  MOMENT OF THE SESSION.** `sorted(...)` → `list(set(sorted(names)))` →
  `reversed(list(set(names)))` → `sorted(list(set(names)))`. Asked to trace the
  second, **he demolished his own proposed fix using the set-unordered fact he
  had been promoted on twenty minutes earlier**: *"oh right set doesn't store
  elements in a sequence."* **He self-corrects reliably when asked to trace and
  not at all when asked to write.**

### Student record

- **Two promotions**, both cold and later-day: **set is UNORDERED** (7/10 — named
  unprompted off his own failing output, then sharpened from *"doesn't have a
  fixed order"* to **unordered**, no positions at all, which is why a set is not
  subscriptable); and **`sort` vs `sorted`**, the clean cold pass CURRICULUM had
  recorded as owed since the S24 inversion.
- **ONE CURRICULUM TICK: 1.8 tuple `[~]` → `[x]`**, on the task-first cold pass
  owed since S26. ⚠ **An echo caveat was written next to the tick rather than
  hidden**: `.count()` had been an honest gap hours earlier in S33.
- ⚠ **`list` WAS HELD `[~]` DELIBERATELY.** Its roster, slicing and
  `sorted`/`.sort()` were all clean, but the bullet's own named core — the
  returns-`None` tell — failed live in his code the same hour. **A bullet whose
  load-bearing half breaks in front of the mentor does not get ticked.**
- **He declared an honest gap rather than guessing** (the unnameable error), and
  **self-reported fatigue unprompted** — *"I am actually doing this for long, and
  lost my concentration"* — immediately before producing the correct answer.
- **He closed the session himself and set the next one.** Session length was his
  call throughout; the mentor stated what remained and did not propose an end.
- ⚠ **Only one confidence rating was taken all session, because the mentor did
  not ask.** The S33 finding got a second instance: **the genuine misses carried
  no rating at all, because he could not produce an answer to rate. Silence is
  the low rating.**
- **Channel: mtime caught an untouched file on the first "Done"**, and nothing
  was said about his code until he confirmed it was saved.

### Teaching mistakes this session

1. ⚠⚠ **A GATE WAS MADE IMPOSSIBLE TO DISCHARGE — and this is the worst shape in
   the file, because it punishes the student for the mentor's error.** The five
   checks were correctly enforced on the word "done", **twice**. But the form
   demanded was `python3 -m pytest`, and **STATE item 8 has said for two
   sessions that pytest is not taught, is not scheduled in Layer 0, and is never
   his to run.** He was held to a standard the channel could not deliver, and he
   had to stop it himself: *"I am not able to run the test myself, can you do
   that, don't delay the session for unnecessary things."* **Pushback 56, upheld
   in full.** THE RULE THAT ALREADY COVERS IT: channel before blame. **THE
   EXTENSION WORTH CARRYING: check that an instruction is EXECUTABLE BY HIM
   before enforcing it — enforcing an impossible instruction is worse than not
   enforcing at all, because it spends his goodwill on the gate itself.** The
   five checks are discharged by calling his own function and looking at what
   comes back.

2. ⚠ **A PROMISED ASK WAS NEVER FIRED, AND IT BLOCKS A CURRICULUM BULLET.** After
   `shared_keys` the mentor said out loud that it would ask what `a.keys()` is
   and why `&` works on it — **the last thing standing between the 1.8 dict
   bullet and `[x]`** — and then lost it to the `unique_sensors` debugging.
   **Write a promised ask into the resume point the moment it is made.**

3. ⚠ **THE SESSION'S ONE RAISING SNIPPET ARRIVED BY ACCIDENT.** S30–S33 each
   built a deliberate one; S34's came out of his own bug. It worked well and the
   S27 error-naming rule fired cleanly on it — **but it was luck, not design,
   which is the second session running that this has been written down.**

**Pushback 57, part-upheld, and both halves were said to his face.** He argued
that revision should be random and spread across days rather than
*"this-yesterday-should-be-tested-today"*, and that finishing a subsection should
not require `[x]` on every bullet first, *"because what if I do correct today and
forget them after some day?"*
**UPHELD, and it is the more important half: random spaced recall is already this
file's binding doctrine** (RETENTION SYSTEM 2, 3 and 5), **and the evidence that
its hand-execution has failed is overwhelming** — `while` mechanics eight
sessions overdue, `.keys()`/`.values()` never asked since S26, `SyntaxError`
missed in S27 and again in S32.
**NOT UPHELD, on the facts: S34 did not test S33's material.** Everything asked
was S24–S27, two to five days cold, and all S33 material had been deferred at the
open for precisely his reason.
⚠ **What he has actually re-derived, independently, is RULES proposal 6 — move
the re-test queue into a SCRIPT once it passes ~30 rows. It is at 75+, it has
been settled since S21, and it is designated build block 02.** The ruling was
parked to the S35 open under the rule-change cap, **with the mentor's
recommendation recorded as: do not write a rule, build the tool.**

**No rule was adopted. RULES stays at v5.**

## What Session 35 established (Sunday 30 August 2026 — ⚠ date disputed, see mentor failure 4)

**THE SESSION IN ONE LINE: 1.9 was opened and half-taught, the 1.8 `set` bullet
closed in three minutes, the four-station hook was retired as a failed artefact
and replaced with a question, the re-test queue became a script — and the drill
came back 29/29 on the first run.**

### 1. THE HEADLINE STUDENT FINDING: A TRANSFER GAP, NOT A KNOWLEDGE GAP

This is the most important thing in the session and it must not be softened.

He was shown, live, a file where a one-character typo inside a `try` was
"handled" by a bare `except:`. The output was:

```
skipping bad reading: 45
skipping bad reading: 90
skipping bad reading: n/a
skipping bad reading: 30
total: 0
```

No crash. Exit code 0. Two perfectly good readings reported as junk. He was
asked which was more dangerous, the crash or the `total: 0`, and answered
unprompted and correctly: ***"obviously total:0 is more dangerous, because you
ended up believing that program is running fine, and never got to know where was
the error."*** The word *believing* was his.

**Forty minutes later he wrote `except: pass` in his own `total_valid`.**

**The tests did not catch it, because nothing else in them raises.** It was
found by reading his code at the close. Shown the line and asked what
`total_valid(["45", None])` returns, he named it immediately and correctly —
*"total_valid doesn't raise any exception at all, that's the worst possible
behaviour… it hands back 45."*

**THE DIAGNOSIS, and it is a new one for this file: he could PREDICT it, he could
JUDGE it, and he did not APPLY it.** Every previous finding here has been about
retention — a fact that faded. This one did not fade; it was live and correct in
his mouth in the same hour. **S33's lesson was "change WHERE the ask sits".
S34's was "an ask that can be satisfied without executing anything will be".
S35's is the next one: THE TEST OF A TAUGHT IDEA IS WHETHER IT APPEARS IN HIS
NEXT FILE, NOT WHETHER HE CAN PREDICT IT.**

### 2. AN ARTEFACT FAILED TWICE, AND WHAT REPLACED IT WORKED FIRST TIME

Asked to name the four-station hook's stations in order — a pure cold [RECALL],
last fired S32 — he said: ***"yes I still don't remember that hook, it has not
been working for me."***

**That is the SECOND artefact failure on this exact material.** The S26 error
TABLE failed inside twenty minutes and the hook was built to replace it. The
hook has now failed outright. **The diagnosis was given to him plainly and it is
this file's own Term Retention System read back: NAAM → DOT → TYPE → CHEEZ is
five arbitrary words stacked on top of machinery he already owns, which is
precisely the thing he reliably drops. Logged against the artefact, not against
him.**

**THE REPLACEMENT IS A QUESTION, NOT A LIST: "HOW FAR DID PYTHON GET?"**

Fired immediately on `angles["shoulder"]` against a dict without that key, he
walked the entire timeline unaided, and — the part that matters — **he started
at syntax without being told to**:

> *"first thing is always the syntax, if the syntax isn't right the code can't be
> [run]… second line again syntax is ok, now as we go inside the print function,
> angles — does that name exist? yes… but the key "shoulder" doesn't exist so
> key error."*

Self-rated **6**, and under-rated. **This is the S17 discriminator ruling applied
to error labels: give him a question he can ask the code, never a roster.** The
same move that killed the mutating-methods roster in S17 has now killed the
error-label roster.

### 3. HE DERIVED THE COMPILE/RUN SPLIT HIMSELF, OFF ONE TRACEBACK

Third session running with an unprompted derivation (S32 shallow copy, S34 the
set-unordered demolition of his own fix, now this). Shown that a missing colon
on line 5 stopped line 1 from printing, he stopped and volunteered:

> *"so python compiler is compiling the file to bytecode, and all the syntax
> error is checked there itself, and if one exist its pointed out. Ok now once
> the bytecode is there, then execution starts, and then we come towards the
> other errors — am I saying correct??"*

**He was.** It was confirmed, and sharpened with the one thing missing: **the
compiler checks GRAMMAR, never MEANING.** Proved by running two files side by
side — one whose line 1 printed despite a typo'd NAME on line 5 (`NameError`,
runtime, WITH frames), one whose line 1 did **not** print because line 5 was
missing a colon (`SyntaxError`, compile time, **no frames at all**).

**The tell he now owns: `SyntaxError` is the only error he will meet with no
traceback frames. If there are frames, something ran.** `.pyc` and what the
bytecode actually is were parked to 1.10, with the promise recorded.

### 4. `SyntaxError` — HALF CLOSED, AND THE OTHER HALF BROKE IN THE SAME BREATH

Fired cold in a **new shape** (a missing colon, not S27's and S32's
statement-inside-`print`, which he had missed twice five sessions apart).

**LABEL: HIT. First time in three firings**, with the cause named — *"for loop
needs a `:` where the for line ends."*

**NO-FRAMES HALF: MISSED.** Asked whether `checking limits` on line 1 appears
before the error, he said *"yes it will appear because that line already executed
without any problem."* It does not. **He rated that 7/10 — his first over-rating
in a long stretch; his documented signature is under-rating.** Row held `[~]`.

### 5. TWO ONE-LINE ASKS CLOSED A CURRICULUM BULLET IN THREE MINUTES

Both were queued at the S34 close and both were S27 material, seven days cold —
legitimate regardless of how the interval gate was ruled.

**`set()` vs `{}` — PROMOTED, 7/10, and it CLOSES THE 1.8 `set` BULLET.** He
wrote both lines cold and attached the mechanism to each without being asked:
*"seen = set() — set for unique value; limits = {} — dictionary for mapping
between names to numbers."*

**`.keys()` as a VIEW — honest gap, declared precisely**, and the precision is
the useful part: *"I don't know what will be the datatype of dict.keys() and the
& operation is valid for sets only."* **He had named the exact unknown.** Taught:
a view **BUILDS NOTHING** — it is a live window, which is why `set(a) & set(b)`
works but does more work than it needs to, and why the view saw a key added
after it was made. His second clause was corrected too: **`&` is valid for any
TYPE that defines it**, which is his own `TypeError` rule read forwards.
**The 1.8 `dict` bullet is now unblocked but NOT closed — the view was taught
today, so it cannot be tested today. One cold later-day ask closes it.**

### 6. `TypeError` vs `ValueError` WOBBLED, AND HE DIAGNOSED IT HIMSELF

Volunteering a revision unprompted, he offered `1 + "a"` **and** `int("2.6")` as
`ValueError`. The first is a `TypeError`. **Recovered in full on a one-line
narrowing** — with the right mechanism both ways and a good counter-example he
produced himself (*"if 1 was "1" then "1"+"a" will become 1a"*).

His own account of it is the finding: ***"this is my problem, its old content,
not being revised for long, although I got it correct earlier, now I forgot
because we didn't use it for long."*** That is the argument for the script,
stated by him, an hour after he ruled the script into existence.

**Discriminator given, and it replaces his longer route through "stages of
conversion": change only the VALUE and it works ⇒ `ValueError`; change only the
TYPE and it works ⇒ `TypeError`.**

### 7. HE TALKED HIMSELF OUT OF A CORRECT ANSWER

Asked whether `finally` runs when the raised exception matches no `except`, his
first instinct was right — *"should[n't it be] like the other cases"* — and he
then reversed it: ***"but since you are specifically showing this case I presume
not."***

Named to his face, without softening, because it is an interview-cost behaviour:
**the framing of a question is not evidence. If your model says X, say X and let
the code disagree with you.** Compounding the point, the answer was already on
screen: the demonstration two minutes earlier had **no `except` at all** and
`finally` still ran.

### 8. THE DRILL: 29/29 ON THE FIRST RUN

`drills/s35_faults.py`, four functions, every signature and expected value given
(SPEC BEFORE PUZZLE held; the boundary case `angle == limit` was kept out of the
docstrings and put in the tests, per the S30 cost note).

- `total_valid` — try/except inside a loop ✅ (but with a **bare** `except:`)
- `check_angle` — `raise ValueError(...)` with a message naming both numbers ✅
- `safe_angles` — decides via `check_angle` and holds **no second copy of the
  rule**, enforced by a source-inspecting test, **passed first run** ✅
- `measure` — `try` / `finally`, cleanup on every exit path, failure still
  propagates ✅ — written correctly after **one** pointing question

**A reference solution was written and run against the suite before issuing, so
29/29 was known to be reachable.** Two style notes carried forward: a leftover
debug `print` in `measure`, a `print(e)` inside `safe_angles` (a library function
that prints has decided the caller's output policy — the same division-of-labour
point `raise` was taught with), and `{angle:4.1f}` rendering an `int` reading as
`200.0`.

### 9. THE RE-TEST QUEUE IS NOW A SCRIPT — the first structural fix to the retention system since the four-file split

The S34 ruling was taken at the open. Recommendation put in one line — *do not
write a rule; the policy is already doctrine and what failed is its execution by
hand* — and **he ruled: "do the script."** He then added the constraint that
makes it a mentor tool rather than a curriculum item: ***"maintain it in such a
way that I don't need to know about it, and you can audit it whenever you
want."***

Built and committed this session: **`tools/retest.py` + `tools/queue.json`,
121 rows seeded from STATE.md** — 67 `[x]`, 54 `[~]`, 12 overdue, 12 never
asked. It selects what is due, shuffles it, pins the three worst offenders, and
records results (`--asked "<term>" --result pass --rating 7`) with the interval
set from the rating per RULES proposal 2. **The queue table has been deleted
from STATE.md.**

⚠ **CONSEQUENCE: BUILD BLOCK 02 HAS LOST ITS TASK** and needs a new one.

### 10. THREE PUSHBACKS, ALL UPHELD IN WHOLE OR PART — running total 60/59

**(58) UPHELD IN FULL, and it is the best one he has ever raised.** Handed a
[PREDICT] built on `raise ValueError(f"...")`, he refused to answer it:
***"wait am I eligible to answer this because : raise statement ValueError() and
you are using it as a function this is totally unknown to me."***
**Define-before-use, substrate included — ELEVENTH occurrence.** And it is a
first: on the previous ten he answered anyway and the breach was caught
afterwards. **Here he invoked the eligibility rule himself, before answering,
and stopped the block.** The repair became the best teaching of the session:
every error name is a **CLASS**; `ValueError("…")` is a **constructor call** that
**builds** an exception object; and **the text after the colon in every traceback
he has ever read is that constructor's argument.**

**(59) PART-UPHELD.** On being shown the five-checks reporting form he objected
to the cost: *"for such an extensive list I will have to test the function by
writing it somewhere else… my learning time will reduce a lot."* **He was right
that the mentor had silently escalated past his own S24 ruling — SCAN all five,
REPORT only the ones that bite.** The execution requirement stood (S34's
reported-but-not-run failure is why it exists) and **the cost was fixed with a
TOOL, not a lecture**: `drills/s35_check.py`, a runner that calls his functions
with the five-check cases and prints what came back, judging nothing. Same shape
as the queue ruling an hour earlier: **fix the behaviour, build the tool, do not
grow the rulebook.**

**(60) UPHELD.** He proposed the new drill flow: *"I will just do the Done words
and you execute the test on the drill file, and if some error comes, you can ask
me to find the error, then I will implement the check."* **Right on the
economics — the mentor's tests already cover boundary/khaali/ek/bahar, so
hand-running them duplicated work.** The counter he accepted immediately (*"this
makes more sense"*): **before the tests run, one line naming the function he is
least sure about and the case that worries him.** **First data point was
excellent — he flagged `check_angle` for missing `bahar`-by-TYPE**, the subtle
half of check 4, unprompted. Ruled out of scope (the spec says `angle : int`),
same ruling as his own S24 `take_last([])` call. **Parked as the S36 rule
candidate.**

### MENTOR FAILURES

1. ⚠⚠ **DEFINE BEFORE USE, ELEVENTH OCCURRENCE** — pushback 58 above.

2. ⚠ **A DEFECTIVE SNIPPET.** The first bare-`except:` [PREDICT] typo'd a
   variable as `reading`, one character from the list `readings`. He read it as
   the list and answered `TypeError` — **correct reasoning for the snippet he
   saw.** Owned in session and re-posed with an unmistakable name.
   **A snippet that tests attention instead of the concept is a defective
   snippet.**

3. ⚠ **AN ACCIDENTAL [TEACH-BACK] TAG COST A PROMOTION.** Asked what `set(a)`
   builds, he answered *"the constructor of the set **builds** the set object
   over the iterable passed to it"* — **the exact first word the `constructors`
   row has been waiting for since S33, unprompted.** It could not be banked,
   because the block had been tagged [TEACH-BACK], which is never
   ledger-eligible. Said to his face, cost accepted. **Check the tag before
   posing, not after — a wrong tag costs in both directions.**

4. ⚠⚠ **THE INTERVAL GATE MAY HAVE BEEN RULED ON THE WRONG DATE, AND THIS IS THE
   ONE TO FIX.** The session was declared a **same sitting** at the open on two
   pieces of evidence: the model's own context header (29 Aug) and his *"today
   is saturday"*. **Every file mtime and the system clock at the close say Sunday
   30 August.** If the 30th is right, S34's material was eligible all along and
   was deferred for nothing — a whole session of promotable evidence discarded.
   **The ledger is NOT corrupted: everything promoted in S35 was S27 material,
   seven days cold under either reading.** The cost is opportunity, not accuracy.
   **THE RULE-SHAPED LESSON, and it is the S15 stale-file lesson in a new
   costume: DO NOT REASON FROM MEMORY OR FROM A HEADER ABOUT A FACT YOU CAN
   CHECK. Verify the date from `git log -1` and file mtimes before ruling the
   gate.**

**No rule was adopted. RULES stays at v5.** The S36 candidate is parked in
STATE.md with the mentor's recommendation recorded as **adopt**.
