class pwskills:
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    
    def return_details(self):
        return self.name,self.email_id

arjun = pwskills('arjun','arjun@gmail.com')
print(arjun.return_details())
print(arjun.name)
print(arjun.email_id)


class pwskills1:
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    
    def return_details(self):
        return self.name,self.email_id
    
arjun = pwskills1.details('arjun','arjun123@gmail.com')
print(arjun.name)
print(arjun.email_id)
print(arjun.return_details())


class pwskills2:

    phone_number = 8005792198

    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id

    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    
    @classmethod
    def change_phone_number(cls,number):
        pwskills2.phone_number = number
    
    def return_details(self):
        return self.name,self.email_id,pwskills2.phone_number
arjun = pwskills2('arjun','shekhawatsingharjun12345@gmail.com')
print(arjun.return_details())
arjun.change_phone_number(63376129260)
print(arjun.return_details())
print(arjun.return_details())
arjun.change_phone_number(6376129260)
print(arjun.return_details())
print(arjun.phone_number)
print(arjun.email_id)




class pwskills3:

    phone_number = 8005792198

    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id

    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    
    @classmethod
    def change_phone_number(cls,number):
        pwskills3.phone_number = number
    
    def return_details(self):
        return self.name,self.email_id,pwskills3.phone_number
   
    
def course_details(cls,course_name):
    print(f"Course name is {course_name}")

pwskills3.course_details = classmethod(course_details)
pwskills3.course_details('data science master')

def mentor(cls,mentor_list):
    print(mentor_list)

ae = pwskills3('arjun','ase')
pwskills3.mentor = classmethod(mentor)
pwskills3.mentor(['arjun','manjeet'])

del pwskills3.change_phone_number
# delattr(pwskills3,'details')
pwskills3.phone_number = 5558789654
print(pwskills3.details())

pwskills3.change_phone_number(123)
pwskills3.change_phone_number()
del pwskills3.change_phone_number

pwskills3.change_phone_number()

class codehelp:
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    
    def return_details(self):
        return self.name,self.email_id

obj = codehelp('arjun','arjun@gmail.com')
print(obj.return_details())
print(obj.name)
print(obj.email_id)


class codehelp:
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    
    def return_details(self):
        return self.name,self.email_id

obj1 = codehelp.details('arjun','rajput@gmail.com')
print(obj1.return_details())
print(obj1.name)
print(obj1.email_id)

class codehelp:
    phone_number = 8005792198
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    @classmethod
    def change_number(cls,number):
        codehelp.phone_number = number

    
    def return_details(self):
        return self.name,self.email_id,codehelp.phone_number
    
print(codehelp.phone_number)
codehelp.phone_number = 123456789
print(codehelp.phone_number)

obj1 = codehelp.details('govind','govind@gmail.com')
obj1.phone_number = 789456123

print(obj1.return_details())

obj1.change_number(456987125)
print(obj1.return_details())


class codehelp:
    phone_number = 8005792198
    def __init__(self,name,email_id):
        self.name = name
        self.email_id = email_id
    @classmethod
    def details(cls,name,email_id):
        return cls(name,email_id)
    @classmethod
    def change_number(cls,number):
        codehelp.phone_number = number
    def return_details(self):
        return self.name,self.email_id,codehelp.phone_number
    
def course(cls,course_name):
    print(f"course name is {course_name}")

codehelp.course = classmethod(course)
codehelp.course('data science')

def mentor(cls,mentor_list):
    print(mentor_list)

codehelp.mentor = classmethod(mentor)
codehelp.mentor(['arjun','manjeet'])

# del codehelp.details
q=codehelp.details('govind','as')

print(q.return_details())
delattr(codehelp,'change_number')
# codehelp.change_number(789)
