import json

my_dict={
   "people": [ 
    {
    "name":"anu","age":18,
    },
    {"name":"viz","age":24,}
    ]
}

print(my_dict)
json_string=json.dumps(my_dict,indent=3)
print(json_string,'fgf')
print(type(json_string))
with open("my_dict.json","w+") as f:
    f.write(json_string)
    print(f.read())
# print(dir(json))