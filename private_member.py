student_list = []

class student:
    def __init__(self,id,name,div,marks):
        self.id= id
        self.name= name
        self.div= div
        self.__marks= marks
        
    def add_student(self):
        student_list.append((self.id,self.name,self.div,self.__marks))
        print("student added...")
        
    def remove_student(self,id):
        for i in student_list:
            if(id == i[0]):
                position = student_list.index(i)
                student_list.pop(position)
        
    def setmarks(self,id,marks):
        for i in student_list:
            if(id == i[0]):
                position = student_list.index(i)
                
                i = list(i)
                # print(i)
                i[3] = marks
                i=tuple(i)
                # print(i)
                
                
                student_list.pop(position)
                student_list.insert(position,i)
                
    def getmarks(self,id):
        for i in student_list:
            if(id == i[0]):
                position = student_list.index(i)
                print("marks : ",student_list[position][3])
        
    def see_details(self,id=0,marks=0,div=0):
        if id==0 and marks==0 and div==0:
            for i in student_list:
                print(i)
                
        elif id!=0 and marks==0 and div==0:
            for i in student_list:
                if(id==i[0]):
                    print(i)
                    
        elif id==0 and marks==0 and div!=0:
            for i in student_list:
                if(div==i[2]):
                    print(i)

        elif id==0 and marks!=0 and div==0:
            for i in student_list:
                if(marks<=i[3]):
                    print(i)
        
s1 = student(101,"devarsh",12,80)
s2 = student(102,"devarsh",12,80)
s3 = student(103,"devarsh",12,80)
s1.add_student()
s2.add_student()
s3.add_student()
s1.see_details()

# s2.remove_student(101)

# s1.see_details()

# s2.remove_student(103)
# s1.see_details()

s1.setmarks(101,20)
s1.setmarks(102,40)
s1.see_details()
# s1.getmarks(102)

print("---------- id -----------")
s1.see_details(id=103)


print("---------- div -----------")
s1.see_details(div=12)


print("---------- marks -----------")
s1.see_details(marks=40)