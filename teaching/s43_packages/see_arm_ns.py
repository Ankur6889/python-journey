import sys
import arm

print([k for k in sys.modules if k.startswith("arm")])
print([k for k in vars(arm) if not k.startswith("__")])

import arm.limits

print([k for k in sys.modules if k.startswith("arm")])
print([k for k in vars(arm) if not k.startswith("__")])
