# ASSOCIATING BETWEEN CLASSES

                        # DEFINE USER CLASS
class User:
    def __init__(self, username = 'unk', email_address = 'unk'):
        self.user = username
        self.email = email_address
        self.account = BankAccount(0, 0.01)

    def make_deposit(self, amount):
        print(f"{self.user} deposits ${amount}")
        self.account.balance += amount
        return self

    def make_withdrawal(self, amount):
        print(f"{self.user} withdraws ${amount}")
        self.account.balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.user}'s balance: ${self.account.balance}\n", "-"*50)

    def transfer_money(self, other_user, amount):
        print(f"{self.user} transfers ${amount} to {other_user.user}")
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

    def yield_interest(self):
        if self.account.balance > 0:
            int_yield = self.account.balance * self.account.interest
            self.account.balance += int_yield
            print(f"${int_yield} interest added to {self.user}'s account.")
        return self


                    #  Define Bank Account Class
class BankAccount:
    def __init__(self, start_bal = 0, start_int_rate = 0.01):
        self.balance = start_bal
        self.interest = start_int_rate


mike = User("Michael", "mike@here.com")
anna = User("Anna", "annie@here.com")
guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

def print_everybody():
    userArray = [mike, anna, guido, monty]
    for i in userArray:
        print(f"{i.user}: ${i.account.balance}")
    print("-"*50)

print_everybody()

mike.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(75).yield_interest().display_user_balance()

anna.make_deposit(100).make_deposit(500).make_withdrawal(50).make_withdrawal(175).yield_interest().display_user_balance()

guido.make_deposit(100).make_withdrawal(7.50).make_withdrawal(20).make_withdrawal(54).yield_interest().display_user_balance()

mike.transfer_money(guido, 100).yield_interest().display_user_balance()

guido.yield_interest().display_user_balance()

print_everybody()