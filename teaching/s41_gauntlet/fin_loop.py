def inside(items):
    for x in items:
        try:
            print("work", x)
        finally:
            print("done")

def around(items):
    try:
        for x in items:
            print("work", x)
    finally:
        print("done")

print("-- try INSIDE the loop")
inside([1, 2, 3])
print("-- try AROUND the loop")
around([1, 2, 3])
