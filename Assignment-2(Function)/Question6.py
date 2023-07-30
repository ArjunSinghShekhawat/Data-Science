# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter
# function.
# ['python', 'php', 'aba', 'radar', 'level']

l1 = ['python', 'php', 'aba', 'radar', 'level']

print(list(filter(lambda s:s==s[::-1],l1 )))