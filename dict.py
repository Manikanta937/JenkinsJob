import requests


res= requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

a=res.json()

for i in range(len(a)):
    print(a[i]["user"]["node_id"])