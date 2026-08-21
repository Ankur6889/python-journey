"""
S24 — lists under constraint.

Four separate jobs. Each one states what the CALLER must be able to
observe after your function has run. Nothing else is specified: the
observable behaviour is the whole contract.

Assume every `readings` argument is a list of numbers.

1. ordered_copy(readings)
   The caller hands you their list and keeps using it afterwards.
   After your call returns, THEIR list must be exactly as it was.
   Your call must evaluate to the same values arranged smallest first.

2. order_in_place(readings)
   The opposite deal. After your call returns, the CALLER'S OWN list
   must itself be arranged smallest first.
   Your call must evaluate to nothing the caller can use.

3. take_last(readings)
   After your call returns, the caller's list must be exactly one
   shorter, and the value that is no longer in it must be what your
   call evaluated to.
   You may assume the list is not empty.

4. last_three(readings)
   Your call must evaluate to a separate list holding the final three
   values, oldest of the three first. The caller's list must be
   unchanged. If the caller's list holds fewer than three values, your
   call evaluates to all of them.
   This one must not raise for ANY length of input, including zero.

Before you say done, run the five checks on all four.
"""


def ordered_copy(readings):
    readings_copy = readings[:]
    readings_copy.sort()
    return readings_copy




def order_in_place(readings):
    return readings.sort()


def take_last(readings):
    if readings == []:
        return 
    return readings.pop()


def last_three(readings):
    return readings[-3:]
