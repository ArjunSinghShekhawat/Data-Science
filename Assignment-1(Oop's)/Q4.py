# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.

"""
Setter - > setter in python is used to set the private data member class.
 Getter -> getter in python is used to get the private data member.

 """
class bank_account:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance = self.__balance+amount

    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance = self.__balance-amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self.__balance
    
arjun = bank_account(1000)
print(arjun.get_balance())
arjun.deposite(2000)
print(arjun.withdraw(1000))

 
