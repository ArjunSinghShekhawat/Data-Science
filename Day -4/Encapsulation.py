class test:

    def __init__(self,a,b):
        self.a = a
        self.b = b

obj1 = test(11,22)
obj1.a = 12345

print(obj1.a)

class car:
    def __init__(self,year,make,model,speed):
        self.__year = year
        self.__make =make
        self.__model = model
        self.__speed = 0
    def set_speed(self,speed):
        self.__speed = 0 if speed<0 else speed

    def get_speed(self):
        return self.__speed
     
a1 = car(2021,"toyota","innova",12)
a1.set_speed(12)

print(a1.get_speed())

class bank_account :
    def __init__(self,balance) :
        self.__balance = balance

    def deposite(self,amount):
        self.__balance = self.__balance+amount

    def withdraw(self,amount):
        if self.__balance>=amount :
            self.__balance = self.__balance-amount
            return True
        else :
            return False
    def get_balance(self):
        return self.__balance

arjun = bank_account(1000)
print(arjun.get_balance())
arjun.deposite(1000)
print(arjun.get_balance())
arjun.withdraw(1500)
print(arjun.get_balance())
ans = arjun.withdraw(600)
print(ans)
print(arjun.get_balance())

class bank_account :
    
    def __init__(self,balance) :
        self.__balance = balance

    def deposite(self,amount) :
        self.__balance = self.__balance+amount
    
    def withdraw(self,amount) :
        if self.__balance>=amount :
            self.__balance = self.__balance-amount
            return True
        else :
            return False
    def get_balance(self) :
        return self.__balance

arjun = bank_account(10000)
print(arjun.get_balance())

# print(arjun.withdraw(20000))
print(arjun.withdraw(5000))
print(arjun.get_balance())
arjun.deposite(20000)
print(arjun.get_balance())





