class Account:
    """
    A class representing details for an account object
    """
    
    def __init__(self, name: str) -> None:
        """
        Constructor to create initial state of an account object
        :param name: Account's name
        
        """
        self.__account_name = name
        self.__account_balance = 0
        
    def deposit(self, amount: int):
        """
        Method to check the amount 
        :return True or False
        """
        
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

    def withdraw(self, amount: int):
        """
        Method to check amount
        :return True or False
        """
        
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

    def get_balance(self) -> int:
        """
        Method to access a account's name
        :return: Account's name
        """
        
        return self._account_balance

    def get_name(self) -> str:
        """
        Method to access a account's name
        :return: Account's name
        """
        
        return self._account_name
            
