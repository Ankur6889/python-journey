"""
S23 DRILL — ordering by a runtime-chosen reference point.

A list of joint angles has to be put in order by how far each angle sits
from a TARGET angle. The target is not known when the ordering tool is
written: it is chosen at call time, and different calls use different
targets.

The ordering must be done by `sorted(values, key=...)`.

THE CONSTRAINT THAT MATTERS: `sorted` calls whatever you give to `key=`
with EXACTLY ONE argument — the element being sorted. It will not pass
anything else, and it offers no way to hand it extra information.

Complete this file so that:

    order_by_distance([10, 4, 7], 5)   ->  [4, 7, 10]
    order_by_distance([10, 4, 7], 9)   ->  [10, 7, 4]

and so that `make_distance_key(target)` produces something that can be
handed straight to `sorted(..., key=...)` and will measure distance from
that target.

Two calls to `make_distance_key` with different targets must not
interfere with each other.

Substrate you may use: def, return, sorted(..., key=...), abs(), lists,
arithmetic. Nothing here needs anything you have not been taught.
"""


def make_distance_key(target):
    def distance_from_target(val):
        return abs(val - target)
    return distance_from_target



def order_by_distance(values, target):
    calculate_distance = make_distance_key(target)
    return sorted(values,key=calculate_distance)


