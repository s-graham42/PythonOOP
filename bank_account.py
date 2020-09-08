class BankAccount:
    def __init__(self, user_name = "unk", start_bal = 0, start_int_rate = 0.01):
        self.user = user_name
        self.balance = start_bal
        self.interest = start_int_rate
    
    def deposit(self, amount):
        print(f"{self.user} deposits ${amount}.")
        self.balance += amount
        return self

    def withdraw(self, amount):
        print(f"{self.user} withdraws ${amount}.")
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.user}'s Balance: {self.balance}.")
        print("-"*20)
        return self

    def yield_interest(self):
        if self.balance > 0:
            int_yield = self.balance * self.interest
            self.balance += int_yield
            print(f"${int_yield} interest added to {self.user}'s account.")
        return self

def print_all(arr):
    print("-"*50)
    for i in arr:
        print(f"{i.user}'s balance: {i.balance} (interest rate: {i.interest}) ")
    print("-"*50)

anna = BankAccount("Anna", 150, 0.0096)
mike = BankAccount("Mike")
guido = BankAccount("Guido", 275, 0.012)
monty = BankAccount("Monty", 0, 0.005)
unknown = BankAccount()

users = [anna, mike, guido, monty, unknown]

print_all(users)
anna.deposit(150).deposit(68).deposit(50).withdraw(275).yield_interest().display_account_info()
mike.deposit(150).deposit(300).withdraw(25).withdraw(50).withdraw(175).withdraw(28).yield_interest().display_account_info()
print_all(users)