from collections import Counter

words="aaaffffffffaaeeed"

check=Counter(words)
print(check)
print(check['a']) # get the values count as per the input give a dictionary as the out put



print(check.most_common(1))  # get most common value give in the input giving as a duple inside a list


print(check.most_common(1)[0])  # get the first value inside the list


print(check.most_common(2)[1][0])  # here is we get most two elements in the give input and we will take the second element in that list and get that value 

print(check.most_common(2)[1][1]) # here we take the 2nd most element has how much amount of count presented it.