# Why Python ?
# Python supports all programming paradigms including :-
# 1. Functional Programming (original data remains unaltered during the process.
# 2. Procedural Programming : where large code is broken down into small functions.
# 3. Object Oriented Programming : where every thing in a program can be considered
# as an object and can represent any real world entity.

# Object ? Any real world entity can be termed as an object. For e.g. if there's a
# company then every employee can be considered as an object.
# Every object has certain data that can be called as an attribute(Variables) and
# based on this data it can perform certain actions known to be the behaviour(Methods)
# Methods :- Funcitons in OOPs is called as Methods.

# Classes ? It is like a Factory that is responsible for DESIGNING different objects.
# For e.g. A fan needs to be designed at a particular place, and there is not just one
# fan, but many different fans of the same brand in different households. Fan can be
# considered as an object(i.e. instance of the class) and the factory used for designing
# can be considered as a Class. Thus, before creating an Object we need to create a Class.


# Class is defined by 'class' keyword along with the name of the class.
class Computers:

    # Heap Memory :- Place where all the objects are stored in Memory. Whenever an object
    # is created it is stored in Heap Memory(print(id(comp1))). Now, the size allocated
    # depending upon the number of variables defined in the constructor.

    # For defining Variables of the class we make use of the Special Method also known as
    # the constructor of the class. It is a special method because unlike config(), it'll be
    # automatically each time an object is created.
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    # Since every computer has a configuration.[Method]
    # 'self' is the pointer to the present object that we are passing, from line 32 self->comp1
    # self.cpu is required as CPU is not a local variable but associated with the Object.
    def config(self):
        return ("{}, {} , 1TB".format(self.cpu,self.ram))

    # Comparing 2 objects, one reference via 'self' other via the 'other'[can have any value] name.
    def compare(self,other):
        if self.cpu == other.cpu:
            return True
        else:
            return False

# creating an instance/Object of the class
comp1=Computers("i5",16)
comp2=Computers("amd A4",8)

# To use the fn of the class
print(Computers.config(comp1))      # if no value is given in config it shoots an error as it doesn't
print(Computers.config(comp2))     # know which object we are dealing with.

# In place of the above code, directly this can also be used, behind the scene config takes comp1 as argument.
print(comp1.config())

# Changing and Printing the variable values
comp1.cpu='i7'
print(comp1.cpu,comp1.ram)

# Comparing 2 objects
if comp1.compare(comp2):
    print("Same Machines")
else:
    print("Different Machines")
