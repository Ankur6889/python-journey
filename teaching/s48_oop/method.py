class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def move(self, delta):
        self.angle = self.angle + delta

a = Joint("elbow", 10)
b = Joint("wrist", 45)

a.move(5)
b.move(-40)
print(vars(a))
print(vars(b))

Joint.move(a, 100)
print(vars(a))
