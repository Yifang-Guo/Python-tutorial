class BalanceException(Exception):
    pass



class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' created. \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f" Account '{self.name}' has balance of ${self.balance:.2f}.")

    def deposit(self, amount):
        self.balance += amount
        print(f"\n Account '{self.name}' deposited ${amount:.2f}.")

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account '{self.name}' only has balance of ${self.balance:.2f}."
            )
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted.❌\n{error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance += (amount * 1.05)
        print("\n Deposit completed.")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\n Withdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\n Withdraw interrupted: {error}")




