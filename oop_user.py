class User:
    def __init__(self, username, email_address):
        self.user = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        print(f"{self.user} deposits ${amount}")
        self.account_balance += amount

    def make_withdrawal(self, amount):
        print(f"{self.user} withdraws ${amount}")
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.user}'s balance: ${self.account_balance}\n", "-"*50)

    def transfer_money(self, other_user, amount):
        print(f"{self.user} transfers ${amount} to {other_user.user}")
        self.account_balance -= amount
        other_user.account_balance += amount

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

mike.make_deposit(100)
mike.make_deposit(100)
mike.make_deposit(100)
mike.make_withdrawal(75)
mike.display_user_balance()

anna.make_deposit(100)
anna.make_deposit(500)
anna.make_withdrawal(50)
anna.make_withdrawal(175)
anna.display_user_balance()

guido.make_deposit(100)
guido.make_withdrawal(7.50)
guido.make_withdrawal(20)
guido.make_withdrawal(54)
guido.display_user_balance()

mike.transfer_money(guido, 100)
mike.display_user_balance()
guido.display_user_balance()
print_everybody()