from collections import namedtuple



Name=namedtuple('Value',"x,y")

pt=Name(1,0)   # the out put is get by the class Value and the elemts inside is x,y
print(pt.x)    # geting the value directly via calling with .
print(pt.y)
pt=Name(4,4,)
print(pt)   