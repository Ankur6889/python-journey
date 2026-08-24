"""
S30 DRILL — containers backlog. Six functions. Write the bodies. Nothing else.

BINDING CONSTRAINT, ALL SIX:
    The body of each function is EXACTLY ONE `return` statement.
    No loops. No `if` statements. No temporary variables.

The signatures below are exact. The expected values below are exact.
Run: python3 -m pytest tests/test_s30_containers.py -q


1) limits_for(limits, joint)
   limits : dict of joint name -> a pair of numbers
   joint  : a string
   returns: the pair for that joint, or (0, 0) when the joint is absent.
            Absence here is EXPECTED, not a bug.

   LIMITS = {"shoulder": (-90, 90), "elbow": (0, 145)}
   limits_for(LIMITS, "elbow")   ->  (0, 145)
   limits_for(LIMITS, "wrist")   ->  (0, 0)


2) shared_joints(a, b)
   a, b   : lists of joint names, each may contain duplicates
   returns: every name that appears in BOTH, with no duplicates and no order.

   shared_joints(["shoulder", "elbow", "wrist"], ["elbow", "wrist", "gripper"])
       ->  {"elbow", "wrist"}
   shared_joints(["shoulder", "shoulder"], ["shoulder"])  ->  {"shoulder"}
   shared_joints(["shoulder"], ["elbow"])                 ->  set()


3) pop_limit(limits, joint)
   limits : dict of joint name -> number.  THIS FUNCTION CHANGES IT.
   joint  : a string
   returns: the value that was removed, or None when the joint is absent.
            Absence here is EXPECTED, not a bug.

   d = {"shoulder": 90, "elbow": 45}
   pop_limit(d, "elbow")   ->  45     and afterwards d == {"shoulder": 90}
   pop_limit(d, "wrist")   ->  None   and afterwards d == {"shoulder": 90}


4) snapshot(angles)
   angles : list of numbers
   returns: a NEW list with the same numbers, independent of the original —
            changing one must not change the other.

   a = [10, 20, 30]
   b = snapshot(a)      ->  [10, 20, 30]
   b.append(99)         ->  a is still [10, 20, 30]


5) span(low, high)
   low, high : numbers
   returns   : ONE object carrying the low, the high, and the distance
               between them, in that order.

   span(0, 145)    ->  (0, 145, 145)
   span(-90, 90)   ->  (-90, 90, 180)


6) total(angles)
   angles : list of numbers
   returns: their sum.

   total([10, 20, 30])   ->  60
   total([])             ->  0
"""


def limits_for(limits, joint):
    return limits.get(joint,(0,0)) 


def shared_joints(a, b):
    return set(a)&set(b)

def pop_limit(limits, joint):
    return limits.pop(joint,None) 

def snapshot(angles):
    return angles[:]


def span(low, high):
    return (low,high,abs((low)-(high)))


def total(angles):
    return sum(angles)
