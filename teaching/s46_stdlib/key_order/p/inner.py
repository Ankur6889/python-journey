import sys
print("p/inner.py running, keys now:", [k for k in sys.modules if k.startswith("p")])
