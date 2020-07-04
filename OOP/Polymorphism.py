# Polymorphism : means 1 thing that can take many forms i.e.  a single object can take many forms.
# Implementation in Python :
# 1. Duck Typing : Same method under different classes and behaves differently.
# 2. Operator Overloading : same '+' performs different with different objects. e.g. with int performs addition
# and with str performs concatenation.(for coding make use of Magic Methods)
# 3. Method Overloading : Same class with same method name but different arguments.(Not in Pyhton)
# 4. Method Overriding : Class A and Class B with same method name and same sets of arguments.
'''
# Uncomment for understaning Duck typing
class PyCharm:
    def execute(self):
        print('Starting Pycharm')
        print('Compliling')
        print('Running')

# Say another IDE
class MyEditor:
    def execute(self):
        print('Starting MyEditor')
        print('Auto complete')
        print('Dynamic Check')
        print('Compliling')
        print('Running')

class Laptop:

    def code(self,ide):
        # Type of ide depends upon the type
        ide.execute()

ide1=PyCharm()
ide2=MyEditor()

lap1=Laptop()
lap1.code(ide1)
lap1.code(ide2)
'''

# Understanding Operator Overloading (Uncomment for understanding)
'''
a,b=5,10
print(a+b)
print(int.__add__(a,b))
# Thus in the background + is calling __add__ to perform operations.
# same with - : __sub__() ; / : __div__() etc.

class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    # Magic fn to perform additions of their marks, and we are overloading the Operator.
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3

    # Magic Fn for '>' operations
    def __gt__(self,other):
        v1=self.m1+self.m2
        v2=other.m1+other.m2

        if v1>v2:
            return True
        elif v1<v2:
            return False

s1=Student(30,36)
s2=Student(28,39)

# To make this work we need to define __add__()
s3=s1+s2
print(s3.m1,s3.m2)

# to use > define "__gt__()"
if s1 > s2:
    print("s1 is greater")
else:
    print("s2 is greater")
'''

# Understanding Method Overloading, by default if we try overloading with same method name but differnt
# arguments it only runs the one with max number of arguments and none other. Hence to implement Method
# Overloading in Python we can use some tricks.
class Student:

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c

        elif a!=None and b!=None:
            return a+b

        else:
            return a
s1=Student()
print(s1.sum(2,3))
