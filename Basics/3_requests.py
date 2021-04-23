import requests

res = requests.get("http://google.com")
res.raise_for_status()
#print("response code :", res.status_code) #200 = normal

#if res.status_code == requests.codes.ok:
#   print("Normal")
#else:
#   print("Error. [Error Code ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w") as f:
    f.write(res.text)