# Q4. Write a python program using reduce function to compute the product of a list containing numbers
# from 1 to 25.

from functools import reduce

list1 = list(range(1,26))
print(reduce(lambda a,b:a*b,list1))