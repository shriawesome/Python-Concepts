# Inheritance : similar to real life all the property of the parents is inherited by
# the Child class.
# Parent Class also called as the Super Class and Child Class as the Sub Class.
# Types of inheritance :
# 1. Single level Inheritance (A<-B)
# 2. Multilevel Inheritance (A<-B<-C)
# 3. Multiple Inheritance (A<-C ; B<-C)

class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

# Simplying by  class B(a) , we are inheriting features of A.
# B is the child class and A is the parent class.
class B:
    def __init__(self):
        # Used to call the init of class 'A'
        #super().__init__()
        print('in B init')

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")



# Multiple inheritance
class C(A,B):
    def __init__(self):
        # has 2 super class, hence makes use of MRO(Method Resolution Order L->R)
        super().__init__()
        print("in C init")

    def feature5(self):
       print("Feature 5 working")

#a1=A()
#a1.feature1()
#a1.feature2()

# If B inherits A and B has no contructor then it calls the constructor of A and if
# B has its own contructor then it uses __init__ of itself.
b1=B()
b1.feature3()
b1.feature4()

# Now in order for B to use features of A, that's when Inheritance comes into picture.
# Thus after Inheritance. Change the code before uncommenting
#b1.feature1()
#b1.feature2()

# Uncomment if using C
c=C()
#c.feature1()
#c.feature3()
#c.feature5()
