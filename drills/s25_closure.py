"""
S25 DRILL — a safety clamp that remembers its own limit.

A joint has a symmetric travel limit. Any commanded angle must be pulled
back inside that limit before it reaches the hardware.

Different joints have different limits, and the limits are known when the
robot is CONFIGURED — not when the clamping code is written.

    shoulder = make_clamp(90)
    wrist    = make_clamp(15)

    shoulder(120)   ->   90
    shoulder(-120)  ->  -90
    shoulder(45)    ->   45
    wrist(120)      ->   15

THE CONSTRAINTS. These are the whole exercise; a solution that clamps
correctly but breaks one of these is wrong.

1. The tool that `make_clamp` hands back takes EXACTLY ONE argument:
   the commanded angle. There is nowhere to pass it the limit.

2. No `global`. The limit may not live at module level, and there may
   not be a module-level name holding it.

3. `make_clamp` has completely finished and returned long before the
   tool it produced is ever used. The tool must still clamp to the right
   limit on its ten-thousandth call, hours later.

4. `shoulder` and `wrist` are alive at the same time and must not
   interfere with each other in either direction.

5. clamp_all(angles, limit). Four separate requirements:

   (a) It builds its tool by calling make_clamp.
   (b) Your call evaluates to a list.
   (c) That list is a DIFFERENT object from the one the caller passed
       in, and the caller's own list is unchanged afterwards.
   (d) Position by position, that list holds each of the caller's
       angles after clamping. Position 0 comes from position 0, and so
       on for every position.

        angles = [120, -120, 45]
        clamp_all(angles, 90)   ->   [90, -90, 45]
        angles                  ->   [120, -120, 45]

Substrate you may use: def, return, lambda, if/else, comparison
operators, for, lists, list methods, slicing, sorted/key. Nothing here
needs anything you have not been taught.

Before you say done, run the five checks on both functions.
"""




def make_clamp(limit):
    def impose_limit(given_value):
        if abs(given_value)> limit:
            if given_value <0:
                return -limit
            else : 
                return limit
        return given_value
    return impose_limit
   
   


def clamp_all(angles, limit):
    imposed_limit = make_clamp(limit)
    clamped_angles = angles[:]
    for i in range(len(clamped_angles)):
       clamped_angles[i] = imposed_limit(clamped_angles[i])
    return clamped_angles
       
