# Encapsulation :
# One of the feature of OOPs is encapsulation that prevents the access to certain
# variables and methods and protect the same.
# It is about putting restrictions on accessing variables and methods directly and can
# prevent the accidental modification of data.
# Different Levels of encapsulation :
# 1. Protected members : Members of the class that cannot be accessed outside the class.
# Can be achieved by using a single "_" before a function or variable name.
# 2. Private members : Class members declared private should not be accessed by either
# outside the class or by derived class.
class Base:

    def __init__(self):
        # Protected Variable
        self._a=2

        # Declaring a Private Variable.
        self.__b="Private Variable"

class Derived(Base):

    def __init__(self):
        super().__init__()
        print("Calling the protected member a....")
        print(self._a)
        print("Calling the private member")
        print(self.__b)

obj1=Derived()

obj2=Base()
# Calling protected member outside the class will result in Attribute error.
print(obj2.a)
