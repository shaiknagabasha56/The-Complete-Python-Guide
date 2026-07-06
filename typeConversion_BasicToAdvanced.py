#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56


#---------------------BASIC LEVEl-----------------
#TYPE CONVERSION / IMPLICIT CONVERSION
#numeric Tower: bool → int → float → complex

#possible conversions in implicit:-

# bool can implicitly become int, float, or complex
# int can implicitly become float or complex (but never back to bool)
# float can implicitly become complex (but never back to int or bool)
# complex is the final stage — it never converts back to anything

#This is because to prevent the data loss 
#In this no user interference,python automatically converts it.


#1.converting bool to int,float and complex:
"""
x=True
print(x+2,type(x+2))          #converting to int
print(x+99.9,type(x+99.9))    #converting to float
print(x+5j,type(x+5j))         #converting to complex
"""

#2.converting int to float and complex
"""
num1=30
floatConversion=num1+88.6
print(floatConversion,type(floatConversion))
complexConversion=num1+3j
print(complexConversion,type(complexConversion))
"""

#3.trying to convert int to bool
"""
num1=2872
print(num1+True,type(num1+True))    #2872 becomes 2873 type is int only
print(num1-True)
print(num1+False)
print(num1*False)
#so from the above we cant convert int to bool but we can perform arthematic operations.
#True=1 and False=0

print(True+True+True)
print(True/True*False)
print(True-False)
"""

#4.trying to convert float to int and bool:
"""
num1=593.3
#float to int
print(num1+0.7,type(num1+0.7))     #not converted to int but operation is performed.
print(num1-88.6)
print(num1%9.2)
#float to bool
print(num1+True)                   #not converted to bool but operations are performed well
print(num1+False)
print(num1%True)
"""

#5.trying to convert complex to int,float and bool using type conversion:
"""
complexNum=5+2j
print(complexNum)

#complex to int:            #not converted to int but all the basic operations are performing well
print(complexNum+697,type(complexNum+697))   
print(complexNum-522)
print(complexNum*34)
print(complexNum/5)
#complex to float:          #not converted to float but all the basic operations are performing well
print(complexNum+22.9,type(complexNum+22.9))
print(complexNum*45.6)
#complex to bool:           #not converted to bool but all the basic operations are performing well
print(complexNum+True,type(complexNum+True))
print(complexNum/True)
print(complexNum-False)
"""

#Conclusion:
#-> In this method data is converted from small to big but not big to small.this is because to prevent the data loss
#-> Data is converted from bool->int->float->complex but not reverse
#-> True=1 and False=1. and we can also pe#not converted to int but all the basic operations are performing wellrform the operations using True and False.


#-------------------INTERMEDIATE LEVEL-----------------
#TYPE CASTING / EXPLICIT CONVERSION:

#This method, user uses some built-in functions to convert big data to small data.
#data loss is there

#Str can be converted to int,float,bool,list,tuple,set
#int & float can be converted to int,float,str,bool
#bool can be converted to int,float,str
#list/tuple can be converted to str,bool,tuple,set,dic(if key:value pair is there)
#dict can be converted to str,bool,list(keys only),tuple(keys only),sets(keys only)


#6.converting str to int,float,bool,list,tuple and set
"""
myStringNum="100"

#converting to int:
convertedToInt=int(myStringNum)
print(convertedToInt,type(convertedToInt))
#converting to float:
convertedToFloat=float(myStringNum)
print(convertedToFloat,type(convertedToFloat))
#converting to bool:
convertedToBool=bool(myStringNum)
print(convertedToBool,type(convertedToBool))
#converting to list:
list1=list(myStringNum)
print(list1,type(list1))
#converting to tuple:
tuple1=tuple(myStringNum)
print(tuple1,type(tuple1))
#converting to set:
set1=set(myStringNum)
print(set1,type(set1))

#NOTE:-we have to use number strings only to convert str to int,float and bool
"""

#7.converting int to float,str an bool
"""
num1=89
#to float:
convertedToFloat=float(num1)
print(convertedToFloat,type(convertedToFloat))
#to str:
convertedToString=str(num1)
print(convertedToString,type(convertedToString))
#to bool:
convertedToBool=bool(num1)
print(convertedToBool,type(convertedToBool))
"""

#8.converted float to int,str,bool
"""
num1=87.9
#to int:
convertedToInt=int(num1)
print(convertedToInt,type(convertedToInt))
#to str:
convertedToString=str(num1)
print(convertedToString,type(convertedToString))
#to bool:
convertedToBool=bool(num1)
print(convertedToBool,type(convertedToBool))
"""

#9.list can be converted to str,bool,tuple,set,dic(if key:value pair is there)
"""
list1=["nagabasha",200,99.9,"cse"]
#to str:
convertedToString=str(list1)
print(convertedToString,type(convertedToString))
#to bool:
convertedToBool=bool(list1)
print(convertedToBool,type(convertedToBool))
#to tuple:
tuple1=tuple(list1)
print(tuple1,type(tuple1))
#to set:
set1=set(list1)
print(set1,type(set1))

#to dict:iy has multipe options to do this
#using two lists.
keys=["Name","Roll","Branch"]
values=["Nagabasha",46,"CSE"]
myDict=dict(zip(keys,values))
print(myDict,type(myDict))

#using list of lists:
list2=[["id",1],["Name","Nagabasha"],["Branch","CSE"]]
myDict2=dict(list2)
print(myDict2)
"""


#10.tuple can be converted to str,bool,set,dic(if key:value pair is there)
"""
tuple1=("Nagabasha",46,"CSE")

#to string:
convertedToString=str(tuple1)
print(convertedToString,type(convertedToString))
#to bool:
convertedToBool=bool(tuple1)
print(convertedToBool,type(convertedToBool))
#to set:
convertedToSet=set(tuple1)
print(convertedToSet,type(convertedToSet))
#to dict:
tuple2=(("Name","Nagabasha"),("Branch","CSE"))
convertedToDict=dict(tuple2)
print(convertedToDict)
"""


#10.dict can be converted to str,bool,list(keys only),tuple(keys only),sets(keys only)
"""
myDict={"id":1,"Name":"Nagabasha","Branch":"CSE"}

#to string:
convertedToString=str(myDict)
print(convertedToString,type(convertedToString))
#to bool:
convertedToBool=bool(myDict)
print(convertedToBool,type(convertedToBool))
#to tuple:keys only
convertedToTuple=tuple(myDict)
print(convertedToTuple,type(convertedToTuple))
#to sets:keys only
convertedToSets=set(myDict)
print(convertedToSets,type(convertedToSets))
#to list:
convertedToList=list(myDict)
print(convertedToList,type(convertedToList))
"""


#-----------------------ADVANCED---------------------
# 11. BASIC - Explicit casting: int to str (concatenation)
"""
score = 90
print("Score: " + str(score))
"""


#12.bool from different values (truthy/falsy trap)
"""
print(bool(0), bool(1), bool(""), bool("False"), bool([]), bool([0]))
"""

#13.INTERMEDIATE - int base conversion (binary/hex/oct string to int)
"""
binary_str = "1010"
hex_str = "1A"
print(int(binary_str, 2), int(hex_str, 16))
"""

#14.complex number conversion:
"""
x = 5
y = 2.5
z = complex(x, y)
print("12.", z, type(z))
"""

#15.chained casting (str -> float -> int)
"""
raw = "12.75"
final = int(float(raw))
print(final)
"""

#16.casting inside list comprehension:
"""
str_numbers = ["1", "2", "3", "4"]
int_numbers = [int(n) for n in str_numbers]
print(int_numbers, sum(int_numbers))
"""

#17.dict values type casting
"""
raw_data = {"a": "10", "b": "20", "c": "30"}
converted_data = {k: int(v) for k, v in raw_data.items()}
print(converted_data)
"""

# 18.float precision loss with large int
"""
big_num = 10**20
print("18.", float(big_num))  # precision may be lost
"""
