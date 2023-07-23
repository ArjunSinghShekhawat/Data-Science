class test:
    def test_math(self):
        print("This is my first class test :")
class child_test(test):
    pass

child_test_obj = child_test()
child_test_obj.test_math()

class class1:
    def test_class1(self):
        return "this is a method from class test_class1:"
    
class class2(class1):
    def test_class2(self):
        return "this is a method from class2:"
    
class class3(class2):
    def test_class3(self):
       return "this is a method from class 3:"
class class4(class3):
    pass

obj = class4()
print(obj.test_class1())
print(obj.test_class2())
print(obj.test_class3())

class Demo1:
    def demo1(self):
        return "demo1"
class Demo2:
    def demo2(self):
        return "demo2"
class Demo3(Demo1,Demo2):
    pass

obj1 = Demo3()

print(obj1.demo1())
print(obj1.demo2())


