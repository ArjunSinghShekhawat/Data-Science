class student:
    def __init__(self,course_price):
       self.__course_price  = course_price
    @property
    def course_price_access(self):
        return self.__course_price
    @course_price_access.setter
    def set_price(self,price):
     if price <=3500:
         pass
     else :
        self.__course_price = price
    @course_price_access.deleter
    def delete_course(self):
       del self.__course_price

obj1 = student(1000)
# print(obj1._student__course_price)
print(obj1.course_price_access)
obj1.set_price = 5000
print(obj1.course_price_access)
del obj1.delete_course
print(obj1.course_price_access)