#Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.


def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

obj = fib()
for i in range(10):
    print(next(obj))
    