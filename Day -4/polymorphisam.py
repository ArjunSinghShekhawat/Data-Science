def test(a,b):
    return a+b

print(test(10,40))
print(test("arjun"," bansal"))

class data_science:
    def syllabus(self):
        print("This is syllabus of adsta science master class :")

class web_dev:
    def syllabus(self):
        print("This is my syllabus of web dev class :")

def course_syllabus(class_obj):
    for i in class_obj:
        i.syllabus()

data_science = data_science()
web_dev = web_dev()

class_obj = [data_science,web_dev]
course_syllabus(class_obj)

