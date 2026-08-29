"""
S33 drill — four functions. Write the bodies only.

Nothing here needs anything you have not been taught.
`import` whatever you need at the top of this file.


1. snapshot(config)

   config is a dict mapping a joint name to a two-item list [low, high].

       {"elbow": [0, 150], "wrist": [-90, 90]}

   Return a copy that is INDEPENDENT ALL THE WAY DOWN: after you have the
   copy, changing any inner list of the copy must leave config completely
   unchanged, and changing any inner list of config must leave the copy
   completely unchanged.

   The returned dict must compare equal to config.

       snapshot({"elbow": [0, 150]})  ->  {"elbow": [0, 150]}


2. drop_unsafe(angles, ceiling)

   angles is a list of numbers. ceiling is a number.

   Return a NEW list holding the angles that are not above the ceiling,
   in the order they appeared. The list you were passed must NOT be
   changed in any way.

       drop_unsafe([10, 200, 250, 30], 180)  ->  [10, 30]
       drop_unsafe([5, 7], 100)              ->  [5, 7]


3. replay_order(steps)

   steps is a list of strings.

   Return a NEW list holding the same strings last-to-first. The list you
   were passed must NOT be changed in any way.

       replay_order(["home", "pick", "lift"])  ->  ["lift", "pick", "home"]


4. missing_joints(required, present)

   required and present are both lists of joint-name strings. Either list
   may contain the same name more than once.

   Return the names that appear in required and do not appear in present.
   The return value must be a set.

       missing_joints(["elbow", "wrist", "base"], ["elbow", "base"])  ->  {"wrist"}


Before you tell me you are done: run the five checks on this file yourself.
That is the gate on the word "done", not something I ask for afterwards.
"""


def snapshot(config):
    import copy 
    return copy.deepcopy(config)


def drop_unsafe(angles, ceiling):
    return [i for i in angles if i<=ceiling]


def replay_order(steps):
    return [steps[-(i+1)] for i in range(len(steps))]


def missing_joints(required, present):
    return set(required)-set(present)
