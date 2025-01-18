class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount <= 0:
            print("You can only deposit an amount greater than zero")
        else:
            result = self.account_balance + amount
            print(f"Deposited: ${result}")
    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("You can only withdraw an amount greater than zero")
        else:
            result = self.account_balance - amount
            print(f"Withdrew: ${result}")
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")
        
account = BankAccount(100)
account.display_balance()