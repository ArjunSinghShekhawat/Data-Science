#Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.


ans = [i for i in list(range(1,101)) if i%2!=0]
print(ans)

