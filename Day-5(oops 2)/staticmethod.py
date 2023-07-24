# class codehelp:
#     def student_details(self,name,email):
     
#       print(name,email)

# obj = codehelp()
# obj.student_details('arjun','arjun@gmail.com')

# class codehelp:
#     def student_details(self,name,email):
#         print(name,email)
#     @staticmethod
#     def mentor_list(mentor_list):
#         print(mentor_list)

# codehelp.mentor_list(['arjun','rahul'])   


class codehelp:
    def student_details(self,name,email):
        print(name,email)
    
    @staticmethod
    def mentor_mail_id(mentor_id_list):
        print(mentor_id_list)
    @staticmethod
    def mentor_list(mentor_list):
        codehelp.mentor_mail_id(['govind@gmail.com','anshu@gmail.com'])
        print(mentor_list)
    @classmethod
    def class_name(cls):
        cls.mentor_list(['govind','snshu'])
    def student_details(self):
        self.mentor_list(['arjun','anshu'])

#codehelp.mentor_list(['arjun','narpat'])
obj = codehelp()
obj.student_details()