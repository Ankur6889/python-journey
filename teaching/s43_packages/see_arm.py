import sys

print([k for k in sys.modules if k.startswith("arm")])

import arm.limits

print([k for k in sys.modules if k.startswith("arm")])
print(sys.modules["arm"])
print(sys.modules["arm.limits"])
