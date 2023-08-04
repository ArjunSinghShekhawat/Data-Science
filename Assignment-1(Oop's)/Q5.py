# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

"""Method overriding - methid overriding means inherit class the same method name and argument but 
defination can be change in which present parent class the child class method is called overriding method."""

class Father:
    def name(self):
        print("My name is rajendra singh.")
class Sun(Father):
    def name(self):
        print("My name is arjun singh.")
class Brother(Father):
    def name(self):
        print("My name is manjeet singh.")
        
obj0 = Father()
obj0.name()

obj1 = Sun()
obj1.name()

obj2 = Brother()
obj2.name()