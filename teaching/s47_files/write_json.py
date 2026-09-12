import json

cfg = {"robot": "gen3", "limits": (10, 45), "safe": True, "note": None}

with open("out.json", "w") as f:
    json.dump(cfg, f, indent=2)

print(open("out.json").read())

with open("out.json") as f:
    back = json.load(f)
print(back["limits"], type(back["limits"]))
