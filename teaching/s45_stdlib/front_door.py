import sys
import json

print([k for k in sys.modules if k.startswith("json")])
print([k for k in vars(json) if not k.startswith("_")])
print(json.decoder.__file__)
