class BankAcc:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance        # Private attribute
    #@getter and setter methods
    #@property
    #def balance(self):
     #   return self.__balance

   # @balance.setter
   # def balance(self, amount):
   #     if amount < 0:
   #         print("Error: Balance cannot be negative!")
   #     else:
    #        self.__balance = amount
    def deposit(self, amount):  #getters and setters can also be used at this point for later updations
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number
    
# Example usage:
acc = BankAcc("123456789", 1000)
acc.deposit(500)
acc.withdraw(200)
