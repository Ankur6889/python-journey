def read(text):
    try:
        return int(text)
    finally:
        print("finally ran for", repr(text))

print(read("45"))
print(read("n/a"))
