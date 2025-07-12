import mysql.connector as con
db = con.connect(user="root",password="",database="py25",host="localhost")

print("connection established....")

mycursor = db.cursor()

id = int(input("enter id to change : "))
# name = input("enter your name : ")
# age = int(input("enter your age : "))
# email = input("enter your email : ")
# mobile = input("enter your mobile : ")

# sql = "update student set name=%s,age=%s,email=%s,mobile=%s where id=%s"
# values = [name,age,email,mobile,id]


sql = "delete from student where id=%s"
values = [id]
mycursor.execute(sql,values)
# print("record updated.....")
db.commit()