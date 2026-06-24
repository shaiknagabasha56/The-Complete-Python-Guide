#author:Shaik Nagabasha
#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56

#NOTE: '#' refers to comments,these are not executed and we write it for clarity about what the program do. 


# ----------------------------------------------BASIC LEVEL-----------------------------------------------

#1.Printing the names,To print names(strings) we use double quotes or single quotes:
print("Hello,World")	#whatever in the double quotes are displayed as it is in output
print("Hyderabad")
print("Python Programming learning with Nagabasha")
print("1+2+3") 		#observe the output clearly
print("what type of 'Operating System' you are using?")  	#single quotes under double quotes for highlighting the text
print('Im using "Linux" Operating System')					#double quotes under single quotes for highlighting the text
#observe the above two outputs for better understanding
print("---------------------------------------------------------------------------------------------")


#2.Printing the numbers, we don't use quotes for numbers 
print(100)
#print(001)			doesn't works, will get error
print(100000)
print("10") 		#it is a string, not a number
print(type("10"))
print("---------------------------------------------------------------------------------------------")

#3.printing multiple values:To print multiple values we use comma between values
print("Apple","Banana","Mango")
print(10,100,1000,10000)
print("My name is:-","Nagabasha")
print("5 Apples","Price:-",100)
print("1Apple:-",20,"1Banana:-",4,"1Pineapple:-",100,"1Guava:-",5)

#4.Printing values with custom seperator using sep
print("Linux","Mac","Windows")				#in output they are seperated with space
print("Linux","Mac","Windows", sep="@")		#Now these are sepearted with @ symbol
print("Linux","Mac","Windows", sep="#")		#Now these are sepearted with # symbol
print("Linux","Mac","Windows", sep="$")		#Now these are sepearted with $ symbol
print("---------------------------------------------------------------------------------------------")

#5.Printing values without newline
#with newline print(value,end="\n")
print("Switch")
print("Router")
print("Server")
#if you observe the output these are displayed one after another because in print() function the default is newline (\n)

#without newline print(value,end="user defined symbol")
print("Switch",end=" ")
print("Router",end=" ")
print("Server",end=" ")
#observe the above output, now these are printing side by side with space between because i used space in end
print("\n") #used for newline, because above code has space in new line but i want the below output in new line so i used it
print("Switch",end="@")
print("Router",end="@")
print("Server",end="@")
#observe the above output, now these are printing side by side with @ symbol between because i used @ in end
print("\n")
print("Switch",end="$")
print("Router",end="$")
print("Server",end="$")
print("\n")
#observe the above output, now these are printing side by side with $ symbol between because i used $ in end


#6.printng the newline
#end="\n" by default in print(), which means print output and immediately print newline
#end="@" means, after printing the output in present line, immediately @ is printed and the next output is also printed after @ symbol instead of newline
#end="&" means, after printing the output in present line, immediately & is printed and the next output is also printed after & symbol instead of newline

print("IP address")
print("MAC address")
# the above two lines are printed one after another

print("IP address",end="@")
print("MAC address")
# the above two lines are printed side by side with @ symbol seperator

print("IP address",end="@")
print()
print("MAC address")
#Normally above two lines are printed side by side with @ symbol but we have used print() which means newlinw is added and these two are printed one after another

print("Laptop",end="0000")
print("\n") # also do the same, print the newline
print("Computer")
print("----------------------------------------------------------------------------")






#------------------------------------INTERMEDIATE LEVEL------------------------------------------------

#7.performing mathematical operations using print()
print(100+100)
print(99.9-1.9)
print(4*5)
print(2**3)
print(110/2)
print(10//3)
print(10%3)
print(10*20+30/40)
print(1&2)
print(1|2)
print(1>>1)
print(1<<1)
print("----------------------------------------------------------------------------")

#8.printing string concatenation(combining multiple strings)
#when we use + symbol between numebers those are added 
#but when we we use + symbol between strings those are combined

print("ABC"+"DE")           #no space will be displayed between two words
print("Long"+"Word")
print("Long"+" "+"Word")    #maual space is added
print("Computer"*3)         #displays name into specific times (here 3 time)
print("Networking"*7)
print("3"+"3")
print("99"+"100")
#print("400"+400)           #raises error
print("----------------------------------------------------------------------------")

#9.printing variable name
myName="Nagabasha"  #here myName is a variable and Nagabasha is value stored in myName variable
print(myName)
print("my name is:-",myName)
print("I am",myName,"and I am a Good Boyyy")

myAge=20
print(myAge)
print("my age is:-",myAge)

randomNumber=8080
print(randomNumber)
print(randomNumber+120)     #we can add,sub,mul,divide and perform other mathematical operations too
print(randomNumber*2)
print("----------------------------------------------------------------------------")

#10.printing variables using fstrings (stands for formatted strings)
portNum=8080
print(f"port is running on:{portNum}")  #observe the difference, in this we didnt used comma to seperate the string and variable name

doorNum=8090
print(f"my port number is {portNum} and my door number is {doorNum}")


print(f"sum of port and door numbers are:-{portNum+doorNum}")
print("----------------------------------------------------------------------------")


#11.Printing special characters using escape sequences
print("Hello my name is \"Nagabasha\", I am a CS studet")       #to highlight a text using double quotes under double quotes
print('Hi my name is \'Basha\',I am also a CS student')
print("----------------------------------------------------------------------------")


#13. Printing multiple lines using triple quotes
print("""hi
Hello
How are you ??""")
print("----------------------------------------------------------------------------")



#----------------------------------ADVANCED LEVEL------------------------------------
#some topics are not covered but, same print() methods are used in later chapters.

#14. Printing with multiple separators and ending characters combined
print("Signal","packets","data",sep=" | ", end=" || END\n")
print("router","switch","hub")
print("----------------------------------------------------------------------------")

#15. Printing a formatted number (decimal precision)
PI=3.14159265
print(f"PI value is {PI:.2f}")  #prints only two digits after decimal
print("----------------------------------------------------------------------------")


#16. Printing in a loop without moving to a new line each time
for i in range(1,6):
    print(i)
print("-------------")
#The above loop produces output one after another

for i in range(1,6):
    print(i,end=" ")
print("\n")
#the above loop produces output side by side with space between them.
print("----------------------------------------------------------------------------")


#17.instead of printing the output in a terminal, we can save it in a file
with open("output.txt","w") as f:
    print("Hi packets are saving in the output.txt file",file=f)
#that file is saved in the directory where this program exists.
print("----------------------------------------------------------------------------")


#18. Printing using flush=True (forces immediate output, useful in real-time logs)
import time
print("Loading",flush=True)
time.sleep(1)
print("...Done")
print("----------------------------------------------------------------------------")


#19.Printing a dictionary in a structured way
students={1:"Alex",2:"Bobby",3:"Chetri"}
print(f"student-1:{students[1]} student-2:{students[2]}")
print("----------------------------------------------------------------------------")

#20.Printing a formatted table-like output using string alignment
print(f"{'Name':<10}{'Age':<5}")
print(f"{'Alex':<10}{25:<5}")
print(f"{'Sara':<10}{30:<5}")





#NOTE:If you learn something from the above programs please follow me in instgram,github and subscribe my youtube channel

#Instagram:https://www.instagram.com/mirapakaaytech/
#Youtube: https://youtube.com/@mirapakaaytech?si=pC5ZmkIl6xgIyGuM
#GitHub: https://github.com/shaiknagabasha56
