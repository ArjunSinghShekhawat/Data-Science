l = [1,2,3,4,5,6,7,8,9]
l1 = []
for i in l :
    print(i+1)
    l1.append(i+1)
print(l1)

l2 = ["arjun","manjeet","pooja"]
l3 = []

for i in l2 :
    l3.append(i.upper())
print(l3)
list1 = [1,2,12.43,16.45,3,4,4,"arjun","pooja",65,43,56]
list2_num = []
list3_str = []

for i in list1 :
    if type(i)==int or type(i)==float :
        list2_num.append(i)
    else :
        list3_str.append(i)       

print(list2_num)
print(list3_str)


    


