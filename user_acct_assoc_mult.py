# ASSOCIATING BETWEEN CLASSES

                        # DEFINE USER CLASS
class User:
    def __init__(self, username = 'unk', email_address = 'unk', num_accts = 1):
        self.user = username
        self.email = email_address
        self.accounts = {}          # create a blank dictionary
        for i in range(num_accts):  # create the number of accounts specified by num_accts
            self.accounts["Account" + str(i+1)] = BankAccount(0, 0.01)
                                    # creates dict accounts =  {"Account1" : BankAccount(balance, interest), etc. }

    def make_deposit(self, amount, acctNum = 'Account1'):
        print(f"{self.user} deposits ${amount} into {acctNum}")
        self.accounts[acctNum].balance += amount
        return self

    def make_withdrawal(self, amount, acctNum = 'Account1'):
        print(f"{self.user} withdraws ${amount} out of {acctNum}")
        self.accounts[acctNum].balance -= amount
        return self

    def display_all_balances(self):
        print("-"*50)
        print(f"{self.user}:")
        for x, y in self.accounts.items():  # iterates through dict returning Key as x and value as y
            print(f"\t{x} Balance:  ${y.balance}")
        print("-"*50)
        return self

    def display_acct_balance(self, acctNum = 'Account1'):
        print(f"{self.user}'s balance in {acctNum}:  ${self.accounts[acctNum].balance}\n", "-"*50)

    def transfer_money(self, other_user, amount = 0, acctOut = 'Account1', acctIn = 'Account1'):
        print(f"{self.user} transfers ${amount} from {acctOut}\nto: {other_user.user}, into {acctIn}.")
        self.accounts[acctOut].balance -= amount
        other_user.accounts[acctIn].balance += amount
        return self

    def yield_all_interest(self):
        for i in self.accounts:
            if self.accounts[i].balance > 0:
                int_yield = self.accounts[i].balance * self.accounts[i].interest
                self.accounts[i].balance += int_yield
                print(f"${int_yield} interest added to {self.user}'s {i}.")
        return self


                    #  Define Bank Account Class
class BankAccount:
    def __init__(self, start_bal = 0, start_int_rate = 0.01):
        self.balance = start_bal
        self.interest = start_int_rate


mike = User("Michael", "mike@here.com", 3)
anna = User("Anna", "annie@here.com", 2)
guido = User("Guido Van Rossum", "guido@python.com", 1)
monty = User("Monty Python", "monty@python.com", 4)

mike.display_all_balances()
mike.display_acct_balance('Account2')

def print_everybody():
    print("*"*50)
    userArray = [mike, anna, guido, monty]
    for i in userArray:
        i.display_all_balances()
    print("*"*50)

print_everybody()

mike.make_deposit(200, 'Account1').make_deposit(100, 'Account2').make_deposit(100, 'Account3').make_withdrawal(75, 'Account1').yield_all_interest().display_all_balances()

anna.make_deposit(100).make_deposit(500, 'Account2').make_withdrawal(50, 'Account2').make_withdrawal(175).yield_all_interest().display_all_balances()

guido.make_deposit(100, 'Account1').make_withdrawal(7.50).make_withdrawal(20).make_withdrawal(54).yield_all_interest().display_all_balances()

mike.transfer_money(monty, 100).yield_all_interest().display_all_balances()

monty.yield_all_interest().display_all_balances()

print_everybody()