# Data Structure : It is the way to organise, store and manage data for efficient 'access' and 'modification'.
# Types of Data Structures:
# 1. Built-in DS : lists, dictionary, tuple, sets
# 2. User-Defined DS : Arrays(stack, queue), linked list, tree, graph

# 1. Lists: 
    # a. List have hetrogeneous items(items with different datatypes) in it
    # b. Lists are mutable i.e. the contents within can be changed

mylist=[1,'shri',2.0,True]

# insert elements, append() : adds element to the end.
mylist.append(3)
#print(mylist)

# extend() : adds elements in the list as single elements
mylist.extend((5,6))
#print(mylist)

#insert(idx,element)
mylist.insert(0,'First')
#print(mylist)

# REMOVING ELEMENTS : del, pop() : returns that element, remove() : won't return any value
del mylist[0]
a=mylist.pop(2)
# print(a)

# sorted() : actual list data is not changed, sort() : makes changes in the list itself
list1=[3,4,1,2,5]
# print(sorted(list1),list1)
list1.sort(reverse=True)
# print(list1)

# RETURN THE INDEX OF THE ELEMENT
# print(list1.index(3))
# print(list1.count(3))    # return the count of element 3

# 2. Tuples:
    # a. Same as lists but are not mutable i.e. once created can't be changed.
    # b. Faster than lists. How ?
    #    i. Can be reused instead of copied like in list i.e. 'b=tuple(a)' is same as b, but in list 'b=list(a)' copies all the elements of a to b
    #       since b can be changed.
    #   ii. Since tuples are of fixed size, it can be stored more compactly than lists which need to over-allocate to make append() operations efficient. 
    #  iii. Tuples directly referende their elements unlike list which have an extra layer of indirection to an external array of pointers.
mytuple=(1,2,3)
# print(mytuple)
# data can't be changed once created thus assignment operator is not allowed, when concatenating a new tuple is created.

# tuple comprehension
b=tuple(i for i in (1,2,3))
#print(b)

# 3. Dictionary:
    # a. Holds key, value pairs
    # b. are mutables
mydict={i:i+1 for i in range(1,4)}

# modifying value, mydict[key]=value, adding value is the same.
mydict[1]='shri'
#print(mydict)

# removing element : del mydict[1], pop(), popitem(): returns (key, value)
#print(mydict.popitem())

# Few functions
#print(mydict.keys())  # return all the key values
#print(mydict.values())
#print(mydict.items())  # returns key, value pairs.

# 4. Sets:
    # a. Un-ordered collection of unique elements.
    # b. Sets are mutable
    # c. Contains unique value of elements
set1={1,2,3,4,4,4,5}
print(set1)

# Adding elements in sets set1.add(element)
# Different operations : Union, intersection, difference, symmetric_difference() : both 'sets' differences is given
set2={3,4,5,6,7}
print(set1.union(set2))  # same for intersection


# II. User-defined data types
# 1. Array (contains data of specific data types)
# 2. Stacks:
    # a. Follows LIFO principle  
# 3. Queues :
    # same as stacks but follows FIFO principle and has a Head and the Tail
# 4. Trees :
    # useful for defining hierarchy
    # consist of the Node that contains the data and the left and the right child
# 5. Linked List :
    # single node consists of the data and pointer to the next value.
    

