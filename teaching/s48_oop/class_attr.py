class Joint:
    unit = "deg"

    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a.unit, b.unit)
print(vars(a))
print(vars(b))
print("unit" in vars(Joint))
print("__init__" in vars(Joint))
