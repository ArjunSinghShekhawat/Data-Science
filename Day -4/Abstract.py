import abc
class pwskills:
    @abc.abstractclassmethod
    def student_details(self):
        pass
    @abc.abstractclassmethod
    def student_assignment(self):
        pass
    @abc.abstractclassmethod
    def student_marks(self):
        pass

class student_details1(pwskills):

    def student_details(self):
        return "this is a meth for taking details"
    def student_assignment(self):
        return "this is a meth for taking student assignment"

class data_science(pwskills):
    def student_details(self):
        return "this is a meth for data science taking details"
    def student_assignment(self):
        return "this is a meth for data science taking student assignment"

dsm = data_science()
print(dsm.student_details())

sd = student_details1()
print(sd.student_details())

  

