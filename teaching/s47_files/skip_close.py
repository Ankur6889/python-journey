f = open("skip.txt", "w")
try:
    f.write("elbow 10\n")
    f.write(42)
    f.close()
except TypeError:
    print("write raised. did close run?", f.closed)

print("on disk:", repr(open("skip.txt").read()))
