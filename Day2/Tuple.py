tuple = (1,2,3,4,"arjun",54.76,[12,43,"arjun"])
print(tuple)

print(tuple.count("arjun"))
print(tuple[0])
print(tuple[-1])

print(tuple.index(3))

print(len(tuple))

print(tuple[0:3:1])

# tuple[0] = "arjun"
tuple[0] = 12
print(tuple)
