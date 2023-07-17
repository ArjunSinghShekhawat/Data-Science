#Using while loop verify if the number A division by B and if so then how many types it can be divisible.

A = int(input())
B = int(input())
count = 0

while A%B==0 :
    print("A division by B")
    A = A/B
    count+=1

print("The number A divided by B",count,"times")




