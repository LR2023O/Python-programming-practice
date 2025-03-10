#Encapsulation in python
class BankAccount:
    def __init__ (self, balance, name, number):
        self._balance = balance
        self.name = name
        self._number = number
    def deposit(self, amount):
        self._balance +=amount
        return f"Deposited: {amount}"
    def get_balance(self):
        return f"New Balance: {self._balance}"
    
account = BankAccount( 1500, "John", 1234)
#print(account._balance)
print(account.name)
print(account._number)

print(account.deposit(2000))
print(account.get_balance())
