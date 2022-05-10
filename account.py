#!/usr/bin/env python3 

# create a class called Account that has a username and a balance 
# class Account also has functions deposit, withdraw, transfer, and get_balance

from unicodedata import name


class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = float(balance)
    
    # deposit function that adds to the balance 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # withdraw function that subtracts from the balance
    def withdraw(self, amount):
        if self.balance - amount < 0:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    # transfer function that transfers from one account to another
    def transfer(self, other, amount_out):
        if self.balance - amount_out < 0:
            return "Insufficient funds"
        else:
            self.balance -= amount_out
            other.balance += amount_out
            return self.balance, other.balance

    # get_balance function that returns the balance of each account
    def get_balance(self):
        name = self.username
        balance = self.balance
        print(f"Hi {name} your account balance is {balance}")

# main function that creates three accounts and calls the class Account functions
def main():
    # create three accounts with account balances of 0 for each account 

    wanjiru = Account("Wanjiru", 0)
    juma = Account("Juma", 0)
    linda = Account("Linda", 0)

    # outline the transcation flow for each account

    wanjiru.deposit(152.00)
    wanjiru.transfer(linda, 218.25)
    linda.deposit(154.00)
    wanjiru.transfer(juma, 97.50)
    linda.deposit(156.00)
    wanjiru.transfer(linda,246.75)
    juma.deposit(1557.17)
    linda.withdraw(20.00)
    wanjiru.deposit(158.00)
    wanjiru.withdraw(159.00)
    linda.deposit(160.00)
    linda.deposit(162.00)
    juma.transfer(linda, 2000.00)
    wanjiru.deposit(164.00)
    wanjiru.withdraw(165.00)
    juma.deposit(1757.92)
    wanjiru.withdraw(166.00)
    linda.withdraw(167.00)
    linda.deposit(169.00)
    wanjiru.transfer(juma, 300.00)
    wanjiru.deposit(171.00)
    linda.deposit(174.00)
    linda.transfer(juma, 2000.00)
    juma.deposit(1757.92)
    wanjiru.withdraw(175.00)
    linda.withdraw(176.00)
    wanjiru.deposit(178.00)
    wanjiru.transfer(linda, 500.00)
    linda.deposit(180.00)
    wanjiru.withdraw(181.00)
    wanjiru.deposit(182.00)
    juma.transfer(linda, 500.00)
    wanjiru.withdraw(184.00)
    wanjiru.transfer(juma,600.00)
    wanjiru.deposit(188.00)

    # print the balance of each account
    wanjiru.get_balance()
    juma.get_balance()
    linda.get_balance()

    # The total balance of each account should be:
    # Wanjiru: 231.5
    # Juma: 4670.51 
    # Linda: 1292.0


    # print the total balance of all accounts
    #print(f"The total balance of all accounts is {wanjiru.balance + juma.balance + linda.balance}")

main()


