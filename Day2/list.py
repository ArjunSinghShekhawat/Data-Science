l = [1,2,'arjun',True,23.65,"singh"]
print(type(l))

print(l[0])
print(l[1])
print(l[-5])
print(l[-2])

# print(l[90])

#slice concept available in list
print(l[0:3:1])
print(l[-1])

print(l[::-1])
print(l[::2])
print(l[1::2])

s = "arjun"
# print(l+s)
print(l+list(s))
print(l)

print(l[2][0:2])
print(str(l[2])[0:2])


print(l[3])

list1 = ["arjun",10,True,"singh",54.978,False]
# print(list1)
# print(type(list1))

# print(list1[0])
# print(list1[2])
# print(list1[4])
# print(list1[5])

# print(list1[-2])
# print(list1[-3])
# print(list1[-4])

# print(list1[::-1])
# print(list1[0::2])
# print(list1[2::3])


list2 = [12,34,'arjun']
# print(list1+list2)
# # print(list1+1)

# str = "arjun"
# print(list1+list(str))

# print(list1)
# print(list1[3])
# print(list1[3][0:2:1])
# print(list1[2])


print(str(list1[2])[0:2])

# print(str(list1[2])[0:2:1])

print(list1*5)

print(len(list1))
print(list1)

list1.append(5)
print(list1)

list1.append("manjeet")
print(list1)
list1.append(list2)
print(list1)
print(list1[-1][1:2:])
print(list1)

list1.extend("arjun")
print(list1)

print(list1)


l = [12,23,45]
print(l)

l.insert(0,"arjun singh")
print(l)

l.insert(2,[12,34,65,"manjeet"])
print(l)

l.insert(-1,"pooja")
print(l)

print(l.pop())
print(l)

print(l.pop())
print(l)

print(l)
print(l.pop(2))
print(l)

l.remove(12)
print(l)

# l.remove(23)
# print(l)

l1 = [21,43,'arjun']
l2 = [43.76,78,'singh']

print(l1)
print(l2)

print(l1+l2)

l3 = [1,2,3,4,5]

l1.append(l3)
print(l1)

print(l1[3])
l1[3].remove(3)
print(l1)

print(l1[2])
# l1[2][3:5:1].remove()#error
print(l1)

print(l1)

print(l1[::-1])
print(l1)

l1.reverse()
print(l1)

li1 = [1,2,8,7,5,6,7]
print(li1)

li1.sort()
print(li1)

name = ['arjun','arjun','ankit','anshu']
print(name)

name.sort()
print(name)

name.sort(reverse=True)
print(name)

print(name.index("arjun"))

print(name.count("arjun"))

str = "arjun"
str = str.replace('a','Z')
print(str)












