# Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.

list1 = list(range(1,26))

for i in list1:
    if i%3==0:
        print(i," divisible by 3 ")
    else:
        print(i," not divisible by 3")
