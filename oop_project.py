from bank_account import *

Dave = BankAccount(1000, "Dave")
Yifang = BankAccount(5000, "Yifang")

Dave.getBalance()
Yifang.getBalance()

Dave.deposit(500)

Dave.withdraw(1000)


Dave.transfer(200, Yifang)

Tom = InterestRewardsAcct(2000, "Tom")

Tom.deposit(1000)

Jerry = SavingsAcct(300, "Jerry")
Jerry.withdraw(250)