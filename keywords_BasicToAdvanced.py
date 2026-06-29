#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56

#-------------------BASIC LEVEL--------------------------
#Some topics are not covered but covered later

#1.program for demonstrating boolean keywords:
#Boolean keywords=True & False
"""
isDownloaded=False
print(isUploaded)
print(isDownloaded)

#Tip:we can write above sentences in one line alos:
print(isUploaded);print(isDownloaded)
#Not only above statements, we can write multiple statements in one line by using ; sem-colon
"""

#2.demonstrating None Keyword:
"""
ipAddress=None
dataleft=None
print(ipAddress)
print(dataleft)
"""

#3.basic if-else keywords using a simple condition:
"""
age =20
if(age>=18):    #if block executes when the condition is True,In this case it is True because 20 >= 18
    print("Eligible to Vote")
else:           #else block is executed when the if condition is False
    print("Not Eligible to Vote")
"""

#4.basic if-elif-else keywords using simple conditions:
"""
marks=74
if marks>=90:               #If block is executed when the condition is True
    print("A-grade")
elif marks>=75:             #this elif block is executed when the above if condition id False and this elif condition is True
    print("B-grade")
elif marks>=50:             #this elif block is executed when the above else block and if block condtions are False and this elif block condition is True
    print("C-grade")
elif marks>=35:             #this elif block is executed when the above all blocks condition is False and this elif block condition is True
    print("D-grade")
else:                       #this else block is executed when the above all the conditions are False
    print("fail")       
"""

#5.for and in keywords demonstration with a simple program:
"""
fruits=["Apple","Mango","Banana","Papaya"]

for fruit in fruits:        #this loop will iterate over above fruits list and prints the all the fruits in it on by one
    print(fruit,end=" ")
print("\n")
"""


#-------------------------INTERMEDIATE LEVEL------------------


#6.while and break keywords demonstration:
"""
count=0
while(True):
    print(count)
    if count==3:        #whenever the count value is 3, then the loop is terminated(stopped)
        break   
    count+=1
"""

#7.for and continue keywords demonstration:
"""
for i in range(1,11):
    if(i==5):       #whenver the i value is 5,then that value is skipped and loop goes to next iteration
        continue
    print(i)
"""

#8.and / or / not keywords demonstration:
"""
username="Nagabasha"
password="0ab1c2d3e4"

if username=="Nagabasha" and password=="0ab1c2d3e4":
    print(f"Welcome back to website {username}")
elif username=="Nagabasha" or not(password=="0ab1c2d3e4"):
    print("username is valid, but password is not valid")
else:
    print("username and password incorrect")
"""

#9.is and is not keywords demonstration:
"""
x=100
y=x

if x is y:
    print("Both x and y are pointing to same address")
elif x is not y:
    print("Both x and y are not pointing to same address")
else:
    print("Invalid")
"""

#-------------------------ADVANCED LEVEL------------------------


#10.def keyoword demonstration
#def is a keyword used to create a function
"""
def sumOfTwoNums(num1,num2):        #defining a function with two parameters
    print(f"Sum={num1+num2}")

number1=100
number2=200
sumOfTwoNums(number1,number2)       #calling a functon with two arguments
"""


#11.demontrating pass keyword in a function:
"""
def featureUnderConstruction(): #function is created but
    pass                      #here i have given pass, which means function is constructed and implemented later

featureUnderConstruction()    #calling the above function.

"""

#12.try,except and finally block demonstration:
"""
try:
    num1=int("abc") #this statement is wrong, and this will raise error
except ValueError:
    print("caught an error, string to integer conversion is failed")    #this block will displays the error
finally:
    print("This block will be executed always, even the error raises or not")
"""


#13.import and as keywords demonstration:
"""
import math as m
#import is used to bring math module to this program and use math functions
#as is used to alias the math.means, instead of using math.sqrt() we simply use m.sqrt()

num1=9
print(m.sqrt(num1))
"""

#14.checking the total no.of keywords:
"""
import keyword
print(len(keyword.kwlist))
"""

#15.displaying all the keywords:
"""
import keyword
print(keyword.kwlist)
"""


#16.checking if specific words are keywords or not:
"""
import keyword
print(keyword.iskeyword("if"))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("def"))
print(keyword.iskeyword("print"))
print(keyword.iskeyword("variable"))
"""
