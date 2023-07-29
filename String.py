#String is collection of charector
#string is imutable data type
name = "arjun"
print(name)
print(type(name))

#forward indexing
print(name[0])

#backword indexing
print(name[-1])

#string slicing
print(name[::-1])
print(name[3:7:1])
print(name[-4:-8:-1])

#operator
data = "  this is my first class:"
print(data)

print(data.strip())

print(data.split())

print(data.upper())

print(data.lower())

print(data.capitalize())

print(data.title())

print(data.islower())

print(data.isupper())

print(data.isalpha())

print(data.isdigit())

print(data.count('i'))

print(data.index('c'))

print(data.find('c'))

print(data.replace('class','b.tech'))

print(len(data))

print('class' in data)
print('b.tech' in data)
print('b.tech' not in data)

_name = "my name is arjun and my age {0}"
age = 90
print(_name.format(age))








