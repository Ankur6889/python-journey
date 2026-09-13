"""
Session 48 drill — a joint as a type of its own.

CONSTRAINTS (the tests decide; read them in tests/test_s48_joint.py):

1. `Joint(name, angle, limit)` must produce an object carrying exactly
   three attributes, `name`, `angle`, `limit`, holding what was passed.
   Two joints made one after the other must not share data.

2. `j.move(delta)` must change `j.angle` by `delta`, on the same object,
   and must return None. Two moves add up.

3. `j.is_safe()` must return True when `j.angle` lies between
   `-j.limit` and `j.limit`, and False otherwise. Which side the
   boundary falls on is in the tests, not here.

4. `j.describe()` must return the string  "<name> at <angle> deg"  for
   example  "elbow at 15 deg".

Nothing else. No printing.
"""


class Joint:
    def __init__(self, name, angle, limit):
        self.name = name 
        self.angle = angle 
        self.limit = limit

    def move(self, delta):
        self.angle = self.angle + delta

    def is_safe(self):
        if self.angle >= -abs(self.limit) and self.angle <= abs(self.limit):
            return True
        else:
            return False 
        

    def describe(self):
        return f"{self.name} at {self.angle} deg"
