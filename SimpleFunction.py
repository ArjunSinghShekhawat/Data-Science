#function is a set of instruction

def demo():
    pass


def test1():
    print("Hy everyone!")
test1()


def test2():
    return 'hellow ji kese ho aap sb log'
test2()
print(test2())

def test3():
    return 11,22,'arjun','manjeet',[12,43,56]
print(test3())

def add(a,b):
    return a+b

print(add(12,43))
print(add("arjun",' singh'))



def test4():
    ans = 12+90/54
    return ans
print(test4())


def test5(a,b,c):
    d=a+b/c
    return d
print(test5(123,43,54))


def test6(*args):
    return args
print(test6([12,32,43,"ajun"],(123,43,56),"manjeet"))


def test7(*args,a):
    return args,a
print(test7(12,43,56,"manjeet",a=90))


def test8(a,b,c=900):
    return a,b,c
print(test8(12,34,657))


def test9(**kwargs):
    return kwargs

print(test9(a=90,name="arjun",marks=12.54))






