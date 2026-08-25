"""
S31 — SIX FUNCTIONS. THREE PAIRS. Each pair does the same job twice,
once for a caller who EXPECTS the thing to be missing, and once for a
caller for whom a missing thing is a BUG.

⚠ THE CONSTRAINT THAT MAKES THIS A DRILL AND NOT TYPING PRACTICE:

    In this file you may NOT write  `if`,  `in`,  `else`,  or  `try`.

    Every body is ONE line, except the two set functions which get two.
    If you find yourself guarding a lookup, stop — you are hand-rolling
    something that already exists.

You write drills/s31_shrug.py only. I wrote tests/test_s31_shrug.py.
Run:  python3 -m pytest tests/test_s31_shrug.py -q


LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145)}


--- PAIR 1 : reading a limit -------------------------------------------

limit_for(LIMITS, "elbow")     == (0, 145)
limit_for(LIMITS, "gripper")   == (-180, 180)      <- absence is EXPECTED

must_limit(LIMITS, "elbow")    == (0, 145)
must_limit(LIMITS, "gripper")  -> raises           <- absence is a BUG


--- PAIR 2 : removing a limit ------------------------------------------
Both of these CHANGE the dict they are given.

d = {"shoulder": (-90, 90), "elbow": (0, 145)}

drop_limit(d, "elbow")    == (0, 145)   and afterwards d == {"shoulder": (-90, 90)}
drop_limit(d, "gripper")  is None       and d is unchanged   <- EXPECTED

must_drop(d, "gripper")   -> raises                          <- a BUG


--- PAIR 3 : taking a joint out of service -----------------------------
`active` is a SET of joint names. Both of these CHANGE it and return it.

retire({"shoulder", "elbow"}, "elbow")   == {"shoulder"}
retire({"shoulder", "elbow"}, "gripper") == {"shoulder", "elbow"}  <- EXPECTED

must_retire({"shoulder", "elbow"}, "gripper") -> raises            <- a BUG


The SOLUTION is withheld. Nothing else is.
"""


def limit_for(limits, joint):
    ...


def must_limit(limits, joint):
    ...


def drop_limit(limits, joint):
    ...


def must_drop(limits, joint):
    ...


def retire(active, joint):
    ...


def must_retire(active, joint):
    ...
