import math

class Register(object):
    def __init__(self, saldo=0.0):
        self.amount=saldo

    def deposit(self, amount):
        self.amount+=amount
        
    def withdraw(self, amount):
        self.amount-=amount

