class bankaccount:
    def __init__(self,acc__no,name,acc__type,balance):
        self.acc__no=acc__no
        self.name=name
        self.acc__type=acc__type
        self.balace=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print("amount deposited successfully.")
        else:
            print("invalid amount.")
    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount.")
        elif amount<=self.balance:
            self.balance-=amount
            print("amount withdraw successfully.")
        else:
            print("insufficient balance.")
    def display(self):
        print("\naccount number;",self.acc__no)
        print("Name:",self.name)
        print("account type:",self.acc_type)
        print("balance;",self.balance)
        acc=normalize_encoding
while true:
 print("\n---BANK MENU---")
print("1.account creation")
print("2.deposit")
print("3.withraw")
print("4.display")
print("5.exit")
choice=int(input("enter your choice:"))
if choice==1:
    acc__no=input("enter account number:")
    name=input("enter account name:")
    acc__type=input("enter account type:")
    balance=float(input("enter initial balance:"))
    if balance<0:
            print("initial balance cannot be negative.")
    else:
        acc=bankaccount(acc__no,name,acc__type,balance)
        print("account created successfully.")
elif choice==2:
        if acc is none:
            print("please created an account first.")
        else:
            amount=float(input("enter amount to deposit:"))
            acc.deposit(amount)
elif choice==3:
        if acc is none:
            print("please create an account first.")
        else:
            acc.display()
elif choice==4:
    if acc is none:
          print("please create an account first.")
    else:
         acc.display()
elif choice==5:
    print("thank you for using the bank.")
    break
else:
        print("invalid choice.please try again.")

