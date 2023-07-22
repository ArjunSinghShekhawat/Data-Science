print(range(10))

for i in range(10):
    print(i)

    def fib():
        a,b = 0,1
        while True :# for i in range(n):
            yield a
            a,b = b,a+b

# print(fib(10))
obj = fib()

print("\n")
for i in range(10):
    print(next(obj))

s = "arjun"

s=iter(s)
print(type(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))


def count_print(n):
    count = 1
    while count<=n:
        yield count
        count = count+1

print("\n")
obj1 = count_print(10)

for i in obj1:
    print(i)

# iter(11)


"""
Prectice 

"""

print(range(10))

for i in range(10):
    print(i)

def fib_1():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b
print("\n")
obj_1 = fib_1()

for i in range(10):
    print(next(obj_1))


_name = "manjeet"
print(_name)
print(type(_name))

_name = iter(_name)

print(type(_name))

print(next(_name))
print(next(_name))
print(next(_name))
print(next(_name))

def fib_2(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fib_2(10):
    print(i)

print("\n")
def count_num(n):
    count_num = 1
    while count_num<n:
        yield count_num
        count_num  = count_num+1

for i in count_num(10):
    print(i)

a = 10

a = iter(10)

