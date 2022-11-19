import pytest
from functions import *
    def test_get_name():
        assert __init__('Jane') == 'Jane'
        assert __init__('Joe') == 'Joe'
        assert __init__('Joe') != "Jane"
        
    def test_get_balance() :
        assert get_balance(1000) == 1000
        assert get_balance(500) == 500
        assert get_balance(500) != 1000
      
    
    def test_deposit():
        assert deposit(True) is True 
        assert deposit(False) is False 

    def test_withdraw():
        assert withdraw(True) is True
        assert withdraw(False) is False 
