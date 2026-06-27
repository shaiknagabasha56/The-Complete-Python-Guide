#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56

#----------------BASIC LEVEL---------------------------
#1.Arthemeatic operations:
"""
num1=100
num2=200
print(f"Addition of {num1} and {num2}={num1+num2}")
print(f"Subtraction of {num1} and {num2}={num2-num1}")
print(f"Multiplication of {num1} and {num2}={num1*num2}")
print(f"Division of {num1} and {num2}={num2/num1}")
print(f"Floor Division of {num1} and {num2}={num2//num1}")
print(f"Modulus of {num1} and {num2}={num1%num2}")
print(f"powerof  of {2} ^ {3}={2**3}")

#concatenation(adding) of two strings:
print("Naga"+"basha")
#repetetion of a string using *
print("Nagabasha "*3)
myname="Nagabasha"
print("Hello" + myname + ", How are you ?")
"""

#2.Comparison Operators:
"""
num1=100
num2=200
print(f"{num1}=={num2}?: {num1==num2}")
print(f"{num1}!={num2}?: {num1!=num2}")
print(f"{num1}>{num2}?: {num1>num2}")
print(f"{num1}<{num2}?: {num1<num2}")
print(f"{num1}>={num2}?: {num1>=num2}")
print(f"{num1}<={num2}?: {num1<=num2}")

#comparing strings
string1="Nagabasha"
string2="nagabasha"
print(f"{string1}=={string2}?: {string1==string2}")
print(f"{string1}!={string2}?: {string1!=string2}")
print(f"{string1}>{string2}?: {string1>string2}")
print(f"{string1}<{string2}?: {string1<string2}")
print(f"{string1}>={string2}?: {string1>=string2}")
print(f"{string1}<={string2}?: {string1<=string2}")
"""

#3.Assignment Operators:
"""
num1=100
num1+=20
print(num1)
num1-=90
print(num1)
num1*=5
print(num1)
num1/=10
print(num1)
num1//=6
print(num1)
"""

#4.Logical operators:
"""
num1=100
print(num1>=50 and num1<=500)
print(num1>=500 or num1<=100 )
print(not(num1==100))

#Note:-
# and: Returns the first empty string, or the last string if both are non-empty.
# or: Returns the first non-empty string, or the last empty string if both are empty.
# not: Always returns a boolean (True or False)

print("" and "Nagabasha")   #it has one empty string, so it returns that empty strig
print("Nagabasha" and "")   #it has one empty string, so it returns that empty strig
print("Nagabasha" and "Basha")  #it has no empty strings, so it returns second string 
print("Nagabasha" or "Basha")   #no empty strings are there, so it returns the first string 
print("" or "Nagabasha" )    #contains one empty string only , so it returns non-empty string
print("Nagabasha" or "") #contains one empty string only, so it returns non-empty string
print("" or "") #contains two empty strings, it returns second non-empty string
print(not("Nagabasha"))
"""


#5.membership orperators:
"""
list1=[1,2,"Apple",3,"Mango"]
print(1 in list1)
print("Mango" in list1)
print(3 not in list1)
print("Apple" not in list1)

print("basha" in "Nagabasha")
print("B" not in "Nagabasha")

tuple1=(401,"Android","Computer",400)
print(tuple1)
"""

#6.Identity Operators:
"""
myName="Nagabasha"
temp_var=myName

#Both are pointing to same address
print(id(myName))
print(id(temp_var))

#check:
print(myName is temp_var)
print(myName is not temp_var)
"""

#------------------INTERMEDIATE LEVEL-------------
#7.Bitwise and/or/xor
"""
num1=1
num2=2
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)

#print("A" & "B") #raises error because, bitwise operators wont support strings
"""

#8.Bitwise not and shift operators
"""
num1=5
print(f"5 << 1 : {num1 << 1}")
print(f"5 >> 2 : {num1 >> 2}")
print(~4)  #inverting the bits
"""

#9.Operator precedence:
"""
result = 10 + 2 * 3 ** 2 - (4 / 2)
# Order: ** first, then *, then + and - left to right
print("Result of 10 + 2 * 3**2 - (4/2):", result)
print("-" * 40)
 
print(10*20/2+100)
print(100/20/20)
print(10-90/20*5)
"""

#10.Ternary Operator:it is nothing but a shorthand of if-else 
#if -else syntax is: 
# if(condition):
#   //statements
#else:
#   //statements
#But, whenever we have only single statement we simply use ternary operator to reduce the if-else steps and write it in single line

#Syntax: true statement if(condition) else false statement
#true statement executes when the condition is True
#if condition is False false statement will be executed

"""
print("100 is Greater than 50" if(100>50) else "50 is Greater than 100")

marks=90
status="Pass" if(marks>=30) else "Fail"
print(status)
"""


#11.Walrus Operator
# The walrus operator (:=) in Python officially called the assignment expression operator, allows you to assign a value to a variable inside an expression.
# Introduced in Python 3.8,
# it gets its nickname because the symbol := resembles the eyes and tusks of a sideways walrus.
# Why Use It?
# Reduces repetition: Saves you from running the same function or calculation multiple times.
# Shortens code: Combines assignment and evaluation into a single line.
# Improves performance: Keeps code efficient by storing reusable values on the fly.

# Simply,Assigns and checks in the same expression

"""
numbers=[1,2,3,4,5,6,7,8,9,10]
filtered=[y for x in numbers if (y:=x*2)>8 ]
print(filtered)
"""

#Explanation:
#first focus on "for x in numbers"
#This means each value in numbers(list) like 1,2,3,4,5,6,7,8,9,10
#Then it checks condition (y:=x*2)>8 which means (y=x*2)>8 for each value in list
#Then if condtion is True y value is stored in list(filtered)

#Tracing:-
#1 will come and checks (y=1*2)>8 condition false,so not included in filtered list
#2 will come and checks (y=2*2)>8 condition false,so not included in filtered list 
#3 will come and checks (y=3*2)>8 condition false,so not included in filtered list 
#4 will come and checks (y=4*2)>8 condition false,so not included in filtered list 
#5 will come and checks (y=5*2)>8 condition True,so it is included in filtered list 
#6 will come and checks (y=6*2)>8 condition True,so it is included in filtered list 
#7 will come and checks (y=7*2)>8 condition True,so it is included in filtered list 
#8 will come and checks (y=8*2)>8 condition True,so it is included in filtered list 
#9 will come and checks (y=9*2)>8 condition True,so it is included in filtered list 
#10 will come and checks (y=10*2)>8 condition True,so it is included in filtered list 

#Final filtered name list is [10,12,14,16,18,20]


#-----------------------ADVANCED-------------------
#Some topics are not covered, but the below are useful for later

#12.list operations: + and *
"""
list1=[1,2,3]
list2=[4,5,6]

print(list1+list2)  #combines elemnts of two lists and returns combined list
print(list1*2)      #repeats the elements iof 
"""

#13.swapping two variables using XOR trick
#asked in interviews also
"""
m = 6
k = 9
m = m ^ k
k = m ^ k
m = m ^ k
print("After XOR swap -> m:", m, ", k:", k)
print("-" * 40)

=> Xor (^) means, if two bits are different then result is 1 else 0

step1: m = m ^ k
=>m becomes 6 ^ 9 
=>In binary: m = 0110, k = 1001₂.
=>0110 ^ 1001 = 1111 (which is 15 in decimal).
=>Result: m is now 15. k is still 9.

step2: k=m ^ k
=>k becomes 15 ^ 9
=>1111 ^ 1001 = 0110 (which is 6 in decimal).
=>Result:k is 6 now.m is still 15

step3: m=m^k
=>m becomes 15 ^ 6
=>1111 ^ 0110 = 1001
=>Result: m is now 9 and k is 6 

#swapped two values successfully.
"""

#14.Even or Odd number check using bitwise AND
#asked in interviews also
# It is a faster
# low-level alternative to using the modulo operator (num1 % 2 == 0)

"""
num1=2

if num1 & 1 == 0:
    print("Even number")
else:
    print("Odd number")
"""

#Explanation:
#In the binary system (base 2)
#Every number is represented by bits (0s and 1s)
#Even numbers always end with a 0
#Odd numbers always end with a 1

#for example:
#4 in binary is 0100 (Ends in 0 → Even)
#5 in binary is 0101 (Ends in 1 → Odd)
#6 in binary is 0110 (Ends in 0 → Even)
#7 in binary is 0111 (Ends in 1 → Odd)

#When you perform num1 & 1, you are comparing num1 against the number 1 (which in binary is 0001).
#Because all the leading bits of 1 are 0, the & operation ignores every bit in num1 except for the very last one


#15.Powers of 2 using Left Shift
"""
print(2**2) #2^2=4
print(1<<2) #alternative of above
print(1<<3) #equivalent to 2^3
"""

