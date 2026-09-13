class Joint:
    pass

a = Joint()
b = Joint()

a.name = "elbow"
a.angle = 10
b.name = "wrist"

print(vars(a))
print(vars(b))
print(vars(a)["angle"])
