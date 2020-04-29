# Python Concepts
**Version 1.0.0**
- - -
1. Abstract Classes :
  * An abstract class can be considered as a blueprint for other classes.
  * It allows you to create a set of methods that must be created within any child classes built from the abstract class.
  * It can be used to define a common API for a set of subclasses. This capability is especially useful in a situation where a third-party is going to provide implementations, such as plugins etc.
  * Python does not provide inbuilt support for abstract class.
  * It comes with a module named abc(Abstract Base Class) for the purpose.
  * Important modules :-
    * `from abc import ABCMeta,abstractmethod`
- - -

2. Beyond Basic Functions :
  a.` __call__()`:
    * This is used so as to make an instance of the class created behave as an function directly.
    * For e.g. refer to AboutFunctions/resolver.py
  b. lambdas :
    * Is an expression that evaluates to the Function.
    * Unlike function defined using def() keyword it need not be defined and can be anonymous i.e. it has no name.
    * Argument list terminated by colon, separated by commas i.e. e.g.  `lambda a,b,c : a+b+c`
    * It can also support zero or more arguments. For zero argument `lambda : `
    * Body contains only a single statement. More than one statement is not permitted.
    * The single statement itself is a return statement and can't contain a keyword `return`.
    * e.g. `sorted(,key=)` in python contains a key argument accepts lambda function as a value.
    * Hence, given a list of names to sort for one can sort the names based on last name using this.
    * [lambda implementation](https://github.com/shriawesome/Python-Concepts/blob/master/imgs/lambda.png)

- - -
