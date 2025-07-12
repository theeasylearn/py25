import mysql.connector as con
db = con.connect(user="root",password="",database="py25",host="localhost")

print("connection established....")

mycursor = db.cursor()

sql = "select * from student"

# print(mycursor.fetchall())
data = mycursor.fetchall()
for i in data:
    print(i)

sql = "select name from student"
mycursor.execute(sql)

# print(mycursor.fetchone())
data = mycursor.fetchall()
print(data)
