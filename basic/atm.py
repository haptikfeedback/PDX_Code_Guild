import math
#test
class BankAccount:
    def __init__(self, name, interest=0.01, balance=0):
        self.client_name = name
        self.interest = interest
        self.balance = balance
        self.transactions_list = []

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))
        return self.balance

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))
        else:
            print('Sorry {}. You do not have enough funds. Your balance is ${}.'.format(self.client_name, self.balance))

    def calc_interest(self, balance):
        interest = (self.balance * self.interest)
        print(f'The interest on ${self.balance} is ${interest} at a rate of {self.interest}%')

    def print_transactions(self):
        print(self.transactions_list)

    def __str__(self):
        return self.balance

def user_option():
    return f"Would you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl\n\t4) " \
           f"Check my interest rate\n\t5) View my transactions\n>>>"


name = input('What is your name?'.lower())
account = BankAccount(name)
menu_option = int(input(
    f"How can I help you?\nWould you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl"
    f"\n\t4) Check my interest rate\n\t5) View my transactions\n>>>"))
while True:
    if menu_option == 1:
        print(f'Your balance is ${account.balance}\n')
        menu_option = int(input(user_option()))
    elif menu_option == 2:
        amount = int(input("How much would you like to deposit?\n"))
        account.deposit(amount)
        account.transactions_list.append(f'Deposit: ${amount}')
        print(account.transactions_list)
        menu_option = int(input(user_option()))
    elif menu_option == 3:
        amount = int(input("How much would you like to withdrawl?\n"))
        account.withdraw(amount)
        account.transactions_list.append(f'Withdrawl: ${amount}')
        menu_option = int(input(user_option()))
    elif menu_option == 4:
        account.calc_interest(account.balance)
        menu_option = int(input(user_option()))
    elif menu_option == 5:
        account.print_transactions()
        menu_option = int(input(user_option()))