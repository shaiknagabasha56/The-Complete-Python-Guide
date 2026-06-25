#Author:Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56


#--------------------------BASIC LEVEL----------------------------

#1.Simple variable assignment:
"""
myName="Nagabasha"
print(myName)

myAge=20
print(myAge)

Indian=True
print(Indian)

cgpa=9.5
print(cgpa)

num1=100
num2=200
print(f"Addition:-{num1+num2}")
print(f"Subtraction:-{num2-num1}")
print(f"Multiplication:-{num1*num2}")
print(f"Division:-{num2/num1}")
"""

#2.multiple variables and multiple values:
"""
num1,num2,num3 = 100,200,300
#first value assigned to first var
#second value assigned to second var
#third value assigned to third var
print(num1)
print(num2)
print(num3)

#The below line tells, we can write multiple statements in one line using ; and it is not related to multiple variable assignment
number1=10;number2=20;number3=30
print(number1)
print(number2)
print(number3)

device1="Android";device2="Linux";device3="Windows"
print(device1);print(device2);print(device3)
"""

#3.Assigning same value to multiple variables:
"""
num1=num2=num3=100  #100 is assigned to num1, num2, num3 variables
print(num1)
print(num2)
print(num3)

device1=device2=device3="Android"
print(f"device1={device1},device2={device2},device3={device3}")
"""

#4.Checking the type of a variable:means we can check which type of data is stored in a variable like interger type or string type,...
"""
#type() built-in function is used to check what type of data is stored in a variable
port=8080
device="Linux"
compatable=True
latency=9.1

print(type(port))
print(type(device))
print(type(compatable))
print(type(latency))
"""

#5.Reassigning a variable to a different type (dynamic typing)
#if store string type of value in a variable and later we can change it to some other type like integer,boolean,...This is called Dynamic Typing
"""
myName="Nagabasha"  #string type
print(f"My name is {myName} and its type is {type(myName)}")

myName=10101010     #integer type
print(f"My name is {myName} and its type is {type(myName)}")

number1=1000        #integer type
print(f"Number1={number1} and its type is {type(number1)}")

number1=999.9       #float type
print(f"Number1={number1} and its type is {type(number1)}")
"""


#-----------------------INTERMEDIATE LEVEL------------------
#6.swapping two variables:swapping means changing variable1 value to variable2 and variale2 value to variable1
"""
num1,num2=100,200
print(f"Before swapping:-num1={num1} and num2={num2}")

num1,num2=num2,num1
print(f"After swapping:-num1={num1} and num2={num2}")

firstName="Naga"
lastName="Basha"
print(f"Before swapping:-firstname={firstName} and lastname={lastName}")

firstName,lastName=lastName,firstName
print(f"After swapping:-firstname={firstName} and lastname={lastName}")
"""

#7.performing arthematic operations using variables
"""
length=10
breadth=5
area=length * breadth
print(f"Area={area}")

base=10
exponent=2
print(f"10^2={base ** exponent}")

principalAmmount=100000
interest=15000
totalAmmount=principalAmmount+interest
print(f"totalAmmount={totalAmmount}")
"""

#8.Declaring constants in python
#generally python doesnt have constans truely like in the other languages
#we just write variable names in capital letters and assumes it as constant
"""
PI=3.14
print(PI)
print(type(PI))     #returns float but not constant

EULERSNUMBER=2.71828
print(f"EulersNumber={EULERSNUMBER}")

GOLDENRATIO=1.61803
print(f"GoldenRatio={GOLDENRATIO}")

#Generally costant means the value which is assigned to a variable is not changed, if we try to change it we will get error
NUM1=99.99
NUM1+=0.1       #In other programming languages like C / Java we will get error because we trying to modifying constant value
print(NUM1)
#But in python, we dont have true constants,we just assume a variable as constant by writing it in capital letters,thats why we dont get any errors
"""


#13.Using id() to check variable's memory reference
#id() is a built-in function that returns the unique integer
#which is used to identiyfy that the variable is pointing to memory address
#simply,variable is stored in memory and that memory has address the id() used to diaply that address

"""
portNumOfSMTP=25
portNumOfHTTP=80
print(id(portNumOfSMTP))
print(id(portNumOfHTTP))
#both returns diiferent addresses

myName="Nagabasha"
myAge=20
myOperatingSystem="Linux"
myCgpa=9.5

print(id(myName))
print(id(myAge))
print(id(myOperatingSystem))
print(id(myCgpa))
"""


#-------------------Advanced Level-----------------------
#Some concepts are not covered but later the below type of programs are used

#14.Global and Local variables
#Global variables: The variables that can be accessed in anywhere and any block of the program and its lifetime ends when program ends
#Local variables: The variables that can be accessed within a particular block only and its lifetime ends when that block ends

"""
initialValue=1  #Global variable

for i in range(1,6):
    count+=i    #Local variable

print(initialValue)     #accessing global variable without error
#print(count)            #trying to access local variable so im getting error

"""


#15.Multiple variable assignment with unpacking from a list
"""
list1=["Nagabasha",20,9.5]  #list
myName,myAge,myCgpa=list1   

#each value in list is assigned to each variable,this is called unpacking
#the elements in list and no.of variables must be same

print(myName)
print(myAge)
print(myCgpa)

"""

#16.Using * to unpack remaining values into a variable
"""
list1=["Apple","Mango","Banana"]
fruit,*fruits=list1
#First element in list1 goes to first varible
#Remaining all elements in list1 goes to second variable as a list
#Note * must be used

print(fruit)
print(fruits)


devicesList=["Phone","Router","Switch","Hub","Laptop","Computer"]
device1,device2,device3,*devices=devicesList

print(device1)
print(device2)
print(device3)
print(devices)

"""

#18.Using nonlocal keyword in nested functions
"""
def outer():    #outer function
    msg = "Hi"
    def inner():    #inner function/nested function/function in function
        nonlocal msg
        msg = "Hello"   #accessing outer function variable in inner function
    inner()
    print(msg)

outer()

"""

#19.Checking memory size of a variable using sys.getsizeof()
"""
import sys
num1=12345 
print(sys.getsizeof(num1))  

myName="Basha"
print(sys.getsizeof(myName))
"""

#20.Dynamically creating variables using a dictionary (since Python doesn't support true dynamic variable names)
"""
variables = {}      #actually it is empty dictionary,but we assume it as variable declaration 
variables['dynamic_var'] = 50 #actually adding new key-pair into dictionary,but we asssume it as intialization of a variable
print(variables['dynamic_var'])
"""


