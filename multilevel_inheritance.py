# write a program that convert bytes to kb,mb,gb

class bytes:
    def __init__(self,byte):
        self.byte = byte
        
    def getbytes(self):
        return self.byte
    
class kb(bytes):
    def __init__(self, byte):
        super().__init__(byte)
        
    def getkb(self):
        ans = self.byte / 1000
        return ans
        
class mb(kb):
    def __init__(self, byte):
        super().__init__(byte)
        
    def getmb(self):
        ans = super().getkb() / 1000
        return ans
    
class gb(mb):
    def __init__(self, byte):
        super().__init__(byte) 
        
    def getgb(self):
        ans = super().getmb() / 1000
        return ans
    
o1 = gb(5000)
print("bytes : ",o1.getbytes())
print("kb : ",o1.getkb())
print("mb : ",o1.getmb())
print("gb : ",o1.getgb())

