import json
f = open("sojson.com.json", "r")
xx = json.loads(f.read())
print(xx)