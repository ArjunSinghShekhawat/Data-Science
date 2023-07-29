#List is collection of multiple data type
#list is mutable data type

list1 = [1,2,3,'arjun',90+9j,True]
print(list1)
print(type(list1))

print("\n")

#forward indexing
print(list1[0])
print(list1[1])

print("\n")

#backword indexing
print(list1[-1])
print(list1[-2])

print("\n")
#mutability
list1[0] = 'data science master'

print(list1)

print("\n")

list2 = [12,23.54,54+90j,True,"arjun",[11,22,33,44,"manjeet",True,89+9j],("data sciece","java with dsa",123,True,False,78+9j)]
print(list2)

list_number = []
list_str = []

for i in list2:
    if type(i)==list or type(i)==tuple:
        for j in i:
            if type(j)==int or type(j)==float or type(j)==complex:
                list_number.append(j)
            else:
                list_str.append(j)
    else:
        if type(i)==int or type(i)==float or type(i)==complex:
                list_number.append(i)
        else:
                list_str.append(i)
print(list_number)
print(list_str)


#operation

print(list1+list("arjun"))

list1.append("anshu")
print(list1)

list1.extend("manjeet")
print(list1)

list1.insert(3,"java with system design")
print(list1)


print(list1.count('anshu'))

print(list1.index('anshu'))

list1.reverse()
print(list1)

print(list1.pop())
print(list1)

print(list1.pop(2))
print(list1)

list1.remove('arjun')
print(list1)

del  list1[-3]

print(list1)

list1.clear()

print(list1)

list3 = [1,23.65,"arjun",True,[11,22,"arjun",True],(11,22,33,"data science"),{1,2,3,4,4,3,2,1},{'key':'value'}]
print(list3)

print(list3[4][0:2:1])
print(list3[4][2][0:3])
print(str(list3[4][3])[0:2])

print(list3[2][0:3])


print(list3[5][3][0:3:1])
print(list3[-1]['key'])

