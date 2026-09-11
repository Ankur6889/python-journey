import sys
import p
print("main after import, keys now:", [k for k in sys.modules if k.startswith("p")])
