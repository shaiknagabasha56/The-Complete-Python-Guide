#In Python OOP, you have already seen regular methods 
# that use 'self' to talk to an individual object

#@classmethod and @staticmethod are decorators 
#that let you create methods that belong to the entire class itself, rather than a single object.



#Analogy:- compariing the above with the local and global variables:-

# 1.Regular Method (self)  -   Local Scope (Inside a function)       -      Only that one specific object. A change here doesn't affect any other object.
# 2.@classmethod (cls)     -   Global Scope (Inside a module/file)   -      The entire class. A change here instantly changes the behavior for every object made from this class.
# 3.@staticmethod          -   An Independent External Function      -      Anyone, but it doesn't see inside the class or the object. It has its own isolated local scope


#1.@classmethod:-
#A class method takes 'cls' (short for class) as its first argument instead of self. 
#This means it knows about the class it belongs to and can modify things that affect all objects of that class.
#Why do we use it:-
#->To handle Class Variables:To update data that is shared by every single instance
#->Alternative Constructors:To create new objects using different types of inputs


#2.@staticmethod (The Independent Utility Method):
#A static method is completely isolated. 
#It does not take self or cls as an argument. 
#It behaves exactly like a regular, plain Python function,
#but it lives inside the class because it is logically related to what the class does.


#example1:
"""
class Student:
    no_of_students=0

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        Student.no_of_students+=1
    
    def print_info(self):
        print(f"Total students={self.no_of_students}")
        print(f"name={self.name}, marks={self.marks}")
    
    @classmethod
    def change_no_of_students(cls):
        cls.no_of_students=100
    
    @staticmethod
    def pass_grade(grade):
        if grade in ["A","B","C","D","E"]:
             print("pass")

s1=Student("Basha",100)     #normal object declaration 
s1.print_info()             #normal method calling and no.of students=1


s2=Student("Naveen",90)     #here no.of students=2
s2.print_info()

Student.change_no_of_students() #when i call this classmethod, no.of students are resets from 2 to 100 

s3=Student("Siddu",80)      #after calling the above classmethod, now no.of students are 101
s3.print_info()

Student.pass_grade("B")      #calling the static function that dont effect any above functions and this is simply like normal python function but defined inside a class so it is logically relates to the class
"""


#example2:
"""
class BankAccount:
    bank_name="Bank of Basha"
    no_of_customers=0

    def __init__(self,account_num,name,balance):
        self.account_num=account_num
        self.name=name
        self.balance=balance
        BankAccount.no_of_customers+=1

    def show_info(self):
        print(f"Name of the Bank = {BankAccount.bank_name}")
        print(f"Account Number={self.account_num}")
        print(f"Account Holder={self.name}")
        print(f"Available Balance={self.balance}")
        print("---------------------------------------")
    
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    
    @staticmethod
    def bank_info():
        print(f"BANK NAME: {BankAccount.bank_name}")
        print("LOCATION:Ongole,AndhraPradesh")
        print("Owner:Nagabasha")
        print(f"NO.OF CUSTOMERS={BankAccount.no_of_customers}")
        print("CONTACT:9000xxxxxx")
        print("-----------------")

    
a1=BankAccount(98722,"Aditya",20000)
a2=BankAccount(98733,"Manisharma",9678)

a1.show_info()
a2.show_info()

#upto here perfect and obsreve carefully im changing the bank name using classmethod
BankAccount.bank_info() #tells bank name Bank of Basha

BankAccount.change_bank_name("Nagabasha Bank")  #this changes the entire bank name 

BankAccount.bank_info() #tells bank name Nagabasha Bank

a3=BankAccount(98744,"Siddu",765411)
a4=BankAccount(98755,"Surya",89076)

a1.show_info()
a2.show_info()
"""


#one of the important feature of @classmethod is it is used as a constructor.
#By default, a Python class only has one __init__ constructor. 
#But in the real world, data comes in all kinds of formats—like a comma-separated string from a file, 
#a JSON dictionary from the web, or a timestamp from a database.

#An alternative constructor is just a class method that takes that weird data format, 
# cleans it up, and passes it to __init__ to create a brand new object for you.

#ANALOGY:-

#Imagine you are building an app to manage employees. 
#Your standard __init__ constructor expects a name and a role.
#But what if you get employee data formatted as a single hyphenated string like "Basha-Developer"? 
# Instead of splitting that string manually in your main code every single time,
#  you can create a @classmethod to do it cleanly.

#example:
"""
class Employee:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    def show_info(self):
        print(f"NAME={self.name}")
        print(f"ROLE={self.role}")
        print("---------------------")
    
    @classmethod
    def data_format(cls,data):
        name,role = data.split("-")
        return cls(name,role)

e1=Employee("Basha","Developer")   #using normal __init__ constructor
e1.show_info()

#using @classmethod as a constructor for raw data like "name-role"
raw_data="Naveen-Tester"
e2=Employee.data_format(raw_data)#Passing data to the @classmethod constructor
e2.show_info()
"""


