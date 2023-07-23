
"""Class is a classified real world entity.
   class is a blue print of an object.
   class is a user define data type.
"""

""" Object is a real world entity.
    object also called instance,variable,and object
"""



class test :
    pass

class test1 :
    def msd(self):
        print("hello")

arjun = test1()
arjun.msd()

print(type(arjun))

class pwskill:
    def __init__(self,student_id,phone_number,email_id):
        self.student_id = student_id
        self.phone_number = phone_number
        self.email_id = email_id
    
    def return_student_record(self):
        return self.student_id,self.phone_number,self.email_id
    
arjun = pwskill(101,12345677,'arjun123gmail.com')
print(arjun.return_student_record())

print(arjun.email_id)

class pwskill1:
    def __init__(arju,student_id,phone_number,email_id):
        arju.student_id = student_id
        arju.phone_number = phone_number
        arju.email_id = email_id
    
    def return_student_record(arju):
        return arju.student_id,arju.phone_number,arju.email_id
    
arjun1 = pwskill1(102,92345677,'anshu123gmail.com')
print(arjun1.return_student_record())

print(arjun1.email_id)


