#Attributes are nothing but variables
#Two types of Attributes:
#i.Instance attributes
#ii.Class attributes

#1.INSTANCE ATTRIBUTES:
#An instance attribute is owned by a specific objectn of a class.
#Every time you create a new object, it gets its own completely separate copy of these variables. 
#Changing the value in one object will never affect another.
#Where are they defined: Inside the class methods (usually inside the __init__ constructor) using self.variable_name
# Who can see them:Only that specific object.
#accessed via object name

#example:
"""
class Phones:
    def __init__(self,brand,color):
        self.brand=brand    #instance attributes
        self.color=color    #instance attributes

p1=Phones("Nothing","Black")
p2=Phones("Realme","Blue")

#showing info:
print(p1.brand,p1.color)
print(p2.brand,p2.color)

#modifying the p1 object attribute
p1.color="Orange"

#checking whether its reflcts on both object's attributes
print(p1.brand,p1.color)    #changes applied to p1 obj
print(p2.brand,p2.color)    #changes not applied to p2 obj
"""
#NOTE:so, changing one instance attribute will not effect the other object's instance attributes


#2.CLASS ATTRIBUTES:
#A class attribute belongs to the entire class itself. 
#All objects created from this class share the exact same variable. 
#If you change a class attribute, that change instantly reflects across every single object.
#accessed with class name


#example:
"""
class Phones:
    store_name="Nothing Store"
    def __init__(self,model,price):
        self.model=model
        self.price=price
p1=Phones("Cmf",20000)
p2=Phones("Nothing 3a",30000)

print("Info:-")
print(f"Store={Phones.store_name}")
print(f"Phone1={p1.model},{p1.price}")
print(f"Phone2={p2.model},{p2.price}")
print("---------------------------------")

Phones.store_name="Basha Store"     #changing the store name of a class

print("Info:-")
print(f"Store={Phones.store_name}")
print(f"Phone1={p1.model},{p1.price}")
print(f"Phone2={p2.model},{p2.price}")
print("---------------------------------")
"""


#example:combined together
"""
class Experiment:
    no_of_experiments=0     #class attribute
    def __init__(self,exp_num,exp_name):
        self.exp_num=exp_num        #instance attributes
        self.exp_name=exp_name      #instance attributes
        Experiment.no_of_experiments+=1
    def show_info(self):
        print(f"NO.OF EXPERIMENTS={Experiment.no_of_experiments}")
        print(f"EXPERIMENT NUMBER={self.exp_num}")
        print(f"EXPERIMENT NAME={self.exp_name}")
        print("-----------------------------------------")

exp1=Experiment(1,"Ohms Law")
exp1.show_info()

exp2=Experiment(2,"Kirchoffs Law")
exp2.show_info()

exp3=Experiment(3,"Hooks Law")
exp3.show_info()
"""


