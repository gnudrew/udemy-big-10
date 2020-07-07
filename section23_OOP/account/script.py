class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as fp:
            self.balance = int(fp.read())

    def withdraw(self, amount):
        self.balance = self.balance - int(amount)

    def deposit(self, amount):
        self.balance = self.balance + int(amount)

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    type="checking"

    def overdraft(self, amount):
        print("Your account overdrafted by... "+str(amount))
        pass

act = Account("balance.txt")
print(act.balance)
act.withdraw(100)
print(act.balance)
act.deposit(200)
print(act.balance)
act.commit()

# chk = Checking("balance.txt")
# print(chk.balance)
# print(chk.overdraft(145))