# Q7. What do you understand about mutable and immutable data types? Give examples for both showing
# this property.

# mutable -> mutable data type is list because in list re-assignment is allowed at a perticular index .
# imutabile-> imutable data type is string because in string re-assignment is not allowed at a perticular index.

name = "arjun"
print(name)
print(type(name))

# name[0] = 'w' error because it is imutable data type

list1 = [1,2,3,True,"arjun"]
print(list1)
print(type(list1))

list1[0]='data science'#re-assignment is allowed because it is mutable
list1[1] = 'big data'

print(list1)