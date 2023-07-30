student_id = ['S01','S02','S03','S04','S05']
gender = ['M','F','M','F','M']
dept = ['CSE','ME','CSE','CSE','Civil']
sessional_per = [54,60,73,65.76,71.23]
total_marks = [680,800,760,650,680]
back_log = [False,True,False,False,False]


#Task -
#       If any student has received more than 70% in their sessional, increase the total marks by 2%

for i in range(len(student_id)):
    if sessional_per[i]>70:
        total_marks[i] = total_marks[i]+total_marks[i]*0.02
    else:
        print("Marks did not change")
print(total_marks)

#Task -
#      S01 and S04 have got Backlogs and we need to update them
print("Before",back_log)

update_back_log = ['S01','S04']
for i in range(len(student_id)):
    if student_id[i] in update_back_log:
        back_log[i] = True

print("After",back_log)

# Task -
#       If a student's total marks is greater than 750 and they have no backlog and they are from CS dept, they will receive a 'High Achiever Scholarship'.
#       If a student has no backlog and has marks between 650 and 720, they will receive 'Achiever Scholarship'

print(dept)
print(back_log)
print(total_marks)

print("\n")

scholarship = ['no scholarship' for _ in range(len(student_id))]
print(scholarship)
print("\n")

for i in range(len(student_id)):

    if total_marks[i]>750 and back_log[i]==False and dept[i]=='CSE':
        scholarship[i] = 'High Achiever Scholarship'

    elif total_marks[i]>=650 and total_marks[i]<=720 and back_log[i]==False:
        scholarship[i] = 'Achiever Scholarship'

    else:
        scholarship[i] = 'No Scholarship'

print(scholarship)


student_record = {
    'student_id':student_id,
    'gender':gender,
    'department':dept,
   'sessional_per':sessional_per,
   'total_marks':total_marks,
   'back_log':back_log,
   'scholarship':scholarship
}
print("\n")

print(student_record)

print("\n")
print(student_record.keys())

print("\n")
print(student_record.values())

print("\n")
print(student_record.items())

for k,w in student_record.items():
    print(w)

print('sessional_per' in student_record)