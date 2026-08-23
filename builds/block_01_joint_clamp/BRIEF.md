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
