# Q3. Explain why the __init__() function is used. Give a suitable example.

"""The __init__() is a dunder function .It is a constructor.It is used to take input by object and assign the 
value to class variable using by self and other reference words."""

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
arjun = student('arjun',21)
print(arjun.name)
print(arjun.age)
