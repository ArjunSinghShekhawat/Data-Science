list1 = [1,2,3,4,5]
print(list1)
#map function

def add(a):
    return a**2
print(list(map(add,list1)))
print(list(map(lambda a:a**2,list1)))

print(list(map(lambda a:a+1,list1)))

list2 = [1,2,3,4,5]
list3 = [5,6,7,8,9]

print(list(map(lambda a,b:a+b,list2,list3)))

list4 = ['arjun','anshu','govind']
print(list(map(lambda s:s.upper(),list4)))


#reduce function
from functools import reduce

print(reduce(lambda a,b:a+b,list1))
print(reduce(lambda a,b:a*b,list1))

#filter function

list5 = list(range(1,26))
print(list5)

print(list(filter(lambda x:x%2==0,list5)))
print(list(filter(lambda x:x%2!=0,list5)))

