# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the
# filter function.
# [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

s1 = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

print(list(filter(lambda a:a%2==0 or a%3==0,s1)))