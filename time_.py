# import time

# print(time.time())


# Importing the module  
# import time  
   
# # getting the current time by using ctime function passed with the number of seconds since epoch  
# current = time.ctime(time.time())      # give the time get exact details of the time is unique
# print("Current time: ", current)  




import time  
from datetime import datetime  
  
epoch = time.gmtime()     #give a parameter that corresponding to exact time date will get it
print(epoch.tm_year)  
print(epoch.tm_yday)  
print(epoch.tm_hour)  



# Converting the struct_time object to standard datetime   
print(datetime.fromtimestamp(time.mktime(epoch)))  