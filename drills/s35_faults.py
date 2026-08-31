"""
S35 DRILL — 1.9, faults.

Four small functions. Every interface and every expected value is given.
The only thing withheld is how you write the body.

THE GATE ON THE WORD "DONE": run THE FIVE CHECKS on each function you
finish, and report them to me in this form —
    the CASE you ran, the VALUE that came back, and whether it MATCHED.
You run them by CALLING YOUR OWN FUNCTION and looking at what comes back.
Never by pytest. An `if` sitting in the body is not a check.
"""


def total_valid(readings):
    """
    readings : list of str, each one supposed to spell a whole number.

    Returns the sum of the ones that DO spell a whole number, as an int.
    Any string that does not spell a whole number is ignored.
    Nothing is printed. Nothing crashes, whatever is in the list.

    total_valid(["45", "90", "n/a", "30"])   -> 165
    total_valid(["12", "8"])                 -> 20
    """
    filtered_readings = []
    for i in readings:
        try:
            filtered_readings.append(int(i))
        except ValueError as e:
            print(f"There is a problem with the reading {i} you are supposed to enter numbers only")
    return sum(filtered_readings)


def check_angle(angle, limit):
    """
    angle : int, a joint reading in degrees.
    limit : int, the highest reading this joint is allowed to report.

    If the angle is allowed, hands it straight back, unchanged.

    If the angle is NOT allowed, the caller must be told in a way that
    CANNOT be mistaken for a reading and cannot be used by accident as
    one. That report must be a ValueError, and its message must contain
    both the angle and the limit, as decimal numbers, in that order.

    check_angle(90, 180)   -> 90
    """
    if angle>limit:
        raise ValueError(f"The angle :{angle:4.1f} should not be greater than {limit:4.1f}")
    return angle
        


def safe_angles(readings, limit):
    """
    readings : list of int, joint readings in degrees.
    limit    : int, the highest reading this joint is allowed to report.

    Returns a NEW list holding only the allowed readings, in the order
    they appeared. `readings` must be unchanged after the call.

    Whether a reading is allowed is decided by check_angle above, and by
    nothing else -- this function must not contain its own copy of that
    rule.

    safe_angles([45, 90, 200, 30], 180)   -> [45, 90, 30]
    """
    checked_readings = []
    for r in readings:
        try:
            checked_readings.append(check_angle(r,limit))
        except ValueError as e:
            print(e)
    return checked_readings    

def measure(text, log):
    """
    text : str, supposed to spell a whole number.
    log  : list, used to record that this call finished with the sensor
           shut down properly.

    Hands back the whole number the text spells.

    If the text does not spell a whole number, this function does NOT
    hide that from the caller -- the caller must still find out, and must
    find out in the same way it would have if `measure` did not exist.

    Either way -- value handed back, or caller told -- the string
    "closed" must have been appended to `log` exactly once by the time
    control leaves this function.

    log = []
    measure("45", log)   -> 45,  and log is now ["closed"]
    """
    try:
        return int(text)
    finally:
        log.append("closed")
        print(f"{text}, and log is now {log}")
    