# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].


#ans iterator which data or variable access its next data by using next function is called iterator.The iter() method 
# to used initilize the iterator and this concept is used for loop the implimantation of for loop used iter().

list1 =  [2, 4, 6, 8, 10, 12, 14,16, 18, 20]
print(list1)

value = iter(list1)
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))
