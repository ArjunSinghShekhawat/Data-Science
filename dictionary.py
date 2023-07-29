# dictionary - dictionary is a collection of key and vakue.
#it is mutable

d1 = {'key':'value'}
print(d1)
print(type(d1))

d1 = {'name':"arjun",'email_id':'arjun@gmail.com','phone_no':8005792198}
print(d1)

print(d1['name'])
print(d1['email_id'])
print(d1['phone_no'])

d1['name'] = 'anshu'
d1['email_id'] = 'anshu@gmail.com'
d1['phone_no'] = 6376129260

print(d1['name'])
print(d1['email_id'])
print(d1['phone_no'])

print(d1)

d2 = {'assignment':[2,3,4,5,6],'score':(2,5,7,3,2),'quiz':{1,2,3,4,5,5},'student_info':{'name':'arjun','email_id':'arjun@gmail.com','phone_no':521364789}}
print(d2)

print("\n")

print(d2.keys())
print("\n")
print(d2.values())
print("\n")
print(d2.items())
print("\n")

print(d2['assignment'])
print(d2['student_info']['email_id'])


for k,w in d2.items():
    print(k)

#duplicate is not allowed

d3 = {'name':'arjun','email_id':'arjun@gmail.com','name':'anshu'}
print(d3)

#namming convension
d4 = {123:'arjun','_email_id':'asnu@gmail.com',True:'course'}
print(d4)

#dict as a function
d5 = dict(name='arjun',email_id='anshu@gmail.com0',phone_no=8005792198)
print(d5)

print(type(d5))

#get function

d6 = {'student':'arjun','email_id':'a@gmailcom'}
a = d6['student']
print(a)

b = d6.get('email_id')
print(b)

d6['course'] = ['dsa','web','data science']
print(d6)

#key,values,items function
print(d6.keys())
print("\n")
print(d6.values())
print("\n")
print(d6.items())
print("\n")

print('course' in d6)

d6.update({'course':[12,34,65]})

print(d6)

d6.update({'assignment':[12,34,65]})

print(d6)

d6.popitem()
print(d6)
    

d6.pop('student')
print(d6)

del d6['course']

print(d6)

d6.clear()

print(d6)

d7 = {'name':"arjun",'email_id':'arjun@gmail.com','phone_no':8005792198}

for i in d7:
    print(d7[i])


for i in d7.values():
    print(i)

print("\n")

d8 = {'name':"arjun",'email_id':'arjun@gmail.com','phone_no':8005792198}
print(d8)

d9 = d8.copy()
print(d9)

d10 = dict(d9)
print(d10)

print('\n')

d11 = {
    'child1':{'name':'arjun','year':2002},
    'child2':{'name':'anshu','year':2012},
    'child3':{'name':'govind','year':2232},

}
print(d11)

print('\n')

key = ('key1','key2','key3')
value = 0

d12 = dict.fromkeys(key,value)
print(d12)