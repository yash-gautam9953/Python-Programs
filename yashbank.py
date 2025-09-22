class yash:
    def __init__(self, bal):
        self.balance = bal

    def debit(self, a):
        res2 = self.balance - a
        print("After Debit, available balance is =", res2)
        self.balance = res2

    def credit(self, b):
        res = self.balance + b
        print("After Credit, available balance is =", res)
        self.balance = res

    def check(self, c):
        self.accno = c
        if self.accno == 9953047014:
            print("Your balance is =", self.balance)
        else:
            print("Acc no. wrong! TRY AGAIN")


y1 = yash(100000)

count = 0
while count == 0:
   
    name = input("WELCOME AT YASH BANK what's your name :")
    print(name)
    option =int(input("Enter 1, 2, 3, or 4 for Debit, Credit, Check Balance, or Exit respectively = "))
    print(option)
    if option == 1:
        a = int(input("Enter Debit Amount = "))
        y1.debit(a)
    elif option == 2:
        b = int(input("Enter Credit Amount = "))
        y1.credit(b)
    elif option == 3:
        c = int(input("For Check Account Balance (Enter Acc.no.) = "))
        y1.check(c)
    elif option == 4:
        count = 1
    else:
        print("Invalid option! Please try again.")
