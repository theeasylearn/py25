class saving_account:
    def __init__(self,interest):
        self.interest = interest
        
    def getinterest(self):
        print("interest added: ",self.interest,"%")
        

class current_account:
    def __init__(self,limit):
        self.limit = limit
        
    def getlimit(self):
        print("your limit is creadited : ",self.limit)
        
        
class bank(saving_account,current_account):
    def __init__(self,interest,limit):
        saving_account.__init__(self,interest)
        current_account.__init__(self,limit)
        
    def getdetail(self):
        print("bank details here")

b1 = bank(20,2000)
b1.getinterest()
b1.getlimit()
b1.getdetail()
    