
#Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.

num1 = int(input("Enter the number :"))

reverse = 0
num = num1
while num>0:
    digit = num%10
    reverse = reverse*10+digit
    num = num//10

if reverse==num1:
    print("Palindrome ")
else:
    print("not Palindrome")
    



