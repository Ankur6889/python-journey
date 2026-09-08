import sys
print("self_check.py line 2, still running")
print("self_check" in sys.modules)
print(vars(sys.modules["self_check"]).get("X"))
X = 1
print("self_check.py done")
