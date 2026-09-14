class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def __repr__(self):
        return f"Joint('{self.name}', {self.angle})"

    def move(self, delta):
        self.angle = self.angle + delta

    @classmethod
    def from_dict(cls, d):
        print("cls is", cls)
        return cls(d["name"], d["angle"])

d = {"name": "elbow", "angle": 10}
a = Joint.from_dict(d)
print(a)
print(vars(a))
print(a.move)
