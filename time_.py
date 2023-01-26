# import time

# print(time.time())


# Importing the module  
# import time  
   
# # getting the current time by using ctime function passed with the number of seconds since epoch  
# current = time.ctime(time.time())      # give the time get exact details of the time is unique
# print("Current time: ", current)  




# import time  
# from datetime import datetime  
  
# epoch = time.gmtime()     #give a parameter that corresponding to exact time date will get it
# print(epoch.tm_year)  
# print(epoch.tm_yday)  
# print(epoch.tm_hour)  



# # Converting the struct_time object to standard datetime   
# print(datetime.fromtimestamp(time.mktime(epoch)))



# # Importing the time module  
# import time  
# b = time.ctime()  
# print(b)  
# for i in range(5):  
      
#     # using the sleep() function to halt the execution  
#     time.sleep(1)   
#     print(i*2)  
# e = time.ctime()  
# print(e)  








# # Python program to get the local time   
# # importing the time module  
# import time  
# from datetime import datetime  
   
# # This function will convert the current time represented in seconds that have passed since the epoch to a struct_time object in Local time  
# current = time.localtime( time.time() )  
# tiems=time.gmtime()
# print(tiems)
   
# print(current)  
  
# # Converting the struct_time object to standard datetime   
# print(datetime.fromtimestamp(time.mktime(current)))  







# import time;    
    
# #returns a time tuple     
    
# print(time.localtime(time.time()))    
  
# print(time.asctime(time.localtime(time.time())))  



import datetime  
#returns the current datetime object     
print(datetime.datetime.now())



import datetime    
#returns the datetime object for the specified date    
print(datetime.datetime(2020,4,4))    




import calendar;    
cal = calendar.month(2023,2)    
#printing the calendar of December 2018    
print(cal)    


import calendar    
#printing the calendar of the year 2019    
s = calendar.prcal(2023)  