# COLD BUILD BLOCK 01 — Sunday 23 Aug 2026

FIRST BUILD BLOCK TO ACTUALLY RUN. Carried three dates (S26, S27, S28).
This is NOT a curriculum item. It is a MEASUREMENT INSTRUMENT — it measures
what you can build with the scaffold removed.

## THE TASK (your own choice, S26)

Extend the joint-limit clamp to MULTIPLE JOINTS, using `*args` and `**kwargs`.

That is the whole brief. The design is yours. So are the tests.

## CONDITIONS — all four are binding, and the block is void if any breaks

1. **90 MINUTES, TIMED.** Set a real timer.
2. **NO AI.** Close Claude Code. Disable Copilot / any autocomplete that
   suggests whole lines. No googling for a solution to the design; language
   reference (docs.python.org) is allowed, a worked answer is not.
3. **GIT.** `git commit` at START and at END. The commit timestamps ARE the
   clock — that is the objective record, not your memory of it.
4. **PYTEST.** You write the tests. "Does it work" is decided by pytest,
   not by opinion.

## WHAT COUNTS AS DONE

You decide. But the honest bar: a module that clamps angles for several
joints at once, with limits supplied per joint, and a test file that passes.

## WHILE YOU WORK — write it down, don't remember it

Keep a `LOG.md` in this folder. I cannot see you work, so what you write is
the only evidence of the process. Two things only:

- **Where you STALLED.** The exact moment you did not know what to do next,
  and for roughly how long. This is the most valuable line in the whole block.
- **Anything you reached for and could not produce cold.** Syntax, a name,
  a method — whatever you had to look up.

Do not clean this up. A tidy log is a useless log.

## BEFORE YOU CALL IT DONE

Run THE FIVE CHECKS on your own code. Yours, not mine:
"Boundary pe khaali ek bahar mila."

BOUNDARY FIRST — a clamp is made of boundaries. The angle sitting EXACTLY on
the limit is the first test you write, not the last. You have shipped three
boundary bugs (S20 `n <= 10`, the planted `len(word) == 1`, S28 `len(n) > 5`).
This task is built entirely out of the thing you keep getting wrong.

## AFTER

Come back, say done, and Session 29 opens on the result. I hold two things
back until then, deliberately, and I am not going to slip.

---

# THE EXERCISE (added 23 Aug, at his request)

Build a module that clamps robot joint angles to their safe limits.

**One name is fixed so we can talk about it: `clamp_joints`.**
**Everything else — the parameter list above all — is yours to design.
The signature IS the deliverable.**

Work the levels in order. Getting to L3 with clean tests beats reaching L5
with a broken L2. Stop where you stop; where you stop is the measurement.

## L1 — one joint

Given an angle and a low/high limit pair, produce the safe angle.

- inside the limits  -> unchanged
- below the low limit -> becomes the low limit
- above the high limit -> becomes the high limit
- **EXACTLY ON a limit -> unchanged, and it is NOT clamped.**
  This is spec, not a detail. Both ends. Test it first.

## L2 — many joints, one shared limit pair

One call must accept ANY NUMBER of angles positionally:

    clamp_joints(10, -200, 95, ...)

and give back all of them, clamped, in the same order. Two angles, five
angles, one angle, zero angles — same call shape, no list built by the caller.

## L3 — per-joint limits, supplied BY NAME

Different joints have different limits. The caller must be able to say, in
the same call, which limits belong to which joint — by name, not by position.

The result must make clear WHICH JOINT ended up with WHICH VALUE. A bare
sequence of numbers is not enough at this level.

⚠ This is the level the whole block exists for. Expect it to be harder than
it looks. When it fights you, that is the exercise working — log the stall
and keep going.

## L4 — absence

Some joint gets an angle but no limits were supplied for it.

You decide: raise, or shrug and pass the value through. **Whichever you
choose, write ONE line in LOG.md saying why.** There is a right answer and
it depends on whether that situation is a BUG or an EXPECTED CASE — say
which you think it is.

## L5 — stretch, only if time remains

Report how many joints were actually clamped, and print a readable summary
line per joint: name, angle in, angle out, and whether it was clamped.

## TESTS — required, and they are half the mark

`pytest` decides whether it works. Your test file must contain a test for
**each of the five checks**, and each test's NAME must make clear which
check it is. You know the five. Map them onto this task yourself — that
mapping is part of what is being measured.

Beyond those: L1's four cases, L3's per-joint routing, and L4's decision.

## ROUGH TIME SPLIT (guide, not a rule)

L1 + its tests: 20 min. L2: 15 min. L3: 35 min. L4: 10 min. Five checks
and a final pytest run: 10 min.

## THE ONE THING THAT MAKES THIS VOID

Do not ask me anything until the timer stops.
