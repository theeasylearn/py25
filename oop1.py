class person:
    def walk(self):
        print("i can walk....")
        
    def talk(self):
        print("i can talk....")
        
    def detalis(self,name,age):
        print(name)
        print(age)
        
        
p1 = person()
p1.walk()
p1.talk()
p1.detalis("devarsh",17)

p2 = person()
p2.detalis("parth",23)