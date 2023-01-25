

# old model

# file=open("dummy.txt","r")
# print(file.read())
# file.close()


# with out closing manuely

with open("dummy.txt","r") as p:
    print(p.read(2))