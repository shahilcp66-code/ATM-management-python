# ATM 
# class atm:
#     def __init__(self,account_no,acc_holder,balance):
#         self.acc_no=account_no
#         self.acc_h=acc_holder
#         self.b=balance
#         self.deposits=0

#     def balance_enquiry(self):
#         print(f"{self.acc_no}\n{self.acc_h}\nbalance={self.b}")

#     def deposit(self):
#         deposit=int(input("enter deposit amount: "))
#         print("current balance=",self.b+deposit)
#         self.deposits=self.b+deposit

#     def withdraw(self):
#         self.b=self.deposits
#         withdraw=int(input("enter withdraw amount: "))
#         if withdraw>self.b:
#             print("insufiicient balance")
#         else:
#             print("current balanc=",self.b-withdraw)

# person1=atm(123456,"shenu",10000)
# person1.balance_enquiry()
# person1.deposit()
# person1.withdraw()

