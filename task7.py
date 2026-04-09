import json

name = input()
age = int(input())
city = input()

with open("user.json","w") as f:
    json.dump({"name":name,"age":age,"city":city},f,indent=4)
