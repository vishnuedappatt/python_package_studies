import json


with open("my_dict.json","r") as f:
    json_dict=json.loads(f.read())
print(json_dict["people"][0]["name"])
print(type(json_dict))