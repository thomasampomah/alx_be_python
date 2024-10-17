class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
            self.account_balance += amount
            print (f"Deposited ${amount:.2f}") 
    
    def withdraw(self,amount):
        self.account_balance -= amount
        if self.account_balance <= 0:
            print("Insufficient funds for this withdrawal.")
            return False
        else:
            return True
    
    def display_balance(self):
        print(f"current balance:${self.account_balance:.2f} ")
    
account = BankAccount(100)

print (account.account_balance)
    
    


