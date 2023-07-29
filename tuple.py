#tuple-tuple is collection of multipe data type .Tuple is not changeble but it is available index base accessing.
#tuple is imutable data type

t1 = ()
print(t1)
print(type(t1))

t2 = (1,2,3,"arjun",12.98,43+90j,True)
print(t2)

print("\n")

#forward indexing
print(t2[0])
print(t2[1])

print("\n")

#backword indexing
print(t2[-1])
print(t2[-2])

#slicing

print(t2[::-1])
print(t2[-3:-1:-1])
print(t2[3::2])

#operation
print(t2.index('arjun'))

print(t2.count('arjun'))

print(len(t2))

t3 = (11,23.54,'govind',[11,22,"manjeet",'java'],('data',12.54,True),{11,22,33,33,22,11},{'key':'value'},True,"data")
print(t3[2][0:3])
print(t3[3][2][0:4:1])

print(t3[4][0][0:2:1])

print(str(t3[4][2])[0:2:1])

print(t3[6]['key'])