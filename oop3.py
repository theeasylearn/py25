class student:
    def __init__(self,name,age,roll):
        # instance variable
        self.name = name
        self.age = age
        self.roll = roll
        self.marks = {}
        
    
    def getmarks(self):
        maths = int(input("enter maths marks : "))
        eng = int(input("enter eng marks : "))
        science = int(input("enter science marks : "))
        self.marks['maths'] = maths
        self.marks['eng'] = eng
        self.marks['science'] = science
    
    def details(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("roll no : ",self.roll)
        print("marks : ",self.marks)
        

s1 = student("devarsh",17,101)
s1.getmarks()
s1.details()