# COLD BUILD BLOCK 01 — Sunday 23 Aug 2026

FIRST BUILD BLOCK TO ACTUALLY RUN. Carried three dates (S26, S27, S28).
NOT a curriculum item. A MEASUREMENT INSTRUMENT — it measures what you can
build with the scaffold removed.

## CONDITIONS — binding; the block is void if any breaks

1. **90 MINUTES, TIMED.** Real timer.
2. **NO AI.** Close Claude Code. Disable autocomplete that suggests whole
   lines. docs.python.org is allowed. A worked answer is not.
3. **GIT.** Commit at START and at END. The timestamps are the clock.
4. **PYTEST.** You write the tests.

## LOG.md — write it AS YOU GO

- **Where you STALLED**, and roughly how long.
- **Anything you could not produce cold** and had to look up.

A tidy log is a useless log.

---

# THE PROBLEM — CONCRETE

A 3-joint robot arm. Someone commands angles. Some are unsafe. Your code
returns angles that are safe to send to the hardware.

## THE ARM (fixed, use exactly these)

| joint    | low  | high |
|----------|------|------|
| shoulder | -90  | 90   |
| elbow    | 0    | 145  |
| wrist    | -180 | 180  |

## THE RULE

- angle inside its limits            -> unchanged, NOT clamped
- angle below low                    -> becomes low, clamped
- angle above high                   -> becomes high, clamped
- **angle EXACTLY EQUAL to a limit   -> unchanged, NOT clamped**

That last line is spec. Both ends. Get it wrong and three tests fail.

## THE CASES YOUR CODE MUST GET RIGHT

| joint    | commanded | safe angle | clamped? |
|----------|-----------|------------|----------|
| shoulder | 120       | 90         | yes      |
| shoulder | -90       | -90        | **no**   |
| shoulder | 0         | 0          | no       |
| elbow    | -10       | 0          | yes      |
| elbow    | 145       | 145        | **no**   |
| elbow    | 200       | 145        | yes      |
| wrist    | 90        | 90         | no       |
| wrist    | -400      | -180       | yes      |

Copy this table into your tests. It is the acceptance criteria.

---

# THE LEVELS

Work them in order. **L3 clean beats L5 broken.** Stop where you stop.

## L1 — one joint, one angle

Produce the safe angle for a single joint given its low and high.
All eight rows above must come out right, one at a time.

## L2 — many angles at once, one shared limit pair

Handle ANY NUMBER of angles in a single call, positionally — not a list
built by the caller. Same low/high applies to all of them.

Concrete: with low=-90, high=90, the angles `120, -90, 0, 200` must come
back as `90, -90, 0, 90`, in that order. Zero angles must also work.

**Use `*args` for this.** It is what you chose in S26 and it is why this
block exists.

## L3 — real per-joint limits, named

Now each joint has its OWN limits, and the caller supplies them BY NAME —
`shoulder` gets -90/90, `elbow` gets 0/145, `wrist` gets -180/180.

Concrete: commanded shoulder=120, elbow=-10, wrist=90 must produce
shoulder=90, elbow=0, wrist=90 — and **the result must say which joint got
which value.** A bare `(90, 0, 90)` is not enough here; something has to
carry the names.

**Use `**kwargs` for the limits.** Angles still arrive as `*args`.

⚠ **THIS IS THE LEVEL THE BLOCK EXISTS FOR.** It is harder than it looks
and it is supposed to be. When it fights you, log the stall and keep
working it. Do not come to me.

## L4 — a joint with no limits

Commanded: `gripper = 30`. No limits were supplied for `gripper`.

You decide: **raise, or pass it through unchanged.** Then write ONE line
in LOG.md saying why. The deciding question is whether that situation is a
BUG in the caller or an EXPECTED case.

## L5 — stretch, only if time remains

Report how many joints were actually clamped, and print one readable line
per joint. Something like:

    shoulder :  120.0 ->   90.0  CLAMPED
    elbow    :  -10.0 ->    0.0  CLAMPED
    wrist    :   90.0 ->   90.0  ok

Numbers aligned, two decimal places or one — your call, but make the
columns line up.

---

# TESTS — half the mark

`pytest` decides whether it works, not you.

Required, minimum:
- **the eight rows** in the acceptance table above
- L2's multi-angle case, including zero angles
- L3's per-joint routing
- L4's decision, whichever you chose

Plus **one test for each of THE FIVE CHECKS**, named so the name says which
check it is. You know the five. Mapping them onto this task is yours — that
mapping is part of what is being measured. If you cannot recall all five,
write down which ones you could not, and move on. Do not stall on it.

# ROUGH TIME SPLIT (guide)

L1 + tests 20 · L2 15 · L3 35 · L4 10 · five checks + final run 10
