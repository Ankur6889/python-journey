import sys

print(type(sys.modules))
print("robot" in sys.modules)

import robot

print("robot" in sys.modules)
print(sys.modules["robot"])
