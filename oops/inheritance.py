#Aquiring parent features like attributes and methods to child is called inheritance

#example:Basic inheritance
"""
class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        return f"{self.name} eats well"
    def sleep(self):
        return f"{self.name} sleeps well"

class Dog(Animal):
    def barks(self):
        return f"{self.name} barks well"

d1=Dog("Puppy")
print(d1.name)
print(d1.eat())
print(d1.sleep())
print(d1.barks()) 
"""

#NOTE:
# Dog never wrote __init__, eat(), or sleep() 
# It got them for free from Animal. 
# Dog only added what's genuinely new (bark).


#super() function
#In Python, super() is a built-in function 
#used to gain access to the methods and properties of a parent (or sibling) class.
#ANOLOGY:-
#lets assume, 10 attributes and 5 methods are present in the parent class,
#The same attributes with extra 2 attributes are required for child class
#Normally, what we should do, we again write 12 attributes in the child class
#But,super() function helps to reduce this, if we use super() function,
#All the above 10 attributes are defined here exactly like in the above parent class but its in a single line instead of 10 lines
#And then we simply, define remaining 2 attributes in child class
#Simply,it takes only 3 lines instead of 12 lines.

#example:
"""
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_info(self):
        return f"NAME:{self.name} | SALARY:{self.salary}"

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)   #this brings above parent class attributes declaration
        self.department=department
    def show_Info(self):
        return f"{super().show_info()} | DEPARTMENT:{self.department}"

m1=Manager("Nagabasha",100000,"IT")
print(m1.show_Info())
print(m1.show_info())
"""

#TYPES OF INHERITANCE:
#In Python, there are five main types of inheritance. 
#The type depends on how many parent classes a child has, and how deep the family tree goes.

#1.Single Inheritance:-
#A child class inherits from one single parent class. 
#This is the simplest and most common form of inheritance.
#example:
"""
class Device:
    def power_on(self):
        return "Device is powerd on"
class Laptop(Device):
    def boot_os(self):
        return "Booting the Operating System"
myLaptop=Laptop()
print(myLaptop.power_on())
print(myLaptop.boot_os())
"""

#2.Multiple Inheritance:-
#A child class inherits directly from more than one parent class. 
#This allows the child to combine features from different places.
"""
class Land:
    def onLand(self):
        return "Lives on Land"
class Water:
    def water(self):
        return "Lives under Water"
class Frog(Land,Water):
    def sound(self):
        return "croak...croak..."
f=Frog()
print(f.onLand())
print(f.water())
print(f.sound())
"""


#3.Multilevel Inheritance
#A child class inherits from a parent class, 
#which in turn inherits from another parent class. 
#It forms a vertical chain (like Grandparent -> Parent -> Child).
#example:
"""
class School:
    def primary(self):
        return "School:Primary Education"
class College(School):
    def secondary(self):
        return "College:Secondary Education"
class University(College):
    def higher(self):
        return "University:Higher Education"

student=University()
print(student.primary())
print(student.secondary())
print(student.higher())
"""


#4.Hierarchical Inheritance:-
#Multiple child classes inherit from the same single parent class. 
#Think of it as siblings sharing the same parent.
#example:
'''
class Shape:
    def info(self):
        return "A 2-Dimensional shape"
class Circle(Shape):
    def circle_diagram(self):
        return """  
  . . . . . . . 
 .               .
.                 .
.                 .
 .               .
   . . . . . . . 
"""
class Square(Shape):
    def square_diagram(self):
        return """
┌─────────┐
│    •    │
└─────────┘
"""

c=Circle()
s=Square()
print(c.info())
print(c.circle_diagram())
print(s.info())
print(s.square_diagram())
'''

#5.Hybrid Inheritance:-
#Hybrid inheritance is a combination of two or more types of inheritance mentioned above.
#example:
"""
# Base Parent Class
class SchoolMember:
    def introduce(self):
        return "I belong to this school."

# Hierarchical split: Student and Teacher both inherit from SchoolMember
class Student(SchoolMember):
    def study(self):
        return "Studying for exams."

class Teacher(SchoolMember):
    def teach(self):
        return "Grading assignments."

# Multiple inheritance: TA inherits from BOTH Student and Teacher
class TeachingAssistant(Student, Teacher):
    def assist(self):
        return "Helping the professor."

# Testing
ta = TeachingAssistant()
print(ta.introduce()) 
print(ta.study())     
print(ta.teach())     
print(ta.assist())    
"""

#METHOD OVERRIDING:
#Method overriding happens when a child class provides 
#its own specific implementation of a method that is already defined in its parent class.
#rules: 
# same method name,
# same parameters,
# inheritance required


#*****WITHOUT OVERIDING*******:-
#Assume two classes are there one is parent class and another is child class
#If parente is inherited to child and both contains same method name with same parameters
#when we call the child method, intead of executing the child method python executes the parent method.
"""
class StandardShipping:
    def calculate_delivery_days(self,distance_in_km):
        #lets assume for 800km it takes one day
        days=distance_in_km/800
        return days
class ExpressShipping(StandardShipping):
    def calculate_delivery_days(self):
        #delivers next day only,means 1 day.
        return 1
d1=StandardShipping()
days1=d1.calculate_delivery_days(2400)
print(f"No.of days={days1}")


d2=ExpressShipping()
days2=d2.calculate_delivery_days(3000)
print(f"No.of days={days2}")
"""
#in the above i have not used the same parameters,
#even though i called the child function,python is executing the above parent function only.


#*********WITH OVERRIDING********:-
class StandardShipping:
    def calculate_delivery_days(self,distance_in_km):
        #lets assume for 800km it takes one day
        days=distance_in_km/800
        return days
class ExpressShipping(StandardShipping):
    def calculate_delivery_days(self,distance_in_km):
        #delivers next day only,means 1 day.
        return 1
d1=StandardShipping()
days1=d1.calculate_delivery_days(2400)
print(f"No.of days={days1}")

d2=ExpressShipping()
days2=d2.calculate_delivery_days(2400)
print(f"No.of days={days2}")

#in the above, i have used same method name and same parameters
#but,now method is overriden because, this python is not executed the parent class method
#python executed chid class method only. this is method overriding.

#in method overriding child class says:
#if anyone calls this method name on me, use my code, 
#and ignore my parent's code entirely!"

