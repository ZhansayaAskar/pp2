import json


with open("lab4/sample-data.json") as f:
    data = json.load(f)


print("Interface Status")
print("=" * 79)
print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<6}")
print("-" * 50, "-" * 20, "-" * 6, "-" * 6)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr["dn"]
    descr = attr["descr"]
    speed = attr["speed"]
    mtu = attr["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<6} {mtu:<6}")
