import json
with open("vehicle.json", "w") as f:
    data = json.load(f)
data.update({"category": "bike"})
    json.dump(data,f)
    
