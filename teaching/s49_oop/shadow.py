class Joint:
    unit = "deg"

    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

a.unit = "rad"
print(a.unit)
print(b.unit)
print(vars(a))
print(vars(Joint)["unit"])
