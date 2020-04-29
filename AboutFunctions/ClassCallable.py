# By default at the time when we are creating an instance of the class say
# resolver=Resolver()  ->  () :- calls the contructor of the class that can be used
# for initialising the values. Functionality of this can be extended as below

def sequence_class(immutable):
    if immutable:
        class_=tuple

    else:
        class_=list
    return class_

if __name__=='__main__':
    seq=sequence_class(immutable=True)
    # seq is of type class in this particular case tuple class
    t=seq('shri')
    # Now t contains a tuple with values as each alphabet of shri
    print(t)
