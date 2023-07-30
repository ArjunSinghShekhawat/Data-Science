# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
# function.

#Generator function is not store data so the generator function generate the value one by one and take by yield keyword
#Yield keyword is used to take current data gererate by generator function.

def fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b

for i in fib(10):
    print(i)
    