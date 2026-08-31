"""
S36 DRILL -- 1.9, signals.

One type and four functions. Every interface and every expected value is
given. The only thing withheld is how you write the body.

THE GATE ON THE WORD "DONE" (the rule adopted this session):
say "done", plus ONE LINE naming the function you trust least and the
case about it that worries you. Then I run the tests.

Nothing in this file prints. Not one of these functions decides what its
caller does about anything.
"""


# ---------------------------------------------------------------------------
# THE TYPE
#
# This module must provide a name `OverLimit`.
#
# A caller must be able to react to an angle being out of range WITHOUT
# also reacting to a string that was never a number in the first place --
# and a different caller, one that only wants to know "did anything go
# wrong at all", must still catch it without naming it.
#
# OverLimit("angle 200 exceeds limit 180")   must be raisable.
# ---------------------------------------------------------------------------
class OverLimit(Exception):
    pass 

class UnknownJointError(Exception):
    pass 

def check_limit(angle, limit):
    """
    angle : int, a joint reading in degrees.
    limit : int, the highest reading this joint is allowed to report.

    If the angle is allowed, hands it straight back, unchanged.

    If the angle is NOT allowed, the caller must be told in a way that
    cannot be stored, compared, or mistaken for a reading -- and in a way
    that can be reacted to on its own, separately from a complaint about
    text that is not a number. The report must carry both numbers, the
    angle first and the limit second, as decimal integers.

    check_limit(90, 180)   -> 90
    """
    if angle > limit: 
        raise OverLimit(f"The angle : {angle} is greater then allowed limit i.e. {limit}")
    return angle 

def read_limit(config, joint):
    """
    config : dict, joint name (str) -> highest allowed reading (int).
    joint  : str, the joint being asked about.

    Hands back that joint's limit.

    If that joint is not in config, the caller must find out at the point
    it asked -- not three lines later, and not by inspecting whatever came
    back. This function does not choose what the caller does about it.

    read_limit({"elbow": 150, "wrist": 90}, "elbow")   -> 150
    """
    if joint not in config: 
        raise UnknownJointError(f"You asked for '{joint}' but its not in the config i.e. {[i for i in config]} ")
    return config[joint]

def sort_faults(readings, limit):
    """
    readings : list of str, each one supposed to spell a whole number of
               degrees.
    limit    : int, the highest reading allowed.

    Returns a dict with exactly three keys:

        "ok"     -> list of int: the readings that spelled a number and
                    were allowed, in the order they appeared.
        "over"   -> list of int: the readings that spelled a number and
                    were not allowed, in the order they appeared.
        "broken" -> list of str: the readings that did not spell a whole
                    number at all, kept exactly as they arrived, in order.

    Whether a number is allowed is decided by check_limit above and by
    nothing else -- this function must not contain its own copy of that
    rule.

    `readings` must be unchanged after the call. Nothing crashes, whatever
    is in the list.

    sort_faults(["45", "200", "n/a", "90"], 180)
        -> {"ok": [45, 90], "over": [200], "broken": ["n/a"]}
    """
    state_dict = {"ok":[],"over":[],"broken":[]}
    for r in readings:
        try:
            state_dict["ok"].append(check_limit(int(r),limit))
        except OverLimit:
            state_dict["over"].append(int(r))
        except ValueError:
            state_dict["broken"].append(r)
        
    
    return state_dict


def audited(readings, limit, log):
    """
    readings : list of int, joint readings in degrees.
    limit    : int, the highest reading allowed.
    log      : list, used to record that a fault was seen here.

    Returns a new list of the allowed readings, in order.

    The first reading that is not allowed ends the call. Before control
    leaves this function, the string "OVER" must have been appended to
    `log` exactly once -- and the caller must still find out about that
    fault, in exactly the same way, and pointing at exactly the same
    place, as it would have if `audited` did not exist at all.

    If every reading is allowed, `log` is untouched.

    log = []
    audited([45, 90], 180, log)   -> [45, 90],  and log is still []
    """
    allowed =[]
    for r in readings: 
        try: 
            allowed.append(check_limit(r,limit))
        except OverLimit:
            log.append("OVER")
            raise 
    return allowed
