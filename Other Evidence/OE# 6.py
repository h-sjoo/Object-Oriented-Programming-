class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid! Must be positive")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid Withdraw!")
    def display_account_info(self):
        print(f"Your Account Number: {self.__account_number} \nCurrent Balance: {self.__balance}")
    def get_account_number(self, account_number):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    def set_balance(self, balance):
        if balance >= 0:
             self.__balance = balance
        else:
         print("Invalid balance. Balance must be non-negative.")

money = BankAccount(120805, 10000)
money.display_account_info()
money.deposit(float(input("Deposit Amount: ")))
money.display_account_info()
money.withdraw(float(input("Withdraw Amount: ")))
money.display_account_info()
money.set_balance(float(input("Set Balance: ")))
money.display_account_info()
