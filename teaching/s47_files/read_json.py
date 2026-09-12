import json

with open("config.json") as f:
    cfg = json.load(f)

print(type(cfg))
print(cfg["hz"], type(cfg["hz"]))
print(cfg["safe"], cfg["note"])
print(cfg["joints"][1]["limit"])
