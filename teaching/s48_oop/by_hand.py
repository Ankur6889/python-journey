class Joint:
    def __init__(self, name, angle):
        self.name = name
        self.angle = angle

a = Joint("elbow", 10)
print(vars(a))

result = Joint.__init__(a, "shoulder", 90)
print(result)
print(vars(a))

b = Joint(a, "elbow", 10)
