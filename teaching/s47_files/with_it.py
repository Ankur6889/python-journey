with open("with.txt", "w") as f:
    f.write("elbow 10\n")
    print("inside block, closed?", f.closed)

print("after block,  closed?", f.closed)
print("on disk:", repr(open("with.txt").read()))
