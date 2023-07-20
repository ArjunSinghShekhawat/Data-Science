t = (1,2,3,4,"arjun",23.65,False,True,[1,2,3],3+8j)

print(t)
print(type(t))

print(len(t))

print(t[::-1])

print(t[::2])

print(t[2:5:1])

#tuple is imutable data type

print(t[3])


#not allow
# t[3] = "arjun"
# print(t[3])

print(t.count(2))
print(t.index(False))



