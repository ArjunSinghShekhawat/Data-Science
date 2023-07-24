# def test():
#     print("my function is started ")
#     print(12+90)
#     print("My function is end")
# test()

# def deco(func):
#     def inner_deco():

#         print("my function is started ")
#         func()
#         print("My function is end")

#     return inner_deco
# @deco
# def test2():
#     print(12+900)

# test2()

# @deco
# def test3():
#     print(200-90)

# test3()

#time
import time
def dec(func):
    def inner_dec():
        start = time.time()
        print(start)
        func()
        end = time.time()
        print(end)
        print(end - start)
    return inner_dec
@dec
def name():
    for i in range(1000):
        pass
name()