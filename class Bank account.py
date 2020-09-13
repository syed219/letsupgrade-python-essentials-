# class Bank_Account
class Bank_Account():
    def __init__(self,owner):
         self.balance = 0
         self.owner=owner
    print("Hello Welcome to deposite and withdrawal machine")
 # function to deposite amount
    def deposit(self):
        amount=float(input("enter amount to be deposited:"))
        self.balance+=amount
        print("Amount deposited:",amount)
    # function to withdraw the amount
    def withdraw(self):
        amount = float(input("enter amount to be withdrawn:"))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdrew:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Net available balance= ",self.balance)

s= Bank_Account("Aishu")
print(s.owner)
s.deposit()
s.withdraw()
s.display()



