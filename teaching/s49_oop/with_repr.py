class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def __repr__(self):
        return f"Joint('{self.name}', {self.angle})"

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a)
print("__repr__" in vars(Joint))
print([a, b])
