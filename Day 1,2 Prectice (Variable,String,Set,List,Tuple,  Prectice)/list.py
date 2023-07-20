#list data type
l1 = ["arjun",12,678.987,"singh",True,False,"shekhawat",23+7j]

print(l1)
print(type(l1))

#forward indexing
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[6])

print("\n")

#backward indexing
print(l1[-1])
print(l1[-2])
print(l1[-3])
print(l1[-6])
print(l1[-4])

#sliceining
print(l1[::-1])

print(l1[::2])

print(l1[:0:-1])

print(l1[0][:3:1])

print(l1[7].real)
print(l1[7].imag)

print(l1[6][5::1])

# print(l1[90]) list index out of range

l2 = [12,43,65,87]
print(l2)

#mutable
l2[2] = "arjun"

print(l2)

str = "pwSkill"
# print(str+l2)
print(list(str)+l2)

print(l1+l2)


print(l2)
l2.append("java")
print(l2)

l2.append("data science")
print(l2)

l2.extend("DSA")
print(l2)

l3 = [12,43,True,False]
print(l3[2])

print(len(l1))
print(l1.count('arjun'))
print(l1.index('arjun'))

l5 = [12,43,23+87j,"arjun","java",32.65,(1,2,3,4,5,6),["pooja","Manjeet","arjun"]]

print(l5)


print(l5[-1][1])
print(l5[-2][3])

l6 = [{1,2,3,4},["java","data science","web development"],(1,2,3,4,5)]
print(l6)

l5.insert(0,"ramkishor")
print(l5)


print(l5.pop())

l6 = [12,34,56,"arjun"]
print(l6.pop())

print(l6.pop())

print(l6)

l6.remove(12)
print(l6)

l7 = [2,6,4,8,9,56,12]
l7.sort(reverse=True)

print(l7)

l7.clear()
print(l7)

l8 = [1,4,3,7,True,"arjun",[1,2,3]]

# l8[5].remove(2)
# l8[5].remove(1)

# print(l8)
l8.reverse()
print(l8)

l9 = [1,2,3,6,5]

#String in imutable
s1 = "arjun"

print(s1[0])

print(s1.replace('a','z'))
print(s1)

s1 = "1rjun"
print(s1)

print(l9)
l9[2] = "singh"

print(l9)