#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56

#---------------------------------------------------------------
#1.Write a loop that prints numbers from 1 to 10
"""
for i in range(1,11):
    print(i,end=" ")
print("\n")


print("with while loop:")
j=1
while j<=10:
    print(j,end=" ")
    j+=1
print("\n")
"""

#2.Print all even numbers between 1 and 20
"""
#using for loop:
for i in range(1,21):
    if i % 2 == 0:
        print(i,end=" ")
print("\n")
#using while loop:
j=1
while j<=20:
    if j % 2 == 0:
        print(j,end=" ")
    j+=1
print("\n")

#another method to find the even or odd numbers:mostly asked in interview questions(i have already did this method in previous concepts)
for k in range(1,21):
    if (k & 1) == 0:
        print(k,end=" ")
print("\n")
"""

#3.sum of digits: example:123=1+2+3=6
"""
num1=int(input("enter a number:"))
sum=0

while num1 > 0:
    digit=num1%10
    sum+=digit
    num1=num1//10    
print(sum)
"""


#4.factorial of a given number:
"""
num1=int(input("enter a number:"))
fact=1

for i in range(1,num1+1):
    fact*=i
print(fact)
"""


#5.multiplication table:
"""
num1=int(input("enter a number:"))
for i in range(1,11):
    print(f"{num1} * {i} = {num1 * i}")
"""


#6.fibanacci series:
# num1=int(input("enter a number:"))
# a=0
# b=1

# for i in range(num1):
#     print(a)
#     a,b=b,a+b


#7.given num is prime num or not?
"""
num1=int(input("enter a num:"))
count=0

for i in range(1,num1+1):
    if num1%i == 0:
        count+=1

print(f"{num1} is a prime number" if(count == 2) else f"{num1} is not  a prime number")     #ternary operator/shorthand if-else
"""


#8.reverse a string:
"""
myString=input("enter a string:")
tempString=""

index=len(myString)-1
while(index>=0):
    tempString+=myString[index]
    index-=1
print(f"reversed string is {tempString}")
"""

#9.palindrom number or not:
"""
num1=int(input("enter a number:"))
temp=num1
rev=0

while num1 > 0 :
    last=num1%10
    rev=rev*10+last
    num1=num1//10

result=f"{temp} is a palindrome number" if temp == rev else f"{temp} is not a palindrome number"
print(result)
"""

#10.count vowels and consonants in a string:
"""
myString=input("enter a string:")
vowels=0
consonants=0

for i in myString:
    if i in ["a","e","i","o","u"]:
        vowels+=1
    else:
        consonants+=1
print(f"vowels={vowels}");print(f"consonants={consonants}")
"""

#11.Armstrong number: sum of cubes of digits equals to that number ex:153=> 1^3 + 5^3 + 3^3 = 153
"""
num1=int(input("enter a number:"))
temp=num1
cube=0

while num1 > 0:
    last=num1%10
    cube+=(last**3)
    num1 = num1 // 10

result=f"{temp} is a armstrong number" if temp == cube else f"{temp} is not a armstrong number"
print(result)
"""


#12.guessing the number
"""
import random

while True:
    num1 = int(input("enter a number:"))
    guess=random.randint(1,10)
    if num1 == guess:
        print(f"I have guessed your number and that is {guess}")
        break
    else:
        print("oops! i will try to guess next number")
"""



#13.find the maximum number in the list without using built-in functions
"""
maximumNum=0
list1=[1,32,21,12,543,31,22]
for  i in list1:
    if i >= maximumNum:
        maximumNum=i
print(f"Maximum number={maximumNum}")
"""

#14.use the break, continue in loops:
"""
for i in range(1,11):
    print(i)
    if i == 5:
        break

        
for j in range(11):
    if j == 5:
        continue
    print(j)
"""


#15.print the following pattern
# *
# **
# ***
# ****
# *****
"""
for i in range(6):
    for j in range(6):
        if j < i:
            print("*",end=" ")
    print("\n")
"""



#16.print the following pattern:
#     *
#    ***
#   *****
#  *******
# *********

"""
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
"""


#17.print the following pattern:
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
"""


#18.print the following pattern:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
"""
for i in range(1,6):
    for j in range(1,i+5):
        if j<i:
            print(j,end=" ")
    print("\n")

"""
