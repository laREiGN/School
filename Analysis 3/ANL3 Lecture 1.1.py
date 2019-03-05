# class MyClass:
#     a = None   # a is public
#     __b = None   #b is private
#
#     def __init__(self, a, b):
#         self.a = a
#         self.__b = b
#
#     def pub(self):
#         print ('This is a public function.')
#         print ('a and b:', self.a, self.__b)
#
#     def __priv(self):
#         print ('This is a private function.')
#         print ('a and b:', self.a, self.__b)
#
#         def call(self):
#         print ('This is a call function.')
#         self.__priv()

#obj = MyClass(10,3)
#print(obj.a)    #can be accessed, as it is public
#print(obj.b)   #can not be accessed, as it is private

#obj.pub()   #can be accessed, as pub is public
#obj.priv()   #can again not be accessed, as __priv is private
#obj.__priv()   #can again not be accessed, as __priv is private
#obj.call()   #can be accessed, as it is a public function that calls a private function from the inside

#Practice

class BankAccount:
    __balance = None

    def __init__(self, bal):
        self.__balance = bal

    def checkbalance(self):
        print ('This is your current balance:', self.__balance)

    def deposit(self, a):
        self.__balance = self.__balance + a
        print ('You have deposited', a)
        print ('Your current balance is', self.__balance)

    def withdraw(self, a):
        if a < self.__balance:
            self.__balance = self.__balance - a
            print ('You have withdrawn', a)
            print ('Your current balance is', self.__balance)
        else:
            print ('This account does not have enough balance.')

    def transfer(self, target, amount):
        available = self.withdraw(amount)
        target.deposit(available)




bank = BankAccount(100)
bank2 = BankAccount(50)
#bank.withdraw(80)
#bank2.withdraw(80)
bank.transfer(bank2, 20)
