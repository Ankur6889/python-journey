f = open("buf.txt", "w")
try:
    f.write("elbow 10\n")
    f.write("wrist 45\n")
finally:
    f.close()

print(repr(open("buf.txt").read()))
