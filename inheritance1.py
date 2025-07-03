# parent base
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def walk(self):
        print("i can walk...")
        
    def talk(self):
        print("i can talk...")
        
    def details(self):
        print("name : ",self.name)
        print("age : ",self.age)
   
# child  derived     
class student(person):
    def __init__(self, name, age,roll,school):
        super().__init__(name, age)
        self.roll = roll
        self.school = school
    
    def read(self):
        print("i can read...")
        
    def write(self):
        print("i can write...")
        
    def student_details(self):
        super().details()
        print("roll no : ",self.roll)
        print("school : ",self.school)
        
        
# p1 = person()
# p1.walk()
# p1.talk()

s1 = student("devarsh",17,101,"kpes")
# s1.read()
# s1.write()
# s1.walk()
# s1.talk()
# s1.details()
s1.student_details()