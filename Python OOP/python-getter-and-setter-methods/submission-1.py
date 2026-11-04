class BankAccount:
    def __init__(self, balance: int):
        pass  # Add private balance
        self.__balance = balance
    
    # TODO: Add getter method for balance
    def get_balance(self):
        return self.__balance

    # TODO: Add setter method for balance
    def set_balance(self, new_level):
        if new_level >= 0:
            self.__balance = new_level
        else:
            print("Cannot set negative balance!")

# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
