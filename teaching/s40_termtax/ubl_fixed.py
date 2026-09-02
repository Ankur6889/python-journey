count = 0

def bump():
    print(count)      # no assignment anywhere in the body -> count is GLOBAL here

bump()
