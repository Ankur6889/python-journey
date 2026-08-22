"""
S27 DRILL — five small functions.

Each function has CONSTRAINTS attached. The constraints are part of the task:
code that passes the tests but breaks a constraint does not count. I check the
constraints by reading your code; pytest only checks the behaviour.

Rules for this file:
  - no imports
  - nothing we have not covered

Run the tests with:
    python3 -m pytest tests/test_s27_flow.py -q

-------------------------------------------------------------------------
1. first_big(values, limit)

   Return the first item of `values` that is greater than `limit`.
   If no item is greater than `limit`, return None.

   (a) once the answer has been found, no further item may be examined
   (b) the function body contains EXACTLY ONE `return`, and it is the
       LAST line of the function

-------------------------------------------------------------------------
2. total_positive(values)

   Return the total of the items of `values` that are greater than zero.
   Items that are zero or negative contribute nothing.

   (a) the `if` inside the loop has NO `else`
   (b) the line that does the adding is NOT inside that `if`

-------------------------------------------------------------------------
3. find_index(values, target)

   Return the position of the first item of `values` equal to `target`.
   If `target` is not in `values`, the function must print exactly

       missing

   and return None.

   (a) the function contains EXACTLY ONE `return`, and it is the LAST
       line of the function
   (b) the printing line runs ONLY when the loop was allowed to reach
       its natural end
   (c) no `if` may appear after the loop

-------------------------------------------------------------------------
4. label(n)

   Return the string "high" when n is greater than 10, and the string
   "low" otherwise.

   (a) the body is a SINGLE line
   (b) that line is a `return`

-------------------------------------------------------------------------
5. todo(x)

   A placeholder for a function that is not written yet. Calling it must
   not crash, and it must produce None.

   (a) the body is EXACTLY one line
   (b) that line is not a `return`, not a string, and not an assignment
-------------------------------------------------------------------------
"""


def first_big(values, limit):
    """Return the first item of `values` that is greater than `limit`.
       If no item is greater than `limit`, return None.
    
       (a) once the answer has been found, no further item may be examined
       (b) the function body contains EXACTLY ONE `return`, and it is the
           LAST line of the function
    """
    for i in values: 
        if i > limit:
            break
    else : 
        i = None 
    return i



def total_positive(values):
    """Return the total of the items of `values` that are greater than zero.
       Items that are zero or negative contribute nothing.
    
       (a) the `if` inside the loop has NO `else`
       (b) the line that does the adding is NOT inside that `if`"""
    sum = 0
    for i in values: 
        if i<=0:
            continue
        sum = sum + i 
    return sum 

def find_index(values, target):
    """ find_index(values, target)

   Return the position of the first item of `values` equal to `target`.
   If `target` is not in `values`, the function must print exactly

       missing

   and return None.

   (a) the function contains EXACTLY ONE `return`, and it is the LAST
       line of the function
   (b) the printing line runs ONLY when the loop was allowed to reach
       its natural end
   (c) no `if` may appear after the loop"""
    l= len(values)
    for i in range(l):
        if values[i]==target:
            break
    else:
        i=None
        print("missing")
    return i 

def label(n):
    """label(n)

   Return the string "high" when n is greater than 10, and the string
   "low" otherwise.

   (a) the body is a SINGLE line
   (b) that line is a `return`"""
    return "high" if n>10 else "low"

def todo(x):
    """odo(x)

   A placeholder for a function that is not written yet. Calling it must
   not crash, and it must produce None.

   (a) the body is EXACTLY one line
   (b) that line is not a `return`, not a string, and not an assignment"""
    pass 