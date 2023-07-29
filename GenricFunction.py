def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b = b,a+b

for i in fib(10):
    print(i)

def fib1():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b
obj = fib1()
for i in range(10):
    print(next(obj))


print("\n")

#counting print
def counting(n):
    count = 1
    while count<=n:
        yield count
        count = count+1
for i in counting(10):
    print(i)

print(iter(obj))
print(iter('name'))
print(obj)

