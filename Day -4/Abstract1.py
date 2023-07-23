import abc
class Codehelp:
    
    @abc.abstractclassmethod
    def assignment_details(self):
        pass
    @abc.abstractclassmethod
    def video_seen_details(self):
        pass
    @abc.abstractclassmethod
    def score_details(self):
        pass
    @abc.abstractclassmethod
    def quiz_details(self):
        pass

class Dsa(Codehelp) :
    
    def __init__(self,student_name,student_email_id,student_age):
        print("DSA SUPREME MASTER CLASS :")
        self.student_name = student_name
        self.student_email_id = student_email_id
        self.student_age = student_age

    def get_student_details(self):
        return self.student_name,self.student_age,self.student_email_id
    
    def assignment_details(self):
        return "80 assignment submit out of 100 by user"
    def video_seen_details(self):
        return "70% video seen by user "
    def quiz_details(self):
        return "200 number achived out of 500 by user "
    
class Web_dev(Codehelp) :
    
    def __init__(self,student_name,student_email_id,student_age):
        print("WEB DEV MASTER CLASS :")
        self.student_name = student_name
        self.student_email_id = student_email_id
        self.student_age = student_age

    def get_student_details(self):
        return self.student_name,self.student_age,self.student_email_id
    
    def assignment_details(self):
        return "20 assignment submit out of 100 by user"
    def video_seen_details(self):
        return "90% video seen by user "
    def quiz_details(self):
        return "400 number achived out of 500 by user "
    
    
Dsa_obj = Dsa("arjun","arjun123@gmail.com",22)
print(Dsa_obj.get_student_details())
print(Dsa_obj.quiz_details())


Web_dev_obj = Web_dev("govind","govind123@gmail.com",20)
print(Web_dev_obj.get_student_details())
print(Web_dev_obj.assignment_details())



    
    


    
    
