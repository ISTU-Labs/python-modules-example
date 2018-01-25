import register

class Accounts(object):
    def __init__(self, names, saldos):
        self.accounts={k:register.Register(s) for k,s in zip(names, saldos)}

    def deposit(self, name, amount):
        a=self.accounts
        a[name].deposit(amount)

    def __getitem__(self, name):
        return self.accounts[name].amount


def main():
    accs = Accounts(["50","70"], [0, 2000])
    accs.deposit("70", 100)
    print(accs["70"])


main()
