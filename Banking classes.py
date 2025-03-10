class BankAccount:
    def __init__ (self, account_no, balance, date_of_opening, customer_name):
        self.account_no = account_no
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name  = customer_name
    def deposit(self,amount):
        self.balance += amount
        return f"Deposited amount: {amount}"
    def withdraw(self,amount):
        if amount>self.balance:
            return f"Insufficient balance"
        else:
            self.balance -=amount
            return f"Withdrawn: {amount}"
    def check_balance(self):
        return f"Current balance is: {self.balance}"
    def customer_details(self):
        return f"Customer details: Account number: {self.account_no}\n Name: {self.customer_name}\n Balance: {self.balance}\n Date of opening: {self.date_of_opening}"
account = BankAccount(1111222333444, 5000, "1st March 2024", "Larry")
print(account.deposit(2000))
print(account.withdraw(500))
print(account.check_balance())
print(account.customer_details())

