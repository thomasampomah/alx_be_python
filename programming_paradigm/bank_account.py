class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self,amount):
        self.account_balance += amount
        print(f"Deposited ${amount:.2f}")
    
    def withdraw(self,amount):
        self.account_balance -= amount
        if self.account_balance > 0:
            return True
        else:
            print("Insufficient funds")
            return False
    
    def display_balance(self):
        print(f"Current Balance:${self.account_balance:.2f}")
    

    
    


