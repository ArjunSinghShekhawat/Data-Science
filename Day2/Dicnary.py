# d1 = {}
# print(d1)
# print(type(d1))


# d2 = {"Name" : "Arjun", "email" : "shekhawat123@gmail.com", "PhoneNo" : "12354"}
# print(d2)

# # d3 = {$key : "anshu"}
# d3 = {123 : "arjun"}

# print(d3)

# d4 = {True : "manjeet"}
# print(d4)

# print(d3[123])
# print(d4[1])

d5 = {'name' : "arjun","email" :"singh123","name" : "manjeet"}

print(d5["name"])


d6 = {"company" :"pwskill","course" :["java","dsa","data science"]}

print(d6)
print(d6["course"][1])

d7 = {"number" : [2,4,6,8,10],"Assignment" :(1,2,3,4,5,6),"date" :{2,4,6,8},"classTime":{"web":"2.00","dsa":"3.00"}}
print(d7["classTime"]["dsa"])

d7["mentor"] = ["arjun","manjeet","anshu"]

print(d7)

print(list(d7.keys()))
print(list(d7.values()))

print(list(d7.items()))

