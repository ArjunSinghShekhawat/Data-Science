list1 = [12,54,23,65.909,"arjun",23+54j,True,124,"manjeet"]

print(list1)
print(type(list1))

print(list1[5])
print(list1[5].real)
print(list1[5].imag)

print(list1[0])
print(list1[1])

print(list1[-2])
print(list1[-3])

print(type(list1))

# # print(list1[20])  list index out of range

#slicing
print(list1[0:3])
print(list1[::-1])
print(list1[-1])
print(list1[0::2])

print(list1)

str = "arjun"

# print(list1+str) can only concatenate list (not "str") to list

print(list1+list(str))

print(list1)
print(type(list1[4]))

print(list1[4][0:3:1])


print(str(list1[6])[0:3:1])

print(list1[3])
print(str(list1[3])[0:3:1])


print(list1)

#print(list1+5) can only concatenate list (not "int") to list

list2 = [12,43,65,98,"arjun"]
print(list1+list2)


# print(list1*5)

list1.append("narpat")
print(list1)

list1.append(1)
print(list1)

list1.extend("arjun")
print(list1)

list2 = [12,43,76,"arjun"]
list1.append(list2)

print(list1)


list1.insert(2,"java")
print(list1)

list1.insert(1,list2)
print(list1)

list1.pop()
print(list1)

list1.remove(54)
print(list1)


list1.sort()
print(list1)


t = (1,2,3,4,5,6)
print(t)
print(type(t))


print(t.count(1))
print(t.index(3))

print(len(t))
print(t[::-1])
print(t[1::2])

# t[0] = 75 error

s = {}

print(type(s))
print(s)


s1 = {1,2,4,3,5,6,7,3,4,5,6}

print(type(s1))
print(s1)


s3 = {"arjun","manjeet",12,54}
print(s3)
print(type(s3))


s3.add(12)

print(s3)
