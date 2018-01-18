#  Example 1
#
# class Drink:
#     def __init__(self, n, l):
#         self.name = n
#         self.liquid = l
#
#     def product_info(self):
#         print(self.name)
#         print(self.liquid)
#
#
# monster = Drink('Monster Energy', 'Energy Junk')
# pepsi = Drink('Pepsi', 'Soda')
#
# monster.product_info()
# pepsi.product_info()


# Example 2



class BankAccount:
    def __init__(self, name, account_number):
        self.client_name = name
        self.balance = 0
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount
        print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))
        else:
            print('Sorry {}. You do not have enough funds. Your balance is ${}.'.format(self.client_name, self.balance))


class SecondChanceBankAccount(BankAccount):
    def __init__(self, name, account_number):
        super().__init__(name, account_number)

    def withdraw(self, amount):
        if self.balance - amount - 100 >= 0:
            self.balance -= amount
            print('Thanks {}! Your balance is now ${}.'.format(self.client_name, self.balance))
        else:
            print('Sorry {}. You do not have enough funds. Your balance is ${}. '
                  'You must keep at least $100 in your account.'.format(self.client_name, self.balance))


chris = SecondChanceBankAccount('Chris', '000001')
katie = BankAccount('Katie', '000002')
chris.deposit(101)
chris.withdraw(10)
katie.deposit(250)
katie.withdraw(200)
print(BankAccount(katie, '000002'))