purchase_cost = int(input("Enter purchase price"))
sales_price = int(input("Enter sale price"))
difference = sales_price - purchase_cost

if difference>0: # == != < > <= >=
    print("profit = " + str(difference))

if difference<0:
    print("loss = " + str(difference))


if difference==0:
    print("no profit no loss")
    
print(type(difference))