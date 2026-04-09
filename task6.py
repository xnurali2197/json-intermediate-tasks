data = {"users":[{"name":"A","active":True},{"name":"B","active":False}]}
print([u["name"] for u in data["users"] if u["active"]])
