#student college database

#first sem student college database 
student_name = ['arjun','govind','anshu','ankit','kesav','hemlta']
student_father_name = ["rajendra","ram singh","vikarm singh","sanjay singh","narpat singh","arun singh"]
student_id   = [101,102,103,105,105,106]
student_branch = ['cse','cse','ece','me','civil','ai']
student_first_mid_score = [0,0,0,0,0,0]
student_second_mid_score = [0,0,0,0,0,0]
student_first_sem_fees = [0,0,0,0,0,0]
student_gender = ['M','M','m','m','m','f']
student_back_log = [False,False,False,False,False,False]
student_Scholarship = ["no Scholarship","no Scholarship","no Scholarship","no Scholarship","no Scholarship","no Scholarship"]


#first task is all list in all string convert into upper case

for i in range(len(student_id)):
    student_name[i] = student_name[i].upper().strip()
    student_gender[i] = student_gender[i].upper().strip()
    student_Scholarship[i] = student_Scholarship[i].upper().strip()
    student_branch[i] = student_branch[i].upper().strip()
    student_father_name[i] = student_father_name[i].upper().strip()

"""***********Task complete*************"""

print(student_name)
print(student_father_name)
print(student_Scholarship)
print(student_gender)
print(student_branch)



s0 =  "take fees for each student"
print(s0.title())
print("\n")
for i in range(len(student_id)):
    print(f"{student_name[i]} you are given first sem fees select 1(True) or 0(False)")
    user_input = int(input())

    if user_input == 1:
        print("Your first sem total amount 25000 than complete fees deposit at a time so plese given complete 25000 amount ")
        amount = int(input())
        if amount==25000:
          
            student_first_sem_fees[i] = student_first_sem_fees[i]+amount
           
            print("Payment processing ...")
            print("Your fees successfully deposit !")
            print("Thanking you!")
            
        else :
            print("Please given 25000 amount to deposit fees!")
            print("Enter total 25000 amount last chance again exit this application Enter 1(True) and 0(False)")
            user_input = int(input())

            if user_input == 1:
                print("Your first sem total amount 25000 than complete fees deposit at a time so plese given complete 25000 amount ")
                amount = int(input())

                if amount == 25000:
                    student_first_sem_fees[i] = student_first_sem_fees[i]+amount
                    print("Payment processing ...")
                    print("Your fees successfully deposit !")
                    print("Thanking you!")
                else :
                    if student_name[i] in student_name:
                        continue
    else :
        print("Your last date fees deposite in 7 days")
        print("Thanking you")
print("\n")

#********************Task complete*******************

print(student_first_sem_fees)

s1 = "first midterm marks assignment"
print(s1.title())
print("\n")
for i in range(len(student_id)):
    print(f"{student_name[i]} Achieve persantage  in first mid term(out of 100)")
    student_first_mid_score[i] = int(input())


# print(student_first_mid_score)

#********************Task complete*******************


s2 = "Second midterm marks assignment"
print(s2.title())
print("\n")
for i in range(len(student_id)):
    print(f"{student_name[i]} Achieve persantage  in second mid term(out of 100)")
    student_second_mid_score[i] = int(input())

#********************Task complete*******************

# print(student_second_mid_score)


s3 = "back log in college"
print(s3.title())
print("\n")
for i in range(len(student_id)):
    if student_first_mid_score[i]<40 or student_second_mid_score[i]<40:
        student_back_log[i] = True

#********************Task complete*******************

s4 = "given Scholarship condition no back log, first and second mid term marks>=75 and feed deposite  Scholarship givrn 12500"
print(s4.title())
s5 =  "and first and second midterm marks >=65 and <75 Scholarship given 6000 ,no back log ,fees deposite"
print(s5.title())
print("\n")
for i in range(len(student_id)):
    
    if student_first_mid_score[i]>=75 and student_second_mid_score[i]>=75 and student_back_log[i]==False and student_first_sem_fees[i] == 25000:
        student_Scholarship[i] = "given Scholarship 12500"
        print("Your fees less 12500 ")
        student_first_sem_fees[i] = student_first_sem_fees[i]-12500
        student_Scholarship[i] = "12500 Scholarship "
        student_Scholarship[i]  = student_Scholarship[i].upper()
    elif student_first_mid_score[i]>=65 and student_second_mid_score[i]<75 and student_back_log[i] == False and student_first_sem_fees[i]==25000:
           student_Scholarship[i] = "given Scholarship 6000"
           print("Your fees less 6000 ")
           student_first_sem_fees[i] = student_first_sem_fees[i]-6000
           student_Scholarship[i] = "6000 Scholarship "
           student_Scholarship[i]  = student_Scholarship[i].upper()
    else :
        print("No Scholarship")
print("\n")
#********************Task complete*******************

s6 = "student first sem data"
print(s6.title()) 


print("\n")
for i in range(len(student_id)):

    print("*********************************************************************************************************************************")
    print(f"Student Name = {student_name[i]}")
    print(f"Student Father Name = {student_father_name[i]}")
    print(f"Student Id = {student_id[i]}")
    print(f"Student First Mid Term Marks={student_first_mid_score[i]}")
    print(f"Student Second Mid Term Marks={student_second_mid_score[i]}")
    print(f"Student Back Log = {student_back_log[i]}")
    print(f"Student fees Details = {student_first_sem_fees[i]}")
    print("*********************************************************************************************************************************\n")

#********************Task complete*******************
print("\n")  

student_record = {
   " student_name" : student_name,
   " student_father_name" :student_father_name,
    "student_id"   :student_id,
    "student_branch" : student_branch,
    "student_first_mid_score ":student_first_mid_score,
    "student_second_mid_score" :student_second_mid_score ,
    "student_first_sem_fees" :student_first_sem_fees ,
    "student_gender" :student_gender ,
    "student_back_log" : student_back_log,
    "student_Scholarship" :student_Scholarship,
}

print(student_record)
print("\n")

print(student_record.keys())
print("\n")

print(student_record.values())
print("\n")

print(student_record.items())
print("\n")


