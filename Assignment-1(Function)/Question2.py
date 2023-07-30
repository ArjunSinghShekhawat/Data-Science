# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.


#ans. *args is used to take multiple input like list,tuple,int,float,str etc and **kwargs is used to take key
# and value pair like dict .


def first(*args):
    return args

print(first(1,'arjun',12.43,True,[1,2,3],('java','dsa')))

def second(**kwargs):
    return kwargs
print(second(name='arjun',email_id = 'arjun@gmail.com'))

