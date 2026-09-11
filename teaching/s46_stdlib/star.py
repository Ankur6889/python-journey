def clamp(value, low, high, *, verbose=False):
    if verbose:
        print("clamping", value, "into", low, high)
    return max(low, min(value, high))

print(clamp(150, 0, 100))
print(clamp(150, 0, 100, verbose=True))
print(clamp(150, 0, 100, True))
