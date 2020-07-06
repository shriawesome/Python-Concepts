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


# Generators come handy when we don't want the entire values in a single go in the memory,
# and use one value at a time which can save the memory consumption.
