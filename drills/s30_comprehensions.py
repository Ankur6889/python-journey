"""
S30 DRILL — four functions. Write the bodies. Nothing else.

BINDING CONSTRAINT, ALL FOUR:
    The body of each function is EXACTLY ONE `return` statement.
    No loops. No temporary variables. No `.append()`.
    In format_row additionally: no `+`, no `str()`, no `.format()`.

The signatures below are exact. The expected values below are exact.
Run: python3 -m pytest tests/test_s30_comprehensions.py -q


1) over_limit(angles, ceiling)
   angles  : list of numbers
   ceiling : a number
   returns : a NEW list holding the angles that are above the ceiling,
             in the order they appeared.

   over_limit([10, 45, 90, 45, 5], 45)   ->  [90]
   over_limit([1, 2, 3], 10)             ->  []
   over_limit([-30, 0, 30], -30)         ->  [0, 30]


2) scaled(limits, factor)
   limits  : dict of joint name -> number
   factor  : a number
   returns : a NEW dict, same keys, each value multiplied by factor.

   scaled({"shoulder": 90, "elbow": 45}, 2)   ->  {"shoulder": 180, "elbow": 90}
   scaled({}, 5)                              ->  {}


3) names_over(limits, ceiling)
   limits  : dict of joint name -> number
   ceiling : a number
   returns : a NEW list of the NAMES whose value is above the ceiling,
             in the dict's own order.

   names_over({"shoulder": 90, "elbow": 45, "wrist": 120}, 45)  ->  ["shoulder", "wrist"]
   names_over({"shoulder": 90, "elbow": 45}, 200)               ->  []


4) format_row(name, value)
   name    : a string
   value   : a number
   returns : one string — the name occupying 10 character columns,
             then the value occupying 8 character columns with 2 decimal places.

   format_row("shoulder", 12.5)         ->  "shoulder     12.50"
   format_row("elbow", 4.0)             ->  "elbow         4.00"
   format_row("wrist_rotation", 100.456)->  "wrist_rotation  100.46"
"""


def over_limit(angles, ceiling):
    return [x for x in angles if x > ceiling]


def scaled(limits, factor):
    return {key:value*factor for key,value in limits.items() }


def names_over(limits, ceiling):
    return [key for key,value in limits.items() if value>ceiling]


def format_row(name, value):
    return f"{name:10s}{value:8.2f}"
