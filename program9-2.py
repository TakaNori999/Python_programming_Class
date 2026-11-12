class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Your balance is {self.balance}.")
        else:
            print("No balance..")
    def check_balance(self):
        print(f"Your balance is {self.balance}")
bankaccount = BankAccount("Taro", 10000)
bankaccount.check_balance()
bankaccount.deposit(5000)
bankaccount.check_balance()
bankaccount.withdraw(2000)
bankaccount.check_balance()