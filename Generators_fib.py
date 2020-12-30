# Generators : Like iterators are used to generate a sequence. This is particularly
# implemented by defining a function and replacing a 'return' keyword with a keyword "yield"
# which unlike 'return' will not just return a value but a Generator obj.

# Implementing Generators via fibonacci series

def fib(limit):
     a,b=0,1

     while a<limit:
         # yield keyword that returns a Generator obj, unlike 'return' it'll not terminate the fn
         yield a
         a,b=b,a+b

x=fib(5)
print(next(x))
print(x.__next__())
print(next(x))
print(next(x))
print(next(x))

print('Using for loop')
for i in fib(5):
    print(i)


# BENEFIT of using a GENERATORS : 
# 1. makes the code more readable.
# 2. Generators come handy when we don't want the entire values in a single go in the memory,
#    and use one value at a time which can save the memory consumption.

# When all the 'next()' options are exhausted then it returns an "StopIteration" error.
# 'for' loop can be used in place of using 'next()' all the time.

'''
# Squaring the numbers using list comprehension to yield result in generator

# By using '(',')' one can yeild result in generators, in below sqr_nums is a generator
sqr_nums=(x*x for x in [1,2,3,4,5])

# To print all the numbers together, by doing this we loose the performance benefits of using a generator
print(list(sqr_nums))
'''
