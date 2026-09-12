w = open("buf.txt", "w")
w.write("elbow 10\n")

r = open("buf.txt")
print("before close:", repr(r.read()))
r.close()

w.close()

r = open("buf.txt")
print("after close: ", repr(r.read()))
r.close()
