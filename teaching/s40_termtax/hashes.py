print(hash(1) == hash(1.0))     # equal values hash equal
print(hash("a") == hash("a"))
try:
    hash([1, 2])
except TypeError as e:
    print("TypeError:", e)
