# a = [1,2,3,9]  
# b= ['a', 'b', 'c']  
# c = list(zip(a,b))  
# print(c)  



# import itertools  
  
# for i in itertools.count(1,1):   #first arg is start and 2nd arg is optional stop or step
#     if i == 50: 
#         break  
#     else:  
#         print(i,end=" ")  



# import itertools  
# temp = 0  
# for i in itertools.cycle("123"):  
#     print(i,end='dd')                  #the 123 will cycle one by one like 1,2,3,1,2,3 ...
#     if temp > 10:  
#         break  
#     else:  
#         print(i,end=' ')  
#         temp = temp+1  






# from itertools import product  
  
# print("We are computing cartesian product using repeat Keyword Argument:")  
# print(list(product([1, 2],[9,0])))  
# print()  
  
# print("We are computing cartesian product of the containers:")  
# print(list(product(['Java', 'T', 'point'], '5','0',[1,0])))  
# print()  
  
# print("We are computing product of the containers:")  
# print(list(product('CD', [4, 5])))  



# from itertools import permutations  
  
# print("Computing all permutation of the following list")  
# print(list(permutations([3,"Python"])))  
# print()  
  
# print("Permutations of following string")  
# print(list(permutations('AB')))  
# print()  
  
# print("Permutation of the given container is:")  
# print(list(permutations(range(4),2)))  





# from itertools import combinations  
# print("Combination of list in sorted order(without replacement)",list(combinations(['B',3],2)))  
# print()  
  
# print("Combination of string in sorted order",list(combinations([1,0,8,9],2)))  
# print()  
  
# print("Combination of list in sorted order",list(combinations(range(20),1)))  




import itertools  
import operator  
  
# initializing list 1  
list1 = [1, 4, 5, 7, 9, 11]  
  
# using accumulate() that will prints the successive summation of elements  
print("The sum is : ", end="")  
print(list(itertools.accumulate(list1)))  
  
# using accumulate() that will prints the successive multiplication of elements  
print("The product is : ", end="")  
print(list(itertools.accumulate(list1, operator.mul)))  
  
  
# using accumulate() that will prints the successive summation of elements  
print("The sum is : ", end="")  
print(list(itertools.accumulate(list1)))  
  
# using accumulate() that will prints the successive multiplication of elements  
print("The product is : ", end="")  
print(list(itertools.accumulate(list1, operator.add)))  