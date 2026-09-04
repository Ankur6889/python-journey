"""
S41 DRILL -- 1.9, cold, at a real gap. pytest decides.

One type and three functions. Every interface and every expected value is
given. The only thing withheld is how you write the body.

DONE LINE: say "done", plus ONE LINE naming the function you trust least
and the CASE about it that worries you. Then I run the tests.

Nothing in this file prints. No function here decides what its caller does
about anything.
"""

LIMITS = {"base": 180, "shoulder": 90, "elbow": 120}


# ---------------------------------------------------------------------------
# THE TYPE
#
# This module must provide a name `BadCommand`.
#
# A caller that only reacts to "a value was wrong" in the general, built-in
# sense -- the same way it would react to int("n/a") failing -- must catch
# this WITHOUT naming it. A different caller that wants to react to a bad
# COMMAND specifically, and to nothing else, must be able to do that too.
#
# BadCommand("no such joint: wrist")   must be raisable.
# ---------------------------------------------------------------------------
class BadCommand(ValueError):
    pass


def to_angle(text):
    """
    text : str, supposed to spell a whole number of degrees.

    Returns that number as an int.

    If text does not spell a whole number, the caller must find out at the
    point it asked, and the report must be a BadCommand whose message
    contains `text` exactly as it arrived. For that case, NO OTHER KIND of
    report may leave this function.

    to_angle("45")   -> 45
    """
    try:
        return int(text)
    except BadCommand:
        raise BadCommand(f"The text:{text} you provided doesen't convert to number")
    


def check(joint, angle):
    """
    joint : str, a joint name.
    angle : int, degrees.

    Returns angle unchanged when joint is a key of LIMITS and
    0 <= angle <= LIMITS[joint].

    Unknown joint             -> BadCommand, message contains the joint name.
    Angle outside the range   -> BadCommand, message contains the angle and
                                 the limit, as decimal integers.
    Angle that is not an int at all (for example "45", or 45.0)
                              -> the built-in report for a wrong TYPE.
                                 That is not a bad command and must not be
                                 reported as one.

    check("shoulder", 45)   -> 45
    """
    try:
        
        if 0 <= int(angle) <= LIMITS[joint]:
            return angle 
        else:
            raise BadCommand(f"Entered angle {angle} does not follow in range 0<={angle}<={LIMITS[joint]}")
    except KeyError:
        raise BadCommand(f"The Entered joint: {joint} does not match any joint in {[i for i in LIMITS.keys()]} ")
    
    
    
def run(cmds, log):
    """
    cmds : list of (joint, text) pairs,
           e.g. [("shoulder", "45"), ("elbow", "n/a")].
    log  : list. Appended to, never replaced.

    For each pair, in order: turn text into an angle with to_angle, check it
    with check, and if BOTH steps succeed append ("ok", joint, angle) to log.
    If either step reports a bad command, append ("bad", joint, text) to log
    and carry on with the next pair.

    Any OTHER report leaves run exactly as it would have if run did not
    exist. BUT: before control leaves this function -- on normal completion
    AND on the way out with a report -- the LAST entry in log must be
    ("done", n), where n is the number of ("ok", ...) entries appended so
    far.

    Returns n on normal completion.

    log = []
    run([("shoulder", "45"), ("elbow", "n/a"), ("base", "200")], log) -> 1
    log == [("ok", "shoulder", 45),
            ("bad", "elbow", "n/a"),
            ("bad", "base", "200"),
            ("done", 1)]
    """
    ok_entries = 0
    try: 
        for joint_name,original_angle_value in cmds:
            try : 
                original_angle_value_int = to_angle(original_angle_value)
                corrected_angle_value = check(joint_name,original_angle_value_int)
            except BadCommand:
                log.append(("bad",joint_name,original_angle_value))

            else : 
                log.append(("ok",joint_name,original_angle_value_int))
                ok_entries = ok_entries+1
    finally:
        log.append(("done",ok_entries))
            
    return ok_entries