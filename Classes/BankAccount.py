class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount < 0:
            print("invalid amount")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
                print("Insufficient funds")
        elif amount < 0:
                print("invalid amount")
        else:
            self.balance -= amount


account = Account("John Smith", 1000)
print(account.balance)
account.deposit(500)
print(account.balance)
account.withdraw(-2000)
print(account.balance)