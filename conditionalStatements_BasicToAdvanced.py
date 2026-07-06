#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56


#1.if and nested if
#2.if-else and nested if-else
#3.if-elif-else laddar

#1.Find the greatest number among two numbers
"""
num1=100
num2=678
if num1 >= num2:
    print(f"{num1} is greater than {num2}")
print(f"{num2} is greater than {num1}")
"""

#2.check the given num is even or odd:
"""
num1=int(input("enter a number:"))
if num1%2 == 0:
    print(f"{num1} is a Even number")
else:
    print(f"{num1} is a Odd number")
"""

#3.Age eligilibility check for vote:
"""
age=int(input("enter a number:"))
if age>=18:
    print("You are eligible to Vote")
else:
    print("You are not eligible to vote")
    print(f"You have to wait until {18-age} year to vote")
"""

#4.Guess the entered number is +ve or -ve or Zero:
"""
num1=int(input("enter a number:"))
if num1>0:
    print(f"{num1} is a +ve number")
elif num1<0:
    print(f"{num1} is a -ve number")
else:
    print(f"{num1 } is zero")
"""

#5.determine the entered year is leap year or not:
# In the Gregorian calendar, a year is a leap year 
# if it is exactly divisible by 4, except for century years, 
# which must be perfectly divisible by 400
"""
year=int(input("enter a number:"))
if (year%4==0 and year%400!=0) or year%400==0:
    print(f"{year} is a Leap year")
else:
    print(f"{year} is not a leap year")
"""

#6.Find the entered letter is a vowel or consonant:
"""
letter=input("enter a letter:").lower()
if letter in ['a','e','i','o','u']:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
"""

#7.Traffic light action simulator:
"""
light=input("enter the light(red/yellow/green):").lower()
if light=="red":
    print(f"light is in {light} color so, STOP")
elif light=="yellow":
    print(f"light is in {light} color so, SLOW DOWN")
elif light=="green":
    print(f"light is in {light} color so, GO")
else:
    print("Invalid light color")
"""

#8.student grading system:
"""
marks=int(input("enter your marks:"))

if marks>90 and marks<=100:
    print("Your Grade-Ex")
elif marks>80 and marks<=90:
    print("Your Grade-A")
elif marks>70 and marks<=80:
    print("Your Grade-B")
elif marks>60 and marks<=70:
    print("Your Grade-C")
elif marks>50 and marks<=60:
    print("Your Grade-D")
elif marks>40 and marks<=50:
    print("Your Grade-E")
elif marks<40:
    print("Fail")
else:
    print("Invalid Marks entred")
"""

#9.BMI classification:
"""
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"BMI: {bmi:.1f} - Underweight")
elif 18.5 <= bmi < 25:
    print(f"BMI: {bmi:.1f} - Normal weight")
elif 25 <= bmi < 30:
    print(f"BMI: {bmi:.1f} - Overweight")
else:
    print(f"BMI: {bmi:.1f} - Obesity")
"""


#10.Quadratic Equation Root Classifier:
"""
import math
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    print("Two distinct real roots")
elif discriminant == 0:
    print("One real repeating root")
else:
    print("Complex/Imaginary roots")
"""


#11.weekday or weekend evaluation:
"""
day = input("Enter day of the week: ").strip().lower()
if day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("It is a weekday.")
elif day in ["saturday", "sunday"]:
    print("It is the weekend!")
else:
    print("Not a valid day.")
"""


#12.authentication:
""""
username="Nagabashashaik"
password="3k8$&@1pXn2Fd"

if username=="Nagabashashaik":
    if password=="3k8$&@1pXn2Fd":
        print(f"Welcome back {username}")
    else:
        print("entered password is incorrect")
else:
    print("user doesn't exist")
"""

