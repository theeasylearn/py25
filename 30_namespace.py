amount = 2000 #amount is global variable as it is declared outside function
def AddMoney(): # Uncomment the following line to fix the code:
    global amount 
    amount = amount + 1 #it will access and change global amount variable
print (amount )
AddMoney()
print (amount )
