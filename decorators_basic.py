# Decorators are mainly used to add some additional functionality to the already present method
# by without explicitly changing the code inside that method.
# Suppose we have a divide f'n


# Suppose we always want a > b then in that case without changing the div() code we can do so
# by implementing decorators.
def div_decorator(func):
    def inner(a,b):
        if a < b:
            a,b=b,a

        func(a,b)

    return inner

@div_decorator
def div(a,b):
    print(a/b)

#div(2,4)

#other way
div=div_decorator(div)
div(2,4)

# other example i.e. to use decortors to calculate time take by the code to execute.
import time
import math

def calculate_time(func):
    def inner(*args,**kwargs):
        begin=time.time()
        func(*args,**kwargs)
        end=time.time()

        print('Total time taken in : ',func.__name__,end-begin)

    return inner

@calculate_time
def factorial(n):
    time.sleep(2)
    print(math.factorial(n))

factorial(10)
