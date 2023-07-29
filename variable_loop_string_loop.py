#Variable

age = 12
print(age)
print(type(age))

print("\n")

marks = 7576.4
print(marks)
print(type(marks))

print("\n")

is_prime = True
print(is_prime)
print(type(is_prime))

print("\n")

print(True+True)
print(False+False)
print(True+False)
# print(True/False)error


print("\n")

v1 = 12+9j
print(v1)
print(v1.real)
print(v1.imag)

v2 = complex(12,54)
print(v2)

v3 = complex(8)
print(v3)

print(type(v1))

print("\n")

a,b,c = 11,22,"arjun"
print(a,b,c)

list1 = [1,2,3,4,"manjeet"]
a,b,c,d,e = list1
print(a,b,c,d,e)

print("\n")

num = 900
def test1():
    num = 100
    print(num)

test1()
print(num)

print("\n")

num = 900
def test1():
    global num
    num = 100
    print(num)

test1()
print(num)

#operator

print(1+8)
print(89-23)
print(87/32)
print(78%23)
print(12//5)
print(2**10)

print("\n")

print(True>False)
print(True<False)
print(True>=False)
print(True<=False)
print(True==False)


print("\n")

print(True and True)
print(True and False)
print(False and False)
print(False and True)


print("\n")


print(True or True)
print(True or False)
print(False or False)
print(False or True)


print("\n")

print(not True)
print(not False)


print("\n")

print(0 and 1)
print(1 and 0)
print(0 and 0)
print(0 and 1)


print("\n")


print(1 or 1)
print(1 or 0)
print(0 or 0)
print(0 or 1)


print("\n")

print(not 1)
print(not 0)


print("\n")

print(12&23)
print(13|90)


print("\n")

print(10>>2)
print(23<<2)


print("\n")

print(bin(10))

#loop
name = "arjun"

for i in name:
    print(i)

print("\n")

#break
# i=1
# while i<=10:
#     if i==5:
#         break
#     print(i)
#     i = i+1
# print("\n")


#continues

for i in range(10):
    
    if i==5:
        continue
    print(i)

print("\n")

#break
for i in range(10):
    
    if i==5:
        break
    print(i)