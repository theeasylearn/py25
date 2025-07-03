# create a class for bank
# deposite : min 2000
# withdraw
# details
# hitrory

from datetime import datetime

class bank:
    bank_name = 'SBI'
    
    def __init__(self,name,account_id,ifsc,balance):
        self.name = name
        self.account_id = account_id
        self.ifsc = ifsc
        self.balance = balance
        self.transaction = []
        

    def deposite(self,amount):
        if amount<2000:
            print("min deposite : 2000")
            
        else:
            self.balance =  self.balance + amount
            print("deposite successfully completed :",amount)
            dt = datetime.now()
            self.transaction.append(('deposite',amount,dt.strftime('%d-%m-%Y'),dt.strftime('%S:%M:%H')))
            
            
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficiante amount")
            
        else:
            self.balance = self.balance - amount
            print("withdraw successfully completed :",amount)
            dt = datetime.now()
            self.transaction.append(('withdraw',amount,dt.strftime('%d-%m-%Y'),dt.strftime('%S:%M:%H')))
            
    
    def history(self):
        # print(self.transaction)
        print("operation    amount    date      time")
        print("--------------------------------------------------")
        for i in self.transaction:
            print(f"{i[0]}   {i[1]}   {i[2]}    {i[3]}")
                
    
    def details(self):
        print("name : ",self.name)
        print("account no : ",self.account_id)
        print("ifsc : ",self.ifsc)
        print("balance : ",self.balance)
        

print(bank.bank_name)
       
name = input("enter your name : ")
id = int(input("enter your account id : "))
ifsc = input("enter your ifsc : ")
balance = int(input("enter your balance : "))
if(name=='devarsh' and id==1234 and ifsc=='sbi001'):
    ac1 = bank(name,id,ifsc,balance)
    print("login success....")
    
    while(1):
        print("\n------------- choise ----------------\n")
        print("1 for withdraw\n2 for deposite\n3 for get details\n4 for history\n0 for exit")
        choise = int(input("enter your choise : "))
        
        if choise == 1:
            amount = int(input("enter amount to withdraw : "))
            ac1.withdraw(amount)
            
        elif choise ==2:
            amount = int(input("enter amount to deposite : "))
            ac1.deposite(amount)
            
        elif choise==3:
            ac1.details()
            
        elif choise==4:
            ac1.history()
            
        elif choise==0:
            print("logout")
            break
            
        else:
            print("invalid choise!!!")
        
        
else:
    print("invalid username & password!!!")