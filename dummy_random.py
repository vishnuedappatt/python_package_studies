import random

value=random.random()
print(value)  #float random value  between 0,1
print(float(value)) 

val=random.uniform(1,10)  #for getiing a random float value between 1,10
print(val)


val=random.randint(1,10)
print(val)

words=["gdmrng","gdaftrnon","gdevng","gdngt"]

val=random.choice(words)
print(val)   #getiing a value from the list randomly


val=random.choices(words)
print(val)   #getiing a value from the list randomly in a list  ['gdevng']


val=random.choices(words,k=2)
print(val)   #getiing a value from the list randomly in a list  and getiing multiple result k is 2 then 2 results

words=['red',"blue",'green']
val=random.choices(words ,weights=[30,35,35],k=10)
print(val)   #getiing a value from the list randomly in a list  ['gdevng']

