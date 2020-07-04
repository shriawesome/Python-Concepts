# Abstract Method : Method that only has a declaration but no functionality.
# Abstract Class : The one that contains an abstract method. Objects of such classes can't be
# created.
# Python by defalt doesn't support Abstraction and hence to do that we can make use of
# abc module.

# Hackerrank Day 13 challenge(30 Days of Code)
#Given a Book class and a Solution class,
# write a MyBook class that does the following:
# 1. Inherits from Book
# 2. Has a parameterized constructor taking these  parameters:
#    string Title
#    string author
#    int Price
# Implements the Book class' abstract display() method
# so it prints these  lines:
# 1. Title : <title>
# 2. Author : <author>
# 3. Price : <price>


from abc import ABCMeta, abstractmethod

class Book(metaclass=ABCMeta):
	def __init__(self,title,author):
		self.title=title
		self.author=author

	# Abstractmethod keyword tells that this is an abstract method
	@abstractmethod
	def display(): pass

class MyBook(Book):
	def __init__(self,title,author,price):
		super().__init__(title,author)     # inherits property from the Parent class
		self.price=price

    # Implementing the Abstract method from the base class
	def display(self):
		print("Title: {}\nAuthor: {}\nPrice: {}".format(self.title,self.author,self.price))


if __name__=='__main__':
	title=input()
	author=input()
	price=int(input())
	new_novel=MyBook(title,author,price)
	new_novel.display()


#---------------OUTPUT------------------------
# Shri-2:AbstractClass shri$ python  Bookabc.py
# The Alchemist
# Paulo Coelho
# 248
# Title: The Alchemist
# Author: Paulo Coelho
# Price: 248
