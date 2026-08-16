# ROBOTICS CAREER CURRICULUM — MASTER REFERENCE FILE
# Target: £80k+ UK robot-learning / embodied-AI role by March 2027
# ═══════════════════════════════════════════════════
# HOW TO USE THIS FILE (for Claude):
# This is the master context document for Ankur's complete robotics
# career preparation. It ABSORBS the existing Python Learning Journey
# file — it does not replace it.
# 1. Read this file fully before responding
# 2. GOVERNANCE RULE: Until Layer 0 (Python Core) is closed, the
# Python Learning Journey file governs sessions — its rules, its
# "Where We Left Off", its session structure. After Layer 0 closes,
# THIS file governs every session.
# 2a. SINGLE-FILE SESSION PROTOCOL (adopted post-Session 14, 8 Aug 2026,
# at the student's request to cut per-session context load): during
# Layer 0, this master file is NOT loaded at session start. The Python
# file alone runs the session — every session-relevant binding rule,
# watch-area and queue is mirrored there (including the North Star).
# This file is loaded at SESSION END, after teaching is done, so both
# files are updated together and returned as downloads. EXCEPTIONS —
# load this file at session START when: (a) it is a monthly checkpoint
# / gauntlet session; (b) a scope decision or re-baseline is on the
# agenda; (c) the student explicitly asks. Both files are still
# updated every session; only the load timing changed.
# **SESSION 15 PRECEDENT: the student asked mid-session for a schedule
# review against the original plan. That is exception (c) and it
# correctly triggered loading this file mid-session. A plan question
# answered from memory is a guess; this file exists to prevent that.**
# **SESSION 18 CONFIRMED THE PROTOCOL'S COST AS WELL AS ITS BENEFIT.
# The protocol worked — the session ran long and taught well on the
# Python file alone — but the master update then had to be produced
# after a context compaction, from a file read fresh at the end. That
# is survivable and it is still the right trade, but see the new
# FILE-GROWTH note at the 31 Aug checkpoint: both files are now large
# enough that their SIZE is itself a scheduling variable, and the
# student raised this himself at the S18 close.**
# 3. All teaching-style agreements, coaching standards, watch areas,
# and behavioural patterns from the Python file carry over VERBATIM
# to every layer of this curriculum. They are summarised below but
# the Python file remains the authoritative record of Sessions 0–18.
# 4. At the end of every session: update the governing file, produce
# session_<N>.pdf notes (with Thinking Gaps + Teaching Mistakes
# sections + Reference Checklist), and RETURN BOTH FILES TO THE
# STUDENT FOR HIM TO UPLOAD MANUALLY. **DO NOT attempt to upload to
# Google Drive directly — Drive upload has failed at session end in
# Sessions 10, 11 and 12. Hand the files back as downloads every
# time; the student uploads them himself. This is now the standing
# procedure, not a fallback.** Non-negotiable. Saved filenames
# follow: <name>_<YYYY-MM-DD>_v<N>.md — version LAST.
# **4a. READ THE LATEST VERSION, NOT THE FIRST SEARCH HIT (added Session
# 15 after a serious mentor failure — see the Session 15 addendum).
# Both files live in Drive as a numbered series. A stale unversioned
# `robotics_career_curriculum.md` from 31 Jul 2026 ALSO still sits in
# the same folder and ranks in search results. BEFORE READING EITHER
# FILE: list the folder, sort by version number, and open the HIGHEST
# v<N>. Confirm the version line inside matches. If the file you have
# open does not carry a VERSION header at all, it is the stale copy —
# stop and find the right one.**
# **4b. THE TWO FILES LIVE IN DIFFERENT FOLDERS — added Session 16, and
# it is the missing piece that made 4a keep failing in practice. A
# search scoped to the Python folder returns NOTHING for the master,
# which reads like "the file does not exist" rather than "you are
# looking in the wrong place." The verified map is in the DRIVE MAP
# section below and is mirrored in the Python file. LIST BY parentId;
# do not search by title and hope.**
# **4c. SEQUENCING THE END-OF-SESSION DELIVERY IS ALLOWED; SILENCE IS NOT
# (added Session 17). Both files are now large — Python ~160 KB,
# master ~140 KB — and reproducing them faithfully in a single pass is
# where corruption happens. Delivering the governing file first and
# this one second, in separate messages, is acceptable PROVIDED THE
# SPLIT IS STATED TO THE STUDENT WHEN IT IS MADE. What is not
# acceptable is quietly delivering one and letting the other slide —
# that is the exact failure that produced 4b.**
# **SESSION 18 EXERCISED 4c AS DESIGNED AND IT HELD: the split was
# announced, the Python file and the session PDF went first, and this
# file followed. The rule is now demonstrated rather than theoretical.
# The remaining risk it does NOT cover is a context compaction landing
# between the two deliveries — which is what happened in S18. The
# countermeasure is to state the outstanding half explicitly in the
# message that makes the split, so the debt survives a context reset.**
# 5. Do NOT ask for re-introductions. Continue from the tracker.
# 6. RECONCILED 29 Jul 2026 (Session 6). RECONCILED AGAIN 31 Jul 2026
# (Session 8): the nine voice-era rules. AGAIN 31 Jul 2026 (Session 9):
# language-precision corrections; reinforced proactive mode-switch.
# AGAIN 1 Aug 2026 (Session 10): the short-form cross-check.
# AGAIN 1 Aug 2026 (Session 11): THE DEPTH DOCTRINE, the north star,
# and the recall-first-notes-second rule.
# AGAIN 3 Aug 2026 (Session 12): THE TERM RETENTION SYSTEM (the
# "recall thing" — name-decoding, term-tax at session open, no naked
# terms) mirrored here from the Python file; and the file-return rule
# in point 4 made explicit and binding.
# AGAIN 8 Aug 2026 (post-Session 14): SINGLE-FILE SESSION PROTOCOL
# (point 2a) — Python file alone at session start; master at session
# end, on request, and at the start of checkpoints/gauntlets. The
# NORTH STAR was mirrored into the Python file the same day.
# AGAIN 8 Aug 2026 (Session 15): CONFIDENCE AFTER RECALL, NEVER AFTER
# THE ANSWER (new binding rule, below); and the READ-THE-LATEST-VERSION
# rule at point 4a.
# AGAIN 9 Aug 2026 (Session 16): THE FIVE PROCESS-INTEGRITY RULES
# (below), plus the DRIVE MAP at point 4b and its own section.
# Produced after five mentor failures in one session, three of which
# the student caught in real time. The governing insight is not any
# single rule but the root cause they share: SPEED IS NEVER A REASON
# TO SKIP A GATE. A backlog is not licence. This file carries a
# zero-margin schedule to March 2027, which means the pressure that
# produced those failures is STRUCTURAL and will recur in every
# layer — it was not a one-off bad session.
# AGAIN 10 Aug 2026 (Session 17): THE THREE INSTRUMENT-VALIDITY
# RULES (below) — the interval gate, ambiguous assent, and
# whitespace-is-not-testable — plus point 4c above. Where the Session
# 16 five fix protocol steps SKIPPED under time pressure, these three
# fix the opposite failure: protocol steps EXECUTED after the
# circumstances that justified them had already changed. The written
# plan is a plan, not an instruction set.
# **AGAIN 10 Aug 2026 (Session 18): THE TWO SESSION 18 RULES (below) —
# the [TEACH-BACK] instrument tag, and SESSION LENGTH IS THE STUDENT'S
# CALL. Both came from mentor failures the student caught. Read them
# alongside the S17 three: S16 fixed gates SKIPPED, S17 fixed gates
# RUN PAST THEIR VALIDITY, and S18 fixes the mentor SUBSTITUTING ITS
# OWN JUDGEMENT for his on decisions that were never the mentor's to
# make.**
#
# CHECKLIST LEGEND:
# [ ] = not started
# [~] = introduced / partially covered — not drilled, not complete
# [x] = fully covered, drilled, student demonstrated understanding
# WITHOUT AI assistance and WITHOUT notes
#
# VERSION: v13, 16 Aug 2026 (Sessions 19 AND 20). Supersedes v12 of 10 Aug 2026.
# ⚠ **THIS VERSION COVERS TWO PYTHON SESSIONS, NOT ONE, AND THAT IS A LOGGED
# PROCESS FAILURE.** The master was NOT updated at the close of Session 19 on
# 12 Aug 2026 — v12 was re-uploaded unchanged alongside the Python v15. The
# END-OF-SESSION PROCEDURE exists precisely to prevent this and it was not
# followed. **S19's master-level content is written into this version
# retrospectively, from the Python file's record, and is marked as such.**
#
# **SESSION 20 (Sun 16 Aug 2026) IS THE SESSION THAT FOUND A DEFECT IN THE
# LEDGER ITSELF, AND THAT MATTERS MORE AT MASTER LEVEL THAN ANY SUBSECTION.**
# `traceback` had been fired as a [RECALL] in S16, S18 and S19 and logged three
# times as a student failure — including once as "PRIORITY, the lowest
# self-rating of the session". In S20 it emerged that the item had **NEVER BEEN
# TAUGHT, only repeatedly ASKED.** Three sessions of measurement were measuring
# a hole in the delivery. The prior results are STRUCK as invalid and the clock
# is reset. **THE GENERALISABLE RULE, and it belongs at master level because it
# applies to every layer of this curriculum: A REPEATEDLY-FAILING ITEM IS
# EVIDENCE ABOUT THE TEACHING BEFORE IT IS EVIDENCE ABOUT THE STUDENT. Audit
# any carry-forward item that has failed three or more times against a single
# question — was it ever actually delivered, or only ever asked?**
#
# **RECURSION WAS FINALLY TAUGHT after four deferrals, PURE FUNCTIONS vs SIDE
# EFFECTS with it, and EDGE-CASE ANALYSIS WAS ADDED TO THE CURRICULUM AS A NEW
# SUBSECTION (1.7.11) AT THE STUDENT'S DIRECT REQUEST.** He named the gap
# himself and was right that nothing in this curriculum taught it. **1.7 now has
# four items left and one session should close it.**
#
# **THREE NEW BINDING RULES, ALL THREE THE STUDENT'S, ALL THREE ABOUT
# BANDWIDTH: the DOUBT GATE, the RESPONSE LENGTH CAP, and DEPTH-BEFORE-ANSWER.**
# The second carries information this curriculum did not have: **he does not
# read long messages to the end.** That single disclosure retro-explains a run
# of logged "student lapses" across S19 and S20. **Mirrored into the Python file
# and binding across every layer of this one.**
# **Running total of correct student pushbacks: TWENTY-FIVE, still zero wrong.**
#
# VERSION: v12, 10 Aug 2026 (Session 18). Supersedes v11 of the same day.
# **SESSION 18 IS THE HIGHEST-YIELD RETENTION SESSION OF THE COURSE SO FAR,
# AND IT IS THE SESSION THE INTERVAL GATE WAS BUILT TO MAKE POSSIBLE.** It ran
# on Monday evening 10 Aug, a genuine later day after the S16/S17 Sunday
# double. The interval gate was checked FIRST, PASSED, and the deferred
# exception-family block — the oldest outstanding diagnostic in the course and
# the cluster this file has called its weakest — finally ran.
# **SEVEN ITEMS PROMOTED [~] → [x] ON GENUINE LATER-DAY COLD EVIDENCE:**
# `NameError`, `ValueError` and `TypeError` (the triad that was conflated
# THREE TIMES in one session in S16 — now clean, fired in mixed order, 8/10),
# exceptions-are-signals (7/10), `StopIteration`'s category (7/10), and the
# mutable/immutable discriminator (10/10). **THE EXCEPTION FAMILY IS NO LONGER
# THE WEAKEST CLUSTER IN THE FILE.**
# **THREE ITEMS HELD AT [~], AND THEY ARE NOW THE WHOLE OF THE WEAK LIST:**
# `traceback` (3/10 — he has the object but missed the UNCAUGHT trigger),
# ITERATOR CAUSATION (3/10, **failed a THIRD time on a THIRD separate day** —
# the most durable defect in the course), and `__defaults__` (**a FOURTH cold
# miss; the only item in the file never once produced cold**).
# **1.7 (FUNCTIONS) OPENED AND IS ROUGHLY TWO-THIRDS TAUGHT:** def-vs-call,
# parameters-vs-arguments, return and implicit `None`, LEGB (with E established
# as LEXICAL, not dynamic), default arguments, functions as first-class
# objects, and nested functions by definition. **CLOSURES WERE DESCRIBED AND
# THEN DELIBERATELY NOT TAGGED AT THE STUDENT'S OWN INSTRUCTION** — he judged
# the treatment too thin to count and asked for it to reopen from scratch in
# TEXT. **RECURSION HAS STILL NOT STARTED. He has now deferred it three times
# himself, and it remains the thing he most wants.**
# TWO MASTER-LEVEL BINDING CHANGES: **THE TWO SESSION 18 RULES** — the
# [TEACH-BACK] tag (a fourth instrument, carrying NO rating and never
# ledger-eligible) and **SESSION LENGTH IS THE STUDENT'S CALL** (the mentor
# does not propose ending a session; it reports state and asks).
# **THE RUNNING COUNT: EIGHTEEN correct process pushbacks by the student,
# ZERO wrong — and the S18 five include him correcting a RULE THE MENTOR HAD
# JUST TAUGHT HIM, which is the strongest single instance on record.**
# VERSION: v11, 10 Aug 2026 (Session 17). Supersedes v10 of 9 Aug 2026.
# Session 17 began late on Sunday 9 Aug and ran into Monday 10 Aug, starting
# only a short time after Session 16 ended. **PYTHON SUBSECTION 1.6 (CONTROL
# FLOW) IS CLOSED.** The owed found-flag exercise was completed and loop
# `else` was earned by contrast rather than told; `pass`, ternary expressions
# and the loop-pitfalls block were taught; the owed `if`/`elif`/`else`
# confirmation was answered cold and PROMOTED to [x]; and the
# mutating-vs-non-mutating IDENTIFICATION drill — the debt created when the
# student asked for his own S16 demotion — was delivered at 4/5.
# **THE STRUCTURAL FACT THAT GOVERNS HOW TO READ THIS SESSION: its evidence is
# SAME-DAY.** Everything taught is [~] and stays [~]. The three planned recall
# blocks (exception family, iterator causation, modulo identity) were DEFERRED
# OUT of the session — by the student, before a single question was answered.
# ONE MASTER-LEVEL BINDING CHANGE:
# **THE THREE SESSION 17 RULES — the INSTRUMENT-VALIDITY block.** All three
# were caught by the student, and the first is the most consequential
# governance addition since the Session 16 five: **a recall test run at too
# short an interval does not merely fail to inform, it CORRUPTS THE LEDGER**,
# because a pass gets written in as later-day evidence. He stopped it.
# ALSO RECORDED: the mentor misread a one-word reply and opened Layer 0's next
# subsection against his explicit request to close the session; that material
# was discarded at his instruction and appears in neither file.
# **THE RUNNING COUNT NOW MATTERS AS A DATUM IN ITS OWN RIGHT: thirteen
# correct process pushbacks by the student, zero wrong.**
# VERSION: v10, 9 Aug 2026 (Session 16). Supersedes v9 of 8 Aug 2026.
# Session 16 ran on SUNDAY 9 Aug — a genuine LATER DAY after the S14+S15
# Saturday double, which is what made it the highest-yield ledger session of
# the course so far. THE 8–12 AUG PROMOTION PASS WAS RUN AND CLEARED: nine
# Python items moved [~] → [x], including `==` vs `is` (owed since Session 7)
# and the negative-`%` case (one of the two items this file repeatedly called
# weakest). Six terms also promoted. 1.6 is now nearly closed.
# THREE BINDING CHANGES AT MASTER LEVEL, all from Session 16:
# (1) THE FIVE PROCESS-INTEGRITY RULES — instrument tagging, prerequisite
# gate, no-promotion-without-confidence, mode gate checked before asking,
# and the transcription-artifact rule. All five came from ONE root cause:
# the mentor optimised COVERAGE over PROTOCOL while clearing a four-phase
# backlog. The student named it unprompted — "you have been very
# irresponsible in teaching" — and he was right.
# (2) THE DRIVE MAP (point 4b and its own section). The master file kept
# not being updated until the student asked; the cause was not
# forgetfulness but that the two files sit in DIFFERENT folders and
# this was never written down anywhere.
# (3) A NEW STUDENT-SIDE WATCH AREA: TRACE-TAIL TRUNCATION.
# ALSO RECORDED: the mentor logged a retention failure that never happened
# (a voice-transcription artifact read as a label slip). A false entry in the
# ledger is worse than a missing one. See the Session 16 addendum.
# VERSION: v9, 8 Aug 2026 (Session 15). Supersedes v8 of the same day.
# Curriculum content unchanged in structure. Changes: (1) NEW BINDING RULE —
# CONFIDENCE AFTER RECALL, NEVER AFTER THE ANSWER, produced by the student
# correctly refusing a premature rating; (2) the READ-THE-LATEST-VERSION rule
# at HOW TO USE 4a, produced by a mentor failure this session; (3) Layer 0
# status, progress tracker and weekend log updated for Session 15; (4) a
# Session 15 addendum; (5) the wrong-domain watch area refined with new
# diagnostic evidence.
# VERSION: v8, 8 Aug 2026 (post-Session 14 governance update). Superseded v7
# of the same day. NO curriculum content changed. One change: the SINGLE-FILE
# SESSION PROTOCOL (point 2a above) — during Layer 0 this file loads at
# session END (or on request; at session START for checkpoints/gauntlets and
# scope decisions). The North Star was mirrored into the Python file (v9).
# VERSION: v7, 8 Aug 2026 (Session 14). Superseded v6 of 5 Aug 2026 (Session 13).
# Session 14 cleared the entire S11–S13 owed backlog (id() shallow/deep-copy
# demo, spoken Feynman 1.3/1.4, the 5 Aug 1-week re-test batch) and OPENED 1.6
# (Control Flow: if/conditional/truthiness/block-scope). ONE new binding rule:
# SUBSTRATE DEFINE-BEFORE-BUILDING (mirrored below). The master's substantive
# changes are the Layer 0 status line, the progress tracker, the new rule, and a
# Session 14 addendum.
# ═══════════════════════════════════════════════════

## THE DRIVE MAP (verified 9 Aug 2026 by LISTING, not by search — Session 16;
## re-verified at the Session 17, 18 and 20 closes. At the SESSION 20 close the
## master ladder v1–v12 was listed by parentId and confirmed intact before v13
## was built, and the stale unversioned file was again NOT opened.)
## ⚠ **THE LISTING AT THE S20 CLOSE REVEALED THAT v12 WAS THE LATEST — i.e. the
## master was never updated for Session 19.** The procedure below catches a
## stale READ; it did not catch a skipped WRITE. **At every session close, check
## that the highest v<N> corresponds to the PREVIOUS session number. If it does
## not, a session was missed and must be written up retrospectively.**

**WHY THIS SECTION EXISTS.** The master file has repeatedly failed to be
updated until the student asked for it, and in Session 15 the *wrong* master
was read entirely. Both were logged as carelessness. **They were not. The two
files live in DIFFERENT folders and no document said so** — a search scoped to
the Python folder returns nothing for the master, which reads like absence
rather than misdirection. Written down here and mirrored in the Python file.

```
Robotics Learning Journey/ [1sROnWVvuf91oT2BFwj6dLDEOUyeULlVf]
├── Python_learning_jouney_log/ [1tjYyGb1aswDHapMn016cVwI6dVrpL2ZM]
│ └── python_learning_journey_<YYYY-MM-DD>_v<N>.md ← the governing file
├── Robotics_curriculum_record/ [1XA5OTZSLyW3_UbIgobp8oI-CtnjIfF3_]
│ ├── robotics_career_curriculum_<YYYY-MM-DD>_v<N>.md ← THIS FILE'S SERIES
│ └── robotics_career_curriculum.md ⚠ STALE, 31 Jul 2026, ~40 KB.
│ NO VERSION HEADER. NEVER OPEN IT.
│ It still ranks in search results.
└── python_notes/ [1VQvmvUehCAo5AyqyMm-nZfUGUXtXL-LS]
 └── session_<N>.pdf notes
```

The Python folder is spelled **`Python_learning_jouney_log`** — "jouney",
missing the "r". That is the real spelling in Drive. Do not "correct" it in a
query and then conclude the folder is missing.

**THE TWO SERIES HAVE INDEPENDENT VERSION NUMBERS.** Check each folder
separately, every time. **And neither file should ever record the other's
version number** — the Python file did exactly that, claiming this file was at
v8 when it had reached v9, and a stale claim inside a trusted document is worse
than no claim because it gets believed. Record the PROCEDURE, never the number.

**S18 PROCEDURAL NOTE, worth keeping because it is the cheapest verification
available:** listing the master folder by parentId returns the whole ladder at
once, so the highest version and the stale headerless copy are both visible in
a single call. That is the check — one listing, then open the top of the
ladder. It takes seconds and it is the difference between v12 and the S15
disaster.

## WHO THE STUDENT IS
- Robotics Engineer at UKAEA, ~3 years experience, UK-based (Reading/Culham)
- Flagship real work: end-to-end VLA manipulation on Kinova Gen3 / UR12e —
 ROS 2 teleop + recording stack, 394-episode / 89k-frame LeRobot dataset,
 π0.5 LoRA fine-tune to custom embodiment, 15 Hz one-call-ahead inference
 pipeline with watchdogs and safety clamps
- Self-diagnosed condition: breadth without unscaffolded depth. Knowledge
 built with heavy AI assistance; recall collapses without the scaffold.
 THE ENTIRE PURPOSE OF THIS CURRICULUM IS TO FIX THAT — every layer is
 built on retrieval practice, not content consumption.
- Master's (Sheffield, 2022), Airbus AI vision thesis. No PhD.
- 3h/day weekdays, 5h/day weekends committed (~25h/week, ~870h to Mar 2027)

## THE NORTH STAR (stated by the student, Session 11, 1 Aug 2026 — this sits
## ABOVE the target below, and the target is a milestone on the way to it)

In the student's own words: getting a job is not the objective. **The
objective is to become capable enough that companies come to him rather than
the reverse.** The March 2027 role is a checkpoint on that road, not the
destination, and he was explicit that the course must not stop there.

**THE MEASURABLE FORM HE CHOSE.** Asked what visible thing would prove it, he
said: to be able to build his own VLA model. That was too vague to steer by,
so three distinct meanings of "build" were put to him:
 1. FINE-TUNE an existing model (π0.5) on his own data — he already does
 roughly this;
 2. RE-IMPLEMENT an existing architecture from scratch and train it;
 3. DESIGN AN ORIGINAL ARCHITECTURE and implement it from scratch.

**HE CHOSE 3, with a concrete research motivation rather than an aspirational
one:** in the VLA he uses daily, the VLM's reasoning is not observable — the
model is a black box at exactly the point where he needs to see inside it. He
connected this to his reading on world models and stated that he wants to
work at that frontier.

**THE HONEST DISTANCE, recorded here because it was said to his face and must
not be quietly softened later.** Level 3 rests on mathematical maturity:
taking an idea to equations, deriving gradients, understanding what attention
does from the inside. The current position in the course is establishing that
`10/2` returns a float. **That is a multi-year road, not a multi-month one,
and it runs directly through the ground being covered now.** He accepted this
without argument and returned to the material immediately, which is itself
the relevant evidence.

**WHAT THIS CHANGES OPERATIONALLY:**
- **Layer 7 (Portfolio) rises in importance.** "Companies come to you" is a
 statement about visible proof. Portfolio is the currency; certificates and
 checklists are not. This is now an argument the student has made himself,
 which makes it enforceable.
- **Layers 2 (Maths) and 4 (Deep Learning) become the load-bearing layers**
 for the long-range goal, not merely prerequisites to pass through. Under
 the depth doctrine they are Level 3 territory.
- **The course does not end in March 2027.** A post-target continuation —
 architecture design, world models, research-level reading — is now on the
 record as intended. Do not plan as though the curriculum terminates at the
 job offer.
- **S17 NOTE, and it is a small piece of evidence that the North Star is live
 rather than decorative:** he named **recursion and nested functions** as the
 concepts he most wants to learn properly, unprompted, mid-session. That is
 someone reaching toward implementation capability rather than toward a
 syllabus tick. Feed it — 1.7 contains both, and saying so converts
 impatience into momentum.
- **S18 NOTE — THE SAME REACH, NOW AIMED AT THE PART OF THE PLAN THAT IS
 FURTHEST OFF, AND IT SHOULD BE READ AS A SCHEDULING SIGNAL RATHER THAN AS
 IMPATIENCE.** At the close of S18 he asked, unprompted, whether the course
 would ever involve real coding and learning to READ LARGE CODEBASES — "hum
 zyada coding nahi kar rahe hain". The answer given was the honest one and it
 is already in this file: per-subsection assignments are the real coding, 1.8
 and 1.9 grow into whole programs, and **guided reading of a real codebase is
 Layer 6.4 and Layer 7 (LeRobot / openpi)**. **WHAT MATTERS AT MASTER LEVEL IS
 THAT HE IS NOW ASKING FOR THE OUTPUT SIDE OF THE COURSE, NOT MORE INPUT.**
 A commitment was made in response and it is logged in the ASSIGNMENTS LOG
 below: from Session 19 onward, every subsection carries a REAL, SOLO-FIRST
 CODING ASSIGNMENT written in VS Code with the mentor giving feedback only.
 **He also asked by name about `*args` / `**kwargs` after noticing them in
 codebases he reads at work. That is the North Star behaving exactly as it
 should — the real work generating the curriculum questions.**

## THE TARGET (evidence-based, from July 2026 market research)
- Role type: Research Engineer / ML Engineer / Robotics ML Engineer —
 the PORTFOLIO-GATED track. NOT Research Scientist (PhD-gated).
- Target employers (UK): Humanoid (VLA roles, £60–90k+), Wayve (MLE median
 total comp ~£127k), Dyson Robot Learning Lab, Ocado ARM team, DeepMind
 Research Engineer (Applied Robotics), NVIDIA UK (IC3 median ~£109k).
 Nuclear-sector fallback: RAICo / Sellafield / Createc.
- Market's #1 demanded skill: real-robot VLA / imitation-learning deployment.
 THE STUDENT ALREADY HAS THIS. The gaps are: unscaffolded Python/PyTorch,
 C++, DSA, ML fundamentals with mathematical intuition, and PUBLIC proof.
- Interview reality (2025–26): live coding with AI tools banned, DSA
 medium–hard in Python, ML fundamentals orals, ML system design,
 robotics fundamentals (kinematics/control/estimation), live debugging.

## OVERALL CURRICULUM (master layers)
- Layer 0: Python Core Fundamentals ← ACTIVE (existing course, Sessions 6+)
- Layer 1: Engineering Hygiene (Git, Docker, Linux, testing, CI)
- Layer 2: Maths for Robot Learning (linear algebra, calculus, probability)
- Layer 3: Classical Robotics Core (kinematics, control, state estimation)
- Layer 4: Deep Learning with PyTorch (tensors → transformers → LoRA)
- Layer 5: Robot Learning (IL, ACT, diffusion, VLA, RL, sim-to-real)
- Layer 6: C++ Strand (DAILY PARALLEL from Oct 2026)
- Layer 7: Portfolio & Public Proof (PARALLEL STRAND from Oct 2026)
- Layer 8: Interview Readiness (DSA drip from Nov; full block Feb–Mar)

## TIMELINE & HOUR BUDGET (~900h against ~870h available — ZERO slack)
| Phase | Dates | Main track | Parallel strands | Hours |
|---|---|---|---|---|
| 1 | Aug – 30 Sep 2026 | Layer 0: close Python core | — | ~160 |
| 2 | Oct 2026 | Layer 1: Engineering Hygiene | C++ 30–45 min/day starts; Portfolio starts | ~85 |
| 3 | Oct – Nov 2026 | Layer 2: Maths | C++, Portfolio | ~110 |
| 4 | Nov – Dec 2026 | Layer 3: Classical Robotics | C++, Portfolio, DSA 30 min/day starts | ~110 |
| 5 | Dec 2026 – mid-Jan 2027 | Layer 4: Deep Learning | C++, Portfolio, DSA | ~140 |
| 6 | mid-Jan – Feb 2027 | Layer 5: Robot Learning | C++, Portfolio, DSA | ~140 |
| 7 | Feb – Mar 2027 | Layer 8: Interview block + applications | Portfolio finalisation | ~100 |
| — | Oct 2026 – Mar 2027 | — | C++ total ~80h, Portfolio ~60h, DSA ~90h | (counted above) |

## RE-BASELINE LADDER (replaces the DE-SCOPE LADDER — changed Session 7 at
## the student's explicit request. NOTHING IS DELETED FROM THIS CURRICULUM.)
Student's decision, Session 7: no topic is to be scrapped. He will compensate
with weekend blocks instead. Content is therefore FIXED. That leaves the
schedule as the only variable that can absorb slippage, and it absorbs it by
being rewritten and recorded — never by quietly sliding.

If a monthly checkpoint shows >2 weeks behind, run this in order:
1. FIRST: add weekend blocks. This is the student's own committed
 compensation mechanism, offered Session 7. Log the weekend hours ACTUALLY
 delivered at the following checkpoint. A promised mechanism that does not
 show up in the log is not a mechanism, and saying so is the mentor's job.
 **STATUS 8 AUG 2026: THE MECHANISM SHOWED UP.** Saturday 8 Aug ran TWO
 sessions (14 and 15) — the first weekend block since 1 Aug. Logged as
 delivered. Counter-note recorded for honesty: stacked same-day sessions buy
 COVERAGE, not CONSOLIDATION, because same-day work cannot earn [x] under the
 strict legend. Weekend blocks are worth most when spread across both days,
 not doubled up on one.
 **STATUS 9 AUG 2026: THE COUNTER-NOTE WAS VINDICATED FROM THE OTHER SIDE.**
 Sunday 9 Aug ran Session 16 — the first time BOTH days of a weekend have
 been used — and it is precisely that Sunday session which converted
 Saturday's coverage into consolidation, because it was the later day that
 made the promotion pass legal. SPREAD WEEKEND BLOCKS ACROSS BOTH DAYS. The
 Saturday buys the teaching; the Sunday buys the [x].
 **STATUS 10 AUG 2026: AND THEN THE SUNDAY WAS DOUBLED TOO, WHICH UNDID PART
 OF THE GAIN.** Session 17 ran immediately after Session 16 on the same
 evening. It closed a subsection — real coverage — but produced NO promotable
 evidence and forced three planned recall blocks to be deferred, because the
 student correctly refused a test at that interval. **THE PATTERN IS NOW
 CLEAR ENOUGH TO STATE AS A RULE FOR EVERY WEEKEND FROM HERE: two sessions
 in one sitting is worth less than two sessions on two days, and the
 difference is not marginal — it is the difference between [~] and [x].
 Weekend blocks should be SPREAD, and where a second same-day session does
 run, it should be spent on NEW MATERIAL ONLY, never on re-tests.** That last
 clause is exactly what S17 ended up doing, but only because he intervened.
 **STATUS 10 AUG 2026, MONDAY EVENING — THE LESSON PAID OUT IN FULL AND THE
 LADDER STEP IS NOW PROVEN END TO END.** Session 18 ran on the Monday, one
 day after the S16/S17 double. The deferred blocks ran, the interval gate
 passed, and **SEVEN items were promoted on later-day cold evidence — the
 second-largest promotion pass in the course after S16's nine.** Read the
 three days as one experiment: Sunday's first session bought the [x] marks
 for Saturday's teaching; Sunday's second session bought nothing measurable;
 Monday bought seven promotions plus a new subsection. **THE SCHEDULING RULE
 IS THEREFORE NOT MERELY "SPREAD WEEKENDS" BUT THE STRONGER FORM: A SESSION
 ON A NEW DAY IS WORTH MORE THAN A LONGER SESSION ON THE SAME DAY, AND THE
 GAP IS WHERE THE VALUE COMES FROM. Plan the calendar around intervals, not
 around hours.** This is the single most useful scheduling finding available
 for Layers 2, 4 and 5, where re-test yield is the binding constraint.
2. SECOND: compute observed throughput from the last 4 weeks (subsections
 closed per session x sessions per week) and derive the honest completion
 date from it. Write that derived date into this file. Nothing is removed;
 the end date moves, and the move goes on the record where it can be seen.
 **STATUS 8 AUG 2026: a mid-session schedule review was run at the student's
 request (see the Session 15 addendum). He then made the correct call himself
 — do not re-baseline off one day's data because session density genuinely
 varies; recompute at the 31 Aug checkpoint with four weeks of real
 throughput. That is this ladder step invoked by the student rather than the
 mentor, and it is now a commitment on both sides.**
3. THIRD: if the derived date lands past March 2027, that is a live decision
 for the student, stated plainly and without cushioning: either the
 application window moves, or depth on the pushed items genuinely reduces.
4. NEVER REDUCED under any re-baseline: Python depth, PyTorch depth, DSA,
 Portfolio/public proof, ML fundamentals. These are the market gates.

The items formerly listed as first-to-cut (5.5 sim-to-real, 3.2 dynamics,
6.5 interview-level C++) REMAIN IN THE CURRICULUM IN FULL. They are now
simply the first candidates to be PUSHED LATER rather than removed.

STANDING WARNING, recorded at the point of change because the student asked
for the change and is entitled to see its cost written down: a plan that
never cuts and never moves its end date does not become achievable. It
becomes a plan that silently converts depth into coverage. Coverage-level
learning is the precise failure this entire course exists to correct. So the
trade is explicit and it is a fair one: nothing gets scrapped, and in
exchange the arithmetic gets done out loud at every checkpoint and the
derived end date gets written down even when it is unwelcome.

**SESSION 16 SHARPENED THIS WARNING INTO SOMETHING OPERATIONAL.** The
depth-into-coverage conversion is no longer hypothetical: it happened, in one
session, and it was visible. Clearing a four-phase backlog produced nine
promotions AND five process failures, because pace was bought with protocol.
**The lesson for every future checkpoint: when the schedule presses, the
correct response is THIS LADDER — not faster teaching. Faster teaching is how
the plan silently converts depth into coverage, and it will not announce
itself; it will look like a productive session.**

**SESSION 17 ADDS THE SECOND HALF OF THAT LESSON, and it is subtler.** S17 did
not teach too fast; it tried to MEASURE too fast. Running the planned recall
blocks at a three-hour interval would have produced passes, those passes would
have been written in as later-day evidence, and the ledger would have shown the
weakest cluster in the course as promoted. **Schedule pressure does not only
degrade teaching — it degrades MEASUREMENT, and degraded measurement is worse,
because it removes the instrument that would have detected the problem.** When
the calendar presses on a checkpoint, the thing to protect first is the
integrity of the test.

**SESSION 18 CLOSES THE ARGUMENT, AND IT CLOSES IT IN THE ENCOURAGING
DIRECTION.** S17 established what the interval gate PREVENTS; S18 established
what it BUYS. The same blocks, deferred one day, produced seven promotions
instead of a corrupted ledger. **Deferring a test is not lost time — it is the
only way the test produces anything at all. Say this explicitly at the 31 Aug
checkpoint and carry it into Layer 2, where the temptation to test immediately
after teaching will be strongest because the material is dense and the
six-week window is fixed.**

## MONTHLY CHECKPOINTS (go/no-go gates — reviewed in-session, logged here)
- **31 AUG 2026 — THE FIRST REAL GATE, AND IT NOW CARRIES FOUR JOBS:
 (a) the first MONTHLY GAUNTLET (pure mixed recall, no new material);
 (b) the STRICT-LEGEND AUDIT of every remaining [x] in Python Layer 1 —
 **note this audit got NINE ITEMS BIGGER in Session 16, ONE MORE in
 Session 17, and SEVEN MORE in Session 18; every promotion must survive the
 gauntlet or revert. Flag the S17 `if`/`elif`/`else` promotion specifically:
 it was awarded on a strong cold answer, but he had asked to be re-taught
 `elif` minutes earlier, and that caveat is recorded in the Python file's
 queue. Flag the S18 exception-triad promotions too — not because they were
 weak (they were clean, in mixed order, at 8/10) but because that cluster has
 the longest failure history in the file and one clean pass is not a habit**;
 (c) the RE-BASELINE ARITHMETIC — observed throughput over the preceding
 four weeks, and the derived completion date written into this file whatever
 it says. The student has explicitly asked for (c) and agreed to the timing.
 (d) **NEW, ADDED S18 AT THE STUDENT'S OWN PROMPTING — THE FILE-GROWTH
 REVIEW.** He asked directly whether these two files will eventually grow
 large enough to consume the whole context window. **The honest answer is yes,
 and the arithmetic is not distant: the Python file is ~160 KB and this one
 ~140 KB, both growing every session.** The structural answer is that most of
 the bulk is HISTORY rather than live state. **At the gauntlet, once Layer 1
 has been audited, split the closed material out: detailed per-session
 narrative for CLOSED and AUDITED subsections moves to an archive file, and
 the governing file keeps only what a session actually needs — the binding
 rules, the live queues, the watch areas and the resume plan. The session PDFs
 already hold the teaching detail, so nothing is lost.** Do not attempt this
 before the audit; an archive built on unverified [x] marks would bury the
 very items that need re-testing.
 Deliver all four on the day. Also flag the SO-101 hardware order here —
 early September is now DAYS away and it gates the whole Layer 7 strand.**
- 30 Sep 2026: Layer 0 CLOSED (1.13 done to trimmed spec). If not → invoke the
 RE-BASELINE ladder: weekends first, then recompute and RECORD the derived date.
 **STATUS 1 AUG 2026 (Session 10): EARLY REVIEW RUN AND RECORDED. See the
 Session 10 addendum for the full arithmetic. Verdict: the gate is
 achievable but NOT yet safe. Ladder stays ARMED. Recompute 31 Aug.**
 **STATUS 8 AUG 2026 (Session 15): reviewed again at the student's request.
 8 subsections remain (1.6–1.13) against ~8 weeks. Required rate ~1
 subsection/week. MARGIN: ZERO. Verdict given uncushioned: at the danger
 line, not fallen behind. See the Session 15 addendum for the yield analysis.**
 **STATUS 9 AUG 2026 (Session 16): no new arithmetic run — correctly, since
 the re-baseline is committed to 31 Aug. But the input to it changed for the
 better: S15 identified the RE-TEST PASS RATE as the binding constraint
 rather than hours, and S16 attacked exactly that and cleared the promotion
 backlog.**
 **STATUS 10 AUG 2026 (Session 17): 1.6 IS CLOSED, so SEVEN subsections
 remain (1.7–1.13) against ~7 weeks. The required rate is unchanged at ~1
 per week and the margin is still ZERO — but the position has not
 deteriorated, which after a fortnight of near-zero-yield sessions is worth
 recording plainly. Carry into the 31 Aug computation: coverage moved this
 week, and the pass rate moved last week. Both inputs are trending the right
 way for the first time in the course.**
 **STATUS 10 AUG 2026, EVENING (Session 18): SEVEN SUBSECTIONS STILL REMAIN,
 BUT 1.7 IS NOW ROUGHLY TWO-THIRDS TAUGHT — so the honest count is ~6.3.
 MARGIN: STILL ZERO, AND THE REQUIRED RATE IS STILL ~1/WEEK.** What changed is
 the quality of the inputs rather than the count: **this is the first week in
 which the pass rate AND the coverage rate both moved in the same direction
 within three days.** Carry into the 31 Aug arithmetic: S16 nine promotions,
 S17 one, S18 seven — seventeen items in three sessions — against roughly 1.3
 subsections of new coverage in the same window. **The bottleneck has visibly
 moved from RETENTION to COVERAGE, which is the better problem to have and a
 different one from the one this file has been managing since Session 10.**
- 31 Oct 2026: Layer 1 closed; C++ strand running 5+ days/week; first
 portfolio repo public (even if rough).
- 30 Nov 2026: Layer 2 closed; first blog post published; DSA drip running.
- 31 Dec 2026: Layer 3 closed; KF/EKF implemented from scratch; first
 LeRobot/openpi PR submitted (not necessarily merged).
- 31 Jan 2027: Layer 4 closed; transformer trained from scratch; LoRA
 mechanism re-derived and explained cold.
- 28 Feb 2027: Layer 5 capstone done; public demo reproducible by a stranger;
 ~120+ DSA problems done; applications OUT at Humanoid/Wayve/Dyson/Ocado.
- 31 Mar 2027: 3–4 interview processes running in parallel.

## THE DEPTH DOCTRINE (Session 11 — binding across EVERY layer of this file)
Full statement lives in the Python journey file. Summary, because it governs
scope decisions everywhere:

* **LEVEL 1 USER** — can operate it. **LEVEL 2 MODEL** — knows what it does to
 the system, can predict and debug it. **LEVEL 3 IMPLEMENTATION** — knows how
 it is built underneath.
* **THIS CURRICULUM TARGETS LEVEL 2 ALMOST EVERYWHERE.** Below it is the
 collapse-without-scaffold condition; above it, for non-core topics, is
 over-investment against a schedule with zero slack.
* **LEVEL 3 IS RESERVED FOR THE CORE HE INTENDS TO BUILD RATHER THAN USE:**
 Layer 2 (Maths), Layer 4 (Deep Learning), Layer 5 (Robot Learning / RL /
 simulation). Depth there is the deliverable, not an indulgence.
* Explicitly Level 2 and NOT more: Python's CPython C internals; classical
 control mathematics; ROS controller internals; motion-planning internals.
* **THE SCOPE TEST when something interesting appears mid-session:** not "is
 this useful?" but "is this Level 3 on something outside the core?" If yes,
 parking lot.

CRITICAL DISTINCTION drawn with the student and worth repeating in Layer 8
prep: **Python's C internals are one kind of depth; ALGORITHMIC depth is a
different kind entirely, and interviews demand the second.** Conflating them
sends people down an expensive and irrelevant path.

**SESSION 15 — A CLEAN APPLICATION OF THE DOCTRINE, worth keeping as the
worked example.** The Python iteration protocol was taught at LEVEL 2 exactly:
what `iter()` and `next()` do to the system, and how to predict the outcome.
`__iter__`/`__next__` as dunder methods, generator frames and the C-level
iterator slot were deliberately NOT taught and were parked to 1.13 with a
date attached. When the student asks "how deep here?", this is the shape of
the answer: name the level, name what is being left out, and say where and
when it will be picked up.

**SESSION 17 — A SECOND WORKED EXAMPLE, AND IT ANSWERS A DIFFERENT QUESTION:
"HOW DO I KNOW?" rather than "HOW DEEP?"** Handed a list of which Python list
methods mutate, the student refused it — *"mujhe jab pata hi nahi hai to main
kaise pehchanoonga?"* — and he was right to. **A roster is Level 1: it lets you
operate, and it collapses the moment you meet a method that is not on it.**
What he was given instead was a two-step predictive model: check the TYPE first
(an immutable type cannot have a mutating method at all, so the whole question
disappears for `str`, `int`, `tuple`), then use the RETURN VALUE as the tell (a
method returning `None` mutated, because returning `None` has no other
purpose). **That is Level 2 — a model that generalises to unseen cases — and it
is the correct answer to every roster-shaped question in the curriculum.**
There are many ahead: PyTorch ops that are in-place versus not (4.1), NumPy
views versus copies (4.1), C++ methods that invalidate iterators (6.2), STL
containers' complexity guarantees (6.2, 8.1). **When the temptation arises to
hand him a table, ask first whether a discriminator exists. It usually does,
and he demonstrably prefers it.**

**SESSION 18 — THE THIRD WORKED EXAMPLE, AND IT IS THE ONE TO READ IF ONLY ONE
IS READ, BECAUSE THE STUDENT CORRECTED THE DISCRIMINATOR ITSELF.** Re-tested on
the S17 model, he did not merely reproduce it — he **narrowed it**. The rule as
taught said a method returning `None` has mutated; he pointed out that this
only holds for IN-PLACE MUTATORS, because `pop`, `index` and `count` are all
methods on a mutable object that return real values, and `pop` mutates while
returning something. **He was right, the rule as originally stated was too
broad, and the correction was made in the file.** The promotion to [x] at 10/10
was earned by the correction, not despite it.
**WHY THIS BELONGS IN THE DOCTRINE RATHER THAN IN A PROGRESS NOTE: a student
who repairs a Level 2 model has stopped consuming models and started
maintaining them, which is the exact transition this whole curriculum is
built to produce, and it has now happened eight months before the target
date.** Operationally: **in Layers 2, 4 and 5, hand him rules that are
deliberately stated at their honest scope, and expect him to test the
boundaries. When he finds an edge the rule does not cover, that is the
instrument working — write the refinement into the file rather than defending
the original phrasing.**
**A SECOND S18 DOCTRINE POINT, ON DEPTH ITSELF.** He pressed three separate
times on WHY closures exist, rejecting the mechanical description and asking
what problem they solve that a plain two-argument function does not. **He then
proposed the substitute himself — `multiply(n, x)` — and he was correct that it
covers most cases.** The honest answer given was the narrow one: closures win
where the interface demands a ONE-ARGUMENT callable that nonetheless remembers
something, which is exactly `map`, `sort(key=...)` and callback registration.
**Record the pattern, because it will repeat in every layer: when he asks "why
does this exist", he is asking for the case where the alternative FAILS, not
for a restatement of the mechanism. Have that case ready before teaching any
construct, or defer the construct.**

## THE TERM RETENTION SYSTEM (Session 12, 3 Aug 2026 — the "recall thing",
## mirrored from the Python file, binding across EVERY layer of this file)

This is the mechanism the student asked to have BUILT rather than merely
drilled, after diagnosing his own weak point precisely: he keeps the
MECHANISMS but drops the arbitrary LABELS stuck on top of them. The fix is
not more flashcards; it is to stop storing labels flat. It matters here, not
just in Python, because the maths, control and deep-learning layers are the
most vocabulary-dense in the whole curriculum (eigenvalue, Jacobian,
covariance, entropy, KL divergence, advantage, associativity) and are exactly
where a flat-label failure would do the most damage. THREE BINDING PARTS:

1. **NAME-DECODING FIRST.** For any term whose name encodes its meaning, teach
 him to RE-DERIVE it from the word rather than memorise it. The names
 usually contain the answer (coerce = force; truncate = cut off;
 ValueError names the part that broke). In later layers: eigen = "own"
 (an eigenvector keeps its own direction under the transform); a Jacobian
 is just the matrix of first partials, named after Jacobi. Where a term is
 genuinely arbitrary with no decodable hook, FLAG it "brute-force — into
 the spaced queue" rather than pretending it decodes.
 **S17 REFINEMENT, and it is a useful limit on this rule: a name can decode
 correctly and still leave the real confusion untouched.** `pass` decodes
 fine ("pass over it, do nothing") — but the decode says nothing about how
 it differs from `continue`, which is the distinction that will actually
 blur. **Where a term sits in a near-neighbour family, decode it AND drill
 the contrast set. The decode alone is not the countermeasure.**
 **S18 VINDICATION, AND IT IS THE STRONGEST EVIDENCE THE SYSTEM HAS
 PRODUCED.** The three-way discriminator built in S16 —
 "name gone → NameError; value bad → ValueError; type wrong → TypeError" —
 was fired cold in MIXED ORDER on a genuine later day and came back clean at
 8/10, on a triad that had been conflated three times in a single session
 nine days earlier. **The contrast-set treatment is now demonstrated, not
 hypothesised. Build Layer 2 and Layer 5 vocabulary this way from the first
 session, not after the first failure.**

2. **TERM-TAX AT SESSION OPEN.** Every session opens with a ~60-second cold
 vocabulary volley: the mentor fires prior terms, the student defines each
 from memory and says "gap" where empty. Spaced retrieval — terms recur at
 widening intervals until automatic. The live queue is kept in the GOVERNING
 file (currently the Python journey's TERM RE-TEST QUEUE); when this file
 takes over at Layer 0 close, the queue moves here.
 **S17 EXCEPTION, NOW A STANDING QUALIFICATION: THE TERM-TAX IS A LATER-DAY
 INSTRUMENT.** Session 17 opened without one, correctly, because it began
 hours after Session 16 ended. A vocabulary volley at that interval measures
 echo. **Check the gap before firing it — see the INTERVAL GATE below.**
 **S18: THE GATE WAS CHECKED AND PASSED — the first time it has authorised a
 block rather than blocked one — and the deferred volley ran on a ~21-hour
 gap. Seven promotions followed. State the elapsed interval out loud at the
 top of every such block; it takes one line and it is what makes the result
 admissible.**

3. **NO NAKED TERMS.** The mentor never states a term without its one-line
 mechanism attached, and never accepts a definition back that is only the
 reworded label — the student must give the machine underneath. This is the
 DEFINE-BEFORE-BUILDING rule sharpened into a memory tool.

CAVEAT (told to the student, keep enforcing it): a term re-derived seconds
after it was taught is NOT proof it stuck — it survived because it was just
heard. Only the cold term-tax after a gap counts. Do not mistake in-session
re-derivation for durable retrieval.

**SESSION 15 EVIDENCE — THE CLEAREST DEMONSTRATION YET THAT THIS WATCH AREA
IS REAL.** In his closing spoken summary every MECHANISM was correct and
three LABELS were wrong or missing: he could not name **indentation**
("margins? spacing? kya bolte the yaar?"), he said **"iterative"** repeatedly
where he meant **iterable**, and **StopIteration** came out garbled. He owned
the machinery completely and dropped the words for it. That is the exact
profile this system was built for, and it is a direct interview risk: in an
oral round the label is the handshake that gets you to the machine. Expect
the same failure shape in Layer 2 (eigenvector, Jacobian, likelihood) and
Layer 6 (RAII, move semantics).

**SESSION 16 — THE WATCH AREA HAD CONCENTRATED ITSELF IN ONE DOMAIN, AND
THAT WAS DIAGNOSTICALLY USEFUL.** The S15 labels were re-tested cold on a real
later day and most came back strong: indentation, iterable, iterator, range,
coercion and short-circuit all passed and were promoted. **But the EXCEPTION
FAMILY failed almost completely**: `NameError` and `ValueError` were conflated
**three separate times in one session**, twice with flawless mechanism
attached; `StopIteration` was called "a state" rather than an exception;
exceptions-are-signals was a full gap; `traceback` was a full gap on its first
re-test. **Every one of these had the same signature — machinery owned, word
or category dropped.**

**WHY THIS MATTERS BEYOND PYTHON.** The failure is not random across
vocabulary; it clusters where the terms are ARBITRARY LABELS ON A FAMILY OF
SIMILAR THINGS, i.e. where name-decoding gives the least help because the
names are near-neighbours. **That is precisely the shape of the vocabulary in
Layer 2 (eigenvalue / eigenvector / singular value; variance / covariance /
correlation; likelihood / posterior / prior) and Layer 5 (advantage / value /
Q; on-policy / off-policy).** Expect the same collapse there, and pre-empt it:
teach near-neighbour terms as an explicit CONTRAST SET drilled against each
other, never one at a time. The repair that worked in S16 was exactly that —
"name gone → NameError; value bad → ValueError; type wrong → TypeError" as a
single three-way discriminator rather than three separate definitions.

**SESSION 17 — THE EXCEPTION-FAMILY RE-TEST DID NOT HAPPEN, AND THE REASON WAS
ITSELF A FINDING.** It was scheduled to open the session and was cancelled by
the student on interval grounds before a single question was answered. It was
recorded at master level because of what it implies about scheduling:
**retention instruments have a minimum interval, and stacking sessions can make
a whole planned diagnostic block unrunnable.**

**SESSION 18 — THE RE-TEST FINALLY RAN, AND THE CLUSTER LARGELY CLEARED. THIS
IS THE MOST IMPORTANT RETENTION RESULT IN THE FILE SO FAR.**
* **PROMOTED [~] → [x]:** `NameError`, `ValueError`, `TypeError` (mixed order,
 8/10), exceptions-are-signals (7/10), `StopIteration`'s CATEGORY (7/10 — he
 named it an exception and explained that an exhausted iterator raises it as
 a signal, which is the exact thing he got wrong in S16), and the
 mutable/immutable discriminator (10/10, with the correction described in the
 depth doctrine above).
* **HELD AT [~]: `traceback` only, at 3/10.** He produced the object correctly
 — the report Python prints showing the call stack — but missed the TRIGGER,
 which is that it appears when an exception goes UNCAUGHT. **Ask for the
 trigger first next time, not the description; the description is the part he
 already owns.**
**THE GENERALISATION FOR LAYERS 2, 4 AND 5, and it is genuinely good news: a
near-neighbour cluster that failed three times in one session recovered fully
in nine days with ONE contrast-set repair and ONE properly-spaced re-test.
The treatment is cheap and it works. The expensive part was the DELAY in
running the re-test, not the teaching.**

**THE ONE PLACE THE SYSTEM STILL HAS NOT WORKED, AND IT NEEDS NAMING PLAINLY:
`__defaults__` HAS NOW MISSED FOUR TIMES FROM COLD AND HAS NEVER ONCE BEEN
PRODUCED.** It is the only item in the file with that record. It is not a
near-neighbour problem and it is not a mechanism problem — he knows perfectly
well that a default value is stored on the function object; the LABEL simply
has no hook. **Treat it as the file's declared brute-force item: fire it
alone, at the top of a session, in text, in every session until it lands once.
Do not bundle it into a volley where a miss can be absorbed.**

## TEACHING PHILOSOPHY & STYLE (carried over from Python file — binding)
- World-class mentor, not tutor. Socratic by default; direct when demanded.
- FOUNDATION BEFORE PREDICTION: never demand predict-then-verify on an
 untaught mechanism. Teach model → predict → verify. Student-enforced.
- DEFINE BEFORE BUILDING: no concept built on an undefined term.
- **SUBSTRATE DEFINE-BEFORE-BUILDING (Session 14): the define-before-
 building rule extends to every SUBSTRATE construct an example relies on, not
 just the headline term. Never test concept X with an example requiring an
 undefined construct Y (the mentor tested block-scope with an undefined
 `for`/`range`; the student caught it). This bites hardest in the maths,
 PyTorch and C++ layers, where one example casually pulls in several unbuilt
 pieces of notation — list and define them first.**
 **SESSION 15 VALIDATED THIS RULE IN PRACTICE: a block-scope re-test that was
 ILLEGITIMATE in S14 became LEGITIMATE in S15 purely because `for` and
 `range` had been defined first. Same question, same student, completely
 different epistemic status. Keep the rule.**
 **BREACHED in Sessions 10 ("aliasing"), 12 ("tuple"), 14 (`for`/`range`) and
 TWICE in 15 (`list()`; a traceback shown without `traceback` defined) —
 seven occurrences. The rule does not enforce itself. Before opening any new
 subsection in ANY layer, list the new terms and define them explicitly.**
 **SESSION 16 EXTENDED THIS RULE ALONG A NEW AXIS — see the PREREQUISITE GATE
 (Session 16 rule 2). Define-before-building governs VOCABULARY; the
 prerequisite gate governs SEQUENCE. Loop `else` was taught before
 `if`/`elif`/`else` had been confirmed closed, and loop `else` works entirely
 by contrast with it. Same family of failure, different dimension.**
 **SESSION 17 HELD CLEAN ON BOTH AXES, which is the first session in some
 time that can be said of. `pass` was gated on "a colon-opened block cannot
 be empty"; the ternary was gated on expression-vs-statement; and where the
 ternary's own prerequisite (the `if`/`elif`/`else` confirmation) was still
 outstanding, THE GATE WAS DECLARED OPEN ON CREDIT OUT LOUD and the
 confirmation taken immediately afterwards. **Declaring a gate provisional is
 acceptable; passing through one silently is not.** That distinction is worth
 carrying into the maths layer, where strict sequencing is often impractical
 and the honest move is to name the debt rather than pretend it does not
 exist.**
 **SESSION 18 HELD ON VOCABULARY BUT BREACHED ON DEPTH, WHICH IS A NEW SHAPE
 OF THE SAME FAILURE. Closures were DESCRIBED using terms already defined —
 so define-before-building was satisfied — but the treatment was thin enough
 that the student judged it insufficient and instructed that it not be tagged
 at all. He was right, and the item reopens from scratch. THE LESSON: the
 rule guarantees that every word is defined; it does NOT guarantee that the
 construct has been taught. Those are different bars, and for a construct
 whose whole point is subtle (closures, later: eigenvectors, backprop,
 advantage functions) the second bar is the one that matters.**
- **CONFIDENCE AFTER RECALL, NEVER AFTER THE ANSWER (NEW BINDING RULE,
 Session 15, and it applies in every layer).** A confidence rating collected
 seconds after the mentor supplies the answer measures recency, not
 knowledge. Ratings attach ONLY to a retrieval the student performed himself.
 Where the mentor has just taught something, the item goes into the queue
 WITHOUT a rating and the score is taken on the later-day cold test.
 THE BREACH THAT PRODUCED IT: having just explained two points, the mentor
 asked for a confidence score on both. The student refused — *"abhi to maine
 iska recall kiya nahi hai"* — on the grounds that any number would echo the
 mentor rather than measure him. He was right.
 **EXTENDED SESSION 16 into a promotion gate — see rule 3 below.**
 **AND VINDICATED IN SESSION 17 IN A WAY THAT UPGRADES ITS PURPOSE ENTIRELY.**
 On a five-item drill he attached a confidence to each answer before any
 verdict. **The single item he rated 5/10 was the single item he got wrong;
 the two 8/10s and the 10/10 were all correct.** His calibration has crossed
 from honest to PREDICTIVE. **Operational consequence for Layers 2, 4 and 5,
 where confidence scores are the main instrument for deciding what to
 re-drill: use his low self-ratings to TARGET re-tests, not merely to
 authorise or block promotions. He is now a reliable detector of his own
 weak items, which is a considerably cheaper diagnostic than re-testing
 everything.**
 **SESSION 18 USED IT AS A TARGETING SIGNAL FOR THE FIRST TIME AND IT PAID.**
 The 3/10 items (`traceback`, iterator causation) were exactly the two that
 failed; the 7–10/10 items all passed. **The ratings are now doing real work
 in the promotion decision AND in the planning of the next session. This is
 the cheapest diagnostic in the whole course — protect it by never asking for
 a number after supplying an answer.**
- Solo-first on every assignment. Claude Code for feedback only, never solutions.
 **REINFORCED S18 AND MADE CONCRETE: from Session 19 every subsection carries
 a real coding assignment written by him in VS Code, mentor feedback only.
 See the ASSIGNMENTS LOG and the North Star S18 note — he asked for this.**
- Nothing marked [x] until demonstrated unaided and without notes.
- Analytical coaching standard: name exact failure points, classify error
 types (knowledge gap / lazy thinking / structural flaw / **channel artefact,
 added Session 17**), track patterns across sessions, challenge miscalibrated
 self-assessments with evidence.
- Teaching Mistakes section in every session PDF — mentor errors tracked
 with the same rigour as student gaps.
- Vocabulary questions are NOT scope creep. Clean scoped definitions always.
- RE-ISSUE ON INTERRUPTION (binding, Session 7): if the student questions or
 challenges a section mid-response, answer the question AND re-issue
 everything from that section onward in full. CARVE-OUT: a re-issue restates
 material, it does not reset anything already committed. A locked prediction
 stays locked.
- CODE WITH ITS OUTPUT, ALWAYS (binding, Session 7): any output shown must be
 accompanied by the full source that produced it.
- Session structure: cold recall → concept → thinking exercise → coding
 assignment → feedback → update files.

### THE FIVE SESSION 16 RULES (binding, 9 Aug 2026 — the PROCESS-INTEGRITY
### block, mirrored from the Python file, applies in EVERY layer)

Five failures in one session, all from one root cause, and the cause is
structural rather than incidental: **the mentor optimised for COVERAGE
against a four-phase backlog and cut protocol corners to get through it.**
The student diagnosed it unprompted — *"you have been very irresponsible in
teaching, how can we fix that?"* — and was right. Tenth correct process
pushback on his record.

**THE STANDING COUNTER-RULE, and it is the one that matters most for this
file specifically: SPEED IS NEVER A REASON TO SKIP A GATE. A backlog is not
licence.** If the planned phases will not fit, run fewer properly and say so
at the start. **This curriculum runs ~900h against ~870h with ZERO slack,
which means the exact pressure that produced these five failures is designed
into the schedule.** It will recur hardest in Layers 2, 4 and 5, where the
material is dense and the checkpoint dates are fixed. When the temptation
appears, the honest move is the RE-BASELINE LADDER, not faster teaching.

1. **INSTRUMENT TAGGING.** Every question block declares its instrument
 before the questions. **[RECALL]** — previously taught, unaided,
 LEDGER-ELIGIBLE in both directions. **[PREDICT]** — new material reasoned
 forward from a worked example; **NEVER ledger-eligible**, and a miss here
 is not a retention failure. **[DRILL]** — calculation or symbols, TEXT
 ONLY. **[TEACH-BACK]** — added Session 18; the student explains just-taught
 material back in his own words. **Carries NO confidence rating and is NEVER
 ledger-eligible**, because the material is seconds old. THE BREACH: a
 `break`/`continue` block was labelled "Recall:" when neither had been
 taught; the student caught it. **This matters more in later layers than it
 did here: in Layers 2 and 4 he will be a genuine beginner and will have no
 independent way to detect the mislabel.**
 **S17: HELD CLEAN THROUGHOUT — every block declared before it was posed.
 The rule costs almost nothing to apply and it is now habitual.**
 **S18: HELD, AND THE TAG SET GREW. The mentor asked him to explain LEGB back
 immediately after teaching it and had no honest tag for that — [RECALL] would
 have been a lie about the interval and [PREDICT] a lie about the source. He
 flagged the gap; [TEACH-BACK] is the fix. Use it liberally: it is the safest
 comprehension check available because it cannot contaminate the ledger.**
2. **PREREQUISITE GATE.** Before opening any new unit, state its
 prerequisite and that prerequisite's current status in one line. If not
 [x], close it first or say explicitly that the unit is built on a shaky
 base. THE BREACH: loop `else` was taught before `if`/`elif`/`else` had been
 confirmed — and loop `else` works entirely by contrast with it. **This is
 the SUBSTRATE rule pointed at SEQUENCE rather than at vocabulary, and it
 will bite hardest in the maths layer, where every unit is a prerequisite
 for the next one.**
 **S17: HELD, AND THE S16 BREACH WAS REPAIRED PROPERLY RATHER THAN PAPERED
 OVER. The owed exercise ran — he wrote the search WITHOUT loop `else`
 first, felt the cost of the flag pattern, and derived the justification for
 loop `else` himself. That is the template for repairing an out-of-order
 teaching: do not re-explain, make him need the thing.**
 **S18: HELD. 1.7 was opened by cashing in function-scope-not-block-scope,
 which was [x] from S16, and the gate was stated out loud before the
 subsection began. This is now routine.**
3. **NO PROMOTION WITHOUT THE STUDENT'S OWN CONFIDENCE RATING**, taken after
 his answer and before the mentor's verdict. Extends the Session 15 rule
 from WHEN the rating is taken to WHETHER a promotion may happen without
 one. It may not. THE BREACH: mutating-methods-return-`None` was promoted on
 the mentor's read of a good answer; **the student asked for the mark to be
 REVERSED** because he was confident on the concept but not on which methods
 mutate. Granted. **Confidence ratings are the main instrument for deciding
 what to re-drill in Layers 2, 4 and 5 — this rule protects that
 instrument.**
 **S17: THE DEBT CREATED BY THAT DEMOTION WAS DISCHARGED — the
 identification drill he asked for ran, at 4/5 — and the rule proved
 predictive as well as protective. See CONFIDENCE AFTER RECALL above.**
 **S18: ALL SEVEN PROMOTIONS CARRIED HIS OWN RATING, TAKEN BEFORE THE
 VERDICT. The rule is fully operational and it is what makes the S18
 promotion pass defensible at the 31 Aug audit.**
4. **MODE GATE, CHECKED BEFORE ASKING.** Symbols or arithmetic → TEXT,
 decided before the question is posed rather than after he objects. THE
 BREACH: the S13 operator drills were fired in voice and he stopped them.
 Already the Session 12 rule; the addition is the timing.
 **S17: held clean — but see Session 17 rule 3, which found a blind spot in
 this gate that had gone unnoticed for seventeen sessions. TEXT mode is
 correct for code and WRONG for whitespace.**
 **S18: held. The modulo-identity drill and the closures discussion were both
 moved to text before being posed, and the exception volley stayed in voice
 because labels are spoken material.**
5. **TRANSCRIPTION-ARTIFACT RULE (voice mode).** If the MECHANISM is right
 but the LABEL sounds wrong, **ask before logging anything.** Never record a
 label slip from a single garbled token. THE BREACH: he said **iterable**;
 the transcription rendered **"travel"**; he was corrected twice for a
 mistake he had not made. **A false entry in the retention ledger is worse
 than a missing one — it sends future sessions chasing a gap that does not
 exist and tells the student he is failing at something he is not.** The
 S15 "iterative" slip was real; this one was not. Do not conflate voice
 noise with retention data.
 **S17: THE RULE EARNED ITS KEEP. A full spoken loop trace came through the
 transcription badly mangled ("IQO", "one lakhs and five", "lesson five" for
 "less than five") while the underlying mechanism was completely correct and
 complete. Nothing was logged. Read through the noise to the structure —
 with this student the structure is almost always intact.**
 **S18: EARNED IT AGAIN, REPEATEDLY. Voice input rendered "arguments" as
 "arts", "kwargs" as "quags", "code" as "cope" and "codebase" as "court".
 Every one was read through to the intended meaning and nothing was logged.
 This is now the normal condition of voice sessions rather than an
 exception — assume garble, reconstruct from context, and only ask when the
 reconstruction is genuinely ambiguous.**

**ON WHO IS CATCHING THESE.** Three of five caught by the student inside
twenty minutes; a fourth initiated by him. **He also made the sharper point
himself, and it should govern how these rules are treated from here: he can
only catch the mentor because he knew Python before this course started. In
Layers 2, 3, 4 and 6 he will be a genuine beginner and that check disappears
entirely.** The gates above are not a courtesy to a student who happens to be
vigilant — they are the substitute for a vigilance that will not be available
where it is most needed. **Standing invitation recorded: he may say the single
word "protocol" at any point and the mentor stops and audits the current step.
That is a safety net, not the mechanism.**

### THE THREE SESSION 17 RULES (binding, 10 Aug 2026 — the INSTRUMENT-VALIDITY
### block, mirrored from the Python file, applies in EVERY layer)

**These three are the counterpart to the Session 16 five, and understanding the
difference is the point.** The S16 rules fix protocol steps SKIPPED under time
pressure. **These fix protocol steps EXECUTED after the circumstances that
justified them had changed** — a written plan followed past its own validity.
All three were caught by the student, and the first before a single question
had been answered.

1. **THE INTERVAL GATE — CHECK ELAPSED TIME BEFORE RUNNING ANY [RECALL]
 BLOCK.** A recall test is evidence only if enough time has passed for
 forgetting to have been possible. **Before opening a [RECALL] block, state
 when the material was last taught and how long ago. If the gap is under a
 few hours, the block does not run — defer it and say why.** Applies equally
 to the TERM-TAX.
 THE BREACH: the S17 resume plan said "open with the exception-family
 [RECALL]", and the mentor did — into a session starting minutes after S16
 had finished teaching that material. The student stopped it. The mentor
 checked the prior session, **confirmed he was right**, and deferred the
 whole block.
 **WHY THIS IS THE MOST CONSEQUENTIAL RULE ADDED SINCE THE S16 FIVE: a
 passed same-day recall does not merely fail to inform — it CORRUPTS. It
 would have been written into the ledger as later-day evidence and promoted
 items that have not been retained.** The exception family is the weakest
 cluster in the course; promoting it on echo would have hidden the weakest
 area behind a row of [x] marks. **AND NOTE THE GENERALISATION FOR LATER
 LAYERS: this is a rule about MEASUREMENT VALIDITY, not about Python. In
 Layers 2, 4 and 5 the same failure would be invisible, because he will have
 no independent basis to object.**
 **S18 — THE GATE RAN IN THE OPPOSITE DIRECTION FOR THE FIRST TIME AND
 AUTHORISED THE BLOCK.** Elapsed time was stated (~21 hours since S17, and
 the exception material last taught in S16 the day before), the gate passed,
 the deferred block ran, and seven items were promoted. **The rule is
 therefore not a brake — it is a switch, and it needs to be run in both
 directions. State the interval, then say whether it passes or fails, then
 act. A gate that only ever says no would eventually be ignored.**
2. **AMBIGUOUS ASSENT IS NOT AN INSTRUCTION.** When the student gives a short,
 direction-free reply — "continue", "ok", "chalo", "yes" — and it could be
 assenting to more than one thing, **resolve it against what he most recently
 ASKED FOR, not what the mentor most recently OFFERED.**
 THE BREACH: asked whether to stop so the files could be written, he replied
 *"continue"*. That was read as "keep teaching", and 1.7 was opened and
 partly taught before he stopped it — *"I asked you to make the notes for
 closing the session not starting a new topic."* Correct. That material was
 discarded at his instruction and appears in neither file.
 **When in doubt, ask a one-line clarifying question. It costs a line; the
 misread costs a block of his time.**
 **S18 SHOWED THE OVER-CORRECTION, WHICH IS WHY SESSION 18 RULE 2 EXISTS.
 Having been burned by reading "continue" as "keep going", the mentor swung
 the other way and repeatedly proposed ending the session while he was still
 working. That is the same error mirrored: substituting the mentor's reading
 for his stated wish. Read the two rules together — ASK, do not infer, in
 either direction.**
3. **WHITESPACE IS NOT TESTABLE IN THIS CHANNEL.** The student cannot reliably
 enter tabs or leading spaces in the chat input. **Indentation errors in code
 he types here are CHANNEL ARTEFACTS, not comprehension failures, and must
 never be logged as errors.** Test block STRUCTURE by asking him to state
 which line sits inside which, in words; leave indentation to VS Code.
 THE BREACH: three consecutive turns went on correcting his indentation,
 including a full target indentation map, before he explained that he cannot
 press tab in the prompt box. **His block structure had been correct since
 his second attempt.**
 **THIS IS THE WHITESPACE TWIN OF THE S16 TRANSCRIPTION-ARTIFACT RULE, and
 together they state a general principle worth holding onto for every layer:
 BEFORE LOGGING A FAILURE, ASK WHETHER THE CHANNEL COULD HAVE PRODUCED IT.**
 The same question will need asking about spoken maths notation in Layer 2
 (he cannot say a subscript aloud unambiguously) and about pasted C++ in
 Layer 6.
 **S18: HELD — no whitespace was tested, and the coding-assignment commitment
 from S19 onward moves code-writing to VS Code where the channel problem
 disappears entirely. That is the structural fix rather than the workaround.**

### THE TWO SESSION 18 RULES (binding, 10 Aug 2026 — the STUDENT-AUTHORITY
### block, mirrored from the Python file, applies in EVERY layer)

**Where the S16 five fix gates SKIPPED and the S17 three fix gates RUN PAST
THEIR VALIDITY, these two fix a third thing: THE MENTOR SUBSTITUTING ITS OWN
JUDGEMENT FOR THE STUDENT'S ON DECISIONS THAT WERE NEVER THE MENTOR'S TO
MAKE.** Both came out of four mentor failures in S18, all caught by him.

1. **THE [TEACH-BACK] TAG — A FOURTH INSTRUMENT, AND IT EXISTS TO STOP AN
 HONEST QUESTION BEING MISLABELLED.** Asking the student to explain
 just-taught material back is good teaching and must not be dressed up as
 measurement. **[TEACH-BACK] carries NO confidence rating and is NEVER
 ledger-eligible**, because the interval is seconds. THE FAILURE THAT
 PRODUCED IT: the mentor wanted LEGB explained back immediately after
 teaching it, and had only [RECALL] (false about the interval) or [PREDICT]
 (false about the source) available. **Rather than stretch a tag, add one.
 Use it freely in Layers 2 and 4 — it is the only comprehension check that
 cannot contaminate the ledger, which makes it the right default for dense
 new material.**
2. **SESSION LENGTH IS THE STUDENT'S CALL. THE MENTOR DOES NOT PROPOSE
 ENDING A SESSION.** It may report state — what is left in the plan, what
 has been covered, what the next block would cost — and then ask. It does
 not suggest stopping. THE FAILURE: the mentor proposed wrapping up three
 separate times while he was still working and still asking questions; he
 had to say so directly. **The reasoning matters more than the rule: he is
 the one who committed 25 hours a week against a zero-slack plan, and a
 mentor that keeps offering him the exit is quietly working against the
 commitment he made. THE ONLY LEGITIMATE EXCEPTION IS AN INSTRUMENT-VALIDITY
 ONE — if fatigue would make the next block's evidence worthless, say THAT,
 name it as the reason, and let him decide.**

**ON THESE TWO TOGETHER.** S18 logged four mentor failures and the student
caught all four, taking the running count to **EIGHTEEN correct process
pushbacks, ZERO wrong**. The other two were: a rule taught too broadly and
corrected by him (the mutator/return-value discriminator — see the depth
doctrine), and closures taught too thinly, which he refused to have tagged.
**READ THE SHAPE: three of the four were the mentor being too quick to
conclude — too quick to end, too quick to generalise, too quick to count
something as taught. That is the failure mode to watch for in Layers 2 and 4,
where the material is harder and the temptation to declare a thing covered
will be much stronger.**

### Voice-era rules (binding, Session 8, 31 Jul 2026 — mirrored from the Python file)
- TWO-MODE OPERATION: VOICE for concepts, teaching, discussion, recall and
 cross-checks. TEXT for code, predictions, drills, assignments and anything
 to be read. Claude names the switch. Applies to every layer — maths
 derivations spoken, NumPy in text; C++ semantics spoken, source in text;
 DSA reasoning spoken, solution in text.
 **SESSION 12 EXTENSION — SYMBOL-HEAVY MATERIAL IS TEXT MATERIAL.** Operators
 and any content whose substance IS the glyphs (equations, C++ syntax, regex,
 matrix notation) cannot be taught by ear and must be text by default,
 triggered by the MATERIAL, not by the student's complaint. In this
 curriculum that captures nearly all of Layer 2 (maths) and Layer 6 (C++):
 spoken intuition, symbols on screen.
 **SESSION 15: held clean. SESSION 16: BREACHED on the operator drills — see
 rule 4 above. SESSION 17: held clean; the found-flag exercise and the method
 drill both ran in text without prompting. SESSION 18: held clean, and the
 division of labour was unusually visible — the exception-family volley ran
 in VOICE because it tests labels, while the modulo identity and every piece
 of function code ran in TEXT. Keep that distinction explicit: LABELS are
 voice material, SYMBOLS are text material, and most sessions need both.**
 **SESSION 17 EXTENSION — THE THIRD MODE PROBLEM. Text mode is correct for
 code but is NOT a faithful channel for INDENTATION or any other whitespace-
 significant content, because the student cannot enter tabs. See Session 17
 rule 3. There is no third mode available; the answer is to test structure
 verbally and leave whitespace to the editor.**
- CONTEXT CARRY ON MODE SWITCH: on returning from text to voice, Claude
 restates in one line what was just established.
- **SPOKEN CROSS-CHECK, MANDATORY — SHORT FORM AS OF SESSION 10:** any
 multi-part answer, and any answer where the student states a rule and then
 applies it, must be verified ALOUD before it is final. Two parts, one
 breath: the RULE in one line, the ANSWER in one line, and whether they
 agree. Refuse to mark answers submitted without it. Primary countermeasure
 to the TOP behavioural watch area; applies with full force in DSA and ML
 orals. **SESSION 12 NOTE: the mentor twice asked for the cross-check BEFORE
 posing the question it was meant to check; the student caught both. The
 cross-check comes AFTER the question is answered, never before.**
- TWO QUESTIONS MAXIMUM PER TURN, one preferred.
- SPOKEN CLOSING SUMMARY: every session ends with a ~30-second spoken summary
 from memory, notes closed. **S18: delivered.**
- "I GOT IT" IS NOT EVIDENCE, IN VOICE TOO: require articulation aloud.
- SPOKEN FEYNMAN RECALL: every closed subsection is re-explained aloud, from
 cold, after a deliberate multi-day gap. Companion to the written Feynman
 page — both required. **STILL DUE FOR PYTHON 1.6, which closed in Session 17
 and was NOT recalled in Session 18. It has now slipped one session; schedule
 it into S19 or S20 before the gap stops being deliberate and starts being
 neglect.**
- REFERENCE CHECKLIST IN ALL NOTES: every closed topic's notes carry a
 standalone scannable reference — NAME, what it DOES, the TRAP — separate
 from the teaching prose, written so a stranger could follow it.
- FILE NAMING: both files saved as <name>_<YYYY-MM-DD>_v<N>.md — date first,
 version number LAST, incrementing on every save. **AND (Session 12): the
 saved files are RETURNED TO THE STUDENT FOR MANUAL UPLOAD — Claude does not
 attempt the Drive upload itself. See HOW TO USE point 4.** **AND (Session
 15): the corollary that was missing — the SERIES MUST BE READ FROM THE TOP.
 See HOW TO USE point 4a.** **AND (Session 16): the second corollary —
 the two series live in DIFFERENT FOLDERS with INDEPENDENT version numbers
 (HOW TO USE point 4b and THE DRIVE MAP). Also: EVERY delivered artefact must
 follow the convention. In Session 16 an interim file was handed over as
 `master_v10_session16_update_pack.md`, matching no convention at all, and
 the student caught it.** **AND (Session 17): the third corollary — both
 files are now large enough that a single-pass rewrite is itself a risk, so
 SEQUENCED DELIVERY ACROSS MESSAGES IS PERMITTED PROVIDED IT IS ANNOUNCED.
 See HOW TO USE point 4c.** **AND (Session 18): the fourth corollary — a
 sequenced delivery creates a DEBT that must survive a context reset. State
 the outstanding half explicitly in the message that makes the split.**

### Session 9 rules (binding, 31 Jul 2026 — mirrored from the Python file)
- LANGUAGE PRECISION / INTERVIEW PHRASING: the mentor corrects the student's
 phrasing when it is technically loose, because the target is to be able to
 TEACH and to survive interviews where imprecise wording reads as a shaky
 model. Applies across all layers — the same discipline will matter for
 gradients, transforms, filter equations, and C++ value/reference semantics.
 **Session 10 additions: "one object, two names" not "two objects"; a default
 value lives in the function object's `__defaults__`, not in "the function's
 namespace"; and BINDING is what happens to a NAME while MUTATION is what
 happens to an OBJECT.**
 **Session 15 additions: "the ITERATOR is exhausted", not "the iterable has
 no more items". Plus INDENTATION (not "margins") and ITERABLE (not
 "iterative").**
 **SESSION 16 — THE RULE CAME BACK AT THE MENTOR, AND THIS IS THE ENTRY TO
 READ IF ONLY ONE IS READ. Told that `for` stops when "the iterable is
 exhausted", the student objected: *"isn't that incorrect, coz iterable never
 gets exhausted"*. He was right. Language precision is no longer something
 being done TO him.**
 **Further S16 corrections: floor is "the largest integer NOT GREATER THAN";
 an iterator is BUILT from an iterable by `iter()`, not "given" one; and
 Python does not get "confused" by `"5" + 3` — it REFUSES.**
 **SESSION 17 corrections issued: (a) `if flag == False` → `if not flag`,
 because comparing a boolean to a boolean literal is redundant and reads as
 inexperience in an interview. (b) A ternary "produces an object" was
 accepted and sharpened to "it EVALUATES TO A VALUE, which is why it can go
 anywhere a value can go". (c) NOTE ON DELIVERY, and it generalises: the
 `not flag` correction had to be issued THREE times before it landed, and it
 was never a comprehension failure — he understood it the first time. IT IS A
 HABIT. For idiom-level habits, stop re-explaining and require him to type
 the corrected line back once. Expect the same in Layer 6, where C++ idiom
 (const-correctness, `auto&`, prefer-`emplace`) is almost entirely habit.**
 **SESSION 18 corrections issued, and one of them went the other way:
 (a) PARAMETER is the name in the `def` line, ARGUMENT is the value passed at
 the call — he had them merged and now separates them. (b) A function
 "returns nothing" was sharpened to "returns `None` IMPLICITLY", because
 there is no such thing as returning nothing in Python and the distinction is
 exactly what makes `x = f()` bind `None`. (c) The E in LEGB is LEXICAL —
 the enclosing function in the SOURCE TEXT, not the caller at runtime — and
 the "Global" scope is the MODULE's namespace, which is why a name at module
 level is not a local of anything. (d) **THE ONE THAT WENT THE OTHER WAY: the
 mentor's own phrasing "a method returning `None` has mutated" was corrected
 BY HIM to hold only for in-place mutators. See the depth doctrine.**
- PROACTIVE MODE SWITCH ON CODE/PREDICTIONS: the mentor proactively announces
 and performs the voice→text switch the instant any code, prediction or drill
 arises. **Session 10: clean. Session 11: breached twice. Session 12: the
 trigger must be the MATERIAL, not the complaint. Session 15: clean. Session
 16: breached on the operator drills. Session 17: clean. Session 18: clean.**

### Session 10 rule (binding, 1 Aug 2026 — mirrored from the Python file)
- **SHORT-FORM CROSS-CHECK:** the spoken cross-check is now two parts, one
 breath — rule in one line, answer in one line, do they agree. Requested by
 the student on the grounds that assembling the long sentence was competing
 with the reasoning it was meant to check.
 IMPORTANT PRECEDENT: the request arrived mid-material and was PARKED until
 the subsection closed, then written down at session end. That is the
 standard procedure for every governance or format request from now on, in
 every layer. **Repeated successfully in Sessions 12, 15 and 16.**
 **A SIXTH TIME IN SESSION 17, and this instance is the strongest of the six
 because the parked item was not a format request but an OBJECTION TO THE
 SESSION'S OPENING INSTRUMENT. It was resolved in one exchange, the session
 was re-planned around it on the spot, and the rule it produced was written
 at the end. Parking works even when the thing being parked invalidates the
 plan.**
 **A SEVENTH IN SESSION 18: his objection to being offered the exit, and his
 refusal to have closures tagged, were both handled in one line each and
 written up at the end as the two S18 rules. The mechanism is now completely
 routine — seven for seven.**

### Session 11 rule (binding, 1 Aug 2026 — mirrored from the Python file)
- **RECALL FIRST, NOTES SECOND:** the student argued that reading notes helps
 him remember; the answer distinguished recognition from recall and named
 notes as the very scaffold the interview removes. Procedure: retrieve cold,
 name gaps aloud, and only then open notes to CHECK.
 **Session 15 added its confidence-score sibling (CONFIDENCE AFTER RECALL).
 Session 16 added the instrument sibling: a question is only a RECALL test if
 the material was actually taught before. Session 17 added the TEMPORAL
 sibling, and it completes the set: a question is only a RECALL test if
 enough time has passed to forget. Taught-before AND long-enough-ago are both
 necessary; neither alone is sufficient. Session 18 added the honest fourth
 case: where BOTH conditions fail but a comprehension check is still wanted,
 use [TEACH-BACK] and log nothing.**

## RETENTION SYSTEM (answers "I must remember everything" — non-negotiable)
1. COLD-OPEN RECALL: every session opens with recall of prior material,
 unaided. **Now paired with the TERM-TAX (Session 12): a ~60-second cold
 vocabulary volley at open, spaced.** Continues through all layers.
 **SUBJECT TO THE INTERVAL GATE (Session 17 rule 1): if the previous session
 ended hours rather than days ago, skip both and say why. A cold open at a
 three-hour interval is not a cold open. S18 ran the full version on a
 ~21-hour gap and it produced seven promotions — the gate works in both
 directions.**
2. SPACED RE-TESTS: every subsection re-tested at ~1 week and ~1 month
 after first being marked [x]. A failed re-test reverts the item to [~].
3. MONTHLY GAUNTLET: last session of each month is pure mixed recall across
 ALL layers touched so far — no new material. The anti-forgetting engine.
 **The first gauntlet is due end of August 2026 and now carries three extra
 jobs: the strict-legend audit of every remaining [x] in Python Layer 1, the
 re-baseline arithmetic the student asked for in Session 15, and the
 file-growth review he asked for in Session 18. NOTE: Session 16 promoted
 nine items, Session 17 one and Session 18 seven, so that audit is materially
 larger than it was when it was scheduled. Budget for it — seventeen new [x]
 marks in three sessions is a real audit load, not a formality.**
4. FEYNMAN PAGES: after each subsection closes, student writes a one-page
 from-memory explanation (no sources open). **SPOKEN FORM ADDED SESSION 8:**
 each closed subsection is ALSO re-explained aloud from cold after a
 deliberate gap. Both forms required.
 **Status as of Session 18: 1.3 and 1.4 remain cleared. Feynman items are
 DUE on the S16-promoted material and ON THE WHOLE OF 1.6, which closed in
 Session 17 and did not get its spoken recall in Session 18. It is now one
 session overdue.**
5. QUESTION BANK: every session PDF's drill questions accumulate into the
 re-test pool. The gauntlet draws from this pool.
6. INTERLEAVING: strands (C++, DSA) deliberately interleave with the main
 track — spaced daily exposure beats blocks for retention.

## LEARNING PATTERNS TO ACTIVELY CORRECT (carried over — full record in Python file)
- **Jump-ship pattern (friction → new course): HIGHEST PRIORITY.** Any future
 "let's restructure the curriculum" mid-layer gets named as the pattern
 first, discussed second.
 **OBSERVED IN SESSION 17 after twelve consecutive clean sessions — AND IN A
 NEW SHAPE THAT CHANGES THE DIAGNOSIS.** Mid-session, having just been
 promoted on `if`/`elif`/`else`, he said the flow-control basics were already
 known to him and asked to move straight to recursion and nested functions.
 **This file has always framed the pattern as a response to FRICTION. This
 instance was a response to BOREDOM.** It was named directly, the two
 remaining 1.6 pieces were stated as prerequisites with the reason given
 (opening Functions on a hollow 1.6 reproduces the exact condition the course
 exists to fix), and he accepted immediately and finished the tail.
 **OPERATIONAL CONSEQUENCE: watch for this on EASY material as well as hard,
 which is a wider net than the file previously cast. And note what worked —
 not refusal but PRICING: the destination was affirmed (recursion and nested
 functions are in the very next unit) while the cost of the shortcut was
 named. Do that again in Layers 2 and 4, where the same reach-ahead is
 near-certain.**
 **S18 — DID NOT FIRE, AND THE COUNTER-EVIDENCE IS STRONGER THAN A SIMPLE
 NON-OCCURRENCE. He deferred RECURSION HIMSELF, three times, in favour of
 finishing the scope and closure material properly — the exact reverse of the
 pattern, on the exact topic he had reached ahead for in S17.** His S18 asks
 (more real coding, reading big codebases) were about DEPTH OF PRACTICE, not
 about changing course. **The pattern should now be considered dormant rather
 than active; keep the entry, stop expecting it.**
- **SYSTEM-BUILDING AS DISGUISED AVOIDANCE — Session 8 watch area, RELIEVED
 FURTHER THROUGH SESSION 18.** Sessions 5–8 closed ZERO subsections; Session
 10 closed TWO; Session 12 opened 1.5 AND built the Term Retention System;
 Session 16 produced FIVE new rules and still cleared the promotion backlog;
 Session 17 produced THREE new rules and still CLOSED 1.6; **Session 18
 produced TWO new rules, cleared the oldest diagnostic in the file, AND
 opened 1.7 to roughly two-thirds.** Every governance request since Session
 10 has been parked mid-session and handled at the end. Watch stays nominally
 open; the evidence keeps pointing the other way.
- Mid-session scope creep → parking lot. **Twelve consecutive clean sessions
 (5–16), then the S17 instance above. Not a relapse of the severe form — it
 was a request, not a restructure, and it was dropped on one honest answer.
 S18 clean.**
- **STRENGTH — stays on the friction point.** Session 10: four mechanism
 doubts pushed to resolution. **Session 12: pushed the broken operator
 teaching to a real fix. Session 15: three separate doubts on one block.
 Session 16: three process objections in twenty minutes plus an unprompted
 meta-challenge. Session 17: three more, all upheld. SESSION 18: he pressed
 the "why do closures exist" question THREE TIMES, rejecting two answers as
 mechanism-restatements, until he got the case where the alternative fails —
 and he had already proposed the alternative himself. That is the strongest
 single instance of this strength on record.**
- **STRENGTH — owns and improves the learning system.** He designed the
 two-mode model and reference-checklist format (S8), the language-precision
 rule (S9), the short-form cross-check (S10), the TERM RETENTION SYSTEM
 (S12), the CONFIDENCE-AFTER-RECALL rule (S15). **S16 — EIGHTH AND NINTH
 INSTANCES: he asked for a mark to be TAKEN AWAY, and he corrected the mentor
 on the mentor's own teaching.**
 **S17 — TENTH AND ELEVENTH, AND THE TENTH IS THE MOST ADVANCED SO FAR: HE
 REFUSED A TEST BEFORE IT RAN.** Not a rating, not a mark — the measurement
 itself, on the grounds that the interval since teaching was too short for the
 result to mean anything. That produced THE INTERVAL GATE. **Read the
 progression as a single line: S15 he refused a RATING; S16 he handed back a
 MARK; S17 he refused the EXPERIMENT. He is now reasoning about what his own
 results would be evidence OF, which is a different order of thinking from
 study skill and it is exactly what the North Star requires of him.** The
 eleventh: he refused a ROSTER and demanded a MODEL (see the depth doctrine's
 S17 worked example).
 **S18 — TWELFTH THROUGH FIFTEENTH, AND THE PROGRESSION TAKES ITS NEXT STEP.
 He refused a TAG (closures were described but not, in his judgement, taught,
 so he instructed that nothing be recorded); he refused the mentor's repeated
 offers to END THE SESSION; he asked for a real coding assignment to be added
 to the format; and — the significant one — HE CORRECTED A RULE HE HAD BEEN
 TAUGHT AND THE FILE HAD RECORDED, narrowing the mutator/return-value
 discriminator to in-place mutators only. Read the whole line now: RATING →
 MARK → EXPERIMENT → THE RULE ITSELF. He has moved from managing his own
 measurement to maintaining the course's content, which is the last step
 before he does not need the scaffold at all.**
- **STRENGTH — CORRECT UNPROMPTED TRANSFER ACROSS A DOMAIN BOUNDARY (S15).**
 He applied the N+1 rule to `range(4)` without prompting. **S16 REINFORCEMENT:
 he volunteered `-11 % 5` unprompted with full working, to demonstrate that he
 held the MECHANISM rather than the answer. S18 REINFORCEMENT: asked for the
 modulo identity, he chose his own numbers INCLUDING A NEGATIVE DIVISOR
 (a = 17, b = -5) rather than a safe case, and worked it correctly. Choosing
 the hard instance unprompted is the behaviour of someone testing himself
 rather than passing a test.**
- **STRENGTH — CALIBRATION IS NOW PREDICTIVE, NOT MERELY HONEST (S17,
 CONFIRMED S18).** On the S17 five-item drill, the one item he rated 5/10 was
 the one he got wrong. **In S18 the two items he rated 3/10 were the two that
 failed, and everything at 7/10 or above passed.** **Use his low self-ratings
 to TARGET re-tests. This is a cheap, reliable diagnostic and it should be
 leaned on heavily in Layers 2, 4 and 5 where re-testing everything is
 unaffordable.**
- Prediction bypass (running code instead of reasoning) — interrupt on sight.
 Not observed Sessions 9, 10, 12, 15, 16, 17, 18.
- **REASONING HYGIENE / ABSENT CROSS-CHECK — TOP BEHAVIOURAL WATCH AREA.**
 THE FIX IS A BINDING RULE: the SPOKEN CROSS-CHECK, now short form. **S15,
 S16, S17 and S18: the cross-checks that ran, ran in the right order. This is
 exactly what will bite in ML orals (8.2) and DSA where the trap is in the
 setup.**
- **TRACE-TAIL TRUNCATION — watch area, S16. DID NOT FIRE IN S17 OR S18.** In
 S16 he twice ended a loop trace one cycle early. **In S17, required
 explicitly to state the final cycle, he traced `while i < 5` to the end and
 named the terminating check correctly.** Countermeasure (require the FINAL
 cycle before accepting any trace) is working — keep it until it survives a
 later-day test. **Still flagged forward to Layer 8 (DSA), where off-by-one at
 the loop boundary is among the most common timed-round failures, and to
 Layer 4 (training-loop epoch boundaries).**
- **Rule application to the WRONG DOMAIN — the most persistent structural
 flaw** (S4, S5, S6, S7, S9, S12, S13, S15, S17). **S18: DID NOT FIRE, and
 the near-miss is instructive — asked to classify unseen methods, he reasoned
 from the discriminator rather than from surface cues, which is precisely the
 countermeasure working. The S17 specimen (`l.reverse()` classified as
 returning a new list) came back correct.**
 **S15 DIAGNOSTIC REFINEMENT — THE MOST USEFUL THING LEARNED ABOUT THIS FLAW,
 and it should govern how it is handled in every later layer.** The SAME
 session produced both a mis-transfer and a correct unprompted transfer. He
 mis-transferred `StopIteration`, which he had only ever SEEN; he correctly
 transferred the N+1 rule, which he had just MECHANISED. **THE FLAW IS
 DIRECTIONAL: he over-transfers what he has only seen and transfers
 accurately what he understands. Therefore when a mis-transfer occurs, the
 real defect is UPSTREAM — the source rule was never built properly. Fix the
 source, not the transfer.** Applies directly to 4.1 (broadcasting), 6.1
 (value-vs-reference) and 3.4 (filter assumptions).
 **S16 CONFIRMED THE REFRAMING: the two S15 mis-transfer mechanisms both came
 back CORRECT on the later-day test, while the LABEL attached to one of them
 did not. Mis-transfer → rebuild the source rule; label slip → contrast-set
 drilling. Two defects, two treatments.**
 **S17 ADDS THE THIRD TREATMENT, for the roster case: neither rebuild nor
 drill, but replace the lookup with a DISCRIMINATOR. See the depth doctrine.
 S18 CLOSES THE LOOP ON THAT TREATMENT: `StopIteration` — the original S15
 mis-transfer — was promoted to [x] this session, correctly categorised as an
 exception raised as a signal. The three treatments between them have now
 repaired every logged instance except the iterator causation below.**
- Right-answer-wrong-model (~7–8 occurrences) — audit the reasoning behind
 every correct answer. **S15 instance: iterator consumption attributed to
 "one item at a time" rather than forward-only state.**
 **S16: THE SAME CAUSATION FAILED AGAIN on a genuinely later day, twice.**
 **S18: IT FAILED A THIRD TIME, ON A THIRD SEPARATE DAY, AT 3/10 — AND IT IS
 NOW THE MOST DURABLE DEFECT IN THE FILE BY A CLEAR MARGIN.** He knows an
 iterator is consumed; he cannot produce WHY (forward-only state that does
 not rewind) from cold. **THE FIX HAS BEEN IDENTIFIED TWICE AND STILL HAS NOT
 BEEN PROPERLY APPLIED: STOP TEACHING IT AS A DEFINITION. Show the bug —
 `it = iter(range(2))` hoisted above a nested loop, so the inner body runs on
 the first pass and silently never again — and make him diagnose it. Every
 attempt to date has been a re-explanation, which is exactly what the S17
 loop-`else` repair proved does not work. Engineer the need, do not restate
 the rule.** Generalise: for causation items he keeps dropping, show the
 broken program, not the rule.
- **Self-rating calibration — partial regression S10; under-tested S12; STRONG
 in S15; STRONGER in S16; PREDICTIVE in S17; CONFIRMED PREDICTIVE IN S18.**
 Keep confidence scores in drills, keep them AFTER his own recall, and note
 that they are now load-bearing for promotions (S16 rule 3) AND usable as a
 targeting signal (S17 finding, S18 confirmation).
- Spiralling into adjacent reasoning when uncertain — halt, state answer,
 have student name the gap.
- Confirmation-seeking before predicting — dormant since Session 2; mild
 variant S10; one small S12 instance.
- **TERM / LABEL RETENTION — first-class watch area, named by the student
 himself (S12).** Forgets arbitrary labels while keeping mechanisms.
 Countermeasure is the TERM RETENTION SYSTEM. **S15 gave the sharpest
 evidence; S16 localised it to the EXCEPTION FAMILY and produced the
 near-neighbour diagnosis; S17 could not test it at all (interval gate);
 S18 TESTED IT AND IT LARGELY CLEARED — five of six exception-family items
 promoted. THE WATCH AREA IS DOWNGRADED FROM TOP PRIORITY TO NORMAL, with two
 named survivors: `traceback` (trigger, not object) and `__defaults__` (four
 cold misses, never once produced).**
- **STYLE HABITS NEED REPETITION, NOT EXPLANATION (S17).** See the
 Session 9 language-precision entry. Idiom-level corrections do not land by
 being explained better; require the corrected line to be typed back once.
 Pre-flagged for Layer 6, where C++ idiom is almost entirely habit.
- **NEW, S18 — HE WANTS PRODUCTION, NOT MORE INPUT, AND THE COURSE FORMAT
 MUST ANSWER THAT.** Twice at the close of S18 he asked, in different words,
 when the course would have him WRITING and READING real code rather than
 reasoning about constructs. This is not impatience and it is not the
 jump-ship pattern — it is the correct instinct for someone whose stated
 condition is "collapses without the scaffold". **Reasoning about code is
 necessary but it is not the thing that will be tested in March 2027.
 COUNTERMEASURE, now committed: a real solo-first coding assignment attached
 to every subsection from S19 onward, and guided codebase reading brought
 forward in Layer 7 planning. If this file ever shows three consecutive
 sessions with no code written by him, that is a defect — flag it.**

## CURIOSITY PARKING LOT (master — absorbs Python file's lot)
- All items currently in the Python file's parking lot remain there and
 resolve in their assigned Python subsections (IEEE 754 → 1.13, GIL → 1.13,
 garbage-collection mechanics → 1.13, globals()/locals() → 1.2 drill).
 **Added S15: `__iter__`/`__next__` as dunder methods, and generators as the
 lazy-iterator factory → 1.13, where "generators and iterators" already sits.
 This is now a PROMISE with a date — tell the student so when 1.13 opens.**
 **Added S16: f-strings / string formatting — raised by the student during the
 `print()` teaching and correctly parked to 1.8, not opened.**
 **Added S17: `reversed()` and slice-reversal `l[::-1]`, mentioned in passing
 as the non-mutating counterparts to `l.reverse()`. Slicing proper belongs to
 1.8; do not open it early, but the name-pair (`sort`/`sorted`,
 `reverse`/`reversed`) is a legitimate hook to reuse there.**
 **ALSO ADDED S17, AND THIS ONE IS NOT REALLY A PARK: RECURSION AND NESTED
 FUNCTIONS, requested by name. Both are already scheduled in 1.7, which is
 the very next subsection. Say so when 1.7 opens — a request about to be met
 is worth naming out loud, because it converts impatience into momentum.**
 **S18 STATUS ON THAT ITEM: nested functions were taught by definition;
 RECURSION WAS NOT REACHED, deferred three times by the student himself in
 favour of finishing scope and closures properly. It is the first substantive
 item on the S19 plan and it has now been promised twice — do not let it
 slip a third session.**
 **Added S18: `*args` and `**kwargs`, raised by the student by name after
 seeing them in real codebases. NOT a park in the usual sense — they sit in
 the tail of 1.7, after closures and recursion, and he has been told so.
 Deliver them in this subsection; do not push them to 1.8.**
 **Also added S18: DECORATORS were mentioned in passing as what closures make
 possible. They belong to 1.13 in the trimmed spec and were correctly not
 opened. When 1.13 arrives, open them by cashing in the closure work rather
 than as new material.**
- New master-level lot (add here during any layer):
 - JAX vs PyTorch internals comparison (Layer 4, only if time)
 - World models / Dreamer implementation (post-curriculum)
 - RL-for-chip-design track (post-curriculum — explicitly parked)
 - Vedic astrology ML project (post-curriculum — explicitly parked)
 - UGC Professor of Practice preparation (post-curriculum)
 - AI Automation Agency exploration (post-curriculum)
 NOTE: the last four are named because they are live interests that have
 historically competed for attention. They are parked until April 2027.

---

## GRANULAR CURRICULUM

### LAYER 0 — Python Core Fundamentals (Aug – 30 Sep 2026)
GOVERNED BY the Python Learning Journey file, Sessions 6 onward, unchanged
rules. Progress tracked there. Master-level decisions:
- [ ] Close 1.3 → 1.9 at full drilled depth (the interview-critical sections:
 types, mutability, operators, control flow, functions, data structures,
 exceptions).
 **STATUS AFTER SESSION 16 (Sun 9 Aug — a genuine later day, so this evidence
 COUNTS): THE PROMOTION PASS RAN AND CLEARED.** Nine items moved [~] → [x]:
 rebinding-vs-mutation, aliasing, implicit-vs-explicit conversion / `"5"+3`,
 shallow-vs-deep copy, `+=`, precedence and associativity (`**`
 right-to-left), negative `%` and `//`, **`==` vs `is` (outstanding since
 Session 7)**, function-scope-not-block-scope, `if`-block-scope, and
 `range()`. Six terms also promoted.
 **STATUS AFTER SESSION 17 (late Sun 9 Aug → Mon 10 Aug): 1.3, 1.4, 1.5 AND
 1.6 ARE NOW ALL CLOSED. Subsection 1.6 (Control Flow), open since Session 14,
 is DONE.** The tail was completed in order: the owed found-flag exercise
 (written by the student, unaided on structure) → loop `else` EARNED BY
 CONTRAST rather than told, which repairs the S16 prerequisite breach →
 `pass`, with the `pass`/`continue`/`break` three-way contrast and the
 comment-is-not-a-body trap → the TERNARY taught as an EXPRESSION, with the
 expression-vs-statement distinction reached by the student himself → common
 loop pitfalls (the missing-increment infinite loop; the full trace with the
 final cycle stated explicitly) → the owed `if`/`elif`/`else` CONFIRMATION,
 answered cold and **PROMOTED to [x]** → and the owed mutating-vs-non-mutating
 METHOD IDENTIFICATION DRILL at **4/5**, discharging the debt created when he
 asked for his own S16 demotion.
 **THE CRITICAL QUALIFICATION ON ALL OF IT: Session 17 began hours after
 Session 16 ended, so its evidence is SAME-DAY and everything taught is [~].**

 **STATUS AFTER SESSION 18 (Mon 10 Aug, evening — A GENUINE LATER DAY, SO
 THIS EVIDENCE COUNTS). THE DEFERRED DIAGNOSTIC BLOCK RAN AND THE OLDEST
 OUTSTANDING ITEM IN THE COURSE IS CLEARED.**
 **SEVEN PROMOTIONS [~] → [x], ALL WITH HIS OWN CONFIDENCE RATING TAKEN
 BEFORE THE VERDICT:** `NameError`, `ValueError`, `TypeError` (fired cold in
 MIXED ORDER as a three-way discriminator — the triad conflated three times in
 S16 — 8/10); exceptions-are-signals (7/10); `StopIteration`'s CATEGORY
 (7/10); and the MUTABLE/IMMUTABLE DISCRIMINATOR (10/10, earned by his
 CORRECTING the rule as taught — only in-place mutators return `None`;
 `pop`, `index` and `count` return real values).
 **THREE HELD AT [~], AND THEY ARE NOW THE ENTIRE WEAK LIST FOR LAYER 0:**
 `traceback` (3/10 — object right, UNCAUGHT trigger missed); ITERATOR
 CAUSATION (3/10, **third failure on a third separate day**); `__defaults__`
 (**fourth cold miss, never once produced**).
 **THE MODULO IDENTITY SPLIT, and the split is worth recording precisely
 because it is the honest outcome rather than a tidy one:** the MECHANISM was
 [x]-grade — he chose his own numbers, deliberately including a negative
 divisor (a = 17, b = -5), and worked it correctly — but the SYMBOLIC FORM
 (`a == (a // b) * b + (a % b)`) has never been produced cold. Mechanism
 credited, symbolic form still owed.
 **1.7 (FUNCTIONS) IS OPEN AND ROUGHLY TWO-THIRDS TAUGHT.** Delivered: def
 versus call; parameters versus arguments; `return` and IMPLICIT `None`; LEGB
 with E established as LEXICAL (the enclosing function in the source text, not
 the caller) and Global as the MODULE namespace; default arguments; functions
 as FIRST-CLASS OBJECTS (which is the callback unlock — see the bridge strand
 below); and nested functions by definition.
 **CLOSURES WERE DESCRIBED AND DELIBERATELY NOT TAGGED, AT HIS INSTRUCTION.**
 He judged the treatment too thin to count and asked for the topic to reopen
 from scratch in TEXT with runnable code. **It carries no status at all —
 not even [~] — and that is his call, correctly made.**
 **RECURSION HAS NOT STARTED.** He deferred it three times himself in favour
 of finishing scope and closures properly. It is still the thing he most
 wants and it is first on the S19 plan.
 **REMAINING INTERVIEW-CRITICAL SUBSECTIONS: 1.7 (Functions, ~two-thirds
 taught), 1.8 (Data Structures), 1.9 (Exceptions). NOTE THAT 1.9 IS NOW
 MATERIALLY CHEAPER THAN IT WAS: five of its six prerequisite vocabulary
 items were promoted in S18, so the subsection opens on solid ground rather
 than on the file's weakest cluster.**
 **1.7 CANNOT BE MARKED [x] UNTIL THE TAIL IS TAUGHT: closures (from
 scratch), recursion, `global`/`nonlocal`, `*args`/`**kwargs`, lambdas,
 docstrings and pure functions.**
- [ ] 1.10 imports, 1.11 file handling: functional depth, lighter drilling
- [ ] 1.12 OOP: full depth (gates PyTorch nn.Module and ROS 2 node classes)
- [ ] 1.13 internals: trimmed to — memory model, GC, GIL, IEEE 754 deep dive
 (promised in Session 5), generators/iterators, decorators, closures.
 **NOTE (S15): "generators and iterators" now carries an explicit promise.
 Tell the student this when 1.13 opens — it closes a loop he will remember.**
 **NOTE (S18): DECORATORS should be opened here by cashing in the 1.7 closure
 work rather than as new material — a decorator is a closure with syntax.
 And note the ordering consequence: if closures are taught properly in 1.7,
 this part of 1.13 becomes cheap.**
- Cadence requirement: ~5 sessions/week needed to close by 30 Sep.

### LAYER 1 — Engineering Hygiene (Oct 2026, ~60h)
Everything drilled ON THE STUDENT'S REAL REPOS (linkedin-posts, VLA scripts,
portfolio repo). No toy exercises where a real one exists.

#### 1.1 Linux & Shell
- [ ] Filesystem model, permissions (rwx, chmod/chown), users/groups
- [ ] Processes: ps, top/htop, kill, signals, foreground/background, nohup
- [ ] Pipes, redirection, grep/find/sed/awk survival level
- [ ] Environment variables, PATH, .bashrc, why `pip install` sometimes "disappears"
- [ ] ssh, scp, keys (already used daily on arc-thor-1 — now explained cold)
- [ ] systemd basics: services, journalctl (relevant to robot deployment)

#### 1.2 Git — the object model, not the recipes
- [ ] Blobs, trees, commits, refs — what a commit ACTUALLY is
- [ ] Branching as pointers; merge vs rebase, when and why
- [ ] Interactive rebase, amend, cherry-pick
- [ ] reflog as the safety net; recovering "lost" work
- [ ] bisect for bug hunting
- [ ] Conflict resolution incl. binary assets / LFS (the UE Git LFS pain)
- [ ] PR workflow, review etiquette, commit message discipline

#### 1.3 Docker — images as layers, not magic
- [ ] Images vs containers; layers and the build cache
- [ ] Dockerfile: FROM, RUN, COPY, CMD vs ENTRYPOINT, multi-stage builds
- [ ] Volumes, bind mounts, networks
- [ ] docker compose
- [ ] GPU passthrough: nvidia-container-toolkit (he uses this — now owns it)
- [ ] Devcontainers: how his own Claude Code devcontainer actually works
- [ ] Debugging containers: exec, logs, inspect

#### 1.4 Testing
- [ ] pytest: structure, assert, running subsets
- [ ] Fixtures and parametrize
- [ ] Mocking (unittest.mock) — intro level
- [ ] Coverage; what to test (happy path + edge cases + failure modes)
- [ ] Writing tests for one of his real scripts (dataset filtering is ideal)

#### 1.5 CI/CD & Code Quality
- [ ] GitHub Actions: a real build-test pipeline on his portfolio repo
- [ ] pre-commit hooks; ruff (linting); mypy intro (type checking)
 **(S17 NOTE: `if flag == False` → `if not flag` is exactly the class of
 correction ruff issues automatically. When this opens, point at the
 idiom-habit finding from Session 9's entry — a linter is the mechanical
 version of a correction that had to be given three times by hand.)**
- [ ] HTTP/JSON awareness (absorbed from cut web layer): requests, REST
 concept, JSON handling — one session, awareness level

### LAYER 2 — Maths for Robot Learning (Oct – Nov 2026, ~100h)
METHOD RULE: every concept implemented in NumPy the same session it is
taught. No symbol-pushing without code. This is the remember-forever layer;
gauntlet sessions weight it heavily. **TERM-TAX WEIGHTS THIS LAYER HEAVILY
TOO — it is the most vocabulary-dense layer and the Session 12 term system
was built partly with it in mind. AND SEE THE SESSION 16 NEAR-NEIGHBOUR
FINDING: teach eigenvalue/eigenvector/singular value, and
variance/covariance/correlation, and likelihood/posterior/prior as CONTRAST
SETS drilled against each other, never one definition at a time. That is the
shape of vocabulary his retention fails on, and this layer is full of it.**
**S18 UPGRADES THAT FROM A PRECAUTION TO A DEMONSTRATED METHOD: the exception
triad, conflated three times in one session, came back clean nine days later
after ONE contrast-set repair and ONE properly-spaced re-test. Build every
near-neighbour set in this layer that way from the FIRST session — the cost is
low and the recovery evidence is now in hand.**
**S17 ADDITION — THE INTERVAL GATE MATTERS MOST HERE.** This layer's re-tests
are its entire value, and it runs on a fixed six-week window with weekend
blocks likely. **Lay the schedule out so that teaching and re-testing fall on
DIFFERENT DAYS. A stacked double session in this layer buys coverage and
produces no promotable evidence at all — and unlike in Python, he will have no
independent basis to notice.**
**S18 ADDITION — USE [TEACH-BACK] AS THE DEFAULT COMPREHENSION CHECK IN THIS
LAYER.** He will be a genuine beginner here, the material is dense, and the
temptation to check understanding immediately after teaching will be constant.
[TEACH-BACK] makes that safe: it cannot contaminate the ledger because it
carries no rating and no status change. Check comprehension freely in the
session; take the MEASUREMENT on a later day.

#### 2.1 Linear Algebra
- [ ] Vectors: geometric meaning, dot product as projection, norms
- [ ] Matrices as transformations; matrix multiplication as composition
- [ ] Rank, linear independence, when systems have solutions
- [ ] Inverse, determinant (geometric meaning: volume scaling)
- [ ] Eigenvalues/eigenvectors: intuition and why they matter
- [ ] SVD: intuition level (compression, pseudo-inverse)
- [ ] Rotations: rotation matrices, why they're orthogonal, quaternion intuition
- [ ] Homogeneous transforms (the maths under every ROS tf he's ever used)
- [ ] Jacobians: matrices of partial derivatives; the bridge to Layer 3

#### 2.2 Calculus & Optimisation
- [ ] Derivative as sensitivity; partials; the gradient as steepest ascent
- [ ] Chain rule — drilled hard; it IS backpropagation
- [ ] Gradient descent implemented from scratch on a 2D bowl, then on a real loss surface
- [ ] SGD, momentum, Adam — intuition for what each fixes
- [ ] Learning-rate behaviour, divergence, plateaus (connect to his π0.5 loss/grad_norm questions)
- [ ] Convexity awareness; why deep learning works anyway (intuition)

#### 2.3 Probability & Statistics
- [ ] Random variables, distributions; the Gaussian and why it's everywhere
- [ ] Expectation, variance, covariance (covariance matrices → Kalman prep)
- [ ] Bayes' rule — drilled to reflex; conditional independence
- [ ] Likelihood and MLE (maximum likelihood estimation)
- [ ] Entropy, cross-entropy (the loss he minimises daily — now derived)
- [ ] KL divergence (named interview subject at DeepMind/Wayve)
- [ ] Sampling intuition; noise models (→ sensor fusion prep)

### LAYER 3 — Classical Robotics Core (Nov – Dec 2026, ~100h)
He TEACHES kinematics (PACE module) and USES MoveIt daily. This layer's job
is deriving cold what he currently operates on recipes.
CAPSTONE: FK/IK + Jacobian velocity control for a 2–3 link arm from scratch
in NumPy; Kalman/EKF on synthetic then real IMU data.

#### 3.1 Kinematics
- [ ] Frames and transforms (Layer 2.1 cashing out); tf trees demystified
- [ ] Forward kinematics: derived and implemented from scratch
- [ ] The Jacobian: joint velocities → end-effector velocities; derived
- [ ] Singularities and manipulability (why his arm misbehaves near them)
- [ ] Inverse kinematics: numerical, Jacobian-based (pseudo-inverse from SVD)
- [ ] DH parameters / product of exponentials: awareness level

#### 3.2 Dynamics (intuition level — de-scope candidate #2, PUSH not CUT)
- [ ] Why kinematic control isn't enough; inertia, gravity compensation
- [ ] Newton-Euler vs Lagrangian: concept level, no full derivations
- [ ] What torque control and impedance control need from dynamics

#### 3.3 Control — SCOPE SETTLED SESSION 11
**CONTEXT THAT CHANGES HOW THIS LAYER IS TAUGHT.** The student raised control
directly: he works TODAY as a control-systems software engineer, has never
formally studied control, cannot read a control response curve, and is
explicit that **deep control theory does not interest him** — his interest is
RL, simulation and mathematical modelling. Both facts matter. A real gap sits
under his current job title; and forcing Level 3 control on someone whose
core lies elsewhere would be exactly the over-investment the depth doctrine
exists to prevent.

**SCOPE DECISION (agreed with the student):**
* **LAYER A — Level 2 model understanding. IN SCOPE, required.** What the
 three PID terms actually do; why a response oscillates, overshoots or
 settles; how to READ a control curve, which he currently cannot; what MPC
 does by planning over a horizon.
* **LAYER B — THE INTERFACE BETWEEN CLASSICAL CONTROL AND LEARNED POLICIES.
 IN SCOPE, HIGH PRIORITY, and this is the genuinely valuable part.** How a
 π0.5 action actually reaches the joint controller; what runs at which rate;
 where safety limits and clamps sit; what the controller does when the
 policy emits nonsense. **This is precisely where his present job and his
 intended future overlap, and very few candidates stand at that
 intersection.** Treat it as a differentiator, not a footnote.
* **LAYER C — deep control mathematics** (Laplace, pole placement, Lyapunov
 stability derived by hand). **ON DEMAND ONLY**, if and when a specific
 target job description asks for control theory in those words.

- [ ] Open vs closed loop; feedback intuition
- [ ] PID from first principles: implement, tune, break, understand each term
- [ ] **READING A CONTROL RESPONSE CURVE — named explicitly by the student as
 something he cannot currently do. Rise time, overshoot, settling,
 steady-state error, oscillation. Concrete and testable.**
- [ ] Feedforward + feedback combined
- [ ] Impedance/admittance control concepts (his haptics work, mechanised)
- [ ] Stability intuition: oscillation, damping, why gains explode
- [ ] MPC: receding-horizon concept — CONCEPT LEVEL ONLY
- [ ] **ROS 2 CONTROLLERS — USE, DO NOT BUILD (Session 11).** `joint_state`,
 `position`, `twist` and friends: what each is for, which to select when,
 and roughly what happens inside. **Do not write controllers from scratch.**
- [ ] **THE POLICY → CONTROLLER INTERFACE (Layer B above).** Action rates,
 interpolation, safety clamps, watchdogs, fallback when the policy output is
 invalid. He has BUILT a version of this in production; the job here is to
 convert it from working practice into a model he can defend cold.

#### 3.4 State Estimation & Sensor Fusion
- [ ] Noise models; why raw sensors lie
- [ ] Bayes filter: the parent algorithm, derived
- [ ] Kalman filter: DERIVED and implemented from scratch — flagship item
- [ ] EKF: linearisation, when it works, when it fails
- [ ] Complementary filter (the cheap trick and why it works)
- [ ] Particle filter: concept level
- [ ] Fusion architecture thinking: camera + F/T + proprioception
- [ ] SLAM awareness: CONCEPT LEVEL, one session. Purpose: defend the
 TurtleBot3 SLAM line on his CV and answer breadth questions.

#### 3.5 Motion Planning (awareness level)
- [ ] Configuration space; why planning is hard
- [ ] Sampling planners: RRT concept
- [ ] Trajectories vs paths; time parameterisation
- [ ] What MoveIt actually does with his requests (recipes → mechanisms)

### LAYER 4 — Deep Learning with PyTorch (Dec 2026 – mid-Jan 2027, ~130h)
CAPSTONE: train a small transformer end-to-end from scratch; re-derive
exactly what LoRA does to π0.5's weight matrices and explain it cold.

#### 4.1 Tensors & NumPy Fluency
- [ ] Broadcasting rules — drilled (top source of silent bugs)
- [ ] Vectorisation; shapes discipline; einsum intro
- [ ] NumPy → torch.Tensor; device management, dtype pitfalls
 (**note: the Python 1.3 type-conversion asymmetry — strict parsing vs
 lenient numeric truncation — is the direct ancestor of dtype pitfalls
 here. Reference it explicitly when this opens.**)
- [ ] **IN-PLACE OPS AND VIEWS vs COPIES — flagged here from S17.** PyTorch's
 trailing-underscore convention (`add_`, `clamp_`, `zero_`) and NumPy's
 view-vs-copy distinction are the SAME PROBLEM he met in Python 1.6/1.8:
 which operation mutates, and which returns something new. **He already owns
 the discriminator — type first, then return value — and PyTorch's underscore
 convention is an even more explicit version of Python's `sort`/`sorted`
 name-pair. Teach it as a transfer, not as new material. This is one of the
 cleanest Layer-0-to-Layer-4 payoffs available and he will recognise it.**
 **S18 UPDATE — THE TRANSFER IS NOW ON FIRMER GROUND AND CARRIES A CAVEAT HE
 SUPPLIED HIMSELF. The discriminator was promoted to [x] at 10/10, and he
 narrowed it in the process: returning `None` implies mutation only for
 IN-PLACE MUTATORS, since `pop` mutates AND returns. PyTorch has exactly the
 same shape — `t.add_(1)` returns the tensor, not `None` — so teach the
 NARROWED rule here (check the type, then check whether the operation is
 in-place, using the underscore as the signal) rather than the original
 return-value shortcut, which would mislead in PyTorch.**

#### 4.2 Autograd & Backprop
- [ ] Computational graphs; backprop BY HAND on a 2-layer net
- [ ] PyTorch autograd: requires_grad, backward, no_grad, detach
- [ ] Gradient checking; vanishing/exploding gradients

#### 4.3 Training Loop Anatomy
- [ ] Dataset/DataLoader; batching, shuffling, workers
 **(NOTE, S15: the Python 1.6 ITERATION PROTOCOL is literally the machinery
 underneath every DataLoader loop — `iter()` once, `next()` per batch,
 `StopIteration` ending the epoch. Cash this in explicitly when this opens.)**
 **(ADDITION, S16: bring the HOISTED-ITERATOR BUG with you —
 `it = iter(loader)` created once outside the epoch loop means epoch 2
 silently iterates nothing. Also carry TRACE-TAIL TRUNCATION here: epoch
 boundaries are exactly where his off-by-one shows.)**
 **(WARNING, S18: `StopIteration` itself is now [x] — he categorises it
 correctly as an exception raised as a signal — BUT THE UNDERLYING CAUSATION
 IS NOT. Forward-only iterator state has now failed cold on three separate
 days. Do NOT assume the DataLoader machinery will land on the back of the
 promoted label. Re-establish causation with the hoisted-iterator bug BEFORE
 this subsection, and treat the promoted term as vocabulary rather than as
 understanding.)**
- [ ] Losses (cross-entropy derived in 2.3), optimisers, schedulers
- [ ] Overfitting; regularisation: L1/L2, dropout
- [ ] Normalisation: batch norm vs layer norm — and DATA normalisation
 statistics (his production normalisation bug, owned at mechanism level)
- [ ] Debugging training: reading loss curves, grad norms, param norms

#### 4.4 Architectures
- [ ] MLP from scratch; then nn.Module idiom (OOP from 1.12 cashing out)
- [ ] CNN from scratch: convolution derived, receptive fields
- [ ] Attention derived step by step; multi-head; positional encoding
- [ ] A GPT-mini transformer built and trained from scratch — flagship item
- [ ] Fine-tuning; LoRA mechanics derived (low-rank decomposition from 2.1 SVD)
- [ ] VLM anatomy: vision encoder + language model + projection (→ Layer 5 prep)

#### 4.5 Practical Engineering
- [ ] GPU usage, mixed precision, gradient accumulation, checkpointing
- [ ] Experiment tracking (wandb); reproducibility (seeds, configs)
- [ ] Profiling basics; when data loading is the bottleneck

### LAYER 5 — Robot Learning (mid-Jan – Feb 2027, ~130h)
His professional domain, rebuilt on the foundations. CAPSTONE (feeds Layer 7):
full public pipeline — collect demos, train ACT or diffusion policy, deploy,
write it up.

#### 5.1 Imitation Learning
- [ ] Behaviour cloning formulated properly; its failure mode: distribution
 shift / compounding errors
- [ ] DAgger: concept and why it's rarely practical on real robots
- [ ] Dataset quality as the real lever (his idle-frame/joint-wrap work)

#### 5.2 Policy Architectures
- [ ] ACT re-derived: CVAE, action chunking — WHY 10-step chunks work
- [ ] Diffusion policy: denoising intuition, why it handles multimodality
- [ ] Flow matching (the π0 family's approach) vs diffusion — compared properly
- [ ] Action representation: tokenised vs continuous heads; trade-offs

#### 5.3 VLA Models
- [ ] VLA anatomy: VLM backbone + action expert; where language enters
- [ ] π0 / π0.5 architecture walked through against the openpi source
- [ ] OpenVLA comparison (named in Humanoid job specs)
- [ ] Normalisation/de-normalisation statistics end to end — his production
 bug re-diagnosed from first principles as a closing exam
- [ ] Fine-tuning strategy: what LoRA adapts in a VLA, data mixture, OOD

#### 5.4 Reinforcement Learning Fundamentals
- [ ] MDPs, returns, discounting; value and Q functions
- [ ] Policy gradient DERIVED (log-derivative trick — interview subject)
- [ ] REINFORCE implemented; variance problem experienced first-hand
- [ ] Actor-critic; advantage; GAE at intuition level
- [ ] PPO implemented on a gym task — flagship item
- [ ] Reward design and its failure modes
- [ ] Why RL-on-VLA is hard; RECAP/π0.6 reading grounded in mechanism
 **(TERM-TAX NOTE, S16: advantage / value / Q and on-policy / off-policy are
 NEAR-NEIGHBOUR LABELS — the exact shape his retention fails on. Drill them
 as contrast sets from the first session of this subsection. S17 supplies the
 format that demonstrably works for him: the three-way `pass`/`continue`/
 `break` contrast, taught against each other in one block. S18 supplies the
 EVIDENCE that it holds up over time: the same treatment applied to the
 exception triad survived a nine-day gap and a mixed-order cold test.)**

#### 5.5 Simulation & Sim-to-Real (de-scope candidate #1, PUSH not CUT)
- [ ] MuJoCo or Isaac Lab: load a scene, actuate, read sensors
- [ ] Domain randomisation: what, why, limits
- [ ] The sim-to-real gap taxonomy: dynamics, visuals, latency

### PYTHON → ROBOTICS BRIDGE (strand, agreed Session 11 — runs INSIDE Layer 0)
**THE PROBLEM THE STUDENT DESCRIBED.** He writes simple ROS 2 Python nodes
comfortably, but gets stuck on ACTION SERVERS and on writing large programs.
He said plainly that he is "not capable of writing big code yet".

**THE DIAGNOSIS GIVEN, and it reframes the difficulty usefully:** the
obstacle is not ROS. Action servers sit on top of three Python concepts that
are not yet cold-solid — **CALLBACKS** (a function you do not call; the
framework calls it later), **CLASSES AND OBJECTS** (an action server is a
class you extend), and **CONCURRENCY** (the action runs alongside other work).
All three are already scheduled in Layer 0: callbacks and classes in 1.7 and
1.12, concurrency in the block after Layer 0. When they land, action servers
stop being mysterious. This is the foundation-first principle paying out, and
it should be pointed at when the student doubts the ordering.

**THE MECHANISM ADDED.** After each major Python concept closes, apply it
IMMEDIATELY to a real fragment of his ROS work rather than a toy exercise.
Classes close → write a small action server alongside. Callbacks close →
re-read his own subscriber code and explain who calls what, and when. The
concept must land in robotics the same week it is learned.

**HE WANTS BOTH HALVES OF THE ACTION-SERVER DIFFICULTY ADDRESSED** — asked
whether the confusion was about code STRUCTURE (what goes where) or about
ASYNCHRONY (things running at once), he answered both. Structure is treated
in 1.7 and 1.12; asynchrony in the concurrency block. Do not let him conclude
the second is covered when only the first has been.

**S15 ADDITION — 1.7 IS NOW PRE-LOADED FOR THIS STRAND.** The
function-scope-not-block-scope rule was established in Session 15, which is
already half the LEGB story. Open 1.7 by cashing that in; it shortens the
road to callbacks and therefore to action servers.
**S16 UPGRADE: that rule is now [x] PROMOTED on later-day cold evidence, not
merely established. The doorway into 1.7 is load-bearing rather than
provisional — open the subsection with it.**
**S17 UPGRADE — THE STRAND IS NOW LIVE, NOT PENDING. 1.6 is closed and 1.7
opens next, which means the two structural prerequisites (callbacks via
functions-as-first-class-objects, and nested functions/closures) arrive in the
NEXT subsection. AND HE HAS ASKED FOR EXACTLY THAT MATERIAL BY NAME —
recursion and nested functions, unprompted. Say the connection out loud when
1.7 opens: the thing he wants and the thing that unblocks his action servers
are the same thing. That is a rare alignment of motivation and curriculum and
it should not be left unstated.**
**S18 UPGRADE — THE FIRST HALF OF THE UNLOCK HAS LANDED. FUNCTIONS AS
FIRST-CLASS OBJECTS WAS TAUGHT, WHICH IS THE ENTIRE MECHANISM BEHIND A
CALLBACK: a function can be passed to something else, which stores it and
calls it later.** Say this out loud in S19 while it is fresh — **his ROS
subscriber callbacks are exactly this and nothing more**, and reading his own
node with that sentence in hand is the cheapest possible payout of the whole
strand. **THE SECOND HALF IS NOT DONE: closures reopen from scratch, and the
`self` half of the story waits for 1.12.**
**AND NOTE WHAT HE ASKED FOR AT THE S18 CLOSE, because it is this strand
arriving under its own steam:** he asked when the course would teach him to
READ LARGE CODEBASES, and separately asked about `*args`/`**kwargs` because he
sees them in the code he reads at work. **The strand's original promise —
apply each concept to a real fragment of his own work the same week — is
overdue for actual delivery. From S19, the per-subsection coding assignment is
the delivery mechanism. Use HIS repositories, not toy problems, exactly as
this section has said since Session 11.**

### LAYER 6 — C++ STRAND (daily 30–45 min, Oct 2026 – Mar 2027, ~80h)
Spine: existing Mitropoulos Udemy course. Our drilling on top. THIRD
de-scope candidate — reading-level survives any push.

#### 6.1 Core Language
- [ ] Compilation model: preprocessor, compiler, linker (vs Python's model
 from 1.1 — direct contrast)
- [ ] Types, value semantics vs Python's reference semantics — drilled hard
 (his documented C++-model-leak error from Session 2, now made an asset.
 **Session 10 note: the BINDING-vs-MUTATION distinction he drilled in Python
 1.4 is the exact conceptual hinge this section turns on. Session 12 note:
 the += mutate-vs-rebind repair reinforces the same hinge. S16 note: BOTH of
 those items are now [x] PROMOTED on later-day cold evidence, so the contrast
 can be built on them rather than re-taught first.**)
- [ ] Pointers vs references; const correctness
- [ ] Stack vs heap; RAII — the big idea of the language
- [ ] Classes, constructors/destructors, rule of 3/5/0 awareness

#### 6.2 Modern C++
- [ ] Smart pointers (unique_ptr, shared_ptr) — no raw owning pointers
- [ ] Move semantics: intuition level
- [ ] STL: vector, map, unordered_map, string, algorithms, iterators
 **(NOTE, S15: C++ iterators are the SAME IDEA as the Python iteration
 protocol taught in Session 15, with different ergonomics — a position that
 moves forward and knows when it has run out. Teach them as a comparison: he
 will already own the concept and only needs the syntax mapped.)**
 **(CAUTION, ESCALATED S18: the FORWARD-ONLY causation has now failed cold on
 THREE separate days — S15, S16 and S18 — and is the most durable defect in
 the file. It is NOT transferable for free and the promoted `StopIteration`
 label does not mean the causation is owned. Re-establish it with the
 broken-program demo before mapping any C++ syntax onto it.)**
 **(S17 ADDITION — MUTATING vs NON-MUTATING, THE C++ EDITION. `std::sort(v)`
 mutates while `std::ranges::sort` on a copy does not; `v.push_back` mutates
 while `v + something` is not even an operation; iterator-invalidating
 operations are exactly "this call changed the object underneath you". He now
 owns the Python discriminator — check the type, then check what comes back —
 and C++ makes the same distinction with different signals (const-ness,
 return type, reference vs value). TEACH IT AS THE SAME QUESTION IN NEW
 NOTATION. Do not hand him a table of which STL calls invalidate iterators;
 he demonstrably refuses rosters and does better with a rule.)**
 **(S18 REFINEMENT ON THAT: use his own narrowed version. The tell is not
 "returns nothing" but "is this operation in-place?" — which is exactly how
 C++ signals it too, through const-ness and reference returns. His correction
 in Python transfers to C++ more cleanly than the original rule did.)**
- [ ] Lambdas; templates at usage level
 **(S18 NOTE: teach C++ lambda CAPTURE against Python closures. He will have
 met the concept in 1.7 — a function object that carries values from its
 enclosing scope — and C++ makes the capture explicit in the brackets, which
 is arguably the clearer teaching order. If closures land properly in 1.7,
 this becomes a five-minute mapping instead of a new concept.)**

#### 6.3 Build Systems
- [ ] Headers vs sources; include guards; linking errors decoded
- [ ] CMake basics (enough to build and modify a ROS 2 C++ package)

#### 6.4 Applied C++
- [ ] Read a ROS 2 C++ node line by line (rclcpp)
- [ ] Port one of his own Python nodes to C++
- [ ] Guided reading of a real codebase section: ros2_control or MoveIt
 **(S18 NOTE: HE ASKED FOR THIS BY NAME at the S18 close — how does one learn
 to read big codebases. This line and Layer 7.3 are the answer, and he should
 be told that they exist rather than left to wonder. Consider bringing a
 lightweight version forward: reading a short section of LeRobot or his own
 ROS node is possible as soon as 1.7 and 1.12 close, and it would answer a
 question he is asking now rather than in October.)**

#### 6.5 Interview-Level C++ (pushed first within this layer)
- [ ] 30–50 easy/medium DSA problems re-solved in C++ (Feb–Mar)

### LAYER 7 — PORTFOLIO & PUBLIC PROOF (strand, Oct 2026 – Mar 2027, ~60h)
For portfolio-gated roles, a public reproducible real-robot demo + merged
open-source PRs substitute for publications. His best work is locked inside
UKAEA. This strand fixes that. NEVER CUT.

- [ ] 7.1 Public reproducible IL/VLA demo: open hardware (SO-ARM class) or
 high-fidelity sim; README a stranger can follow to a policy rollout.
 HARDWARE SPEC (agreed 27 Jul 2026): SO-101 leader + follower pair,
 self-assembled, budget £350–450 all-in. **ORDER EARLY SEPTEMBER 2026** —
 arrives for the October strand start. Training on owned 4x RTX 4090;
 edge-deployment story on Jetson AGX Thor. NO drone, NO lidar robot.
 **STATUS 10 AUG 2026: three weeks out and still not ordered. Flag it
 explicitly at the 31 Aug checkpoint — a late order pushes the entire Layer 7
 strand and therefore the public proof the North Star depends on. This is the
 one item on the whole plan whose lead time is outside his control.**
- [ ] 7.2 Technical blog posts (3 minimum): (a) LeRobot dataset engineering
 lessons; (b) the normalisation-bug post-mortem; (c) the deployment
 pipeline. All sanitised of UKAEA-proprietary detail.
- [ ] 7.3 Open-source: 2–3 merged PRs to LeRobot and/or openpi. Ladder:
 docs fix → small bugfix → feature. First PR submitted by 31 Dec.
 **(S18 NOTE: this is the other half of the answer to "when will I learn to
 read big codebases". A docs-fix PR requires reading enough of LeRobot to
 find something wrong in it, which is codebase reading with a deliverable
 attached. Say so when the question recurs — and it will.)**
- [ ] 7.4 GitHub/LinkedIn presence: portfolio repo pinned; linkedin-posts
 routine feeds consistent visibility
- [ ] 7.5 CV rewrite (market-language: "robot learning", "VLA" explicit) +
 referral pipeline built (Wayve referrals ~3x interview likelihood)
- [ ] 7.6 Global Talent visa (Tech Nation) evidence file assembled in
 parallel — the portfolio doubles as the endorsement evidence

### LAYER 8 — INTERVIEW READINESS (DSA drip from Nov; block Feb–Mar 2027, ~90h)
NEVER CUT. AI tools are banned in real interview rounds — every drill here
is unaided by definition.

**WHAT A CODING INTERVIEW ACTUALLY IS — explained in full, Session 11, at the
student's request after a real interview signalled a coding round ahead. He
confirmed it is not time-pressured, so no crash preparation was started and
the November drip stands. Recorded here because it is the spec this layer is
built against.**
* Format: 45–60 minutes, one interviewer, a shared editor with syntax
 highlighting but no autocomplete and no AI. His round is language-agnostic
 and the interviewer sees the screen.
* Problem type: usually ONE medium problem from a familiar family, not a
 trick puzzle. Typical shapes: find or count something in an array or
 string; two numbers summing to a target; longest substring without a
 repeated character.
* **The 45 minutes, budgeted — where most candidates lose time:** ~5 min
 understanding and asking edge-case questions (empty input? duplicates?);
 ~5–10 min stating a brute-force approach, then the optimisation, and
 getting the interviewer's agreement on the direction; ~15–20 min writing
 the code; ~5 min running his own code on two or three examples.
* **What is actually being assessed:** thinking aloud throughout; behaviour
 when stuck (verbalising calmly beats silence); the ability to state time
 and space complexity; and whether the model is genuinely his own with no
 scaffold available. **A slower, clearly-reasoning candidate outranks a fast
 silent one who lands the answer.**
* **DIRECT LINK TO THE COURSE MECHANICS, and it was drawn for him:** the
 final step — testing your own code before claiming it works — is the same
 operation as the SPOKEN CROSS-CHECK. The AI-banned setting targets exactly
 the collapse-without-scaffold condition this curriculum was built to fix.
 **S16 ADDS A SECOND LINK, and it is a concrete weakness rather than an
 analogy: TRACE-TAIL TRUNCATION. He twice walked a loop one cycle short. In
 the "run your own code on two or three examples" step, that is precisely the
 error that lets a wrong answer be declared correct. S17 UPDATE: with the
 countermeasure applied (state the FINAL cycle explicitly) it did not fire.
 Carry the countermeasure into the mocks verbatim — it is a rehearsable
 habit, not an insight.**
 **S18 ADDS A THIRD, AND IT IS THE MOST DIRECT ONE YET: FROM S19 HE WRITES
 REAL CODE, SOLO-FIRST, IN VS CODE, EVERY SUBSECTION. That is the same
 operation as this layer's exam, running seven months early on easier
 material. Treat the per-subsection assignments as the DSA drip's warm-up
 rather than as homework — and log them, because "wrote code unaided" is the
 only evidence that answers his own stated fear.**
* **PREPARATION METHOD FOR THIS LAYER (confirmed with him): live mock
 interviews.** Claude gives a problem, he solves it thinking aloud, Claude
 interrupts as an interviewer would with edge cases and challenges, then
 gives feedback on where the reasoning was clean and where time was lost.
 He agreed to keep this at its scheduled November start rather than pulling
 it forward — a scope-discipline decision worth noting.

#### 8.1 DSA (Python primary; drip 30 min/day from Nov, intensify Feb)
- [ ] Arrays & strings; hashmaps
- [ ] Two pointers; sliding window
- [ ] Stacks & queues; linked lists
- [ ] Binary search (and on answer spaces)
- [ ] Trees, BST, traversals
- [ ] Graphs: BFS/DFS, basic shortest path
- [ ] Heaps; intervals
- [ ] Recursion & backtracking **(S17 NOTE: he named recursion unprompted as
 something he wants to learn properly. It is introduced in Python 1.7 well
 before this layer — arrive here with it already mechanised, not new.
 S18 UPDATE: it was NOT reached in 1.7's first session — he deferred it three
 times himself to finish scope properly — and it is first on the S19 plan.
 The intent is unchanged; the delivery has slipped one session.)**
- [ ] DP: 1D and classic 2D patterns
- [ ] Target: ~150 problems total; a medium solved in <25 min unaided
- [ ] Big O fluency woven throughout
NOTE (Session 10): the mutable-default trap and aliasing drilled in Python 1.4
are live DSA hazards, not just trivia — accumulating state across calls and
accidentally mutating a shared list are two of the most common silent bugs in
timed problems. Fold both into the first arrays/hashmaps block. **Session 12
adds a third: += on a list mutates in place, so `acc += row` inside a loop
silently aliases and grows a shared list. Session 15 adds a fourth: an
ITERATOR IS CONSUMED — draining a generator or `zip`/`map` object once and
then iterating it again silently yields nothing.** **Session 16 adds a fifth,
behavioural rather than conceptual: `continue` in a `while` loop skips the
state update below it and hangs. He found that one himself.** **Session 17 adds
a sixth and it is the most common of all: `l = l.sort()` and `l = l.reverse()`
silently replace the list with `None`, because mutating methods return `None`.
He now owns the discriminator that prevents it — check the type, then check the
return value — but the roster is still weak, and `reverse` specifically was his
one miss. Drill it here.** **Session 18 sharpens the sixth rather than adding a
seventh: the discriminator is now [x] AND he has narrowed it correctly, so the
version to drill here is "is the operation in-place?" — which also protects
against the `pop` case, where a mutating method DOES return something useful.**
**And see TRACE-TAIL TRUNCATION — off-by-one at the loop boundary is the single
most common way a timed answer is wrongly declared finished.**

#### 8.2 ML Fundamentals Orals (answered aloud, no notes)
- [ ] Bias/variance; over/underfitting; regularisation incl. L1 sparsity
- [ ] Optimisation: SGD/Adam trade-offs, LR schedules
- [ ] Probability: Bayes, MLE, KL divergence, cross-entropy — derivable
- [ ] Transformers: attention explained on a whiteboard
- [ ] Diffusion/flow-matching policies explained to a non-expert
- [ ] Classic breadth: CNNs, batch norm, etc.
NOTE (Session 8): this subsection is the eventual exam for the voice-mode
rules. Everything here is spoken, unaided, under pressure. **Session 10 added
the counter-evidence that matters most: when he could not identify what the
question was actually asking, he cross-checked the wrong thing confidently.
Session 12 adds that the TERM RETENTION SYSTEM directly rehearses this layer.
Session 15 adds the sharpest warning: mechanisms all correct, three LABELS
wrong — in an oral round that reads as a shaky model even when the model is
sound.** **Session 16 sharpens it into something actionable: the failure is NOT
general vocabulary loss — it is specific to NEAR-NEIGHBOUR labels within one
family, which is exactly what an ML oral probes (bias vs variance; likelihood
vs posterior; on-policy vs off-policy). Rehearse as contrast sets.**
**Session 17 adds the delivery format that demonstrably works: a THREE-WAY
DISCRIMINATOR taught in one block (`pass` / `continue` / `break`), not three
definitions given separately. Build the oral rehearsals the same way.**
**SESSION 18 SUPPLIES THE PROOF THAT THE FORMAT SURVIVES TIME, WHICH IS THE
PART THAT ACTUALLY MATTERS FOR AN ORAL ROUND: the three-way exception
discriminator was fired cold, in mixed order, nine days after the repair, and
came back at 8/10 on labels that had failed three times in one session. THE
ORAL-ROUND RISK FROM S15 IS MATERIALLY REDUCED. What remains is the item with
no decodable hook — `__defaults__` — and that is a different problem needing a
different treatment (isolated repetition, not contrast).**

#### 8.3 ML System Design
- [ ] Design a training pipeline (data → cluster → checkpoints → eval)
- [ ] Design an inference serving system (his one-call-ahead pipeline
 generalised: latency budgets, batching, fallbacks)
- [ ] Design a robot data-collection platform (he BUILT one)

#### 8.4 Robotics Fundamentals Orals
- [ ] Kinematics/Jacobian questions cold
- [ ] PID and control questions cold
- [ ] Kalman filter derivation on a whiteboard
- [ ] "How would you debug a policy that fails on hardware?" — his war
 stories, structured into an answer framework

#### 8.5 Behavioural & Project Narration
- [ ] Each UKAEA project narrated cold: problem → constraints → decisions
 → failure modes → impact. No notes. THE FINAL EXAM for the "nothing
 without AI" fear.
- [ ] STAR-format bank for behavioural rounds
- [ ] Mock interviews (minimum 4: one DSA, one ML, one robotics, one design)

#### 8.6 Applications & Negotiation
- [ ] Applications out by 28 Feb: Humanoid, Wayve, Dyson RLL, Ocado ARM,
 DeepMind RE, NVIDIA; nuclear-sector parallel track as safety net
- [ ] Run 3–4 processes in parallel (competing offers → 15–25% better outcomes)
- [ ] Negotiation prep: know the bands and anchor accordingly

---

## PROGRESS TRACKER
- Master curriculum created: 27 Jul 2026 (from live market research, July 2026)
- Current governing file: PYTHON LEARNING JOURNEY (Layer 0 active)
- Current position: Python **Session 20 COMPLETE (Sun 16 Aug 2026). RECURSION
 DELIVERED AFTER FOUR DEFERRALS; 1.7 HAS FOUR ITEMS LEFT.** S20 taught 1.7.9
 recursion in full (base/recursive case, pre-order vs post-order, value-
 returning recursion, the identity-value rule for base cases, `RecursionError`,
 the two termination conditions, printer-vs-calculator), 1.7.10 pure functions
 vs side effects, and **1.7.11 EDGE-CASE ANALYSIS — A NEW SUBSECTION ADDED AT
 THE STUDENT'S REQUEST**, taught as a five-check procedure.
 **ZERO PROMOTIONS, third session running — but for a new reason.** The cell
 causation, asked four times in S19 and never produced, came back CORRECT
 UNAIDED FROM COLD and was blocked only by his own 5/10 on an answer that was
 ~85% right. **That is the first recorded UNDER-rating in the course.** His
 calibration has been the most reliable instrument in this curriculum since
 S15 and it is used as a targeting signal; an undershoot wastes sessions
 re-teaching what he already owns.
 **REMAINING BEFORE 1.7 CLOSES: `global`, `*args`/`**kwargs`, lambdas,
 docstrings.**
- **THE S20 LEDGER DEFECT — logged at master level because it is a method
 failure, not a Python failure.** `traceback` was tested three times and never
 taught. See the VERSION note. **Struck from the record; clock reset; the rest
 of the carry-forward list is to be audited for the same defect before the
 31 Aug gauntlet.**
- Previous position (RETROSPECTIVE — the master was not updated at the time):
 Python **Session 19 COMPLETE (Tue 12 Aug 2026). CLOSURES TAUGHT FROM SCRATCH
 IN TEXT.** Free variables, cells, `__closure__`, per-object cell isolation,
 `nonlocal`, the three-error separation, and `sorted`/`key=` taught from zero.
 **The iterator causation PASSED ON FIRST ATTEMPT after failing on three
 separate prior days — bug-first delivery vindicated.** ZERO promotions
 (6/10, 4/10, 7/10 all below the bar). **Four motivating examples for closures
 were offered and all four correctly rejected by the student, costing roughly
 half the session — a mentor failure, and the honest answer was already
 written in the file and went unused until the fifth attempt.**
- Position before that: Python **Session 18 COMPLETE (Mon 10 Aug 2026, evening).
 THE DEFERRED DIAGNOSTIC BLOCK RAN ON A GENUINE LATER DAY AND SEVEN ITEMS
 WERE PROMOTED. SUBSECTION 1.7 (FUNCTIONS) IS OPEN AND ~TWO-THIRDS TAUGHT.**
 Promoted: `NameError`, `ValueError`, `TypeError` (mixed order, 8/10),
 exceptions-are-signals (7/10), `StopIteration` category (7/10), the
 mutable/immutable discriminator (10/10). Held [~]: `traceback` (3/10),
 iterator causation (3/10, third failure on a third day), `__defaults__`
 (fourth cold miss). **1.3, 1.4, 1.5 and 1.6 closed; 1.7 in progress.**
- **WHAT 1.7 STILL OWES BEFORE IT CAN CLOSE — DOWN TO FOUR ITEMS:** `global`
 (to be taught AGAINST `nonlocal`, which he now owns), `*args`/`**kwargs`
 (asked for by name — tell him so), lambdas, docstrings.
 **CLEARED SINCE v12:** closures and `nonlocal` (S19, from scratch in text),
 recursion (S20), pure functions vs side effects (S20). **Edge-case analysis
 was ADDED to the subsection in S20 and taught in the same session.**
- Previous position: Python **Session 17 COMPLETE (late Sun 9 Aug → Mon 10 Aug
 2026). SUBSECTION 1.6 (CONTROL FLOW) CLOSED** — open since Session 14. Its
 evidence was SAME-DAY, so everything taught was [~] with one documented
 promotion (`if`/`elif`/`else`).
- **CADENCE.** S16 ~0.5; S17 ~0.3 and closes one; S18 ~0.65; **S19 ~0.35**
 (halved by the closure-motivation detour, a mentor failure); **S20 ~0.4**
 (held back by the traceback re-teach and the doubt-gate stoppage, both of
 which were the right calls). Across S10–S20 ≈ 4.95 subsections over 11
 sessions ≈ **0.45/session** — essentially flat over three weeks.
 ⚠ **CARRY THIS INTO THE 31 AUG RE-BASELINE AND DO NOT SOFTEN IT: at
 0.45/session and roughly five sessions a week, the remaining 1.7 tail plus
 1.8–1.13 is ~6.2 subsections, which is about three weeks of perfect
 attendance against the 30 Sep deadline — with the whole of Layers 1+ still
 untouched. The arithmetic is due in fifteen days and it is not going to be
 comfortable.**
- **THE HONEST SCHEDULE POSITION AS OF 10 AUG 2026 (evening):** **seven
 subsections remain (1.7–1.13) against ~7 weeks** to the 30 Sep gate, but 1.7
 is ~two-thirds taught, so the honest figure is ~6.3. Required rate ~1/week.
 **MARGIN: ZERO — unchanged.** What has changed is that both inputs are now
 moving together for the first time: seventeen promotions across S16–S18, and
 ~1.3 subsections of new coverage in the same three sessions. **The binding
 constraint has visibly shifted from RETENTION to COVERAGE. The formal
 re-baseline arithmetic is still due 31 Aug and this line does not replace it.**
- **WEEKEND BLOCK LOG (ladder step 1):** Sat 1 Aug delivered S10+S11. Sun 2 Aug
 NOT used. **Sat 8 Aug DELIVERED — S14 + S15, two sessions in one day.**
 **Sun 9 Aug DELIVERED — S16 + S17, also two sessions in one day (S17 running
 past midnight into Mon 10 Aug). BOTH DAYS OF THE WEEKEND USED, WHICH IS THE
 FIRST FULL WEEKEND OF THE COURSE.** **Mon 10 Aug evening — S18, a weekday
 session on a new day, and the highest-yield retention session of the course.**
 **THE LESSON, now confirmed from all three directions: the Sunday session
 (S16) converted Saturday's teaching into [x] marks; the SECOND Sunday session
 (S17) produced good coverage but ZERO promotable evidence; and the MONDAY
 session (S18) converted S17's deferred blocks into seven promotions. SPREAD
 THE BLOCKS. A new day is worth more than a longer sitting.**
 Log actual hours at the 31 Aug checkpoint.
- Layers closed: none
- Checkpoints passed: none yet — **first real gate 31 Aug 2026 (gauntlet +
 strict-legend audit + re-baseline arithmetic + the file-growth review)**,
 then 30 Sep for Layer 0.
- Strands running: none yet — C++/Portfolio start Oct, DSA starts Nov
- **SO-101 hardware order: EARLY SEPTEMBER 2026 — three weeks out and not yet
 placed. Flag at the 31 Aug checkpoint. It gates the entire Layer 7 strand.**
- Re-test queue: LIVE in the Python file. **S16 fired the S15 terms cold and
 promoted eight. S17 RAN NO TERM-TAX AT ALL (interval gate). S18 RAN THE
 DEFERRED VOLLEY ON A ~21-HOUR GAP AND PROMOTED SEVEN MORE — the exception
 triad, exceptions-as-signals, `StopIteration`'s category and the
 mutable/immutable discriminator. The queue now carries three named
 survivors plus the 1.7 material taught in S18.**
- **THE EXCEPTION FAMILY IS NO LONGER THE WEAKEST CLUSTER IN THE PYTHON FILE.**
 It was the oldest outstanding diagnostic in the course, deferred out of S17
 on interval grounds, and it cleared in S18 on a mixed-order cold test. **Only
 `traceback` survives from that cluster, and the gap is specific: he has the
 OBJECT (the report showing the call stack) but not the TRIGGER (it appears
 when an exception goes UNCAUGHT). Ask for the trigger first.** **The cluster's
 recovery materially de-risks subsection 1.9.**
- **THE WEAK LIST IS NOW THREE ITEMS, AND IT SHOULD BE READ AS A LIST OF THREE
 DIFFERENT PROBLEMS RATHER THAN ONE:** (1) `traceback` — a partial model,
 needs the trigger drilled; (2) ITERATOR CAUSATION — **failed cold on three
 separate days, the most durable defect in the file; the fix is the
 hoisted-iterator BUG, not another explanation**; (3) `__defaults__` — **four
 cold misses and never once produced; a pure label problem with no decodable
 hook. Fire it alone, in text, at the top of every session until it lands.**
- Strict-legend audit outstanding: 11 Python items were downgraded [x] → [~]
 at the Session 6 reconciliation, and every remaining [x] in Python Layer 1
 is unverified. Full audit is the first task of the first monthly gauntlet
 (end of August 2026). **NOTE: Session 16 added NINE new [x] items, Session 17
 one and Session 18 SEVEN — seventeen in three sessions. Every one must
 survive the gauntlet or revert. Flag the S17 `if`/`elif`/`else` promotion
 specifically (he had asked to be re-taught `elif` shortly before answering),
 and re-fire the S18 exception triad, which is clean but has the longest
 failure history in the file.**
- **Feynman backlog: 1.3 and 1.4 remain cleared. Items are DUE on the
 S16-promoted material AND ON THE WHOLE OF 1.6, which closed in S17 and did
 not get its spoken recall in S18. IT IS NOW ONE SESSION OVERDUE — schedule
 into S19 or S20.**

## ASSIGNMENTS LOG (master — Layer 0 assignments logged in Python file)
| Session | Layer | Assignment | Status | Notes |
|---------|-------|------------|--------|-------|
| 19 → | 0 | **Per-subsection REAL coding assignment, written solo in VS Code; mentor gives feedback only, never solutions** | COMMITTED | Agreed S18 at the student's request — he asked when the course would have him writing real code. Starts with a FUNCTIONS assignment in S19. Use fragments of his OWN repos where possible (bridge strand). |
| — | 1+ | (opens when Layer 1 begins) | — | — |

## WHERE WE LEFT OFF (master view)
Curriculum created 27 Jul 2026 following market research into UK/global
robot-learning roles at £80k+. Key structural decisions, all agreed:
1. ABSORB not scrap: the Python course continues untouched as Layer 0.
2. Target is the PORTFOLIO-GATED engineer track (no PhD needed).
3. C++ confirmed in scope but as a daily parallel strand from October.
4. Hour budget is ~900h against ~870h available: zero slack. RE-BASELINE
 ladder pre-agreed. Never-reduced list: Python, PyTorch, DSA, Portfolio,
 ML fundamentals.
5. Retention system formalised (written AND spoken Feynman as of Session 8;
 TERM RETENTION SYSTEM / term-tax added Session 12).
6. Competing interests parked until April 2027 by agreement.

### Session 6 addendum (29 Jul 2026) — first reconciliation
Two files reconciled; strict [x] legend, retention system, layer supersession
mapping, and trimmed 1.13 spec imported into the Python file. Applying the
strict legend cost 8 items ([x] → [~]). Lesson: a rule that lives only in the
non-governing file does not exist.

### Session 7 addendum (29 Jul 2026)
1. De-scope ladder replaced by RE-BASELINE ladder at the student's request.
2. Two binding rules added (re-issue on interruption; code with output).
3. Cadence alert escalated to three consecutive zero-subsection sessions.
4. Three further Python [x] → [~] downgrades. Running total 11.

### Session 8 addendum (31 Jul 2026)
1. THE JOURNEY MOVED TO VOICE. Nine binding rules designed and mirrored.
2. THE SPOKEN CROSS-CHECK is the first mechanism aimed directly at the top
 behavioural watch area rather than a knowledge gap.
3. Notes format upgraded: REFERENCE CHECKLISTS now mandatory.
4. Retention item 4 extended: Feynman now written AND spoken.
5. GOVERNANCE-ONLY SESSION. ZERO subsections. FOURTH CONSECUTIVE. New pattern:
 SYSTEM-BUILDING AS DISGUISED AVOIDANCE.
6. File naming convention adopted; both files v1.

### Session 9 addendum (31 Jul 2026) — master-level changes
1. FIRST SESSION IN FIVE TO WORK IN THE MATERIAL.
2. THE SPOKEN CROSS-CHECK IS PROVEN — UNDER ENFORCEMENT.
3. THE `==`/`is` FAILURE IS NOW UNDERSTOOD AT MECHANISM LEVEL: he was
 inferring identity from value equality, not "forgetting".
4. TWO NEW BINDING RULES: language-precision corrections; reinforced
 proactive mode-switch.
5. Both files saved as v2.

### Session 10 addendum (1 Aug 2026) — master-level changes
**1. TWO SUBSECTIONS CLOSED. THE ZERO-YIELD STREAK IS OVER.** Python 1.3 and
1.4 closed. First multi-subsection session, in a weekend block.
**2. THE 30 SEP EARLY REVIEW — RUN, arithmetic recorded.** Ladder stays ARMED,
recompute 31 Aug.
**3. THE AVOIDANCE COUNTERMEASURE WORKED:** a governance request was parked.
**4. NEW BINDING RULE: SHORT-FORM CROSS-CHECK.**
**5. A LIVE BREACH OF DEFINE BEFORE BUILDING, CAUGHT BY THE STUDENT** ("aliasing").
**6. THE CROSS-CHECK FAILURE MODE CHANGED** from resistance to not knowing what
to compare — the oral-round failure mode.
**7. Both files v3.** Delivered as local downloads for manual upload.

### Session 11 addendum (1 Aug 2026) — master-level changes
**1. THE DEPTH DOCTRINE** — three levels; Level 2 nearly everywhere; Level 3
reserved for the core (Layers 2, 4, 5).
**2. THE NORTH STAR** — design an original VLA/world-model architecture from
scratch; the job is a checkpoint, not the destination.
**3. CONTROL — SCOPE SETTLED** (3.3): Level 2 required incl. reading a response
curve; the control↔policy interface promoted to a differentiator.
**4. THE PYTHON → ROBOTICS BRIDGE STRAND ADDED.**
**5. CODING-INTERVIEW SPEC RECORDED (Layer 8)** with the 45-min budget.
**6. PYTHON CERTIFICATIONS researched, deliberately NOT scheduled.**
**7. THE FEYNMAN BACKLOG CLEARED — a first.**
**8. NEW BINDING RULE: RECALL FIRST, NOTES SECOND.**
**9. Both files v4.**

### Session 12 addendum (3 Aug 2026) — master-level changes
**1. THE TERM RETENTION SYSTEM** — mirrored into this file and binding across
every layer. Three parts: name-decoding first, term-tax at session open, no
naked terms.
**2. THE FILE-RETURN RULE MADE EXPLICIT AND BINDING (HOW TO USE point 4).**
**3. 1.5 OPENED (~60%) AND FIRST LATER-DAY COLD RE-TESTS RUN.**
**4. THE MOST PERSISTENT STRUCTURAL FLAW appeared twice and was corrected.**
**5. SYMBOL-HEAVY MATERIAL IS TEXT MATERIAL** — new extension to two-mode.
**6. FIVE MENTOR PROCESS ERRORS, ALL CAUGHT BY THE STUDENT.**
**7. Python v6, master v5.**

### Session 13 addendum (5 Aug 2026) — master-level changes
**1. 1.5 (OPERATORS) COVERED END-TO-END.**
**2. THE TERM-TAX PASSED ITS FIRST REAL GAP TEST.** 11 of 13 held cold.
**3. MUTATING-METHODS-RETURN-None SLIPPED A THIRD TIME, THEN TAUGHT PROPERLY.**
**4. THE WRONG-DOMAIN FLAW APPEARED AGAIN — on negative `%`.**
**5. CONFIDENCE RATINGS REINSTATED.**
**6. OWED AND CARRIED TO S14:** the id() demo, spoken Feynman 1.3/1.4, the
5 Aug re-test batch.
**7. Python v7, master v6.**

### Session 14 addendum (8 Aug 2026) — master-level changes
**1. THE ENTIRE S11–S13 OWED BACKLOG CLEARED.**
**2. `result = q.append(4)` PASSED COLD ON A LATER DAY (3-day gap).**
**3. 1.6 (CONTROL FLOW) OPENED, TERM-FIRST.**
**4. THE STUDENT SELF-CAUGHT THE WRONG-DOMAIN REFLEX — A FIRST.**
**5. ONE NEW BINDING RULE: SUBSTRATE DEFINE-BEFORE-BUILDING.**
**6. THE STUDENT POLICED THE FILES' OWN TRUTHFULNESS.**
**7. Python v8, master v7.**

### Session 15 addendum (8 Aug 2026) — master-level changes
**1. NEW BINDING RULE ACROSS ALL LAYERS: CONFIDENCE AFTER RECALL, NEVER AFTER
THE ANSWER.** Produced by the student refusing to rate his confidence on
material the mentor had just supplied.
**2. 1.6 SUBSTANTIALLY ADVANCED — THE ITERATION PROTOCOL TAUGHT AT LEVEL 2.**
The load-bearing result: **iterables are reusable, iterators are consumed,
because an iterator holds forward-only state.**
**3. THE SUBSTRATE RULE FROM S14 WAS VALIDATED IMMEDIATELY.**
**4. FOUR MENTOR FAILURES, ALL CAUGHT BY THE STUDENT** — the serious one being
that **THE MENTOR READ THE WRONG MASTER FILE** and wrote a replacement on top
of a stale 31 Jul copy, which would have destroyed v2–v8 had it been uploaded.
He caught it with a screenshot of the folder. ROOT CAUSE: reading by
search-hit rather than by version. FIX: HOW TO USE point 4a. **STANDING
LESSON: a file that is not the current file is worse than no file, because it
looks authoritative while being wrong.**
**5. THE SCHEDULE REVIEW WAS RUN AT THE STUDENT'S REQUEST** — note honestly
that it was delivered while the STALE master was open; redo it properly at the
31 Aug checkpoint. Do not treat the S15 review as the re-baseline.
**6. DIAGNOSTIC REFINEMENT ON THE WRONG-DOMAIN FLAW: it is DIRECTIONAL.** Fix
the SOURCE rule, not the transfer.
**7. WEEKEND BLOCK DELIVERED** (S14 + S15), with the counter-note that stacked
same-day sessions buy coverage, not consolidation.
**8. Python v10, master v9.**

### Session 16 addendum (9 Aug 2026) — master-level changes

**1. THE PROMOTION PASS RAN AND CLEARED — the single most overdue item in
both files.** Nine Python items moved [~] → [x] on real later-day cold
evidence. **Two deserve naming: `==` vs `is`, outstanding since Session 7; and
the negative-`%` case, which this file had repeatedly called one of its two
weakest items. Neither is weak now.** The operator drill was 6-for-6 cold in
text, and he then volunteered `-11 % 5` unprompted with full working, **to
demonstrate he held the mechanism rather than the answer.**

**2. FIVE MENTOR PROCESS FAILURES, THREE CAUGHT BY THE STUDENT IN TWENTY
MINUTES, AND AN UNPROMPTED META-CHALLENGE.** He asked directly how the
teaching quality was going to be fixed. **The finding that generalises: his
objection now fires faster than the mentor's own check does — and he named the
reason it cannot be relied on, which is that he only catches the mentor
because he knew Python beforehand. In Layers 2, 3, 4 and 6 that check is gone.**

**3. A FALSE ENTRY WAS ALMOST WRITTEN INTO THE RETENTION LEDGER.** A
voice-transcription artifact rendered his correct word "iterable" as "travel".
**Recorded at master level because the files ARE the memory, so a wrong entry
does not merely fail to help — it actively misdirects every future session.**
**An artefact that looks authoritative while being wrong is worse than a
missing one. Missing gets noticed; wrong gets believed.**

**4. THE STUDENT SURRENDERED A MARK HE HAD ALREADY BEEN GIVEN.** Eighth
instance of him producing or correcting the course's own machinery, and the
first by giving something up. It produced binding rule 3.

**5. 1.6 NEARLY CLOSED.** Two teaching moments to carry forward: the
`while`+`continue` infinite loop, which **he found unprompted**, and the
hoisted-iterator nested loop. **That second one is forward-only state shown as
a BUG rather than as a DEFINITION, and it is the best available handle on the
one causation he has failed on two separate days. Reuse it in Layer 4
(DataLoader epochs), Layer 6 (C++ iterators) and Layer 8 (drained generators).**

**6. NEW WATCH AREA: TRACE-TAIL TRUNCATION.** Flagged forward to Layer 8 DSA
boundaries and Layer 4 epoch boundaries.

**7. THE EXCEPTION FAMILY EMERGED AS A SINGLE CLUSTERED WEAKNESS.** The
generalisable lesson is about NEAR-NEIGHBOUR VOCABULARY and it is pre-loaded
for Layers 2 and 5: teach contrast sets, not definitions.

**8. THE DRIVE MAP WAS WRITTEN DOWN** and the root cause of a repeated failure
finally identified: the two files live in DIFFERENT folders.

**9. Python v12, master v10.**

### Session 17 addendum (late 9 Aug → 10 Aug 2026) — master-level changes

**1. PYTHON SUBSECTION 1.6 (CONTROL FLOW) IS CLOSED.** Open since Session 14,
carried through four sessions, and finished here. The tail ran in the right
order for once: the owed found-flag exercise first, then loop `else` derived
from it by contrast, then `pass` and the ternary, then loop pitfalls, then the
two owed diagnostic items from S16. **1.3, 1.4, 1.5 and 1.6 are now all
closed; 1.7 (Functions) opens next.**

**2. THE STUDENT REFUSED A TEST BEFORE IT RAN — AND THAT IS THE SESSION'S
DOMINANT FINDING.** S17 was scripted to open with the exception-family recall.
It did, into a session beginning minutes after S16 had finished teaching that
material. **He stopped it before a single question was answered, on the grounds
that nothing could have been forgotten in the interval, so the result would
measure echo rather than retention.** The mentor checked the prior session,
confirmed he was right, and deferred the entire block.
**WHY IT MATTERS AT MASTER LEVEL: a passed same-day recall does not merely fail
to inform, it CORRUPTS — the pass gets written in as later-day evidence and
promotes items that have not been retained.** It produced **THE INTERVAL GATE**
(Session 17 rule 1).
**AND READ THE PROGRESSION AS ONE LINE: S15 he refused a RATING; S16 he handed
back a MARK; S17 he refused the EXPERIMENT.**

**3. THREE MENTOR FAILURES, ALL CAUGHT BY HIM, ALL OF THE SAME NEW SHAPE.**
Where the S16 five were protocol steps SKIPPED under time pressure, these three
were protocol steps EXECUTED after the circumstances had changed. **THE THREE
SESSION 17 RULES are the fix. The unifying lesson: the written plan is a plan,
not an instruction set — check that its preconditions still hold before
executing it.**

**4. THE S16 PREREQUISITE BREACH WAS REPAIRED PROPERLY.** The repair was not to
re-explain but to make him need the construct: he wrote the search with only
`for`, `if`, `break` and a flag, felt the cost, and articulated the
justification himself. **This is the template for repairing any out-of-order
teaching in later layers: do not re-teach, engineer the need.**

**5. THE `if`/`elif`/`else` CONFIRMATION WAS ANSWERED COLD AND PROMOTED** — the
last item owed from S16. **Flagged for the 31 Aug audit because of the
re-teach immediately prior.**

**6. THE MUTATING-METHODS DEBT FROM S16 WAS DISCHARGED, AND IT PRODUCED THE
SESSION'S MOST TRANSFERABLE TEACHING.** The identification drill ran at 4/5,
and when he refused the roster he was given a DISCRIMINATOR instead: check the
TYPE first, then use the RETURN VALUE as the tell. **He reliably refuses lookup
tables and does better with rules — teach to that everywhere.**

**7. HIS CALIBRATION IS NOW PREDICTIVE, NOT MERELY HONEST.**

**8. THE JUMP-SHIP PATTERN FIRED ON EASY MATERIAL, WHICH IS A NEW SHAPE.**
What worked was pricing rather than refusal.

**9. THE WEEKEND-BLOCK LESSON IS NOW CONFIRMED FROM BOTH DIRECTIONS.**
**SPREAD WEEKEND BLOCKS ACROSS DAYS; where a same-day second session runs,
spend it on NEW MATERIAL ONLY and schedule no re-tests into it.**

**10. Python v13, master v11.** Returned as downloads for manual upload, per
the standing file-return rule — **delivered across two messages, with the split
announced when it was made (HOW TO USE point 4c).**

### Session 20 addendum (Sun 16 Aug 2026) — master-level changes

**1. A DEFECT WAS FOUND IN THE MEASUREMENT SYSTEM ITSELF, AND IT IS THE MOST
IMPORTANT THING THIS CURRICULUM HAS LEARNED IN A FORTNIGHT.** `traceback` was
fired as a [RECALL] in S16, S18 and S19, and logged three times as a student
retention failure. In S20 the student rated it 0/10 and said precisely what he
did and did not have — he could read the line-number half and had no idea what
`<stdin>` meant. **The item had never been taught. It had only ever been asked.
Repeating a question is not teaching.** The three prior results were measuring a
hole in the delivery, not a hole in his memory. They are STRUCK, the item was
taught in full, and the clock is reset.
**THE RULE THIS PRODUCES BELONGS AT MASTER LEVEL BECAUSE IT APPLIES TO EVERY
LAYER OF THIS CURRICULUM, NOT JUST PYTHON: A REPEATEDLY-FAILING ITEM IS EVIDENCE
ABOUT THE TEACHING BEFORE IT IS EVIDENCE ABOUT THE STUDENT.** Any item that has
failed three or more times gets audited against one question — was it ever
actually delivered, or only ever asked? **Do this to the whole carry-forward
list before the 31 Aug gauntlet.** The strict [x] legend protects against
promoting on weak evidence; it does nothing to protect against *demoting* on
invalid evidence, and this file has now done that three times to one item.

**2. THREE NEW BINDING RULES, ALL THREE THE STUDENT'S, AND THEY ARE A NEW
CATEGORY.** S16's five were about measurement integrity, S17's three about
evidence validity, S18's two about instrument declaration, S19's one about
formatting. **S20's three are about BANDWIDTH — how much a single teaching turn
can carry before the student stops being able to use it.** (i) **THE DOUBT
GATE**: ask for doubts and WAIT before opening any new subsection, and restate
the just-taught material in full if any come. (ii) **THE RESPONSE LENGTH CAP**:
one teaching idea per turn, instructions near the top. (iii)
**DEPTH-BEFORE-ANSWER**: a correct output never discharges a request for a
mechanism, and he runs the five checks on his own code before submitting it.

**3. THE DISCLOSURE BEHIND RULE (ii) CHANGES HOW PAST SESSIONS SHOULD BE READ.**
*"I tend to not read the full chat if its too long and that's the reason I don't
do things you asked for."* **The four missing S19 confidence ratings, the
skipped `digit_sum` trace and the unanswered S19 cell-causation re-fire were not
compliance failures — they were asks buried in messages he never finished.**
This is a mentor problem with a mechanical fix. **It also means the file has
been logging length as a student attention deficit when it is a delivery
defect.** Mirrored into the Python file.

**4. EDGE-CASE ANALYSIS ADDED TO THE CURRICULUM AS SUBSECTION 1.7.11, AT HIS
REQUEST, AND HE WAS RIGHT THAT IT WAS MISSING.** *"I am unable to think about
the failure cases and dissect the problem the way you do... I have never done
this, and don't know how to find the edge cases."* **This curriculum had
"needs to develop habit of thinking about edge cases and failures" as a one-line
watch item from day one and nothing that actually taught it.** It is now a
five-check procedure — boundary of every condition, empty/zero, one, the
assumed type or sign, and whether the step lands on the base case — and it
transferred on first use in the same session. **It does not wait for Layer 6
testing. It applies to every drill from here.**

**5. HIS OWN DIAGNOSIS IS SHARPER THAN THE FILE'S AND IT SHOULD REPLACE THE
FILE'S FRAMING.** *"I just did the things at surface level and always do that
and that's why i was not able to catch the edge case."* **The behavioural
watch list has recorded right-answer-without-mechanism for months as a symptom.
This is the habit underneath it, named by him: the first plausible answer is
taken as the finished answer and the probing pass never runs.** The
countermeasure is now mechanical rather than exhortative.

**6. THE TRANSFER FAILURE IS THE ONE TO WATCH NEXT.** He predicted `2 1 0` for a
post-order recursion, having imagined a single mutating `n` instead of four
frames each holding their own — **twenty minutes after correctly and unaidedly
explaining the identical isolation principle for closure cells.** Same idea,
different container, not recognised. **This is the sharpest instance yet of a
pattern this curriculum has been circling: concepts are owned locally and do not
travel. Given that the North Star is designing a novel VLA architecture, the
ability to carry a principle across contexts is not a nicety — it is the whole
skill. Test transfer explicitly from here, not just recall.**

**7. THE MASTER WAS NOT UPDATED AT THE S19 CLOSE.** v12 was re-uploaded
unchanged. The END-OF-SESSION PROCEDURE exists to prevent exactly this and was
not followed. **The Drive-map check has been amended: at every session close,
confirm the highest v<N> corresponds to the PREVIOUS session number.**

### Session 19 addendum (Tue 12 Aug 2026) — master-level changes
### ⚠ WRITTEN RETROSPECTIVELY AT THE SESSION 20 CLOSE (see above)

**1. CLOSURES TAUGHT FROM SCRATCH IN TEXT, AND HE BUILT THE MECHANISM HIMSELF.**
Free variables, cells, `__closure__`, per-object cell isolation, `nonlocal`, the
three-error separation (`TypeError`/`NameError`/`UnboundLocalError`), and
`sorted`/`key=` taught from zero. Given the contradiction — the enclosing frame
is dead but the value is still reachable — he worked to the answer across three
guesses, **and both wrong guesses were productive.**

**2. THE MOST STUBBORN ITEM IN THE COURSE CAME GOOD, AND THE DELIVERY METHOD IS
WHY.** The iterator causation had failed on three separate days, every time by
reaching for "one item at a time". Delivered BUG-FIRST in S19 — a hoisted
iterator above a nested loop — **he diagnosed it unaided on first attempt.**
**Definition-first failed three times; bug-first has now worked twice. How a
repair is delivered decides whether it holds.** That is a master-level teaching
finding and it generalises well beyond Python.

**3. FOUR MOTIVATING EXAMPLES REJECTED, ALL FOUR CORRECTLY, COSTING HALF THE
SESSION.** Each could be done with two parameters, a hardcoded value, or a loop
and a dict. **The honest motivation — a callback that will only ever be handed
ONE argument — was already written in the Python file from S18 and went unused
until the fifth attempt.** A mentor failure, not a comprehension failure.
Recursion was deferred a fourth time as a direct consequence.

**4. ZERO PROMOTIONS AND THAT WAS CORRECT.** `traceback` 6/10, iterator
causation 4/10, `__defaults__` 7/10 — all improved, all below the bar. **A
correct answer that does not promote because the student does not trust it is
the strict legend working as designed.**

### Session 18 addendum (Mon 10 Aug 2026, evening) — master-level changes

**1. THE OLDEST OUTSTANDING DIAGNOSTIC IN THE COURSE RAN AND CLEARED, AND THE
INTERVAL GATE IS WHAT MADE IT WORTH ANYTHING.** The exception-family block —
deferred out of S17 by the student on interval grounds — opened S18 after the
elapsed time was stated aloud and the gate was checked and PASSED (~21 hours
since S17; the material itself last taught in S16, the day before). **SEVEN
ITEMS PROMOTED [~] → [x] on genuine later-day cold evidence, every one with
his own confidence rating taken before the verdict:** the
`NameError`/`ValueError`/`TypeError` triad fired in MIXED ORDER at 8/10 —
**the same triad he conflated three separate times in a single session nine
days earlier** — plus exceptions-are-signals (7/10), `StopIteration`'s category
(7/10), and the mutable/immutable discriminator (10/10).
**WHY THIS IS THE MOST IMPORTANT ENTRY IN THIS FILE SINCE THE S16 PROMOTION
PASS: it closes the argument the S17 rules opened. S17 showed what the interval
gate PREVENTS — a corrupted ledger. S18 showed what it BUYS. Same blocks, one
day later, seven promotions. Deferring a test is not lost time; it is the only
condition under which the test produces anything.**

**2. THREE ITEMS HELD AT [~], AND THEY ARE THREE DIFFERENT PROBLEMS.**
`traceback` at 3/10 — he has the OBJECT but missed the TRIGGER (it appears when
an exception goes UNCAUGHT), so ask for the trigger first next time. **ITERATOR
CAUSATION at 3/10 — A THIRD FAILURE ON A THIRD SEPARATE DAY, which makes it the
most durable defect in the file.** The fix has been identified twice and still
not applied: **stop explaining it and show the hoisted-iterator BUG.**
`__defaults__` — **a FOURTH cold miss; it is the only item in the file that has
never once been produced.** A pure label problem with no decodable hook: fire
it alone, in text, at the top of every session until it lands.

**3. 1.7 (FUNCTIONS) OPENED AND IS ~TWO-THIRDS TAUGHT.** def-vs-call,
parameters-vs-arguments, `return` and implicit `None`, LEGB (with E established
as LEXICAL and Global as the MODULE namespace), default arguments, functions as
FIRST-CLASS OBJECTS, and nested functions by definition. **The first-class-
objects piece is the callback unlock the bridge strand has been waiting for
since Session 11 — say so in S19 while it is fresh.**

**4. THE STUDENT REFUSED A TAG, WHICH IS THE NEXT STEP IN A PROGRESSION THIS
FILE HAS BEEN TRACKING FOR FOUR SESSIONS.** Closures were described; he judged
the treatment too thin to count and instructed that the item carry no status at
all. **It is recorded with NO tag — not even [~] — and reopens from scratch in
TEXT with runnable code.** Read the line: **S15 he refused a RATING; S16 he
handed back a MARK; S17 he refused the EXPERIMENT; S18 he refused the RECORD
ITSELF, and separately CORRECTED A RULE THE FILE HAD TAUGHT HIM.**

**5. HE NARROWED A RULE THE MENTOR HAD TAUGHT AND THE FILE HAD RECORDED — the
single strongest instance of student-side ownership on record.** The S17
discriminator said a method returning `None` has mutated. He pointed out this
holds only for IN-PLACE MUTATORS, since `pop`, `index` and `count` are methods
on a mutable object that return real values, and `pop` mutates while returning.
**He was right; the rule was too broad; the file now carries his version.** The
10/10 promotion was earned BY the correction. **This transfers directly to
PyTorch (4.1), where `t.add_(1)` returns the tensor rather than `None` and the
original phrasing would have actively misled him.**

**6. FOUR MENTOR FAILURES, ALL CAUGHT BY HIM, PRODUCING THE TWO SESSION 18
RULES.** (a) The mentor proposed ending the session three separate times while
he was still working → **SESSION LENGTH IS THE STUDENT'S CALL.** (b) A
comprehension check on just-taught LEGB had no honest instrument tag →
**[TEACH-BACK]**, carrying no rating and never ledger-eligible. (c) The
over-broad discriminator above. (d) Closures taught too thinly.
**RUNNING COUNT: EIGHTEEN correct process pushbacks by the student, ZERO
wrong.** **THE SHAPE OF THREE OF THE FOUR IS THE SAME AND IT IS WORTH NAMING:
the mentor being too quick to conclude — too quick to end, too quick to
generalise, too quick to count something as taught. That is the failure mode to
watch for in Layers 2 and 4.**

**7. HE ASKED FOR MORE REAL CODING AND FOR CODEBASE READING, AND A FORMAT
CHANGE WAS COMMITTED IN RESPONSE.** At the close he asked, unprompted, whether
the course would ever have him writing real code and learning to read large
codebases. **From Session 19, every subsection carries a real solo-first coding
assignment written in VS Code, mentor feedback only — logged in the ASSIGNMENTS
LOG.** Codebase reading already lives in 6.4 and 7.3; a lightweight version can
be brought forward once 1.7 and 1.12 close. **He also asked about
`*args`/`**kwargs` by name, having met them in code he reads at work — they sit
in the tail of 1.7 and he has been told so.**

**8. HE RAISED THE FILE-GROWTH PROBLEM HIMSELF, AND HE IS RIGHT.** He asked
whether these files will eventually consume the entire context window. **The
honest answer is yes on the current trajectory. The structural answer is that
most of the bulk is HISTORY, not live state.** Added as job (d) at the 31 Aug
checkpoint: after the strict-legend audit, split closed-and-audited narrative
into an archive file and keep the governing file to binding rules, live queues,
watch areas and the resume plan. **Not before the audit — an archive built on
unverified [x] marks would bury exactly the items that need re-testing.**

**9. THE WEEKEND-BLOCK LESSON PAID OUT ON A WEEKDAY, WHICH COMPLETES IT.**
Sat 8 Aug: two sessions, coverage only. Sun 9 Aug: S16 converted that into nine
[x] marks; S17 the same evening produced none. Mon 10 Aug: S18, a new day,
produced seven. **THE RULE IN ITS FINAL FORM: A SESSION ON A NEW DAY IS WORTH
MORE THAN A LONGER SESSION ON THE SAME DAY. Plan the calendar around intervals,
not hours.** Carry this into Layer 2's fixed six-week window.

**10. Python v14, master v12.** Returned as downloads for manual upload.
**Delivered across messages per point 4c, with the split announced — and note
for the record that a context compaction landed between the two halves, which
is why 4c now carries the S18 corollary: state the outstanding half explicitly
so the debt survives a reset.**

NEXT ACTION: **Python Session 19. CHECK THE DATE FIRST — the interval gate runs
before the prerequisite gate, and it runs in BOTH directions: state the elapsed
time, then say whether it passes.**
**OPEN WITH A SHORT [RECALL] ON THE THREE ITEMS THAT DID NOT PROMOTE, and treat
each as its own problem:** `traceback` — **ask for the TRIGGER first**, not the
description; **ITERATOR CAUSATION — show the hoisted-iterator BUG and make him
diagnose it, do not define it again** (three cold failures on three days say the
explanation route is exhausted); and **`__defaults__` FIRED ALONE, IN TEXT**, not
inside a volley where a miss can be absorbed.
**THEN CLOSURES, FROM SCRATCH, IN TEXT WITH RUNNABLE CODE** — he refused the S18
treatment and the item carries no status. Build `make_multiplier`, show
`__closure__` so the captured value is visible rather than asserted, and **cash
in HIS OWN argument: he proposed `multiply(n, x)` as the substitute and was
right that it covers most cases, so lead with the case where it fails — a
one-argument callable that must still remember something (`map`, `sort(key=)`,
callback registration).** Then `nonlocal`.
**THEN RECURSION** — deferred three times by him, still the thing he most wants,
and it has now been promised twice. Do not let it slip again.
**THEN THE 1.7 TAIL:** `global`/`nonlocal`, `*args`/`**kwargs` (asked for by
name), lambdas, docstrings, pure functions. **1.7 CANNOT BE MARKED [x] UNTIL
ALL OF IT IS TAUGHT.**
**AND THE NEW STANDING ITEM: THE FIRST REAL CODING ASSIGNMENT.** Functions,
written solo in VS Code, mentor feedback only. He asked for this; deliver it in
S19, not later.
**ALSO DUE: the spoken Feynman recall for the whole of 1.6 — NOW THREE SESSIONS
OVERDUE.** Scheduled and dropped in S18, S19 and S20. **Either run it in S21 or
move it formally into the gauntlet and stop carrying it as a live item; a
standing commitment that is never honoured is worse than one that is retired.**
**31 AUG: first monthly gauntlet + strict-legend audit (now SEVENTEEN items
larger than when it was scheduled) + the re-baseline arithmetic + the
file-growth review. Flag the SO-101 order — early September is days away and it
gates Layer 7.**

## NOTES FOR CLAUDE (every session under this file)
- Enforce the governance rule: Python file runs sessions until Layer 0 closes.
 Do not start Layer 1+ material early.
- **CHECK THE INTERVAL BEFORE RUNNING ANY [RECALL] BLOCK OR THE TERM-TAX.
 State when the material was last taught and how long ago. Under a few hours
 → the block does not run. A passed same-day recall corrupts the ledger; it
 does not merely waste time (Session 17 rule 1). AND RUN THE GATE IN BOTH
 DIRECTIONS — in Session 18 it AUTHORISED the block and seven promotions
 followed. A gate that only ever says no gets ignored.**
- **READ THE LATEST VERSION OF BOTH FILES, NOT THE FIRST SEARCH HIT. A stale
 unversioned `robotics_career_curriculum.md` from 31 Jul 2026 still sits in
 the Robotics_curriculum_record folder and ranks in search. List the folder,
 take the highest v<N>, and confirm the VERSION line inside before trusting
 anything. (HOW TO USE point 4a.)**
- **THE TWO FILES LIVE IN DIFFERENT FOLDERS WITH INDEPENDENT VERSION NUMBERS.
 LIST BY parentId — see THE DRIVE MAP. Neither file should ever record the
 other's version number. (HOW TO USE point 4b.)**
- **RETURN THE UPDATED FILES AND THE session_<N>.pdf NOTES TO THE STUDENT AS
 DOWNLOADS FOR HIM TO UPLOAD MANUALLY. Do NOT attempt the Drive upload
 yourself. EVERY delivered artefact follows the naming convention. Sequenced
 delivery across messages is permitted if announced (point 4c) — and STATE
 THE OUTSTANDING HALF EXPLICITLY, so the debt survives a context reset (S18).**
- **UPDATE THE MASTER AT SESSION END WITHOUT BEING ASKED. The student had to
 request it in Sessions 15 and 16. That request is itself a defect.**
- **DO NOT PROPOSE ENDING A SESSION. Session length is the student's call
 (Session 18 rule 2). Report state — what is left, what the next block costs —
 and ask. The only legitimate exception is instrument validity: if fatigue
 would make the next block's evidence worthless, say THAT and let him decide.**
- **RESOLVE AMBIGUOUS ONE-WORD REPLIES ("continue", "ok", "chalo") AGAINST WHAT
 HE MOST RECENTLY ASKED FOR, NOT WHAT YOU MOST RECENTLY OFFERED. When in
 doubt, ask one clarifying line (Session 17 rule 2). Read this together with
 the rule above: do not infer in EITHER direction.**
- **NEVER LOG A WHITESPACE OR TRANSCRIPTION ERROR AS A COMPREHENSION FAILURE.
 Before recording any failure, ask whether the CHANNEL could have produced it
 (Session 16 rule 5 + Session 17 rule 3). In S18 voice rendered "arguments"
 as "arts", "kwargs" as "quags" and "code" as "cope" — assume garble,
 reconstruct from context, ask only when genuinely ambiguous.**
- **TAG EVERY QUESTION BLOCK [RECALL] / [PREDICT] / [DRILL] / [TEACH-BACK]
 BEFORE ASKING, and STATE THE PREREQUISITE AND ITS STATUS before opening any
 new unit (Session 16 rules 1 and 2; Session 18 rule 1). A PREDICT miss is NOT
 a retention failure, and a TEACH-BACK carries NO rating and NEVER touches the
 ledger. If a gate must be opened on credit, SAY SO OUT LOUD and settle the
 debt in the same session.**
- **DO NOT PROMOTE AN ITEM TO [x] WITHOUT HIS OWN CONFIDENCE RATING, taken
 after his answer and before your verdict (Session 16 rule 3). AND USE HIS LOW
 RATINGS TO TARGET RE-TESTS — his calibration is predictive (S17, confirmed
 S18: the two 3/10 items were the two that failed).**
- **IF HE JUDGES SOMETHING NOT PROPERLY TAUGHT, IT CARRIES NO TAG. He refused
 to have closures recorded in S18 and he was right. A [~] awarded over his
 objection is a false entry, and false entries are worse than gaps.**
- **SPEED IS NEVER A REASON TO SKIP A GATE. A backlog is not licence. And note
 the S17 corollary: schedule pressure degrades MEASUREMENT before it degrades
 teaching, and degraded measurement removes the instrument that would have
 detected the problem. The answer is the RE-BASELINE LADDER, not faster
 teaching and not faster testing.**
- **Apply the DEPTH DOCTRINE when scope is questioned: Level 2 everywhere
 except the core (Layers 2, 4, 5), which is Level 3. Name the level, name
 what is being left out, and say where it will be picked up.**
- **PREFER A DISCRIMINATOR TO A ROSTER. He refuses lookup tables and reasons
 well from rules. Before handing him a list to memorise, ask whether a
 two-step test exists (S17). AND STATE THE RULE AT ITS HONEST SCOPE — he
 narrowed the mutator rule himself in S18 and was right to.**
- **WHEN HE ASKS "WHY DOES THIS EXIST", HE WANTS THE CASE WHERE THE ALTERNATIVE
 FAILS, not the mechanism restated (S18, closures — he asked three times).
 Have that case ready before teaching any construct, or defer the construct.**
- **RECALL FIRST, NOTES SECOND on every cold re-test.**
- **ANNOUNCE every mode switch; symbol-heavy material is TEXT by default — the
 trigger is the material, not his complaint, and the check happens BEFORE the
 question is posed. LABELS are voice material; SYMBOLS and CODE are text.**
- Foundation before prediction is binding across ALL layers. Teach first.
- **Define before building is binding across ALL layers, and it has been
 breached in Sessions 10, 12, 14 and twice in 15. List and define new terms
 before a subsection opens, and check the SUBSTRATE of every example too.
 Session 16 added the SEQUENCE dimension — the prerequisite gate. Session 18
 added the DEPTH dimension: every word being defined does not mean the
 construct has been taught.**
- **Teach NEAR-NEIGHBOUR vocabulary as CONTRAST SETS, never one definition at
 a time (S16 finding; S17 supplies the working format — a three-way
 discriminator taught in one block; S18 supplies the proof that it survives a
 nine-day gap and a mixed-order cold test).**
- **For causation items he keeps dropping, show the BROKEN PROGRAM, not the
 rule (S16 finding — forward-only state). THIS IS NOW OVERDUE: the same
 causation has failed cold on three separate days while the fix has been
 written in this file twice and never actually delivered.**
- Audit reasoning behind correct answers everywhere. **When the wrong-domain
 flaw appears, remember it is directional — fix the source rule, which was
 never mechanised, rather than drilling the transfer.**
- **On every trace, require the FINAL cycle to be stated explicitly before
 accepting the answer (trace-tail truncation, S16 — countermeasure confirmed
 working in S17 and S18).**
- **For idiom-level habits, stop re-explaining and require the corrected line
 to be typed back once (S17).**
- **GIVE HIM CODE TO WRITE. From S19 every subsection carries a real
 solo-first assignment in VS Code, feedback only. If three consecutive
 sessions pass with no code written by him, that is a defect — flag it.**
- The monthly gauntlet is sacred. Skipping it is the jump-ship pattern in
 disguise. First gauntlet: end of August 2026.
- If the student proposes restructuring this curriculum mid-layer, name the
 pattern, require the current layer's exit criteria first, then discuss.
 **Sessions 10, 11, 12, 15, 16, 17 and 18 demonstrate the parking mechanism
 working — repeat it verbatim. And note the S17 refinement: with a
 reach-ahead request, PRICE the shortcut rather than refusing the
 destination. S18 note: the pattern did not fire at all — he deferred
 recursion himself, three times, to finish the current material properly.**
- Two-mode operation is binding. NAME the switch PROACTIVELY. Restate on return.
- The spoken cross-check is SHORT FORM: rule, answer, do they agree. Pose the
 question BEFORE asking for the cross-check.
- Correct loose phrasing in the moment (language-precision rule, Session 9).
- Two questions maximum per turn. One is better.
- Every session closes with a ~30-second spoken summary from memory.
- Session PDFs: Thinking Gaps section, Teaching Mistakes section, and a
 Reference Checklist for any closed topic. All mandatory.
- The student is entitled to enforce every agreement in this file on the
 mentor — **and on the evidence of Sessions 10 through 18 he is better at it
 than the mentor is. EIGHTEEN correct process pushbacks, ZERO wrong. When he
 says a rule has been broken, check the rule against the actual artefacts
 before answering; do not reason from memory, and do not invent a history to
 explain the symptom.**
