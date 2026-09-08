import arm.limits

print("arm" in vars())
print("limits" in vars())
print("arm.limits" in vars())

print("limits" in vars(arm))
print(arm.limits.MAX_ANGLE)
