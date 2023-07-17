#Q6.What is mutable and imutable data type explain with example

# Mutable data type -> In mutable data type re-assignment of data at a perticular index this concept is called mutability for example list.
# Imutable data type-> In imutable data type re-assignment of data at a perticular index is not allowed this concept is called imutability for example string , tuple,

# Mutable example ->
list = ['java','python','c++',12,65,76.87]
print(list)
print(type(list))

print(list[3])
print(list[-4])

list[2] = 'data science'
print(list)

list[1] = 'arjun'
print(list)

#Imutable example ->
name = 'arjun'
print(name)
print(type(name))

print(name[1])
print(name[-2])

#occure error for re-assignment
name[2] = 'w'
print(name)

