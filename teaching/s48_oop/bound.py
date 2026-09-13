class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

    def move(self, delta):
        self.angle = self.angle + delta

a = Joint("elbow", 10)

print(vars(a))
print(Joint.move)
print(a.move)

m = a.move
m(5)
print(vars(a))
