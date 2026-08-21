"""
S25 DRILL — walking a sequence by hand.

Two jobs. Both take `items`, a list.

    first_two([10, 20, 30, 40])   ->   [10, 20]
    drop_first([10, 20, 30, 40])  ->   [20, 30, 40]

`drop_first` must not disturb the caller's own list.

THE CONSTRAINT, and it is the whole exercise. In this file you may NOT
use any of these:

    for            while          [ ] for position or slicing
    .pop()         .remove()      .index()        enumerate

You may assume both lists have at least two items.

Everything you need to do this has already been taught. If you find
yourself wanting one of the banned things, that is the drill working:
the thing those constructs are built on top of is what is being asked
for here.
"""


def first_two(items):
    val = iter(items)
    f_t = [] 
    f_t.append(next(val))
    f_t.append(next(val))
    return f_t
    


def drop_first(items):
    val=iter(items)
    next(val)
    remaining = list(val)
    return remaining 
    
