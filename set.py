#set - set is a collection of multiple data type . In which not index base accessing and remove duplicate data.
set1 = {}
print(set1)
print(type(set1))

set2 = {11,2,1,2,3,4,5,6,6,54,4,3,2,5,6,7,8}
print(set2)

#operation
set2.add('arjun')
print(set2)

set2.remove(11)
print(set2)

set2.clear()
print(set2)

s3 = {1,2,3,"arjun",(1,2,3,4)}
print(s3)


for i in s3:
    print(i)

print('arjun' in s3)

#add item
s3.add('manjeet')
print(s3)

l1 = ['apple','mango']

s3.update(l1)
print(s3)

#remove item

s3.pop()
print(s3)

s3.remove('apple')
print(s3)

del s3


a1 = {'1','2','3',4}
a2 = {'a','b','c',4}

a3 = a1.union(a2)
print(a3)

print(a1.intersection_update(a2))
