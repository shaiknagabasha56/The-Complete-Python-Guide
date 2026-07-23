# Encapsulation means: hide the internal data, 
# expose only controlled ways to read/write it, 
# so invalid states get rejected before they happen.

# encapsulation is the practice of bundling data (variables) and the methods (functions) 
# that act on that data into a single unit—a class.

# Python doesn't enforce true privacy like Java/C++. 
# It signals intent through underscores:

# ANALOGY::-
# Think of it like a capsule of medicine; 
# the outer shell protects the contents inside 
# and only lets them interact with your body in a controlled way.

# In python we dont restrict or hide the access like in other languages.
# But we achieve this restriction using a naming convention with underscores

# 1.PUBLIC MEMBERS(Accessible everywhere):
# By default, every variable and method you create in a Python class is public. 
# Anyone can read or change them from outside the class.

#example:
"""
class Employee:
    def __init__(self,name,salary): 
        self.name=name  #public variable
        self.salary=salary  #public variable

emp1=Employee("Manisharma",100000)
print(emp1.name)    
print(emp1.salary)  #anybody can access it

emp1.salary-=20000  #anybody can modify it

print(emp1.salary)
"""


# 2.Protected Members (A Gentle Warning):
# If you prefix a variable name with a single underscore (like _salary), 
# you are telling other programmers, 
# "Hey, this is internal. 
# Please don't touch it outside this class or its subclasses."

# Note: Python doesn't actually enforce privacy here.
# It's a gentleman's agreement. You can still technically access it, but you shouldn't.

#example:
"""
class Employee:
    def __init__(self,name,salary):
        self._name=name     #protected attribute
        self._salary=salary #protected attribute
emp1=Employee("Manisharma",100000)
print(emp1._name)   #we have accessed the protected attributes
print(emp1._salary)
"""
# Technically possible, but bad practice:


# Private Members (Strict Enforcement):
# To truly hide data, prefix the variable name with a double underscore (like __salary). 
# Python will actively block direct access from outside the class.

#example:
"""
class Employees:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
emp1=Employees("Manisharma",100000)
#print(emp1.__name)  #this raises attribute error
#print(emp1.__salary) #this raises attribute error

#NOTE: __name isn't truly hidden — Python renames it internally to _Employee__name
#NOTE: __salary isn't truly hidden — Python renames it internally to _Employee__salary
#we can access using  emp1._Employee__name and emp1._Employee__salary

print(emp1._Employees__name)    #we can access them
print(emp1._Employees__salary)  
emp1._Employees__salary-=20000
print(emp1._Employees__salary)  #we can also even modify it
"""

#NOTE:
# To see or modify this hidden data,
# we use controlled methods called Getters (to read) and Setters (to write).
# This lets you add rules or validation before data is changed.

#example:real world
"""
class ShoppingCart:
    def __init__(self,name):
        self.customerName=name
        self.__items={} #created a dictionary for cart items
        self.__total=0.0
    
    def get_items(self):        #getter
        return self.__items
    def get_total(self):        #getter
        return self.__total

    def add_item(self,name,price):  #setter
        self.__items[name]=price
        self.__total+=price

myCart=ShoppingCart("Basha")
myCart.add_item("Nothing-Earbuds",4500)
myCart.add_item("Fastrack-Watch",2500)

print(myCart.get_items())
print(myCart.get_total())
"""

#example:
"""
class UserAccount:
    def __init__(self,name,password):
        self.name=name
        self.__password=self.hashed(password)

    def hashed(self,password):
        return f"ABC{password}ABC"
    
    def login(self,name,passwd):
        if name==self.name:
            
            if self.hashed(passwd)==self.__password:
                return f"Login Success"
            else:
                return "Incorrect password"
        else:
            return "Incorrect name"

user=UserAccount("Nagabasha","Naga")
print(user.login("Nagabasha","Naga123"))
print(user.login("Nagabasha","Naga"))
"""


#NOTE:upto now we have used the old style getters and setters to read and modify the private attribute values
#modern style is @property - for getter and  @x.setter - for setter
#GOLDEN RULE: The getter and the setter must have the exact same method name.
#That name becomes the clean "public" variable name you use outside the class.

#@property turns a method into a Getter
"""
class User:
    def __init__(self,name,age):
        self.name=name
        self.__age=age   #private attribute,cant access directly.
    
    #Getter
    @property
    def age(self):
        return self.__age
    
    #Setter
    @age.setter
    def age(self,new_age):
        self.__age=new_age

u1=User("Nagabasha",20)
print(u1.age)   #automatically calls the getter
u1.age=21       #automatically calls the setter
print(u1.age)
"""
#we cannot use the different method names for getters and setters using @property and @x.setter.
#if you want to use like that, then you have to go for manual getters and setters method
"""
class DigitalMoneyExchange:
    def __init__(self,name,inr):
        self.name=name
        self.__inr=inr
        self.__usd=0
        self.__to_usd_rate=90
    @property
    def money(self):
        return f"INR={self.__inr} and USD={self.__usd}"
    @money.setter
    def money(self,usd):
        exchange=usd * self.__to_usd_rate
        if exchange<=self.__inr:
            self.__usd=exchange
            self.__inr-=self.__usd
        else:
            raise ValueError("not enough money")
    
u1=DigitalMoneyExchange("Nagabasha",1000)
print(u1.money)
u1.money=10
print(u1.money)
"""

#example:
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @property
    def marks(self):
        return f"NAME:{self.name}|MARKS:{self.__marks}"
    @marks.setter
    def marks(self,new_marks):
        if not isinstance(new_marks,(int,float)):
            raise TypeError(f"Marks must be a number,got {type(new_marks).__name__}")
        if not (0<=new_marks<=100):
            raise ValueError(f"marks must be between 0 and 100, got {new_marks}")
        self.__marks=new_marks
s1=Student("Nagabasha",100)
print(s1.marks)
s1.marks=99
print(s1.marks)
#s1.marks=999 #raises error when print the s1.marks





