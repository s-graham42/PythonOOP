class User:
    def __init__(self, username, email_address):
        self.user = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        print(f"{self.user} deposits ${amount}")
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        print(f"{self.user} withdraws ${amount}")
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.user}'s balance: ${self.account_balance}\n", "-"*50)
        return self

    def transfer_money(self, other_user, amount):
        print(f"{self.user} transfers ${amount} to {other_user.user}")
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

mike = User("Michael", "mike@here.com")
anna = User("Anna", "annie@here.com")
guido = User("Guido Van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")

def print_everybody():
    userArray = [mike, anna, guido, monty]
    for i in userArray:
        print(f"{i.user}: ${i.account_balance}")
    print("-"*50)

print_everybody()

mike.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(75).display_user_balance()

anna.make_deposit(100).make_deposit(500).make_withdrawal(50).make_withdrawal(175).display_user_balance()

guido.make_deposit(100).make_withdrawal(7.50).make_withdrawal(20).make_withdrawal(54).display_user_balance()

mike.transfer_money(guido, 100).display_user_balance()

guido.display_user_balance()

print_everybody()