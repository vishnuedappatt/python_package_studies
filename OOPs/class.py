class Person:  
    def __init__(self,name='unknown', age=None):  
        self.name = name  
        self.age = age  

    def display(self):  
        print(self.name,self.age)  
  
c1 = Person("vishnu", 24) 
c2= Person("Anusha",18)
c3=Person()
c1.display()  
c2.display()
c3.display()