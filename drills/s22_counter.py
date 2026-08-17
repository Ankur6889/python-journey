"""
Two functions sharing one running count.

    tick()  -> int   each call returns the next integer: 1, then 2, then 3, ...
    reset() -> None  after this, the next tick() returns 1 again.

Constraints:
- No classes. No nested functions, no factories. No default-argument tricks.
- Both are plain top-level functions, callable in any order, any number
  of times, and the count must survive between calls.
"""

count = 0

def tick():
    global count
    count = count+1
    return count 
    

def reset():
    global count 
    count = 0

