# Types of Variables :
# 1. Instance Variables : Different for different objects
# 2. Class Variables : Variables whose value is same accross all the objects.

# Types of Methods :
# 1. Instance Method : any method that has 'self' as an argument.
# Note : Accessor Methods(When we just want to access the values), Mutator Methods(Modifying the values)
# 2. Class Method : any method that deals with class variables.
# 3. Static Method : Methods used to add additional functionality and doesn't work with class/ instance
# variables.

# namespace : area where you create and store objects/Variables.
class Cars:
    # Variables defined outside init are termed as Class variables and are created in
    # Class namespace
    wheels=4

    # Varibale defined within init are said to be instance Variables and are created in
    # Instance namespace
    def __init__(self):
        self.mil=10
        self.com="BMW"

class Student:

    school="APS"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    # Instance Method as it is having an argument 'self'
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # Class Method : 'cls' keyword, decorator needed for 'cls'
    @classmethod
    def info(cls):
        return (cls.school)

    # Decorator for static methods.
    @staticmethod
    def stats_class():
        return ('This is a Student Class with 3 methods')

if __name__=='__main__':
    c1=Cars()
    c2=Cars()

    # Changing values of instance variables.
    c1.mil=8

    print(c1.com,c1.mil,c1.wheels)
    print(c2.com,c2.mil,c2.wheels)

    s1=Student(25,36,30)
    s2=Student(40,39,42)
    print(s1.avg())
    print(s2.avg())
    print(Student.info())
    print(Student.stats_class())
