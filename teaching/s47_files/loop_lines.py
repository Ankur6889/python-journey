f = open("limits.txt")
for line in f:
    print(repr(line))
print(repr(f.read()))
f.close()
