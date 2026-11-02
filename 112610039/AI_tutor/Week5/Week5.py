class BankAccount():

    account_counter = 1000

    def __init__(self, owner, balance=0.0):
        if balance < 0:
            raise ValueError
        self.owner = owner
        self.balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1

    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.account_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Insufficient funds or invalid amount")
        self.balance -= amount

    def __str__(self):
        return f"Account {self.account_number} - Owner: {self.owner}, Balance: {self.balance}"

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance=0.0, interest_rate=0.02):
        BankAccount.__init__(self, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self):
        return f"SavingsAccount {self.account_number} - Owner: {self.owner}, Balance: {self.balance}, Rate: {self.interest_rate}"
