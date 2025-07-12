import mysql.connector as con
db = con.connect(user="root",password="",database="py25",host="localhost")

print("connection established....")

mycursor = db.cursor()

# insert into student values(...)
name = input("enter your name : ")
age = int(input("enter your age : "))
email = input("enter your email : ")
mobile = input("enter your mobile : ")

sql = "insert into student values(%s,%s,%s,%s,%s)"
values = ["",name,age,email,mobile]

mycursor.execute(sql,values)
print("record inserted...")
db.commit()