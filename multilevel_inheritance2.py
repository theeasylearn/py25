# convert seconds to minitues , hours ,day

class second:
    def __init__(self,sec):
        self.sec = sec
        
    def getsecond(self):
        return self.sec
    
    
class minute(second):
    def __init__(self, sec):
        super().__init__(sec)
        
    def getmin(self):
        return self.sec / 60
    
class hours(minute):
    def __init__(self, sec):
        super().__init__(sec)
        
    def gethours(self):
        return super().getmin() / 60
    
class days(hours):
    def __init__(self, sec):
        super().__init__(sec)
        
    def getdays(self):
        return super().gethours() / 24
    
obj = days(3600)
print(obj.getsecond())    
print(obj.getmin())    
print(obj.gethours())    
# print(obj.getdays()) 
day = obj.getdays()   
print(round(day,2))