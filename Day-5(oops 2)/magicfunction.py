print(dir(int))
print("\n")
print(dir(str))
print(12+90)
a = 90
print(a.__add__(90))

class student:
    # def __new__(self):
    #     print("This is my new function")
    def __init__(self):
        print("this is my init function")
        self.phone_number = 582365480

    def __str__(self):
        return 'this is my obj address'
    
obj = student()
print(obj)
# print(obj.phone_number)