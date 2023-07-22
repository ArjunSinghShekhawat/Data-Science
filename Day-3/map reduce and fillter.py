l = [1,2,3,4,5,6]

def test(l):
    l1 = []
    for i in l:
        l1.append(i**2)
    return l1

print(test(l))

def sq(x):
    return x**2

print(list(map(sq,l)))



print(list(map(lambda x : x**2,l)))


l2 = [1,2,3,4,5]
l3 = [6,7,8,9,10]

print(list(map(lambda x,y:x+y,l2,l3)))

def add(x,y):
    return x+y

print(list(map(add,l2,l3)))

s = "arjun"

print(list(map(lambda s : s.upper(),s)))


#reduce

from functools import reduce
l5 = [1,2,3,4,5]

print(reduce(lambda x,y:x+y,l5))
print(reduce(lambda x,y:x+y,[1]))
print(reduce(lambda x,y:x*y,l5))
print(reduce(lambda x,y:x if x>y else y,l5))

#fillter

l6 = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x : x%2==0,l6)))
print(list(filter(lambda x : x%2!=0,l6)))


l7 = [1,-9,-7,5,-3,4]

print(list(filter(lambda x : x<0,l7)))

l8 = ["arjun","manjeet","krish","rajhul"]

print(list(filter(lambda x:len(x)<6,l8)))

"""
Prectice

"""

a1 = [1,2,3,4,5,6]

def sq(a1):
    a2 = []
    for i in a1:
        a2.append(i**2)
    return a2
print(sq(a1))

def sq(a):
    return a**2

print(list(map(sq,a1)))

print(list(map(lambda a:a**2,a1)))

a3 = [1,2,3,4,5]
a4 = [6,7,8,9,10]

print(list(map(lambda x,y:x+y,a3,a4)))

# print(iter(7))
a5 = ["arjun","ankit","anshu","govind","kesav","hemlta","komal","rahul","narpat","rekha","pooja","manjeet"]
s = 'ar'
print(list(map(lambda s:s.upper().strip().split(),a5)))

#reduce
from functools import reduce

a9 = [1,2,3,4,5,6,7,8,9]

print((reduce(lambda x,y:x+y,a9)))
print((reduce(lambda x,y:x+y,[1])))

print(reduce(lambda x,y:x if x>y else y,a9))

#filter
a10 = [1,2,3,4,5,6,7,8,9,10]

print(list(filter(lambda x:x%2==0,a10)))
print(list(filter(lambda x:x%2!=0,a10)))