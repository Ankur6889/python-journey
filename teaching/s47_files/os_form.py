import os

print("shell is in:", os.getcwd())

here = os.path.dirname(os.path.abspath(__file__))
print("script is in:", here)

path = os.path.join(here, "limits.txt")
print("opening:", path)

with open(path) as f:
    print(repr(f.read()))
