class BankAccount:
    def __init__(self, name, balance = 0):
        self.client_name = name
        self.balance = balance
        self.interest = 0.01

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

    def interest(self):
        return f'Your interest rate is {self.interest()}%'

    def __str__(self):
        return self.balance
        return self.interest



name = input('What is your name?'.lower())
account = BankAccount(name)
menu_option = int(input(
    f"How can I help you?\nWould you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl"
    f"\n\t4) Check my interest rate\n\t5) View my transactions\n>>>"))
while True:
    if menu_option == 1:
        print(f'Your balance is ${account.balance}\n')
        menu_option = int(input(
            f"Would you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl"
            f"\n\t4) Check my interest rate\n\t5) View my transactions\n>>>"))
    elif menu_option == 2:
        amount = int(input("How much would you like to deposit?\n"))
        account.deposit(amount)
        menu_option = int(input(
            f"Would you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl"
            f"\n\t4) Check my interest rate\n\t5) View my transactions\n>>>"))
    elif menu_option == 3:
        amount = int(input("How much would you like to withdrawl?\n"))
        account.withdraw(amount)
        menu_option = int(input(
            f"Would you like to:\n\t1) Check my Balance\n\t2) Make a Deposit\n\t3) Make a Withdrawl"
            f"\n\t4) Check my interest rate\n\t5) View my transactions\n>>>"))
