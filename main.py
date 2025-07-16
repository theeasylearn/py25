from myfunctions import *

while(True):
        
    choise = int(input("1 for seller view\n2 for customer view\n0 for exit : "))
    if choise==1:
        while(True):
            print("welcome as seller")  
            print("1 for add product\n2 for remove product\n3 for update product\n4 for view product\n5 for payments\n6 for view customer\n0 for exit")
            operation = int(input("enter your operation : "))
            
            if operation ==1:
                name = input("enter product name : ")
                price = int(input("enter product price : "))
                quntity = int(input("enter product quntity : "))
                details = input("enter product details : ")
                
                add_product(name,price,quntity,details)
                
            elif operation ==2:
                id = int(input("enter product id to remove : "))
                remove_product(id)
                
            elif operation ==3:
                id = int(input("enter product id to update : "))
                name = input("enter product name : ")
                price = int(input("enter product price : "))
                quntity = int(input("enter product quntity : "))
                details = input("enter product details : ")
                
                update_product(id,name,price,quntity,details) 
                
                
            elif operation ==4:
                view_products()
                
            elif operation==5:
                view_payments()
                
            elif operation==6:
                view_customers()
                
            elif operation==0:
                break
                
            else:
                print("invalid operation!!!")
            
        
    elif choise==2:
        print("welcome as customer")
        while(True):
            choise = int(input("1 for login\n2 for register\n0 for exit : "))
            if choise==1:
                cid = int(input("enter your customer id : "))
                sql = "select id from customers"
                mycursor.execute(sql)
                data = mycursor.fetchall()
                for i in data:
                    if i[0] == cid:
                        print("login successfull")
                        print("\nour products : ")
                        view_products()
                        
                        pid = int(input("enter produc id to buy : "))
                        quntity = int(input("enter quntity to buy : "))
                        buy_product(pid,cid,quntity)
            
            elif choise==2:
                name = input("enter customer name : ")
                age = int(input("enter customer age : "))
                address = (input("enter customer address : "))
                email = input("enter customer email : ")
                sql = "insert into customers values(%s,%s,%s,%s,%s) "
                values = ["",name,age,address,email]
                mycursor.execute(sql,values)
                print("register successfull... ")
                
                sql = "select id from customers where name=%s and age=%s and address=%s and email=%s"
                values = [name,age,address,email]
                mycursor.execute(sql,values)
                data = mycursor.fetchall()
                data = data[0][0]
                print(f"your customer id : {data}")

            elif choise==0:
                break
            
            else:
                print("invalid choise!!!")

    elif choise==0:
        break    

    else:
        print("invalid choise!!!")