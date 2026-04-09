import json

with open("products.json") as f:
    data = json.load(f)

top3 = sorted(data,key=lambda x:x["price"],reverse=True)[:3]
print(top3)
