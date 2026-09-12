try:
    with open("with_err.txt", "w") as f:
        f.write("elbow 10\n")
        f.write(42)
        print("this line never runs")
except TypeError:
    print("write raised. closed?", f.closed)

print("on disk:", repr(open("with_err.txt").read()))
