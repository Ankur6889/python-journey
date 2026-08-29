"""
S34 DRILL — the 1.8 tail.

Seven small functions. Every interface and every expected value is given.
The only thing withheld is how you write the body.

THE GATE ON THE WORD "DONE": run THE FIVE CHECKS on each function you
finish, and report them to me. "Done" without the five checks is not done.
"""


def build_queue(base, extras, urgent):
    """
    base    : list of str, task names, in the order they should run.
    extras  : list of str, to go at the END, in the order given.
    urgent  : str, a single name that must go at the very FRONT.

    Returns a NEW list.
    `base` must be unchanged after the call.

    build_queue(["scan", "grip"], ["lift", "drop"], "estop")
        -> ["estop", "scan", "grip", "lift", "drop"]
    """
    
    """    
    new_queue = []
    for u in urgent:
        new_queue.append(u)
    for b in base:
        new_queue.append(b)
    for e in extras:
        new_queue.append(e)
    return new_queue
    -------this is one way , and the easiest , but since you want me to show my learning see below
    """
    ## the point here is there are so many ways to do this and I guess you are trying to see the use of list methods
    new_queue = base[:]
    new_queue = new_queue + extras  # may be I could have used .extend() method here 
    new_queue.insert(0,urgent)  # or I could have used addition here but urgent+ new_queu
    return new_queue

def drop_task(queue, name):
    """
    queue : list of str.
    name  : str.

    Deletes the FIRST occurrence of `name` from `queue`, changing `queue`
    itself. If `name` is not in `queue`, `queue` is left exactly as it was.
    Returns None in both cases.

    q = ["scan", "grip", "scan"]
    drop_task(q, "scan")      # q is now ["grip", "scan"]
    drop_task(q, "weld")      # q is still ["grip", "scan"]
    """
    if name in queue:
        return queue.remove(name)
    else:
        return None 

def ranked(values):
    """
    values : list of int.

    Returns a NEW list holding the same values in ascending order.
    `values` must be unchanged after the call.

    ranked([3, 1, 2]) -> [1, 2, 3]
    """
    # ok so there are 2 ways of doing this since only requirement is values remains unchanged , nothing about the actual list should remain unchange 
    return sorted(values) # could have also used values.sort() but that will mutate the passed list so not using that

def rank_in_place(values):
    """
    values : list of int.

    Puts `values` itself into ascending order. Builds nothing new.
    Returns None.

    v = [3, 1, 2]
    rank_in_place(v)          # v is now [1, 2, 3]
    """
    return values.sort() # ah I didn't see this in previous function so I wrote that comment

def reading_stats(readings, target):
    """
    readings : a tuple of int.
    target   : int.

    Returns a tuple of two ints: (how_many, first_position), where
    how_many is how many times `target` appears in `readings`, and
    first_position is the 0-based position of its first appearance.
    If `target` never appears, return (0, -1).

    reading_stats((4, 7, 4, 9), 4) -> (2, 0)
    reading_stats((4, 7, 4, 9), 7) -> (1, 1)
    """
    if target in readings:
        return readings.count(target),readings.index(target)
    else:
        print("This was not necessary and not asked but just for other cases")
        return (0,-1) 
    

def shared_keys(a, b):
    """
    a, b : dicts.

    Returns a SET holding every name that is a key in `a` AND a key in `b`.

    shared_keys({"x": 1, "y": 2}, {"y": 9, "z": 3}) -> {"y"}
    """
    return set(a) & set(b)

def unique_sensors(names):
    """
    names : list of str, possibly with repeats.

    Returns a LIST of the names that occur, each one appearing once,
    in ascending alphabetical order.

    unique_sensors(["b", "a", "b", "c"]) -> ["a", "b", "c"]
    """
    
    return sorted(list(set(names)))