import sys
from arm.limits import MAX_ANGLE
print([k for k in sys.modules if k.startswith("arm") or k == "limits"])
print("MAX_ANGLE" in vars(), "limits" in vars(), "arm" in vars())
