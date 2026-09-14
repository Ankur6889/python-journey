class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
b = Joint("wrist", 45)

print(a)
print([a, b])
