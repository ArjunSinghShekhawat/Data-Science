a = 10
print(type(a))

course = "data science master"
print(type(course))

class test :
    pass

obj1 = test()
print(type(obj1))


class pwskill :
    def welcome_msg(self):
        print("Welcome to pwskill")

arjun = pwskill()
arjun.welcome_msg()

govind = pwskill()
govind.welcome_msg()


class pwskill1 :
    def __init__(self,student_id,email_id,phone_number):
        self.student_id = student_id
        self.email_id = email_id
        self.phone_number = phone_number

    def return_student_details(self):
        return self.student_id,self.phone_number,self.email_id

arjun = pwskill1(101,'singh123@gmail.com',1234567)
print(arjun.return_student_details())

manjeet = pwskill1(102,'shekhawat123@gmail.com',98576433)
print(manjeet.return_student_details())

#oop's concepts

class Demo:
    pass
print("hello")

class friend:

    def good_night_msg(self):
        print("good night all friends")

ajay = friend()
ajay.good_night_msg()


#student record

class student :

    def __init__(self,student_name,student_age,student_phone_number,student_branch,student_section):
        self.student_name = student_name
        self.student_age = student_age
        self.student_phone_number = student_phone_number
        self.student_branch = student_branch
        self.student_section = student_section

    def return_student_record(self):
        return self.student_name,self.student_age,self.student_phone_number,self.student_branch,self.student_section
    
aknush = student("ankush",22,1234567890,'CSE','A1')
print(aknush.return_student_record())


class student1 :

    def __init__(arju,student_name,student_age,student_phone_number,student_branch,student_section):
        arju.student_name = student_name
        arju.student_age = student_age
        arju.student_phone_number = student_phone_number
        arju.student_branch = student_branch
        arju.student_section = student_section

    def return_student_record(arju):
        return arju.student_name,arju.student_age,arju.student_phone_number,arju.student_branch,arju.student_section
    
aknush1 = student1("ankush",22,1234567890,'CSE','A1')
print(aknush1.return_student_record())     




