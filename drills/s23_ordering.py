"""
S23 DRILL — ordering by a computed property, with documentation that
survives to runtime.

Two orderings are needed.

    sort_by_last_digit([21, 45, 13])   ->  [21, 13, 45]
        (ordered by the final digit of each number: 1, 3, 5)

    sort_by_length(["bbb", "a", "cc"]) ->  ["a", "cc", "bbb"]

Both must be done with `sorted(..., key=...)`.

THE CONSTRAINTS:

1. This file must contain EXACTLY the two `def` statements already
   written below. You may not add a third one anywhere, at any level.

2. Neither function may modify the list it was given.

3. Every function in this file must carry its own description, and that
   description must still be readable while the program is RUNNING —
   something the program itself can print back out. A `#` comment does
   not survive to runtime and will not satisfy this.

Substrate you may use: def, return, sorted(..., key=...), len(), %,
lists, strings. Nothing here needs anything you have not been taught.
"""


def sort_by_last_digit(numbers):
    """ This function sorts the provided list based on the last digit of each number in the list"""
    last_digit = lambda x : x%10
    return sorted(numbers,key=last_digit)


def sort_by_length(words):
    """ This function sorts the provided list based on the length of the words"""
    length = lambda x : len(x)
    return sorted(words,key=length)
