class Accounts:
    def __init__(self,account_number,account_balance):
        self.account_number=account_number
        self.account_balance=account_balance


    def balance_check(self):
        print(f'your balance is  {self.account_balance}')

    def withdraw_money(self,amount):
        if self.account_balance > amount:
            print(f"you with draw {amount}")
            self.account_balance=self.account_balance-amount
            print(f"your available balance is {self.account_balance}")
        else:
            print("your account has a limited amount of money sorry")
            print(f"your available balance is {self.account_balance}")


anu=Accounts("x124",2000)
viz=Accounts("x4ds",2000)


anu.withdraw_money(10000)