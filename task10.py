import json

class P:
    def __init__(self,n,p,q):
        self.n=n; self.p=p; self.q=q

data=[P("A",1,2).__dict__]

with open("p.json","w") as f:
    json.dump(data,f)
