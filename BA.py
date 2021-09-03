class BankAccount:

    accounts=[]




    def __init__(self, int_rate, balance):

        self.int_rate=int_rate

        self.balance=balance

        BankAccount.accounts.append(self)


    def deposit(self, amount):

        self.balance+=amount

        return self


    def withdraw(self, amount):

            if(self.balance-amount)>=0:

                self.balance-=amount

            else:

                print("Insufficient Funds: Charging a $5 fee")

                self.balance-=5

            return self


    def display_account_info(self):

                print(f"Balance:{self.balance}")

                return self


    def yield_interest(self):

            if self.balance>0:

                self.balance+=(self.balance*self.int_rate)

            return self


#    @classmethod
    
#    def print_all_accounts(cls):
        
#        for account in cls.accounts:
            
#            account.display_account_info()






savings = BankAccount (.18,2500)

checking = BankAccount (.09,1250)

savings.deposit(25).deposit(45).deposit(15).withdraw(50).yield_interest().display_account_info()

checking.deposit(165).deposit(35).withdraw(23).withdraw(26).withdraw(75).withdraw(85).yield_interest().display_account_info()