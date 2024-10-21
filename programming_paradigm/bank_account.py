class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            return(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")
        


    def withdraw(self,amount):
        self.account_balance -= amount
        if self.account_balance > amount:
            return True
        else:
            print("Insufficient funds.")
            
    
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
    

    
    


