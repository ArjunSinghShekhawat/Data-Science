n  = 3
p = 2

def test(n,p):
    return n**p
print(test(3,2))

#lamda function

a = lambda n,p :n**p#anonymus function

print(a(3,2))

add = lambda a,b : a+b
print(add(12,88))


c_to_f = lambda c:(9/5)*c+32
print(c_to_f(45))


find_max = lambda x,y: x if x>y else y
print(find_max(19,89))

s = "arjun"

length = lambda s :len(s)
print(length(s))







