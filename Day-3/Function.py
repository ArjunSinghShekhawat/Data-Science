#Function
print("This is my function class")

l1 = [1,2,3,4,5]
print(type(l1))
print(len(l1))

print("\n")

def test1():#initialization
    pass

def test2():
    print("This is my very first function ")

test2()
#reusability ,optimizataio,increase by function

# print(test2()+'arjun') None type

def test3():
    return "arjun",12,12+9j

print(test3())

a,b,c = test3()
print("arjun ji",a,b,c)


def test4():
    return "arjun singh"

print(test4())
print(test4()+" shekhawat")

def test5():
    a = 2+6/2
    return a
print(test5())

def test6(a,b,c):
    d = a+b/c
    return d
print(test6(12,43,5))


def test7(a,b):
    return a+b
print(test7(12,43))
print(test7("arjun"," singh"))

li1 = [1,2,3,4,5,"arjun",[11,22,33,44,55],12.54,56,56,54]
l2 = []
def test8(li1):
    """ doc stream
    fun work seprate int and float number"""
    for i in li1:
        if type(i)==list:
            for j in i:
               if type(j)==int or type(j)==float:
                l2.append(j)
        else :
            if type(i)==int or type(i)==float:
                l2.append(i)
    return l2

print(test8(li1))
print(l2)
# l2 = []

# def test8(li1):
#     for i in li1:
#         if type(i)==int or type(i) == float:
#             l2.append(i)
#     return l2


# print(test8(li1))
# print(l2)

def test9(*args):
    return args

print(test9(1,2,3,4,5))
print(test9("arjun","singh"," shekhawat"))
print(test9(1,2,3,[1,2,3,"arjun"],{1,1,2,3,3,2},(1,2,3)))

def test10(*args,a):
    return *args,a

print(test10(1,2,3,4,5,a="arjun"))

def test11(c,d,a=12,b=90):
    return a,b,c,d
print(test11(12,23))
print(test11(121,233,23,43))


def test12(**kwargs):
    return kwargs

print(type(test12()))
print(test12(name = 'arjun',b = 12,c = [1,2,3]))


"""
Function Prectice

"""
print("Hellow i am arjun!")
list1 = [1,2,3,4,"arjun"]

print(type(list1))
print(len(list1))

def demo():
    pass

def demo1():
    print("This is my function first class!")

demo1()

def demo2():
    return "arjun"

print(demo2()+" singh")

def demo3():
    return 12,23,"manjeet",87+9j,True

print(demo3())

def demo4():
    a = 12+98/23
    return a
print(demo4())

def demo4(a,b,c):
    d = a+b/c
    return d
print(demo4(12,43,56))

list2 = [1,2,"anshu",3,4,5,(11,22,33,44,55,12.65,"manjeet","pooja"),[121,232,"rekha",456,12.54,76,"arjun"],"govind"]
list3 = []
list4 = []

def demo5(list2):

    for i in list2 :
        if type(i)==list or type(i)==tuple :
            for j in i :
                if type(j)==int or type(j)==float :
                    list3.append(j)
                else :
                    if type(j)==str :
                        list4.append(j)
        else :
            if type(i)==int or type(i)==float :
                list3.append(i)
            else :
                if type(i)==str:
                    list4.append(i)

    return list3,list4

print(demo5(list2))

print(list3)
print(list4)

def demo6(*args):
    return args

print(demo6(1,2,3,4,[6,5,4],("arjun",54.65)))

def demo7(*args,a):
    return args,a
print(demo7(1,2,3,("arjun","singh"),12,a=900))

def demo8(**kwargs):
    return kwargs

print(demo8(a=90,b="arjun",course=["web",'dsa','data science']))


def demo9(a,b,c=9000,d=98000):
    return a,b,c,d

print(demo9(12,23))
print(demo9(11,122,133,1555))
