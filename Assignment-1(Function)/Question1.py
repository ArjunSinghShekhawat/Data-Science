# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.


#ans. The def keyword is used to create function.

list1 = list(range(1,26))
print(list1)

def OddNumber(list1):
    odd_number = []
    for i in list1:
        if i%2!=0:
            odd_number.append(i)
    return odd_number
print(OddNumber(list1))

