# Q3. What is multiple inheritance? Write a python code to demonstrate multiple inheritance.

"""Multiple inheritance one child class inherit  two parent class then child class aquire all proprty of both parent
class this concept is called multiple inheritance."""

class Father:
    def mind(self):
        print("Father mind is very fast and mind baloing person")
class Mother:
    def eye(self):
        print("Mother eye's is blue in colour:")
class sun(Father,Mother):
    pass
arjun = sun()
arjun.mind()
arjun.eye()