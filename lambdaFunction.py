def add(a,b):
    return a+b
print(add(12,43))

#lambda function

add = lambda a,b:a+b
print(add(123,54))

maxi = lambda a,b:a if a>b else b
print(maxi(12,43))

c_to_f = lambda c:(9/5)*c+32
print(c_to_f(50))

name = "arjun singh"
data  = lambda name:name.upper()
print(data(name))

length = lambda name:len(name)
print(length(name))
