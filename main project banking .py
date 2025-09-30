import random
from datetime import datetime

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, name, initial_balance):
        account_number = self.generate_account_number()
        pin = self.generate_pin()
        account = Account(account_number, name, initial_balance, pin)
        self.accounts[account_number] = account
        return account_number, pin

    def generate_account_number(self):
        return random.randint(10000000, 99999999)

    def generate_pin(self):
        return random.randint(1000, 9999)

    def authenticate(self, account_number, pin):
        if account_number in self.accounts:
            return self.accounts[account_number].pin == pin
        return False

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
            return True
        return False

    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        if account:
            return account.withdraw(amount)
        return False

    def check_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.balance
        return None

    def get_transaction_history(self, account_number):
        account = self.get_account(account_number)
        if account:
            return account.transaction_history
        return None

class Account:
    def __init__(self, account_number, name, initial_balance, pin):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance
        self.pin = pin
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append((datetime.now(), 'Deposit', amount))
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append((datetime.now(), 'Withdrawal', amount))
            return True
        return False

bank = Bank("My Bank")

while True:
    print("\n==== Main Menu ====")
    print("1. Create Account")
    print("2. Perform Transactions")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please choose again.")
        continue

    if choice == '1':
        name = input("Enter your name: ")
        initial_balance = float(input("Enter initial balance for {}: ".format(name)))
        account_number, pin = bank.create_account(name, initial_balance)
        print("Account created successfully!")
        print("Your account number is:", account_number)
        print("Please remember your PIN:", pin)
        
    elif choice == '2':
        while True:
            action = input("\nChoose action (deposit/withdraw/exit): ").lower()
            if action == 'exit':
                break
            while True:
                account_number = int(input("Enter your account number: "))
                pin = int(input("Enter your PIN: "))
                if bank.authenticate(account_number, pin):
                    break
                print("Authentication failed. Please try again.")
            if action == 'deposit':
                amount = float(input("Enter amount to deposit: "))
                if bank.deposit(account_number, amount):
                    print("Deposit successful. Current balance:", bank.check_balance(account_number))
                else:
                    print("Deposit failed. Please enter a valid amount.")
            elif action == 'withdraw':
                amount = float(input("Enter amount to withdraw: "))
                if bank.withdraw(account_number, amount):
                    print("Withdrawal successful. Current balance:", bank.check_balance(account_number))
                else:
                    print("Withdrawal failed. Insufficient funds or invalid amount.")
            else:
                print("Invalid action. Please choose deposit or withdraw.")
    
    elif choice == '3':
        print("Exiting the program. Thank you!")
        break


