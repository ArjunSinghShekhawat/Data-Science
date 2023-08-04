# Q5. What is inheritance? Give an example for each type of inheritance.

#Inheritance - inheritance means child class aqure the all property from parent class but private data
# member is not aqure this concept is called inheritance.
"""

There are multiple types of inheritance avilable in python
1.single inheritance
2.multiple inheritance
3.multilevel inheritance
4.hybride inheritance
"""

#1.single inheritance
class test:
    def test_meth(self):
        return "this is my first class"
class child_test(test):
    pass

obj = child_test()
print(obj.test_meth())


#2.Multiple inheritance -example
class class1:
    def test_class1(self):
        print("This is class 1 method")
class class2:
    def test_class2(self):
        print("This is class 2 method")
class class3(class1,class2):
    pass
  
obj3 = class3()
obj3.test_class1()
obj3.test_class2()

#3.multilevel inheritance
class class1:
    def test_class1(self):
        print("This is class 1 method")
class class2(class1):
    def test_class2(self):
        print("This is class 2 method")
class class3(class2):
    pass
obj1 = class3()
obj1.test_class1()
obj1.test_class2()

#4.hybride inheritance
class demo1:
    def test_class1(self):
        print("This is class 1 method")
class demo2:
    def test_class2(self):
        print("This is class 2 method")
class demo3(demo1,demo2):
    def test_class3(self):
        print("This is class 3 method")
class demo4(demo3):
    pass

demo4 = demo4()
demo4.test_class1()
demo4.test_class2()
demo4.test_class3()

        


