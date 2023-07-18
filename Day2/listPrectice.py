list1 = ["arjun",True,12,43.65,123,"singh",'arjun']
print(list1)
print(type(list1))

#forward accessing
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])
print(list1[5])

#backward accessing
print(list1[-1])
print(list1[-2])
print(list1[-3])
print(list1[-4])
print(list1[-5])
print(list1[-6])

#basic operation
print(list1.count("arjun"))
print(list1.index('singh'))

#slicing concept
print(list1[0:4:1])
print(list1[2::2])

print(list1)
print(list1[::-1])

# print(list1+"arjun singh")
print(list1+list("arjun singh"))

print(list1)

list1.append("arjun singh")
print(list1)

list1.extend("manjeet")
print(list1)

# list1.extend(2)
# print(list1)

list2 = [12,86,4,98,23,98]
print(list2)

list2.sort()
print(list2)

list2.sort(reverse=True)
print(list2)


list3 = [12,43,54.675,"arjun"]
list4 = [43,67,"manjeet"]

print(type(list3))
print(type(list4))


print(list3+list4)

list3.append(list4)
print(list3)

print(list3[4])
print(list3[4][1])
print(list3[4][2])

print(list3[4][2])

print(list3[3])
print(list3[3][0:2])

print(list4)
list4.remove(43)
print(list4)
list4.pop(0)
print(list4)



