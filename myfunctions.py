import mysql.connector as con
from datetime import datetime
import qrcode as qr
import pdf_maker as pm

db = con.connect(user='root',password='',database='py25',host='localhost')
mycursor = db.cursor()

def add_product(name,price,quntity,details):
    sql = "insert into products values(%s,%s,%s,%s,%s)"
    values = ["",name,price,quntity,details]
    
    mycursor.execute(sql,values)
    print("product added...")
    
def remove_product(id):
    sql = "delete from products where id=%s"
    values = [id]
    
    mycursor.execute(sql,values)
    print("product deleted...")

def update_product(id,name,price,quntity,details):
    sql = "update products set name=%s,price=%s,quntity=%s,details=%s where id=%s"
    values = [name,price,quntity,details,id]
    
    mycursor.execute(sql,values)
    print("product updated...")
    
    
def view_products():
    sql = "select * from products"
    mycursor.execute(sql)
    
    data = mycursor.fetchall()
    
    title = ["id","name","price","quntity","details"]
    print(f"{title[0]:2} {title[1]:15}      {title[2]:10}{title[3]:5}   {title[4]:20}")
    print("----------------------------------------------------------------------------")
    for i in data:
        print(f"{i[0]:2} {i[1]:15}{i[2]:10}{i[3]:10}        {i[4]:20}")
    
    # print(data)
    
def view_customers():
    sql = "select * from customers"
    mycursor.execute(sql)
    
    data = mycursor.fetchall()
    
    title = ["id","name","age","address","email"]
    print(f"{title[0]:2} {title[1]:15}      {title[2]:10}{title[3]:5}   {title[4]:20}")
    print("----------------------------------------------------------------------------")
    for i in data:
        print(f"{i[0]:2} {i[1]:15}{i[2]:10}{i[3]:10}        {i[4]:20}")
    
    # print(data)
   
def view_payments():
    sql = "select * from payments"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    title = ["id","customer id","date","time","product id","quntity","amount"]
    print(f"{title[0]:2} {title[1]:5} {title[2]:10}{title[3]:15}   {title[4]:2}   {title[5]:5} {title[6]:10}")
    print("----------------------------------------------------------------------------")
    for i in data:
        print(f"{i[0]:2} {i[1]:5}        {str(i[2]):10}{str(i[3]):15}{i[4]:2}    {i[5]:5} {i[6]:10}")
        
        
 
def buy_product(id,customerid,quntity):
    sql4 = "select quntity from products where id=%s"
    values4 = [id]
    mycursor.execute(sql4,values4)
    qun = mycursor.fetchall()
    qun = qun[0][0]
    
    if qun<quntity:
        print(f"you can buy max. {qun}")
        
    else:
        choise = int(input("enter 1 for payment & 0 for cancel : "))
        if choise == 1:
            print("payment complete")
            dt = datetime.now()
            d = dt.strftime('%Y-%m-%d')
            t = dt.strftime('%S:%M:%H')
            amount = 0
            sql1 = "select price from products where id=%s"
            values1 = [id]
            
            mycursor.execute(sql1,values1)
            price = mycursor.fetchall()
            amount = price[0][0] * quntity
            
            sql2 = "insert into payments values(%s,%s,%s,%s,%s,%s,%s)"
            values2 = ["",customerid,d,t,id,quntity,amount]
            mycursor.execute(sql2,values2)

            new = qun - quntity
            sql3 = "update products set quntity=%s where id=%s"
            values3 = [new,id]
            
            mycursor.execute(sql3,values3)
            
            
            sql = "select id from payments where date = %s and time=%s"
            values = [d,t]
            mycursor.execute(sql,values)
            
            data = mycursor.fetchall()
            payment_id = data[0][0]

            sql = "select * from payments where id=%s"
            values = [payment_id]
            mycursor.execute(sql,values)
            
            payment_data = mycursor.fetchall()
            
            data = qr.make(payment_data)
            name = str(customerid)+".png"
            data.save(name)
            print(f"your bill qr code is : {name}")
            
            # ---------------------------------------------------
            # Set up the base font for the PDF
            name = str(customerid)+".pdf"
            basefont = "ArialMT"
            file = pm.NewPDF(filepath=name, _basefont=basefont)

            # Define the starting position on the page
            start_x = 20
            start_y = 700
            line_height = 14  # Space between lines in the table
            column_widths = [50, 80, 120, 60, 50, 60, 60]  # Column widths for each column

            # Table Header
            headers = ["Payment ID", "Customer ID", "Date", "Time", "Product ID", "Price", "Quantity", "Amount"]
            for i, header in enumerate(headers):
                file.text(page=0, x=start_x + sum(column_widths[:i]), y=start_y, 
                        line_space=1, size=12, base=0, rotate=0, 
                        h_align="middle", v_align="bottom", text=header)

            # Add rows of data
            current_y = start_y - line_height
            for row in payment_data:
                for i, cell in enumerate(row):
                    file.text(page=0, x=start_x + sum(column_widths[:i]), y=current_y, 
                            line_space=1, size=12, base=0, rotate=0, 
                            h_align="middle", v_align="bottom", text=str(cell))
                current_y -= line_height

            # Save the PDF
            file.save()
            print(f"pdf bill : {name}")
    
    
db.commit()