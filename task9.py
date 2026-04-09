data = {"students":[{"name":"Ali","scores":{"math":80,"eng":90}}]}

for s in data["students"]:
    avg = sum(s["scores"].values())/len(s["scores"])
    print(s["name"],avg)
