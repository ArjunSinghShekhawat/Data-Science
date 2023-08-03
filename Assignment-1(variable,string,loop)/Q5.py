# Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many
# times it can be divisible.

num1 = 21
num2 = 3
count = 0
while num1>=num2 and num1%num2==0:
    count+=1
    num1 = num1//num2
print("Times :",count)