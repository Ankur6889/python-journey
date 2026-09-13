a = list()

try:
    a.name = "ankur"
except AttributeError as e:
    print("attach:", e)

try:
    print(vars(a))
except TypeError as e:
    print("vars:  ", e)

def f():
    pass

f.name = "ankur"
print(vars(f))
