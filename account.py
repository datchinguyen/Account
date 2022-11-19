class Account:
    def __int__(self,name):
        self.__account_name = name
        self.__account_balance = 0
    def deposit(self, amount):
        if amount <= 0:
            de = False
            pass
        else:
            self.__account_balance += amount
            de = True
        if de:
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__account_balance:
            de = False
            pass
        
        else:
            self.__account_balance -= amount
            de = True

        if True:
            return True
        else:
            return False

    def get_balance(self):
        return self._account_balance

    def get_name(self):
        return self._account_name
            
