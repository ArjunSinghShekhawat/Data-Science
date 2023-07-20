#String-> Collection of charactors
s1 = "data science "
print(s1)
print(type(s1))

#str follow forward and backword index accessing 

print("Forward accessing\n")

print(s1[0])
print(s1[1])
print(s1[2])
print(s1[3])
print(s1[6])
print(s1[7])
print(s1[8])

print("\nBackword accessing\n")

print(s1[-1])
print(s1[-2])
print(s1[-3])
print(s1[-4])
print(s1[-5])
print(s1[-8])
print(s1[-9])

#str follow slicining property
print(s1[0:3])#dat

print(s1[::-1])#reverse

print(s1[::2])#dt cec

print(s1[2:5:1])#ta

#print(s1[::0])#occure error slice step can not zero

print(s1[2:7:-1])#' ' arise confilict

print(s1[11::-1])#ecneics atad

print(s1[::])#data science

#print(s1[90])#str index out of range error occure

print(s1[:-90:])#print blank ' '

print(s1[:-90:-1])#reverse


#inbult function in string
s2 = "this is my string class"

print(s2)
print(type(s2))


print(len(s2))#length of str

print(s2.find('s'))#find char and str given first occurence
print(s2.find("is"))
print(s2.find("java"))#not present in str given -1

print(s2.upper())#Upper case

print(s2.lower())

print(s2.title())

print(s2.capitalize())

print(s2.count('i'))
print(s2.count('z'))#not present given 0

print(s2.index('i'))#given first occurence of index


#print(s2+1)#occure error can only concatenate str (not "int") to str

print(s1+s2)

#type casting
print(s2+str(123))

print(s2*5)

#print(s2/23)#do not work

s3 = "don't do copy and paste in my class"
print(s3)

"""
this is a code of string
data science , java, c++
this is multi line comment
"""

s4 = "manjeet"
print(s4)

#imutable 

# s4[0] = 'Z'
# print(s4)

s4 = "zanjeet"
print(s4)

print(s4.replace('z','M'))
print(s4)
