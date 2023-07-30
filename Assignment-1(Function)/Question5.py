# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.

def isPrime(num):
    i = 2
    while i<num:
        if num%i==0:
            break
        else:
            return True
        i = i+1
    return False

def prime_number():
    n = 2
    while True:
        if isPrime(n):
            yield n
        n = n+1
obj = prime_number()

ans = [next(obj) for _ in range(20)]
print(ans)