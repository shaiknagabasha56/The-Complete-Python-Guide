#1.declaring an empty class declaration:-

# class MyClass:
#     pass

#2.declaring an empty class with onbject declaration:-
"""
class MyClass:
    pass

obj1=MyClass()
obj2=MyClass()
"""


#example:
"""
class Experiment:
    pass

exp1=Experiment()
exp2=Experiment()
exp3=Experiment()
"""


#3.__init__ : it is a constructor used to call the method automatically when the object is declared.
"""
class MyClass:
    def __init__():
        pass

class1=MyClass()
class2=MyClass()
"""

#example1:calling the constructor automatically and printing the value automatically
""""
class Student:
    def __init__(self,roll,name,marks):
        print(name,roll,marks)
s1=Student(100,"Basha",9.5)
"""

#example2:calling the constructor automatically and printing the values manually.
"""
class Experiment:
    def __init__(self,exp_num,exp_name):
        self.experiment_number =exp_num
        self.experiment_name=exp_name

exp1=Experiment(1,"Ohms Law")
exp2=Experiment(2,"Kirchoffs Law")

print(f"Experiment details: {exp1.experiment_number} {exp1.experiment_name}")
print(f"Experiment details: {exp2.experiment_number} {exp2.experiment_name}")
"""

#4.using two methods to calculate the area & Perimeter of a Rectangle:
#by using __init__ the values like self.len,self.bredth can be used in all methods.
"""
class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        print(f"Ara of Rectangle = {self.length * self.breadth}")

    def calculate_perimeter(self):
        print(f"perimeter of Rectangle ={2 * (self.length + self.breadth)}")
        #we have to use () brackets for 2*(len+bre) 

rectangle1=Area(10,5)
rectangle2=Area(200,90)
rectangle3=Area(110,67)

rectangle1.calculate_area()
rectangle1.calculate_perimeter()

rectangle2.calculate_area()
rectangle2.calculate_perimeter()

rectangle3.calculate_area()
rectangle3.calculate_perimeter()
"""

#5.calculating the area and perimeter of a rectangle without using the __init__ constructor:-
#here,lenth and breadth are limited to that specific method only, if we want to use in anothr method we again have to pass them.
"""
class Rectangle():
    def calculate_area(self,length,breadth):
        print(f"area of rectangle = {length * breadth }")   

    def caluculate_perimeter(self,length,breadth):
        print(f"Perimeter of rectangle = { 2 * (length + breadth) }")

rectangle1=Rectangle()
rectangle2=Rectangle()

rectangle1.calculate_area(10,5)
rectangle1.caluculate_perimeter(10,5)

rectangle1.calculate_area(100,50)
rectangle1.caluculate_perimeter(100,50)
"""


#6. __str__ and __repr__ (special/magic/dunder methods):
"""
class MyClass:
    pass

class1=MyClass()
class2=MyClass()

#the below prints the object location/address and that is not understandable by the normal users so, instead of displayig like this we use __str__ and __repr__ methods to display something understandable to the users.
print(class1)
print(class2)
"""


# That above output is completely useless to a human, 
# and it doesn't help you debug your code either. 
# To fix this, Python gives us __str__ and __repr__.

#1. __str__ (Short for "String")
# Purpose: To give a friendly, readable summary for regular humans.
# When is it triggered? Automatically when you use print(s1) or str(s1).
# What it should return: A nice sentence.
# Example: "Student Basha is in grade A"

#2. __repr__ (Short for "Representation")
# Purpose: To give a detailed, exact representation for you (the programmer) when debugging.
# When is it triggered? When you look at code in the Python console, or when your objects are hidden inside a list or dictionary.
# What it should return: Text that looks exactly like the Python code used to create the object.
# Example: "Student(name='Basha', grade='A')"


#example:
"""
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def __str__(self):
        return f"User have {self.brand} {self.color} car"
    
    def __repr__(self):
        return f"Car(brand='{self.brand}',color='{self.color}')"

car1=Car("Toyato","red")
car2=Car("BMW","black")
#print(car1,car2)    #displays addres that is not understandable if we dont use __str__ or __repr__ methods

print(car1)
print(car2)

print(repr(car1))
print(repr(car2))
print([car1])   #if write object in under list [] , python automatically calls the __repr__ method


#What happens if we put students in a list? 
# Python uses __repr__ here so developers can inspect the list contents clearly!
cars=[Car("Audi","white"),Car("Benz","Black")]
print(cars)
"""

#NOTE:-
#Methods should RETURN values, not just print them
# Printing inside a method locks that value inside the method.
# Returning lets you reuse, store, compare, or test the result.
"""
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def show_info(self):
        return f"Brand={self.brand} and color={self.color}"

c1=Car("BMW","Black")
c2=Car("Audi","White")

c1_info=c1.show_info()
print(c1_info)

c2_info=c2.show_info()
print(c2_info)
"""

#NOTE:-
#A method calling ANOTHER method on the same object
# Real classes build up complex behavior from small reusable pieces
"""
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calculate_area(self):
        return self.length * self.breadth
    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)
    def show_info(self):
        area=self.calculate_area()  #calling the other methods inside a method
        perimeter=self.calculate_perimeter()  
        return f"AREA={area} and PERIMETER={perimeter}"
rec1=Rectangle(10,5)
print(rec1.show_info()) #it not only gives expected output but also gives additional info because this method reused other methods
"""


#example:
class Student:
    school_name="RGUKT"
    total_no_of_students=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.total_no_of_students+=1
    def show_info(self):
        return f"SCHOOL NAME:{Student.school_name}\nNAME:{self.name}\nMARKS:{self.marks}\n-----------------------"
    
s1=Student("Basha",100)
print(s1.show_info())

s2=Student("Naveen",90)
print(s2.show_info())
    